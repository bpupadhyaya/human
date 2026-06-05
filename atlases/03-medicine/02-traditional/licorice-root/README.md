---
schema: medicine-entry/v1
id: licorice-root
name: Licorice Root (Glycyrrhiza glabra / G. uralensis)
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Glycyrrhiza root triterpene saponin glycyrrhizin hydrolyzed to glycyrrhetic acid, which inhibits renal 11β-HSD2 → pseudo-hyperaldosteronism: Na+ retention, hypertension, hypokalemia. DGL (deglycyrrhizinated) promotes ulcer healing safely. Antiviral against SARS-CoV, HIV."
aliases: ["licorice", "liquorice", "Glycyrrhiza glabra", "Glycyrrhiza uralensis", "Glycyrrhiza inflata", "glycyrrhizin", "glycyrrhizic acid", "glycyrrhetic acid", "DGL", "deglycyrrhizinated licorice", "gancao", "甘草"]
sources:
  - id: pharmacognosy-textbook
    type: textbook
    cite: "Evans WC. Trease and Evans' Pharmacognosy. 16th ed. Saunders; 2009."
    url: "https://www.elsevier.com/books/trease-and-evans-pharmacognosy/evans/978-0-7020-2933-2"
    accessed: "2026-06-05"
  - id: pubmed-cochrane
    type: review
    cite: "Cochrane Database of Systematic Reviews. Various authors. cochrane.org"
    url: "https://www.cochranelibrary.com/"
    accessed: "2026-06-05"
  - id: cinatl-2003-glycyrrhizin-sars
    type: peer-reviewed
    cite: "Cinatl J, Morgenstern B, Bauer G, et al. Glycyrrhizin, an active component of liquorice roots, and replication of SARS-associated coronavirus. Lancet. 2003;361(9374):2045-6."
    url: "https://doi.org/10.1016/S0140-6736(03)13615-X"
    accessed: "2026-06-05"
  - id: walker-1994-glycyrrhizin-11bhsd
    type: peer-reviewed
    cite: "Walker BR, Edwards CR. Licorice-induced hypertension and syndromes of apparent mineralocorticoid excess. Endocrinol Metab Clin North Am. 1994;23(2):359-77."
    pmid: "8070431"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Glycyrrhetic acid inhibits 11β-HSD2 in renal collecting duct cells, blocking cortisol-to-cortisone conversion. Cortisol activates mineralocorticoid receptors, causing Na+ retention, K+ loss, and hypertension — resembling mineralocorticoid excess."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Pseudo-hyperaldosteronism → hypertension and QT prolongation via hypokalemia. Na+ retention raises BP dose-dependently. Hypokalemia predisposes to ventricular arrhythmias. DGL formulations largely eliminate cardiovascular risk."
  - target: 01-human/06-organ/stomach
    relation: modulates
    note: "DGL stimulates gastric mucus secretion by increasing mucin biosynthesis and prostaglandin E2 production, promoting mucosal barrier integrity and ulcer healing. Comparable to antacid therapy in pilot RCTs; no systemic mineralocorticoid risk."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulates
    note: "By inhibiting 11β-HSD2, glycyrrhetic acid amplifies glucocorticoid receptor activation in mineralocorticoid-target tissues. Glycyrrhizin also binds GR directly, modulating anti-inflammatory transcription of IL-10 and lipocortin-1."
---

# Licorice Root (Glycyrrhiza glabra / G. uralensis)

## Overview

**Glycyrrhiza** (family Fabaceae, subfamily Papilionoideae) is a genus of perennial herbs native to Mediterranean Europe, central Asia, and East Asia. The name derives from Greek *glykys* (sweet) + *rhiza* (root) — reflecting the intensely sweet taste of the dried rhizome and root, which is approximately **50 times sweeter than sucrose** due to glycyrrhizin. The two principal pharmaceutical species are:
- **Glycyrrhiza glabra** (Spanish or Italian licorice): used in European and Western pharmacopoeial preparations; root produces the traditional licorice candy flavour
- **Glycyrrhiza uralensis** (Chinese licorice; *gancao*, 甘草): the dominant species in Traditional Chinese Medicine (TCM); one of the most frequently prescribed herbs in TCM formulas, used as a "harmonising" herb to moderate the effects of other ingredients and for cough, gastric ulcers, and detoxification

**Traditional use**: Licorice root is among the oldest medicinal plants documented — found in Egyptian tombs (Tutankhamun's tomb), prescribed by Dioscorides, Hippocrates, and extensively in TCM and Ayurveda. Historical uses include peptic ulcers, cough/bronchitis, adrenal fatigue, and as a flavouring to mask bitter medicines. These uses align closely with modern mechanistic understanding.

**Primary active constituents**:
- **Glycyrrhizin (glycyrrhizic acid)**: a triterpene saponin consisting of glycyrrhetic acid (18β-glycyrrhetic acid) linked to two glucuronic acid molecules; constitutes 4–20% of dry root weight; responsible for both therapeutic effects and the dose-dependent toxicity profile; hydrolysed by intestinal bacterial β-glucuronidase to **glycyrrhetic acid (GA)** for systemic absorption
- **Glycyrrhetic acid (GA)**: the bioactive aglycone; primary driver of 11β-HSD2 inhibition and glucocorticoid/mineralocorticoid effects; also found as glycyrrhetinic acid in older literature
- **Flavonoids**: liquiritin, isoliquiritin, liquiritigenin, formononetin — anti-inflammatory, antioxidant, and phytoestrogenic activities
- **Chalcones**: isoliquiritigenin — antispasmodic, MAO-A inhibition, AMPK activation

**DGL (Deglycyrrhizinated Licorice)**: a processed form where glycyrrhizin is specifically removed (>97% reduction), producing a preparation retaining the flavonoid/mucilagenic components responsible for mucosal healing but eliminating the mineralocorticoid-excess risk. DGL is used specifically for gastric and peptic ulcer indications.

## Mechanism

### 11β-HSD2 Inhibition — Pseudo-Hyperaldosteronism

This is the clinically most important mechanism, explaining both the therapeutic cortisol-potentiating effect and the dose-dependent toxicity:

**Physiology of 11β-HSD2**:
- The kidney's collecting duct expresses **mineralocorticoid receptors (MR)** that bind both aldosterone and cortisol with equal affinity
- Normally, **11β-hydroxysteroid dehydrogenase type 2 (11β-HSD2)** converts cortisol → cortisone (inactive) in renal cells, protecting MR from cortisol — which circulates at concentrations 100-1000× higher than aldosterone
- This enzymatic inactivation ensures aldosterone remains the primary physiological MR agonist in the kidney

**Glycyrrhetic acid (GA) inhibition**:
- GA is a **potent competitive inhibitor of 11β-HSD2** (Ki ~0.1–1 μM; IC50 ~0.5 μM in renal cell preparations)
- With 11β-HSD2 inhibited, renal cortisol concentrations increase → cortisol activates MR
- **Physiological consequences of sustained MR activation by cortisol**:
  1. **↑ ENaC expression**: Increased epithelial sodium channel density in collecting duct principal cells → Na+ reabsorption
  2. **↑ Na+/K+-ATPase activity**: Enhanced active transport of Na+ out of tubular cells → increased reabsorption
  3. **K+ secretion**: Intracellular K+ depleted as Na+/K+-ATPase pumps Na+ out and K+ in; K+ then secreted via ROMK channels → **hypokalemia**
  4. **Volume expansion**: Na+ retention → osmotic water reabsorption → expanded extracellular volume
  5. **Hypertension**: Increased cardiac output (volume) and increased vascular resistance

This clinical syndrome — hypertension + hypokalemia + low renin + low aldosterone — is called **apparent mineralocorticoid excess (AME) or pseudo-hyperaldosteronism**, and licorice is the most common acquired (non-genetic) cause.

**Dose-response**: The syndrome is dose-dependent and time-dependent:
- Casual confectionery consumption (<50 g/week, low-glycyrrhizin content): typically no significant effect
- High traditional intake (100 mg glycyrrhizin/day ≈ 50–100 g licorice candy/day): clinically significant after weeks
- Medicinal doses of licorice root or glycyrrhizin: effects can emerge within days

### Glucocorticoid and Anti-inflammatory Effects

- **Direct GR interaction**: Glycyrrhizin and GA bind glucocorticoid receptor (GR) with weak agonist activity (Ki ~100–1000× weaker than cortisol); insufficient for direct pharmacological GR agonism at standard doses
- **Cortisol potentiation via 11β-HSD1**: In tissues expressing 11β-HSD1 (liver, adipose, brain), which normally converts cortisone → cortisol (the opposite of 11β-HSD2), GA has inhibitory effects — the net impact on local cortisol levels in these tissues is complex and context-dependent
- **Anti-inflammatory via PLA₂ inhibition**: Glycyrrhizin inhibits phospholipase A₂ (PLA₂) → reduced arachidonic acid liberation → reduced prostaglandin and leukotriene biosynthesis; this mechanism is shared with glucocorticoids, potentially explaining synergism with steroids
- **Transcriptional: NF-κB suppression**: Glycyrrhizin reduces NF-κB activation, decreasing pro-inflammatory cytokine transcription (TNF-α, IL-6) — separate from the 11β-HSD2 mechanism
- **Complement modulation**: Glycyrrhizin inhibits complement activation (alternative pathway), relevant in inflammatory and autoimmune settings

### Antiviral Mechanisms

- **SARS-CoV and SARS-CoV-2**: Cinatl et al. (2003) [^cinatl-2003-glycyrrhizin-sars] demonstrated glycyrrhizin inhibits replication of SARS-associated coronavirus in Vero E6 cells (EC50 ~300 μg/mL); mechanism includes membrane fusion inhibition and possibly viral adsorption interference
- **HIV**: Glycyrrhizin inhibits HIV-1 protease in vitro; may also reduce cell-to-cell HIV transmission; not clinically studied as monotherapy
- **HBV**: Intravenous glycyrrhizin (Stronger Neo-Minophagen C, Japan) has been used for decades for chronic hepatitis B — reduces ALT, inflammation markers; approved in Japan for this indication
- **HSV**: Glycyrrhizin inhibits herpes simplex virus thymidine kinase and viral replication in vitro

### Mucosal Healing Mechanism (DGL)

In DGL preparations (glycyrrhizin removed):
- **Mucus stimulation**: Flavonoid components (liquiritigenin, isoliquiritin) stimulate mucin MUC5AC and MUC5B gene expression in gastric surface mucous cells → increased mucus layer thickness
- **Prostaglandin E₂ (PGE₂) upregulation**: DGL components stimulate constitutive COX-1 in gastric mucosa → increased PGE₂ → mucosal cell proliferation, mucus secretion, and bicarbonate secretion ("mucosal defence")
- **Growth factor upregulation**: Some evidence that DGL promotes epidermal growth factor (EGF) binding and mucosal cell proliferation
- The mechanism is distinct from PPIs/H₂ blockers (which reduce acid production) — DGL instead strengthens mucosal defence

## Clinical Use

### Indications and Dosing

| Indication | Dose / Form | Duration | Evidence Grade |
|:---|:---|:---|:---|
| Peptic / duodenal ulcer (healing) | DGL 380 mg chewed before meals, 3–4×/day | 8–16 weeks | Low-Moderate |
| Gastroesophageal reflux (GERD) | DGL 380–760 mg/meal | Ongoing | Low |
| Chronic hepatitis B (liver protection) | IV glycyrrhizin 40–100 mL/day (SNMC) | Months-years | Moderate (Japan) |
| Addison's disease (adrenal support) | Glycyrrhizin extract (clinical supervision) | Short-term only | Anecdotal |
| Antiviral / respiratory (investigational) | Glycyrrhizin IV or high-dose oral | Variable | Low |
| Canker sores / oral mucositis | DGL mouthwash | 1–2 weeks | Low |

**Critical distinction**: Whole licorice root and glycyrrhizin preparations are NOT interchangeable with DGL. DGL is the only form appropriate for self-medication without cardiovascular monitoring.

**Safe daily limit for glycyrrhizin**: WHO/EMEA guidelines suggest ≤100 mg/day glycyrrhizin as an upper limit for long-term intake. European Food Safety Authority (EFSA) notes that 100 mg/day can cause hypertension in sensitive individuals.

### Drug Interactions

- **Antihypertensives**: Glycyrrhizin antagonises the effect of all antihypertensive drug classes (BP raises despite therapy); **clinically important monitoring issue**
- **Diuretics (thiazides, loop)**: Additive potassium loss → severe hypokalemia; digoxin toxicity risk from hypokalemia
- **Corticosteroids**: Synergistic effect — glycyrrhizin inhibits corticosteroid metabolism (11β-HSD), prolonging steroid activity; may increase both therapeutic effects and adverse effects
- **Digoxin**: Hypokalemia from glycyrrhizin → increased digoxin toxicity risk (digoxin sensitivity is K+-dependent)
- **Warfarin**: Some licorice flavonoids modulate CYP2C9; inconsistent data; monitor INR with high-dose preparations
- **Spironolactone**: Competitive MR antagonism may diminish glycyrrhizin's mineralocorticoid effect — pharmacodynamic antagonism

### Contraindications

- **Absolute** (whole licorice / glycyrrhizin-containing preparations): hypertension, heart failure, kidney disease, hypokalemia, hepatic cirrhosis, pregnancy (inhibits 11β-HSD1 in placenta, potentially reducing protective cortisone in foetal compartment)
- **Relative**: concurrent diuretic use; concurrent corticosteroid use without monitoring; oedematous states
- **DGL**: generally safe; avoid in known allergy to Fabaceae (legume family); monitor for rare GI intolerance

### Monitoring

For patients using glycyrrhizin-containing preparations:
- Blood pressure monitoring at baseline and every 2–4 weeks
- Serum potassium every 4 weeks (target K+ >3.5 mmol/L)
- ECG monitoring if K+ falls below 3.0 mmol/L (QT prolongation risk)
- Renin and aldosterone levels (suppressed in pseudo-hyperaldosteronism — helpful diagnostically)

## Evidence

### Peptic Ulcer / GI Mucosal Healing

DGL clinical evidence:
- **Glick et al. (1982)**: RCT, n=100, DGL 760 mg three times daily vs. cimetidine 200 mg three times daily for 12 weeks in peptic ulcer — endoscopic healing rates: DGL 78% vs. cimetidine 60%; symptom improvement similar
- **Morgan et al. (1982)**: Maintenance study, n=92, DGL 380 mg vs. antacid maintenance — similar relapse rates
- **Limitations**: Small trials; not replicated in modern RCTs with placebo control; endoscopy criteria not standardised
- **GRADE evidence**: Low (small trials, methodological limitations, not replicated); DGL is not first-line therapy per current gastroenterology guidelines (PPIs are standard of care for peptic ulcer)

### Chronic Hepatitis B — IV Glycyrrhizin (Japan)

Stronger Neo-Minophagen C (SNMC) — IV glycyrrhizin 0.2% solution + glycine + cysteine:
- Long-term use in Japan (licensed indication for chronic hepatitis) over 20+ years; observational data suggest sustained ALT reduction and reduced fibrosis progression
- A retrospective cohort (Arase et al., 1997, n=453 over 10 years): reduced hepatocellular carcinoma incidence vs. untreated controls
- **Limitation**: No placebo-controlled RCT of adequate size; regulatory approval based on cohort and open-label data

### SARS-CoV-1 (Historical)

Cinatl et al. (2003) [^cinatl-2003-glycyrrhizin-sars] — in vitro study of SARS-CoV in Vero E6 cells:
- Glycyrrhizin had the greatest anti-SARS-CoV activity among a panel of known antivirals tested (including ribavirin, mycophenolic acid, interferon)
- EC50 ~300 μg/mL — achievable in lung tissue only with IV administration
- **Clinical translation**: No clinical RCT was completed; SARS epidemic ended before trials could be organised
- Cited extensively during COVID-19 pandemic as background for glycyrrhizin research; no definitive COVID-19 clinical trial data

### 11β-HSD2 / Hypertension Mechanism Evidence

Walker and Edwards (1994) [^walker-1994-glycyrrhizin-11bhsd] — comprehensive clinical review establishing the mechanism:
- Volunteers consuming 100 g licorice/day (glycyrrhizin content ~150 mg/day) for 2–4 weeks develop measurable hypertension (+15 mmHg systolic), hypokalemia (−0.4 mmol/L), suppressed renin and aldosterone
- GA and glycyrrhizin directly inhibit 11β-HSD2 activity in renal cortical cells (confirmed in vivo using urinary cortisol:cortisone ratio as a biomarker — ratio increases 3–10 fold with licorice consumption, directly quantifying 11β-HSD2 inhibition)
- Case reports describe severe hypokalemia (K+ <2.0 mmol/L), rhabdomyolysis, and hypertensive emergencies from high licorice confectionery or supplement intake

### Evidence Gaps

- No large placebo-controlled RCT for DGL vs. PPI-equivalent for peptic ulcer healing (would require significant resource investment but is feasible)
- Glycyrrhizin antiviral potential (HBV, COVID-19) requires adequately powered clinical trials
- Safe long-term dose for glycyrrhizin in individuals with borderline BP not well established
- Interaction between licorice and genetic variants in 11β-HSD2 (which cause congenital AME) is not characterised

## Connections

- **Modulates** → [Kidney](../../../../../01-human/06-organ/kidney/README.md): Glycyrrhetic acid (GA) inhibits 11β-HSD2 in the renal cortical collecting duct, blocking the local inactivation of cortisol to cortisone. Unmetabolised cortisol then activates mineralocorticoid receptors, increasing ENaC expression, Na+ reabsorption, K+ secretion, and plasma volume — producing the classic pseudo-hyperaldosteronism syndrome of hypertension and hypokalemia.

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): Pseudo-hyperaldosteronism from 11β-HSD2 inhibition elevates blood pressure dose-dependently via Na+ retention and volume expansion. Consequent hypokalemia prolongs the QT interval and predisposes to ventricular arrhythmias, including torsades de pointes. DGL formulations (glycyrrhizin removed) largely eliminate this cardiovascular toxicity risk.

- **Modulates** → [Stomach](../../../../../01-human/06-organ/stomach/README.md): DGL (deglycyrrhizinated licorice) stimulates gastric surface mucous cells to increase mucin biosynthesis and promotes prostaglandin E₂ production via COX-1, strengthening the mucosal defence barrier and accelerating peptic ulcer healing. Unlike acid-suppressing drugs, DGL acts through cytoprotective mucosal defence mechanisms without systemic mineralocorticoid risk.

- **Modulates** → [Glucocorticoid Receptor](../../../../../01-human/03-molecular/glucocorticoid-receptor/README.md): By inhibiting renal 11β-HSD2, glycyrrhetic acid amplifies cortisol availability at mineralocorticoid receptors (which have equal affinity for cortisol and aldosterone) in renal and other target tissues. GA and glycyrrhizin additionally bind GR directly with weak agonist affinity, modulating transcription of anti-inflammatory target genes including IL-10 and lipocortin-1, contributing to the systemic anti-inflammatory profile.

---

[^cinatl-2003-glycyrrhizin-sars]: Cinatl J, et al. Lancet. 2003;361(9374):2045-6. doi:10.1016/S0140-6736(03)13615-X
[^walker-1994-glycyrrhizin-11bhsd]: Walker BR, Edwards CR. Endocrinol Metab Clin North Am. 1994;23(2):359-77. PMID:8070431
