---
schema: human-scale-entry/v1
id: sepsis
name: Sepsis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Life-threatening organ dysfunction from dysregulated host response to infection (Sepsis-3: SOFA ≥2). LPS triggers TLR4→NF-κB and NLRP3 inflammasome; cytokine storm causes vasodilation, DIC, and organ failure. Mortality 20–30%; treated with antibiotics and vasopressors."
aliases: ["septicemia", "bacteremia", "septic shock", "SIRS", "systemic inflammatory response syndrome"]
sources:
  - id: singer-2016-sepsis3
    type: peer-reviewed
    cite: "Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810."
    doi: "10.1001/jama.2016.0287"
    pmid: "26903338"
    url: "https://doi.org/10.1001/jama.2016.0287"
  - id: vanderpoll-2017-sepsis-immunopathology
    type: peer-reviewed
    cite: "van der Poll T, van de Veerdonk FL, Scicluna BP, Netea MG. The immunopathology of sepsis and potential therapeutic targets. Nat Rev Immunol. 2017;17(7):407-420."
    doi: "10.1038/nri.2017.36"
    pmid: "28436424"
    url: "https://doi.org/10.1038/nri.2017.36"
  - id: evans-2021-surviving-sepsis
    type: peer-reviewed
    cite: "Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Intensive Care Med. 2021;47(11):1181-1247."
    doi: "10.1007/s00134-021-06506-y"
    pmid: "34599691"
    url: "https://doi.org/10.1007/s00134-021-06506-y"
cross_links:
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe sepsis can evolve into cytokine storm; TNF-α, IL-1β, IL-6, and HMGB1 drive vascular leak, DIC, and multi-organ failure; overlap with macrophage activation syndrome (MAS) and HLH makes distinguishing sepsis from primary hyperinflammation difficult."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "LPS and bacterial DAMPs activate NLRP3 inflammasome in macrophages → caspase-1 → IL-1β/IL-18 and pyroptotic cell death → amplify the septic inflammatory cascade; NLRP3 inhibition (MCC950) attenuates organ injury in preclinical sepsis models."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "TLR4 (LPS) and TLR2 (lipoteichoic acid) signal via MyD88/TRIF → IRAK4→TRAF6→TAK1→IKK → NF-κB nuclear translocation → TNF-α, IL-1β, IL-6, iNOS, COX-2; NF-κB is the master transcription factor of the innate immune activation in gram-negative and gram-positive sepsis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is an early dominant mediator of septic shock; TLR4 → NF-κB → rapid TNF-α release from macrophages → iNOS-mediated NO → vasodilation → distributive shock; despite strong preclinical rationale, anti-TNF therapy has consistently failed to improve sepsis survival in RCTs."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "ADM rises dramatically in sepsis proportional to severity; vasodilation (CLR/RAMP2 → cAMP → vasodilation) contributes to distributive shock; MR-proADM predicts 28-day mortality with AUC >0.80 and guides antibiotic de-escalation in the ADAPT-sepsis trial."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "TLR4/LPS triggers gram-negative sepsis: LPS-MD-2-CD14 → TLR4 → MyD88 (NF-κB: cytokine storm) + TRIF (IRF3: IFN-β); TLR4 Asp299Gly/Thr399Ile SNPs → altered sepsis risk; OxLDL activates TLR4 → sterile inflammation; TAK-242 (TLR4 antagonist) failed Phase III sepsis trials."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 mediates the immunosuppressive phase of sepsis: inflammatory peak → IL-10 surge → macrophage STAT3 → ↓TNF-α, ↓IL-1β, ↓IL-12 → immunoparalysis → secondary nosocomial infections; elevated day-1 IL-10 predicts mortality; PD-1/PD-L1 co-upregulation amplifies immunosuppression."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-2 released from Weibel-Palade bodies in sepsis → Tie2 destabilization → VE-cadherin cleavage → vascular hyperpermeability → organ edema; plasma Ang-2 >10 ng/mL on day 1 predicts ICU mortality; high Ang-2/Ang-1 ratio defines the severe vascular leak phenotype."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "cTnI and cTnT are elevated in 40-85% of septic patients reflecting cardiomyocyte injury from hypoperfusion, inflammatory cytokines, and ROS; sepsis-induced cardiomyopathy causes new LV dysfunction; troponin elevation in sepsis independently predicts ICU mortality."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "In sepsis, contact activation (FXII → kallikrein → bradykinin) contributes to vascular leak; C1-INH levels fall during severe sepsis from consumption; C1-INH concentrate investigated for sepsis capillary leak; C1-INH inhibits complement and contact activation in septic shock."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "APC is consumed in sepsis-DIC → protein C levels < 40% predict 28-day mortality; acquired PC deficiency → purpura fulminans; drotrecogin alfa (rhAPC) reduced mortality in PROWESS (2001) but PROWESS-SHOCK (2011) showed no benefit in septic shock → withdrawn 2011."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: treated-by
    note: "Vancomycin is first-line empiric IV therapy for MRSA bacteremia and gram-positive sepsis; added to beta-lactam empiric regimens when MRSA risk is elevated; AUC/MIC-guided dosing (IDSA 2021); MIC ≤1 mg/L required for endocarditis; daptomycin alternative for high MIC."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Sepsis is the leading cause of disseminated intravascular coagulation: microbial products trigger tissue-factor expression that consumes clotting factors and platelets, causing simultaneous clotting and bleeding—a marker of severe sepsis and poor prognosis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial dysfunction is the heart of septic shock: inflammatory mediators make endothelial cells leaky and prothrombotic, causing capillary leak, hypotension, and microthrombosis that drive multi-organ failure—the endothelium, not infection alone, sets outcome."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are double-edged in sepsis: they fight the infection but their NETs and proteases injure host tissue and endothelium, and as sepsis progresses they become dysfunctional (immunoparalysis), so both hyperinflammation and later immunosuppression worsen outcomes."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide drives septic shock: overwhelming inflammation induces iNOS, flooding vessels with NO that causes profound vasodilation and hypotension refractory to fluids—so the molecule that normally tunes blood flow becomes the engine of distributive shock in sepsis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Acute kidney injury is among the commonest organ failures in sepsis: hypotension, inflammation and microvascular thrombosis cut renal perfusion, so rising creatinine and falling urine output mark severity—and septic AKI strongly predicts mortality and may need dialysis."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Escherichia coli is a leading cause of sepsis: gram-negative bacteremia, often from urinary or abdominal sources, releases LPS endotoxin that triggers the TLR4-driven cytokine cascade—so a common gut commensal becomes a frequent driver of life-threatening septic shock."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help ignite sepsis: sensing bacterial products through TLRs, they release the TNF and IL-6 surge that drives the dysregulated systemic inflammation, yet later become immunoparalyzed—so sepsis is both hyperinflammation and immune exhaustion."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Sepsis is the leading cause of ARDS: systemic inflammation and capillary leak flood the alveoli, so the lungs become stiff and hypoxemic—acute respiratory distress is one of the most common and lethal organ failures of severe sepsis."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Streptococcus pneumoniae is a top cause of sepsis: pneumococcal pneumonia and bacteremia trigger the systemic inflammatory cascade, especially in the asplenic and elderly—why pneumococcal vaccination is a key sepsis-prevention measure."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Staphylococcus aureus is a leading cause of sepsis: from skin, lines, and wounds it invades the bloodstream, and MRSA bacteremia and toxins can rapidly tip into septic shock—so prompt source control and the right antibiotics are decisive."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is both defender and casualty in sepsis: it clears gut-derived endotoxin and mounts the acute-phase response, but septic shock starves it of blood, causing 'shock liver' and cholestasis that worsen coagulopathy and multi-organ failure."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Sepsis consumes platelets: widespread endothelial activation and DIC trap and destroy platelets, so a falling platelet count is an early warning of severe sepsis—and the bleeding-clotting imbalance it signals drives organ damage."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lungs are sepsis's most vulnerable organ: systemic inflammation injures the alveolar-capillary barrier, flooding air sacs to cause ARDS—the acute respiratory failure that often dominates and drives the need for ventilation in severe sepsis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Septic shock involves a vasopressin deficit: the inflammatory vasodilation that drops blood pressure outstrips the body's vasopressin, so vasopressin is added to norepinephrine as a vasopressor to restore perfusion in refractory shock."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Sepsis ends in immune paralysis as T cells die off: after the early cytokine storm, massive lymphocyte apoptosis and T-cell exhaustion leave survivors immunosuppressed and prone to secondary infections—a target for immune-restoring therapies."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Sepsis starves tissues of oxygen despite full lungs: leaky vessels, low blood pressure and mitochondrial failure stop cells using oxygen, so lactate rises—a key warning that sepsis is becoming shock."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Sepsis can stun the heart: inflammatory mediators depress the heart muscle in septic cardiomyopathy, so even a structurally normal heart pumps weakly, deepening the shock and the drop in tissue perfusion."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Sepsis flips into immune paralysis partly via regulatory T cells: as the early storm fades, expanding Tregs help suppress the exhausted immune system, leaving survivors unable to fight the secondary infections that often kill them."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Sepsis clouds the brain early: inflammation, poor perfusion, and toxins cause sepsis-associated encephalopathy, so confusion and delirium are often the first and most sensitive sign that an infection has turned to sepsis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Septic shock turns the blood acidic: starved cells switch to anaerobic metabolism and pour out lactic acid, so rising hydrogen ions (and lactate) mark the metabolic acidosis that signals worsening shock."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Sepsis later cripples its own helper T cells: widespread apoptosis wipes out CD4 T-helper cells, leaving an immunoparalysis that makes survivors prey to secondary infections in the days and weeks after."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Finding sepsis's source needs imaging: CT and X-ray photons hunt the abscess, pneumonia or perforation driving the infection, since draining the source is as vital as the antibiotics."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Sepsis drives the bone marrow hard: it ramps up neutrophil production—the 'left shift' of immature bands in the blood—and, in severe disease, becomes suppressed, deepening the cytopenias of overwhelming infection."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Sepsis can wreck the adrenal glands: fulminant meningococcal sepsis bleeds into them (Waterhouse-Friderichsen) to cause acute adrenal failure, and critical-illness adrenal insufficiency complicates shock."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows sepsis starving cells of energy: mitochondria swell and fail in a 'cytopathic hypoxia' where oxygen is present but unusable, while the endothelial glycocalyx sheds away, opening vessels to leak and clot."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut is called the motor of sepsis: shock starves the intestinal lining until its barrier fails, letting bacteria and their toxins translocate into the blood and stoke the inflammation that perpetuates multi-organ failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Sepsis drops the calcium: inflammation and impaired parathyroid and vitamin D handling leave many septic patients hypocalcemic, a disturbance that can weaken the already failing heart and must be watched in the ICU."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin shows shock at the bedside: mottled, cold, slow-to-refill skin signals the collapsing perfusion of septic shock, and in fulminant disease purpura fulminans marks the disseminated clotting beneath."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Survivors are left weak for months: ICU-acquired weakness — a critical-illness myopathy and polyneuropathy driven by sepsis inflammation and immobility — wastes muscle and slows recovery long after the infection clears."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Sepsis thins and shears the red cells: inflammation suppresses their production and repeated blood draws deplete them, while disseminated clotting fragments them into the schistocytes of microangiopathy."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is a central alarm of sepsis: it pours from activated immune cells to drive fever and the acute-phase response, serving as a severity marker, and blocking it (tocilizumab) tempers the cytokine storm of severe infection."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement runs wild in sepsis: explosive C5a generation recruits and over-activates neutrophils and injures the endothelium, amplifying the inflammation and clotting, which is why C5-blockade is studied to calm the storm."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Maternal sepsis is a leading cause of death in childbirth: postpartum uterine infection and chorioamnionitis can spill into the bloodstream, and the physiologic changes of pregnancy can mask the early warning signs."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Sepsis unleashes the kinin cascade: contact activation generates bradykinin, a potent vasodilator that drops blood pressure and leaks the capillaries, contributing to the shock and edema of severe infection."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Not all sepsis is bacterial: Candida bloodstream infection is a leading cause of fungal sepsis in the ICU, hard to clear, slow to diagnose, and carrying a high mortality in the immunocompromised."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Sepsis turns immune-suppressive after the storm: it depletes dendritic cells and cripples their antigen presentation, a key part of the immunoparalysis that leaves survivors prey to secondary infection."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "The stress axis falters in sepsis: cortisol surges early, but critical-illness-related corticosteroid insufficiency can leave the response inadequate for the vasodilatory shock, which is why low-dose hydrocortisone is given in refractory septic shock."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Meningococcus causes the most fulminant sepsis: Neisseria meningitidis endotoxin can trigger purpura fulminans and Waterhouse-Friderichsen adrenal hemorrhage, killing previously well young people within hours."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is the guard against overwhelming sepsis: it clears encapsulated bacteria from the blood, so asplenic patients face fulminant OPSI from pneumococcus and meningococcus and need vaccination and standby antibiotics."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "It is the leading cause of kidney injury in the critically ill: septic shock starves and inflames the kidneys into acute kidney injury, and survivors of severe episodes often progress to chronic kidney disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The heart stuns under the cytokine storm: septic cardiomyopathy depresses myocardial contractility through inflammatory mediators and nitric oxide, a reversible heart failure that worsens the shock and is usually flagged by a troponin rise."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Sepsis is intensely prothrombotic: endothelial injury, immobility and activated coagulation make deep-vein thrombosis and pulmonary embolism common in septic ICU patients, even beyond the microthrombi of overt DIC."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "It can trigger the most explosive shock: Streptococcus pyogenes causes streptococcal toxic shock syndrome and necrotizing fasciitis, where superantigen-driven cytokine release produces a fulminant sepsis with rapid multiorgan failure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Sepsis can strike the brain's vessels: septic emboli from endocarditis, the profound hypotension of shock and the prothrombotic state can all cause ischemic stroke during severe sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Survival carries a lasting mental toll: survivors of severe sepsis frequently develop depression, anxiety and cognitive impairment — part of the post-intensive-care syndrome that follows critical illness."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Surviving the ICU can leave trauma: the delirium, ventilation and life-threatening course of severe sepsis frequently leave survivors with post-traumatic stress, a core part of post-intensive-care syndrome."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Critical illness damages the nerves: severe sepsis causes critical-illness polyneuropathy and myopathy, leaving lasting weakness and neuropathic pain that prolong recovery for months."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Shock and microthrombi starve the skin: sepsis-driven hypoperfusion, vasopressors and disseminated coagulation cause tissue ischemia and necrosis — even limb gangrene — leaving major wounds that heal poorly."
---

# Sepsis

## Overview

**Sepsis** is a life-threatening syndrome of **organ dysfunction caused by a dysregulated host response to infection** — defined by the **Sepsis-3 consensus** (Singer et al., 2016) as a suspected or confirmed infection plus an acute increase in the **SOFA (Sequential Organ Failure Assessment) score ≥2** [^singer-2016-sepsis3]. The definition deliberately shifted from the earlier SIRS (systemic inflammatory response syndrome) criteria, which were non-specific and did not require organ dysfunction, recognizing that the pathological hallmark of sepsis is **aberrant immune activation causing collateral organ damage**, not merely systemic inflammation.

**Septic shock** is the most severe form: sepsis plus vasopressor requirement to maintain mean arterial pressure ≥65 mmHg plus serum lactate >2 mmol/L (despite adequate volume resuscitation) — in-hospital mortality ~40%.

**Epidemiology:**
- ~49 million cases of sepsis globally per year; ~11 million deaths (~20% of all global deaths; Global Burden of Disease 2017)
- In ICUs, sepsis is the leading cause of mortality in high-income countries
- Disproportionate burden in low- and middle-income countries due to limited diagnostic and therapeutic resources
- Risk factors: extremes of age, immunocompromise, cancer, CKD, diabetes, prior hospitalization, invasive devices

**Common causative organisms:**
- Gram-negative bacteria (E. coli, Klebsiella, Pseudomonas, Acinetobacter): LPS-mediated TLR4 activation
- Gram-positive bacteria (S. aureus, Streptococcus, Enterococcus): lipoteichoic acid (TLR2), peptidoglycan, superantigens (TCR Vβ cross-linking → massive cytokine release)
- Fungi (Candida, Aspergillus): typically in immunocompromised hosts
- Viral (COVID-19, influenza): cytokine storm with features overlapping bacterial sepsis

## Structure

### Sepsis as a systemic syndrome: organ-by-organ dysfunction

Sepsis is not localized to one system — it manifests as dysfunction across multiple organs simultaneously, scored by SOFA:

| SOFA Component | Measurement | Score 0-4 based on severity |
|:---|:---|:---|
| Respiratory | PaO₂/FiO₂ ratio | Normal >400 → severe ARDS <100 |
| Coagulation | Platelet count | Normal >150K → <50K |
| Liver | Bilirubin | <1.2 → ≥12 mg/dL |
| Cardiovascular | MAP or vasopressors | No vasopressors → high-dose dual vasopressors |
| CNS | GCS | 15 → <6 |
| Renal | Creatinine or urine output | <1.2 mg/dL → ≥5 mg/dL or <200 mL/day |

**Key pathological processes:**

1. **Septic cardiomyopathy:** Cytokines (TNF-α, IL-1β, NO) suppress myocardial contractility → biventricular dysfunction; usually reversible if patient survives
2. **Septic encephalopathy:** BBB disruption (NF-κB, COX-2, iNOS in brain endothelium), neuroinflammation, cerebral hypoperfusion → delirium (most common ICU complication); long-term cognitive impairment in survivors
3. **Acute Kidney Injury (AKI):** Renal hypoperfusion + direct cytokine toxicity + tubular apoptosis → oliguric AKI; renal replacement therapy required in ~5% of sepsis patients
4. **Disseminated Intravascular Coagulation (DIC):** Endothelial injury + thrombin generation + consumption of platelets and coagulation factors → simultaneous microvascular thrombosis and hemorrhage

## Function

### Pathophysiology: the immune cascade [^vanderpoll-2017-sepsis-immunopathology]

**Phase 1 — Pattern recognition and innate activation:**
- Bacterial PAMPs (pathogen-associated molecular patterns): LPS (gram-negative), LTA and peptidoglycan (gram-positive), flagellin, bacterial DNA (CpG)
- Host DAMPs (damage-associated molecular patterns): HMGB1 (released by necrotic cells), mitochondrial DNA, ATP, heat shock proteins — released as organ injury progresses
- **TLR4 (LPS receptor):** LPS → CD14/MD-2/TLR4 complex → MyD88→IRAK4→TRAF6→TAK1→IKK → NF-κB (TNF-α, IL-1β, IL-6, IL-8, MCP-1, iNOS, COX-2) and TRIF→IRF3 → IFN-β
- **TLR2 (gram-positive):** LTA → heterodimer TLR2/1 or TLR2/6 → MyD88 → NF-κB (same cytokine program)

**Phase 2 — Cytokine storm amplification:**
- TNF-α (first peak, 1-2 hours): Primary mediator of cardiovascular collapse; causes iNOS induction in endothelium and smooth muscle → NO → vasodilation → distributive shock; also induces endothelial E-selectin, VCAM-1 → neutrophil adhesion → tissue damage
- IL-1β (NLRP3 inflammasome-derived): Amplifies TNF-α effects; promotes tissue factor expression → DIC; pyrogenic
- IL-6 (12-24 hours): Acute phase response (liver: CRP, fibrinogen, SAA); drives Th17 differentiation; best temporal correlate of sepsis mortality
- **HMGB1 (late, 16-32 hours):** Alarmin released from necrotic cells; sustains late-phase inflammation; explains why late anti-inflammatory interventions fail

**Phase 3 — Immune paralysis (late phase):**
- Paradoxically, most late sepsis deaths occur in an immunosuppressed state — "immunoparalysis":
- Lymphocyte apoptosis (massive T and B cell death via mitochondrial apoptosis, FasL/Fas, and BCL-2-dependent pathways) → lymphopenia
- Monocyte deactivation: reduced HLA-DR expression → impaired antigen presentation → secondary infections
- NK cell and NK-T cell exhaustion
- PD-1/PD-L1 upregulation on T cells → functional exhaustion (checkpoint therapy [anti-PD-1] in clinical trials for sepsis immunoparalysis)

### Coagulation dysfunction in sepsis: DIC

1. Endothelial injury + inflammatory cytokines → **tissue factor (TF, FIII) upregulation** on monocytes and endothelial cells → activates extrinsic coagulation cascade → thrombin burst
2. Thrombin → fibrinogen → fibrin → microvascular thrombi (consume platelets, FIII, FV, FVIII, fibrinogen) → thrombocytopenia + prolonged PT/aPTT + low fibrinogen + high D-dimer
3. Plasminogen activator inhibitor-1 (PAI-1) upregulated by cytokines → impairs fibrinolysis → fibrin clots persist → microangiopathy → AKI, ARDS, gut ischemia
4. Simultaneous hemorrhage from consumption of factors → bleeding complications

**DIC management:** Treat underlying sepsis; platelet/FFP transfusion for active bleeding or prophylaxis at <10K or <50K (procedural); recombinant thrombomodulin (approved in Japan) — modest mortality benefit in DIC-complicated sepsis.

## Pathology

### Mortality predictors and risk stratification

- **Lactate >4 mmol/L:** Tissue hypoperfusion marker; 3-hour lactate >4 = septic shock mortality 40-50%
- **SOFA score:** 1-point increase = ~10% increase in ICU mortality
- **Procalcitonin (PCT):** Reflects bacterial translocation and cytokine-driven hepatic synthesis; PCT-guided antibiotic de-escalation reduces antibiotic exposure
- **Low monocyte HLA-DR (<30%):** Marks immunoparalysis → risk of secondary nosocomial infection

### Treatment: Surviving Sepsis Campaign 2021 [^evans-2021-surviving-sepsis]

**Hour-1 bundle (targets to initiate within 1 hour):**
1. **Measure lactate** (repeat if initial >2 mmol/L)
2. **Blood cultures** before antibiotics (≥2 sets; do not delay antibiotics >45 minutes for cultures)
3. **Broad-spectrum antibiotics within 1 hour** of sepsis recognition — every hour of antibiotic delay increases mortality by ~7%
4. **30 mL/kg IV crystalloid** bolus if hypotension or lactate ≥4
5. **Vasopressors** (norepinephrine first-line) if MAP <65 during/after fluid resuscitation

**Subsequent management:**
- **Source control:** Drainage of abscess, catheter removal, debridement within 6-12 hours
- **Norepinephrine:** First-line vasopressor; targets MAP ≥65; add vasopressin (0.03 U/min, spares norepinephrine dose) for refractory shock
- **Corticosteroids:** Hydrocortisone 200 mg/day IV for vasopressor-refractory septic shock (APROCCHSS/ADRENAL trials — reduces shock duration, modest impact on mortality)
- **Glucose control:** Target 140-180 mg/dL (NICE-SUGAR trial: tight control 80-110 mg/dL worsened survival)
- **Lung-protective ventilation:** Tidal volume ≤6 mL/kg IBW, PEEP as per ARDSnet protocol for sepsis-associated ARDS

**Failed immunomodulatory strategies:**
- Anti-TNF-α (filgrastim, lenercept, afelimomab): multiple Phase III trials — no survival benefit
- Recombinant IL-1ra (anakinra): Phase III negative; promising in macrophage activation syndrome-associated sepsis
- Activated protein C (drotrecogin alfa): approved 2001, withdrawn 2011 (PROWESS-SHOCK: no benefit, bleeding risk)
- Anti-HMGB1: preclinical only; no approved therapy
- IL-7 (reverse immunoparalysis): Phase II positive signals — ongoing trials

## Connections

- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — severe sepsis can evolve into cytokine storm with massive TNF-α, IL-1β, IL-6, and HMGB1 release; DIC, vascular leak, and multi-organ failure overlap with macrophage activation syndrome; pathological immune amplification is the shared mechanism.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — LPS and bacterial DAMPs activate NLRP3 in macrophages → IL-1β/IL-18 secretion and pyroptosis → amplify the septic inflammatory cascade; NLRP3 inhibitors are in preclinical development for sepsis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — TLR4→MyD88→NF-κB is the master signaling axis of innate immune activation in sepsis; NF-κB drives all major pro-inflammatory mediators including TNF-α, IL-1β, IL-6, iNOS, and COX-2.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is the dominant early mediator of septic cardiovascular collapse; despite strong mechanistic rationale, anti-TNF therapies have failed in sepsis RCTs — demonstrating that blocking individual cytokines cannot overcome the redundant inflammatory cascade of systemic sepsis.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — ADM rises dramatically in sepsis proportional to severity; vasodilation (CLR/RAMP2 → cAMP → vasodilation) contributes to distributive shock; MR-proADM predicts 28-day mortality with AUC >0.80 and guides antibiotic de-escalation in the ADAPT-sepsis trial.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4/LPS triggers gram-negative sepsis: LPS-MD-2-CD14 → TLR4 → MyD88 (NF-κB: cytokine storm) + TRIF (IRF3: IFN-β); TLR4 Asp299Gly/Thr399Ile SNPs → altered sepsis risk; OxLDL activates TLR4 → sterile inflammation; TAK-242 (TLR4 antagonist) failed Phase III sepsis trials.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — IL-10 mediates the immunosuppressive phase of sepsis: inflammatory peak → IL-10 surge → macrophage STAT3 → ↓TNF-α, ↓IL-1β, ↓IL-12 → immunoparalysis → secondary nosocomial infections; elevated day-1 IL-10 predicts mortality; PD-1/PD-L1 co-upregulation amplifies immunosuppression.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 released from Weibel-Palade bodies in sepsis → Tie2 destabilization → VE-cadherin cleavage → vascular hyperpermeability → organ edema; plasma Ang-2 >10 ng/mL on day 1 predicts ICU mortality; high Ang-2/Ang-1 ratio defines the severe vascular leak phenotype.
- `connects-to` → **[Troponin Complex](../../03-molecular/troponin-complex/README.md)** — cTnI and cTnT are elevated in 40-85% of septic patients reflecting cardiomyocyte injury from hypoperfusion, inflammatory cytokines, and ROS; sepsis-induced cardiomyopathy causes new LV dysfunction; troponin elevation in sepsis independently predicts ICU mortality.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — In sepsis, contact activation (FXII → kallikrein → bradykinin) contributes to vascular leak; C1-INH levels fall during severe sepsis from consumption; C1-INH concentrate investigated for sepsis capillary leak; C1-INH inhibits complement and contact activation in septic shock.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — APC is consumed in sepsis-DIC → protein C levels < 40% predict 28-day mortality; acquired PC deficiency → purpura fulminans; drotrecogin alfa (rhAPC) reduced mortality in PROWESS (2001) but PROWESS-SHOCK (2011) showed no benefit in septic shock → withdrawn 2011.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Sepsis is the leading cause of disseminated intravascular coagulation: microbial products trigger tissue-factor expression that consumes clotting factors and platelets, causing simultaneous clotting and bleeding—a marker of severe sepsis and poor prognosis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial dysfunction is the heart of septic shock: inflammatory mediators make endothelial cells leaky and prothrombotic, causing capillary leak, hypotension, and microthrombosis that drive multi-organ failure—the endothelium, not infection alone, sets outcome.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are double-edged in sepsis: they fight the infection but their NETs and proteases injure host tissue and endothelium, and as sepsis progresses they become dysfunctional (immunoparalysis), so both hyperinflammation and later immunosuppression worsen outcomes.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide drives septic shock: overwhelming inflammation induces iNOS, flooding vessels with NO that causes profound vasodilation and hypotension refractory to fluids—so the molecule that normally tunes blood flow becomes the engine of distributive shock in sepsis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Acute kidney injury is among the commonest organ failures in sepsis: hypotension, inflammation and microvascular thrombosis cut renal perfusion, so rising creatinine and falling urine output mark severity—and septic AKI strongly predicts mortality and may need dialysis.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Escherichia coli is a leading cause of sepsis: gram-negative bacteremia, often from urinary or abdominal sources, releases LPS endotoxin that triggers the TLR4-driven cytokine cascade—so a common gut commensal becomes a frequent driver of life-threatening septic shock.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help ignite sepsis: sensing bacterial products through TLRs, they release the TNF and IL-6 surge that drives the dysregulated systemic inflammation, yet later become immunoparalyzed—so sepsis is both hyperinflammation and immune exhaustion.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Sepsis is the leading cause of ARDS: systemic inflammation and capillary leak flood the alveoli, so the lungs become stiff and hypoxemic—acute respiratory distress is one of the most common and lethal organ failures of severe sepsis.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Streptococcus pneumoniae is a top cause of sepsis: pneumococcal pneumonia and bacteremia trigger the systemic inflammatory cascade, especially in the asplenic and elderly—why pneumococcal vaccination is a key sepsis-prevention measure.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Staphylococcus aureus is a leading cause of sepsis: from skin, lines, and wounds it invades the bloodstream, and MRSA bacteremia and toxins can rapidly tip into septic shock—so prompt source control and the right antibiotics are decisive.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is both defender and casualty in sepsis: it clears gut-derived endotoxin and mounts the acute-phase response, but septic shock starves it of blood, causing 'shock liver' and cholestasis that worsen coagulopathy and multi-organ failure.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Sepsis consumes platelets: widespread endothelial activation and DIC trap and destroy platelets, so a falling platelet count is an early warning of severe sepsis—and the bleeding-clotting imbalance it signals drives organ damage.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lungs are sepsis's most vulnerable organ: systemic inflammation injures the alveolar-capillary barrier, flooding air sacs to cause ARDS—the acute respiratory failure that often dominates and drives the need for ventilation in severe sepsis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Septic shock involves a vasopressin deficit: the inflammatory vasodilation that drops blood pressure outstrips the body's vasopressin, so vasopressin is added to norepinephrine as a vasopressor to restore perfusion in refractory shock.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Sepsis ends in immune paralysis as T cells die off: after the early cytokine storm, massive lymphocyte apoptosis and T-cell exhaustion leave survivors immunosuppressed and prone to secondary infections—a target for immune-restoring therapies.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Sepsis starves tissues of oxygen despite full lungs: leaky vessels, low blood pressure and mitochondrial failure stop cells using oxygen, so lactate rises—a key warning that sepsis is becoming shock.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Sepsis can stun the heart: inflammatory mediators depress the heart muscle in septic cardiomyopathy, so even a structurally normal heart pumps weakly, deepening the shock and the drop in tissue perfusion.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Sepsis flips into immune paralysis partly via regulatory T cells: as the early storm fades, expanding Tregs help suppress the exhausted immune system, leaving survivors unable to fight the secondary infections that often kill them.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Sepsis clouds the brain early: inflammation, poor perfusion, and toxins cause sepsis-associated encephalopathy, so confusion and delirium are often the first and most sensitive sign that an infection has turned to sepsis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Septic shock turns the blood acidic: starved cells switch to anaerobic metabolism and pour out lactic acid, so rising hydrogen ions (and lactate) mark the metabolic acidosis that signals worsening shock.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Sepsis later cripples its own helper T cells: widespread apoptosis wipes out CD4 T-helper cells, leaving an immunoparalysis that makes survivors prey to secondary infections in the days and weeks after.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Finding sepsis's source needs imaging: CT and X-ray photons hunt the abscess, pneumonia or perforation driving the infection, since draining the source is as vital as the antibiotics.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Sepsis drives the bone marrow hard: it ramps up neutrophil production—the 'left shift' of immature bands in the blood—and, in severe disease, becomes suppressed, deepening the cytopenias of overwhelming infection.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Sepsis can wreck the adrenal glands: fulminant meningococcal sepsis bleeds into them (Waterhouse-Friderichsen) to cause acute adrenal failure, and critical-illness adrenal insufficiency complicates shock.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows sepsis starving cells of energy: mitochondria swell and fail in a 'cytopathic hypoxia' where oxygen is present but unusable, while the endothelial glycocalyx sheds away, opening vessels to leak and clot.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut is called the motor of sepsis: shock starves the intestinal lining until its barrier fails, letting bacteria and their toxins translocate into the blood and stoke the inflammation that perpetuates multi-organ failure.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Sepsis drops the calcium: inflammation and impaired parathyroid and vitamin D handling leave many septic patients hypocalcemic, a disturbance that can weaken the already failing heart and must be watched in the ICU.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin shows shock at the bedside: mottled, cold, slow-to-refill skin signals the collapsing perfusion of septic shock, and in fulminant disease purpura fulminans marks the disseminated clotting beneath.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Survivors are left weak for months: ICU-acquired weakness — a critical-illness myopathy and polyneuropathy driven by sepsis inflammation and immobility — wastes muscle and slows recovery long after the infection clears.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Sepsis thins and shears the red cells: inflammation suppresses their production and repeated blood draws deplete them, while disseminated clotting fragments them into the schistocytes of microangiopathy.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 is a central alarm of sepsis: it pours from activated immune cells to drive fever and the acute-phase response, serving as a severity marker, and blocking it (tocilizumab) tempers the cytokine storm of severe infection.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement runs wild in sepsis: explosive C5a generation recruits and over-activates neutrophils and injures the endothelium, amplifying the inflammation and clotting, which is why C5-blockade is studied to calm the storm.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Maternal sepsis is a leading cause of death in childbirth: postpartum uterine infection and chorioamnionitis can spill into the bloodstream, and the physiologic changes of pregnancy can mask the early warning signs.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Sepsis unleashes the kinin cascade: contact activation generates bradykinin, a potent vasodilator that drops blood pressure and leaks the capillaries, contributing to the shock and edema of severe infection.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Not all sepsis is bacterial: Candida bloodstream infection is a leading cause of fungal sepsis in the ICU, hard to clear, slow to diagnose, and carrying a high mortality in the immunocompromised.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Sepsis turns immune-suppressive after the storm: it depletes dendritic cells and cripples their antigen presentation, a key part of the immunoparalysis that leaves survivors prey to secondary infection.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — The stress axis falters in sepsis: cortisol surges early, but critical-illness-related corticosteroid insufficiency can leave the response inadequate for the vasodilatory shock, which is why low-dose hydrocortisone is given in refractory septic shock.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Meningococcus causes the most fulminant sepsis: Neisseria meningitidis endotoxin can trigger purpura fulminans and Waterhouse-Friderichsen adrenal hemorrhage, killing previously well young people within hours.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is the guard against overwhelming sepsis: it clears encapsulated bacteria from the blood, so asplenic patients face fulminant OPSI from pneumococcus and meningococcus and need vaccination and standby antibiotics.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — It is the leading cause of kidney injury in the critically ill: septic shock starves and inflames the kidneys into acute kidney injury, and survivors of severe episodes often progress to chronic kidney disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The heart stuns under the cytokine storm: septic cardiomyopathy depresses myocardial contractility through inflammatory mediators and nitric oxide, a reversible heart failure that worsens the shock and is usually flagged by a troponin rise.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Sepsis is intensely prothrombotic: endothelial injury, immobility and activated coagulation make deep-vein thrombosis and pulmonary embolism common in septic ICU patients, even beyond the microthrombi of overt DIC.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — It can trigger the most explosive shock: Streptococcus pyogenes causes streptococcal toxic shock syndrome and necrotizing fasciitis, where superantigen-driven cytokine release produces a fulminant sepsis with rapid multiorgan failure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Sepsis can strike the brain's vessels: septic emboli from endocarditis, the profound hypotension of shock and the prothrombotic state can all cause ischemic stroke during severe sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Survival carries a lasting mental toll: survivors of severe sepsis frequently develop depression, anxiety and cognitive impairment — part of the post-intensive-care syndrome that follows critical illness.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Surviving the ICU can leave trauma: the delirium, ventilation and life-threatening course of severe sepsis frequently leave survivors with post-traumatic stress, a core part of post-intensive-care syndrome.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Critical illness damages the nerves: severe sepsis causes critical-illness polyneuropathy and myopathy, leaving lasting weakness and neuropathic pain that prolong recovery for months.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Shock and microthrombi starve the skin: sepsis-driven hypoperfusion, vasopressors and disseminated coagulation cause tissue ischemia and necrosis — even limb gangrene — leaving major wounds that heal poorly.
- `treated-by` → **[Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md)** — First-line empiric IV therapy for MRSA bacteremia and gram-positive sepsis; added to beta-lactam empiric regimens when MRSA risk is elevated; AUC/MIC-guided dosing (IDSA 2021); MIC ≤1 mg/L required for endocarditis; daptomycin alternative for high MIC.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^singer-2016-sepsis3]: Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). *JAMA.* 2016;315(8):801-810. [doi:10.1001/jama.2016.0287](https://doi.org/10.1001/jama.2016.0287) · [PubMed 26903338](https://pubmed.ncbi.nlm.nih.gov/26903338/)
[^vanderpoll-2017-sepsis-immunopathology]: van der Poll T, van de Veerdonk FL, Scicluna BP, Netea MG. The immunopathology of sepsis and potential therapeutic targets. *Nat Rev Immunol.* 2017;17(7):407-420. [doi:10.1038/nri.2017.36](https://doi.org/10.1038/nri.2017.36) · [PubMed 28436424](https://pubmed.ncbi.nlm.nih.gov/28436424/)
[^evans-2021-surviving-sepsis]: Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. *Intensive Care Med.* 2021;47(11):1181-1247. [doi:10.1007/s00134-021-06506-y](https://doi.org/10.1007/s00134-021-06506-y) · [PubMed 34599691](https://pubmed.ncbi.nlm.nih.gov/34599691/)
