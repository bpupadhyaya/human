---
schema: human-scale-entry/v1
id: musculoskeletal-system
name: Musculoskeletal System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "206 bones and ~600 skeletal muscles providing support, movement, haematopoiesis, mineral homeostasis, thermogenesis, and endocrine signaling via osteocalcin and myokines (IL-6, irisin, BDNF)."
aliases: ["locomotor system", "skeletal system", "muscular system", "myoskeletal system"]
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
  - target: 01-human/05-tissue/bone-marrow
    relation: contains
    note: "Red bone marrow (flat bones, vertebrae, proximal femur/humerus in adults) is the primary haematopoietic organ; osteoblasts regulate the HSC niche via CXCL12, SCF, and angiopoietin-1."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Skeletal muscle exercise drives cardiac output (↑HR, ↑SV, ↑CO); metabolites (CO₂, H⁺, K⁺, adenosine) trigger local vasodilation; myokines (IL-6, VEGF) promote capillary angiogenesis."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Bone marrow is the site of HSC haematopoiesis producing all immune cells; exercise-induced IL-6 from muscle induces anti-inflammatory IL-10/IL-1RA; muscle wasting in cachexia is driven by TNF-α/IL-6."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Motor neurons innervate skeletal muscle via NMJ (ACh/nicotinic); sensory innervation via muscle spindles (Ia), Golgi tendon organs (Ib); spinal reflexes and cerebellar coordination govern muscle tone."
  - target: 03-medicine/03-food/vitamin-d
    relation: modulated-by
    note: "Modulated by Vitamin D (Calciferol)."
  - target: 03-medicine/03-food/zinc-dietary
    relation: modulated-by
    note: "Modulated by Dietary Zinc."
  - target: 01-human/03-molecular/myostatin
    relation: modulated-by
    note: "Myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA."
---

# Musculoskeletal System

## Overview

The musculoskeletal system encompasses the body's load-bearing framework — 206 bones in the adult skeleton — together with approximately 600 skeletal muscles (~40% of body mass), their associated tendons and ligaments, the articular cartilages of ~400 joints, and the connective tissue matrices that bind these structures together [^guyton-hall]. Far from merely providing mechanical support, this system is a major metabolic, endocrine, haematopoietic, and thermogenic organ that communicates bidirectionally with virtually every other system through circulating signals.

Key integrative roles include:
- **Mineral homeostasis**: the skeleton holds 99% of body calcium and 85% of inorganic phosphate in hydroxyapatite [Ca₁₀(PO₄)₆(OH)₂], releasing them under PTH and 1,25(OH)₂D₃ control
- **Haematopoiesis**: red bone marrow (axial skeleton and proximal long bones in adults) continuously produces all blood cell lineages
- **Endocrine**: osteocalcin from osteoblasts enters the circulation to promote insulin secretion and muscle glucose uptake; skeletal muscle secretes myokines (IL-6, irisin, BDNF, VEGF, FGF21) that coordinate whole-body metabolism
- **Thermogenesis**: shivering thermogenesis via rapid, oscillatory skeletal muscle contraction generates the majority of metabolic heat during cold exposure

## Structure

### Bone

Bones are classified by shape — long (femur, humerus), short (carpals, tarsals), flat (skull, scapula, sternum, ribs), irregular (vertebrae, facial bones), and sesamoid (patella) — and by architecture: compact (cortical) bone in diaphyses and flat bone surfaces, and cancellous (trabecular) bone at epiphyses and flat bone interiors [^guyton-hall].

The long bone anatomy:
- **Diaphysis** — shaft of compact cortical bone surrounding the medullary canal
- **Epiphyses** — expanded ends, covered by articular hyaline cartilage
- **Metaphysis** — flared junction between diaphysis and epiphysis
- **Growth plate (physis)** — hyaline cartilage disk present until skeletal maturity (~18–25 years); chondrocyte proliferation and hypertrophy, followed by vascular invasion and ossification, drive longitudinal growth under GH/IGF-1 and sex steroid control
- **Periosteum** — fibrous + cambial outer layer; osteoprogenitor cells for appositional growth and fracture repair
- **Endosteum** — inner trabecular and medullary surface; osteoprogenitor niche

**Bone cells**:
| Cell | Origin | Function |
|:---|:---|:---|
| Osteoblasts | Mesenchymal stem cells | Bone matrix synthesis (type I collagen, osteocalcin, osteopontin, bone sialoprotein); mineralization; HSC niche regulation (CXCL12, SCF, Angpt-1) |
| Osteocytes | Osteoblasts embedded in matrix | Mechanosensing via canalicular network; produce sclerostin (Wnt/LRP5 antagonist) to locally suppress formation; FGF-23 (phosphatonin) to regulate kidney Pi excretion |
| Osteoclasts | Monocyte-macrophage lineage (RANKL-driven) | Bone resorption via ruffled border proton pump (V-ATPase) + cathepsin K + MMPs; create Howship's lacunae; controlled by RANKL/RANK/OPG triad |
| Bone lining cells | Quiescent osteoblasts | Surface coverage of resting bone; activated by mechanical stimuli or PTH |

**Bone remodelling (Basic Multicellular Units)**:
The remodelling cycle continuously renews ~10% of the skeleton per year through tightly coupled osteoclast–osteoblast activity [^guyton-hall]:
1. **Activation** — osteocyte mechanosensing or systemic signals (PTH, cytokines) recruit osteoclast precursors; RANKL (from osteoblasts/osteocytes) binds RANK; OPG acts as decoy receptor, antagonizing RANKL
2. **Resorption** — osteoclasts acidify the lacunar space (V-ATPase H⁺ pumping → pH ~4.5) and secrete cathepsin K → dissolve mineral then matrix; takes 2–4 weeks
3. **Reversal** — mononuclear cells prepare the surface; coupling factors released from resorbed matrix (TGF-β, IGF-1, BMP) recruit osteoblasts
4. **Formation** — osteoblasts synthesize osteoid (type I collagen matrix), then deposit hydroxyapatite; takes 3–4 months
5. **Mineralization and rest** — mature bone; lining cells quiesce

**Regulatory signals**:
- **PTH** (parathyroid): ↑osteoclastogenesis via ↑RANKL/↓OPG; also anabolic at intermittent doses (teriparatide mechanism)
- **1,25(OH)₂D₃** (calcitriol): ↑calcium absorption (gut), ↑osteoclast differentiation; indirect anabolic effects
- **Oestrogen**: ↑OPG → ↓RANKL → ↓bone resorption; deficiency at menopause → rapid bone loss → osteoporosis
- **Testosterone**: anabolic via aromatisation to oestradiol (bone density) and direct AR-mediated effects on periosteal expansion
- **Sclerostin (SOST gene)**: Wnt/LRP5/6 antagonist from osteocytes; inhibits osteoblast bone formation; mechanically loaded bone suppresses sclerostin → localised anabolic response; target of romosozumab

### Skeletal Muscle

Each of the ~600 skeletal muscles contains bundles (fascicles) of muscle fibres (myocytes), each a multinucleated cell (10–100 μm diameter; up to 30 cm long in large muscles) derived from fusion of myoblasts during development. Each fibre is subdivided into **myofibrils** composed of sarcomeres in series (Z-disk to Z-disk, ~2.2 μm at rest) — the repeating contractile unit [^alberts-mol-cell-biology].

**Sarcomere structure**:
- **Thin filaments**: actin (F-actin, double helix), tropomyosin, troponin complex (TnC [Ca²⁺ sensor], TnI [inhibitory], TnT [tropomyosin-binding]) — anchored to Z-disk
- **Thick filaments**: myosin II hexamers (2 MHC heavy chains + 4 MLCs light chains); myosin heads (S1 subdomain) are the ATPases and actin-binding motors; arranged in A-band
- **Titin**: giant elastic protein (3.7 MDa) spanning from M-band to Z-disk; molecular spring providing passive tension in stretched sarcomeres
- **Nebulin**: actin filament length ruler in thin filaments

**Fibre types**:
| Type | Metabolism | Myosin isoform | Fatigue resistance | Function |
|:---|:---|:---|:---|:---|
| I (slow oxidative) | Oxidative; high mitochondria; myoglobin-rich (red) | MHC-I (slow, high ATPase efficiency) | Very high | Posture, prolonged low-intensity activity |
| IIa (fast oxidative-glycolytic) | Mixed | MHC-IIa | Intermediate | Intermediate activities |
| IIx/IIb (fast glycolytic) | Glycolytic; low mitochondria; pale | MHC-IIx (humans) | Low | Explosive movements, sprinting |

**Excitation-contraction (EC) coupling**:
1. Somatic motor neuron fires → ACh released at NMJ → nAChR (Nm) → end-plate potential → propagating action potential along sarcolemma
2. AP enters T-tubules → activates voltage-sensor **DHPR (L-type Ca²⁺ channel)** in T-tubule membrane
3. DHPR mechanically gates **RyR1** in sarcoplasmic reticulum (SR) → massive Ca²⁺ release from SR (cytosolic [Ca²⁺] rises from 100 nM to 10–100 μM)
4. Ca²⁺ binds troponin C → conformational change → tropomyosin shifts off actin's myosin-binding sites
5. Myosin S1 binds actin → ATP hydrolysis → power stroke (pulling thin filament toward M-line, shortening sarcomere) → ADP+Pi release → rigor state → new ATP resets
6. Relaxation: SERCA1a (sarcoplasmic/endoplasmic reticulum Ca²⁺-ATPase 1a) pumps Ca²⁺ back into SR; phospholamban (PLN) modulates SERCA; ATP-dependent

**Motor unit recruitment (Henneman's size principle)**:
Small motor units (slow type I fibres) have small, low-threshold motoneurons and are recruited first; large motor units (fast type IIx) have large, high-threshold motoneurons recruited last. This ensures smooth gradation of force and energy-efficient use of fatigue-resistant fibres for low-intensity tasks.

### Joints

| Classification | Examples | Mobility |
|:---|:---|:---|
| Fibrous (sutures) | Skull sutures, distal tibiofibular | Fixed (synarthrosis) |
| Cartilaginous (synchondrosis/symphysis) | Pubic symphysis, intervertebral discs | Slightly movable (amphiarthrosis) |
| Synovial | Knee, hip, shoulder, elbow, wrist, facets | Freely movable (diarthrosis) |

**Synovial joints** consist of articular hyaline cartilage (type II collagen, aggrecan proteoglycan — avascular, aneural; nutrition by diffusion from synovial fluid), a synovial membrane (type A macrophage-like cells + type B fibroblast-like synoviocytes secreting hyaluronic acid and lubricin for boundary lubrication), joint capsule (fibrous layer reinforced by intrinsic and extrinsic ligaments), and in some joints menisci (fibrocartilage, type I/II collagen) or labra (fibrocartilage rings increasing socket depth) [^guyton-hall].

**Cartilage types**:
- **Hyaline** (articular, growth plate, costal, tracheal): type II collagen, aggrecan; translucent; no intrinsic repair capacity once injured
- **Fibrocartilage** (menisci, IVD annulus fibrosus, pubic symphysis): type I + II collagen; tensile + compressive loading
- **Elastic** (auricle, epiglottis, larynx): type II collagen + elastin; resilient

### Tendons, Ligaments, and Entheses

**Tendons** transmit muscle force to bone. Composed predominantly of type I collagen (~65–80% dry weight), organized in a hierarchical crimp structure: collagen molecules → fibrils → fibres → fascicles → tendon. The crimp (sinusoidal waviness) provides the characteristic toe region (low stiffness at small strains) followed by the linear region (high stiffness); failure occurs at strains >8–10% [^guyton-hall].

**Ligaments** stabilize joints; type I + III collagen, slightly lower collagen density than tendons, containing more elastin; allow controlled mobility while preventing abnormal translation.

**Enthesis** — the bone-tendon/ligament insertion — is a fibrocartilaginous gradient zone (unmineralized fibrocartilage → mineralized fibrocartilage → cortical bone) that dissipates the abrupt mechanical discontinuity between compliant tendon and stiff bone. Enthesopathy (inflammation at enthesis) is a hallmark of seronegative spondyloarthropathies (e.g., ankylosing spondylitis, psoriatic arthritis).

## Function

### Mechanical and Protective Functions

- **Support and posture**: the skeleton provides the rigid framework resisting gravitational loading; continuous tonic motor unit firing in postural muscles (erector spinae, soleus) maintains upright stance
- **Locomotion**: coordinated voluntary contraction of agonist/antagonist/synergist muscle groups, controlled by descending motor pathways (corticospinal tract), basal ganglia (movement initiation and smoothing), and cerebellum (coordination and error correction)
- **Protection**: the skull (brain), vertebral column (spinal cord), ribcage (heart, lungs), and pelvis (pelvic viscera) are protective bony enclosures

### Metabolic and Endocrine Functions

**Mineral homeostasis**: the skeleton is the body's calcium reservoir; osteoclastic resorption and osteoblastic formation are continuously balanced to maintain serum ionized Ca²⁺ at 1.1–1.3 mM; regulated jointly with the kidneys and gut by PTH, calcitriol, and calcitonin [^guyton-hall].

**Haematopoiesis**: in adults, red (haematopoietically active) marrow is confined to flat bones (sternum, skull, scapulae, ribs), vertebrae, and the proximal ends of long bones (femur, humerus). Osteoblasts are essential niche cells regulating HSC quiescence and mobilisation via CXCL12/CXCR4, SCF/c-Kit, Angpt-1/Tie2, and OPN/CD44 interactions.

**Skeletal muscle as metabolic organ**: at rest, skeletal muscle accounts for ~20% of resting O₂ consumption; during maximal exercise, this rises to ~80–90%. Muscle is the dominant insulin-stimulated glucose disposal tissue (~80% of postprandial glucose uptake via GLUT4 translocation, driven by insulin → PI3K → AKT → TBC1D4 → GLUT4 exocytosis). Exercise activates AMPK → independent GLUT4 translocation (insulin-independent pathway — relevant for T2D management) [^alberts-mol-cell-biology].

**Myokines** — exercise-induced secretory proteins from contracting muscle:
| Myokine | Trigger | Key effects |
|:---|:---|:---|
| IL-6 | Muscle contraction (AMPK); glycogen depletion | Hepatic gluconeogenesis; induces anti-inflammatory IL-10 and IL-1RA; insulin-sensitising; lipolysis in adipose |
| Irisin (FNDC5 cleavage product) | Exercise via PGC-1α | Browning of white adipose tissue (↑UCP1 in subcutaneous fat); ↑BDNF in hippocampus → memory; ↑bone density |
| BDNF | Endurance exercise | Hippocampal neurogenesis; memory; motor learning |
| VEGF | Hypoxia, exercise | Angiogenesis; ↑capillary density in trained muscle |
| FGF21 | Prolonged exercise/fasting | ↑fatty acid oxidation; ↑ketogenesis; ↑insulin sensitivity |

**Thermogenesis**: shivering (involuntary rapid oscillatory skeletal muscle contractions, controlled by anterior hypothalamic cold sensors → dorsomedial hypothalamus → rostral ventromedial medulla → motor neurons) generates heat by ATP hydrolysis without net mechanical work; major source of heat production in cold exposure in adults. Non-shivering thermogenesis (BAT, UCP1) predominates in neonates and cold-adapted individuals.

### Exercise Adaptation

Chronic exercise drives profound musculoskeletal remodelling [^guyton-hall]:
- **Myofibre hypertrophy**: resistance training → mechanical stretch + mTORC1 activation → ↑muscle protein synthesis; satellite cell (muscle stem cell) activation → myonuclei addition to existing fibres
- **Mitochondrial biogenesis**: endurance training → Ca²⁺ transients + AMPK → PGC-1α → TFAM → ↑mitochondrial DNA + protein synthesis; ↑oxidative capacity, VO₂max
- **GLUT4 upregulation**: both resistance and endurance training → ↑total GLUT4 protein (greater insulin-stimulated glucose uptake at rest)
- **Capillary density**: VEGF secretion → angiogenesis → ↓O₂ diffusion distance to mitochondria
- **Bone density**: mechanical loading → osteocyte mechanosensing → ↓sclerostin → ↑Wnt → ↑bone formation; weight-bearing exercise is the most effective non-pharmacologic intervention for osteoporosis prevention

## Connections

- **Contains:** [bone-marrow](../../05-tissue/bone-marrow/README.md) — red marrow within the skeleton is the primary haematopoietic site; osteoblasts regulate the HSC niche
- **Modulates:** [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — exercise drives cardiac output; metabolites trigger vasodilation; myokines promote angiogenesis
- **Modulates:** [immune-system](../../07-system/immune-system/README.md) — bone marrow produces all immune cells; exercise myokines (IL-6) induce anti-inflammatory responses
- **Modulates:** [nervous-system](../../07-system/nervous-system/README.md) — motor neurons innervate muscle via NMJ; spinal reflexes and cerebellar coordination control movement
- `modulated-by` → **[Myostatin](../../03-molecular/myostatin/README.md)** — myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA.

## Pathology

### Osteoporosis

Imbalanced remodelling with net resorption exceeding formation leads to reduced bone mineral density (BMD), microarchitectural deterioration, and fragility fractures [^guyton-hall]. The most common cause is oestrogen deficiency at menopause (postmenopausal osteoporosis) — oestrogen normally suppresses RANKL-driven osteoclastogenesis. Secondary causes include glucocorticoid excess (suppresses OPG, impairs collagen synthesis, decreases intestinal Ca²⁺ absorption → steroid-induced osteoporosis), hyperparathyroidism, hypogonadism, and malabsorption (vitamin D/Ca²⁺ deficiency).

**Fracture risk (FRAX score)**: BMD T-score ≤ −2.5 defines osteoporosis; T-score −1.0 to −2.5 is osteopenia.

**Treatment**: Antiresorptives (bisphosphonates [alendronate: inhibit osteoclast FPP synthase → ↑apoptosis], denosumab [anti-RANKL mAb]), anabolic agents (teriparatide [intermittent PTH 1-34], abaloparatide, romosozumab [anti-sclerostin mAb → ↑Wnt → ↑formation + ↓resorption]).

### Osteoarthritis (OA)

Progressive breakdown of articular cartilage (↑MMP-1/3/13, ADAMTS-4/5, ↓aggrecan, ↓type II collagen synthesis by chondrocytes), subchondral bone remodelling (sclerosis + osteophyte formation), and synovial inflammation (↑IL-1β, TNF-α, IL-6 from synoviocytes). Risk factors: aging, obesity (mechanical loading + adipokine-mediated inflammation), female sex, previous joint injury. Management: exercise (most effective intervention), weight loss, NSAIDs, intra-articular corticosteroids, and ultimately total joint arthroplasty.

### Rheumatoid Arthritis (RA)

Autoimmune synovitis driven by anti-citrullinated protein antibodies (ACPA) and rheumatoid factor against synovial joints. Pathology: Th17 and macrophage-driven pannus formation → cartilage and bone erosion via RANKL-mediated osteoclast activation and MMPs. Systemic effects (cardiovascular risk, anaemia of chronic disease). Treatment: DMARDs (methotrexate, hydroxychloroquine), biologics (anti-TNF [etanercept, adalimumab], anti-IL-6R [tocilizumab], abatacept [CTLA4-Ig], rituximab [anti-CD20]).

### Sarcopenia

Age-related loss of skeletal muscle mass and function (muscle loss ~1%/year after age 30; accelerates after 60). Pathophysiology: ↓satellite cell pool, ↓anabolic sensitivity (anabolic resistance to protein/leucine and insulin), ↑myostatin (TGF-β family → Smad2/3 → ↓protein synthesis), chronic low-grade inflammation (inflammaging — IL-6, TNF-α → ↑ubiquitin-proteasome degradation), ↓motor unit innervation. Clinical: falls, disability, ↑mortality in frail elderly. Treatment: resistance exercise + adequate protein (1.2–1.6 g/kg/day); leucine supplementation; vitamin D; investigational myostatin inhibitors.

### Duchenne Muscular Dystrophy (DMD)

X-linked frameshift mutation in dystrophin gene (Xp21.2) — largest human gene. Dystrophin connects the actin cytoskeleton to the extracellular matrix (laminin) via the dystrophin-associated protein complex (DAPC). Absence → mechanical fragility → repeated contraction-induced membrane damage → Ca²⁺ overload → necrosis → replacement with fibrotic/fatty tissue. Progressive: loss of ambulation by ~12 years, respiratory failure by 20s without ventilatory support. Exon-skipping therapies (eteplirsen, golodirsen for specific exon mutations), micro-dystrophin gene therapy, glucocorticoids (standard of care — slow progression).

### Rhabdomyolysis

Massive skeletal muscle necrosis releasing myoglobin into blood → myoglobin precipitates in renal tubules (at acid pH) + direct tubular toxicity → acute kidney injury. Causes: extreme exertion, crush injury, seizures, statins (in CYP3A4 interactions), viral myositis. Hallmark: markedly elevated CK (>5,000 IU/L), myoglobinuria (urine dipstick positive for blood, microscopy negative for RBCs). Treatment: aggressive IV fluid resuscitation → alkalinise urine → protect kidneys.

### Fracture Healing

Four overlapping phases [^guyton-hall]:
1. **Haematoma** (hours–days): fracture disrupts periosteal vasculature; haematoma forms; hypoxic environment → macrophage/monocyte infiltration → inflammatory cytokines (IL-1, IL-6, TNF-α) → angiogenesis
2. **Soft callus** (days 1–3 weeks): periosteal osteoprogenitors + mesenchymal stem cells → fibrocartilaginous callus (type II collagen + proteoglycans); stabilizes fracture
3. **Hard callus** (weeks 3–12): chondrocytes hypertrophy → vascular invasion (VEGF) → endochondral ossification → woven bone callus
4. **Remodelling** (months–years): woven bone remodelled to lamellar cortical/trabecular bone by coupled BMU activity; restoration of medullary canal; final structure reflects mechanical loading environment (Wolff's law)

## See Also

- [bone-marrow](../../05-tissue/bone-marrow/README.md) — haematopoietic niche within the musculoskeletal system
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — exercise-muscle-heart crosstalk
- [immune-system](../../07-system/immune-system/README.md) — haematopoiesis, myokine immunomodulation
- [nervous-system](../../07-system/nervous-system/README.md) — motor control, NMJ, reflexes
- [collagen](../../03-molecular/collagen/README.md) — structural backbone of bone, tendon, cartilage, ligament
- [il-6](../../03-molecular/il-6/README.md) — key exercise myokine from skeletal muscle
- [insulin](../../03-molecular/insulin/README.md) — key anabolic hormone for muscle glucose uptake via GLUT4

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
