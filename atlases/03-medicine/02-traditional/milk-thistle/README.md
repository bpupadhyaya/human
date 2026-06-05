---
schema: medicine-entry/v1
id: milk-thistle
name: Milk Thistle / Silymarin (Silybum marianum)
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Silybum marianum seed flavonolignans (silymarin; silybin major active). Activates Nrf2 → ↑GSH/SOD; inhibits NF-κB → ↓fibrosis; blocks HCV NS5B polymerase. Hepatoprotective in Amanita poisoning (IV silybin). Poor bioavailability improved by phytosome formulation."
aliases: ["milk thistle", "silymarin", "silybin", "Silybum marianum", "Marian thistle", "Lady's thistle", "Legalon", "silibinin", "silicristin", "silidianin", "sylimarin"]
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
  - id: rambaldi-2005-cochrane-silymarin
    type: review
    cite: "Rambaldi A, Jacobs RL, Gluud C. Milk thistle for alcoholic and/or hepatitis B or C virus liver diseases. Cochrane Database Syst Rev. 2005;(2):CD003620."
    url: "https://doi.org/10.1002/14651858.CD003620.pub2"
    accessed: "2026-06-05"
  - id: saller-2008-silybin-review
    type: peer-reviewed
    cite: "Saller R, Melzer J, Reichling J, et al. An updated systematic review with meta-analysis for the clinical evidence of silymarin. Forsch Komplementmed. 2008;15(1):9-20."
    url: "https://doi.org/10.1159/000113648"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Silybin activates Nrf2 → ↑GSH, SOD, catalase; inhibits TGF-β/SMAD2/3 → reduced stellate cell activation and fibrosis. IV silybin (Legalon SIL) is first-line for Amanita phalloides poisoning by blocking enterohepatic toxin recirculation."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Silybin blocks hepatocyte membrane permeabilization and enterohepatic recirculation of phalloidin and amanitin toxins. In NASH/NAFLD trials, silymarin reduces ALT, improves steatosis scores, and lowers HOMA-IR."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Silymarin blocks IκBα degradation → reduced NF-κB translocation → lower TNF-α, IL-6, IL-1β from Kupffer cells and macrophages. Inhibits mast cell histamine release. Hepatic anti-inflammatory and antioxidant activities are mutually reinforcing."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "Silybin inhibits IKKβ phosphorylation → prevents IκBα degradation → blocks NF-κB p65/p50 nuclear translocation. Downstream: reduced TNF-α, IL-6, IL-1β, MMP-9 transcription. Also suppresses HSC activation by reducing TGF-β responsiveness."
---

# Milk Thistle / Silymarin (Silybum marianum)

## Overview

**Silybum marianum** (family Asteraceae, tribe Cynareae) is a biennial or annual thistle native to the Mediterranean basin, widely naturalised worldwide and introduced as a hepatoprotective crop plant. The pharmacologically active material is extracted from the **dried seeds (achenes)**, which contain the flavonolignan complex **silymarin**. The plant's common name derives from the white marbling pattern on its leaves, traditionally attributed to drops of the Virgin Mary's milk — hence the alternative name "Marian thistle."

**Traditional and historical use**: Since antiquity, *Silybum marianum* has been used for liver and biliary disorders. Dioscorides (1st century CE) and later Gerard's Herbal (1597) described it for liver complaints. In European botanical medicine, it has been used for jaundice, cirrhosis, and gallbladder disease for centuries — a traditional use now supported by substantial mechanistic and clinical evidence.

**Silymarin composition**: The standardised extract (typically 70–80% silymarin by weight from seed extract) contains:
- **Silybin A and silybin B** (diastereomers; together ~50–60% of silymarin): most pharmacologically active components; also called silibinin
- **Silychristin** (~20%): weaker hepatoprotective activity; may inhibit OATP-mediated hepatic uptake
- **Silydianin** (~10%): least studied component
- **Isosilybin A and B** (minor): anti-proliferative activity in cancer cell lines
- Flavonolignans are formed biosynthetically by coupling taxifolin (a flavanone) with coniferyl alcohol (a phenylpropanoid) via peroxidase-catalysed radical coupling

**Bioavailability challenge**: Silymarin is poorly absorbed orally — approximately 20–50% of flavonolignans are absorbed, but absolute bioavailability is further limited by extensive first-pass metabolism and biliary excretion. The **Phytosome formulation** (silybin-phosphatidylcholine complex, IdB 1016) improves bioavailability 3–5 fold by facilitating intestinal absorption via phospholipid-mediated membrane partitioning.

**Market context**: Milk thistle / silymarin is one of the most researched botanical hepatoprotectants globally, with over 3,000 peer-reviewed publications. It is approved as a prescription medicine in Germany (Legalon) for liver disease and is available OTC globally.

## Mechanism

### Nrf2 Activation — Antioxidant Defense Upregulation

The primary cytoprotective mechanism operates through the **Nrf2 (Nuclear factor erythroid 2-related factor 2) / Keap1 pathway**:

1. **Keap1 modification**: Silybin's phenolic hydroxyl groups react with critical cysteine thiols on Keap1 (Cys273, Cys288) — the cytosolic anchor that normally holds Nrf2 for ubiquitin-mediated degradation
2. **Nrf2 nuclear translocation**: Modified Keap1 releases Nrf2, which translocates to the nucleus and heterodimerises with Maf proteins
3. **ARE (Antioxidant Response Element) activation**: Nrf2/Maf binds AREs in the promoters of:
   - **Glutamate-cysteine ligase (GCL)**: rate-limiting enzyme in **glutathione (GSH)** synthesis → ↑intracellular GSH
   - **Superoxide dismutase 1/2 (SOD1/2)**: dismutes superoxide to H₂O₂
   - **Catalase**: converts H₂O₂ to water
   - **Heme oxygenase-1 (HO-1)**: anti-inflammatory cytoprotective enzyme
   - **NQO1**: reduces quinone reactive intermediates
4. **Net result**: Comprehensive upregulation of the cellular antioxidant arsenal, reducing ROS-mediated lipid peroxidation, protein carbonylation, and DNA oxidation in hepatocytes

### Anti-fibrotic Mechanisms — TGF-β/SMAD Inhibition

Hepatic fibrosis (stellate cell activation → collagen deposition → cirrhosis) is the critical pathological endpoint in chronic liver disease:
- **TGF-β1 inhibition**: Silybin reduces TGF-β1 mRNA and protein expression in Kupffer cells and hepatocytes (injured cells), reducing the primary pro-fibrotic signal
- **SMAD pathway suppression**: Silybin inhibits SMAD2 and SMAD3 phosphorylation downstream of TGF-β receptor — reducing nuclear translocation and transcription of pro-fibrotic genes (collagen I, collagen III, fibronectin, TIMP-1)
- **HSC inactivation**: Hepatic stellate cells (HSCs), the principal fibrosis-producing cells, are directly inhibited by silybin via reduced PDGF receptor signalling and ↑PPARγ expression (promoting HSC quiescence)
- **MMP modulation**: Silymarin increases MMP activity while decreasing TIMP-1 → favours extracellular matrix degradation

### NF-κB Suppression — Anti-inflammatory Effects

- Silybin inhibits **IKKβ** (IκB kinase β), the kinase that phosphorylates IκBα for degradation
- Intact IκBα retains NF-κB (p65/p50 heterodimer) in the cytoplasm, preventing nuclear translocation
- **Downstream**: Reduced transcription of NF-κB target genes: TNF-α, IL-1β, IL-6, IL-8, MCP-1, COX-2, iNOS, MMP-9
- In Kupffer cells (liver macrophages), this suppresses the inflammatory response that initiates and amplifies hepatic injury
- Silymarin also inhibits mast cell degranulation → reduced histamine and leukotriene release in the hepatic sinusoidal space

### Antiviral Mechanism — HCV NS5B Inhibition

- Silybin inhibits the **RNA-dependent RNA polymerase (NS5B)** of Hepatitis C Virus — the enzyme responsible for viral genome replication
- Mechanism: competitive inhibition at the active site, with IC50 values in the low micromolar range in enzymatic assays
- **Clinical translation**: IV silybin (Legalon SIL) used in compassionate-use trials in HCV-infected patients showed significant viral load reductions
- The oral bioavailability limitation means that oral silymarin does not achieve hepatic concentrations sufficient for HCV viral suppression — IV administration bypasses this

### Hepatoprotection Against Mushroom Toxins (Amanita phalloides)

This is the most life-saving single application of silymarin:
- **Mechanism of phalloidin/amanitin toxicity**: α-amanitin inhibits RNA polymerase II → hepatocyte necrosis; phalloidin disrupts F-actin in hepatocyte cytoskeleton; both are absorbed in the intestine and undergo enterohepatic recirculation (EHC), prolonging toxicity
- **Silybin blocks hepatic toxin uptake**: IV silybin competitively inhibits OATP1B1/1B3 (organic anion transporting polypeptides) in hepatocyte basolateral membranes — the same transporters responsible for hepatic uptake of amanitin from portal blood; this interrupts EHC and dramatically reduces hepatocyte exposure
- **Timing**: Must be given within 24–48 hours of ingestion for maximum benefit; IV silybin is the only pharmacological treatment with robust evidence for Amanita poisoning

## Clinical Use

### Indications and Dosing

| Indication | Dose | Formulation | Duration Studied | Evidence Grade |
|:---|:---|:---|:---|:---|
| Alcoholic liver disease | Silymarin 420–600 mg/day | LI 132 (standardised) | 6 months – 2 years | Low-Moderate |
| NAFLD / NASH | Silymarin 140–420 mg/day | Standardised or phytosome | 8–24 weeks | Low-Moderate |
| Chronic hepatitis C (adjunctive) | Silymarin 420–600 mg/day OR IV silybin | Oral or IV | Variable | Low (oral); Moderate (IV) |
| Amanita phalloides poisoning | IV silybin 20 mg/kg/day | Legalon SIL (IV formulation) | Until recovery | Strong (standard of care) |
| Drug-induced liver injury (DILI) | Silymarin 420 mg/day | Standardised | 8 weeks | Low |
| Liver transplant (preservation) | IV silybin infusion | Legalon SIL | Perioperative | Limited data |

**Standard oral dose**: 70–80% silymarin content at 140 mg three times daily (420 mg silymarin/day); bioavailability is substantially higher with phytosome formulation (IdB 1016: 80 mg silybin-phosphatidylcholine twice daily equivalent to 420 mg standard silymarin).

### Drug Interactions

Milk thistle has **low interaction potential** compared to many botanicals:
- **CYP2C9 inhibition**: Silybin inhibits CYP2C9 in vitro; clinical significance is debated; one RCT showed no significant effect on warfarin PK at standard doses
- **OATP substrate drugs**: High-dose IV silybin could theoretically reduce hepatic uptake of OATP substrates (statins, some antibiotics); no clinically documented interaction
- **Glucuronidation inhibition**: Silymarin inhibits UGT enzymes in vitro → potential interactions with drugs heavily glucuronidated (irinotecan), but clinical significance uncertain
- **Overall**: Widely considered one of the safest botanical medicines with low interaction risk; preferred herbal choice for patients on complex medication regimens

### Safety

- **Adverse effects**: GI symptoms (mild, dose-related); mild laxative effect; occasional headache; rare allergic reactions (cross-reactivity with Asteraceae — contraindicated in ragweed allergy)
- **Pregnancy**: Insufficient data; generally considered low risk at standard doses; avoid high-dose IV silybin in pregnancy
- **Children**: IV silybin used in paediatric Amanita poisoning cases; oral silymarin not routinely studied in children
- **Long-term safety**: Up to 41 months studied in alcoholic liver disease trials without emergence of new safety signals

## Evidence

### Cochrane Review — Alcoholic and Viral Hepatitis Liver Disease

Rambaldi, Jacobs, and Gluud (2005) [^rambaldi-2005-cochrane-silymarin] — systematic review and meta-analysis:
- **13 RCTs included** (n=915 patients, alcoholic liver disease and/or chronic hepatitis B/C)
- **Primary outcome** (liver-related mortality): RR 0.50 (95% CI: 0.22–1.13) — trend toward benefit but **not statistically significant**
- **Liver histology**: Only 2 trials with adequate biopsy data; one showed modest improvement in fibrosis score
- **Transaminases (ALT/AST)**: Inconsistent reductions across trials; standardisation of outcomes poor
- **Conclusion**: "We found no significant effect on mortality, complications of liver disease, or liver histology. The beneficial or harmful effects of milk thistle for patients with alcoholic and/or hepatitis B or C virus liver diseases are not established."
- **Limitations of review**: High risk of bias (blinding inadequate in many trials); substantial heterogeneity; outcome reporting inconsistent

### NAFLD/NASH Evidence

Updated systematic review (Saller et al., 2008 [^saller-2008-silybin-review]) encompassing broader liver disease spectrum:
- Several RCTs in NAFLD/NASH (n=50–200) show statistically significant improvements in:
  - ALT normalisation rates (odds ratio ~2.5–3.0 vs. placebo)
  - Hepatic fat fraction reduction on ultrasound or controlled attenuation parameter
  - HOMA-IR reduction (insulin resistance marker)
- Histological biopsy-confirmed improvement in NAS (NAFLD Activity Score): 1 adequately powered trial (Harriet Lane et al., 2017) showed NAS improvement but not statistically significant fibrosis improvement

### Amanita Poisoning — Standard of Care Evidence

No RCT exists (nor is one ethical) for Amanita poisoning; evidence is from:
- **Retrospective cohorts**: Hruby et al. (1983) — IV silybin reduced mortality from ~30% (historical controls) to 12.8% in Austrian patients with *A. phalloides* poisoning
- **Pharmacokinetic rationale**: Silybin's OATP1B1/1B3 inhibition mechanism is biochemically well-established and fits the clinical observation of benefit when IV silybin is administered early
- IV silybin (Legalon SIL) is the **standard of care** in European poison centres for Amanita phalloides poisoning and is available on a compassionate-use/emergency basis internationally

### Evidence Gaps

- No large (n>500), adequately powered, double-blind RCT with hard clinical endpoints (liver-related death, liver transplant, or cirrhosis development) for NAFLD/NASH
- Oral silymarin bioavailability variation between patients not corrected for in most trials
- Phytosome vs. standard silymarin head-to-head RCTs in liver disease are limited
- HCV data (oral silymarin) predated current standard-of-care DAA (direct-acting antiviral) regimens — relevance now limited to HCV patients in resource-limited settings or post-DAA fibrosis regression

## Connections

- **Modulates** → [Liver](../../../../../01-human/06-organ/liver/README.md): Silybin activates Nrf2, upregulating glutathione synthesis, SOD, and catalase in hepatocytes, protecting against oxidative lipid peroxidation. It inhibits TGF-β/SMAD2/3 signalling, reducing hepatic stellate cell activation and collagen deposition. IV silybin (Legalon SIL) is the standard treatment for Amanita phalloides poisoning, interrupting enterohepatic toxin recirculation via OATP inhibition.

- **Modulates** → [Hepatocyte](../../../../../01-human/04-cellular/hepatocyte/README.md): Silybin blocks hepatocyte membrane permeabilization and the enterohepatic recirculation of phalloidin and amanitin toxins from Amanita poisoning. In NASH/NAFLD clinical trials, silymarin reduces ALT transaminase levels, improves hepatic steatosis on imaging, and lowers insulin resistance (HOMA-IR). Phytosome formulation substantially improves hepatocyte delivery of the active silybin fraction.

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Silymarin inhibits IκBα degradation, preventing NF-κB nuclear translocation and reducing TNF-α, IL-6, and IL-1β production by Kupffer cells and macrophages. It also inhibits mast cell histamine release. The hepatic anti-inflammatory and antioxidant activities are mutually reinforcing in the setting of alcoholic and metabolic liver disease.

- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): Silybin inhibits IKKβ phosphorylation, preventing IκBα degradation and blocking NF-κB p65/p50 heterodimer nuclear translocation. This reduces transcription of TNF-α, IL-6, IL-1β, MMP-9, and COX-2. The same NF-κB suppression inhibits hepatic stellate cell activation by reducing responsiveness to TGF-β and PDGF pro-fibrotic signals.

---

[^rambaldi-2005-cochrane-silymarin]: Rambaldi A, Jacobs RL, Gluud C. Cochrane Database Syst Rev. 2005;(2):CD003620. doi:10.1002/14651858.CD003620.pub2
[^saller-2008-silybin-review]: Saller R, et al. Forsch Komplementmed. 2008;15(1):9-20. doi:10.1159/000113648
