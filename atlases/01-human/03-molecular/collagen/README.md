---
schema: human-scale-entry/v1
id: collagen
name: Collagen
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Most abundant human protein (~30% of total protein); triple-helix of Gly-X-Y repeats (~300 nm). >28 types; types I–IV underpin bone, skin, cartilage, and basement membranes. Mutations cause OI, Alport syndrome, Ehlers-Danlos; excess deposition causes fibrosis."
aliases: ["type I collagen", "type IV collagen", "procollagen", "tropocollagen", "collagen fibril"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "~30% of total protein mass; types I–VII provide tensile strength in bone, skin, cartilage, tendons, blood vessel walls and basement membranes throughout every organ system."
  - target: 01-human/05-tissue/glomerulus
    relation: part-of
    note: "Type IV collagen forms the glomerular basement membrane network; Alport syndrome (COL4A3/4/5 mutations) disrupts GBM structure causing haematuria and progressive CKD."
  - target: 01-human/05-tissue/myocardium
    relation: part-of
    note: "Cardiac ECM is ~2–5% collagen (mainly types I and III); the collagen network transmits cardiomyocyte force and maintains ventricular geometry; excess deposition causes restrictive physiology."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Liver fibrosis: stellate cell activation → excess type I/III collagen deposition → scar tissue replaces hepatic lobule architecture → cirrhosis and portal hypertension."
  - target: 01-human/05-tissue/cortical-bone
    relation: composed-of
    note: "Composed Of by Cortical Bone."
---

# Collagen

## Overview

**Collagen** is the most abundant protein in the human body, comprising approximately **30% of total protein mass** and providing the structural scaffold for virtually every tissue [^stryer-biochemistry]. The collagen superfamily contains **more than 28 distinct types**, encoded by at least 44 genes, ranging from the large fibril-forming collagens (types I–III, V, XI) that provide tensile strength in bone, skin, and tendon, to the sheet-forming type IV that scaffolds all basement membranes, to transmembrane collagens that anchor cells to the extracellular matrix (ECM).

Its defining feature — the **triple helix** — was elucidated by Ramachandran and Kartha in 1955 and confirmed crystallographically thereafter. This rope-like structure achieves extraordinary mechanical strength: a single type I collagen fibril can withstand tensile stresses of ~1 GPa, exceeding that of many steel alloys of comparable cross-section.

Collagen pathology is correspondingly broad: **scurvy** (vitamin C deficiency), **osteogenesis imperfecta** (brittle bone disease), **Ehlers-Danlos syndrome** (connective tissue fragility), **Alport syndrome** (hereditary nephritis), and **fibrosis** of liver, lung, and kidney are all fundamentally collagen disorders.

## Structure

### Triple-helix architecture

The basic unit of all collagens is the **triple helix**:

- Three **α-chains**, each adopting a left-handed **polyproline II (PPII) helix** conformation
- Three PPII helices coil around each other into a right-handed **superhelix** (~300 nm long, 1.5 nm diameter for fibrillar collagens)
- **Gly-X-Y repeat**: every third residue must be **glycine** (Gly) — the only residue small enough to occupy the sterically restricted center of the triple helix; X is frequently **proline** (Pro), Y is frequently **4-hydroxyproline** (Hyp)
- **Hyp at the Y position** forms interchain H-bonds via water bridges that critically stabilize the triple helix; loss of hydroxylation (scurvy) destabilizes the structure

### Collagen types and distribution

| Type | Gene(s) | Distribution | Primary role |
|:---|:---|:---|:---|
| **I** | COL1A1/A2 | Bone, skin, tendon, cornea, dentin | Tensile strength; ~90% of body collagen |
| **II** | COL2A1 | Cartilage, vitreous | Compressive force resistance |
| **III** | COL3A1 | Fetal skin, blood vessels, GI tract | Often co-deposited with type I |
| **IV** | COL4A1–A6 | All basement membranes (GBM, tubular BM, skin BMZ) | Sheet network; filtration scaffold |
| **V** | COL5A1/A2 | Cornea, interstitial tissues | Regulates fibril diameter |
| **VI** | COL6A1–A3 | Widespread | Beaded microfilaments; links fibrils to ECM |
| **VII** | COL7A1 | Skin dermal-epidermal junction | Anchoring fibrils |
| **XVII** | COL17A1 | Skin hemidesmosomes | Transmembrane; BPAG2 |

## Function

Collagen's functions follow its structural diversity:

**Mechanical support:** Type I fibrils in bone are mineralized with hydroxyapatite, providing a composite material that resists both tension (collagen) and compression (mineral). In tendon, type I fibrils are precisely aligned axially, creating near-perfect tensile cables. In skin, a random criss-cross weave confers multidirectional resistance.

**Filtration scaffold:** Type IV collagen in the glomerular basement membrane (GBM) forms a covalently cross-linked network (the only collagen type that does so in vivo) that contributes to the charge and size selectivity of glomerular filtration [^alberts-mol-cell-biology].

**Basement membrane organization:** Type IV collagen networks (assembled from α1–α6 chains) provide the platform for laminin polymerization, integrin attachment, and growth factor sequestration in all BMs — vascular, pulmonary, renal, neural, and cutaneous.

**Signaling scaffold:** Collagens bind and present growth factors (FGFs, TGF-β), regulate MMP activity, and transduce signals via integrin receptors (α1β1, α2β1, αVβ3) and the discoidin domain receptors (DDR1/2), modulating cell proliferation, migration, and differentiation.

**Cardiac ECM:** Types I and III collagen form the myocardial collagen network (perimysium, endomysium) that couples cardiomyocyte shortening to chamber ejection and prevents over-distension; the ratio of stiff type I to compliant type III determines passive ventricular stiffness.

## Mechanism

### Biosynthesis

Collagen biosynthesis is among the most elaborately post-translationally modified of any protein [^stryer-biochemistry]:

1. **Ribosomal synthesis** of pre-pro-α-chains; signal peptide directs to ER
2. **ER processing:**
   - Signal peptide cleavage
   - Prolyl 4-hydroxylase (P4H; requires Fe²⁺, O₂, ascorbate, α-KG as cofactors) → Pro → 4-Hyp (~100 per chain)
   - Prolyl 3-hydroxylase → 3-Hyp at Pro986 (1 per chain)
   - Lysyl hydroxylase (PLOD1/2/3) → Lys → Hydroxylysine (Hyl) — subsequently O-glycosylated (galactosyl-Hyl; glucosyl-galactosyl-Hyl)
   - Disulfide bonding of C-propeptides nucleates α-chain association → triple helix propagates N-terminally (zipper mechanism)
3. **Golgi:** Further glycosylation; packaging into secretory vesicles
4. **Extracellular processing:**
   - ADAMTS2/14 (N-proteinase) and BMP1/tolloid (C-proteinase) cleave N- and C-propeptides → **tropocollagen** (~300 nm × 1.5 nm)
   - Tropocollagen self-assembles into **D-staggered fibrils** (67 nm D-period) by charge- and shape-complementarity; N-propeptide cleavage regulates fibril diameter (type V acts as a template)
5. **Cross-linking:** Lysyl oxidase (LOX; Cu²⁺-dependent; extracellular) oxidizes lysine/Hyl → allysine; spontaneous condensation → **pyridinoline and deoxypyridinoline crosslinks** (trivalent; provide fibril mechanical strength)

### Degradation

Triple helices resist most proteases. Cleavage requires:
- **Collagenases (MMP-1, MMP-8, MMP-13):** cleave the triple helix at a specific Gly-Ile/Leu site ~75% from the N-terminus → ¾ and ¼ fragments that denature at 37°C
- **Gelatinases (MMP-2, MMP-9):** degrade denatured collagen fragments
- **MT-MMPs (MMP-14):** pericellular collagen degradation in invasion and tissue remodeling
- **Cathepsins (B, K, L):** intracellular lysosomal collagen degradation (relevant in osteoclast bone resorption)

MMP activity is regulated by TIMPs (tissue inhibitors of metalloproteinases); imbalance toward proteolysis drives ECM degradation (joint destruction, tumor invasion) while imbalance toward synthesis drives fibrosis.

### Post-translational modifications in disease

- **AGEs (advanced glycation end-products):** non-enzymatic glycation of collagen in diabetes → crosslinks that stiffen the collagen network → arterial stiffness, reduced GFR, cardiac diastolic dysfunction
- **Citrullination:** by PAD4 → anti-citrullinated collagen antibodies in RA
- **Nitration (ONOO⁻):** nitrotyrosine modification in inflammatory states → altered MMP cleavage

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): Collagen constitutes ~30% of total protein mass; types I–VII provide tensile strength in bone, skin, cartilage, tendons, blood vessel walls and basement membranes throughout every organ system [^stryer-biochemistry].
- **Part-of** → [Glomerulus](../../05-tissue/glomerulus/README.md): Type IV collagen forms the glomerular basement membrane network; Alport syndrome (COL4A3/4/5 mutations) disrupts GBM structure causing haematuria and progressive CKD [^alberts-mol-cell-biology].
- **Part-of** → [Myocardium](../../05-tissue/myocardium/README.md): Cardiac ECM is ~2–5% collagen (mainly types I and III); the collagen network transmits cardiomyocyte force and maintains ventricular geometry; excessive deposition in heart failure causes restrictive physiology [^stryer-biochemistry].
- **Modulates** → [Liver](../../06-organ/liver/README.md): Liver fibrosis involves hepatic stellate cell activation driving excess type I/III collagen deposition, replacing hepatic lobule architecture with scar tissue and producing cirrhosis and portal hypertension [^alberts-mol-cell-biology].

## Pathology

| Disease | Mechanism | Clinical features |
|:---|:---|:---|
| **Scurvy** | Vitamin C deficiency → prolyl hydroxylase failure → unstable triple helix | Bleeding gums, perifollicular haemorrhages, wound dehiscence, corkscrew hairs |
| **Osteogenesis imperfecta (OI)** | COL1A1/A2 Gly substitution → dominant-negative defect in triple helix | Brittle bones, blue sclerae, dentinogenesis imperfecta; 8 types (I–VIII) |
| **Ehlers-Danlos syndrome (EDS)** | Classical: COL5A1/A2; Vascular: COL3A1; Kyphoscoliotic: PLOD1 | Joint hypermobility, skin hyperextensibility; vascular EDS: arterial rupture risk |
| **Alport syndrome** | COL4A3/A4/A5 mutations → GBM structural failure | Haematuria, proteinuria, progressive CKD, sensorineural deafness |
| **Pulmonary fibrosis (IPF)** | TGF-β → myofibroblast activation → excess type I/III collagen | Honeycombing on CT, ↓DLCO, progressive dyspnoea; antifibrotics: pirfenidone, nintedanib |
| **Liver cirrhosis** | Portal fibroblasts + stellate cells → type I/III collagen → bridging fibrosis | Portal hypertension, ascites, hepatic encephalopathy, HCC risk |
| **Renal fibrosis** | Tubular EMT + interstitial myofibroblasts → collagen I/III/IV → GFR decline | Progressive CKD; seen in diabetic nephropathy, IgA nephropathy |
| **Keloid / hypertrophic scar** | Unregulated type I/III collagen from dermal fibroblasts post-injury | Raised scar beyond wound margins (keloid); treatments: steroids, laser, pressure |

## See Also

- [ATP](../atp/README.md) — provides energy for prolyl hydroxylase reaction (indirectly, via NADPH regeneration) and collagen secretion
- [IL-6](../il-6/README.md) — drives TGF-β-mediated fibrogenic signaling; hepatic and pulmonary collagen remodeling
- [TNF-alpha](../tnf-alpha/README.md) — induces MMP-1/MMP-3 in synovial fibroblasts; net collagen degradation in RA
- [NF-kB](../nf-kb/README.md) — transcriptional activator of collagenases (MMP-1, -3, -9) in inflammatory states
- [Hepatic lobule](../../05-tissue/hepatic-lobule/README.md) — normal hepatic architecture progressively replaced by collagen in fibrosis
- [Podocyte](../../04-cellular/podocyte/README.md) — directly contacts type IV collagen GBM via α3β1 integrin; podocyte injury and GBM disruption co-occur in Alport syndrome

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
