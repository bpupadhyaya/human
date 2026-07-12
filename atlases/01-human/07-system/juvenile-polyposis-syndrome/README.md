---
schema: human-scale-entry/v1
id: juvenile-polyposis-syndrome
name: Juvenile Polyposis Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Juvenile polyposis syndrome (JPS) is caused by germline SMAD4 (~20%) or BMPR1A (~25%) mutations; hamartomatous GI polyps with CRC risk ~40-50% by age 60; SMAD4-JPS patients also have hereditary hemorrhagic telangiectasia features; colonoscopy from age 15."
aliases: ["juvenile polyposis syndrome", "JPS", "SMAD4 JPS", "BMPR1A JPS", "hamartomatous polyposis", "juvenile polyps GI", "JPS CRC risk", "JPS HHT overlap", "hereditary juvenile polyposis"]
sources:
  - id: howe-1998-smad4-jps
    type: peer-reviewed
    cite: "Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. Science. 1998;280(5366):1086-1088."
    doi: "10.1126/science.280.5366.1086"
    pmid: "9582123"
    url: "https://doi.org/10.1126/science.280.5366.1086"
  - id: aretz-2007-jps-spectrum
    type: peer-reviewed
    cite: "Aretz S, Stienen D, Uhlhaas S, et al. High proportion of large genomic deletions and a genotype-phenotype update in 80 unrelated families with juvenile polyposis syndrome. J Med Genet. 2007;44(11):702-709."
    doi: "10.1136/jmg.2007.051839"
    pmid: "17601924"
    url: "https://doi.org/10.1136/jmg.2007.051839"
cross_links:
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Germline SMAD4 loss causes ~20% of JPS; SMAD4-JPS has larger, more numerous polyps, earlier CRC onset, and concurrent HHT features (pulmonary/cerebral AVMs, telangiectasias) requiring vascular surveillance beyond standard JPS protocol."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "JPS polyps arise from TGF-β/BMP pathway disruption (SMAD4 or BMPR1A LOF) → stromal hamartomatous growth; wild-type epithelium overgrows abnormal stroma; TGF-β loss promotes adenomatous transformation within JPS polyps → elevated CRC risk."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "JPS confers ~40-50% lifetime CRC risk by age 60 (vs ~5% population risk); CRC arises from adenomatous foci within JPS hamartomas; SMAD4-JPS has the highest CRC risk; annual colonoscopy from age 15 with polypectomy; colectomy if polyp burden unmanageable."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "JPS hamartomas differ from FAP (APC-mutant) adenomas: hamartomas have a complex stroma with muscle fibers and cysts (not pure epithelial dysplasia); however, adenomatous foci within JPS polyps carry CRC risk; colonoscopic polypectomy controls burden in both syndromes."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN ties JPS to the overlapping hamartoma syndromes: contiguous 10q22-23 deletions can remove both BMPR1A and PTEN → a severe combined JPS/Cowden phenotype, and the BMP→SMAD4→PTEN→mTOR axis is the rationale for rapamycin chemoprevention being explored in JPS."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers is the main hamartomatous-polyposis differential: STK11-driven polyps have an arborizing smooth-muscle core (vs JPS's edematous, cyst-rich juvenile stroma) plus mucocutaneous melanotic macules absent in JPS; both carry high GI cancer risk via different pathways."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "JPS studs the colorectum with hamartomatous polyps (5-200) from which adenomatous foci drive a ~40-50% lifetime colorectal cancer risk; annual colonoscopy with polypectomy from age 15 controls burden, and colectomy is indicated when polyps become unmanageable."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Juvenile polyposis and Lynch are both dominant hereditary colorectal cancer syndromes but opposite: JPS is TGF-β/BMP loss making many hamartomatous polyps, Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas — stromal overgrowth versus repair defect."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Juvenile polyposis and FAP are both polyposis syndromes but with different polyps: JPS hamartomas have an edematous, cyst-rich stroma (TGF-β/BMP loss), FAP adenomas are purely dysplastic epithelium (APC loss); both stud the colon and need polypectomy, but histology differs."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "SMAD4-mutant juvenile polyposis characteristically floods the stomach with hamartomatous polyps — sometimes massive gastric polyposis causing bleeding, anemia, and protein-losing enteropathy — with elevated gastric cancer risk, so upper-GI surveillance is part of SMAD4-JPS care."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Gastric cancer is a major juvenile-polyposis risk, especially with SMAD4 mutations: hamartomatous gastric polyps accumulate dysplasia, giving JPS one of the highest hereditary gastric-cancer risks after hereditary diffuse gastric cancer—justifying surveillance and gastrectomy."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Juvenile polyposis and MUTYH-associated polyposis are inherited polyposis syndromes raising colorectal-cancer risk but distinct: JPS makes hamartomatous polyps from SMAD4/BMPR1A defects, MAP makes adenomas from biallelic MUTYH repair loss—different polyps, shared surveillance."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Juvenile polyposis disrupts the intestinal epithelium's stromal signaling: SMAD4/BMPR1A loss impairs BMP signals that restrain crypt stem-cell expansion, so hamartomatous polyps with abundant lamina propria and dilated glands form—and dysplasia within them drives cancer risk."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "JPS and pulmonary arterial hypertension converge on BMP/TGF-β signaling: SMAD4 and BMPR1A mutations cause juvenile polyposis (often overlapping HHT), and the same BMP genes underlie PAH—one pathway yielding gut polyps, vascular malformations and pulmonary hypertension."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "JPS and Cowden are both hamartomatous polyposis syndromes with different genes: JPS from SMAD4/BMPR1A (TGF-β/BMP) loss, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomatous polyps and raise GI cancer risk, while Cowden adds breast and thyroid tumors."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "JPS shares its key gene with pancreatic cancer: SMAD4 (DPC4), mutated in juvenile polyps, is also lost in most pancreatic adenocarcinomas—both show how dismantling TGF-β/BMP growth control transforms epithelium: benign-prone colon polyps versus lethal pancreatic cancer."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Juvenile polyposis links BMP/SMAD4 loss to Wnt-driven growth: SMAD4 or BMPR1A mutations remove a brake on epithelial proliferation, and crosstalk with Wnt/beta-catenin fuels the hamartomatous polyps—mechanistically distinct from APC-driven adenomatous polyposis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Juvenile polyposis can stud the whole gut including the small intestine: hamartomatous polyps arise throughout the GI tract, not just the colon, so surveillance and bleeding/obstruction risk extend beyond the large bowel."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron-deficiency anemia is a classic presentation of juvenile polyposis: friable GI hamartomas bleed chronically, so children present with anemia, rectal bleeding or polyp prolapse—often the first clue that prompts colonoscopy and genetic testing."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Juvenile polyposis fills the digestive tract with hamartomatous polyps: SMAD4 or BMPR1A loss seeds numerous juvenile polyps from stomach to rectum that bleed and, over time, raise gastrointestinal cancer risk—so surveillance endoscopy is central to care."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "SMAD4 juvenile polyposis overlaps with a vascular disease: patients with SMAD4 mutations can have combined JPS and hereditary hemorrhagic telangiectasia, with arteriovenous malformations and bleeding telangiectasias—so the cardiovascular system needs screening too."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "Juvenile polyposis carries gastric cancer risk that overlaps other syndromes: SMAD4-related JPS causes massive gastric polyposis predisposing to stomach cancer, so it joins HDGC and FAP among the inherited causes of gastric malignancy needing surveillance."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Juvenile polyps are hamartomas defined by their stroma: an abundant, fibroblast-rich, inflamed and edematous lamina propria surrounds cystically dilated glands—so the diagnosis rests on this stromal overgrowth, reflecting how SMAD4/BMPR1A loss deranges mesenchyme."
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "STK11 distinguishes the hamartomatous polyposis syndromes: JPS comes from BMPR1A or SMAD4, whereas STK11 (LKB1) loss causes Peutz-Jeghers—different genes producing different polyp histology and cancer risks, so gene testing sorts which syndrome a patient has."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "The juvenile polyp's bulk is connective tissue: an expanded collagen-rich stroma, not glandular crowding, gives these hamartomas their rounded, smooth shape—distinguishing them from the adenomas of FAP where the epithelium itself is neoplastic."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "SMAD4 juvenile polyposis overlaps with a blood-vessel disease: SMAD4 carriers can also have hereditary hemorrhagic telangiectasia, where faulty endothelial BMP/TGF-β signaling builds fragile telangiectasias and arteriovenous malformations that bleed."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "JPS-HHT's vascular lesions run on VEGF: dysregulated angiogenesis from disrupted BMP signaling spawns telangiectasias and AVMs, so anti-VEGF drugs like bevacizumab are used to control the severe bleeding in SMAD4 carriers."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Juvenile polyps teem with macrophages: these hamartomas carry a heavy inflammatory infiltrate in their stroma, and the immune cells plus dilated mucus-filled glands make the polyps fragile and prone to the bleeding that causes anemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Juvenile polyps bleed and drain iron: the fragile, mucus-filled hamartomas erode and ooze blood into the gut, so chronic blood loss makes iron-deficiency anemia a common and early sign of the syndrome in children."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "SMAD4-related JPS overlaps HHT and reaches the lungs: patients with SMAD4 mutations can develop pulmonary arteriovenous malformations, so this gut-polyp syndrome carries a vascular lung risk needing screening."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells join the inflamed stroma of juvenile polyps: alongside the heavy macrophage infiltrate, antigen-presenting dendritic cells populate the hamartomas, part of the immune-rich microenvironment that makes the polyps inflamed and friable."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SMAD4-related JPS can starve the blood of oxygen: in its HHT overlap, lung arteriovenous malformations shunt blood past the air sacs, so unfiltered blue blood lowers oxygen and bypasses the lungs' clot filter."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "SMAD4-JPS extends vascular risk to the brain: the HHT overlap brings cerebral arteriovenous malformations that can bleed or cause strokes, so brain screening joins the syndrome's care."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Juvenile polyps are stroma-rich hamartomas: an expanded, edematous fibrous stroma with inflamed glands makes them friable and prone to bleed, the histology that names and defines the syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "JPS is watched by light and imaging: endoscopy removes the polyps, and in SMAD4 carriers CT and MRI photons screen for the lung and brain AVMs of the overlapping HHT."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "SMAD4-JPS overlaps HHT in the liver too: hepatic arteriovenous malformations can shunt blood and strain the heart, part of the telangiectasia syndrome's vascular reach."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "JPS bleeds chronically: friable polyps and HHT telangiectasias drain blood, pushing the bone marrow to ramp up red-cell output against recurrent iron-deficiency anemia."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows JPS polyps are hamartomas, not adenomas: cystically dilated mucus-filled glands sit in an expanded, inflamed lamina propria, the disorganized overgrowth that names the juvenile polyp."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "SMAD4-driven JPS overlaps with HHT: these patients sprout mucocutaneous telangiectasias on the lips, tongue, and fingertips, tiny dilated vessels that bleed and flag the combined polyposis-vascular syndrome."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The HHT overlap can dot the eye: conjunctival telangiectasias join those on the skin and gut, fragile little vessel tufts that mark the vascular side of the SMAD4 syndrome."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Bleeding polyps drain the red cells: friable juvenile polyps ooze chronically and can hemorrhage acutely, leaving children pale and sometimes transfusion-dependent until the polyps are cleared by colonoscopy or surgery."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Loss of SMAD4 can be seen on the slide: immunohistochemistry with an anti-SMAD4 antibody shows absent nuclear staining in polyps from SMAD4-mutant patients, a stain that helps separate this syndrome from sporadic juvenile polyps."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The same SMAD4 loss that drives the polyps also imperils the pancreas: SMAD4 (DPC4) is a key pancreatic tumor suppressor, so JPS adds pancreatic and upper-GI cancer to the lifetime risk that surveillance must cover."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "SMAD4 patients can stroke through their lungs: those with the combined JPS-hereditary hemorrhagic telangiectasia syndrome harbor pulmonary AVMs that let clots and bacteria bypass the lung filter, causing paradoxical stroke and brain abscess."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SMAD4 is the meeting point for a family of signals: it carries the message not just of TGF-beta and BMP but of activin too, so its loss in JPS derails activin signaling along with the others that normally restrain gut epithelial growth."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The vascular malformations can overload the heart: in JPS-HHT, large hepatic and pulmonary arteriovenous shunts force the heart to pump extra volume, leading toward high-output cardiac failure on top of the pulmonary hypertension SMAD4 can cause."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The polyps are overgrowths driven by spared brakes: where the syndrome overlaps PTEN/Cowden biology, loss of restraint on the PI3K-AKT-mTOR axis lets the gut lining pile up into hamartomatous polyps, making mTOR a candidate target for chemoprevention."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Juvenile polyps are inflammatory hamartomas: their loose lamina propria is packed with mast cells, eosinophils and other inflammatory cells around dilated cystic glands, the histology that distinguishes them from the adenomas of other polyposis syndromes."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "The cancer risk runs the length of the gut: beyond the colon and stomach, the lifelong predisposition extends up the upper tract, so surveillance watches the esophagus and small bowel as well as the sites where polyps cluster most densely."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "A second hit turns the polyp malignant: beyond the germline SMAD4 or BMPR1A loss, somatic TP53 and other mutations accumulate as a juvenile polyp progresses to colorectal or gastric cancer."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cancer and major surgery raise the clot risk: a colorectal cancer arising in JPS, and the colectomy or gastrectomy used to treat heavy polyposis, both predispose to perioperative venous thromboembolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery carries the infectious risk: the colectomy or gastrectomy that high polyp burden eventually demands can be complicated by anastomotic leak and intra-abdominal sepsis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Inflamed polyps signal through STAT3: loss of SMAD4/BMP restraint plus IL-6-driven STAT3 in the inflamed juvenile polyps adds a proliferative push that helps tip them toward malignancy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation in the polyps feeds NF-κB: the eroded, inflamed surface of juvenile polyps activates NF-κB, contributing pro-survival, pro-proliferative signaling to the syndrome's gastrointestinal cancer risk."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Bleeding polyps and inflammation drain the blood: beyond the iron loss of chronically bleeding juvenile polyps, their inflammation suppresses erythropoiesis, adding an anemia of chronic disease to the iron deficiency."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its SMAD4-HHT overlap can overload the heart: SMAD4-mutant juvenile polyposis overlaps hereditary hemorrhagic telangiectasia, whose hepatic arteriovenous malformations shunt blood and can drive high-output heart failure."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Chronic GI losses and surgery thin the bones: protein-losing enteropathy from extensive polyps, malnutrition and any colectomy with malabsorption can leave reduced bone density in juvenile polyposis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An inherited cancer risk from childhood weighs on the mind: living with lifelong polyp surveillance, repeated procedures and elevated GI-cancer risk from a young age carries a substantial psychological burden."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Recurrent polyp surgery and SMAD4 vessels tax healing: repeated polypectomies and colectomy, plus the fragile telangiectatic vessels of the SMAD4-HHT overlap, leave wounds prone to bleeding and slow healing."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Repeated abdominal surgery irritates nerves: the colectomies and recurrent operations for juvenile polyposis can leave adhesions and post-surgical neuropathic abdominal pain."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong surveillance from childhood breeds worry: the constant polyp screening, recurrent procedures and inherited cancer risk of juvenile polyposis foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its SMAD4 form telangiectases the skin: when juvenile polyposis is caused by SMAD4 it overlaps hereditary haemorrhagic telangiectasia, with mucocutaneous telangiectasias on the lips, tongue and fingers."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "SMAD4 overlap riddles the lungs with shunts: the JPS-HHT overlap causes pulmonary arteriovenous malformations that bleed, cause hypoxaemia and let clots and bacteria bypass the lung filter."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its vascular malformations reach the brain: SMAD4-related JPS-HHT causes cerebral arteriovenous malformations that can rupture into haemorrhagic stroke or seed brain abscess via right-to-left shunts."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Heavy polyposis leaks protein from the gut: extensive juvenile polyposis, especially in infants, causes protein-losing enteropathy with low albumin and oedema as protein escapes into the bowel."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can bleed from kidney and gut: SMAD4-related JPS-HHT can form renal arteriovenous malformations causing haematuria, while chronic polyp bleeding drives iron-deficiency anaemia."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its gene also governs immunity: SMAD4 transduces TGF-β signalling that regulates immune tolerance, so its loss has effects beyond the gut and vasculature."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It demands genetic counselling: as an autosomal-dominant SMAD4/BMPR1A condition, juvenile polyposis raises questions of inheritance and prenatal testing for affected families."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can stunt childhood growth: a heavy polyp burden causes chronic blood and protein loss with anaemia and failure to thrive, impairing growth in affected children."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet supports the at-risk colon: a high-fibre diet aids colorectal health, a backdrop to the lifelong endoscopic surveillance that juvenile polyposis's raised cancer risk requires."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for the cancers it breeds: juvenile polyposis carries a high lifetime risk of colorectal and gastric cancer, treated with standard chemotherapy when surveillance and surgery are outrun."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Mostly microsatellite-stable: like FAP, the gastrointestinal cancers of juvenile polyposis are usually microsatellite-stable and, unlike Lynch tumours, respond poorly to PD-1 checkpoint inhibitors."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Lung AVMs open a path to brain abscess: SMAD4 juvenile polyposis overlaps hereditary haemorrhagic telangiectasia, whose pulmonary arteriovenous malformations let bacteria like Staphylococcus aureus bypass the lung and seed brain abscesses."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Diseases of one signalling axis: juvenile polyposis arises from loss of SMAD4, the central transducer of TGF-β/BMP signalling, while Marfan syndrome stems from FBN1 loss that unleashes excess TGF-β—opposite disturbances of the same pathway."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "SMAD4 keeps the vessel wall intact: SMAD4 relays the BMP9/ALK1 signals maintaining the arterial wall, so its loss in SMAD4-type juvenile polyposis yields the fragile telangiectatic vessels and AVMs of overlapping hereditary haemorrhagic telangiectasia."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "The same signal builds the heart valves: TGF-β/BMP-SMAD4 signalling drives the endocardial cushion transformation that forms cardiac valves, so SMAD4 loss in juvenile polyposis can accompany the congenital valvular and septal anomalies seen in its HHT overlap."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pulmonary AVMs of the JPS-HHT overlap: SMAD4 mutations cause combined juvenile polyposis and hereditary haemorrhagic telangiectasia, with pulmonary arteriovenous malformations in the alveolar bed that risk paradoxical embolism and hypoxaemia."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatic AVMs: the JPS-HHT overlap also produces hepatic arteriovenous malformations shunting blood through the liver lobule, which can cause high-output heart failure."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Two germline cancer syndromes: like Li-Fraumeni, juvenile polyposis is an autosomal-dominant predisposition requiring lifelong surveillance, though JPS targets the gut while Li-Fraumeni spans many organs."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "The hamartoma family: like the juvenile polyps of JPS, the lesions of tuberous sclerosis are hamartomas—disorganised overgrowths of native tissue—linking these syndromes through dysregulated growth-factor and mTOR signalling rather than a single oncogene."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Vascular morphogenesis gone wrong: SMAD4 loss in JPS-HHT disrupts the BMP/TGF-beta control of angiogenesis that works alongside angiopoietin-Tie2 signalling, producing the arteriovenous malformations of the combined syndrome."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "High-output strain: large hepatic and pulmonary arteriovenous malformations in SMAD4-mutant JPS-HHT shunt blood and force the myocardium into chronic high-output work, a route to heart failure."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 chemoprevention angle: juvenile polyps overexpress COX-2 and prostaglandins, suggesting NSAID chemoprevention may help reduce polyp burden as it does in other polyposis syndromes."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflamed stroma: the abundant inflammatory, IL-6-rich lamina propria of juvenile polyps fuels chronic inflammation that contributes to their progression toward cancer."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Hamartoma and vessel walls: smooth muscle within the polyp stroma and the malformed vessel walls of associated HHT reflect the SMAD4/BMP control of mesenchymal and vascular cells."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT cooperation: loss of SMAD4-mediated growth control activates PI3K/AKT signalling that helps drive the epithelial overgrowth of juvenile polyps toward cancer."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: as juvenile polyps acquire Wnt and other oncogenic hits, MYC activation drives the proliferation that underlies their malignant progression."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Polyp hypoxia: the inflamed, growing juvenile polyps become hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that feeds their expansion."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Oncogenic progression: acquired KRAS mutations drive the progression of juvenile polyps toward gastrointestinal carcinoma, a key step beyond the germline SMAD4/BMPR1A loss that initiates the polyps."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT reactivation maintains telomeres as juvenile polyps progress to carcinoma, granting the replicative capacity of the gastric and colorectal cancers of the syndrome."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Inflammatory polyp stroma: CCL2 recruits macrophages into the characteristically inflamed, oedematous stroma of juvenile polyps, sustaining the microenvironment that drives their growth."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "HHT vascular overlap: SMAD4 loss impairs BMP9-ALK1-SMAD4 signalling that normally restrains endothelial nitric oxide, causing the arteriovenous malformations and telangiectasias of the hereditary haemorrhagic telangiectasia seen in SMAD4-juvenile polyposis."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Epithelial proliferation: EGFR-driven proliferation of the polyp epithelium contributes to the growth of the hamartomatous juvenile polyps once the BMP/SMAD4 brake on epithelial homeostasis is lost."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Lost apoptotic control: BMP/SMAD4 signalling normally promotes apoptosis in the gut epithelium, so its loss in juvenile polyposis impairs caspase-3-mediated cell death, contributing to polyp formation and the elevated cancer risk."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "HHT vascular overlap: SMAD4-mutant juvenile polyposis overlaps with hereditary haemorrhagic telangiectasia, where the same BMP/TGF-β defect produces arteriovenous malformations and the endothelial dysfunction reflected in endothelin signalling, causing epistaxis and GI bleeding."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Hereditary-cancer differential: juvenile polyposis (SMAD4/BMPR1A) sits among the hereditary gastrointestinal-cancer syndromes that must be distinguished from Lynch syndrome (MLH1 and other mismatch-repair genes), each with its own surveillance and risk profile."
  - target: 01-human/03-molecular/mutyh
    relation: connects-to
    note: "Polyposis differential: the hamartomatous polyps of juvenile polyposis must be distinguished histologically and genetically from the adenomatous polyposis of FAP and MUTYH-associated polyposis, a distinction that determines cancer risk and management."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK progression: KRAS-driven (mapped) MAPK-ERK signalling contributes to the progression of juvenile-polyposis hamartomatous polyps toward colorectal and gastric carcinoma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K cooperation: PIK3CA activation of the PI3K-AKT-mTOR axis (PTEN, AKT and mTOR already mapped) cooperates in the malignant transformation of juvenile-polyposis polyps."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and invasion: loss of E-cadherin during epithelial-mesenchymal transition accompanies the progression of juvenile-polyposis polyps to invasive adenocarcinoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory stroma: IL-6-STAT3 signalling (IL-6 and STAT3 already mapped) sustains the inflammatory stroma of the hamartomatous polyps and contributes to their malignant potential in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota inflammation: gut-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides an inflammatory drive promoting the polyp-to-carcinoma progression of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cancer progression: loss of the RB1-E2F checkpoint is among the cooperating events in the progression of juvenile-polyposis polyps to gastrointestinal carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is upregulated during the polyp-to-carcinoma progression of juvenile polyposis syndrome, modulating tumour-cell adhesion and immune evasion."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss contributes to the malignant progression of the hamartomatous polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the inflammatory and immune microenvironment of the gastrointestinal neoplasia in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the gastrointestinal neoplasia in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (RB1 already mapped) drives the cell-cycle progression of the adenoma-carcinoma sequence in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by PI3K-AKT signalling, is progressively lost in the malignant transformation of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling that cooperates with SMAD4 loss in the polyposis of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the polyp-to-cancer progression of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory stroma of the hamartomatous polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative epithelial signaling of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation during the progression of the polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the cancer risk of the hamartomatous polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the neoplasms of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the epithelial cells of the hamartomatous polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the polyps of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the polyps and carcinomas of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the polyp and tumor microenvironment of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neoplasms of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the intestinal inflammatory tumor microenvironment of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding and HHT overlap: the juvenile polyps bleed and SMAD4 carriers also have hereditary haemorrhagic telangiectasia with epistaxis and AVMs (angiopoietin already mapped), so chronic blood loss causes the iron-deficiency anaemia that lowers haemoglobin."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the many hamartomatous polyps of juvenile polyposis progress to gastrointestinal cancer, and antigen presentation is relevant to chemoprevention and immunotherapy."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell responses contribute to immune control of the neoplastic progression in juvenile polyposis, part of the adaptive immunity acting on its polyp-carpeted gastrointestinal tract."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunosurveillance effectors: cytotoxic CD8 T cells (MHC class II and IL-2 already mapped) police the many hamartomatous polyps of juvenile polyposis for malignant transformation, the cellular arm of the immune control of neoplastic progression."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic mucosal inflammation and the high epithelial turnover of the polyps generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds the hamartoma-carcinoma progression of juvenile polyposis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the polyp microenvironment dampens anti-tumour immunity (MHC class II already mapped), part of the immune tolerance that allows some juvenile-polyposis polyps to progress to cancer."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the hamartomatous polyp stroma of juvenile polyposis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the hamartoma-carcinoma progression, a modifiable dietary influence on the cancer risk of juvenile polyposis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and proliferation: the adipokine leptin links obesity to colorectal carcinogenesis, promoting the epithelial proliferation (Wnt already mapped) that can accelerate the malignant progression of the polyps in juvenile polyposis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomatous polyps of juvenile polyposis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the iron-deficiency (already mapped) anaemia of the chronically bleeding polyps of juvenile polyposis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the colorectal carcinogenesis, part of the modifiable adipokine influence on the cancer risk of juvenile polyposis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic influence on the colorectal carcinogenesis of juvenile polyposis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Malabsorption zinc: the zinc deficiency from the malabsorption and protein-losing enteropathy of the extensive GI polyposis of juvenile polyposis impairs the healing and immunity."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Micronutrient malabsorption: the calcium and micronutrient malabsorption of the protein-losing enteropathy and extensive polyposis of juvenile polyposis, contributing to the nutritional depletion."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic polyps: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the inflammatory infiltrate of the hamartomatous juvenile polyps."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immune surveillance: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the polyps and the cancer-risk surveillance of juvenile polyposis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the colorectal-cancer risk of juvenile polyposis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the polyps and cancer-risk surveillance of juvenile polyposis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of the juvenile polyps."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed juvenile polyp stroma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflamed stroma of the juvenile polyps."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the inflamed stroma of the juvenile polyps."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the malignant transformation of the juvenile polyps to colorectal cancer (already mapped)."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the juvenile polyps."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the juvenile polyps."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Bleeding iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron-deficiency anaemia from the chronic gastrointestinal blood loss of the juvenile polyps."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP released by the inflamed JPS intestinal epithelium activates mast cells and dendritic cells, promoting the type-2 inflammatory stroma of juvenile polyps and accelerating the SMAD4-mutant adenoma-carcinoma transition."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Hamartomatous stroma: periostin, a SMAD4-downstream ECM protein, drives the mesenchymal overgrowth and fibroblast invasion of the juvenile polyp stroma; elevated periostin in JPS lesions correlates with stroma-driven polyp expansion."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Anti-polyposis VDR: vitamin D (VDR modulates WNT/beta-catenin already mapped) reduces colorectal cancer risk in polyposis syndromes; low serum vitamin D associates with accelerated adenoma progression in SMAD4/BMPR1A germline carriers."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Mucosal pain and permeability: bradykinin, via B1/B2 receptors on intestinal epithelial cells (already mapped) and mast cells (already mapped), amplifies vascular permeability and the inflammatory juvenile-polyp stroma, worsening the GI blood loss of JPS."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: C1-INH controls the classical and lectin complement pathways (C3 and C5aR1 already mapped) that amplify the inflammatory activation of the juvenile-polyp stroma and the vascular permeability of the JPS gastrointestinal mucosa."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "GI-blood-loss anaemia: erythropoietin corrects the iron-deficiency anaemia (already mapped) from the chronic gastrointestinal blood loss of the juvenile polyps; the EPO response reflects the severity of the haematological burden of JPS."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mucosal mast-cell histamine: histamine released by mast cells in the juvenile polyp stroma activates H1/H2 receptors on SMAD4-mutant intestinal epithelial cells (already mapped), amplifying mucosal inflammation and the vascular permeability of the hamartomatous JPS polyps."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Colorectal antiproliferative: melatonin suppresses WNT/β-catenin signalling (already mapped) via MT1/MT2 receptors on SMAD4-mutant (already mapped) colonic epithelial cells, reducing polyp proliferation and the adenoma-carcinoma transition risk in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen receptor in JPS: testosterone, via androgen receptor on SMAD4-mutant colonic epithelial cells (already mapped), modulates WNT/β-catenin proliferative signalling and may contribute to the male-skewed colorectal cancer risk in juvenile polyposis syndrome."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "JPS prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "JPS oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the polyposis inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of JPS."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "JPS vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the polyposis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "JPS serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the colonic TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "JPS selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative polyp cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "JPS iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "JPS sodium: sodium regulates macrophage (already mapped) and intestinal epithelium (already mapped) ion homeostasis; sodium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) polyp cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "JPS magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "JPS copper: copper, via ceruloplasmin in macrophages (already mapped) and mast cells (already mapped), scavenges mucosal ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "JPS carbon: carbon as backbone of WNT (already mapped) and SMAD4 (already mapped) signalling proteins in colonocytes (already mapped) sustains proliferative control; carbon depletion amplifies TGF-β (already mapped) and NF-κB (already mapped) polyp cascade of JPS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "JPS chloride: chloride regulates colonocyte (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) protumorigenic cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "JPS nitrogen: nitrogen in amino-acid scaffold of SMAD4 (already mapped) and BMPR1A signalling sustains polyp suppression; nitrogen dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "JPS hydrogen: hydrogen in water and hydroxyl chemistry of SMAD4 (already mapped) and BMPR1A sustains polyp-suppressive signalling; hydrogen dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "JPS phosphorus: phosphorus in PI3K-Akt and SMAD4 (already mapped) phosphorylation relays governs colonocyte (already mapped) growth control; phosphorus dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of JPS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "JPS potassium: potassium ion gradients in colonocytes (already mapped) and macrophages (already mapped) regulate membrane potential; potassium dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) protumorigenic cascade of JPS."
---

# Juvenile Polyposis Syndrome

## Overview

**Juvenile polyposis syndrome (JPS)** is an autosomal dominant hereditary gastrointestinal polyposis syndrome characterized by multiple hamartomatous polyps of the colon, rectum, stomach, and small intestine, with a significantly elevated risk of colorectal and gastric cancers. JPS affects approximately **1 in 100,000-160,000** individuals and is caused by germline pathogenic variants in **SMAD4** (~20%), **BMPR1A** (~25%), or as yet unidentified genes (~55%) [^howe-1998-smad4-jps] [^aretz-2007-jps-spectrum]. The term "juvenile" refers to the characteristic **juvenile polyp histology** (edematous stroma, dilated mucus-filled glands, inflammatory infiltrate, surface erosion) — not to patient age at onset, though onset in childhood is common. JPS is distinct from Peutz-Jeghers syndrome (STK11-driven hamartomas with arborizing smooth muscle core) and Cowden syndrome (PTEN-driven; trichilemmomal cysts, macrocephaly, breast/thyroid risk).

**JPS compared to other hamartomatous polyposis syndromes:**

| Feature | JPS | Peutz-Jeghers (PJS) | Cowden (CS) |
|---|---|---|---|
| Gene(s) | SMAD4, BMPR1A | STK11 | PTEN |
| Polyp histology | Juvenile (edematous stroma) | Hamartoma with arborizing smooth muscle | Hamartoma (variable) |
| GI distribution | Colon > stomach > SI | Small intestine > colon > stomach | Colon, stomach, esophagus |
| Melanotic macules | Absent | Present (lips, buccal, digits) | Absent |
| Skin lesions | Rare | None | Trichilemmoma, keratoses |
| CRC lifetime risk | ~40-50% | ~39% | ~9-18% |
| HHT overlap | SMAD4-JPS only | Absent | Absent |
| Pathway | TGF-β/BMP (SMAD) | LKB1/AMPK/mTOR | PI3K/AKT/mTOR |

## Structure

### Diagnostic criteria for JPS

Clinical diagnosis requires **one or more** of:
1. **≥5 juvenile polyps** in the colorectum
2. **Juvenile polyps throughout the GI tract** (colon + stomach/small bowel)
3. **Any number of juvenile polyps** with a family history of JPS

Juvenile polyp histology: pedunculated or sessile; smooth rounded surface; edematous lamina propria with inflammatory cells (eosinophils, plasma cells, neutrophils); dilated mucus-filled crypts (retention cysts); surface erosion and granulation tissue; no smooth muscle core (distinguishes from PJS hamartoma)

JPS differs from a **solitary juvenile polyp** (common in children 2-5 years, ~1% of children; benign, no increased cancer risk; >1 polyp raises JPS concern; ≥5 polyps = likely JPS).

### Genetic subtypes

**SMAD4-JPS (~20%):**
- Germline SMAD4 pathogenic variants (missense, truncating, splice, large deletions — MLPA required)
- **SMAD4-HHT overlap syndrome**: JPS + hereditary hemorrhagic telangiectasia (HHT) phenotype
  - Telangiectasias: mucocutaneous (lips, tongue, fingertips), GI (epistaxis, GI bleeding)
  - Pulmonary AVMs: right-to-left shunt → paradoxical embolism → stroke, brain abscess
  - Hepatic AVMs: high-output cardiac failure in severe cases
  - Cerebral AVMs: hemorrhagic stroke risk
  - Nasal epistaxis (recurrent): most common early symptom
- SMAD4-JPS polyps: often larger, more numerous, pancolonic; earlier onset of CRC; higher density gastric juvenile polyposis
- Screening: cardiac echo (bubble study) + chest CT + brain MRI for AVM detection at diagnosis

**BMPR1A-JPS (~25%):**
- Germline BMPR1A pathogenic variants (BMP type I receptor; chromosome 10q22-q23)
- No HHT features
- Pure polyposis phenotype; some overlap with Cowden-like features (macrocephaly, PTEN-like features in a few families)
- Large genomic deletions of BMPR1A (up to entire gene) detected by MLPA; ~30% of BMPR1A pathogenic variants are large deletions
- Overlapping 10q deletion: contiguous deletions of BMPR1A + PTEN have been reported → more severe phenotype (Cowden + JPS features)

**Unknown genetic cause (~55%):**
- May include: PTEN variants (overlap with Cowden), BMPR1A large deletions missed by sequencing, BMPR2 variants, somatic mosaic SMAD4/BMPR1A mutations, or as-yet-unidentified genes
- No pathogenic variant found on clinical germline testing does not exclude JPS clinically

### GI polyposis distribution

- **Colorectal polyps**: present in virtually all JPS patients; polyp count 5-200 (variable); colon is most common site
- **Gastric juvenile polyposis (GJP)**: ~15-30% of JPS patients; diffuse fundic gland polyposis + juvenile polyp histology; higher in SMAD4-JPS; protein-losing enteropathy, hypoalbuminemia, edema
- **Small bowel polyps**: 10-15%; usually fewer; small bowel capsule endoscopy for detection
- **Duodenal polyps**: 10-15%; Spigelman staging not established for JPS (unlike FAP)
- **Rectal sparing**: uncommon; rectum usually involved

## Function

### Disease mechanism: stromal-epithelial BMP signaling disruption

JPS hamartomas arise from disrupted **BMP/SMAD signaling in the intestinal stroma**. In normal intestine:
- Mesenchymal cells secrete BMP2/4/7 → bind BMPR1A/BMPR2 on epithelial crypt cells → SMAD1/5/8 phosphorylation → SMAD4 complex → p21/Notch suppression → stem cell quiescence
- BMP gradient: high at crypt-villus boundary (suppresses proliferation), low at crypt base (allows stem cell cycling)

In JPS (SMAD4 or BMPR1A LOF in epithelium):
- BMP signals cannot be transduced → epithelial SMAD1/5/8-SMAD4 complex non-functional → loss of BMP anti-proliferative output → crypt cell proliferation + polyp formation
- Stromal component: edematous stromal expansion (inflammatory infiltrate, granulation tissue) — the "hamartoma" stroma — is thought to result from aberrant paracrine signaling between dysregulated epithelium and mesenchyme
- Adenomatous foci within JPS polyps: where biallelic SMAD4/BMPR1A LOH occurs → loss of remaining allele → adenoma-carcinoma sequence can proceed → CRC risk

### Cancer risk

**Colorectal cancer (CRC):**
- Lifetime CRC risk: ~40-50% by age 60 (vs ~5% population); may reach 68% in some series by age 70
- CRC arises predominantly from adenomatous transformation within JPS polyps, not de novo
- SMAD4-JPS: higher CRC risk than BMPR1A-JPS
- Median age of CRC diagnosis: ~37-44 years in JPS (vs ~72 years for sporadic CRC)

**Gastric cancer:**
- Risk: ~15-21% lifetime; particularly in SMAD4-JPS with diffuse gastric polyposis
- Gastric cancer surveillance: upper endoscopy every 1-2 years

**Small bowel and duodenal cancer:**
- Risk elevated but rare; small bowel surveillance with capsule endoscopy

**Pancreatic cancer:**
- Some families with SMAD4-JPS report elevated pancreatic cancer risk (SMAD4 is also a major PDAC driver); formal risk quantification limited by small series

## Pathology

### Surveillance recommendations

**Genetic testing:**
- Germline SMAD4 and BMPR1A sequencing + large deletion analysis (MLPA)
- Predictive testing of at-risk relatives after age 15 (onset of endoscopy surveillance)
- Testing of all first-degree relatives if pathogenic variant identified

**Endoscopic surveillance:**
- **Colonoscopy**: from age 15 (or when diagnosis suspected); annually if polyps present; every 2-3 years if no polyps
- **Upper endoscopy (EGD)**: from age 15; annually if gastric polyps present; every 2-3 years if clean
- **Small bowel capsule endoscopy**: every 2-3 years if small bowel polyps

**SMAD4-specific vascular surveillance (HHT overlap):**
- Transthoracic echocardiogram with bubble study (TTCE): screen for pulmonary AVM at diagnosis
- If TTCE positive → CT pulmonary angiogram → transcatheter embolization of pulmonary AVMs >3 mm
- Brain MRI (gadolinium): screen for cerebral AVM at diagnosis; repeat every 5 years
- Annual CBC (anemia from GI/epistaxis blood loss); iron supplementation

**Surgical management:**
- **Colectomy with ileorectal anastomosis (IRA)**: for unmanageable polyp burden; ileal pouch-anal anastomosis (IPAA) if rectum involved; prophylactic surgery generally at age 15-25 when polyp count becomes unmanageable (>50-100 polyps)
- **Total/subtotal gastrectomy**: for severe gastric polyposis with protein-losing enteropathy or unresectable polyps; nutritional reconstruction after gastrectomy in young patients
- **Appendectomy**: at time of colectomy; appendiceal juvenile polyps reported

### Medical management

No approved chemopreventive agents specifically for JPS. Options under investigation or used off-label:
- **COX-2 inhibitors (celecoxib)**: rationale from FAP data; reduces polyp formation in animal models of Smad4-deficient polyposis; no Phase 3 JPS data
- **Rapamycin/mTOR inhibitors**: rationale from BMPR1A-JPS (BMP → SMAD4 → PTEN → mTOR pathway); pre-clinical data; no clinical trials
- **Bevacizumab**: used in SMAD4-HHT for severe GI telangiectasia bleeding and pulmonary AVMs unresponsive to embolization; off-label; reduces bleeding frequency

## Connections

- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Germline SMAD4 loss causes ~20% of JPS; SMAD4-JPS has larger, more numerous polyps, earlier CRC onset, and concurrent HHT features (pulmonary/cerebral AVMs, telangiectasias) requiring vascular surveillance beyond standard JPS protocol.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — JPS polyps arise from TGF-β/BMP pathway disruption (SMAD4 or BMPR1A LOF) → stromal hamartomatous growth; wild-type epithelium overgrows abnormal stroma; TGF-β loss promotes adenomatous transformation within JPS polyps → elevated CRC risk.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — JPS confers ~40-50% lifetime CRC risk by age 60 (vs ~5% population risk); CRC arises from adenomatous foci within JPS hamartomas; SMAD4-JPS has the highest CRC risk; annual colonoscopy from age 15 with polypectomy; colectomy if polyp burden unmanageable.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — JPS hamartomas differ from FAP (APC-mutant) adenomas: hamartomas have a complex stroma with muscle fibers and cysts (not pure epithelial dysplasia); however, adenomatous foci within JPS polyps carry CRC risk; colonoscopic polypectomy controls burden in both syndromes.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN ties JPS to the overlapping hamartoma syndromes: contiguous 10q22-23 deletions can remove both BMPR1A and PTEN → a severe combined JPS/Cowden phenotype, and the BMP→SMAD4→PTEN→mTOR axis is the rationale for rapamycin chemoprevention being explored in JPS.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers is the main hamartomatous-polyposis differential: STK11-driven polyps have an arborizing smooth-muscle core (vs JPS's edematous, cyst-rich juvenile stroma) plus mucocutaneous melanotic macules absent in JPS; both carry high GI cancer risk via different pathways.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — JPS studs the colorectum with hamartomatous polyps (5-200) from which adenomatous foci drive a ~40-50% lifetime colorectal cancer risk; annual colonoscopy with polypectomy from age 15 controls burden, and colectomy is indicated when polyps become unmanageable.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Juvenile polyposis and Lynch are both dominant hereditary colorectal cancer syndromes but opposite: JPS is TGF-β/BMP loss making many hamartomatous polyps, Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas — stromal overgrowth versus repair defect.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Juvenile polyposis and FAP are both polyposis syndromes but with different polyps: JPS hamartomas have an edematous, cyst-rich stroma (TGF-β/BMP loss), FAP adenomas are purely dysplastic epithelium (APC loss); both stud the colon and need polypectomy, but histology differs.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — SMAD4-mutant juvenile polyposis characteristically floods the stomach with hamartomatous polyps — sometimes massive gastric polyposis causing bleeding, anemia, and protein-losing enteropathy — with elevated gastric cancer risk, so upper-GI surveillance is part of SMAD4-JPS care.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Gastric cancer is a major juvenile-polyposis risk, especially with SMAD4 mutations: hamartomatous gastric polyps accumulate dysplasia, giving JPS one of the highest hereditary gastric-cancer risks after hereditary diffuse gastric cancer—justifying surveillance and gastrectomy.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Juvenile polyposis and MUTYH-associated polyposis are inherited polyposis syndromes raising colorectal-cancer risk but distinct: JPS makes hamartomatous polyps from SMAD4/BMPR1A defects, MAP makes adenomas from biallelic MUTYH repair loss—different polyps, shared surveillance.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Juvenile polyposis disrupts the intestinal epithelium's stromal signaling: SMAD4/BMPR1A loss impairs BMP signals that restrain crypt stem-cell expansion, so hamartomatous polyps with abundant lamina propria and dilated glands form—and dysplasia within them drives cancer risk.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — JPS and pulmonary arterial hypertension converge on BMP/TGF-β signaling: SMAD4 and BMPR1A mutations cause juvenile polyposis (often overlapping HHT), and the same BMP genes underlie PAH—one pathway yielding gut polyps, vascular malformations and pulmonary hypertension.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — JPS and Cowden are both hamartomatous polyposis syndromes with different genes: JPS from SMAD4/BMPR1A (TGF-β/BMP) loss, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomatous polyps and raise GI cancer risk, while Cowden adds breast and thyroid tumors.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — JPS shares its key gene with pancreatic cancer: SMAD4 (DPC4), mutated in juvenile polyps, is also lost in most pancreatic adenocarcinomas—both show how dismantling TGF-β/BMP growth control transforms epithelium: benign-prone colon polyps versus lethal pancreatic cancer.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Juvenile polyposis links BMP/SMAD4 loss to Wnt-driven growth: SMAD4 or BMPR1A mutations remove a brake on epithelial proliferation, and crosstalk with Wnt/beta-catenin fuels the hamartomatous polyps—mechanistically distinct from APC-driven adenomatous polyposis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Juvenile polyposis can stud the whole gut including the small intestine: hamartomatous polyps arise throughout the GI tract, not just the colon, so surveillance and bleeding/obstruction risk extend beyond the large bowel.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron-deficiency anemia is a classic presentation of juvenile polyposis: friable GI hamartomas bleed chronically, so children present with anemia, rectal bleeding or polyp prolapse—often the first clue that prompts colonoscopy and genetic testing.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Juvenile polyposis fills the digestive tract with hamartomatous polyps: SMAD4 or BMPR1A loss seeds numerous juvenile polyps from stomach to rectum that bleed and, over time, raise gastrointestinal cancer risk—so surveillance endoscopy is central to care.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — SMAD4 juvenile polyposis overlaps with a vascular disease: patients with SMAD4 mutations can have combined JPS and hereditary hemorrhagic telangiectasia, with arteriovenous malformations and bleeding telangiectasias—so the cardiovascular system needs screening too.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — Juvenile polyposis carries gastric cancer risk that overlaps other syndromes: SMAD4-related JPS causes massive gastric polyposis predisposing to stomach cancer, so it joins HDGC and FAP among the inherited causes of gastric malignancy needing surveillance.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Juvenile polyps are hamartomas defined by their stroma: an abundant, fibroblast-rich, inflamed and edematous lamina propria surrounds cystically dilated glands—so the diagnosis rests on this stromal overgrowth, reflecting how SMAD4/BMPR1A loss deranges mesenchyme.
- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — STK11 distinguishes the hamartomatous polyposis syndromes: JPS comes from BMPR1A or SMAD4, whereas STK11 (LKB1) loss causes Peutz-Jeghers—different genes producing different polyp histology and cancer risks, so gene testing sorts which syndrome a patient has.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The juvenile polyp's bulk is connective tissue: an expanded collagen-rich stroma, not glandular crowding, gives these hamartomas their rounded, smooth shape—distinguishing them from the adenomas of FAP where the epithelium itself is neoplastic.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — SMAD4 juvenile polyposis overlaps with a blood-vessel disease: SMAD4 carriers can also have hereditary hemorrhagic telangiectasia, where faulty endothelial BMP/TGF-β signaling builds fragile telangiectasias and arteriovenous malformations that bleed.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — JPS-HHT's vascular lesions run on VEGF: dysregulated angiogenesis from disrupted BMP signaling spawns telangiectasias and AVMs, so anti-VEGF drugs like bevacizumab are used to control the severe bleeding in SMAD4 carriers.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Juvenile polyps teem with macrophages: these hamartomas carry a heavy inflammatory infiltrate in their stroma, and the immune cells plus dilated mucus-filled glands make the polyps fragile and prone to the bleeding that causes anemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Juvenile polyps bleed and drain iron: the fragile, mucus-filled hamartomas erode and ooze blood into the gut, so chronic blood loss makes iron-deficiency anemia a common and early sign of the syndrome in children.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — SMAD4-related JPS overlaps HHT and reaches the lungs: patients with SMAD4 mutations can develop pulmonary arteriovenous malformations, so this gut-polyp syndrome carries a vascular lung risk needing screening.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells join the inflamed stroma of juvenile polyps: alongside the heavy macrophage infiltrate, antigen-presenting dendritic cells populate the hamartomas, part of the immune-rich microenvironment that makes the polyps inflamed and friable.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SMAD4-related JPS can starve the blood of oxygen: in its HHT overlap, lung arteriovenous malformations shunt blood past the air sacs, so unfiltered blue blood lowers oxygen and bypasses the lungs' clot filter.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — SMAD4-JPS extends vascular risk to the brain: the HHT overlap brings cerebral arteriovenous malformations that can bleed or cause strokes, so brain screening joins the syndrome's care.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Juvenile polyps are stroma-rich hamartomas: an expanded, edematous fibrous stroma with inflamed glands makes them friable and prone to bleed, the histology that names and defines the syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — JPS is watched by light and imaging: endoscopy removes the polyps, and in SMAD4 carriers CT and MRI photons screen for the lung and brain AVMs of the overlapping HHT.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — SMAD4-JPS overlaps HHT in the liver too: hepatic arteriovenous malformations can shunt blood and strain the heart, part of the telangiectasia syndrome's vascular reach.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — JPS bleeds chronically: friable polyps and HHT telangiectasias drain blood, pushing the bone marrow to ramp up red-cell output against recurrent iron-deficiency anemia.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows JPS polyps are hamartomas, not adenomas: cystically dilated mucus-filled glands sit in an expanded, inflamed lamina propria, the disorganized overgrowth that names the juvenile polyp.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — SMAD4-driven JPS overlaps with HHT: these patients sprout mucocutaneous telangiectasias on the lips, tongue, and fingertips, tiny dilated vessels that bleed and flag the combined polyposis-vascular syndrome.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The HHT overlap can dot the eye: conjunctival telangiectasias join those on the skin and gut, fragile little vessel tufts that mark the vascular side of the SMAD4 syndrome.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Bleeding polyps drain the red cells: friable juvenile polyps ooze chronically and can hemorrhage acutely, leaving children pale and sometimes transfusion-dependent until the polyps are cleared by colonoscopy or surgery.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Loss of SMAD4 can be seen on the slide: immunohistochemistry with an anti-SMAD4 antibody shows absent nuclear staining in polyps from SMAD4-mutant patients, a stain that helps separate this syndrome from sporadic juvenile polyps.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The same SMAD4 loss that drives the polyps also imperils the pancreas: SMAD4 (DPC4) is a key pancreatic tumor suppressor, so JPS adds pancreatic and upper-GI cancer to the lifetime risk that surveillance must cover.
- `connects-to` → **[Stroke](../stroke/README.md)** — SMAD4 patients can stroke through their lungs: those with the combined JPS-hereditary hemorrhagic telangiectasia syndrome harbor pulmonary AVMs that let clots and bacteria bypass the lung filter, causing paradoxical stroke and brain abscess.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — SMAD4 is the meeting point for a family of signals: it carries the message not just of TGF-beta and BMP but of activin too, so its loss in JPS derails activin signaling along with the others that normally restrain gut epithelial growth.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The vascular malformations can overload the heart: in JPS-HHT, large hepatic and pulmonary arteriovenous shunts force the heart to pump extra volume, leading toward high-output cardiac failure on top of the pulmonary hypertension SMAD4 can cause.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The polyps are overgrowths driven by spared brakes: where the syndrome overlaps PTEN/Cowden biology, loss of restraint on the PI3K-AKT-mTOR axis lets the gut lining pile up into hamartomatous polyps, making mTOR a candidate target for chemoprevention.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Juvenile polyps are inflammatory hamartomas: their loose lamina propria is packed with mast cells, eosinophils and other inflammatory cells around dilated cystic glands, the histology that distinguishes them from the adenomas of other polyposis syndromes.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — The cancer risk runs the length of the gut: beyond the colon and stomach, the lifelong predisposition extends up the upper tract, so surveillance watches the esophagus and small bowel as well as the sites where polyps cluster most densely.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — A second hit turns the polyp malignant: beyond the germline SMAD4 or BMPR1A loss, somatic TP53 and other mutations accumulate as a juvenile polyp progresses to colorectal or gastric cancer.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cancer and major surgery raise the clot risk: a colorectal cancer arising in JPS, and the colectomy or gastrectomy used to treat heavy polyposis, both predispose to perioperative venous thromboembolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery carries the infectious risk: the colectomy or gastrectomy that high polyp burden eventually demands can be complicated by anastomotic leak and intra-abdominal sepsis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Inflamed polyps signal through STAT3: loss of SMAD4/BMP restraint plus IL-6-driven STAT3 in the inflamed juvenile polyps adds a proliferative push that helps tip them toward malignancy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation in the polyps feeds NF-κB: the eroded, inflamed surface of juvenile polyps activates NF-κB, contributing pro-survival, pro-proliferative signaling to the syndrome's gastrointestinal cancer risk.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Bleeding polyps and inflammation drain the blood: beyond the iron loss of chronically bleeding juvenile polyps, their inflammation suppresses erythropoiesis, adding an anemia of chronic disease to the iron deficiency.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its SMAD4-HHT overlap can overload the heart: SMAD4-mutant juvenile polyposis overlaps hereditary hemorrhagic telangiectasia, whose hepatic arteriovenous malformations shunt blood and can drive high-output heart failure.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Chronic GI losses and surgery thin the bones: protein-losing enteropathy from extensive polyps, malnutrition and any colectomy with malabsorption can leave reduced bone density in juvenile polyposis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An inherited cancer risk from childhood weighs on the mind: living with lifelong polyp surveillance, repeated procedures and elevated GI-cancer risk from a young age carries a substantial psychological burden.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Recurrent polyp surgery and SMAD4 vessels tax healing: repeated polypectomies and colectomy, plus the fragile telangiectatic vessels of the SMAD4-HHT overlap, leave wounds prone to bleeding and slow healing.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Repeated abdominal surgery irritates nerves: the colectomies and recurrent operations for juvenile polyposis can leave adhesions and post-surgical neuropathic abdominal pain.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong surveillance from childhood breeds worry: the constant polyp screening, recurrent procedures and inherited cancer risk of juvenile polyposis foster chronic health anxiety alongside depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its SMAD4 form telangiectases the skin: when juvenile polyposis is caused by SMAD4 it overlaps hereditary haemorrhagic telangiectasia, with mucocutaneous telangiectasias on the lips, tongue and fingers.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — SMAD4 overlap riddles the lungs with shunts: the JPS-HHT overlap causes pulmonary arteriovenous malformations that bleed, cause hypoxaemia and let clots and bacteria bypass the lung filter.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its vascular malformations reach the brain: SMAD4-related JPS-HHT causes cerebral arteriovenous malformations that can rupture into haemorrhagic stroke or seed brain abscess via right-to-left shunts.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Heavy polyposis leaks protein from the gut: extensive juvenile polyposis, especially in infants, causes protein-losing enteropathy with low albumin and oedema as protein escapes into the bowel.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can bleed from kidney and gut: SMAD4-related JPS-HHT can form renal arteriovenous malformations causing haematuria, while chronic polyp bleeding drives iron-deficiency anaemia.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its gene also governs immunity: SMAD4 transduces TGF-β signalling that regulates immune tolerance, so its loss has effects beyond the gut and vasculature.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It demands genetic counselling: as an autosomal-dominant SMAD4/BMPR1A condition, juvenile polyposis raises questions of inheritance and prenatal testing for affected families.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can stunt childhood growth: a heavy polyp burden causes chronic blood and protein loss with anaemia and failure to thrive, impairing growth in affected children.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet supports the at-risk colon: a high-fibre diet aids colorectal health, a backdrop to the lifelong endoscopic surveillance that juvenile polyposis's raised cancer risk requires.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for the cancers it breeds: juvenile polyposis carries a high lifetime risk of colorectal and gastric cancer, treated with standard chemotherapy when surveillance and surgery are outrun.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Mostly microsatellite-stable: like FAP, the gastrointestinal cancers of juvenile polyposis are usually microsatellite-stable and, unlike Lynch tumours, respond poorly to PD-1 checkpoint inhibitors.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Lung AVMs open a path to brain abscess: SMAD4 juvenile polyposis overlaps hereditary haemorrhagic telangiectasia, whose pulmonary arteriovenous malformations let bacteria like Staphylococcus aureus bypass the lung and seed brain abscesses.
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Diseases of one signalling axis: juvenile polyposis arises from loss of SMAD4, the central transducer of TGF-β/BMP signalling, while Marfan syndrome stems from FBN1 loss that unleashes excess TGF-β—opposite disturbances of the same pathway.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — SMAD4 keeps the vessel wall intact: SMAD4 relays the BMP9/ALK1 signals maintaining the arterial wall, so its loss in SMAD4-type juvenile polyposis yields the fragile telangiectatic vessels and AVMs of overlapping hereditary haemorrhagic telangiectasia.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — The same signal builds the heart valves: TGF-β/BMP-SMAD4 signalling drives the endocardial cushion transformation that forms cardiac valves, so SMAD4 loss in juvenile polyposis can accompany the congenital valvular and septal anomalies seen in its HHT overlap.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pulmonary AVMs of the JPS-HHT overlap: SMAD4 mutations cause combined juvenile polyposis and hereditary haemorrhagic telangiectasia, with pulmonary arteriovenous malformations in the alveolar bed that risk paradoxical embolism and hypoxaemia.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatic AVMs: the JPS-HHT overlap also produces hepatic arteriovenous malformations shunting blood through the liver lobule, which can cause high-output heart failure.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Two germline cancer syndromes: like Li-Fraumeni, juvenile polyposis is an autosomal-dominant predisposition requiring lifelong surveillance, though JPS targets the gut while Li-Fraumeni spans many organs.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — The hamartoma family: like the juvenile polyps of JPS, the lesions of tuberous sclerosis are hamartomas—disorganised overgrowths of native tissue—linking these syndromes through dysregulated growth-factor and mTOR signalling rather than a single oncogene.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Vascular morphogenesis gone wrong: SMAD4 loss in JPS-HHT disrupts the BMP/TGF-beta control of angiogenesis that works alongside angiopoietin-Tie2 signalling, producing the arteriovenous malformations of the combined syndrome.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — High-output strain: large hepatic and pulmonary arteriovenous malformations in SMAD4-mutant JPS-HHT shunt blood and force the myocardium into chronic high-output work, a route to heart failure.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 chemoprevention angle: juvenile polyps overexpress COX-2 and prostaglandins, suggesting NSAID chemoprevention may help reduce polyp burden as it does in other polyposis syndromes.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflamed stroma: the abundant inflammatory, IL-6-rich lamina propria of juvenile polyps fuels chronic inflammation that contributes to their progression toward cancer.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Hamartoma and vessel walls: smooth muscle within the polyp stroma and the malformed vessel walls of associated HHT reflect the SMAD4/BMP control of mesenchymal and vascular cells.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT cooperation: loss of SMAD4-mediated growth control activates PI3K/AKT signalling that helps drive the epithelial overgrowth of juvenile polyps toward cancer.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: as juvenile polyps acquire Wnt and other oncogenic hits, MYC activation drives the proliferation that underlies their malignant progression.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Polyp hypoxia: the inflamed, growing juvenile polyps become hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that feeds their expansion.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Oncogenic progression: acquired KRAS mutations drive the progression of juvenile polyps toward gastrointestinal carcinoma, a key step beyond the germline SMAD4/BMPR1A loss that initiates the polyps.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT reactivation maintains telomeres as juvenile polyps progress to carcinoma, granting the replicative capacity of the gastric and colorectal cancers of the syndrome.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Inflammatory polyp stroma: CCL2 recruits macrophages into the characteristically inflamed, oedematous stroma of juvenile polyps, sustaining the microenvironment that drives their growth.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — SMAD4 loss impairs the BMP9-ALK1-SMAD4 signaling that restrains endothelial nitric oxide, causing the arteriovenous malformations and telangiectasias of the hereditary hemorrhagic telangiectasia seen in SMAD4-juvenile polyposis overlap.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR-driven proliferation of the polyp epithelium contributes to the growth of the hamartomatous juvenile polyps once the BMP/SMAD4 brake on epithelial homeostasis is lost in the syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — BMP/SMAD4 signaling normally promotes apoptosis in the gut epithelium, so its loss in juvenile polyposis impairs caspase-3-mediated cell death—contributing to polyp formation and the substantially elevated gastrointestinal cancer risk.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — SMAD4-mutant juvenile polyposis overlaps with hereditary hemorrhagic telangiectasia, where the same BMP/TGF-β defect produces arteriovenous malformations and the endothelial dysfunction reflected in endothelin signaling, causing epistaxis and GI bleeding.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — Juvenile polyposis (SMAD4/BMPR1A) sits among the hereditary gastrointestinal-cancer syndromes that must be distinguished from Lynch syndrome (MLH1 and other mismatch-repair genes), each with its own surveillance and risk profile.
- `connects-to` → **[MUTYH](../../03-molecular/mutyh/README.md)** — The hamartomatous polyps of juvenile polyposis must be distinguished histologically and genetically from the adenomatous polyposis of FAP and MUTYH-associated polyposis, a distinction that determines cancer risk and management.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS-driven (mapped) MAPK-ERK signaling contributes to the progression of juvenile-polyposis hamartomatous polyps toward colorectal and gastric carcinoma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA activation of the PI3K-AKT-mTOR axis (PTEN, AKT and mTOR already mapped) cooperates in the malignant transformation of juvenile-polyposis polyps.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition accompanies the progression of juvenile-polyposis polyps to invasive adenocarcinoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-STAT3 signaling (IL-6 and STAT3 already mapped) sustains the inflammatory stroma of the hamartomatous polyps and contributes to their malignant potential in juvenile polyposis syndrome.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides an inflammatory drive promoting the polyp-to-carcinoma progression of juvenile polyposis syndrome.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Loss of the RB1-E2F checkpoint is among the cooperating events in the progression of juvenile-polyposis polyps to gastrointestinal carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is upregulated during the polyp-to-carcinoma progression of juvenile polyposis syndrome, modulating tumor-cell adhesion and immune evasion.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss contributes to the malignant progression of the hamartomatous polyps of juvenile polyposis syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the inflammatory and immune microenvironment of the gastrointestinal neoplasia in juvenile polyposis syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the gastrointestinal neoplasia in juvenile polyposis syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (RB1 already mapped) drives the cell-cycle progression of the adenoma-carcinoma sequence in juvenile polyposis syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by PI3K-AKT signaling, is progressively lost in the malignant transformation of juvenile polyposis syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling that cooperates with SMAD4 loss in the polyposis of juvenile polyposis syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the polyp-to-cancer progression of juvenile polyposis syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory stroma of the hamartomatous polyps of juvenile polyposis syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative epithelial signaling of juvenile polyposis syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation during the progression of the polyps of juvenile polyposis syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the cancer risk of the hamartomatous polyps of juvenile polyposis syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the neoplasms of juvenile polyposis syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the epithelial cells of the hamartomatous polyps of juvenile polyposis syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the polyps of juvenile polyposis syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of juvenile polyposis syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the polyps and carcinomas of juvenile polyposis syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the polyp and tumor microenvironment of juvenile polyposis syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neoplasms of juvenile polyposis syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the intestinal inflammatory tumor microenvironment of juvenile polyposis syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of juvenile polyposis syndrome.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding and HHT overlap: the juvenile polyps bleed and SMAD4 carriers also have hereditary haemorrhagic telangiectasia with epistaxis and AVMs (angiopoietin already mapped), so chronic blood loss causes the iron-deficiency anaemia that lowers haemoglobin.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the many hamartomatous polyps of juvenile polyposis progress to gastrointestinal cancer, and antigen presentation is relevant to chemoprevention and immunotherapy.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell responses contribute to immune control of the neoplastic progression in juvenile polyposis, part of the adaptive immunity acting on its polyp-carpeted gastrointestinal tract.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunosurveillance effectors: cytotoxic CD8 T cells (MHC class II and IL-2 already mapped) police the many hamartomatous polyps of juvenile polyposis for malignant transformation, the cellular arm of the immune control of neoplastic progression.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic mucosal inflammation and the high epithelial turnover of the polyps generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds the hamartoma-carcinoma progression of juvenile polyposis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the polyp microenvironment dampens anti-tumour immunity (MHC class II already mapped), part of the immune tolerance that allows some juvenile-polyposis polyps to progress to cancer.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the hamartomatous polyp stroma of juvenile polyposis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the hamartoma-carcinoma progression, a modifiable dietary influence on the cancer risk of juvenile polyposis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and proliferation: the adipokine leptin links obesity to colorectal carcinogenesis, promoting the epithelial proliferation (Wnt already mapped) that can accelerate the malignant progression of the polyps in juvenile polyposis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomatous polyps of juvenile polyposis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the iron-deficiency (already mapped) anaemia of the chronically bleeding polyps of juvenile polyposis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the colorectal carcinogenesis, part of the modifiable adipokine influence on the cancer risk of juvenile polyposis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic influence on the colorectal carcinogenesis of juvenile polyposis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Malabsorption zinc: the zinc deficiency from the malabsorption and protein-losing enteropathy of the extensive GI polyposis of juvenile polyposis impairs the healing and immunity.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Micronutrient malabsorption: the calcium and micronutrient malabsorption of the protein-losing enteropathy and extensive polyposis of juvenile polyposis, contributing to the nutritional depletion.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilic polyps: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the inflammatory infiltrate of the hamartomatous juvenile polyps.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immune surveillance: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the polyps and the cancer-risk surveillance of juvenile polyposis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the colorectal-cancer risk of juvenile polyposis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the polyps and cancer-risk surveillance of juvenile polyposis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of the juvenile polyps.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed juvenile polyp stroma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflamed stroma of the juvenile polyps.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the inflamed stroma of the juvenile polyps.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the malignant transformation of the juvenile polyps to colorectal cancer (already mapped).
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the juvenile polyps.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the juvenile polyps.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Bleeding iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron-deficiency anaemia from the chronic gastrointestinal blood loss of the juvenile polyps.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP released by the inflamed JPS intestinal epithelium activates mast cells and dendritic cells, promoting the type-2 inflammatory stroma of juvenile polyps and accelerating the SMAD4-mutant adenoma-carcinoma transition.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Hamartomatous stroma: periostin, a SMAD4-downstream ECM protein, drives the mesenchymal overgrowth and fibroblast invasion of the juvenile polyp stroma; elevated periostin in JPS lesions correlates with stroma-driven polyp expansion.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Anti-polyposis VDR: vitamin D (VDR modulates WNT/beta-catenin already mapped) reduces colorectal cancer risk in polyposis syndromes; low serum vitamin D associates with accelerated adenoma progression in SMAD4/BMPR1A germline carriers.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Mucosal pain and permeability: bradykinin, via B1/B2 receptors on intestinal epithelial cells (already mapped) and mast cells (already mapped), amplifies vascular permeability and the inflammatory juvenile-polyp stroma, worsening the GI blood loss of JPS.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: C1-INH controls the classical and lectin complement pathways (C3 and C5aR1 already mapped) that amplify the inflammatory activation of the juvenile-polyp stroma and the vascular permeability of the JPS gastrointestinal mucosa.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — GI-blood-loss anaemia: erythropoietin corrects the iron-deficiency anaemia (already mapped) from the chronic gastrointestinal blood loss of the juvenile polyps; the EPO response reflects the severity of the haematological burden of JPS.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mucosal mast-cell histamine: histamine released by mast cells in the juvenile polyp stroma activates H1/H2 receptors on SMAD4-mutant intestinal epithelial cells (already mapped), amplifying mucosal inflammation and the vascular permeability of the hamartomatous JPS polyps.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Colorectal antiproliferative: melatonin suppresses WNT/β-catenin signalling (already mapped) via MT1/MT2 receptors on SMAD4-mutant (already mapped) colonic epithelial cells, reducing polyp proliferation and the adenoma-carcinoma transition risk in juvenile polyposis syndrome.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen receptor in JPS: testosterone, via androgen receptor on SMAD4-mutant colonic epithelial cells (already mapped), modulates WNT/β-catenin proliferative signalling and may contribute to the male-skewed colorectal cancer risk in juvenile polyposis syndrome.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — JPS prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — JPS oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the polyposis inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of JPS.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — JPS vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the polyposis; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — JPS serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the colonic TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of juvenile polyposis syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — JPS selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative polyp cascade of juvenile polyposis syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — JPS iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of juvenile polyposis syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — JPS sodium: sodium regulates macrophage (already mapped) and intestinal epithelium (already mapped) ion homeostasis; sodium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) polyp cascade of juvenile polyposis syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — JPS magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — JPS copper: copper, via ceruloplasmin in macrophages (already mapped) and mast cells (already mapped), scavenges mucosal ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — JPS carbon: carbon as backbone of WNT (already mapped) and SMAD4 (already mapped) signalling proteins in colonocytes (already mapped) sustains proliferative control; carbon depletion amplifies TGF-β (already mapped) and NF-κB (already mapped) polyp cascade of JPS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — JPS chloride: chloride regulates colonocyte (already mapped) and macrophage (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) protumorigenic cascade of juvenile polyposis syndrome.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — JPS nitrogen: nitrogen in amino-acid scaffold of SMAD4 (already mapped) and BMPR1A signalling sustains polyp suppression; nitrogen dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — JPS hydrogen: hydrogen in water and hydroxyl chemistry of SMAD4 (already mapped) and BMPR1A sustains polyp-suppressive signalling; hydrogen dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of juvenile polyposis syndrome.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — JPS phosphorus: phosphorus in PI3K-Akt and SMAD4 (already mapped) phosphorylation relays governs colonocyte (already mapped) growth control; phosphorus dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of JPS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — JPS potassium: potassium ion gradients in colonocytes (already mapped) and macrophages (already mapped) regulate membrane potential; potassium dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) protumorigenic cascade of JPS.

[^howe-1998-smad4-jps]: Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. *Science.* 1998;280(5366):1086-1088. [doi:10.1126/science.280.5366.1086](https://doi.org/10.1126/science.280.5366.1086) · [PubMed 9582123](https://pubmed.ncbi.nlm.nih.gov/9582123/)
[^aretz-2007-jps-spectrum]: Aretz S, Stienen D, Uhlhaas S, et al. High proportion of large genomic deletions and a genotype-phenotype update in 80 unrelated families with juvenile polyposis syndrome. *J Med Genet.* 2007;44(11):702-709. [doi:10.1136/jmg.2007.051839](https://doi.org/10.1136/jmg.2007.051839) · [PubMed 17601924](https://pubmed.ncbi.nlm.nih.gov/17601924/)
