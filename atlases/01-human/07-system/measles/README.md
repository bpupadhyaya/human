---
schema: human-scale-entry/v1
id: measles
name: Measles
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Measles virus (MV; Morbillivirus; negative-sense ssRNA) caused ~128,000 deaths in 2021; SLAM/CD150 tropism enables immune amnesia (memory B/T cell depletion lasting 2-3 years); Koplik's spots and Warthin-Finkeldey giant cells are pathognomonic; MMR vaccine provides >97% efficacy."
aliases: ["measles", "rubeola", "measles virus", "MV", "Morbillivirus", "measles immune amnesia", "SSPE", "Warthin-Finkeldey", "Koplik's spots", "MMR vaccine", "measles encephalitis", "measles pneumonia", "measles bronchopneumonia", "immune amnesia virus"]
sources:
  - id: panum-1847-faroe-measles
    type: peer-reviewed
    cite: "Panum PL. Observations made during the epidemic of measles on the Faroe Islands in the year 1846. Med Classics. 1939;3:829-886."
    url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2536613/"
    accessed: "2026-06-08"
  - id: mina-2019-immune-amnesia
    type: peer-reviewed
    cite: "Mina MJ, Kula T, Leng Y, et al. Measles virus infection diminishes preexisting antibodies that offer protection from other pathogens. Science. 2019;366(6465):599-606."
    doi: "10.1126/science.aay6485"
    pmid: "31672891"
    url: "https://doi.org/10.1126/science.aay6485"
    accessed: "2026-06-08"
  - id: strebel-2019-measles-lancet
    type: peer-reviewed
    cite: "Strebel PM, Orenstein WA. Measles. N Engl J Med. 2019;381(4):349-357."
    doi: "10.1056/NEJMcp1905181"
    pmid: "31340710"
    url: "https://doi.org/10.1056/NEJMcp1905181"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mv-h-protein
    relation: connects-to
    note: "MV-H (hemagglutinin) binds SLAM/CD150 on immune cells and nectin-4 on airway epithelium; H-F fusion complex drives syncytia (Warthin-Finkeldey cells); SLAM tropism enables immune amnesia by depleting memory B and T cells."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MV negative-sense ssRNA replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β; MV V protein sequesters MDA5 and LGP2 → blocks MAVS activation; P protein blocks IRF3 phosphorylation; attenuated vaccine strains (Edmonston) with impaired V/P activate MAVS → faster clearance."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MV V protein binds STAT1/STAT2 → blocks JAK-STAT signaling → ISG suppression; MV C protein blocks IFN-β induction; MV P/V proteins sequester MDA5/LGP2 → prevent MAVS-IRF3-IFN-β; wild-type MV IFN evasion is more complete than attenuated strains — key pathogenicity distinction."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "MV (Morbillivirus; negative-sense ssRNA; R₀ 12-18) is the causative agent; SLAM/CD150 attachment glycoprotein H mediates systemic lymphoid spread; F protein drives syncytia (Warthin-Finkeldey cells); persistent MV in neurons with hypermutated genome causes SSPE."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "MV-H binds SLAM/CD150 on dendritic cells → productive DC infection → impaired IL-12/IFN-α production and reduced T cell priming; MV-infected DCs poorly present antigens; DC dysfunction contributes to measles immune amnesia lasting 2-3 years post-infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects SLAM-high memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections after measles."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Measles erases immune memory by destroying memory B cells: these cells carry the most SLAM/CD150 (3-10× naive B cells), exactly the receptor measles H protein binds, so the virus preferentially infects and deletes them — wiping out 20-70% of a child's antibody repertoire."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Measles attacks the brain in several ways: acute post-infectious encephalitis and ADEM, and — years to decades later — SSPE, a fatal degeneration driven by hypermutated measles virus persisting in neurons; the MMR vaccine essentially eliminates all of these."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Measles induces a profound, lasting immunosuppression that can reactivate latent tuberculosis: measles-infected dendritic cells make less IL-12, crippling the Th1 response that contains TB — one way post-measles immune amnesia raises susceptibility to other infections for years."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Both are vaccine-preventable respiratory viruses but differ sharply: measles (paramyxovirus) is among the most contagious pathogens (R0 12-18) and causes immune amnesia, while influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pneumonia is the leading cause of measles death: the virus directly infects respiratory epithelium and, by erasing immune memory (immune amnesia), opens the door to secondary bacterial pneumonia for months afterward; giant-cell pneumonia can be fatal in the immunocompromised."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Measles both needs and subverts cytotoxic T cells: CD8+ T cells clear measles-infected cells and drive recovery, but the virus infects memory lymphocytes via CD150/SLAM and depletes them, causing 'immune amnesia' that erases pre-existing immunity to other pathogens for 2-3 years."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "Measles and RSV are paramyxoviruses but cause very different disease: RSV is a bronchiolitis-causing pneumovirus of infants, while measles is a contagious morbillivirus with rash, fever, and Koplik spots—both can cause severe pneumonia, the leading killer in measles."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Measles can attack neurons years after infection: persistent defective virus in the brain causes subacute sclerosing panencephalitis (SSPE), a fatal degenerative disease appearing years later—one reason measles is far more than a transient childhood rash."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Measles spreads through the body via myeloid cells: alveolar macrophages and dendritic cells in the airway are the first infected, carrying the virus to lymphoid tissue where it amplifies—so these innate sentinels become the vehicle for systemic measles dissemination."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help control measles early: NK and interferon responses limit initial viral spread, but measles still infects immune cells and causes profound, lasting immunosuppression—so the innate response is overwhelmed by a virus that targets immunity itself."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Measles is especially dangerous in HIV and immunosuppression: without competent T-cell immunity, measles can cause giant-cell pneumonia and fatal disease without the typical rash, so live measles vaccine is contraindicated in severe immunosuppression."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Measles and COVID-19 illustrate herd-immunity thresholds at opposite extremes: measles is so contagious (R0 12-18) that ~95% vaccination is needed to stop spread, far above COVID's threshold—so falling measles vaccination quickly reignites outbreaks."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The measles rash is its most recognizable sign: T-cell attack on virus-infected skin capillaries produces the spreading maculopapular eruption, preceded by Koplik spots on oral mucosa—the rash marks immune engagement, not direct skin destruction."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Measles can devastate the nervous system: acute postinfectious encephalitis strikes ~1 in 1,000 cases, and years later the relentless subacute sclerosing panencephalitis (SSPE) can emerge from persistent virus—rare but fatal reasons measles is far from benign."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Measles infection leaves lifelong IgG immunity but also 'immune amnesia': it depletes memory B and T cells, erasing antibodies to other pathogens for years, so it raises susceptibility to unrelated infections—while the vaccine protects without this harm."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Measles is lymphotropic: it enters via the SLAM (CD150) receptor on immune cells and replicates in lymph nodes, spleen, and tonsils, causing generalized lymphadenopathy and the giant cells seen in lymphoid tissue—lymphoid organs are its main amplification site."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Measles can blind through the eye: the virus causes keratoconjunctivitis, and in vitamin-A-deficient children corneal ulceration and scarring lead to blindness—so measles remains a leading cause of childhood blindness in poor settings, treated with vitamin A."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Measles depletes T cells acutely: by infecting activated lymphocytes it causes sharp lymphopenia and suppressed cell-mediated immunity during infection, which is why bacterial pneumonia—not the virus itself—causes most measles deaths."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Measles erases immune memory by killing plasma and memory cells: the virus depletes the long-lived B cells and plasma cells holding antibody memory, so survivors lose protection against other pathogens for years—'immune amnesia.'"
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Measles in pregnancy is dangerous across the placenta: maternal infection raises the risk of miscarriage, prematurity and severe disease, and the virus can cross to cause congenital or neonatal measles—so vaccination before pregnancy matters."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Measles' late brain disease attacks memory circuits: SSPE (subacute sclerosing panencephalitis), a fatal years-later complication of persistent virus, progressively destroys neurons—including hippocampal memory regions—causing dementia and seizures."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Measles' biggest killer is often the gut: the virus inflames the intestinal lining, causing severe diarrhea and dehydration that, with malnutrition, account for much of measles mortality in young children."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Measles' late brain disease destroys myelin: in SSPE the persistent virus damages oligodendrocytes and white matter alongside neurons, so demyelination joins neuron loss in the relentless years-later deterioration."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Measles leaves the immune system amnesic: by infecting and depleting memory lymphocytes and inducing a regulatory, IL-10-skewed state, it erases protection against other germs for months to years, raising deaths from later infections."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Measles kills mostly by stealing oxygen: its pneumonia—whether from the virus or a bacterial superinfection—is the leading cause of measles death, flooding the lungs and dropping blood oxygen."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Measles infects the gut lining: spreading to the intestinal epithelium, it causes the diarrhea that dehydrates young children, a major contributor to measles deaths in the malnourished."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Measles can crash the platelets: the infection sometimes triggers immune thrombocytopenia, causing the bruising and bleeding of 'black measles,' a rare but dangerous hemorrhagic complication."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Measles pneumonia and its rare brain disease show on imaging: chest X-ray photons reveal the giant-cell pneumonia, and MRI maps the white-matter damage of subacute sclerosing panencephalitis."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Measles damages the alveoli: the virus forms giant cells in the air sacs (Hecht's giant-cell pneumonia), the lung injury that is a leading cause of measles death in young children."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Measles can inflame the heart: myocarditis and pericarditis are uncommon complications, adding cardiac strain to the systemic toll of a severe infection."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows measles fusing cells: the paramyxovirus drives infected cells to merge into Warthin-Finkeldey giant cells stuffed with nucleocapsids, the multinucleated hallmark seen in infected lymphoid tissue."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Diarrhea is measles' great killer: the virus strips the gut lining, and the resulting severe diarrhea and dehydration — worsened by malnutrition — are a leading cause of measles death in young children."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Measles erases immune memory: it infects and depletes the memory lymphocytes built up over a lifetime, an 'immune amnesia' that leaves children vulnerable to other infections they were once protected against for years afterward."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Measles lives and dies by antibody: the MMR vaccine and natural infection both raise protective anti-measles antibody, IgM confirms acute infection — yet the virus's immune amnesia destroys the antibody memory against other germs."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Measles can inflame the liver: a transient hepatitis with raised transaminases is common, especially in adults, one of the systemic features that make measles in grown-ups more severe than in children."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The danger of measles is what comes after: its deep, weeks-long immunosuppression opens the door to secondary bacterial pneumonia, otitis, and other infections — the complications, not the rash, that cause most measles deaths."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Measles erases immune memory: by infecting and killing memory lymphocytes and depleting the lymphoid tissue, it causes 'immune amnesia,' wiping out years of acquired protection against other pathogens long after recovery."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Measles is dangerous in pregnancy: it raises the risk of miscarriage, preterm birth, and severe maternal disease, and because the vaccine is live it cannot be given during pregnancy, leaving immunization to be timed beforehand."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "In malnourished children the gut tips the balance: measles brings vomiting and profuse diarrhea, and the resulting dehydration and worsened malnutrition are a major contributor to its mortality in low-resource settings."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Years later the virus can smolder in the brain: in subacute sclerosing panencephalitis a persistent measles strain drives chronic microglial activation and demyelination, a fatal late neurodegeneration after early-childhood infection."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Measles erases immune memory and opens the door: by depleting memory B and T cells it leaves children prey to secondary pneumococcal pneumonia and otitis, the bacterial superinfections behind much of its death toll."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The brain complications bring seizures: acute measles encephalitis and the late SSPE both injure the cortex, causing seizures — in SSPE the characteristic periodic myoclonic jerks that mark its relentless course."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "RIG-I is the front-line sensor of measles: it detects MV 5′-triphosphate RNA replication intermediates and signals through MAVS to launch type I interferon — which the virus's V and C proteins fight to suppress, a tug-of-war that sets infection outcome."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is a hub of measles immune amnesia: MV reaches splenic white pulp and infects the SLAM-high memory B and T cells massed there, depleting the antibody repertoire and leaving lasting susceptibility to other pathogens."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The measles rash is endothelial: virus-laden T cells deliver MV to dermal capillary endothelium, where infection plus the host T-cell response produces the perivascular inflammation seen as the classic maculopapular exanthem and Koplik spots."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus tampers with the inflammation switch: measles proteins modulate NF-κB signaling as part of the immune disruption that drives both the acute cytokine response and the profound immunosuppression of the infection."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Its pneumonia can drown the lungs: severe measles produces a giant-cell pneumonia that, especially in the immunocompromised, can progress to acute respiratory distress syndrome — a leading cause of measles death."
  - target: 02-pathogen/06-environmental/diarrheal-disease
    relation: connects-to
    note: "It empties the gut as well as the immune system: measles infects the intestinal lining and, compounded by immune amnesia, causes severe diarrhea that is a major cause of measles mortality in malnourished children."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Immune amnesia opens the door to deadly infection: measles erases existing immune memory and depletes lymphocytes for months, leaving children prone to secondary bacterial infections that disseminate into sepsis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Post-measles immune collapse lets mold in: the profound lymphopenia and immune amnesia after measles can permit opportunistic fungal infections like invasive aspergillosis, especially in malnourished or immunocompromised children."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "A weakened host invites the yeast: measles immunosuppression and its painful oral mucosal lesions favor oral and esophageal candidiasis, one of the opportunistic infections riding on its immune amnesia."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Damaged mucosa and lost immunity invite Staph: measles strips the airway epithelium and erases immune memory, so secondary Staphylococcus aureus pneumonia and skin infection are common, dangerous complications."
  - target: 02-pathogen/01-viruses/rotavirus
    relation: connects-to
    note: "Immune amnesia opens the gut to other infections: by wiping out immune memory, measles leaves children vulnerable for months to enteric pathogens like rotavirus, contributing to post-measles diarrheal deaths."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Erased immunity invites invasive bacteria: the prolonged immunosuppression after measles leaves children prone to severe bacterial infections, including E. coli sepsis, part of its delayed mortality."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It announces itself on the skin: measles produces the pathognomonic Koplik spots inside the cheeks followed by a confluent maculopapular rash spreading from the face downward over the body."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It attacks the airways and lungs: measles causes croup, bronchitis and a giant-cell pneumonia, and secondary bacterial pneumonia is the leading cause of measles death in children."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It inflames the gut and depletes vitamin A: measles causes stomatitis, diarrhoea and hepatitis, and it sharply lowers vitamin A, worsening outcomes, so vitamin A is given as treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can inflame the heart: myocarditis and pericarditis are uncommon but recognised complications of measles, causing chest pain, arrhythmia and rarely heart failure."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe disease threatens the kidney: profuse diarrhoea and high fever in measles cause dehydration and acute kidney injury, with rare post-infectious glomerulonephritis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches in the muscles: measles causes prominent myalgia during the febrile prodrome, and rare post-infectious myositis can follow."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Micronutrients change outcomes: WHO recommends vitamin A in measles to cut mortality and blindness, and zinc supplementation shortens the diarrhoea that frequently complicates and kills in measles."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D supports antiviral defence: deficiency is linked to more severe respiratory viral infection, and adequate status may modestly aid recovery from the respiratory complications of measles."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "A fellow vaccine-preventable exanthem: distinguishing measles from chickenpox is a classic clinical exercise, both being highly contagious viral rashes spread by the respiratory route."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "It erases immune memory: measles causes prolonged immunosuppression and tuberculin anergy, reactivating latent tuberculosis and leaving children vulnerable to it for years after recovery."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Giant-cell pneumonia attacks the alveolus: measles infects alveolar type II pneumocytes, fusing them into the multinucleated giant cells of Hecht pneumonia, a severe complication in the malnourished and immunocompromised."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Secondary bacteria invade the damaged host: post-measles immune suppression and skin breakdown predispose to group A streptococcal pneumonia, otitis and soft-tissue infection."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "It erases immune memory: measles infects and depletes memory B and T cells in lymphoid germinal centres, causing 'immune amnesia' that wipes out prior immunity and raises mortality from other infections for years."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "The disproven MMR-autism myth: a fraudulent 1998 study falsely linked the measles vaccine to autism; the claim is thoroughly debunked, but the resulting vaccine hesitancy has driven measles resurgence."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "It can persist and spread neuron to neuron: in rare subacute sclerosing panencephalitis, mutant measles virus persists in the brain and spreads trans-synaptically years after infection, causing fatal progressive neurodegeneration."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "From pathogen to cancer cure: an engineered oncolytic measles virus selectively infects and lyses myeloma cells via the CD46 receptor, a striking repurposing of a vaccine-preventable virus as cancer therapy."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Measles can inflame the heart: myocarditis is a rare complication of severe measles, viral inflammation of the myocardium that can provoke arrhythmia and transient heart failure."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Infection and the allergic airway: by transiently rewiring immunity, measles has been studied for whether it raises or lowers later asthma and allergy risk—an unresolved strand of the hygiene-hypothesis debate."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "Viruses that invade the brain: like West Nile virus, measles crosses into the CNS—causing acute encephalitis and the late, fatal SSPE—two RNA viruses illustrating neuroinvasion by different routes."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "Post-infectious neurology: measles can trigger acute disseminated encephalomyelitis and Guillain-Barré-like demyelination, immune-mediated nerve injury following the acute infection."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "An oncolytic platform: engineered measles virus that targets cancer cells (trialled in myeloma) is also studied against glioblastoma and ovarian cancer, the vaccine strain repurposed to lyse tumours."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "SSPE, years later: subacute sclerosing panencephalitis is a fatal slow measles infection of the brain emerging years after the acute illness, a demyelinating panencephalitis destroying white-matter tracts and axons."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Post-viral low platelets: measles (and rarely its vaccine) can trigger acute immune thrombocytopenia, antibody-mediated platelet destruction adding bleeding risk to the acute illness."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Measles and the heart: myocarditis is an uncommon complication of measles, inflaming the myocardium and its conduction system to cause arrhythmia during severe infection."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Cell-mediated clearance: IFN-γ from T cells is essential for clearing measles virus, and the cellular immune response it drives produces the characteristic rash as the virus is eliminated."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Acute inflammation: IL-6 rises in acute measles to drive the fever and acute-phase response, part of the cytokine surge of the systemic viral illness."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory mediator: TNF-α contributes to the systemic inflammation and tissue injury of severe measles, including its pneumonia and encephalitis complications."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: CD8 T cells use perforin and granzyme to clear measles-infected cells, the response required for recovery whose recruitment of cytotoxic immunity also mediates the rash."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune amnesia and suppression: measles induces IL-10 and depletes memory lymphocytes, producing the prolonged immunosuppression and 'immune amnesia' that leaves survivors vulnerable to other infections."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and macrophages into measles-infected tissues, contributing to the giant-cell pneumonia and the inflammatory response of the systemic infection."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 suppression: measles infection of dendritic cells suppresses IL-12 production, crippling the Th1 response and contributing to the profound, weeks-long immunosuppression that follows acute measles."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Interferon evasion: the measles V and P proteins bind and block STAT1, shutting down interferon signal transduction so the virus evades the type-I-interferon response during acute infection."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune amnesia: by infecting antigen-presenting cells via SLAM and depleting memory lymphocytes, measles erodes the MHC-class-II-restricted memory repertoire, the basis of the 'immune amnesia' that erases prior immunity."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal neutralisation: secretory IgA on the respiratory epithelium neutralises measles at its airway portal of entry, and the durable mucosal and systemic antibody induced by vaccination is what makes measles immunity so long-lasting."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Endosomal sensing: plasmacytoid dendritic cells sense measles RNA through TLR7 signalling via MyD88 to produce type-I interferon, the endosomal innate arm complementing the cytosolic RIG-I pathway the virus's V protein antagonises."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Lymphocyte depletion: measles drives caspase-3-mediated apoptosis of infected and bystander lymphocytes, the cell loss that produces the transient lymphopenia and contributes to the immune amnesia leaving children vulnerable to other infections."
---

# Measles

## Overview

**Measles** (caused by measles virus, MV; family *Paramyxoviridae*, genus *Morbillivirus*) is a **highly contagious acute viral infection** — with a basic reproduction number (R₀) of 12-18, measles is the most transmissible human pathogen. Despite the existence of a safe, inexpensive, and >97%-efficacious vaccine (MMR), measles remains a significant cause of global child mortality: WHO estimates ~128,000 measles deaths in 2021, down from ~2.6 million annually in the pre-vaccine era but reflecting dangerous resurgences linked to vaccine hesitancy and supply disruptions.

The legendary epidemiological observation by **Peter Ludwig Panum in 1846** — who investigated a measles outbreak on the Faroe Islands and documented that elderly islanders who had been infected 65 years earlier were completely protected from reinfection — established that measles confers **lifelong immunity** after natural infection. This immunity requires adequate MV-specific memory B cells and neutralizing antibodies against MV-H and MV-F. The paradox of measles immunology is that while it induces strong long-lived immunity against MV itself, it simultaneously **destroys pre-existing immunological memory** to other pathogens — the phenomenon of **immune amnesia** [^mina-2019-immune-amnesia], now understood as a consequence of SLAM/CD150-expressing memory B and T cell infection and depletion.

**Public health crisis:** Multiple high-income countries lost measles-eliminated status in 2017-2019 due to vaccine hesitancy outbreaks (United States, Europe). The 2019 DRC outbreak exceeded 300,000 cases. COVID-19 pandemic disruptions caused global routine immunization to fall to 2008 levels by 2021, setting the stage for large resurgences.

## Structure

### MV genome and proteins

Measles virus has a ~16 kb negative-sense ssRNA genome (one of the largest among Paramyxoviridae) encoding **8 proteins** from 6 genes:

| Gene | Proteins | Function |
|------|----------|----------|
| **N (nucleoprotein)** | N | Encapsidates RNA → nucleocapsid (helical symmetry); serology target (anti-N IgM, anti-N IgG) |
| **P** | P, V, C | P: L-polymerase cofactor; **V**: IFN antagonist (cysteine-rich C-terminus; binds MDA5, LGP2, STAT1/2, IRF9); **C**: Short ORF; IFN-β antagonist; required for pathogenicity |
| **M (matrix protein)** | M | Virion assembly; bridges nucleocapsid and glycoproteins |
| **F (fusion protein)** | F | Class I viral fusogen; F0 cleaved by cathepsin/furin → F1+F2; drives cell-cell fusion → syncytia |
| **H (hemagglutinin)** | H | Receptor binding; binds SLAM/CD150 (immune cells), nectin-4 (epithelium); drives H-F fusion complex; target of neutralizing antibodies |
| **L (large protein)** | L | RNA-dependent RNA polymerase (RdRp); 5′-mRNA capping, N7-methylation |

Two proteins encoded by RNA editing (P gene): **V** (V-domain from P-gene RNA edited with one G insertion; V is the primary IFN antagonist) and **C** (alternative ORF from P gene).

### MV surface glycoproteins and receptor tropism

**Receptor switching — three phases of infection:**
1. **Lymph nodes / lymphoid organs** → H binds **SLAM/CD150** (signaling lymphocytic activation molecule; CD150) on **T cells, B cells, dendritic cells, macrophages** → systemic dissemination + immune suppression
2. **Lung** → H binds **SLAM/CD150** on alveolar macrophages and DC → RSV-like bronchiolitis
3. **Airway epithelium (shedding)** → H binds **nectin-4** (PVRL4; an adherens junction protein) on polarized bronchial epithelium → amplification and respiratory transmission
4. *(Historical)* **Neurons (SSPE)** → H-independent entry via unknown receptor + MV genome accumulation

**Atypical measles:** Historical vaccine VED (killed measles vaccine, 1960s) → non-neutralizing H antibodies + Th2 skew → on wild-type MV exposure → eosinophilic pneumonitis; abandoned in 1967.

## Function

### Immune amnesia — the most important measles biology

The **immune amnesia** phenomenon was mechanistically demonstrated by Mina et al. (2019) [^mina-2019-immune-amnesia] using the VirScan platform:
1. MV-H binds SLAM/CD150 on **memory B cells** (the cells with highest CD150 expression) → infects and depletes them preferentially
2. Loss of memory B cells → loss of 11-73% of pre-existing antibody diversity (depends on MV exposure duration)
3. Surviving naive B cells cannot compensate because they lack the antigen-specific memory necessary to reconstitute protection against previously cleared pathogens
4. **Clinical consequence**: Children recovering from measles are susceptible to previously controlled infections for **2-3 years** — this re-susceptibility to other pathogens explains why measles indirectly accounts for far more child deaths than direct measles mortality

**VirScan serology:** Comparing pre- and post-measles antibody repertoires showed measles erases 20-70% of antibody diversity (median ~40% loss) — the antigen-specific antibodies lost were those the child had accumulated through years of infection and vaccination.

**SLAM/CD150 expression on memory B cells** is the key determinant: Memory B cells express ~3-10× more SLAM than naive B cells → measles specifically targets the cells encoding immunological history.

### IFN evasion — the MV V/P/C system

MV has evolved one of the most sophisticated IFN evasion systems among RNA viruses:

**V protein:**
- N-terminal CARD-like domain (shared with P): Required for polymerase activity
- C-terminal cysteine-rich V-domain (unique to V): Multifunctional IFN antagonist
  - Binds **MDA5** and **LGP2** → sequesters RNA sensors → prevents MAVS activation
  - Binds **STAT1 and STAT2** → prevents JAK-STAT phosphorylation → ISG suppression
  - Binds **IRF9** → blocks ISGF3 assembly
  - Binds **IKKα** → blocks NF-κB-driven IFN-β induction in some contexts

**P protein:**
- Larger protein sharing N-terminus with V
- Sequesters **IRF3** → blocks TBK1-mediated IRF3 phosphorylation → prevents IFN-β transcription
- Coordinates with V for full IFN suppression

**C protein:**
- Short protein from alternative ORF of P gene
- Inhibits IFN-β induction independently; acts at MAVS level
- Required for efficient viral replication in vivo; C-deleted MV is attenuated

**Attenuated vaccine strains (Edmonston, Schwarz):** Multiple passages in non-immune cells selected for mutations in V and P that reduce IFN evasion efficiency → attenuated strains activate stronger innate IFN responses → faster clearance by immune cells → vaccine attenuation.

### Immunosuppression mechanisms

Beyond immune amnesia (memory B cell depletion), MV causes acute immune suppression through:
1. **IL-12 suppression**: MV-infected DCs produce less IL-12 → impaired Th1 responses → susceptibility to TB reactivation post-measles
2. **IL-10 upregulation**: MV-infected DCs → high IL-10 → anti-inflammatory; secondary immunosuppression
3. **FasL upregulation**: MV-infected cells express FasL → Fas-FasL killing of CD4+ T cells → lymphopenia
4. **mTOR-mediated anergy**: MV → mTOR inhibition in T cells → transcriptional anergy
5. **Lymphopenia**: Absolute lymphocyte count falls 40-60% during acute measles (B and T cells both lost)

## Pathology

### Clinical course and manifestations

**Incubation:** 8-12 days (range 7-21 days) from exposure to prodrome
**Prodrome (3-4 days):** Classic **3 C's**: Cough, Coryza (runny nose), Conjunctivitis (photophobia); high fever (>40°C); **Koplik's spots** (pathognomonic): transient white salt-grain-sized spots on buccal mucosa opposite molars; appear 1-2 days before rash
**Exanthem:** **Morbilliform (maculopapular) rash** begins behind ears → spreads centrifugally to trunk/extremities (3 days); rash is caused by MV-specific CD4+ T cell attack on MV-infected dermal capillary endothelium (not direct viral cytopathology)
**Infectivity:** Begins 4 days before rash; highest during prodrome; resolves 4 days after rash onset

**Warthin-Finkeldey giant cells:** Pathognomonic multinucleated syncytia formed by H-F fusion of infected lymphoid cells; visible in lymph nodes, tonsils, appendix, and lung on histology; created by MV F protein on infected cell surfaces fusing with SLAM+ neighbor cells.

### Complications

| Complication | Incidence | Mechanism | Risk factors |
|---|---|---|---|
| **Otitis media** | 7-9% | Secondary bacterial (Streptococcus, H. influenzae) | Age <5 years |
| **Pneumonia (primary)** | ~1-6% | MV-induced interstitial pneumonitis (giant cell pneumonia); Warthin-Finkeldey cells in alveoli | Immunocompromised, malnourished |
| **Secondary pneumonia** | ~5% | Bacterial superinfection (pneumococcus, Staph) | Any age |
| **Diarrhea** | ~8% | MV intestinal epithelial infection → mucosal damage | Developing countries; contributes to measles mortality |
| **Croup** | ~1-2% | MV-induced laryngotracheitis | Young children |
| **Acute measles encephalitis (AME)** | 1/1000 | MV-specific T cell-mediated autoimmune attack on CNS (not direct MV invasion) | Any age; high mortality/morbidity |
| **ADEM (acute disseminated encephalomyelitis)** | ~1/1000 | Autoimmune demyelination post-measles; similar to AME | Any age |
| **SSPE (subacute sclerosing panencephalitis)** | ~1-2/10,000; higher in <2 year infection | Persistent MV CNS infection with hypermutated genome; decades-later fatal encephalitis | First infection <2 years old |
| **Measles inclusion body encephalitis (MIBE)** | Rare; immunocompromised | Acute MV CNS replication without immune control | Immunosuppressed |
| **Vitamin A deficiency → blindness** | ~20,000/year globally | MV → conjunctivitis + vitamin A deficiency → corneal ulceration → blindness | Developing countries |

**SSPE (Subacute Sclerosing Panencephalitis):**
- Fatal progressive neurodegenerative disease occurring 5-15 years after acute measles (range 1-27 years)
- Caused by **persistent MV infection in neurons** with defective, hypermutated viral genome (accumulation of biased hypermutation in M, F, and H genes → non-cytopathic variant cannot complete replication cycle but persists in neurons)
- **MV M gene mutations** → loss of matrix protein assembly → virus cannot bud → neuronal spread only
- **MV H gene mutations** (especially in cytoplasmic tail) → altered antigenicity; allows escape from immune clearance in CNS
- **MV F gene biased hypermutation** (A-to-I/G RNA editing) → hyperfusogenic F → enhanced cell-cell spread → syncytium-mediated neuronal loss
- Clinical stages: Stage I (behavioral change, memory loss; EEG normal) → Stage II (myoclonic seizures, deteriorating cognition; EEG: Rademecker complexes) → Stage III (decorticate rigidity, coma) → Stage IV (death); total duration 1-3 years
- **Prevention**: MMR vaccine essentially eliminates SSPE risk; avoiding measles infection in infancy is the only prevention; no effective treatment

### Diagnosis

- **Clinical**: Rash + 3 C's + Koplik's spots during endemic period; straightforward
- **Serology**: MV IgM (positive 1-2 days after rash onset; peaks day 5-14; wanes by 30-60 days); MV IgG seroconversion
- **RT-PCR**: Throat/nasopharyngeal swab, urine, blood; gold standard for confirmation and genotyping; 10 WHO genotypes (A-D, F-H, N-D)
- **Virus culture**: BSL-2; not routine clinical use
- **Notifiable disease**: Mandated reporting in all WHO member states

### Treatment and prevention

**No approved antiviral therapy for measles.** Management is supportive:
- **Vitamin A supplementation**: WHO recommends for all children with measles in developing countries (reduces mortality 50%); mechanism: vitamin A → retinoic acid → epithelial integrity + IFN-γ production + ILC3 function; reduces pneumonia severity and measles-induced vitamin A deficiency
- Fever management; hydration; antibiotics for bacterial superinfections
- Ribavirin has in vitro activity but no established clinical benefit

**Prevention — MMR vaccine:**
- Live attenuated **Edmonston lineage** strains (USA: Moraten; Europe: Schwarz, Enders) for measles; combined with attenuated rubella (Wistar RA 27/3) and mumps (Jeryl Lynn or Urabe)
- **Primary schedule**: Dose 1 at 12-15 months; Dose 2 at 4-6 years; seroconversion rate >97% after two doses
- **Coverage threshold for elimination**: >95% two-dose coverage required in all age cohorts (R₀ ~12-18 requires >91-94% herd immunity)
- **MMRV** (measles-mumps-rubella-varicella): quadrivalent; approved; slightly higher febrile seizure risk in 12-23 month age group vs. MMR + separate varicella (∼1 extra febrile seizure per 2,300-2,600 doses MMRV vs. separate vaccines)
- **Maternal measles antibody waning**: Passively transferred maternal MV-IgG wanes by 4-6 months in exclusively formula-fed infants, 9-12 months in breastfed infants → window of susceptibility before MMR at 12 months

## Connections

**→ [MV-H Protein](../../../03-molecular/mv-h-protein/)**: MV-H (hemagglutinin) binds SLAM/CD150 on immune cells for systemic spread and nectin-4 on airway epithelium for respiratory shedding; H-F fusion complex drives syncytia formation (Warthin-Finkeldey giant cells); SLAM tropism is the mechanistic basis of measles-induced immune amnesia by targeting memory B and T cells.

**→ [MAVS](../../../03-molecular/mavs/)**: MV negative-sense RNA replication generates 5′ppp RNA intermediates → RIG-I → MAVS → TBK1/IRF3 → IFN-β; MV V protein sequesters MDA5 and LGP2 → prevents MAVS activation; MV P protein blocks IRF3 phosphorylation; attenuated vaccine strains with impaired V/P activate MAVS more robustly → faster innate response.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: MV V protein binds STAT1/STAT2 → blocks JAK-STAT signaling → ISG suppression; MV C protein blocks IFN-β induction; V-domain mutations in attenuated Edmonston/Schwarz strains reduce STAT1 binding affinity → stronger type I IFN response in vaccinated individuals vs. WT MV infection → basis of vaccine attenuation.

- `connects-to` → **[Measles Virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — MV (Morbillivirus; negative-sense ssRNA; R₀ 12-18) is the causative agent; SLAM/CD150-binding H glycoprotein mediates systemic lymphoid spread; F protein drives syncytia (Warthin-Finkeldey cells); persistent MV with hypermutated genome causes SSPE.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — MV-H binds SLAM/CD150 on DCs → productive DC infection → impaired IL-12/IFN-α production and reduced T cell priming; MV-infected DCs poorly present antigens; DC dysfunction is a core driver of measles immune amnesia lasting 2-3 years.
- `connects-to` → **[Immune System](../../immune-system/README.md)** — Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects SLAM-high memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Measles erases immune memory by destroying memory B cells: these cells carry the most SLAM/CD150 (3-10× naive B cells), exactly the receptor measles H protein binds, so the virus preferentially infects and deletes them — wiping out 20-70% of a child's antibody repertoire.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — RIG-I is the front-line sensor of measles: it detects MV 5′-triphosphate RNA replication intermediates and signals through MAVS to launch type I interferon — which the virus's V and C proteins fight to suppress, a tug-of-war that sets infection outcome.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is a hub of measles immune amnesia: MV reaches splenic white pulp and infects the SLAM-high memory B and T cells massed there, depleting the antibody repertoire and leaving lasting susceptibility to other pathogens.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The measles rash is endothelial: virus-laden T cells deliver MV to dermal capillary endothelium, where infection plus the host T-cell response produces the perivascular inflammation seen as the classic maculopapular exanthem and Koplik spots.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Measles attacks the brain in several ways: acute post-infectious encephalitis and ADEM, and — years to decades later — SSPE, a fatal degeneration driven by hypermutated measles virus persisting in neurons; the MMR vaccine essentially eliminates all of these.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Measles induces a profound, lasting immunosuppression that can reactivate latent tuberculosis: measles-infected dendritic cells make less IL-12, crippling the Th1 response that contains TB — one way post-measles immune amnesia raises susceptibility to other infections for years.
- `connects-to` → **[Influenza](../influenza/README.md)** — Both are vaccine-preventable respiratory viruses but differ sharply: measles (paramyxovirus) is among the most contagious pathogens (R0 12-18) and causes immune amnesia, while influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pneumonia is the leading cause of measles death: the virus directly infects respiratory epithelium and, by erasing immune memory (immune amnesia), opens the door to secondary bacterial pneumonia for months afterward; giant-cell pneumonia can be fatal in the immunocompromised.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Measles both needs and subverts cytotoxic T cells: CD8+ T cells clear measles-infected cells and drive recovery, but the virus infects memory lymphocytes via CD150/SLAM and depletes them, causing 'immune amnesia' that erases pre-existing immunity to other pathogens for 2-3 years.
- `connects-to` → **[RSV](../rsv/README.md)** — Measles and RSV are paramyxoviruses but cause very different disease: RSV is a bronchiolitis-causing pneumovirus of infants, while measles is a contagious morbillivirus with rash, fever, and Koplik spots—both can cause severe pneumonia, the leading killer in measles.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Measles can attack neurons years after infection: persistent defective virus in the brain causes subacute sclerosing panencephalitis (SSPE), a fatal degenerative disease appearing years later—one reason measles is far more than a transient childhood rash.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Measles spreads through the body via myeloid cells: alveolar macrophages and dendritic cells in the airway are the first infected, carrying the virus to lymphoid tissue where it amplifies—so these innate sentinels become the vehicle for systemic measles dissemination.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help control measles early: NK and interferon responses limit initial viral spread, but measles still infects immune cells and causes profound, lasting immunosuppression—so the innate response is overwhelmed by a virus that targets immunity itself.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Measles is especially dangerous in HIV and immunosuppression: without competent T-cell immunity, measles can cause giant-cell pneumonia and fatal disease without the typical rash, so live measles vaccine is contraindicated in severe immunosuppression.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Measles and COVID-19 illustrate herd-immunity thresholds at opposite extremes: measles is so contagious (R0 12-18) that ~95% vaccination is needed to stop spread, far above COVID's threshold—so falling measles vaccination quickly reignites outbreaks.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The measles rash is its most recognizable sign: T-cell attack on virus-infected skin capillaries produces the spreading maculopapular eruption, preceded by Koplik spots on oral mucosa—the rash marks immune engagement, not direct skin destruction.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Measles can devastate the nervous system: acute postinfectious encephalitis strikes ~1 in 1,000 cases, and years later the relentless subacute sclerosing panencephalitis (SSPE) can emerge from persistent virus—rare but fatal reasons measles is far from benign.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Measles infection leaves lifelong IgG immunity but also 'immune amnesia': it depletes memory B and T cells, erasing antibodies to other pathogens for years, so it raises susceptibility to unrelated infections—while the vaccine protects without this harm.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Measles is lymphotropic: it enters via the SLAM (CD150) receptor on immune cells and replicates in lymph nodes, spleen, and tonsils, causing generalized lymphadenopathy and the giant cells seen in lymphoid tissue—lymphoid organs are its main amplification site.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Measles can blind through the eye: the virus causes keratoconjunctivitis, and in vitamin-A-deficient children corneal ulceration and scarring lead to blindness—so measles remains a leading cause of childhood blindness in poor settings, treated with vitamin A.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Measles depletes T cells acutely: by infecting activated lymphocytes it causes sharp lymphopenia and suppressed cell-mediated immunity during infection, which is why bacterial pneumonia—not the virus itself—causes most measles deaths.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Measles erases immune memory by killing plasma and memory cells: the virus depletes the long-lived B cells and plasma cells holding antibody memory, so survivors lose protection against other pathogens for years—'immune amnesia.'
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Measles in pregnancy is dangerous across the placenta: maternal infection raises the risk of miscarriage, prematurity and severe disease, and the virus can cross to cause congenital or neonatal measles—so vaccination before pregnancy matters.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Measles' late brain disease attacks memory circuits: SSPE (subacute sclerosing panencephalitis), a fatal years-later complication of persistent virus, progressively destroys neurons—including hippocampal memory regions—causing dementia and seizures.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Measles' biggest killer is often the gut: the virus inflames the intestinal lining, causing severe diarrhea and dehydration that, with malnutrition, account for much of measles mortality in young children.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Measles' late brain disease destroys myelin: in SSPE the persistent virus damages oligodendrocytes and white matter alongside neurons, so demyelination joins neuron loss in the relentless years-later deterioration.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Measles leaves the immune system amnesic: by infecting and depleting memory lymphocytes and inducing a regulatory, IL-10-skewed state, it erases protection against other germs for months to years, raising deaths from later infections.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Measles kills mostly by stealing oxygen: its pneumonia—whether from the virus or a bacterial superinfection—is the leading cause of measles death, flooding the lungs and dropping blood oxygen.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Measles infects the gut lining: spreading to the intestinal epithelium, it causes the diarrhea that dehydrates young children, a major contributor to measles deaths in the malnourished.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Measles can crash the platelets: the infection sometimes triggers immune thrombocytopenia, causing the bruising and bleeding of 'black measles,' a rare but dangerous hemorrhagic complication.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Measles pneumonia and its rare brain disease show on imaging: chest X-ray photons reveal the giant-cell pneumonia, and MRI maps the white-matter damage of subacute sclerosing panencephalitis.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Measles damages the alveoli: the virus forms giant cells in the air sacs (Hecht's giant-cell pneumonia), the lung injury that is a leading cause of measles death in young children.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Measles can inflame the heart: myocarditis and pericarditis are uncommon complications, adding cardiac strain to the systemic toll of a severe infection.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows measles fusing cells: the paramyxovirus drives infected cells to merge into Warthin-Finkeldey giant cells stuffed with nucleocapsids, the multinucleated hallmark seen in infected lymphoid tissue.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Diarrhea is measles' great killer: the virus strips the gut lining, and the resulting severe diarrhea and dehydration — worsened by malnutrition — are a leading cause of measles death in young children.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Measles erases immune memory: it infects and depletes the memory lymphocytes built up over a lifetime, an 'immune amnesia' that leaves children vulnerable to other infections they were once protected against for years afterward.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Measles lives and dies by antibody: the MMR vaccine and natural infection both raise protective anti-measles antibody, IgM confirms acute infection — yet the virus's immune amnesia destroys the antibody memory against other germs.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Measles can inflame the liver: a transient hepatitis with raised transaminases is common, especially in adults, one of the systemic features that make measles in grown-ups more severe than in children.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The danger of measles is what comes after: its deep, weeks-long immunosuppression opens the door to secondary bacterial pneumonia, otitis, and other infections — the complications, not the rash, that cause most measles deaths.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Measles erases immune memory: by infecting and killing memory lymphocytes and depleting the lymphoid tissue, it causes 'immune amnesia,' wiping out years of acquired protection against other pathogens long after recovery.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Measles is dangerous in pregnancy: it raises the risk of miscarriage, preterm birth, and severe maternal disease, and because the vaccine is live it cannot be given during pregnancy, leaving immunization to be timed beforehand.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — In malnourished children the gut tips the balance: measles brings vomiting and profuse diarrhea, and the resulting dehydration and worsened malnutrition are a major contributor to its mortality in low-resource settings.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Years later the virus can smolder in the brain: in subacute sclerosing panencephalitis a persistent measles strain drives chronic microglial activation and demyelination, a fatal late neurodegeneration after early-childhood infection.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Measles erases immune memory and opens the door: by depleting memory B and T cells it leaves children prey to secondary pneumococcal pneumonia and otitis, the bacterial superinfections behind much of its death toll.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The brain complications bring seizures: acute measles encephalitis and the late SSPE both injure the cortex, causing seizures — in SSPE the characteristic periodic myoclonic jerks that mark its relentless course.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus tampers with the inflammation switch: measles proteins modulate NF-κB signaling as part of the immune disruption that drives both the acute cytokine response and the profound immunosuppression of the infection.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Its pneumonia can drown the lungs: severe measles produces a giant-cell pneumonia that, especially in the immunocompromised, can progress to acute respiratory distress syndrome — a leading cause of measles death.
- `connects-to` → **[Diarrheal Disease](../../../02-pathogen/06-environmental/diarrheal-disease/README.md)** — It empties the gut as well as the immune system: measles infects the intestinal lining and, compounded by immune amnesia, causes severe diarrhea that is a major cause of measles mortality in malnourished children.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Immune amnesia opens the door to deadly infection: measles erases existing immune memory and depletes lymphocytes for months, leaving children prone to secondary bacterial infections that disseminate into sepsis.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Post-measles immune collapse lets mold in: the profound lymphopenia and immune amnesia after measles can permit opportunistic fungal infections like invasive aspergillosis, especially in malnourished or immunocompromised children.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — A weakened host invites the yeast: measles immunosuppression and its painful oral mucosal lesions favor oral and esophageal candidiasis, one of the opportunistic infections riding on its immune amnesia.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Damaged mucosa and lost immunity invite Staph: measles strips the airway epithelium and erases immune memory, so secondary Staphylococcus aureus pneumonia and skin infection are common, dangerous complications.
- `connects-to` → **[Rotavirus](../../../02-pathogen/01-viruses/rotavirus/README.md)** — Immune amnesia opens the gut to other infections: by wiping out immune memory, measles leaves children vulnerable for months to enteric pathogens like rotavirus, contributing to post-measles diarrheal deaths.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Erased immunity invites invasive bacteria: the prolonged immunosuppression after measles leaves children prone to severe bacterial infections, including E. coli sepsis, part of its delayed mortality.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It announces itself on the skin: measles produces the pathognomonic Koplik spots inside the cheeks followed by a confluent maculopapular rash spreading from the face downward over the body.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It attacks the airways and lungs: measles causes croup, bronchitis and a giant-cell pneumonia, and secondary bacterial pneumonia is the leading cause of measles death in children.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It inflames the gut and depletes vitamin A: measles causes stomatitis, diarrhoea and hepatitis, and it sharply lowers vitamin A, worsening outcomes, so vitamin A is given as treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can inflame the heart: myocarditis and pericarditis are uncommon but recognised complications of measles, causing chest pain, arrhythmia and rarely heart failure.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe disease threatens the kidney: profuse diarrhoea and high fever in measles cause dehydration and acute kidney injury, with rare post-infectious glomerulonephritis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches in the muscles: measles causes prominent myalgia during the febrile prodrome, and rare post-infectious myositis can follow.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Micronutrients change outcomes: WHO recommends vitamin A in measles to cut mortality and blindness, and zinc supplementation shortens the diarrhoea that frequently complicates and kills in measles.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D supports antiviral defence: deficiency is linked to more severe respiratory viral infection, and adequate status may modestly aid recovery from the respiratory complications of measles.
- `connects-to` → **[Varicella-zoster virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — A fellow vaccine-preventable exanthem: distinguishing measles from chickenpox is a classic clinical exercise, both being highly contagious viral rashes spread by the respiratory route.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — It erases immune memory: measles causes prolonged immunosuppression and tuberculin anergy, reactivating latent tuberculosis and leaving children vulnerable to it for years after recovery.
- `connects-to` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Giant-cell pneumonia attacks the alveolus: measles infects alveolar type II pneumocytes, fusing them into the multinucleated giant cells of Hecht pneumonia, a severe complication in the malnourished and immunocompromised.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Secondary bacteria invade the damaged host: post-measles immune suppression and skin breakdown predispose to group A streptococcal pneumonia, otitis and soft-tissue infection.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — It erases immune memory: measles infects and depletes memory B and T cells in lymphoid germinal centres, causing 'immune amnesia' that wipes out prior immunity and raises mortality from other infections for years.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — The disproven MMR-autism myth: a fraudulent 1998 study falsely linked the measles vaccine to autism; the claim is thoroughly debunked, but the resulting vaccine hesitancy has driven measles resurgence.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — It can persist and spread neuron to neuron: in rare subacute sclerosing panencephalitis, mutant measles virus persists in the brain and spreads trans-synaptically years after infection, causing fatal progressive neurodegeneration.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — From pathogen to cancer cure: an engineered oncolytic measles virus selectively infects and lyses myeloma cells via the CD46 receptor, a striking repurposing of a vaccine-preventable virus as cancer therapy.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Measles can inflame the heart: myocarditis is a rare complication of severe measles, viral inflammation of the myocardium that can provoke arrhythmia and transient heart failure.
- `connects-to` → **[Asthma](../asthma/README.md)** — Infection and the allergic airway: by transiently rewiring immunity, measles has been studied for whether it raises or lowers later asthma and allergy risk—an unresolved strand of the hygiene-hypothesis debate.
- `connects-to` → **[West Nile Virus](../west-nile-virus/README.md)** — Viruses that invade the brain: like West Nile virus, measles crosses into the CNS—causing acute encephalitis and the late, fatal SSPE—two RNA viruses illustrating neuroinvasion by different routes.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — Post-infectious neurology: measles can trigger acute disseminated encephalomyelitis and Guillain-Barré-like demyelination, immune-mediated nerve injury following the acute infection.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — An oncolytic platform: engineered measles virus that targets cancer cells (trialled in myeloma) is also studied against glioblastoma and ovarian cancer, the vaccine strain repurposed to lyse tumours.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — SSPE, years later: subacute sclerosing panencephalitis is a fatal slow measles infection of the brain emerging years after the acute illness, a demyelinating panencephalitis destroying white-matter tracts and axons.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Post-viral low platelets: measles (and rarely its vaccine) can trigger acute immune thrombocytopenia, antibody-mediated platelet destruction adding bleeding risk to the acute illness.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Measles and the heart: myocarditis is an uncommon complication of measles, inflaming the myocardium and its conduction system to cause arrhythmia during severe infection.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Cell-mediated clearance: IFN-γ from T cells is essential for clearing measles virus, and the cellular immune response it drives produces the characteristic rash as the virus is eliminated.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Acute inflammation: IL-6 rises in acute measles to drive the fever and acute-phase response, part of the cytokine surge of the systemic viral illness.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory mediator: TNF-α contributes to the systemic inflammation and tissue injury of severe measles, including its pneumonia and encephalitis complications.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic clearance: CD8 T cells use perforin and granzyme to clear measles-infected cells, the response required for recovery whose recruitment of cytotoxic immunity also mediates the rash.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune amnesia and suppression: measles induces IL-10 and depletes memory lymphocytes, producing the prolonged immunosuppression and 'immune amnesia' that leaves survivors vulnerable to other infections.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes and macrophages into measles-infected tissues, contributing to the giant-cell pneumonia and the inflammatory response of the systemic infection.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Measles infection of dendritic cells suppresses IL-12 production, crippling the Th1 response and contributing to the profound, weeks-long immunosuppression that follows acute measles and predisposes to secondary infection.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The measles V and P proteins bind and block STAT1, shutting down interferon signal transduction so the virus evades the type-I-interferon response that would otherwise restrain its replication during acute infection.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — By infecting antigen-presenting cells via the SLAM receptor and depleting memory lymphocytes, measles erodes the MHC-class-II-restricted memory repertoire—the basis of the "immune amnesia" that erases years of accumulated immunity.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Secretory IgA on the respiratory epithelium neutralizes measles at its airway portal of entry, and the durable mucosal and systemic antibody induced by vaccination is what makes measles immunity so long-lasting.
- `connects-to` → **[MyD88](../../03-molecular/myd88/README.md)** — Plasmacytoid dendritic cells sense measles RNA through TLR7 signaling via MyD88 to produce type-I interferon, the endosomal innate arm complementing the cytosolic RIG-I pathway the virus's V protein antagonizes.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Measles drives caspase-3-mediated apoptosis of infected and bystander lymphocytes, the cell loss that produces the transient lymphopenia and contributes to the immune amnesia leaving children vulnerable to other infections.

[^panum-1847-faroe-measles]: Panum PL. Observations made during the epidemic of measles on the Faroe Islands in the year 1846. *Med Classics.* 1939;3:829-886.
[^mina-2019-immune-amnesia]: Mina MJ, Kula T, Leng Y, et al. Measles virus infection diminishes preexisting antibodies that offer protection from other pathogens. *Science.* 2019;366(6465):599-606. [doi:10.1126/science.aay6485](https://doi.org/10.1126/science.aay6485) · [PubMed 31672891](https://pubmed.ncbi.nlm.nih.gov/31672891/)
[^strebel-2019-measles-lancet]: Strebel PM, Orenstein WA. Measles. *N Engl J Med.* 2019;381(4):349-357. [doi:10.1056/NEJMcp1905181](https://doi.org/10.1056/NEJMcp1905181) · [PubMed 31340710](https://pubmed.ncbi.nlm.nih.gov/31340710/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
