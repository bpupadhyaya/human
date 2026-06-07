---
schema: human-scale-entry/v1
id: pcsk9
name: PCSK9
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PCSK9 promotes lysosomal degradation of LDL receptors, elevating LDL-C; GOF mutations → familial hypercholesterolemia; LOF mutations → low LDL-C and cardiovascular protection; PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C 50-60% and major cardiovascular events."
aliases: ["PCSK9", "proprotein convertase subtilisin kexin 9", "NARC-1", "PCSK9 inhibitor", "evolocumab target", "alirocumab target", "LDL receptor regulator", "PCSK9 FH", "PCSK9 LOF", "PCSK9 cardiovascular"]
cross_links:
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "PCSK9 binds LDLR extracellular domain → promotes lysosomal degradation instead of recycling → fewer surface LDL receptors → elevated LDL-C; statins upregulate PCSK9, partially offsetting their LDL-lowering — explaining the synergy of PCSK9 inhibitors with statin therapy."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "LDL-C-driven carotid atherosclerosis causes ischemic stroke via thromboembolism; PCSK9 inhibitors (evolocumab, alirocumab) reduce stroke risk ~25% in post-MI patients; very low LDL-C (<25 mg/dL) with PCSK9 inhibition does not impair cognition and reduces stroke incidence."
sources:
  - id: abifadel-2003-pcsk9-cloning
    type: peer-reviewed
    cite: "Abifadel M, Varret M, Rabès JP, et al. Mutations in PCSK9 cause autosomal dominant hypercholesterolaemia. Nat Genet. 2003;34(2):154-156."
    doi: "10.1038/ng1161"
    pmid: "12730697"
    url: "https://doi.org/10.1038/ng1161"
  - id: sabatine-2017-fourier
    type: peer-reviewed
    cite: "Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and clinical outcomes in patients with cardiovascular disease. N Engl J Med. 2017;376(18):1713-1722."
    doi: "10.1056/NEJMoa1615664"
    pmid: "28304224"
    url: "https://doi.org/10.1056/NEJMoa1615664"
---

# PCSK9

## Overview

**PCSK9** (proprotein convertase subtilisin/kexin type 9; also NARC-1) is a serine protease and secreted glycoprotein encoded on chromosome 1p32.3 that post-translationally regulates the **LDL receptor (LDLR)** and controls circulating LDL-cholesterol (LDL-C) levels. Abifadel et al. (2003) identified PCSK9 gain-of-function (GOF) mutations as the cause of autosomal dominant hypercholesterolemia (ADH3) in French families [^abifadel-2003-pcsk9-cloning]. Conversely, natural loss-of-function (LOF) mutations in PCSK9 (prevalent in African Americans: Y142X, C679X; present in Europeans: R46L) cause lifelong low LDL-C (~100 mg/dL reduction) and dramatically reduce cardiovascular disease risk (~88% RRR for CHD events over 15 years in Dallas Heart Study), without apparent adverse effects.

PCSK9 became one of the most validated drug targets in cardiovascular medicine: the FOURIER trial (evolocumab; n=27,564) demonstrated that PCSK9 inhibition on top of statin therapy reduced major adverse cardiovascular events (MACE) by 15% over ~26 months with ~60% LDL-C reduction from ~90 to ~30 mg/dL [^sabatine-2017-fourier]. ODYSSEY OUTCOMES (alirocumab) similarly showed 15% MACE reduction plus a mortality benefit in post-ACS patients. Two FDA-approved monoclonal antibodies (evolocumab/Repatha; alirocumab/Praluent) and an siRNA (inclisiran, given twice-yearly) are now standard-of-care for high-risk patients.

**PCSK9 genetic variants:**

| Variant | Type | LDL-C effect | CVD risk | Prevalence |
|---|---|---|---|---|
| D374Y | GOF | ~3× elevation | High FH penetrance | Rare |
| S127R | GOF | ~2× elevation | High FH | Rare |
| E670G | GOF | Modest elevation | Moderate | Common |
| Y142X | LOF | ~40 mg/dL reduction | ~88% CHD protection | ~2% African American |
| R46L | LOF | ~15 mg/dL reduction | Moderate protection | ~3% European |

## Structure

PCSK9 is synthesized as a 692 amino acid proprotein (MW ~74 kDa) with:

**Signal peptide (aa 1–30):** directs ER import.

**Prodomain (aa 31–152):** acts as an intramolecular chaperone; autocleaved in the ER at VFAQ↓SIP152 site by PCSK9 itself (autocatalytic cleavage required for PCSK9 folding and ER exit) → prodomain remains non-covalently associated with the catalytic domain, blocking the active site — PCSK9 is thus an **inactive protease** after secretion.

**Catalytic domain (aa 153–452):** Serine protease (Ser386-His226-Asp186 catalytic triad); structurally similar to subtilisins but enzymatically inactive due to prodomain blocking. D374Y (hot spot FH mutation) lies in the catalytic domain and dramatically increases PCSK9-LDLR binding affinity.

**C-terminal domain (CTD; aa 453–692):** Three-bladed β-propeller (MODY motif); binds LDL directly and modulates PCSK9 secretion and activity; some evidence for CTD autoregulation.

**LDLR binding:** PCSK9 binds the EGF-A domain of LDLR via its catalytic domain face; the interaction is pH-dependent — weak at neutral pH (extracellular), strong at acidic pH (endosomal). This pH-switching is key: after endocytosis of the LDL-LDLR-PCSK9 ternary complex, endosomal acidification strengthens PCSK9-LDLR binding → LDLR cannot dissociate → lysosomal degradation of LDLR rather than recycling to cell surface.

## Function

**LDLR regulation:** PCSK9 circulates in plasma at ~300–400 ng/mL and binds LDLR on hepatocytes (primary site) and extrahepatic cells. After LDLR-mediated endocytosis:
- Without PCSK9: LDL releases at acidic pH, LDLR recycles to surface (~150 cycles/LDLR)
- With PCSK9: PCSK9-LDLR complex is retained in lysosome → LDLR degraded → fewer surface LDL receptors → less LDL uptake → elevated plasma LDL-C

**Other PCSK9 substrates:** PCSK9 also targets ApoER2, VLDLR, CD81, and integrin αV for lysosomal degradation. CD81 targeting may affect hepatitis C virus entry. ApoER2 degradation in neurons has been proposed to affect neuronal function.

**PCSK9 and triglyceride-rich lipoproteins:** PCSK9 regulates VLDLR and ApoER2, with modest effects on VLDL and triglyceride metabolism; PCSK9 inhibition primarily affects LDL-C and ApoB with minimal triglyceride effect.

**Statin-PCSK9 interaction:** Statins (HMG-CoA reductase inhibitors) upregulate PCSK9 transcription via SREBP-2 → increase PCSK9 secretion → offset up to 40% of the expected statin-induced LDLR upregulation and LDL-C reduction. This explains why PCSK9 inhibitors, by blocking this compensatory mechanism, achieve dramatic additional LDL-C lowering (~50-60%) on top of statins.

## Mechanism

**PCSK9-LDLR lysosomal targeting mechanism:**
1. PCSK9 secreted by hepatocytes → binds LDLR at cell surface (Kd ~170 nM at pH 7.4)
2. LDLR-LDL-PCSK9 ternary complex endocytosed via clathrin-coated pits
3. Endosomal acidification (pH 5.0–5.5) → PCSK9 catalytic domain undergoes conformational change → LDLR EGF-A binding affinity increases 100-fold (Kd ~8 nM at pH 5.0)
4. PCSK9-LDLR complex remains locked → LDLR cannot adopt "closed conformation" needed for LDL release and recycling
5. LDLR traffics to lysosomes → proteolytic degradation
6. Net effect: fewer LDLR on hepatocyte surface → reduced LDL clearance → elevated LDL-C

**Anti-PCSK9 therapeutics:**
- **Evolocumab (Repatha):** Fully human IgG2 monoclonal antibody; subcutaneous injection (140 mg/2 weeks or 420 mg/month); FOURIER: LDL-C ~60% reduction; ~15% MACE reduction in 3 years
- **Alirocumab (Praluent):** Fully human IgG1; ODYSSEY OUTCOMES: ~15% MACE reduction, 15% mortality reduction in post-ACS patients
- **Inclisiran (Leqvio):** siRNA targeting PCSK9 mRNA in hepatocytes via GalNAc conjugate; twice-yearly dosing (day 1, day 90, then every 6 months); ~50% LDL-C reduction; ORION trials confirmed durable effect; VICTORION outcomes trial expected ~2025
- **Oral PCSK9 inhibitors:** Small molecule PCSK9 inhibitors (adnectin-based, macrocycles) in development; AZD0780 and MK-0616 in Phase 2

## Connections

PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD.

PCSK9 binds LDLR extracellular domain → promotes lysosomal degradation instead of recycling → fewer surface LDL receptors → elevated LDL-C; statins upregulate PCSK9, partially offsetting their LDL-lowering — explaining the synergy of PCSK9 inhibitors with statin therapy.

Elevated LDL-C from PCSK9 GOF mutations accelerates coronary atherosclerosis → MI → ischemic cardiomyopathy and heart failure; PCSK9 inhibitors reduce MI risk in high-risk CVD patients; PCSK9 may also have direct myocardial effects via apoE and apoB receptor pathways.

LDL-C-driven carotid atherosclerosis causes ischemic stroke via thromboembolism; PCSK9 inhibitors (evolocumab, alirocumab) reduce stroke risk ~25% in post-MI patients; very low LDL-C (<25 mg/dL) with PCSK9 inhibition does not impair cognition and reduces stroke incidence.
