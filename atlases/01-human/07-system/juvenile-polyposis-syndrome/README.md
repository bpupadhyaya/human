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

[^howe-1998-smad4-jps]: Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. *Science.* 1998;280(5366):1086-1088. [doi:10.1126/science.280.5366.1086](https://doi.org/10.1126/science.280.5366.1086) · [PubMed 9582123](https://pubmed.ncbi.nlm.nih.gov/9582123/)
[^aretz-2007-jps-spectrum]: Aretz S, Stienen D, Uhlhaas S, et al. High proportion of large genomic deletions and a genotype-phenotype update in 80 unrelated families with juvenile polyposis syndrome. *J Med Genet.* 2007;44(11):702-709. [doi:10.1136/jmg.2007.051839](https://doi.org/10.1136/jmg.2007.051839) · [PubMed 17601924](https://pubmed.ncbi.nlm.nih.gov/17601924/)
