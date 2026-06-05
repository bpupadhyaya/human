---
schema: medicine-entry/v1
id: statins
name: Statins
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "HMG-CoA reductase inhibitors — cornerstone of cardiovascular risk reduction. Reduce plasma LDL-C 30–55% via hepatic cholesterol synthesis inhibition. Landmark RCTs demonstrate 20–35% relative risk reductions in major cardiovascular events across primary and secondary prevention."
aliases: ["HMG-CoA reductase inhibitors", "statins", "statin therapy"]
sources:
  - id: fourS-1994
    type: peer-reviewed
    cite: "Scandinavian Simvastatin Survival Study Group. Randomised trial of cholesterol lowering in 4444 patients with coronary heart disease: the Scandinavian Simvastatin Survival Study (4S). Lancet. 1994;344(8934):1383-9."
    doi: "10.1016/S0140-6736(94)90566-5"
    pmid: "7968073"
    url: "https://doi.org/10.1016/S0140-6736(94)90566-5"
  - id: woscops-1995
    type: peer-reviewed
    cite: "Shepherd J, Cobbe SM, Ford I, et al. Prevention of coronary heart disease with pravastatin in men with hypercholesterolemia. N Engl J Med. 1995;333(20):1301-7."
    doi: "10.1056/NEJM199511163332001"
    pmid: "7566020"
    url: "https://doi.org/10.1056/NEJM199511163332001"
  - id: hps-2002
    type: peer-reviewed
    cite: "Heart Protection Study Collaborative Group. MRC/BHF Heart Protection Study of cholesterol lowering with simvastatin in 20,536 high-risk individuals. Lancet. 2002;360(9326):7-22."
    doi: "10.1016/S0140-6736(02)09327-3"
    pmid: "12114036"
    url: "https://doi.org/10.1016/S0140-6736(02)09327-3"
  - id: ctt-2010-meta
    type: peer-reviewed
    cite: "Cholesterol Treatment Trialists' Collaboration. Efficacy and safety of more intensive lowering of LDL cholesterol: a meta-analysis of data from 170,000 participants in 26 randomised trials. Lancet. 2010;376(9753):1670-81."
    doi: "10.1016/S0140-6736(10)61350-5"
    pmid: "21067804"
    url: "https://doi.org/10.1016/S0140-6736(10)61350-5"
  - id: acc-aha-2018-lipid-guideline
    type: clinical-guideline
    cite: "Grundy SM, Stone NJ, Bailey AL, et al. 2018 AHA/ACC/AACVPR/AAPA/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Blood Cholesterol. J Am Coll Cardiol. 2019;73(24):e285-e350."
    doi: "10.1016/j.jacc.2018.11.003"
    pmid: "30423393"
    url: "https://doi.org/10.1016/j.jacc.2018.11.003"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "Statins reduce atherosclerotic plaque burden in the systemic vasculature, lowering the risk of major adverse cardiovascular events (MI, stroke, cardiovascular death) — the primary beneficial effect at the system scale."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Statins inhibit HMG-CoA reductase in hepatocytes, the rate-limiting step in cholesterol synthesis; compensatory LDL receptor upregulation clears plasma LDL-C by 30–55% depending on agent and dose."
  - target: 01-human/06-organ/liver
    relation: treats
    note: "NASH/steatohepatitis: statins reduce hepatic steatosis and inflammation markers; generally safe in compensated liver disease and not contraindicated in NAFLD, despite early concerns about statin hepatotoxicity."
---

# Statins

## Overview

Statins are **HMG-CoA reductase inhibitors** — competitive inhibitors of 3-hydroxy-3-methylglutaryl-coenzyme A reductase, the rate-limiting enzyme in the mevalonate pathway that produces cholesterol in the liver. By blocking this enzyme, statins reduce hepatic cholesterol synthesis, causing a compensatory upregulation of low-density lipoprotein receptors (LDL-R) on hepatocytes, which clears LDL-C from the plasma. The net result is a 30–55% reduction in plasma LDL-C, depending on the agent and dose [^ctt-2010-meta].

They are the most widely prescribed cardiovascular drugs globally and have one of the strongest evidence bases in clinical pharmacology. Landmark trials across five decades have consistently demonstrated that lowering LDL-C with statins reduces major adverse cardiovascular events (MACE: MI, stroke, cardiovascular death) in both primary prevention (no prior CV disease) and secondary prevention (established ASCVD) [^fourS-1994][^woscops-1995][^hps-2002][^ctt-2010-meta]. The Cholesterol Treatment Trialists meta-analysis (2010) — pooling data from 26 trials and 170,000 participants — found a 22% reduction in MACE per 1 mmol/L (~39 mg/dL) reduction in LDL-C, a dose-response relationship that is linear and consistent across risk groups.

## Mechanism

### Primary Mechanism: HMG-CoA Reductase Inhibition

The mevalonate pathway:

```
Acetyl-CoA → HMG-CoA →[HMG-CoA reductase]→ Mevalonate → ... → Cholesterol
                          ↑ STATIN BINDS HERE
```

Statins contain a structural mimic of the HMG-CoA substrate that occupies the active site of HMG-CoA reductase with high affinity (nanomolar Ki). Competitive inhibition at this step:

1. Reduces intracellular cholesterol in hepatocytes.
2. Activates **SREBP-2** (sterol regulatory element-binding protein 2) — the cholesterol sensor.
3. SREBP-2 drives transcription of **LDLR** (LDL receptor gene) — receptor density on hepatocyte surface increases.
4. Increased LDL-R captures LDL particles from the plasma → LDL-C falls.
5. VLDL secretion also mildly reduced; HDL-C increases modestly (~5–10%).

### Pleiotropic Effects

Statins produce benefits beyond LDL-C reduction that are observed at the tissue and system level:

- **Plaque stabilization:** Statins reduce macrophage infiltration into plaques, upregulate eNOS, and stabilize the fibrous cap, reducing risk of rupture even before significant volume regression.
- **Anti-inflammatory:** Reduced hsCRP; modulation of NF-κB and cytokine production.
- **Endothelial function:** Improved nitric oxide bioavailability → vasodilation; reduced endothelial dysfunction (a precursor of atherosclerosis).
- **Antithrombotic:** Reduced tissue factor expression; attenuated platelet aggregation.

Whether pleiotropic effects provide clinical benefit independent of LDL-C lowering remains debated; the CTT meta-analysis supports LDL-C reduction as the dominant mechanism.

## Clinical Use

Per the 2018 AHA/ACC Guideline on Management of Blood Cholesterol [^acc-aha-2018-lipid-guideline]:

| Patient group | Recommendation | Statin intensity |
|:---|:---|:---|
| Clinical ASCVD (secondary prevention) | High-intensity statin | Atorvastatin 40–80 mg or rosuvastatin 20–40 mg |
| LDL ≥ 190 mg/dL (familial hypercholesterolemia) | High-intensity statin ± ezetimibe ± PCSK9i | Atorvastatin 40–80 mg or rosuvastatin 20–40 mg |
| Diabetes + age 40–75, LDL 70–189 | Moderate-intensity | Atorvastatin 10–20 mg, rosuvastatin 5–10 mg, simvastatin 20–40 mg |
| 10-yr ASCVD risk ≥ 7.5%, LDL ≥ 70 | Moderate-intensity (discuss risk) | As above |
| Lower risk (primary prevention) | Shared decision-making | Based on 10-yr risk calculation |

## Key Agents

| Agent | Potency (LDL-C reduction at max approved dose) | Half-life | Metabolism | Notes |
|:---|:---:|:---:|:---|:---|
| **Rosuvastatin** (Crestor) | ~55% (40 mg) | ~19 h | Minimal CYP450; mainly renal/fecal | Hydrophilic; lowest drug-drug interaction |
| **Atorvastatin** (Lipitor) | ~50% (80 mg) | ~14 h (active metabolites longer) | CYP3A4 | Most widely prescribed; both primary and secondary prevention trials |
| **Simvastatin** (Zocor) | ~38% (40 mg) | ~2 h (prodrug) | CYP3A4 | HPS trial; dose-limited by myopathy risk at 80 mg |
| **Pravastatin** (Pravachol) | ~28% (40 mg) | ~2 h | Not CYP metabolized; renal | Lowest drug-drug interaction; WOSCOPS trial |
| **Fluvastatin** | ~24% (80 mg) | ~3 h | CYP2C9 | Weaker; less used |
| **Pitavastatin** | ~32% (4 mg) | ~11 h | Minimal CYP | Preferred in patients on complex regimens |

### Intensity Classification

- **High-intensity:** Atorvastatin 40–80 mg, Rosuvastatin 20–40 mg (≥50% LDL-C reduction expected)
- **Moderate-intensity:** Atorvastatin 10–20 mg, Rosuvastatin 5–10 mg, Simvastatin 20–40 mg (30–50% reduction)
- **Low-intensity:** Simvastatin 10 mg, Pravastatin 10–20 mg (<30% reduction)

## Evidence

### Landmark Trials

| Trial | Drug | Population | Key result |
|:---|:---|:---|:---|
| **4S (1994)** | Simvastatin 20–40 mg | 4,444 patients, CAD, LDL 213 mg/dL | 30% relative risk reduction in mortality; 34% in MACE [^fourS-1994] |
| **WOSCOPS (1995)** | Pravastatin 40 mg | 6,595 men, no prior MI, hypercholesterolemia | 31% reduction in non-fatal MI + coronary death (primary prevention) [^woscops-1995] |
| **HPS (2002)** | Simvastatin 40 mg | 20,536 high-risk, LDL ≥ 116 mg/dL | 25% reduction in MACE across all LDL levels, including LDL < 116 mg/dL [^hps-2002] |
| **CTT meta-analysis (2010)** | Multiple statins | 170,000 participants, 26 trials | 22% MACE reduction per 1 mmol/L LDL-C fall; linear dose-response [^ctt-2010-meta] |

### The Lower-the-Better Principle

CTT data support a continuous, log-linear relationship: every additional 1 mmol/L (~39 mg/dL) reduction in LDL-C reduces MACE by ~22%, with no safety floor identified in statin trials. This underpins the 2018 guideline principle of maximizing statin intensity in high-risk patients.

## Side Effects

- **Myopathy / statin-associated muscle symptoms (SAMS):** Most common reason for discontinuation. Spectrum: myalgia (no CK elevation) → myositis (CK elevation) → rhabdomyolysis (CK > 10× ULN + renal injury; rare, ~0.1%). Risk increased by high-dose statins, CYP3A4 inhibitors (with atorvastatin/simvastatin), hypothyroidism, renal insufficiency.
- **Liver enzyme elevation:** Transaminase rises > 3× ULN in ~0.1–1% of patients; usually transient; dose-dependent; routine monitoring not required in absence of symptoms.
- **New-onset diabetes:** Moderate increased risk (~10–15% relative; smaller absolute risk); more prevalent with high-intensity statins in pre-diabetic individuals. Clinical benefits of statins overwhelmingly exceed this risk.
- **Cognitive effects:** Rare case reports; not confirmed in large RCTs; not a contraindication.
- **Teratogenicity:** Contraindicated in pregnancy (cholesterol essential for fetal development).

## Connections

- **Acts on** → [Cardiovascular System](../../../../01-human/07-system/cardiovascular-system/README.md): Reduce atherosclerotic plaque burden in the systemic circulation, lowering risk of MI, stroke, and peripheral arterial disease.
- **Molecular target** (planned entry): HMG-CoA reductase — an enzyme expressed primarily in the liver and other tissues that synthesize cholesterol. A future entry at the `01-human/03-molecular/` scale will cover this enzyme and the mevalonate pathway.

[^fourS-1994]: Scandinavian Simvastatin Survival Study Group. Randomised trial of cholesterol lowering in 4444 patients with coronary heart disease (4S). *Lancet.* 1994;344(8934):1383-9. [doi:10.1016/S0140-6736(94)90566-5](https://doi.org/10.1016/S0140-6736(94)90566-5) · [PubMed 7968073](https://pubmed.ncbi.nlm.nih.gov/7968073/)
[^woscops-1995]: Shepherd J, Cobbe SM, Ford I, et al. Prevention of coronary heart disease with pravastatin (WOSCOPS). *N Engl J Med.* 1995;333(20):1301-7. [doi:10.1056/NEJM199511163332001](https://doi.org/10.1056/NEJM199511163332001) · [PubMed 7566020](https://pubmed.ncbi.nlm.nih.gov/7566020/)
[^hps-2002]: Heart Protection Study Collaborative Group. MRC/BHF Heart Protection Study of cholesterol lowering with simvastatin. *Lancet.* 2002;360(9326):7-22. [doi:10.1016/S0140-6736(02)09327-3](https://doi.org/10.1016/S0140-6736(02)09327-3) · [PubMed 12114036](https://pubmed.ncbi.nlm.nih.gov/12114036/)
[^ctt-2010-meta]: Cholesterol Treatment Trialists' Collaboration. Efficacy and safety of more intensive lowering of LDL cholesterol. *Lancet.* 2010;376(9753):1670-81. [doi:10.1016/S0140-6736(10)61350-5](https://doi.org/10.1016/S0140-6736(10)61350-5) · [PubMed 21067804](https://pubmed.ncbi.nlm.nih.gov/21067804/)
[^acc-aha-2018-lipid-guideline]: Grundy SM, Stone NJ, Bailey AL, et al. 2018 AHA/ACC Guideline on the Management of Blood Cholesterol. *J Am Coll Cardiol.* 2019;73(24):e285-e350. [doi:10.1016/j.jacc.2018.11.003](https://doi.org/10.1016/j.jacc.2018.11.003) · [PubMed 30423393](https://pubmed.ncbi.nlm.nih.gov/30423393/)
