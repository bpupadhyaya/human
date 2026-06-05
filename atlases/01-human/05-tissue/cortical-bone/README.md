---
schema: human-scale-entry/v1
id: cortical-bone
name: Cortical Bone
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Dense outer shell of bone (~80% of bone mass) composed of concentric Haversian osteons. Hydroxyapatite-mineralised type I collagen matrix provides compressive and tensile strength; osteocytes in the lacunocanalicular network sense strain and orchestrate remodelling."
aliases: ["compact bone", "lamellar bone", "haversian bone", "cortex", "cortical bone tissue"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Cortical bone forms the dense shell of all bones (~80% of bone mass); provides mechanical support for locomotion and organ protection; stores 99% of body Ca²⁺ and 85% of phosphate in hydroxyapatite crystals."
  - target: 01-human/05-tissue/bone-marrow
    relation: modulates
    note: "Cortical bone forms the rigid casing of the medullary canal; the endosteal surface provides the HSC niche via osteoblast-secreted CXCL12, SCF/Kit-L, and angiopoietin-1; Haversian canals supply vasculature to the cortex."
  - target: 01-human/03-molecular/collagen
    relation: part-of
    note: "Type I collagen (~90% of bone organic matrix) forms D-banded fibrils that template hydroxyapatite mineralisation; collagen mutation (osteogenesis imperfecta) or degradation (scurvy, MMPs) destabilises the cortical bone composite."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Osteocalcin (VitK-carboxylated for HA binding) circulates in decarboxylated form → binds GPRC6A → ↑insulin secretion and ↑muscle glucose uptake during exercise; links bone to metabolic and cardiovascular homeostasis."
---

# Cortical Bone

## Overview

Cortical bone (compact bone) is the dense, solid bone tissue that forms the outer shell of every bone in the human skeleton and constitutes the entire diaphysis (shaft) of long bones. It accounts for approximately 80% of total adult bone mass (~2 kg in a 70 kg adult). Compared with cancellous/trabecular bone (spongy, 20% of bone mass, predominating in vertebrae, flat bones, and metaphyses), cortical bone has low porosity (~4–10%), high stiffness, and high compressive and tensile strength, making it the principal load-bearing material of the skeleton.[^guyton-hall]

Beyond its mechanical role, cortical bone is the body's largest mineral reservoir, storing 99% of total body calcium (approximately 1 kg) and 85% of phosphate in the form of hydroxyapatite crystals. It participates in mineral homeostasis through osteoclastic resorption (releasing Ca²⁺ and Pi under PTH stimulation) and osteoblastic deposition (under calcitriol, oestrogen, and mechanical stimuli). Osteocytes embedded throughout the matrix serve as mechanosensors and endocrine cells, secreting sclerostin (Wnt pathway inhibitor) and FGF23 (phosphate regulator) to couple mechanical loading, bone mass, and mineral metabolism.[^alberts-mol-cell-biology]

## Structure

**Osteon (Haversian system) — the primary structural unit.** Cortical bone is organised into cylindrical osteons, each 100–300 µm in diameter and up to several millimetres long, running parallel to the long axis of the bone. Each osteon consists of 5–20 concentric lamellae (3–8 µm thick each) of mineralised collagen surrounding a central Haversian canal (40–50 µm diameter). Adjacent lamellae have collagen fibrils oriented in alternating helical directions (~30° offset), conferring resistance to multidirectional mechanical loads — analogous to plywood cross-lamination. Haversian canals contain arterioles, venules, unmyelinated nerve fibres, and lymphatics. Volkmann's canals (transverse/oblique channels) interconnect adjacent Haversian canals and link the periosteal and endosteal surfaces to the Haversian network, enabling nutrient/waste exchange across the full cortical thickness.[^guyton-hall]

**Osteocyte lacunocanalicular network (LCN).** Osteocytes (mature osteoblasts encased in mineralised matrix during bone formation) reside in lacunae (~25,000/mm³; ~42 billion osteocytes total in the adult skeleton). Each osteocyte extends 40–60 slender cytoplasmic dendrites through narrow canaliculi (~200–300 nm diameter), contacting neighbouring osteocytes via gap junctions (connexin-43, Cx43) and, at the bone surface, osteoblasts and bone-lining cells. Interstitial fluid flows through this canalicular network driven by bone deformation during locomotion (~2,000–4,000 microstrain at habitual activity); this fluid shear activates osteocyte primary cilia, piezoelectric signals, and integrin mechanosensors → prostaglandin E₂, NO, and ATP release → anabolic osteoblast stimulation.[^alberts-mol-cell-biology]

**Mineral-matrix composite.** Cortical bone is a hierarchical composite material:
- *Mineral phase* (70% wet weight): Calcium hydroxyapatite [Ca₁₀(PO₄)₆(OH)₂] platelets 60–70 nm long × 10–30 nm wide × 2–4 nm thick, oriented with their c-axis aligned along the collagen fibril axis. Hydroxyapatite provides compressive stiffness; carbonated apatite substitutions modulate solubility.
- *Organic matrix* (22% wet weight): ~90% type I collagen fibrils (D-banded, 67 nm periodicity); ~10% non-collagenous proteins: osteocalcin (Gla residues bind HA, also circulates as a hormone), osteopontin (RGD motif, integrin-binding, osteoclast attachment), osteonectin/SPARC, bone sialoprotein, fibronectin, biglycan, decorin.
- *Water* (~8% wet weight): In canalicular fluid and bound to matrix macromolecules; critical for viscoelasticity and fracture toughness. Dehydration sharply increases brittleness.[^guyton-hall]

**Periosteum and endosteum.**
- *Periosteum*: Bi-layered outer membrane. Fibrous outer layer (type I collagen, Sharpey's fibres anchoring tendons and ligaments) + inner cambial layer (osteoprogenitor cells, periosteal stem cells, fibroblasts, capillaries). The cambial layer is the primary source of cortical bone appositional growth (during development) and fracture callus (during repair via intramembranous and endochondral ossification). The periosteum is densely innervated (sensory C and Aδ fibres) — periosteal pain is the dominant feature of fractures, periostitis, and metastatic bone disease.
- *Endosteum*: Thin cellular layer lining the marrow canal and Haversian canal walls; contains bone-lining cells (quiescent osteoblasts), osteoclasts, and osteoprogenitors; site of cortical bone remodelling and the osteoblastic HSC niche.

## Function

**Mechanical support and protection.** Mechanical properties of cortical bone (longitudinal axis): Young's modulus 17–25 GPa, ultimate tensile strength ~100–130 MPa, ultimate compressive strength ~170–190 MPa, fracture toughness 2–5 MPa·m^0.5. These values reflect the mineral-collagen composite: hydroxyapatite provides stiffness (prevents deformation) while collagen fibril networks absorb crack energy (toughness). Cortical bone is anisotropic: stronger in the longitudinal axis (aligned with habitual loading — explains why femoral shafts can sustain >3× body weight in running). Ageing reduces toughness: non-enzymatic collagen crosslinking by advanced glycation end-products (AGEs) → more brittle matrix; reduced water content also decreases fracture resistance.[^guyton-hall]

**Calcium and phosphate homeostasis.** Osteoclast-mediated cortical resorption releases Ca²⁺ and Pi — regulated primarily by:
- PTH (parathyroid hormone): ↑osteoclast recruitment and activity (via RANKL upregulation on osteoblasts/osteocytes) → bone resorption → ↑serum Ca²⁺ (also ↑renal Ca²⁺ reabsorption, ↑calcitriol synthesis → ↑intestinal Ca²⁺ absorption). Chronic PTH excess → cortical bone loss (PTH acts as an anabolic stimulus for trabecular bone but catabolic for cortical bone).
- Calcitriol (1,25-dihydroxyvitamin D₃): ↑intestinal Ca²⁺/Pi absorption, ↑osteoclastogenesis for bone mineral mobilisation; also promotes osteoblast differentiation → bone mineralisation.
- Calcitonin (from thyroid C-cells): ↓osteoclast activity → ↑bone Ca²⁺ deposition → ↓serum Ca²⁺.

**Mechanosensing and adaptive remodelling.** Osteocytes detect mechanical strain through fluid shear in the LCN → reduce sclerostin secretion (Wnt inhibitor) → ↑Wnt/β-catenin signalling in osteoblasts → ↑bone formation. Mechanically induced osteocyte signals also include RANKL (→ osteoclast activation at sites of microdamage for targeted repair) and DMP1/PHEX (regulate FGF23 → renal phosphate handling). Disuse (bed rest, paralysis, space flight) → ↑sclerostin → ↓bone formation + ↑resorption → cortical thinning (1–2% per month in complete unloading).[^alberts-mol-cell-biology]

**Endocrine function.** Osteocalcin secreted by osteoblasts/osteocytes undergoes post-translational carboxylation (vitamin K-dependent γ-carboxylase → Gla residues → HA binding → matrix retention). Under conditions of bone resorption or decarboxylation at low pH, undercarboxylated osteocalcin (ucOC) is released into circulation → binds GPRC6A receptor in pancreatic β-cells (↑insulin secretion), skeletal muscle (↑glucose uptake, ↑exercise capacity), Leydig cells (↑testosterone synthesis), and brain (↑memory). FGF23 from osteocytes suppresses renal phosphate reabsorption (↓NaPi2a/2c) and ↓calcitriol synthesis — a feedback loop that prevents hyperphosphataemia from excessive bone resorption.[^guyton-hall]

## Connections

- **part-of** [human-body](../../08-whole-body/human-body/README.md): Cortical bone forms the dense shell of all bones (~80% of bone mass); provides mechanical support for locomotion and organ protection; stores 99% of body Ca²⁺ and 85% of phosphate in hydroxyapatite crystals.
- **modulates** [bone-marrow](../../05-tissue/bone-marrow/README.md): Cortical bone forms the rigid casing of the medullary canal; the endosteal surface provides the HSC niche via osteoblast-secreted CXCL12, SCF/Kit-L, and angiopoietin-1; Haversian canals supply vasculature to the cortex.
- **part-of** [collagen](../../03-molecular/collagen/README.md): Type I collagen (~90% of bone organic matrix) forms D-banded fibrils that template hydroxyapatite mineralisation; collagen mutation (osteogenesis imperfecta) or degradation (scurvy, MMPs) destabilises the cortical bone composite.
- **modulates** [cardiovascular-system](../../07-system/cardiovascular-system/README.md): Osteocalcin (VitK-carboxylated for HA binding) circulates in decarboxylated form → binds GPRC6A → ↑insulin secretion and ↑muscle glucose uptake during exercise; links bone to metabolic and cardiovascular homeostasis.

## Pathology

**Osteoporosis (cortical component).** Cortical bone porosity increases from ~4% at age 40 to ~15% by age 80, reflecting a shift toward Haversian remodelling that creates large, interconnected pores (Haversian canal enlargement). Loss of oestrogen at menopause → ↑RANKL, ↓OPG → ↑osteoclast activity → accelerated cortical thinning. Cortical bone loss increases hip and distal radius fracture risk more strongly than trabecular loss. Treatment: bisphosphonates (↓osteoclast apoptosis → ↓resorption), denosumab (anti-RANKL monoclonal antibody), teriparatide/romosozumab (anabolic, ↑osteoblast).[^guyton-hall]

**Stress fractures.** Fatigue failure when repetitive submaximal loading accumulates microcracks faster than osteocyte-directed remodelling can repair them. Common sites: metatarsal shafts (march fracture), tibial diaphysis, femoral neck (high-risk — complete fracture risk), navicular, sacrum. Risk factors: abrupt training intensity increase, low bone density, relative energy deficiency in sport (RED-S, formerly female athlete triad), vitamin D deficiency. Management: relative rest, load reduction; high-risk fractures (femoral neck, anterior tibia) may require internal fixation.

**Osteonecrosis (avascular necrosis, AVN).** Interruption of cortical/subchondral blood supply → osteocyte death within 12–48 hours → cortical structural failure → articular collapse. Commonest site: femoral head (blood supply via lateral femoral circumflex artery — vulnerable to intracapsular fracture or dislocation). Risk factors: corticosteroids (most common non-traumatic cause — ↓osteoblast proliferation, ↑adipogenesis, fat emboli to subchondral vessels), alcohol, sickle cell disease, decompression illness. Treatment: core decompression (early), total hip replacement (late). Bisphosphonate-related osteonecrosis of the jaw (BRONJ): suppression of bone remodelling → exposed, devitalised jaw cortex after dental extraction.

**Paget's disease of bone.** Focal dysregulation of osteoclast and osteoblast activity (measles paramyxovirus sequestration in osteoclasts, SQSTM1/p62 mutations) → accelerated, disorganised remodelling → replacement of lamellar cortical bone with disorganised woven bone → ↑bone volume but ↓strength (↑fracture risk), bone pain, deformity (bowed tibia, enlarged skull), ↑alkaline phosphatase, ↑sarcoma risk (osteosarcoma in <1%). Treatment: bisphosphonates (zoledronate).

**Osteosarcoma.** Primary malignant bone tumour arising from osteoblastic progenitors in cortical bone, most commonly around the knee (distal femur, proximal tibia) in adolescents (2nd peak in elderly with Paget's). Radiographic features: mixed lytic/sclerotic cortical lesion, periosteal reaction (Codman's triangle — elevated periosteum), sunburst pattern (mineralised tumour matrix). Treatment: neoadjuvant chemotherapy (cisplatin, doxorubicin, methotrexate) + limb-salvage surgery; 5-year survival ~60–70% for localised disease.

## See Also

- [bone-marrow](../../05-tissue/bone-marrow/README.md) — haematopoietic tissue enclosed and supported by the cortical shell
- [collagen](../../03-molecular/collagen/README.md) — primary organic matrix component of cortical bone
- [human-body](../../08-whole-body/human-body/README.md) — whole-body mineral reservoir and mechanical scaffold context
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — osteocalcin endocrine link to metabolic homeostasis
- [insulin](../../03-molecular/insulin/README.md) — osteocalcin-stimulated β-cell secretion connects bone to glycaemic control
