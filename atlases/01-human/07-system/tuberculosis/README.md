---
schema: human-scale-entry/v1
id: tuberculosis
name: Tuberculosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Tuberculosis (MTB; Mycobacterium tuberculosis) causes ~10M cases and 1.3M deaths annually; inhaled droplet nuclei → macrophage phagosome arrest → granuloma; HRZE 6-month regimen for drug-sensitive TB; BPaL (bedaquiline-pretomanid-linezolid) for MDR-TB."
aliases: ["TB", "pulmonary tuberculosis", "Mycobacterium tuberculosis", "MTB", "MTBC", "LTBI", "latent TB", "MDR-TB", "XDR-TB", "Pott's disease", "phthisis", "consumption"]
sources:
  - id: who-tb-report-2023
    type: clinical-guideline
    cite: "World Health Organization. Global Tuberculosis Report 2023. Geneva: WHO; 2023."
    url: "https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2023"
    accessed: "2026-06-08"
  - id: nahid-2016-tb-treatment
    type: peer-reviewed
    cite: "Nahid P, Dorman SE, Alipanah N, et al. Official ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. Clin Infect Dis. 2016;63(7):e147-e195."
    doi: "10.1093/cid/ciw376"
    pmid: "27516382"
    url: "https://doi.org/10.1093/cid/ciw376"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IFN-γ axis is essential for granuloma formation and MTB containment; IL12B or IL12RB1 loss of function → MSMD (recurrent BCG/NTM disease); ustekinumab (anti-p40) and other IL-12 pathway inhibitors → latent TB reactivation; IGRA screening before therapy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is essential for granuloma formation and maintenance in TB; anti-TNF agents → 4-25× increased TB reactivation risk; antibody-based anti-TNF (infliximab/adalimumab) carries higher TB risk than etanercept; IGRA/TST mandatory before anti-TNF initiation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ activates macrophages to restrict MTB growth (phagosome acidification, ROS burst, cathelicidin production); IFN-γ from MTB-sensitized T cells is the basis of IGRA diagnostic tests; IFNGR1/IFNGR2 mutations → MSMD phenotype with disseminated MTB/BCG disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "TB is a classic cause of ACD: sustained MTB infection → IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; TB treatment → inflammation subsides → ACD recovers; ACD severity correlates with TB disease activity (smear positivity, extent of lung disease)."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MTB evades innate immunity by arresting phagosome maturation, secreting ESAT-6 to escape to cytosol, inhibiting MHC-II antigen presentation, and inducing regulatory T cells; CD4+ Th1 cells orchestrate granuloma; AIDS → CD4+ loss → TB reactivation is the paradigmatic example."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV-AIDS is the most important co-factor for TB reactivation globally: HIV depletes CD4+ Th1 cells and destroys granuloma integrity → latent TB reactivates; TB is the leading cause of AIDS-related death; concurrent ART + HRZE treatment mandatory; IRIS risk with early ART."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ → STAT1 → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling → impaired macrophage activation; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM susceptibility — demonstrating STAT1 is non-redundant."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is tuberculosis's primary battleground: inhaled M. tuberculosis seeds the alveoli, where Th1 granulomas wall it off; reactivation in oxygen-rich upper lobes makes caseating cavities that shed bacilli in cough — the infectious form — and a Ghon focus marks healed disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The macrophage is host and battleground in tuberculosis: M. tuberculosis is phagocytosed but blocks phagosome maturation to survive inside, while IFN-γ-activated macrophages fight back with NO; the granuloma is a ball of infected macrophages that contains but rarely clears it."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis is caused by Mycobacterium tuberculosis: its waxy mycolic-acid wall (acid-fast) resists killing and drives the slow granulomatous response; it grows slowly (weeks to culture) and demands months of multidrug RIPE therapy, while MDR/XDR-TB resistance grows."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes roughly triples the risk of active tuberculosis: hyperglycemia impairs macrophage and T-cell function, so diabetics reactivate latent TB more readily and fare worse—bidirectional, as TB also worsens glycemic control."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Control of tuberculosis depends on Th1 helper T cells: IFN-γ from CD4+ Th1 cells activates infected macrophages to kill the bacillus and maintain the granuloma, which is why HIV-driven CD4 loss so dramatically raises TB reactivation and dissemination."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Mycobacterium tuberculosis subverts dendritic cells to delay immunity: by slowing DC migration and antigen presentation to T cells in lymph nodes, the bacillus buys weeks before an adaptive Th1 response forms—part of why TB establishes a foothold before containment."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Tuberculosis and COPD interact in both directions: past TB scarring causes airflow obstruction resembling COPD, while COPD and its inhaled steroids raise TB risk—so in high-burden regions chronic cough and obstruction warrant testing for active or prior TB."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D underpins macrophage defense against tuberculosis: vitamin-D signaling induces the antimicrobial peptide cathelicidin that helps macrophages kill M. tuberculosis, so deficiency raises TB risk—the old link behind 'sunlight and cod-liver oil' sanatorium cures."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Tuberculosis and lung cancer overlap clinically: both can present as a cavitary or spiculated lung mass, old TB scars raise later lung-cancer risk, and chronic granulomatous inflammation may promote carcinogenesis—so a 'mass' in an endemic area needs both worked up."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is harmful in tuberculosis, unlike in viral infection: a type I IFN signature marks active, severe TB because it suppresses the protective IFN-gamma/macrophage response—so the same cytokine family that fights viruses helps Mtb evade killing."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are a double-edged sword in tuberculosis: they swarm to infected lung but, when overwhelmed, drive the tissue necrosis and cavitation that spreads Mtb—so a neutrophil-dominated response marks severe, transmissible disease rather than control."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Tuberculosis is a classic cause of adrenal insufficiency: hematogenous spread can destroy both adrenal glands, producing Addison's disease—historically the leading cause—so adrenal calcification or new Addison's should prompt a search for TB."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic CD8 T cells help contain tuberculosis: alongside CD4 help, they kill infected macrophages that fail to clear the bacillus and secrete IFN-γ, so they are central to granuloma immunity and a key target for next-generation TB vaccines."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Tuberculosis often localizes to the lymphatic system: cervical node TB (scrofula) is the classic extrapulmonary form, and lymphatic and bloodstream spread of the bacillus seeds miliary disease throughout the body when immunity fails."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Tuberculosis can invade the brain: hematogenous seeding causes TB meningitis and tuberculomas, among the deadliest forms—so suspected CNS TB demands urgent treatment with steroids, since inflammation, not just infection, drives the damage."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Tuberculosis frequently spreads to the kidney: genitourinary TB is a leading extrapulmonary form, seeding the kidney to cause sterile pyuria, scarring and ureteral strictures—so persistent urinary symptoms with negative routine cultures should raise suspicion."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Macrophages kill tuberculosis partly with nitric oxide: activated by IFN-gamma, they generate reactive nitrogen species via iNOS to attack the bacterium inside the phagosome, a key defense the pathogen evolves to resist and survive within the granuloma."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help tuberculosis persist: by dampening the protective Th1 response, expanded Tregs can let M. tuberculosis survive in latency, part of the immune balance that keeps the infection contained yet not cleared."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "TB is an oxygen-seeking infection: aerobic M. tuberculosis favors the oxygen-rich upper lung where reactivation strikes, while deep in the granuloma's hypoxic, oxygen-starved core the bacteria turn dormant—the latency that makes TB so hard to cure."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Healed TB leaves fibrosis behind: granulomas resolve with dense scarring, apical fibrosis, and traction bronchiectasis that permanently damage the lung, so survivors often carry lasting post-TB lung disease even after cure."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells join the early fight against TB: alongside macrophages they pour out interferon-gamma to activate killing of the bacteria, an innate first line before the slower T-cell granuloma response takes over."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Healed TB leaves a calcium signature: the Ghon focus and lymph node it drains often calcify into the Ranke complex, so flecks of calcium on a chest X-ray mark old, walled-off infection that can later reactivate."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "TB can settle in the gut: swallowed bacteria or bloodborne spread seed intestinal tuberculosis, especially the ileocecal region, mimicking Crohn's disease with pain, obstruction and weight loss."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1beta shapes the TB granuloma's balance: the inflammasome cytokine helps control the bacteria but, in excess, drives the tissue destruction and cavitation that spread infection, so it sits at the knife-edge of protection and damage."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Tuberculosis is a fight over iron: the bacterium needs iron to grow and scavenges it from the host, while the body locks iron away to starve it—a tug-of-war in which iron overload tilts toward the microbe."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Tuberculosis can wrap the heart: TB pericarditis fills the sac with fluid and later scars it into a constricting shell, a dangerous extrapulmonary form especially common with HIV."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Miliary tuberculosis seeds the bone marrow: bloodborne spread studs the marrow with granulomas, suppressing blood production and causing the pancytopenia of disseminated disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons hunt tuberculosis throughout its course: the chest X-ray shows the upper-lobe cavities and the fine 'millet seed' miliary spread, CT maps the damage, and old calcified Ghon foci mark where a long-healed infection once smoldered."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Miliary tuberculosis peppers the spleen: bloodborne bacilli seed it with countless tiny granulomas, swelling the organ — splenomegaly studded with white tubercles is a classic finding of disseminated disease at autopsy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Spinal tuberculosis threatens the nerves it surrounds: Pott's disease erodes the vertebrae and forms a cold abscess that compresses the spinal cord and its roots, causing the paraplegia that is TB's most feared skeletal complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Curing TB endangers the liver: the core drugs — isoniazid, rifampin, and pyrazinamide — are all hepatotoxic, so transaminases are watched and the regimen held if they climb, balancing the risk against leaving the infection untreated."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "TB walls itself in with collagen: the granuloma rings its caseous core with epithelioid cells and a fibrous, collagen-rich cuff, and healing leaves the scarred, calcified lesions and lung cavities that mark old or arrested disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "TB's stain hangs on a waxy wall: Mycobacterium tuberculosis sheathes itself in mycolic-acid lipids that electron microscopy resolves as a thick envelope — the layer that traps the Ziehl-Neelsen dye and makes the bacillus acid-fast."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "TB is fought by cells, not antibodies: the response is T-cell and macrophage driven, so antibody serology is too unreliable for diagnosis that the WHO recommends against it, and detection rests instead on IGRA, smear, culture, and molecular tests."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "TB can eat into the skeleton: spread to the spine causes Pott's disease, collapsing vertebrae into a gibbus deformity, while tuberculous arthritis and dactylitis mark its reach into bone and joint beyond the lung."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The cure is hard on the liver: isoniazid, rifampin, and pyrazinamide are all hepatotoxic, injuring hepatocytes into a drug-induced hepatitis that is the chief reason TB therapy must be monitored and sometimes interrupted."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "TB quietly causes infertility: genitourinary tuberculosis scars the fallopian tubes and epididymis, an important and treatable cause of infertility in high-burden regions, while active TB in pregnancy threatens mother and fetus."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "The bacillus turns the body's brakes against it: M. tuberculosis induces IL-10, the anti-inflammatory cytokine that dampens the protective Th1 response and helps the organism survive inside macrophages as latent infection."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "TB can settle in the eye: hematogenous spread seeds choroidal tubercles in miliary disease and drives a chronic uveitis, an ocular tuberculosis that can threaten sight and signals disseminated infection."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Infection begins in the air sacs: inhaled bacilli are first engulfed by alveolar macrophages, and it is here in the alveoli that the primary granuloma forms, the foothold from which TB either is contained or spreads."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "A cellular self-eating defense is the battleground: macrophage autophagy can capture and destroy the bacilli, so the bug actively blocks phagosome maturation to survive — making autophagy-boosting drugs a host-directed therapy idea against TB."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The infected macrophage's master switch is hijacked: Mycobacterium tuberculosis manipulates NF-κB signaling to tune inflammation and its own survival, balancing the cytokine storm that builds the granuloma against the cell-death pathways that would clear it."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 tilts the immune response toward tolerance: driven by IL-10 in TB, STAT3 dampens the macrophage's killing program, a regulatory brake the bacillus exploits to persist inside the granuloma."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Chronic infection thickens the blood: active TB is a recognized prothrombotic state, raising deep-vein thrombosis and pulmonary embolism risk through inflammation, immobility and the acute-phase rise in clotting factors."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Overwhelming disease can mimic bacterial sepsis: disseminated miliary TB, especially in the immunocompromised, produces a fulminant septic picture with shock and multiorgan failure that needs prompt anti-tuberculous therapy."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "It leaves cavities the mold colonizes: healed TB scars the lung with cavities where Aspergillus settles into an aspergilloma (fungus ball), a classic late complication that can cause life-threatening hemoptysis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "TB meningitis inflames the brain's arteries: the basal exudate of tuberculous meningitis triggers a vasculitis of perforating vessels, causing ischemic stroke that is a major cause of the disease's neurological damage."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It can armor the heart: tuberculous pericarditis heals into a thick, calcified shell, and the resulting constrictive pericarditis impairs ventricular filling to produce a distinctive right-sided heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its key drug starves the nerves of vitamin B6: isoniazid depletes pyridoxine and causes a dose-dependent peripheral neuropathy with burning neuropathic pain, which routine co-prescribed B6 is given to prevent."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Kidney and TB injure each other: TB can directly infect the kidney as genitourinary disease, while chronic kidney disease and dialysis blunt immunity enough to reactivate latent infection — a two-way relationship."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A long, stigmatized illness and its drugs darken mood: the months of treatment, social isolation and stigma of TB, plus the neuropsychiatric effects of isoniazid and cycloserine, contribute to depression during therapy."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is the classic cause of adrenal failure worldwide: TB can destroy both adrenal glands, producing Addison's disease, and tuberculous involvement of the pituitary or thyroid adds further endocrine damage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "TB attacks the gut and its drugs poison the liver: intestinal and peritoneal tuberculosis mimic Crohn's disease and cause obstruction, while isoniazid, rifampicin and pyrazinamide are all hepatotoxic."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A long, isolating, stigmatised illness breeds worry: the months of treatment, infectivity precautions and social stigma of TB foster chronic anxiety alongside the depression its course and drugs can bring."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lung is its home: pulmonary tuberculosis is the dominant form, cavitating the upper lobes and causing chronic cough, haemoptysis and fibrosis, and it spreads by infectious aerosols."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It invades the brain and spine: tuberculous meningitis and intracranial tuberculomas are devastating, and Pott's disease of the spine can collapse vertebrae onto the spinal cord."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It seeds the urinary tract: genitourinary tuberculosis causes sterile pyuria, ureteric strictures and renal destruction, a common site of extrapulmonary disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can wrap and squeeze the heart: tuberculous pericarditis causes a pericardial effusion that can progress to constrictive pericarditis, a major extrapulmonary manifestation in endemic regions."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It settles in and reacts on the skin: cutaneous tuberculosis such as lupus vulgaris and scrofuloderma, and the reactive panniculitis of erythema nodosum, are dermatological signs of infection."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "One of its drugs raises uric acid: pyrazinamide, a first-line antitubercular, reduces urate excretion and can cause hyperuricaemia and precipitate gout flares."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids help in some sites: adjunctive corticosteroids reduce mortality in tuberculous meningitis and pericarditis by dampening the destructive granulomatous inflammation."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Undernutrition and TB feed each other: malnutrition is a leading risk factor for active tuberculosis, and zinc and other micronutrient support aids recovery alongside drug treatment."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Biologics reawaken it: anti-TNF drugs like adalimumab can reactivate latent tuberculosis, so screening and treatment of latent infection are mandatory before starting them."
  - target: 03-medicine/01-modern/06-antimicrobial/rifampicin
    relation: connects-to
    note: "The cornerstone of cure: rifampicin anchors the multi-drug RIPE regimen that sterilises tuberculosis over months; a potent CYP450 inducer that turns secretions orange, its loss to resistance defines multidrug-resistant TB."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Pott's disease destroys the spine: skeletal tuberculosis, especially tuberculous spondylitis of the thoracolumbar vertebrae, erodes bone and intervertebral discs, causing gibbus deformity, cold abscesses and spinal-cord compression."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Abdominal TB mimics Crohn's: intestinal tuberculosis produces ileocaecal ulceration, strictures and granulomas almost indistinguishable from Crohn's disease — a critical distinction, since the anti-TNF drugs used for IBD reactivate latent TB."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Its biologics reawaken the bacillus: like inflammatory bowel disease, rheumatoid arthritis treated with anti-TNF agents risks reactivating latent tuberculosis, so TB screening is mandatory before starting them."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It infects the liver and its cure injures it: miliary tuberculosis seeds granulomas in the hepatic lobules, while first-line drugs—isoniazid, rifampicin, pyrazinamide—are hepatotoxic, making liver monitoring routine in treatment."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Beyond the cavitary kidney lesions: chronic tuberculosis can drive secondary AA amyloidosis that deposits in the glomerulus, adding nephrotic proteinuria and renal failure to genitourinary TB's destructive disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Granuloma immunity: the TB granuloma is ringed by lymphoid aggregates with germinal-centre-like B-cell follicles, and BCG works by priming these adaptive responses—immunity that fades, leaving latent bacilli walled but alive."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous TB: lupus vulgaris and scrofuloderma are direct mycobacterial skin infections, while erythema nodosum is a hypersensitivity rash—both show TB and the immune response to it reaching the skin."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "The BCG paradox: the live attenuated TB vaccine is instilled into the bladder to treat early bladder cancer, the mycobacterial immune activation that fights cancer being the same response TB exploits and evades."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "CNS tuberculosis seizes the brain: tuberculous meningitis and tuberculomas are major causes of seizures and chronic epilepsy in endemic regions, especially in children, long after the infection is treated."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Pleural mimics: tuberculous pleurisy and mesothelioma both produce pleural thickening, effusion and a rind, an infectious-versus-malignant differential resolved only by biopsy especially where TB is common."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A deadly syndemic: COVID-19 disrupted TB diagnosis and treatment programmes worldwide and reversed years of progress, while the two respiratory infections can coexist and worsen each other's outcomes."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Building the granuloma wall: fibroblasts lay down the collagen capsule that walls off the tuberculous granuloma, and their dysregulated activity drives the cavitation and lung fibrosis of advanced TB."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome immunity: Mycobacterium tuberculosis activates the NLRP3 inflammasome to release IL-1β, central to granuloma formation but also to the immunopathology of the disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 early defence: IL-17/Th17 responses recruit neutrophils and help organise the granuloma in early tuberculosis, complementing the dominant IFN-γ/Th1 response."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic killing: CD8 cytotoxic T cells use perforin and granulysin to kill Mtb-infected macrophages, a key arm of immunity against tuberculosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the lung to form the granuloma, the organised immune structure that walls off Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Granuloma hypoxia: the necrotic core of the TB granuloma is hypoxic, stabilising HIF-1α in macrophages, which shapes their metabolism and bactericidal capacity."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate recognition: Toll-like receptors including TLR4 (with TLR2) sense Mycobacterium tuberculosis cell-wall lipids on macrophages, triggering the NF-κB-driven cytokine response that initiates the anti-mycobacterial defence."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic sensing: the Mtb ESX-1 system permeabilises the phagosome, exposing bacterial DNA to cGAS-STING, which drives both protective autophagy and the type-I interferon that can paradoxically worsen disease."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: macrophages and dendritic cells present Mtb antigens on MHC class II to prime the CD4 Th1 cells whose IFN-γ is indispensable for controlling tuberculosis — the basis of its vulnerability in HIV."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Macrophage death mode: the balance between prostaglandin E2 and lipoxin A4 in infected macrophages decides whether they die by protective apoptosis, which contains Mtb, or by necrosis, which releases viable bacilli — a host-directed-therapy target in tuberculosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Granuloma angiogenesis: VEGF drives the abnormal vascularisation of the tuberculous granuloma, and the resulting leaky vessels limit drug penetration, the rationale for VEGF-blocking host-directed therapy to normalise granuloma vasculature."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron nutritional immunity: infection-driven hepcidin sequesters iron inside macrophages to starve Mtb, but this also produces the anaemia of chronic disease common in active tuberculosis, a double-edged host strategy in the fight for iron."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Granuloma and immune evasion: TGF-β within the tuberculous granuloma promotes the fibrotic walling-off of the lesion while suppressing protective Th1 immunity, a host-pathogen balance Mtb exploits for persistence."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Early innate cytokine: IL-6 is an early macrophage cytokine in M. tuberculosis infection that shapes the Th17/Th1 balance and drives the acute-phase response and wasting of active tuberculosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the Th17 cells whose IL-17A (already mapped) recruits neutrophils and helps organise the protective granuloma in tuberculosis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate sensing: TLR2/TLR4 recognition of Mtb lipoproteins (TLR4 mapped) signals through MyD88 to activate NF-κB (mapped) and the macrophage antimycobacterial response in tuberculosis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Autophagy brake: mTOR suppresses the autophagy (mapped) that delivers Mtb to lysosomes, so mTOR inhibition enhances xenophagic clearance — a host-directed-therapy strategy in tuberculosis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis vs necrosis: the fate of the infected macrophage is decisive in TB — caspase-3-mediated apoptosis contains Mtb, whereas necrosis releases it, the balance the bacterium manipulates to spread."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon signal transduction: IFN-γ and type-I-interferon signalling through JAK-STAT (IFN-γ, STAT1 and type-I IFN already mapped) governs both the protective macrophage activation and the detrimental type-I-IFN response in tuberculosis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Macrophage fate: the BCL-2 family balance between apoptosis and necrosis of infected macrophages determines whether Mycobacterium tuberculosis is contained or disseminated (caspase-3 already mapped), a fate Mtb actively manipulates."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Macrophage redox: NRF2 antioxidant signalling shapes the macrophage redox environment and the oxidative-burst control of Mycobacterium tuberculosis within the granuloma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 accumulates around the phagosomal membrane damaged by Mycobacterium tuberculosis, marking the bacillus for selective autophagy within the macrophage."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling promotes the survival of Mtb-infected macrophages and is subverted by the bacillus to inhibit phagosome maturation in the granuloma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling downstream of pattern-recognition receptors tunes the macrophage cytokine response (including TNF-α) to Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate macrophage autophagy and antimicrobial gene programs that determine control of intracellular Mtb."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA) signaling shapes macrophage autophagy and the inflammatory cytokine output that tips containment versus progression of Mtb."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Calprotectin (S100A8/A9) released by neutrophils in TB granulomas amplifies inflammation and contributes to tissue destruction and cavitation."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the macrophage IL-10/IL-12 balance that tips protective immunity versus pathology in tuberculosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-driven autophagy (autophagy already mapped) is a host xenophagy defense that Mycobacterium tuberculosis subverts."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling in macrophages modulates the phagosome maturation and inflammatory response to Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation and macrophage epigenetic reprogramming (trained immunity) shape the host response to tuberculosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the type-2 and regulatory immune balance of the tuberculosis granuloma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling recruits leukocytes into the granuloma that walls off Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and granuloma organization of tuberculosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3-mediated opsonization participates in the macrophage uptake of Mycobacterium tuberculosis and the innate response to tuberculosis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunosuppressive and anti-inflammatory modulation of the tuberculous granuloma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage recruitment and granuloma formation of tuberculosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the macrophage epigenetic reprogramming (trained immunity) of tuberculosis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to tuberculosis."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Adjunctive corticosteroids: dexamethasone acting through the glucocorticoid receptor reduces mortality in tuberculous meningitis and pericarditis by dampening the host immunopathology that damages tissue around the granuloma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Undernutrition and risk: malnutrition is the leading global driver of tuberculosis, and low leptin in the undernourished impairs the cell-mediated immunity that contains Mycobacterium tuberculosis, linking nutritional state to reactivation risk."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2 drives the clonal proliferation of the antigen-specific T cells that sustain granuloma control of tuberculosis, and IL-2 responses mark protective immunity, a rationale for its trial as adjunctive immunotherapy."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of infection: active tuberculosis commonly causes anaemia of chronic disease through hepcidin-driven iron sequestration (hepcidin already mapped) and marrow suppression, lowering haemoglobin and marking disease severity."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Tuberculous pericarditis: tuberculosis is a major cause of pericarditis, especially in HIV, and the resulting effusive-constrictive disease can injure the myocardium, with troponin marking the cardiac involvement of this extrapulmonary form."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Airway mucosal defence: secretory IgA on the respiratory mucosa is part of the first-line barrier against inhaled Mycobacterium tuberculosis, and mucosal immunity is a target of next-generation tuberculosis vaccines."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen priming: dendritic cells carry Mycobacterium tuberculosis antigen from the lung to the draining lymph nodes to prime the CD4 Th1 response (IL-12 and interferon-gamma already mapped), the delay in which lets the infection establish."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron tug-of-war: Mycobacterium tuberculosis needs iron to grow, and the host sequesters it through hepcidin (already mapped), a nutritional-immunity battle that also produces the anaemia of chronic tuberculosis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative killing and injury: reactive oxygen species, to which xanthine oxidase contributes, help macrophages (already mapped) kill the bacillus but also drive the tissue damage of the granuloma, part of the double-edged oxidative response in tuberculosis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cholesterol as carbon source: Mycobacterium tuberculosis catabolises host cholesterol as a carbon and energy source inside the macrophage (already mapped), the foamy lipid-laden macrophages of the granuloma reflecting this metabolic dependency."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc nutritional immunity: the macrophage poisons the phagosome with a burst of zinc to kill the ingested bacillus, part of the nutritional-immunity metal warfare (iron already mapped) waged against Mycobacterium tuberculosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper nutritional immunity: the macrophage also floods the phagosome with toxic copper to kill the bacillus, and with zinc (already mapped) this metal poisoning is a key host defence that Mycobacterium tuberculosis must resist."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Non-protective Th2 arm: IL-4 and the Th2 response, when they dominate over the protective Th1 (IFN-γ and IL-12 already mapped) axis, are associated with poorer control of Mycobacterium tuberculosis and more progressive disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the Th1 response shapes the granulomatous control of tuberculosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Wasting and metabolism: adiponectin, with leptin (already mapped), reflects the wasting and the metabolic-nutritional depletion — the classic 'consumption' — of chronic active tuberculosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Wasting adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the wasting and the systemic inflammation (IL-6 and TNF already mapped) of chronic active tuberculosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant defence: the selenoprotein antioxidant defence; the low selenium of the TB-associated malnutrition worsens the oxidative (xanthine oxidase already mapped) tissue damage and the antimycobacterial immunity."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Cathelicidin defence: the vitamin-D-dependent macrophage (already mapped) cathelicidin antimicrobial response against Mycobacterium tuberculosis; vitamin-D deficiency raises the TB risk."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "HIV-TB syndemic: the HIV-1 co-infection, by depleting the CD4 T-helper cells (already mapped), is the leading driver of the TB reactivation and progression, the deadly co-pathogen of tuberculosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Th2-shift arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the Th2 shift that antagonises the protective Th1 (IFN-γ already mapped) immunity and worsens tuberculosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) marks the type-2 immune dimension that opposes the protective cell-mediated immunity against Mycobacterium tuberculosis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Granuloma B cells: the B cells form the lymphoid follicles of the tuberculous granuloma and shape the local T-cell (already mapped) response and the emerging antibody-mediated protection against Mycobacterium tuberculosis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody arm: the plasma cells, downstream of the B cells (already mapped), secrete the anti-mycobacterial antibodies (immunoglobulin already mapped) of the increasingly recognised humoral immunity to tuberculosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell response: the mast cells infiltrate the tuberculous granuloma and contribute to the innate and type-2 immune response to Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in granuloma: the complement C5 and its C5a (with C3 already mapped) contribute to the recruitment of the myeloid cells to the tuberculous granuloma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the neutrophil (already mapped) and monocyte recruitment in the immune response to Mycobacterium tuberculosis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Nutritional immunity: transferrin, by withholding iron (already mapped) from Mycobacterium tuberculosis, is part of the iron-restriction innate defence against tuberculosis, which the bacterium counters with siderophores."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) that opsonises Mycobacterium tuberculosis for the macrophage (already mapped) uptake into its intracellular niche."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Lectin/classical regulation: the C1-esterase inhibitor regulates the classical and lectin (mannose-binding) complement pathways that opsonise Mycobacterium tuberculosis in the innate response to tuberculosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Cavitary fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator of the fibrotic remodelling and the cavity-wall formation of pulmonary tuberculosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-driven tolerance: TSLP from the MTB-infected airway epithelium (alveolus already mapped) drives dendritic-cell (already mapped) polarisation toward an immunosuppressive type-2 phenotype that contributes to the mycobacterial immune evasion of tuberculosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact-pathway coagulation: bradykinin, generated by kallikrein activation in the pleural and pericardial exudates of tuberculosis, amplifies the vascular permeability and pleural effusion characteristic of the serosal forms of pulmonary tuberculosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia of TB: erythropoietin is a key driver of recovery from the anaemia of chronic disease (already mapped) of active tuberculosis, and EPO signalling may modulate the iron-restriction (iron already mapped) innate defences of the infected macrophage (already mapped)."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Granuloma mast-cell mediator: histamine from mast cells recruited to the tuberculosis granuloma amplifies the local type-2 regulatory immune response and vascular permeability, contributing to the containment-versus-immunopathology balance within the TB lesion."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian TB immunity: melatonin stimulates macrophage (already mapped) antimycobacterial killing; reduced nocturnal melatonin during active TB impairs the phagocytic burst and contributes to the immunological dysregulation of tuberculosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Neuroimmune TB amplifier: prolactin is elevated in active tuberculosis and stimulates macrophage (already mapped) activation, T-cell proliferation, and the anti-mycobacterial Th1 (IFN-γ and IL-12 already mapped) immune response essential for bacterial containment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "TB testosterone: testosterone suppresses macrophage (already mapped) antimycobacterial killing via androgen-receptor signalling, promoting mycobacterial immune evasion; androgen-mediated immunosuppression contributes to the male predominance and severity of tuberculosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "TB serotonin: serotonin modulates macrophage (already mapped) activation and Mycobacterium tuberculosis phagocytosis via 5-HT receptors; altered serotonin metabolism in active TB also contributes to the neuropsychiatric symptoms and social withdrawal of the disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "TB oxytocin: oxytocin receptors on macrophages (already mapped) and T cells (already mapped) modulate cytokine secretion and granuloma formation in tuberculosis; oxytocin deficiency contributes to the social withdrawal, anxiety and depression complicating active tuberculosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "TB vasopressin: vasopressin modulates macrophage (already mapped) cytokine secretion and granuloma vascular tone in tuberculosis; V1A receptor activation intersects NF-κB (already mapped) and IL-1β (already mapped)-driven inflammatory cascades in active TB."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "TB iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) antimycobacterial killing and NF-κB (already mapped) cytokine production in tuberculosis; hypothyroidism impairs granuloma competence and worsens control of Mycobacterium tuberculosis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "TB sodium: high dietary sodium amplifies Th17 polarisation and NF-κB (already mapped)-mediated pro-inflammatory cytokine production in tuberculosis, potentially worsening granuloma-associated tissue damage and exacerbating the inflammatory lung pathology of active disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "TB magnesium: magnesium, as mycobacterial phagosome-lysis cofactor in macrophages (already mapped), supports antimycobacterial killing; magnesium deficiency impairs NF-κB (already mapped)-mediated granuloma competence and T-cytotoxic-cell (already mapped) anti-TB immunity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "TB potassium: potassium efflux via NLRP3 inflammasome in macrophages (already mapped) and neutrophils (already mapped) drives IL-1β and IL-6 (already mapped) secretion; potassium dysregulation amplifies NF-κB (already mapped) cascade of granuloma inflammation in tuberculosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "TB phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and dendritic-cell (already mapped), fuels antimycobacterial burst; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs T-cytotoxic-cell (already mapped) in TB."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "TB chloride: chloride flux through CFTR in alveolar macrophages (already mapped) and epithelial cells modulates phagosome acidification and MTB killing; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) granulomatous inflammation of tuberculosis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "TB sulfur: hydrogen sulfide from sulfur-amino acids in macrophages (already mapped) and neutrophils (already mapped) inhibits MTB replication and promotes mitophagy; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) immunopathology of tuberculosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "TB nitrogen: nitric oxide from iNOS in macrophages (already mapped) directly kills intracellular MTB; nitrogen depletion impairs phagosome-lysosome fusion and amplifies NF-κB (already mapped) and IL-6 (already mapped) granulomatous tissue destruction in tuberculosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "TB carbon: carbon, as metabolic backbone of mycobacterial lipids in macrophages (already mapped) and neutrophils (already mapped), drives granuloma formation; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) immunopathology of tuberculosis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "TB hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and neutrophils (already mapped), quenches MTB-induced ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) granulomatous damage of tuberculosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "TB PD-1: PD-1 on T-cytotoxic-cell (already mapped) and T-helper-cell (already mapped) is upregulated during chronic MTB infection; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of tuberculosis."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "TB GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and T-cells (already mapped) modulates metabolic-immune balance; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "TB angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and T-cells (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "TB Wnt/β-catenin: Wnt/β-catenin signalling in macrophages (already mapped) and T-cells (already mapped) modulates immune homeostasis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis."
---

# Tuberculosis

## Overview

Tuberculosis (TB), caused by *Mycobacterium tuberculosis* (MTB), is the world's leading infectious disease killer among single pathogens, responsible for approximately **10 million new cases** and **1.3 million deaths** annually as of 2023 [^who-tb-report-2023]. An estimated one-quarter of the global population carries latent TB infection (LTBI); roughly 5–10% of these individuals will develop active TB over their lifetime, with the lifetime risk rising to >50% in people living with HIV.

TB is an airborne disease: an infectious person exhales droplet nuclei (1–5 μm diameter) that remain suspended in air and can be inhaled by contacts. As few as one to ten inhaled bacilli suffice for infection. High-burden regions include South-East Asia (India, Indonesia, Philippines), Africa, and Central Asia; multidrug-resistant TB (MDR-TB) is a particular threat in Eastern Europe and former Soviet states.

The WHO End TB Strategy targets a 90% reduction in incidence and 95% reduction in mortality by 2035 compared to 2015 baselines, requiring universal access to diagnosis, treatment, and prevention.

## Structure

### *Mycobacterium tuberculosis* Cell Biology

MTB is a **slow-growing, obligate aerobic, acid-fast bacillus** with several distinctive structural features:

| Feature | Detail |
|:--------|:-------|
| **Growth rate** | Doubling time 18–24 hours; colonies visible on solid media in 3–6 weeks |
| **Staining** | Acid-fast (Ziehl-Neelsen stain: pink bacilli on blue background); fluorochrome (auramine-rhodamine) for screening |
| **Cell wall** | Unusually thick: mycolic acids (C60–C90 fatty acids) + arabinogalactan + peptidoglycan core; the mycolic acid layer is the basis of acid-fastness and confers innate resistance to complement and many antibiotics |
| **Genome** | ~4.4 Mb circular chromosome; ~4,000 genes; highly conserved; GC content ~65% |
| **Virulence factors** | ESAT-6 (6-kDa early secretory antigen-6, ESX-1 secretion system); ManLAM (mannose-capped lipoarabinomannan, TLR2 agonist and phagosome maturation inhibitor); PE/PPE protein family |

**Key virulence mechanisms:**
- **ESAT-6** (encoded by *esxA*) is secreted via the ESX-1 (Type VII secretion) system → phagosomal membrane perforation → MTB escapes to cytosol → activates inflammasome and cGAS-STING (innate DNA sensing) while avoiding phagolysosomal killing
- **ManLAM** binds TLR2 → IL-10 production (suppressing IL-12); blocks phagosome acidification by preventing Rab7-mediated late-endosome fusion
- **Catalase-peroxidase (KatG)** detoxifies reactive oxygen species; *katG* mutations → isoniazid resistance

### Granuloma Architecture

The **granuloma** is the pathological hallmark of TB — a structured immune containment structure:

```
Central caseous necrosis (MTB + dead cells)
↓
Epithelioid macrophages (MTB-infected, activated)
↓
Langhans giant cells (macrophage fusion, horseshoe nucleus)
↓
CD4+ T cells (Th1, IFN-γ producing) + CD8+ CTLs
↓
B cells (follicle-like aggregates in chronic TB)
↓
Fibroblasts + fibrous capsule (outer containment)
```

In **latent TB**, granulomas are intact and immunologically active; MTB persists in a non-replicating or slowly-replicating state. In **active TB**, granuloma walls break down → caseous necrosis liquefies → cavity formation (providing aerobic niche for explosive MTB growth) → sputum-positive transmission.

## Function

### Infection Dynamics

**Primary infection:**
1. Inhaled droplet nuclei reach alveoli → alveolar macrophages phagocytose MTB via multiple receptors (complement receptors CR3/CR4, mannose receptor, DC-SIGN)
2. MTB arrests phagosome maturation → survives in early endosome (pH ~6.4 rather than 4.5)
3. Intracellular multiplication → macrophage lysis → infects neighbouring macrophages and DCs
4. DCs migrate to regional lymph nodes → prime CD4⁺ T cells (2–8 weeks incubation period) → T cell-mediated immunity begins → granuloma forms → bacillary replication controlled

**Latent TB infection (LTBI):**
- ~90% of immunocompetent adults who are infected do not develop active disease
- MTB persists in granulomas in a state of relative dormancy
- IGRA/TST converts to positive (indicates immune sensitisation, not necessarily active disease)
- Reactivation triggers: HIV (CD4 depletion), anti-TNF therapy, diabetes mellitus, malnutrition (BMI <18.5), silicosis, corticosteroids, ageing, organ transplant

**Transmission:**
- Pulmonary TB (especially smear-positive) is the main source; laryngeal TB is highly infectious
- Extrapulmonary TB (except laryngeal) is non-infectious
- Infectiousness falls dramatically within 2 weeks of effective treatment

### Immune Evasion

MTB is an expert intracellular pathogen with multiple immune evasion strategies:
- Phagosome maturation arrest (blocks Rab7, LAMP-1, lysosomal cathepsins)
- ESAT-6-mediated phagosome perforation → cytosolic MTB → blocks cGAS-STING → limits type I interferon activation (beneficial for the host: excessive IFN-β from MTB promotes bacterial growth)
- ManLAM → TLR2 → IL-10 → suppresses DC IL-12 production
- Inhibits MHC-II antigen loading → impairs CD4⁺ T cell priming
- Induces FoxP3⁺ Treg expansion → dampens effector T cell response
- Adapts to nutrient deprivation by metabolising host cholesterol as carbon source

## Pathology

### Disease Spectrum

| Category | Definition | Characteristics |
|:---------|:-----------|:----------------|
| **LTBI** | MTB infection, positive IGRA/TST, no symptoms, normal CXR | Non-infectious; 5-10% lifetime reactivation risk; treat if high-risk |
| **Primary TB** | Active disease in a newly infected individual | Often hilar adenopathy + lower/middle lobe infiltrate (Ghon complex); can progress in immunocompromised or young children |
| **Post-primary TB** | Reactivation in previously infected person | Upper lobe cavitary disease; highest infectiousness; cough + haemoptysis + night sweats + weight loss |
| **Miliary TB** | Haematogenous dissemination → seeding of all organs | 1–3 mm nodules on CXR (millet seed pattern); high mortality; common in HIV |
| **Extrapulmonary TB** | Any organ outside lungs | TB meningitis (highest mortality), Pott's disease (vertebral), genitourinary, pericardial, pleural, lymph node (scrofula) |

### Drug-Sensitive TB Treatment

Standard **HRZE** regimen [^nahid-2016-tb-treatment]:
- **Intensive phase (2 months):** Isoniazid (H) + Rifampicin (R) + Pyrazinamide (Z) + Ethambutol (E)
- **Continuation phase (4 months):** Isoniazid + Rifampicin
- Total duration: 6 months (can extend to 9 months for cavitary disease with positive 2-month culture)
- Treatment completion rate target: >90%

**Drug mechanisms:**
| Drug | Target | Key Side Effects |
|:-----|:-------|:----------------|
| Isoniazid | KatG → active form inhibits InhA (mycolic acid synthesis) | Hepatotoxicity, peripheral neuropathy (supplement B6) |
| Rifampicin | RNA polymerase β subunit (RpoB) | Hepatotoxicity, orange urine, drug interactions (CYP450 inducer) |
| Pyrazinamide | PncA → active acid disrupts membrane potential | Hyperuricaemia, hepatotoxicity; active only in acidic phagolysosome |
| Ethambutol | EmbB (arabinogalactan synthesis) | Optic neuritis (dose-dependent; monitor visual acuity) |

### MDR-TB and XDR-TB

- **MDR-TB:** Resistant to both isoniazid and rifampicin (~500,000 cases/year)
- **XDR-TB:** MDR + resistant to fluoroquinolones + at least one of bedaquiline/linezolid
- **BPaL regimen** (ZeNix trial 2022): Bedaquiline (ATP synthase inhibitor) + Pretomanid (nitroimidazole, respiratory chain) + Linezolid (oxazolidinone, 50S) × 6 months → ~89% cure rate for XDR-TB and treatment-intolerant MDR-TB; WHO-approved 2022

### Diagnosis

| Test | Mechanism | Sensitivity / Specificity | Notes |
|:-----|:----------|:--------------------------|:------|
| **Sputum smear (ZN/fluorescence)** | Acid-fast bacillus visualisation | Sens ~50-70% / Spec ~99% | Rapid, cheap; misses paucibacillary disease |
| **MGIT liquid culture** | Growth in Mycobacteria Growth Indicator Tube | Sens ~90% / Spec ~99% | Gold standard; results in 1–3 weeks |
| **Xpert MTB/RIF** | Real-time PCR + RIF resistance probe | Sens ~85-90% / Spec ~99% | 2-hour result; WHO recommended first-line |
| **TST (Mantoux)** | T cell recall response to PPD | Variable; cross-reactive with BCG/NTM | 48–72h reading; induration ≥5 mm (HIV), ≥10 mm (high-risk), ≥15 mm (low-risk) |
| **IGRA (QuantiFERON/T-SPOT)** | Ex vivo IFN-γ release to ESAT-6/CFP-10 | Sens ~80-90% / Spec ~95-99% | Not affected by BCG; preferred in vaccinated populations |
| **ADA (adenosine deaminase)** | Pleural/CSF marker of T cell activity | High sensitivity for pleural/meningeal TB | Useful for extrapulmonary TB diagnosis |

### Prevention

- **BCG vaccine (Bacillus Calmette-Guérin):** Live-attenuated *M. bovis*; given at birth in high-burden countries; 80% protection against severe childhood TB (meningeal, miliary); variable protection against adult pulmonary TB (~0–80%)
- **LTBI treatment:** Isoniazid × 6–9 months, or 3HP (isoniazid + rifapentine weekly × 12 doses), or 4R (rifampicin × 4 months) — reduces reactivation risk by ~60–90%
- **Airborne precautions:** Negative-pressure isolation rooms; N95 respirators for healthcare workers; UV germicidal irradiation

## Connections

- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IFN-γ axis is essential for granuloma formation and MTB containment; IL12B or IL12RB1 loss-of-function → MSMD with recurrent BCG/NTM disease; ustekinumab (anti-p40) → latent TB reactivation risk; IGRA screening mandatory before anti-IL-12 therapy initiation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is required for granuloma assembly and maintenance; anti-TNF biologic therapy (infliximab, adalimumab, certolizumab) → 4–25× increased TB reactivation risk; TNF receptor fusion proteins (etanercept) carry lower risk; mandatory IGRA/TST screening and LTBI treatment before anti-TNF initiation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ activates macrophages to restrict MTB growth via phagosome acidification, ROS burst, and cathelicidin (LL-37) production; IFN-γ released by MTB-sensitised T cells in response to ESAT-6/CFP-10 is the molecular basis of IGRA diagnostic tests; IFNGR1/IFNGR2 loss → MSMD with disseminated MTB/BCG disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — TB is a classic ACD cause: MTB-driven IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; ACD severity tracks TB disease activity (smear positivity, cavitary extent); successful treatment resolves ACD within weeks to months.
- `connects-to` → **[Immune System](../immune-system/README.md)** — MTB exemplifies intracellular immune evasion: phagosome maturation arrest, ESAT-6-mediated cytosolic escape, MHC-II inhibition, Treg induction; CD4⁺ Th1 cells orchestrate granuloma through IFN-γ and IL-2; HIV-related CD4⁺ depletion → TB reactivation is the archetypal immunodeficiency-pathogen interaction.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is the single most powerful risk factor for TB reactivation; HIV-driven CD4⁺ T cell depletion collapses granuloma integrity → latent TB reactivates; TB is the leading cause of AIDS-related mortality worldwide; concurrent ART + HRZE are required; IRIS (immune reconstitution inflammatory syndrome) complicates early ART initiation in TB-HIV co-infection.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ → STAT1 → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling → impaired macrophage activation; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM susceptibility — demonstrating STAT1 is non-redundant.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is tuberculosis's primary battleground: inhaled M. tuberculosis seeds the alveoli, where Th1 granulomas wall it off; reactivation in oxygen-rich upper lobes makes caseating cavities that shed bacilli in cough — the infectious form — and a Ghon focus marks healed disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The macrophage is host and battleground in tuberculosis: M. tuberculosis is phagocytosed but blocks phagosome maturation to survive inside, while IFN-γ-activated macrophages fight back with NO; the granuloma is a ball of infected macrophages that contains but rarely clears it.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis is caused by Mycobacterium tuberculosis: its waxy mycolic-acid wall (acid-fast) resists killing and drives the slow granulomatous response; it grows slowly (weeks to culture) and demands months of multidrug RIPE therapy, while MDR/XDR-TB resistance grows.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes roughly triples the risk of active tuberculosis: hyperglycemia impairs macrophage and T-cell function, so diabetics reactivate latent TB more readily and fare worse—bidirectional, as TB also worsens glycemic control.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Control of tuberculosis depends on Th1 helper T cells: IFN-γ from CD4+ Th1 cells activates infected macrophages to kill the bacillus and maintain the granuloma, which is why HIV-driven CD4 loss so dramatically raises TB reactivation and dissemination.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Mycobacterium tuberculosis subverts dendritic cells to delay immunity: by slowing DC migration and antigen presentation to T cells in lymph nodes, the bacillus buys weeks before an adaptive Th1 response forms—part of why TB establishes a foothold before containment.
- `connects-to` → **[COPD](../copd/README.md)** — Tuberculosis and COPD interact in both directions: past TB scarring causes airflow obstruction resembling COPD, while COPD and its inhaled steroids raise TB risk—so in high-burden regions chronic cough and obstruction warrant testing for active or prior TB.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D underpins macrophage defense against tuberculosis: vitamin-D signaling induces the antimicrobial peptide cathelicidin that helps macrophages kill M. tuberculosis, so deficiency raises TB risk—the old link behind 'sunlight and cod-liver oil' sanatorium cures.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Tuberculosis and lung cancer overlap clinically: both can present as a cavitary or spiculated lung mass, old TB scars raise later lung-cancer risk, and chronic granulomatous inflammation may promote carcinogenesis—so a 'mass' in an endemic area needs both worked up.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is harmful in tuberculosis, unlike in viral infection: a type I IFN signature marks active, severe TB because it suppresses the protective IFN-gamma/macrophage response—so the same cytokine family that fights viruses helps Mtb evade killing.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils are a double-edged sword in tuberculosis: they swarm to infected lung but, when overwhelmed, drive the tissue necrosis and cavitation that spreads Mtb—so a neutrophil-dominated response marks severe, transmissible disease rather than control.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Tuberculosis is a classic cause of adrenal insufficiency: hematogenous spread can destroy both adrenal glands, producing Addison's disease—historically the leading cause—so adrenal calcification or new Addison's should prompt a search for TB.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic CD8 T cells help contain tuberculosis: alongside CD4 help, they kill infected macrophages that fail to clear the bacillus and secrete IFN-γ, so they are central to granuloma immunity and a key target for next-generation TB vaccines.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Tuberculosis often localizes to the lymphatic system: cervical node TB (scrofula) is the classic extrapulmonary form, and lymphatic and bloodstream spread of the bacillus seeds miliary disease throughout the body when immunity fails.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Tuberculosis can invade the brain: hematogenous seeding causes TB meningitis and tuberculomas, among the deadliest forms—so suspected CNS TB demands urgent treatment with steroids, since inflammation, not just infection, drives the damage.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Tuberculosis frequently spreads to the kidney: genitourinary TB is a leading extrapulmonary form, seeding the kidney to cause sterile pyuria, scarring and ureteral strictures—so persistent urinary symptoms with negative routine cultures should raise suspicion.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Macrophages kill tuberculosis partly with nitric oxide: activated by IFN-gamma, they generate reactive nitrogen species via iNOS to attack the bacterium inside the phagosome, a key defense the pathogen evolves to resist and survive within the granuloma.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help tuberculosis persist: by dampening the protective Th1 response, expanded Tregs can let M. tuberculosis survive in latency, part of the immune balance that keeps the infection contained yet not cleared.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — TB is an oxygen-seeking infection: aerobic M. tuberculosis favors the oxygen-rich upper lung where reactivation strikes, while deep in the granuloma's hypoxic, oxygen-starved core the bacteria turn dormant—the latency that makes TB so hard to cure.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Healed TB leaves fibrosis behind: granulomas resolve with dense scarring, apical fibrosis, and traction bronchiectasis that permanently damage the lung, so survivors often carry lasting post-TB lung disease even after cure.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells join the early fight against TB: alongside macrophages they pour out interferon-gamma to activate killing of the bacteria, an innate first line before the slower T-cell granuloma response takes over.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Healed TB leaves a calcium signature: the Ghon focus and lymph node it drains often calcify into the Ranke complex, so flecks of calcium on a chest X-ray mark old, walled-off infection that can later reactivate.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — TB can settle in the gut: swallowed bacteria or bloodborne spread seed intestinal tuberculosis, especially the ileocecal region, mimicking Crohn's disease with pain, obstruction and weight loss.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1beta shapes the TB granuloma's balance: the inflammasome cytokine helps control the bacteria but, in excess, drives the tissue destruction and cavitation that spread infection, so it sits at the knife-edge of protection and damage.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Tuberculosis is a fight over iron: the bacterium needs iron to grow and scavenges it from the host, while the body locks iron away to starve it—a tug-of-war in which iron overload tilts toward the microbe.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Tuberculosis can wrap the heart: TB pericarditis fills the sac with fluid and later scars it into a constricting shell, a dangerous extrapulmonary form especially common with HIV.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Miliary tuberculosis seeds the bone marrow: bloodborne spread studs the marrow with granulomas, suppressing blood production and causing the pancytopenia of disseminated disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons hunt tuberculosis throughout its course: the chest X-ray shows the upper-lobe cavities and the fine 'millet seed' miliary spread, CT maps the damage, and old calcified Ghon foci mark where a long-healed infection once smoldered.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Miliary tuberculosis peppers the spleen: bloodborne bacilli seed it with countless tiny granulomas, swelling the organ — splenomegaly studded with white tubercles is a classic finding of disseminated disease at autopsy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Spinal tuberculosis threatens the nerves it surrounds: Pott's disease erodes the vertebrae and forms a cold abscess that compresses the spinal cord and its roots, causing the paraplegia that is TB's most feared skeletal complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Curing TB endangers the liver: the core drugs — isoniazid, rifampin, and pyrazinamide — are all hepatotoxic, so transaminases are watched and the regimen held if they climb, balancing the risk against leaving the infection untreated.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — TB walls itself in with collagen: the granuloma rings its caseous core with epithelioid cells and a fibrous, collagen-rich cuff, and healing leaves the scarred, calcified lesions and lung cavities that mark old or arrested disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — TB's stain hangs on a waxy wall: Mycobacterium tuberculosis sheathes itself in mycolic-acid lipids that electron microscopy resolves as a thick envelope — the layer that traps the Ziehl-Neelsen dye and makes the bacillus acid-fast.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — TB is fought by cells, not antibodies: the response is T-cell and macrophage driven, so antibody serology is too unreliable for diagnosis that the WHO recommends against it, and detection rests instead on IGRA, smear, culture, and molecular tests.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — TB can eat into the skeleton: spread to the spine causes Pott's disease, collapsing vertebrae into a gibbus deformity, while tuberculous arthritis and dactylitis mark its reach into bone and joint beyond the lung.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The cure is hard on the liver: isoniazid, rifampin, and pyrazinamide are all hepatotoxic, injuring hepatocytes into a drug-induced hepatitis that is the chief reason TB therapy must be monitored and sometimes interrupted.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — TB quietly causes infertility: genitourinary tuberculosis scars the fallopian tubes and epididymis, an important and treatable cause of infertility in high-burden regions, while active TB in pregnancy threatens mother and fetus.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The bacillus turns the body's brakes against it: M. tuberculosis induces IL-10, the anti-inflammatory cytokine that dampens the protective Th1 response and helps the organism survive inside macrophages as latent infection.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — TB can settle in the eye: hematogenous spread seeds choroidal tubercles in miliary disease and drives a chronic uveitis, an ocular tuberculosis that can threaten sight and signals disseminated infection.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Infection begins in the air sacs: inhaled bacilli are first engulfed by alveolar macrophages, and it is here in the alveoli that the primary granuloma forms, the foothold from which TB either is contained or spreads.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — A cellular self-eating defense is the battleground: macrophage autophagy can capture and destroy the bacilli, so the bug actively blocks phagosome maturation to survive — making autophagy-boosting drugs a host-directed therapy idea against TB.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The infected macrophage's master switch is hijacked: Mycobacterium tuberculosis manipulates NF-κB signaling to tune inflammation and its own survival, balancing the cytokine storm that builds the granuloma against the cell-death pathways that would clear it.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 tilts the immune response toward tolerance: driven by IL-10 in TB, STAT3 dampens the macrophage's killing program, a regulatory brake the bacillus exploits to persist inside the granuloma.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Chronic infection thickens the blood: active TB is a recognized prothrombotic state, raising deep-vein thrombosis and pulmonary embolism risk through inflammation, immobility and the acute-phase rise in clotting factors.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Overwhelming disease can mimic bacterial sepsis: disseminated miliary TB, especially in the immunocompromised, produces a fulminant septic picture with shock and multiorgan failure that needs prompt anti-tuberculous therapy.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — It leaves cavities the mold colonizes: healed TB scars the lung with cavities where Aspergillus settles into an aspergilloma (fungus ball), a classic late complication that can cause life-threatening hemoptysis.
- `connects-to` → **[Stroke](../stroke/README.md)** — TB meningitis inflames the brain's arteries: the basal exudate of tuberculous meningitis triggers a vasculitis of perforating vessels, causing ischemic stroke that is a major cause of the disease's neurological damage.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It can armor the heart: tuberculous pericarditis heals into a thick, calcified shell, and the resulting constrictive pericarditis impairs ventricular filling to produce a distinctive right-sided heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its key drug starves the nerves of vitamin B6: isoniazid depletes pyridoxine and causes a dose-dependent peripheral neuropathy with burning neuropathic pain, which routine co-prescribed B6 is given to prevent.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Kidney and TB injure each other: TB can directly infect the kidney as genitourinary disease, while chronic kidney disease and dialysis blunt immunity enough to reactivate latent infection — a two-way relationship.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A long, stigmatized illness and its drugs darken mood: the months of treatment, social isolation and stigma of TB, plus the neuropsychiatric effects of isoniazid and cycloserine, contribute to depression during therapy.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is the classic cause of adrenal failure worldwide: TB can destroy both adrenal glands, producing Addison's disease, and tuberculous involvement of the pituitary or thyroid adds further endocrine damage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — TB attacks the gut and its drugs poison the liver: intestinal and peritoneal tuberculosis mimic Crohn's disease and cause obstruction, while isoniazid, rifampicin and pyrazinamide are all hepatotoxic.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A long, isolating, stigmatised illness breeds worry: the months of treatment, infectivity precautions and social stigma of TB foster chronic anxiety alongside the depression its course and drugs can bring.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The lung is its home: pulmonary tuberculosis is the dominant form, cavitating the upper lobes and causing chronic cough, haemoptysis and fibrosis, and it spreads by infectious aerosols.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It invades the brain and spine: tuberculous meningitis and intracranial tuberculomas are devastating, and Pott's disease of the spine can collapse vertebrae onto the spinal cord.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It seeds the urinary tract: genitourinary tuberculosis causes sterile pyuria, ureteric strictures and renal destruction, a common site of extrapulmonary disease.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can wrap and squeeze the heart: tuberculous pericarditis causes a pericardial effusion that can progress to constrictive pericarditis, a major extrapulmonary manifestation in endemic regions.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It settles in and reacts on the skin: cutaneous tuberculosis such as lupus vulgaris and scrofuloderma, and the reactive panniculitis of erythema nodosum, are dermatological signs of infection.
- `connects-to` → **[Gout](../gout/README.md)** — One of its drugs raises uric acid: pyrazinamide, a first-line antitubercular, reduces urate excretion and can cause hyperuricaemia and precipitate gout flares.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids help in some sites: adjunctive corticosteroids reduce mortality in tuberculous meningitis and pericarditis by dampening the destructive granulomatous inflammation.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Undernutrition and TB feed each other: malnutrition is a leading risk factor for active tuberculosis, and zinc and other micronutrient support aids recovery alongside drug treatment.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Biologics reawaken it: anti-TNF drugs like adalimumab can reactivate latent tuberculosis, so screening and treatment of latent infection are mandatory before starting them.
- `connects-to` → **[Rifampicin](../../../03-medicine/01-modern/06-antimicrobial/rifampicin/README.md)** — The cornerstone of cure: rifampicin anchors the multi-drug RIPE regimen that sterilises tuberculosis over months; a potent CYP450 inducer that turns secretions orange, its loss to resistance defines multidrug-resistant TB.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Pott's disease destroys the spine: skeletal tuberculosis, especially tuberculous spondylitis of the thoracolumbar vertebrae, erodes bone and intervertebral discs, causing gibbus deformity, cold abscesses and spinal-cord compression.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Abdominal TB mimics Crohn's: intestinal tuberculosis produces ileocaecal ulceration, strictures and granulomas almost indistinguishable from Crohn's disease — a critical distinction, since the anti-TNF drugs used for IBD reactivate latent TB.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Its biologics reawaken the bacillus: like inflammatory bowel disease, rheumatoid arthritis treated with anti-TNF agents risks reactivating latent tuberculosis, so TB screening is mandatory before starting them.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It infects the liver and its cure injures it: miliary tuberculosis seeds granulomas in the hepatic lobules, while first-line drugs—isoniazid, rifampicin, pyrazinamide—are hepatotoxic, making liver monitoring routine in treatment.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Beyond the cavitary kidney lesions: chronic tuberculosis can drive secondary AA amyloidosis that deposits in the glomerulus, adding nephrotic proteinuria and renal failure to genitourinary TB's destructive disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Granuloma immunity: the TB granuloma is ringed by lymphoid aggregates with germinal-centre-like B-cell follicles, and BCG works by priming these adaptive responses—immunity that fades, leaving latent bacilli walled but alive.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous TB: lupus vulgaris and scrofuloderma are direct mycobacterial skin infections, while erythema nodosum is a hypersensitivity rash—both show TB and the immune response to it reaching the skin.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — The BCG paradox: the live attenuated TB vaccine is instilled into the bladder to treat early bladder cancer, the mycobacterial immune activation that fights cancer being the same response TB exploits and evades.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — CNS tuberculosis seizes the brain: tuberculous meningitis and tuberculomas are major causes of seizures and chronic epilepsy in endemic regions, especially in children, long after the infection is treated.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Pleural mimics: tuberculous pleurisy and mesothelioma both produce pleural thickening, effusion and a rind, an infectious-versus-malignant differential resolved only by biopsy especially where TB is common.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A deadly syndemic: COVID-19 disrupted TB diagnosis and treatment programmes worldwide and reversed years of progress, while the two respiratory infections can coexist and worsen each other's outcomes.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Building the granuloma wall: fibroblasts lay down the collagen capsule that walls off the tuberculous granuloma, and their dysregulated activity drives the cavitation and lung fibrosis of advanced TB.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome immunity: Mycobacterium tuberculosis activates the NLRP3 inflammasome to release IL-1β, central to granuloma formation but also to the immunopathology of the disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 early defence: IL-17/Th17 responses recruit neutrophils and help organise the granuloma in early tuberculosis, complementing the dominant IFN-γ/Th1 response.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic killing: CD8 cytotoxic T cells use perforin and granulysin to kill Mtb-infected macrophages, a key arm of immunity against tuberculosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into the lung to form the granuloma, the organised immune structure that walls off Mycobacterium tuberculosis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Granuloma hypoxia: the necrotic core of the TB granuloma is hypoxic, stabilising HIF-1α in macrophages, which shapes their metabolism and bactericidal capacity.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Toll-like receptors including TLR4 (with TLR2) sense Mycobacterium tuberculosis cell-wall lipids on macrophages, triggering the NF-κB-driven cytokine response that initiates the anti-mycobacterial defense at first contact.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The Mtb ESX-1 secretion system permeabilizes the phagosome, exposing bacterial DNA to cGAS-STING, which drives both protective autophagy and the type-I interferon that can paradoxically worsen disease—a double-edged innate response.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Macrophages and dendritic cells present Mtb antigens on MHC class II to prime the CD4 Th1 cells whose IFN-γ is indispensable for controlling tuberculosis—explaining why CD4 depletion in HIV so dramatically raises TB risk.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The balance between prostaglandin E2 and lipoxin A4 in infected macrophages decides whether they die by protective apoptosis, which contains Mtb, or by necrosis, which releases viable bacilli—a host-directed-therapy target in tuberculosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF drives the abnormal vascularization of the tuberculous granuloma, and the resulting leaky vessels limit drug penetration, the rationale for VEGF-blocking host-directed therapy to normalize granuloma vasculature.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Infection-driven hepcidin sequesters iron inside macrophages to starve Mtb, but this also produces the anemia of chronic disease common in active tuberculosis, a double-edged host strategy in the fight for iron.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the tuberculous granuloma promotes the fibrotic walling-off of the lesion while suppressing protective Th1 immunity, a host-pathogen balance Mtb exploits for persistence.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 is an early macrophage cytokine in M. tuberculosis infection that shapes the Th17/Th1 balance and drives the acute-phase response and wasting of active tuberculosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the Th17 cells whose IL-17A (already mapped) recruits neutrophils and helps organise the protective granuloma in tuberculosis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR2/TLR4 recognition of Mtb lipoproteins (TLR4 mapped) signals through MyD88 to activate NF-κB (mapped) and the macrophage antimycobacterial response in tuberculosis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR suppresses the autophagy (mapped) that delivers Mtb to lysosomes, so mTOR inhibition enhances xenophagic clearance—a host-directed-therapy strategy in tuberculosis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The fate of the infected macrophage is decisive in TB—caspase-3-mediated apoptosis contains Mtb, whereas necrosis releases it, the balance the bacterium manipulates to spread.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IFN-γ and type-I-interferon signaling through JAK-STAT (IFN-γ, STAT1 and type-I IFN already mapped) governs both the protective macrophage activation and the detrimental type-I-IFN response in tuberculosis.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The BCL-2 family balance between apoptosis and necrosis of infected macrophages determines whether Mycobacterium tuberculosis is contained or disseminated (caspase-3 already mapped), a fate Mtb actively manipulates.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling shapes the macrophage redox environment and the oxidative-burst control of Mycobacterium tuberculosis within the granuloma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 accumulates around the phagosomal membrane damaged by Mycobacterium tuberculosis, marking the bacillus for selective autophagy within the macrophage.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling promotes the survival of Mtb-infected macrophages and is subverted by the bacillus to inhibit phagosome maturation in the granuloma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of pattern-recognition receptors tunes the macrophage cytokine response (including TNF-α) to Mycobacterium tuberculosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate macrophage autophagy and antimicrobial gene programs that determine control of intracellular Mtb.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA) signaling shapes macrophage autophagy and the inflammatory cytokine output that tips containment versus progression of Mtb.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) released by neutrophils in TB granulomas amplifies inflammation and contributes to tissue destruction and cavitation.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the macrophage IL-10/IL-12 balance that tips protective immunity versus pathology in tuberculosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-driven autophagy (autophagy already mapped) is a host xenophagy defense that Mycobacterium tuberculosis subverts.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling in macrophages modulates the phagosome maturation and inflammatory response to Mycobacterium tuberculosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation and macrophage epigenetic reprogramming (trained immunity) shape the host response to tuberculosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the type-2 and regulatory immune balance of the tuberculosis granuloma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling recruits leukocytes into the granuloma that walls off Mycobacterium tuberculosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and granuloma organization of tuberculosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3-mediated opsonization participates in the macrophage uptake of Mycobacterium tuberculosis and the innate response to tuberculosis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunosuppressive and anti-inflammatory modulation of the tuberculous granuloma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage recruitment and granuloma formation of tuberculosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the macrophage epigenetic reprogramming (trained immunity) of tuberculosis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to tuberculosis.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Adjunctive corticosteroids: dexamethasone acting through the glucocorticoid receptor reduces mortality in tuberculous meningitis and pericarditis by dampening the host immunopathology that damages tissue around the granuloma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Undernutrition and risk: malnutrition is the leading global driver of tuberculosis, and low leptin in the undernourished impairs the cell-mediated immunity that contains Mycobacterium tuberculosis, linking nutritional state to reactivation risk.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2 drives the clonal proliferation of the antigen-specific T cells that sustain granuloma control of tuberculosis, and IL-2 responses mark protective immunity, a rationale for its trial as adjunctive immunotherapy.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of infection: active tuberculosis commonly causes anaemia of chronic disease through hepcidin-driven iron sequestration (hepcidin already mapped) and marrow suppression, lowering haemoglobin and marking disease severity.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Tuberculous pericarditis: tuberculosis is a major cause of pericarditis, especially in HIV, and the resulting effusive-constrictive disease can injure the myocardium, with troponin marking the cardiac involvement of this extrapulmonary form.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Airway mucosal defence: secretory IgA on the respiratory mucosa is part of the first-line barrier against inhaled Mycobacterium tuberculosis, and mucosal immunity is a target of next-generation tuberculosis vaccines.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen priming: dendritic cells carry Mycobacterium tuberculosis antigen from the lung to the draining lymph nodes to prime the CD4 Th1 response (IL-12 and interferon-gamma already mapped), the delay in which lets the infection establish.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron tug-of-war: Mycobacterium tuberculosis needs iron to grow, and the host sequesters it through hepcidin (already mapped), a nutritional-immunity battle that also produces the anaemia of chronic tuberculosis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative killing and injury: reactive oxygen species, to which xanthine oxidase contributes, help macrophages (already mapped) kill the bacillus but also drive the tissue damage of the granuloma, part of the double-edged oxidative response in tuberculosis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cholesterol as carbon source: Mycobacterium tuberculosis catabolises host cholesterol as a carbon and energy source inside the macrophage (already mapped), the foamy lipid-laden macrophages of the granuloma reflecting this metabolic dependency.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc nutritional immunity: the macrophage poisons the phagosome with a burst of zinc to kill the ingested bacillus, part of the nutritional-immunity metal warfare (iron already mapped) waged against Mycobacterium tuberculosis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper nutritional immunity: the macrophage also floods the phagosome with toxic copper to kill the bacillus, and with zinc (already mapped) this metal poisoning is a key host defence that Mycobacterium tuberculosis must resist.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Non-protective Th2 arm: IL-4 and the Th2 response, when they dominate over the protective Th1 (IFN-γ and IL-12 already mapped) axis, are associated with poorer control of Mycobacterium tuberculosis and more progressive disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immunity: IL-13, with IL-4 (already mapped), is part of the type-2 arm whose balance against the Th1 response shapes the granulomatous control of tuberculosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Wasting and metabolism: adiponectin, with leptin (already mapped), reflects the wasting and the metabolic-nutritional depletion — the classic 'consumption' — of chronic active tuberculosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Wasting adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the wasting and the systemic inflammation (IL-6 and TNF already mapped) of chronic active tuberculosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant defence: the selenoprotein antioxidant defence; the low selenium of the TB-associated malnutrition worsens the oxidative (xanthine oxidase already mapped) tissue damage and the antimycobacterial immunity.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Cathelicidin defence: the vitamin-D-dependent macrophage (already mapped) cathelicidin antimicrobial response against Mycobacterium tuberculosis; vitamin-D deficiency raises the TB risk.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — HIV-TB syndemic: the HIV-1 co-infection, by depleting the CD4 T-helper cells (already mapped), is the leading driver of the TB reactivation and progression, the deadly co-pathogen of tuberculosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Th2-shift arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the Th2 shift that antagonises the protective Th1 (IFN-γ already mapped) immunity and worsens tuberculosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) marks the type-2 immune dimension that opposes the protective cell-mediated immunity against Mycobacterium tuberculosis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Granuloma B cells: the B cells form the lymphoid follicles of the tuberculous granuloma and shape the local T-cell (already mapped) response and the emerging antibody-mediated protection against Mycobacterium tuberculosis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Antibody arm: the plasma cells, downstream of the B cells (already mapped), secrete the anti-mycobacterial antibodies (immunoglobulin already mapped) of the increasingly recognised humoral immunity to tuberculosis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell response: the mast cells infiltrate the tuberculous granuloma and contribute to the innate and type-2 immune response to Mycobacterium tuberculosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in granuloma: the complement C5 and its C5a (with C3 already mapped) contribute to the recruitment of the myeloid cells to the tuberculous granuloma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the neutrophil (already mapped) and monocyte recruitment in the immune response to Mycobacterium tuberculosis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Nutritional immunity: transferrin, by withholding iron (already mapped) from Mycobacterium tuberculosis, is part of the iron-restriction innate defence against tuberculosis, which the bacterium counters with siderophores.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) that opsonises Mycobacterium tuberculosis for the macrophage (already mapped) uptake into its intracellular niche.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Lectin/classical regulation: the C1-esterase inhibitor regulates the classical and lectin (mannose-binding) complement pathways that opsonise Mycobacterium tuberculosis in the innate response to tuberculosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Cavitary fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator of the fibrotic remodelling and the cavity-wall formation of pulmonary tuberculosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-driven tolerance: TSLP, released from the Mycobacterium tuberculosis-infected airway epithelium (alveolus already mapped), drives the dendritic-cell (already mapped) polarisation toward an immunosuppressive type-2 phenotype that contributes to the mycobacterial immune evasion of tuberculosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact-pathway coagulation: bradykinin, generated by kallikrein activation in the pleural and pericardial exudates of tuberculosis, amplifies the vascular permeability and pleural effusion characteristic of the serosal forms of pulmonary tuberculosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia of TB: erythropoietin is a key driver of recovery from the anaemia of chronic disease (already mapped) of active tuberculosis, and EPO signalling may modulate the iron-restriction (iron already mapped) innate defences of the infected macrophage (already mapped).
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Granuloma mast-cell mediator: histamine from mast cells recruited to the tuberculosis granuloma amplifies the local type-2 regulatory immune response and vascular permeability, contributing to the containment-versus-immunopathology balance within the TB lesion.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian TB immunity: melatonin stimulates macrophage (already mapped) antimycobacterial killing; reduced nocturnal melatonin during active TB impairs the phagocytic burst and contributes to the immunological dysregulation of tuberculosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Neuroimmune TB amplifier: prolactin is elevated in active tuberculosis and stimulates macrophage (already mapped) activation, T-cell proliferation, and the anti-mycobacterial Th1 (IFN-γ and IL-12 already mapped) immune response essential for bacterial containment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — TB testosterone: testosterone suppresses macrophage (already mapped) antimycobacterial killing via androgen-receptor signalling, promoting mycobacterial immune evasion; androgen-mediated immunosuppression contributes to the male predominance and severity of tuberculosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — TB serotonin: serotonin modulates macrophage (already mapped) activation and Mycobacterium tuberculosis phagocytosis via 5-HT receptors; altered serotonin metabolism in active TB also contributes to the neuropsychiatric symptoms and social withdrawal of the disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — TB oxytocin: oxytocin receptors on macrophages (already mapped) and T cells (already mapped) modulate cytokine secretion and granuloma formation in tuberculosis; oxytocin deficiency contributes to the social withdrawal, anxiety and depression complicating active tuberculosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — TB vasopressin: vasopressin modulates macrophage (already mapped) cytokine secretion and granuloma vascular tone in tuberculosis; V1A receptor activation intersects NF-κB (already mapped) and IL-1β (already mapped)-driven inflammatory cascades in active TB.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — TB iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) antimycobacterial killing and NF-κB (already mapped) cytokine production in tuberculosis; hypothyroidism impairs granuloma competence and worsens control of Mycobacterium tuberculosis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — TB sodium: high dietary sodium amplifies Th17 polarisation and NF-κB (already mapped)-mediated pro-inflammatory cytokine production in tuberculosis, potentially worsening granuloma-associated tissue damage and exacerbating the inflammatory lung pathology of active disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — TB magnesium: magnesium, as mycobacterial phagosome-lysis cofactor in macrophages (already mapped), supports antimycobacterial killing; magnesium deficiency impairs NF-κB (already mapped)-mediated granuloma competence and T-cytotoxic-cell (already mapped) anti-TB immunity.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — TB potassium: potassium efflux via NLRP3 inflammasome in macrophages (already mapped) and neutrophils (already mapped) drives IL-1β and IL-6 (already mapped) secretion; potassium dysregulation amplifies NF-κB (already mapped) cascade of granuloma inflammation in tuberculosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — TB phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and dendritic-cell (already mapped), fuels antimycobacterial burst; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs T-cytotoxic-cell (already mapped) in TB.

## See Also

- [^who-tb-report-2023] World Health Organization. *Global Tuberculosis Report 2023.* Geneva: WHO; 2023.
- [^nahid-2016-tb-treatment] Nahid P et al. Official ATS/CDC/IDSA Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. *Clin Infect Dis.* 2016;63(7):e147-e195. [doi:10.1093/cid/ciw376](https://doi.org/10.1093/cid/ciw376) · [PubMed 27516382](https://pubmed.ncbi.nlm.nih.gov/27516382/)
- Related entries: [il-12](../../03-molecular/il-12/README.md), [tnf-alpha](../../03-molecular/tnf-alpha/README.md), [ifn-gamma](../../03-molecular/ifn-gamma/README.md), [anemia-of-chronic-disease](../anemia-of-chronic-disease/README.md), [immune-system](../immune-system/README.md)
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — TB chloride: chloride flux through CFTR in alveolar macrophages (already mapped) and epithelial cells modulates phagosome acidification and MTB killing; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) granulomatous inflammation of tuberculosis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — TB sulfur: hydrogen sulfide from sulfur-amino acids in macrophages (already mapped) and neutrophils (already mapped) inhibits MTB replication and promotes mitophagy; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) immunopathology of tuberculosis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — TB nitrogen: nitric oxide from iNOS in macrophages (already mapped) directly kills intracellular MTB; nitrogen depletion impairs phagosome-lysosome fusion and amplifies NF-κB (already mapped) and IL-6 (already mapped) granulomatous tissue destruction in tuberculosis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — TB carbon: carbon, as metabolic backbone of mycobacterial lipids in macrophages (already mapped) and neutrophils (already mapped), drives granuloma formation; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) immunopathology of tuberculosis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — TB hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and neutrophils (already mapped), quenches MTB-induced ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) granulomatous damage of tuberculosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — TB PD-1: PD-1 on T-cytotoxic-cell (already mapped) and T-helper-cell (already mapped) is upregulated during chronic MTB infection; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of tuberculosis.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — TB GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and T-cells (already mapped) modulates metabolic-immune balance; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — TB angiotensin-II: angiotensin-II signalling in macrophages (already mapped) and T-cells (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — TB Wnt/β-catenin: Wnt/β-catenin signalling in macrophages (already mapped) and T-cells (already mapped) modulates immune homeostasis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of tuberculosis.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
