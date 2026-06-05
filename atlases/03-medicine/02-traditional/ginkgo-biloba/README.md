---
schema: medicine-entry/v1
id: ginkgo-biloba
name: Ginkgo biloba (EGb 761)
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Standardized Ginkgo biloba leaf extract (EGb 761). Ginkgolide B antagonizes PAF; flavonoids scavenge ROS and boost NO-mediated vasodilation. Modest evidence for dementia, claudication, tinnitus. Antiplatelet: caution with warfarin/aspirin."
aliases: ["ginkgo", "EGb 761", "ginkgo biloba", "maidenhair tree", "bai guo ye", "Ginkgophyta leaf extract", "ginkgolide", "bilobalide"]
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
  - id: birks-2009-cochrane-ginkgo
    type: review
    cite: "Birks J, Evans JG. Ginkgo biloba for cognitive impairment and dementia. Cochrane Database Syst Rev. 2009;(1):CD003120."
    url: "https://doi.org/10.1002/14651858.CD003120.pub3"
    accessed: "2026-06-05"
  - id: weinmann-2010-ginkgo-dementia
    type: peer-reviewed
    cite: "Weinmann S, Roll S, Schwarzbach C, et al. Effects of Ginkgo biloba in dementia. BMC Geriatr. 2010;10:14."
    url: "https://doi.org/10.1186/1471-2318-10-14"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "EGb 761 increases cerebral blood flow via PAF antagonism and NO-mediated vasodilation. Flavonoid antioxidants reduce neuronal oxidative damage. Cochrane: modest, inconsistent cognitive benefit in mild-moderate dementia vs. placebo."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "EGb 761 improves mitochondrial function and reduces amyloid-beta neurotoxicity in vitro. Ginkgolide J inhibits neuronal apoptosis. Trials show limited but measurable improvements in attention and working memory in cognitively impaired elderly."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Ginkgolide B antagonizes PAF, reducing platelet aggregation and thrombus risk. Flavonoids boost NO synthase → vasodilation, improving peripheral blood flow in claudication. Antiplatelet activity raises bleeding risk with warfarin/aspirin co-use."
  - target: 01-human/04-cellular/platelet
    relation: modulates
    note: "Ginkgolide B competitively antagonizes PAF at its receptor, inhibiting platelet aggregation and degranulation. May reduce thromboxane synthesis. Combined antiplatelet activity contraindicates use with anticoagulants without physician oversight."
---

# Ginkgo biloba (EGb 761)

## Overview

**Ginkgo biloba** is the sole surviving species of the division Ginkgophyta — a "living fossil" with an unbroken fossil record extending 270 million years. The fan-shaped leaves of the deciduous tree are the pharmacological source. Cultivated extensively in China, South Korea, France (Bordeaux region), and the United States, it is one of the world's highest-selling herbal supplements by volume.

**Traditional use** spans over 2,000 years in Chinese medicine: leaves for cardiovascular support, seeds (bai guo) for respiratory and urinary complaints. Seeds contain **ginkgotoxin** (4'-methoxypyridoxine), a neurotoxin that antagonises pyridoxine (vitamin B6) and can cause seizures; raw or excessive seed ingestion is dangerous. Medicinal preparations uniformly use **leaf extract**, not seeds.

The modern pharmaceutical-grade preparation is **EGb 761** (Dr. Willmar Schwabe GmbH), standardised to:
- **24% flavonol glycosides**: predominantly quercetin, kaempferol, and isorhamnetin glycosides — the antioxidant fraction
- **6% terpene lactones**: ginkgolides A, B, C, J (diterpenes) and bilobalide (sesquiterpene) — the vasoactive/PAF-antagonist fraction

This standardisation is critical: non-standardised preparations may lack the bioactive terpene lactone fraction and have not been validated in clinical trials.

**Global use**: Ginkgo is the most widely prescribed herbal medicine in Germany and France (licensed as a pharmaceutical), and among the top-selling botanical supplements in the United States. Annual global market exceeds $1 billion. Primary indications driving use: age-related cognitive decline, dementia, peripheral arterial disease (claudication), tinnitus, and altitude sickness.

Ginkgo's popularity has driven substantial clinical trial investment, and it is one of the few botanical medicines with multiple systematic reviews and large RCTs — making its evidence profile better characterised than most traditional medicines, though the overall clinical effect remains modest and inconsistently demonstrated.

## Mechanism

### Platelet-Activating Factor (PAF) Antagonism — Ginkgolide B

The most pharmacologically specific mechanism is **ginkgolide B's competitive antagonism of the PAF receptor** (PAFR, a Gi-coupled GPCR):
- PAF (1-O-alkyl-2-acetyl-sn-glycero-3-phosphocholine) is a potent lipid mediator promoting platelet aggregation, neutrophil activation, bronchoconstriction, and vasodilation at physiological concentrations
- Ginkgolide B structurally mimics PAF at the lipophilic binding pocket of PAFR, blocking PAF-induced platelet aggregation and degranulation (IC50 approximately 0.5–2 μM)
- Clinical consequence: reduced platelet thrombus formation; increased bleeding time; clinically significant interaction potential with anticoagulants and antiplatelet drugs
- Ginkgolides A, C, and J show weaker but additive PAF antagonism

### Antioxidant Activity — Flavonol Glycosides

Quercetin, kaempferol, and isorhamnetin glycosides:
- **Direct radical scavenging**: catechol ring donates electrons to quench superoxide (O₂⁻), hydroxyl radical (OH•), and lipid peroxyl radicals; electron spin resonance studies confirm reduction in ROS signal
- **Mitochondrial protection**: ginkgo flavonoids reduce mitochondrial ROS generation (Complex I/III leakage) and prevent cytochrome c release triggered by oxidative stress
- **NO bioavailability**: flavonoids inhibit superoxide-mediated NO quenching → increased endothelial NO → vasodilation

### Nitric Oxide–Mediated Vasodilation

- EGb 761 upregulates endothelial NOS (eNOS) expression and activity, increasing NO production in vascular endothelium
- Reduced superoxide (via antioxidant flavonoids) preserves NO half-life
- Result: cerebral and peripheral vasodilation → increased blood flow to ischaemic tissue → partial mechanistic basis for claudication and cognitive blood-flow effects

### Neuroprotective Mechanisms

- **Anti-apoptotic**: Ginkgolide J inhibits apoptosis-inducing factor (AIF) release from mitochondria; bilobalide inhibits NMDA receptor-mediated excitotoxicity
- **Amyloid antagonism**: flavonoids inhibit amyloid-β aggregation in vitro (inhibition of β-sheet formation) and reduce amyloid-induced mitochondrial dysfunction
- **Mitochondrial biogenesis**: EGb 761 stimulates PGC-1α → increased mitochondrial density and ATP production in neuronal cell lines
- **Monoamine modulation**: weak inhibition of MAO-A and MAO-B has been reported but is not considered a primary mechanism

## Clinical Use

### Indications and Dosing

| Indication | Standard Dose | Duration Studied | Evidence Grade |
|:---|:---|:---|:---|
| Dementia (Alzheimer's / vascular) | EGb 761 120–240 mg/day | 12–52 weeks | Low-Moderate |
| Peripheral arterial disease / claudication | EGb 761 120–160 mg/day | 12–24 weeks | Moderate |
| Tinnitus | EGb 761 120–160 mg/day | 12 weeks | Low |
| Altitude sickness (prophylaxis) | 80–120 mg twice daily | Started 2 days before ascent | Low (contradictory) |
| Normal age-related memory decline | 120 mg/day | 12–24 weeks | Low (inconsistent) |

The only clinically validated standardised extract is **EGb 761**. Doses used in well-designed trials range from 120–240 mg/day in two divided doses. Non-standardised ginkgo supplements cannot be assumed equivalent.

### Drug Interactions (Clinically Significant)

- **Warfarin/anticoagulants**: Ginkgolide B PAF antagonism and antiplatelet activity → additive bleeding risk; **case reports of clinically significant bleeding**; INR monitoring essential
- **Aspirin/NSAIDs/clopidogrel**: Additive antiplatelet effects; increased spontaneous bleeding risk
- **Anticonvulsants (phenytoin, carbamazepine)**: Ginkgo may lower seizure threshold (mechanism unclear; separate from seed ginkgotoxin); clinical relevance uncertain
- **CYP2C9 substrates**: Ginkgo modestly inhibits CYP2C9 in vitro; clinical significance for warfarin (a CYP2C9 substrate) unclear but adds to the interaction concern
- **Trazodone**: Case report of coma in an Alzheimer's patient co-prescribed ginkgo and trazodone — mechanism unknown; caution advised

### Contraindications and Safety

- **Absolute**: Known hypersensitivity to ginkgo; concurrent use of anticoagulants in patients at high bleeding risk; **raw ginkgo seed ingestion (ginkgotoxin risk)**
- **Relative**: Pre-operative use (discontinue 2–3 weeks before surgery); pregnancy (theoretical uterotonic effect of ginkgolides); concurrent SSRI/MAOI use (case reports of serotonin-like reactions)
- **Common adverse effects**: Headache, GI upset, dizziness, allergic skin reactions; spontaneous subdural haematoma reported rarely
- **Ginkgolic acids**: Raw leaf preparations may contain ginkgolic acids (potent skin sensitisers; potentially mutagenic); pharmaceutical EGb 761 has ginkgolic acids removed to <5 ppm

## Evidence

### Cochrane Review — Cognitive Impairment and Dementia

Birks and Evans (2009) [^birks-2009-cochrane-ginkgo] — 36 trials included in systematic review; 9 trials (n>200, EGb 761 use confirmed, duration ≥24 weeks) considered higher quality:
- Heterogeneity was high across all outcomes
- **Cognition** (MMSE, ADAS-Cog): Small improvements vs. placebo (SMD ~−0.2 to −0.5); statistically significant in some individual trials, not consistently across review
- **Function (ADLs)**: Some positive trials; overall evidence weak
- **Mood/emotional function**: Some positive signal
- **Conclusion**: "No convincing evidence that Ginkgo biloba is efficacious for dementia or cognitive impairment"
- **Update (post-2009 evidence)**: The GIEM trial (2012, n=3069, GuidAge study) — EGb 761 240 mg/day for 5 years in elderly with memory concerns — found no reduction in Alzheimer's disease conversion rate (HR 0.84, 95% CI 0.60–1.18, p=0.306), the largest single negative trial

### Peripheral Arterial Disease (Claudication)

Weinmann et al. (2010) [^weinmann-2010-ginkgo-dementia] and earlier meta-analyses:
- EGb 761 120–160 mg/day for 12–24 weeks improves **pain-free walking distance** by 30–100 metres vs. placebo in patients with intermittent claudication
- Comparable to pentoxifylline in some head-to-head trials
- **Grade: Moderate** — consistent direction across RCTs; effect clinically modest but reproducible
- Not a first-line therapy per vascular guidelines, but an option where pharmacological alternatives are not tolerated

### Tinnitus

Evidence is weak and inconsistent:
- Individual RCTs show benefit; pooled analyses do not reliably confirm superiority to placebo
- A systematic review by Drew and Davies (2001) found no significant benefit in placebo-controlled trials
- **Grade: Low** — insufficient evidence to recommend for tinnitus as a primary indication

### Evidence Quality Limitations

- Most dementia trials use surrogate cognitive outcomes, not hard clinical endpoints (delay to diagnosis, long-term function)
- Bioavailability of EGb 761 in different patient populations is not well characterised
- Publication bias toward positive findings in older literature
- Lack of large trials in non-Asian populations for claudication

## Connections

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): EGb 761 increases cerebral blood flow via PAF antagonism (ginkgolide B) and NO-mediated vasodilation (flavonoids). Antioxidant flavonols reduce oxidative neuronal damage and protect mitochondrial function. Cochrane review confirms modest, inconsistent cognitive benefit in mild-moderate dementia against placebo controls.

- **Modulates** → [Brain](../../../../../01-human/06-organ/brain/README.md): Bilobalide blocks NMDA receptor excitotoxicity; ginkgolide J inhibits AIF-triggered apoptosis; flavonoids inhibit amyloid-β aggregation and support mitochondrial biogenesis via PGC-1α. Clinical trials show limited but measurable improvements in attention and working memory in patients with cognitive impairment.

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): Ginkgolide B PAF receptor antagonism reduces platelet aggregation and thrombus formation. Flavonoid-mediated eNOS upregulation and NO preservation promote arterial vasodilation, improving peripheral blood flow in claudication. Antiplatelet activity raises clinically significant bleeding risk with warfarin and aspirin.

- **Modulates** → [Platelet](../../../../../01-human/04-cellular/platelet/README.md): Ginkgolide B competitively antagonizes the PAF receptor (PAFR), inhibiting PAF-induced platelet aggregation, granule release, and thromboxane synthesis. This antiplatelet effect is the primary basis for drug interaction warnings with anticoagulants and antiplatelet agents; physician oversight is required when co-prescribed.

---

[^birks-2009-cochrane-ginkgo]: Birks J, Evans JG. Ginkgo biloba for cognitive impairment and dementia. Cochrane Database Syst Rev. 2009;(1):CD003120. doi:10.1002/14651858.CD003120.pub3
[^weinmann-2010-ginkgo-dementia]: Weinmann S, Roll S, Schwarzbach C, et al. Effects of Ginkgo biloba in dementia. BMC Geriatr. 2010;10:14. doi:10.1186/1471-2318-10-14
