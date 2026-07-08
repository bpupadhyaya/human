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
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement pours fuel on the fire: explosive C5a generation recruits and over-activates neutrophils and macrophages, amplifying the cytokine surge — which is why C5 blockade is tested to calm severe COVID and sepsis storms."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells light the first match: by sensing the trigger and over-presenting antigen they drive the T-cell and macrophage activation that snowballs into the self-amplifying cytokine cascade."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "The storm can be a treatment's price: CAR-T therapy for acute lymphoblastic leukemia routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "IL-2 can both cause and characterize the storm: high-dose IL-2 immunotherapy triggers a capillary-leak cytokine-release syndrome, and the IL-2 surge from over-activated T cells is part of the cascade in other storms."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Superantigens unleash the storm directly: Streptococcus pyogenes toxins cross-link MHC and T-cell receptors to activate huge numbers of T cells at once, flooding the blood with cytokines in toxic shock syndrome."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Autoimmune flares can tip into a storm: macrophage activation syndrome — a cytokine storm with runaway ferritin and hemophagocytosis — complicates lupus and other rheumatic diseases, blurring the line between flare and storm."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 drives the storm through STAT3: the flood of IL-6 signals via STAT3 to amplify the inflammatory cascade, which is why the IL-6 blocker tocilizumab and JAK-STAT inhibitors can quell a cytokine storm."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The storm starves the kidneys: hypotension, microthrombi and direct cytokine injury cause acute kidney injury during a cytokine storm, and survivors of severe multiorgan involvement can be left with chronic kidney disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Hyperinflammation clots the veins: the storm's endothelial activation and immunothrombosis sharply raise the risk of deep-vein thrombosis and pulmonary embolism, beyond the microthrombi of overt DIC."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Its cellular therapy can ignite the storm: the CAR-T-cell and bispecific-antibody treatments for multiple myeloma and other blood cancers commonly trigger cytokine release syndrome, the iatrogenic face of a cytokine storm."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The flood of cytokines stuns the heart: TNF-α, IL-6 and nitric oxide depress myocardial contractility during a cytokine storm, causing an acute, often reversible cardiac dysfunction that worsens the shock."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hyperinflammation can strike the brain: endothelial injury, immunothrombosis and the profound hemodynamic swings of a cytokine storm can cause ischemic stroke amid its multiorgan assault."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Its treatment is a deliberate trigger: CAR-T cell therapy for DLBCL unleashes a controlled cytokine release syndrome, the iconic iatrogenic cytokine storm managed with the IL-6 blocker tocilizumab."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Immunotherapy for leukemia ignites it: CAR-T cells and bispecific antibodies against acute lymphoblastic leukemia provoke cytokine release syndrome, a frequent and sometimes severe storm during treatment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Surviving the storm leaves a mental toll: the critical illness, ICU stay and neuroinflammation of a cytokine storm contribute to the depression and cognitive impairment of post-intensive-care syndrome."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is the immune system turned against itself: a cytokine storm is uncontrolled hyperactivation of immune cells and their mediators, as in HLH, macrophage activation syndrome and CAR-T cytokine release."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It floods the lungs first: the capillary leak and inflammation of a cytokine storm cause acute respiratory distress syndrome, the most common and lethal organ failure it produces."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can inflame the brain: cytokine storms, especially CAR-T cell therapy, cause immune-effector-cell-associated neurotoxicity (ICANS) with encephalopathy, seizures and cerebral oedema."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It collapses the circulation: massive cytokine release causes vasodilatory shock with capillary leak and myocardial depression, the cardiovascular failure that makes cytokine release syndrome life-threatening."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "In HLH the macrophages run wild: macrophage activation syndrome causes hepatosplenomegaly and haemophagocytosis in the marrow, spleen and lymph nodes, a defining feature of this cytokine storm."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It floods and inflames the abdomen: hepatic dysfunction with soaring ferritin and transaminases is a hallmark, and capillary leak causes ascites and gut oedema."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It shuts down the kidney: the systemic inflammation and capillary leak of a cytokine storm cause hypotension and acute kidney injury, often needing dialysis in severe cases."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It flushes and leaks at the skin: cytokine release causes widespread rash, flushing and capillary leak with oedema, prominent in CAR-T cell and infection-triggered storms."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches deep in the muscles: high circulating IL-6 and TNF cause severe myalgia, and extreme cases bring rhabdomyolysis from inflammatory muscle injury."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "It IS the signature CAR-T toxicity: cytokine release syndrome is the defining adverse effect of CAR-T therapy, the same IL-6-driven cascade, reversed by the IL-6-receptor blocker tocilizumab."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "The pandemic's deadly hyperinflammation: severe COVID-19 drives a cytokine storm with high IL-6 and ferritin, the target of dexamethasone and tocilizumab that lower its mortality."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: connects-to
    note: "Haemorrhagic fever's lethal surge: Ebola and other viral haemorrhagic fevers kill partly through a massive cytokine storm that drives vascular leak, shock and coagulopathy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Cytokine-blocking biologics quench it: tocilizumab against IL-6, anakinra against IL-1, emapalumab against IFN-γ and JAK inhibitors directly interrupt the cytokine cascade of CAR-T CRS, COVID and HLH."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Etoposide tames the macrophage storm: in HLH and macrophage activation syndrome the chemotherapy agent etoposide depletes the hyperactivated macrophages and T cells, a cornerstone of the HLH-94 protocol for that lethal cytokine storm."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cytokines stun the heart: high circulating IL-6 and TNF directly depress myocardial contractility, so cytokine storm — in sepsis, CRS or COVID — causes a reversible cardiomyopathy that deepens the shock."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "ARDS at the gas-exchange surface: the cytokine flood makes alveolar capillaries leak and flood the air sacs, causing the acute respiratory distress syndrome that is the commonest fatal endpoint."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Cytokine acute kidney injury: systemic inflammation and microvascular injury impair the glomerulus, a major contributor to the multi-organ failure of cytokine storm."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatitis of the storm: in HLH and macrophage-activation syndrome the cytokine surge inflames the hepatic lobule, causing hepatitis, hepatosplenomegaly and extreme hyperferritinaemia."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Endothelial leak: the cytokine storm activates and disrupts the endothelium of the arterial wall and capillaries, causing the vascular leak, hypotension and oedema of severe systemic inflammation."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "Inflammation injures the infant lung: severe RSV bronchiolitis drives an exaggerated cytokine response that damages airways and alveoli, a paediatric cytokine storm beyond direct viral injury."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Treatment-triggered storms: Burkitt and other aggressive lymphomas can unleash cytokine release syndrome with CD19 immunotherapy and severe tumour lysis, acute systemic-inflammation emergencies."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV-driven HLH: Epstein-Barr virus is the classic trigger of secondary haemophagocytic lymphohistiocytosis, a prototypical cytokine storm of uncontrolled T-cell and macrophage activation."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Superantigen shock: staphylococcal TSST-1 and related superantigens cross-link T cells en masse, unleashing the massive cytokine release of toxic shock syndrome."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon-driven hyperinflammation: dysregulated type I interferon fuels the systemic inflammation of viral cytokine storms and interferonopathies, a double-edged antiviral response."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement amplification: C5a signalling through C5aR1 activates neutrophils and macrophages in the cytokine storm, a complement-driven feed-forward loop targeted by anti-C5 therapy."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 contribution: IL-17 from activated T cells adds neutrophil-recruiting inflammation to the cytokine storm, broadening tissue injury beyond the dominant IL-6/TNF axis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Shock and hypoxia: the circulatory collapse and tissue hypoxia of severe cytokine storm stabilise HIF-1α, which further amplifies inflammatory gene expression in a vicious cycle."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte mobilisation: CCL2 floods the circulation in cytokine storm, recruiting and activating monocytes and macrophages that pour out IL-6 and TNF in the self-amplifying inflammatory cascade."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Ignition by DAMPs and PAMPs: TLR4 sensing of bacterial LPS and host damage signals is a key trigger that ignites the NF-κB-driven cytokine release initiating the storm."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Alarmin feed-forward: S100A8/A9 released by activated myeloid cells acts on TLR4 to further amplify cytokine production, a feed-forward alarmin loop that sustains the cytokine storm."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Consumptive coagulopathy: the cytokine storm of HLH/MAS consumes fibrinogen into disseminated coagulation, so falling fibrinogen alongside soaring ferritin is a diagnostic hallmark of the hyperinflammatory state."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "HMGB1 sustainer: HMGB1 released by dying and activated cells signals through RAGE as a late mediator that perpetuates the cytokine storm, sustaining inflammation beyond the initial trigger."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial-DNA amplification: mitochondrial DNA and other DAMPs released during the cytokine storm activate cGAS-STING, adding a type-I-interferon arm to the runaway innate-immune activation."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hyperferritinaemia: the cytokine storm of macrophage activation syndrome and HLH drives extreme hyperferritinaemia through IL-6-stimulated hepcidin and macrophage ferritin release, a striking biomarker that helps diagnose and grade the hyperinflammatory state."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Corticosteroid suppression: high-dose glucocorticoids acting through the glucocorticoid receptor are a first-line therapy for cytokine storm, broadly suppressing the runaway cytokine production, used alongside targeted blockers like anti-IL-6 and JAK inhibitors."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Consumptive coagulopathy: the cytokine storm activates coagulation through tissue factor and thrombin generation, producing the disseminated intravascular coagulation and microthrombi that drive the multi-organ failure of severe hyperinflammation."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IFN-γ amplifier: IL-12 drives Th1 and NK cells to pour out IFN-γ (already mapped), the cytokine that dominates the haemophagocytic lymphohistiocytosis and macrophage-activation forms of cytokine storm."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Distributive shock: cytokine-induced iNOS floods the circulation with nitric oxide, causing the vasodilation and refractory hypotension that produce the distributive shock of severe cytokine storm."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement amplification: the cytokine storm activates complement at C3, feeding the C5-C5aR1 axis already mapped to amplify neutrophil recruitment, endothelial injury and the thromboinflammation of hyperinflammatory states."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Initiating innate circuit: TLR-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped), triggered by PAMPs and DAMPs, is a principal initiating circuit of the runaway cytokine production in cytokine storm."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "Viral-RNA sensing: RIG-I-MAVS sensing of viral RNA drives the type-I-interferon response (already mapped) that, when unrestrained, contributes to the cytokine storm of severe viral infection."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Macrophage hyperactivation: IFN-γ signalling through STAT1 (IFN-γ already mapped) hyperactivates macrophages, the central effector mechanism of the macrophage-activation-syndrome form of cytokine storm."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-regulated immunometabolic reprogramming fuels the hyperactivated immune cells driving the cytokine storm."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies macrophage activation, contributing to the macrophage-activation-syndrome forms of cytokine storm."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling sustains the survival and effector responses of the hyperactivated immune cells in cytokine storm."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling downstream of cytokine and pattern-recognition receptors amplifies the feed-forward cytokine production of the cytokine storm."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA) signalling (AKT already mapped) drives the immunometabolic activation of the hyperinflammatory myeloid and lymphoid cells in cytokine storm."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling participates in the counter-regulatory resolution phase that must restrain the hyperinflammation of cytokine storm."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the immune-cell survival and metabolic reprogramming that shape the hyperinflammatory response of cytokine storm."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB- and inflammasome-driven cytokine production that sustains cytokine storm."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BTK signaling in macrophages amplifies the inflammatory cytokine release of cytokine storm, the rationale for BTK inhibition in severe cases."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling regulates the immunometabolic reprogramming of the hyperactivated immune cells driving the cytokine storm."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of Fc and cytokine receptors amplifies the myeloid and lymphocyte activation of the cytokine storm."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates inflammasome activation and the survival of the hyperinflammatory immune cells in the cytokine storm."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment amplifies the immune-cell infiltration and hyperinflammation of a cytokine storm."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated epigenetic regulation of immune-cell activation modulates the hyperinflammatory response of a cytokine storm."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven vascular permeability contributes to the endothelial leak and hypotension of a cytokine storm."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and immune-cell recruitment of the cytokine storm."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling amplifies the innate immune activation of the cytokine storm."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling provides immunoregulatory counter-signaling that modulates the hyperinflammation of the cytokine storm."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hyperinflammatory immune gene programs of cytokine storm."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell hyperactivation of cytokine storm (a target of calcineurin inhibitors in HLH/macrophage-activation syndrome)."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage activation and hyperinflammatory responses of cytokine storm."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac injury: the hyperinflammation of cytokine storm, including CAR-T cytokine-release syndrome and macrophage-activation syndrome, injures the myocardium, and troponin elevation marks the cardiac dysfunction that contributes to its mortality."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Cytopenias: haemophagocytic lymphohistiocytosis at the severe end of cytokine storm consumes blood cells, dropping haemoglobin along with platelets and neutrophils, one of the diagnostic features of the syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen-driven hyperactivation: MHC class II presentation of pathogen or superantigen drives the T-cell hyperactivation that ignites many cytokine storms, and antigen presentation is central to the CAR-T-associated cytokine-release syndrome."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial leak: activated endothelium in cytokine storm releases angiopoietin-2, destabilising the vasculature and, with the cytokines already mapped, producing the capillary leak, oedema and shock that cause organ failure."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Thromboinflammation: endothelial activation releases von Willebrand factor multimers that promote platelet microthrombi, part of the thromboinflammation and disseminated intravascular coagulation (thrombin already mapped) of severe cytokine storm."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Anticoagulant consumption: the coagulopathy of cytokine storm consumes the natural anticoagulant protein C, tipping the balance toward the microthrombosis and disseminated intravascular coagulation that damage organs."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Fever and vasodilation: prostaglandin E2 driven by the IL-1 and IL-6 (already mapped) of the storm produces the high fever, and vasodilatory prostaglandins contribute to the hypotension of the hyperinflammatory state."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-mediated shock: bradykinin and the contact system amplify the vascular permeability and hypotension of cytokine storm, part of the distributive shock that, with the vasodilation (nitric oxide already mapped), causes organ hypoperfusion."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative tissue damage: the hyperinflammation generates a burst of reactive oxygen species, to which xanthine oxidase contributes, adding oxidative injury to the endothelial and organ damage of cytokine storm."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Counter-regulatory arm: IL-4, with IL-10 (already mapped), is part of the compensatory anti-inflammatory response that tries to restrain the runaway pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of cytokine storm."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 balance: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the resolution or persistence of cytokine storm."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine severity marker: resistin, a pro-inflammatory adipokine released by the activated leukocytes, rises markedly in sepsis and cytokine storm (IL-6 already mapped) and tracks with the severity of the hyperinflammation."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Inflammatory adipokine: leptin, with resistin (already mapped), rises in the acute inflammation (IL-6 already mapped) of the cytokine storm, part of the adipokine dimension of the hyperinflammatory response."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine axis: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis whose balance shapes the metabolic-inflammatory response of the cytokine storm."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immunoparalysis exhaustion: PD-1 is upregulated on the exhausted T cells of the immunoparalysis phase that follows the cytokine storm, contributing to the secondary infections of the hyperinflammatory syndromes."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "HLH NK defect: the impaired NK/CTL cytotoxicity (perforin already mapped) of the familial and secondary HLH fails to kill the activated antigen-presenting cells, perpetuating the cytokine storm."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial leak: the endothelial activation and the glycocalyx damage (angiopoietin and VWF already mapped) drive the vascular leak, the shock and the coagulopathy of the cytokine storm."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "COVID driver: the severe COVID-19 is a major cause of the cytokine storm (the IL-6 already mapped hyperinflammation), the tocilizumab/dexamethasone target."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) arm, one contributor to the broad cytokine milieu of the cytokine storm."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mixed cytokine profile of the cytokine storm."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell source: the mast cells (a source of IL-6 and TNF already mapped) contribute to the hyperinflammation, as in the mast-cell-activation forms of the cytokine storm."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), arms the mast cells (already mapped) of the mast-cell-activation forms of the cytokine storm."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response that can accompany or drive some forms of the cytokine storm."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B-cell arm: the B cells contribute to the immune dysregulation of some cytokine storms (e.g. the B-cell-driven forms of MAS and the CAR-T-cell target-related CRS)."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption and dysregulation amplify the complement storm of the cytokine storm."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems at the interface driving the vascular leak and coagulopathy of the cytokine storm."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Hyperferritinaemic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the extreme hyperferritinaemia that is a hallmark of the MAS/HLH cytokine storm."
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
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement pours fuel on the fire: explosive C5a generation recruits and over-activates neutrophils and macrophages, amplifying the cytokine surge — which is why C5 blockade is tested to calm severe COVID and sepsis storms.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells light the first match: by sensing the trigger and over-presenting antigen they drive the T-cell and macrophage activation that snowballs into the self-amplifying cytokine cascade.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — The storm can be a treatment's price: CAR-T therapy for acute lymphoblastic leukemia routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 can both cause and characterize the storm: high-dose IL-2 immunotherapy triggers a capillary-leak cytokine-release syndrome, and the IL-2 surge from over-activated T cells is part of the cascade in other storms.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Superantigens unleash the storm directly: Streptococcus pyogenes toxins cross-link MHC and T-cell receptors to activate huge numbers of T cells at once, flooding the blood with cytokines in toxic shock syndrome.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Autoimmune flares can tip into a storm: macrophage activation syndrome — a cytokine storm with runaway ferritin and hemophagocytosis — complicates lupus and other rheumatic diseases, blurring the line between flare and storm.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 drives the storm through STAT3: the flood of IL-6 signals via STAT3 to amplify the inflammatory cascade, which is why the IL-6 blocker tocilizumab and JAK-STAT inhibitors can quell a cytokine storm.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The storm starves the kidneys: hypotension, microthrombi and direct cytokine injury cause acute kidney injury during a cytokine storm, and survivors of severe multiorgan involvement can be left with chronic kidney disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Hyperinflammation clots the veins: the storm's endothelial activation and immunothrombosis sharply raise the risk of deep-vein thrombosis and pulmonary embolism, beyond the microthrombi of overt DIC.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Its cellular therapy can ignite the storm: the CAR-T-cell and bispecific-antibody treatments for multiple myeloma and other blood cancers commonly trigger cytokine release syndrome, the iatrogenic face of a cytokine storm.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The flood of cytokines stuns the heart: TNF-α, IL-6 and nitric oxide depress myocardial contractility during a cytokine storm, causing an acute, often reversible cardiac dysfunction that worsens the shock.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hyperinflammation can strike the brain: endothelial injury, immunothrombosis and the profound hemodynamic swings of a cytokine storm can cause ischemic stroke amid its multiorgan assault.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Its treatment is a deliberate trigger: CAR-T cell therapy for DLBCL unleashes a controlled cytokine release syndrome, the iconic iatrogenic cytokine storm managed with the IL-6 blocker tocilizumab.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Immunotherapy for leukemia ignites it: CAR-T cells and bispecific antibodies against acute lymphoblastic leukemia provoke cytokine release syndrome, a frequent and sometimes severe storm during treatment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Surviving the storm leaves a mental toll: the critical illness, ICU stay and neuroinflammation of a cytokine storm contribute to the depression and cognitive impairment of post-intensive-care syndrome.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is the immune system turned against itself: a cytokine storm is uncontrolled hyperactivation of immune cells and their mediators, as in HLH, macrophage activation syndrome and CAR-T cytokine release.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It floods the lungs first: the capillary leak and inflammation of a cytokine storm cause acute respiratory distress syndrome, the most common and lethal organ failure it produces.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can inflame the brain: cytokine storms, especially CAR-T cell therapy, cause immune-effector-cell-associated neurotoxicity (ICANS) with encephalopathy, seizures and cerebral oedema.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It collapses the circulation: massive cytokine release causes vasodilatory shock with capillary leak and myocardial depression, the cardiovascular failure that makes cytokine release syndrome life-threatening.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — In HLH the macrophages run wild: macrophage activation syndrome causes hepatosplenomegaly and haemophagocytosis in the marrow, spleen and lymph nodes, a defining feature of this cytokine storm.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It floods and inflames the abdomen: hepatic dysfunction with soaring ferritin and transaminases is a hallmark, and capillary leak causes ascites and gut oedema.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It shuts down the kidney: the systemic inflammation and capillary leak of a cytokine storm cause hypotension and acute kidney injury, often needing dialysis in severe cases.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It flushes and leaks at the skin: cytokine release causes widespread rash, flushing and capillary leak with oedema, prominent in CAR-T cell and infection-triggered storms.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches deep in the muscles: high circulating IL-6 and TNF cause severe myalgia, and extreme cases bring rhabdomyolysis from inflammatory muscle injury.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — It IS the signature CAR-T toxicity: cytokine release syndrome is the defining adverse effect of CAR-T therapy, the same IL-6-driven cascade, reversed by the IL-6-receptor blocker tocilizumab.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — The pandemic's deadly hyperinflammation: severe COVID-19 drives a cytokine storm with high IL-6 and ferritin, the target of dexamethasone and tocilizumab that lower its mortality.
- `connects-to` → **[Ebola Virus](../../../02-pathogen/01-viruses/ebola-virus/README.md)** — Haemorrhagic fever's lethal surge: Ebola and other viral haemorrhagic fevers kill partly through a massive cytokine storm that drives vascular leak, shock and coagulopathy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Cytokine-blocking biologics quench it: tocilizumab against IL-6, anakinra against IL-1, emapalumab against IFN-γ and JAK inhibitors directly interrupt the cytokine cascade of CAR-T CRS, COVID and HLH.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Etoposide tames the macrophage storm: in HLH and macrophage activation syndrome the chemotherapy agent etoposide depletes the hyperactivated macrophages and T cells, a cornerstone of the HLH-94 protocol for that lethal cytokine storm.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cytokines stun the heart: high circulating IL-6 and TNF directly depress myocardial contractility, so cytokine storm — in sepsis, CRS or COVID — causes a reversible cardiomyopathy that deepens the shock.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — ARDS at the gas-exchange surface: the cytokine flood makes alveolar capillaries leak and flood the air sacs, causing the acute respiratory distress syndrome that is the commonest fatal endpoint.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Cytokine acute kidney injury: systemic inflammation and microvascular injury impair the glomerulus, a major contributor to the multi-organ failure of cytokine storm.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatitis of the storm: in HLH and macrophage-activation syndrome the cytokine surge inflames the hepatic lobule, causing hepatitis, hepatosplenomegaly and extreme hyperferritinaemia.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Endothelial leak: the cytokine storm activates and disrupts the endothelium of the arterial wall and capillaries, causing the vascular leak, hypotension and oedema of severe systemic inflammation.
- `connects-to` → **[RSV](../rsv/README.md)** — Inflammation injures the infant lung: severe RSV bronchiolitis drives an exaggerated cytokine response that damages airways and alveoli, a paediatric cytokine storm beyond direct viral injury.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Treatment-triggered storms: Burkitt and other aggressive lymphomas can unleash cytokine release syndrome with CD19 immunotherapy and severe tumour lysis, acute systemic-inflammation emergencies.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV-driven HLH: Epstein-Barr virus is the classic trigger of secondary haemophagocytic lymphohistiocytosis, a prototypical cytokine storm of uncontrolled T-cell and macrophage activation.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Superantigen shock: staphylococcal TSST-1 and related superantigens cross-link T cells en masse, unleashing the massive cytokine release of toxic shock syndrome.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon-driven hyperinflammation: dysregulated type I interferon fuels the systemic inflammation of viral cytokine storms and interferonopathies, a double-edged antiviral response.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement amplification: C5a signalling through C5aR1 activates neutrophils and macrophages in the cytokine storm, a complement-driven feed-forward loop targeted by anti-C5 therapy.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 contribution: IL-17 from activated T cells adds neutrophil-recruiting inflammation to the cytokine storm, broadening tissue injury beyond the dominant IL-6/TNF axis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Shock and hypoxia: the circulatory collapse and tissue hypoxia of severe cytokine storm stabilise HIF-1α, which further amplifies inflammatory gene expression in a vicious cycle.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte mobilisation: CCL2 floods the circulation in cytokine storm, recruiting and activating monocytes and macrophages that pour out IL-6 and TNF in the self-amplifying inflammatory cascade.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Ignition by DAMPs and PAMPs: TLR4 sensing of bacterial LPS and host damage signals is a key trigger that ignites the NF-κB-driven cytokine release initiating the storm.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Alarmin feed-forward: S100A8/A9 released by activated myeloid cells acts on TLR4 to further amplify cytokine production, a feed-forward alarmin loop that sustains the cytokine storm.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — The cytokine storm of HLH/MAS consumes fibrinogen into disseminated coagulation, so falling fibrinogen alongside soaring ferritin is a diagnostic hallmark of the hyperinflammatory state and a marker of severity.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — HMGB1 released by dying and activated cells signals through RAGE as a late mediator that perpetuates the cytokine storm, sustaining the inflammatory cascade well beyond the initial infectious or therapeutic trigger.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial DNA and other DAMPs released during the cytokine storm activate cGAS-STING, adding a type-I-interferon arm to the runaway innate-immune activation that defines the hyperinflammatory state.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — The cytokine storm of macrophage activation syndrome and HLH drives extreme hyperferritinemia through IL-6-stimulated hepcidin and macrophage ferritin release, a striking biomarker that helps diagnose and grade the hyperinflammatory state.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — High-dose glucocorticoids acting through the glucocorticoid receptor are a first-line therapy for cytokine storm, broadly suppressing the runaway cytokine production, used alongside targeted blockers like anti-IL-6 and JAK inhibitors.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — The cytokine storm activates coagulation through tissue factor and thrombin generation, producing the disseminated intravascular coagulation and microthrombi that drive the multi-organ failure of severe hyperinflammation.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 drives Th1 and NK cells to pour out IFN-γ (already mapped), the cytokine that dominates the hemophagocytic lymphohistiocytosis and macrophage-activation forms of cytokine storm.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Cytokine-induced iNOS floods the circulation with nitric oxide, causing the vasodilation and refractory hypotension that produce the distributive shock of severe cytokine storm.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The cytokine storm activates complement at C3, feeding the C5-C5aR1 axis already mapped to amplify neutrophil recruitment, endothelial injury and the thromboinflammation of hyperinflammatory states.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped), triggered by PAMPs and DAMPs, is a principal initiating circuit of the runaway cytokine production in cytokine storm.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — RIG-I-MAVS sensing of viral RNA drives the type-I-interferon response (already mapped) that, when unrestrained, contributes to the cytokine storm of severe viral infection.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ signaling through STAT1 (IFN-γ already mapped) hyperactivates macrophages, the central effector mechanism of the macrophage-activation-syndrome form of cytokine storm.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated immunometabolic reprogramming fuels the hyperactivated immune cells driving the cytokine storm.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies macrophage activation, contributing to the macrophage-activation-syndrome forms of cytokine storm.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling sustains the survival and effector responses of the hyperactivated immune cells in cytokine storm.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of cytokine and pattern-recognition receptors amplifies the feed-forward cytokine production of the cytokine storm.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA) signaling (AKT already mapped) drives the immunometabolic activation of the hyperinflammatory myeloid and lymphoid cells in cytokine storm.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling participates in the counter-regulatory resolution phase that must restrain the hyperinflammation of cytokine storm.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the immune-cell survival and metabolic reprogramming that shape the hyperinflammatory response of cytokine storm.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB- and inflammasome-driven cytokine production that sustains cytokine storm.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK signaling in macrophages amplifies the inflammatory cytokine release of cytokine storm, the rationale for BTK inhibition in severe cases.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling regulates the immunometabolic reprogramming of the hyperactivated immune cells driving the cytokine storm.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of Fc and cytokine receptors amplifies the myeloid and lymphocyte activation of the cytokine storm.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates inflammasome activation and the survival of the hyperinflammatory immune cells in the cytokine storm.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment amplifies the immune-cell infiltration and hyperinflammation of a cytokine storm.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated epigenetic regulation of immune-cell activation modulates the hyperinflammatory response of a cytokine storm.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven vascular permeability contributes to the endothelial leak and hypotension of a cytokine storm.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and immune-cell recruitment of the cytokine storm.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling amplifies the innate immune activation of the cytokine storm.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling provides immunoregulatory counter-signaling that modulates the hyperinflammation of the cytokine storm.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hyperinflammatory immune gene programs of cytokine storm.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell hyperactivation of cytokine storm (a target of calcineurin inhibitors in HLH/macrophage-activation syndrome).
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage activation and hyperinflammatory responses of cytokine storm.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac injury: the hyperinflammation of cytokine storm, including CAR-T cytokine-release syndrome and macrophage-activation syndrome, injures the myocardium, and troponin elevation marks the cardiac dysfunction that contributes to its mortality.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Cytopenias: haemophagocytic lymphohistiocytosis at the severe end of cytokine storm consumes blood cells, dropping haemoglobin along with platelets and neutrophils, one of the diagnostic features of the syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen-driven hyperactivation: MHC class II presentation of pathogen or superantigen drives the T-cell hyperactivation that ignites many cytokine storms, and antigen presentation is central to the CAR-T-associated cytokine-release syndrome.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial leak: activated endothelium in cytokine storm releases angiopoietin-2, destabilising the vasculature and, with the cytokines already mapped, producing the capillary leak, oedema and shock that cause organ failure.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Thromboinflammation: endothelial activation releases von Willebrand factor multimers that promote platelet microthrombi, part of the thromboinflammation and disseminated intravascular coagulation (thrombin already mapped) of severe cytokine storm.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Anticoagulant consumption: the coagulopathy of cytokine storm consumes the natural anticoagulant protein C, tipping the balance toward the microthrombosis and disseminated intravascular coagulation that damage organs.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Fever and vasodilation: prostaglandin E2 driven by the IL-1 and IL-6 (already mapped) of the storm produces the high fever, and vasodilatory prostaglandins contribute to the hypotension of the hyperinflammatory state.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-mediated shock: bradykinin and the contact system amplify the vascular permeability and hypotension of cytokine storm, part of the distributive shock that, with the vasodilation (nitric oxide already mapped), causes organ hypoperfusion.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative tissue damage: the hyperinflammation generates a burst of reactive oxygen species, to which xanthine oxidase contributes, adding oxidative injury to the endothelial and organ damage of cytokine storm.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Counter-regulatory arm: IL-4, with IL-10 (already mapped), is part of the compensatory anti-inflammatory response that tries to restrain the runaway pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of cytokine storm.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 balance: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the pro-inflammatory signals shapes the resolution or persistence of cytokine storm.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine severity marker: resistin, a pro-inflammatory adipokine released by the activated leukocytes, rises markedly in sepsis and cytokine storm (IL-6 already mapped) and tracks with the severity of the hyperinflammation.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Inflammatory adipokine: leptin, with resistin (already mapped), rises in the acute inflammation (IL-6 already mapped) of the cytokine storm, part of the adipokine dimension of the hyperinflammatory response.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine axis: adiponectin, with leptin and resistin (already mapped), completes the adipokine axis whose balance shapes the metabolic-inflammatory response of the cytokine storm.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immunoparalysis exhaustion: PD-1 is upregulated on the exhausted T cells of the immunoparalysis phase that follows the cytokine storm, contributing to the secondary infections of the hyperinflammatory syndromes.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — HLH NK defect: the impaired NK/CTL cytotoxicity (perforin already mapped) of the familial and secondary HLH fails to kill the activated antigen-presenting cells, perpetuating the cytokine storm.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial leak: the endothelial activation and the glycocalyx damage (angiopoietin and VWF already mapped) drive the vascular leak, the shock and the coagulopathy of the cytokine storm.
- `connects-to` → **[COVID-19](../covid-19-disease/README.md)** — COVID driver: the severe COVID-19 is a major cause of the cytokine storm (the IL-6 already mapped hyperinflammation), the tocilizumab/dexamethasone target.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 arm: IL-23 sustains the Th17 (IL-17 already mapped) arm, one contributor to the broad cytokine milieu of the cytokine storm.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mixed cytokine profile of the cytokine storm.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell source: the mast cells (a source of IL-6 and TNF already mapped) contribute to the hyperinflammation, as in the mast-cell-activation forms of the cytokine storm.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), arms the mast cells (already mapped) of the mast-cell-activation forms of the cytokine storm.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response that can accompany or drive some forms of the cytokine storm.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — B-cell arm: the B cells contribute to the immune dysregulation of some cytokine storms (e.g. the B-cell-driven forms of MAS and the CAR-T-cell target-related CRS).
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose consumption and dysregulation amplify the complement storm of the cytokine storm.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems at the interface driving the vascular leak and coagulopathy of the cytokine storm.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Hyperferritinaemic iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the extreme hyperferritinaemia that is a hallmark of the MAS/HLH cytokine storm.

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
