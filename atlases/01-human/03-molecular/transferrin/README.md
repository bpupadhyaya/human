---
schema: human-scale-entry/v1
id: transferrin
name: Transferrin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Transferrin (TF; 79 kDa; SIDERO domain) is the plasma iron-transport protein; binds Fe³⁺ with Kd ~10⁻²⁰ M at pH 7.4; TFR1/CD71-mediated endocytosis delivers iron to erythroid precursors; TSAT and ferritin together diagnose iron deficiency anemia vs iron overload."
aliases: ["transferrin", "TF", "serotransferrin", "siderophilin", "TSAT", "transferrin saturation", "iron-binding protein", "TFR1", "transferrin receptor"]
sources:
  - id: ganz-2013-systemic-iron-homeostasis
    type: peer-reviewed
    cite: "Ganz T, Nemeth E. Iron homeostasis in host defence and inflammation. Nat Rev Immunol. 2015;15(8):500-510."
    doi: "10.1038/nri3863"
    pmid: "26160612"
    url: "https://doi.org/10.1038/nri3863"
  - id: muckenthaler-2017-iron-balance
    type: peer-reviewed
    cite: "Muckenthaler MU, Rivella S, Hentze MW, Galy B. A red carpet for iron metabolism. Cell. 2017;168(3):344-361."
    doi: "10.1016/j.cell.2016.12.034"
    pmid: "28129536"
    url: "https://doi.org/10.1016/j.cell.2016.12.034"
cross_links:
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Transferrin delivers Fe³⁺ to erythroid precursors via TFR1; iron is inserted into protoporphyrin IX by ferrochelatase → haem; each haemoglobin tetramer requires 4 Fe²⁺ atoms; erythropoiesis demands ~80% of total body iron daily — the major functional iron compartment."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin degrades ferroportin → blocks duodenal iron absorption and macrophage recycling → lowers transferrin saturation; elevated TSAT → liver BMP6 + TFR2/HJV → hepcidin upregulation → restrains iron loading; hepcidin-transferrin axis is the core iron homeostasis sensor."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "β-thalassaemia major: massive ineffective erythropoiesis → ERFE suppresses hepcidin → unconstrained duodenal iron absorption → transferrin saturation 100% → non-transferrin-bound iron (NTBI) → tissue deposition (liver, heart, pituitary); chelation with deferasirox targets NTBI."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Chronic transfusion therapy in SCD (for stroke prevention, recurrent ACS) leads to transfusional iron overload; elevated TSAT + ferritin >1000 ng/mL → iron chelation required; deferasirox is preferred oral chelator in SCD; cardiac and hepatic MRI T2* monitors iron deposition."
---

# Transferrin

## Overview

**Transferrin (TF; gene *TF*, chromosome 3q22.1)** is the principal plasma iron-transport protein — a **79 kDa bilobed glycoprotein** (N-lobe + C-lobe, each containing one iron-binding site) responsible for carrying virtually all circulating iron in the form of diferric transferrin [^ganz-2013-systemic-iron-homeostasis]. The body cannot rapidly excrete iron, so the elaborate transferrin/receptor/hepcidin axis precisely controls iron absorption and distribution.

**Iron pharmacokinetics:**
- Total body iron in adults: ~3-5 g (women 3 g; men 4-5 g)
- Distribution: ~65-70% in haemoglobin; ~25% in storage (ferritin, haemosiderin); ~3-4% in myoglobin, enzymes; ~0.1% in plasma transferrin
- Daily turnover: ~20-25 mg Fe recycled from erythrophagocytosis (RBC → macrophage → ferritin → ferroportin → transferrin); ~1-2 mg absorbed from diet; ~1-2 mg lost in skin shedding, menstruation, GI tract

Transferrin is typically ~30% saturated with iron in healthy adults (transferrin saturation, TSAT = serum iron / TIBC × 100%); the remaining ~70% of sites are free to bind iron released from tissues and recycled from aging red cells.

## Structure

**Primary structure:** 679 amino acids (nascent); signal peptide cleavage → 698 aa mature protein. Two homologous lobes connected by a hinge:
- **N-lobe** (residues 1-336): binds Fe³⁺ at a site formed by Asp63, Tyr95, Tyr188, His249, and Arg124 (with synergistic carbonate anion as bidentate ligand)
- **C-lobe** (residues 337-679): similar coordination chemistry; slightly higher iron affinity; preferred loading site in alkaline pH

**Iron binding affinity:**
- Kd ~10⁻²⁰ M at pH 7.4 (physiological) — extraordinarily tight, ensuring virtually all plasma iron is protein-bound
- Kd ~10⁻⁶ M at pH 5.5 (endosomal pH after TFR1-mediated endocytosis) — conformational opening releases Fe³⁺ in the acidified endosome → iron recycled; TF-TFR1 complex recycles to cell surface

**Transferrin receptor 1 (TFR1/CD71):**
- 90 kDa type II transmembrane homodimer; binds holo-Tf (diferric Tf) with Kd ~1 nM; low affinity for apo-Tf
- Constitutively expressed on erythroid precursors (up to 800,000 copies/cell), hepatocytes, rapidly dividing cells
- Iron-responsive element (IRE): TFR1 mRNA 3'-UTR contains multiple IREs; when iron is low → IRP1/IRP2 bind IREs → stabilize TFR1 mRNA → ↑ TFR1 expression → more iron uptake; when iron is high → IRPs do not bind → TFR1 mRNA degraded

**Transferrin receptor 2 (TFR2):**
- Liver-specific; binds holo-Tf with Kd ~30 nM (lower affinity than TFR1); not regulated by IREs
- TFR2 + hemojuvelin (HJV) + BMP6 → signal transducer for hepcidin regulation: high TSAT → more holo-Tf → TFR2 activation → BMP-SMAD → hepcidin transcription → ferroportin degradation → iron restriction
- TFR2 mutations → hereditary hemochromatosis type III (impaired hepcidin sensing)

## Function

### Iron delivery to erythropoiesis

1. Apo-transferrin from hepatocytes enters plasma → picks up Fe³⁺ from ferroportin on duodenal enterocytes and macrophages → diferric-Tf in circulation
2. Diferric-Tf binds TFR1 on erythroid precursors → receptor-mediated endocytosis (clathrin-coated pit) → endosome acidified by H⁺-ATPase → pH 5.5 → Fe³⁺ released from Tf → Fe³⁺ reduced to Fe²⁺ by STEAP3 (metalloreductase) → DMT1 (SLC11A2) exports Fe²⁺ to cytoplasm → mitochondrial iron import for haem synthesis
3. Apo-Tf + TFR1 complex recycled to cell surface → apo-Tf released at pH 7.4 → cycle repeats
4. ~20-25 mg iron cycled daily through this pathway — largely from macrophage erythrophagocytosis

### Non-erythroid iron delivery

- **Myoglobin:** Muscle TFR1 delivers iron for myoglobin haem synthesis
- **Iron-sulfur cluster proteins:** Mitochondrial Fe-S assembly requires labile iron pool; TFR1-mediated uptake fuels the Fe-S biogenesis pathway (crucial for respiratory chain, DNA repair enzymes)
- **Enzymes:** Ribonucleotide reductase (rate-limiting step in DNA synthesis), catalase, cytochrome P450 enzymes all require iron
- **Brain:** Transferrin + TFR1 at blood-brain barrier endothelium → transcytosis; neurons and oligodendrocytes express TFR1; iron deficiency in early life → impaired myelination → cognitive deficits

### Transferrin as iron homeostasis sensor

The liver senses circulating iron burden through plasma transferrin saturation:
- **Low TSAT:** ↓ holo-Tf → ↓ TFR2 signaling → ↓ BMP6-SMAD → ↓ hepcidin → ↑ ferroportin → ↑ iron absorption and recycling → TSAT normalizes
- **High TSAT:** ↑ holo-Tf → ↑ TFR2 + BMP6-SMAD → ↑ hepcidin → ferroportin degradation → ↓ iron → TSAT normalizes
- This feedback loop maintains TSAT at ~25-35% under normal conditions

## Mechanism

### Clinical interpretation of iron studies

| Parameter | Iron deficiency | Anemia of chronic disease | Hemochromatosis | Thalassaemia |
|:----------|:---------------|:--------------------------|:----------------|:-------------|
| Serum iron | ↓ | ↓ | ↑ | ↑ (transfused) or normal |
| TIBC (transferrin) | ↑ | ↓ or normal | ↓ | ↓ or normal |
| TSAT | ↓ (<20%) | ↓ or normal | ↑↑ (>60%) | ↑↑ |
| Serum ferritin | ↓ (<12 ng/mL) | ↑ (acute phase) | ↑↑ | ↑ (iron overload) |
| Soluble TFR1 (sTFR) | ↑ (more TFR1 on cells) | Normal | ↓ | ↑ (erythropoietic expansion) |
| Reticulocyte Hb content | ↓ | ↓ | Normal | ↓ |

**Key diagnostic combinations:**
- **Iron deficiency anemia (IDA):** Low ferritin (<12 ng/mL is diagnostic; <30 ng/mL with anemia = probable IDA) + low TSAT + high TIBC + microcytic hypochromic anemia
- **Anemia of chronic disease (ACD):** Low TSAT but high/normal ferritin (ferritin is acute-phase reactant); low TIBC; normal or high serum ferritin; distinguish with sTFR/log ferritin ratio
- **Hereditary hemochromatosis:** High TSAT (>50% women, >60% men) + high ferritin + C282Y or H63D HFE mutations; normal or low TIBC
- **Transfusion iron overload:** TSAT 100% + ferritin >1,000-2,500 ng/mL → chelation threshold

### Non-transferrin-bound iron (NTBI)

When transferrin is 100% saturated (as in β-thalassaemia major, hemochromatosis, massive transfusion), excess plasma iron circulates as NTBI:
- NTBI = Fe²⁺ not bound to transferrin (albumin-bound, citrate-bound, or free)
- NTBI is rapidly taken up by hepatocytes, cardiomyocytes, endocrine glands (pituitary, pancreas, gonads) via ZIP14 (SLC39A14) transporter
- NTBI in cardiomyocytes → Fenton reaction → ROS → mitochondrial damage → arrhythmia and cardiomyopathy (the most dangerous complication of iron overload)
- Labile plasma iron (LPI): the redox-active fraction of NTBI; measured by fluorescent probe; correlates with cardiac iron deposition on MRI T2*

**Iron chelation targets NTBI:**
- **Deferoxamine (DFO):** Parenteral (SC/IV infusion); binds Fe³⁺ with high affinity; first-line for decades; 8-12h infusion × 5-7 days/week; hearing and vision monitoring required
- **Deferasirox (Exjade/Jadenu):** Oral once daily; tridentate iron chelator; nephrotoxic (creatinine monitoring); preferred for transfusion iron overload in SCD and thalassaemia
- **Deferiprone (Ferriprox):** Oral 3×/day; bidentate; penetrates cell membranes → cardiac iron chelation (superior to DFO for cardiac iron); agranulocytosis risk (CBC weekly monitoring)
- **Combination chelation:** Deferasirox + deferiprone or DFO + deferiprone for severe cardiac or hepatic iron overload

## Connections

- `connects-to` → **[Hemoglobin](../hemoglobin/README.md)** — Transferrin delivers Fe³⁺ to erythroid precursors via TFR1; iron is inserted into protoporphyrin IX by ferrochelatase → haem; each haemoglobin tetramer requires 4 Fe²⁺ atoms; erythropoiesis demands ~80% of total body iron daily — the major functional iron compartment.
- `connects-to` → **[Hepcidin](../hepcidin/README.md)** — Hepcidin degrades ferroportin → blocks duodenal iron absorption and macrophage recycling → lowers transferrin saturation; elevated TSAT → liver BMP6 + TFR2/HJV → hepcidin upregulation → restrains iron loading; hepcidin-transferrin axis is the core iron homeostasis sensor.
- `connects-to` → **[Thalassemia](../../07-system/thalassemia/README.md)** — β-thalassaemia major: massive ineffective erythropoiesis → ERFE suppresses hepcidin → unconstrained duodenal iron absorption → transferrin saturation 100% → NTBI → tissue deposition (liver, heart, pituitary); chelation with deferasirox targets NTBI.
- `connects-to` → **[Sickle Cell Disease](../../07-system/sickle-cell-disease/README.md)** — Chronic transfusion therapy in SCD (for stroke prevention, recurrent ACS) leads to transfusional iron overload; elevated TSAT + ferritin >1000 ng/mL → iron chelation required; deferasirox is preferred oral chelator in SCD; cardiac and hepatic MRI T2* monitors iron deposition.

[^ganz-2013-systemic-iron-homeostasis]: Ganz T, Nemeth E. Iron homeostasis in host defence and inflammation. *Nat Rev Immunol.* 2015;15(8):500-510. [doi:10.1038/nri3863](https://doi.org/10.1038/nri3863) · [PubMed 26160612](https://pubmed.ncbi.nlm.nih.gov/26160612/)
[^muckenthaler-2017-iron-balance]: Muckenthaler MU, Rivella S, Hentze MW, Galy B. A red carpet for iron metabolism. *Cell.* 2017;168(3):344-361. [doi:10.1016/j.cell.2016.12.034](https://doi.org/10.1016/j.cell.2016.12.034) · [PubMed 28129536](https://pubmed.ncbi.nlm.nih.gov/28129536/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
