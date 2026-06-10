---
schema: human-scale-entry/v1
id: cytokine-storm
name: Cytokine Storm
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Dysregulated systemic immune amplification with massive cytokine release (IL-6, TNF-α, IL-1β, IFN-γ). Macrophage-T cell loop causes ARDS, DIC, organ failure. Triggers: COVID-19, CAR-T CRS, HLH. Treatment: tocilizumab, dexamethasone, anakinra."
aliases: ["cytokine storm", "cytokine release syndrome", "CRS", "hypercytokinemia", "macrophage activation syndrome", "MAS", "HLH"]
sources:
  - id: fajgenbaum-june-2020-cytokine-storm
    type: peer-reviewed
    cite: "Fajgenbaum DC, June CH. Cytokine Storm. N Engl J Med. 2020;383(23):2255-2273."
    doi: "10.1056/NEJMra2026131"
    pmid: "33264547"
    url: "https://doi.org/10.1056/NEJMra2026131"
  - id: tisoncik-2012-cytokine-storm-review
    type: peer-reviewed
    cite: "Tisoncik JR, Korth MJ, Simmons CP, Farrar J, Martin TR, Katze MG. Into the eye of the cytokine storm. Microbiol Mol Biol Rev. 2012;76(1):16-32."
    doi: "10.1128/MMBR.05015-11"
    pmid: "22390970"
    url: "https://doi.org/10.1128/MMBR.05015-11"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: modulated-by
    note: "Macrophages are central amplifiers of cytokine storm: activated macrophages produce IL-6, TNF-α, IL-1β, IL-12, and IL-18, engaging in feedback loops with T cells; MAS represents uncontrolled macrophage activation."
  - target: 01-human/03-molecular/il-6
    relation: modulated-by
    note: "IL-6 is the dominant cytokine in cytokine storm across multiple triggers (COVID-19, CAR-T CRS, HLH); it drives the acute-phase response, endothelial activation, and coagulopathy; tocilizumab (anti-IL-6R) reduces mortality in COVID-ARDS and CRS."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulated-by
    note: "TNF-α is an early proximal alarm cytokine in cytokine storm, activating NF-κB on endothelial cells, hepatocytes, and macrophages; drives ICAM-1 upregulation, vascular permeability, and DIC via tissue factor induction."
  - target: 01-human/03-molecular/nf-kb
    relation: modulated-by
    note: "NF-κB is the master transcriptional driver of the pro-inflammatory cytokine cascade in cytokine storm; activated by TNF-α, IL-1β, LPS, and viral PAMPs, it drives expression of IL-6, IL-8, TNF-α, MCP-1, and tissue factor in macrophages and endothelial cells."
  - target: 01-human/06-organ/lung
    relation: modulates
    note: "Cytokine storm causes ARDS in the lung: IL-8-driven neutrophil recruitment, endothelial barrier disruption, surfactant dysfunction, and hyaline membrane formation; the lung is the most vulnerable end-organ due to its exposure to the entire cardiac output."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: modulated-by
    note: "Dexamethasone suppresses cytokine storm via GR:NF-κB transrepression (↓ IL-1β/IL-6/TNF-α) and GRE transactivation (IκBα/IL-10/ANXA1 upregulation); primary mechanism of RECOVERY trial mortality benefit and CAR-T cytokine release syndrome treatment."
---

# Cytokine Storm

## Overview

Cytokine storm (CS) is a **life-threatening dysregulated systemic inflammatory response** characterized by massive, self-amplifying cytokine release that causes end-organ damage through direct cytotoxicity and immune-mediated injury. It represents a failure of normal immune regulatory mechanisms — a "runaway" positive-feedback loop in which activated immune cells (primarily macrophages and T cells) drive ever-escalating cytokine production, leading to systemic immunopathology [^fajgenbaum-june-2020-cytokine-storm].

The unifying feature across all CS etiologies is **disproportionate cytokine elevation** (particularly IL-6, TNF-α, IL-1β, IFN-γ, CXCL8/IL-8) relative to the initial triggering stimulus, distinguishing CS from normal protective inflammation. This disproportionate response is what drives the systemic pathology: ARDS, disseminated intravascular coagulation (DIC), hepatic failure, acute kidney injury, and cardiovascular collapse [^tisoncik-2012-cytokine-storm-review].

**Common CS etiologies:**
| Trigger | Cytokine pattern | Key features |
|:---|:---|:---|
| **Severe COVID-19** | IL-6, TNF-α, IL-8, IL-1β, IFN-γ | ARDS + hypercoagulability; tocilizumab + dexamethasone proven |
| **CAR-T cell CRS** | IL-6, IFN-γ, MCP-1 (macrophage-driven) | Fever + hypotension ± ARDS within 1–14 days; graded (ASTCT scale) |
| **HLH/MAS** | IFN-γ, IL-18, sIL-2R, ferritin ↑↑↑ | Hyperferritinemia, cytopenias, hemophagocytosis; very high mortality |
| **Sepsis/bacterial** | TNF-α, IL-1β, IL-6, IL-8 | Endothelial dysfunction, distributive shock |
| **Checkpoint inhibitor** | IL-6, TNF, IFN-γ | Immune reconstitution after anti-PD-1; can affect any organ |
| **Pancreatitis/burns** | IL-6, IL-1β, TNF-α | Sterile inflammation triggering systemic response |

## Structure

### Cytokine Network in Cytokine Storm

The cytokine storm response involves a hierarchical, interconnected network:

**"Alarm" cytokines (first wave — minutes to hours):**
- **TNF-α** — produced by macrophages within minutes of TLR activation; activates NF-κB on endothelial cells, hepatocytes, and other immune cells; increases vascular permeability; induces tissue factor → DIC risk
- **IL-1β** — processed by NLRP3 inflammasome; potent fever inducer (PGE2); amplifies TNF-α effects; induces IL-6 and CXCL8

**"Amplifier" cytokines (second wave — hours to days):**
- **IL-6** — produced by macrophages, T cells, endothelial cells; drives acute-phase response (CRP, fibrinogen, ferritin ↑); promotes Th17 over Treg; drives hepatic thrombopoietin → thrombocytosis; JAK1/2-STAT3 signaling; the most clinically targetable cytokine
- **IFN-γ** — produced by activated T cells and NK cells; potent macrophage activator (M1 polarization); essential driver in HLH/MAS and viral CS; synergizes with TNF-α to cause hepatocyte apoptosis

**Chemokines (tissue recruitment):**
- **CXCL8 (IL-8)** — primary neutrophil chemokine; massively elevated in ARDS-associated CS; drives pulmonary neutrophilia
- **MCP-1 (CCL2)** — monocyte/macrophage recruitment; particularly elevated in CAR-T CRS; secondary macrophage amplification

**The self-amplifying macrophage-T cell loop:**
Activated macrophages → IFN-γ on T cells → T cell production of IFN-γ → further macrophage activation → more TNF-α, IL-6, IL-1β → more T cell activation → cycle continues until feedback fails

### Coagulation Cascade Activation

CS drives a **consumptive coagulopathy (DIC)**:
- TNF-α + IL-1β → endothelial tissue factor (TF) expression → extrinsic coagulation pathway → thrombin generation → fibrin deposition in microvasculature → thrombotic microangiopathy
- Plasminogen activator inhibitor-1 (PAI-1) upregulation → impaired fibrinolysis
- Platelet consumption → thrombocytopenia
- Factor consumption → bleeding tendency paradoxically coexists with microvascular thrombosis (the DIC paradox)
- **COVID-19 hypercoagulability**: particularly driven by anti-phospholipid antibodies and endothelial injury in addition to DIC

## Function

### Pathophysiology of End-Organ Damage

**Lung (ARDS):**
- Endothelial barrier disruption (TNF-α, VEGF, histamine) → protein-rich edema
- Massive neutrophil recruitment (CXCL8) → neutrophil elastase, ROS, NETs → epithelial and endothelial necrosis
- Surfactant inhibition → microatelectasis
- IL-6 → systemic acute-phase response amplifies pulmonary inflammation

**Cardiovascular:**
- Myocarditis: IFN-γ + TNF-α → cardiomyocyte apoptosis and impaired contractility
- Distributive shock: NO overproduction (iNOS induction) → vasoplegia → refractory hypotension
- Stress cardiomyopathy (Takotsubo pattern) in severe CS

**Liver:**
- IFN-γ + TNF-α → hepatocyte apoptosis and necrosis → transaminase elevation
- Hyperferritinemia (ferritin released from damaged macrophages and hepatocytes) — diagnostic marker of MAS/HLH
- Coagulopathy from reduced hepatic synthetic function

**Kidney:**
- Inflammatory cytokines + hemodynamic compromise + direct tubular cytotoxicity → AKI
- Thrombotic microangiopathy in small renal vessels

**CNS:**
- Encephalopathy: cytokine-mediated BBB disruption; IL-6-driven neuroinflammation
- Hypercoagulability → ischemic stroke risk

### Grading Systems

**CAR-T CRS (ASTCT 2019 consensus):**
| Grade | Features |
|:---|:---|
| 1 | Fever only (≥38°C) |
| 2 | Fever + hypotension (IVF-responsive) or O₂ requirement (low-flow) |
| 3 | Hypotension (vasopressors) or O₂ by HF nasal cannula/mask |
| 4 | Life-threatening hypotension or mechanical ventilation |

**HLH diagnostic criteria (HScore/HLH-2004):** Fever, splenomegaly, cytopenias (≥2 lineages), hypertriglyceridemia, hemophagocytosis, low NK activity, hyperferritinemia (>500), elevated sIL-2R

## Connections

- `modulated-by` → **[Macrophage](../../04-cellular/macrophage/README.md)** — primary amplifiers of cytokine storm via self-reinforcing activation loops with T cells; macrophage activation syndrome (MAS) represents uncontrolled macrophage activation
- `modulated-by` → **[IL-6](../../03-molecular/il-6/README.md)** — dominant amplifier cytokine; tocilizumab (anti-IL-6R) reduces CS mortality in COVID-ARDS and CAR-T CRS
- `modulated-by` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — proximal alarm cytokine activating NF-κB; drives vascular permeability, DIC, and hepatocyte injury
- `modulated-by` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — master transcriptional driver of pro-inflammatory cytokine expression in macrophages and endothelial cells during CS
- `modulates` → **[Lung](../../06-organ/lung/README.md)** — cytokine storm causes ARDS via neutrophil-mediated alveolar damage and endothelial barrier disruption
- `modulated-by` → **[Dexamethasone](../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — suppresses cytokine storm via GR:NF-κB transrepression (↓ IL-1β/IL-6/TNF-α) and GRE transactivation (IκBα/IL-10/ANXA1); primary mechanism of RECOVERY trial benefit and CAR-T CRS treatment.

## Pathology

### Treatment Strategies

**Trigger-specific management:**
- **COVID-19 ARDS**: Dexamethasone 6 mg/day × 10 days (RECOVERY trial: 35% reduction in 28-day mortality in ventilated patients) + Tocilizumab 8 mg/kg IV (RECOVERY + REMAP-CAP: additional 24% mortality reduction)
- **CAR-T CRS**: Grade 1–2: supportive; Grade ≥2: Tocilizumab 8 mg/kg IV ± dexamethasone; Grade 4: ICU support + high-dose corticosteroids
- **HLH**: HLH-94 protocol: etoposide + dexamethasone + cyclosporine; IL-1R blockade (anakinra) increasingly used in MAS/sHLH; Emapalumab (anti-IFN-γ) approved for primary HLH
- **Sepsis**: Source control + antibiotics + supportive care; no specific anti-cytokine therapy proven except IL-6 blockade in COVID-ARDS

**Monitoring biomarkers:**
- Ferritin (markedly elevated in HLH/MAS; trends with disease activity)
- CRP and IL-6 levels (cytokine storm activity; guide tocilizumab use)
- D-dimer, fibrinogen (DIC monitoring)
- Troponin, BNP (cardiac involvement)
- LDH (cellular injury, hemophagocytosis)

[^fajgenbaum-june-2020-cytokine-storm]: Fajgenbaum DC, June CH. Cytokine Storm. *N Engl J Med.* 2020;383(23):2255-2273. [doi:10.1056/NEJMra2026131](https://doi.org/10.1056/NEJMra2026131) · [PubMed 33264547](https://pubmed.ncbi.nlm.nih.gov/33264547/)
[^tisoncik-2012-cytokine-storm-review]: Tisoncik JR et al. Into the eye of the cytokine storm. *Microbiol Mol Biol Rev.* 2012;76(1):16-32. [doi:10.1128/MMBR.05015-11](https://doi.org/10.1128/MMBR.05015-11) · [PubMed 22390970](https://pubmed.ncbi.nlm.nih.gov/22390970/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
