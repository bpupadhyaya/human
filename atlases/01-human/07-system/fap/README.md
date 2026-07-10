---
schema: human-scale-entry/v1
id: fap
name: Familial Adenomatous Polyposis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Familial adenomatous polyposis (FAP) is caused by germline APC mutations; >100 colorectal adenomas from age 10-20; CRC by 30-40 without treatment; prophylactic proctocolectomy is curative; desmoid tumor, duodenal adenomas, and Gardner syndrome are extracolonic features."
aliases: ["FAP", "familial adenomatous polyposis", "APC polyposis", "Gardner syndrome", "attenuated FAP", "AFAP", "FAP colon", "hereditary CRC APC", "APC syndrome", "FAP desmoid"]
sources:
  - id: kinzler-1991-apc
    type: peer-reviewed
    cite: "Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. Science. 1991;253(5020):661-665."
    doi: "10.1126/science.1651562"
    pmid: "1651562"
    url: "https://doi.org/10.1126/science.1651562"
  - id: fearon-1990-vogelstein
    type: peer-reviewed
    cite: "Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. Cell. 1990;61(5):759-767."
    doi: "10.1016/0092-8674(90)90186-i"
    pmid: "2188735"
    url: "https://doi.org/10.1016/0092-8674(90)90186-i"
cross_links:
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "Germline APC truncating mutations cause FAP; codon position determines phenotype: codons 1250-1464 = classic profuse FAP; codons 1310-2011 = mesenteric desmoid risk; codons <168 or >1580 = attenuated FAP; codon 1309 hotspot = most severe; nuclear β-catenin in FAP adenomas"
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "APC LOF → insufficient β-catenin destruction complex → nuclear β-catenin → TCF/LEF → Wnt-ON; FAP tumors show nuclear β-catenin by IHC; FAP desmoid (APC codons 1310-2011) driven by APC LOF, not CTNNB1 mutation; functionally equivalent outcome via distinct mechanisms"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "FAP: 100% CRC penetrance by age 40 without colectomy; proctocolectomy (IPAA or ileostomy) is definitive prevention; annual colonoscopy from age 10-12; celecoxib FDA-approved for FAP adenoma reduction; sulindac reduces polyp burden; duodenal surveillance required"
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "APC germline mutations (codons 1310-2011) → FAP-associated mesenteric desmoid; more aggressive than sporadic CTNNB1-mutant desmoid; post-colectomy FAP mesenteric desmoid is a leading mortality cause in FAP; nirogacestat FDA-approved for all desmoid including FAP-associated"
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Biallelic MUTYH mutations cause an autosomal-recessive phenocopy of attenuated FAP (10-100 adenomas) with no germline APC mutation; defective 8-oxoG base-excision repair drives G:C→T:A transversions in APC and KRAS; ~30% of APC-negative AFAP is actually MAP."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS activating mutations (G12D/V, ~50% of large FAP adenomas) are a key step in the Fearon-Vogelstein adenoma-carcinoma sequence after biallelic APC loss; the same APC→KRAS→SMAD4→TP53 progression as sporadic CRC, but compressed and universal because APC LOF is pre-present."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "FAP carpets the colorectal mucosa with hundreds-to-thousands of adenomas; every colonocyte carries the germline APC first hit, so independent somatic second hits seed many foci; prophylactic proctocolectomy removes the at-risk mucosa and is curative for colorectal risk."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "FAP and hereditary diffuse gastric cancer are both dominant GI cancer syndromes but opposite in lesion: FAP carpets the colon with thousands of APC-driven adenomas, while HDGC seeds the stomach with CDH1-driven signet-ring foci that never form polyps — adenomatous versus diffuse."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "After colectomy the duodenum becomes FAP's most dangerous site: duodenal and ampullary adenomas (Spigelman-staged) progress to cancer in 3-5% and are the leading cause of cancer death in FAP, mandating lifelong upper-GI surveillance and sometimes pancreas-sparing duodenectomy."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with FAP, can be the presenting sign of an undiagnosed APC mutation — prompting colonoscopy and germline testing when it appears."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "FAP and juvenile polyposis are both autosomal-dominant polyposis syndromes with high colorectal-cancer risk but differ in polyp biology: FAP carpets the colon with adenomas (APC/Wnt), while JPS makes fewer hamartomatous polyps (SMAD4/BMPR1A)—both need surveillance, often surgery."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "FAP affects the upper GI tract, not just the colon: nearly all patients develop fundic gland polyps and duodenal/ampullary adenomas, and gastric-cancer risk is raised, so after colectomy upper endoscopic surveillance of the stomach and duodenum becomes the priority."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "FAP is a disease of the intestinal epithelium's stem cells: germline APC loss removes the brake on Wnt/β-catenin in colonic crypt stem cells, so the entire epithelium is primed to form adenomas—hundreds to thousands—making the field, not a single clone, the cancer-prone tissue."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "FAP and Lynch syndrome are the major hereditary colorectal cancer syndromes but opposite: FAP floods the colon with hundreds of adenomatous polyps via APC loss, while Lynch causes few polyps but mismatch-repair failure—polyposis versus microsatellite instability."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "FAP and Peutz-Jeghers are both inherited GI polyposis conditions but differ in polyp type and gene: FAP's APC loss yields hundreds of adenomas, while PJS's STK11 loss gives hamartomatous polyps and mucocutaneous pigmentation—different polyps, different cancer risks."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "FAP can include brain tumors as Turcot syndrome: the same germline APC mutation that drives colonic polyposis also raises risk of medulloblastoma, linking Wnt-pathway dysregulation in gut and cerebellum—one mutated gene producing tumors in two very different organs."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "FAP is the textbook Wnt-pathway cancer syndrome: germline APC loss removes the brake on beta-catenin, so constitutive Wnt signaling drives the hundreds of colonic adenomas—mechanistically the same pathway activated somatically in most sporadic colorectal cancers."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach is an extracolonic FAP target: patients develop numerous fundic gland polyps and have raised gastric and duodenal cancer risk, so surveillance endoscopy of the upper GI tract complements colectomy in managing the syndrome."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "FAP raises the risk of pancreatic and other extracolonic cancers: APC loss predisposes beyond the colon to duodenal, pancreatic, thyroid and hepatoblastoma tumors—so even after prophylactic colectomy, FAP patients need broader cancer surveillance."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "FAP carpets the digestive tract with polyps: APC loss seeds hundreds to thousands of colonic adenomas that inevitably progress to colorectal cancer without colectomy, plus duodenal and gastric polyps—so FAP is a whole-gut polyposis, not just a colon disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "A retinal sign helps flag FAP: congenital hypertrophy of the retinal pigment epithelium (CHRPE) appears as pigmented fundus patches in many families, so an eye exam can provide an early, noninvasive clue to the APC mutation before polyps are found."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "FAP's Gardner variant shows in skin and bone: APC loss produces epidermoid cysts, fibromas and osteomas (especially of the jaw and skull), so these extraintestinal lumps of the integumentary and skeletal system can be the first visible sign of the syndrome."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "FAP raises childhood hepatoblastoma risk: young children with an APC mutation have a markedly increased chance of this liver cancer, so some families screen infants with abdominal ultrasound and AFP before the colonic polyps even appear."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "FAP overlaps brain tumors in Turcot syndrome: an APC mutation predisposes to medulloblastoma and other CNS tumors, so the colon and brain share a Wnt-pathway driver—linking a bowel polyposis syndrome to childhood brain cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "FAP's Gardner variant is a fibroblast disease too: APC loss drives fibroblasts to form desmoid tumors, Gardner fibromas, and excess scar, so the same Wnt activation that carpets the colon also makes connective tissue overgrow."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "FAP grows bony osteomas as a Gardner feature: APC loss spurs osteoblasts to build benign bone tumors in the jaw and skull, an extracolonic clue that—with skin cysts and dental anomalies—can flag the syndrome before colon polyps declare themselves."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "FAP's polyps grow because APC loss unleashes MYC: with APC gone, β-catenin piles up and switches on MYC, the master proliferation gene, so every adenoma is driven by the Wnt-to-MYC signal that turns normal colon lining into a carpet of polyps."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "FAP tumors are immunologically cold: unlike the mismatch-repair-deficient cancers of Lynch syndrome, APC-driven colorectal cancers are microsatellite-stable with few neoantigens, so they respond poorly to the checkpoint immunotherapy that helps Lynch tumors."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "FAP reaches the skin in its Gardner variant: beyond the colon, APC loss spawns epidermoid cysts, lipomas, fibromas and bony osteomas, so skin and jaw lumps can be the first visible clue to the syndrome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "FAP polyps recruit blood vessels via VEGF: as adenomas grow they drive VEGF-fueled angiogenesis, part of why COX-2 inhibitors—which lower this signaling—reduce polyp burden as chemoprevention in the syndrome."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages populate the stroma of FAP's polyps: drawn into the adenomas, tumor-associated macrophages secrete growth and inflammatory factors that help the APC-driven lesions progress toward colorectal cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "FAP's polyps bleed away iron: hundreds of colonic adenomas ooze blood, so chronic loss drains the body's iron into a deficiency anemia that can be an early clue before cancer develops."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "FAP extends cancer risk to the pancreas: beyond the colon, the APC defect raises the chance of duodenal, periampullary, and pancreatic tumors, so surveillance reaches the upper GI tract too."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "FAP's adenomas summon endothelial cells: VEGF from the growing polyps drives these vessel-lining cells to build blood supply, which is why COX-2 inhibitors that curb this angiogenesis shrink polyp burden."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "FAP is policed by light: lifelong colonoscopy hunts the polyps, and a dilated eye exam spots CHRPE—the dark retinal patches that mark the syndrome—both relying on visible-light viewing."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "FAP's desmoid tumors are fibrosis run amok: APC loss lets fibroblasts build invasive fibrous masses, the desmoids that become a leading cause of death once the colon is removed."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "FAP raises thyroid cancer risk: a distinctive cribriform-morular papillary thyroid carcinoma occurs especially in young women with the syndrome, so thyroid screening is advised."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads FAP's two telltale lesions: the dysplastic glands of its countless colonic adenomas, and the pigment-stuffed cells of CHRPE, the dark retinal patches that flag the syndrome at an eye exam."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "In the Gardner variant, FAP grows bone: benign osteomas sprout from the jaw and skull, bony overgrowths of the marrow-bearing facial bones that, with skin cysts, can betray the syndrome before the gut polyps do."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "FAP's osteomas are built of calcium: the Gardner-syndrome bony tumors lay down dense calcium-phosphate mineral, hard masses on the skull and jaw visible as bright opacities on imaging."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Gardner syndrome marks the skeleton and teeth: FAP's variant grows osteomas on the jaw and skull and brings dental anomalies — supernumerary teeth and odontomas — extracolonic clues that can predate the bowel polyps."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The Turcot variant ties FAP to the brain: alongside its colonic polyps it predisposes to CNS tumors, classically medulloblastoma, so neurological symptoms can be part of the syndrome's reach."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "FAP quietly enlarges the adrenals: benign adrenal adenomas are more common than in the general population, usually silent incidentalomas found on the imaging done to track the syndrome's other tumors."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Losing APC unleashes the growth genes: stabilized beta-catenin switches on cyclin D1 and MYC, pushing the colonic cells through the cell cycle — the molecular engine that turns the thousands of FAP polyps into ever-larger adenomas."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "FAP children risk a liver tumor: hepatoblastoma, arising from immature hepatocyte precursors, is hundreds of times more common in FAP infants, so screening with alpha-fetoprotein and ultrasound is offered in the early years."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Aspirin's polyp-shrinking effect runs partly through platelets: blocking platelet COX-1 — alongside COX-2 in the polyps — underlies why aspirin and other NSAIDs reduce colorectal adenoma burden, a chemoprevention strategy studied in FAP."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 loss is the last step to cancer: FAP's polyps start with APC loss, then accumulate KRAS and finally TP53 mutations along the adenoma-carcinoma sequence, p53 failure marking the leap to invasive colorectal cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The immune climate shapes polyp fate: regulatory T cells infiltrate colorectal adenomas and dampen the local antitumor response, part of the microenvironment that lets some of FAP's countless polyps progress."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "It headlines the polyposis differential: FAP's hundreds of adenomas must be told apart from the hamartomatous polyposes like Cowden and Peutz-Jeghers, each a distinct gene with its own cancer spectrum and surveillance."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Hundreds of polyps bleed quietly: chronic occult blood loss from FAP's carpet of colonic adenomas (and any cancer) causes iron-deficiency anemia, sometimes the first clue that prompts the colonoscopy revealing the polyposis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Major surgery and cancer raise the clot risk: the prophylactic colectomy central to FAP care, and any colorectal cancer that develops, both predispose to perioperative venous thromboembolism needing prophylaxis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery brings infectious risk: anastomotic leak and pouchitis after the colectomy or ileal-pouch reconstruction that FAP requires can seed intra-abdominal infection and sepsis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation collaborates with the Wnt drive: NF-κB activation in the polyp-laden mucosa adds pro-survival, pro-proliferative signals to the APC-loss Wnt pathway, helping push FAP adenomas toward carcinoma."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 feeds the adenoma through STAT3: inflammatory IL-6/STAT3 signaling in the carpet of FAP polyps promotes epithelial proliferation and survival, one of the inflammatory accelerants of its inevitable cancer."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Hundreds of polyps and inflammation drain the blood: beyond the iron loss of chronic polyp bleeding, the inflammatory milieu of FAP can suppress erythropoiesis, adding an anemia of chronic disease to the iron deficiency."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its desmoids can throttle the ureters: the intra-abdominal desmoid tumors that FAP predisposes to can compress the ureters into obstruction, and prolonged hydronephrosis can erode kidney function toward chronic kidney disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the colon costs the bones: total colectomy and the malabsorption of vitamin D and calcium after surgery, plus the disease's chronic GI losses, leave FAP patients prone to bone loss and osteoporosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Prophylactic colectomy and inherited cancer risk weigh on the mind: facing inevitable colorectal cancer without surgery, living with a stoma or pouch, and the hereditary burden give FAP a substantial psychological toll."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Repeated abdominal surgery taxes healing: prophylactic colectomy, pouch construction and desmoid resections in FAP leave patients with recurrent surgical wounds, adhesions and the slow healing of reoperated tissue."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Surgery and desmoids irritate nerves: extensive abdominal operations and mesenteric desmoid tumors in FAP can entrap and compress nerves, producing chronic post-surgical and neuropathic abdominal pain."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Inevitable cancer risk and surveillance breed worry: the certainty of colorectal cancer without surgery and the lifelong endoscopic surveillance of FAP foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "APC loss reaches the endocrine glands: FAP raises the risk of papillary thyroid cancer (the cribriform-morular variant) and adrenal adenomas, extending its tumour spectrum into the endocrine system."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It marks the eye and, rarely, the brain: FAP causes congenital hypertrophy of the retinal pigment epithelium, and the Turcot variant pairs colonic polyposis with brain tumours like medulloblastoma."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut bacteria speed its polyps to cancer: in FAP the colonic microbiome — colibactin-producing E. coli and enterotoxigenic Bacteroides — accelerates the progression of its myriad adenomas toward carcinoma."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It passes to half the children: FAP is autosomal dominant with a 50% transmission risk, driving cascade genetic testing and reproductive choices, and pregnancy can trigger desmoid growth."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its desmoids can block the ureters: large intra-abdominal desmoid tumours in FAP can compress the ureters, causing hydronephrosis and obstructive renal impairment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its desmoids encase the great vessels: bulky mesenteric desmoid tumours in FAP can compress and encase major abdominal vessels, complicating surgery and risking ischaemia."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "NSAIDs slow the polyps: sulindac and celecoxib, in the same anti-inflammatory family as ibuprofen, reduce colorectal adenoma burden in FAP as an adjunct to surveillance and surgery."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its desmoids choke lymph flow: the mesenteric desmoid tumours that commonly arise in FAP can obstruct lymphatic drainage and cause chylous ascites."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet modifies colorectal risk: a high-fibre diet supports gut health and colorectal-cancer prevention generally, a backdrop to the surveillance and surgery that FAP's near-certain cancer risk demands."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy mostly misses it: FAP-associated colorectal cancers are microsatellite-stable from chromosomal instability, so unlike Lynch tumours they respond poorly to PD-1 checkpoint inhibitors."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for cancers that escape surveillance: metastatic FAP-associated colorectal cancer is treated with standard cytotoxic chemotherapy, and low-dose regimens are used for its desmoid tumours."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "A gut microbe abets the mutation: colibactin-producing Escherichia coli damages colonic DNA and accelerates APC-driven carcinogenesis, linking the gut microbiome to FAP's polyp-to-cancer progression."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Gardner's bony stigmata: the Gardner variant of FAP produces osteomas of the skull, mandible and long bones, plus dental anomalies and epidermoid cysts — extracolonic clues that often precede the polyposis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It threatens the child's liver: young children with FAP carry a markedly raised risk of hepatoblastoma, a liver cancer arising in the hepatic lobule, prompting AFP and ultrasound surveillance in infancy."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin curbs the polyps: beyond the sulindac and celecoxib used in FAP, regular aspirin reduces colorectal adenoma and cancer risk (as in the CAPP trials), a chemopreventive adjunct to the surveillance and surgery that anchor hereditary polyposis care."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Two syndromes, two medulloblastomas: FAP (via Turcot) predisposes to WNT-subgroup medulloblastoma while Gorlin syndrome causes the SHH subgroup—two inherited routes to the same childhood brain tumour through different pathways."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Duodenal neuroendocrine tumours: beyond adenomas, FAP raises the risk of duodenal and ampullary neuroendocrine tumours, adding to the upper-GI surveillance burden after colectomy."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Childhood-and-adult tumour syndromes: like Li-Fraumeni, FAP is an autosomal-dominant predisposition striking from childhood (hepatoblastoma, medulloblastoma) into adulthood, demanding lifelong multi-organ surveillance."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Hepatobiliary tumours: beyond colorectal cancer, FAP raises the risk of ampullary, biliary and pancreatic adenocarcinomas, including cholangiocarcinoma of the bile ducts."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Childhood liver cancer: FAP raises the risk of hepatoblastoma in young children, a primary liver tumour distinct from adult hepatocellular carcinoma but reflecting APC/Wnt's role in the liver."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Urinary-tract tumours: FAP can produce adenomatous polyps and rare carcinomas of the urinary tract, an uncommon extracolonic manifestation of widespread APC loss."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 chemoprevention: FAP polyps overexpress COX-2 and prostaglandins, the rationale for NSAID and celecoxib chemoprevention that shrinks polyp burden in the disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Adenoma-to-carcinoma switch: loss of TGF-β/SMAD tumour-suppressor signalling drives the progression of APC-initiated adenomas toward invasive carcinoma in FAP."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR downstream of APC loss: unrestrained Wnt signalling from APC loss activates mTOR, and mTOR inhibition reduces intestinal polyp formation in APC-deficient models."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT cooperation: AKT signalling cooperates with Wnt activation from APC loss to drive the growth of the adenomatous polyps that carpet the colon in FAP."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic progression: EZH2-mediated silencing of tumour-suppressor genes accompanies the adenoma-to-carcinoma progression of FAP polyps."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Polyp hypoxia: as FAP adenomas grow, HIF-1α stabilised in their hypoxic cores drives the VEGF angiogenesis that supports progression toward carcinoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase in progression: TERT reactivation immortalises cells along the adenoma-to-carcinoma sequence of FAP, one of the late events converting benign polyps into invasive colorectal cancer."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Desmoid driver: PDGF-driven fibroblast proliferation underlies the desmoid tumours that arise in FAP, a leading cause of death after prophylactic colectomy removes the cancer risk."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β escape: loss of SMAD4-mediated TGF-β growth suppression is a key step in the adenoma-carcinoma progression of FAP polyps, freeing them from a major antiproliferative brake."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Destruction-complex failure: APC scaffolds the GSK-3β destruction complex that degrades β-catenin, so the germline APC loss of FAP disables this control and locks in the Wnt signalling that initiates every adenoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Crypt stem-cell expansion: Notch signalling cooperates with Wnt in the intestinal crypt to maintain the stem-cell compartment, contributing to the adenoma formation that fills the FAP colon with thousands of polyps."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemoprevention target: COX-2-derived prostaglandins suppress caspase-3-mediated apoptosis in FAP adenomas, so NSAIDs and COX-2 inhibitors restore polyp apoptosis — the basis of chemoprevention in the syndrome."
  - target: 01-human/03-molecular/mutyh
    relation: connects-to
    note: "Polyposis differential: FAP (dominant APC loss) must be distinguished from MUTYH-associated polyposis, a recessive base-excision-repair defect that produces a similar but usually milder adenomatous polyposis, a key distinction for genetic counselling and family screening."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Hereditary-CRC differential: FAP and Lynch syndrome (MLH1 and other mismatch-repair genes) are the two major hereditary colorectal-cancer syndromes, distinguished by FAP's florid adenomatous polyposis versus Lynch's few polyps but high per-polyp cancer risk."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Desmoid signalling: FAP patients develop desmoid tumours, especially after abdominal surgery, in which FGFR and Wnt signalling drive the myofibroblast proliferation, a leading cause of FAP morbidity after the colon is removed."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Adenoma growth: EGFR signalling drives the proliferation of colorectal adenomas and carcinomas in the FAP adenoma-carcinoma sequence, an upstream receptor input feeding the RAS-MAPK axis and a target of anti-EGFR therapy in metastatic disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK progression: once a KRAS mutation is acquired (KRAS already mapped), the MAPK-ERK cascade drives the progression of FAP adenomas toward invasive carcinoma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K cooperation: PIK3CA mutations activating PI3K-AKT-mTOR (AKT and mTOR already mapped) are a cooperating late event in the malignant progression of FAP colorectal adenomas."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K suppressor loss: loss of the PTEN tumour suppressor releases the same PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped), cooperating with Wnt/β-catenin in the progression of FAP adenomas."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota-driven progression: gut-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) promotes the adenoma-to-carcinoma progression of the APC-mutant epithelium in familial adenomatous polyposis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Tumour-promoting inflammation: IL-6-STAT3 signalling (STAT3 already mapped) sustains the inflammatory, tumour-promoting microenvironment of the colorectal neoplasia of FAP."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is upregulated in colorectal adenoma-to-carcinoma progression and modulates tumour-cell adhesion and immune evasion in FAP-associated neoplasia."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A silencing releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle during the adenoma-carcinoma sequence in familial adenomatous polyposis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the inflammatory and immune microenvironment of FAP colorectal tumorigenesis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the adenomas and carcinomas arising in familial adenomatous polyposis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "APC loss stabilises β-catenin and drives cyclin-D-CDK4/6 activity (cyclin-D1 already mapped), accelerating the adenoma-carcinoma progression of familial adenomatous polyposis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by Wnt and PI3K-AKT signalling, is progressively lost in the polyp-to-cancer progression of familial adenomatous polyposis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the adenoma-to-carcinoma progression of familial adenomatous polyposis must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory colonic microenvironment that promotes the adenoma progression of familial adenomatous polyposis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the adenoma-carcinoma sequence of familial adenomatous polyposis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the progression of the adenomas of familial adenomatous polyposis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the adenoma-carcinoma sequence in familial adenomatous polyposis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the Wnt-driven adenomatous epithelial cells of familial adenomatous polyposis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the adenomas and carcinomas of familial adenomatous polyposis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the inflammatory tumor microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of familial adenomatous polyposis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the adenomas and carcinomas of familial adenomatous polyposis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the polyp and tumor microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the intestinal inflammation and tumor microenvironment of familial adenomatous polyposis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Gardner osteomas: the benign osteomas of the skull and jaw in the Gardner variant of FAP form through RANKL-regulated bone remodelling, part of the extraintestinal manifestations (skin cysts and eye CHRPE already mapped) that can signal the diagnosis before colonic symptoms."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Desmoid hormonal axis: the desmoid tumours (already mapped) that afflict familial adenomatous polyposis are hormone-responsive, often growing during pregnancy, implicating estrogen in the extracolonic fibromatosis that is a leading cause of death after colectomy."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the thousands of adenomas in familial adenomatous polyposis progress along the adenoma-carcinoma sequence, and antigen presentation is relevant to chemoprevention and vaccine strategies."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Occult bleeding: the carpet of adenomas in familial adenomatous polyposis bleeds chronically, and the resulting iron-deficiency anaemia lowering haemoglobin is often the sign that brings the polyposis or its cancers to attention."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunosurveillance effectors: cytotoxic CD8 T cells (MHC class II and perforin already mapped) police the many adenomas of familial adenomatous polyposis, and boosting this response underlies the vaccine chemoprevention being explored."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic colonic inflammation and the high proliferative turnover of the adenomas generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds the adenoma-carcinoma sequence in FAP."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive adenoma milieu: IL-10 in the adenoma microenvironment dampens the anti-tumour T-cell response (MHC class II and perforin already mapped), part of the immune tolerance the vaccine chemoprevention explored in FAP aims to overcome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and adenoma growth: the adipokine leptin links obesity to the colorectal adenoma-carcinoma sequence, promoting the proliferation (Wnt already mapped) that accelerates polyp growth in familial adenomatous polyposis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the adenoma-carcinoma sequence, a modifiable dietary influence on the polyp burden of FAP."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the adenomas of familial adenomatous polyposis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the numerous adenomas in familial adenomatous polyposis."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Dietary chemoprevention: omega-3 fatty acids are studied for colorectal chemoprevention, their anti-inflammatory action (prostaglandins already mapped) reducing the polyp burden alongside the NSAIDs used in familial adenomatous polyposis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity-adenoma adipokine: adiponectin, with leptin (already mapped), links the obesity-related metabolic milieu to the adenoma-carcinoma progression of familial adenomatous polyposis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related contribution to the polyp burden of familial adenomatous polyposis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-regulatory anaemia: hepcidin drives the iron sequestration that, with the chronic occult bleeding of the numerous adenomas (iron and haemoglobin already mapped), produces the anaemia of familial adenomatous polyposis."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Polyp-burden modifier: the obesity (leptin, adiponectin and resistin already mapped) is a modifiable factor that adds to the adenoma/polyp burden and the colorectal-cancer risk of familial adenomatous polyposis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate adenoma immunity: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the FAP adenomas along the adenoma-carcinoma sequence."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Adenoma antigen presentation: the dendritic cells present the neoantigens of the accumulating FAP adenomas, the immune surveillance whose evasion accompanies the progression to colorectal cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity along the adenoma-carcinoma sequence of FAP."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the FAP adenomas."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the FAP adenomas."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of the FAP adenomas."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the FAP adenomas."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the adenoma stroma contribute to the angiogenesis (VEGF already mapped) and the tumour-promoting type-2 microenvironment of the FAP polyps."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the mucosal immune microenvironment of the FAP adenomas."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the FAP adenoma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the FAP polyps."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the adenoma stroma of familial adenomatous polyposis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflamed adenoma stroma of familial adenomatous polyposis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "GI blood-loss iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the chronic gastrointestinal blood loss from the innumerable polyps of familial adenomatous polyposis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-FAP axis: TSLP, from the APC-deficient (already mapped) intestinal epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the polyposis stroma of FAP."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-FAP axis: bradykinin, via B1/B2 receptors on the polyp endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory milieu of the innumerable colorectal polyps of familial adenomatous polyposis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-FAP axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and the iron-deficiency anaemia of FAP, activates the EPOR on APC-deficient (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the FAP polyp stroma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-FAP axis: histamine, released by mast cells in the adenoma stroma of familial adenomatous polyposis, signals via H1/H2 receptors on APC-deficient (already mapped) epithelium, promoting polyp-stroma angiogenesis and the immunosuppressive adenoma microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-FAP axis: melatonin, via MT1/MT2 receptors on APC-deficient (already mapped) colonic epithelium, suppresses Wnt-driven (already mapped) proliferation, promotes apoptosis, and modulates the antioxidant defence of the FAP mucosa."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-FAP axis: testosterone, via androgen receptor signalling on the colonic epithelium and the desmoid-tumour (already mapped) stroma, modulates WNT/β-catenin proliferation and the sex-biased extracolonic manifestation risk in familial adenomatous polyposis."
---

# Familial Adenomatous Polyposis

## Overview

**Familial adenomatous polyposis (FAP)** is an autosomal dominant colorectal cancer predisposition syndrome caused by germline pathogenic variants in **APC** (adenomatous polyposis coli), a scaffold for the β-catenin destruction complex. FAP is characterized by the development of hundreds to thousands of colorectal adenomas beginning in adolescence, with a 100% lifetime risk of colorectal carcinoma (CRC) by the 4th-5th decade of life if the colon is not removed. In addition to colorectal polyps, FAP patients develop characteristic extracolonic manifestations: **desmoid tumors** (especially mesenteric, post-colectomy), **duodenal and periampullary adenomas** (lifetime cancer risk ~5-10%), **fundic gland polyps**, **congenital hypertrophy of the retinal pigment epithelium (CHRPE)**, and the classic **Gardner syndrome** triad (colorectal polyps + osteomas + soft tissue tumors). FAP accounts for ~1% of all CRC in Western countries. Prophylactic proctocolectomy is the definitive intervention, and endoscopic surveillance + celecoxib chemoprevention are used to manage residual rectal or duodenal adenoma burden [^kinzler-1991-apc] [^fearon-1990-vogelstein].

**Epidemiology:**
- Prevalence: 1/10,000-30,000 in Western populations; ~15,000-20,000 patients in the USA
- Inheritance: autosomal dominant; 50% transmission; ~25-30% de novo (no family history)
- APC germline variant: ~100% of classic FAP; ~70% of attenuated FAP (AFAP); ~30% of AFAP are MUTYH-associated polyposis (MAP), biallelic MUTYH mutations — autosomal recessive
- Classic FAP: typically >100 adenomas, carpeting colorectum
- Attenuated FAP (AFAP): 10-99 adenomas; later onset (age 30-40); more distal colon; APC mutations at 5' end (<168), 3' end (>1580), or exon 9

**APC mutation-phenotype correlations:**

| APC codon region | Phenotype | CRC onset | Desmoid |
|---|---|---|---|
| <168 | AFAP (few polyps, late onset) | 50-60 yrs | Rare |
| 168-1250 | Classic FAP | 30-40 yrs | Uncommon |
| 1250-1464 (MCR) | Profuse classic FAP | 20-30 yrs | Uncommon |
| 1310-2011 | Classic + desmoid risk | 30-40 yrs | High (~50%) |
| 1309 (hotspot) | Most severe FAP | 20s | Uncommon |
| >1580 | AFAP (3' attenuated) | 50-60 yrs | Rare |

## Structure

### APC and the β-catenin destruction complex in FAP

**Molecular basis:**
APC protein scaffolds the β-catenin destruction complex (APC + AXIN + GSK-3β + CK1α): sequential phosphorylation of β-catenin at S45 (CK1α) → T41/S37/S33 (GSK-3β) → β-TrCP E3 ligase → proteasomal degradation → Wnt-OFF; germline APC pathogenic variant (truncating) → one allele non-functional at birth → somatic second hit (LOH at 5q21 or somatic truncating mutation) in a single colonocyte → biallelic APC LOF → β-catenin accumulates → nuclear → TCF/LEF → MYC, CCND1, VEGFA → stem cell expansion → adenoma

**From one cell to thousands of polyps:**
In FAP, every colonocyte carries the germline APC first hit; over time, independent somatic second-hit events in separate stem cells → multiple simultaneous adenoma foci; because millions of colonocytes are at risk, FAP patients develop hundreds to thousands of adenomas rather than the 1-5 sporadic adenomas a normal individual accumulates over a lifetime; polyp density is proportional to the residual APC protein function (truncation site determines how many β-catenin binding 20 aa repeats are retained)

**Adenoma-to-carcinoma sequence in FAP:**
Within FAP adenomas, additional mutations accumulate: KRAS (G12D/V, ~50% of large adenomas) → SMAD4 LOF → TP53 LOF → CRC; the sequence is the same as sporadic CRC (Fearon-Vogelstein model) but the timeline is compressed and universal because the initiating APC LOF is pre-present; FAP CRC typically arises from one of the most dysplastic adenomas (often >1 cm, villous features, high-grade dysplasia)

### MUTYH-associated polyposis (MAP)

**MAP genetics and phenotype:**
- Biallelic pathogenic variants in MUTYH (MutY DNA glycosylase; base excision repair): autosomal recessive
- MUTYH removes adenine mispaired with 8-oxoguanine (oxidative DNA damage) → prevents G:C → T:A transversions
- Biallelic MUTYH LOF → accumulation of G:C → T:A mutations → accumulates KRAS G12C/D and APC codon 1309 mutations → adenoma formation without germline APC mutation
- Phenotype: 10-100 adenomas (AFAP-like); CRC lifetime risk ~80%; onset slightly later than classic FAP
- Molecular signature: characteristic APC somatic mutations (APC codon 1369, 1450 missense/nonsense from G:C→T:A transversions) + KRAS G12C (G:C→T:A)
- IHC/testing: MUTYH germline sequencing for biallelic testing; both copies must be mutated (compound heterozygous or homozygous); heterozygous MUTYH carriers: minor CRC risk increase (~1.5-2×)

## Function

### Carcinogenesis in FAP

**Polyp development timeline:**
- Age 10-15: microscopic adenomas detectable by high-resolution colonoscopy; CHRPE (CHRPE associated with mutations at codons 311-1444) already present from birth
- Age 15-25: macroscopic adenomas apparent; annual colonoscopy positive; polypectomy insufficient due to polyp burden
- Age 25-35: hundreds to thousands of polyps; progressive high-grade dysplasia in largest polyps
- Age 30-40: CRC inevitable without colectomy; 90% of untreated classic FAP patients develop CRC by age 40

**Extracolonic manifestations:**

*Gardner syndrome* (the full extracolonic FAP triad):
- **Osteomas**: mandible (most common), skull, long bones; benign; may precede colon polyps by years; detected by panoramic dental X-ray; marker of FAP in young patients
- **Desmoid tumors**: mesenteric (post-colectomy trigger) or abdominal wall; ~15-20% of FAP patients; especially APC codons 1310-2011; mesenteric desmoid can be life-threatening; see desmoid-tumor entry
- **Epidermoid/sebaceous cysts**: back, face, extremities; benign; FAP stigmata
- **Supernumerary teeth** (hyperdontia): rare; associated with FAP

*Duodenal/periampullary disease:*
- Duodenal adenomas: ~90% of FAP patients develop them by age 50; periampullary carcinoma lifetime risk ~5-10% (4th most common FAP cancer after CRC, desmoid, thyroid)
- **Spigelman staging** (0-IV based on number, size, histology, dysplasia of duodenal polyps): Stage IV → prophylactic pancreaticoduodenectomy (Whipple) consideration
- Surveillance: EGD every 1-5 years depending on Spigelman stage; ampullary/periampullary polyps get endoscopic ampullectomy

*Fundic gland polyps (FGPs):*
- ~90% of FAP patients; stomach body and fundus; NOT adenomas (non-dysplastic, hyperplastic-like glands); rarely progress to cancer; biopsied to confirm FGP vs adenoma

*CHRPE (congenital hypertrophy of retinal pigment epithelium):*
- Bilateral, multifocal CHRPE: highly specific for FAP with APC mutations at codons 311-1444; absent in AFAP (mutations <168 or >1580); detected by fundoscopy; useful for surveillance of at-risk relatives pre-genotyping
- Non-FAP CHRPE: unilateral, unifocal; much more common; not associated with APC mutation

*Thyroid cancer (papillary, cribriform-morular variant):*
- ~1-2% of FAP patients; young women predominance; cribriform-morular thyroid carcinoma is pathognomonic for FAP (nuclear β-catenin by IHC); annual thyroid US recommended by some guidelines

## Pathology

### Diagnosis and genetic evaluation

**Clinical diagnosis:**
- Classic FAP: ≥100 colorectal adenomas (any age) OR personal/family history of FAP + any adenomas
- AFAP: 10-99 colorectal adenomas + APC pathogenic variant OR biallelic MUTYH pathogenic variant
- Pathological: carpeting carpet adenomas; tubulovillous histology predominates large polyps; high-grade dysplasia precedes CRC

**Genetic testing:**
- APC germline sequencing (full coding + splice sites) + MLPA (multiplex ligation-dependent probe amplification) for large rearrangements: ~95% sensitivity for APC pathogenic variant in classic FAP
- Negative APC → MUTYH biallelic testing (rule out MAP)
- Negative APC+MUTYH → POLE/POLD1 germline testing (polymerase proofreading-associated polyposis, PPAP): rare; 10-100 adenomas + extracolonic features
- Cascade testing: all first-degree relatives of APC carrier should be offered testing; start surveillance colonoscopy at age 10-12 in APC+ relatives

### Surveillance protocols (NCCN/ESMO 2024)

**Colorectal:**
- APC-positive individuals (or at-risk relatives pending testing): annual sigmoidoscopy or colonoscopy from age 10-12
- Once polyps detected: annual colonoscopy + polypectomy until polyp burden mandates colectomy (typically age 15-25 for classic FAP)
- Post-colectomy (if IRA): annual or biannual flexible sigmoidoscopy of rectal remnant (pouch or stump); rectal polyp burden dictates completion proctectomy timing

**Duodenal/upper GI:**
- EGD starting age 25-30; frequency based on Spigelman stage:
  - Stage 0-I: every 5 years
  - Stage II: every 3 years
  - Stage III: every 1-2 years
  - Stage IV: surgical consultation (Whipple vs ampullectomy)

**Desmoid:**
- Baseline abdominal MRI at time of diagnosis (FAP with codons 1310-2011 or family history of desmoid); repeat MRI if symptomatic or annually in high-risk
- Desmoid screening intensified 1-2 years post-colectomy (surgery triggers desmoid development)

### Surgical management and chemoprevention

**Prophylactic colectomy options:**

1. **Total proctocolectomy with IPAA (ileal pouch-anal anastomosis)**: most definitive; removes all colorectal mucosa; ileostomy reversed; continence preserved (pouch acts as neorectum); risk of pouchitis, nighttime incontinence
2. **Colectomy with ileorectal anastomosis (IRA)**: preserves rectum; fewer complications; requires annual rectal surveillance; pouch formation later if rectal polyps progress
3. **Total proctocolectomy with end ileostomy**: for patients with low sphincter function or inability to undergo IRA/IPAA; permanent ileostomy
4. **Timing**: colectomy typically performed in teens to early 20s, before polyp burden is unmanageable; urgency based on polyp density and dysplasia

**Medical/chemopreventive therapy:**
- **Celecoxib (400 mg BID)**: FDA-approved for reduction of colorectal polyps in FAP patients; Phase 3 data: reduces duodenal + colorectal polyp number by ~28-45%; NOT a substitute for surveillance or surgery; concurrent use with post-colectomy surveillance
- **Sulindac (150 mg BID)**: non-selective COX-1/COX-2 NSAID; reduces adenoma number ~50-60% in some FAP patients; polyp regression but rarely elimination; rebound after stopping; GI toxicity limits use; used in AFAP patients with low adenoma burden
- **Eflornithine**: ornithine decarboxylase (ODC) inhibitor; explored in FAP (NCI clinical trials); less data than celecoxib

**Desmoid management in FAP:**
- Watch-and-wait (many FAP desmoids are stable): first-line for asymptomatic or slowly growing mesenteric desmoid
- Nirogacestat (FDA 2023): indicated for all progressing desmoid tumors regardless of etiology (FAP or sporadic); ovarian toxicity in women
- Sorafenib (VEGFR/PDGFR inhibitor): off-label; used in FAP desmoid with ORR ~15-20%
- Imatinib + sulindac combination: Phase 2 data in FAP desmoid; partial responses
- Surgery: reserved for localized desmoid with complete resection achievable; mesenteric desmoid often unresectable due to adherence to mesenteric vessels

**Prognosis:**
With modern surveillance and prophylactic colectomy: FAP is no longer an inevitable death sentence; colectomy by age 25 eliminates CRC risk from the colorectum; remaining risks are duodenal cancer (~5-10%), desmoid (~10-20% cause significant morbidity/mortality), papillary thyroid (~1-2%), and gastric cancer in high-risk populations; overall life expectancy now approaches near-normal if colectomy performed and extracolonic surveillance maintained

## Connections

- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — Germline APC truncating mutations cause FAP; codon position determines phenotype: codons 1250-1464 = classic profuse FAP; codons 1310-2011 = mesenteric desmoid risk; codons <168 or >1580 = attenuated FAP; codon 1309 hotspot = most severe; nuclear β-catenin in FAP adenomas
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — APC LOF → insufficient β-catenin destruction complex → nuclear β-catenin → TCF/LEF → Wnt-ON; FAP tumors show nuclear β-catenin by IHC; FAP desmoid (APC codons 1310-2011) driven by APC LOF, not CTNNB1 mutation; functionally equivalent outcome via distinct mechanisms
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — FAP: 100% CRC penetrance by age 40 without colectomy; proctocolectomy (IPAA or ileostomy) is definitive prevention; annual colonoscopy from age 10-12; celecoxib FDA-approved for FAP adenoma reduction; sulindac reduces polyp burden; duodenal surveillance required
- `connects-to` → **[Desmoid Tumor](../../07-system/desmoid-tumor/README.md)** — APC germline mutations (codons 1310-2011) → FAP-associated mesenteric desmoid; more aggressive than sporadic CTNNB1-mutant desmoid; post-colectomy FAP mesenteric desmoid is a leading mortality cause in FAP; nirogacestat FDA-approved for all desmoid including FAP-associated
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Biallelic MUTYH mutations cause an autosomal-recessive phenocopy of attenuated FAP (10-100 adenomas) with no germline APC mutation; defective 8-oxoG base-excision repair drives G:C→T:A transversions in APC and KRAS; ~30% of APC-negative AFAP is actually MAP.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS activating mutations (G12D/V, ~50% of large FAP adenomas) are a key step in the Fearon-Vogelstein adenoma-carcinoma sequence after biallelic APC loss; the same APC→KRAS→SMAD4→TP53 progression as sporadic CRC, but compressed and universal because APC LOF is pre-present.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — FAP carpets the colorectal mucosa with hundreds-to-thousands of adenomas; every colonocyte carries the germline APC first hit, so independent somatic second hits seed many foci; prophylactic proctocolectomy removes the at-risk mucosa and is curative for colorectal risk.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — FAP and hereditary diffuse gastric cancer are both dominant GI cancer syndromes but opposite in lesion: FAP carpets the colon with thousands of APC-driven adenomas, while HDGC seeds the stomach with CDH1-driven signet-ring foci that never form polyps — adenomatous versus diffuse.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — After colectomy the duodenum becomes FAP's most dangerous site: duodenal and ampullary adenomas (Spigelman-staged) progress to cancer in 3-5% and are the leading cause of cancer death in FAP, mandating lifelong upper-GI surveillance and sometimes pancreas-sparing duodenectomy.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — FAP confers a distinctive thyroid risk: cribriform-morular thyroid carcinoma, a rare papillary variant occurring almost exclusively in young women with FAP, can be the presenting sign of an undiagnosed APC mutation — prompting colonoscopy and germline testing when it appears.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — FAP and juvenile polyposis are both autosomal-dominant polyposis syndromes with high colorectal-cancer risk but differ in polyp biology: FAP carpets the colon with adenomas (APC/Wnt), while JPS makes fewer hamartomatous polyps (SMAD4/BMPR1A)—both need surveillance, often surgery.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — FAP affects the upper GI tract, not just the colon: nearly all patients develop fundic gland polyps and duodenal/ampullary adenomas, and gastric-cancer risk is raised, so after colectomy upper endoscopic surveillance of the stomach and duodenum becomes the priority.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — FAP is a disease of the intestinal epithelium's stem cells: germline APC loss removes the brake on Wnt/β-catenin in colonic crypt stem cells, so the entire epithelium is primed to form adenomas—hundreds to thousands—making the field, not a single clone, the cancer-prone tissue.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — FAP and Lynch syndrome are the major hereditary colorectal cancer syndromes but opposite: FAP floods the colon with hundreds of adenomatous polyps via APC loss, while Lynch causes few polyps but mismatch-repair failure—polyposis versus microsatellite instability.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — FAP and Peutz-Jeghers are both inherited GI polyposis conditions but differ in polyp type and gene: FAP's APC loss yields hundreds of adenomas, while PJS's STK11 loss gives hamartomatous polyps and mucocutaneous pigmentation—different polyps, different cancer risks.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — FAP can include brain tumors as Turcot syndrome: the same germline APC mutation that drives colonic polyposis also raises risk of medulloblastoma, linking Wnt-pathway dysregulation in gut and cerebellum—one mutated gene producing tumors in two very different organs.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — FAP is the textbook Wnt-pathway cancer syndrome: germline APC loss removes the brake on beta-catenin, so constitutive Wnt signaling drives the hundreds of colonic adenomas—mechanistically the same pathway activated somatically in most sporadic colorectal cancers.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach is an extracolonic FAP target: patients develop numerous fundic gland polyps and have raised gastric and duodenal cancer risk, so surveillance endoscopy of the upper GI tract complements colectomy in managing the syndrome.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — FAP raises the risk of pancreatic and other extracolonic cancers: APC loss predisposes beyond the colon to duodenal, pancreatic, thyroid and hepatoblastoma tumors—so even after prophylactic colectomy, FAP patients need broader cancer surveillance.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — FAP carpets the digestive tract with polyps: APC loss seeds hundreds to thousands of colonic adenomas that inevitably progress to colorectal cancer without colectomy, plus duodenal and gastric polyps—so FAP is a whole-gut polyposis, not just a colon disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — A retinal sign helps flag FAP: congenital hypertrophy of the retinal pigment epithelium (CHRPE) appears as pigmented fundus patches in many families, so an eye exam can provide an early, noninvasive clue to the APC mutation before polyps are found.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — FAP's Gardner variant shows in skin and bone: APC loss produces epidermoid cysts, fibromas and osteomas (especially of the jaw and skull), so these extraintestinal lumps of the integumentary and skeletal system can be the first visible sign of the syndrome.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — FAP raises childhood hepatoblastoma risk: young children with an APC mutation have a markedly increased chance of this liver cancer, so some families screen infants with abdominal ultrasound and AFP before the colonic polyps even appear.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — FAP overlaps brain tumors in Turcot syndrome: an APC mutation predisposes to medulloblastoma and other CNS tumors, so the colon and brain share a Wnt-pathway driver—linking a bowel polyposis syndrome to childhood brain cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — FAP's Gardner variant is a fibroblast disease too: APC loss drives fibroblasts to form desmoid tumors, Gardner fibromas, and excess scar, so the same Wnt activation that carpets the colon also makes connective tissue overgrow.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — FAP grows bony osteomas as a Gardner feature: APC loss spurs osteoblasts to build benign bone tumors in the jaw and skull, an extracolonic clue that—with skin cysts and dental anomalies—can flag the syndrome before colon polyps declare themselves.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — FAP's polyps grow because APC loss unleashes MYC: with APC gone, β-catenin piles up and switches on MYC, the master proliferation gene, so every adenoma is driven by the Wnt-to-MYC signal that turns normal colon lining into a carpet of polyps.
- `connects-to` → **[Immune System](../immune-system/README.md)** — FAP tumors are immunologically cold: unlike the mismatch-repair-deficient cancers of Lynch syndrome, APC-driven colorectal cancers are microsatellite-stable with few neoantigens, so they respond poorly to the checkpoint immunotherapy that helps Lynch tumors.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — FAP reaches the skin in its Gardner variant: beyond the colon, APC loss spawns epidermoid cysts, lipomas, fibromas and bony osteomas, so skin and jaw lumps can be the first visible clue to the syndrome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — FAP polyps recruit blood vessels via VEGF: as adenomas grow they drive VEGF-fueled angiogenesis, part of why COX-2 inhibitors—which lower this signaling—reduce polyp burden as chemoprevention in the syndrome.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages populate the stroma of FAP's polyps: drawn into the adenomas, tumor-associated macrophages secrete growth and inflammatory factors that help the APC-driven lesions progress toward colorectal cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — FAP's polyps bleed away iron: hundreds of colonic adenomas ooze blood, so chronic loss drains the body's iron into a deficiency anemia that can be an early clue before cancer develops.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — FAP extends cancer risk to the pancreas: beyond the colon, the APC defect raises the chance of duodenal, periampullary, and pancreatic tumors, so surveillance reaches the upper GI tract too.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — FAP's adenomas summon endothelial cells: VEGF from the growing polyps drives these vessel-lining cells to build blood supply, which is why COX-2 inhibitors that curb this angiogenesis shrink polyp burden.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — FAP is policed by light: lifelong colonoscopy hunts the polyps, and a dilated eye exam spots CHRPE—the dark retinal patches that mark the syndrome—both relying on visible-light viewing.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — FAP's desmoid tumors are fibrosis run amok: APC loss lets fibroblasts build invasive fibrous masses, the desmoids that become a leading cause of death once the colon is removed.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — FAP raises thyroid cancer risk: a distinctive cribriform-morular papillary thyroid carcinoma occurs especially in young women with the syndrome, so thyroid screening is advised.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads FAP's two telltale lesions: the dysplastic glands of its countless colonic adenomas, and the pigment-stuffed cells of CHRPE, the dark retinal patches that flag the syndrome at an eye exam.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — In the Gardner variant, FAP grows bone: benign osteomas sprout from the jaw and skull, bony overgrowths of the marrow-bearing facial bones that, with skin cysts, can betray the syndrome before the gut polyps do.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — FAP's osteomas are built of calcium: the Gardner-syndrome bony tumors lay down dense calcium-phosphate mineral, hard masses on the skull and jaw visible as bright opacities on imaging.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Gardner syndrome marks the skeleton and teeth: FAP's variant grows osteomas on the jaw and skull and brings dental anomalies — supernumerary teeth and odontomas — extracolonic clues that can predate the bowel polyps.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The Turcot variant ties FAP to the brain: alongside its colonic polyps it predisposes to CNS tumors, classically medulloblastoma, so neurological symptoms can be part of the syndrome's reach.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — FAP quietly enlarges the adrenals: benign adrenal adenomas are more common than in the general population, usually silent incidentalomas found on the imaging done to track the syndrome's other tumors.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Losing APC unleashes the growth genes: stabilized beta-catenin switches on cyclin D1 and MYC, pushing the colonic cells through the cell cycle — the molecular engine that turns the thousands of FAP polyps into ever-larger adenomas.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — FAP children risk a liver tumor: hepatoblastoma, arising from immature hepatocyte precursors, is hundreds of times more common in FAP infants, so screening with alpha-fetoprotein and ultrasound is offered in the early years.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Aspirin's polyp-shrinking effect runs partly through platelets: blocking platelet COX-1 — alongside COX-2 in the polyps — underlies why aspirin and other NSAIDs reduce colorectal adenoma burden, a chemoprevention strategy studied in FAP.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53 loss is the last step to cancer: FAP's polyps start with APC loss, then accumulate KRAS and finally TP53 mutations along the adenoma-carcinoma sequence, p53 failure marking the leap to invasive colorectal cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The immune climate shapes polyp fate: regulatory T cells infiltrate colorectal adenomas and dampen the local antitumor response, part of the microenvironment that lets some of FAP's countless polyps progress.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — It headlines the polyposis differential: FAP's hundreds of adenomas must be told apart from the hamartomatous polyposes like Cowden and Peutz-Jeghers, each a distinct gene with its own cancer spectrum and surveillance.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Hundreds of polyps bleed quietly: chronic occult blood loss from FAP's carpet of colonic adenomas (and any cancer) causes iron-deficiency anemia, sometimes the first clue that prompts the colonoscopy revealing the polyposis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Major surgery and cancer raise the clot risk: the prophylactic colectomy central to FAP care, and any colorectal cancer that develops, both predispose to perioperative venous thromboembolism needing prophylaxis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery brings infectious risk: anastomotic leak and pouchitis after the colectomy or ileal-pouch reconstruction that FAP requires can seed intra-abdominal infection and sepsis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation collaborates with the Wnt drive: NF-κB activation in the polyp-laden mucosa adds pro-survival, pro-proliferative signals to the APC-loss Wnt pathway, helping push FAP adenomas toward carcinoma.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 feeds the adenoma through STAT3: inflammatory IL-6/STAT3 signaling in the carpet of FAP polyps promotes epithelial proliferation and survival, one of the inflammatory accelerants of its inevitable cancer.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Hundreds of polyps and inflammation drain the blood: beyond the iron loss of chronic polyp bleeding, the inflammatory milieu of FAP can suppress erythropoiesis, adding an anemia of chronic disease to the iron deficiency.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its desmoids can throttle the ureters: the intra-abdominal desmoid tumors that FAP predisposes to can compress the ureters into obstruction, and prolonged hydronephrosis can erode kidney function toward chronic kidney disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the colon costs the bones: total colectomy and the malabsorption of vitamin D and calcium after surgery, plus the disease's chronic GI losses, leave FAP patients prone to bone loss and osteoporosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Prophylactic colectomy and inherited cancer risk weigh on the mind: facing inevitable colorectal cancer without surgery, living with a stoma or pouch, and the hereditary burden give FAP a substantial psychological toll.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Repeated abdominal surgery taxes healing: prophylactic colectomy, pouch construction and desmoid resections in FAP leave patients with recurrent surgical wounds, adhesions and the slow healing of reoperated tissue.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Surgery and desmoids irritate nerves: extensive abdominal operations and mesenteric desmoid tumors in FAP can entrap and compress nerves, producing chronic post-surgical and neuropathic abdominal pain.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Inevitable cancer risk and surveillance breed worry: the certainty of colorectal cancer without surgery and the lifelong endoscopic surveillance of FAP foster chronic health anxiety alongside depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — APC loss reaches the endocrine glands: FAP raises the risk of papillary thyroid cancer (the cribriform-morular variant) and adrenal adenomas, extending its tumour spectrum into the endocrine system.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It marks the eye and, rarely, the brain: FAP causes congenital hypertrophy of the retinal pigment epithelium, and the Turcot variant pairs colonic polyposis with brain tumours like medulloblastoma.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Gut bacteria speed its polyps to cancer: in FAP the colonic microbiome — colibactin-producing E. coli and enterotoxigenic Bacteroides — accelerates the progression of its myriad adenomas toward carcinoma.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It passes to half the children: FAP is autosomal dominant with a 50% transmission risk, driving cascade genetic testing and reproductive choices, and pregnancy can trigger desmoid growth.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its desmoids can block the ureters: large intra-abdominal desmoid tumours in FAP can compress the ureters, causing hydronephrosis and obstructive renal impairment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its desmoids encase the great vessels: bulky mesenteric desmoid tumours in FAP can compress and encase major abdominal vessels, complicating surgery and risking ischaemia.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs slow the polyps: sulindac and celecoxib, in the same anti-inflammatory family as ibuprofen, reduce colorectal adenoma burden in FAP as an adjunct to surveillance and surgery.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its desmoids choke lymph flow: the mesenteric desmoid tumours that commonly arise in FAP can obstruct lymphatic drainage and cause chylous ascites.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet modifies colorectal risk: a high-fibre diet supports gut health and colorectal-cancer prevention generally, a backdrop to the surveillance and surgery that FAP's near-certain cancer risk demands.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy mostly misses it: FAP-associated colorectal cancers are microsatellite-stable from chromosomal instability, so unlike Lynch tumours they respond poorly to PD-1 checkpoint inhibitors.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for cancers that escape surveillance: metastatic FAP-associated colorectal cancer is treated with standard cytotoxic chemotherapy, and low-dose regimens are used for its desmoid tumours.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — A gut microbe abets the mutation: colibactin-producing Escherichia coli damages colonic DNA and accelerates APC-driven carcinogenesis, linking the gut microbiome to FAP's polyp-to-cancer progression.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Gardner's bony stigmata: the Gardner variant of FAP produces osteomas of the skull, mandible and long bones, plus dental anomalies and epidermoid cysts — extracolonic clues that often precede the polyposis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It threatens the child's liver: young children with FAP carry a markedly raised risk of hepatoblastoma, a liver cancer arising in the hepatic lobule, prompting AFP and ultrasound surveillance in infancy.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin curbs the polyps: beyond the sulindac and celecoxib used in FAP, regular aspirin reduces colorectal adenoma and cancer risk (as in the CAPP trials), a chemopreventive adjunct to the surveillance and surgery that anchor hereditary polyposis care.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Two syndromes, two medulloblastomas: FAP (via Turcot) predisposes to WNT-subgroup medulloblastoma while Gorlin syndrome causes the SHH subgroup—two inherited routes to the same childhood brain tumour through different pathways.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Duodenal neuroendocrine tumours: beyond adenomas, FAP raises the risk of duodenal and ampullary neuroendocrine tumours, adding to the upper-GI surveillance burden after colectomy.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Childhood-and-adult tumour syndromes: like Li-Fraumeni, FAP is an autosomal-dominant predisposition striking from childhood (hepatoblastoma, medulloblastoma) into adulthood, demanding lifelong multi-organ surveillance.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Hepatobiliary tumours: beyond colorectal cancer, FAP raises the risk of ampullary, biliary and pancreatic adenocarcinomas, including cholangiocarcinoma of the bile ducts.
- `connects-to` → **[HCC](../hcc/README.md)** — Childhood liver cancer: FAP raises the risk of hepatoblastoma in young children, a primary liver tumour distinct from adult hepatocellular carcinoma but reflecting APC/Wnt's role in the liver.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Urinary-tract tumours: FAP can produce adenomatous polyps and rare carcinomas of the urinary tract, an uncommon extracolonic manifestation of widespread APC loss.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 chemoprevention: FAP polyps overexpress COX-2 and prostaglandins, the rationale for NSAID and celecoxib chemoprevention that shrinks polyp burden in the disease.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Adenoma-to-carcinoma switch: loss of TGF-β/SMAD tumour-suppressor signalling drives the progression of APC-initiated adenomas toward invasive carcinoma in FAP.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR downstream of APC loss: unrestrained Wnt signalling from APC loss activates mTOR, and mTOR inhibition reduces intestinal polyp formation in APC-deficient models.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT cooperation: AKT signalling cooperates with Wnt activation from APC loss to drive the growth of the adenomatous polyps that carpet the colon in FAP.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic progression: EZH2-mediated silencing of tumour-suppressor genes accompanies the adenoma-to-carcinoma progression of FAP polyps.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Polyp hypoxia: as FAP adenomas grow, HIF-1α stabilised in their hypoxic cores drives the VEGF angiogenesis that supports progression toward carcinoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase in progression: TERT reactivation immortalises cells along the adenoma-to-carcinoma sequence of FAP, one of the late events converting benign polyps into invasive colorectal cancer.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Desmoid driver: PDGF-driven fibroblast proliferation underlies the desmoid tumours that arise in FAP, a leading cause of death after prophylactic colectomy removes the cancer risk.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β escape: loss of SMAD4-mediated TGF-β growth suppression is a key step in the adenoma-carcinoma progression of FAP polyps, freeing them from a major antiproliferative brake.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — APC scaffolds the GSK-3β destruction complex that degrades β-catenin, so the germline APC loss of FAP disables this control and locks in the Wnt signaling that initiates every one of the syndrome's adenomas.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signaling cooperates with Wnt in the intestinal crypt to maintain the stem-cell compartment, contributing to the adenoma formation that fills the FAP colon with hundreds to thousands of polyps.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — COX-2-derived prostaglandins suppress caspase-3-mediated apoptosis in FAP adenomas, so NSAIDs and COX-2 inhibitors (sulindac, celecoxib) restore polyp apoptosis—the molecular basis of chemoprevention in the syndrome.
- `connects-to` → **[MUTYH](../../03-molecular/mutyh/README.md)** — FAP (dominant APC loss) must be distinguished from MUTYH-associated polyposis, a recessive base-excision-repair defect that produces a similar but usually milder adenomatous polyposis, a key distinction for genetic counseling and family screening.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — FAP and Lynch syndrome (MLH1 and other mismatch-repair genes) are the two major hereditary colorectal-cancer syndromes, distinguished by FAP's florid adenomatous polyposis versus Lynch's few polyps but high per-polyp cancer risk.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FAP patients develop desmoid tumors, especially after abdominal surgery, in which FGFR and Wnt signaling drive the myofibroblast proliferation, a leading cause of FAP morbidity after the colon is removed.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR signaling drives the proliferation of colorectal adenomas and carcinomas in the FAP adenoma-carcinoma sequence, an upstream receptor input feeding the RAS-MAPK axis and a target of anti-EGFR therapy in metastatic disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Once a KRAS mutation is acquired (KRAS already mapped), the MAPK-ERK cascade drives the progression of FAP adenomas toward invasive carcinoma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations activating PI3K-AKT-mTOR (AKT and mTOR already mapped) are a cooperating late event in the malignant progression of FAP colorectal adenomas.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of the PTEN tumor suppressor releases the same PI3K-AKT-mTOR axis (AKT, PIK3CA and mTOR already mapped), cooperating with Wnt/β-catenin in the progression of FAP adenomas.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) promotes the adenoma-to-carcinoma progression of the APC-mutant epithelium in familial adenomatous polyposis.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains the inflammatory, tumor-promoting microenvironment of the colorectal neoplasia of FAP.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is upregulated in colorectal adenoma-to-carcinoma progression and modulates tumor-cell adhesion and immune evasion in FAP-associated neoplasia.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A silencing releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle during the adenoma-carcinoma sequence in familial adenomatous polyposis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the inflammatory and immune microenvironment of FAP colorectal tumorigenesis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the adenomas and carcinomas arising in familial adenomatous polyposis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — APC loss stabilizes β-catenin and drives cyclin-D-CDK4/6 activity (cyclin-D1 already mapped), accelerating the adenoma-carcinoma progression of familial adenomatous polyposis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by Wnt and PI3K-AKT signaling, is progressively lost in the polyp-to-cancer progression of familial adenomatous polyposis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the adenoma-to-carcinoma progression of familial adenomatous polyposis must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory colonic microenvironment that promotes the adenoma progression of familial adenomatous polyposis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the adenoma-carcinoma sequence of familial adenomatous polyposis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the progression of the adenomas of familial adenomatous polyposis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the adenoma-carcinoma sequence in familial adenomatous polyposis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the Wnt-driven adenomatous epithelial cells of familial adenomatous polyposis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the adenomas and carcinomas of familial adenomatous polyposis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the inflammatory tumor microenvironment of familial adenomatous polyposis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of familial adenomatous polyposis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the adenomas and carcinomas of familial adenomatous polyposis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the polyp and tumor microenvironment of familial adenomatous polyposis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of familial adenomatous polyposis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of familial adenomatous polyposis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of familial adenomatous polyposis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the intestinal inflammation and tumor microenvironment of familial adenomatous polyposis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Gardner osteomas: the benign osteomas of the skull and jaw in the Gardner variant of FAP form through RANKL-regulated bone remodelling, part of the extraintestinal manifestations (skin cysts and eye CHRPE already mapped) that can signal the diagnosis before colonic symptoms.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Desmoid hormonal axis: the desmoid tumours (already mapped) that afflict familial adenomatous polyposis are hormone-responsive, often growing during pregnancy, implicating estrogen in the extracolonic fibromatosis that is a leading cause of death after colectomy.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the thousands of adenomas in familial adenomatous polyposis progress along the adenoma-carcinoma sequence, and antigen presentation is relevant to chemoprevention and vaccine strategies.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Occult bleeding: the carpet of adenomas in familial adenomatous polyposis bleeds chronically, and the resulting iron-deficiency anaemia lowering haemoglobin is often the sign that brings the polyposis or its cancers to attention.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunosurveillance effectors: cytotoxic CD8 T cells (MHC class II and perforin already mapped) police the many adenomas of familial adenomatous polyposis, and boosting this response underlies the vaccine chemoprevention being explored.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic colonic inflammation and the high proliferative turnover of the adenomas generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds the adenoma-carcinoma sequence in FAP.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive adenoma milieu: IL-10 in the adenoma microenvironment dampens the anti-tumour T-cell response (MHC class II and perforin already mapped), part of the immune tolerance the vaccine chemoprevention explored in FAP aims to overcome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and adenoma growth: the adipokine leptin links obesity to the colorectal adenoma-carcinoma sequence, promoting the proliferation (Wnt already mapped) that accelerates polyp growth in familial adenomatous polyposis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the adenoma-carcinoma sequence, a modifiable dietary influence on the polyp burden of FAP.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the adenomas of familial adenomatous polyposis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the numerous adenomas in familial adenomatous polyposis.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Dietary chemoprevention: omega-3 fatty acids are studied for colorectal chemoprevention, their anti-inflammatory action (prostaglandins already mapped) reducing the polyp burden alongside the NSAIDs used in familial adenomatous polyposis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity-adenoma adipokine: adiponectin, with leptin (already mapped), links the obesity-related metabolic milieu to the adenoma-carcinoma progression of familial adenomatous polyposis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related contribution to the polyp burden of familial adenomatous polyposis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron-regulatory anaemia: hepcidin drives the iron sequestration that, with the chronic occult bleeding of the numerous adenomas (iron and haemoglobin already mapped), produces the anaemia of familial adenomatous polyposis.
- `connects-to` → **[Obesity](../obesity/README.md)** — Polyp-burden modifier: the obesity (leptin, adiponectin and resistin already mapped) is a modifiable factor that adds to the adenoma/polyp burden and the colorectal-cancer risk of familial adenomatous polyposis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate adenoma immunity: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the FAP adenomas along the adenoma-carcinoma sequence.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Adenoma antigen presentation: the dendritic cells present the neoantigens of the accumulating FAP adenomas, the immune surveillance whose evasion accompanies the progression to colorectal cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity along the adenoma-carcinoma sequence of FAP.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the FAP adenomas.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the FAP adenomas.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of the FAP adenomas.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the FAP adenomas.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the adenoma stroma contribute to the angiogenesis (VEGF already mapped) and the tumour-promoting type-2 microenvironment of the FAP polyps.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the mucosal immune microenvironment of the FAP adenomas.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the FAP adenoma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the FAP polyps.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the adenoma stroma of familial adenomatous polyposis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflamed adenoma stroma of familial adenomatous polyposis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — GI blood-loss iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the chronic gastrointestinal blood loss from the innumerable polyps of familial adenomatous polyposis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-FAP axis: TSLP, from the APC-deficient (already mapped) intestinal epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the polyposis stroma of FAP.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-FAP axis: bradykinin, via B1/B2 receptors on the polyp endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory milieu of the innumerable colorectal polyps of familial adenomatous polyposis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-FAP axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and the iron-deficiency anaemia of FAP, activates the EPOR on APC-deficient (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the FAP polyp stroma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-FAP axis: histamine, released by mast cells in the adenoma stroma of familial adenomatous polyposis, signals via H1/H2 receptors on APC-deficient (already mapped) epithelium, promoting polyp-stroma angiogenesis and the immunosuppressive adenoma microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-FAP axis: melatonin, via MT1/MT2 receptors on APC-deficient (already mapped) colonic epithelium, suppresses Wnt-driven (already mapped) proliferation, promotes apoptosis, and modulates the antioxidant defence of the FAP mucosa.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-FAP axis: testosterone, via androgen receptor signalling on the colonic epithelium and the desmoid-tumour (already mapped) stroma, modulates WNT/β-catenin proliferation and the sex-biased extracolonic manifestation risk in familial adenomatous polyposis.

[^kinzler-1991-apc]: Kinzler KW, Nilbert MC, Su LK, et al. Identification of FAP locus genes from chromosome 5q21. *Science.* 1991;253(5020):661-665. [doi:10.1126/science.1651562](https://doi.org/10.1126/science.1651562) · [PubMed 1651562](https://pubmed.ncbi.nlm.nih.gov/1651562/)
[^fearon-1990-vogelstein]: Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. *Cell.* 1990;61(5):759-767. [doi:10.1016/0092-8674(90)90186-i](https://doi.org/10.1016/0092-8674(90)90186-i) · [PubMed 2188735](https://pubmed.ncbi.nlm.nih.gov/2188735/)
