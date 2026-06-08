---
schema: human-scale-entry/v1
id: adrenomedullin
name: Adrenomedullin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Adrenomedullin (ADM) is a 52-aa vasodilatory peptide from adrenal medulla and endothelium; CLR/RAMP2 → cAMP → NO → vasodilation and vascular barrier protection; mid-regional pro-ADM (MR-proADM) is a sepsis severity biomarker and guides antibiotic duration."
aliases: ["adrenomedullin", "ADM", "MR-proADM", "mid-regional pro-adrenomedullin", "CLR", "RAMP2", "RAMP3", "CGRP family"]
cross_links:
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "ADM rises dramatically in sepsis proportional to severity; vasodilation (CLR/RAMP2 → cAMP → vasodilation) contributes to distributive shock; MR-proADM predicts 28-day mortality with AUC >0.80 and guides antibiotic de-escalation in the ADAPT-sepsis trial."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "ADM is elevated in HF proportional to NYHA class and correlates with pulmonary artery pressure; exogenous ADM infusion reduces PVR and SVR in acute decompensated HF; MR-proADM independently predicts HF mortality beyond NT-proBNP."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "ADM → CLR/RAMP2 → Gs → cAMP → PKA → eNOS Ser1177 phosphorylation → NO production; NO mediates the vasodilatory arm of ADM signaling; endothelial NO also mediates ADM-induced vascular barrier protection via Rac1 → VE-cadherin stabilization."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "ADM and BNP are both endothelial/myocardial stress peptides upregulated in sepsis, heart failure, and cardiogenic shock; MR-proADM captures endothelial dysfunction (vascular compartment) while NT-proBNP reflects myocardial wall stress — complementary biomarkers."
sources:
  - id: kitamura-1993-adrenomedullin
    type: peer-reviewed
    cite: "Kitamura K, Kangawa K, Kawamoto M, et al. Adrenomedullin: a novel hypotensive peptide isolated from human pheochromocytoma. Biochem Biophys Res Commun. 1993;192(2):553-560."
    doi: "10.1006/bbrc.1993.1451"
    pmid: "8387282"
    url: "https://doi.org/10.1006/bbrc.1993.1451"
  - id: schuetz-2011-mradm-sepsis
    type: peer-reviewed
    cite: "Schuetz P, Wolbers M, Christ-Crain M, et al. Prohormones for prediction of adverse medical outcome in community-acquired pneumonia and lower respiratory tract infections. Crit Care. 2010;14(3):R106."
    doi: "10.1186/cc9055"
    pmid: "20529248"
    url: "https://doi.org/10.1186/cc9055"
---

# Adrenomedullin

## Overview

**Adrenomedullin (ADM)** is a **52-amino acid peptide** (gene *ADM*, chromosome 11p15.4) belonging to the **calcitonin gene-related peptide (CGRP) superfamily** — which also includes CGRP, calcitonin, amylin, and intermedin (adrenomedullin-2). It was discovered in 1993 by Kitamura et al. in extracts from human pheochromocytoma as a potent hypotensive agent [^kitamura-1993-adrenomedullin], making it one of the most recent members of this peptide hormone family to be characterized.

ADM is produced by **adrenal medullary chromaffin cells** (original source), **vascular endothelial cells** (the dominant systemic source), **vascular smooth muscle cells**, cardiomyocytes, pulmonary epithelium, and macrophages. Expression is induced by hypoxia (HIF-1α), cytokines (TNF-α, IL-1β, IL-6), LPS, shear stress, and oxidative stress — explaining why ADM is dramatically elevated in sepsis, heart failure, and pulmonary hypertension.

**Two key biological roles:**
1. **Vasodilator and vascular barrier protector**: ADM → CLR/RAMP2 receptor → Gs → cAMP → PKA + eNOS → vasodilation and NO production; simultaneously maintains endothelial barrier integrity via Rac1-GEF/VE-cadherin axis — a unique combination of vasodilation without barrier leak (distinct from most vasodilatory mediators)
2. **Stress biomarker via its stable precursor MR-proADM**: Mature ADM has a plasma half-life of ~22 minutes and is difficult to measure; **mid-regional pro-adrenomedullin (MR-proADM, residues 45–92 of pre-pro-ADM)** is the clinically measured stable surrogate — a superior sepsis and heart failure severity biomarker [^schuetz-2011-mradm-sepsis]

**Clinical context — sepsis and the vasodilatory paradox:**
In sepsis, TNF-α and IL-1β massively upregulate ADM in endothelial cells → systemic ADM levels rise 5–30× above normal → contributes to the vasodilatory distributive shock phenotype (low SVR, high CO with hypotension). Paradoxically, ADM's endothelial barrier-protective effect may limit capillary leak — making the overall net effect of ADM in sepsis complex: pro-vasodilatory yet partly protective of the microcirculation. MR-proADM >1.5 nmol/L at admission identifies high-risk sepsis patients requiring ICU-level care.

**CGRP superfamily context:**

| Peptide | Gene | Primary receptor | Primary action |
|---|---|---|---|
| CGRP (α/β) | CALCA/CALCB | CLR/RAMP1 | Vasodilation, migraine |
| Adrenomedullin (ADM) | ADM | CLR/RAMP2, CLR/RAMP3 | Vasodilation, barrier protection |
| Adrenomedullin-2/intermedin | ADM2 | CLR/RAMP2, CLR/RAMP3 | Vasodilation, anti-fibrotic |
| Calcitonin | CALCA (alt transcript) | CTR (CALCR) | Osteoclast inhibition |
| Amylin | IAPP | CTR/RAMP1/2/3 | Satiety, glucoregulation |

## Structure

**Pre-pro-ADM (185 aa) processing:**
**Signal peptide (1–21)** → cleaved → **Pro-ADM (164 aa)** → tissue-specific processing:
- **N-terminal pro-ADM (NTMAD, residues 1–21):** Vasoactive; poorly characterized in vivo
- **MR-proADM (residues 45–92):** The stable mid-regional fragment; not biologically active but mirrors ADM secretion kinetics; immunoassay target for clinical measurement
- **Mature ADM (residues 93–146, 52 aa):** The bioactive peptide
- **Adrenomedullin-G (PAMP-12/20):** C-terminal fragment; antimicrobial activity

**Mature ADM structure (52 aa):**
- Single disulfide bond: Cys16-Cys21 → constrains a 6-aa ring structure; essential for CLR receptor binding
- C-terminal amidation (Tyr52-NH₂): required for high-affinity receptor interaction (generated by PAM peptidylglycine amidating monooxygenase)
- N-terminal helix (residues 1–13): amphipathic α-helix; interacts with RAMP2 extracellular domain
- Structural homology with CGRP: both have a C-terminal amide and N-terminal disulfide ring — accounting for partial cross-reactivity at CLR receptors

**Receptor complex (Calcitonin Receptor-Like Receptor + RAMP):**
- **CLR (CALCRL):** 7-TM GPCR; the peptide-binding subunit; cannot traffic to the cell surface without RAMP chaperones
- **RAMP2:** Determines ADM1 receptor selectivity (CLR/RAMP2 = AM1 receptor; 10× higher affinity for ADM than CGRP)
- **RAMP3:** CLR/RAMP3 = AM2 receptor (binds both ADM and CGRP, lower affinity than AM1)
- **RAMP1:** CLR/RAMP1 = CGRP receptor (primary CGRP receptor; low ADM affinity)
- RAMPs are single-TM chaperone proteins that dictate ligand selectivity of CLR — a unique receptor pharmacology mechanism; RAMP2 knockout mice develop vascular defects (similar to ADM knockout) confirming AM1 as the critical ADM receptor in vivo

## Function

**Vascular smooth muscle (vasodilation):**
1. ADM → AM1 receptor (CLR/RAMP2) → Gs → adenylyl cyclase → ↑cAMP → PKA → MLCK inactivation (Ser19 phosphorylation) + MLCP activation → smooth muscle relaxation → vasodilation
2. ADM → Gs → cAMP → PKA → eNOS Ser1177 phosphorylation → ↑NO → guanylyl cyclase → cGMP → PKG → vasodilation (second arm)
3. Net: potent arteriolar vasodilation; reduces systemic vascular resistance and pulmonary vascular resistance

**Endothelial barrier protection (unique to ADM among vasodilators):**
- ADM → CLR/RAMP2 on endothelium → Gs/cAMP → Epac1 (guanine nucleotide exchange factor for Rap1) → Rac1 activation → lamellipodia formation → cortical actin ring → VE-cadherin junction stabilization → reduced paracellular permeability
- This is mechanistically distinct from the vasodilatory cAMP/PKA pathway — ADM simultaneously dilates vessels AND tightens the endothelial barrier
- Contrast with VEGF (vasodilator + barrier disruption) — ADM's barrier-protective effect makes it attractive for sepsis where capillary leak drives organ failure
- Anti-ADM antibody (adrecizumab/HAM8101): in septic shock preclinical models, neutralizing ADM paradoxically improves outcome by correcting excessive vasodilation — concept of "biased" ADM modulation

**Anti-inflammatory and anti-fibrotic:**
- ADM → cAMP → PKA → NF-κB inhibition (IκBα stabilization) → ↓TNF-α, IL-6, IL-1β secretion by macrophages
- ADM → ↑IL-10 (anti-inflammatory) via cAMP-dependent pathways
- In the kidney: ADM inhibits TGF-β1 → ↓mesangial matrix production → anti-fibrotic effect in CKD models
- In the lung: ADM reduces bleomycin-induced pulmonary fibrosis in rodent models

**Diuretic and natriuretic:**
- ADM → CLR/RAMP2 on renal tubules → cAMP → ↓Na+/K+-ATPase activity → natriuresis
- ADM → renal afferent arteriole dilation → ↑GFR
- These renal effects complement the cardiovascular vasodilation — ADM acts as a cardiorenal protective peptide in HF, countering RAAS/ADH-mediated Na+ and water retention

## Mechanism

**ADM in septic shock — vasodilation and the circuitry:**

1. **Sepsis trigger:** Gram-negative LPS or gram-positive lipoteichoic acid → TLR4/TLR2 → NF-κB → massive endothelial ADM transcription (>10× baseline within 2 hours)
2. **Systemic ADM release:** Endothelial cells throughout the vascular tree release mature ADM → plasma ADM rises 5–30× above normal
3. **AM1 receptor activation on VSMC:** Gs → cAMP → MLCK inactivation → arteriolar dilation → SVR falls → hypotension (distributive shock)
4. **Partial endothelial barrier protection:** Simultaneously, endothelial AM1 → Epac1 → Rac1 → VE-cadherin stabilization → partially restrains capillary leak (imperfect — severe sepsis still has massive leak)
5. **Biomarker application:** MR-proADM (stable pre-pro-ADM fragment) measured by Lumipulse/BRAHMS assay at ICU admission: >1.5 nmol/L → high mortality risk; guides sepsis triage and antibiotic duration (ADAPT-sepsis trial)

**MR-proADM in clinical practice:**
- **ADAPT-sepsis trial:** MR-proADM-guided antibiotic duration (de-escalate when MR-proADM falls) vs. PCT-guided → shorter antibiotic duration without increased mortality; establishes MR-proADM as a management tool, not just a prognostic biomarker
- **Sepsis triage:** MR-proADM + lactate + SOFA improves mortality prediction vs. any single marker; added to the Biomarker-Enhanced Triage (BET) strategies for ED sepsis
- **Combination biomarker strategy:** MR-proADM (vascular stress/endothelial dysfunction) + PCT (bacterial infection) + NT-proBNP (myocardial stress) + lactate (tissue hypoperfusion) — each captures a distinct sepsis pathophysiology domain

**ADM in heart failure:**
- Elevated HF ADM correlates with NYHA class, PAP, and PVR; independent predictor of mortality beyond NT-proBNP
- Exogenous ADM infusion (Phase 2 trials): reduces SVR, PVR, and PCWP in decompensated HF; improves cardiac index; vasodilation without reflex tachycardia (unlike most vasodilators) — attributed to ADM's partial sympatholytic effect
- Anti-ADM antibody trials (Adrenomed GmbH): AMY-101 trial in COVID-19 ARDS-like conditions; concept is to "rescue" excessive ADM-driven vasoplegia

## Connections

ADM rises dramatically in sepsis proportional to severity; vasodilation (CLR/RAMP2 → cAMP → vasodilation) contributes to distributive shock; MR-proADM predicts 28-day mortality with AUC >0.80 and guides antibiotic de-escalation in the ADAPT-sepsis trial.

ADM is elevated in HF proportional to NYHA class and correlates with pulmonary artery pressure; exogenous ADM infusion reduces PVR and SVR in acute decompensated HF; MR-proADM independently predicts HF mortality beyond NT-proBNP.

ADM → CLR/RAMP2 → Gs → cAMP → PKA → eNOS Ser1177 phosphorylation → NO production; NO mediates the vasodilatory arm of ADM signaling; endothelial NO also mediates ADM-induced vascular barrier protection via Rac1 → VE-cadherin stabilization.

ADM and BNP are both endothelial/myocardial stress peptides upregulated in sepsis, heart failure, and cardiogenic shock; MR-proADM captures endothelial dysfunction (vascular compartment) while NT-proBNP reflects myocardial wall stress — complementary biomarkers.

[^kitamura-1993-adrenomedullin]: Kitamura K, Kangawa K, Kawamoto M, et al. Adrenomedullin: a novel hypotensive peptide isolated from human pheochromocytoma. *Biochem Biophys Res Commun.* 1993;192(2):553-560. [doi:10.1006/bbrc.1993.1451](https://doi.org/10.1006/bbrc.1993.1451) · [PubMed 8387282](https://pubmed.ncbi.nlm.nih.gov/8387282/)
[^schuetz-2011-mradm-sepsis]: Schuetz P, Wolbers M, Christ-Crain M, et al. Prohormones for prediction of adverse medical outcome in community-acquired pneumonia and lower respiratory tract infections. *Crit Care.* 2010;14(3):R106. [doi:10.1186/cc9055](https://doi.org/10.1186/cc9055) · [PubMed 20529248](https://pubmed.ncbi.nlm.nih.gov/20529248/)
