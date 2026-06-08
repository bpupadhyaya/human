---
schema: human-scale-entry/v1
id: il-6
name: Interleukin-6
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "21 kDa pleiotropic cytokine (4-helix bundle; IL-6 family). Produced by macrophages, T cells, fibroblasts. Signals via IL-6R/gp130 → JAK1/2 → STAT3. Drives acute-phase response, Th17 differentiation, and cytokine storm; target of tocilizumab."
aliases: ["IL-6", "BSF-2", "B-cell stimulatory factor-2", "IFN-beta-2", "interleukin 6"]
taxonomy:
  gene_symbol: "IL6"
  uniprot: "P05231"
sources:
  - id: kishimoto-1985-bsf2
    type: peer-reviewed
    cite: "Hirano T, Yasukawa K, Harada H, et al. Complementary DNA for a novel human interleukin (BSF-2) that induces B lymphocytes to produce immunoglobulin. Nature. 1986;324(6092):73-6."
    pmid: "3920967"
  - id: tanaka-2016-il6-disease
    type: peer-reviewed
    cite: "Tanaka T, Narazaki M, Kishimoto T. IL-6 in inflammation, immunity, and disease. Cold Spring Harb Perspect Biol. 2014;6(10):a016295. [Updated review: Tanaka T, et al. Nat Rev Immunol. 2016.]"
    doi: "10.1038/nri.2016.43"
  - id: stone-2017-gca-tocilizumab
    type: peer-reviewed
    cite: "Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. N Engl J Med. 2017;377(4):317-28."
    doi: "10.1056/NEJMoa1607948"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: expressed-by
    note: "Activated CD4⁺ T helper cells co-produce IL-6 with TGF-β to drive Th17 differentiation in an autocrine/paracrine loop."
  - target: 01-human/07-system/immune-system
    relation: expressed-by
    note: "IL-6 is produced broadly across immune and non-immune cells (fibroblasts, endothelial cells, adipocytes, osteoblasts) and is the central cytokine coordinator of the acute-phase response."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "IL-6 shapes adaptive immunity: promotes Th17 differentiation, suppresses Treg development, drives B cell differentiation to plasma cells, and activates effector T cells."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "IL-6 is the dominant inducer of hepatic acute-phase protein synthesis: CRP, fibrinogen, serum amyloid A, ferritin, hepcidin; concurrently suppresses albumin and transferrin."
  - target: 01-human/07-system/immune-system
    relation: modulated-by
    note: "IL-6 production is upregulated by pro-inflammatory signals (TNF, IL-1β, LPS) and downregulated by IL-10, glucocorticoids, and tocilizumab-mediated IL-6R blockade."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulated-by
    note: "TNF-α is a potent inducer of IL-6 transcription via NF-κB; the two cytokines act synergistically in driving the acute-phase response and cytokine storm."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: modulated-by
    note: "Corticosteroids suppress IL-6 transcription via GR-mediated transrepression of NF-κB and AP-1 at the IL-6 promoter; this mechanism underlies the mortality benefit of dexamethasone in severe COVID-19."
  - target: 01-human/04-cellular/macrophage
    relation: expressed-by
    evidence: tanaka-2016-il6-disease
    note: "M1-polarised macrophages are the primary cellular source of IL-6 after TLR4/LPS activation via NF-κB; macrophage-derived IL-6 drives the hepatic acute-phase response, Th17 differentiation, and cytokine storm."
  - target: 03-medicine/02-traditional/berberine
    relation: modulated-by
    evidence: tanaka-2016-il6-disease
    note: "Berberine inhibits IKKβ phosphorylation, blocking NF-κB nuclear translocation and reducing IL-6 transcription; NLRP3 inflammasome inhibition further decreases downstream IL-1β/IL-18. Clinically reduces CRP and IL-6 in metabolic syndrome."
  - target: 03-medicine/03-food/curcumin
    relation: modulated-by
    evidence: tanaka-2016-il6-disease
    note: "Curcumin's covalent IKKβ inhibition (Michael addition to Cys-179) and AP-1 suppression (via JNK inhibition) reduce IL-6 transcription; direct JAK/STAT3 inhibition attenuates downstream IL-6 signalling amplitude. RCTs show modest IL-6 reduction."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: modulated-by
    evidence: tanaka-2016-il6-disease
    note: "EPA/DHA competitively displace arachidonic acid from membrane phospholipids, shifting eicosanoid synthesis toward weaker PGE₃/LTB₅; reduced prostaglandin signalling lowers IL-6 production. SPMs (resolvins, protectins) actively resolve inflammation."
  - target: 01-human/03-molecular/stat3
    relation: modulates
    evidence: tanaka-2016-il6-disease
    note: "IL-6 trans-signals via sIL-6R→gp130 homodimerisation→JAK1/JAK2 activation→STAT3 Tyr705 phosphorylation; this is the dominant pathway for STAT3 activation in systemic inflammation, the acute-phase response, and cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: modulated-by
    evidence: tanaka-2016-il6-disease
    note: "NF-κB p65/p50 binds two κB sites in the IL-6 promoter and drives IL-6 transcription in macrophages and stromal cells; IκBα-mediated NF-κB cycling produces oscillating IL-6 pulses during LPS stimulation."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulated-by
    evidence: tanaka-2016-il6-disease
    note: "GR activation by glucocorticoids transrepresses IL-6 transcription via direct protein–protein interaction with NF-κB p65, competing for coactivators CBP/p300 and recruiting HDAC2 to the IL-6 promoter."
  - target: 01-human/02-atomic/sulfur
    relation: modulated-by
    note: "Modulated by Sulfur."
  - target: 01-human/04-cellular/osteoblast
    relation: modulated-by
    note: "Modulated by Osteoblast."
  - target: 01-human/04-cellular/osteoclast
    relation: modulated-by
    note: "Modulated by Osteoclast."
  - target: 01-human/04-cellular/fibroblast
    relation: modulated-by
    note: "Modulated by Fibroblast."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "IL-6 amplifies acute GvHD: conditioning damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis; IL-6 blockade with calcineurin inhibitors reduces GvHD incidence."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and CTGF; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score (mRSS) and ILD activity in dcSSc."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "IL-6 drives plasmablast expansion → AQP4-IgG production in NMOSD; satralizumab (anti-IL-6R; FDA Aug 2020) reduced ARR ~55% vs placebo (SAkuraStar); tocilizumab is used off-label for NMOSD; IL-6R blockade also reduces Th17-driven neuroinflammation."
---

# Interleukin-6

## Overview

Interleukin-6 (IL-6) is a **21 kDa pleiotropic cytokine** and one of the most versatile signaling molecules of the immune system. Originally identified in 1985 as B-cell stimulatory factor-2 (BSF-2) by Kishimoto's group [^kishimoto-1985-bsf2] — a factor that induced immunoglobulin secretion by activated B cells — IL-6 has since been recognized as a master coordinator of the **acute inflammatory response**, bridging innate and adaptive immunity while simultaneously acting on non-immune organs including the liver, bone, brain, and muscle.

IL-6 belongs to the **IL-6 cytokine family**, which also includes IL-11, IL-12, IL-27, leukemia inhibitory factor (LIF), oncostatin M (OSM), and ciliary neurotrophic factor (CNTF). All family members signal through the shared signal transducer **gp130** (IL6ST, CD130), explaining their overlapping biological effects and providing a rationale for broad-spectrum blockade strategies.

The clinical importance of IL-6 became dramatically apparent during the **COVID-19 pandemic**, where cytokine storm — characterized by markedly elevated IL-6, IL-1β, and TNF — drove ARDS and multi-organ failure in critically ill patients. The anti-IL-6 receptor monoclonal antibody **tocilizumab** subsequently demonstrated mortality benefit in ICU patients, validating IL-6 as a therapeutic target in hyperinflammatory states [^stone-2017-gca-tocilizumab].

## Structure

### Protein architecture

IL-6 is a **4-helix bundle cytokine** — the canonical topology of the IL-6 family and many hematopoietic cytokines. The four anti-parallel α-helices (A–D) are connected by three loops (AB, BC, CD), with the loop regions contributing to receptor binding specificity. The mature protein (after signal peptide cleavage) is 184 amino acids; the molecular weight of ~21 kDa reflects N- and O-linked glycosylation that is important for biological activity and half-life.

### Receptor complex

IL-6 signaling is initiated by formation of a hexameric signaling complex:

| Component | Gene | Role |
|:---|:---|:---|
| **IL-6** | *IL6* | Cytokine ligand |
| **IL-6Rα (mIL-6R)** | *IL6R* | Ligand-binding α subunit; membrane-anchored on hepatocytes, leukocytes, and some epithelial cells |
| **gp130 (IL6ST)** | *IL6ST* | Signal-transducing β subunit; ubiquitously expressed; shared with all IL-6 family members |

Two IL-6 molecules bind two IL-6Rα/gp130 pairs → **hexameric complex** (2:2:2 stoichiometry) → gp130 dimerization → intracellular signaling cascade.

### Classical vs. trans-signaling

A critical feature of IL-6 biology is **soluble IL-6Rα (sIL-6R)**, generated by proteolytic shedding (ADAM10/17) or alternative splicing:

- **Classical signaling**: IL-6 binds membrane IL-6Rα (mIL-6R) on cells that express it (mainly hepatocytes, neutrophils, monocytes, some lymphocytes) → gp130 homodimerization → JAK/STAT3
- **Trans-signaling**: IL-6 + sIL-6R form a complex → binds gp130 on cells lacking mIL-6R (most non-immune cells: endothelium, smooth muscle, neurons, epithelium) → dramatically expands IL-6 target cell range

Trans-signaling is largely **pro-inflammatory** and is the dominant mode in chronic inflammatory disease; sgp130 (soluble gp130) acts as a natural decoy receptor selectively inhibiting trans-signaling. This distinction has therapeutic implications: IL-6R blockade (tocilizumab) inhibits both modes, while sgp130Fc constructs (olamkicept) selectively block only trans-signaling.

## Function

### Acute-phase response

IL-6 is the **primary inducer of the hepatic acute-phase response** — the rapid reprogramming of liver protein secretion that occurs within hours of infection or injury. Hepatocytes express high mIL-6R and respond robustly:

**Positive acute-phase proteins** (IL-6 induces):
- **C-reactive protein (CRP)** — rises from <1 mg/L to >100–200 mg/L within 24–48 h; opsonizes bacteria, activates complement
- **Fibrinogen** — rises 2–4× baseline; contributes to ESR elevation
- **Serum amyloid A (SAA)** — rises 1000×; apo-lipoprotein with antimicrobial activity
- **Ferritin** — sequesters iron from pathogens; extreme elevation (hyperferritinemia) is a hallmark of cytokine storm and MAS
- **Hepcidin** — antimicrobial peptide; reduces circulating iron (→ anemia of inflammation)

**Negative acute-phase proteins** (IL-6 suppresses):
- **Albumin** — falls (dilutional effect plus suppressed synthesis)
- **Transferrin** — falls (reduces iron availability)

### Adaptive immune regulation

IL-6 bridges innate activation to adaptive immunity responses:

- **Th17 differentiation**: IL-6 + TGF-β → phospho-STAT3 → RORγt transcription factor → Th17 cells (IL-17, IL-22 producing). IL-6 is essential for Th17 commitment; in its absence (with TGF-β alone), Foxp3⁺ **Tregs** develop instead. This Th17/Treg balance is pivotal in autoimmune disease.
- **B cell terminal differentiation**: IL-6 drives differentiation of activated B cells to plasma cells (hence the original BSF-2 designation); combined IL-6 + IL-21 is the dominant Tfh-provided signal for plasmablast generation in germinal centers.
- **T cell survival and effector function**: IL-6 promotes survival of activated effector T cells and enhances their proliferative capacity; in tumor microenvironments, this can sustain anti-tumor immunity (or, in chronic inflammation, drive immunopathology).

### Metabolic and systemic effects

Beyond immunity, IL-6 has significant **pleiotropic endocrine-like effects**:
- **Skeletal muscle**: during exercise, muscle-derived IL-6 (myokine) is released in enormous quantities, acting as an energy sensor to promote hepatic glucose production and lipolysis — a physiological role distinct from inflammatory IL-6
- **Bone**: IL-6 + sIL-6R promotes osteoclast differentiation → bone resorption; relevant in RA joint destruction and osteoporosis
- **Hematopoiesis**: IL-6 is a growth factor for hematopoietic progenitors; drives thrombocytosis (↑ thrombopoietin, megakaryocyte maturation) during inflammation
- **Brain**: IL-6 produced by glia mediates neuroinflammation; crosses the BBB via trans-signaling; contributes to fever (via prostaglandin E2 in the preoptic area), fatigue, and depression-like behavior ("sickness behavior")
- **Metabolic syndrome**: chronic low-grade IL-6 elevation from visceral adipose tissue macrophages drives hepatic insulin resistance and is a mechanistic link between obesity and T2DM

## Mechanism

### JAK-STAT3 signaling cascade

The canonical IL-6 signaling pathway proceeds through JAK kinases and STAT3:

1. IL-6/(m or s)IL-6R complex binds and dimerizes two gp130 chains
2. **JAK1** (constitutively associated with gp130 Box1/Box2 motifs) and **JAK2/TYK2** trans-phosphorylate each other → activated JAK1/2 phosphorylate tyrosine residues (Y767, Y814, Y905, Y915) on gp130 cytoplasmic tail
3. **STAT3** is recruited via its SH2 domain to phospho-tyrosine docking sites on gp130 → STAT3 is phosphorylated at Tyr705 by JAK1
4. Phospho-STAT3 dimerizes → translocates to nucleus → binds STAT-response elements → transcriptional activation of target genes: *CRP*, *FGA/FGB/FGG* (fibrinogen), *SOCS3*, *BCL2*, *MCL1*, *MYC*, *VEGF*, and many others

**SOCS3** (suppressor of cytokine signaling 3) is a STAT3 target gene that feeds back to inhibit JAK1/JAK2 — the primary negative regulator of IL-6 signaling.

### Non-canonical IL-6 signaling

gp130 also activates:
- **RAS/MAPK/ERK pathway** via SHP2 (Grb2-Sos scaffold) — promotes proliferation and cell survival, relevant in myeloma and hepatocellular carcinoma
- **PI3K/AKT** — promotes cell survival; activated via JAK-mediated IRS-1 phosphorylation

### Therapeutic inhibition

**Tocilizumab** (RoActemra/Actemra) is a humanized anti-IL-6R IgG1 monoclonal antibody that blocks both mIL-6R and sIL-6R. Binding IL-6Rα prevents IL-6 from engaging gp130 → complete blockade of downstream JAK/STAT3 signaling. **Sarilumab** is a second anti-IL-6R mAb with higher affinity. **Siltuximab** directly binds IL-6 (not the receptor).

**JAK inhibitors** (tofacitinib, baricitinib, upadacitinib) block JAK1/JAK2/TYK2 downstream of multiple cytokine receptors including gp130, providing broader (but less selective) anti-inflammatory effects.

## Connections

- `expressed-by` → **macrophage** — primary producers in infection/injury (forward ref; entry pending)
- `expressed-by` → **t-helper-cell** — co-produces IL-6 for Th17 differentiation (forward ref; entry pending)
- `expressed-by` → **[immune-system](../../07-system/immune-system/README.md)** — broad cellular sources including fibroblasts, endothelium, adipocytes
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — Th17/Treg balance, plasma cell differentiation, effector T cell survival
- `modulates` → **[liver](../../06-organ/liver/README.md)** — acute-phase response induction: CRP, fibrinogen, SAA, ferritin, hepcidin
- `modulated-by` → **[immune-system](../../07-system/immune-system/README.md)** — upstream activators: TNF, IL-1β, LPS; suppressors: IL-10, glucocorticoids, tocilizumab
- `connects-to` → **[GvHD](../../07-system/gvhd/README.md)** — IL-6 amplifies acute GvHD: conditioning damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis; IL-6 blockade with calcineurin inhibitors reduces GvHD incidence.
- `connects-to` → **[Systemic Sclerosis](../../07-system/systemic-sclerosis/README.md)** — IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and CTGF; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score (mRSS) and ILD activity in dcSSc.
- `connects-to` → **[NMOSD](../../07-system/nmo/README.md)** — IL-6 drives plasmablast expansion → AQP4-IgG production in NMOSD; satralizumab (anti-IL-6R; FDA Aug 2020) reduced ARR ~55% vs placebo (SAkuraStar); tocilizumab used off-label; IL-6R blockade reduces Th17-driven neuroinflammation.

## Pathology

| Disease | IL-6 role | Therapeutic implication |
|:---|:---|:---|
| **Rheumatoid arthritis** | Synovial fibroblasts + macrophages produce IL-6 → STAT3-driven synovitis, joint destruction, systemic inflammation | Tocilizumab; sarilumab (IL-6R blockers); JAK inhibitors |
| **Giant cell arteritis (GCA)** | IL-6-driven granulomatous vasculitis; elevated serum IL-6 correlates with disease activity | Tocilizumab reduces steroid exposure and relapse rate [^stone-2017-gca-tocilizumab] |
| **COVID-19 cytokine storm** | Markedly elevated IL-6 (+ IL-1β, TNF, IL-8) → ARDS, endothelial injury, multi-organ failure | Tocilizumab + dexamethasone reduces ICU mortality |
| **Cytokine release syndrome (CRS)** | CAR-T/BiTE therapy triggers massive T cell IL-6 production → fever, hypotension, ARDS | Tocilizumab first-line treatment; graded by ASTCT criteria |
| **Castleman disease** | IL-6-producing plasmacytoid dendritic cell neoplasm (iMCD) | Siltuximab (direct IL-6 blockade); tocilizumab |
| **Multiple myeloma** | IL-6/STAT3 → plasma cell proliferation, MCL-1 survival, angiogenesis | Investigational anti-IL-6; indirect via proteasome inhibitors |
| **Cancer (various)** | IL-6/JAK/STAT3 → proliferation, survival, angiogenesis (HCC, CRC, breast, ovarian) | JAK inhibitors in clinical trials |
| **Metabolic syndrome / T2DM** | Visceral adipose IL-6 → hepatic insulin resistance, NAFLD, systemic inflammation | Lifestyle; metformin suppresses IL-6 partly via AMPK |
| **Depression / inflammaging** | Elevated IL-6 in depression, aging; cytokine-mediated "sickness behavior" | Anti-inflammatory strategies; exercise (IL-6 myokine paradox) |

[^kishimoto-1985-bsf2]: Hirano T, Yasukawa K, Harada H, et al. Complementary DNA for a novel human interleukin (BSF-2) that induces B lymphocytes to produce immunoglobulin. *Nature.* 1986;324(6092):73-6. [PubMed 3920967](https://pubmed.ncbi.nlm.nih.gov/3920967/)
[^tanaka-2016-il6-disease]: Tanaka T, Narazaki M, Kishimoto T. Interleukin-6 in disease: biology, pathogenesis and targeted therapy. *Nat Rev Immunol.* 2016. [doi:10.1038/nri.2016.43](https://doi.org/10.1038/nri.2016.43)
[^stone-2017-gca-tocilizumab]: Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. *N Engl J Med.* 2017;377(4):317-28. [doi:10.1056/NEJMoa1607948](https://doi.org/10.1056/NEJMoa1607948)
