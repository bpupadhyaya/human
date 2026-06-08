---
schema: human-scale-entry/v1
id: erythropoietin
name: Erythropoietin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "30.4 kDa glycoprotein from renal peritubular cells (~90%) regulated by HIF-2α. Drives erythropoiesis via JAK2/STAT5 on BFU-E/CFU-E progenitors. rHuEPO treats CKD anaemia; high Hb targets increase thrombotic risk."
aliases: ["EPO", "erythropoetin", "haematopoietic growth factor", "recombinant EPO", "rHuEPO"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/erythrocyte
    relation: modulates
    note: "EPO binds EPOR homodimer on BFU-E/CFU-E progenitors → JAK2/STAT5 → ↓apoptosis (↑Bcl-xL) + ↑haemoglobin synthesis; drives the entire erythropoiesis programme; ↑EPO → ↑RBC production within 3–7 days."
  - target: 01-human/05-tissue/bone-marrow
    relation: modulates
    note: "EPO acts on erythroid progenitor pool (BFU-E, CFU-E) in bone marrow, expanding erythroid islands around macrophage nurse cells that supply transferrin, ferritin, and survival signals to EPO-stimulated progenitors."
  - target: 01-human/06-organ/kidney
    relation: expresses
    note: "Peritubular interstitial fibroblast-like cells in renal cortex/outer medulla produce ~90% of EPO; HIF-2α is the primary transcription factor; loss of these cells in CKD is the primary cause of CKD-related anaemia."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "EPO raises RBC mass (↑O₂-carrying capacity) → ↑viscosity, ↑haematocrit; rHuEPO at Hb targets >12 g/dL increases thrombotic events (DVT, stroke, MI) via haemoconcentration and possible direct platelet activation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "CKD destroys renal peritubular EPO-producing cells → EPO deficiency → normochromic normocytic anemia; treated with ESAs (darbepoetin, epoetin) or HIF-PHI (roxadustat, daprodustat); KDIGO target Hb 10–11 g/dL to balance anemia symptoms and thrombotic risk."
---

# Erythropoietin

## Overview

Erythropoietin (EPO) is the principal hormone governing red blood cell production. A 30.4 kDa glycoprotein of 165 amino acids, it is released from the kidney in response to hypoxia and acts on erythroid progenitors in the bone marrow to sustain — and massively amplify — red blood cell output when oxygen delivery falls. Its discovery as a humoral factor by Carnot and Deflandre (1906), purification by Miyake and Goldwasser (1977), and cloning by Lin et al. (1985) enabled the development of recombinant human EPO (rHuEPO), which has transformed the management of anaemia in chronic kidney disease (CKD) and cancer [^stryer-biochemistry].

Normal serum EPO: 5–30 mU/mL. In severe anaemia this can rise more than 1,000-fold (>10,000 mU/mL). The speed and magnitude of the response — bone marrow reticulocyte output measurably rises within 3–5 days — make EPO one of the most sensitive and powerful homeostatic feedback loops in human physiology [^guyton-hall].

## Structure

EPO is a **single-chain glycoprotein** of 165 amino acids (after signal peptide cleavage) with four α-helices (A–D) arranged in a left-handed antiparallel bundle — the canonical class I cytokine fold. Key structural features:

| Feature | Detail |
|:---|:---|
| **Molecular weight** | 30.4 kDa (protein 18.4 kDa + carbohydrate ~12 kDa) |
| **N-glycosylation** | Asn24, Asn38, Asn83 — complex-type chains (~40% of MW) |
| **O-glycosylation** | Ser126 |
| **Disulfide bonds** | Cys7–Cys161 (critical for activity), Cys29–Cys33 |
| **Isoforms** | 7–14 sialic acid residues; more sialic acid → longer half-life |

The carbohydrate chains are **essential for in vivo bioactivity**: sialic acid residues prevent rapid hepatic clearance (asialoglycoprotein receptor); desialylated EPO is biologically active in vitro but cleared from circulation within minutes in vivo. Glycosylation also protects against aggregation and denaturation.

**EPOR (EPO receptor):** A preformed homodimer (single transmembrane domain, class I cytokine receptor). JAK2 is constitutively associated with the cytoplasmic Box1/Box2 motifs. EPO binding induces a conformational change that reorients the two JAK2 molecules for transphosphorylation.

**Engineered variants:**
- **Darbepoetin alfa** — two additional N-glycosylation sites (Asn30, Asn88) → 5 N-chains → half-life ~24 h (vs ~8 h for epoetin)
- **CERA (methoxy-PEG-epoetin beta)** — large PEG polymer attached to Lys45 or Lys52 → half-life ~130 h; once-monthly dosing

## Function

EPO exerts three main functional roles:

1. **Erythroid proliferation and survival** — primary function; maintains and expands the committed erythroid progenitor compartment
2. **Haemoglobin synthesis induction** — stimulates expression of ALAS2 (erythroid δ-aminolevulinic acid synthase, rate-limiting for haem synthesis) and transferrin receptor (↑iron uptake)
3. **Non-haematopoietic cytoprotection** — EPO receptors are expressed in brain, heart, and endothelium (as EPOR/βcR heterodimers); neuroprotection and cardioprotection have been described in ischaemia models, but clinical translation remains unproven and controversial [^stryer-biochemistry]

The net functional output: **↑circulating red blood cells → ↑oxygen-carrying capacity → closure of the hypoxia feedback loop** that originally triggered EPO secretion.

## Mechanism

### Oxygen Sensing and EPO Gene Regulation

The molecular switch linking tissue hypoxia to EPO transcription is the **HIF (hypoxia-inducible factor) pathway**:

1. **Normoxia:** Prolyl hydroxylase domain enzymes (PHD1/2/3, Fe²⁺- and 2-oxoglutarate-dependent dioxygenases) hydroxylate HIF-α at Pro402 and Pro564 → VHL E3 ubiquitin ligase binds → proteasomal degradation; HIF-α half-life < 5 min
2. **Hypoxia:** O₂ falls → PHD activity drops (requires O₂ as co-substrate) → HIF-2α accumulates → dimerises with ARNT (HIF-1β) → transactivates EPO gene via hypoxia-response element (HRE) in the 3'-flanking region at −14 kb
3. **HIF-2α is the primary driver** of renal EPO (HIF-1α predominates in most other organs); peritubular interstitial fibroblast-like cells express very high HIF-2α → unique EPO-producing capacity
4. PHD inhibitors (cobalt chloride, DMOG, and clinical drugs: roxadustat, daprodustat, molidustat) mimic hypoxia by blocking PHD → ↑EPO even in CKD patients who have lost peritubular cells (though these patients show attenuated EPO response even with PHD inhibitors)

### Receptor Signalling (JAK2/STAT5 Pathway)

EPO binding to the preformed EPOR homodimer:

1. Conformational change → JAK2 transphosphorylation (Tyr1007/Tyr1008)
2. Activated JAK2 phosphorylates EPOR cytoplasmic tyrosines (Tyr343, Tyr401, Tyr429, Tyr431, Tyr479) → docking sites for SH2-domain proteins
3. **STAT5a/b** (primary effector) → phospho-Tyr-STAT5 dimerises → nucleus → **↑Bcl-xL** (anti-apoptotic, most important → CFU-E survival), ↑Bcl-2; STAT5 also induces oncostatin M, PIM-1 kinase
4. **PI3K/Akt** (via IRS-2) → ↑GLUT1, ↑cell cycle progression
5. **MAPK/ERK1/2** (via Grb2-SOS-Ras) → cell proliferation
6. Negative regulation: **SOCS1/SOCS3** (STAT5-induced) bind and inhibit JAK2; SHP-1 phosphatase dephosphorylates EPOR Tyr479 → terminates signalling; EPOR is rapidly internalised and degraded

### Erythropoiesis Cascade

EPO acts primarily at the **CFU-E stage** (committed erythroid progenitors, highest EPOR density ~1,000 sites/cell) and, to a lesser degree, BFU-E:
- Without EPO → BFU-E/CFU-E undergo BIM-mediated apoptosis within 12–24 h
- EPO → STAT5 → ↑Bcl-xL → cell survives → proerythroblast → basophilic → polychromatophilic → orthochromatic erythroblast → reticulocyte (enucleated) → circulating RBC (120-day lifespan)
- EPO does **not** directly control the final reticulocyte → mature RBC maturation step (constitutive)
- Hypoxia → ↑EPO → reticulocytosis measurable in 3–5 days; full RBC mass effect in 2–3 weeks

## Connections

- `modulates` → **[erythrocyte](../../04-cellular/erythrocyte/README.md)** — EPO binds EPOR on BFU-E/CFU-E, activating JAK2/STAT5 → Bcl-xL → cell survival and haemoglobin synthesis, driving RBC production
- `modulates` → **[bone-marrow](../../05-tissue/bone-marrow/README.md)** — EPO expands the erythroid progenitor pool in marrow, stimulating erythroid islands around macrophage nurse cells
- `expresses` → **[kidney](../../06-organ/kidney/README.md)** — ~90% of EPO is produced by peritubular fibroblast-like cells in the renal cortex/outer medulla, regulated by HIF-2α; CKD destroys these cells, causing EPO-deficiency anaemia
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — EPO raises RBC mass and haematocrit; excessively high targets with rHuEPO increase thrombosis risk (CHOIR, TREAT trials)
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — CKD destroys renal peritubular EPO-producing cells → EPO deficiency → normochromic normocytic anemia; treated with ESAs (darbepoetin, epoetin) or HIF-PHI (roxadustat, daprodustat); KDIGO target Hb 10–11 g/dL to balance anemia symptoms and thrombotic risk.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **CKD anaemia** | Loss of peritubular EPO-producing cells → normochromic normocytic anaemia; surviving cells show attenuated HIF-2α response | Most common cause of EPO deficiency; treated with ESAs (epoetin, darbepoetin, CERA) or PHD inhibitors (roxadustat); KDIGO target Hb ~10–11 g/dL |
| **Pure red cell aplasia (PRCA)** | Anti-EPO neutralising antibodies (especially subcutaneous epoetin alfa with polysorbate-80 [Eprex formulation] → immune recognition) → complete erythroid aplasia | Reticulocyte count falls to near zero; diagnosed by anti-EPO Ab; switch to darbepoetin or IV formulation; some require immunosuppression |
| **Polycythaemia vera (PV)** | JAK2 V617F (exon 14, ~97%) or exon 12 mutation → constitutive JAK2/STAT5 activation → EPO-independent erythroid proliferation | ↓serum EPO (suppressed by ↑RBC mass); ↑haematocrit, ↑risk of thrombosis and transformation to myelofibrosis; treated with phlebotomy, hydroxyurea, ruxolitinib (JAK2 inhibitor) |
| **Secondary polycythaemia** | ↑EPO from: high altitude, COPD/hypoventilation, VHL mutation (loss of VHL → constitutive HIF → ↑EPO), EPO-secreting tumours (renal cell carcinoma, hepatocellular carcinoma, cerebellar haemangioblastoma) | ↑Hb/Hct with ↑or inappropriately normal EPO; differentiate from PV (which has ↓EPO) |
| **EPO doping** | Exogenous rHuEPO increases RBC mass → ↑VO₂max (3–5%) → endurance performance advantage | WADA prohibited; detected by isoelectric focusing (recombinant EPO bands differ from endogenous), Hb passport (Athlete Biological Passport) |

## See Also

- [^stryer-biochemistry] Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
- [^guyton-hall] Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
- Related entries: [erythrocyte](../../04-cellular/erythrocyte/README.md), [hemoglobin](../hemoglobin/README.md), [bone-marrow](../../05-tissue/bone-marrow/README.md), [kidney](../../06-organ/kidney/README.md)
