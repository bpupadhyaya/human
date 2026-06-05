---
schema: medicine-entry/v1
id: arbs
name: Angiotensin Receptor Blockers
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Selectively block the AT1 receptor, preventing angiotensin II–driven vasoconstriction and aldosterone release. No bradykinin inhibition — no ACE-I cough. First-line for hypertension, HFrEF, diabetic nephropathy, and post-MI LV dysfunction."
drug_class: angiotensin II receptor antagonist
modality: small molecule
key_agents: [losartan, valsartan, irbesartan, candesartan, olmesartan, telmisartan, azilsartan]
who_essential_medicine: false
atc: C09CA
aliases: ["ARB", "sartans", "angiotensin II receptor blockers", "AT1 receptor antagonists", "losartan", "valsartan", "candesartan", "telmisartan"]
tags: [arb, sartan, hypertension, heart-failure, raas, at1-receptor, renoprotection, cardioprotection]
sources:
  - id: valheft-2001
    type: peer-reviewed
    cite: "Cohn JN, Tognoni G; Valsartan Heart Failure Trial Investigators. A randomized trial of the angiotensin-receptor blocker valsartan in chronic heart failure. N Engl J Med. 2001;345(23):1667-75."
    doi: "10.1056/NEJMoa010713"
    url: "https://doi.org/10.1056/NEJMoa010713"
  - id: life-2002
    type: peer-reviewed
    cite: "Dahlöf B, Devereux RB, Kjeldsen SE, et al. Cardiovascular morbidity and mortality in the Losartan Intervention For Endpoint reduction in hypertension study (LIFE): a randomised trial against atenolol. Lancet. 2002;359(9311):995-1003."
    doi: "10.1016/S0140-6736(02)08089-3"
    url: "https://doi.org/10.1016/S0140-6736(02)08089-3"
  - id: renaal-2001
    type: peer-reviewed
    cite: "Brenner BM, Cooper ME, de Zeeuw D, et al. Effects of losartan on renal and cardiovascular outcomes in patients with type 2 diabetes and nephropathy. N Engl J Med. 2001;345(12):861-9."
    doi: "10.1056/NEJMoa011161"
    url: "https://doi.org/10.1056/NEJMoa011161"
  - id: ontarget-2008
    type: peer-reviewed
    cite: "ONTARGET Investigators; Yusuf S, Teo KK, Pogue J, et al. Telmisartan, ramipril, or both in patients at high risk for vascular events. N Engl J Med. 2008;358(15):1547-59."
    doi: "10.1056/NEJMoa0801317"
    pmid: "18378520"
    url: "https://doi.org/10.1056/NEJMoa0801317"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: treats
    note: "ARBs reduce systemic vascular resistance, decrease cardiac afterload and preload, and interrupt RAAS-driven adverse cardiac remodelling. First-line for hypertension and HFrEF in ACE-I–intolerant patients."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "AT1 receptor blockade shifts angiotensin II signalling toward the AT2 receptor, promoting vasodilation, anti-fibrotic signalling, and anti-proliferative effects across the cardiovascular system."
  - target: 01-human/07-system/renal-system
    relation: treats
    note: "ARBs dilate the efferent arteriole, reducing intraglomerular hypertension and proteinuria. Losartan demonstrated a 16% reduction in the composite renal endpoint (ESRD, doubling of serum creatinine, death) in type 2 diabetic nephropathy in the RENAAL trial."
  - target: 01-human/07-system/renal-system
    relation: modulates
    note: "RAAS blockade via AT1 antagonism reduces glomerular filtration pressure, decreases proteinuria, and slows CKD progression — independent of blood pressure reduction."
---

# Angiotensin Receptor Blockers

## Overview

Angiotensin receptor blockers (ARBs), or sartans, are a class of antihypertensive and cardioprotective agents that **selectively antagonise the angiotensin II type 1 (AT1) receptor**, the primary mediator of angiotensin II's harmful cardiovascular and renal effects. Unlike ACE inhibitors — which reduce angiotensin II production and simultaneously inhibit bradykinin degradation — ARBs act downstream, at the receptor level, leaving bradykinin metabolism intact. This mechanistic distinction explains the defining clinical difference: ARBs do **not** cause the bradykinin-mediated dry cough that leads to ACE-I discontinuation in 25–40% of patients.

ARBs are first-line or equally acceptable alternatives to ACE inhibitors for:

- **Hypertension** (all causes)
- **Heart failure with reduced ejection fraction (HFrEF)** — preferred when ACE-I is not tolerated
- **Diabetic nephropathy** (type 2 DM with proteinuria)
- **Post-MI with LV dysfunction** (in ACE-I–intolerant patients)
- **Stroke prevention** in hypertension with LV hypertrophy (LIFE trial)

The class was introduced in the 1990s with **losartan** (the first clinically available ARB) and has expanded to include seven FDA-approved agents, each with modestly different receptor binding kinetics, half-lives, and ancillary pharmacology.

## Mechanism

### AT1 Receptor Blockade

The RAAS cascade generates **angiotensin II**, which acts on two receptor subtypes:

```
Angiotensin II
     │
     ├─► AT1 receptor (vascular smooth muscle, adrenal, kidney, heart, brain)
     │        → vasoconstriction, aldosterone secretion, sympathetic potentiation,
     │          renal Na⁺ reabsorption, cardiac fibrosis, myocyte hypertrophy
     │
     └─► AT2 receptor (less expressed in adults; upregulated in disease states)
              → vasodilation, anti-fibrotic, anti-proliferative, natriuresis
```

ARBs competitively (most) or insurmountably (e.g., candesartan, olmesartan — pseudo-irreversible) bind the AT1 receptor, preventing angiotensin II from activating it. Crucially, **angiotensin II accumulates** and is redirected to the unblocked **AT2 receptor**, augmenting vasodilatory and anti-fibrotic AT2-mediated signalling — a potentially beneficial "AT2 overdrive" distinct from ACE inhibition.

### Consequences of AT1 Blockade

| Effect | Mechanism | Clinical relevance |
|:---|:---|:---|
| ↓Blood pressure | ↓SVR (arteriolar dilation), ↓preload (↓aldosterone → ↓Na⁺/H₂O) | Core antihypertensive effect |
| ↓Cardiac afterload/preload | Arterial and venous vasodilation | Reduces cardiac work in HFrEF |
| ↓Glomerular hypertension | Efferent arteriole dilation (Ang II preferentially constricts efferent) | Renoprotection: ↓proteinuria, slows CKD |
| ↓Aldosterone | ↓AT1 stimulation of adrenal zona glomerulosa | Risk of hyperkalaemia (monitor K⁺) |
| ↓Cardiac fibrosis | ↓AT1-driven TGF-β, fibroblast activation | Reverse remodelling in HFrEF |
| AT2 agonism (indirect) | Accumulated Ang II → unopposed AT2 | Additional vasodilation, anti-fibrotic effects |

### No Bradykinin Accumulation — Key Distinction from ACE-I

ARBs do **not** inhibit ACE and therefore do **not** impair bradykinin degradation. This means:

- No bradykinin-mediated dry cough (the class is preferred in the ~25–40% of patients who cannot tolerate ACE-I cough)
- Significantly lower risk of angioedema (bradykinin-mediated) compared to ACE-I — though AT2-mediated kinin pathways can still rarely cause angioedema
- Slightly less vasodilatory potency than ACE-I (no bradykinin-augmented vasodilation)

## Clinical Use

### Indications

| Indication | Evidence level | Preferred agents |
|:---|:---|:---|
| **Hypertension** | Class I | Any ARB; losartan, valsartan, telmisartan, candesartan |
| **HFrEF (ACE-I intolerant)** | Class I, Level A | Candesartan (CHARM), valsartan (Val-HeFT) |
| **Diabetic nephropathy (T2DM + proteinuria)** | Class I | Losartan (RENAAL), irbesartan (IDNT) |
| **Post-MI with LV dysfunction (ACE-I intolerant)** | Class IIa | Valsartan (VALIANT) |
| **Stroke prevention in hypertension + LVH** | Class I | Losartan (LIFE) |
| **HFpEF (heart failure with preserved EF)** | Class IIb | Candesartan (CHARM-Preserved) — modest benefit |

### Key Agents

| Drug | Half-life | Notable pharmacology |
|:---|:---:|:---|
| **Losartan** | 2 h (active metabolite EXP-3174: 6–9 h) | Active metabolite; uricosuric (mild); first ARB approved |
| **Valsartan** | 6 h | Val-HeFT, VALIANT; widely used in HFrEF component of sacubitril/valsartan (ARNI) |
| **Candesartan** | 9 h | Prodrug (candesartan cilexetil); pseudo-irreversible AT1 binding; CHARM trials |
| **Irbesartan** | 11–15 h | IDNT trial (diabetic nephropathy); partial AT1 inverse agonist |
| **Olmesartan** | 13 h | Pseudo-irreversible; high AT1 affinity; once daily |
| **Telmisartan** | 24 h | Longest half-life; once daily; partial PPARγ agonist (potential metabolic benefit) |
| **Azilsartan** | 11 h | Newest; medoxomil prodrug; possibly greater BP reduction vs. other ARBs |

### Dosing Principle

As with ACE inhibitors, ARBs in HFrEF should be **titrated to the maximum tolerated dose** that was used in evidence-generating trials (e.g., candesartan 32 mg daily, valsartan 160 mg twice daily). Under-dosing is common in clinical practice and diminishes the mortality-reduction benefit.

### Contraindications and Cautions

- **Pregnancy** — Category D; angiotensin II is essential for fetal renal development; causes oligohydramnios, renal tubular dysplasia, and skull hypoplasia. Same teratogenicity profile as ACE-I; contraindicated in all trimesters
- **Bilateral renal artery stenosis** — reduces GFR by dilating efferent arteriole (shared risk with ACE-I); may precipitate acute kidney injury
- **Hyperkalaemia** (K⁺ >5.5 mmol/L) — ↓aldosterone → K⁺ retention; high risk with concomitant MRA or potassium-sparing diuretics
- **Dual RAAS blockade (ARB + ACE-I)** — ONTARGET demonstrated **no added cardiovascular benefit** and significantly increased renal adverse events, hypotension, and hyperkalaemia. Combination is generally **not recommended** unless in carefully selected HFrEF patients with specialist oversight

## Evidence

### Landmark Randomised Controlled Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **Val-HeFT (2001)** | Valsartan | 5,010 patients with HFrEF (NYHA II–IV), on conventional therapy | **13.2% reduction in combined morbidity/mortality** (hospitalisation + death); 33% reduction in HF hospitalisation alone [^valheft-2001] |
| **LIFE (2002)** | Losartan vs atenolol | 9,193 hypertensive patients with ECG-confirmed LVH | Losartan reduced **primary composite (CV death, MI, stroke) by 13%** vs atenolol; **25% reduction in stroke** — greater than expected from BP difference alone [^life-2002] |
| **RENAAL (2001)** | Losartan | 1,513 patients with T2DM and nephropathy | **16% reduction in composite ESRD/doubling of creatinine/death**; 35% reduction in ESRD hospitalisation; 28% reduction in first hospitalisation for HF [^renaal-2001] |
| **CHARM-Alternative (2003)** | Candesartan | 2,028 HFrEF patients intolerant to ACE-I | **23% reduction in CV death or HF hospitalisation** vs placebo; established ARBs as HFrEF first-line when ACE-I not tolerated |
| **ONTARGET (2008)** | Telmisartan ± ramipril | 25,620 high-risk patients | Telmisartan non-inferior to ramipril; combination: **no added CV benefit, significantly more renal adverse events** [^ontarget-2008] |

### ARBs vs ACE-I vs ARNI in HFrEF

- ARBs and ACE inhibitors have broadly **equivalent mortality benefits** in HFrEF; cross-trial comparisons show no significant advantage of either class over the other
- **PARADIGM-HF** (sacubitril/valsartan vs enalapril): the ARNI — which combines valsartan (ARB) with sacubitril (neprilysin inhibitor, augmenting natriuretic peptides and bradykinin) — reduced CV death/HF hospitalisation by a further 20% over enalapril. ARBs/ACE-I are now superseded by ARNI as the preferred RAAS strategy in eligible HFrEF patients
- ARBs remain the preferred RAAS agent in HFrEF patients transitioning to ARNI (no 36-hour washout required, unlike ACE-I → ARNI transition)

## Connections

- **Treats** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): ARBs reduce SVR, blood pressure, aldosterone-mediated volume overload, and RAAS-driven cardiac fibrosis — core therapeutic effects across the entire cardiovascular system in hypertension and HFrEF.
- **Modulates** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): Indirect AT2 receptor agonism (from accumulated angiotensin II) promotes vasodilatory and anti-fibrotic signalling, modulating cardiovascular structure and function beyond simple AT1 blockade.
- **Treats** → [Renal system](../../../../01-human/07-system/renal-system/README.md): By dilating the efferent arteriole, ARBs reduce intraglomerular pressure and proteinuria, slowing diabetic and non-diabetic CKD progression.
- **Modulates** → [Renal system](../../../../01-human/07-system/renal-system/README.md): RAAS blockade at the AT1 receptor reduces sodium reabsorption, aldosterone-driven potassium excretion, and glomerular filtration pressure — systemic renal modulation.
- **Compare with** → [ACE inhibitors](../ace-inhibitors/README.md): Both block the RAAS and reduce angiotensin II's end-organ effects. ACE-I additionally raises bradykinin (causing cough, rare angioedema); ARBs redirect angiotensin II to AT2 receptor. Clinically interchangeable in most settings; ARBs preferred when ACE-I cough occurs.
- **Superseded by** → Sacubitril/valsartan (ARNI): In eligible HFrEF patients, ARNI provides superior outcomes over either ACE-I or ARB alone; valsartan is the ARB component of this combination.

[^valheft-2001]: Cohn JN, Tognoni G; Valsartan Heart Failure Trial Investigators. A randomized trial of the angiotensin-receptor blocker valsartan in chronic heart failure. *N Engl J Med.* 2001;345(23):1667-75. [doi:10.1056/NEJMoa010713](https://doi.org/10.1056/NEJMoa010713)
[^life-2002]: Dahlöf B, Devereux RB, Kjeldsen SE, et al. Cardiovascular morbidity and mortality in the Losartan Intervention For Endpoint reduction in hypertension study (LIFE). *Lancet.* 2002;359(9311):995-1003. [doi:10.1016/S0140-6736(02)08089-3](https://doi.org/10.1016/S0140-6736(02)08089-3)
[^renaal-2001]: Brenner BM, Cooper ME, de Zeeuw D, et al. Effects of losartan on renal and cardiovascular outcomes in patients with type 2 diabetes and nephropathy. *N Engl J Med.* 2001;345(12):861-9. [doi:10.1056/NEJMoa011161](https://doi.org/10.1056/NEJMoa011161)
[^ontarget-2008]: ONTARGET Investigators; Yusuf S, Teo KK, Pogue J, et al. Telmisartan, ramipril, or both in patients at high risk for vascular events. *N Engl J Med.* 2008;358(15):1547-59. [doi:10.1056/NEJMoa0801317](https://doi.org/10.1056/NEJMoa0801317) · [PubMed 18378520](https://pubmed.ncbi.nlm.nih.gov/18378520/)
