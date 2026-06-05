---
schema: human-scale-entry/v1
id: angiotensin-ii
name: Angiotensin II
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Octapeptide (Asp-Arg-Val-Tyr-Ile-His-Pro-Phe; MW 1046); RAAS effector produced by ACE from Ang I. Acts via AT1R (vasoconstriction, aldosterone, Na⁺ retention, cardiac hypertrophy) and AT2R (counter-regulatory). Key target of ACEi and ARBs."
aliases: ["AngII", "Ang II", "angiotensin-2", "AII", "vasoconstrictor octapeptide"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Ang II is the most potent endogenous vasoconstrictor; AT1R on VSM → IP3→Ca²⁺→vasoconstriction; AT1R on heart → hypertrophy/fibrosis. RAAS-targeting drugs (ACEi, ARBs) reduce MACE in HF, post-MI, and diabetic nephropathy."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Ang II constricts efferent arterioles (maintaining GFR despite ↓RBF), ↑NHE3 (proximal Na⁺), stimulates aldosterone (Na⁺/K⁺ balance), and drives CKD progression via TGF-β mesangial fibrosis."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: modulated-by
    note: "ACE inhibitors block Ang I → Ang II conversion, reducing AT1R-mediated vasoconstriction, aldosterone secretion, and cardiac fibrosis; they also accumulate bradykinin via B2 receptor, causing cough and angioedema."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Angiotensinogen is synthesised by hepatocytes (~0.5–1 µM plasma) as the sole renin substrate; hepatocyte-derived angiotensinogen is rate-limiting for RAAS when renin is very high; hepatic AT1R mediates glycogenolysis."
---

# Angiotensin II

## Overview

Angiotensin II (Ang II) is an **octapeptide** (Asp¹-Arg²-Val³-Tyr⁴-Ile⁵-His⁶-Pro⁷-Phe⁸; MW 1046 Da) and the principal effector of the **renin-angiotensin-aldosterone system (RAAS)** — one of the most important neurohumoral axes regulating blood pressure, fluid balance, and cardiovascular homeostasis. It is the most potent endogenous vasoconstrictor known [^stryer-biochemistry].

Ang II is generated in the circulation from angiotensinogen (a hepatocyte-derived glycoprotein, 452 aa) through a two-step proteolytic cascade: **renin** (juxtaglomerular apparatus) cleaves angiotensinogen → Ang I (10 aa), then **ACE** (angiotensin-converting enzyme, lung and renal endothelium) removes two C-terminal residues → Ang II. The biological actions of Ang II are mediated by two GPCRs — **AT1R** (mediating the classical vasoconstrictive and pro-fibrotic effects) and **AT2R** (largely counter-regulatory) — and are therapeutically targeted by some of the most widely used cardiovascular drugs: ACE inhibitors and angiotensin receptor blockers (ARBs) [^stryer-biochemistry].

Ang II is also a key driver of **end-organ damage** in hypertension and heart failure: beyond acute vasoconstriction, chronic AT1R activation drives cardiac hypertrophy, fibrosis (via TGF-β/SMAD), and CKD progression (via intraglomerular hypertension and mesangial TGF-β). The counter-regulatory **ACE2/Ang 1-7/Mas axis** provides an endogenous brake — and was thrust into clinical prominence when SARS-CoV-2 was identified to use ACE2 as its cellular entry receptor [^janeway-immunobiology].

## Structure

### Peptide sequence and chemistry

| Property | Value |
|:---|:---|
| Sequence | Asp-Arg-Val-Tyr-Ile-His-Pro-Phe |
| Molecular weight | 1046.18 Da |
| Precursor | Angiotensin I (10 aa) |
| Generating enzyme | ACE (dipeptidyl carboxypeptidase, Zn²⁺-dependent) |
| Plasma half-life | ~15–60 seconds (degraded by angiotensinases) |
| Primary receptor | AT1R (Gq + Gi; AGTR1) |

The C-terminal Phe⁸ and His⁶ residues are critical for AT1R binding; the Pro⁷ imparts rigidity to the C-terminal dipeptide, protecting it from ACE cleavage and contributing to receptor binding geometry.

### ACE structure and mechanism

ACE is a **Zn²⁺-dependent dipeptidyl carboxypeptidase** (clan MA, family M2) that removes dipeptides from peptide C-termini. It exists in two isoforms:
- **Somatic ACE** (1306 aa, two catalytic domains N and C): expressed predominantly on lung vascular endothelium (pulmonary capillary bed), renal proximal tubule brush border, and CNS; responsible for the bulk of circulating Ang II generation
- **Germinal ACE** (732 aa, single catalytic domain): expressed on testicular spermatids; reproductive function

ACE also cleaves **bradykinin** (vasodilatory nonapeptide from the kallikrein-kinin system) → inactive fragments. ACE inhibitors block both Ang II generation and bradykinin degradation — the latter causes bradykinin accumulation → B2 receptor activation → prostaglandin E2 + substance P → **dry cough** (up to 15% of patients) and **angioedema** (rare, 0.1–0.3%).

### Receptors

| Receptor | Gene | G-protein coupling | Expression | Key effects |
|:---|:---|:---|:---|:---|
| **AT1R** | *AGTR1* | Gq + Gi; also β-arrestin | Vascular SM, heart, adrenal ZG, kidney, brain, liver | Vasoconstriction, aldosterone, ADH, Na⁺ retention, cardiac hypertrophy/fibrosis, sympathetic activation |
| **AT2R** | *AGTR2* | Gi, phosphatases, NO/cGMP | Fetal tissues, brain, adrenal medulla; upregulated in injury/HF | Vasodilation, anti-proliferative, anti-fibrotic, anti-apoptotic; counter-regulatory to AT1R |

## Function

### RAAS pathway: synthesis to action

```
↓BP / ↓Na⁺ / ↑renal sympathetics
        │
        ▼
  Renin (JGA) → cleaves Angiotensinogen (hepatocyte) → Ang I (10 aa)
        │
        ▼
  ACE (lung/kidney endothelium) → removes C-terminal His-Leu → Ang II (8 aa)
        │
     ┌──┴──────────────────────┐
     AT1R (dominant)         AT2R (counter-regulatory)
     │                        │
  Vasoconstriction           Vasodilation
  Aldosterone release        Anti-fibrosis
  ADH release                Anti-proliferation
  Na⁺ retention              NO production (cGMP)
  Cardiac hypertrophy
  Fibrosis (TGF-β)
```

**ACE2 counter-axis** [^janeway-immunobiology]:
- ACE2 (expressed in heart, kidney, lung, gut, brain) cleaves Ang II → **Ang 1-7** (vasodilatory, anti-fibrotic, anti-inflammatory)
- Ang 1-7 → **Mas receptor** → NO production, cGMP, ↓TGF-β → opposes AT1R effects
- SARS-CoV-2 spike protein binds ACE2 → viral entry → ↓surface ACE2 → ↑Ang II:Ang 1-7 ratio → ↑inflammation, ↑fibrosis (COVID-19 cardiovascular pathology)

### Cardiovascular actions (AT1R)

1. **Vasoconstriction**: AT1R on vascular smooth muscle → Gq → PLC → IP3 → ↑intracellular Ca²⁺ → myosin light chain kinase → smooth muscle contraction → ↑peripheral vascular resistance; most powerful endogenous vasoconstrictive signal
2. **Cardiac effects**: AT1R on cardiomyocytes → Gq/ERK1/2/Akt → **hypertrophic gene program** (ANP, BNP, β-MHC, VEGF); AT1R on cardiac fibroblasts → TGF-β/SMAD2/3 → collagen I/III → fibrosis → impaired diastolic function → heart failure with preserved ejection fraction (HFpEF) progression

### Renal actions

1. **Efferent arteriole constriction**: preferential efferent > afferent constriction → ↑GFR maintenance despite ↓renal blood flow (essential for GFR support in hypovolaemia)
2. **Proximal tubule**: AT1R → ↑NHE3 (Na⁺/H⁺ exchanger) + ↑NBC (Na⁺/HCO₃⁻ co-transporter) → ↑Na⁺ and HCO₃⁻ reabsorption (~65% of filtered Na⁺)
3. **Aldosterone axis**: AT1R on zona glomerulosa → ↑CYP11B2 (aldosterone synthase) → aldosterone → MR in distal nephron → ↑ENaC + ↑Na/K-ATPase → Na⁺ retention, K⁺ excretion → ↑plasma volume → ↑BP
4. **Mesangial cell contraction**: ↓Kf (glomerular filtration coefficient) → modifies GFR
5. **Fibrosis in CKD**: Ang II → TGF-β → mesangial matrix expansion → glomerulosclerosis → CKD progression

### CNS and sympathetic actions

- AT1R in circumventricular organs (OVLT, subfornical organ — outside BBB) → ↑sympathetic outflow from rostral VLM → ↑heart rate, ↑NE release, ↑vasoconstriction
- AT1R on hypothalamic nuclei → ↑ADH (vasopressin) release → V2R in collecting duct → aquaporin-2 trafficking → water reabsorption → ↑plasma volume
- AT1R on adrenergic presynaptic terminals → facilitates NE release → potentiates sympathetic vasoconstriction

## Mechanism

### AT1R signaling in detail

AT1R is a **class A GPCR** (7 transmembrane helices) that couples to multiple transducers:

**Gq pathway** (dominant, vasoconstriction):
1. Gαq → PLC-β → PIP2 → IP3 + DAG
2. IP3 → IP3R on SR/ER → Ca²⁺ release
3. Ca²⁺ + calmodulin → MLCK → MLC phosphorylation → smooth muscle contraction
4. DAG + Ca²⁺ → PKC → various downstream phosphorylations (NHE3, NADPH oxidase)

**MAPK pathway** (cardiac hypertrophy and growth):
1. AT1R → Gβγ/Gαq → Ras/RAF/MEK → ERK1/2 → transcription factors (GATA4, SRF) → fetal gene re-expression (β-MHC, ANP, BNP)
2. AT1R → JAK2 (ligand-independent) → STAT3 → hypertrophic gene program

**TGF-β/SMAD pathway** (fibrosis):
1. AT1R → Gq → PKC/NADPH oxidase → reactive oxygen species
2. ROS → latent TGF-β activation → TGF-βR → SMAD2/3 phosphorylation → nuclear translocation → collagen I/III, fibronectin transcription

**β-Arrestin pathway** (biased signaling, internalization):
- AT1R + β-arrestin → receptor internalization, desensitization; also β-arrestin-biased AT1R signaling activates ERK without Gq (cardioprotective bias; explored with "biased agonists")

### AT2R counter-regulatory signaling

AT2R couples to **Gi** (↓cAMP), protein tyrosine phosphatases (inactivates ERK/MAPK), and **bradykinin B2/NO/cGMP** pathway:
- AT2R activation → ↑eNOS → ↑NO → ↑cGMP → PKG → smooth muscle relaxation (vasodilation)
- AT2R → ↓ERK1/2 → anti-proliferative (blocks Ang II-induced VSMC proliferation)
- Upregulated in cardiac hypertrophy, myocardial infarction, and stroke — potentially endogenous repair signal

### Aldosterone generation

Ang II → AT1R on adrenal zona glomerulosa → Gq → ↑IP3→↑Ca²⁺ → StAR protein activation → mitochondrial cholesterol transport → CYP11A1 → pregnenolone → progesterone → 11-deoxycorticosterone → corticosterone → **aldosterone** (via CYP11B2/aldosterone synthase, the rate-limiting step). Aldosterone → type I mineralocorticoid receptor (MR) in distal nephron and collecting duct → ENaC + Na/K-ATPase upregulation → Na⁺ retention, K⁺ secretion.

## Connections

- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — the most potent endogenous vasoconstrictor; AT1R-mediated VSM contraction, cardiac hypertrophy/fibrosis, and sympathetic potentiation; ACEi/ARBs are first-line in HF, post-MI, hypertension [^stryer-biochemistry]
- `modulates` → **[kidney](../../06-organ/kidney/README.md)** — efferent arteriole constriction (GFR maintenance), ↑NHE3 (proximal Na⁺ reabsorption), aldosterone axis (distal Na⁺/K⁺), and CKD progression via TGF-β mesangial fibrosis [^stryer-biochemistry]
- `modulated-by` → **[ace-inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — ACEi block conversion of Ang I → Ang II; reduce AT1R-mediated vasoconstriction, aldosterone, and cardiac fibrosis; bradykinin accumulation causes cough and angioedema via B2R [^stryer-biochemistry]
- `modulates` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — angiotensinogen is synthesised exclusively by hepatocytes; rate-limiting substrate for renin; hepatic AT1R mediates glycogenolysis; hepatic angiotensin system has local paracrine roles in fibrosis [^stryer-biochemistry]

## Pathology

| Condition | Mechanism | Clinical relevance |
|:---|:---|:---|
| **Essential hypertension** | RAAS over-activation (genetic + environmental); ↑Ang II → ↑peripheral resistance + ↑volume | ACEi/ARBs first-line; ARBs in ACEi-intolerant patients |
| **Renovascular hypertension** | Renal artery stenosis → ↓RBF → ↑renin → ↑Ang II (secondary hyperaldosteronism); fibromuscular dysplasia or atherosclerosis | Captopril test (↑renin after ACEi); revascularisation vs. ACEi/ARB |
| **Conn syndrome (primary aldosteronism)** | Autonomous aldosterone-producing adenoma → ↑aldosterone, ↑Na⁺, ↓K⁺, ↓renin; Ang II is NOT the driver | Adrenalectomy (adenoma) or MR antagonists (bilateral hyperplasia) |
| **Heart failure (HFrEF)** | Chronic Ang II → cardiac hypertrophy, fibrosis, maladaptive remodelling; neurohormonal vicious cycle | ACEi + β-blocker + MRA ± ARB; sacubitril/valsartan superior in HFrEF (PARADIGM-HF) |
| **Diabetic nephropathy** | Intraglomerular hypertension + TGF-β → glomerulosclerosis → progressive CKD | ACEi/ARBs reduce proteinuria and slow CKD; FIDELIO (finerenone, MRA) additive |
| **Acute kidney injury (ACEi in bilateral RAS)** | ACEi blocks efferent arteriole constriction → ↓GFR catastrophically if bilateral renal artery stenosis | Creatinine must be monitored; ACEi contraindicated in bilateral RAS |
| **CKD progression** | Ang II → mesangial TGF-β → matrix expansion → glomerulosclerosis → tubular atrophy | ACEi/ARBs standard of care regardless of BP |
| **COVID-19 cardiovascular pathology** | SARS-CoV-2 + ACE2 → ↓ACE2 → ↑Ang II:Ang 1-7 ratio → ↑inflammation, ↑TGF-β fibrosis, ↑thrombosis | Continued ACEi/ARBs in COVID-19 (not contraindicated — evidence base reviewed 2020) |
| **Neonatal renal dysgenesis** | In utero ACEi or ARB exposure → ↓Ang II → impaired renal tubular development | ACEi/ARBs contraindicated in pregnancy (teratogenic class D/X after 1st trimester) |
| **Angioedema (ACEi-induced)** | ↑Bradykinin (ACE blocks kinin degradation) → B2R → ↑vascular permeability → laryngeal/tongue/lips swelling | Discontinue ACEi immediately; treat with icatibant (B2R antagonist) or C1-INH |

## See Also

- [Cortisol](../cortisol/README.md) — parallel stress hormone; cortisol upregulates angiotensinogen expression in liver and sensitizes AT1R
- [Nitric oxide](../nitric-oxide/README.md) — counter-regulatory vasodilator; ACE2/Ang 1-7 stimulates eNOS-derived NO opposing Ang II vasoconstriction
- [Insulin](../insulin/README.md) — insulin resistance associated with RAAS over-activation; Ang II impairs insulin signaling (IRS-1 serine phosphorylation via AT1R/ERK)
- [NF-κB](../nf-kb/README.md) — downstream of AT1R in vascular inflammation; mediates ICAM-1, MCP-1, IL-6 expression
- [Glucocorticoid receptor](../glucocorticoid-receptor/README.md) — cortisol/GR upregulates hepatic angiotensinogen and sensitizes RAAS
- [Cardiovascular system](../../07-system/cardiovascular-system/README.md) — primary system context
- [Kidney](../../06-organ/kidney/README.md) — primary organ target; renal haemodynamics and fibrosis
- [ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md) — pharmacological blockade of ACE; most important therapeutic target
- [ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md) — AT1R direct blockers; preferred when ACEi not tolerated

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Macmillan Learning](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^janeway-immunobiology]: Murphy K, Weaver C. *Janeway's Immunobiology.* 9th ed. Garland Science; 2017. [Garland Science](https://www.garlandscience.com/product/isbn/9780815345053)
