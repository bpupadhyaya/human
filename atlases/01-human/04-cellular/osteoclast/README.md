---
schema: human-scale-entry/v1
id: osteoclast
name: Osteoclast
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Large multinucleated haematopoietic cells (monocyte lineage) that resorb bone via ruffled-border V-ATPase acidification and cathepsin K collagenolysis. RANK-RANKL-OPG axis and NFATc1 govern differentiation; key targets in osteoporosis, RA bone erosion, and Paget disease."
aliases: ["bone-resorbing cell", "multinucleated giant cell", "resorption lacuna cell", "tartrate-resistant acid phosphatase positive cell", "TRAP+ cell"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    note: "Osteoclast precursors (monocyte lineage, RANK+CCR2+) home to bone marrow via CCL2 and RANKL gradients; M-CSF from marrow stromal cells and RANKL from osteoblasts drive fusion into multinucleated osteoclasts in the endosteal niche."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Osteoclasts are haematopoietic (monocyte lineage) and respond to immune signals; Th17 cells (IL-17 → osteoblast RANKL), TNF-α, and M-CSF regulate differentiation; immunodeficiency and GVHD alter bone metabolism via osteoclast dysregulation."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Osteoclasts share monocyte/macrophage lineage (CD68, CD14 low, MHC-II) and regulatory signals (M-CSF, Fc receptor); in inflammatory joint disease, macrophages at the pannus-bone interface convert via RANKL into bone-eroding osteoclasts."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "IL-6 via gp130/STAT3 on osteoblasts increases RANKL and decreases OPG, tipping balance toward osteoclastogenesis; IL-6 also acts directly on osteoclast precursors; tocilizumab (anti-IL-6R) reduces bone erosion in RA."
  - target: 01-human/03-molecular/rankl
    relation: modulated-by
    note: "RANKL (TNFSF11) binds RANK on osteoclast precursors → TRAF6 → NF-κB + AP-1 → NFATc1 → cathepsin K, TRAP, integrin β3 → mature resorbing osteoclast; OPG is the decoy receptor; denosumab mimics OPG to suppress osteoclastogenesis."
---

# Osteoclast

## Overview

Osteoclasts are large, terminally differentiated, multinucleated cells that are the principal mediators of bone resorption. Unlike osteoblasts (mesenchymal origin), osteoclasts arise from the haematopoietic monocyte/macrophage lineage, forming by fusion of circulating osteoclast precursors (OCPs) in response to RANKL (receptor activator of nuclear factor-κB ligand) and M-CSF signals. They attach to bone surfaces via an actin sealing zone, acidify the enclosed Howship's lacuna with vacuolar-ATPase-generated protons (pH 4.5), and dissolve the mineral phase before proteolytically digesting the organic collagen matrix with cathepsin K (CTSK).[^alberts-mol-cell-biology]

The RANK–RANKL–OPG axis couples osteoclast activity to osteoblast signals, making the system exquisitely tunable by systemic hormones (PTH, oestrogen, calcitonin) and local immune signals (IL-1, TNF-α, IL-6, IL-17). NFATc1 is the master transcription factor of osteoclast differentiation, activated by RANKL → TRAF6 → NF-κB + ITAM co-stimulatory signalling → Ca²⁺-calcineurin dephosphorylation of NFATc1 → nuclear translocation. Osteoclast dysregulation — excess activity over osteoblast output — underlies osteoporosis, rheumatoid arthritis erosions, Paget's disease, and lytic bone metastases.[^guyton-hall]

## Structure

**Size and morphology.** Osteoclasts are 20–100 µm in diameter and contain 3–20 or more nuclei (in pathological states up to 50+). On bone surfaces they adopt a distinctive polarised morphology with four specialised membrane domains:
1. **Ruffled border (apical/resorptive domain):** Highly folded plasma membrane invagination facing the resorption lacuna; rich in V-ATPase (proton pump subunits Atp6v0d2, Atp6v1a), CLC-7 (chloride channel), CTSK vesicle fusion sites, and LAMP2. Equivalent to the lysosomal membrane — the ruffled border is essentially an exofacing lysosome.
2. **Sealing zone (actin ring):** Circumferential belt of podosomes (actin cores + integrin αvβ3/vitronectin receptor periphery) that fuse into a continuous gasket against the bone surface, isolating the resorption lacuna from the extracellular fluid.
3. **Basolateral domain:** Faces away from bone; site of ion extrusion (HCO₃⁻/Cl⁻ exchange via AE2, Na⁺/K⁺-ATPase) and transcytotic vesicle exocytosis of digested matrix products.
4. **Functional secretory domain:** Basolateral area where transcytotic vesicles exocytose collagen fragments and TRAP (tartrate-resistant acid phosphatase).

**Key markers.** TRAP (TRAP5b serum isoform — osteoclast-specific clinical marker of bone resorption), cathepsin K (CTSK), calcitonin receptor (CALCR), αvβ3 integrin, RANK (TNFRSF11A), CD68 (shared with macrophages), DC-STAMP, OC-STAMP (fusion markers).

## Function

**Bone resorption (stepwise mechanism):**

1. **Sealing zone formation.** αvβ3 integrin binds RGD-containing bone matrix proteins (osteopontin, bone sialoprotein) → podosome superstructure (actin-Arp2/3 cores with talin, vinculin, paxillin periphery) organises into a continuous sealing ring → isolates Howship's lacuna.[^alberts-mol-cell-biology]

2. **Ruffled border acidification.** Vacuolar-type H⁺-ATPase (V-ATPase, composed of V₀ membrane sector [a3/TCIRG1, d2/ATP6V0D2, c subunits] + V₁ cytoplasmic ATPase) pumps H⁺ into the lacuna → local pH 4.5 → dissolution of hydroxyapatite: Ca₁₀(PO₄)₆(OH)₂ + 14H⁺ → 10Ca²⁺ + 6H₂PO₄⁻ + 2H₂O. CLC-7 (chloride-proton antiporter) co-transports Cl⁻ to maintain charge neutrality. Inside the osteoclast, carbonic anhydrase II (CAII) generates H⁺ (CO₂ + H₂O → H⁺ + HCO₃⁻); HCO₃⁻ exits at the basolateral membrane via AE2 (exchanged for Cl⁻) to sustain the cycle.[^guyton-hall]

3. **Proteolytic matrix digestion.** Cathepsin K (CTSK) — a cysteine protease maximally active at pH 4–5 — is the primary collagenase; it cleaves type I collagen triple helix at multiple sites (including the helical domain, unlike MMPs which can only cleave the telopeptide region). MMP-9 and MMP-13 contribute at higher pH near the lacuna margins. Collagen C-terminal (CTX) and N-terminal (NTX) crosslinked fragments released into blood/urine are standard clinical markers of bone resorption.

4. **Transcytosis.** Degraded mineral and collagen fragments are taken up into transcytotic vesicles at the ruffled border → traverse osteoclast cytoplasm via tubulovesicular network → exocytosis at the basolateral functional secretory domain. TRAP (released into blood as TRAP5b) dephosphorylates osteopontin fragments, preventing re-binding to bone and enabling further resorption.

**RANKL/RANK/OPG axis.** RANKL (TNFSF11), expressed on osteoblast/stromal cell surface and as a soluble form, binds RANK (TNFRSF11A) on OCPs → TRAF6 recruitment → NF-κB (IKKβ → p65/p50 canonical; IKKα → RelB/p52 non-canonical for osteoclast survival) + MAP kinases (JNK, ERK, p38) + PI3K/Akt. ITAM co-stimulatory signalling (DAP12/FcRγ with receptors OSCAR, TREM2, PIR-A) → Syk → PLCγ → IP₃ → Ca²⁺ oscillations → calcineurin → dephosphorylates NFATc1 → nuclear translocation → NFATc1 transactivates CTSK, TRAP, CLC-7, RANK, Atp6v0d2, αvβ3, CALCR — the full osteoclast gene programme.[^alberts-mol-cell-biology]

## Lifecycle

**Development:**
HSC → common myeloid progenitor (CMP) → granulocyte-monocyte progenitor (GMP) → monocyte precursor (bone marrow) → blood monocyte (classical CD14⁺⁺CD16⁻) → osteoclast precursor (OCP, CCR2⁺CX₃CR1⁺RANK⁺) — circulates in blood → homes to bone endosteum via CCL2 and RANKL chemotactic gradients → RANKL + M-CSF on bone surface → OCP proliferation (M-CSF → c-Fms → ERK/Akt) and commitment → OCP–OCP fusion (DC-STAMP/OC-STAMP, CD9, CD47-SIRPα interaction) → multinucleated pre-osteoclast → attachment to bone → activated osteoclast (ruffled border, sealing zone, V-ATPase assembly).[^guyton-hall]

**Lifespan.** Mature osteoclasts are short-lived (1–2 weeks). Survival signals: RANKL → anti-apoptotic NFκB (RelB/p52), PI3K/Akt, Bcl-xL; M-CSF → Mcl-1. Pro-apoptotic signals: OPG (decoy receptor, blocks RANKL), calcitonin, oestrogen, bisphosphonates (N-containing: mevalonate pathway blockade → ↓prenylation of Ras/Rho/Rac → caspase activation → apoptosis). After resorption lacuna is complete, osteoclasts detach, migrate, and undergo apoptosis; coupling factors (TGF-β, BMP, IGF-1, Slit3 from resorbed matrix) recruit osteoblast precursors to initiate the formation phase of the remodelling cycle.

## Connections

- **Part-of bone-marrow [^guyton-hall]:** Osteoclast precursors (monocyte lineage, RANK⁺CCR2⁺) circulate in blood and home to bone marrow via CCL2 and RANKL gradients; M-CSF from marrow stromal cells and RANKL from osteoblasts drive fusion into multinucleated osteoclasts in the endosteal niche.
- **Modulates immune-system [^alberts-mol-cell-biology]:** Osteoclasts are haematopoietic (monocyte lineage) and respond to immune signals; Th17 cells (IL-17 → osteoblast RANKL), TNF-α, and M-CSF regulate osteoclast differentiation; immunodeficiency and GVHD alter bone metabolism via osteoclast dysregulation.
- **Modulates macrophage [^alberts-mol-cell-biology]:** Osteoclasts share the monocyte/macrophage lineage (CD68, CD14 low, MHC-II) and regulatory signals (M-CSF, Fc receptor); in inflammatory joint disease, macrophages at the pannus-bone interface are converted by RANKL into bone-eroding osteoclasts.
- **Modulates IL-6 [^guyton-hall]:** IL-6 via gp130/STAT3 on osteoblasts increases RANKL expression and decreases OPG, tipping the balance toward osteoclastogenesis; IL-6 also acts directly on osteoclast precursors; tocilizumab (anti-IL-6R) reduces bone erosion in RA.
- **Modulated-by RANKL:** RANKL (TNFSF11) binds RANK on osteoclast precursors → TRAF6 → NF-κB + AP-1 → NFATc1 → cathepsin K, TRAP, integrin β3 → mature resorbing osteoclast; OPG is the decoy receptor; denosumab mimics OPG to suppress osteoclastogenesis.

## Pathology

**Osteoporosis.** ↑Osteoclast activity relative to osteoblast output → net bone loss → microarchitectural deterioration → fragility fractures (vertebral compression, hip, Colles'). Primary (postmenopausal: oestrogen withdrawal → ↑RANKL/OPG), secondary (glucocorticoid-induced: ↑osteoclast lifespan via Bcl-2, ↑osteoblast apoptosis; hyperparathyroidism; multiple myeloma). Treatment: bisphosphonates (alendronate, zoledronate — N-containing → FPP synthase inhibition → ↓Ras/Rho prenylation → osteoclast apoptosis), denosumab (anti-RANKL mAb, subcutaneous 60 mg 6-monthly), odanacatib (cathepsin K inhibitor — never approved due to stroke risk in phase III).

**Rheumatoid Arthritis Bone Erosion.** Synovial fibroblasts, Th17 cells, and macrophages at the pannus produce RANKL, TNF-α, and IL-17 → osteoclastogenesis at the cartilage-bone interface → periarticular cortical erosions (hallmark of RA, Sharp/van der Heijde score). Anti-TNF biologics (etanercept, adalimumab), tocilizumab (anti-IL-6R), abatacept, and denosumab reduce radiographic progression by suppressing the cytokine drivers of osteoclastogenesis.

**Paget's Disease of Bone.** Focal uncontrolled osteoclast activation (SQSTM1/p62 mutations affecting NF-κB signalling; paramyxoviral inclusions in osteoclast nuclei — measles, canine distemper virus — controversial) → lytic phase (↑ALP, ↑CTX, bone pain) → compensatory ↑osteoblast → disorganised coarse woven bone (mosaic lamellar pattern on histology). Complications: bone deformity (bowing tibia "sabre shin"), pathological fracture, spinal canal stenosis, hearing loss (temporal bone), high-output cardiac failure (↑bone vascularity), rare malignant transformation to osteosarcoma (<1%). Treatment: bisphosphonates (zoledronate 5 mg single IV dose — most effective, suppresses TRAP5b and CTX for years).

**Giant Cell Tumour of Bone (GCT).** Osteoclast-like multinucleated giant cells within a background of mononuclear stromal cells that drive osteoclastogenesis via RANKL; H3F3A (H3.3 K36M) mutation in stromal cells. Locally aggressive, rarely metastatic; epiphyseal location (distal femur, proximal tibia). Treatment: curettage + bone cement; denosumab (anti-RANKL) for unresectable/recurrent GCT → converts osteoclast-rich tumour to fibrous stromal tissue.

**Multiple Myeloma Bone Disease.** Myeloma plasma cells secrete DKK1 (inhibits osteoblast Wnt), RANKL, MIP-1α (CCL3), IL-3, HGF → ↑osteoclast + ↓osteoblast → extensive osteolytic lesions, vertebral compression fractures, hypercalcaemia (↑PTHrP). Zoledronate (bisphosphonate IV) reduces skeletal-related events and may have direct anti-myeloma activity; denosumab non-inferior to zoledronate in trials.

## See Also

- `../osteoblast/README.md` — RANKL/OPG axis, bone formation coupling
- `../../05-tissue/bone-marrow/README.md` — HSC niche, osteoclast precursor origin
- `../../03-molecular/il-6/README.md` — IL-6 in osteoclastogenesis and RA erosion
- `../../07-system/immune-system/README.md` — osteoimmunology, Th17-RANKL axis
- `../macrophage/README.md` — shared monocyte lineage, macrophage-osteoclast plasticity
