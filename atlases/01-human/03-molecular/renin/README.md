---
schema: human-scale-entry/v1
id: renin
name: Renin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Renin (juxtaglomerular cell aspartyl protease) cleaves angiotensinogen to angiotensin I → ACE → angiotensin II → vasoconstriction and aldosterone; RAAS overactivation drives hypertension; suppressed renin plus elevated aldosterone diagnoses primary aldosteronism."
aliases: ["renin", "REN", "RAAS", "renin-angiotensin system", "angiotensin converting enzyme", "angiotensinogen", "prorenin", "aliskiren", "juxtaglomerular", "plasma renin activity", "PRA", "ARR", "direct renin inhibitor"]
cross_links:
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Renin catalyzes the first and rate-limiting step of Ang II synthesis: angiotensinogen → angiotensin I; ACE converts Ang I → Ang II; Ang II provides negative feedback to suppress renin at JG cells; aliskiren blocks renin → reduces Ang II and aldosterone."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Renin → angiotensin II → adrenal zona glomerulosa → aldosterone; primary aldosteronism (autonomous aldosterone) suppresses renin → low PRA + high ARR is the diagnostic signature; plasma renin activity (PRA) distinguishes primary from secondary aldosteronism."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Impaired pressure-natriuresis and reduced renal perfusion in CKD → RAAS overactivation → renin-dependent hypertension and sodium retention; ACE-I/ARBs reduce intraglomerular pressure and proteinuria; aliskiren added to ACE-I/ARB (ALTITUDE trial) increased adverse renal events."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "β1-adrenergic stimulation of JG cells by epinephrine/norepinephrine → cAMP → renin granule exocytosis; β-blockers (metoprolol, bisoprolol) reduce renin → lower Ang II and BP; β1-selectivity exploits JG cell β1-R dominance → renin suppression without β2-bronchospasm."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Excess cortisol (Cushing syndrome) → MR activation → sodium retention → renin suppression; Cushing HTN mimics primary aldosteronism (low renin, elevated BP) but distinguished by ACTH/cortisol excess; 11β-HSD2 deficiency similarly suppresses renin via RAAS volume inhibition."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α is the transcriptional activator of renin: renal ischemia → HIF-1α binds HRE on REN promoter → renin upregulation in JG cells; ACE-I/ARBs do not suppress HIF-1α-driven renin upregulation in CKD — reactive renin rise is expected and represents a RAAS escape mechanism."
sources:
  - id: atlas-2011-aliskiren-altitude
    type: peer-reviewed
    cite: "Parving HH, Brenner BM, McMurray JJV, et al. Cardiorenal end points in a trial of aliskiren for type 2 diabetes. N Engl J Med. 2012;367(23):2204-2213."
    doi: "10.1056/NEJMoa1208799"
    pmid: "23121378"
    url: "https://doi.org/10.1056/NEJMoa1208799"
  - id: carey-2019-primary-aldosteronism
    type: peer-reviewed
    cite: "Carey RM, Calhoun DA, Bakris GL, et al. Resistant hypertension: detection, evaluation, and management. Hypertension. 2018;72(5):e53-e90."
    doi: "10.1161/HYP.0000000000000084"
    pmid: "30354828"
    url: "https://doi.org/10.1161/HYP.0000000000000084"
---

# Renin

## Overview

**Renin** (gene *REN*, chromosome 1q32.1) is an **aspartyl protease** secreted by **juxtaglomerular (JG) cells** — specialized smooth muscle cells of the afferent arteriole in the renal cortex. Renin is the **rate-limiting enzyme** of the **renin-angiotensin-aldosterone system (RAAS)**, the dominant neurohumoral axis controlling blood pressure, fluid volume, and electrolyte balance. Renin cleaves the single peptide bond (Leu10–Val11) of angiotensinogen (a liver-derived α₂-globulin) to release the decapeptide **angiotensin I**, which is then rapidly converted to **angiotensin II** by **ACE** (angiotensin-converting enzyme) on pulmonary and renal endothelium.

RAAS dysregulation — excessive renin secretion in response to reduced renal perfusion, sodium depletion, or sympathetic activation — is a central mechanism in primary (essential) hypertension, heart failure, CKD, and renovascular disease. Conversely, **suppressed renin** in the setting of elevated aldosterone is the biochemical hallmark of **primary aldosteronism (Conn syndrome)** — the most common secondary cause of hypertension, affecting ~10% of hypertensive patients.

**Clinical significance of renin measurement:**

| Scenario | Renin | Aldosterone | Interpretation |
|---|---|---|---|
| Primary aldosteronism | ↓↓ (suppressed) | ↑↑ | Autonomous aldosterone; ARR >30:1 (ng/dL:ng/mL/h) |
| Secondary aldosteronism (HF, cirrhosis) | ↑↑ | ↑ | Appropriate RAAS activation |
| Renovascular HTN (renal artery stenosis) | ↑↑ | ↑ | Unilateral ischemia → renin hypersecretion |
| ACE-I/ARB therapy | ↑ (reactive) | ↓ | Expected pharmacologic response |
| Direct renin inhibitor (aliskiren) | ↑ total renin | ↓ | Prorenin accumulates; angiotensin I and II suppressed |
| Liddle syndrome | ↓ | ↓ | ENaC overactivation; pseudo-aldosteronism |

## Structure

Renin is synthesized as **prepro-renin (406 aa)** → signal peptide cleavage → **pro-renin (381 aa; stored in JG cell granules)** → proteolytic cleavage of 43-aa prosegment by **cathepsin B/D** in secretory granules → **active renin (338 aa)**:

**Catalytic domain:**
- Bilobed aspartyl protease fold with two catalytic aspartate residues (Asp32/Asp215 by pepsin numbering); the active site cleft accommodates the Leu10–Val11 bond of angiotensinogen
- High substrate specificity: angiotensinogen is the only known in vivo substrate for renin
- pH optimum: ~6.5 (relevant to renal tubular microenvironment and inflammatory/ischemic niches)

**Aliskiren binding site:**
- Aliskiren (Tekturna) binds the renin active site cleft with subnanomolar affinity (Kᵢ ~0.6 nM); interacts with the S1–S3 binding subsites; does not compete with angiotensinogen binding in a simple competitive manner — occupies the full binding cleft
- Unlike ACE inhibitors (which trap bradykinin → cough/angioedema), renin inhibition does not affect bradykinin metabolism

**Prorenin and the (P)RR receptor:**
- Prorenin circulates at 5–10× higher concentration than active renin; can bind the **(pro)renin receptor ((P)RR; ATP6AP2)** on cardiac fibroblasts, mesangial cells, and neurons → non-proteolytic conformational activation → Ang I generation locally
- (P)RR also functions as a V-ATPase accessory protein → Wnt/β-catenin signaling; its role in hypertension and cardiorenal disease is an active research area

## Function

**Three stimuli for renin secretion from JG cells:**

1. **Baroreceptor pathway:** Reduced afferent arteriolar wall stretch → JG cell depolarization relief → cAMP ↑ → renin granule exocytosis; this is the principal pressure-sensitive mechanism linking hypoperfusion to RAAS activation
2. **Macula densa pathway:** Reduced NaCl delivery to the distal tubule (macula densa cells) → paracrine prostaglandin E₂ (PGE₂) and prostacyclin release → JG cell cAMP ↑ → renin release; connects tubuloglomerular feedback to systemic RAAS
3. **Sympathetic pathway:** Renal sympathetic nerve activation → norepinephrine → JG cell β₁-adrenergic receptors → cAMP → renin release; explains RAAS overactivation in heart failure and shock

**Negative feedback on renin:**
- Angiotensin II → AT1R on JG cells → renin secretion inhibition (short-loop feedback)
- High renal perfusion pressure → stretch → inhibits renin
- High NaCl at macula densa → inhibits renin
- Atrial natriuretic peptide (ANP/BNP) → NPR-A/cGMP → reduces renin release

**RAAS cascade summary:**
Angiotensinogen (liver) + Renin → **Angiotensin I** (10 aa) + Ang I fragments  
→ ACE (lung/endothelium) → **Angiotensin II** (8 aa)  
→ AT1R → Vasoconstriction + Aldosterone (adrenal) + SNS activation + ADH + renal Na⁺ retention  
→ AT2R → Vasodilation + Anti-proliferative + Natriuresis (protective counter-pathway)

## Mechanism

**Renin-angiotensin in hypertension:**

Essential hypertension is a renin-driven state in a subset of patients (**high-renin hypertension**, ~30%): volume-depleted, salt-sensitive, often with elevated sympathetic activity. These patients respond better to ACE-I/ARBs and beta-blockers than to diuretics. The complementary group (**low-renin hypertension**, ~30%) is more common in African Americans and responds better to thiazides and calcium channel blockers. Mixed or normal renin (~40%) is intermediate.

**Renovascular hypertension:**
Renal artery stenosis (atherosclerotic or fibromuscular dysplasia) → reduced perfusion to affected kidney → marked renin hypersecretion from the ischemic kidney → high Ang II → hypertension + aldosterone elevation + contralateral kidney suppressed; treated with revascularization (stenting for fibromuscular dysplasia) or ACE-I/ARBs.

**Aliskiren pharmacology:**
- Direct renin inhibitor (DRI); first in class (FDA approved 2007 for hypertension)
- Monotherapy: BP reduction comparable to ACE-I/ARBs; added to ACE-I/ARB → further modest BP reduction
- **ALTITUDE trial** (aliskiren + ACE-I/ARB in T2D with CKD and/or CVD): increased risk of renal failure, hypotension, and hyperkalemia → combination with ACE-I or ARB is now contraindicated; limited clinical adoption beyond monotherapy
- Paradox: DRI raises plasma renin concentration (PRC) by blocking Ang II feedback) → high measured renin on assay, but Ang I and Ang II remain suppressed → the elevated renin is biologically inactive while drug is present

**Aldosterone-to-Renin Ratio (ARR) in primary aldosteronism diagnosis:**
- ARR >30:1 (ng/dL:ng/mL/h for aldosterone:PRA) with aldosterone >15 ng/dL is highly suspicious
- Confirmatory testing: sodium loading test or fludrocortisone suppression test
- Subtype differentiation: adrenal CT + adrenal venous sampling (AVS) — distinguishes unilateral adenoma (resectable) from bilateral hyperplasia (treated with MRA)
- Unilateral PA: laparoscopic adrenalectomy → cure in ~35–65%; hypertension improved in nearly all

## Connections

- `connects-to` → **[Hypertension](../../07-system/hypertension/README.md)** — Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism.
- `connects-to` → **[Angiotensin II](../angiotensin-ii/README.md)** — Renin catalyzes the first and rate-limiting step of Ang II synthesis: angiotensinogen → angiotensin I; ACE converts Ang I → Ang II; Ang II provides negative feedback to suppress renin at JG cells; aliskiren blocks renin → reduces Ang II and aldosterone.
- `connects-to` → **[Aldosterone](../aldosterone/README.md)** — Renin → angiotensin II → adrenal zona glomerulosa → aldosterone; primary aldosteronism (autonomous aldosterone) suppresses renin → low PRA + high ARR is the diagnostic signature; plasma renin activity (PRA) distinguishes primary from secondary aldosteronism.
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — Impaired pressure-natriuresis and reduced renal perfusion in CKD → RAAS overactivation → renin-dependent hypertension and sodium retention; ACE-I/ARBs reduce intraglomerular pressure and proteinuria; aliskiren added to ACE-I/ARB (ALTITUDE trial) increased adverse renal events.
- `connects-to` → **[Epinephrine](../epinephrine/README.md)** — β1-adrenergic stimulation of JG cells by epinephrine/norepinephrine → cAMP → renin granule exocytosis; β-blockers (metoprolol, bisoprolol) reduce renin → lower Ang II and BP; β1-selectivity exploits JG cell β1-R dominance → renin suppression without β2-bronchospasm.
- `connects-to` → **[Cortisol](../cortisol/README.md)** — Excess cortisol (Cushing syndrome) → MR activation → sodium retention → renin suppression; Cushing HTN mimics primary aldosteronism (low renin, elevated BP) but distinguished by ACTH/cortisol excess; 11β-HSD2 deficiency similarly suppresses renin via RAAS volume inhibition.
- `connects-to` → **[HIF-1α](../hif-1alpha/README.md)** — HIF-1α is the transcriptional activator of renin: renal ischemia → HIF-1α binds HRE on REN promoter → renin upregulation in JG cells; ACE-I/ARBs do not suppress HIF-1α-driven renin upregulation in CKD — reactive renin rise is expected and represents a RAAS escape mechanism.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^atlas-2011-aliskiren-altitude]: Parving HH, Brenner BM, McMurray JJV, et al. Cardiorenal end points in a trial of aliskiren for type 2 diabetes. *N Engl J Med.* 2012;367(23):2204-2213. [doi:10.1056/NEJMoa1208799](https://doi.org/10.1056/NEJMoa1208799) · [PubMed 23121378](https://pubmed.ncbi.nlm.nih.gov/23121378/)
[^carey-2019-primary-aldosteronism]: Carey RM, Calhoun DA, Bakris GL, et al. Resistant hypertension: detection, evaluation, and management. *Hypertension.* 2018;72(5):e53-e90. [doi:10.1161/HYP.0000000000000084](https://doi.org/10.1161/HYP.0000000000000084) · [PubMed 30354828](https://pubmed.ncbi.nlm.nih.gov/30354828/)
