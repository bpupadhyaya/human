---
schema: human-scale-entry/v1
id: cystic-fibrosis
name: Cystic Fibrosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Cystic fibrosis is caused by biallelic CFTR mutations; defective chloride and bicarbonate transport → viscous mucus → progressive bronchiectasis, chronic Pseudomonas infection, and exocrine pancreatic insufficiency; median survival >40 years with CFTR modulator therapy."
aliases: ["cystic fibrosis", "CF", "CFTR disease", "CF lung disease", "CF bronchiectasis", "CF pancreatic insufficiency", "CF-related diabetes", "CFTR mutation disease", "mucoviscidosis", "cystic fibrosis Trikafta"]
sources:
  - id: riordan-1989-cftr-cloning
    type: peer-reviewed
    cite: "Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. Science. 1989;245(4922):1066-1073."
    doi: "10.1126/science.2475911"
    pmid: "2475911"
    url: "https://doi.org/10.1126/science.2475911"
  - id: heijerman-2019-etd-cf
    type: peer-reviewed
    cite: "Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation. Lancet. 2019;394(10212):1940-1948."
    doi: "10.1016/S0140-6736(19)32597-8"
    pmid: "31679946"
    url: "https://doi.org/10.1016/S0140-6736(19)32597-8"
cross_links:
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients."
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CF airway dominated by massive neutrophil recruitment (IL-8-driven); neutrophil elastase → proteolysis → bronchiectasis; NETs provide extracellular DNA that increases sputum viscoelasticity; dornase alfa (DNase I) cleaves NET-derived DNA → improved mucus clearance."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "NLRP3 inflammasome activation in CF airway → IL-1β/IL-18 release → amplifies airway inflammation; CFTR LOF → oxidative stress → NLRP3 priming; IL-1β drives CXCL8 production by airway epithelium → neutrophil recruitment loop; canakinumab (anti-IL-1β) explored as CF lung adjunct."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "CFTR mutations (5T, R117H) are second-hit modifiers in hereditary pancreatitis (PRSS1/SPINK1 mutations); compound heterozygosity → idiopathic chronic pancreatitis; CFTR LOF → reduced pancreatic duct bicarbonate → trypsinogen aggregation and premature activation → acinar injury."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Cystic fibrosis is at root a chloride-transport disease: CFTR is an apical chloride channel, so its loss leaves epithelia unable to move chloride and water, dehydrating secretions into thick mucus — and the same defect raises sweat chloride above 60 mmol/L, the diagnostic test."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung carries most of cystic fibrosis's morbidity: dehydrated mucus cripples mucociliary clearance, inviting chronic Pseudomonas and Staph infection and neutrophilic inflammation that scars airways into bronchiectasis — historically the leading cause of CF death."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Staphylococcus aureus is typically the first chronic airway colonizer in cystic fibrosis, dominating childhood before Pseudomonas takes over in adolescence; persistent S. aureus feeds the neutrophilic inflammation that drives early bronchiectasis."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is a major target of cystic fibrosis: thick CFTR-deficient secretions plug pancreatic ducts → autodigestion and fibrosis → exocrine insufficiency (malabsorption, steatorrhea needing enzyme replacement) and, as islets are destroyed, CF-related diabetes."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Cystic fibrosis and COPD are both chronic obstructive, neutrophil-driven airway diseases with mucus plugging and infective exacerbations, but differ in cause: CF is a monogenic CFTR channel defect from birth, COPD an acquired (usually smoking-driven) disease of later life."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Cystic fibrosis-related diabetes is the commonest CF comorbidity in adults: progressive destruction of pancreatic islets by the same ductal disease that causes exocrine failure produces an insulin-deficient diabetes distinct from type 1 and type 2, worsening lung function."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The respiratory system bears the lethal burden of cystic fibrosis: defective CFTR chloride transport thickens airway mucus, causing impaired clearance, chronic infection, bronchiectasis, and respiratory failure—the leading cause of death, now eased by CFTR modulators."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Cystic fibrosis disrupts the entire digestive system: thick secretions block pancreatic ducts causing exocrine insufficiency and malabsorption, plug the bowel as meconium ileus in newborns, and thicken bile—so enzyme replacement and nutrition are central to CF care."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cystic fibrosis usually causes male infertility: nearly all men with CF have congenital bilateral absence of the vas deferens from CFTR dysfunction, so they are azoospermic despite normal sperm production—and isolated CBAVD can be the only sign of mild CFTR mutations."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium transport is deranged in cystic fibrosis: defective CFTR not only blocks chloride exit but unleashes excess sodium and water absorption, dehydrating airway mucus—and the resulting high sweat sodium chloride is the basis of the diagnostic sweat test."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Aspergillus colonizes the cystic fibrosis airway: the thick mucus lets Aspergillus fumigatus grow, and the hypersensitivity response (ABPA) causes wheezing, mucus plugging and lung decline—so CF care monitors for and treats this fungal complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a CF target organ: thick bile from defective CFTR blocks small bile ducts, causing focal biliary cirrhosis and, in some, progressive CF liver disease with portal hypertension—a leading non-pulmonary cause of death in cystic fibrosis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Cystic fibrosis obstructs the small intestine with thick secretions: newborns can present with meconium ileus, and older patients suffer distal intestinal obstruction syndrome, while impaired pancreatic enzyme flow causes the fat malabsorption central to CF."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "CF-related diabetes is a common endocrine complication: thick secretions scar the pancreas and destroy insulin-producing islets, so a distinct form of diabetes emerges with age—now a leading comorbidity as CF patients live longer."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Cystic fibrosis weakens bone: malabsorption of vitamin D and calcium, chronic inflammation, steroids and delayed puberty cause CF-related low bone density, so fractures and osteoporosis are an increasingly important problem in the aging CF population."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Cystic fibrosis is named for the scarring it causes: thick secretions and chronic inflammation replace pancreatic and lung tissue with fibrosis and cysts, so progressive fibrotic destruction—not the gene defect alone—drives organ failure."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "CF cripples the lung's macrophages: the CFTR defect impairs how macrophages acidify phagosomes and kill bacteria, so weakened innate immunity lets Pseudomonas and other microbes establish the chronic infection central to CF lung disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CF lung disease is a self-damaging immune cycle: impaired clearance invites chronic bacterial infection that draws relentless neutrophilic inflammation, whose enzymes destroy airways more than the microbes do—so anti-inflammatory strategies complement antibiotics."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Cystic fibrosis starves the body of vitamin D: pancreatic insufficiency blocks absorption of fat-soluble vitamins, so CF patients run low on vitamin D and need high-dose supplements to fend off the bone disease that shadows the illness."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Cystic fibrosis breeds its own diabetes through insulin loss: scarring of the pancreas destroys insulin-producing islet cells, causing CF-related diabetes—a distinct form, neither type 1 nor type 2, that worsens lung decline and needs insulin."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Treating cystic fibrosis can deplete magnesium: the IV aminoglycosides used against Pseudomonas waste magnesium through the kidney, and malabsorption adds to it, so low magnesium is a recurring complication to monitor and replace."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Cystic fibrosis lungs over-inflame through NF-kB: the defective CFTR channel primes airway cells to ramp up this inflammatory switch, so even modest infection triggers a damaging neutrophil flood, driving the relentless lung destruction."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-helper cells skew the cystic fibrosis airway toward harm: a Th17- and Th2-tilted response amplifies inflammation against chronic Pseudomonas and fungi rather than clearing them, adding adaptive immunity to the neutrophilic damage."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Cystic fibrosis ends as an oxygen problem: thick mucus, infection and scarring wreck gas exchange, so chronic low oxygen drives pulmonary hypertension and cor pulmonale, the respiratory failure that defines advanced disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Cystic fibrosis is also a bicarbonate problem: the CFTR channel normally exports bicarbonate, so its loss leaves secretions acidic, thickening mucus and crippling pancreatic enzymes—an acid-base angle beyond the chloride defect."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Cystic fibrosis can block the bowel: thick secretions cause meconium ileus in newborns and distal intestinal obstruction syndrome later, plugging the large intestine in ways that mimic appendicitis or obstruction."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cystic fibrosis scars its organs through fibroblasts: chronic inflammation activates them to lay down the fibrosis that destroys the pancreas (giving the disease its name) and stiffens the lungs."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "CF lungs are tracked by imaging: chest CT photons reveal the bronchiectasis—dilated, mucus-filled airways—and plugging that map the progressive lung destruction long before lung function fails."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CF is diagnosed through the skin: defective CFTR can't reabsorb chloride in sweat glands, so the sweat is salty—the basis of the sweat-chloride test and the 'salty kiss' parents notice."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "CFTR lines the gut: without it the intestinal epithelium can't hydrate its secretions, so thick mucus causes meconium ileus, malabsorption and obstruction throughout the bowel."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the failed mucociliary escalator: with CFTR's chloride channel broken, the airway surface dehydrates, the protective fluid layer collapses, and the cilia flatten under thick, immovable mucus."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Decades of lung disease overload the right heart: chronic low oxygen raises pulmonary pressures until the right ventricle fails into cor pulmonale, a common terminal pathway in advanced cystic fibrosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney bears the cost of treatment: lifelong courses of aminoglycoside antibiotics for lung infections are nephrotoxic, and dehydration and stones add to the renal risk these patients carry."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "CF unsettles the upper gut: reflux is near-universal as cough and physiotherapy push acid up, and thickened secretions slow the stomach, while lower down the same mucus jams the bowel into distal intestinal obstruction syndrome."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An allergic antibody storm complicates CF lungs: allergic bronchopulmonary aspergillosis, an IgE- and IgG-driven hypersensitivity to the Aspergillus colonizing the airways, worsens wheeze and lung damage and is treated with steroids and antifungals."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "CF quietly lowers the red cells: chronic infection's anemia of inflammation, malabsorption of iron and vitamins, and GI blood loss combine to leave many patients anemic despite their other reserves."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "CF liver disease can enlarge the spleen: thick bile scars the liver into focal biliary cirrhosis, and the resulting portal hypertension swells the spleen and drops platelet and white-cell counts through hypersplenism, a serious extrapulmonary complication."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "CF thins bone from the cellular level up: chronic inflammation, vitamin D and K malabsorption, and steroid use tip the balance toward osteoclast bone resorption, producing the early osteopenia and fracture risk of CF bone disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron fuels the airway invaders: the CF lung's mucus is iron-rich, and Pseudomonas exploits that iron to build the biofilms that entrench chronic infection, making iron acquisition both a bacterial strategy and a potential treatment target."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "CF carries its own diabetes: scarring of the pancreas destroys the insulin-making islets, producing CF-related diabetes — an insulin-deficient disease like type 1 that becomes common as patients live longer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "The CF airway runs hot with IL-6: persistent neutrophilic infection drives high IL-6 and other cytokines, the chronic inflammation that progressively destroys the lung even between exacerbations."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Immune sensing goes awry in the CF lung: dysregulated dendritic cells fail to resolve infection and instead help sustain the damaging inflammation, part of why the CF airway cannot clear its chronic colonizers."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17 arm recruits the destructive neutrophils: IL-17A is elevated in CF airways and drives the neutrophil influx and mucin production that wreck the lung, making the IL-17 axis a candidate anti-inflammatory target."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Infection can break out of the lung: severe exacerbations and Burkholderia cepacia 'cepacia syndrome,' along with long-term indwelling venous catheters, expose CF patients to bloodstream infection and sepsis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Allergy compounds the CF airway: mast cells drive the allergic bronchopulmonary aspergillosis and airway hyper-reactivity that often complicate cystic fibrosis on top of its chronic bacterial infection."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "CFTR is also a gut tumor suppressor: people with cystic fibrosis face a markedly raised colorectal cancer risk that rises further after lung transplant, so earlier and more frequent colonoscopy screening is now recommended."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "End-stage lungs back up onto the heart: chronic hypoxia and destroyed pulmonary vasculature in advanced CF raise pulmonary artery pressure into cor pulmonale, a marker of severe disease and transplant need."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Neutrophilic airway inflammation funnels through STAT3: IL-6 and IL-17 in the chronically infected CF lung drive STAT3 signaling that sustains the relentless inflammation damaging the airways."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Lifelong aminoglycosides scar the kidney: the repeated courses of nephrotoxic aminoglycosides for chronic Pseudomonas infection, plus dehydration from salt loss, leave many CF patients with chronic kidney disease."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Chronic pancreatic damage raises the cancer risk: the recurrent pancreatic inflammation and duct injury of CF are associated with an elevated risk of pancreatic and other digestive-tract cancers in adults."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A demanding lifelong illness weighs on mood: the daily treatment burden, recurrent infections and shortened life expectancy of CF carry high rates of depression and anxiety, now routinely screened for."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its indwelling lines clot the veins: the long-term central venous catheters and ports CF patients need for repeated IV antibiotics, plus chronic inflammation, raise the risk of venous thromboembolism."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Its liver disease can scar toward cancer: CF-related liver disease causes biliary cirrhosis in a subset of patients, and the resulting cirrhosis carries a risk of hepatocellular carcinoma."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A relentless treatment burden breeds worry: the constant therapies, fear of infection and uncertain prognosis of CF drive anxiety alongside depression, now part of routine mental-health screening."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its sweat is salty by defect: defective CFTR in sweat glands fails to reabsorb chloride, giving the salt-losing skin the sweat-chloride test diagnoses and a risk of salt depletion in the heat."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Chronic lung disease strains the right heart: the progressive hypoxaemia and pulmonary hypertension of advanced CF overload the right ventricle into cor pulmonale and right heart failure."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It weakens bone and inflames joints: malabsorption and chronic inflammation cause CF-related low bone density and fractures, and an episodic CF arthropathy with finger clubbing accompanies the disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Fat malabsorption starves the nerves: deficiency of fat-soluble vitamin E can cause peripheral neuropathy and ataxia, and the aminoglycosides used for infections add ototoxicity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic lung disease overloads the right heart: progressive CF lung disease raises pulmonary pressures, leading to pulmonary hypertension and cor pulmonale with right heart failure."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Salt loss and antibiotics tax the kidney: heavy sweat salt loss can cause a pseudo-Bartter syndrome with hypochloraemic alkalosis, and repeated aminoglycoside courses are nephrotoxic."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Mycobacteria threaten the CF lung: non-tuberculous mycobacteria related to M. tuberculosis, such as M. abscessus, are emerging chronic infections in cystic fibrosis that can complicate transplant."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: connects-to
    note: "Lifelong antibiotics disturb the gut: the heavy, repeated antibiotic courses for CF lung infections raise the risk of Clostridioides difficile colitis."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Fat malabsorption drains nutrients: pancreatic insufficiency in CF impairs absorption of fat-soluble vitamins and zinc, contributing to poor growth and weakened immunity."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: connects-to
    note: "MRSA now haunts the CF airway: methicillin-resistant Staphylococcus aureus is an increasingly common chronic coloniser of cystic-fibrosis lungs, treated with vancomycin and linked to faster lung-function decline."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: connects-to
    note: "Early antibiotics guard young lungs: anti-staphylococcal antibiotics are used from infancy in cystic fibrosis to treat and sometimes prevent the Staphylococcus aureus infections that begin the cycle of airway damage."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Allergic airway disease overlaps it: many people with cystic fibrosis have coexisting asthma and allergic bronchopulmonary aspergillosis, adding reversible airway obstruction to their fixed disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "CFTR modulators transformed it: small-molecule correctors and potentiators — culminating in elexacaftor-tezacaftor-ivacaftor (Trikafta) — restore mutant CFTR function and dramatically improve lung function and survival in cystic fibrosis."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It destroys the airways: thick CFTR-deficient mucus plugs the bronchi, breeding chronic Pseudomonas and Staphylococcus infection that scar the lung into bronchiectasis — the airway destruction that drives most CF mortality."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "It destroys the islets too: progressive pancreatic fibrosis and fatty replacement damage the islets of Langerhans, causing cystic-fibrosis-related diabetes — the commonest CF comorbidity, with features of both type 1 and type 2."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "CF liver disease: thick bile from CFTR loss in cholangiocytes obstructs the bile ductules of the hepatic lobule, causing focal biliary cirrhosis and portal hypertension—a leading non-pulmonary cause of death."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Anaemia of chronic infection: persistent airway infection and inflammation in CF raise hepcidin and blunt erythropoiesis, causing an anaemia of chronic disease despite adequate iron stores."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "CF bone disease: malabsorption of vitamin D and calcium, chronic inflammation and steroids thin cortical bone, causing the early osteoporosis and fractures common in CF adults."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Allergic and invasive fungus: Aspergillus fumigatus colonises CF airways, causing allergic bronchopulmonary aspergillosis (ABPA) that worsens airflow and accelerates lung decline."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Viral exacerbations: respiratory viruses like influenza and RSV trigger severe pulmonary exacerbations in cystic fibrosis, accelerating lung decline and predisposing to bacterial superinfection."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Mucus plugging reaches the air sacs: as CF lung disease advances, thick secretions and chronic infection extend into the small airways and alveoli, driving the respiratory failure that ends the disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Self-sustaining inflammation: TNF-α amplifies the relentless neutrophilic airway inflammation of cystic fibrosis, joining IL-1β, IL-6 and IL-17 in the cytokine loop that destroys lung tissue."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Cystic fibrosis liver disease: defective CFTR in biliary epithelium plugs bile ducts and causes focal biliary cirrhosis, injuring hepatocytes and progressing to portal hypertension."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Compromised host defence: chronic inflammation and proteases degrade and inactivate pulmonary surfactant in cystic fibrosis, weakening innate immune defence and small-airway stability."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Inflammatory cell recruitment: CCL2 draws monocytes into cystic-fibrosis airways, adding to the relentless neutrophil-dominated inflammation that destroys the lung."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Mucus-plug hypoxia: thick mucus and Pseudomonas biofilms create steep oxygen gradients in cystic-fibrosis airways, stabilising HIF-1α in epithelial and immune cells."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bronchial angiogenesis: chronic inflammation in cystic fibrosis raises VEGF, expanding tortuous bronchial vessels that are the source of the life-threatening haemoptysis of advanced disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil alarmin: S100A8/A9 from the neutrophils flooding cystic-fibrosis airways amplifies inflammation, and sputum calprotectin tracks the burden of airway disease and exacerbations."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Misfolded-CFTR proteostasis: the ΔF508 CFTR mutant is cleared by autophagy and ERAD, and impaired autophagy in cystic fibrosis lets the misfolded protein and aggregates accumulate, worsening inflammation."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "CF bone disease: chronic inflammation, malabsorption and corticosteroid use drive RANKL-mediated bone resorption, causing the osteoporosis and fractures common in adults with cystic fibrosis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Pseudomonas sensing: TLR4 recognition of the lipopolysaccharide of chronically colonising Pseudomonas drives the relentless NF-κB-mediated neutrophilic airway inflammation that destroys the cystic-fibrosis lung."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Mucin overproduction: EGFR signalling in the CF airway drives goblet-cell metaplasia and MUC5AC mucin secretion that compounds the dehydrated, viscous mucus already caused by defective CFTR chloride transport."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Reduced airway NO: cystic-fibrosis airways paradoxically show low nitric oxide, impairing ciliary function and antimicrobial defence and contributing to the susceptibility to chronic bacterial infection."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal defence: the dehydrated, viscous airway surface liquid of cystic fibrosis impairs mucociliary clearance and the function of secretory IgA, weakening the first-line mucosal barrier and helping the chronic Pseudomonas and Staphylococcus infections take hold."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative airway injury: the massive neutrophil infiltrate of the cystic-fibrosis airway, with xanthine-oxidase activity, generates reactive oxygen species that damage the epithelium, compounding the oxidative stress worsened by depleted antioxidant glutathione."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Failed inflammation resolution: airway neutrophils in cystic fibrosis show delayed caspase-3-mediated apoptosis, so they persist and necrose rather than being cleared, perpetuating the self-amplifying inflammation that destroys the lung."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative imbalance: CFTR dysfunction impairs NRF2-driven antioxidant defence and glutathione transport, so oxidant stress goes unchecked and amplifies the airway inflammation that drives cystic-fibrosis lung damage."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Failed regulation: relative deficiency of the anti-inflammatory cytokine IL-10 in the cystic-fibrosis airway removes a brake on neutrophilic inflammation, contributing to the exaggerated, self-perpetuating immune response."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Infection-driven complement: chronic Pseudomonas colonisation in cystic fibrosis activates complement (C3) and generates immune complexes, and the resulting complement-mediated injury accelerates the progressive bronchiectasis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Neutrophilic airway inflammation: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped), driven by chronic Pseudomonas and Staphylococcus infection, sustains the destructive neutrophilic inflammation of the cystic-fibrosis lung."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Autophagy and CFTR clearance: mTOR-regulated autophagy (autophagy already mapped) governs the handling of misfolded ΔF508-CFTR, and its modulation is explored to rescue mutant CFTR trafficking in cystic fibrosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine amplification: IL-6 and inflammatory-cytokine signalling through JAK-STAT3 (IL-6 and STAT3 already mapped) amplifies the chronic airway inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) is dysregulated in CFTR-deficient epithelia and shapes the inflammatory and autophagy responses of cystic fibrosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EGFR-ERK-MAPK signalling (EGFR mapped) drives the mucin hypersecretion and airway epithelial remodelling of cystic fibrosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the neutrophil-dominated airway inflammation characteristic of cystic fibrosis lung disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies the antiviral and antibacterial response that shapes the recurrent infections of cystic fibrosis lung disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA from neutrophil extracellular traps and bacteria in the cystic-fibrosis airway engages cGAS-STING, amplifying the chronic airway inflammation."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGFB1 a recognised modifier of cystic-fibrosis severity) drives the airway and pancreatic fibrosis of cystic fibrosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the airway epithelial oxidative-stress defense and immune-metabolic balance perturbed in the chronic infection of cystic fibrosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven hyperinflammation of the cystic-fibrosis airway."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic activity by CD8 T and NK cells contributes to the immune-mediated tissue damage of the chronically infected cystic-fibrosis airway."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the airway epithelial and neutrophilic inflammatory responses of cystic fibrosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling interacts with the CFTR channel and the autophagic responses (CFTR and autophagy already mapped) dysregulated in cystic fibrosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the airway inflammatory and epithelial responses of cystic fibrosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the chronic neutrophilic airway inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic modulation of the inflammatory responses in cystic fibrosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement C5a-driven inflammation contributes to the neutrophilic airway inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking of the chronic neutrophilic inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of cystic fibrosis."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen deposition contributes to the airway remodeling and fibrosis of chronic cystic-fibrosis lung disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway-epithelial and immune gene programs of cystic fibrosis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the airway T-cell inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the airway-surface-liquid regulation and inflammation of cystic fibrosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Salt-wasting alkalosis: excessive loss of salt in the abnormally salty sweat of cystic fibrosis, worsened by heat, can cause a hypochloraemic hypokalaemic metabolic alkalosis (pseudo-Bartter syndrome), a recognised presentation in infants."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Bone disease: pancreatic insufficiency in cystic fibrosis impairs fat and fat-soluble vitamin D absorption (vitamin D already mapped), reducing calcium availability and contributing to the low bone density and fracture risk of the disease."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Chronic-infection immunity: MHC class II antigen presentation shapes the adaptive response to the chronic Pseudomonas and other airway infections of cystic fibrosis, a response that both defends and, through persistent inflammation, damages the lung."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Respiratory acidosis: advanced cystic-fibrosis lung disease retains carbon dioxide, and the resulting proton accumulation produces the respiratory acidosis of end-stage respiratory failure that heralds the need for transplant."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 and ABPA: IL-13 and the type-2 response drive the allergic bronchopulmonary aspergillosis that complicates cystic fibrosis, adding a Th2 arm to the neutrophilic and Th17 (IL-17 already mapped) inflammation of the airway."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cor pulmonale: chronic hypoxaemia in advanced cystic fibrosis raises pulmonary pressures and strains the right heart, and troponin elevation can mark the myocardial injury of the cor pulmonale of end-stage lung disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Airway inflammatory eicosanoids: prostaglandins from the intensely neutrophilic airway (S100A8/A9 and IL-8-type signals, IL-6 and TNF already mapped) amplify the chronic inflammation that destroys the cystic-fibrosis lung."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Malabsorption micronutrient deficiency: the exocrine pancreatic insufficiency of cystic fibrosis impairs absorption of zinc and other micronutrients, contributing to the growth failure, immune impairment and skin changes of the malnourished child."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Fat malabsorption: the exocrine pancreatic insufficiency of cystic fibrosis causes fat malabsorption, disturbing cholesterol and essential-fatty-acid handling and the absorption of fat-soluble vitamins, part of its nutritional burden."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Essential fatty-acid deficiency: the fat malabsorption (cholesterol already mapped) of cystic fibrosis depletes the omega-3 essential fatty acids and shifts the fatty-acid profile, and their supplementation is studied for the anti-inflammatory benefit in the CF airway."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 inflammation and ABPA: IL-4, with IL-13 (already mapped), drives the type-2 response that underlies the allergic bronchopulmonary aspergillosis complicating the cystic fibrosis airway."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Malnutrition and prognosis: the low body weight and cachexia of cystic fibrosis (from malabsorption and the chronic infection) disturb leptin, and the nutrition-lung-function link makes nutritional status a key prognostic factor."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Malnutrition adipokine: adiponectin, with leptin (already mapped), is part of the adipokine disturbance of the malnutrition and the CF-related metabolic dysregulation (insulin already mapped) of cystic fibrosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the chronic inflammation (IL-6 already mapped) and nutritional disturbance of cystic fibrosis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: hepcidin, driven by the chronic infection and inflammation (IL-6 already mapped), sequesters iron (already mapped) and produces the anaemia of chronic disease of cystic fibrosis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "CF liver disease: the CFTR (already mapped) defect in the biliary epithelium causes the focal biliary cirrhosis and the portal hypertension of the CF liver disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sweat sodium: the elevated sweat sodium (with chloride already mapped) is the diagnostic sweat-test hallmark of cystic fibrosis, reflecting the CFTR (already mapped) defect."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "CF bone disease: the malabsorption, the chronic inflammation (RANKL already mapped) and the corticosteroid use cause the CF-related low bone density and osteoporosis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "ABPA/colonisation: Aspergillus fumigatus colonises the CF airway and causes the allergic bronchopulmonary aspergillosis (ABPA), a type-2 (IL-13 already mapped) hypersensitivity complication of cystic fibrosis."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Alveolar CFTR: the type-II pneumocytes express the CFTR (already mapped) and produce the surfactant (already mapped); the distal-airway/alveolar involvement is part of the CF lung disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Antiviral exacerbation interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, mediates the antiviral response to the respiratory-virus exacerbations of cystic fibrosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil/ABPA arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the allergic bronchopulmonary aspergillosis (Aspergillus already mapped) that complicates cystic fibrosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 antibacterial arm: IL-12 polarises the Th1 (IFN-γ arm) response of the antibacterial airway immunity against the chronic infection of cystic fibrosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) airway inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment and the chronic airway inflammation of cystic fibrosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "ABPA arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), mediates the allergic bronchopulmonary aspergillosis, a frequent Aspergillus-driven complication of cystic fibrosis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "ABPA fungus: Aspergillus fumigatus colonises the cystic-fibrosis airways and drives the IgE-mediated (already mapped) allergic bronchopulmonary aspergillosis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the chronically infected cystic-fibrosis airway, a pathway the colonising pathogens also exploit."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Airway iron: transferrin, the iron carrier, reflects the disordered airway iron handling (hepcidin already mapped) that fuels the Pseudomonas biofilm growth in the cystic-fibrosis airway."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Airway remodelling: periostin, downstream of the IL-13 (already mapped) signalling, is part of the bronchiectatic small-airway remodelling of cystic fibrosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-CF axis: TSLP, released from the CFTR-dysfunctional airway epithelium, drives dendritic-cell (already mapped) Th2 priming and amplifies the eosinophilic airway inflammation that overlays the neutrophilic core of cystic fibrosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-CF axis: bradykinin, via B1/B2 receptors on CF airway epithelium and mast cells (already mapped), augments mucus secretion, neutrophil (already mapped) recruitment, and the inflammatory vascular permeability of cystic fibrosis airways."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Hypoxia-EPO axis: erythropoietin, induced by mucus-plug hypoxia in the CF airway, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation, linking the chronic anaemia of inflammation to lung disease in cystic fibrosis."
---

# Cystic Fibrosis

## Overview

**Cystic fibrosis (CF)** is the most common life-shortening **autosomal recessive genetic disease** in European ancestry populations, affecting approximately 1 in 2,500 live births in Northern Europe and ~1 in 3,500 in the United States (~40,000 Americans, ~100,000 worldwide). CF is caused by biallelic loss-of-function mutations in **CFTR** (cystic fibrosis transmembrane conductance regulator; chromosome 7q31.2), an ATP-gated apical chloride and bicarbonate channel expressed in epithelial cells of the airways, pancreatic and biliary ducts, intestine, sweat glands, and reproductive tract. CFTR dysfunction impairs ion and fluid transport across these epithelia → thick, dehydrated, viscous secretions → luminal obstruction, chronic infection, and progressive organ destruction. CF was first described as a distinct clinical entity by Dorothy Andersen in 1938; CFTR was identified by positional cloning in 1989 [^riordan-1989-cftr-cloning].

CF is a **multi-system disease** dominated by lung pathology: mucociliary clearance failure → chronic bacterial infection (Pseudomonas aeruginosa, Staphylococcus aureus, Haemophilus influenzae) → neutrophilic airway inflammation → progressive bronchiectasis → respiratory failure. The exocrine pancreas is destroyed in ~85% of CF patients (pancreatic insufficiency → malabsorption, fat-soluble vitamin deficiency, growth failure), and ~40-50% of adults develop **CF-related diabetes (CFRD)** — a unique form of insulin deficiency from progressive β-cell loss. The **F508del** mutation (Phe508 deletion in CFTR NBD1) accounts for ~70% of CF alleles worldwide and causes protein misfolding with ER retention. The approval of **elexacaftor/tezacaftor/ivacaftor (Trikafta)** in 2019 — a triple combination that corrects F508del misfolding and potentiates channel gating — has transformed CF: ppFEV1 improved ~14 percentage points, exacerbation rates fell ~63%, and projected median survival has increased from ~40 years to potentially >50 years [^heijerman-2019-etd-cf].

**CF epidemiology by ancestry:**

| Ancestry | Carrier frequency | Disease incidence |
|---|---|---|
| Northern European | ~1/25 | ~1/2,500 |
| Ashkenazi Jewish | ~1/25-29 | ~1/3,200 |
| Hispanic | ~1/46 | ~1/8,500 |
| African-American | ~1/65 | ~1/17,000 |
| Asian | ~1/90+ | ~1/32,000+ |

## Structure

### Genetic basis of cystic fibrosis

**CFTR mutation spectrum:**
- Over 2,000 CFTR variants identified; ClinVar and CFTR2 database classify for clinical significance
- **F508del** (c.1521_1523delCTT; p.Phe508del): ~70% of all CF alleles worldwide; causes Class II defect (protein misfolded → ER retained → degraded before surface); most severe lung phenotype class
- **G551D**: ~3-5% of CF alleles; Class III gating mutation (protein reaches surface but channel gate stuck shut); responsive to ivacaftor monotherapy; historically worst FEV1 outcomes
- **W1282X**, **G542X**: common truncating (nonsense) mutations; Class I (no protein produced); not responsive to current modulators; ataluren/ELX-02 targeting these
- **R117H**: Class IV (reduced conductance); phenotype varies widely from male infertility/CBAVD only to mild CF; R117H with 5T poly-T tract → classic CF; with 7T → CBAVD only; with 9T → carrier without disease
- **2789+5G→A**, **3849+10kbC→T**: Class V splice mutations; reduced but present CFTR function; generally milder CF
- **Genotype-phenotype correlation**:
  - Pancreatic insufficiency/sufficiency: strongly correlated (Class I/II → PI; Class IV/V/R117H → PS)
  - Lung function: poorly correlated with genotype — predominantly determined by modifier genes, infection history, adherence, and environmental factors
  - CFRD: risk ~40-50% regardless of CFTR genotype class

**CFTR2 database and modifier genetics:**
- CFTR2 database (cftr2.org): clinical outcome data for >40,000 CF patients linked to CFTR variants; used for pathogenicity classification
- **Modifier genes** significantly influence CF lung disease severity:
  - TGF-β1 promoter (high-expression genotypes → worse lung disease; lower response to modulators)
  - MBL2 (mannose-binding lectin): low-MBL genotypes → worse P. aeruginosa outcomes
  - IFRD1, SLC26A9: associated with lung function variation
  - CXCR1/2: IL-8 receptor polymorphisms → differential neutrophil trafficking in CF airways

**Carrier screening:**
- ACMG/ACOG recommend universal carrier screening for CF in all pregnancies
- 23-mutation ACMG panel detects ~90% of CF alleles in Northern European ancestry; expanded panels (80-320 mutations) increase sensitivity to >99%
- Carrier couples (both partners positive): 25% chance of affected offspring; prenatal diagnosis by CVS or amniocentesis; PGT available

**Neonatal screening:**
- Most US states and many countries: immunoreactive trypsinogen (IRT, elevated in CF newborns) → if elevated → CFTR mutation panel; 2-tiered IRT/DNA protocol identifies >95% of CF newborns
- Early diagnosis → early pancreatic enzyme replacement → nutritional outcomes markedly improved; early modulator therapy → preserved lung function

## Function

### Clinical features of cystic fibrosis

**Pulmonary disease (dominant cause of morbidity and mortality):**
- **Airway infection**: earliest detectable pathology; S. aureus (MSSA/MRSA) common in childhood; P. aeruginosa (mucoid biofilm phenotype) colonizes in adolescence/adulthood (~40-60% of adults, declining with Trikafta era); Burkholderia cepacia complex (worst prognosis, lung transplant contraindication in some centers); Achromobacter xylosoxidans; NTM (nontuberculous mycobacteria, ~10-15% prevalence)
- **Chronic neutrophilic inflammation**: IL-8-driven massive neutrophil recruitment to airway; neutrophil elastase released → proteolytic damage to airways and epithelia → airway wall destruction; IL-6, IL-1β elevated
- **Bronchiectasis**: progressive permanent dilation and distortion of bronchi; visible on CT from early childhood; leads to air trapping, hyperinflation, reduced FEV1
- Respiratory failure: progressive FEV1 decline; severe CF: FEV1 <30% predicted; respiratory failure from hypercarbia/hypoxemia → lung transplant consideration
- **CF pulmonary exacerbations**: acute worsening of respiratory symptoms (increased cough, sputum, dyspnea, decreased FEV1); treated with IV antibiotics (usually 2-3 week courses) + intensified airway clearance; hospitalized exacerbations → faster FEV1 decline

**Pulmonary management:**
- **CFTR modulators**: F508del homozygotes + eligible heterozygotes → ETD (Trikafta) daily; reduces exacerbations ~63%, improves ppFEV1 ~14 pp, sweat Cl⁻ ↓ ~41 mmol/L; most transformative intervention in CF history
- **Airway clearance therapy (ACT)**: chest physiotherapy, high-frequency chest wall oscillation (ThAIRapy vest), oscillating positive expiratory pressure (Flutter, Aerobika); daily 20-30 min sessions
- **Dornase alfa (Pulmozyme)**: recombinant human DNase I; cleaves extracellular DNA (from neutrophil NETs) in CF sputum → reduces viscoelasticity → easier clearance; ppFEV1 ↑ ~5 pp
- **Hypertonic saline (7%)**: inhaled osmotic agent → draws water onto airway surface → thins mucus; reduces exacerbations ~56%
- **Azithromycin**: 3×/week long-term macrolide → anti-inflammatory + anti-Pseudomonas biofilm effects; reduces exacerbations ~35%; standard therapy for P. aeruginosa-colonized CF
- **Inhaled antibiotics**: tobramycin (TOBI, nebulized or inhaler), aztreonam (Cayston), colistin (inhaled); alternating monthly regimens for chronic P. aeruginosa suppression
- **Lung transplantation**: bilateral lung transplant when FEV1 <30-40% predicted + rapid decline; 5-year survival post-CF lung transplant ~50-55%; CF lower airway disease eliminated but chronic lung allograft dysfunction risk persists

**Gastrointestinal and nutritional disease:**
- **Exocrine pancreatic insufficiency (EPI, ~85%)**: absent lipase/protease/amylase in duodenum → fat malabsorption → steatorrhea, fat-soluble vitamin (A, D, E, K) deficiency, essential fatty acid deficiency → growth failure
- **Pancreatic enzyme replacement therapy (PERT)**: Creon/Zenpep/Pancreaze with all fat-containing meals; dose 1,000-2,500 IU lipase/kg/meal; dramatically improves nutritional outcomes
- **CF-related diabetes (CFRD)**: affects ~40-50% of CF adults; caused by progressive β-cell loss (pancreatic fibrosis, islet disruption) + peripheral insulin resistance; not classic T1DM (autoimmune) or T2DM (primarily insulin resistance); insulin therapy required (not oral hypoglycemics); Hb A1c may underestimate glycemia in CF (increased RBC turnover); CFRD → worsened FEV1 and nutritional status → treat aggressively
- **CF liver disease (CFLD, ~15-20%)**: biliary CFTR LOF → inspissated bile → focal biliary cirrhosis → multilobular cirrhosis in ~5%; portal hypertension, esophageal varices; ursodeoxycholic acid (UDCA) may slow progression; liver transplant in severe CFLD
- **Distal intestinal obstruction syndrome (DIOS)**: impacted fecal material in distal ileum/cecum → acute abdominal pain, vomiting; treated with polyethylene glycol lavage, Gastrografin enema; prevented by adequate hydration and PERT dosing
- **GERD**: highly prevalent in CF; acid aspiration worsens lung disease; treat with PPI + promotility agents

**CF reproductive and musculoskeletal features:**
- Male infertility: CBAVD (congenital bilateral absence of vas deferens) in ~98% of CF males; TESE + ICSI available
- Female fertility: reduced but possible; cervical mucus thicker → reduced sperm penetration; uterus and ovaries normal; pregnancy possible in CF with modulator therapy; Trikafta safe in pregnancy (growing evidence)
- CF-related bone disease (CFBD): osteopenia/osteoporosis from malabsorption (Ca, Vit D), chronic inflammation, GC use, hypogonadism; annual DEXA from age 18; bisphosphonates for established osteoporosis
- CF arthropathy: episodic periarthritis, symmetric non-erosive joint inflammation; HLA-linked predisposition; responds to NSAIDs; not responsive to CF antibiotics
- **Digital clubbing**: present in ~50-70% of CF patients with significant lung disease; correlates with FEV1

### The CFTR modulator era

**Transformative impact of ETD (Trikafta):**
- FDA-approved October 2019 for ages 12+ with ≥1 F508del allele; expanded to ages 2+ (2021)
- Clinical outcomes (Heijerman 2019 Phase 3, F508del homozygotes): ppFEV1 ↑ 14.3 pp (placebo-adjusted); sweat Cl⁻ ↓ 41.8 mmol/L; pulmonary exacerbations ↓ 63%; BMI ↑ 1.04 kg/m²
- Long-term data: continued ppFEV1 improvement at 3-5 years; hospitalization rates ↓ 65%; lung transplant referrals dramatically reduced; fertility improved (female CF patients increasingly conceiving)
- Mutation eligibility: ~90% of CF patients (all F508del homozygotes + heterozygotes with responsive second allele); ~10% not eligible (Class I premature stop mutations, rare class II mutations not responsive to elexacaftor)
- Future pipeline: CFTR mRNA therapy (Translate Bio + Sanofi); gene editing (ex vivo airway stem cell CRISPR; in vivo lipid nanoparticle delivery); next-generation correctors with improved thermostability

## Pathology

### Diagnosis

**Diagnostic criteria (CF Foundation, 2017):**
1. ≥1 characteristic phenotypic feature (chronic sinopulmonary disease, GI/nutritional abnormalities, CBAVD, or elevated sweat electrolytes) OR positive NBS (newborn screen)
AND
2. Evidence of CFTR dysfunction: sweat Cl⁻ ≥60 mmol/L (on 2 separate occasions) OR 2 CF-causing CFTR pathogenic variants in trans OR CFTR transepithelial nasal potential difference (NPD) consistent with CF

**Sweat chloride test:**
- Gibson-Cooke pilocarpine iontophoresis; sweat Cl⁻ ≥60 mmol/L = CF; 30-59 = intermediate (CF possible); <30 = normal
- Most sensitive and specific diagnostic test; must be performed at CF-certified laboratory; minimum sweat volume required (>75 mg)

**Differential diagnosis:**
- Primary ciliary dyskinesia (PCD): recurrent sinopulmonary infections, bronchiectasis, situs inversus; normal sweat Cl⁻; nasal nitric oxide low; electron microscopy of cilia
- Allergic bronchopulmonary aspergillosis (ABPA): CF complication or separate; elevated IgE, Aspergillus-specific IgE, eosinophilia; responds to antifungals + steroids
- Severe combined immunodeficiency (SCID): neonatal; no CF mutations; lymphocyte subset deficiency
- Shwachman-Diamond syndrome (SBDS gene): pancreatic insufficiency + bone marrow failure; normal sweat Cl⁻; neutropenia; SBDS sequencing
- Hirschsprung disease: neonatal bowel obstruction; normal sweat Cl⁻; absent ganglia on biopsy

**Multidisciplinary CF center care:**
- Pulmonology: airway clearance therapy, modulator prescribing, exacerbation management
- Gastroenterology/nutrition: PERT dosing, nutritional optimization, liver disease monitoring, CFRD management
- Endocrinology: CFRD (insulin management), bone disease (DEXA, bisphosphonates)
- Reproductive health: fertility counseling, pregnancy management
- Psychology/social work: CF is a lifelong demanding disease; mental health support integral (depression/anxiety prevalence ~3x general population in CF)
- CF microbiology: specialized sputum culture protocols for CF pathogens (Burkholderia, Pseudomonas susceptibility testing)
- Physiotherapy: ACT technique training and prescription
- Annual assessments: spirometry, CT chest (alternate years), glucose tolerance test, DEXA scan, sputum culture, liver ultrasound, comprehensive labs (vitamins, HbA1c, renal function)

## Connections

- `connects-to` → **[CFTR](../../03-molecular/cftr/README.md)** — Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients.
- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CF airway dominated by massive neutrophil recruitment (IL-8-driven); neutrophil elastase → proteolysis → bronchiectasis; NETs provide extracellular DNA that increases sputum viscoelasticity; dornase alfa (DNase I) cleaves NET-derived DNA → improved mucus clearance.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — NLRP3 inflammasome activation in CF airway → IL-1β/IL-18 release → amplifies airway inflammation; CFTR LOF → oxidative stress → NLRP3 priming; IL-1β drives CXCL8 production by airway epithelium → neutrophil recruitment loop; canakinumab (anti-IL-1β) explored as CF lung adjunct.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — CFTR mutations (5T, R117H) are second-hit modifiers in hereditary pancreatitis (PRSS1/SPINK1 mutations); compound heterozygosity → idiopathic chronic pancreatitis; CFTR LOF → reduced pancreatic duct bicarbonate → trypsinogen aggregation and premature activation → acinar injury.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Cystic fibrosis is at root a chloride-transport disease: CFTR is an apical chloride channel, so its loss leaves epithelia unable to move chloride and water, dehydrating secretions into thick mucus — and the same defect raises sweat chloride above 60 mmol/L, the diagnostic test.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung carries most of cystic fibrosis's morbidity: dehydrated mucus cripples mucociliary clearance, inviting chronic Pseudomonas and Staph infection and neutrophilic inflammation that scars airways into bronchiectasis — historically the leading cause of CF death.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Staphylococcus aureus is typically the first chronic airway colonizer in cystic fibrosis, dominating childhood before Pseudomonas takes over in adolescence; persistent S. aureus feeds the neutrophilic inflammation that drives early bronchiectasis.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is a major target of cystic fibrosis: thick CFTR-deficient secretions plug pancreatic ducts → autodigestion and fibrosis → exocrine insufficiency (malabsorption, steatorrhea needing enzyme replacement) and, as islets are destroyed, CF-related diabetes.
- `connects-to` → **[COPD](../copd/README.md)** — Cystic fibrosis and COPD are both chronic obstructive, neutrophil-driven airway diseases with mucus plugging and infective exacerbations, but differ in cause: CF is a monogenic CFTR channel defect from birth, COPD an acquired (usually smoking-driven) disease of later life.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Cystic fibrosis-related diabetes is the commonest CF comorbidity in adults: progressive destruction of pancreatic islets by the same ductal disease that causes exocrine failure produces an insulin-deficient diabetes distinct from type 1 and type 2, worsening lung function.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — The respiratory system bears the lethal burden of cystic fibrosis: defective CFTR chloride transport thickens airway mucus, causing impaired clearance, chronic infection, bronchiectasis, and respiratory failure—the leading cause of death, now eased by CFTR modulators.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Cystic fibrosis disrupts the entire digestive system: thick secretions block pancreatic ducts causing exocrine insufficiency and malabsorption, plug the bowel as meconium ileus in newborns, and thicken bile—so enzyme replacement and nutrition are central to CF care.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cystic fibrosis usually causes male infertility: nearly all men with CF have congenital bilateral absence of the vas deferens from CFTR dysfunction, so they are azoospermic despite normal sperm production—and isolated CBAVD can be the only sign of mild CFTR mutations.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium transport is deranged in cystic fibrosis: defective CFTR not only blocks chloride exit but unleashes excess sodium and water absorption, dehydrating airway mucus—and the resulting high sweat sodium chloride is the basis of the diagnostic sweat test.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Aspergillus colonizes the cystic fibrosis airway: the thick mucus lets Aspergillus fumigatus grow, and the hypersensitivity response (ABPA) causes wheezing, mucus plugging and lung decline—so CF care monitors for and treats this fungal complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a CF target organ: thick bile from defective CFTR blocks small bile ducts, causing focal biliary cirrhosis and, in some, progressive CF liver disease with portal hypertension—a leading non-pulmonary cause of death in cystic fibrosis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Cystic fibrosis obstructs the small intestine with thick secretions: newborns can present with meconium ileus, and older patients suffer distal intestinal obstruction syndrome, while impaired pancreatic enzyme flow causes the fat malabsorption central to CF.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — CF-related diabetes is a common endocrine complication: thick secretions scar the pancreas and destroy insulin-producing islets, so a distinct form of diabetes emerges with age—now a leading comorbidity as CF patients live longer.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Cystic fibrosis weakens bone: malabsorption of vitamin D and calcium, chronic inflammation, steroids and delayed puberty cause CF-related low bone density, so fractures and osteoporosis are an increasingly important problem in the aging CF population.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Cystic fibrosis is named for the scarring it causes: thick secretions and chronic inflammation replace pancreatic and lung tissue with fibrosis and cysts, so progressive fibrotic destruction—not the gene defect alone—drives organ failure.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — CF cripples the lung's macrophages: the CFTR defect impairs how macrophages acidify phagosomes and kill bacteria, so weakened innate immunity lets Pseudomonas and other microbes establish the chronic infection central to CF lung disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CF lung disease is a self-damaging immune cycle: impaired clearance invites chronic bacterial infection that draws relentless neutrophilic inflammation, whose enzymes destroy airways more than the microbes do—so anti-inflammatory strategies complement antibiotics.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Cystic fibrosis starves the body of vitamin D: pancreatic insufficiency blocks absorption of fat-soluble vitamins, so CF patients run low on vitamin D and need high-dose supplements to fend off the bone disease that shadows the illness.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Cystic fibrosis breeds its own diabetes through insulin loss: scarring of the pancreas destroys insulin-producing islet cells, causing CF-related diabetes—a distinct form, neither type 1 nor type 2, that worsens lung decline and needs insulin.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Treating cystic fibrosis can deplete magnesium: the IV aminoglycosides used against Pseudomonas waste magnesium through the kidney, and malabsorption adds to it, so low magnesium is a recurring complication to monitor and replace.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Cystic fibrosis lungs over-inflame through NF-kB: the defective CFTR channel primes airway cells to ramp up this inflammatory switch, so even modest infection triggers a damaging neutrophil flood, driving the relentless lung destruction.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-helper cells skew the cystic fibrosis airway toward harm: a Th17- and Th2-tilted response amplifies inflammation against chronic Pseudomonas and fungi rather than clearing them, adding adaptive immunity to the neutrophilic damage.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Cystic fibrosis ends as an oxygen problem: thick mucus, infection and scarring wreck gas exchange, so chronic low oxygen drives pulmonary hypertension and cor pulmonale, the respiratory failure that defines advanced disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Cystic fibrosis is also a bicarbonate problem: the CFTR channel normally exports bicarbonate, so its loss leaves secretions acidic, thickening mucus and crippling pancreatic enzymes—an acid-base angle beyond the chloride defect.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Cystic fibrosis can block the bowel: thick secretions cause meconium ileus in newborns and distal intestinal obstruction syndrome later, plugging the large intestine in ways that mimic appendicitis or obstruction.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cystic fibrosis scars its organs through fibroblasts: chronic inflammation activates them to lay down the fibrosis that destroys the pancreas (giving the disease its name) and stiffens the lungs.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — CF lungs are tracked by imaging: chest CT photons reveal the bronchiectasis—dilated, mucus-filled airways—and plugging that map the progressive lung destruction long before lung function fails.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CF is diagnosed through the skin: defective CFTR can't reabsorb chloride in sweat glands, so the sweat is salty—the basis of the sweat-chloride test and the 'salty kiss' parents notice.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — CFTR lines the gut: without it the intestinal epithelium can't hydrate its secretions, so thick mucus causes meconium ileus, malabsorption and obstruction throughout the bowel.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the failed mucociliary escalator: with CFTR's chloride channel broken, the airway surface dehydrates, the protective fluid layer collapses, and the cilia flatten under thick, immovable mucus.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Decades of lung disease overload the right heart: chronic low oxygen raises pulmonary pressures until the right ventricle fails into cor pulmonale, a common terminal pathway in advanced cystic fibrosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney bears the cost of treatment: lifelong courses of aminoglycoside antibiotics for lung infections are nephrotoxic, and dehydration and stones add to the renal risk these patients carry.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — CF unsettles the upper gut: reflux is near-universal as cough and physiotherapy push acid up, and thickened secretions slow the stomach, while lower down the same mucus jams the bowel into distal intestinal obstruction syndrome.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An allergic antibody storm complicates CF lungs: allergic bronchopulmonary aspergillosis, an IgE- and IgG-driven hypersensitivity to the Aspergillus colonizing the airways, worsens wheeze and lung damage and is treated with steroids and antifungals.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — CF quietly lowers the red cells: chronic infection's anemia of inflammation, malabsorption of iron and vitamins, and GI blood loss combine to leave many patients anemic despite their other reserves.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — CF liver disease can enlarge the spleen: thick bile scars the liver into focal biliary cirrhosis, and the resulting portal hypertension swells the spleen and drops platelet and white-cell counts through hypersplenism, a serious extrapulmonary complication.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — CF thins bone from the cellular level up: chronic inflammation, vitamin D and K malabsorption, and steroid use tip the balance toward osteoclast bone resorption, producing the early osteopenia and fracture risk of CF bone disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron fuels the airway invaders: the CF lung's mucus is iron-rich, and Pseudomonas exploits that iron to build the biofilms that entrench chronic infection, making iron acquisition both a bacterial strategy and a potential treatment target.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — CF carries its own diabetes: scarring of the pancreas destroys the insulin-making islets, producing CF-related diabetes — an insulin-deficient disease like type 1 that becomes common as patients live longer.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — The CF airway runs hot with IL-6: persistent neutrophilic infection drives high IL-6 and other cytokines, the chronic inflammation that progressively destroys the lung even between exacerbations.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Immune sensing goes awry in the CF lung: dysregulated dendritic cells fail to resolve infection and instead help sustain the damaging inflammation, part of why the CF airway cannot clear its chronic colonizers.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17 arm recruits the destructive neutrophils: IL-17A is elevated in CF airways and drives the neutrophil influx and mucin production that wreck the lung, making the IL-17 axis a candidate anti-inflammatory target.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Infection can break out of the lung: severe exacerbations and Burkholderia cepacia 'cepacia syndrome,' along with long-term indwelling venous catheters, expose CF patients to bloodstream infection and sepsis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Allergy compounds the CF airway: mast cells drive the allergic bronchopulmonary aspergillosis and airway hyper-reactivity that often complicate cystic fibrosis on top of its chronic bacterial infection.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — CFTR is also a gut tumor suppressor: people with cystic fibrosis face a markedly raised colorectal cancer risk that rises further after lung transplant, so earlier and more frequent colonoscopy screening is now recommended.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — End-stage lungs back up onto the heart: chronic hypoxia and destroyed pulmonary vasculature in advanced CF raise pulmonary artery pressure into cor pulmonale, a marker of severe disease and transplant need.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Neutrophilic airway inflammation funnels through STAT3: IL-6 and IL-17 in the chronically infected CF lung drive STAT3 signaling that sustains the relentless inflammation damaging the airways.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Lifelong aminoglycosides scar the kidney: the repeated courses of nephrotoxic aminoglycosides for chronic Pseudomonas infection, plus dehydration from salt loss, leave many CF patients with chronic kidney disease.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Chronic pancreatic damage raises the cancer risk: the recurrent pancreatic inflammation and duct injury of CF are associated with an elevated risk of pancreatic and other digestive-tract cancers in adults.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A demanding lifelong illness weighs on mood: the daily treatment burden, recurrent infections and shortened life expectancy of CF carry high rates of depression and anxiety, now routinely screened for.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its indwelling lines clot the veins: the long-term central venous catheters and ports CF patients need for repeated IV antibiotics, plus chronic inflammation, raise the risk of venous thromboembolism.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Its liver disease can scar toward cancer: CF-related liver disease causes biliary cirrhosis in a subset of patients, and the resulting cirrhosis carries a risk of hepatocellular carcinoma.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A relentless treatment burden breeds worry: the constant therapies, fear of infection and uncertain prognosis of CF drive anxiety alongside depression, now part of routine mental-health screening.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its sweat is salty by defect: defective CFTR in sweat glands fails to reabsorb chloride, giving the salt-losing skin the sweat-chloride test diagnoses and a risk of salt depletion in the heat.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Chronic lung disease strains the right heart: the progressive hypoxaemia and pulmonary hypertension of advanced CF overload the right ventricle into cor pulmonale and right heart failure.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It weakens bone and inflames joints: malabsorption and chronic inflammation cause CF-related low bone density and fractures, and an episodic CF arthropathy with finger clubbing accompanies the disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Fat malabsorption starves the nerves: deficiency of fat-soluble vitamin E can cause peripheral neuropathy and ataxia, and the aminoglycosides used for infections add ototoxicity.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic lung disease overloads the right heart: progressive CF lung disease raises pulmonary pressures, leading to pulmonary hypertension and cor pulmonale with right heart failure.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Salt loss and antibiotics tax the kidney: heavy sweat salt loss can cause a pseudo-Bartter syndrome with hypochloraemic alkalosis, and repeated aminoglycoside courses are nephrotoxic.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Mycobacteria threaten the CF lung: non-tuberculous mycobacteria related to M. tuberculosis, such as M. abscessus, are emerging chronic infections in cystic fibrosis that can complicate transplant.
- `connects-to` → **[Clostridioides difficile](../../../02-pathogen/02-bacteria/clostridioides-difficile/README.md)** — Lifelong antibiotics disturb the gut: the heavy, repeated antibiotic courses for CF lung infections raise the risk of Clostridioides difficile colitis.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Fat malabsorption drains nutrients: pancreatic insufficiency in CF impairs absorption of fat-soluble vitamins and zinc, contributing to poor growth and weakened immunity.
- `connects-to` → **[Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md)** — MRSA now haunts the CF airway: methicillin-resistant Staphylococcus aureus is an increasingly common chronic coloniser of cystic-fibrosis lungs, treated with vancomycin and linked to faster lung-function decline.
- `connects-to` → **[Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md)** — Early antibiotics guard young lungs: anti-staphylococcal antibiotics are used from infancy in cystic fibrosis to treat and sometimes prevent the Staphylococcus aureus infections that begin the cycle of airway damage.
- `connects-to` → **[Asthma](../asthma/README.md)** — Allergic airway disease overlaps it: many people with cystic fibrosis have coexisting asthma and allergic bronchopulmonary aspergillosis, adding reversible airway obstruction to their fixed disease.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — CFTR modulators transformed it: small-molecule correctors and potentiators — culminating in elexacaftor-tezacaftor-ivacaftor (Trikafta) — restore mutant CFTR function and dramatically improve lung function and survival in cystic fibrosis.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It destroys the airways: thick CFTR-deficient mucus plugs the bronchi, breeding chronic Pseudomonas and Staphylococcus infection that scar the lung into bronchiectasis — the airway destruction that drives most CF mortality.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — It destroys the islets too: progressive pancreatic fibrosis and fatty replacement damage the islets of Langerhans, causing cystic-fibrosis-related diabetes — the commonest CF comorbidity, with features of both type 1 and type 2.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — CF liver disease: thick bile from CFTR loss in cholangiocytes obstructs the bile ductules of the hepatic lobule, causing focal biliary cirrhosis and portal hypertension—a leading non-pulmonary cause of death.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Anaemia of chronic infection: persistent airway infection and inflammation in CF raise hepcidin and blunt erythropoiesis, causing an anaemia of chronic disease despite adequate iron stores.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — CF bone disease: malabsorption of vitamin D and calcium, chronic inflammation and steroids thin cortical bone, causing the early osteoporosis and fractures common in CF adults.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Allergic and invasive fungus: Aspergillus fumigatus colonises CF airways, causing allergic bronchopulmonary aspergillosis (ABPA) that worsens airflow and accelerates lung decline.
- `connects-to` → **[Influenza](../influenza/README.md)** — Viral exacerbations: respiratory viruses like influenza and RSV trigger severe pulmonary exacerbations in cystic fibrosis, accelerating lung decline and predisposing to bacterial superinfection.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Mucus plugging reaches the air sacs: as CF lung disease advances, thick secretions and chronic infection extend into the small airways and alveoli, driving the respiratory failure that ends the disease.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Self-sustaining inflammation: TNF-α amplifies the relentless neutrophilic airway inflammation of cystic fibrosis, joining IL-1β, IL-6 and IL-17 in the cytokine loop that destroys lung tissue.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Cystic fibrosis liver disease: defective CFTR in biliary epithelium plugs bile ducts and causes focal biliary cirrhosis, injuring hepatocytes and progressing to portal hypertension.
- `connects-to` → **[Surfactant](../../03-molecular/surfactant/README.md)** — Compromised host defence: chronic inflammation and proteases degrade and inactivate pulmonary surfactant in cystic fibrosis, weakening innate immune defence and small-airway stability.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Inflammatory cell recruitment: CCL2 draws monocytes into cystic-fibrosis airways, adding to the relentless neutrophil-dominated inflammation that destroys the lung.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Mucus-plug hypoxia: thick mucus and Pseudomonas biofilms create steep oxygen gradients in cystic-fibrosis airways, stabilising HIF-1α in epithelial and immune cells.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bronchial angiogenesis: chronic inflammation in cystic fibrosis raises VEGF, expanding tortuous bronchial vessels that are the source of the life-threatening haemoptysis of advanced disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil alarmin: S100A8/A9 from the neutrophils flooding cystic-fibrosis airways amplifies inflammation, and sputum calprotectin tracks the burden of airway disease and exacerbations.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Misfolded-CFTR proteostasis: the ΔF508 CFTR mutant is cleared by autophagy and ERAD, and impaired autophagy in cystic fibrosis lets the misfolded protein and aggregates accumulate, worsening inflammation.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — CF bone disease: chronic inflammation, malabsorption and corticosteroid use drive RANKL-mediated bone resorption, causing the osteoporosis and fractures common in adults with cystic fibrosis.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 recognition of the lipopolysaccharide of chronically colonizing Pseudomonas aeruginosa drives the relentless NF-κB-mediated neutrophilic airway inflammation that progressively destroys the cystic-fibrosis lung.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR signaling in the CF airway drives goblet-cell metaplasia and MUC5AC mucin secretion that compounds the dehydrated, viscous mucus already produced by defective CFTR chloride and bicarbonate transport.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Cystic-fibrosis airways paradoxically show low nitric oxide, impairing ciliary function and the antimicrobial defense of the epithelium and contributing to the chronic bacterial infection that defines the disease.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — The dehydrated, viscous airway surface liquid of cystic fibrosis impairs mucociliary clearance and the function of secretory IgA, weakening the first-line mucosal barrier and helping the chronic Pseudomonas and Staphylococcus infections take hold.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — The massive neutrophil infiltrate of the cystic-fibrosis airway, with xanthine-oxidase activity, generates reactive oxygen species that damage the epithelium, compounding the oxidative stress worsened by depleted antioxidant glutathione.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Airway neutrophils in cystic fibrosis show delayed caspase-3-mediated apoptosis, so they persist and necrose rather than being cleared, perpetuating the self-amplifying inflammation that destroys the lung.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — CFTR dysfunction impairs NRF2-driven antioxidant defense and glutathione transport, so oxidant stress goes unchecked and amplifies the airway inflammation that drives cystic-fibrosis lung damage.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Relative deficiency of the anti-inflammatory cytokine IL-10 in the cystic-fibrosis airway removes a brake on neutrophilic inflammation, contributing to the exaggerated, self-perpetuating immune response.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Chronic Pseudomonas colonization in cystic fibrosis activates complement (C3) and generates immune complexes, and the resulting complement-mediated injury accelerates the progressive bronchiectasis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped), driven by chronic Pseudomonas and Staphylococcus infection, sustains the destructive neutrophilic inflammation of the cystic-fibrosis lung.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated autophagy (autophagy already mapped) governs the handling of misfolded ΔF508-CFTR, and its modulation is explored to rescue mutant CFTR trafficking in cystic fibrosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 and inflammatory-cytokine signaling through JAK-STAT3 (IL-6 and STAT3 already mapped) amplifies the chronic airway inflammation of cystic fibrosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) is dysregulated in CFTR-deficient epithelia and shapes the inflammatory and autophagy responses of cystic fibrosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR-ERK-MAPK signaling (EGFR mapped) drives the mucin hypersecretion and airway epithelial remodeling of cystic fibrosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the neutrophil-dominated airway inflammation characteristic of cystic fibrosis lung disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies the antiviral and antibacterial response that shapes the recurrent infections of cystic fibrosis lung disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA from neutrophil extracellular traps and bacteria in the cystic-fibrosis airway engages cGAS-STING, amplifying the chronic airway inflammation.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGFB1 a recognized modifier of cystic-fibrosis severity) drives the airway and pancreatic fibrosis of cystic fibrosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the airway epithelial oxidative-stress defense and immune-metabolic balance perturbed in the chronic infection of cystic fibrosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven hyperinflammation of the cystic-fibrosis airway.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic activity by CD8 T and NK cells contributes to the immune-mediated tissue damage of the chronically infected cystic-fibrosis airway.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the airway epithelial and neutrophilic inflammatory responses of cystic fibrosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling interacts with the CFTR channel and the autophagic responses (CFTR and autophagy already mapped) dysregulated in cystic fibrosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the airway inflammatory and epithelial responses of cystic fibrosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the chronic neutrophilic airway inflammation of cystic fibrosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic modulation of the inflammatory responses in cystic fibrosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement C5a-driven inflammation contributes to the neutrophilic airway inflammation of cystic fibrosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the airway leukocyte trafficking of the chronic neutrophilic inflammation of cystic fibrosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the airway epithelial and innate immune responses of cystic fibrosis.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen deposition contributes to the airway remodeling and fibrosis of chronic cystic-fibrosis lung disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the airway-epithelial and immune gene programs of cystic fibrosis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the airway T-cell inflammation of cystic fibrosis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the airway-surface-liquid regulation and inflammation of cystic fibrosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Salt-wasting alkalosis: excessive loss of salt in the abnormally salty sweat of cystic fibrosis, worsened by heat, can cause a hypochloraemic hypokalaemic metabolic alkalosis (pseudo-Bartter syndrome), a recognised presentation in infants.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Bone disease: pancreatic insufficiency in cystic fibrosis impairs fat and fat-soluble vitamin D absorption (vitamin D already mapped), reducing calcium availability and contributing to the low bone density and fracture risk of the disease.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Chronic-infection immunity: MHC class II antigen presentation shapes the adaptive response to the chronic Pseudomonas and other airway infections of cystic fibrosis, a response that both defends and, through persistent inflammation, damages the lung.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Respiratory acidosis: advanced cystic-fibrosis lung disease retains carbon dioxide, and the resulting proton accumulation produces the respiratory acidosis of end-stage respiratory failure that heralds the need for transplant.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 and ABPA: IL-13 and the type-2 response drive the allergic bronchopulmonary aspergillosis that complicates cystic fibrosis, adding a Th2 arm to the neutrophilic and Th17 (IL-17 already mapped) inflammation of the airway.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cor pulmonale: chronic hypoxaemia in advanced cystic fibrosis raises pulmonary pressures and strains the right heart, and troponin elevation can mark the myocardial injury of the cor pulmonale of end-stage lung disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Airway inflammatory eicosanoids: prostaglandins from the intensely neutrophilic airway (S100A8/A9 and IL-8-type signals, IL-6 and TNF already mapped) amplify the chronic inflammation that destroys the cystic-fibrosis lung.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Malabsorption micronutrient deficiency: the exocrine pancreatic insufficiency of cystic fibrosis impairs absorption of zinc and other micronutrients, contributing to the growth failure, immune impairment and skin changes of the malnourished child.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Fat malabsorption: the exocrine pancreatic insufficiency of cystic fibrosis causes fat malabsorption, disturbing cholesterol and essential-fatty-acid handling and the absorption of fat-soluble vitamins, part of its nutritional burden.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Essential fatty-acid deficiency: the fat malabsorption (cholesterol already mapped) of cystic fibrosis depletes the omega-3 essential fatty acids and shifts the fatty-acid profile, and their supplementation is studied for the anti-inflammatory benefit in the CF airway.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 inflammation and ABPA: IL-4, with IL-13 (already mapped), drives the type-2 response that underlies the allergic bronchopulmonary aspergillosis complicating the cystic fibrosis airway.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Malnutrition and prognosis: the low body weight and cachexia of cystic fibrosis (from malabsorption and the chronic infection) disturb leptin, and the nutrition-lung-function link makes nutritional status a key prognostic factor.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Malnutrition adipokine: adiponectin, with leptin (already mapped), is part of the adipokine disturbance of the malnutrition and the CF-related metabolic dysregulation (insulin already mapped) of cystic fibrosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the chronic inflammation (IL-6 already mapped) and nutritional disturbance of cystic fibrosis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: hepcidin, driven by the chronic infection and inflammation (IL-6 already mapped), sequesters iron (already mapped) and produces the anaemia of chronic disease of cystic fibrosis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — CF liver disease: the CFTR (already mapped) defect in the biliary epithelium causes the focal biliary cirrhosis and the portal hypertension of the CF liver disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sweat sodium: the elevated sweat sodium (with chloride already mapped) is the diagnostic sweat-test hallmark of cystic fibrosis, reflecting the CFTR (already mapped) defect.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — CF bone disease: the malabsorption, the chronic inflammation (RANKL already mapped) and the corticosteroid use cause the CF-related low bone density and osteoporosis.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — ABPA/colonisation: Aspergillus fumigatus colonises the CF airway and causes the allergic bronchopulmonary aspergillosis (ABPA), a type-2 (IL-13 already mapped) hypersensitivity complication of cystic fibrosis.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Alveolar CFTR: the type-II pneumocytes express the CFTR (already mapped) and produce the surfactant (already mapped); the distal-airway/alveolar involvement is part of the CF lung disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Antiviral exacerbation interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, mediates the antiviral response to the respiratory-virus exacerbations of cystic fibrosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil/ABPA arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the allergic bronchopulmonary aspergillosis (Aspergillus already mapped) that complicates cystic fibrosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 antibacterial arm: IL-12 polarises the Th1 (IFN-γ arm) response of the antibacterial airway immunity against the chronic infection of cystic fibrosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neutrophilic (already mapped) airway inflammation of cystic fibrosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment and the chronic airway inflammation of cystic fibrosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — ABPA arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), mediates the allergic bronchopulmonary aspergillosis, a frequent Aspergillus-driven complication of cystic fibrosis.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — ABPA fungus: Aspergillus fumigatus colonises the cystic-fibrosis airways and drives the IgE-mediated (already mapped) allergic bronchopulmonary aspergillosis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) on the chronically infected cystic-fibrosis airway, a pathway the colonising pathogens also exploit.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Airway iron: transferrin, the iron carrier, reflects the disordered airway iron handling (hepcidin already mapped) that fuels the Pseudomonas biofilm growth in the cystic-fibrosis airway.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Airway remodelling: periostin, downstream of the IL-13 (already mapped) signalling, is part of the bronchiectatic small-airway remodelling of cystic fibrosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-CF axis: TSLP, released from the CFTR-dysfunctional airway epithelium, drives dendritic-cell (already mapped) Th2 priming and amplifies the eosinophilic airway inflammation that overlays the neutrophilic core of cystic fibrosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-CF axis: bradykinin, via B1/B2 receptors on CF airway epithelium and mast cells (already mapped), augments mucus secretion, neutrophil (already mapped) recruitment, and the inflammatory vascular permeability of cystic fibrosis airways.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Hypoxia-EPO axis: erythropoietin, induced by mucus-plug hypoxia in the CF airway, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation, linking the chronic anaemia of inflammation to lung disease in cystic fibrosis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^riordan-1989-cftr-cloning]: Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. *Science.* 1989;245(4922):1066-1073. [doi:10.1126/science.2475911](https://doi.org/10.1126/science.2475911) · [PubMed 2475911](https://pubmed.ncbi.nlm.nih.gov/2475911/)
[^heijerman-2019-etd-cf]: Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation. *Lancet.* 2019;394(10212):1940-1948. [doi:10.1016/S0140-6736(19)32597-8](https://doi.org/10.1016/S0140-6736(19)32597-8) · [PubMed 31679946](https://pubmed.ncbi.nlm.nih.gov/31679946/)
