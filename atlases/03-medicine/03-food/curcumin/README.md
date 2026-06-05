---
schema: medicine-entry/v1
id: curcumin
name: Curcumin
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Polyphenol from Curcuma longa (turmeric). Inhibits NF-κB (via IKKβ) and AP-1 → reduces TNF-α, IL-1β, IL-6. Activates Nrf2 → antioxidant response. ~1% oral bioavailability without piperine. RCTs: reduces CRP/IL-6 in metabolic syndrome; anti-fibrotic in NAFLD. 5,000+ publications."
aliases: ["curcumin", "diferuloylmethane", "turmeric extract", "curcuminoids", "Curcuma longa", "haldi", "haridra", "jiang huang", "curcumin I", "bis-demethoxycurcumin"]
sources:
  - id: aggarwal-2009-curcumin-diseases
    type: peer-reviewed
    cite: "Aggarwal BB, Harikumar KB. Potential therapeutic effects of curcumin, the anti-inflammatory agent, against neurodegenerative, cardiovascular, pulmonary, metabolic, autoimmune and neoplastic diseases. Int J Biochem Cell Biol. 2009;41(1):40-59."
    doi: "10.1016/j.biocel.2008.06.010"
    pmid: "18662800"
    url: "https://doi.org/10.1016/j.biocel.2008.06.010"
  - id: tayyem-2006-curcumin-content
    type: peer-reviewed
    cite: "Tayyem RF, Heath DD, Al-Delaimy WK, Rock CL. Curcumin content of turmeric and curry powders. Nutr Cancer. 2006;55(2):126-31."
    doi: "10.1207/s15327914nc5502_2"
    pmid: "17044766"
    url: "https://doi.org/10.1207/s15327914nc5502_2"
  - id: hewlings-2017-curcumin-review
    type: peer-reviewed
    cite: "Hewlings SJ, Kalman DS. Curcumin: a review of its effects on human health. Foods. 2017;6(10):92."
    doi: "10.3390/foods6100092"
    pmid: "29065496"
    url: "https://doi.org/10.3390/foods6100092"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    evidence: aggarwal-2009-curcumin-diseases
    note: "Curcumin directly inhibits IKKβ (IκB kinase β), preventing phosphorylation and degradation of IκBα, thereby trapping NF-κB in the cytoplasm in an inactive complex. NF-κB is the master transcriptional driver of TNF-α, IL-1β, IL-6, COX-2, and iNOS. Curcumin also inhibits AP-1 (via JNK suppression) and the JAK-STAT3 pathway, providing multi-level suppression of the pro-inflammatory transcriptional programme. Effect is concentration-dependent; plasma concentrations achievable without enhanced formulations are generally below the EC50 in cell-based assays."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: hewlings-2017-curcumin-review
    note: "NF-κB and AP-1 co-regulate IL-6 gene transcription; curcumin's dual suppression of both transcription factors leads to reduced IL-6 mRNA and protein. STAT3 (a key IL-6 downstream effector) is also directly inhibited by curcumin. In meta-analyses of RCTs, curcumin supplementation reduces circulating IL-6 and CRP significantly in subjects with metabolic syndrome, obesity, and inflammatory conditions, though effect sizes are modest (IL-6 reduction ~0.5–1.5 pg/mL in most trials)."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    evidence: aggarwal-2009-curcumin-diseases
    note: "Curcumin activates Nrf2 (nuclear factor erythroid 2-related factor 2) in hepatocytes by modifying Keap1 cysteine residues, releasing Nrf2 to translocate to the nucleus and drive ARE (antioxidant response element) gene expression: HO-1 (heme oxygenase-1), NQO1 (NAD(P)H:quinone oxidoreductase), glutathione S-transferases, and ferritin — providing cytoprotection against oxidative/electrophilic stress. Curcumin inhibits TGF-β-induced hepatic stellate cell (HSC) activation, suppressing α-SMA expression and collagen type I secretion → anti-fibrotic in NAFLD/NASH models. These hepatoprotective mechanisms are primarily established in cell culture and animal models; clinical biopsy-confirmed anti-fibrotic data in humans are limited."
---

# Curcumin

## Overview

**Curcumin** (diferuloylmethane, C₂₁H₂₀O₆, MW 368.4 Da) is the primary bioactive polyphenol of **turmeric** (*Curcuma longa*, family Zingiberaceae), accounting for approximately 75–80% of the total curcuminoid fraction in the rhizome. The remaining curcuminoids are demethoxycurcumin (~15–20%) and bis-demethoxycurcumin (~5%), all with the characteristic β-diketone backbone and two phenolic rings connected by a heptadienedione linker.

**Turmeric** has been used for millennia across South and Southeast Asia:
- **Ayurveda:** *haridra* (Sanskrit) — one of the most commonly employed herbs; used topically and internally for wound healing, skin disorders, liver disease, joint pain, and digestive complaints; categorised as *kaphahara* (reduces kapha) and *pittahara* (reduces pitta excess)
- **Siddha medicine:** *manjal* — foundational herb in formulations for jaundice, diabetes, and parasitic infections
- **TCM:** *jiang huang* — used for blood stagnation, pain, and jaundice
- **Unani medicine:** *urad desi* — anti-inflammatory and digestive use
- **Culinary tradition:** Core ingredient in curry powders across South Asia; responsible for the characteristic yellow colour (via the phenolic chromophore absorbing at ~420 nm)

**Turmeric composition:** Dried rhizome contains 2–5% curcuminoids by weight [^tayyem-2006-curcumin-content]; commercial curry powders contain 0.58–3.14% curcumin. Daily dietary turmeric intake in India (~1.5–2 g powder/day) delivers approximately **30–90 mg curcumin** — far below the doses used in most clinical trials (500–1500 mg/day of standardised extract).

Curcumin has generated over **5,000 publications** and attracted intense research interest due to its multi-target pharmacology, but this has also attracted criticism: curcumin is a **pan-assay interference compound (PAINS)** — a compound with physicochemical properties that produce artefactual positive results in multiple biochemical assays (autofluorescence, metal chelation, non-specific protein binding, electrophilic reactivity). This means some of curcumin's reported molecular targets require interpretation with caution.

## Mechanism

### NF-κB Inhibition (Primary Anti-Inflammatory Pathway)

The canonical mechanism of curcumin's anti-inflammatory action:

1. **IKKβ inhibition:** Curcumin inhibits IκB kinase β (IKKβ), the kinase responsible for phosphorylating IκBα (the NF-κB inhibitor protein), targeting a specific cysteine residue (Cys-179) in the activation loop of IKKβ; this is a **covalent modification** (Michael acceptor chemistry via the β-diketone moiety)
2. **IκBα stabilisation:** Unphosphorylated IκBα is not ubiquitinated and degraded → remains bound to NF-κB (p65/p50 heterodimer) in the cytoplasm → NF-κB cannot translocate to the nucleus
3. **Transcriptional suppression:** NF-κB-driven genes are downregulated: TNF-α, IL-1β, IL-6, IL-8, COX-2, iNOS, MMP-9, VEGF, survivin — a broad anti-inflammatory, anti-angiogenic, and pro-apoptotic (in cancer cells) transcriptional effect [^aggarwal-2009-curcumin-diseases]

### AP-1 and MAPK Pathway Inhibition

- Curcumin inhibits c-Jun N-terminal kinase (JNK) → reduced AP-1 (c-Jun/c-Fos) activation → complementary suppression of inflammatory gene transcription independent of NF-κB
- p38 MAPK inhibition reduces downstream MK2/MK3 activity → reduced ARE-mediated mRNA stability of cytokine transcripts (TNF-α, IL-6 mRNA have AU-rich elements stabilised by p38 pathway)
- ERK1/2 inhibition at high curcumin concentrations; ERK is a pro-proliferative/survival kinase, relevant in cancer biology

### JAK-STAT3 Pathway Inhibition

- Curcumin directly inhibits JAK1 and JAK2 kinase activity (proposed), reducing STAT3 Tyr705 phosphorylation
- Unphosphorylated STAT3 cannot dimerize or translocate to the nucleus → reduced transcription of STAT3 target genes: Bcl-2, Bcl-xL, cyclin D1, VEGF, MMP-2
- STAT3 is constitutively active in many cancers and in chronic inflammatory conditions; curcumin's STAT3 inhibition is a mechanistic basis for both anti-inflammatory and putative anti-cancer effects

### Nrf2 Activation (Antioxidant Response)

The paradox: curcumin is both a pro-oxidant (at high doses, generating ROS) and an antioxidant inducer (at physiological doses via Nrf2):

1. **Keap1 modification:** Curcumin (as a Michael acceptor) covalently modifies cysteine residues on Keap1 (Cys151, Cys273, Cys288), the E3 ubiquitin ligase adaptor that normally targets Nrf2 for proteasomal degradation
2. **Nrf2 stabilisation:** Modified Keap1 cannot ubiquitinate Nrf2 → Nrf2 accumulates → translocates to nucleus → binds AREs (antioxidant response elements)
3. **ARE target gene induction:** HO-1 (heme oxygenase-1; cytoprotective, anti-inflammatory), NQO1 (NAD(P)H quinone oxidoreductase; 2-electron reductase detoxifying quinone electrophiles), GCL (glutamate cysteine ligase; rate-limiting enzyme of glutathione synthesis), ferritin (iron sequestration), thioredoxin reductase
4. **Hepatoprotective consequence in hepatocytes:** Nrf2-mediated HO-1 and NQO1 induction protects against oxidative and electrophilic injury; relevant in acetaminophen toxicity models and NAFLD contexts [^aggarwal-2009-curcumin-diseases]

### Anti-fibrotic Mechanisms in the Liver

- Curcumin inhibits TGF-β receptor signalling → reduced Smad2/3 phosphorylation → reduced activation of hepatic stellate cells (HSCs)
- Inhibits HSC transdifferentiation to myofibroblast phenotype → reduced α-smooth muscle actin (α-SMA) and collagen type I/III secretion
- Induces HSC apoptosis via mitochondrial pathway
- Activates PPARγ in HSCs → reverses the pro-fibrogenic programme (PPARγ activation antagonises TGF-β-driven fibrogenesis)

### Bioavailability — The Critical Limitation

Curcumin has famously poor oral bioavailability:
- **Aqueous solubility:** ~11 ng/mL at pH 7 (essentially insoluble); hydrophobic β-diketone structure
- **Intestinal absorption:** Limited due to insolubility; P-gp-mediated efflux in enterocytes
- **Rapid metabolism:** Glucuronidation and sulfation in intestinal enterocytes and hepatocytes → curcumin glucuronide and sulfate conjugates (pharmacologically less active)
- **Systemic bioavailability of free curcumin:** ~1% following standard powder administration; plasma concentrations rarely exceed 10–50 nM after 1–2 g curcumin — below EC50 for most of the reported in vitro mechanisms

**Bioavailability-enhancement strategies:**
- **Piperine (BioPerine):** Inhibits glucuronidation (UGT enzymes) and P-gp efflux → 2000% increase in curcumin AUC reported (Shoba et al., 1998); widely used commercially; piperine at 20 mg/day is generally safe but inhibits drug metabolism — caution with narrow-therapeutic-index drugs
- **Phospholipid complex (Meriva):** Curcumin-phosphatidylcholine complex → improved intestinal permeation; ~29-fold improved absorption vs. standard curcumin in one study
- **Nanoparticle/liposomal formulations:** Nano-curcumin, solid lipid nanoparticles — research stage or limited clinical data
- **SLCP (solid lipid curcumin particle; Longvida):** Lipid-encapsulated; improved plasma free curcumin concentrations; used in some cognitive RCTs

The bioavailability problem means **the gap between cell-culture EC50 concentrations and achievable plasma concentrations is large** — most of curcumin's in vitro pharmacology occurs at 1–50 µM, while plasma free curcumin is in the low nM range. Whether metabolites (tetrahydrocurcumin, curcumin glucuronide) are biologically active and whether luminal GI concentrations (which are high) account for local gut effects is a matter of ongoing research.

## Clinical Use

### Indications and Dosing

| Indication | Dose | Formulation | Evidence quality |
|:---|:---|:---|:---|
| Osteoarthritis pain | 500 mg 2–3× daily | Standard + piperine or Meriva | Moderate |
| Metabolic syndrome / inflammation (CRP) | 1000–1500 mg/day | Standard + piperine | Moderate |
| NAFLD | 1000–1500 mg/day | Standard or phospholipid | Low-moderate |
| Inflammatory bowel disease (UC) | 1000–3000 mg/day | Enema or oral | Low |
| Anterior uveitis | Topical / 375 mg 3× daily oral | Standard | Low |
| Cancer prevention | Not established | N/A | Insufficient |

No regulatory body has approved curcumin as a drug. It is sold as a dietary supplement (GRAS status in the US as a food additive, up to 0.5% of food weight). Standard supplemental doses range from **500–1500 mg/day** of curcumin extract.

### Drug Interactions

- **Anticoagulants / antiplatelets:** Curcumin inhibits platelet TXA₂ synthesis and has mild anticoagulant properties; additive bleeding risk with warfarin, aspirin, NSAIDs, clopidogrel — monitor INR; avoid high-dose curcumin pre-operatively
- **Chemotherapy:** Complex interactions — curcumin may sensitise cancer cells to some chemotherapy agents (experimental) but also inhibits CYP3A4 and P-gp, potentially increasing toxicity of narrow-index cytotoxics; do not use without oncologist guidance
- **CYP1A2 inhibition:** Curcumin inhibits CYP1A2 → increased levels of CYP1A2 substrates (clozapine, theophylline, caffeine)
- **Iron absorption:** Curcumin chelates iron; concerns about iron-deficiency anaemia with high-dose long-term supplementation in susceptible individuals
- **Piperine (if included):** See above — inhibits numerous CYP enzymes and P-gp; drug interaction risk is substantially higher with piperine-containing formulations

## Evidence

### Meta-analytic Evidence for Inflammatory Markers

Hewlings and Kalman (2017) [^hewlings-2017-curcumin-review] comprehensive review:
- Multiple RCTs demonstrate reductions in CRP (pooled reduction ~2–5 mg/L in elevated-CRP populations), IL-6, and TNF-α with curcumin supplementation
- Effects are consistent but modest; clinically meaningful reduction in biomarker-defined inflammation
- GRADE: **Low to Moderate** — heterogeneous populations, formulations, and doses; most trials small (n=30–100); short duration; some industry involvement

Specific meta-analyses (Tabrizi et al., 2019; Sahebkar et al., 2016):
- CRP: weighted mean difference −6.4 mg/L (95% CI: −7.0 to −5.8) across 10 RCTs
- IL-6: weighted mean difference −0.52 pg/mL (modest effect)
- TNF-α: weighted mean difference −3.8 pg/mL
- Substantial heterogeneity (I² >75%) limits pooled estimates

### Osteoarthritis Evidence

Multiple RCTs (n=40–350, 8–24 weeks) comparing curcumin (typically 1500 mg/day + piperine or Meriva) vs. ibuprofen or placebo:
- WOMAC pain and function scores improved vs. placebo (effect size ~0.4–0.8 SD)
- One RCT found curcumin (1500 mg/day) non-inferior to ibuprofen (1200 mg/day) for knee osteoarthritis pain — with fewer GI adverse events
- These trials consistently show meaningful pain reduction; quality of evidence rated **Moderate** by Cochrane-style assessments
- Limitations: heterogeneous curcumin preparations; most single-centre; short follow-up; structural joint modification not assessed

### NAFLD Evidence

RCTs using curcumin 1000–1500 mg/day for 8–16 weeks in confirmed NAFLD patients show:
- Significant reductions in ALT/AST
- Reduced hepatic steatosis on ultrasound grading
- Reductions in BMI, fasting glucose, insulin resistance (HOMA-IR)
- One biopsy-confirmed trial (n=50) showed significant improvement in NAFLD Activity Score vs. placebo
- GRADE: **Low** — small trials, unblinded assessment in some, no hard clinical endpoints

### Cognition and Neuroprotection

Emerging evidence for curcumin in mild cognitive impairment (small Longvida formulation RCTs) shows modest improvements in working memory and attention vs. placebo. Not adequately powered to assess Alzheimer's disease endpoints. GRADE: **Low**.

### Limitations and PAINS Issue

A prominent critique by Nelson et al. (2017, J Med Chem) classified curcumin as a PAINS compound — its β-diketone and phenolic groups cause:
- Autofluorescence (creates false positives in fluorescence-based assays)
- Metal chelation (can sequester metal ions required for enzyme activity in assays, producing apparent "inhibition")
- Electrophilic/non-specific covalent protein modification (can adduct Cys/Lys residues non-specifically)
- Instability (degrades in aqueous solution, yielding reactive breakdown products that may be the actual active species)

This does not invalidate all curcumin research, but means that **in vitro mechanistic studies should be interpreted cautiously** and emphasis should be placed on properly designed clinical RCTs with validated biomarkers.

## Connections

- **Modulates** → [TNF-α](../../../../../01-human/03-molecular/tnf-alpha/README.md): Curcumin's covalent IKKβ inhibition (via Michael addition to Cys-179) is the primary mechanism of NF-κB suppression and consequent TNF-α transcriptional reduction. The electrophilic β-diketone moiety also directly inhibits AP-1 (via JNK inhibition) and JAK-STAT3, providing multi-level suppression of the TNF-α-driven inflammatory programme. These effects are well-characterised in macrophages, synoviocytes, and hepatocytes at concentrations achievable with enhanced bioavailability formulations.

- **Modulates** → [IL-6](../../../../../01-human/03-molecular/il-6/README.md): NF-κB and AP-1 co-regulate the IL-6 gene promoter; dual inhibition by curcumin produces additive IL-6 suppression. Direct STAT3 inhibition (a central IL-6 downstream effector) further attenuates IL-6 signalling amplitude. Meta-analyses of clinical RCTs confirm modest but consistent reductions in circulating IL-6 in inflammatory conditions with supplemental curcumin; effect sizes are most pronounced in subjects with elevated baseline IL-6 (metabolic syndrome, osteoarthritis, NAFLD).

- **Modulates** → [Hepatocyte](../../../../../01-human/04-cellular/hepatocyte/README.md): Curcumin exerts two complementary hepatoprotective actions in hepatocytes: (1) Nrf2 activation (via Keap1-Cys modification → HO-1, NQO1, GSH induction) provides cytoprotection against oxidative and electrophilic stress — relevant in drug toxicity and NAFLD contexts; (2) inhibition of TGF-β/Smad2/3 signalling and HSC activation provides anti-fibrotic effects — supported by in vitro and animal data, with emerging clinical RCT evidence in NAFLD. The poor bioavailability of standard curcumin formulations means luminal and portal concentrations in the gut/liver may be substantially higher than systemic plasma concentrations, potentially making the liver a more relevant target than peripheral tissues.

[^aggarwal-2009-curcumin-diseases]: Aggarwal BB, Harikumar KB. Int J Biochem Cell Biol. 2009;41(1):40-59. doi:10.1016/j.biocel.2008.06.010
[^tayyem-2006-curcumin-content]: Tayyem RF et al. Nutr Cancer. 2006;55(2):126-31. doi:10.1207/s15327914nc5502_2
[^hewlings-2017-curcumin-review]: Hewlings SJ, Kalman DS. Foods. 2017;6(10):92. doi:10.3390/foods6100092
