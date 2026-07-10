---
schema: human-scale-entry/v1
id: mutyh-associated-polyposis
name: MUTYH-Associated Polyposis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "MUTYH-associated polyposis (MAP) is an autosomal recessive CRC predisposition syndrome caused by biallelic MUTYH mutations; 10-100 colorectal adenomas; CRC risk ~40-75% lifetime; two founder variants (Y179C, G396D) in most Western patients; annual colonoscopy from age 25."
aliases: ["MAP", "MUTYH-associated polyposis", "MYH-associated polyposis", "biallelic MUTYH", "MUTYH polyposis", "MAP CRC", "MYH polyposis", "autosomal recessive polyposis", "MAP colorectal"]
sources:
  - id: sieber-2003-mutyh-map
    type: peer-reviewed
    cite: "Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. N Engl J Med. 2003;348(9):791-799."
    doi: "10.1056/NEJMoa025283"
    pmid: "12606733"
    url: "https://doi.org/10.1056/NEJMoa025283"
  - id: al-tassan-2002-mutyh
    type: peer-reviewed
    cite: "Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. Nat Genet. 2002;30(2):227-232."
    doi: "10.1038/ng828"
    pmid: "11818965"
    url: "https://doi.org/10.1038/ng828"
cross_links:
  - target: 01-human/03-molecular/mutyh
    relation: connects-to
    note: "Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "MAP adenomas harbor somatic APC mutations driven by MUTYH-induced G:C→T:A transversions (SBS18); APC germline (FAP) and MUTYH biallelic (MAP) cause polyposis via distinct mechanisms (Wnt dysregulation vs oxidative mutational load); germline testing distinguishes both."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "MAP-associated CRC is predominantly right-sided; MUTYH SBS18 signature drives KRAS G12C transversions in MAP-CRC; overall CRC risk ~40-75% lifetime by age 60; annual colonoscopy with polypectomy from age 25 is the primary prevention strategy."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MUTYH-induced SBS18 (G:C→T:A transversions) drives KRAS G12C in ~70% of MAP-CRC; KRAS G12C is rare in sporadic CRC (~2-5%) but prevalent in NSCLC; G12C in CRC should prompt MUTYH germline testing; sotorasib and adagrasib (KRAS G12C inhibitors) show modest activity in CRC G12C."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MAP adenomas harbor somatic APC G→T transversions (SBS18) → APC loss → Wnt/β-catenin activation → adenoma initiation; MAP APC transversions create the same Wnt dysregulation as FAP germline truncations via MUTYH oxidative load; CTNNB1 G→T transversions also occur in MAP adenomas."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "MAP and Lynch are key non-FAP hereditary CRC syndromes: MAP (biallelic MUTYH, recessive, MSS, KRAS G12C) vs Lynch (MMR, dominant, MSI-H, extracolonic cancers); MAP is MSS → anti-PD-1 ICB inactive; Lynch MSI-H → pembrolizumab-responsive; germline testing distinguishes both."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "MUTYH-associated polyposis and HLRCC are hereditary cancer syndromes but utterly different: MAP is recessive MUTYH repair failure causing oxidative mutations and colonic polyposis; HLRCC is dominant FH (Krebs-cycle) loss causing fumarate-driven leiomyomas and kidney cancer."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is MAP's main target: biallelic MUTYH failure to repair oxidative 8-oxoguanine lesions lets G:C→T:A transversions accumulate in colonic epithelium, seeding 10-100 adenomas with a ~40-75% lifetime CRC risk — managed by colonoscopy from the mid-20s."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Beyond the colon, MAP affects the upper GI tract: duodenal adenomas develop in ~17-25% of patients (with a smaller duodenal cancer risk than FAP), so periodic upper endoscopy with attention to the ampulla is added to colonoscopic surveillance in MUTYH biallelic carriers."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "MAP and juvenile polyposis are inherited polyposis syndromes distinguished by polyp histology: MAP (biallelic MUTYH) produces adenomatous polyps from defective oxidative DNA repair, while juvenile polyposis (SMAD4/BMPR1A) produces hamartomatous polyps."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "MAP and Peutz-Jeghers are polyposis syndromes at different poles: MAP's MUTYH-driven adenomas carry high colorectal cancer risk through the classic adenoma-carcinoma sequence, while Peutz-Jeghers' STK11 hamartomas plus mucocutaneous pigmentation raise risk across many organs."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "MAP raises upper-GI as well as colorectal risk: many patients develop duodenal and gastric polyps, and gastric/duodenal cancer risk is elevated, so MUTYH biallelic carriers need upper-endoscopic surveillance alongside their colonoscopy."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "MAP and HDGC are inherited GI cancer syndromes with different mechanisms: MAP from biallelic MUTYH loss causing colorectal polyposis, HDGC from CDH1 loss causing diffuse gastric and lobular breast cancer—both warrant upper- and lower-GI surveillance."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "MAP carries extracolonic cancer risk including the pancreas: biallelic MUTYH loss raises risk of duodenal and modestly pancreatic cancers, since unrepaired oxidative DNA damage can transform other epithelia too—so surveillance extends to the upper GI tract."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "MAP raises gynecologic as well as colorectal cancer risk: biallelic MUTYH carriers have increased endometrial (and ovarian) cancer rates, as unrepaired oxidative mutations accumulate in tissues beyond the colon—broadening surveillance for affected women."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "MAP carpets the intestinal epithelium with adenomas: defective MUTYH base-excision repair lets oxidative G-to-T mutations accumulate in colonic crypt cells, driving the tens-to-hundreds of polyps—fewer than FAP but on the same adenoma-carcinoma path."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "MAP extends beyond the colon to the upper GI tract: like FAP, it raises the risk of duodenal and gastric polyps and cancer, so surveillance includes upper endoscopy—the same MUTYH repair defect mutating epithelium throughout the gut."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MAP tumors progress through the usual colorectal genes: MUTYH loss seeds characteristic G-to-T transversions in APC and KRAS, and TP53 loss later drives invasion—so a base-excision-repair defect feeds the standard adenoma-carcinoma mutation sequence."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "MUTYH-associated polyposis predisposes across the digestive tract: biallelic MUTYH loss seeds adenomatous polyps and cancer in the colon plus duodenal and gastric tumors, so it is managed like a milder, recessive cousin of FAP with GI surveillance."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MAP is fundamentally a failure to repair oxidative DNA damage: MUTYH normally excises adenine mispaired with 8-oxoguanine, the lesion left when reactive oxygen attacks DNA, so its loss lets oxygen-driven G:C-to-T:A mutations accumulate and seed polyps."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "MAP raises risk beyond the gut, including bladder cancer: the same defective oxidative-damage repair predisposes the urothelium, so MUTYH carriers face a modestly increased risk of bladder and other extraintestinal cancers warranting awareness."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "MUTYH-driven tumors are hypermutated and immunogenic: unrepaired oxidative damage produces a heavy load of G-to-T mutations and neoantigens that cytotoxic T cells can recognize, so checkpoint immunotherapy is of interest in these cancers."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "MUTYH-associated polyposis raises risk beyond the bowel: biallelic carriers face a modestly increased rate of ovarian and other extracolonic cancers, so management considers gynecologic risk alongside the dominant colorectal surveillance."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Breast cancer is a debated MUTYH extracolonic risk: some studies link biallelic MUTYH loss to a modest rise in breast cancer, adding it to the extracolonic tumors weighed when counseling families with the syndrome."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "MUTYH-associated polyposis writes its mutations as G→T transversions: failed repair of oxidized guanine misspells DNA, hitting APC, KRAS, and tumor suppressors like CDKN2A—a distinctive oxidative signature that turns colon polyps cancerous."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "MAP tumors carry a heavy mutation load that can alert NK cells: the oxidative damage spawns many altered proteins, marking cells for natural killer (and T-cell) attack and making these cancers candidates for immunotherapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "MAP's mutation-rich tumors give dendritic cells plenty to present: the neoantigens from oxidative DNA errors can be displayed to prime T cells, an immune opening that checkpoint therapy may exploit in mismatch-proficient but heavily mutated cancers."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "MAP's colorectal cancers spread to the liver: like other bowel cancers, the tumors that arise from MUTYH-driven polyps metastasize first to the liver through the portal vein, making liver imaging key to staging and follow-up."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation via NF-kB helps MAP polyps progress: in the colon, this inflammatory switch supports survival and proliferation of the mutation-laden cells, adding an inflammatory push to the oxidative DNA damage that defines the syndrome."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells temper the immune response to MAP's mutated tumors: though the oxidative-damage cancers carry many neoantigens, Tregs in the infiltrate restrain the attack, a brake that checkpoint therapy could lift in heavily mutated cases."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "MUTYH-associated polyposis bleeds iron from the colon: its adenomas ooze blood, so iron-deficiency anemia can be the quiet first clue that prompts the colonoscopy revealing the polyps."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "MAP's hypermutated tumors draw macrophages: oxidative-damage mutations spawn neoantigens that pull a dense immune infiltrate including macrophages into the colorectal cancers."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "MAP's colorectal cancers grow in fibrosis: as the adenomas turn malignant they provoke a desmoplastic fibrous stroma that supports invasion, the scar-like tissue typical of colon cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons keep MAP patients alive: lifelong colonoscopy is the surveillance backbone, finding and clearing polyps before they turn cancerous, while upper endoscopy and imaging watch the duodenum where MAP's extracolonic tumors also arise."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "MAP reaches beyond the colon to the thyroid: like FAP, it carries an increased risk of papillary thyroid cancer, so thyroid examination and ultrasound are folded into the surveillance these patients receive for life."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MAP can announce itself on the skin: like other polyposis syndromes it is associated with sebaceous tumors and epidermoid cysts, cutaneous clues that can prompt the genetic testing which uncovers the underlying colon-cancer risk."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "MAP fails to scrub oxidative DNA damage: the MUTYH enzyme normally repairs 8-oxoguanine, the lesion that reactive oxygen leaves in DNA, so without it those errors lock in as the G-to-T mutations that seed the polyps."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "MAP shares some bony features with FAP: osteomas of the jaw and skull and dental anomalies can occur, bony overgrowths of the marrow-bearing facial bones in this milder polyposis cousin."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Pigmented retinal patches occasionally mark MAP: CHRPE, the dark spots on the retina classic for FAP, can appear here too, a clue an ophthalmologist may spot in this related polyposis syndrome."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "MAP looks normal to the Lynch test: its tumors keep their mismatch-repair proteins, so the MLH1/MSH2/MSH6/PMS2 antibody panel stays intact and the cancers are microsatellite-stable — the flaw lies instead in base-excision repair, found only by gene sequencing."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Bleeding polyps drain the red cells: the slow ooze from MAP's colonic adenomas often surfaces first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic blood loss that should trigger colonoscopy."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Oxidative damage is the heart of MAP: with MUTYH unable to repair the 8-oxoguanine lesions that reactive oxygen leaves in DNA, an antioxidant-rich, high-fiber diet whose butyrate nourishes colonocytes is part of the prevention advice alongside surveillance."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "MAP breaks the dominant-inheritance pattern of its cousins: it is autosomal recessive, so two carrier parents — often with no polyposis themselves — have a 1-in-4 risk each pregnancy, making partner carrier testing and recurrence counseling central to families."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Aspirin's colorectal protection extends here: blocking platelet COX-1 and the tumor-promoting signals platelets release underpins the chemoprevention studied across hereditary colorectal syndromes, including MUTYH-driven polyposis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "The repair defect leaves an immune fingerprint: MUTYH loss spawns a heavy load of G-to-T mutations and neoantigens, drawing B cells and plasma cells into the tumor — an immune-rich profile that may make these cancers responsive to checkpoint therapy."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "It breaks a different repair system than Lynch: MAP fails base-excision repair of oxidative damage, whereas Lynch fails mismatch repair through genes like MSH2 — two distinct DNA-maintenance pathways whose loss converges on the same colon, a telling contrast."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "It sits in the polyposis differential: when many colon polyps appear, MAP must be distinguished from hamartomatous syndromes like Cowden (PTEN), since the gene found dictates the cancer risks, the inheritance pattern, and which relatives to test."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "A second hereditary-cancer comparison: unlike BRCA-driven HBOC which fails double-strand-break repair, MAP fails oxidative base repair, yet both are recessive-versus-dominant lessons in how a single broken DNA-maintenance gene seeds a familial cancer syndrome."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "The polyps bleed unseen: chronic occult blood loss from MAP's colonic adenomas or an arising cancer causes iron-deficiency anemia, sometimes the finding that triggers the colonoscopy revealing the polyposis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cancer and its surgery raise the clot risk: a colorectal cancer developing in MAP and the colectomy used to treat heavy polyposis both predispose to perioperative venous thromboembolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Bowel surgery carries infectious risk: the colectomy that high polyp burden eventually requires can be complicated by anastomotic leak and intra-abdominal sepsis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Inflammation feeds the oxidatively-damaged mucosa: IL-6-driven STAT3 signaling adds proliferation and survival to the G:C→T:A mutation burden of MUTYH loss, accelerating the polyps' progression to colorectal cancer."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Wnt activation drives the cell cycle through cyclin D1: the APC/Wnt activation arising in MUTYH-mutated adenomas pushes cyclin D1 expression, speeding the cell-cycle entry behind polyp growth."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Bleeding polyps and inflammation drain the blood: beyond the iron loss of chronically bleeding adenomas, the inflammation of MAP suppresses erythropoiesis, adding an anemia of chronic disease to the iron deficiency."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Colectomy and chemo strain the kidney: the surgery for MAP's polyp burden and any platinum chemotherapy for its colorectal cancers, plus dehydration from altered bowel anatomy, can threaten chronic kidney disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the colon costs the bones: colectomy and the malabsorption of calcium and vitamin D that follows, plus chronic GI losses, can leave reduced bone density in MUTYH-associated polyposis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Inherited cancer risk and surveillance weigh on the mind: living with a recessive polyposis syndrome, repeated colonoscopies and the prospect of colectomy carries a substantial psychological burden."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong cancer vigilance breeds worry: the recessive inheritance, scores of adenomas and unending colonoscopic surveillance of MAP foster chronic health anxiety alongside low mood."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Prophylactic colectomy is a healing challenge: the colectomy or proctocolectomy that removes the polyp-laden bowel in MAP leaves anastomoses and abdominal wounds at risk of leak and slow closure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Oxaliplatin chemotherapy stings the nerves: when MAP progresses to colorectal cancer treated with FOLFOX, the oxaliplatin causes a cold-triggered, often lasting peripheral neuropathy."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Oxidative damage meets the microbiome: MUTYH repairs the 8-oxoguanine lesions that reactive oxygen leaves in DNA, and the colonic microbiome's genotoxins and ROS add to the mutational load that drives MAP's polyps to cancer."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its tumour spectrum reaches the thyroid: beyond the colon, MAP raises the risk of thyroid and other extracolonic cancers, extending the syndrome into the endocrine system."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can show in the skin: MAP is associated with sebaceous gland tumours and other cutaneous lesions, overlapping the skin findings of the mismatch-repair polyposis syndromes."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It shares FAP's bony lesions: like familial adenomatous polyposis, MAP can cause osteomas of the jaw and skull among its FAP-like extracolonic features."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its DNA-repair defect raises mutation burden: MUTYH-deficient tumours accumulate many mutations from unrepaired oxidative DNA damage, which may make them responsive to checkpoint-inhibitor immunotherapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its cancers travel through the nodes: the colorectal cancers of MAP spread to regional lymph nodes, which determines staging and the need for adjuvant chemotherapy."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin lowers colorectal risk: like in other inherited polyposis, regular aspirin reduces colorectal adenoma and cancer risk in MUTYH-associated polyposis as chemoprevention."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It reaches the urinary tract: MUTYH-associated polyposis raises the risk of bladder and other urothelial cancers among its extracolonic tumours."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Advanced disease spreads to the lungs: the colorectal cancers of MUTYH-associated polyposis metastasise to the lungs and liver if they progress."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for cancers that develop: MUTYH-associated polyposis carries a high colorectal-cancer risk, and established cancers are treated with standard cytotoxic chemotherapy."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "A microbe that compounds the defect: colibactin-producing Escherichia coli damages colonic DNA, synergising with MUTYH's failure to repair oxidative lesions to accelerate adenoma-to-carcinoma progression."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Mostly microsatellite-stable: like FAP, MUTYH-associated colorectal cancers are usually microsatellite-stable and respond poorly to PD-1 checkpoint inhibitors, unlike Lynch tumours."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "A disease of unrepaired oxidative damage: MUTYH-associated polyposis comes from failure to excise the 8-oxoguanine lesions oxidative stress creates—the damage the NRF2 (NFE2L2) programme limits—so its mutations are the fingerprint of reactive oxygen on DNA."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Oxidative transversions can reach the marrow: biallelic MUTYH loss raises the risk not only of colorectal cancer but of myeloid neoplasms including acute myeloid leukaemia, which can carry the same G:C→T:A signature of unrepaired oxidative damage."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "It shares the polyposis APC/Wnt risk: MUTYH-associated polyposis drives somatic G:C→T:A hits in APC that activate Wnt, and like FAP it can spawn desmoid tumours—Wnt/β-catenin fibromatoses that complicate abdominal surgery."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Recessive DNA-repair cancer syndromes: like Bloom syndrome, MUTYH-associated polyposis is autosomal-recessive—biallelic loss of a DNA-repair gene (base-excision repair vs RecQ helicase) driving cancer through accumulated mutations."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "A hypermutated, immunogenic tumour: MUTYH-deficient cancers accumulate a distinctive G:C→T:A mutational signature and high neoantigen load, drawing tertiary lymphoid structures and responding to checkpoint blockade."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "FAP-like bony lesions: MUTYH-associated polyposis can show attenuated FAP features including osteomas and dental anomalies in the cortical bone, reflecting its overlap with APC-driven polyposis."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "The genomic-instability family: like Bloom and Werner syndromes, MUTYH-associated polyposis is an autosomal-recessive disorder of genome maintenance—here failed base-excision repair of oxidative DNA damage—predisposing to cancer through accumulated mutations."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Beyond the colon: biallelic MUTYH carriers have a raised risk of myeloid neoplasia, with the unrepaired oxidative mutations driving myelodysplasia and acute myeloid leukaemia as well as gut tumours."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "Different repair, same vulnerability: MUTYH performs base-excision repair of oxidative DNA damage while BRCA2 mediates homologous recombination of double-strand breaks—loss of either is an inherited route to cancer through unrepaired DNA."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Wnt-driven oncogene: the G:C→T:A transversions of MUTYH deficiency activate Wnt signalling and MYC, driving the adenoma-to-carcinoma progression of its colorectal polyps."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "KRAS and anti-EGFR resistance: MUTYH-associated tumours characteristically carry KRAS G12C transversions, which activate EGFR-MAPK signalling and confer resistance to anti-EGFR antibodies."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintaining telomeres accompanies the malignant progression of MUTYH-associated polyps toward invasive cancer."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT cooperation: AKT signalling cooperates with the KRAS and Wnt activation of MUTYH-associated polyps to drive their growth toward colorectal cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels MUTYH-associated adenoma cells through the G1 checkpoint as they progress along the polyp-to-carcinoma sequence."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Polyp hypoxia: as MUTYH-associated adenomas grow, HIF-1α stabilised in their hypoxic cores drives the VEGF angiogenesis supporting progression toward carcinoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β escape: loss of SMAD4-mediated TGF-β growth suppression is a step in the adenoma-carcinoma progression of MUTYH-associated polyps, beyond the initiating base-excision-repair defect."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "Serrated pathway: the G:C→T:A transversions caused by MUTYH loss can hit BRAF, contributing to the serrated route of colorectal carcinogenesis alongside the classic KRAS-driven adenoma sequence."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour macrophages: CCL2 recruits macrophages into the stroma of MUTYH-associated colorectal tumours, part of the inflammatory microenvironment that accompanies their progression."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Destruction-complex disruption: the APC mutations that MUTYH deficiency generates through G:C→T:A transversions disable the GSK-3β destruction complex, unleashing the Wnt signalling that drives the adenomas of the syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Crypt stem-cell expansion: Notch signalling cooperates with the unleashed Wnt pathway in the intestinal crypt to expand the stem-cell compartment, contributing to the polyp formation of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis evasion: MUTYH-associated adenomas evade caspase-3-mediated apoptosis, the cell-death pathway that NSAID and COX-2-inhibitor chemoprevention works to restore in colorectal polyposis syndromes."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative-lesion source: MUTYH repairs the oxidative DNA lesion 8-oxoguanine, so the reactive oxygen species generated by sources such as xanthine oxidase are the very damage whose accumulation, in biallelic MUTYH loss, drives the G:C→T:A transversions behind the polyposis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Chemoprevention: COX-derived prostaglandins promote adenoma growth, and NSAIDs and COX-2 inhibitors that block them are used for chemoprevention of polyposis, reducing polyp burden in the hereditary colorectal-cancer syndromes including MAP."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Hereditary-CRC differential: MUTYH-associated polyposis (recessive base-excision-repair defect) must be distinguished from Lynch syndrome (mismatch-repair genes such as MLH1) and FAP, each a distinct molecular route to hereditary colorectal cancer."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Transversion-driven MAPK: the G:C→T:A transversions of MUTYH deficiency preferentially hit KRAS (mapped), activating MAPK-ERK to drive adenoma progression in MUTYH-associated polyposis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K cooperation: PIK3CA activation of the PI3K-AKT axis (AKT already mapped) is a cooperating event in the malignant progression of MUTYH-associated colorectal adenomas."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle release: the cyclin-D-CDK4/6 axis (CDK4/6, cyclin-D1 and CDKN2A already mapped) releases E2F1 to drive proliferation in the carcinomas arising from MUTYH-associated polyposis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K cooperation: PTEN loss releases PI3K-AKT signalling (AKT and PIK3CA already mapped) that cooperates with the KRAS-driven Wnt activation in the colorectal tumourigenesis of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota inflammation: gut-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides an inflammatory cofactor in the adenoma-to-carcinoma progression of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Tumour-promoting inflammation: IL-6-STAT3 signalling (STAT3 already mapped) sustains the inflammatory, tumour-promoting microenvironment of MUTYH-associated colorectal neoplasia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is upregulated in the colorectal adenoma-to-carcinoma progression of MUTYH-associated polyposis, modulating adhesion and immune evasion."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), a tumour-promoting inflammatory input in MUTYH-associated polyposis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "The genomic instability of MUTYH-deficient base-excision repair generates cytosolic DNA sensed by cGAS-STING, shaping the immune microenvironment of MAP tumours."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "The mutational burden of MUTYH-deficient tumours drives IFN-STAT1 signalling, shaping their antitumour immune response and immunotherapy potential."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors govern the oxidative-stress defences whose failure, with the loss of MUTYH base-excision repair of oxidised guanine, drives the mutagenesis of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the neoantigen-rich tumours of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the adenoma-carcinoma progression of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory colonic microenvironment that promotes tumor progression in MUTYH-associated polyposis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression contributes to the epigenetic dysregulation of the colorectal tumors of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the progression of the adenomas of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the adenoma-carcinoma sequence in MUTYH-associated polyposis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the oxidatively stressed, base-excision-repair-deficient epithelial cells of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the tumors of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the adenomas and carcinomas of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the polyp and tumor microenvironment of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the intestinal inflammation and tumor microenvironment of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding anaemia: the adenomatous polyps of MUTYH-associated polyposis bleed into the gut, and the resulting chronic occult blood loss causes the iron-deficiency anaemia (iron already mapped) that lowers haemoglobin and can prompt investigation."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunogenic mutations: the defective repair of oxidative DNA damage in MUTYH-associated polyposis raises the tumour mutational burden, generating MHC-presented neoantigens that make some of its cancers responsive to immune surveillance and immunotherapy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint therapy: the elevated mutational burden of MUTYH-deficient colorectal cancers can render them responsive to PD-1 checkpoint blockade, an immune approach for the advanced tumours of this polyposis syndrome."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the immune response to the neoantigen-rich, high-mutational-burden cancers of MUTYH-associated polyposis, the basis of their potential checkpoint sensitivity."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: IL-10 in the tumour microenvironment dampens the anti-tumour response to the neoantigens generated by the defective oxidative-damage repair (PD-1 already mapped), one brake on the immunity that checkpoint blockade releases."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 help: helper T cells provide the CD4 help (MHC class II already mapped) that supports the cytotoxic response to the neoantigen-rich MUTYH-deficient tumours, part of the antitumour immunity relevant to their checkpoint therapy."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the adenoma-carcinoma sequence, a modifiable dietary influence on the polyp burden of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the polyp and tumour stroma of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and proliferation: the adipokine leptin links obesity to colorectal carcinogenesis, promoting the epithelial proliferation (Wnt already mapped) that can accelerate the adenoma-carcinoma sequence in MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the polyps of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the colorectal carcinogenesis, part of the modifiable adipokine influence on the cancer risk of MUTYH-associated polyposis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Dietary chemoprevention: dietary calcium reduces colorectal adenoma recurrence, binding the bile acids (cholesterol already mapped) that promote carcinogenesis, a modifiable factor in the risk reduction of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related modifiable colorectal-cancer risk of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-regulatory anaemia: hepcidin drives the iron sequestration that, with the chronic occult bleeding of the numerous adenomas (iron and haemoglobin already mapped), produces the anaemia of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "DNA-damage innate signalling: type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the DNA damage of the base-excision-repair-defective (MUTYH already mapped) cells, is part of the innate-immune response of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the colorectal-cancer risk of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immune infiltrate along the adenoma-carcinoma sequence of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the immune infiltrate of the adenomas of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory infiltrate along the adenoma-carcinoma sequence of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed adenoma stroma of MUTYH-associated polyposis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Adenoma stroma: the fibroblasts and the desmoplastic stroma support the accumulating adenomas along the adenoma-carcinoma sequence of MUTYH-associated polyposis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Adenoma stroma mast cells: the mast cells infiltrate the adenoma stroma and contribute to the angiogenesis and the type-2 (IgE already mapped) microenvironment of the polyps of MUTYH-associated polyposis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Chemoprevention vitamin: the vitamin D status modulates the colorectal-cancer (already mapped) risk along the adenoma-carcinoma sequence of MUTYH-associated polyposis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor countering the oxidative DNA damage (the 8-oxoguanine that MUTYH repairs), is part of the antioxidant chemoprevention dimension of MUTYH-associated polyposis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the MUTYH-associated polyps."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the MUTYH-associated polyps."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the complement dimension of the inflamed adenoma stroma of MUTYH-associated polyposis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Colorectal mucosal alarmin: TSLP from the MAP intestinal epithelium (already mapped) activates dendritic cells and mast cells, driving the inflammatory stroma of MUTYH-deficient polyposis and the adenoma-carcinoma progression to colorectal cancer (already mapped)."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Bleeding anaemia: erythropoietin supports erythropoiesis in the iron-deficiency anaemia from the chronic occult blood loss of the multiple adenomas of MAP; EPO is used adjunctively in MAP patients undergoing repeated colonoscopy and polypectomy for polyp surveillance."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Colonic inflammation: bradykinin activates B2 receptors in the MAP colorectal mucosa (intestinal-epithelium already mapped), amplifying the prostaglandin (already mapped) and NF-kB (already mapped) inflammation of the MUTYH-deficient polyposis stroma and colonic pain."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Colonic complement regulation: C1-INH controls the classical and alternative complement pathways (complement C5 already mapped) in the MUTYH-associated polyposis tumour microenvironment, modulating complement-dependent cytotoxicity against MAP colorectal adenoma cells."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine in polyposis: histamine from the mast cells infiltrating the MAP colorectal polyp stroma promotes VEGF (already mapped) angiogenesis and prostaglandin (already mapped) inflammation of the MUTYH-deficient adenoma mucosa."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Polyposis stroma periostin: periostin secreted by MAP cancer-associated fibroblasts and downstream of TGF-β (already mapped) activates the integrin-AKT (already mapped) pathway, promoting the MUTYH-deficient colorectal adenoma-to-carcinoma invasive progression."
---

# MUTYH-Associated Polyposis

## Overview

**MUTYH-associated polyposis (MAP)** is an **autosomal recessive** hereditary colorectal polyposis syndrome caused by biallelic pathogenic variants in the **MUTYH** (MutY DNA Glycosylase) gene on chromosome **1p34**. MAP is unique among major hereditary colorectal cancer syndromes in its recessive inheritance — all other well-characterized syndromes (FAP/APC, Lynch/MMR, PJS/STK11, JPS/SMAD4) are autosomal dominant. MAP affects approximately **1 in 15,000-20,000** individuals in European-ancestry populations. The phenotype is characterized by **10-100 colorectal adenomas** (occasionally more), elevated colorectal cancer (CRC) risk of ~40-75% lifetime, and an attenuated or FAP-like endoscopic appearance. Two founder pathogenic variants — **Y179C** and **G396D** — account for ~80% of MAP alleles in Western European and UK populations [^sieber-2003-mutyh-map] [^al-tassan-2002-mutyh].

**MAP phenotype compared to other colorectal polyposis syndromes:**

| Feature | MAP (MUTYH biallelic) | FAP (APC germline) | AFAP (APC, C/N-terminal) | Lynch (MMR germline) |
|---|---|---|---|---|
| Inheritance | Autosomal recessive | Autosomal dominant | Autosomal dominant | Autosomal dominant |
| Gene | MUTYH | APC | APC | MLH1/MSH2/MSH6/PMS2 |
| Polyp count | 10-100 (variable) | >100 (usually 1000s) | 10-100 | 0-5 (no polyp syndrome) |
| Polyp type | Adenomas + serrated | Adenomas | Adenomas | Few adenomas (MSI-H) |
| CRC lifetime risk | ~40-75% | ~100% (without surgery) | ~70% | ~40-80% (gene-specific) |
| Age of CRC | 40s-60s | 30-40s (untreated) | 40s-50s | 40-70s |
| De novo pattern | Siblings affected, parents unaffected | One parent usually affected | Variable | Variable |
| MSI | Microsatellite stable | Microsatellite stable | Microsatellite stable | MSI-High |

## Structure

### Genetic basis of MAP

**Biallelic MUTYH requirement:**
Both copies of MUTYH must be inactivated for MAP phenotype. Compound heterozygosity (two different pathogenic variants on separate alleles) is more common than homozygosity in outbred populations. The most frequent genotypes in European populations:

- **Y179C/G396D** (compound heterozygous): ~30-40% of MAP patients in UK/NL series
- **Y179C/Y179C** (homozygous): ~15-20%; associated with higher polyp burden
- **G396D/G396D** (homozygous): ~5-10%
- Other biallelic combinations: ~30-40%

**Founder variants:**
- **Y179C** (c.536A>G, p.Tyr179Cys): exon 7; disrupts 8-oxoG recognition by MUTYH; globally prevalent in European-ancestry populations; also present in Indian, Asian, and Hispanic populations at lower frequency
- **G396D** (c.1187G>A, p.Gly396Asp): exon 13; disrupts MUTYH 4Fe-4S cluster; common in UK, Dutch, Northern European
- **Other ethnic-specific variants**: South Asian MAP patients: E466del, Y104Cys; Japanese: G265del; Ashkenazi Jewish: rare (MUTYH MAP less prevalent in Ashkenazi population)

**Monoallelic (heterozygous) MUTYH carriers:**
- ~1-2% of European-ancestry general population
- ~1.5-2x elevated CRC risk (odds ratio ~1.4-1.6 in meta-analyses)
- Not MAP; do not need MAP surveillance protocol
- Recommend: colonoscopy every 3-5 years from age 40; intensity varies by family history and polyp findings

### Somatic mutation landscape in MAP tumors

MUTYH deficiency creates a characteristic **SBS18 mutational signature** (G:C→T:A transversions; COSMIC Mutational Signatures):
- APC somatic mutations: predominantly nonsense or missense G→T transversions (e.g., K1462N, E1309Stop converted to T); different from the frameshift/truncating APC variants in FAP; MAP APC mutations still activate Wnt/β-catenin
- KRAS somatic mutations: **G12C** (GGT→TGT) transversion in ~70% of MAP-associated CRC; KRAS G12C is rare in sporadic CRC (~2-5%) and prevalent in NSCLC (~14%); KRAS G12C in CRC should prompt MUTYH germline testing
- CTNNB1 (β-catenin) mutations: some MAP adenomas have CTNNB1 G→T transversions activating β-catenin
- Microsatellite stability: MAP tumors are **MSS** (microsatellite stable), unlike Lynch syndrome CRC (MSI-H); this is critical for correct prognostication and immunotherapy selection

## Function

### Disease mechanism

MUTYH deficiency prevents removal of adenine mispaired with 8-oxoguanine (8-oxoG) in the genome. Reactive oxygen species (dietary, inflammatory, metabolic) oxidize guanine to 8-oxoG at thousands of sites per cell per day. DNA polymerase inserts A opposite 8-oxoG → A:8-oxoG mispair. Without MUTYH:
1. A:8-oxoG → next replication → T:A permanently replaces G:C → **G:C→T:A transversion**
2. Transversions accumulate preferentially at GC-rich sequences (proto-oncogene codons and tumor suppressor codon hotspots)
3. Somatic APC G→T transversions → Wnt pathway activation → adenoma initiation
4. Additional transversions (KRAS G12C, CTNNB1) → adenoma-to-carcinoma progression

The key distinction from MMR-deficient (Lynch syndrome) carcinogenesis: MAP generates a different mutational signature (SBS18, large-scale transversions) and produces MSS tumors, while Lynch generates SBS6/SBS15 (small indel hypermutation) and MSI-H tumors.

### Colorectal adenoma progression in MAP

MAP adenomas are morphologically similar to sporadic conventional adenomas (tubular, tubulovillous, villous). However, MAP patients also develop **serrated polyps** (sessile serrated lesions, traditional serrated adenomas) at higher frequency than the general population — consistent with oxidative damage driving the serrated pathway through KRAS G12C activation. The serrated pathway adds to CRC risk beyond classical adenoma-carcinoma progression.

**Upper GI involvement:**
- ~50% of MAP patients develop **duodenal adenomas** (D1-D4); often periampullary; histologically similar to colorectal adenomas; lifetime risk of duodenal/small bowel cancer is elevated (~4-10%); Spigelman staging applied to duodenal polyposis in MAP
- Gastric fundic gland polyps: less common than in FAP but reported in MAP

**Extracolonic malignancies in MAP:**
- **Duodenal/small bowel cancer**: ~4-10% lifetime risk; surveillance recommended
- **Ovarian cancer**: possible modest elevation in some series (biologically plausible: oxidative BER role in ovarian epithelium)
- **Sebaceous gland tumors** (sebaceoma, sebaceous carcinoma): Muir-Torre-like phenotype in a subset of MAP patients; distinct from Lynch-associated Muir-Torre (MMR-deficient tumors); MAP sebaceous tumors are MSS
- **Bladder cancer**: slight elevation in some population-based studies

## Pathology

### Surveillance and management protocol

**Diagnosis criteria:**
- ≥10 colorectal adenomas + biallelic MUTYH pathogenic variants confirmed
- Or CRC with biallelic MUTYH + limited/absent family history (recessive pattern)
- Or CRC with SBS18 signature on tumor profiling → germline confirmation

**Colonoscopy surveillance:**
- From age **25-30** (or 5 years before earliest CRC in family)
- Every **1-2 years** if adenomas present (annual if multiple or large)
- Every **2-3 years** if polyp-free
- Polypectomy at each session; annual if polyp count difficult to control endoscopically
- Chromoendoscopy or image-enhanced endoscopy (NBI, FICE) to detect flat adenomas

**Upper GI surveillance:**
- EGD from age **30-35**
- Every 1-4 years depending on Spigelman stage for duodenal adenomas (Stage 0-II: 5 years; Stage III: 3 years; Stage IV: consider surgery)

**Colectomy indications:**
- Unmanageable polyp burden (>20-30 adenomas per annual colonoscopy with inadequate polypectomy)
- High-grade dysplasia in multiple adenomas
- CRC detected at surveillance
- Options: **segmental colectomy + continued surveillance** (acceptable if polyp burden is low/regional), **subtotal colectomy + ileorectal anastomosis (IRA)** (if diffuse colonic disease), **ileal pouch-anal anastomosis (IPAA)** (if rectum heavily involved)
- Timing: generally around age 40-50, guided by polyp burden and patient preference; much later than FAP (which requires surgery in teens-20s)

**Chemoprevention:**
- **Sulindac** and **celecoxib**: reduce adenoma count in MAP patients in small case series; rationale from FAP (APC-mutant) data; no randomized MAP-specific trial; used as adjunct to endoscopic surveillance
- Antioxidants (vitamin C, E, N-acetylcysteine): theoretical rationale (reduce ROS → reduce 8-oxoG); no clinical evidence for chemoprevention in MAP

### Family cascade testing

Because MAP is autosomal recessive: siblings of MAP patients are at **25%** risk (both parents are obligate carriers); parents are carriers (heterozygous) unless de novo. Cascade testing:
1. Test both parents → confirm each is monoallelic MUTYH carrier
2. Test all siblings: each has 25% chance of biallelic MUTYH; 50% chance of monoallelic (elevated risk)
3. Children of MAP patients: all children of a MAP patient are obligate monoallelic carriers; children are at MAP risk only if the other parent is also a MUTYH carrier (population carrier frequency ~1-2% → MAP child risk ~1-2% for each child of a MAP patient in an outbred population)

## Connections

- `connects-to` → **[MUTYH](../../03-molecular/mutyh/README.md)** — Germline biallelic MUTYH pathogenic variants cause MAP; two founder variants (Y179C and G396D) account for ~80% of Western MAP; monoallelic MUTYH carriers have modestly elevated CRC risk (~1.5-2x); MAP surveillance mimics FAP but with 1-2 year colonoscopy intervals.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — MAP adenomas harbor somatic APC mutations driven by MUTYH-induced G:C→T:A transversions (SBS18); APC germline (FAP) and MUTYH biallelic (MAP) cause polyposis via distinct mechanisms (Wnt dysregulation vs oxidative mutational load); germline testing distinguishes both.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — MAP-associated CRC is predominantly right-sided; MUTYH SBS18 signature drives KRAS G12C transversions in MAP-CRC; overall CRC risk ~40-75% lifetime by age 60; annual colonoscopy with polypectomy from age 25 is the primary prevention strategy.
- `connects-to` → **[FAP](../fap/README.md)** — MAP (biallelic MUTYH) mimics attenuated FAP (APC germline) but has autosomal recessive inheritance, fewer adenomas (10-100 vs >100 in FAP), later CRC onset (40-60s), and includes serrated polyps; genetic testing distinguishes both syndromes in apparent de novo polyposis.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — MUTYH-induced SBS18 (G:C→T:A transversions) drives KRAS G12C in ~70% of MAP-CRC; KRAS G12C is rare in sporadic CRC (~2-5%) but prevalent in NSCLC; G12C in CRC should prompt MUTYH germline testing; sotorasib and adagrasib (KRAS G12C inhibitors) show modest activity in CRC G12C.
- `connects-to` → **[Wnt/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — MAP adenomas harbor somatic APC G→T transversions (SBS18) → APC loss → Wnt/β-catenin activation → adenoma initiation; MAP APC transversions create the same Wnt dysregulation as FAP germline truncations via MUTYH oxidative load; CTNNB1 G→T transversions also occur in MAP adenomas.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — MAP and Lynch are key non-FAP hereditary CRC syndromes: MAP (biallelic MUTYH, recessive, MSS, KRAS G12C) vs Lynch (MMR, dominant, MSI-H, extracolonic cancers); MAP is MSS → anti-PD-1 ICB inactive; Lynch MSI-H → pembrolizumab-responsive; germline testing distinguishes both.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — MUTYH-associated polyposis and HLRCC are hereditary cancer syndromes but utterly different: MAP is recessive MUTYH repair failure causing oxidative mutations and colonic polyposis; HLRCC is dominant FH (Krebs-cycle) loss causing fumarate-driven leiomyomas and kidney cancer.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is MAP's main target: biallelic MUTYH failure to repair oxidative 8-oxoguanine lesions lets G:C→T:A transversions accumulate in colonic epithelium, seeding 10-100 adenomas with a ~40-75% lifetime CRC risk — managed by colonoscopy from the mid-20s.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Beyond the colon, MAP affects the upper GI tract: duodenal adenomas develop in ~17-25% of patients (with a smaller duodenal cancer risk than FAP), so periodic upper endoscopy with attention to the ampulla is added to colonoscopic surveillance in MUTYH biallelic carriers.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — MAP and juvenile polyposis are inherited polyposis syndromes distinguished by polyp histology: MAP (biallelic MUTYH) produces adenomatous polyps from defective oxidative DNA repair, while juvenile polyposis (SMAD4/BMPR1A) produces hamartomatous polyps.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — MAP and Peutz-Jeghers are polyposis syndromes at different poles: MAP's MUTYH-driven adenomas carry high colorectal cancer risk through the classic adenoma-carcinoma sequence, while Peutz-Jeghers' STK11 hamartomas plus mucocutaneous pigmentation raise risk across many organs.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — MAP raises upper-GI as well as colorectal risk: many patients develop duodenal and gastric polyps, and gastric/duodenal cancer risk is elevated, so MUTYH biallelic carriers need upper-endoscopic surveillance alongside their colonoscopy.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — MAP and HDGC are inherited GI cancer syndromes with different mechanisms: MAP from biallelic MUTYH loss causing colorectal polyposis, HDGC from CDH1 loss causing diffuse gastric and lobular breast cancer—both warrant upper- and lower-GI surveillance.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — MAP carries extracolonic cancer risk including the pancreas: biallelic MUTYH loss raises risk of duodenal and modestly pancreatic cancers, since unrepaired oxidative DNA damage can transform other epithelia too—so surveillance extends to the upper GI tract.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — MAP raises gynecologic as well as colorectal cancer risk: biallelic MUTYH carriers have increased endometrial (and ovarian) cancer rates, as unrepaired oxidative mutations accumulate in tissues beyond the colon—broadening surveillance for affected women.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — MAP carpets the intestinal epithelium with adenomas: defective MUTYH base-excision repair lets oxidative G-to-T mutations accumulate in colonic crypt cells, driving the tens-to-hundreds of polyps—fewer than FAP but on the same adenoma-carcinoma path.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — MAP extends beyond the colon to the upper GI tract: like FAP, it raises the risk of duodenal and gastric polyps and cancer, so surveillance includes upper endoscopy—the same MUTYH repair defect mutating epithelium throughout the gut.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — MAP tumors progress through the usual colorectal genes: MUTYH loss seeds characteristic G-to-T transversions in APC and KRAS, and TP53 loss later drives invasion—so a base-excision-repair defect feeds the standard adenoma-carcinoma mutation sequence.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — MUTYH-associated polyposis predisposes across the digestive tract: biallelic MUTYH loss seeds adenomatous polyps and cancer in the colon plus duodenal and gastric tumors, so it is managed like a milder, recessive cousin of FAP with GI surveillance.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MAP is fundamentally a failure to repair oxidative DNA damage: MUTYH normally excises adenine mispaired with 8-oxoguanine, the lesion left when reactive oxygen attacks DNA, so its loss lets oxygen-driven G:C-to-T:A mutations accumulate and seed polyps.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — MAP raises risk beyond the gut, including bladder cancer: the same defective oxidative-damage repair predisposes the urothelium, so MUTYH carriers face a modestly increased risk of bladder and other extraintestinal cancers warranting awareness.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — MUTYH-driven tumors are hypermutated and immunogenic: unrepaired oxidative damage produces a heavy load of G-to-T mutations and neoantigens that cytotoxic T cells can recognize, so checkpoint immunotherapy is of interest in these cancers.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — MUTYH-associated polyposis raises risk beyond the bowel: biallelic carriers face a modestly increased rate of ovarian and other extracolonic cancers, so management considers gynecologic risk alongside the dominant colorectal surveillance.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Breast cancer is a debated MUTYH extracolonic risk: some studies link biallelic MUTYH loss to a modest rise in breast cancer, adding it to the extracolonic tumors weighed when counseling families with the syndrome.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — MUTYH-associated polyposis writes its mutations as G→T transversions: failed repair of oxidized guanine misspells DNA, hitting APC, KRAS, and tumor suppressors like CDKN2A—a distinctive oxidative signature that turns colon polyps cancerous.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — MAP tumors carry a heavy mutation load that can alert NK cells: the oxidative damage spawns many altered proteins, marking cells for natural killer (and T-cell) attack and making these cancers candidates for immunotherapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — MAP's mutation-rich tumors give dendritic cells plenty to present: the neoantigens from oxidative DNA errors can be displayed to prime T cells, an immune opening that checkpoint therapy may exploit in mismatch-proficient but heavily mutated cancers.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — MAP's colorectal cancers spread to the liver: like other bowel cancers, the tumors that arise from MUTYH-driven polyps metastasize first to the liver through the portal vein, making liver imaging key to staging and follow-up.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation via NF-kB helps MAP polyps progress: in the colon, this inflammatory switch supports survival and proliferation of the mutation-laden cells, adding an inflammatory push to the oxidative DNA damage that defines the syndrome.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells temper the immune response to MAP's mutated tumors: though the oxidative-damage cancers carry many neoantigens, Tregs in the infiltrate restrain the attack, a brake that checkpoint therapy could lift in heavily mutated cases.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — MUTYH-associated polyposis bleeds iron from the colon: its adenomas ooze blood, so iron-deficiency anemia can be the quiet first clue that prompts the colonoscopy revealing the polyps.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — MAP's hypermutated tumors draw macrophages: oxidative-damage mutations spawn neoantigens that pull a dense immune infiltrate including macrophages into the colorectal cancers.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — MAP's colorectal cancers grow in fibrosis: as the adenomas turn malignant they provoke a desmoplastic fibrous stroma that supports invasion, the scar-like tissue typical of colon cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons keep MAP patients alive: lifelong colonoscopy is the surveillance backbone, finding and clearing polyps before they turn cancerous, while upper endoscopy and imaging watch the duodenum where MAP's extracolonic tumors also arise.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — MAP reaches beyond the colon to the thyroid: like FAP, it carries an increased risk of papillary thyroid cancer, so thyroid examination and ultrasound are folded into the surveillance these patients receive for life.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MAP can announce itself on the skin: like other polyposis syndromes it is associated with sebaceous tumors and epidermoid cysts, cutaneous clues that can prompt the genetic testing which uncovers the underlying colon-cancer risk.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — MAP fails to scrub oxidative DNA damage: the MUTYH enzyme normally repairs 8-oxoguanine, the lesion that reactive oxygen leaves in DNA, so without it those errors lock in as the G-to-T mutations that seed the polyps.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — MAP shares some bony features with FAP: osteomas of the jaw and skull and dental anomalies can occur, bony overgrowths of the marrow-bearing facial bones in this milder polyposis cousin.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Pigmented retinal patches occasionally mark MAP: CHRPE, the dark spots on the retina classic for FAP, can appear here too, a clue an ophthalmologist may spot in this related polyposis syndrome.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — MAP looks normal to the Lynch test: its tumors keep their mismatch-repair proteins, so the MLH1/MSH2/MSH6/PMS2 antibody panel stays intact and the cancers are microsatellite-stable — the flaw lies instead in base-excision repair, found only by gene sequencing.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Bleeding polyps drain the red cells: the slow ooze from MAP's colonic adenomas often surfaces first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic blood loss that should trigger colonoscopy.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Oxidative damage is the heart of MAP: with MUTYH unable to repair the 8-oxoguanine lesions that reactive oxygen leaves in DNA, an antioxidant-rich, high-fiber diet whose butyrate nourishes colonocytes is part of the prevention advice alongside surveillance.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong cancer vigilance breeds worry: the recessive inheritance, scores of adenomas and unending colonoscopic surveillance of MAP foster chronic health anxiety alongside low mood.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Prophylactic colectomy is a healing challenge: the colectomy or proctocolectomy that removes the polyp-laden bowel in MAP leaves anastomoses and abdominal wounds at risk of leak and slow closure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Oxaliplatin chemotherapy stings the nerves: when MAP progresses to colorectal cancer treated with FOLFOX, the oxaliplatin causes a cold-triggered, often lasting peripheral neuropathy.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Oxidative damage meets the microbiome: MUTYH repairs the 8-oxoguanine lesions that reactive oxygen leaves in DNA, and the colonic microbiome's genotoxins and ROS add to the mutational load that drives MAP's polyps to cancer.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its tumour spectrum reaches the thyroid: beyond the colon, MAP raises the risk of thyroid and other extracolonic cancers, extending the syndrome into the endocrine system.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can show in the skin: MAP is associated with sebaceous gland tumours and other cutaneous lesions, overlapping the skin findings of the mismatch-repair polyposis syndromes.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It shares FAP's bony lesions: like familial adenomatous polyposis, MAP can cause osteomas of the jaw and skull among its FAP-like extracolonic features.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its DNA-repair defect raises mutation burden: MUTYH-deficient tumours accumulate many mutations from unrepaired oxidative DNA damage, which may make them responsive to checkpoint-inhibitor immunotherapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its cancers travel through the nodes: the colorectal cancers of MAP spread to regional lymph nodes, which determines staging and the need for adjuvant chemotherapy.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin lowers colorectal risk: like in other inherited polyposis, regular aspirin reduces colorectal adenoma and cancer risk in MUTYH-associated polyposis as chemoprevention.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It reaches the urinary tract: MUTYH-associated polyposis raises the risk of bladder and other urothelial cancers among its extracolonic tumours.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Advanced disease spreads to the lungs: the colorectal cancers of MUTYH-associated polyposis metastasise to the lungs and liver if they progress.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for cancers that develop: MUTYH-associated polyposis carries a high colorectal-cancer risk, and established cancers are treated with standard cytotoxic chemotherapy.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — A microbe that compounds the defect: colibactin-producing Escherichia coli damages colonic DNA, synergising with MUTYH's failure to repair oxidative lesions to accelerate adenoma-to-carcinoma progression.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Mostly microsatellite-stable: like FAP, MUTYH-associated colorectal cancers are usually microsatellite-stable and respond poorly to PD-1 checkpoint inhibitors, unlike Lynch tumours.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — MAP breaks the dominant-inheritance pattern of its cousins: it is autosomal recessive, so two carrier parents — often with no polyposis themselves — have a 1-in-4 risk each pregnancy, making partner carrier testing and recurrence counseling central to families.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Aspirin's colorectal protection extends here: blocking platelet COX-1 and the tumor-promoting signals platelets release underpins the chemoprevention studied across hereditary colorectal syndromes, including MUTYH-driven polyposis.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — The repair defect leaves an immune fingerprint: MUTYH loss spawns a heavy load of G-to-T mutations and neoantigens, drawing B cells and plasma cells into the tumor — an immune-rich profile that may make these cancers responsive to checkpoint therapy.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — It breaks a different repair system than Lynch: MAP fails base-excision repair of oxidative damage, whereas Lynch fails mismatch repair through genes like MSH2 — two distinct DNA-maintenance pathways whose loss converges on the same colon, a telling contrast.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — It sits in the polyposis differential: when many colon polyps appear, MAP must be distinguished from hamartomatous syndromes like Cowden (PTEN), since the gene found dictates the cancer risks, the inheritance pattern, and which relatives to test.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — A second hereditary-cancer comparison: unlike BRCA-driven HBOC which fails double-strand-break repair, MAP fails oxidative base repair, yet both are recessive-versus-dominant lessons in how a single broken DNA-maintenance gene seeds a familial cancer syndrome.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — The polyps bleed unseen: chronic occult blood loss from MAP's colonic adenomas or an arising cancer causes iron-deficiency anemia, sometimes the finding that triggers the colonoscopy revealing the polyposis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cancer and its surgery raise the clot risk: a colorectal cancer developing in MAP and the colectomy used to treat heavy polyposis both predispose to perioperative venous thromboembolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Bowel surgery carries infectious risk: the colectomy that high polyp burden eventually requires can be complicated by anastomotic leak and intra-abdominal sepsis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Inflammation feeds the oxidatively-damaged mucosa: IL-6-driven STAT3 signaling adds proliferation and survival to the G:C→T:A mutation burden of MUTYH loss, accelerating the polyps' progression to colorectal cancer.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Wnt activation drives the cell cycle through cyclin D1: the APC/Wnt activation arising in MUTYH-mutated adenomas pushes cyclin D1 expression, speeding the cell-cycle entry behind polyp growth.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Bleeding polyps and inflammation drain the blood: beyond the iron loss of chronically bleeding adenomas, the inflammation of MAP suppresses erythropoiesis, adding an anemia of chronic disease to the iron deficiency.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Colectomy and chemo strain the kidney: the surgery for MAP's polyp burden and any platinum chemotherapy for its colorectal cancers, plus dehydration from altered bowel anatomy, can threaten chronic kidney disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the colon costs the bones: colectomy and the malabsorption of calcium and vitamin D that follows, plus chronic GI losses, can leave reduced bone density in MUTYH-associated polyposis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Inherited cancer risk and surveillance weigh on the mind: living with a recessive polyposis syndrome, repeated colonoscopies and the prospect of colectomy carries a substantial psychological burden.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — A disease of unrepaired oxidative damage: MUTYH-associated polyposis comes from failure to excise the 8-oxoguanine lesions oxidative stress creates—the damage the NRF2 (NFE2L2) programme limits—so its mutations are the fingerprint of reactive oxygen on DNA.
- `connects-to` → **[AML](../aml/README.md)** — Oxidative transversions can reach the marrow: biallelic MUTYH loss raises the risk not only of colorectal cancer but of myeloid neoplasms including acute myeloid leukaemia, which can carry the same G:C→T:A signature of unrepaired oxidative damage.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — It shares the polyposis APC/Wnt risk: MUTYH-associated polyposis drives somatic G:C→T:A hits in APC that activate Wnt, and like FAP it can spawn desmoid tumours—Wnt/β-catenin fibromatoses that complicate abdominal surgery.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — Recessive DNA-repair cancer syndromes: like Bloom syndrome, MUTYH-associated polyposis is autosomal-recessive—biallelic loss of a DNA-repair gene (base-excision repair vs RecQ helicase) driving cancer through accumulated mutations.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — A hypermutated, immunogenic tumour: MUTYH-deficient cancers accumulate a distinctive G:C→T:A mutational signature and high neoantigen load, drawing tertiary lymphoid structures and responding to checkpoint blockade.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — FAP-like bony lesions: MUTYH-associated polyposis can show attenuated FAP features including osteomas and dental anomalies in the cortical bone, reflecting its overlap with APC-driven polyposis.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — The genomic-instability family: like Bloom and Werner syndromes, MUTYH-associated polyposis is an autosomal-recessive disorder of genome maintenance—here failed base-excision repair of oxidative DNA damage—predisposing to cancer through accumulated mutations.
- `connects-to` → **[MDS](../mds/README.md)** — Beyond the colon: biallelic MUTYH carriers have a raised risk of myeloid neoplasia, with the unrepaired oxidative mutations driving myelodysplasia and acute myeloid leukaemia as well as gut tumours.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — Different repair, same vulnerability: MUTYH performs base-excision repair of oxidative DNA damage while BRCA2 mediates homologous recombination of double-strand breaks—loss of either is an inherited route to cancer through unrepaired DNA.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Wnt-driven oncogene: the G:C→T:A transversions of MUTYH deficiency activate Wnt signalling and MYC, driving the adenoma-to-carcinoma progression of its colorectal polyps.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — KRAS and anti-EGFR resistance: MUTYH-associated tumours characteristically carry KRAS G12C transversions, which activate EGFR-MAPK signalling and confer resistance to anti-EGFR antibodies.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintaining telomeres accompanies the malignant progression of MUTYH-associated polyps toward invasive cancer.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT cooperation: AKT signalling cooperates with the KRAS and Wnt activation of MUTYH-associated polyps to drive their growth toward colorectal cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels MUTYH-associated adenoma cells through the G1 checkpoint as they progress along the polyp-to-carcinoma sequence.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Polyp hypoxia: as MUTYH-associated adenomas grow, HIF-1α stabilised in their hypoxic cores drives the VEGF angiogenesis supporting progression toward carcinoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β escape: loss of SMAD4-mediated TGF-β growth suppression is a step in the adenoma-carcinoma progression of MUTYH-associated polyps, beyond the initiating base-excision-repair defect.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — Serrated pathway: the G:C→T:A transversions caused by MUTYH loss can hit BRAF, contributing to the serrated route of colorectal carcinogenesis alongside the classic KRAS-driven adenoma sequence.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Tumour macrophages: CCL2 recruits macrophages into the stroma of MUTYH-associated colorectal tumours, part of the inflammatory microenvironment that accompanies their progression.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — The APC mutations that MUTYH deficiency generates through its signature G:C→T:A transversions disable the GSK-3β destruction complex, unleashing the Wnt signaling that drives the adenomas of MUTYH-associated polyposis.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signaling cooperates with the unleashed Wnt pathway in the intestinal crypt to expand the stem-cell compartment, contributing to the polyp formation that defines MUTYH-associated polyposis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — MUTYH-associated adenomas evade caspase-3-mediated apoptosis, the cell-death pathway that NSAID and COX-2-inhibitor chemoprevention works to restore in the colorectal polyposis syndromes.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — MUTYH repairs the oxidative DNA lesion 8-oxoguanine, so the reactive oxygen species generated by sources such as xanthine oxidase are the very damage whose accumulation, in biallelic MUTYH loss, drives the G:C→T:A transversions behind the polyposis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-derived prostaglandins promote adenoma growth, and NSAIDs and COX-2 inhibitors that block them are used for chemoprevention of polyposis, reducing polyp burden in the hereditary colorectal-cancer syndromes including MAP.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MUTYH-associated polyposis (recessive base-excision-repair defect) must be distinguished from Lynch syndrome (mismatch-repair genes such as MLH1) and FAP, each a distinct molecular route to hereditary colorectal cancer.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The G:C→T:A transversions of MUTYH deficiency preferentially hit KRAS (mapped), activating MAPK-ERK to drive adenoma progression in MUTYH-associated polyposis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA activation of the PI3K-AKT axis (AKT already mapped) is a cooperating event in the malignant progression of MUTYH-associated colorectal adenomas.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (CDK4/6, cyclin-D1 and CDKN2A already mapped) releases E2F1 to drive proliferation in the carcinomas arising from MUTYH-associated polyposis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss releases PI3K-AKT signaling (AKT and PIK3CA already mapped) that cooperates with the KRAS-driven Wnt activation in the colorectal tumorigenesis of MUTYH-associated polyposis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides an inflammatory cofactor in the adenoma-to-carcinoma progression of MUTYH-associated polyposis.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains the inflammatory, tumor-promoting microenvironment of MUTYH-associated colorectal neoplasia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is upregulated in the colorectal adenoma-to-carcinoma progression of MUTYH-associated polyposis, modulating adhesion and immune evasion.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), a tumor-promoting inflammatory input in MUTYH-associated polyposis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The genomic instability of MUTYH-deficient base-excision repair generates cytosolic DNA sensed by cGAS-STING, shaping the immune microenvironment of MAP tumors.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The mutational burden of MUTYH-deficient tumors drives IFN-STAT1 signaling, shaping their antitumor immune response and immunotherapy potential.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors govern the oxidative-stress defenses whose failure, with the loss of MUTYH base-excision repair of oxidized guanine, drives the mutagenesis of MUTYH-associated polyposis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the neoantigen-rich tumors of MUTYH-associated polyposis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the adenoma-carcinoma progression of MUTYH-associated polyposis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory colonic microenvironment that promotes tumor progression in MUTYH-associated polyposis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression contributes to the epigenetic dysregulation of the colorectal tumors of MUTYH-associated polyposis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the progression of the adenomas of MUTYH-associated polyposis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the adenoma-carcinoma sequence in MUTYH-associated polyposis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the oxidatively stressed, base-excision-repair-deficient epithelial cells of MUTYH-associated polyposis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of MUTYH-associated polyposis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the tumors of MUTYH-associated polyposis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of MUTYH-associated polyposis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the adenomas and carcinomas of MUTYH-associated polyposis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the polyp and tumor microenvironment of MUTYH-associated polyposis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of MUTYH-associated polyposis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of MUTYH-associated polyposis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of MUTYH-associated polyposis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the intestinal inflammation and tumor microenvironment of MUTYH-associated polyposis.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding anaemia: the adenomatous polyps of MUTYH-associated polyposis bleed into the gut, and the resulting chronic occult blood loss causes the iron-deficiency anaemia (iron already mapped) that lowers haemoglobin and can prompt investigation.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunogenic mutations: the defective repair of oxidative DNA damage in MUTYH-associated polyposis raises the tumour mutational burden, generating MHC-presented neoantigens that make some of its cancers responsive to immune surveillance and immunotherapy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint therapy: the elevated mutational burden of MUTYH-deficient colorectal cancers can render them responsive to PD-1 checkpoint blockade, an immune approach for the advanced tumours of this polyposis syndrome.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the immune response to the neoantigen-rich, high-mutational-burden cancers of MUTYH-associated polyposis, the basis of their potential checkpoint sensitivity.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: IL-10 in the tumour microenvironment dampens the anti-tumour response to the neoantigens generated by the defective oxidative-damage repair (PD-1 already mapped), one brake on the immunity that checkpoint blockade releases.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 help: helper T cells provide the CD4 help (MHC class II already mapped) that supports the cytotoxic response to the neoantigen-rich MUTYH-deficient tumours, part of the antitumour immunity relevant to their checkpoint therapy.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote colonic proliferation and the adenoma-carcinoma sequence, a modifiable dietary influence on the polyp burden of MUTYH-associated polyposis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the polyp and tumour stroma of MUTYH-associated polyposis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and proliferation: the adipokine leptin links obesity to colorectal carcinogenesis, promoting the epithelial proliferation (Wnt already mapped) that can accelerate the adenoma-carcinoma sequence in MUTYH-associated polyposis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the polyps of MUTYH-associated polyposis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the colorectal carcinogenesis, part of the modifiable adipokine influence on the cancer risk of MUTYH-associated polyposis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary chemoprevention: dietary calcium reduces colorectal adenoma recurrence, binding the bile acids (cholesterol already mapped) that promote carcinogenesis, a modifiable factor in the risk reduction of MUTYH-associated polyposis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related modifiable colorectal-cancer risk of MUTYH-associated polyposis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron-regulatory anaemia: hepcidin drives the iron sequestration that, with the chronic occult bleeding of the numerous adenomas (iron and haemoglobin already mapped), produces the anaemia of MUTYH-associated polyposis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — DNA-damage innate signalling: type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the DNA damage of the base-excision-repair-defective (MUTYH already mapped) cells, is part of the innate-immune response of MUTYH-associated polyposis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the colorectal-cancer risk of MUTYH-associated polyposis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immune infiltrate along the adenoma-carcinoma sequence of MUTYH-associated polyposis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the immune infiltrate of the adenomas of MUTYH-associated polyposis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory infiltrate along the adenoma-carcinoma sequence of MUTYH-associated polyposis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed adenoma stroma of MUTYH-associated polyposis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Adenoma stroma: the fibroblasts and the desmoplastic stroma support the accumulating adenomas along the adenoma-carcinoma sequence of MUTYH-associated polyposis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Adenoma stroma mast cells: the mast cells infiltrate the adenoma stroma and contribute to the angiogenesis and the type-2 (IgE already mapped) microenvironment of the polyps of MUTYH-associated polyposis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Chemoprevention vitamin: the vitamin D status modulates the colorectal-cancer (already mapped) risk along the adenoma-carcinoma sequence of MUTYH-associated polyposis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor countering the oxidative DNA damage (the 8-oxoguanine that MUTYH repairs), is part of the antioxidant chemoprevention dimension of MUTYH-associated polyposis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the MUTYH-associated polyps.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed stroma of the MUTYH-associated polyps.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the complement dimension of the inflamed adenoma stroma of MUTYH-associated polyposis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Colorectal mucosal alarmin: TSLP from the MAP intestinal epithelium (already mapped) activates dendritic cells and mast cells, driving the inflammatory stroma of MUTYH-deficient polyposis and the adenoma-carcinoma progression to colorectal cancer (already mapped).
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Bleeding anaemia: erythropoietin supports erythropoiesis in the iron-deficiency anaemia from the chronic occult blood loss of the multiple adenomas of MAP; EPO is used adjunctively in MAP patients undergoing repeated colonoscopy and polypectomy for polyp surveillance.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Colonic inflammation: bradykinin activates B2 receptors in the MAP colorectal mucosa (intestinal-epithelium already mapped), amplifying the prostaglandin (already mapped) and NF-kB (already mapped) inflammation of the MUTYH-deficient polyposis stroma and colonic pain.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Colonic complement regulation: C1-INH controls the classical and alternative complement pathways (complement C5 already mapped) in the MUTYH-associated polyposis tumour microenvironment, modulating complement-dependent cytotoxicity against MAP colorectal adenoma cells.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine in polyposis: histamine from the mast cells infiltrating the MAP colorectal polyp stroma promotes VEGF (already mapped) angiogenesis and prostaglandin (already mapped) inflammation of the MUTYH-deficient adenoma mucosa.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Polyposis stroma periostin: periostin secreted by MAP cancer-associated fibroblasts and downstream of TGF-β (already mapped) activates the integrin-AKT (already mapped) pathway, promoting the MUTYH-deficient colorectal adenoma-to-carcinoma invasive progression.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sieber-2003-mutyh-map]: Sieber OM, Lipton L, Crabtree M, et al. Multiple colorectal adenomas, classic adenomatous polyposis, and germ-line mutations in MYH. *N Engl J Med.* 2003;348(9):791-799. [doi:10.1056/NEJMoa025283](https://doi.org/10.1056/NEJMoa025283) · [PubMed 12606733](https://pubmed.ncbi.nlm.nih.gov/12606733/)
[^al-tassan-2002-mutyh]: Al-Tassan N, Chmiel NH, Maynard J, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. *Nat Genet.* 2002;30(2):227-232. [doi:10.1038/ng828](https://doi.org/10.1038/ng828) · [PubMed 11818965](https://pubmed.ncbi.nlm.nih.gov/11818965/)
