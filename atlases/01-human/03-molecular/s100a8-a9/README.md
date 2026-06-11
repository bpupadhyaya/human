---
schema: human-scale-entry/v1
id: s100a8-a9
name: S100A8/A9
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "S100A8/A9 (calprotectin) is a neutrophil alarmin activating TLR4/RAGE → NF-κB and recruiting myeloid cells; fecal calprotectin is the gold-standard non-invasive biomarker of mucosal inflammation in IBD; serum S100A8/A9 (MRP8/14) is elevated in RA, sepsis, and COVID-19."
aliases: ["S100A8", "S100A9", "calprotectin", "MRP8", "MRP14", "MRP8/14", "S100A8/A9", "fecal calprotectin", "alarmin", "DAMP"]
cross_links:
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "S100A8/A9 → TLR4/RAGE → NF-κB → NLRP3 gene transcription (priming signal); S100A9 also activates NLRP3 assembly via mitochondrial ROS; IL-1β released by NLRP3 → further myeloid S100A8/A9 secretion — a positive feedback loop amplifying sterile inflammation."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "S100A8/A9 binds RAGE at μM concentrations → DIAPH1 → Rac1/Cdc42 → cell migration; in cancer, tumor RAGE activated by S100A8/A9 from MDSCs promotes immunosuppression and metastasis; RAGE blockade reduces tumor-promoting S100A8/A9 signaling in solid tumors."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Serum MRP8/14 (S100A8/A9) correlates with RA disease activity (DAS28) and predicts anti-TNF response; synovial fluid S100A8/A9 is 100-1000× serum levels; S100A8/A9 → TLR4 on synoviocytes → TNF and IL-6 → joint inflammation and cartilage destruction."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "S100A8/A9 → TLR4/RAGE → NF-κB → IL-6, TNF-α, IL-1β; IL-6 is a major downstream effector of S100A8/A9 signaling; elevated S100A8/A9 and IL-6 co-mark RA disease activity; in COVID-19, S100A8/A9-driven IL-6 cascade amplifies cytokine storm → ICU admission and mortality."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "S100A8/A9 is the primary neutrophil cytosolic protein (>60% of cytosol); neutrophil NETosis and necrosis release calprotectin into mucosal secretions → fecal calprotectin reflects gut neutrophilia; S100A8/A9 also activates adjacent neutrophils via TLR4 — autocrine amplification."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "S100A8/A9 among the most elevated plasma proteins in severe COVID-19 (up to 100× normal); SARS-CoV-2 → massive monocyte-neutrophil activation → S100A8/A9 → TLR4/RAGE → NF-κB → cytokine storm; serum S100A8/A9 correlates with ICU admission and 30-day mortality."
sources:
  - id: foell-2007-s100-review
    type: peer-reviewed
    cite: "Foell D, Wittkowski H, Vogl T, Roth J. S100 proteins expressed in phagocytes: a novel group of damage-associated molecular pattern molecules. J Leukoc Biol. 2007;81(1):28-37."
    doi: "10.1189/jlb.0306170"
    pmid: "16943388"
    url: "https://doi.org/10.1189/jlb.0306170"
  - id: tibble-2002-fecal-calprotectin
    type: peer-reviewed
    cite: "Tibble JA, Sigthorsson G, Bridger S, Fagerhol MK, Bjarnason I. Surrogate markers of intestinal inflammation are predictive of relapse in patients with inflammatory bowel disease. Gastroenterology. 2000;119(1):15-22."
    doi: "10.1053/gast.2000.8523"
    pmid: "10889150"
    url: "https://doi.org/10.1053/gast.2000.8523"
---

# S100A8/A9

## Overview

**S100A8/A9 (calprotectin)** is the heterodimeric complex of **S100A8** (MRP8, calgranulin-A; *S100A8* gene, chromosome 1q21.3; 11 kDa) and **S100A9** (MRP14, calgranulin-B; *S100A9* gene, chromosome 1q21.3; 13 kDa), two Ca²⁺- and Zn²⁺-binding proteins of the S100 family. Together as a non-covalent heterodimer (24 kDa), they form the most abundant cytosolic protein in **neutrophils** — comprising >60% of the neutrophil cytosol — and are constitutively expressed in monocytes and activated macrophages.

Calprotectin was discovered in the 1980s as an abundant granulocyte protein with antimicrobial activity. It is now recognized as a **multi-functional alarmin (DAMP)** with three overlapping roles:
1. **Antimicrobial effector** — chelates essential metals (Zn²⁺, Mn²⁺, Fe²⁺) from invading microorganisms → nutritional immunity
2. **Pro-inflammatory DAMP** — activates TLR4 and RAGE on innate immune cells → NF-κB → cytokine storm amplification
3. **Clinical biomarker** — released abundantly from activated neutrophils into mucosal secretions and blood → measurable surrogate of neutrophilic inflammation

**Clinical significance:**
- **Fecal calprotectin (FC):** The standard non-invasive stool marker for mucosal inflammation in IBD — widely used to distinguish IBD from IBS, assess endoscopic remission, predict relapse, and monitor biologic therapy response [^tibble-2002-fecal-calprotectin]
- **Serum MRP8/14 (S100A8/A9):** Biomarker of systemic inflammatory disease (RA, SLE, JIA, vasculitis); dramatically elevated in COVID-19 cytokine storm (one of the top upregulated proteins in severe COVID-19 plasma proteomics)
- **Cancer:** MDSCs (myeloid-derived suppressor cells) in the tumor microenvironment express high S100A8/A9 → promote immune evasion; tumor RAGE activation drives migration and metastasis

**S100 family context:**
- 25 S100 family members (S100A1–S100A16, S100B, S100G, S100P, S100Z)
- All have two EF-hand Ca²⁺-binding domains; most dimerize; some (like calprotectin) form higher-order oligomers
- Disease-associated: S100B (CNS injury, Alzheimer's), S100A4 (metastasis promoter), S100A7 (psoriasis, psoriasin), S100A12 (Kawasaki disease, juvenile arthritis)

## Structure

**S100A8 (11 kDa; 87 aa; MRP8):**
- Two EF-hand motifs: N-terminal pseudo-EF-hand (low Ca²⁺ affinity, ~Kd 0.5 mM) + C-terminal canonical EF-hand (high Ca²⁺ affinity, ~Kd 50 μM)
- Helix-loop-helix topology; forms a compact two-helix bundle
- Ca²⁺ binding induces conformational change → exposes hydrophobic surface → promotes S100A8/A9 heterodimerization

**S100A9 (13 kDa; 114 aa; MRP14):**
- Same EF-hand topology; C-terminal extension unique to S100A9
- Zn²⁺ binding site at the S100A8/A9 interface: each heterodimer contains two Zn²⁺ sites formed by His17 and Asp30 of S100A8, His91 and His95 of S100A9 — this Zn²⁺ coordination is critical for the high-affinity antimicrobial metal sequestration

**Calprotectin heterodimer and higher-order assembly:**
- S100A8/A9 heterodimer (2:2 tetramers at low concentrations)
- At inflammatory concentrations (>1 μM), forms **(S100A8/A9)₃ hexamers** with three Zn²⁺ coordination sites → higher-affinity Zn²⁺ chelation than dimers → explains why calprotectin-rich pus is growth-inhibitory for metal-requiring pathogens
- Mn²⁺ binding at the hexameric interface: calprotectin is one of the few mammalian proteins capable of Mn²⁺ sequestration — critical for *Staphylococcus aureus*, *Klebsiella*, and *Acinetobacter* inhibition

**Secretion:**
- No classical signal peptide → secreted by **non-classical pathways**:
  1. **Pyroptosis** (gasdermin D pores → NLRP3-activated cells)
  2. **NETosis** (neutrophil extracellular traps contain high calprotectin)
  3. **Exocytosis** from specific granules
  4. **Membrane microvesicle** shedding
- Stability: calprotectin is exceptionally stable — resists intestinal proteolysis, is stable at room temperature for 3–7 days in stool → enables fecal biomarker use

## Function

**Antimicrobial activity — nutritional immunity:**
- S100A8/A9 chelates Zn²⁺ (Kd ~25 nM in hexameric form) and Mn²⁺ from bacterial growth media → inhibits metal-dependent enzyme activity (metalloproteinases, SOD, urease, ribonucleotide reductase)
- Effective against: *S. aureus* (Zn²⁺), *Streptococcus pneumoniae* (Mn²⁺), *Acinetobacter baumannii* (Mn²⁺/Zn²⁺), *Candida* species (Zn²⁺/Fe²⁺)
- In abscess formation: calprotectin-rich neutrophil pus creates a Zn/Mn-depleted microenvironment → limits pathogen growth and proteolysis

**TLR4-dependent innate immune activation:**
- Extracellular calprotectin → TLR4 (on monocytes, macrophages, endothelial cells) → MyD88 → IRAK4 → TRAF6 → NF-κB → IL-6, TNF-α, IL-12, IL-1β
- TLR4 activation by S100A8/A9 requires the S100A9 C-terminal tail (the RAGE-binding site and TLR4-recognition domain overlap)
- This autocrine/paracrine amplification loop is why S100A8/A9 is so dramatically elevated in severe bacterial sepsis and COVID-19

**RAGE-dependent signaling:**
- S100A8/A9 → RAGE at μM concentrations (EC50 ~1–5 μM; lower affinity than AGEs, higher than S100B for the CRD) → DIAPH1 → Rho GTPases → cell migration and invasion
- In tumor stroma: MDSC-derived S100A8/A9 → tumor cell RAGE → ERK and Akt → proliferation, invasion, and EMT; RAGE also activates NF-κB → survival signaling in KRAS-mutant tumors
- S100A8/A9 → RAGE on endothelium → upregulates ICAM-1, VCAM-1 → neutrophil transendothelial migration → amplifies mucosal neutrophilia in IBD

**NLRP3 inflammasome connection:**
- S100A8/A9 → TLR4/RAGE → NF-κB → provides **priming signal** for NLRP3 gene transcription (NLRP3, IL-1β, pro-caspase-1)
- Additionally, S100A9 can provide the **activation (second) signal**: S100A9 oligomers → mitochondrial ROS → potassium efflux → NLRP3 assembly → caspase-1 activation → IL-1β/IL-18 secretion
- NLRP3-released IL-1β → stimulates myeloid cells → more S100A8/A9 secretion (positive feedback in chronic gut inflammation, RA, and gout)

## Mechanism

**Fecal calprotectin in IBD monitoring [^tibble-2002-fecal-calprotectin]:**

**Biological basis:**
1. Active IBD mucosal inflammation → neutrophil transmigration through the intestinal epithelium
2. Neutrophils release calprotectin (constitutive 60% of cytosol) as they undergo NETosis and necrosis in the gut lumen
3. Calprotectin mixes with stool — stable at room temperature for up to 7 days
4. ELISA (most common) or lateral flow immunoassay quantifies FC in μg/g stool

**Thresholds and clinical use:**
| FC level | Interpretation |
|---|---|
| <50 μg/g | Normal; IBD highly unlikely; favors IBS |
| 50–150 μg/g | Borderline; repeat in 4–6 weeks; consider colonoscopy |
| >150 μg/g | Mucosal inflammation likely; colonoscopy indicated |
| >250 μg/g | Active endoscopic disease; correlates with mucosal healing targets |
| >800–1000 μg/g | Severe mucosal inflammation; acute flare likely |

**Clinical applications:**
- **IBD vs. IBS differentiation:** FC <50 μg/g rules out active IBD with high sensitivity (~90%); avoids unnecessary colonoscopy (NPV 0.93-0.97)
- **Post-induction monitoring:** FC after 8–14 weeks of anti-TNF or anti-IL-23 therapy predicts endoscopic remission; FC <150 μg/g at week 14 correlates with CDEIS <4 in Crohn's disease
- **Relapse prediction:** Rising FC in asymptomatic IBD patients predicts clinical flare within 3 months (sensitivity ~80%); enables pre-emptive therapy adjustment
- **Post-surgery (Crohn's):** FC >100 μg/g at 6 months post-ileocolonic resection predicts anastomotic recurrence; guides endoscopic monitoring decisions

**Serum MRP8/14 in systemic inflammation:**
- RA: serum S100A8/A9 correlates with DAS28 and CRP; predicts anti-TNF response (responders have higher baseline MRP8/14 in some cohorts); ~6× normal values in active RA synovitis
- COVID-19: S100A8/A9 is among the most dramatically elevated plasma proteins in severe COVID-19 (up to 100× normal) — reflects massive monocyte/neutrophil activation; correlates with ICU admission and mortality
- Sepsis: serum calprotectin >13 mg/L (day 1) predicts 30-day mortality with AUC 0.80; reflects neutrophil and monocyte activation burden beyond PCT or CRP

## Connections

- `connects-to` → **[Inflammatory Bowel Disease](../../07-system/inflammatory-bowel-disease/README.md)** — Mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — S100A8/A9 → TLR4/RAGE → NF-κB → NLRP3 priming; S100A9 also activates NLRP3 assembly via mitochondrial ROS; NLRP3-released IL-1β → further myeloid S100A8/A9 secretion — positive feedback amplifying sterile inflammation.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — S100A8/A9 binds RAGE at μM concentrations → DIAPH1 → Rac1/Cdc42 → cell migration; in cancer, MDSC-derived S100A8/A9 activates tumor RAGE → immunosuppression and metastasis; RAGE blockade reduces tumor-promoting S100A8/A9 signaling.
- `connects-to` → **[Rheumatoid Arthritis](../../07-system/rheumatoid-arthritis/README.md)** — Serum MRP8/14 correlates with RA disease activity (DAS28) and predicts anti-TNF response; synovial fluid S100A8/A9 is 100-1000× serum; S100A8/A9 → TLR4 on synoviocytes → TNF and IL-6 → joint inflammation and cartilage destruction.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — S100A8/A9 → TLR4/RAGE → NF-κB → IL-6, TNF-α, IL-1β; IL-6 is a major downstream effector of S100A8/A9 signaling; elevated S100A8/A9 and IL-6 co-mark RA disease activity; in COVID-19, S100A8/A9-driven IL-6 cascade amplifies cytokine storm → ICU admission and mortality.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — S100A8/A9 is the primary neutrophil cytosolic protein (>60% of cytosol); neutrophil NETosis and necrosis release calprotectin into mucosal secretions → fecal calprotectin reflects gut neutrophilia; S100A8/A9 also activates adjacent neutrophils via TLR4 — autocrine amplification.
- `connects-to` → **[COVID-19 Disease](../../07-system/covid-19-disease/README.md)** — S100A8/A9 among the most elevated plasma proteins in severe COVID-19 (up to 100× normal); SARS-CoV-2 → massive monocyte-neutrophil activation → S100A8/A9 → TLR4/RAGE → NF-κB → cytokine storm; serum S100A8/A9 correlates with ICU admission and 30-day mortality.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^foell-2007-s100-review]: Foell D, Wittkowski H, Vogl T, Roth J. S100 proteins expressed in phagocytes: a novel group of damage-associated molecular pattern molecules. *J Leukoc Biol.* 2007;81(1):28-37. [doi:10.1189/jlb.0306170](https://doi.org/10.1189/jlb.0306170) · [PubMed 16943388](https://pubmed.ncbi.nlm.nih.gov/16943388/)
[^tibble-2002-fecal-calprotectin]: Tibble JA, Sigthorsson G, Bridger S, Fagerhol MK, Bjarnason I. Surrogate markers of intestinal inflammation are predictive of relapse in patients with inflammatory bowel disease. *Gastroenterology.* 2000;119(1):15-22. [doi:10.1053/gast.2000.8523](https://doi.org/10.1053/gast.2000.8523) · [PubMed 10889150](https://pubmed.ncbi.nlm.nih.gov/10889150/)
