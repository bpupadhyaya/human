---
schema: human-scale-entry/v1
id: tuberous-sclerosis-complex
name: Tuberous Sclerosis Complex
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Tuberous sclerosis complex (TSC) is caused by germline TSC1 or TSC2 mutations; mTOR hyperactivation → hamartomas in brain (cortical tubers, SEGA), kidney (angiomyolipoma), lung (LAM), skin; everolimus/sirolimus FDA-approved; epilepsy and intellectual disability are common."
aliases: ["TSC", "tuberous sclerosis complex", "tuberous sclerosis", "TSC1 syndrome", "TSC2 syndrome", "SEGA TSC", "angiomyolipoma TSC", "LAM TSC", "TSC brain", "TSC epilepsy"]
sources:
  - id: crino-2006-tsc-review
    type: peer-reviewed
    cite: "Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. N Engl J Med. 2006;355(13):1345-1356."
    doi: "10.1056/NEJMra055323"
    pmid: "17005952"
    url: "https://doi.org/10.1056/NEJMra055323"
  - id: northrup-2013-tsc-consensus
    type: peer-reviewed
    cite: "Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. Pediatr Neurol. 2013;49(4):243-254."
    doi: "10.1016/j.pediatrneurol.2013.08.001"
    pmid: "24053982"
    url: "https://doi.org/10.1016/j.pediatrneurol.2013.08.001"
cross_links:
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "Germline TSC1 or TSC2 mutations cause TSC; TSC2 mutations more common (~2/3) and associated with more severe phenotype than TSC1; TSC1-TSC2 complex is the GTPase-activating protein for Rheb; TSC2 is phosphorylated by AKT and AMPK; somatic second hit required in each hamartoma"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "TSC1/TSC2 LOF → mTORC1 hyperactivation → S6K1/4EBP1 → hamartoma growth; everolimus FDA-approved for TSC-associated renal AML, SEGA, and pulmonary LAM; sirolimus used in TSC-LAM (off-label); mTOR inhibitor side effects: stomatitis, infections, hyperlipidemia"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK phosphorylates TSC2 Thr1462 → TSC1-TSC2 GTPase activated → Rheb inhibited → mTORC1 OFF; in TSC, this energy-sensing brake is removed → mTORC1 constitutively ON; AMPK activators (metformin) have theoretical benefit in TSC (downstream AMPK activation bypasses TSC2 LOF)"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "TSC-associated renal tumors: angiomyolipoma (AML; fat+muscle+vessels; embolization or everolimus) and rarely clear cell RCC; everolimus FDA-approved for AML >3 cm at risk of hemorrhage; TSC2 somatic mutation in sporadic RCC = mTOR-sensitive subset"
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "TSC epilepsy affects 80-90% of patients; infantile spasms treated with vigabatrin (~70% ORR); everolimus adjunctive (EXIST-3: 40% vs 22% ≥50% seizure reduction); cannabidiol (Epidiolex; GWPCARE 6: 49% vs 26% reduction); cortical tuber resection for refractory focal seizures."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "~50% of TSC patients have ASD, primarily TSC2 mutations with early severe epilepsy; mTOR hyperactivation → excess synaptic protein translation → abnormal synaptogenesis; rapalogue reverses autism-like behaviors in TSC2+/− mice; ASD severity correlates with cortical tuber burden."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K→AKT→TSC2 phosphorylation is the canonical RTK-to-mTORC1 signal; TSC2 integrates PI3K/AKT, ERK, and AMPK inputs into mTORC1 control; PIK3CA activating mutations in sporadic tumors phenocopy TSC LOF for mTOR; PI3K + mTOR dual inhibitors studied in TSC tumor models."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Tuberous sclerosis and von Hippel-Lindau are both dominant phakomatosis syndromes making multi-organ hamartomas via a second hit, but differ in pathway: TSC1/TSC2 loss unleashes mTORC1 growth while VHL loss unleashes HIF-driven angiogenesis — both converging on renal tumors."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin gives away tuberous sclerosis: hypomelanotic ash-leaf macules, facial angiofibromas, shagreen patches, and periungual fibromas are major diagnostic criteria appearing across childhood — mTOR-driven hamartomatous overgrowth that topical sirolimus now treats."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain defines tuberous sclerosis morbidity: cortical tubers and subependymal nodules form in utero, driving epilepsy (80-90%, often infantile spasms) and neuropsychiatric disorders; a subependymal giant-cell astrocytoma can obstruct CSF, and everolimus shrinks SEGAs."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Tuberous sclerosis and NF1 are neurocutaneous syndromes converging on mTOR: NF1's neurofibromin restrains RAS upstream of mTOR, while TSC1/TSC2 loss directly unleashes mTOR—so both cause skin lesions, brain tumors, and seizures, and respond to mTOR-axis drugs."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Cardiac rhabdomyoma is the hallmark fetal tumor of tuberous sclerosis: benign mTOR-driven masses of glycogen-laden cardiomyocytes often appear before birth, are frequently the first clue to TSC on prenatal ultrasound, and typically regress spontaneously after infancy."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Smooth-muscle proliferation underlies two classic TSC tumors: renal angiomyolipomas and pulmonary lymphangioleiomyomatosis (LAM) are mTOR-driven smooth-muscle-like (PEComa) cells, so LAM causes cystic lung destruction in women with TSC and is treated with sirolimus."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Tuberous sclerosis and Cowden syndrome converge on the PI3K-AKT-mTOR pathway: TSC1/TSC2 loss removes a direct brake on mTOR, while Cowden's PTEN loss disinhibits PI3K upstream—both hyperactivate mTOR, cause hamartomas, and respond to mTOR inhibitors."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Tuberous sclerosis is written into astrocytes: cortical 'tubers' and subependymal giant cell astrocytomas (SEGAs) are dysplastic astrocytic lesions from mTOR overactivation, causing the epilepsy and hydrocephalus of TSC—and SEGAs shrink on mTOR inhibitors."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Tuberous sclerosis and Gorlin syndrome are both autosomal-dominant neurocutaneous tumor syndromes with skin and CNS features but different pathways: TSC from TSC1/2-mTOR overactivation, Gorlin from PTCH1-Hedgehog loss—two phakomatoses, two cascades."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "TSC scrambles brain development at the level of neurons: mTOR overactivity from TSC1/TSC2 loss produces cortical tubers and giant cells with disorganized neurons, driving the epilepsy, autism and developmental delay that dominate the syndrome."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a major TSC target: mTOR-driven angiomyolipomas (fat-and-vessel hamartomas) grow and can hemorrhage, and TSC also raises renal cell carcinoma risk—so renal imaging surveillance and mTOR inhibitors (sirolimus) are central to TSC care."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cardiac rhabdomyomas are often the first sign of TSC: these benign mTOR-driven muscle tumors appear on prenatal or infant echocardiography and usually regress, so a fetal cardiac tumor prompts evaluation for tuberous sclerosis."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "TSC causes lymphangioleiomyomatosis (LAM) in the lung: mTOR-driven smooth-muscle-like cells riddle the lungs with cysts, mainly in women, causing breathlessness and pneumothorax—and like other TSC tumors it responds to mTOR inhibitors (sirolimus)."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "TSC marks the eye with retinal hamartomas: benign astrocytic tumors of the retina are a diagnostic feature, usually harmless to vision but, like the brain tubers, evidence of the same mTOR-driven overgrowth across tissues."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "TSC's brain involvement extends to neuropsychiatric disorders (TAND): beyond epilepsy and autism, ADHD and learning and behavior problems are common and often under-treated, so TSC care now screens for attention and behavioral difficulties routinely."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-D is a biomarker of TSC lung disease: lymphangioleiomyomatosis (LAM) in TSC raises serum VEGF-D, which helps diagnose it and track response, reflecting how mTOR overactivation drives the abnormal vascular and lymphatic growth of the hamartomas."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "TSC's facial angiofibromas are fibroblast-driven hamartomas: mTOR-overactive fibroblasts and vessels proliferate to form the characteristic facial papules, one of the visible skin signs—now treatable with topical mTOR-inhibitor (sirolimus) creams."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "TSC and Birt-Hogg-Dube both cause inherited kidney tumors and lung cysts: TSC makes angiomyolipomas via mTOR, while BHD makes chromophobe/oncocytic tumors via folliculin—distinct genes that overlap in needing renal and pulmonary surveillance."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Tuberous sclerosis writes itself on the skin in collagen: facial angiofibromas and the leathery shagreen patch are collagen-rich connective-tissue hamartomas from mTOR overactivity, among the visible signs that anchor the clinical diagnosis."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Tuberous sclerosis epilepsy stems from disordered glutamate: mTOR hyperactivation distorts the balance of excitatory glutamate and inhibitory signaling in malformed cortex, driving the early, often drug-resistant seizures central to the disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Tuberous sclerosis stalls autophagy through runaway mTOR: with TSC1/2 lost, constant mTOR signaling blocks the cell's self-cleaning, helping hamartoma cells survive—and mTOR inhibitors like everolimus restore autophagy as they shrink the tumors."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Tuberous sclerosis leaves calcium marks in the brain: subependymal nodules along the ventricles calcify and show up on imaging, a hallmark that, with cortical tubers, helps diagnose the mTOR-driven syndrome."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Runaway mTOR in tuberous sclerosis disrupts synapses: excess signaling derails the synaptic protein-making and pruning that circuits need, producing the epilepsy and autism that dominate the disease—targets for mTOR-inhibitor therapy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Tuberous sclerosis sits on the AKT-mTOR growth axis: losing TSC1/2 removes the brake just upstream of mTOR, so AKT-driven signaling runs unchecked to grow hamartomas everywhere—why mTOR inhibitors like everolimus shrink them."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Tuberous sclerosis calcifies the brain with calcium phosphate: its subependymal nodules harden into calcium-phosphate deposits visible on imaging, a diagnostic hallmark of the disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Tuberous sclerosis grows fat-laden tumors: its angiomyolipomas blend adipocytes with vessels and smooth muscle, the fatty component giving these kidney and liver growths their characteristic look."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Tuberous sclerosis reaches the liver: angiomyolipomas, the fatty vascular tumors typical of the kidney, also arise in the liver, extending the hamartoma burden of unchecked mTOR beyond it."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons map tuberous sclerosis everywhere: brain MRI finds the cortical tubers and growing SEGAs, a Wood's lamp's ultraviolet light makes the pale ash-leaf skin spots glow, and echocardiography catches the cardiac rhabdomyomas in infancy."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Unchecked mTOR can grow tumors in the pancreas too: tuberous sclerosis predisposes to pancreatic neuroendocrine tumors, including insulinomas, adding the gland to the long list of organs studded with its hamartomas and growths."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Losing TSC control disturbs the brain's wiring insulation: mTOR overactivity impairs oligodendrocytes and myelination, so white-matter migration lines and hypomyelination accompany the tubers, contributing to the epilepsy and autism."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "TSC's kidney tumors are knots of bad blood vessels: angiomyolipomas mix fat and smooth muscle with malformed, aneurysm-prone vessels lined by abnormal endothelium, and these can rupture into a life-threatening retroperitoneal bleed."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Even the bowel sprouts TSC hamartomas: harmless hamartomatous rectal and colonic polyps are a recognized feature, the same unchecked-mTOR overgrowth that studs the brain, skin, and kidneys appearing along the gut."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "TSC's signature cells look bizarre under the microscope: the giant balloon cells of cortical tubers and SEGAs, and the cardiac rhabdomyoma's 'spider cells', show the swollen, disorganized ultrastructure that electron microscopy reveals."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody marks TSC's odd cells: the perivascular epithelioid cells of renal angiomyolipoma and pulmonary LAM stain for HMB-45, a melanocytic marker that confirms these mTOR-driven tumors, while the mTOR-inhibitor drugs that treat them are themselves immunosuppressive."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "TSC's lung disease is a women's disease: lymphangioleiomyomatosis is estrogen-sensitive and strikes women of reproductive age, and pregnancy can swell both LAM and the kidney angiomyolipomas, making reproductive planning part of care."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The mTOR-inhibitor therapy taxes the marrow and mucosa: everolimus and sirolimus, used to shrink SEGAs and angiomyolipomas, can drop neutrophil counts and cause mouth ulcers, raising the infection risk that comes with long-term mTOR blockade."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "TSC seizures yield to a GABA drug: vigabatrin, which raises brain GABA by blocking its breakdown, is uniquely effective first-line for the infantile spasms of TSC, reflecting the GABAergic imbalance the tubers create in the developing cortex."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Overactive mTOR inflames the brain's resident immune cells: microglia around the cortical tubers turn reactive and help drive the epileptogenic, inflamed circuitry, a process that mTOR inhibitors may calm alongside their effect on the neurons."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "The heaviest TSC burden is often behavioral: TSC-associated neuropsychiatric disorders (TAND) include high rates of anxiety and depression beyond the autism and ADHD, a frequently under-recognized and under-treated dimension of the syndrome."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "One TSC tumor runs on estrogen: lymphangioleiomyomatosis, the lung disease that strikes women with TSC, is fueled by estrogen, which is why it worsens in pregnancy and around the reproductive years — a hormone steering an mTOR-driven tumor."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Runaway mTOR turns on the hypoxia program: unchecked mTORC1 in TSC stabilizes HIF and drives VEGF, helping explain the rich vascularity of its angiomyolipomas and brain tumors and supporting the logic of mTOR-inhibitor therapy."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Immune cells populate its lesions: mast cells and other inflammatory cells infiltrate the lymphangioleiomyomatosis and angiomyolipoma tissue of TSC, contributing to the remodeling of these mTOR-driven growths."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "mTOR pushes growth through STAT3 too: the hyperactive mTORC1 of TSC engages STAT3 signaling that supports proliferation in its tumors, one of the pathways that keeps angiomyolipomas and astrocytomas growing."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "mTOR and NF-κB feed each other in its lesions: TSC's unchecked mTORC1 cross-talks with NF-κB inflammatory signaling, contributing to the chronic inflammation found within its slow-growing growths."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Mood disorder is part of the syndrome: TSC-associated neuropsychiatric disorders (TAND) include high rates of depression alongside autism, ADHD and anxiety, reflecting the mTOR pathway's reach into brain function."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidneys carry the heaviest organ toll: renal angiomyolipomas and cysts (worsened in PKD1 contiguous-gene deletions) progressively destroy nephrons, making chronic kidney disease a leading cause of death in TSC."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Renal lesions drive up the pressure: the angiomyolipomas, cysts and parenchymal loss of TSC kidney disease activate the renin-angiotensin axis, producing hypertension that accelerates the decline in renal function."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its mTOR-inhibitor therapy opens the lung: everolimus and sirolimus used to shrink TSC tumors are immunosuppressive, raising the risk of Pneumocystis pneumonia so that prophylaxis is considered during treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "The same mTOR inhibitors invite invasive mold: the immunosuppression from everolimus and sirolimus, used long-term for TSC tumors, can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its mTOR-inhibitor therapy disturbs glucose: everolimus and sirolimus impair insulin signaling and commonly cause hyperglycemia and hyperlipidemia, sometimes precipitating new-onset diabetes during TSC treatment."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Heart tumors and vessel walls can throw clots: the cardiac rhabdomyomas and arrhythmias of TSC, along with its associated arterial aneurysms, create conditions for embolic and hemorrhagic stroke."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its hamartomas are written on the skin: TSC produces facial angiofibromas, hypopigmented ash-leaf macules, shagreen patches and ungual fibromas — skin findings that are major diagnostic criteria."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can riddle the lungs with cysts: lymphangioleiomyomatosis, a smooth-muscle proliferation that destroys lung tissue into cysts and causes pneumothorax, occurs in women with TSC and responds to mTOR inhibitors."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its mTOR-inhibitor therapy impairs healing: everolimus and sirolimus block the mTOR pathway central to tissue repair, so wounds and the surgery for angiomyolipomas or SEGAs heal slowly during TSC treatment."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is fundamentally a brain disease: cortical tubers, subependymal nodules and SEGAs are central-nervous-system hamartomas that underlie the epilepsy, autism and intellectual disability defining TSC's neurological burden."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It seeds the infant heart with tumours: cardiac rhabdomyomas, often the earliest TSC sign on fetal echo, can obstruct outflow or trigger arrhythmias before usually regressing spontaneously after birth."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It studs the liver with hamartomas: hepatic angiomyolipomas are a recognised extrarenal manifestation of TSC, and its mTOR-inhibitor therapy adds stomatitis and diarrhoea to the gastrointestinal picture."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its lung disease invades the lymphatics: lymphangioleiomyomatosis causes chylous pleural effusions, chylous ascites and lymphangioleiomyomas, lymphatic manifestations beyond its lung cysts."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It leaves quiet marks on bone and mouth: sclerotic bone islands, dental enamel pits and gingival fibromas are common minor diagnostic features of TSC."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It touches the pancreas and metabolism: TSC can cause pancreatic neuroendocrine tumours, and the mTOR-inhibitor therapy for its tumours causes hyperglycaemia and dyslipidaemia."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "mTOR inhibitors are its targeted treatment: because TSC1/TSC2 loss unleashes mTOR, everolimus and sirolimus shrink its brain (SEGA), kidney (angiomyolipoma) and lung (LAM) lesions and reduce seizures."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "A fellow mTOR-pathway tumour syndrome: tuberous sclerosis and MEN1 both produce tumours driven by mTOR-pathway dysregulation, and both respond to the mTOR inhibitors now used across these syndromes."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Both cause syndromic heart tumours: tuberous sclerosis produces cardiac rhabdomyomas while Carney complex produces myxomas, two inherited syndromes presenting with childhood cardiac masses."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "A fellow neurocutaneous syndrome: TSC and NF2 are both phakomatoses — dominantly inherited tumour-suppressor disorders causing nervous-system tumours, though TSC drives mTOR-fuelled hamartomas across many organs while NF2 causes schwannomas and meningiomas."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It cystically destroys the lung: women with TSC develop lymphangioleiomyomatosis, in which mTOR-driven smooth-muscle proliferation riddles the lung with cysts, causing recurrent pneumothorax and progressive breathlessness treated with sirolimus."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "It drives early, hard-to-control epilepsy: cortical tubers make TSC a leading genetic cause of infantile spasms and refractory seizures, and the disrupted hippocampal networks underlie much of the memory and cognitive impairment of TSC-associated neuropsychiatric disorders."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its tumour starts in the fetal heart: cardiac rhabdomyomas, mTOR-driven hamartomas of the myocardium, are often the first sign of tuberous sclerosis on prenatal ultrasound and usually regress after birth."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Lung hamartomas can raise pulmonary pressure: tuberous sclerosis causes lymphangioleiomyomatosis (LAM), whose smooth-muscle proliferation destroys lung tissue and can lead to pulmonary arterial hypertension."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Two hamartoma syndromes converging on mTOR: tuberous sclerosis loses the TSC1/2 brake on mTOR while Peutz-Jeghers loses upstream LKB1-AMPK control of it—different lesions, one overactive growth kinase driving hamartomas."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "An under-recognised tumour: TSC's mTOR hyperactivity also predisposes to pancreatic neuroendocrine tumours, the same lesions for which mTOR inhibitors like everolimus—a TSC drug—are standard therapy."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Contiguous-gene kidney disease: TSC2 sits immediately beside PKD1, so a large deletion removing both genes produces tuberous sclerosis with severe early polycystic kidney disease, cysts distorting the glomeruli decades ahead of schedule."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hamartomas beyond the kidney: fat-containing angiomyolipomas in TSC are not confined to the kidney—they also stud the hepatic lobules, usually benign but part of the same systemic hamartomatosis."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Rhabdomyomas in the fetal heart: cardiac rhabdomyomas, often the first sign of TSC on prenatal ultrasound, disrupt the conduction system to cause arrhythmias and pre-excitation before usually regressing in infancy."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Aneurysms that bleed: renal angiomyolipomas in TSC carry abnormal, fragile arterial walls prone to aneurysm formation and catastrophic retroperitoneal haemorrhage (Wunderlich syndrome) once they grow large."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Sclerotic bone lesions: TSC commonly produces scattered sclerotic foci (bone islands) in the cortical bone of the skull, spine and pelvis, a frequently incidental but characteristic skeletal feature."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "mTOR-driven proliferation: unrestrained mTORC1 from TSC1/TSC2 loss upregulates cyclin D1, driving the proliferation of the hamartomas (SEGA, angiomyolipoma) of tuberous sclerosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Pathway crosstalk: ERK/MAPK signalling crosstalks with the dysregulated mTOR pathway in tuberous sclerosis, contributing to tumour growth and resistance to mTOR inhibitors."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "Cystic lung destruction: in TSC-associated lymphangioleiomyomatosis, proliferating smooth-muscle-like LAM cells destroy the alveolar walls and type II pneumocytes lining them, forming diffuse lung cysts."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "mTOR-driven oncogene: unrestrained mTOR signalling from TSC1/TSC2 loss upregulates MYC, driving the proliferation of the hamartomas and tumours of tuberous sclerosis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor input: IGF-1 signalling feeds the PI3K/AKT/mTOR pathway that is constitutively active in tuberous sclerosis, reinforcing tumour growth."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Tumour stroma: PDGF signalling supports the growth and vascularisation of the angiomyolipomas and other mesenchymal tumours of tuberous sclerosis."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Synaptic dysregulation: mTOR hyperactivation in tuberous sclerosis distorts BDNF-dependent synaptic plasticity and dendritic growth, contributing to the epilepsy and the autism/neuropsychiatric features (TAND) of the disorder."
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "Cell-cycle release: mTORC1-S6K signalling drives degradation of the cell-cycle inhibitor p27 (CDKN1B), and in TSC1/2-deficient cells the loss of this brake contributes to the hamartomatous overgrowth."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Hamartoma fibrosis: TGF-β drives the fibrotic, matrix-rich stroma of the renal angiomyolipomas and the lymphangioleiomyomatosis (LAM) lung lesions of tuberous sclerosis, beyond the direct mTOR-driven proliferation."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Epileptogenesis: dysregulated neuronal calcium and calcineurin-NFAT signalling in the malformed cortical tubers of tuberous sclerosis contributes to the hyperexcitability that makes early-onset, often drug-resistant epilepsy a defining feature of the disorder."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Hamartoma vasculature: angiopoietin-Tie2 signalling supports the abnormal blood vessels of the renal angiomyolipomas — the fat-and-vessel hamartomas prone to aneurysmal haemorrhage — and the remodelled vasculature of pulmonary LAM."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Cytostatic, not curative: mTOR hyperactivation in TSC lesions suppresses caspase-3 apoptosis, so mTOR inhibitors (everolimus, sirolimus) shrink hamartomas only while taken — the tumours regrow on discontinuation because the cells were arrested, not killed."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Convergence on mTOR: PTEN restrains the PI3K-AKT signalling that lies upstream of mTORC1, the same node hyperactivated by TSC1/TSC2 loss, so the two tumour-suppressor systems converge on the mTOR pathway central to tuberous sclerosis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Tumour growth: NOTCH signalling is dysregulated downstream of mTOR hyperactivation in TSC-associated lesions such as subependymal giant cell astrocytomas, contributing to their growth."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Hamartoma macrophages: CCL2 recruits macrophages into TSC hamartomas and lymphangioleiomyomatosis, the inflammatory and lymphangiogenic component of the smooth-muscle lesions that destroy the lung in LAM."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "TSC2 regulation: GSK-3β phosphorylates TSC2 to modulate the TSC complex's restraint of mTORC1 (mTOR mapped), integrating Wnt and AKT inputs into the pathway whose loss drives tuberous sclerosis."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: constitutive mTORC1 activity feeds cyclin-D1 (mapped) and the release of E2F1, driving the cell-cycle entry of the hamartoma cells of tuberous sclerosis."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Metabolic reprogramming: hyperactive mTORC1 drives NRF2-mediated antioxidant and anabolic metabolism in TSC lesions, supporting the growth of their hamartomatous cells."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle output: the RB1-E2F checkpoint (CDKN1B, cyclin-D1 and E2F1 already mapped) operates downstream of the mTOR-driven growth signalling that powers proliferation in TSC hamartomas."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Lesion microenvironment: JAK-STAT3 signalling (STAT3 already mapped) cooperates with mTORC1 hyperactivation in the lymphangioleiomyomatosis and hamartomatous lesions of tuberous sclerosis complex."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS cooperation: RAS-ERK signalling (ERK1/2 already mapped) provides a proliferative input that cooperates with mTORC1 hyperactivation in the hamartomas of tuberous sclerosis complex."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "mTORC1 hyperactivation perturbs autophagy and mitochondrial quality control, and the resulting cytosolic DNA can engage cGAS-STING within the lesions of tuberous sclerosis complex."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of TSC-associated tumours such as angiomyolipoma and lymphangioleiomyomatosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) contributes to the fibrotic and matrix-remodelling component of TSC-associated lesions including pulmonary lymphangioleiomyomatosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "TSC1/TSC2 loss drives mTORC1-AKT activity that inactivates FOXO, removing a growth-restraining, pro-autophagy brake in TSC hamartomas."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 already mapped) sustains the proliferative hamartomatous growth of TSC lesions."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in TSC-associated tumors such as angiomyolipoma and LAM, shaping their inflammatory and fibrotic stroma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in the mTORC1-driven hamartomatous lesions of tuberous sclerosis complex."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory component of the hamartoma and SEGA microenvironment of tuberous sclerosis complex."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of PDGFR (PDGF already mapped) contributes to the proliferative and migratory phenotype of the angiomyolipoma and LAM cells of tuberous sclerosis complex."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the hamartomatous lesions of tuberous sclerosis complex."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the immune context of the tumors of tuberous sclerosis complex."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of the tumors of tuberous sclerosis complex."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the microenvironment of the hamartomas and tumors of tuberous sclerosis complex."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory microenvironment of the tumors of tuberous sclerosis complex."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the cell recruitment and lymphangioleiomyomatosis-associated dissemination in tuberous sclerosis complex."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor/hamartoma microenvironment of tuberous sclerosis complex."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune microenvironment of the lesions of tuberous sclerosis complex."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory and lesion microenvironment of tuberous sclerosis complex."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac rhabdomyoma: the earliest tuberous sclerosis lesion is the cardiac rhabdomyoma, a striated-muscle hamartoma expressing sarcomeric proteins including troponin, often found prenatally and typically regressing after birth."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "Infantile spasms therapy: tuberous sclerosis is a leading cause of infantile spasms, for which ACTH is a first-line hormonal treatment alongside vigabatrin, acting to suppress the epileptic encephalopathy of early infancy."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Sleep and TAND: sleep disturbance is highly prevalent in tuberous sclerosis as part of the associated neuropsychiatric disorder, and melatonin is commonly used to manage the disrupted circadian sleep that compounds epilepsy and behaviour."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "LAM hormone sensitivity: the lymphangioleiomyomatosis of tuberous sclerosis occurs almost only in women and worsens with reproductive hormones, so progesterone and estrogen (already mapped) drive the smooth-muscle proliferation that destroys the lung."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "mTOR-insulin axis: the TSC1-TSC2 complex (already mapped) normally restrains mTORC1 downstream of insulin and growth-factor signalling, so its loss uncouples growth from nutrient and insulin cues, the core metabolic lesion driving the hamartomas."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Angiomyolipoma haemorrhage: the renal angiomyolipomas of tuberous sclerosis can bleed catastrophically into the retroperitoneum, and the resulting acute blood loss drops haemoglobin, a leading cause of morbidity that mTOR inhibitors and embolisation aim to prevent."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Hamartoma vasculature: nitric oxide with the mTOR-driven VEGF and angiopoietin (already mapped) shapes the aberrant, aneurysm-prone vasculature of the angiomyolipomas and other vascular hamartomas of tuberous sclerosis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Hamartoma immune milieu: IL-10 among the cytokines of the tuberous-sclerosis hamartoma microenvironment shapes its immune milieu (IL-6 already mapped), part of the inflammatory dimension of these mTOR-driven lesions."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Metabolic oxidative stress: unrestrained mTORC1 anabolism (already mapped) in the tuberous-sclerosis hamartomas raises metabolic and oxidative stress, to which xanthine oxidase contributes, engaging the NRF2 antioxidant response (already mapped)."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage milieu: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped) in the tuberous-sclerosis hamartomas and the lymphangioleiomyomatosis, part of their immune microenvironment."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "mTOR-driven lipogenesis: the unrestrained mTORC1 (already mapped) of the tuberous-sclerosis hamartomas drives cholesterol and lipid synthesis, the anabolic metabolism that the mTOR inhibitors shrinking the lesions target."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic signalling: the mTOR pathway (already mapped) integrates the metabolic signals of leptin and insulin (already mapped), and its dysregulation in tuberous sclerosis links the hamartoma growth to the anabolic-metabolic state."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Angiomyolipoma haemorrhage: the renal angiomyolipomas of tuberous sclerosis can bleed catastrophically, causing the retroperitoneal haemorrhage and the iron-deficiency anaemia (haemoglobin already mapped) that drive their surveillance and embolisation."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomas of tuberous sclerosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), signals through the mTOR-integrated (already mapped) metabolic pathway whose dysregulation drives the anabolic hamartoma growth of tuberous sclerosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine axis of the mTOR-integrated (already mapped) metabolic dysregulation of the hamartomas of tuberous sclerosis."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Retinal hamartomas: the retinal astrocytic hamartomas of the eye are a diagnostic feature of tuberous sclerosis, part of its multi-organ hamartoma (mTOR already mapped) spectrum."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Renal cancer risk: the tuberous sclerosis (mTOR already mapped) angiomyolipomas of the kidney (already mapped) carry an elevated risk of renal cell carcinoma, requiring surveillance."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "mTOR-interferon crosstalk: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is modulated by the mTOR (already mapped) hyperactivation and shapes the neuroinflammatory microenvironment of the tubers of tuberous sclerosis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the neuroinflammation associated with the epileptogenic cortical tubers of tuberous sclerosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory microenvironment implicated in tuberous sclerosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the tuberous-sclerosis hamartomas."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation of the epileptogenic cortical tubers of tuberous sclerosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of tuberous sclerosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the neuroinflammation of the epileptogenic cortical tubers of tuberous sclerosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) contribute to the adaptive-immune component of the neuroinflammation of the cortical tubers of tuberous sclerosis."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells of the CNS-border compartments present antigen to the T cells (already mapped) of the neuroinflammation of tuberous sclerosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tuber myeloid cells: the macrophages and microglia (already mapped) of the cortical tubers contribute to the neuroinflammation implicated in the epilepsy of tuberous sclerosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tuber complement: the complement C3 activation, part of the neuroinflammation of the cortical tubers, contributes to the aberrant synaptic pruning implicated in the epilepsy of tuberous sclerosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation of the cortical tubers of tuberous sclerosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "mTOR-driven alarmin: TSLP expression is amplified by mTORC1 (TSC1/TSC2 already mapped) over-activation in TSC-LAM cells and airway hamartomas, activating mast cells (already mapped) and dendritic cells (already mapped) in the TSC pulmonary microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell effector: histamine released by mast cells (already mapped) in the TSC-LAM lung and skin angiofibromas (skin already mapped) amplifies local type-2 immunity and the angiogenesis (VEGF already mapped) within the hamartoma stroma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Hamartoma ECM: periostin, an ECM glycoprotein downstream of mTORC1 (TSC1/TSC2 already mapped) and TGF-β (already mapped) signalling, contributes to the desmoplastic and invasive extracellular matrix of renal angiomyolipomas and the pulmonary-LAM lesions of tuberous sclerosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin LAM-microenvironment mediator: bradykinin, generated by the kallikrein-kinin system in the TSC-LAM pulmonary microenvironment, amplifies vascular permeability and the mast-cell (already mapped) and endothelial activation of the TSC-LAM lung."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact brake: C1-esterase inhibitor restrains the classical complement C1 and contact system (C3/C5aR1 already mapped) activated in the neuroinflammation of cortical tubers and the TSC renal angiomyolipoma stroma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "TSC-RCC and EPO signalling: erythropoietin and EPOR signalling are relevant to the renal cell carcinoma (already mapped) risk and the polycythaemia associated with renal angiomyolipomas of tuberous sclerosis complex."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "TSC testosterone: androgen receptor signalling modulates mTOR (already mapped) pathway activity in tuberous sclerosis; testosterone may amplify mTOR-driven hamartoma growth in renal angiomyolipomas, and androgen-deprivation therapy reduces angiomyolipoma progression in TSC."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "TSC serotonin: serotonin signalling is dysregulated in the autism spectrum disorder complicating tuberous sclerosis; mTOR (already mapped) hyperactivation in TSC neurons impairs serotonergic neurotransmission, and SSRI treatment addresses the associated behavioural symptoms."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "TSC prolactin: prolactin modulates cortical-tuber neuroinflammation in tuberous sclerosis via immunomodulatory effects on microglia (already mapped); prolactin-driven astrocyte (already mapped) activation amplifies the seizure susceptibility of TSC cortical dysplasia."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "TSC oxytocin: oxytocin receptor-cAMP/PKA signalling on TSC neurons attenuates mTOR (already mapped) hyperactivation downstream of TSC1/TSC2 (already mapped) loss-of-function; oxytocin also modulates the autism spectrum and social-behaviour deficits of tuberous sclerosis complex."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "TSC vasopressin: vasopressin V1A receptors on TSC neurons intersect mTOR (already mapped)/S6K signalling, modulating synaptic plasticity and the epileptic activity of cortical tubers; V1A-mediated calcium signalling may amplify TSC seizure susceptibility."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "TSC selenium: selenium-dependent GPX suppresses oxidative stress and NF-κB (already mapped)-mediated neuroinflammation in TSC cortical tubers; selenium deficiency worsens mTOR (already mapped)-driven VEGF (already mapped) upregulation and angiomyolipoma growth in TSC."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "TSC iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies mTOR (already mapped) and VEGF (already mapped) hamartoma growth and NF-κB (already mapped) neuroinflammation of TSC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "TSC sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped)-driven hamartoma cascade of TSC."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "TSC magnesium: magnesium, as mTOR (already mapped) kinase cofactor in neurons (already mapped) and astrocytes (already mapped), supports synaptic function; magnesium deficiency amplifies NF-κB (already mapped) neuroinflammation and IL-6 (already mapped) cascade of TSC epilepsy."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "TSC copper: copper-dependent SOD in neurons (already mapped) and astrocytes (already mapped) quenches mTOR (already mapped)-driven ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and hamartoma growth of TSC."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "TSC zinc: zinc, as mTOR (already mapped) kinase cofactor in neurons (already mapped) and astrocytes (already mapped), supports synaptic transmission; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) seizure susceptibility and hamartoma growth of TSC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "TSC potassium: potassium efflux in neurons (already mapped) and astrocytes (already mapped) modulates seizure threshold; potassium dysregulation amplifies mTOR (already mapped) and NF-κB (already mapped) cortical excitability and hamartoma cascade of TSC."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "TSC carbon: carbon, as metabolic backbone of mTOR (already mapped) lipid synthesis in neurons (already mapped) and astrocytes (already mapped), drives hamartoma growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of TSC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "TSC chloride: chloride channels in neurons (already mapped) and astrocytes (already mapped) modulate seizure threshold; chloride dysregulation amplifies mTOR (already mapped) and NF-κB (already mapped) cortical excitability and hamartoma cascade of TSC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "TSC hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and astrocytes (already mapped), quenches ROS from mTOR (already mapped) overactivation; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) seizure cascade of TSC."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "TSC nitrogen: nitric oxide from macrophages (already mapped) and neurons (already mapped) modulates mTOR-driven vascular tone; nitrogen imbalance amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "TSC oxygen: reactive oxygen species in macrophages (already mapped) and neurons (already mapped) drive mTOR-linked oxidative stress; oxygen imbalance amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "TSC sulfur: hydrogen sulfide from macrophages (already mapped) and neurons (already mapped) modulates mTOR-driven vascular tone; sulfur deficiency amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex."
---

# Tuberous Sclerosis Complex

## Overview

**Tuberous sclerosis complex (TSC)** is an autosomal dominant multisystem hamartoma syndrome caused by germline pathogenic variants in **TSC1** (hamartin; chromosome 9q34) or **TSC2** (tuberin; chromosome 16p13.3), which together form a GTPase-activating protein (GAP) complex that restrains **mTORC1** (mechanistic target of rapamycin complex 1) activity. Loss of TSC1 or TSC2 → Rheb-GTP → mTORC1 constitutively active → uncontrolled cell growth → hamartomas (benign tumor-like growths composed of disorganized but differentiated tissue) in multiple organ systems. TSC affects approximately 1 in 6,000 newborns worldwide (~50,000 patients in the USA) and is characterized by hamartomas in the **brain** (cortical tubers, subependymal nodules, SEGAs), **kidneys** (angiomyolipomas, cysts), **lungs** (LAM in women), **skin** (ash-leaf spots, angiofibromas, shagreen patches), **heart** (rhabdomyomas), and **eyes** (retinal hamartomas). Neurological manifestations — epilepsy (80-90% of TSC patients) and TSC-associated neuropsychiatric disorders (TAND) including autism spectrum disorder and intellectual disability — dominate morbidity. **Everolimus** (mTOR inhibitor) is FDA-approved for TSC-associated renal AML, SEGA, pulmonary LAM, and adjunctive epilepsy treatment [^crino-2006-tsc-review] [^northrup-2013-tsc-consensus].

**Epidemiology:**
- Prevalence: 1/6,000 live births; ~1.5-2 million patients worldwide; ~50,000 in the USA
- TSC1:TSC2 ratio: TSC1 germline ~33%, TSC2 germline ~67% (of patients with identifiable germline variant)
- De novo mutations: ~66-75% of TSC cases (no family history); high spontaneous mutation rate
- Mosaic TSC: ~15-20% of TSC patients without identifiable germline variant; somatic mosaicism (allele fraction 2-15%); milder phenotype; detected by sensitive NGS or analysis of multiple tissues
- Life expectancy: historically reduced; with modern management (anti-seizure + everolimus), approaching normal; major causes of death: renal hemorrhage from AML, status epilepticus, respiratory failure from LAM

**TSC diagnostic criteria (Northrup 2013):** [^northrup-2013-tsc-consensus]
Definite TSC: 2 major features OR 1 major + ≥2 minor features
- **Major features**: hypomelanotic macules (≥3, ≥5 mm), angiofibromas (≥3) or fibrous cephalic plaque, ungual fibromas (≥2), shagreen patch, multiple retinal hamartomas, cortical dysplasias (cortical tubers or white matter radial migration lines), subependymal nodule (SEN), SEGA, cardiac rhabdomyoma, lymphangioleiomyomatosis (LAM), angiomyolipoma (≥2)
- **Minor features**: "confetti" skin lesions, dental enamel pits (≥3), intraoral fibromas (≥2), retinal achromic patch, multiple renal cysts, nonrenal hamartomas
- **Pathognomonic**: TSC1 or TSC2 pathogenic variant = definite TSC regardless of clinical features

## Structure

### Molecular basis: TSC1-TSC2-Rheb-mTORC1 axis

**TSC1-TSC2 function:**
TSC1 (hamartin) stabilizes TSC2; TSC2 (tuberin) acts as GAP for Rheb → hydrolyzes Rheb-GTP → Rheb-GDP → mTORC1 inactive; germline TSC1 or TSC2 pathogenic variant → haploinsufficient state in all cells → somatic second hit in individual progenitor cells → biallelic TSC LOF → Rheb-GTP → mTORC1 constitutively active → hamartoma

**Upstream regulators of TSC1-TSC2:**
- **AKT** (activated by PI3K/RTK): phosphorylates TSC2 → INHIBITS TSC2 → mTOR ON (growth factor signal)
- **AMPK** (activated by energy depletion, STK11/LKB1): phosphorylates TSC2 → ACTIVATES TSC2 → mTOR OFF (energy stress signal)
- **ERK** (activated by RAS/MAPK): phosphorylates TSC2 → INHIBITS → mTOR ON (proliferative signal)

**mTORC1 consequences in TSC:**
S6K1 (ribosome biogenesis, cell size) + 4EBP1 (cap-dependent translation, HIF-1α, VEGF) + ULK1 inhibition (autophagy suppressed) → cell growth, proliferation, angiogenesis; in TSC cells: feedback loop — mTORC1 → S6K1 → IRS-1 phosphorylation (serine) → IRS-1 degradation → reduced PI3K/AKT input → lower AKT activity in TSC cells (paradoxical); this feedback explains why rapalogue withdrawal → rebound mTOR activity

### TSC manifestations by organ

**Brain:**
Cortical tubers: focal areas of cortical dysplasia with giant cells and dysmorphic neurons; present in ~90% of TSC patients; epileptogenic; number and location correlate with seizure severity and cognitive outcome; appear as T2-hyperintense cortical/subcortical lesions on MRI; calcification common; non-enhancing; histology: loss of cortical lamination, balloon cells (large dysmorphic neurons/astrocytes expressing vimentin)

Subependymal nodules (SENs): calcified nodules along ventricular walls; asymptomatic; appear in early childhood; distinguish from SEGA by lack of growth; "candle-dripping" appearance on MRI (FLAIR/T2 hypointense, calcified)

Subependymal giant cell astrocytoma (SEGA): low-grade astrocytic tumor (WHO Grade 1) arising from subependymal nodule at foramen of Monro; occurs in ~10-15% of TSC patients; progressive growth → obstructive hydrocephalus; may cause sudden neurological deterioration; contrast-enhancing on MRI (unlike SEN); usually age 5-20 years; treatment: everolimus or surgical resection

Radial migration lines (white matter hamartomata): T2-hyperintense subcortical bands extending from periventricular to cortical surface; not epileptogenic in isolation; marker of fetal migration abnormality in TSC

**Kidney:**
Angiomyolipoma (AML): benign hamartoma composed of abnormal blood vessels + smooth muscle + mature adipose tissue; present in ~80% of TSC patients; typically bilateral and multifocal; triphasic CT/MRI (fat, muscle, vascularity) is diagnostic; fat-poor AML may be mistaken for RCC; risk: hemorrhage (Wunderlich syndrome) → spontaneous retroperitoneal hemorrhage → life-threatening; hemorrhage risk increases with size (>3-4 cm) and aneurysm formation; treatment: prophylactic embolization or everolimus for large AML (>3 cm or growing)

TSC-associated RCC: <5% of TSC patients develop RCC; histology variable (clear cell, chromophobe, unclassified); often younger age; treated as sporadic RCC; everolimus may have activity

Renal cysts: ~30-50% of TSC patients; usually small; renal insufficiency rare; TSC2-PKD1 contiguous deletion → polycystic kidney disease

**Lung:**
Lymphangioleiomyomatosis (LAM): proliferation of TSC2-deficient smooth muscle-like cells (LAM cells) in lungs and lymphatics; occurs almost exclusively in women (~50-80% of TSC women); sporadic LAM also exists (only women; somatic TSC2 mutations); symptoms: dyspnea, recurrent pneumothorax (30-40%), chylothorax; HRCT: diffuse bilateral thin-walled cysts (2-5 mm) throughout both lungs; PFTs: obstructive pattern with air trapping; serum VEGF-D (>800 pg/mL): elevated in LAM → diagnostic biomarker; lymph node or pulmonary biopsy: LAM cells (HMB-45+, smooth muscle actin+, PR+); treatment: sirolimus (FDA-approved for LAM, 2015)

**Skin:**
- **Hypomelanotic macules (ash-leaf spots)**: most common TSC skin finding (>90%); present from birth; 5-20 mm depigmented macules (not true vitiligo — melanocytes present but defective); best seen under Wood's lamp (UV); diagnostic major feature
- **Angiofibromas**: malar distribution (butterfly-shaped); 2-5 mm red-pink papules; appear in childhood/adolescence; caused by TSC-deficient fibroblast proliferation + vascularization; treatment: laser (Nd:YAG, CO2), topical sirolimus (approved for facial angiofibromas in TSC, 2022)
- **Shagreen patch**: connective tissue nevus; thickened, orange-peel textured plaque; lumbosacral region; fibrous hamartoma
- **Fibrous cephalic plaque**: irregular fibrous plaque on forehead or scalp; firm, elevated; major diagnostic criterion
- **Ungual fibromas (Koenen tumors)**: periungual or subungual fibromas; appear at puberty; toenails more common than fingernails; painful; surgical removal or laser

**Heart:**
Cardiac rhabdomyomas: most common benign cardiac tumor in children; present in ~50-60% of fetuses/neonates with TSC2 mutations; frequently multiple; located in ventricular walls or septum; may cause outflow obstruction, arrhythmias, or hydrops fetalis; regress spontaneously with age (largely resolve by age 6-10 years without treatment); everolimus may accelerate regression (used in severe fetal/neonatal cases); echocardiography for all newborns with suspected TSC

**Eye:**
Retinal hamartomas (astrocytic hamartomas): flat or elevated white/yellowish lesions; present in ~40-50% of TSC; typically bilateral; calcified (mulberry lesion) or non-calcified (salmon-patch); usually asymptomatic; giant astrocytic hamartoma rarely causes visual impairment

## Function

### TSC-associated neuropsychiatric disorders (TAND)

**Epilepsy in TSC (80-90% of TSC patients):**
- Onset: typically <1 year of age (60% in first year); infantile spasms (IS) most common early presentation; untreated IS → hypsarrhythmia → West syndrome → developmental regression
- Seizure types: infantile spasms, focal seizures, tonic, atonic, absence, rarely GTC
- TSC2 mutations → more cortical tubers → more severe epilepsy than TSC1
- Treatment:
  - Vigabatrin (GABA transaminase inhibitor): first-line for TSC-associated infantile spasms; ORR ~70-80% for IS; visual field restriction toxicity (irreversible; requires visual field testing every 3-6 months)
  - ACTH: alternative first-line for IS (non-vigabatrin approach)
  - Everolimus adjunctive (EXIST-3): ≥50% seizure frequency reduction in 40% vs 22% placebo; approved adjunctive for focal-onset seizures in TSC ≥2 years
  - Cannabidiol (Epidiolex): FDA-approved for TSC-associated seizures (GWPCARE 6 trial: 49% seizure reduction vs 26% placebo); oral CBD solution; for patients ≥1 year
  - Surgical: resection of epileptogenic cortical tuber (identified by MEG, EEG dipole localization, stereoEEG); 50% seizure freedom in selected patients

**TSC-associated neuropsychiatric disorders (TAND):**
Autism spectrum disorder (ASD): ~50% of TSC patients; diagnosed primarily in those with TSC2 mutations and early severe epilepsy; mTOR hyperactivation → synaptic protein overexpression → abnormal synaptic plasticity → autism-related behaviors
Intellectual disability (ID): ~50% of TSC patients; primarily severe in TSC2, milder in TSC1; correlated with cortical tuber burden and seizure onset age
Neuropsychiatric: anxiety, depression, ADHD, OCD, sleep disorders — common in TSC
Behavioral: aggressive behaviors in non-verbal TSC patients with ID

## Pathology

### Diagnosis and surveillance

**Genetic testing:**
- TSC1 + TSC2 comprehensive sequencing + deletion analysis (MLPA): ~85-90% sensitivity in clinically diagnosed TSC; 10-15% remain genetically unsolved (somatic mosaicism, non-coding variants)
- TSC1 NM_000368 (9q34): 23 exons; TSC2 NM_000548 (16p13.3): 41 exons
- TSC2-PKD1 contiguous gene deletion: chromosome 16p13.3 deletion; severe early-onset PKD + TSC; diagnosed by chromosomal microarray

**Surveillance schedule (2012 Consensus/NCCN TSC):** [^northrup-2013-tsc-consensus]
- Brain MRI: every 1-3 years for SEGA (foramen of Monro); more frequently if prior rapid growth; non-enhancing SENs = observe; SEGA enhancing and growing = everolimus or surgery
- Abdominal MRI: every 1-3 years for renal AML and cysts; immediately if symptomatic
- Echocardiogram + EKG: at diagnosis; annually in children while rhabdomyomas present; adults as clinically indicated
- Pulmonary HRCT: at baseline (age 18 years for women; earlier if symptomatic); VEGF-D serum level; if LAM present: PFTs every 6-12 months
- Ophthalmology: at diagnosis; annually in children; as needed in adults
- Dermatology: at diagnosis; annually for new/growing lesions
- Neuropsychological assessment: at diagnosis; every 3 years or at educational transitions
- EEG: at diagnosis; as clinically indicated for seizure changes

### Treatment

**Renal AML:** [^crino-2006-tsc-review]
- AML <3 cm and asymptomatic: surveillance every 1-3 years; no intervention
- AML ≥3 cm or growing: preventive intervention
  - **Everolimus**: EXIST-2 Phase 3 (AML ≥3 cm): AML volume response 42% vs 0%; sustained responses; standard for TSC-associated AML; indefinite treatment (lesions regrow on discontinuation)
  - **Embolization** (selective arterial embolization): for acute hemorrhage (Wunderlich syndrome) or for growing AML in patients intolerant of everolimus; highly effective for hemorrhage control; tumor shrinkage temporary; re-embolization may be required
  - **Surgery**: reserved for isolated renal lesions when embolization fails or RCC cannot be excluded; nephron-sparing approach preferred

**SEGA:**
- Asymptomatic, small (≤1 cm), stable: MRI surveillance every 1-3 years
- Growing SEGA or symptomatic (obstructive hydrocephalus): treatment required
  - **Everolimus** (EXIST-1): 35% reduction in SEGA volume vs 0% placebo; prevents hydrocephalus progression; first-line for unresectable or bilateral SEGA; surgical risk reduction
  - **Surgical resection**: for SEGA with acute hydrocephalus requiring emergent drainage; craniotomy; complete resection preferred if surgically accessible; no adjuvant therapy needed for complete resection (tumor suppressor, no malignancy)
  - **CSF shunting**: ventriculoperitoneal shunt for hydrocephalus if surgery not immediately feasible; temporary measure

**Pulmonary LAM:**
- Sirolimus (rapamycin): MILES trial Phase 3: FEV1 stabilization during treatment (−12 mL/year sirolimus vs −134 mL/year placebo); FDA-approved for LAM (2015); regrowth after discontinuation; indefinite treatment in progressive LAM
- Bronchodilators: for symptomatic obstruction (20-40% of LAM patients respond)
- Pleurodesis: for recurrent pneumothorax (bilateral pleurodesis preferred in TSC-LAM to prevent recurrence on both sides)
- Lung transplantation: for end-stage respiratory failure; TSC-LAM does not recur in transplanted lung (LAM cells in circulation but require local mTOR activation to establish); acceptable outcomes

**Skin:**
- Topical sirolimus (0.1% cream or ointment): FDA-approved for facial angiofibromas in TSC (2022); applied daily; significant improvement in angiofibroma volume; well tolerated topically
- Laser: Nd:YAG or CO2 laser for angiofibromas; vascular IPL for erythema

**Prognosis:**
With modern management: life expectancy increasingly normal; major risks: renal AML hemorrhage (embolization/everolimus mitigates), LAM respiratory failure (sirolimus delays but not prevents), status epilepticus (antiseizure + vigabatrin), SEGA hydrocephalus (everolimus/surgery); intellectual disability and autism remain the dominant long-term challenges; ~40% of TSC patients have normal cognition and near-normal quality of life

## Connections

- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — Germline TSC1 or TSC2 mutations cause TSC; TSC2 mutations more common (~2/3) and associated with more severe phenotype than TSC1; TSC1-TSC2 complex is the GTPase-activating protein for Rheb; TSC2 is phosphorylated by AKT and AMPK; somatic second hit required in each hamartoma
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TSC1/TSC2 LOF → mTORC1 hyperactivation → S6K1/4EBP1 → hamartoma growth; everolimus FDA-approved for TSC-associated renal AML, SEGA, and pulmonary LAM; sirolimus used in TSC-LAM (off-label); mTOR inhibitor side effects: stomatitis, infections, hyperlipidemia
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK phosphorylates TSC2 Thr1462 → TSC1-TSC2 GTPase activated → Rheb inhibited → mTORC1 OFF; in TSC, this energy-sensing brake is removed → mTORC1 constitutively ON; AMPK activators (metformin) have theoretical benefit in TSC (downstream AMPK activation bypasses TSC2 LOF)
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — TSC-associated renal tumors: angiomyolipoma (AML; fat+muscle+vessels; embolization or everolimus) and rarely clear cell RCC; everolimus FDA-approved for AML >3 cm at risk of hemorrhage; TSC2 somatic mutation in sporadic RCC = mTOR-sensitive subset
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — TSC epilepsy affects 80-90% of patients; infantile spasms treated with vigabatrin (~70% ORR); everolimus adjunctive (EXIST-3: 40% vs 22% ≥50% seizure reduction); cannabidiol (Epidiolex; GWPCARE 6: 49% vs 26% reduction); cortical tuber resection for refractory focal seizures.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — ~50% of TSC patients have ASD, primarily TSC2 mutations with early severe epilepsy; mTOR hyperactivation → excess synaptic protein translation → abnormal synaptogenesis; rapalogue reverses autism-like behaviors in TSC2+/− mice; ASD severity correlates with cortical tuber burden.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K→AKT→TSC2 phosphorylation is the canonical RTK-to-mTORC1 signal; TSC2 integrates PI3K/AKT, ERK, and AMPK inputs into mTORC1 control; PIK3CA activating mutations in sporadic tumors phenocopy TSC LOF for mTOR; PI3K + mTOR dual inhibitors studied in TSC tumor models.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Tuberous sclerosis and von Hippel-Lindau are both dominant phakomatosis syndromes making multi-organ hamartomas via a second hit, but differ in pathway: TSC1/TSC2 loss unleashes mTORC1 growth while VHL loss unleashes HIF-driven angiogenesis — both converging on renal tumors.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin gives away tuberous sclerosis: hypomelanotic ash-leaf macules, facial angiofibromas, shagreen patches, and periungual fibromas are major diagnostic criteria appearing across childhood — mTOR-driven hamartomatous overgrowth that topical sirolimus now treats.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain defines tuberous sclerosis morbidity: cortical tubers and subependymal nodules form in utero, driving epilepsy (80-90%, often infantile spasms) and neuropsychiatric disorders; a subependymal giant-cell astrocytoma can obstruct CSF, and everolimus shrinks SEGAs.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Tuberous sclerosis and NF1 are neurocutaneous syndromes converging on mTOR: NF1's neurofibromin restrains RAS upstream of mTOR, while TSC1/TSC2 loss directly unleashes mTOR—so both cause skin lesions, brain tumors, and seizures, and respond to mTOR-axis drugs.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Cardiac rhabdomyoma is the hallmark fetal tumor of tuberous sclerosis: benign mTOR-driven masses of glycogen-laden cardiomyocytes often appear before birth, are frequently the first clue to TSC on prenatal ultrasound, and typically regress spontaneously after infancy.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Smooth-muscle proliferation underlies two classic TSC tumors: renal angiomyolipomas and pulmonary lymphangioleiomyomatosis (LAM) are mTOR-driven smooth-muscle-like (PEComa) cells, so LAM causes cystic lung destruction in women with TSC and is treated with sirolimus.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Tuberous sclerosis and Cowden syndrome converge on the PI3K-AKT-mTOR pathway: TSC1/TSC2 loss removes a direct brake on mTOR, while Cowden's PTEN loss disinhibits PI3K upstream—both hyperactivate mTOR, cause hamartomas, and respond to mTOR inhibitors.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Tuberous sclerosis is written into astrocytes: cortical 'tubers' and subependymal giant cell astrocytomas (SEGAs) are dysplastic astrocytic lesions from mTOR overactivation, causing the epilepsy and hydrocephalus of TSC—and SEGAs shrink on mTOR inhibitors.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Tuberous sclerosis and Gorlin syndrome are both autosomal-dominant neurocutaneous tumor syndromes with skin and CNS features but different pathways: TSC from TSC1/2-mTOR overactivation, Gorlin from PTCH1-Hedgehog loss—two phakomatoses, two cascades.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — TSC scrambles brain development at the level of neurons: mTOR overactivity from TSC1/TSC2 loss produces cortical tubers and giant cells with disorganized neurons, driving the epilepsy, autism and developmental delay that dominate the syndrome.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a major TSC target: mTOR-driven angiomyolipomas (fat-and-vessel hamartomas) grow and can hemorrhage, and TSC also raises renal cell carcinoma risk—so renal imaging surveillance and mTOR inhibitors (sirolimus) are central to TSC care.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cardiac rhabdomyomas are often the first sign of TSC: these benign mTOR-driven muscle tumors appear on prenatal or infant echocardiography and usually regress, so a fetal cardiac tumor prompts evaluation for tuberous sclerosis.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — TSC causes lymphangioleiomyomatosis (LAM) in the lung: mTOR-driven smooth-muscle-like cells riddle the lungs with cysts, mainly in women, causing breathlessness and pneumothorax—and like other TSC tumors it responds to mTOR inhibitors (sirolimus).
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — TSC marks the eye with retinal hamartomas: benign astrocytic tumors of the retina are a diagnostic feature, usually harmless to vision but, like the brain tubers, evidence of the same mTOR-driven overgrowth across tissues.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — TSC's brain involvement extends to neuropsychiatric disorders (TAND): beyond epilepsy and autism, ADHD and learning and behavior problems are common and often under-treated, so TSC care now screens for attention and behavioral difficulties routinely.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-D is a biomarker of TSC lung disease: lymphangioleiomyomatosis (LAM) in TSC raises serum VEGF-D, which helps diagnose it and track response, reflecting how mTOR overactivation drives the abnormal vascular and lymphatic growth of the hamartomas.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — TSC's facial angiofibromas are fibroblast-driven hamartomas: mTOR-overactive fibroblasts and vessels proliferate to form the characteristic facial papules, one of the visible skin signs—now treatable with topical mTOR-inhibitor (sirolimus) creams.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — TSC and Birt-Hogg-Dube both cause inherited kidney tumors and lung cysts: TSC makes angiomyolipomas via mTOR, while BHD makes chromophobe/oncocytic tumors via folliculin—distinct genes that overlap in needing renal and pulmonary surveillance.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Tuberous sclerosis writes itself on the skin in collagen: facial angiofibromas and the leathery shagreen patch are collagen-rich connective-tissue hamartomas from mTOR overactivity, among the visible signs that anchor the clinical diagnosis.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Tuberous sclerosis epilepsy stems from disordered glutamate: mTOR hyperactivation distorts the balance of excitatory glutamate and inhibitory signaling in malformed cortex, driving the early, often drug-resistant seizures central to the disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Tuberous sclerosis stalls autophagy through runaway mTOR: with TSC1/2 lost, constant mTOR signaling blocks the cell's self-cleaning, helping hamartoma cells survive—and mTOR inhibitors like everolimus restore autophagy as they shrink the tumors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Tuberous sclerosis leaves calcium marks in the brain: subependymal nodules along the ventricles calcify and show up on imaging, a hallmark that, with cortical tubers, helps diagnose the mTOR-driven syndrome.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Runaway mTOR in tuberous sclerosis disrupts synapses: excess signaling derails the synaptic protein-making and pruning that circuits need, producing the epilepsy and autism that dominate the disease—targets for mTOR-inhibitor therapy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Tuberous sclerosis sits on the AKT-mTOR growth axis: losing TSC1/2 removes the brake just upstream of mTOR, so AKT-driven signaling runs unchecked to grow hamartomas everywhere—why mTOR inhibitors like everolimus shrink them.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Tuberous sclerosis calcifies the brain with calcium phosphate: its subependymal nodules harden into calcium-phosphate deposits visible on imaging, a diagnostic hallmark of the disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Tuberous sclerosis grows fat-laden tumors: its angiomyolipomas blend adipocytes with vessels and smooth muscle, the fatty component giving these kidney and liver growths their characteristic look.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Tuberous sclerosis reaches the liver: angiomyolipomas, the fatty vascular tumors typical of the kidney, also arise in the liver, extending the hamartoma burden of unchecked mTOR beyond it.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons map tuberous sclerosis everywhere: brain MRI finds the cortical tubers and growing SEGAs, a Wood's lamp's ultraviolet light makes the pale ash-leaf skin spots glow, and echocardiography catches the cardiac rhabdomyomas in infancy.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Unchecked mTOR can grow tumors in the pancreas too: tuberous sclerosis predisposes to pancreatic neuroendocrine tumors, including insulinomas, adding the gland to the long list of organs studded with its hamartomas and growths.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Losing TSC control disturbs the brain's wiring insulation: mTOR overactivity impairs oligodendrocytes and myelination, so white-matter migration lines and hypomyelination accompany the tubers, contributing to the epilepsy and autism.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — TSC's kidney tumors are knots of bad blood vessels: angiomyolipomas mix fat and smooth muscle with malformed, aneurysm-prone vessels lined by abnormal endothelium, and these can rupture into a life-threatening retroperitoneal bleed.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Even the bowel sprouts TSC hamartomas: harmless hamartomatous rectal and colonic polyps are a recognized feature, the same unchecked-mTOR overgrowth that studs the brain, skin, and kidneys appearing along the gut.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — TSC's signature cells look bizarre under the microscope: the giant balloon cells of cortical tubers and SEGAs, and the cardiac rhabdomyoma's 'spider cells', show the swollen, disorganized ultrastructure that electron microscopy reveals.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody marks TSC's odd cells: the perivascular epithelioid cells of renal angiomyolipoma and pulmonary LAM stain for HMB-45, a melanocytic marker that confirms these mTOR-driven tumors, while the mTOR-inhibitor drugs that treat them are themselves immunosuppressive.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — TSC's lung disease is a women's disease: lymphangioleiomyomatosis is estrogen-sensitive and strikes women of reproductive age, and pregnancy can swell both LAM and the kidney angiomyolipomas, making reproductive planning part of care.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The mTOR-inhibitor therapy taxes the marrow and mucosa: everolimus and sirolimus, used to shrink SEGAs and angiomyolipomas, can drop neutrophil counts and cause mouth ulcers, raising the infection risk that comes with long-term mTOR blockade.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — TSC seizures yield to a GABA drug: vigabatrin, which raises brain GABA by blocking its breakdown, is uniquely effective first-line for the infantile spasms of TSC, reflecting the GABAergic imbalance the tubers create in the developing cortex.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Overactive mTOR inflames the brain's resident immune cells: microglia around the cortical tubers turn reactive and help drive the epileptogenic, inflamed circuitry, a process that mTOR inhibitors may calm alongside their effect on the neurons.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — The heaviest TSC burden is often behavioral: TSC-associated neuropsychiatric disorders (TAND) include high rates of anxiety and depression beyond the autism and ADHD, a frequently under-recognized and under-treated dimension of the syndrome.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — One TSC tumor runs on estrogen: lymphangioleiomyomatosis, the lung disease that strikes women with TSC, is fueled by estrogen, which is why it worsens in pregnancy and around the reproductive years — a hormone steering an mTOR-driven tumor.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Runaway mTOR turns on the hypoxia program: unchecked mTORC1 in TSC stabilizes HIF and drives VEGF, helping explain the rich vascularity of its angiomyolipomas and brain tumors and supporting the logic of mTOR-inhibitor therapy.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Immune cells populate its lesions: mast cells and other inflammatory cells infiltrate the lymphangioleiomyomatosis and angiomyolipoma tissue of TSC, contributing to the remodeling of these mTOR-driven growths.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — mTOR pushes growth through STAT3 too: the hyperactive mTORC1 of TSC engages STAT3 signaling that supports proliferation in its tumors, one of the pathways that keeps angiomyolipomas and astrocytomas growing.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — mTOR and NF-κB feed each other in its lesions: TSC's unchecked mTORC1 cross-talks with NF-κB inflammatory signaling, contributing to the chronic inflammation found within its slow-growing growths.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Mood disorder is part of the syndrome: TSC-associated neuropsychiatric disorders (TAND) include high rates of depression alongside autism, ADHD and anxiety, reflecting the mTOR pathway's reach into brain function.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidneys carry the heaviest organ toll: renal angiomyolipomas and cysts (worsened in PKD1 contiguous-gene deletions) progressively destroy nephrons, making chronic kidney disease a leading cause of death in TSC.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Renal lesions drive up the pressure: the angiomyolipomas, cysts and parenchymal loss of TSC kidney disease activate the renin-angiotensin axis, producing hypertension that accelerates the decline in renal function.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its mTOR-inhibitor therapy opens the lung: everolimus and sirolimus used to shrink TSC tumors are immunosuppressive, raising the risk of Pneumocystis pneumonia so that prophylaxis is considered during treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — The same mTOR inhibitors invite invasive mold: the immunosuppression from everolimus and sirolimus, used long-term for TSC tumors, can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its mTOR-inhibitor therapy disturbs glucose: everolimus and sirolimus impair insulin signaling and commonly cause hyperglycemia and hyperlipidemia, sometimes precipitating new-onset diabetes during TSC treatment.
- `connects-to` → **[Stroke](../stroke/README.md)** — Heart tumors and vessel walls can throw clots: the cardiac rhabdomyomas and arrhythmias of TSC, along with its associated arterial aneurysms, create conditions for embolic and hemorrhagic stroke.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its hamartomas are written on the skin: TSC produces facial angiofibromas, hypopigmented ash-leaf macules, shagreen patches and ungual fibromas — skin findings that are major diagnostic criteria.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can riddle the lungs with cysts: lymphangioleiomyomatosis, a smooth-muscle proliferation that destroys lung tissue into cysts and causes pneumothorax, occurs in women with TSC and responds to mTOR inhibitors.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its mTOR-inhibitor therapy impairs healing: everolimus and sirolimus block the mTOR pathway central to tissue repair, so wounds and the surgery for angiomyolipomas or SEGAs heal slowly during TSC treatment.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is fundamentally a brain disease: cortical tubers, subependymal nodules and SEGAs are central-nervous-system hamartomas that underlie the epilepsy, autism and intellectual disability defining TSC's neurological burden.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It seeds the infant heart with tumours: cardiac rhabdomyomas, often the earliest TSC sign on fetal echo, can obstruct outflow or trigger arrhythmias before usually regressing spontaneously after birth.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It studs the liver with hamartomas: hepatic angiomyolipomas are a recognised extrarenal manifestation of TSC, and its mTOR-inhibitor therapy adds stomatitis and diarrhoea to the gastrointestinal picture.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its lung disease invades the lymphatics: lymphangioleiomyomatosis causes chylous pleural effusions, chylous ascites and lymphangioleiomyomas, lymphatic manifestations beyond its lung cysts.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It leaves quiet marks on bone and mouth: sclerotic bone islands, dental enamel pits and gingival fibromas are common minor diagnostic features of TSC.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It touches the pancreas and metabolism: TSC can cause pancreatic neuroendocrine tumours, and the mTOR-inhibitor therapy for its tumours causes hyperglycaemia and dyslipidaemia.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — mTOR inhibitors are its targeted treatment: because TSC1/TSC2 loss unleashes mTOR, everolimus and sirolimus shrink its brain (SEGA), kidney (angiomyolipoma) and lung (LAM) lesions and reduce seizures.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — A fellow mTOR-pathway tumour syndrome: tuberous sclerosis and MEN1 both produce tumours driven by mTOR-pathway dysregulation, and both respond to the mTOR inhibitors now used across these syndromes.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Both cause syndromic heart tumours: tuberous sclerosis produces cardiac rhabdomyomas while Carney complex produces myxomas, two inherited syndromes presenting with childhood cardiac masses.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — A fellow neurocutaneous syndrome: TSC and NF2 are both phakomatoses — dominantly inherited tumour-suppressor disorders causing nervous-system tumours, though TSC drives mTOR-fuelled hamartomas across many organs while NF2 causes schwannomas and meningiomas.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It cystically destroys the lung: women with TSC develop lymphangioleiomyomatosis, in which mTOR-driven smooth-muscle proliferation riddles the lung with cysts, causing recurrent pneumothorax and progressive breathlessness treated with sirolimus.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — It drives early, hard-to-control epilepsy: cortical tubers make TSC a leading genetic cause of infantile spasms and refractory seizures, and the disrupted hippocampal networks underlie much of the memory and cognitive impairment of TSC-associated neuropsychiatric disorders.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its tumour starts in the fetal heart: cardiac rhabdomyomas, mTOR-driven hamartomas of the myocardium, are often the first sign of tuberous sclerosis on prenatal ultrasound and usually regress after birth.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Lung hamartomas can raise pulmonary pressure: tuberous sclerosis causes lymphangioleiomyomatosis (LAM), whose smooth-muscle proliferation destroys lung tissue and can lead to pulmonary arterial hypertension.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Two hamartoma syndromes converging on mTOR: tuberous sclerosis loses the TSC1/2 brake on mTOR while Peutz-Jeghers loses upstream LKB1-AMPK control of it—different lesions, one overactive growth kinase driving hamartomas.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — An under-recognised tumour: TSC's mTOR hyperactivity also predisposes to pancreatic neuroendocrine tumours, the same lesions for which mTOR inhibitors like everolimus—a TSC drug—are standard therapy.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Contiguous-gene kidney disease: TSC2 sits immediately beside PKD1, so a large deletion removing both genes produces tuberous sclerosis with severe early polycystic kidney disease, cysts distorting the glomeruli decades ahead of schedule.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hamartomas beyond the kidney: fat-containing angiomyolipomas in TSC are not confined to the kidney—they also stud the hepatic lobules, usually benign but part of the same systemic hamartomatosis.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Rhabdomyomas in the fetal heart: cardiac rhabdomyomas, often the first sign of TSC on prenatal ultrasound, disrupt the conduction system to cause arrhythmias and pre-excitation before usually regressing in infancy.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Aneurysms that bleed: renal angiomyolipomas in TSC carry abnormal, fragile arterial walls prone to aneurysm formation and catastrophic retroperitoneal haemorrhage (Wunderlich syndrome) once they grow large.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Sclerotic bone lesions: TSC commonly produces scattered sclerotic foci (bone islands) in the cortical bone of the skull, spine and pelvis, a frequently incidental but characteristic skeletal feature.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — mTOR-driven proliferation: unrestrained mTORC1 from TSC1/TSC2 loss upregulates cyclin D1, driving the proliferation of the hamartomas (SEGA, angiomyolipoma) of tuberous sclerosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Pathway crosstalk: ERK/MAPK signalling crosstalks with the dysregulated mTOR pathway in tuberous sclerosis, contributing to tumour growth and resistance to mTOR inhibitors.
- `connects-to` → **[Type II Pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — Cystic lung destruction: in TSC-associated lymphangioleiomyomatosis, proliferating smooth-muscle-like LAM cells destroy the alveolar walls and type II pneumocytes lining them, forming diffuse lung cysts.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — mTOR-driven oncogene: unrestrained mTOR signalling from TSC1/TSC2 loss upregulates MYC, driving the proliferation of the hamartomas and tumours of tuberous sclerosis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor input: IGF-1 signalling feeds the PI3K/AKT/mTOR pathway that is constitutively active in tuberous sclerosis, reinforcing tumour growth.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Tumour stroma: PDGF signalling supports the growth and vascularisation of the angiomyolipomas and other mesenchymal tumours of tuberous sclerosis.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — mTOR hyperactivation in tuberous sclerosis distorts BDNF-dependent synaptic plasticity and dendritic growth, contributing to the epilepsy and the autism and neuropsychiatric features (TAND) that often cause more disability than the tumors.
- `connects-to` → **[p27 (CDKN1B)](../../03-molecular/cdkn1b/README.md)** — mTORC1-S6K signaling drives degradation of the cell-cycle inhibitor p27, and in TSC1/2-deficient cells the loss of this brake contributes to the hamartomatous overgrowth—linking the pathway's growth signal to unchecked cell-cycle entry.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the fibrotic, matrix-rich stroma of the renal angiomyolipomas and the lymphangioleiomyomatosis (LAM) lung lesions of tuberous sclerosis, a fibrotic component layered on the direct mTOR-driven proliferation of the tumor cells.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Dysregulated neuronal calcium and calcineurin-NFAT signaling in the malformed cortical tubers of tuberous sclerosis contributes to the hyperexcitability that makes early-onset, often drug-resistant epilepsy a defining feature of the disorder.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Angiopoietin-Tie2 signaling supports the abnormal blood vessels of the renal angiomyolipomas—the fat-and-vessel hamartomas prone to aneurysmal hemorrhage—and the remodeled vasculature of pulmonary LAM.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — mTOR hyperactivation in TSC lesions suppresses caspase-3 apoptosis, so mTOR inhibitors (everolimus, sirolimus) shrink hamartomas only while taken—the tumors regrow on discontinuation because the cells were arrested, not killed.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restrains the PI3K-AKT signaling that lies upstream of mTORC1, the same node hyperactivated by TSC1/TSC2 loss, so the two tumor-suppressor systems converge on the mTOR pathway central to tuberous sclerosis.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling is dysregulated downstream of mTOR hyperactivation in TSC-associated lesions such as subependymal giant cell astrocytomas, contributing to their growth.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits macrophages into TSC hamartomas and lymphangioleiomyomatosis, the inflammatory and lymphangiogenic component of the smooth-muscle lesions that destroy the lung in LAM.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β phosphorylates TSC2 to modulate the TSC complex's restraint of mTORC1 (mTOR mapped), integrating Wnt and AKT inputs into the pathway whose loss drives tuberous sclerosis.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Constitutive mTORC1 activity feeds cyclin-D1 (mapped) and the release of E2F1, driving the cell-cycle entry of the hamartoma cells of tuberous sclerosis.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Hyperactive mTORC1 drives NRF2-mediated antioxidant and anabolic metabolism in TSC lesions, supporting the growth of their hamartomatous cells.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDKN1B, cyclin-D1 and E2F1 already mapped) operates downstream of the mTOR-driven growth signaling that powers proliferation in TSC hamartomas.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) cooperates with mTORC1 hyperactivation in the lymphangioleiomyomatosis and hamartomatous lesions of tuberous sclerosis complex.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) provides a proliferative input that cooperates with mTORC1 hyperactivation in the hamartomas of tuberous sclerosis complex.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — mTORC1 hyperactivation perturbs autophagy and mitochondrial quality control, and the resulting cytosolic DNA can engage cGAS-STING within the lesions of tuberous sclerosis complex.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of TSC-associated tumors such as angiomyolipoma and lymphangioleiomyomatosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) contributes to the fibrotic and matrix-remodeling component of TSC-associated lesions including pulmonary lymphangioleiomyomatosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — TSC1/TSC2 loss drives mTORC1-AKT activity that inactivates FOXO, removing a growth-restraining, pro-autophagy brake in TSC hamartomas.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 already mapped) sustains the proliferative hamartomatous growth of TSC lesions.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in TSC-associated tumors such as angiomyolipoma and LAM, shaping their inflammatory and fibrotic stroma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in the mTORC1-driven hamartomatous lesions of tuberous sclerosis complex.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory component of the hamartoma and SEGA microenvironment of tuberous sclerosis complex.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of PDGFR (PDGF already mapped) contributes to the proliferative and migratory phenotype of the angiomyolipoma and LAM cells of tuberous sclerosis complex.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the hamartomatous lesions of tuberous sclerosis complex.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the immune context of the tumors of tuberous sclerosis complex.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of the tumors of tuberous sclerosis complex.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the microenvironment of the hamartomas and tumors of tuberous sclerosis complex.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory microenvironment of the tumors of tuberous sclerosis complex.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the cell recruitment and lymphangioleiomyomatosis-associated dissemination in tuberous sclerosis complex.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor/hamartoma microenvironment of tuberous sclerosis complex.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune microenvironment of the lesions of tuberous sclerosis complex.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory and lesion microenvironment of tuberous sclerosis complex.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac rhabdomyoma: the earliest tuberous sclerosis lesion is the cardiac rhabdomyoma, a striated-muscle hamartoma expressing sarcomeric proteins including troponin, often found prenatally and typically regressing after birth.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — Infantile spasms therapy: tuberous sclerosis is a leading cause of infantile spasms, for which ACTH is a first-line hormonal treatment alongside vigabatrin, acting to suppress the epileptic encephalopathy of early infancy.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Sleep and TAND: sleep disturbance is highly prevalent in tuberous sclerosis as part of the associated neuropsychiatric disorder, and melatonin is commonly used to manage the disrupted circadian sleep that compounds epilepsy and behaviour.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — LAM hormone sensitivity: the lymphangioleiomyomatosis of tuberous sclerosis occurs almost only in women and worsens with reproductive hormones, so progesterone and estrogen (already mapped) drive the smooth-muscle proliferation that destroys the lung.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — mTOR-insulin axis: the TSC1-TSC2 complex (already mapped) normally restrains mTORC1 downstream of insulin and growth-factor signalling, so its loss uncouples growth from nutrient and insulin cues, the core metabolic lesion driving the hamartomas.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Angiomyolipoma haemorrhage: the renal angiomyolipomas of tuberous sclerosis can bleed catastrophically into the retroperitoneum, and the resulting acute blood loss drops haemoglobin, a leading cause of morbidity that mTOR inhibitors and embolisation aim to prevent.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Hamartoma vasculature: nitric oxide with the mTOR-driven VEGF and angiopoietin (already mapped) shapes the aberrant, aneurysm-prone vasculature of the angiomyolipomas and other vascular hamartomas of tuberous sclerosis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Hamartoma immune milieu: IL-10 among the cytokines of the tuberous-sclerosis hamartoma microenvironment shapes its immune milieu (IL-6 already mapped), part of the inflammatory dimension of these mTOR-driven lesions.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Metabolic oxidative stress: unrestrained mTORC1 anabolism (already mapped) in the tuberous-sclerosis hamartomas raises metabolic and oxidative stress, to which xanthine oxidase contributes, engaging the NRF2 antioxidant response (already mapped).
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage milieu: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped) in the tuberous-sclerosis hamartomas and the lymphangioleiomyomatosis, part of their immune microenvironment.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — mTOR-driven lipogenesis: the unrestrained mTORC1 (already mapped) of the tuberous-sclerosis hamartomas drives cholesterol and lipid synthesis, the anabolic metabolism that the mTOR inhibitors shrinking the lesions target.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic signalling: the mTOR pathway (already mapped) integrates the metabolic signals of leptin and insulin (already mapped), and its dysregulation in tuberous sclerosis links the hamartoma growth to the anabolic-metabolic state.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Angiomyolipoma haemorrhage: the renal angiomyolipomas of tuberous sclerosis can bleed catastrophically, causing the retroperitoneal haemorrhage and the iron-deficiency anaemia (haemoglobin already mapped) that drive their surveillance and embolisation.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomas of tuberous sclerosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), signals through the mTOR-integrated (already mapped) metabolic pathway whose dysregulation drives the anabolic hamartoma growth of tuberous sclerosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine axis of the mTOR-integrated (already mapped) metabolic dysregulation of the hamartomas of tuberous sclerosis.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Retinal hamartomas: the retinal astrocytic hamartomas of the eye are a diagnostic feature of tuberous sclerosis, part of its multi-organ hamartoma (mTOR already mapped) spectrum.
- `connects-to` → **[Renal cell carcinoma](../renal-cell-carcinoma/README.md)** — Renal cancer risk: the tuberous sclerosis (mTOR already mapped) angiomyolipomas of the kidney (already mapped) carry an elevated risk of renal cell carcinoma, requiring surveillance.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — mTOR-interferon crosstalk: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is modulated by the mTOR (already mapped) hyperactivation and shapes the neuroinflammatory microenvironment of the tubers of tuberous sclerosis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the neuroinflammation associated with the epileptogenic cortical tubers of tuberous sclerosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory microenvironment implicated in tuberous sclerosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the tuberous-sclerosis hamartomas.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammation of the epileptogenic cortical tubers of tuberous sclerosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of tuberous sclerosis.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the neuroinflammation of the epileptogenic cortical tubers of tuberous sclerosis.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) contribute to the adaptive-immune component of the neuroinflammation of the cortical tubers of tuberous sclerosis.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells of the CNS-border compartments present antigen to the T cells (already mapped) of the neuroinflammation of tuberous sclerosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tuber myeloid cells: the macrophages and microglia (already mapped) of the cortical tubers contribute to the neuroinflammation implicated in the epilepsy of tuberous sclerosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tuber complement: the complement C3 activation, part of the neuroinflammation of the cortical tubers, contributes to the aberrant synaptic pruning implicated in the epilepsy of tuberous sclerosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation of the cortical tubers of tuberous sclerosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial-mTOR alarmin: TSLP, whose expression is amplified by the mTORC1-driven proliferation (TSC1/TSC2 already mapped) of TSC-derived LAM cells and airway epithelial hamartomas, activates mast cells (already mapped) and dendritic cells (already mapped) in the TSC pulmonary microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell dimension: histamine, released by the mast cells (already mapped) activated in the TSC pulmonary-LAM microenvironment and the skin angiofibromas (skin already mapped), amplifies the local type-2 immune response and the angiogenesis (VEGF already mapped) of the hamartoma stroma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Hamartoma ECM: periostin, an ECM glycoprotein downstream of mTORC1 (TSC1/TSC2 already mapped) and TGF-β (already mapped) signalling, contributes to the desmoplastic and invasive extracellular matrix of renal angiomyolipomas and the pulmonary-LAM lesions of tuberous sclerosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin LAM-microenvironment mediator: bradykinin, generated by the kallikrein-kinin system in the TSC-LAM pulmonary microenvironment, amplifies vascular permeability and the mast-cell (already mapped) and endothelial activation of the TSC-LAM lung.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact brake: C1-esterase inhibitor restrains the classical complement C1 and contact system (C3/C5aR1 already mapped) activated in the neuroinflammation of cortical tubers and the TSC renal angiomyolipoma stroma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — TSC-RCC and EPO signalling: erythropoietin and EPOR signalling are relevant to the renal cell carcinoma (already mapped) risk and the polycythaemia associated with renal angiomyolipomas of tuberous sclerosis complex.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — TSC testosterone: androgen receptor signalling modulates mTOR (already mapped) pathway activity in tuberous sclerosis; testosterone may amplify mTOR-driven hamartoma growth in renal angiomyolipomas, and androgen-deprivation therapy reduces angiomyolipoma progression in TSC.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — TSC serotonin: serotonin signalling is dysregulated in the autism spectrum disorder complicating tuberous sclerosis; mTOR (already mapped) hyperactivation in TSC neurons impairs serotonergic neurotransmission, and SSRI treatment addresses the associated behavioural symptoms.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — TSC prolactin: prolactin modulates cortical-tuber neuroinflammation in tuberous sclerosis via immunomodulatory effects on microglia (already mapped); prolactin-driven astrocyte (already mapped) activation amplifies the seizure susceptibility of TSC cortical dysplasia.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — TSC oxytocin: oxytocin receptor-cAMP/PKA signalling on TSC neurons attenuates mTOR (already mapped) hyperactivation downstream of TSC1/TSC2 (already mapped) loss-of-function; oxytocin also modulates the autism spectrum and social-behaviour deficits of tuberous sclerosis complex.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — TSC vasopressin: vasopressin V1A receptors on TSC neurons intersect mTOR (already mapped)/S6K signalling, modulating synaptic plasticity and the epileptic activity of cortical tubers; V1A-mediated calcium signalling may amplify TSC seizure susceptibility.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — TSC selenium: selenium-dependent GPX suppresses oxidative stress and NF-κB (already mapped)-mediated neuroinflammation in TSC cortical tubers; selenium deficiency worsens mTOR (already mapped)-driven VEGF (already mapped) upregulation and angiomyolipoma growth in TSC.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — TSC iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies mTOR (already mapped) and VEGF (already mapped) hamartoma growth and NF-κB (already mapped) neuroinflammation of TSC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — TSC sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped)-driven hamartoma cascade of TSC.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — TSC magnesium: magnesium, as mTOR (already mapped) kinase cofactor in neurons (already mapped) and astrocytes (already mapped), supports synaptic function; magnesium deficiency amplifies NF-κB (already mapped) neuroinflammation and IL-6 (already mapped) cascade of TSC epilepsy.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — TSC copper: copper-dependent SOD in neurons (already mapped) and astrocytes (already mapped) quenches mTOR (already mapped)-driven ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammation and hamartoma growth of TSC.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — TSC zinc: zinc, as mTOR (already mapped) kinase cofactor in neurons (already mapped) and astrocytes (already mapped), supports synaptic transmission; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) seizure susceptibility and hamartoma growth of TSC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — TSC potassium: potassium efflux in neurons (already mapped) and astrocytes (already mapped) modulates seizure threshold; potassium dysregulation amplifies mTOR (already mapped) and NF-κB (already mapped) cortical excitability and hamartoma cascade of TSC.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — TSC carbon: carbon, as metabolic backbone of mTOR (already mapped) lipid synthesis in neurons (already mapped) and astrocytes (already mapped), drives hamartoma growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of TSC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — TSC chloride: chloride channels in neurons (already mapped) and astrocytes (already mapped) modulate seizure threshold; chloride dysregulation amplifies mTOR (already mapped) and NF-κB (already mapped) cortical excitability and hamartoma cascade of TSC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — TSC hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and astrocytes (already mapped), quenches ROS from mTOR (already mapped) overactivation; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) seizure cascade of TSC.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — TSC nitrogen: nitric oxide from macrophages (already mapped) and neurons (already mapped) modulates mTOR-driven vascular tone; nitrogen imbalance amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — TSC oxygen: reactive oxygen species in macrophages (already mapped) and neurons (already mapped) drive mTOR-linked oxidative stress; oxygen imbalance amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — TSC sulfur: hydrogen sulfide from macrophages (already mapped) and neurons (already mapped) modulates mTOR-driven vascular tone; sulfur deficiency amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of tuberous sclerosis complex.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^crino-2006-tsc-review]: Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. *N Engl J Med.* 2006;355(13):1345-1356. [doi:10.1056/NEJMra055323](https://doi.org/10.1056/NEJMra055323) · [PubMed 17005952](https://pubmed.ncbi.nlm.nih.gov/17005952/)
[^northrup-2013-tsc-consensus]: Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. *Pediatr Neurol.* 2013;49(4):243-254. [doi:10.1016/j.pediatrneurol.2013.08.001](https://doi.org/10.1016/j.pediatrneurol.2013.08.001) · [PubMed 24053982](https://pubmed.ncbi.nlm.nih.gov/24053982/)
