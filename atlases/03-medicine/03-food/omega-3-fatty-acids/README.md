---
schema: medicine-entry/v1
id: omega-3-fatty-acids
name: Omega-3 Fatty Acids
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Long-chain n-3 PUFA: EPA (C20:5) and DHA (C22:6) from cold-water fish; ALA (C18:3) from plants. EPA/DHA reduce TG 30–50%, decrease platelet aggregation, modulate eicosanoid and SPM synthesis. REDUCE-IT: EPA 4 g/d → −25% MACE. Anti-inflammatory at pharmacological doses."
aliases: ["omega-3 fatty acids", "omega-3", "n-3 PUFA", "EPA", "DHA", "ALA", "eicosapentaenoic acid", "docosahexaenoic acid", "alpha-linolenic acid", "fish oil", "icosapentaenoic acid", "Vascepa", "Lovaza", "Omacor"]
sources:
  - id: bhatt-2019-reduce-it
    type: peer-reviewed
    cite: "Bhatt DL, Steg PG, Miller M, et al. Cardiovascular Risk Reduction with Icosapentaenoic Acid for Hypertriglyceridemia (REDUCE-IT). N Engl J Med. 2019;380(1):11-22."
    doi: "10.1056/NEJMoa1812792"
    pmid: "30415628"
    url: "https://doi.org/10.1056/NEJMoa1812792"
  - id: calder-2017-omega3-inflammation
    type: peer-reviewed
    cite: "Calder PC. Omega-3 fatty acids and inflammatory processes: from molecules to man. Biochem Soc Trans. 2017;45(5):1105-15."
    doi: "10.1042/BST20160474"
    pmid: "28900017"
    url: "https://doi.org/10.1042/BST20160474"
  - id: mozaffarian-2011-omega3-cvd
    type: peer-reviewed
    cite: "Mozaffarian D, Wu JH. Omega-3 fatty acids and cardiovascular disease: effects on risk factors, molecular pathways, and clinical events. J Am Coll Cardiol. 2011;58(20):2047-67."
    doi: "10.1016/j.jacc.2011.06.063"
    pmid: "22051327"
    url: "https://doi.org/10.1016/j.jacc.2011.06.063"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: calder-2017-omega3-inflammation
    note: "EPA competes with arachidonic acid (AA, n-6) for COX-1/2 and 5-LOX enzymes. Substitution of AA with EPA in the substrate pool shifts prostaglandin synthesis from PGE₂ (pro-inflammatory, high potency) to PGE₃ (weak potency), and from LTB₄ to LTB₅ (100× less potent chemotaxis). The resulting reduction in inflammatory signalling lowers IL-6, IL-1β, and TNF-α production in macrophages and endothelial cells. EPA/DHA also generate specialised pro-resolving mediators (SPMs: resolvins, protectins, maresins) that actively resolve inflammation."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    evidence: bhatt-2019-reduce-it
    note: "High-dose icosapentaenoic acid (EPA; Vascepa 4 g/day) in the REDUCE-IT trial reduced major adverse cardiovascular events (MACE) by 25% and cardiovascular death by 20% over 4.9 years in hypertriglyceridaemic patients on statins. Beyond triglyceride reduction, proposed mechanisms include membrane stabilisation, anti-atherosclerotic plaque effects, anti-arrhythmic properties, and endothelial function improvement. Standard-dose fish oil (1 g/day) does not produce equivalent cardiovascular event reduction."
  - target: 01-human/06-organ/heart
    relation: treats
    evidence: mozaffarian-2011-omega3-cvd
    note: "Omega-3 FAs reduce triglycerides 30–50% at pharmacological doses (≥2 g EPA+DHA/day), decrease platelet aggregation (reduced TXA₂ synthesis), lower resting heart rate, improve heart rate variability, reduce cardiac hypertrophy, improve diastolic function in epidemiological and RCT data. At 4 g/day, EPA reduces atrial fibrillation burden and reduces sudden cardiac death risk in post-MI patients. DHA but not EPA increases LDL-C at high doses — clinically relevant distinction when selecting pure EPA vs. combined EPA/DHA preparations."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "EPA/DHA shifts macrophage eicosanoids from LTB₄/PGE₂ to weaker LTB₅/PGE₃; EPA/DHA-derived SPMs (resolvins, protectins, maresins) promote efferocytosis and resolve inflammation; GPR120-β-arrestin signaling reduces M1 polarization and suppresses IL-1β/TNF-α production."
  - target: 01-human/03-molecular/nf-kb
    relation: inhibits
    note: "EPA/DHA suppress NF-κB activation via GPR120 → β-arrestin-2-mediated TAB1 sequestration; membrane EPA/DHA disrupts TLR4 lipid raft clustering; PPARα activation competes with NF-κB for CBP/p300 coactivators; net effect: reduced transcription of IL-6, IL-1β, TNF-α, COX-2."
  - target: 01-human/06-organ/kidney
    relation: treats
    note: "Omega-3s slow IgA nephropathy at 3.6-4 g/day; EPA/DHA reduce renal lipid accumulation and TGF-β fibrosis in diabetic nephropathy; anti-proteinuric via reduced VEGF and mesangial proliferation; renal SPM production promotes glomerular inflammation resolution."
---

# Omega-3 Fatty Acids

## Overview

**Omega-3 fatty acids** (n-3 polyunsaturated fatty acids, PUFAs) are a family of long-chain lipids defined by the position of the first carbon-carbon double bond at the omega-3 (n-3) position from the methyl end of the fatty acid chain. The three clinically relevant members are:

- **ALA** (alpha-linolenic acid, C18:3n-3): the essential plant-derived omega-3; found in flaxseed, chia seeds, walnuts, and canola oil; cannot be synthesised by humans and must be obtained from diet
- **EPA** (eicosapentaenoic acid, C20:5n-3): long-chain omega-3 with 5 double bonds; primary anti-inflammatory and cardiovascular active form; synthesised from ALA in humans at <5–15% efficiency (often <5% in practice)
- **DHA** (docosahexaenoic acid, C22:6n-3): 6 double bonds; critical structural component of neural and retinal cell membranes; accounts for ~40% of fatty acids in the brain's grey matter

**Dietary sources:**
- EPA and DHA: oily cold-water fish (salmon, mackerel, sardines, herring, anchovies), algae (the primary producer in the marine food chain), krill
- ALA: flaxseed (~55% ALA), chia seeds (~60% ALA), walnuts (~13%), canola and soybean oils

Western diets have dramatically shifted the n-6:n-3 ratio — estimated at **15–20:1** in contemporary diets vs. an estimated evolutionary ratio of 1:1 to 4:1. This ratio imbalance shifts arachidonic acid (AA, n-6) metabolism toward pro-inflammatory eicosanoids, forming the biochemical rationale for therapeutic omega-3 supplementation.

**Pharmacological preparations:**
- **Prescription icosapentaenoic acid (IPE/EPA):** Vascepa (AMR101) — pure EPA ethyl ester; 4 g/day for hypertriglyceridaemia
- **Prescription EPA+DHA:** Lovaza/Omacor — EPA+DHA ethyl esters 4 g/day; FDA-approved for severe hypertriglyceridaemia (≥500 mg/dL)
- **Over-the-counter fish oil:** Variable EPA+DHA content; typically 180 mg EPA + 120 mg DHA per 1 g capsule (30% omega-3); quality varies substantially between brands
- **Algal omega-3:** Vegan source of EPA and DHA derived from marine microalgae; bioavailable and increasingly recommended as equivalent source

## Mechanism

### Membrane Incorporation and Competitive Displacement

The fundamental mechanism of omega-3 fatty acid action operates at the **phospholipid membrane level**:

1. Dietary EPA and DHA are incorporated into cell membrane phospholipids (primarily phosphatidylcholine and phosphatidylethanolamine) at the *sn-2* position, **displacing arachidonic acid (AA, n-6)**
2. The degree of substitution is proportional to EPA/DHA intake and inversely proportional to dietary n-6 intake — this is why the n-6:n-3 ratio matters, not absolute omega-3 intake alone
3. Membrane incorporation alters **lipid raft** composition, affecting receptor clustering, transmembrane signalling, and ion channel conductance

### Eicosanoid Competition (AA → EPA Substrate Shift)

When inflammatory stimuli trigger phospholipase A₂ (PLA₂), the fatty acid released from sn-2 position is determined by what is incorporated:

| Enzyme | AA-derived product | EPA-derived product | Relative potency |
|:---|:---|:---|:---|
| COX-1/2 | PGE₂, PGI₂, TXA₂ | PGE₃, PGI₃, TXA₃ | EPA products 10–100× weaker |
| 5-LOX | LTB₄, LTC₄ | LTB₅, LTC₅ | EPA products 10–100× weaker |

The shift from high-potency AA-derived eicosanoids to weaker EPA-derived equivalents reduces:
- Platelet aggregation (TXA₂ → TXA₃)
- Vasoconstriction (PGE₂/TXA₂ → weaker EPA counterparts)
- Neutrophil chemotaxis (LTB₄ → LTB₅)
- Pro-inflammatory cytokine production (IL-6, IL-1β, TNF-α) via reduced prostaglandin-driven inflammatory signalling [^calder-2017-omega3-inflammation]

### Specialised Pro-Resolving Mediators (SPMs)

EPA and DHA are substrate for biosynthesis of a family of lipid mediators that actively **resolve** (not just reduce) inflammation:

- **Resolvins (E-series from EPA, D-series from DHA):** Inhibit neutrophil transmigration, promote macrophage phagocytosis of apoptotic cells (efferocytosis), accelerate resolution
- **Protectins (neuroprotectin D1 from DHA):** Neuroprotective; reduces neuroinflammation
- **Maresins (from DHA):** Enhance macrophage phagocytosis; tissue regeneration signalling

SPMs represent a conceptual shift — omega-3s don't merely dampen inflammation but promote its **active resolution**, which is physiologically distinct from simple anti-inflammatory suppression.

### Triglyceride-Lowering Mechanism

At pharmacological doses (≥2 g EPA+DHA/day):
- EPA/DHA activate **PPARα** (peroxisome proliferator-activated receptor α) in liver → increases hepatic fatty acid β-oxidation gene expression
- Suppress **SREBP-1c** → reduces de novo lipogenesis
- Reduce VLDL secretion from hepatocytes (reduces triglyceride packaging into VLDL)
- Enhance LPL (lipoprotein lipase) activity → increased peripheral triglyceride clearance

Net result: **30–50% triglyceride reduction** at 4 g/day — the most potent non-pharmacological (and comparable to fibrates) triglyceride-lowering intervention.

**Caveat — DHA increases LDL-C:** DHA but not pure EPA increases LDL-C by ~5–10% (mechanism: increased LDL particle size and reduced LDL catabolism), which partially offsets cardiovascular benefit of combined EPA+DHA formulations vs. pure EPA; this mechanistic difference underlies the different cardiovascular trial outcomes (REDUCE-IT with pure EPA vs. STRENGTH/OMEMI with combined EPA+DHA).

### Cardiac Electrophysiology

- EPA/DHA incorporate into cardiomyocyte membranes → alter Nav1.5 (cardiac sodium channel) gating kinetics → reduce sodium current → reduced automaticity and reduced risk of triggered activity
- This anti-arrhythmic mechanism (confirmed in in vitro and animal studies) is the proposed basis for omega-3 reduction of sudden cardiac death in post-MI patients; clinical evidence is supportive in epidemiological studies but less consistent in more recent RCTs

## Clinical Use

### Indications and Dosing

| Indication | Agent | Dose | Evidence quality |
|:---|:---|:---|:---|
| Severe hypertriglyceridaemia (≥500 mg/dL) | Prescription EPA+DHA (Lovaza) | 4 g/day | High (FDA-approved) |
| Cardiovascular risk reduction in hypertriglyceridaemia on statins | Pure EPA (Vascepa) | 4 g/day | High (REDUCE-IT) |
| General CV risk reduction (primary prevention) | OTC fish oil | 1–2 g/day EPA+DHA | Low-moderate (inconsistent) |
| Heart failure (adjunct) | EPA+DHA | 1 g/day | Moderate (GISSI-HF) |
| IgA nephropathy | EPA+DHA | 3.6–4 g/day | Low-moderate |
| Dry eye disease | EPA+DHA | 2–4 g/day | Low-moderate |

**Dietary recommendations:**
- AHA 2021: ≥2 servings oily fish/week for general population (~500 mg/day EPA+DHA); higher in specific cardiovascular conditions
- WHO: ALA ≥0.5% total energy; EPA+DHA ≥250 mg/day

### Drug Interactions and Safety

- **Anticoagulants / antiplatelets:** Omega-3s inhibit TXA₂-mediated platelet aggregation; additive bleeding risk with warfarin, aspirin, P2Y12 inhibitors; monitor INR; clinically significant at doses ≥3 g/day
- **Blood pressure medications:** Additive antihypertensive effect (omega-3s reduce blood pressure modestly); generally beneficial, not a contraindication
- **Orlistat:** Reduces absorption of fat-soluble nutrients including omega-3s; separate doses by 2 hours
- **General safety:** Fishy breath, GI upset, and burping common with standard fish oil capsules; pure EPA and enteric-coated formulations reduce these effects; hepatotoxicity is very rare; high doses (>3 g/day) may suppress immune responses slightly

## Evidence

### REDUCE-IT (2018–2019) — Landmark Trial

Bhatt et al. (2019) [^bhatt-2019-reduce-it] — RCT, n=8,179, statin-treated patients with fasting TG 135–499 mg/dL and established CVD or diabetes plus risk factors:
- **Icosapentaenoic acid (Vascepa) 4 g/day** vs. mineral oil placebo for median 4.9 years
- Primary MACE: **−25%** relative risk reduction (HR 0.75; 95% CI: 0.68–0.83; p<0.001)
- CV death: **−20%** (HR 0.80; p=0.03)
- Fatal/non-fatal MI: **−31%**; stroke: **−28%**
- Triglyceride reduction: −18.3% from baseline vs. placebo
- NNT for primary endpoint: 21 over 5 years
- **Controversies:** Mineral oil placebo may have increased LDL-C and CRP in controls (not inert); effect size larger than expected from TG reduction alone; placebo-arm LDL-C increase at 1 year (~2.2 mg/dL) may partially explain the benefit
- **STRENGTH trial** (EPA+DHA combination, corn oil placebo): no significant cardiovascular benefit; reinforces the pure EPA vs. combined EPA/DHA distinction

### Triglyceride Lowering (Meta-analytic Evidence)

Multiple meta-analyses confirm:
- EPA+DHA ≥2 g/day: TG reduction **−25 to −35%** in hypertriglyceridaemia
- EPA+DHA 4 g/day: TG reduction **40–50%** in severe hypertriglyceridaemia
- Effects are dose-dependent and consistent across populations [^mozaffarian-2011-omega3-cvd]

### Anti-Inflammatory Evidence

Calder (2017) [^calder-2017-omega3-inflammation] systematic review:
- Omega-3 supplementation consistently reduces CRP, IL-6, and TNF-α in inflammatory conditions
- Effect sizes are modest at dietary doses (~1 g/day) but meaningful at pharmacological doses (≥3 g/day)
- SPM generation confirmed in human studies following EPA/DHA supplementation
- GRADE: **Moderate** for CRP reduction; **Low** for clinical inflammatory disease outcomes

### Primary Cardiovascular Prevention (Inconsistent Evidence)

ASCEND (2018), VITAL (2019) — large RCTs in primary prevention populations using 1 g/day EPA+DHA:
- No significant reduction in MACE in general population
- Significant reduction in cancer mortality in VITAL (unexpected secondary finding)
- Suggests **dose and population risk** are critical: benefit concentrated in high-TG, high-CV-risk patients at pharmacological doses

## Connections

- **Modulates** → [IL-6](../../../../../01-human/03-molecular/il-6/README.md): Competitive displacement of arachidonic acid from membrane phospholipids shifts prostaglandin and leukotriene production toward weaker EPA-derived eicosanoids (PGE₃, LTB₅), reducing the IL-6 and TNF-α transcriptional response to inflammatory stimuli. SPM biosynthesis (resolvins E/D, protectins, maresins) from EPA and DHA further promotes inflammation resolution rather than mere suppression. This mechanism is relevant at pharmacological doses (≥2 g/day EPA+DHA); at dietary doses (250–500 mg/day), anti-inflammatory effects are modest.

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): REDUCE-IT established that icosapentaenoic acid 4 g/day reduces MACE by 25% and cardiovascular death by 20% in high-risk, statin-treated, hypertriglyceridaemic patients. Mechanisms include triglyceride reduction, reduced platelet aggregation, anti-arrhythmic membrane effects, plaque stabilisation via reduced oxidative stress, and improved endothelial nitric oxide synthesis. Standard-dose fish oil (1 g/day) does not replicate these benefits in primary prevention populations.

- **Treats** → [Heart](../../../../../01-human/06-organ/heart/README.md): At pharmacological doses, omega-3 FAs reduce cardiac triglyceride content, improve cardiomyocyte membrane fluidity (DHA), reduce arrhythmia susceptibility through sodium channel modulation (EPA), reduce resting heart rate and improve heart rate variability, and decrease cardiac hypertrophy in animal models. GISSI-HF demonstrated a 9% relative risk reduction in all-cause mortality with 1 g/day omega-3 in systolic heart failure, though the signal is smaller than in REDUCE-IT.
- `modulates` → **[Macrophage](../../../../../01-human/04-cellular/macrophage/README.md)** — EPA/DHA shifts macrophage eicosanoids from LTB₄/PGE₂ to weaker LTB₅/PGE₃; EPA/DHA-derived SPMs (resolvins, protectins, maresins) promote macrophage efferocytosis and inflammation resolution; GPR120-β-arrestin signaling reduces M1 polarization and suppresses IL-1β/TNF-α.
- `inhibits` → **[NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md)** — EPA/DHA suppress NF-κB activation via GPR120 → β-arrestin-2-mediated TAB1 sequestration; membrane EPA/DHA disrupts TLR4 lipid raft clustering; PPARα activation competes with NF-κB for CBP/p300 coactivators → reduced IL-6, IL-1β, TNF-α, COX-2 transcription.
- `treats` → **[Kidney](../../../../../01-human/06-organ/kidney/README.md)** — Omega-3s slow IgA nephropathy at 3.6-4 g/day; EPA/DHA reduce renal lipid accumulation and TGF-β fibrosis in diabetic nephropathy; anti-proteinuric via reduced VEGF and mesangial proliferation; renal SPM production promotes glomerular inflammation resolution.

[^bhatt-2019-reduce-it]: Bhatt DL et al. N Engl J Med. 2019;380(1):11-22. doi:10.1056/NEJMoa1812792
[^calder-2017-omega3-inflammation]: Calder PC. Biochem Soc Trans. 2017;45(5):1105-15. doi:10.1042/BST20160474
[^mozaffarian-2011-omega3-cvd]: Mozaffarian D, Wu JH. J Am Coll Cardiol. 2011;58(20):2047-67. doi:10.1016/j.jacc.2011.06.063

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
