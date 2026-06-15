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
  - target: 03-medicine/01-modern/05-antiviral/oseltamivir
    relation: connects-to
    note: "Severe influenza triggers cytokine storm (IL-6, TNF-α, IFN-γ) proportional to viral load; oseltamivir limits viral replication → attenuates cytokine storm magnitude; key rationale for treatment in H5N1 and severe seasonal influenza beyond the 48h window."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulated-by
    note: "The cytokine storm runs on a macrophage-T-cell feedback loop: activated CD4+ T cells and NK cells pour out IFN-γ that hyperactivates macrophages, which release IL-6, TNF-α, and IL-1β feeding back to the T cells — a self-amplifying circuit that escalates until regulation fails."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Severe dengue is a viral cytokine storm: antibody-dependent enhancement raises macrophage viral load while cross-reactive T cells release TNF-α, IL-6, and IFN-γ, and the resulting endothelial activation produces the plasma leakage of dengue hemorrhagic fever and shock."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Cytokine storm drives DIC: TNF-α and IL-1β induce tissue factor on endothelium and monocytes, igniting coagulation that deposits microthrombi and consumes platelets and clotting factors — so the patient bleeds and clots at once, a frequent cause of cytokine-storm organ failure."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Severe COVID-19 is a paradigm cytokine storm: SARS-CoV-2 triggers an overwhelming IL-6/IL-1/TNF surge that drives ARDS, coagulopathy and multiorgan failure rather than direct viral cytopathology, which is why dexamethasone and IL-6 blockade (tocilizumab) cut mortality."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Cytokine release syndrome is the defining acute toxicity of CAR-T and allogeneic transplant: engrafting or engineered T cells flood the body with IFN-γ, IL-6 and TNF, causing fever, hypotension and capillary leak overlapping with severe GVHD; tocilizumab and steroids treat it."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β is a core driver and target of cytokine storm: inflammasome-activated IL-1β amplifies the IL-6/TNF feed-forward loop, fever and vascular leak, so the IL-1 receptor antagonist anakinra is used to break cytokine storm in HLH/MAS, severe COVID-19 and CAR-T toxicity."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Sepsis is the commonest cytokine storm: infection triggers a dysregulated systemic release of IL-6, TNF, and IL-1 that injures the endothelium and drives shock and multi-organ failure—so sepsis and cytokine storm syndromes share mediators and cytokine-targeted therapy."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Severe and pandemic influenza can provoke a lethal cytokine storm: overwhelming innate activation floods the lungs with IL-6, TNF, and chemokines, causing ARDS out of proportion to viral load—part of why young, immunocompetent adults died in the 1918 and H5N1 outbreaks."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CAR-T therapy's main toxicity is a cytokine storm: the engineered cytotoxic T cells, on engaging tumor, trigger massive IL-6 release (cytokine release syndrome), so tocilizumab is kept on hand—a designed T-cell attack causing the same storm seen in infection."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The NLRP3 inflammasome ignites cytokine storms: sensing infection or cell damage, it activates caspase-1 to release IL-1 and IL-18, amplifying the self-reinforcing cascade—so inflammasome and IL-1 blockade (anakinra) treat severe hyperinflammation."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Failed NK/cytotoxic killing triggers the worst cytokine storms: in HLH, defective natural killer and CD8 cells cannot clear activated immune cells, so persistent antigen drives runaway macrophage activation—why HLH is lethal without immunosuppression."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Cytokine storm erupts in autoimmune disease as macrophage activation syndrome: in rheumatoid/Still's disease, uncontrolled macrophage and T-cell activation floods cytokines (high ferritin, falling counts)—the same IL-1/IL-6 biology, treated with the same blockers."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "ARDS is the lung's expression of a cytokine storm: flooding inflammatory mediators damage the alveolar-capillary barrier, so the storm's pulmonary endpoint—diffuse alveolar damage and refractory hypoxemia—is what most often kills in severe COVID, flu and sepsis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial cells are both victim and amplifier of cytokine storm: the inflammatory surge makes vessels leaky and prothrombotic, so capillary leak, edema and microthrombi—not the infection alone—drive the shock and multi-organ failure of severe hyperinflammation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibition is a key brake on cytokine storm: many storm cytokines (IL-6, interferon-gamma) signal through the JAK-STAT pathway, so JAK inhibitors like baricitinib—and IL-6 blockers—dampen the runaway loop, improving survival in severe COVID-19."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Interferon-gamma drives the deadliest cytokine storms: in HLH and macrophage activation syndrome, runaway IFN-γ from T and NK cells hyperactivates macrophages, so the anti-IFN-γ antibody emapalumab can rescue this otherwise fatal hyperinflammation."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Cytokine storm hits the liver hard: hyperinflammation (especially HLH/MAS) inflames the liver, spiking ferritin and transaminases and impairing clotting, so a sky-high ferritin with hepatitis is a key clue to a brewing cytokine storm."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Cytokine storm drives multi-organ failure starting with the kidney: inflammatory mediators and shock collapse renal perfusion, causing acute kidney injury, so rising creatinine marks the systemic spread of hyperinflammation beyond the initial trigger organ."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytokine storm erupts when killing fails: in HLH, defective perforin leaves cytotoxic T and NK cells unable to clear infected cells, so antigen persists and over-stimulates them into a runaway flood of cytokines—the genetic root of primary hemophagocytic syndrome."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is ground zero for hemophagocytosis in cytokine storm: hyperactivated macrophages there and in marrow devour red cells and platelets, so splenomegaly and falling blood counts are red flags for HLH/MAS-type storms."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Cytokine storm reflects a failed brake by regulatory T cells: Tregs normally rein in activated effector cells, so when their restraint is overwhelmed or deficient the inflammatory loop runs unchecked—why restoring Treg control is a therapeutic aim."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Cytokine storm suffocates patients through the lungs: the flood of cytokines makes lung capillaries leak, filling air sacs with fluid in ARDS so oxygen cannot cross, the hypoxemic respiratory failure that kills in severe COVID and sepsis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cytokine storm can stun the heart: high TNF and IL-6 directly depress the heart muscle, so even without infection of the heart, the inflammatory surge causes a cardiomyopathy that deepens shock and organ failure."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils amplify the cytokine storm: recruited en masse, they release enzymes, oxidants and NETs that damage tissue and trigger still more cytokines, turning the innate response into part of the runaway inflammatory loop."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "A cytokine storm acidifies the blood: the shock and tissue hypoperfusion it causes starve cells of oxygen, so they pour out lactic acid and blood pH falls—a metabolic acidosis marking the slide into multi-organ failure."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Cytokine storm can turn the marrow on itself: in HLH and macrophage activation syndrome, overactivated macrophages devour blood cells in the bone marrow (hemophagocytosis), the defining lesion of this extreme inflammatory state."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Cytokine storm consumes platelets: runaway clotting and inflammation use them up, so the falling platelet count, with rising DIC, is an early warning that the storm is damaging the blood and vessels."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging shows the cytokine storm's wreckage: chest CT photons reveal the diffuse lung infiltrates of ARDS, the most visible organ failure of the runaway inflammation."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ferritin soars in cytokine storm: the macrophage activation pours out this iron-storage protein, so an extremely high ferritin is a hallmark and diagnostic clue to HLH and severe inflammation."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cytokine storm clouds the brain: the flood of inflammatory mediators and fever cause encephalopathy, seizures and coma, the neurologic toll of HLH and severe systemic inflammation."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy catches the storm consuming the blood: in hemophagocytic syndromes, macrophages are seen engulfing whole red cells, platelets, and white cells, the cannibalism that empties the blood counts in HLH."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The runaway inflammation can wreck the gut: shock and capillary leak starve the bowel lining, breaking the barrier so bacteria translocate and feed the storm in a vicious cycle of multi-organ failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Cytokine storm drops the calcium: the systemic inflammation and disturbed hormone handling leave critically ill patients hypocalcemic, a derangement that further weakens the failing heart and vasculature."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody therapy both triggers and tames the storm: CAR-T and bispecific antibodies can unleash a cytokine release syndrome, while the anti-IL-6-receptor antibody tocilizumab is the specific drug used to quell it."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The storm clouds the brain: immune effector cell-associated neurotoxicity (ICANS) after CAR-T — and the encephalopathy of severe systemic inflammation — injures and disrupts neurons into confusion, aphasia, and seizures."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "In its HLH/MAS form the storm devours blood cells: hyperactivated macrophages engulf erythrocytes and other lineages (hemophagocytosis), crashing the counts while ferritin soars — a hallmark of the most severe cytokine storms."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "The brake fails as the storm rages: IL-10, the body's main anti-inflammatory cytokine, surges in a compensatory bid to quell the storm, and its high levels track with severity — a sign the counter-regulation is overwhelmed rather than winning."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The storm stuns the heart muscle: IL-6 and TNF directly depress cardiomyocyte contractility, producing the reversible cytokine-mediated cardiomyopathy and falling cardiac output seen in sepsis, severe COVID and CAR-T toxicity."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Severe malaria is a parasitic cytokine storm: falciparum infection drives a TNF- and IFN-gamma-rich surge that fuels cerebral malaria, lactic acidosis and shock, the same dysregulated inflammation seen in its viral and bacterial triggers."
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
- `connects-to` → **[Oseltamivir](../../03-medicine/01-modern/05-antiviral/oseltamivir/README.md)** — Severe influenza triggers cytokine storm (IL-6, TNF-α, IFN-γ) proportional to viral load; oseltamivir limits viral replication → attenuates cytokine storm magnitude; key rationale for H5N1 and severe influenza treatment beyond the 48h window.
- `modulated-by` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — the cytokine storm runs on a macrophage-T-cell feedback loop: activated CD4+ T cells and NK cells pour out IFN-γ that hyperactivates macrophages, which release IL-6, TNF-α, and IL-1β feeding back to the T cells — a self-amplifying circuit that escalates until regulation fails.
- `connects-to` → **[Dengue Fever](../dengue-fever/README.md)** — severe dengue is a viral cytokine storm: antibody-dependent enhancement raises macrophage viral load while cross-reactive T cells release TNF-α, IL-6, and IFN-γ, and the resulting endothelial activation produces the plasma leakage of dengue hemorrhagic fever and shock.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — cytokine storm drives DIC: TNF-α and IL-1β induce tissue factor on endothelium and monocytes, igniting coagulation that deposits microthrombi and consumes platelets and clotting factors — so the patient bleeds and clots at once, a frequent cause of cytokine-storm organ failure.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Severe COVID-19 is a paradigm cytokine storm: SARS-CoV-2 triggers an overwhelming IL-6/IL-1/TNF surge that drives ARDS, coagulopathy and multiorgan failure rather than direct viral cytopathology, which is why dexamethasone and IL-6 blockade (tocilizumab) cut mortality.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Cytokine release syndrome is the defining acute toxicity of CAR-T and allogeneic transplant: engrafting or engineered T cells flood the body with IFN-γ, IL-6 and TNF, causing fever, hypotension and capillary leak overlapping with severe GVHD; tocilizumab and steroids treat it.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β is a core driver and target of cytokine storm: inflammasome-activated IL-1β amplifies the IL-6/TNF feed-forward loop, fever and vascular leak, so the IL-1 receptor antagonist anakinra is used to break cytokine storm in HLH/MAS, severe COVID-19 and CAR-T toxicity.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Sepsis is the commonest cytokine storm: infection triggers a dysregulated systemic release of IL-6, TNF, and IL-1 that injures the endothelium and drives shock and multi-organ failure—so sepsis and cytokine storm syndromes share mediators and cytokine-targeted therapy.
- `connects-to` → **[Influenza](../influenza/README.md)** — Severe and pandemic influenza can provoke a lethal cytokine storm: overwhelming innate activation floods the lungs with IL-6, TNF, and chemokines, causing ARDS out of proportion to viral load—part of why young, immunocompetent adults died in the 1918 and H5N1 outbreaks.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CAR-T therapy's main toxicity is a cytokine storm: the engineered cytotoxic T cells, on engaging tumor, trigger massive IL-6 release (cytokine release syndrome), so tocilizumab is kept on hand—a designed T-cell attack causing the same storm seen in infection.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The NLRP3 inflammasome ignites cytokine storms: sensing infection or cell damage, it activates caspase-1 to release IL-1 and IL-18, amplifying the self-reinforcing cascade—so inflammasome and IL-1 blockade (anakinra) treat severe hyperinflammation.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Failed NK/cytotoxic killing triggers the worst cytokine storms: in HLH, defective natural killer and CD8 cells cannot clear activated immune cells, so persistent antigen drives runaway macrophage activation—why HLH is lethal without immunosuppression.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Cytokine storm erupts in autoimmune disease as macrophage activation syndrome: in rheumatoid/Still's disease, uncontrolled macrophage and T-cell activation floods cytokines (high ferritin, falling counts)—the same IL-1/IL-6 biology, treated with the same blockers.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — ARDS is the lung's expression of a cytokine storm: flooding inflammatory mediators damage the alveolar-capillary barrier, so the storm's pulmonary endpoint—diffuse alveolar damage and refractory hypoxemia—is what most often kills in severe COVID, flu and sepsis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial cells are both victim and amplifier of cytokine storm: the inflammatory surge makes vessels leaky and prothrombotic, so capillary leak, edema and microthrombi—not the infection alone—drive the shock and multi-organ failure of severe hyperinflammation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibition is a key brake on cytokine storm: many storm cytokines (IL-6, interferon-gamma) signal through the JAK-STAT pathway, so JAK inhibitors like baricitinib—and IL-6 blockers—dampen the runaway loop, improving survival in severe COVID-19.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Interferon-gamma drives the deadliest cytokine storms: in HLH and macrophage activation syndrome, runaway IFN-γ from T and NK cells hyperactivates macrophages, so the anti-IFN-γ antibody emapalumab can rescue this otherwise fatal hyperinflammation.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Cytokine storm hits the liver hard: hyperinflammation (especially HLH/MAS) inflames the liver, spiking ferritin and transaminases and impairing clotting, so a sky-high ferritin with hepatitis is a key clue to a brewing cytokine storm.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Cytokine storm drives multi-organ failure starting with the kidney: inflammatory mediators and shock collapse renal perfusion, causing acute kidney injury, so rising creatinine marks the systemic spread of hyperinflammation beyond the initial trigger organ.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytokine storm erupts when killing fails: in HLH, defective perforin leaves cytotoxic T and NK cells unable to clear infected cells, so antigen persists and over-stimulates them into a runaway flood of cytokines—the genetic root of primary hemophagocytic syndrome.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is ground zero for hemophagocytosis in cytokine storm: hyperactivated macrophages there and in marrow devour red cells and platelets, so splenomegaly and falling blood counts are red flags for HLH/MAS-type storms.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Cytokine storm reflects a failed brake by regulatory T cells: Tregs normally rein in activated effector cells, so when their restraint is overwhelmed or deficient the inflammatory loop runs unchecked—why restoring Treg control is a therapeutic aim.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Cytokine storm suffocates patients through the lungs: the flood of cytokines makes lung capillaries leak, filling air sacs with fluid in ARDS so oxygen cannot cross, the hypoxemic respiratory failure that kills in severe COVID and sepsis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cytokine storm can stun the heart: high TNF and IL-6 directly depress the heart muscle, so even without infection of the heart, the inflammatory surge causes a cardiomyopathy that deepens shock and organ failure.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils amplify the cytokine storm: recruited en masse, they release enzymes, oxidants and NETs that damage tissue and trigger still more cytokines, turning the innate response into part of the runaway inflammatory loop.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — A cytokine storm acidifies the blood: the shock and tissue hypoperfusion it causes starve cells of oxygen, so they pour out lactic acid and blood pH falls—a metabolic acidosis marking the slide into multi-organ failure.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Cytokine storm can turn the marrow on itself: in HLH and macrophage activation syndrome, overactivated macrophages devour blood cells in the bone marrow (hemophagocytosis), the defining lesion of this extreme inflammatory state.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Cytokine storm consumes platelets: runaway clotting and inflammation use them up, so the falling platelet count, with rising DIC, is an early warning that the storm is damaging the blood and vessels.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging shows the cytokine storm's wreckage: chest CT photons reveal the diffuse lung infiltrates of ARDS, the most visible organ failure of the runaway inflammation.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ferritin soars in cytokine storm: the macrophage activation pours out this iron-storage protein, so an extremely high ferritin is a hallmark and diagnostic clue to HLH and severe inflammation.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cytokine storm clouds the brain: the flood of inflammatory mediators and fever cause encephalopathy, seizures and coma, the neurologic toll of HLH and severe systemic inflammation.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy catches the storm consuming the blood: in hemophagocytic syndromes, macrophages are seen engulfing whole red cells, platelets, and white cells, the cannibalism that empties the blood counts in HLH.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The runaway inflammation can wreck the gut: shock and capillary leak starve the bowel lining, breaking the barrier so bacteria translocate and feed the storm in a vicious cycle of multi-organ failure.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Cytokine storm drops the calcium: the systemic inflammation and disturbed hormone handling leave critically ill patients hypocalcemic, a derangement that further weakens the failing heart and vasculature.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody therapy both triggers and tames the storm: CAR-T and bispecific antibodies can unleash a cytokine release syndrome, while the anti-IL-6-receptor antibody tocilizumab is the specific drug used to quell it.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The storm clouds the brain: immune effector cell-associated neurotoxicity (ICANS) after CAR-T — and the encephalopathy of severe systemic inflammation — injures and disrupts neurons into confusion, aphasia, and seizures.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — In its HLH/MAS form the storm devours blood cells: hyperactivated macrophages engulf erythrocytes and other lineages (hemophagocytosis), crashing the counts while ferritin soars — a hallmark of the most severe cytokine storms.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The brake fails as the storm rages: IL-10, the body's main anti-inflammatory cytokine, surges in a compensatory bid to quell the storm, and its high levels track with severity — a sign the counter-regulation is overwhelmed rather than winning.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The storm stuns the heart muscle: IL-6 and TNF directly depress cardiomyocyte contractility, producing the reversible cytokine-mediated cardiomyopathy and falling cardiac output seen in sepsis, severe COVID and CAR-T toxicity.
- `connects-to` → **[Malaria](../malaria/README.md)** — Severe malaria is a parasitic cytokine storm: falciparum infection drives a TNF- and IFN-gamma-rich surge that fuels cerebral malaria, lactic acidosis and shock, the same dysregulated inflammation seen in its viral and bacterial triggers.

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
