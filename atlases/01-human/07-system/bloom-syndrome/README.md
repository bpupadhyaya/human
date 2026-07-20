---
schema: human-scale-entry/v1
id: bloom-syndrome
name: Bloom Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Bloom syndrome is caused by biallelic BLM mutations; small body size, sun-sensitive telangiectatic facial erythema, immunodeficiency; elevated sister chromatid exchanges (~10x); pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin cancers); median survival ~30 years."
aliases: ["Bloom syndrome", "Bloom's syndrome", "BLM syndrome", "Bloom syndrome cancer", "Bloom syndrome SCE", "RECQL3 syndrome", "Bloom syndrome ALL", "Bloom syndrome chromosomal instability", "Bloom syndrome hereditary"]
sources:
  - id: ellis-1995-blm-cloning
    type: peer-reviewed
    cite: "Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. Cell. 1995;83(4):655-666."
    doi: "10.1016/0092-8674(95)90105-1"
    pmid: "7585968"
    url: "https://doi.org/10.1016/0092-8674(95)90105-1"
  - id: german-1997-bloom-cancer
    type: peer-reviewed
    cite: "German J. Bloom's syndrome. XX. The first 100 cancers. Cancer. 1997;71(12):4016-4023."
    doi: "10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
    pmid: "9216035"
    url: "https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E"
cross_links:
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Burkitt lymphoma and NHL are among the most common lymphoid malignancies in Bloom syndrome; crossover-mediated LOH at 8q24 (MYC) contributes; BS patients have ~50-100× elevated lymphoma risk; chemotherapy hypersensitivity in BS requires dose reduction in treatment."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC heterozygosity is vulnerable to crossover-mediated LOH in BLM-deficient cells → biallelic APC LOF without a second mutation → colorectal adenoma; GI carcinomas dominate the adult BS cancer spectrum; colonoscopy surveillance from age 15 is a management cornerstone."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "BLM interacts with MLH1 (MMR) via its N-terminal region; BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Bloom and DICER1 are both childhood cancer-predisposition syndromes but mechanistically unrelated: Bloom is genomic instability from a defective BLM helicase (high sister-chromatid exchange), DICER1 faulty microRNA processing — broken DNA repair versus gene dysregulation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The diagnostic hallmark of Bloom syndrome is a sun-sensitive facial rash: telangiectatic erythema in a butterfly distribution across the cheeks and nose that flares with UV exposure, reflecting cells that cannot properly repair replication-associated DNA damage."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Leukemia, especially acute lymphoblastic and myeloid, is the earliest and most common cancer in Bloom syndrome, often in childhood; the BLM-deficient genomic instability also makes these patients hypersensitive to chemotherapy, forcing substantial dose reductions."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Bloom and Werner syndrome are both RecQ-helicase disorders of genomic instability: Bloom (BLM) causes sister-chromatid exchange, sun-sensitive rash, short stature and early cancers, while Werner (WRN) causes premature aging and sarcomas—RecQ members whose loss destabilizes DNA."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Leukemia is a leading Bloom-syndrome cancer: the BLM helicase defect causes extreme chromosomal instability and sister-chromatid exchange, so AML and ALL arise at strikingly young ages, and—because Bloom cells are hypersensitive to DNA-damaging agents—chemo doses must be reduced."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Bloom syndrome is markedly photosensitive: BLM helicase loss leaves cells unable to resolve replication stress, so ultraviolet photons readily cause the characteristic sun-exposed facial erythema (butterfly rash) and add to the cancer risk—patients need strict sun protection."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Bloom syndrome and Rothmund-Thomson are RecQ-helicase genome-instability disorders: Bloom (BLM), Rothmund-Thomson (RECQL4), and Werner (WRN) share defective DNA helicases causing chromosomal instability, growth failure, and high cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Bloom syndrome carries a strikingly high rate of early type 2 diabetes: despite low body weight, severe insulin resistance develops, so diabetes appears in childhood—part of a broad phenotype of growth deficiency, immunodeficiency, and cancer from BLM helicase loss."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Bloom syndrome includes an immunodeficiency: BLM helicase loss impairs lymphocyte development and antibody class-switching, causing low immunoglobulins and recurrent respiratory and ear infections—so immune failure compounds the genome instability driving its cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Bloom and Li-Fraumeni are both inherited genome-instability cancer syndromes by different routes: Bloom from BLM helicase loss causing excess recombination, Li-Fraumeni from p53 loss removing the damage checkpoint—both flood cells with mutations driving cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Bloom syndrome cells struggle to engage p53-driven safeguards: without BLM helicase, stalled forks and excess sister-chromatid exchange overwhelm the damage response, so the p53 checkpoint cannot keep pace—explaining the broad, early cancer risk of the syndrome."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BLM helicase partners with RAD51 in homologous recombination: BLM normally dissolves recombination intermediates that RAD51 forms, preventing crossovers, so its loss causes the hallmark surge in sister-chromatid exchange that defines Bloom syndrome diagnostically."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "Bloom syndrome and BRCA2 cancers share a homologous-recombination theme: BLM helicase works alongside BRCA2 and RAD51 to repair DNA by recombination, so its loss—like BRCA2 loss—causes genomic instability and a broad lifelong cancer predisposition."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Bloom syndrome includes immunodeficiency: defective DNA repair impairs B-cell antibody class-switching, lowering immunoglobulins and causing recurrent infections, while the same instability fuels the lymphomas and leukemias that often arise from these cells."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Bloom syndrome impairs the reproductive system: men are typically infertile and women have reduced, early-ending fertility, reflecting how the genome instability and repair defect that drive its cancers also disrupt the meiotic recombination needed to make gametes."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Bloom syndrome's most visible feature is profound short stature: BLM helicase loss stunts growth from before birth, producing proportionate dwarfism despite normal growth-hormone levels—so it is a growth disorder of the cell's replication machinery, not the hormone."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Bloom syndrome brings recurrent lung infection: an associated immunodeficiency (low immunoglobulins) leaves patients prone to pneumonia and chronic lung disease, so respiratory infections are a major cause of illness alongside the cancer risk."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Bloom syndrome carries an extreme, broad cancer risk including breast: genomic instability from BLM loss drives tumors at unusually young ages across many sites, so carriers need early, intensive surveillance for breast and other cancers."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Bloom syndrome compounds a fragile genome's stress response: BLM helicase untangles stalled replication forks that ATM and ATR guard, so losing BLM forces these damage-sensing kinases to work overtime—and the resulting instability fuels the syndrome's many cancers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Bloom syndrome includes immune deficiency: many patients have low IgG and other antibodies, causing recurrent ear, sinus, and lung infections—an immunodeficiency layered on top of the cancer risk from defective DNA repair."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Bloom syndrome impairs T-cell help: defective DNA repair hampers the lymphocyte proliferation behind antibody class-switching, so weak T-helper support contributes to the low immunoglobulins and recurrent infections these patients suffer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxidative damage compounds Bloom syndrome's repair defect: with the BLM helicase gone, cells handle DNA breaks poorly, so reactive oxygen species and sunlight add lesions the cell cannot fix—fueling the genomic instability and cancer risk."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Bloom syndrome carries a steep colorectal cancer risk: the failed DNA repair lets mutations accumulate in the gut lining, so these patients develop bowel cancers young and need early, frequent colonoscopy among their many tumor risks."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Bloom syndrome is diagnosed in the fibroblast: cultured cells reveal sharply elevated sister-chromatid exchange, the cytogenetic fingerprint of BLM helicase loss that distinguishes it from other DNA-repair disorders."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bloom syndrome makes the marrow turn leukemic: its runaway genomic instability seeds mutations in blood-forming cells, so leukemias and lymphomas arise from the bone marrow at strikingly young ages."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Bloom syndrome burdens the pancreas: patients commonly develop diabetes as the gland's insulin output falters, and their broad cancer predisposition includes pancreatic tumors among many sites."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Bloom syndrome dims immune surveillance: a mild immunodeficiency weakens natural killer and antibody responses, leaving patients prone to infections and less able to cull the cancerous cells their unstable DNA spawns."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Bloom syndrome's butterfly facial rash is vascular: sun exposure dilates dermal endothelial-lined vessels into the telangiectatic erythema across the cheeks that marks the disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Bloom syndrome's commonest cancers strike the gut lining: the unstable DNA of the intestinal epithelium spawns early colorectal and other GI cancers, demanding cancer surveillance from a young age."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Bloom syndrome's universal cancer risk includes the liver: its profound genomic instability predisposes to tumors across the body, hepatocellular carcinoma among the many sites."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Bloom syndrome cannot mend its own DNA: the broken BLM helicase lets chromosomes swap arms in a flurry of sister-chromatid exchanges — the diagnostic hallmark — and leaves cells hypersensitive to radiation and oxidative damage."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sunlight inflames the Bloom syndrome face and eyes: the photosensitive butterfly rash of dilated telangiectatic vessels spreads across the cheeks and onto the conjunctiva, a visible sign of the disorder's UV sensitivity."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bloom syndrome's cancer spectrum reaches the kidney: among the many tumors its genomic instability invites, Wilms tumor and renal carcinoma occur, so the kidney joins the broad lifelong cancer surveillance."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Bloom syndrome leaves the body short of antibody: a common variable immunodeficiency-like drop in immunoglobulins accompanies it, so recurrent ear, sinus, and lung infections trouble these patients from childhood."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The diagnosis is read in the blood cells: Bloom's faulty BLM helicase produces a striking excess of sister-chromatid exchanges in cultured lymphocytes — the classic confirmatory test — while marrow failure can also drop the red cells into anemia."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut troubles span a lifetime: severe reflux and feeding difficulty stunt growth in Bloom infants, and the genomic instability later raises the risk of gastric and other gastrointestinal cancers."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Bloom syndrome comes with immune deficiency: poor antibody responses and reduced thymus-derived T-cell function leave children prone to recurrent ear, sinus and lung infections, part of why infections rival cancer as a cause of early death."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Bloom bodies resist insulin: many patients develop insulin resistance and early type 2 diabetes despite their small, lean frames, a metabolic derangement tied to the syndrome that adds to its lifelong health burden."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Bloom's failing immunity meets its cancer risk: weakened cytotoxic T-cell surveillance lets genomically unstable, mutation-riddled cells slip past immune killing, compounding the extraordinary lifetime cancer predisposition that defines the syndrome."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The growth axis runs low in Bloom: despite normal growth hormone, low IGF-1 signaling underlies the profound pre- and postnatal growth deficiency that gives these patients their characteristic small, lean stature."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The unstable genome breaks first in the marrow: Bloom syndrome's chromosomal instability drives myelodysplastic syndromes and leukemia at strikingly young ages, among the earliest of its many cancers."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody output runs short: Bloom's immunodeficiency includes poor plasma-cell function and low immunoglobulin levels, leaving patients prone to the recurrent respiratory and ear infections of childhood."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Adult Bloom patients face carcinomas of the gut lining: the genomic instability that brings early leukemia later drives GI carcinomas including esophageal cancer, part of the syndrome's relentless lifelong cancer toll."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "The embryonal tumors appear in childhood: Bloom syndrome's chromosomal instability predisposes to Wilms tumor among other paediatric cancers, reflecting how broadly the loss of BLM helicase destabilizes the genome."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "BLM works alongside mismatch repair: the BLM helicase cooperates with the MSH2-containing mismatch-repair machinery to resolve recombination intermediates, so its loss compounds the genomic instability that mismatch-repair defects also cause."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Relentless DNA damage smolders into inflammation: the unrepaired breaks and replication stress of Bloom syndrome trigger DNA-sensing inflammatory signaling that activates NF-κB, a chronic inflammatory tone layered on its cancer risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A faltering immune system invites infection: Bloom syndrome includes an immunodeficiency with low immunoglobulins, so recurrent respiratory and gastrointestinal infections — and the sepsis they can become — are a major cause of illness."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Its cancer net is wide and starts early: Bloom syndrome's genomic instability and immunodeficiency raise the risk of carcinomas including HPV-driven cervical cancer, part of a remarkably broad, young-onset cancer spectrum."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Recurrent lung infection scars the airways: the immunodeficiency of Bloom syndrome causes repeated respiratory infections that can lead to bronchiectasis and chronic obstructive lung disease over time."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Infection, cancer and marrow strain lower the count: chronic infections, the disease's many malignancies and bone-marrow involvement combine to produce an anemia of chronic disease in Bloom syndrome."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A lifetime of cancer and illness weighs on the mind: living with profound cancer predisposition, recurrent infection, short stature and lifelong surveillance carries a substantial psychological burden in Bloom syndrome."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Its immunodeficiency invites recurrent infection: Bloom syndrome includes an antibody deficiency that leaves patients prone to recurrent respiratory and ear infections, often pneumococcal."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Immune defects and cancer therapy open the lung to mold: the immunodeficiency of Bloom syndrome, compounded by chemotherapy for its frequent cancers, can permit invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its DNA-repair defect makes tissue fragile to treatment: Bloom cells are hypersensitive to chemotherapy and radiation, so the doses used against its cancers cause severe tissue damage and poor healing."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Sunlight inflames its skin: Bloom syndrome causes a photosensitive telangiectatic butterfly erythema across the face, along with café-au-lait macules and a raised risk of skin cancer."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It stunts growth and disturbs metabolism: Bloom syndrome features severe proportionate short stature, and patients develop diabetes and hypogonadism with subfertility, tying it to the endocrine system."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Profound cancer risk breeds worry: the chromosomal instability and very high lifetime malignancy risk of Bloom syndrome demand lifelong surveillance that fosters chronic health anxiety."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It stunts the whole skeleton: profound proportionate pre- and postnatal growth deficiency leaves a small, slender frame, one of the defining clinical features of Bloom syndrome."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Antibody deficiency lets the lungs get infected: the immunodeficiency of Bloom syndrome causes recurrent respiratory and ear infections that can progress to bronchiectasis."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It troubles the gut early and late: feeding difficulties and gastro-oesophageal reflux are common in infancy, while a high lifetime risk of gastrointestinal cancers emerges in adulthood."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Genomic instability cripples immunity and lymphoid tissue: Bloom syndrome causes immunodeficiency with low immunoglobulins and recurrent infections, alongside a very high risk of leukaemia and lymphoma."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It predisposes to childhood kidney cancer: Wilms tumour is among the many malignancies the genomic instability of Bloom syndrome can cause, demanding cancer surveillance from childhood."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Metabolic disease reaches the heart: Bloom syndrome carries a high rate of type 2 diabetes and dyslipidaemia, bringing premature cardiovascular risk despite the patients' characteristic small stature."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Treatment must be gentler: the DNA-repair defect of Bloom syndrome makes patients hypersensitive to DNA-damaging chemotherapy and radiation, forcing dose reduction when their many cancers are treated."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Sun sensitivity breeds skin cancer: the photosensitive facial rash of Bloom syndrome reflects defective DNA repair that also drives basal and squamous cell skin cancers at a young age."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Instability seeds gut tumours: chromosomal instability in Bloom syndrome predisposes to gastrointestinal adenocarcinomas, including gastric and colorectal cancer, often decades earlier than usual."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A synthetic-lethal vulnerability: BLM helicase loss leaves Bloom cells reliant on other DNA-repair routes, making homologous-recombination and replication-stress pathways (PARP, ATR) candidate targets — and BLM itself an anticancer drug target in unstable tumours."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Genomic chaos may aid immunotherapy: the extreme chromosomal instability of Bloom syndrome can generate the high mutational burden and neoantigens that make some of its cancers candidates for checkpoint blockade."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Immunodeficiency rides along: Bloom syndrome impairs B-cell maturation and class switching in germinal centres, causing low immunoglobulins and recurrent sinopulmonary infections alongside its cancer risk."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Genome instability fails the marrow: like other DNA-repair-defective syndromes, Bloom syndrome can progress to bone-marrow failure and cytopenias on the path to myelodysplasia and leukaemia."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Short stature and skeletal anomalies: proportionate dwarfism is a defining feature of Bloom syndrome, with thin cortical bone and skeletal anomalies reflecting profoundly impaired growth."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cancer at every site: Bloom syndrome's extreme genomic instability predisposes to the full spectrum of malignancy at young ages, including pancreatic and other gastrointestinal adenocarcinomas."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Lymphoma in a broad spectrum: Bloom syndrome's genomic instability raises the risk of aggressive lymphomas like diffuse large B-cell lymphoma, often at unusually young ages."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Sarcomas of genomic instability: like its sister helicaseopathies Werner and Rothmund-Thomson, Bloom syndrome raises the risk of osteosarcoma and other sarcomas alongside its carcinomas."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver tumours too: the all-cancer predisposition of Bloom syndrome extends to the liver, with hepatocellular and other tumours arising in the hepatic lobules at young ages."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "DNA-repair predisposition: like Lynch syndrome, Bloom syndrome is a hereditary DNA-repair defect that drives early colorectal and other cancers—genome instability from BLM loss rather than mismatch-repair failure."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "Genome-stability partner: ATRX maintains chromatin and telomere stability and suppresses alternative lengthening of telomeres; its loss, like BLM loss, generates the replication stress and genomic instability that fuel cancer."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Sun-sensitive skin cancer: the photosensitivity and chromosomal instability of Bloom syndrome raise the risk of skin cancers including melanoma, alongside the basal cell carcinomas already typical of the disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplification-prone oncogene: the genomic instability of Bloom syndrome favours oncogene amplifications such as MYC, helping drive the broad spectrum of cancers that develop at young ages."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere maintenance: BLM helicase normally helps resolve telomeric replication, and its loss stresses telomere maintenance, where TERT reactivation is one route the resulting tumours take to immortality."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: the chromosomal instability of Bloom syndrome readily amplifies cyclin D1 and other cell-cycle drivers, pushing damaged cells through the G1 checkpoint into proliferation."
  - target: 01-human/03-molecular/recql4
    relation: connects-to
    note: "RecQ-helicase family: BLM is one of five human RecQ helicases, and its loss in Bloom syndrome parallels the genomic instability and cancer predisposition of RECQL4 (Rothmund-Thomson) and WRN (Werner) disease."
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Homologous recombination: BLM cooperates with the BRCA-PALB2 homologous-recombination machinery to resolve recombination intermediates, so its loss raises sister-chromatid exchange and cancer risk."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Tumour-suppressor loss: the rampant chromosomal instability of Bloom syndrome readily inactivates tumour suppressors like CDKN2A, contributing to the exceptionally broad early-onset cancer spectrum."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Checkpoint engagement: the persistent DNA damage and unresolved recombination intermediates of BLM-deficient cells chronically activate the p53-p21 (CDKN1A) checkpoint, arresting cells and contributing to the growth deficiency of Bloom syndrome."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic elimination: cells in Bloom syndrome that accumulate irreparable DNA damage undergo caspase-3-mediated apoptosis, a cell-loss mechanism that compounds the impaired growth alongside the cancer-prone surviving clones."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 setpoint: the MDM2-p53 axis governs the heightened p53 response that BLM-deficient cells mount against their constant DNA damage, balancing tumour suppression against the cell loss that limits growth in Bloom syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Genomic-instability inflammaging: BLM-deficient cells accumulate micronuclei and cytosolic DNA from their excess chromosomal breakage, activating cGAS-STING and a chronic type-I-interferon inflammation that accompanies the genomic instability of Bloom syndrome."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative DNA damage: xanthine-oxidase-derived reactive oxygen species add oxidative lesions to the already unstable BLM-deficient genome, compounding the DNA damage that drives the cancer predisposition and sun-sensitive skin of Bloom syndrome."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Immunodeficiency: Bloom syndrome features low immunoglobulins, including secretory IgA, and the resulting impaired mucosal immunity underlies the recurrent respiratory and gastrointestinal infections that complicate the disorder."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Repair-gene transcription: E2F1 transactivates homologous-recombination genes including RAD51 and BRCA1 (already mapped), so the RB-E2F axis intersects the very repair machinery BLM helicase loss compromises in Bloom syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Proliferative drive: cyclin-D-CDK4/6 (cyclin-D1 already mapped) propels cell-cycle entry, and the genomic instability of BLM-deficient cells accelerates the mutational hits that deregulate this axis in Bloom-associated cancers."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint restraint: RB1 holds back E2F-driven S-phase entry until repair is complete, and the relentless replication stress of Bloom syndrome makes this restraint critical to limiting propagation of damaged genomes."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative genomic stress: NRF2 antioxidant defence limits the reactive-oxygen-species-driven DNA damage that compounds the genomic instability of BLM-helicase deficiency in Bloom syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Growth and survival: PI3K-AKT signalling downstream of growth hormone, IGF-1 and insulin (all already mapped) governs the growth programmes constrained in the growth failure of Bloom syndrome yet co-opted by its cancers."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Cancer angiogenesis: VEGF-driven angiogenesis supports the diverse early-onset malignancies to which the genomic instability of Bloom syndrome predisposes."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "GH/IGF-1/insulin signalling through PI3K-AKT-mTOR (GH, IGF-1, insulin and AKT mapped) governs the growth axis, dysregulated in the growth deficiency of Bloom syndrome."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT signalling (AKT mapped) is a tumour-suppressor counterweight to the proliferative drive in the cancer-prone cells of Bloom syndrome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS-ERK-MAPK proliferative signalling cooperates with the genomic instability of BLM-helicase loss in driving the cancer predisposition of Bloom syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Genomic instability from BLM-helicase loss generates cytosolic DNA that engages cGAS-STING (mapped) and IFN-STAT1 signalling, contributing to the inflammatory phenotype of Bloom syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the chronic oxidative and replicative stress of the genomically unstable cells of Bloom syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the immune-cell activation relevant to the immunodeficiency and cancer surveillance of Bloom syndrome."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signaling shapes the inflammatory tumor-promoting microenvironment relevant to the cancer predisposition of Bloom syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the genomically unstable, malignancy-prone cells of Bloom syndrome depend on."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the DNA-damage response and Wnt/β-catenin signaling relevant to the genomic instability and cancer predisposition of Bloom syndrome."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the genomically unstable cells of Bloom syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory context of the tumor microenvironment in the cancer-prone Bloom syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and oxidative-stress adaptation participates in the cellular stress of the genomically unstable cells of Bloom syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic and growth homeostasis relevant to Bloom syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the cellular stress responses to the genomic instability of Bloom syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation accompanying the genomic instability of Bloom syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the malignancies of Bloom syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal and marrow interactions relevant to Bloom syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape accompanying the genomic instability of Bloom syndrome."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 anti-apoptotic signaling participates in the survival of the genomically unstable cells and the lymphoid-neoplasia predisposition of Bloom syndrome."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 transcription-factor activity participates in the hematopoietic differentiation and leukemia predisposition of Bloom syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory and tumor-microenvironment processes of Bloom syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunodeficiency: Bloom syndrome features immunodeficiency with reduced immunoglobulins (already mapped), and impaired MHC class II-restricted antigen presentation contributes to the recurrent infections that complicate the disorder."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Metabolic risk: Bloom syndrome carries a strikingly high risk of early type 2 diabetes with insulin resistance, so impaired insulin-receptor signalling is a common endocrine complication alongside the short stature already mapped."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: reduced IL-2-driven T-cell responses form part of the cellular immunodeficiency of Bloom syndrome, compounding the antibody deficiency and predisposing to the infections that accompany its genome instability."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Genome-instability interferon: unrepaired DNA and micronuclei in Bloom syndrome cells release cytosolic DNA that, through cGAS-STING (already mapped), triggers a type I interferon response, part of the chronic inflammatory signature of genome-instability disorders."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory dysregulation: the immune dysfunction of Bloom syndrome includes dysregulated pro-inflammatory cytokines such as TNF, contributing to the inflammatory milieu that accompanies its immunodeficiency and cancer predisposition."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Humoral immune defect: the immunodeficiency of Bloom syndrome extends beyond low immunoglobulins (already mapped) to impaired complement-supported humoral defence, part of the broad immune vulnerability to infection."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory dysregulation: the immune dysfunction of Bloom syndrome includes dysregulated pro-inflammatory cytokines such as IL-1 (TNF and IL-6 already mapped), contributing to the inflammatory milieu of its immunodeficiency and cancer predisposition."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunoregulatory balance: the anti-inflammatory IL-10 counters the dysregulated pro-inflammatory cytokines (TNF and IL-6 already mapped) of Bloom syndrome, and the imbalance is part of the broad immune dysfunction of the disorder."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Immunodeficiency: the spleen and the wider immune system are compromised in Bloom syndrome (immunoglobulin G already mapped), contributing to the recurrent infections that accompany its genome-instability and cancer predisposition."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Humoral immune dysregulation: IL-4 and the type-2 response support the B-cell (already mapped) antibody production (immunoglobulin G already mapped) impaired in Bloom syndrome, part of the humoral immunodeficiency that predisposes to recurrent infections."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Cancer-therapy anaemia: the frequent and diverse cancers of Bloom syndrome and their chemotherapy cause anaemia needing transfusion, whose repeated support can load the body with iron in these cancer-prone patients."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Growth failure and low weight: the profound growth retardation and low body weight of Bloom syndrome (growth hormone and IGF-1 already mapped) are reflected in the low leptin of the depleted adipose tissue."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2/M2 immune arm of the immune dysregulation (reduced immunoglobulin already mapped) and the tumour microenvironment of the cancers of Bloom syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine and growth failure: adiponectin, with leptin (already mapped), is the adipokine of the depleted adipose tissue and the growth failure (GH and IGF-1 already mapped) of Bloom syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the low body weight and metabolic state of Bloom syndrome."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Early GI cancer: the genome instability (BLM already mapped) of Bloom syndrome predisposes to the early-onset colorectal and other GI cancers, needing the surveillance."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "SCE diagnostic: the elevated sister-chromatid exchanges (the BLM already mapped hallmark) demonstrated in the cultured fibroblasts/lymphocytes are the diagnostic test of Bloom syndrome."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Leukaemia predisposition: Bloom syndrome predisposes to the acute leukaemias (ALL/AML) and the lymphomas, among its commonest and earliest malignancies."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immune arm: the IFN-γ of the T and NK (already mapped) cells is the type-II interferon arm of the immune dysregulation and the impaired anti-tumour/anti-infective immunity of Bloom syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response, part of the immunodeficiency dimension of Bloom syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of Bloom syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 axis: IL-17A drives the Th17 arm of the immune dysregulation and the recurrent-infection susceptibility of the immunodeficiency of Bloom syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation of Bloom syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Bloom syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) and are part of the immune-surveillance apparatus impaired in the immunodeficiency and cancer predisposition of Bloom syndrome."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Innate immunity: the macrophages are part of the innate immune compartment of the immune dysregulation and recurrent-infection susceptibility of Bloom syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) is part of the innate inflammatory dimension of the immune dysregulation of Bloom syndrome."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) complete the complement cascade of the innate immune dimension of Bloom syndrome."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the immune dysregulation of Bloom syndrome."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the recurrent infections and chronic disease of Bloom syndrome."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-immune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the immune dysregulation of the recurrent infections of Bloom syndrome."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-inflammatory axis: bradykinin, via B1/B2 receptors on mast cells (already mapped) and endothelium (already mapped), amplifies the vascular permeability and the inflammatory milieu of the recurrent infections of Bloom syndrome."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietic support: erythropoietin supports the management of the anaemia of the chronic disease and the myelosuppressive treatment of the cancer predisposition dimension of Bloom syndrome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell inflammatory axis: histamine, from mast cells (already mapped), amplifies the vascular permeability and the immunosuppressive cytokine milieu of the infection-prone and chronic-inflammatory dimension of Bloom syndrome."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-genotoxic axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative DNA damage that compounds the BLM-helicase (already mapped) repair deficiency of Bloom syndrome."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation contributes to the inflammatory milieu of the infection-prone immune dysregulation of Bloom syndrome."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Bloom testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of Bloom syndrome."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Bloom serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immunity; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of Bloom syndrome."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Bloom prolactin: prolactin, via PRLR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immune surveillance; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) immune cascade of Bloom syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Bloom oxytocin: oxytocin, via OXTR on macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates the antitumour immune cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Bloom vasopressin: vasopressin, via V1aR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immune tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Bloom selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS driving genomic instability; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Bloom sodium: sodium dysregulation in bone-marrow (already mapped) stroma and macrophages (already mapped) amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Bloom calcium: calcium regulates macrophage (already mapped) and bone-marrow (already mapped) stromal cell signalling; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and VEGF (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Bloom magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and bone-marrow (already mapped) stroma; magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and mTOR (already mapped) tumour-promoting cascade of Bloom syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "bloom iodine: iodine-dependent thyroid hormones in macrophage (already mapped) and dendritic cell (already mapped) regulate BLM (already mapped) helicase activity; iodine deficiency amplifies RAD51 (already mapped) and P53 (already mapped) cascade in Bloom syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "bloom copper: copper-dependent cuproenzymes in macrophage (already mapped) and dendritic cell (already mapped) regulate DNA repair; copper excess amplifies BLM (already mapped) and BRCA2 (already mapped) and P53 (already mapped) cascade in Bloom syndrome."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "bloom zinc: zinc finger domains of BLM (already mapped) and RAD51 (already mapped) coordinate DNA repair; zinc deficiency disrupts BRCA1 (already mapped) and P53 (already mapped) and BRCA2 (already mapped) cascade in Bloom syndrome."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Bloom carbon: carbon backbone of nucleotides in fibroblasts (already mapped) and b-cells (already mapped) sustains DNA replication; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) genomic instability in Bloom syndrome."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Bloom chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) modulate cellular homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Bloom hydrogen: hydrogen via ROS balance in fibroblasts (already mapped) and macrophages (already mapped) modulates replication-fork stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) genomic cascade in Bloom syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Bloom pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) restrains immune response; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour immune evasion cascade in Bloom syndrome."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Bloom glp-1: GLP-1 on macrophages (already mapped) and dendritic cells (already mapped) attenuates inflammatory skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Bloom angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Bloom WNT/β-catenin: WNT/β-catenin in fibroblasts (already mapped) and BLM-deficient cells (already mapped) modulates DNA-repair-genomic stability; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Bloom rankl: RANKL in macrophages (already mapped) and osteoclasts (already mapped) modulates bone-cancer predisposition; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Bloom smad4: SMAD4 in fibroblasts (already mapped) and macrophages (already mapped) mediates TGF-β tumour-suppression; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Bloom fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) modulates tumour ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Bloom notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) modulates stem-cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Bloom activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Bloom tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) modulates fibrotic repair balance; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Bloom cgrp: CGRP from fibroblasts (already mapped) and macrophages (already mapped) modulates neuroimmune tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Bloom calcitonin: calcitonin from fibroblasts (already mapped) and macrophages (already mapped) modulates calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Bloom substance-p: substance-P from fibroblasts (already mapped) and macrophages (already mapped) modulates neuroimmune pain signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Bloom aldosterone: aldosterone from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Bloom androgen-receptor: androgen receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates tumour sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Bloom norepinephrine: norepinephrine from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Bloom adrenomedullin: adrenomedullin from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Bloom bdnf: BDNF from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour neural tone; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome."
---

# Bloom Syndrome

## Overview

**Bloom syndrome (BS)** is a rare autosomal recessive **chromosomal instability syndrome** caused by biallelic loss-of-function mutations in the **BLM** gene (15q26.1), encoding the BLM RecQ helicase that dissolves double Holliday junctions (dHJs) to suppress crossover during homologous recombination. Bloom syndrome was first described by dermatologist David Bloom in 1954, who reported children with sun-sensitive telangiectatic facial erythema and small body size. The BLM gene was positionally cloned by Ellis et al. in 1995. The **Bloom Syndrome Registry (BSR)**, established by James German at Weill Cornell Medical College and ongoing for >60 years, has registered >300 patients from >40 countries and provides the primary epidemiological and cancer incidence dataset for BS [^ellis-1995-blm-cloning] [^german-1997-bloom-cancer].

BS is characterized by three cardinal features: **small body size** (the most consistent feature — all BS patients are substantially below the 3rd percentile for height and weight throughout life; not corrected by GH treatment), **sun-sensitive telangiectatic facial erythema** (butterfly-distribution erythema over nose/cheeks/lips, exacerbated by sun exposure, without photodamage; telangiectasias develop by 1-2 years), and **immunodeficiency** (reduced serum IgA, IgM; T-cell dysfunction; recurrent sinopulmonary infections). The **cytogenetic hallmark** is dramatically elevated **sister chromatid exchanges (SCE): ~10-fold higher** than in normal cells (50-100 SCEs/metaphase vs ~5-10 normal), the diagnostic gold standard. **Pan-cancer predisposition** affecting virtually every organ system is the dominant clinical threat in adults — arising from unconstrained crossover-mediated loss of heterozygosity (LOH) at tumor suppressor loci throughout the genome.

**Bloom syndrome vs. related chromosomal instability syndromes:**

| Feature | Bloom Syndrome (BLM) | Werner Syndrome (WRN) | Fanconi Anemia (FANC genes) |
|---|---|---|---|
| Inheritance | AR | AR | AR (XL for FANCB) |
| Age of onset | Birth | 3rd decade | Childhood |
| SCE | ~10x elevated | ~2-3x elevated | Normal (elevated breaks) |
| Hallmark cytogenetic | Elevated SCE | Variegated translocations | Radial chromosomes, DSBs |
| Cancer risk | Pan-cancer (ALL, lymphoma, GI) | Sarcomas, melanoma, thyroid | AML, squamous cell carcinoma |
| Skin | Sun-sensitive telangiectasia | Scleroderma-like, ulcers | Café-au-lait, hyperpigmentation |
| Immunodeficiency | Yes (IgA/IgM low) | Mild | Yes (bone marrow failure) |
| Median survival | ~26-30 years | ~47-54 years | Variable (marrow transplant) |

## Structure

### Genetic basis of Bloom syndrome

**BLM gene (15q26.1):**
- 22 exons; 1,417 aa; 159 kDa; ubiquitously expressed, highest in proliferating tissues
- All disease-causing BLM mutations result in loss of helicase activity, BTR complex assembly, or nuclear localization
- Over 70 distinct germline BLM mutations identified; diverse spectrum (nonsense, frameshift, missense in helicase core, splice site)

**blmAsh Ashkenazi Jewish founder mutation:**
- c.2207_2212delATCTGAinsTAGATTC: 6-bp deletion + 7-bp insertion in exon 10 → net +1 frameshift → premature stop codon at aa 740 → truncated non-functional protein
- Carrier frequency ~1/48,000 in Ashkenazi Jewish population; responsible for ~80% of Bloom syndrome in Ashkenazi families
- allele-specific PCR detects blmAsh; included in expanded Ashkenazi carrier panels (alongside HEXA, CFTR, FANCC)
- Non-Ashkenazi mutations: compound heterozygotes common; diverse mutations throughout BLM

**Somatic BLM reversion (diagnostic pitfall):**
- In BS cells (with ~10x elevated SCE), intragenic recombination can restore one BLM allele to wild-type within a clone → somatic mosaic revertant clones with normal SCE and growth advantage → overgrow BS cells in blood
- Clinical implication: a negative BLM gene test or normal SCE in blood does not exclude BS; must test fibroblasts or hair roots if blood results are discordant with clinical features

**Prevalence:**
- Estimated <1/1,000,000 worldwide; most concentrated in Ashkenazi Jewish populations; BSR has >300 registered patients since 1960

### Cytogenetics of Bloom syndrome

**SCE assay — diagnostic gold standard:**
- Cells cultured for two replication cycles in BrdU (bromodeoxyuridine) → sister chromatids differentially labeled (one strand BrdU-substituted) → metaphase spread staining (Hoechst 33258 + Giemsa) → sister chromatids differentially fluorescent → crossover exchanges (SCEs) visible as points where fluorescence switches between sister chromatids
- Normal human cells: ~5-10 SCEs/metaphase
- Bloom syndrome: ~50-100 SCEs/metaphase (~10x elevated; highly reproducible across tissues and age)
- Specificity: SCE ≥50/metaphase is specific for BLM LOF; WRN LOF (~2-3x), BRCA1/2 LOF, and other HR defects do NOT generate this degree of SCE elevation
- Diagnosis: SCE ≥50/metaphase in compatible clinical context = diagnostic; BLM molecular confirmation follows

**Additional cytogenetic findings:**
- Quadriradial chromosomes: four-armed chromosomal configurations from crossover between homologous chromosomes (non-sister); pathognomonic of BS when observed
- Elevated chromatid breaks and gaps
- Elevated numerical aberrations in some cell lineages

## Function

### Clinical features of Bloom syndrome

**Small body size (~100% penetrance):**
- The most consistent and defining feature; average adult height ~147-153 cm; average adult weight significantly below normal
- NOT caused by growth hormone deficiency (GH axis intact; GH treatment ineffective) — reflects intrinsic cellular replication defect
- Low birth weight (~2.5 kg typical); does not catch up with age

**Sun-sensitive facial erythema (~90% penetrance):**
- Telangiectatic erythema in butterfly distribution over nose, cheeks, ears, lower lip; exacerbated by sun exposure; develops 1-3 years of age
- Does NOT involve photodamage (no actinic keratoses, no photoaging — unlike xeroderma pigmentosum); biopsy shows telangiectasias and mild dermal inflammation
- ANA negative (distinguishes from lupus); strict sun avoidance and SPF 50+ sunscreen from infancy

**Immunodeficiency:**
- Reduced serum IgA (~90% of patients); reduced serum IgM (~60%); IgG often low-normal
- Variable T-cell dysfunction; CD4+ lymphopenia in some; NK cell reduction in some
- Clinical: recurrent sinopulmonary infections (otitis media, sinusitis, pneumonia) in childhood
- Management: prophylactic IgG replacement for severely hypogammaglobulinemic patients; antibiotic prophylaxis for recurrent infections

**Additional features:**
- Narrow elongated facies with prominent ears and retrognathia; characteristic but not severe dysmorphia
- Male infertility: azoospermia nearly universal (testes small; Sertoli-cell-only pattern on histology); female infertility: premature ovarian failure (~20-30 years); both sexes severely infertile
- High-pitched voice: laryngeal hypoplasia in many patients
- Diabetes mellitus: subset of older patients; mixed etiology (autoimmune T1DM, Type 3c from chronic pancreatitis, or T2DM-like insulin resistance)
- Normal intelligence: intellectual disability NOT typical (distinguishes BS from Seckel, Cockayne, Fanconi anemia with brain involvement)

### Cancer in Bloom syndrome

**Cancer spectrum (BSR data, >200 cancers in >300 patients) [^german-1997-bloom-cancer]:**
- Leukemia (AML/ALL): most common in first two decades; AML > ALL; ~50-100x general population risk; median age ~25 years for AML/ALL in BSR data
- Non-Hodgkin lymphoma: substantial risk in 3rd-4th decades; Burkitt lymphoma reported
- Gastrointestinal carcinomas: colorectal, gastric, esophageal, small bowel — dominant adult malignancy; colonoscopic surveillance from ~15 years
- Skin carcinomas (BCC, SCC): elevated lifetime risk; immune dysregulation + possible sun-skin interaction
- Breast cancer: elevated; early onset
- Other: lung, oral, cervical, bladder — virtually all carcinoma types have excess risk
- **Pan-cancer phenotype**: no organ is spared; reflects systemic LOH acceleration at all heterozygous tumor suppressor loci throughout the genome

**Cancer mechanism:**
- BLM LOF → unconstrained crossover → crossover-mediated LOH throughout the genome → when a heterozygous tumor suppressor allele undergoes crossover → distal LOH → biallelic TS LOF without additional mutation → tumor initiation
- Every BS patient has a unique background of heterozygous single-nucleotide variants across the genome; LOH can expose TS alleles at many loci → broad, non-tissue-specific predisposition
- Biallelic TS silencing by LOH is ~100x faster in BS cells than normal, because elevated SCE = elevated crossover frequency

## Pathology

### Diagnosis

**Diagnostic approach:**
1. **Clinical suspicion**: small body size + sun-sensitive facial erythema + immunodeficiency + Ashkenazi Jewish background OR family history of cancer → refer for SCE assay
2. **SCE assay (gold standard)**: blood lymphocytes or fibroblasts; ≥50 SCEs/metaphase in compatible clinical context = diagnostic for Bloom syndrome
3. **Molecular confirmation**: BLM sequencing + MLPA; in Ashkenazi patients, blmAsh allele-specific PCR first; compound heterozygotes common in non-Ashkenazi
4. **Pitfall — somatic reversion**: if blood SCE normal but clinical suspicion high, test fibroblasts (skin biopsy) or hair roots; somatic revertant clones in blood can normalize SCE

**Differential diagnosis:**
- Lupus erythematosus: butterfly rash but ANA+, photodamage present, SCE normal, size normal
- Xeroderma pigmentosum: sun sensitivity with photodamage, photoaging, SCE normal, NER deficiency (XPA-XPG genes)
- Fanconi anemia: chromosomal instability presenting as pancytopenia, radial chromosomes (not SCE), ICL sensitivity, FANC gene panel
- Werner syndrome: progeroid adult onset, scleroderma-like skin, SCE only ~2-3x elevated, normal childhood
- Rothmund-Thomson syndrome (RECQL4): poikiloderma from infancy, skeletal abnormalities, osteosarcoma; SCE not elevated
- Seckel syndrome (ATR): microcephaly, intellectual disability; SCE normal

**Surveillance protocol:**
- Annual CBC with differential: leukemia (AML, ALL) surveillance — lifelong from diagnosis
- Annual upper and lower GI endoscopy: from ~15 years; colorectal carcinoma most common adult malignancy
- Annual dermatological exam: skin carcinoma, rare melanoma
- Annual breast MRI/mammogram: from ~25 years
- Regular lymph node assessment: lymphoma surveillance
- Minimize CT scans (ionizing radiation sensitivity) — use MRI where feasible

**Treatment and management:**
- No disease-modifying therapy; management is surveillance and standard cancer treatment
- Chemotherapy sensitivity: BS cells hypersensitive to DNA crosslinkers (cisplatin, mitomycin C, cyclophosphamide) because BLM is required for interstrand crosslink (ICL) repair; dose reduction considerations for hematologic malignancies
- Radiation sensitivity: minimize therapeutic radiation; avoid unless essential; reduce diagnostic imaging
- IgG replacement therapy: for severe hypogammaglobulinemia with recurrent infections; IVIg or subcutaneous IgG
- Sun avoidance and SPF 50+ sunscreen: reduces facial erythema; lifelong
- Genetic counseling: AR inheritance; sibling recurrence 1/4; prenatal diagnosis by CVS/amniocentesis; Ashkenazi Jewish carrier screening includes blmAsh
- Registry: Bloom Syndrome Association and BSR — research cohort participation; clinical coordination; genetic counseling referral

## Connections

- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — Biallelic BLM LOF → Bloom syndrome via crossover accumulation and SCE elevation (~10x); chromosomal instability → LOH at tumor suppressor loci → pan-cancer predisposition (ALL, lymphoma, GI carcinoma, skin); Bloom Syndrome Registry has tracked >300 patients for >60 years.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BLM and BRCA1 form a complex at stalled replication forks to suppress aberrant homologous recombination and resolve Holliday junctions; both BLM LOF and BRCA1 LOF result in chromosomal instability and pan-cancer predisposition via distinct but overlapping HR defects.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — BLM and WRN are both RecQ helicases: BLM resolves double Holliday junctions to suppress crossover (SCE elevated ~10x in BLM LOF); WRN has exonuclease activity and maintains telomeres; BLM LOF → childhood-onset pan-cancer; WRN LOF → adult progeroid syndrome.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — BLM LOF in Bloom syndrome confers elevated colorectal cancer risk due to crossover-mediated LOH at APC and other CRC tumor suppressor loci; GI carcinomas are among the most common malignancies in adult Bloom syndrome patients; colonoscopy surveillance from early adulthood.
- `connects-to` → **[Burkitt Lymphoma](../../07-system/burkitt-lymphoma/README.md)** — Burkitt lymphoma and NHL are among the most common lymphoid malignancies in Bloom syndrome; crossover-mediated LOH at 8q24 (MYC) contributes; BS patients have ~50-100× elevated lymphoma risk; chemotherapy hypersensitivity in BS requires dose reduction.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC heterozygosity is vulnerable to crossover-mediated LOH in BLM-deficient cells → biallelic APC LOF without a second mutation → colorectal adenoma initiation; GI carcinomas dominate the adult BS cancer spectrum; colonoscopy from age 15 is a management cornerstone.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — BLM interacts with MLH1 (MMR); BLM-MLH1 cooperation suppresses microsatellite instability; BLM unwinds heteroduplex DNA during MMR; some BS GI cancers show MSI-H — dual HR + MMR defect may contribute to extreme GI carcinoma risk.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Bloom and DICER1 are both childhood cancer-predisposition syndromes but mechanistically unrelated: Bloom is genomic instability from a defective BLM helicase (high sister-chromatid exchange), DICER1 faulty microRNA processing — broken DNA repair versus gene dysregulation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The diagnostic hallmark of Bloom syndrome is a sun-sensitive facial rash: telangiectatic erythema in a butterfly distribution across the cheeks and nose that flares with UV exposure, reflecting cells that cannot properly repair replication-associated DNA damage.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Leukemia, especially acute lymphoblastic and myeloid, is the earliest and most common cancer in Bloom syndrome, often in childhood; the BLM-deficient genomic instability also makes these patients hypersensitive to chemotherapy, forcing substantial dose reductions.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Bloom and Werner syndrome are both RecQ-helicase disorders of genomic instability: Bloom (BLM) causes sister-chromatid exchange, sun-sensitive rash, short stature and early cancers, while Werner (WRN) causes premature aging and sarcomas—RecQ members whose loss destabilizes DNA.
- `connects-to` → **[AML](../aml/README.md)** — Leukemia is a leading Bloom-syndrome cancer: the BLM helicase defect causes extreme chromosomal instability and sister-chromatid exchange, so AML and ALL arise at strikingly young ages, and—because Bloom cells are hypersensitive to DNA-damaging agents—chemo doses must be reduced.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Bloom syndrome is markedly photosensitive: BLM helicase loss leaves cells unable to resolve replication stress, so ultraviolet photons readily cause the characteristic sun-exposed facial erythema (butterfly rash) and add to the cancer risk—patients need strict sun protection.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Bloom syndrome and Rothmund-Thomson are RecQ-helicase genome-instability disorders: Bloom (BLM), Rothmund-Thomson (RECQL4), and Werner (WRN) share defective DNA helicases causing chromosomal instability, growth failure, and high cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Bloom syndrome carries a strikingly high rate of early type 2 diabetes: despite low body weight, severe insulin resistance develops, so diabetes appears in childhood—part of a broad phenotype of growth deficiency, immunodeficiency, and cancer from BLM helicase loss.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Bloom syndrome includes an immunodeficiency: BLM helicase loss impairs lymphocyte development and antibody class-switching, causing low immunoglobulins and recurrent respiratory and ear infections—so immune failure compounds the genome instability driving its cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Bloom and Li-Fraumeni are both inherited genome-instability cancer syndromes by different routes: Bloom from BLM helicase loss causing excess recombination, Li-Fraumeni from p53 loss removing the damage checkpoint—both flood cells with mutations driving cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Bloom syndrome cells struggle to engage p53-driven safeguards: without BLM helicase, stalled forks and excess sister-chromatid exchange overwhelm the damage response, so the p53 checkpoint cannot keep pace—explaining the broad, early cancer risk of the syndrome.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BLM helicase partners with RAD51 in homologous recombination: BLM normally dissolves recombination intermediates that RAD51 forms, preventing crossovers, so its loss causes the hallmark surge in sister-chromatid exchange that defines Bloom syndrome diagnostically.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — Bloom syndrome and BRCA2 cancers share a homologous-recombination theme: BLM helicase works alongside BRCA2 and RAD51 to repair DNA by recombination, so its loss—like BRCA2 loss—causes genomic instability and a broad lifelong cancer predisposition.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Bloom syndrome includes immunodeficiency: defective DNA repair impairs B-cell antibody class-switching, lowering immunoglobulins and causing recurrent infections, while the same instability fuels the lymphomas and leukemias that often arise from these cells.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Bloom syndrome impairs the reproductive system: men are typically infertile and women have reduced, early-ending fertility, reflecting how the genome instability and repair defect that drive its cancers also disrupt the meiotic recombination needed to make gametes.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Bloom syndrome's most visible feature is profound short stature: BLM helicase loss stunts growth from before birth, producing proportionate dwarfism despite normal growth-hormone levels—so it is a growth disorder of the cell's replication machinery, not the hormone.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Bloom syndrome brings recurrent lung infection: an associated immunodeficiency (low immunoglobulins) leaves patients prone to pneumonia and chronic lung disease, so respiratory infections are a major cause of illness alongside the cancer risk.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Bloom syndrome carries an extreme, broad cancer risk including breast: genomic instability from BLM loss drives tumors at unusually young ages across many sites, so carriers need early, intensive surveillance for breast and other cancers.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Bloom syndrome compounds a fragile genome's stress response: BLM helicase untangles stalled replication forks that ATM and ATR guard, so losing BLM forces these damage-sensing kinases to work overtime—and the resulting instability fuels the syndrome's many cancers.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Bloom syndrome includes immune deficiency: many patients have low IgG and other antibodies, causing recurrent ear, sinus, and lung infections—an immunodeficiency layered on top of the cancer risk from defective DNA repair.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Bloom syndrome impairs T-cell help: defective DNA repair hampers the lymphocyte proliferation behind antibody class-switching, so weak T-helper support contributes to the low immunoglobulins and recurrent infections these patients suffer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxidative damage compounds Bloom syndrome's repair defect: with the BLM helicase gone, cells handle DNA breaks poorly, so reactive oxygen species and sunlight add lesions the cell cannot fix—fueling the genomic instability and cancer risk.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Bloom syndrome carries a steep colorectal cancer risk: the failed DNA repair lets mutations accumulate in the gut lining, so these patients develop bowel cancers young and need early, frequent colonoscopy among their many tumor risks.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Bloom syndrome is diagnosed in the fibroblast: cultured cells reveal sharply elevated sister-chromatid exchange, the cytogenetic fingerprint of BLM helicase loss that distinguishes it from other DNA-repair disorders.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bloom syndrome makes the marrow turn leukemic: its runaway genomic instability seeds mutations in blood-forming cells, so leukemias and lymphomas arise from the bone marrow at strikingly young ages.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Bloom syndrome burdens the pancreas: patients commonly develop diabetes as the gland's insulin output falters, and their broad cancer predisposition includes pancreatic tumors among many sites.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Bloom syndrome dims immune surveillance: a mild immunodeficiency weakens natural killer and antibody responses, leaving patients prone to infections and less able to cull the cancerous cells their unstable DNA spawns.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Bloom syndrome's butterfly facial rash is vascular: sun exposure dilates dermal endothelial-lined vessels into the telangiectatic erythema across the cheeks that marks the disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Bloom syndrome's commonest cancers strike the gut lining: the unstable DNA of the intestinal epithelium spawns early colorectal and other GI cancers, demanding cancer surveillance from a young age.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Bloom syndrome's universal cancer risk includes the liver: its profound genomic instability predisposes to tumors across the body, hepatocellular carcinoma among the many sites.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Bloom syndrome cannot mend its own DNA: the broken BLM helicase lets chromosomes swap arms in a flurry of sister-chromatid exchanges — the diagnostic hallmark — and leaves cells hypersensitive to radiation and oxidative damage.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sunlight inflames the Bloom syndrome face and eyes: the photosensitive butterfly rash of dilated telangiectatic vessels spreads across the cheeks and onto the conjunctiva, a visible sign of the disorder's UV sensitivity.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bloom syndrome's cancer spectrum reaches the kidney: among the many tumors its genomic instability invites, Wilms tumor and renal carcinoma occur, so the kidney joins the broad lifelong cancer surveillance.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Bloom syndrome leaves the body short of antibody: a common variable immunodeficiency-like drop in immunoglobulins accompanies it, so recurrent ear, sinus, and lung infections trouble these patients from childhood.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The diagnosis is read in the blood cells: Bloom's faulty BLM helicase produces a striking excess of sister-chromatid exchanges in cultured lymphocytes — the classic confirmatory test — while marrow failure can also drop the red cells into anemia.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut troubles span a lifetime: severe reflux and feeding difficulty stunt growth in Bloom infants, and the genomic instability later raises the risk of gastric and other gastrointestinal cancers.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Bloom syndrome comes with immune deficiency: poor antibody responses and reduced thymus-derived T-cell function leave children prone to recurrent ear, sinus and lung infections, part of why infections rival cancer as a cause of early death.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Bloom bodies resist insulin: many patients develop insulin resistance and early type 2 diabetes despite their small, lean frames, a metabolic derangement tied to the syndrome that adds to its lifelong health burden.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Bloom's failing immunity meets its cancer risk: weakened cytotoxic T-cell surveillance lets genomically unstable, mutation-riddled cells slip past immune killing, compounding the extraordinary lifetime cancer predisposition that defines the syndrome.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The growth axis runs low in Bloom: despite normal growth hormone, low IGF-1 signaling underlies the profound pre- and postnatal growth deficiency that gives these patients their characteristic small, lean stature.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The unstable genome breaks first in the marrow: Bloom syndrome's chromosomal instability drives myelodysplastic syndromes and leukemia at strikingly young ages, among the earliest of its many cancers.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Antibody output runs short: Bloom's immunodeficiency includes poor plasma-cell function and low immunoglobulin levels, leaving patients prone to the recurrent respiratory and ear infections of childhood.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Adult Bloom patients face carcinomas of the gut lining: the genomic instability that brings early leukemia later drives GI carcinomas including esophageal cancer, part of the syndrome's relentless lifelong cancer toll.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — The embryonal tumors appear in childhood: Bloom syndrome's chromosomal instability predisposes to Wilms tumor among other paediatric cancers, reflecting how broadly the loss of BLM helicase destabilizes the genome.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — BLM works alongside mismatch repair: the BLM helicase cooperates with the MSH2-containing mismatch-repair machinery to resolve recombination intermediates, so its loss compounds the genomic instability that mismatch-repair defects also cause.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Relentless DNA damage smolders into inflammation: the unrepaired breaks and replication stress of Bloom syndrome trigger DNA-sensing inflammatory signaling that activates NF-κB, a chronic inflammatory tone layered on its cancer risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A faltering immune system invites infection: Bloom syndrome includes an immunodeficiency with low immunoglobulins, so recurrent respiratory and gastrointestinal infections — and the sepsis they can become — are a major cause of illness.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Its cancer net is wide and starts early: Bloom syndrome's genomic instability and immunodeficiency raise the risk of carcinomas including HPV-driven cervical cancer, part of a remarkably broad, young-onset cancer spectrum.
- `connects-to` → **[COPD](../copd/README.md)** — Recurrent lung infection scars the airways: the immunodeficiency of Bloom syndrome causes repeated respiratory infections that can lead to bronchiectasis and chronic obstructive lung disease over time.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Infection, cancer and marrow strain lower the count: chronic infections, the disease's many malignancies and bone-marrow involvement combine to produce an anemia of chronic disease in Bloom syndrome.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A lifetime of cancer and illness weighs on the mind: living with profound cancer predisposition, recurrent infection, short stature and lifelong surveillance carries a substantial psychological burden in Bloom syndrome.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Its immunodeficiency invites recurrent infection: Bloom syndrome includes an antibody deficiency that leaves patients prone to recurrent respiratory and ear infections, often pneumococcal.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Immune defects and cancer therapy open the lung to mold: the immunodeficiency of Bloom syndrome, compounded by chemotherapy for its frequent cancers, can permit invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its DNA-repair defect makes tissue fragile to treatment: Bloom cells are hypersensitive to chemotherapy and radiation, so the doses used against its cancers cause severe tissue damage and poor healing.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Sunlight inflames its skin: Bloom syndrome causes a photosensitive telangiectatic butterfly erythema across the face, along with café-au-lait macules and a raised risk of skin cancer.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It stunts growth and disturbs metabolism: Bloom syndrome features severe proportionate short stature, and patients develop diabetes and hypogonadism with subfertility, tying it to the endocrine system.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Profound cancer risk breeds worry: the chromosomal instability and very high lifetime malignancy risk of Bloom syndrome demand lifelong surveillance that fosters chronic health anxiety.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It stunts the whole skeleton: profound proportionate pre- and postnatal growth deficiency leaves a small, slender frame, one of the defining clinical features of Bloom syndrome.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Antibody deficiency lets the lungs get infected: the immunodeficiency of Bloom syndrome causes recurrent respiratory and ear infections that can progress to bronchiectasis.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It troubles the gut early and late: feeding difficulties and gastro-oesophageal reflux are common in infancy, while a high lifetime risk of gastrointestinal cancers emerges in adulthood.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Genomic instability cripples immunity and lymphoid tissue: Bloom syndrome causes immunodeficiency with low immunoglobulins and recurrent infections, alongside a very high risk of leukaemia and lymphoma.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It predisposes to childhood kidney cancer: Wilms tumour is among the many malignancies the genomic instability of Bloom syndrome can cause, demanding cancer surveillance from childhood.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Metabolic disease reaches the heart: Bloom syndrome carries a high rate of type 2 diabetes and dyslipidaemia, bringing premature cardiovascular risk despite the patients' characteristic small stature.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Treatment must be gentler: the DNA-repair defect of Bloom syndrome makes patients hypersensitive to DNA-damaging chemotherapy and radiation, forcing dose reduction when their many cancers are treated.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Sun sensitivity breeds skin cancer: the photosensitive facial rash of Bloom syndrome reflects defective DNA repair that also drives basal and squamous cell skin cancers at a young age.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Instability seeds gut tumours: chromosomal instability in Bloom syndrome predisposes to gastrointestinal adenocarcinomas, including gastric and colorectal cancer, often decades earlier than usual.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A synthetic-lethal vulnerability: BLM helicase loss leaves Bloom cells reliant on other DNA-repair routes, making homologous-recombination and replication-stress pathways (PARP, ATR) candidate targets — and BLM itself an anticancer drug target in unstable tumours.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Genomic chaos may aid immunotherapy: the extreme chromosomal instability of Bloom syndrome can generate the high mutational burden and neoantigens that make some of its cancers candidates for checkpoint blockade.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Immunodeficiency rides along: Bloom syndrome impairs B-cell maturation and class switching in germinal centres, causing low immunoglobulins and recurrent sinopulmonary infections alongside its cancer risk.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Genome instability fails the marrow: like other DNA-repair-defective syndromes, Bloom syndrome can progress to bone-marrow failure and cytopenias on the path to myelodysplasia and leukaemia.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Short stature and skeletal anomalies: proportionate dwarfism is a defining feature of Bloom syndrome, with thin cortical bone and skeletal anomalies reflecting profoundly impaired growth.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cancer at every site: Bloom syndrome's extreme genomic instability predisposes to the full spectrum of malignancy at young ages, including pancreatic and other gastrointestinal adenocarcinomas.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Lymphoma in a broad spectrum: Bloom syndrome's genomic instability raises the risk of aggressive lymphomas like diffuse large B-cell lymphoma, often at unusually young ages.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Sarcomas of genomic instability: like its sister helicaseopathies Werner and Rothmund-Thomson, Bloom syndrome raises the risk of osteosarcoma and other sarcomas alongside its carcinomas.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver tumours too: the all-cancer predisposition of Bloom syndrome extends to the liver, with hepatocellular and other tumours arising in the hepatic lobules at young ages.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — DNA-repair predisposition: like Lynch syndrome, Bloom syndrome is a hereditary DNA-repair defect that drives early colorectal and other cancers—genome instability from BLM loss rather than mismatch-repair failure.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — Genome-stability partner: ATRX maintains chromatin and telomere stability and suppresses alternative lengthening of telomeres; its loss, like BLM loss, generates the replication stress and genomic instability that fuel cancer.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Sun-sensitive skin cancer: the photosensitivity and chromosomal instability of Bloom syndrome raise the risk of skin cancers including melanoma, alongside the basal cell carcinomas already typical of the disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplification-prone oncogene: the genomic instability of Bloom syndrome favours oncogene amplifications such as MYC, helping drive the broad spectrum of cancers that develop at young ages.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomere maintenance: BLM helicase normally helps resolve telomeric replication, and its loss stresses telomere maintenance, where TERT reactivation is one route the resulting tumours take to immortality.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: the chromosomal instability of Bloom syndrome readily amplifies cyclin D1 and other cell-cycle drivers, pushing damaged cells through the G1 checkpoint into proliferation.
- `connects-to` → **[RECQL4](../../03-molecular/recql4/README.md)** — RecQ-helicase family: BLM is one of five human RecQ helicases, and its loss in Bloom syndrome parallels the genomic instability and cancer predisposition of RECQL4 (Rothmund-Thomson) and WRN (Werner) disease.
- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Homologous recombination: BLM cooperates with the BRCA-PALB2 homologous-recombination machinery to resolve recombination intermediates, so its loss raises sister-chromatid exchange and cancer risk.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Tumour-suppressor loss: the rampant chromosomal instability of Bloom syndrome readily inactivates tumour suppressors like CDKN2A, contributing to the exceptionally broad early-onset cancer spectrum.
- `connects-to` → **[p21 (CDKN1A)](../../03-molecular/cdkn1a/README.md)** — The persistent DNA damage and unresolved recombination intermediates of BLM-deficient cells chronically activate the p53-p21 checkpoint, arresting cells and contributing to the growth deficiency characteristic of Bloom syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Cells in Bloom syndrome that accumulate irreparable DNA damage undergo caspase-3-mediated apoptosis, a cell-loss mechanism that compounds the impaired growth alongside the cancer-prone surviving clones.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — The MDM2-p53 axis governs the heightened p53 response that BLM-deficient cells mount against constant DNA damage, balancing the tumor suppression against the cell loss that limits growth in Bloom syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — BLM-deficient cells accumulate micronuclei and cytosolic DNA from their excess chromosomal breakage, activating cGAS-STING and a chronic type-I-interferon inflammation that accompanies the genomic instability of Bloom syndrome.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase-derived reactive oxygen species add oxidative lesions to the already unstable BLM-deficient genome, compounding the DNA damage that drives the cancer predisposition and sun-sensitive skin of Bloom syndrome.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Bloom syndrome features low immunoglobulins, including secretory IgA, and the resulting impaired mucosal immunity underlies the recurrent respiratory and gastrointestinal infections that complicate the disorder.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — E2F1 transactivates homologous-recombination genes including RAD51 and BRCA1 (already mapped), so the RB-E2F axis intersects the very repair machinery BLM helicase loss compromises in Bloom syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cyclin-D-CDK4/6 (cyclin-D1 already mapped) propels cell-cycle entry, and the genomic instability of BLM-deficient cells accelerates the mutational hits that deregulate this axis in Bloom-associated cancers.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 holds back E2F-driven S-phase entry until repair is complete, and the relentless replication stress of Bloom syndrome makes this restraint critical to limiting propagation of damaged genomes.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense limits the reactive-oxygen-species-driven DNA damage that compounds the genomic instability of BLM-helicase deficiency in Bloom syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling downstream of growth hormone, IGF-1 and insulin (all already mapped) governs the growth programs constrained in the growth failure of Bloom syndrome yet co-opted by its cancers.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis supports the diverse early-onset malignancies to which the genomic instability of Bloom syndrome predisposes.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — GH/IGF-1/insulin signaling through PI3K-AKT-mTOR (GH, IGF-1, insulin and AKT mapped) governs the growth axis, dysregulated in the growth deficiency of Bloom syndrome.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT signaling (AKT mapped) is a tumor-suppressor counterweight to the proliferative drive in the cancer-prone cells of Bloom syndrome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK-MAPK proliferative signaling cooperates with the genomic instability of BLM-helicase loss in driving the cancer predisposition of Bloom syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Genomic instability from BLM-helicase loss generates cytosolic DNA that engages cGAS-STING (mapped) and IFN-STAT1 signaling, contributing to the inflammatory phenotype of Bloom syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the chronic oxidative and replicative stress of the genomically unstable cells of Bloom syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the immune-cell activation relevant to the immunodeficiency and cancer surveillance of Bloom syndrome.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling shapes the inflammatory tumor-promoting microenvironment relevant to the cancer predisposition of Bloom syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the genomically unstable, malignancy-prone cells of Bloom syndrome depend on.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the DNA-damage response and Wnt/β-catenin signaling relevant to the genomic instability and cancer predisposition of Bloom syndrome.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the genomically unstable cells of Bloom syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory context of the tumor microenvironment in the cancer-prone Bloom syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and oxidative-stress adaptation participates in the cellular stress of the genomically unstable cells of Bloom syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic and growth homeostasis relevant to Bloom syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the cellular stress responses to the genomic instability of Bloom syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation accompanying the genomic instability of Bloom syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the malignancies of Bloom syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal and marrow interactions relevant to Bloom syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape accompanying the genomic instability of Bloom syndrome.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 anti-apoptotic signaling participates in the survival of the genomically unstable cells and the lymphoid-neoplasia predisposition of Bloom syndrome.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 transcription-factor activity participates in the hematopoietic differentiation and leukemia predisposition of Bloom syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory and tumor-microenvironment processes of Bloom syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunodeficiency: Bloom syndrome features immunodeficiency with reduced immunoglobulins (already mapped), and impaired MHC class II-restricted antigen presentation contributes to the recurrent infections that complicate the disorder.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — Metabolic risk: Bloom syndrome carries a strikingly high risk of early type 2 diabetes with insulin resistance, so impaired insulin-receptor signalling is a common endocrine complication alongside the short stature already mapped.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: reduced IL-2-driven T-cell responses form part of the cellular immunodeficiency of Bloom syndrome, compounding the antibody deficiency and predisposing to the infections that accompany its genome instability.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Genome-instability interferon: unrepaired DNA and micronuclei in Bloom syndrome cells release cytosolic DNA that, through cGAS-STING (already mapped), triggers a type I interferon response, part of the chronic inflammatory signature of genome-instability disorders.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — Inflammatory dysregulation: the immune dysfunction of Bloom syndrome includes dysregulated pro-inflammatory cytokines such as TNF, contributing to the inflammatory milieu that accompanies its immunodeficiency and cancer predisposition.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Humoral immune defect: the immunodeficiency of Bloom syndrome extends beyond low immunoglobulins (already mapped) to impaired complement-supported humoral defence, part of the broad immune vulnerability to infection.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory dysregulation: the immune dysfunction of Bloom syndrome includes dysregulated pro-inflammatory cytokines such as IL-1 (TNF and IL-6 already mapped), contributing to the inflammatory milieu of its immunodeficiency and cancer predisposition.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunoregulatory balance: the anti-inflammatory IL-10 counters the dysregulated pro-inflammatory cytokines (TNF and IL-6 already mapped) of Bloom syndrome, and the imbalance is part of the broad immune dysfunction of the disorder.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Immunodeficiency: the spleen and the wider immune system are compromised in Bloom syndrome (immunoglobulin G already mapped), contributing to the recurrent infections that accompany its genome-instability and cancer predisposition.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Humoral immune dysregulation: IL-4 and the type-2 response support the B-cell (already mapped) antibody production (immunoglobulin G already mapped) impaired in Bloom syndrome, part of the humoral immunodeficiency that predisposes to recurrent infections.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Cancer-therapy anaemia: the frequent and diverse cancers of Bloom syndrome and their chemotherapy cause anaemia needing transfusion, whose repeated support can load the body with iron in these cancer-prone patients.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Growth failure and low weight: the profound growth retardation and low body weight of Bloom syndrome (growth hormone and IGF-1 already mapped) are reflected in the low leptin of the depleted adipose tissue.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2/M2 immune arm of the immune dysregulation (reduced immunoglobulin already mapped) and the tumour microenvironment of the cancers of Bloom syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine and growth failure: adiponectin, with leptin (already mapped), is the adipokine of the depleted adipose tissue and the growth failure (GH and IGF-1 already mapped) of Bloom syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the low body weight and metabolic state of Bloom syndrome.
- `connects-to` → **[Colorectal cancer](../colorectal-cancer/README.md)** — Early GI cancer: the genome instability (BLM already mapped) of Bloom syndrome predisposes to the early-onset colorectal and other GI cancers, needing the surveillance.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — SCE diagnostic: the elevated sister-chromatid exchanges (the BLM already mapped hallmark) demonstrated in the cultured fibroblasts/lymphocytes are the diagnostic test of Bloom syndrome.
- `connects-to` → **[ALL](../all/README.md)** — Leukaemia predisposition: Bloom syndrome predisposes to the acute leukaemias (ALL/AML) and the lymphomas, among its commonest and earliest malignancies.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immune arm: the IFN-γ of the T and NK (already mapped) cells is the type-II interferon arm of the immune dysregulation and the impaired anti-tumour/anti-infective immunity of Bloom syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response, part of the immunodeficiency dimension of Bloom syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of Bloom syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 axis: IL-17A drives the Th17 arm of the immune dysregulation and the recurrent-infection susceptibility of the immunodeficiency of Bloom syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation of Bloom syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Bloom syndrome.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) and are part of the immune-surveillance apparatus impaired in the immunodeficiency and cancer predisposition of Bloom syndrome.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Innate immunity: the macrophages are part of the innate immune compartment of the immune dysregulation and recurrent-infection susceptibility of Bloom syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) is part of the innate inflammatory dimension of the immune dysregulation of Bloom syndrome.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) complete the complement cascade of the innate immune dimension of Bloom syndrome.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the immune dysregulation of Bloom syndrome.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling of the anaemia of the recurrent infections and chronic disease of Bloom syndrome.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-immune axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the immune dysregulation of the recurrent infections of Bloom syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-inflammatory axis: bradykinin, via B1/B2 receptors on mast cells (already mapped) and endothelium (already mapped), amplifies the vascular permeability and the inflammatory milieu of the recurrent infections of Bloom syndrome.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietic support: erythropoietin supports the management of the anaemia of the chronic disease and the myelosuppressive treatment of the cancer predisposition dimension of Bloom syndrome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell inflammatory axis: histamine, from mast cells (already mapped), amplifies the vascular permeability and the immunosuppressive cytokine milieu of the infection-prone and chronic-inflammatory dimension of Bloom syndrome.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-genotoxic axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative DNA damage that compounds the BLM-helicase (already mapped) repair deficiency of Bloom syndrome.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation contributes to the inflammatory milieu of the infection-prone immune dysregulation of Bloom syndrome.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Bloom testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of Bloom syndrome.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Bloom serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immunity; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of Bloom syndrome.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Bloom prolactin: prolactin, via PRLR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immune surveillance; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) immune cascade of Bloom syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Bloom oxytocin: oxytocin, via OXTR on macrophages (already mapped) and T-cytotoxic cells (already mapped), attenuates the antitumour immune cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Bloom vasopressin: vasopressin, via V1aR on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates antitumour immune tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Bloom selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS driving genomic instability; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Bloom sodium: sodium dysregulation in bone-marrow (already mapped) stroma and macrophages (already mapped) amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Bloom calcium: calcium regulates macrophage (already mapped) and bone-marrow (already mapped) stromal cell signalling; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and VEGF (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Bloom magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and bone-marrow (already mapped) stroma; magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and mTOR (already mapped) tumour-promoting cascade of Bloom syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — bloom iodine: iodine-dependent thyroid hormones in macrophage (already mapped) and dendritic cell (already mapped) regulate BLM (already mapped) helicase activity; iodine deficiency amplifies RAD51 (already mapped) and P53 (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — bloom copper: copper-dependent cuproenzymes in macrophage (already mapped) and dendritic cell (already mapped) regulate DNA repair; copper excess amplifies BLM (already mapped) and BRCA2 (already mapped) and P53 (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — bloom zinc: zinc finger domains of BLM (already mapped) and RAD51 (already mapped) coordinate DNA repair; zinc deficiency disrupts BRCA1 (already mapped) and P53 (already mapped) and BRCA2 (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Bloom carbon: carbon backbone of nucleotides in fibroblasts (already mapped) and b-cells (already mapped) sustains DNA replication; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) genomic instability in Bloom syndrome.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Bloom chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) modulate cellular homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Bloom hydrogen: hydrogen via ROS balance in fibroblasts (already mapped) and macrophages (already mapped) modulates replication-fork stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) genomic cascade in Bloom syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Bloom pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) restrains immune response; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour immune evasion cascade in Bloom syndrome.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Bloom glp-1: GLP-1 on macrophages (already mapped) and dendritic cells (already mapped) attenuates inflammatory skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Bloom angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Bloom WNT/β-catenin: WNT/β-catenin in fibroblasts (already mapped) and BLM-deficient cells (already mapped) modulates DNA-repair-genomic stability; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Bloom rankl: RANKL in macrophages (already mapped) and osteoclasts (already mapped) modulates bone-cancer predisposition; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Bloom smad4: SMAD4 in fibroblasts (already mapped) and macrophages (already mapped) mediates TGF-β tumour-suppression; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Bloom fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) modulates tumour ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Bloom notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) modulates stem-cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Bloom activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Bloom tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) modulates fibrotic repair balance; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Bloom cgrp: CGRP from fibroblasts (already mapped) and macrophages (already mapped) modulates neuroimmune tone; cgrp dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Bloom calcitonin: calcitonin from fibroblasts (already mapped) and macrophages (already mapped) modulates calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Bloom substance-p: substance-P from fibroblasts (already mapped) and macrophages (already mapped) modulates neuroimmune pain signalling; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Bloom aldosterone: aldosterone from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — Bloom androgen-receptor: androgen receptor on fibroblasts (already mapped) and macrophages (already mapped) modulates tumour sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in Bloom syndrome.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Bloom norepinephrine: norepinephrine from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Bloom adrenomedullin: adrenomedullin from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in Bloom syndrome.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Bloom bdnf: BDNF from fibroblasts (already mapped) and macrophages (already mapped) modulates tumour neural tone; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cancer-predisposition cascade in Bloom syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ellis-1995-blm-cloning]: Ellis NA, Groden J, Ye TZ, et al. The Bloom's syndrome gene product is homologous to RecQ helicases. *Cell.* 1995;83(4):655-666. [doi:10.1016/0092-8674(95)90105-1](https://doi.org/10.1016/0092-8674(95)90105-1) · [PubMed 7585968](https://pubmed.ncbi.nlm.nih.gov/7585968/)
[^german-1997-bloom-cancer]: German J. Bloom's syndrome. XX. The first 100 cancers. *Cancer.* 1997;71(12):4016-4023. [doi:10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E](https://doi.org/10.1002/1097-0142(19930615)71:12<4016::AID-CNCR18>3.0.CO;2-E) · [PubMed 9216035](https://pubmed.ncbi.nlm.nih.gov/9216035/)
