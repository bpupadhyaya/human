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
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "Interferon evasion: measles V and other proteins block IRF3 and the downstream interferon induction (RIG-I/MAVS already mapped), an immune-evasion mechanism that helps the virus disseminate."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppression: measles induces immunosuppressive TGF-β (with the IL-10 already mapped), part of the profound transient immunosuppression and immune amnesia that leave survivors vulnerable to other infections."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Memory-cell loss: by tipping pre-existing memory lymphocytes toward apoptosis (lowering anti-apoptotic BCL-2), measles erases prior immunological memory, the cellular basis of measles immune amnesia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon evasion: measles V and P proteins target JAK-STAT signalling to block interferon-stimulated-gene induction downstream of STAT1 and type-I interferon (both already mapped), a central immune-evasion mechanism of the virus."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement neutralisation: complement C3 opsonises measles virions and amplifies antibody-mediated neutralisation (IgG already mapped), part of the humoral protection conferred by infection and vaccination."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: measles virus activates the NLRP3 inflammasome, contributing to the inflammatory cytokine response and to the rare CNS immunopathology of subacute sclerosing panencephalitis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Measles virus modulates host PI3K-AKT signalling to support replication and influence infected-cell survival."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is engaged during measles virus replication and contributes to the cellular response to infection."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Measles virus manipulates mTOR-regulated translation to favour viral protein synthesis in infected cells."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the macrophage and dendritic-cell responses involved in the profound immune dysregulation caused by measles."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response to measles infection and its giant-cell pathology."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling contributes to the immunosuppressive milieu that underlies the prolonged immune amnesia following measles."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic nucleic-acid sensing through cGAS-STING, augmented by mitochondrial DNA from damaged cells, contributes to the innate antiviral response to measles virus."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by recruited myeloid cells amplify the inflammation of measles, relevant to its respiratory complications."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the lymphocyte survival and oxidative-stress responses relevant to the profound immune suppression and memory-cell depletion of measles."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the innate antiviral and inflammatory signaling of the immune response to measles virus."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by measles virus to support its replication and modulate infected-cell survival."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Measles virus induces and subverts host autophagy to support its replication and spread."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the host metabolic interplay of measles virus replication."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the epithelial and immune-cell responses to measles virus."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the immune response to measles virus infection."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to measles virus."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and immune responses of measles."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the airway and immune responses to measles virus."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the acute inflammatory response to measles."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the immune response and immunopathology of measles."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to measles."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Giant-cell pneumonia: measles infects and fuses respiratory epithelium into multinucleated giant cells, damaging the type II pneumocytes that make surfactant, and the resulting pneumonia is a leading cause of measles death."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response and lymphopenia: IL-2-driven T-cell expansion clears measles, but the acute infection also causes a transient lymphopenia, part of the immune disruption that leaves children vulnerable to secondary infections."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Malnutrition severity: protein-energy malnutrition, reflected in low leptin, markedly worsens measles outcomes, which is why the disease is far more lethal in undernourished children and why nutritional support is central to management."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Exanthem: the morbilliform measles rash reflects a T-cell attack on infected dermal endothelium with vasodilation and increased vascular permeability, to which histamine contributes, producing the confluent erythematous eruption spreading from the face."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Antibody help: IL-4 and type-2 T-cell help drive the B-cell (already mapped) production of the lifelong neutralising antibodies (IgG already mapped) against the H protein that mediate measles immunity and vaccine protection."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Antiviral and inflammatory nitric oxide: inducible nitric oxide contributes to antiviral defence against measles, and in excess to the tissue inflammation of severe disease, one of the innate effectors engaged by the infection."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Febrile inflammation: prostaglandins, induced by the cytokines (IL-6, TNF and IL-1 already mapped) of the measles immune response, drive the high fever and the inflammatory component of the illness and its rash."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 antibody help: IL-13, with IL-4 (already mapped), supports the B-cell (already mapped) production of the lifelong neutralising antibodies against the H protein that mediate measles immunity and vaccine protection."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and vitamin-A depletion: measles depletes vitamin A and antioxidant reserves, and the oxidative stress, to which xanthine oxidase contributes, worsens the epithelial and immune injury, a rationale for vitamin-A therapy."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and epithelial defence: zinc, with vitamin A, supports the epithelial integrity and the antiviral immunity against measles, and deficiency worsens the severity of the infection and its complications."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium antioxidant defence: selenium and its selenoproteins support the antioxidant defence (xanthine oxidase and vitamin-A depletion already mapped) against the oxidative injury of measles, and deficiency aggravates the disease."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 inflammation resolution: the omega-3 fatty acids give rise to pro-resolving mediators that limit the excessive lung (already mapped) inflammation (prostaglandins already mapped) of measles pneumonia, aiding recovery from the commonest fatal complication."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Malnutrition and immunity: adiponectin, with leptin (already mapped), links the malnutrition common in the endemic setting to the impaired immune response that determines the severity of measles."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 eosinophil arm: IL-5, with the Th2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil-associated type-2 response of the immune shift that accompanies the immunosuppression of measles."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the malnutrition-immunity axis that shapes the susceptibility to and severity of measles."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Measles exanthem: the maculopapular rash (with the Koplik spots) of the skin is the classic measles exanthem, the T-cell (already mapped) response to the infected dermal endothelium."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "SLAM target cells: the measles virus (H protein already mapped) targets the SLAM (CD150)-expressing dendritic cells and macrophages, the initial infection and lymphatic spread."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Immune-amnesia B cells: the measles depletes the memory B cells (with the memory T cells already mapped), erasing the humoral immunity to other pathogens — the 'immune amnesia'."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to the measles virus."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the measles infection."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammation iron: the IL-6-driven (already mapped) hepcidin of the acute measles inflammation contributes to the anaemia, compounded in the malnourished child."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "Causative virus: the measles virus (the H protein already mapped, binding the SLAM/nectin-4 receptors) is the causative paramyxovirus of measles."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Type-2/rash arm: the mast cells, with the type-2 (IL-4, IL-5 and IL-13 already mapped) immunity, contribute to the histamine-mediated (already mapped) vascular changes of the measles rash."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement clearance: the complement C5, with C3 (already mapped), contributes to the opsonisation and lysis of the measles virus and the immune clearance of the infection."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation of the measles infection."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active during the measles complement response, part of the complement-regulator (the CD46 receptor) interface of the measles virus."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways activated by the anti-measles antibodies (already mapped) during the immune clearance of the infection."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Immune-activation matricellular: osteopontin, a matricellular cytokine, is part of the strong pro-inflammatory immune activation of the acute measles infection."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Airway remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the airway inflammation and remodelling of the measles giant-cell pneumonia."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response to the measles infection."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-airway axis: TSLP, from airway epithelium (already mapped) damaged by measles virus, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the type-2 airway inflammation underlying the croup and the post-measles wheezing exacerbation."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-airway axis: bradykinin, via the kallikrein-kinin system activated by the measles-associated vascular endothelial (already mapped) injury, amplifies the airway oedema and the vascular permeability of the measles bronchopneumonia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Post-measles anaemia: erythropoietin drives red-cell regeneration to correct the anaemia driven by the cytokine-storm (IL-6 already mapped) and the haemophagocytic (bone-marrow already mapped) suppression of the severe measles infection."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antiviral immunity: melatonin has antiviral and immunomodulatory properties, modulating the innate antiviral type-I-interferon (already mapped) and the NLRP3-inflammasome (already mapped) responses; disrupted melatonin is seen in the febrile phase of measles."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone immune modulation: testosterone modulates the T-cell (already mapped) and NK-cell (already mapped) antiviral response; the age/sex differences in measles severity include an androgen-mediated component affecting the innate and adaptive immune defence."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stress-immune neuroendocrine: prolactin, elevated by the febrile stress of measles infection, enhances lymphocyte (T-helper-cell and B-cell already mapped) activation and the antibody (immunoglobulin-G already mapped) response against the measles virus."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Measles serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and neurons (already mapped), modulates type-I-interferon (already mapped) and NLRP3 (already mapped) antiviral responses; serotonin dysregulation amplifies the measles cytokine-storm severity."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Measles oxytocin: oxytocin, via OXTR on macrophages (already mapped) and regulatory T cells (already mapped), attenuates the cytokine-storm (already mapped) and NLRP3 (already mapped) immunopathology; oxytocin promotes immune resolution after severe measles infection."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Measles vasopressin: vasopressin, via V2 receptors on macrophages (already mapped) and neurons (already mapped), modulates fluid balance and innate immune tone; vasopressin amplifies the NLRP3 (already mapped) and IL-6 (already mapped) febrile cytokine-storm of measles."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Measles iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and NK-cell (already mapped) antiviral innate immunity; iodine deficiency impairs type-I-interferon (already mapped) and NF-κB (already mapped) antiviral signalling in measles immunopathology."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Measles sodium: sodium, via voltage-gated channels on macrophages (already mapped) and neurons (already mapped), shapes NF-κB (already mapped) innate immune activation; dysregulated sodium amplifies NLRP3 (already mapped) and IL-6 (already mapped) cytokine-storm of measles."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Measles magnesium: magnesium stabilises NLRP3 inflammasome (already mapped) and attenuates NF-κB (already mapped) cytokine-storm (already mapped) immunopathology; magnesium deficiency impairs macrophage (already mapped) and NK-cell (already mapped) antiviral immunity in measles."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Measles copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of measles."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Measles potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in macrophages (already mapped) and dendritic cells (already mapped); potassium depletion amplifies the NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of measles."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Measles phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), supports antiviral immune energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of measles."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Measles iron: iron, as cofactor of macrophage (already mapped) and NK-cell (already mapped) antiviral enzymes, supports innate immunity; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) immune cascade of measles."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Measles calcium: calcium, as second messenger in macrophages (already mapped) and T-cytotoxic cells (already mapped), coordinates antiviral signalling; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of measles."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Measles chloride: chloride regulates macrophage (already mapped) and NK-cell (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) antiviral cascade of measles."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Measles carbon: carbon as backbone of measles-virus nucleocapsid and viral glycoproteins sustains replication in lymphocytes (already mapped); carbon disruption amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of measles."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Measles hydrogen: hydrogen in redox chemistry of lymphocytes (already mapped) and macrophages (already mapped) sustains antiviral glutathione defence; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of measles."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Measles nitrogen: nitrogen in amino-acid scaffold of measles-virus nucleoproteins and host T-cell (already mapped) receptors drives adaptive immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of measles."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Measles sulfur: sulfur in cysteine residues of measles-virus fusion protein and host interferon (already mapped) sustains antiviral redox defence; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of measles."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Measles pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates antiviral immune tolerance; pd-1 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Measles glp-1: GLP-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Measles angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Measles wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates mucosal repair; wnt-beta-catenin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Measles rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) modulates antiviral immune activation; rankl excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Measles vegf: VEGF from macrophages (already mapped) and endothelial cells (already mapped) promotes pulmonary vascular permeability; vegf excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Measles fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes pulmonary ECM remodelling; fibronectin excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Measles notch: NOTCH in macrophages (already mapped) and endothelial cells (already mapped) regulates antiviral immune fate; notch dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Measles igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates antiviral metabolic repair; igf-1 excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Measles activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes antiviral fibrosis; activin-a excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Measles cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates neuroinflammatory tone; cgrp excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Measles calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates calcium tone; calcitonin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles."
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
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — Measles V and other proteins block IRF3 and the downstream interferon induction (RIG-I/MAVS already mapped), an immune-evasion mechanism that helps the virus disseminate.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Measles induces immunosuppressive TGF-β (with the IL-10 already mapped), part of the profound transient immunosuppression and immune amnesia that leave survivors vulnerable to other infections.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — By tipping pre-existing memory lymphocytes toward apoptosis (lowering anti-apoptotic BCL-2), measles erases prior immunological memory, the cellular basis of measles immune amnesia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Measles V and P proteins target JAK-STAT signaling to block interferon-stimulated-gene induction downstream of STAT1 and type-I interferon (both already mapped), a central immune-evasion mechanism of the virus.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 opsonizes measles virions and amplifies antibody-mediated neutralization (IgG already mapped), part of the humoral protection conferred by infection and vaccination.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Measles virus activates the NLRP3 inflammasome, contributing to the inflammatory cytokine response and to the rare CNS immunopathology of subacute sclerosing panencephalitis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Measles virus modulates host PI3K-AKT signaling to support replication and influence infected-cell survival.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is engaged during measles virus replication and contributes to the cellular response to infection.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Measles virus manipulates mTOR-regulated translation to favor viral protein synthesis in infected cells.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the macrophage and dendritic-cell responses involved in the profound immune dysregulation caused by measles.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response to measles infection and its giant-cell pathology.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling contributes to the immunosuppressive milieu that underlies the prolonged immune amnesia following measles.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic nucleic-acid sensing through cGAS-STING, augmented by mitochondrial DNA from damaged cells, contributes to the innate antiviral response to measles virus.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by recruited myeloid cells amplify the inflammation of measles, relevant to its respiratory complications.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the lymphocyte survival and oxidative-stress responses relevant to the profound immune suppression and memory-cell depletion of measles.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the innate antiviral and inflammatory signaling of the immune response to measles virus.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by measles virus to support its replication and modulate infected-cell survival.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Measles virus induces and subverts host autophagy to support its replication and spread.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the host metabolic interplay of measles virus replication.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the epithelial and immune-cell responses to measles virus.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the immune response to measles virus infection.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to measles virus.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and immune responses of measles.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the airway and immune responses to measles virus.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the acute inflammatory response to measles.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the immune response and immunopathology of measles.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to measles.
- `connects-to` → **[Surfactant](../../03-molecular/surfactant/README.md)** — Giant-cell pneumonia: measles infects and fuses respiratory epithelium into multinucleated giant cells, damaging the type II pneumocytes that make surfactant, and the resulting pneumonia is a leading cause of measles death.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response and lymphopenia: IL-2-driven T-cell expansion clears measles, but the acute infection also causes a transient lymphopenia, part of the immune disruption that leaves children vulnerable to secondary infections.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Malnutrition severity: protein-energy malnutrition, reflected in low leptin, markedly worsens measles outcomes, which is why the disease is far more lethal in undernourished children and why nutritional support is central to management.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Exanthem: the morbilliform measles rash reflects a T-cell attack on infected dermal endothelium with vasodilation and increased vascular permeability, to which histamine contributes, producing the confluent erythematous eruption spreading from the face.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Antibody help: IL-4 and type-2 T-cell help drive the B-cell (already mapped) production of the lifelong neutralising antibodies (IgG already mapped) against the H protein that mediate measles immunity and vaccine protection.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Antiviral and inflammatory nitric oxide: inducible nitric oxide contributes to antiviral defence against measles, and in excess to the tissue inflammation of severe disease, one of the innate effectors engaged by the infection.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Febrile inflammation: prostaglandins, induced by the cytokines (IL-6, TNF and IL-1 already mapped) of the measles immune response, drive the high fever and the inflammatory component of the illness and its rash.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 antibody help: IL-13, with IL-4 (already mapped), supports the B-cell (already mapped) production of the lifelong neutralising antibodies against the H protein that mediate measles immunity and vaccine protection.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and vitamin-A depletion: measles depletes vitamin A and antioxidant reserves, and the oxidative stress, to which xanthine oxidase contributes, worsens the epithelial and immune injury, a rationale for vitamin-A therapy.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and epithelial defence: zinc, with vitamin A, supports the epithelial integrity and the antiviral immunity against measles, and deficiency worsens the severity of the infection and its complications.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium antioxidant defence: selenium and its selenoproteins support the antioxidant defence (xanthine oxidase and vitamin-A depletion already mapped) against the oxidative injury of measles, and deficiency aggravates the disease.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 inflammation resolution: the omega-3 fatty acids give rise to pro-resolving mediators that limit the excessive lung (already mapped) inflammation (prostaglandins already mapped) of measles pneumonia, aiding recovery from the commonest fatal complication.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Malnutrition and immunity: adiponectin, with leptin (already mapped), links the malnutrition common in the endemic setting to the impaired immune response that determines the severity of measles.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 eosinophil arm: IL-5, with the Th2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil-associated type-2 response of the immune shift that accompanies the immunosuppression of measles.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the malnutrition-immunity axis that shapes the susceptibility to and severity of measles.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Measles exanthem: the maculopapular rash (with the Koplik spots) of the skin is the classic measles exanthem, the T-cell (already mapped) response to the infected dermal endothelium.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — SLAM target cells: the measles virus (H protein already mapped) targets the SLAM (CD150)-expressing dendritic cells and macrophages, the initial infection and lymphatic spread.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Immune-amnesia B cells: the measles depletes the memory B cells (with the memory T cells already mapped), erasing the humoral immunity to other pathogens — the 'immune amnesia'.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to the measles virus.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the measles infection.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammation iron: the IL-6-driven (already mapped) hepcidin of the acute measles inflammation contributes to the anaemia, compounded in the malnourished child.
- `connects-to` → **[Measles virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — Causative virus: the measles virus (the H protein already mapped, binding the SLAM/nectin-4 receptors) is the causative paramyxovirus of measles.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Type-2/rash arm: the mast cells, with the type-2 (IL-4, IL-5 and IL-13 already mapped) immunity, contribute to the histamine-mediated (already mapped) vascular changes of the measles rash.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement clearance: the complement C5, with C3 (already mapped), contributes to the opsonisation and lysis of the measles virus and the immune clearance of the infection.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid inflammation of the measles infection.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active during the measles complement response, part of the complement-regulator (the CD46 receptor) interface of the measles virus.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways activated by the anti-measles antibodies (already mapped) during the immune clearance of the infection.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Immune-activation matricellular: osteopontin, a matricellular cytokine, is part of the strong pro-inflammatory immune activation of the acute measles infection.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Airway remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the airway inflammation and remodelling of the measles giant-cell pneumonia.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Acute-phase iron: transferrin, the iron carrier, reflects the hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response to the measles infection.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-airway axis: TSLP, from airway epithelium (already mapped) damaged by measles virus, primes dendritic cells (already mapped) and mast cells (already mapped) and amplifies the type-2 airway inflammation underlying the croup and the post-measles wheezing exacerbation.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-airway axis: bradykinin, via the kallikrein-kinin system activated by the measles-associated vascular endothelial (already mapped) injury, amplifies the airway oedema and the vascular permeability of the measles bronchopneumonia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Post-measles anaemia: erythropoietin drives red-cell regeneration to correct the anaemia driven by the cytokine-storm (IL-6 already mapped) and the haemophagocytic (bone-marrow already mapped) suppression of the severe measles infection.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antiviral immunity: melatonin has antiviral and immunomodulatory properties, modulating the innate antiviral type-I-interferon (already mapped) and the NLRP3-inflammasome (already mapped) responses; disrupted melatonin is seen in the febrile phase of measles.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone immune modulation: testosterone modulates the T-cell (already mapped) and NK-cell (already mapped) antiviral response; the age/sex differences in measles severity include an androgen-mediated component affecting the innate and adaptive immune defence.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stress-immune neuroendocrine: prolactin, elevated by the febrile stress of measles infection, enhances lymphocyte (T-helper-cell and B-cell already mapped) activation and the antibody (immunoglobulin-G already mapped) response against the measles virus.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Antiviral immune modulator: serotonin, via 5-HT receptors on macrophages (already mapped) and neurons (already mapped), modulates type-I-interferon (already mapped) and NLRP3 (already mapped) antiviral responses; serotonin dysregulation amplifies the measles cytokine-storm severity.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Immune-resolution neuropeptide: oxytocin, via OXTR on macrophages (already mapped) and regulatory T cells (already mapped), attenuates the cytokine-storm (already mapped) and NLRP3 (already mapped) immunopathology; oxytocin promotes immune resolution after severe measles infection.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Febrile fluid-immune axis: vasopressin, via V2 receptors on macrophages (already mapped) and neurons (already mapped), modulates fluid balance and innate immune tone; vasopressin amplifies the NLRP3 (already mapped) and IL-6 (already mapped) febrile cytokine-storm of measles.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Measles iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and NK-cell (already mapped) antiviral innate immunity; iodine deficiency impairs type-I-interferon (already mapped) and NF-κB (already mapped) antiviral signalling in measles immunopathology.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Measles sodium: sodium, via voltage-gated channels on macrophages (already mapped) and neurons (already mapped), shapes NF-κB (already mapped) innate immune activation; dysregulated sodium amplifies NLRP3 (already mapped) and IL-6 (already mapped) cytokine-storm of measles.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Measles magnesium: magnesium stabilises NLRP3 inflammasome (already mapped) and attenuates NF-κB (already mapped) cytokine-storm (already mapped) immunopathology; magnesium deficiency impairs macrophage (already mapped) and NK-cell (already mapped) antiviral immunity in measles.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Measles copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of measles.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Measles potassium: potassium efflux activates NLRP3 inflammasome (already mapped) in macrophages (already mapped) and dendritic cells (already mapped); potassium depletion amplifies the NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of measles.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Measles phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic cells (already mapped), supports antiviral immune energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of measles.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Measles iron: iron, as cofactor of macrophage (already mapped) and NK-cell (already mapped) antiviral enzymes, supports innate immunity; iron deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) immune cascade of measles.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Measles calcium: calcium, as second messenger in macrophages (already mapped) and T-cytotoxic cells (already mapped), coordinates antiviral signalling; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cytokine cascade of measles.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Measles chloride: chloride regulates macrophage (already mapped) and NK-cell (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) antiviral cascade of measles.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Measles carbon: carbon as backbone of measles-virus nucleocapsid and viral glycoproteins sustains replication in lymphocytes (already mapped); carbon disruption amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of measles.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Measles hydrogen: hydrogen in redox chemistry of lymphocytes (already mapped) and macrophages (already mapped) sustains antiviral glutathione defence; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of measles.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Measles nitrogen: nitrogen in amino-acid scaffold of measles-virus nucleoproteins and host T-cell (already mapped) receptors drives adaptive immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of measles.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Measles sulfur: sulfur in cysteine residues of measles-virus fusion protein and host interferon (already mapped) sustains antiviral redox defence; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of measles.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Measles pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates antiviral immune tolerance; pd-1 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Measles glp-1: GLP-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Measles angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Measles wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates mucosal repair; wnt-beta-catenin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Measles rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) modulates antiviral immune activation; rankl excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Measles vegf: VEGF from macrophages (already mapped) and endothelial cells (already mapped) promotes pulmonary vascular permeability; vegf excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Measles fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes pulmonary ECM remodelling; fibronectin excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Measles notch: NOTCH in macrophages (already mapped) and endothelial cells (already mapped) regulates antiviral immune fate; notch dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Measles igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates antiviral metabolic repair; igf-1 excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Measles activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes antiviral fibrosis; activin-a excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Measles cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates neuroinflammatory tone; cgrp excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Measles calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates calcium tone; calcitonin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and type-i-interferon (already mapped) cascade of measles.

[^panum-1847-faroe-measles]: Panum PL. Observations made during the epidemic of measles on the Faroe Islands in the year 1846. *Med Classics.* 1939;3:829-886.
[^mina-2019-immune-amnesia]: Mina MJ, Kula T, Leng Y, et al. Measles virus infection diminishes preexisting antibodies that offer protection from other pathogens. *Science.* 2019;366(6465):599-606. [doi:10.1126/science.aay6485](https://doi.org/10.1126/science.aay6485) · [PubMed 31672891](https://pubmed.ncbi.nlm.nih.gov/31672891/)
[^strebel-2019-measles-lancet]: Strebel PM, Orenstein WA. Measles. *N Engl J Med.* 2019;381(4):349-357. [doi:10.1056/NEJMcp1905181](https://doi.org/10.1056/NEJMcp1905181) · [PubMed 31340710](https://pubmed.ncbi.nlm.nih.gov/31340710/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
