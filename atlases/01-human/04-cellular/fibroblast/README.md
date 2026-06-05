---
schema: human-scale-entry/v1
id: fibroblast
name: Fibroblast
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Mesenchymal spindle-shaped cells that synthesise and remodel extracellular matrix (collagen I/III, fibronectin, elastin). Activated by TGF-β1 to become contractile myofibroblasts (α-SMA+). Central to wound healing, organ fibrosis, and tumour stroma."
aliases: ["myofibroblast", "stromal fibroblast", "cancer-associated fibroblast", "CAF", "activated fibroblast"]
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
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Hepatic stellate cells (liver fibroblasts) are activated by TGF-β/PDGF after hepatocyte injury → collagen I/III secretion → progressive hepatic fibrosis → cirrhosis; anti-fibrotic targets include TGF-β, PDGF-R, and ROCK."
  - target: 01-human/05-tissue/myocardium
    relation: modulates
    note: "Cardiac fibroblasts (~60% of cardiac cells by number) synthesise myocardial ECM; TGF-β-mediated myofibroblast activation after MI → collagen scar (beneficial acute) → ongoing fibrosis → ↑ventricular stiffness → HFpEF."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Cancer-associated fibroblasts (CAFs) remodel the tumour ECM creating a physical and chemical immunosuppressive barrier; CAF-derived CXCL12, TGF-β, and IL-6 exclude T cells from the tumour core."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "Fibroblasts are major producers of IL-6 during inflammation and in cancer stroma; CAF-derived IL-6 activates JAK/STAT3 in tumour cells (survival, proliferation, therapy resistance) and recruits MDSCs."
---

# Fibroblast

## Overview

The fibroblast is the **principal architect of connective tissue** — a mesenchymal spindle-shaped cell found throughout the body (dermis, organ stroma, tendons, joint capsules, submucosa, periosteum) whose core function is the continuous synthesis, secretion, and remodelling of the **extracellular matrix (ECM)**. In healthy tissue, fibroblasts are largely quiescent (fibrocytes); injury or inflammation activates them, and in pathological states their persistent activation drives organ fibrosis in virtually every tissue [^alberts-mol-cell-biology].

Fibroblasts lack a single definitive positive marker and are identified largely by context and a combination of features: vimentin (intermediate filament), absence of lineage markers (CD45 for haematopoietic, CD31/PECAM for endothelial, EpCAM for epithelial), together with PDGFRα (platelet-derived growth factor receptor α) and FSP1/S100A4 in activated states [^guyton-hall].

The **myofibroblast** — the contractile, highly secretory fibroblast variant induced by TGF-β1 — is the central effector of both physiological wound repair and pathological fibrosis. Understanding the balance between myofibroblast activation and resolution is one of the most clinically important problems in medicine.

## Structure

### Morphology and Markers

| Feature | Quiescent Fibroblast | Activated Myofibroblast |
|:---|:---|:---|
| **Shape** | Elongated, spindle, ~30–50 µm | More spread, stellate, larger stress fibres |
| **Nucleus** | Ovoid, prominent nucleolus | Larger, euchromatic |
| **Key intermediate filament** | Vimentin | Vimentin + **α-SMA (ACTA2)** |
| **ER** | Moderate rough ER | Extensive rough ER (high secretory output) |
| **Stress fibres** | Sparse actin stress fibres | Dense α-SMA-containing stress fibres |
| **Cell-ECM adhesion** | Focal contacts (integrin αvβ3/β5, FAK) | Fibronexus — supermature focal adhesions linking α-SMA fibres to ECM fibronectin EDA |
| **Gap junctions** | Cx43 (sparse) | Cx43 (upregulated — coordinate contraction) |

**Fibroblast markers**: PDGFRα, FSP1/S100A4, fibroblast-specific protein (FAP — cancer/reactive), collagen-I producer, Thy-1 (CD90) in some populations.

### ECM Products

Fibroblasts are the primary source of interstitial ECM:

| ECM Component | Gene(s) | Function |
|:---|:---|:---|
| Collagen I | COL1A1/COL1A2 | Main structural fibrillar collagen; skin, tendon, bone, scar |
| Collagen III | COL3A1 | Reticular fibres; co-deposits with Col I; prominent in early scar |
| Collagen V | COL5A1 | Regulates Col I fibril diameter |
| Fibronectin (EDA/EDB splice) | FN1 | Cell adhesion, wound healing; EDA isoform activates TLR4 |
| Elastin | ELN | Elastic recoil; vascular walls, lung, skin |
| Versican / Decorin / Biglycan | VCAN / DCN / BGN | Proteoglycans; modulate collagen fibrillogenesis and growth factor bioavailability |
| Hyaluronic acid | HAS1/2/3 | Space-filling; water retention; CD44 ligand |
| MMPs (MMP-1, MMP-3, MMP-9) | MMP genes | Matrix metalloproteinases — ECM degradation (balanced by TIMPs) |

## Function

### 1. ECM Homeostasis

In healthy tissue, fibroblasts continuously deposit and remodel ECM in a balanced cycle:
- **Matrix synthesis**: procollagen secreted → extracellular enzymatic processing by BMP-1/tolloid (N- and C-propeptide cleavage) → tropocollagen → fibril assembly (cross-linking by lysyl oxidase LOX)
- **Matrix degradation**: MMPs (collagenases, stromelysins, gelatinases) vs. TIMPs (tissue inhibitors) — balance determines ECM composition and stiffness
- **Mechanosensing**: matrix stiffness sensed via integrins (αvβ3/β5) → FAK/Src → YAP/TAZ nuclear translocation → fibrogenic gene programme (positive feedback loop: stiffness drives more fibrosis)

### 2. Wound Healing and Myofibroblast Differentiation

The transition from quiescent fibroblast to myofibroblast follows a defined sequence driven by biochemical and biomechanical cues:

1. **Injury**: platelet degranulation → PDGF (proliferation, migration), TGF-β1 (activation)
2. **Proto-myofibroblast stage**: fibronectin EDA splice variant incorporation into matrix → early α-SMA expression via mechanosensing
3. **Myofibroblast**: TGF-β1 → TGF-βR2/R1 → **SMAD2/3:SMAD4** complex → nucleus → ↑ACTA2 (α-SMA), ↑COL1A1/COL3A1, ↑CTGF/CCN2, ↑FN1-EDA
4. **Wound contraction**: α-SMA stress fibres generate pulling forces via fibronexus connections
5. **Resolution**: TGF-β clearance → myofibroblast apoptosis (p53/Bax/Fas pathway) → remodelling phase

Key co-activators: PDGF (PDGFRα/β → PI3K, Erk, PLC → proliferation/migration), IL-4 and IL-13 (Th2-type fibrosis; STAT6 → ↑TGF-β, ↑collagen), IL-6/STAT3, mechanical strain (integrin → FAK → MRTF-A → SRF → α-SMA), HIF-1α (hypoxia-driven fibrosis) [^alberts-mol-cell-biology].

### 3. Tissue-Specific Fibroblast Variants

**Hepatic stellate cells (HSC/Ito cells):**
- Perisinusoidal mesenchymal cells in the Space of Disse
- Quiescent: store vitamin A (retinyl esters in lipid droplets), express GFAP, desmin
- Activated (by PDGF, TGF-β1, ET-1, LPS, lipid peroxidation products): lose retinol stores, upregulate PDGFRβ, α-SMA → collagen I/III secretion → portal fibrosis → cirrhosis
- Primary fibrogenic cell in NAFLD/NASH, viral hepatitis, alcoholic liver disease

**Cardiac fibroblasts:**
- ~60–70% of cardiac cells by number (far outnumber cardiomyocytes); contribute ~15% of cardiac mass
- Maintain myocardial ECM architecture; communicate with cardiomyocytes via paracrine (IL-6, TGF-β, FGF) and direct (Cx43 gap junction) pathways
- Post-MI: activated to myofibroblasts → fibrous scar (essential for structural integrity) → ongoing activation → interstitial fibrosis → diastolic dysfunction

**Cancer-associated fibroblasts (CAFs):**
- Heterogeneous population in tumour stroma (origins: resident, bone marrow-derived, epithelial-mesenchymal transition)
- Functions: ECM remodelling (dense collagen capsule — physical barrier to drug penetration), growth factor secretion (FGF, HGF, EGF → tumour proliferation), immunosuppression (TGF-β, CXCL12, IL-10 → T cell exclusion, MDSC recruitment), angiogenic support (VEGF, bFGF)
- High CAF abundance correlates with poor prognosis in pancreatic, breast, colorectal cancer

## Lifecycle

### Development and Origin

Fibroblasts arise from:
- **Mesenchymal stem cells (MSCs)** — the primary source in most connective tissues
- **Neural crest cells** — craniofacial fibroblasts (dermis, stroma of head and neck)
- **Epicardium-derived cells (EPDCs)** — cardiac fibroblasts
- **Epithelial-mesenchymal transition (EMT)** — controversial but described in kidney and liver fibrosis
- **Bone marrow-derived fibrocytes** — circulating CD45+/Col-I+ cells recruited in chronic fibrosis

No single origin; tissue fibroblasts are **positionally specified** during development (Hox gene patterns) and retain memory of their anatomical origin even after multiple passages in culture [^guyton-hall].

### Fibrosis and Resolution

**Normal healing** (acute wound): Injury → inflammation → fibroblast activation (days 3–7) → ECM deposition → wound closure → myofibroblast apoptosis (day 10–21) → scar remodelling

**Fibrosis** (chronic/pathological): Persistent injury or dysregulated signalling → ongoing myofibroblast activation → irreversible ECM accumulation → loss of organ architecture → organ failure

Senescent myofibroblasts (p21+/p16+ cells that escape apoptosis) contribute to persistent fibrosis; their paracrine SASP (senescence-associated secretory phenotype: IL-1, IL-6, MMPs) perpetuates the fibrogenic microenvironment. Clearance by macrophages (via GPNMB/CD206 efferocytosis) is required for resolution.

## Connections

- **Modulates** liver [→ liver](../../06-organ/liver/README.md): Hepatic stellate cells (liver fibroblasts) are activated by TGF-β/PDGF after hepatocyte injury → collagen I/III secretion → progressive hepatic fibrosis → cirrhosis; anti-fibrotic targets include TGF-β, PDGF-R, and ROCK.
- **Modulates** myocardium [→ myocardium](../../05-tissue/myocardium/README.md): Cardiac fibroblasts (~60% of cardiac cells by number) synthesise myocardial ECM; TGF-β-mediated myofibroblast activation after MI → collagen scar (beneficial acute) → ongoing fibrosis → ↑ventricular stiffness → HFpEF.
- **Modulates** immune system [→ immune-system](../../07-system/immune-system/README.md): Cancer-associated fibroblasts (CAFs) remodel the tumour ECM creating a physical and chemical immunosuppressive barrier; CAF-derived CXCL12, TGF-β, and IL-6 exclude T cells from the tumour core.
- **Modulates** IL-6 [→ il-6](../../03-molecular/il-6/README.md): Fibroblasts are major producers of IL-6 during inflammation and in cancer stroma; CAF-derived IL-6 activates JAK/STAT3 in tumour cells (survival, proliferation, therapy resistance) and recruits MDSCs.

## Pathology

| Condition | Key Driver | Features |
|:---|:---|:---|
| **Liver cirrhosis** | Stellate cell/HSC activation (NASH, alcohol, viral hepatitis) | Portal hypertension, hepatocellular failure; irreversible past compensated cirrhosis |
| **IPF (idiopathic pulmonary fibrosis)** | Pathological TGF-β myofibroblast activation in lung | UIP pattern (honeycombing, traction bronchiectasis); nintedanib/pirfenidone slow progression |
| **Cardiac fibrosis** | Post-MI or chronic hypertension → myofibroblast activation | Diastolic dysfunction, HFpEF, arrhythmia (fibrotic remodelling of conduction system) |
| **Systemic sclerosis (SSc)** | Autoimmune TGF-β-driven widespread fibroblast activation | Anti-Scl-70 (topoisomerase I) or anti-centromere Ab; skin thickening, ILD, PAH, renal crisis |
| **Keloid / hypertrophic scar** | Failed apoptosis of dermal myofibroblasts | Excessive collagen I accumulation beyond wound margins (keloid) or within (hypertrophic) |
| **Dupuytren contracture** | Palmar fascia fibroblast transformation | Progressive flexion contracture of ring/little finger; collagenase injection (xiaflex) or fasciectomy |
| **Cancer stroma (CAFs)** | Tumour microenvironment signals (TGF-β, PDGF, FGF) | Dense desmoplastic stroma; drug resistance, immunosuppression, poor prognosis |

## See Also

- [Liver](../../06-organ/liver/README.md) — hepatic stellate cells are the liver-specific fibroblast lineage central to hepatic fibrosis
- [Myocardium](../../05-tissue/myocardium/README.md) — cardiac fibroblasts outnumber cardiomyocytes; critical for scar formation and pathological remodelling
- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — hepatocytes signal to stellate cells via TGF-β and PDGF in liver injury
- [Macrophage](../../04-cellular/macrophage/README.md) — macrophages both activate fibroblasts (M1-derived TNF-α/IL-1β, TGF-β) and resolve fibrosis (M2/anti-inflammatory clearance of senescent myofibroblasts)
- [IL-6](../../03-molecular/il-6/README.md) — key paracrine cytokine secreted by fibroblasts driving tumour cell survival and inflammatory amplification
