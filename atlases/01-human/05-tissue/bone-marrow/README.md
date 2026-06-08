---
schema: human-scale-entry/v1
id: bone-marrow
name: Bone Marrow
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Haematopoietic tissue filling the medullary cavity of flat bones and the epiphyses of long bones. Produces all blood cell lineages from multipotent haematopoietic stem cells (HSCs) at ~500 billion cells/day. Red marrow active; yellow marrow (fat) increases with age."
aliases: ["medulla ossium", "red bone marrow", "yellow bone marrow", "haematopoietic tissue", "marrow"]
sources:
  - id: orkin-2008-hematopoiesis
    type: peer-reviewed
    cite: "Orkin SH, Zon LI. Hematopoiesis: an evolving paradigm for stem cell biology. Cell. 2008;132(4):631-44."
    doi: "10.1016/j.cell.2008.01.025"
    pmid: "18295580"
    url: "https://doi.org/10.1016/j.cell.2008.01.025"
  - id: morrison-2014-hsc-niche
    type: peer-reviewed
    cite: "Morrison SJ, Scadden DT. The bone marrow niche for haematopoietic stem cells. Nature. 2014;505(7483):327-34."
    doi: "10.1038/nature12984"
    pmid: "24429631"
    url: "https://doi.org/10.1038/nature12984"
  - id: short-2018-bone-marrow-overview
    type: peer-reviewed
    cite: "Short NJ, Kantarjian H. Bone marrow anatomy and its role in haematopoiesis. Best Pract Res Clin Haematol. 2021;34(1):101249."
    doi: "10.1016/j.beha.2021.101249"
    pmid: "33762083"
    url: "https://doi.org/10.1016/j.beha.2021.101249"
  - id: hall-guyton-14-blood
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 32."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Bone marrow is a primary lymphoid organ; all haematopoietic cell lineages — including all immune cells — originate from HSCs in marrow. B-cell lymphopoiesis occurs entirely in bone marrow."
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "Bone marrow produces ~2 million erythrocytes per second, sustaining the oxygen-carrying capacity of the cardiovascular system throughout adult life."
  - target: 01-human/04-cellular/erythrocyte
    relation: contains
    note: "Red bone marrow produces ~200 billion erythrocytes per day via erythropoiesis within sinusoidal niches; reticulocytes egress through marrow sinusoid walls."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "B-cell lymphopoiesis occurs entirely in bone marrow: HSC → CLP → pro-B → pre-B → immature B → naive B cell. Bone marrow stromal cells (CXCL12⁺ CXCL13⁺ reticular cells) provide essential survival signals."
  - target: 01-human/04-cellular/macrophage
    relation: contains
    note: "Monocyte precursors and macrophage progenitors are generated in bone marrow from GMPs; macrophage nurse cells (osteoclasts, marrow macrophages) also reside in the niche and support erythroblast island formation."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Bone marrow is distributed across the axial skeleton (vertebrae, sternum, ribs, pelvis) and epiphyses of long bones; total marrow volume in an adult is ~1.5–2 kg (~4% of body weight)."
  - target: 01-human/03-molecular/hemoglobin
    relation: composed-of
    note: "Composed Of by Hemoglobin."
  - target: 01-human/03-molecular/erythropoietin
    relation: modulated-by
    note: "Modulated by Erythropoietin."
  - target: 01-human/02-atomic/phosphorus
    relation: modulated-by
    note: "Modulated by Phosphorus."
  - target: 01-human/07-system/musculoskeletal-system
    relation: part-of
    note: "Part Of by Musculoskeletal System."
  - target: 01-human/05-tissue/cortical-bone
    relation: modulated-by
    note: "Modulated by Cortical Bone."
  - target: 01-human/04-cellular/neutrophil
    relation: composed-of
    note: "Composed Of by Neutrophil."
  - target: 01-human/04-cellular/osteoblast
    relation: composed-of
    note: "Composed Of by Osteoblast."
  - target: 01-human/04-cellular/osteoclast
    relation: composed-of
    note: "Composed Of by Osteoclast."
  - target: 01-human/04-cellular/platelet
    relation: composed-of
    note: "Composed Of by Platelet."
  - target: 01-human/03-molecular/cxcl12
    relation: modulated-by
    note: "CXCL12 from CAR cells (CXCL12-abundant reticular cells) → CXCR4 on HSC → Gαi → PI3K/Akt + actin polymerization → HSC retention in bone marrow niches; plerixafor (AMD3100, CXCR4 antagonist) blocks this → HSC egress into blood → collection for autologous transplant."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "PNH arises from a single PIGA-mutant HSC in bone marrow; immune-mediated destruction of normal HSCs (aplastic anemia context) allows clonal expansion of GPI-deficient clone; 25-40% of aplastic anemia patients have PNH clones; PNH and AA overlap on a continuum."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor HSC engraftment in recipient bone marrow is required for GvHD; the marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark."
---

# Bone Marrow

## Overview

Bone marrow is the soft, highly vascularised connective tissue occupying the medullary cavities of bones. It is the central haematopoietic factory of the adult human body, generating an estimated 500 billion blood cells per day — approximately 3.5 million cells per second — to replace senescent erythrocytes, neutrophils, platelets, and other short-lived blood elements. All major blood cell lineages arise from a small, self-renewing pool of multipotent haematopoietic stem cells (HSCs) maintained in specialised marrow niches.

Beyond haematopoiesis, the bone marrow is a primary lymphoid organ: B-cell lymphopoiesis and T-cell precursor generation both initiate here (T-cell maturation completes in the thymus). It is also a major site of immune memory: long-lived plasma cells produced during systemic immune responses home back to bone marrow survival niches, where they secrete antibodies for years to decades. In addition, bone marrow is a reservoir of mesenchymal stromal cells (MSCs) that support haematopoiesis, contribute to bone and cartilage repair, and exert immunomodulatory functions.

Two functional types of bone marrow exist: **red marrow** (haematopoietically active, red owing to haemoglobin-rich erythrocytes in various maturation stages) and **yellow marrow** (haematopoietically inactive, dominated by adipocytes). At birth, nearly all marrow is red. With age, red marrow gradually converts to yellow marrow in the appendicular skeleton, retracting to the axial skeleton (vertebrae, ribs, sternum, pelvis, skull) and proximal femur/humerus by adulthood. Yellow marrow retains the capacity to reconvert to red marrow under haematopoietic stress (haemolytic anaemia, severe blood loss).

## Structure

**Gross anatomy.** In adults, active red marrow is concentrated in vertebral bodies, the sternum, ribs, flat bones of the pelvis and skull, and the proximal epiphyses of the femur and humerus. Total marrow volume is approximately 1.5–2 kg (~4% of body weight); red marrow accounts for roughly half. The marrow is encased within the endosteum (inner bone surface lined by osteoblasts and osteoclasts) and perfused by a nutrient artery that branches into arterioles → sinusoids.

**Sinusoidal vasculature.** The bone marrow sinusoids are thin-walled, fenestrated endothelial tubes (diameter 10–100 µm) that form an extensive network. They are lined by a discontinuous basal lamina and surrounded by pericytes (CXCL12-abundant reticular cells, CAR cells). Blood cells egress from the parenchyma into the sinusoid lumen through cytoplasmic pores (3–5 µm), a process regulated by CXCR4/CXCL12 and VLA-4/VCAM-1 retention signals and S1P1 egress signalling. Megakaryocytes extend pro-platelet projections directly into sinusoid lumens; erythrocyte reticulocytes squeeze through fenestrations.

**Haematopoietic niches.** HSC maintenance is regulated by two principal niches:

1. **Endosteal niche:** HSCs near the endosteum associate with osteoblasts, CARreticular cells, and CXCL12/SCF-expressing stromal cells. Characterised by lower O₂ tension (hypoxia; ~1–2% pO₂), which promotes HSC quiescence via HIF-1α. THPO (thrombopoietin) from osteoblasts, SCF (stem cell factor, KITLG) from CAR cells, and CXCL12 are key retention/survival signals.
2. **Perivascular niche:** A separate HSC pool lies adjacent to sinusoidal endothelium and perivascular LepR⁺ stromal cells. This niche is more permissive to HSC cycling and mobilisation. Both CXCL12 and SCF are produced here at high levels; leptin receptor (LepR)⁺ mesenchymal progenitors are a key stromal component.

**Erythroblastic islands.** A specialised microanatomical unit: a central macrophage surrounded by 10–30 erythroblasts at varying maturation stages. The macrophage provides iron, growth signals (EpoR signalling amplification), and engulfs extruded nuclei. Disruption of erythroblastic islands impairs erythropoiesis in iron-deficiency and haemolytic states.

**Megakaryocyte-platelet axis.** Megakaryocytes are large (50–150 µm), polyploid (up to 128N via endomitosis) cells that contact sinusoidal walls and shed 1,000–3,000 platelets per cell by cytoplasmic fragmentation. Platelet production (~150–400 × 10⁹/L blood) is driven by thrombopoietin (THPO), with a ~5–7 day megakaryocyte maturation cycle.

**Yellow marrow architecture.** Consists predominantly of unilocular adipocytes (marrow adipose tissue, MAT) interspersed with blood vessels, nerves, and occasional mesenchymal progenitors. MAT is metabolically distinct from subcutaneous and visceral fat; it expands under caloric restriction and stress, and secretes adiponectin, CXCL12, and SCF to modulate haematopoiesis.

## Function

**Haematopoiesis — the myeloid lineage.**
- Granulopoiesis: HSC → CMP → GMP → myeloblast → promyelocyte → myelocyte → band → neutrophil (10 days; ~10¹¹ neutrophils/day). Driven by G-CSF (filgrastim pharmacologically mimics this).
- Monocytopoiesis: GMP → monocyte precursor (cMoP) → classical monocyte (CD14⁺⁺ CD16⁻) → egress into blood (~3 × 10⁷ monocytes/day).
- Erythropoiesis: HSC → MEP → BFU-E → CFU-E → proerythroblast → reticulocyte → erythrocyte (7 days; ~2×10⁶ RBCs/second). EPO from kidneys drives CFU-E expansion.
- Megakaryopoiesis: HSC → MEP → MkP → megakaryocyte → platelets (5–7 days; ~10¹¹ platelets/day). THPO-dependent.

**B-lymphopoiesis.** CLPs → pro-B cells (IL-7R+; IL-7 from stromal cells is the survival signal) → pre-B cells (immunoglobulin heavy-chain VDJ recombination occurs) → immature B cells (light-chain VJ recombination; negative selection against autoreactivity) → IgM⁺ IgD⁺ naive B cells egress to periphery. Marrow stroma provides CXCL12, IL-7, SCF, and FLT3L at each stage.

**Long-lived plasma cell (LLPC) niche.** After peripheral germinal centre reactions, affinity-matured plasma cells express CXCR4 and home back to bone marrow survival niches where CXCL12, IL-6, IL-5 (from eosinophils), APRIL (from megakaryocytes), and BAFF maintain plasma cell survival for decades — the basis of durable serum antibody levels after infection or vaccination.

**Mesenchymal functions.** MSCs support haematopoiesis via paracrine cytokine secretion and can differentiate into osteoblasts, chondrocytes, and adipocytes. MSC-derived extracellular vesicles carry microRNAs that regulate HSC quiescence. MSCs also have potent immunosuppressive properties (via IDO, PGE₂, TGF-β secretion), explored therapeutically in graft-versus-host disease (GvHD).

## Connections

- **Upstream regulators:** EPO (erythropoiesis); G-CSF/GM-CSF (granulopoiesis); THPO (megakaryopoiesis); SCF + FLT3L + IL-7 (lymphopoiesis); CXCL12 (HSC retention); hypoxia → HIF-1α (quiescence); sex hormones — oestrogen suppresses/androgen enhances marrow output.
- **Downstream output:** Erythrocytes, platelets, neutrophils, monocytes, eosinophils, basophils, mast cell progenitors, NK cell progenitors, B-cell precursors, T-cell precursors (→ thymus), dendritic cell precursors.
- **Mobilisation.** G-CSF disrupts CXCR4/CXCL12 and VLA-4/VCAM-1 retention interactions → HSC mobilisation into blood (the basis of HSC harvest for transplantation). AMD3100 (plerixafor) directly antagonises CXCR4 for rapid mobilisation.
- **Pathological conditions:** Aplastic anaemia (HSC destruction/autoimmune suppression); leukaemia (malignant transformation of progenitors, displacing normal haematopoiesis); multiple myeloma (malignant plasma cells in marrow); myelofibrosis (JAK2/CALR/MPL mutations → fibrosis); bone marrow failure syndromes (Fanconi anaemia, dyskeratosis congenita); metastatic infiltration (marrow invasion by carcinoma → leukoerythroblastic blood picture).
- **Clinical interventions:** Bone marrow / HSC transplantation (myeloablative conditioning then donor HSC infusion); growth factor support (G-CSF, EPO, THPO-mimetics); CAR-T manufacturing (ex vivo T-cell gene engineering using marrow-derived or mobilised T precursors).
- `connects-to` → **[PNH](../../07-system/pnh/README.md)** — PNH arises from a single PIGA-mutant HSC in bone marrow; immune-mediated destruction of normal HSCs (aplastic anemia context) allows clonal expansion of GPI-deficient clone; 25-40% of aplastic anemia patients have PNH clones; PNH and AA overlap on a continuum.
- `connects-to` → **[GvHD](../../07-system/gvhd/README.md)** — GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor HSC engraftment in recipient bone marrow is required for GvHD; the marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance.
- `connects-to` → **[Aplastic Anemia](../../07-system/aplastic-anemia/README.md)** — AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark.
