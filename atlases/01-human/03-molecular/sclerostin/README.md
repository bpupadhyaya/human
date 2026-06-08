---
schema: human-scale-entry/v1
id: sclerostin
name: Sclerostin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Sclerostin (SOST, chr17q21.31) is an osteocyte-secreted Wnt antagonist; binds LRP5/LRP6 → blocks Wnt/β-catenin → inhibits osteoblast bone formation; romosozumab (anti-sclerostin) has dual anabolic+antiresorptive action: 73% RRR vertebral fractures (FRAME trial)."
aliases: ["SOST", "sclerostin", "osteocyte Wnt inhibitor", "LRP5/6 antagonist", "BMP antagonist"]
cross_links:
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Sclerostin from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → bone loss; romosozumab (anti-sclerostin, 210 mg SC Q1M × 12 months) derepresses Wnt → bone formation surge; FRAME: 73% RRR vertebral fractures; ARCH: 48% fewer vertebral vs. alendronate."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Romosozumab (anti-sclerostin) derepresses osteoblast Wnt → increased OPG secretion → reduced RANKL signaling → modest antiresorptive effect in addition to its dominant anabolic action; sclerostin blockade is the only approved therapy combining bone formation and antiresorption."
sources:
  - id: li-2005-sost-cloning
    type: peer-reviewed
    cite: "Li X, Zhang Y, Kang H, et al. Sclerostin binds to LRP5/6 and antagonizes canonical Wnt signaling. J Biol Chem. 2005;280(20):19883-19887."
    doi: "10.1074/jbc.M413274200"
    pmid: "15778503"
    url: "https://doi.org/10.1074/jbc.M413274200"
  - id: cosman-2016-romosozumab-frame
    type: peer-reviewed
    cite: "Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. N Engl J Med. 2016;375(16):1532-1543."
    doi: "10.1056/NEJMoa1607948"
    pmid: "27641143"
    url: "https://doi.org/10.1056/NEJMoa1607948"
  - id: saag-2017-romosozumab-arch
    type: peer-reviewed
    cite: "Saag KG, Petersen J, Brandi ML, et al. Romosozumab or alendronate for fracture prevention in women with osteoporosis. N Engl J Med. 2017;377(15):1417-1427."
    doi: "10.1056/NEJMoa1708322"
    pmid: "28892457"
    url: "https://doi.org/10.1056/NEJMoa1708322"
---

# Sclerostin

## Overview

**Sclerostin** (gene *SOST*, chromosome 17q21.31) is a **secreted glycoprotein** produced almost exclusively by mature **osteocytes** — the long-lived, mechanosensing bone cells embedded within mineralized matrix. It functions as a **potent inhibitor of canonical Wnt/β-catenin signaling** in osteoblasts by competitively binding to the co-receptors **LRP5 and LRP6**, which are essential for Wnt ligand-receptor complex assembly. By blocking Wnt signal transduction, sclerostin suppresses osteoblast differentiation, proliferation, and survival — making it the **primary molecular brake on bone formation** [^li-2005-sost-cloning].

The physiological importance of sclerostin was established by two rare genetic disorders:
- **Sclerosteosis** (SOST loss-of-function mutations): Autosomal recessive; homozygous SOST null → complete absence of sclerostin → unrestrained Wnt/β-catenin in osteoblasts → progressive bone overgrowth throughout life → massive cortical thickening, cranial nerve entrapment (facial palsy, hearing loss), and facial distortion
- **Van Buchem disease** (regulatory deletion 52 kb downstream of SOST): Reduced SOST transcription (not complete null); milder phenotype; enlarged mandible, calvarial thickening, progressive bone density increase

These natural experiments definitively confirmed that sclerostin suppression → bone formation increase — the therapeutic rationale for **romosozumab** (Evenity; anti-sclerostin monoclonal antibody, Amgen/UCB; approved FDA April 2019, EMA January 2020).

Beyond Wnt antagonism, sclerostin also inhibits **BMP (bone morphogenetic protein) signaling** through its DAN/gremlin-family cysteine-knot domain, though LRP5/6 binding appears to be the dominant mechanism in bone physiology.

## Structure

**SOST gene and protein:**
- Chromosome 17q21.31; single exon (exon 2 encodes the mature protein); 22.7 kb; transcriptional regulation by MEF2C (mechanical-loading transducer) and androgen receptor (AR) in osteocytes → explains why mechanical loading and testosterone suppress sclerostin
- **Protein:** 213 aa; N-terminal signal peptide (aa 1–23) → 190-aa mature secreted form; 4 disulfide bonds; **DAN (differential screening-selected gene aberrative in neuroblastoma) / gremlin superfamily** — characterized by conserved cysteine-knot fold (TSP-1 domain); molecular weight ~22 kDa (apparent ~30 kDa due to glycosylation)
- **Cysteine-knot architecture:** Three antiparallel β-strands + two disulfide-linked loops; structural homology with TGF-β and BMP family proteins but opposite function (inhibitor rather than receptor ligand)
- **LRP5/LRP6 binding loop:** Central "loop 2" (aa 86–111) is the primary LRP5/6 interaction surface; contains YPLDLASSP binding motif (similar to DKK1 loop 2); this loop is flexible and adopts distinct conformations when bound vs. free

**Receptor binding mechanism:**
- **LRP5 and LRP6** are single-pass type I transmembrane co-receptors of the Wnt signaling complex; their extracellular domains contain four YWTD-type β-propeller domains and four EGF-like domains
- Sclerostin loop 2 binds **LRP5/6 β-propeller 1 (E1E2)** → sterically occludes the binding site for Wnt–Frizzled-LRP ternary complex formation → prevents Dishevelled recruitment → prevents Axin sequestration → GSK3β remains active → phosphorylates β-catenin → ubiquitination by β-TrCP E3 ligase → proteasomal degradation → no nuclear β-catenin transcription
- **Frizzled co-receptor** is NOT required for Wnt inhibition by sclerostin — sclerostin acts upstream at LRP5/6 before Wnt-Frizzled assembly
- Sclerostin has higher affinity for LRP6 (Kd ~1-3 nM) than LRP5; romosozumab binds the same loop 2 epitope as LRP6, preventing LRP5/6 interaction

**BMP antagonism:**
- Sclerostin's cysteine-knot domain allows it to weakly bind BMP ligands (BMP2, BMP4, BMP7) → mild BMP antagonism; BMP2 promotes RUNX2 → osteoblast differentiation; whether BMP antagonism contributes meaningfully to bone mass regulation in vivo is debated — LRP5/6 interaction appears dominant

**Romosozumab (Evenity) structure:**
- Fully human IgG2 monoclonal antibody (Amgen/UCB); binds sclerostin loop 2 epitope → blocks LRP5/6 binding; 210 mg SC Q1M (two 105 mg injections per monthly dose); approved for 12-month treatment course only (bone formation effect attenuates after 12 months due to compensatory OPG reduction)

## Function

**Bone formation regulation by sclerostin:**
- Osteocyte sclerostin production is the primary mechanism by which bone cells communicate systemic "enough bone" homeostatic signals to osteoblasts
- **Key regulators of sclerostin expression:**
  - **Mechanical loading (exercise)** → fluid shear stress → osteocyte primary cilia deflection → ATP release → purinergic signaling + prostaglandin E2 → MEF2C suppression → ↓SOST transcription → sclerostin ↓ → Wnt de-repression → bone formation at loaded sites (load-driven anabolic response)
  - **Immobilization, disuse, microgravity** → ↑sclerostin → bone loss; astronauts show rapid sclerostin rise during spaceflight
  - **PTH (intermittent)** → PTH1R on osteocytes → cAMP → PKA → sclerostin transcription suppression → contributes to anabolic effect of teriparatide (adds to direct osteoblast stimulation)
  - **Testosterone (androgen)** → AR on osteocytes → ↓SOST transcription; explains why hypogonadal men lose bone faster; androgen deprivation therapy (ADT) for prostate cancer → ↑sclerostin → bone loss → bisphosphonate/denosumab indicated
  - **Estrogen** → ↓sclerostin in osteocytes; one of the mechanisms by which estrogen protects bone; postmenopause → ↑sclerostin → ↑bone loss
  - **Glucocorticoids** → ↑sclerostin → contributes to glucocorticoid-induced osteoporosis (GIO); dual mechanism: also directly suppress osteoblast Wnt signaling via DKK-1 upregulation
  - **IL-6, oncostatin M (OSM)** → ↑sclerostin via STAT3; explains inflammatory bone loss in RA and myeloma

**Coupling signal function:**
- After each osteoclastic resorption cycle, TGF-β and IGF-1 released from resorbed bone matrix → recruit osteoblast precursors; simultaneously, osteoclasts produce ephrin-B2 (a contact signal to reverse-signal EphB4 on osteoblasts → ↓sclerostin locally → Wnt de-repression → osteoblast activation at the resorption pit); this bidirectional ephrin-Eph communication enables site-specific osteoblast recruitment

**Wnt target genes in osteoblasts (activated when sclerostin removed):**
- **RUNX2** → osteoblast master TF → osteocalcin, collagen I, alkaline phosphatase
- **SP7/Osterix** → bone sialoprotein, osteopontin
- **Cyclin D1** → osteoblast proliferation
- **OPG (TNFRSF11B)** → decoy receptor blocking RANKL → anti-osteoclastic; explains why romosozumab has an antiresorptive component — anabolic osteoblast stimulation → more OPG → less RANKL-driven osteoclastogenesis

## Mechanism

**Romosozumab — FRAME trial (2016) [^cosman-2016-romosozumab-frame]:**
- **Design:** 7,180 postmenopausal women with osteoporosis (T-score −2.5 to −3.5); romosozumab 210 mg SC Q1M vs. placebo × 12 months; then both groups crossed over to denosumab × 12 months
- **Bone formation markers (first month):** P1NP (N-terminal propeptide of type I procollagen, bone formation marker) +147% vs. placebo → peak anabolic effect; bone resorption marker CTX −54% at month 1 → mild antiresorptive effect; bone formation effect attenuates by 6-9 months but remains greater than placebo throughout
- **BMD (12 months):** +13.3% lumbar spine, +6.9% total hip vs. placebo — largest 12-month BMD gains of any approved osteoporosis therapy
- **Fracture outcomes (12 months romosozumab):** New vertebral fractures: 73% RRR (0.5% vs. 1.8%; p<0.001); clinical fractures: 36% RRR; non-vertebral: not significant at 12 months
- **Fracture outcomes (24 months — after denosumab):** Cumulative benefit maintained with subsequent antiresorptive
- **CV safety:** FRAME: no significant MACE imbalance vs. placebo (2 vs. 4 events per 1000 patient-years); but small numbers

**Romosozumab — ARCH trial (2017) [^saag-2017-romosozumab-arch]:**
- **Design:** 4,093 postmenopausal women at high fracture risk (prior vertebral fracture or femoral neck T-score ≤−2.5 + one clinical risk factor); romosozumab 210 mg Q1M × 12 months then alendronate, vs. alendronate throughout × 24 months
- **Vertebral fractures (24 months):** Romosozumab → alendronate: 48% fewer new vertebral fractures vs. alendronate alone (6.2% vs. 11.9%; p<0.001)
- **Hip fractures (24 months):** 38% RRR (HR 0.62; 95% CI 0.42–0.92)
- **Non-vertebral fractures:** 19% RRR (borderline significant)
- **CV MACE concern:** ARCH: non-significant increase in MACE with romosozumab vs. alendronate (2.5% vs. 1.9%); the comparator (alendronate) is cardioprotective, confounding the estimate; FDA added **Black Box Warning**: do not use romosozumab within 12 months of MI or stroke; avoid in patients with known CV disease; the CV signal was not confirmed in FRAME (placebo control)

**Anabolic-first paradigm:**
- "Anabolic-first then antiresorptive" sequences (romosozumab or teriparatide → bisphosphonate/denosumab) achieve greater BMD gains and fracture reduction than antiresorptive first
- After romosozumab 12 months: transition to antiresorptive (denosumab preferred for largest sustained BMD gains; bisphosphonate acceptable)
- Duration strictly limited to 12 monthly doses — after 12 months, compensatory homeostatic mechanisms (increased RANKL, attenuated P1NP response) reduce efficacy

**Sclerostin in other contexts:**
- **CKD-MBD:** Dialysis patients have elevated sclerostin (impaired renal clearance); contributing to low-turnover adynamic bone disease; romosozumab may increase CV risk in CKD — not approved for use in CKD
- **Diabetes:** T2DM → elevated sclerostin (mechanisms unclear — hyperglycemia, AGEs on osteocyte lacuno-canalicular network); contributes to impaired bone quality in diabetes despite normal/high BMD
- **Multiple myeloma:** MM-secreted DKK1 (a different LRP5/6 antagonist) + sclerostin from myeloma-associated osteocyte suppression → combined Wnt blockade → osteoblast suppression → bone lesions; targeting DKK1 is under clinical study in MM bone disease

## Connections

RANKL (TNFSF11) from osteoblasts/T cells → RANK on osteoclast precursors → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG decoy ratio governs bone mass; denosumab (anti-RANKL) → 68% vertebral and 40% hip fracture risk reduction (FREEDOM trial).

- `connects-to` → **[Osteoporosis](../../07-system/osteoporosis/README.md)** — Sclerostin from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → bone loss; romosozumab (anti-sclerostin, 210 mg SC Q1M × 12 months) derepresses Wnt → bone formation surge; FRAME: 73% RRR vertebral fractures; ARCH: 48% fewer vertebral vs. alendronate.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Romosozumab (anti-sclerostin) derepresses osteoblast Wnt → increased OPG secretion → reduced RANKL signaling → modest antiresorptive effect in addition to its dominant anabolic action; sclerostin blockade is the only approved therapy combining bone formation and antiresorption.

[^li-2005-sost-cloning]: Li X, Zhang Y, Kang H, et al. Sclerostin binds to LRP5/6 and antagonizes canonical Wnt signaling. *J Biol Chem.* 2005;280(20):19883-19887. [doi:10.1074/jbc.M413274200](https://doi.org/10.1074/jbc.M413274200) · [PubMed 15778503](https://pubmed.ncbi.nlm.nih.gov/15778503/)
[^cosman-2016-romosozumab-frame]: Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. *N Engl J Med.* 2016;375(16):1532-1543. [doi:10.1056/NEJMoa1607948](https://doi.org/10.1056/NEJMoa1607948) · [PubMed 27641143](https://pubmed.ncbi.nlm.nih.gov/27641143/)
[^saag-2017-romosozumab-arch]: Saag KG, Petersen J, Brandi ML, et al. Romosozumab or alendronate for fracture prevention in women with osteoporosis. *N Engl J Med.* 2017;377(15):1417-1427. [doi:10.1056/NEJMoa1708322](https://doi.org/10.1056/NEJMoa1708322) · [PubMed 28892457](https://pubmed.ncbi.nlm.nih.gov/28892457/)
