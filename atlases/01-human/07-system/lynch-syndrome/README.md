---
schema: human-scale-entry/v1
id: lynch-syndrome
name: Lynch Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Lynch syndrome is the most common inherited cancer predisposition syndrome; germline MMR gene mutations (MLH1, MSH2, MSH6, PMS2) → MSI-H tumors; CRC lifetime risk ~40-80%; pembrolizumab/dostarlimab FDA-approved for dMMR tumors; universal tumor MMR testing recommended."
aliases: ["Lynch syndrome", "HNPCC", "hereditary nonpolyposis colorectal cancer", "MMR Lynch", "dMMR Lynch", "MLH1 Lynch", "MSH2 Lynch", "MSI-H Lynch", "Lynch colon cancer", "Lynch endometrial"]
sources:
  - id: bonadona-2011-lynch-risks
    type: peer-reviewed
    cite: "Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. JAMA. 2011;305(22):2304-2310."
    doi: "10.1001/jama.2011.743"
    pmid: "21642683"
    url: "https://doi.org/10.1001/jama.2011.743"
  - id: lynch-2015-lynch-review
    type: peer-reviewed
    cite: "Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. Nat Rev Cancer. 2015;15(3):181-194."
    doi: "10.1038/nrc3878"
    pmid: "25673086"
    url: "https://doi.org/10.1038/nrc3878"
cross_links:
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Germline MSH2 mutation causes ~31% of Lynch syndrome; MSH2 IHC loss indicates MSH2 or EPCAM mutation; MSH2-MSH6 (MutSα) detects base-base mismatches; MSH2 LOF → MSI-H → elevated TMB → immunotherapy sensitivity in Lynch tumors"
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "MLH1 germline mutation causes ~50% of Lynch syndrome; MLH1-PMS2 (MutLα) recruited by MutS complexes → MMR strand excision; MLH1 promoter methylation causes sporadic MSI-H CRC (not Lynch); MLH1 + PMS2 IHC co-loss indicates MLH1 mutation or methylation"
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "dMMR Lynch tumors are highly immunogenic → MSI-H → elevated TMB → PD-L1 high; pembrolizumab FDA-approved for dMMR/MSI-H solid tumors (KEYNOTE-158, 2020); dostarlimab for dMMR endometrial; Lynch tumors were the first tissue-agnostic immunotherapy indication"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Lynch CRC: most common Lynch-associated cancer; lifetime risk with MLH1/MSH2: ~40-80%; proximal colon predominance, mucinous histology, tumor-infiltrating lymphocytes; Lynch CRC has good prognosis; colonoscopy from age 25-30 recommended"
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Endometrial cancer is the second most common Lynch cancer and the sentinel tumor in many women (54% with MLH1); usually dMMR/MSI-H endometrioid; risk-reducing hysterectomy plus BSO after childbearing is offered, and dostarlimab (RUBY) is approved for advanced dMMR disease."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Lynch confers a ~13% lifetime gastric cancer risk (MLH1/MSH2) — the main hereditary cause of intestinal-type (not diffuse) gastric cancer; these dMMR/MSI-H tumors have high TIL density, contrasting with CDH1-driven diffuse HDGC; upper endoscopy is offered to carriers."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Colorectal mucosa is the highest-turnover epithelium, so its microsatellites accumulate the most replication errors when MMR fails — why CRC is the commonest Lynch cancer; Lynch CRC favors the proximal colon, is mucinous with brisk lymphocytic infiltrate, screened from age 20-25."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Lynch and juvenile polyposis are both dominant hereditary colorectal cancer syndromes but opposite: Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas, JPS is TGF-β/BMP loss making many hamartomatous polyps — repair defect versus stromal overgrowth."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Lynch and FAP are the two major hereditary colorectal cancer syndromes but differ starkly: FAP (germline APC) carpets the colon with thousands of adenomas and near-100% cancer risk, while Lynch (MMR genes) makes few polyps but fast MSI-high tumors via accelerated mutation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Lynch tumors are the prototype of immunotherapy response: mismatch-repair deficiency generates thousands of frameshift neoantigens that draw dense cytotoxic CD8+ T cells, so dMMR/MSI-H cancers respond strongly to anti-PD-1 — the basis of pembrolizumab's tissue-agnostic approval."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian cancer is part of the Lynch syndrome tumor spectrum: mismatch-repair deficiency raises the lifetime risk of (usually endometrioid or clear-cell) ovarian cancer alongside endometrial and colorectal cancer, so risk-reducing salpingo-oophorectomy is offered to carriers."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Lynch syndrome extends to the urinary tract: MSH2 carriers especially face raised risk of upper-tract urothelial carcinoma (renal pelvis, ureter) and bladder cancer, so urine surveillance is considered; these MSI-high tumors respond to checkpoint immunotherapy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Lynch syndrome cancers are the paradigm of immunotherapy-responsive tumors: mismatch-repair deficiency generates a high microsatellite-instability mutational load and abundant neoantigens, making MSI-high/dMMR tumors—wherever they arise—exquisitely sensitive to PD-1 blockade."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Pancreatic cancer is part of the Lynch spectrum: mismatch-repair deficiency raises pancreatic adenocarcinoma risk, and rare MMR-deficient pancreatic tumors are hypermutated and respond to checkpoint therapy—unlike most pancreatic cancers, which resist immunotherapy."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Cholangiocarcinoma belongs to the Lynch tumor spectrum: mismatch-repair loss predisposes to biliary-tract cancers, and like other Lynch tumors these are microsatellite-unstable and hypermutated—candidates for checkpoint immunotherapy exploiting their neoantigens."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Lynch syndrome can cause brain tumors as Turcot syndrome: mismatch-repair loss predisposes to gliomas including glioblastoma, and biallelic MMR deficiency gives childhood high-grade gliomas—linking a DNA-repair defect in the gut to tumors in the brain."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Lynch syndrome's Muir-Torre variant shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so a sebaceous skin tumor can be the first clue prompting Lynch testing and colon surveillance."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Lynch syndrome raises small-bowel cancer risk: mismatch-repair deficiency predisposes to small-intestinal adenocarcinoma—rare in the general population—so surveillance and a low threshold for investigating GI symptoms extend beyond the colon."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Lynch tumors still travel the Wnt road to cancer: mismatch-repair loss accelerates mutation, but colorectal carcinogenesis still typically requires Wnt/beta-catenin activation via APC—so MMR failure speeds, rather than replaces, the adenoma-carcinoma sequence."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Lynch syndrome predisposes across the digestive system: mismatch-repair loss most often causes colorectal cancer but also stomach, small-bowel, pancreatic and biliary tumors, so broad GI surveillance anchors management of the commonest hereditary cancer syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Lynch syndrome heavily affects the female reproductive system: endometrial cancer rivals colorectal as the most common Lynch tumor and is often the sentinel cancer, and ovarian cancer risk is raised too—so gynecologic surveillance and risk-reducing surgery matter."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The Muir-Torre variant of Lynch syndrome shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so these uncommon skin tumors can be the first clue prompting Lynch genetic testing."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Lynch syndrome reaches the urinary tract above the bladder: MMR deficiency raises the risk of urothelial cancer in the renal pelvis and ureter, so surveillance and any blood in the urine prompt imaging of the upper tracts, not just cystoscopy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Prostate cancer is a lower-penetrance Lynch tumor: MMR-gene carriers face a modestly increased, sometimes more aggressive prostate cancer, so family history of Lynch is weighed alongside PSA in deciding screening for these men."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Lynch tumors are immunotherapy-responsive because they are hypermutated: MMR loss spawns countless neoantigens that dendritic cells present to prime T cells, explaining why checkpoint blockade works so well in mismatch-repair-deficient cancers."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "A BRAF test separates Lynch from look-alike sporadic cancers: sporadic MSI-high colon tumors usually carry a BRAF V600E mutation, while Lynch tumors are BRAF-wild-type, so BRAF status is a key reflex test before diagnosing the inherited syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Lynch tumors' flood of mutations alerts NK cells: mismatch-repair failure makes hypermutated cells display stress signals and odd peptides that natural killer cells (and T cells) can attack—part of why these cancers are so immunotherapy-sensitive."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Lynch (MSI-high) tumors often form B-cell-rich lymphoid structures: clusters of B cells and tertiary lymphoid organs inside these hypermutated cancers help mount the immune response, and their presence predicts better checkpoint-therapy results."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Lynch tumors often knock out the TGF-beta brake: the mismatch-repair defect causes frameshift mutations in TGFBR2, a coding microsatellite, so the colorectal cancers escape TGF-beta's growth restraint—a signature lesion of MSI-high disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Lynch syndrome can reach the brain in its Turcot variant: mismatch-repair loss raises the risk of gliomas including glioblastoma, so brain tumors join the colorectal and endometrial cancers in the syndrome's spectrum."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Even Lynch's hot tumors recruit regulatory T cells: the hypermutated, neoantigen-rich cancers draw a strong immune response, but Tregs in the infiltrate restrain it—part of why checkpoint blockade, which lifts that brake, works so well here."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Lynch colorectal tumors bleed iron away: the cancer oozes blood into the gut, so an unexplained iron-deficiency anemia can be the first clue that prompts the colonoscopy which finds it."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Lynch cancers spring from the gut's epithelium: with mismatch repair broken, mutations pile up in the colonic and endometrial lining, so the epithelium turns malignant faster than in sporadic disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Lynch's hypermutated tumors draw macrophages: the neoantigen-rich cancers attract a dense immune infiltrate including macrophages, part of the inflamed microenvironment behind their strong response to immunotherapy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Lynch is managed by light: frequent colonoscopy from young adulthood catches and removes the fast-arising colorectal cancers, the surveillance that most reduces deaths in carriers."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Lynch raises gastric cancer risk: mismatch-repair-deficient stomach cancers occur, especially in MLH1 and MSH2 carriers, so upper endoscopy joins surveillance in high-incidence regions."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Lynch's Turcot variant strikes the brain: mismatch-repair loss raises the risk of gliomas, extending the syndrome's reach to the neurons of the central nervous system."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Lynch syndrome cannot proofread its DNA: losing a mismatch-repair gene lets tiny errors accumulate at repetitive sequences — microsatellite instability — so its tumors carry a huge mutation load that makes them strikingly responsive to immunotherapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Lynch reaches the liver and bile ducts: it raises the risk of cholangiocarcinoma, and its colorectal cancers spread there, so the liver is both a primary site and the commonest destination of its tumors."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Inheriting two faulty copies is far worse: constitutional mismatch-repair deficiency, the biallelic form, causes childhood leukemias and lymphomas, the marrow joining the syndrome's cancer spectrum in its most severe variant."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Mismatch-repair loss is read off the slide: an antibody panel staining for MLH1, MSH2, MSH6, and PMS2 by immunohistochemistry shows which protein has gone missing in the tumor, the first-line screen that flags Lynch before confirmatory germline sequencing."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Slow tumor bleeding shows up in the red cells: a Lynch colorectal or gastric cancer often declares itself first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic occult blood loss that should prompt early colonoscopy."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas falls within the spectrum: Lynch raises the lifetime risk of pancreatic cancer several-fold, and because such tumors are mismatch-repair-deficient and MSI-high, they are among the rare pancreatic cancers that can respond to checkpoint immunotherapy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Aspirin earns its place in Lynch through platelets: the CAPP2 trial showed daily aspirin sharply cuts colorectal cancer in carriers, an effect tied partly to blocking platelet COX-1 and the tumor-promoting signals activated platelets release."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Lynch tumors teem with immune cells: their mismatch-repair defect spawns countless neoantigens that draw in B cells and plasma cells forming tertiary lymphoid structures, a brisk immune response that underlies their striking sensitivity to checkpoint therapy."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "The mutation count runs high: mismatch-repair failure lets mutations accumulate across genes including KRAS, shaping the tumor's behavior and, with RAS status, guiding which targeted drugs can be added to its treatment."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "The hypermutated tumors are immunotherapy magnets: mismatch-repair loss spawns countless neoantigens, so blocking CTLA-4 alongside PD-1 can unleash a strong T-cell attack, making Lynch cancers among the most checkpoint-responsive of all solid tumors."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Two great hereditary-cancer syndromes sit side by side: where BRCA-driven HBOC fails DNA double-strand repair, Lynch fails mismatch repair — both flagged by family history, but each needing its own gene panel, surveillance plan, and tumor-specific therapies."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "The brain is on the tumor list too: in the Turcot variant, mismatch-repair failure drives gliomas arising from astrocytes, so the same defect that floods the colon with mutations can also seed aggressive brain tumors."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Occult bleeding announces the colon cancer: a Lynch-associated colorectal tumor often bleeds slowly, so unexplained iron-deficiency anemia in a carrier prompts the colonoscopy that finds it."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its cancers clot and its surgery adds risk: the colorectal and other adenocarcinomas of Lynch syndrome carry a raised venous thromboembolism risk, compounded by the resections used to treat them."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery opens the door to infection: the colectomy and other resections that Lynch cancers require can be complicated by anastomotic leak and intra-abdominal sepsis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Inflammation feeds the mismatch-repair-deficient tumor: IL-6-driven STAT3 signaling promotes proliferation and survival in the inflamed Lynch colorectal cancer, a node alongside the heavy immune infiltrate of these MSI-high tumors."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation pushes the polyp to cancer: NF-κB activation in the colonic mucosa adds pro-survival, pro-proliferative signals that, layered on mismatch-repair loss, speed the adenoma-to-carcinoma progression in Lynch syndrome."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor bleeding and inflammation drain the blood: beyond the iron loss of bleeding Lynch colorectal cancers, their inflammatory cytokines suppress erythropoiesis, adding an anemia of chronic disease to the iron deficiency."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its urinary-tract cancers can block the kidneys: Lynch syndrome predisposes to upper-tract urothelial carcinoma, which obstructs the ureters into hydronephrosis, and the platinum chemo for its cancers adds nephrotoxicity threatening chronic kidney disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its colorectal-cancer chemo can wound the heart: the 5-fluorouracil and oxaliplatin used against Lynch-associated colorectal cancer cause coronary vasospasm and cardiotoxicity that can precipitate cardiac dysfunction."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong cancer surveillance weighs on the mind: living with a high inherited risk of multiple cancers, frequent colonoscopies and the threat of new diagnoses gives Lynch syndrome carriers a substantial burden of depression."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Constant cancer surveillance breeds worry: the lifelong colonoscopic and multi-organ screening and inherited multi-cancer risk of Lynch syndrome foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemotherapy injures the nerves: the oxaliplatin used for the colorectal cancers of Lynch syndrome causes a cold-triggered, chronic peripheral neuropathy with neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from chemotherapy for the colorectal and other cancers of Lynch syndrome can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It targets the upper urinary tract: Lynch syndrome causes urothelial carcinoma of the ureter and renal pelvis, a recognised part of its tumour spectrum requiring urinary surveillance."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Risk-reducing and cancer surgery means many wounds: colectomy and prophylactic hysterectomy-oophorectomy in Lynch syndrome leave abdominal wounds and anastomoses that must heal."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Immunotherapy for its MSI-high tumours inflames glands: because Lynch cancers are mismatch-repair-deficient, checkpoint inhibitors are highly effective but trigger endocrine irAEs like thyroiditis and hypophysitis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the brain in the Turcot variant: Lynch carriers have a raised risk of glioblastoma and other brain tumours, and biallelic constitutional MMR deficiency causes childhood brain tumours."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its immunotherapy can inflame the lungs: checkpoint inhibitors, highly effective against its MSI-high cancers, can cause immune-related pneumonitis as an adverse effect."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its immunotherapy can inflame joints and muscle: checkpoint-inhibitor therapy for Lynch-related cancers can trigger inflammatory arthritis and myositis among its immune-related adverse events."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Aspirin lowers its cancer risk: the CAPP2 trial showed regular aspirin substantially reduces colorectal cancer in Lynch syndrome, now offered as chemoprevention."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet supports the at-risk bowel: a high-fibre diet aids colorectal health, complementing the intensive colonoscopic surveillance that Lynch syndrome requires."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment can reach the heart: chemotherapy for Lynch-related cancers, including platinum and fluoropyrimidines, carries cardiotoxic and thrombotic risk."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Mismatch-repair loss makes it immunotherapy-sensitive: Lynch tumours are microsatellite-unstable with a high mutational burden, responding dramatically to PD-1 inhibitors like pembrolizumab, which has tissue-agnostic approval for MSI-high cancer."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo with a twist: Lynch-associated colorectal cancers are treated with chemotherapy, though MSI-high tumours respond poorly to fluorouracil alone, favouring immunotherapy."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "The two great hereditary cancer syndromes: Lynch syndrome (mismatch-repair loss) and Li-Fraumeni (germline TP53) are the archetypal autosomal-dominant multi-cancer predispositions with distinct mechanisms and spectra."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Two DNA-repair colorectal syndromes: Lynch arises from dominant mismatch-repair loss causing microsatellite instability, while MUTYH-associated polyposis comes from recessive base-excision-repair loss causing G:C→T:A mutations—different defects, overlapping colorectal risk."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Its ovarian cancers favour a histology: Lynch-associated ovarian tumours are predominantly endometrioid and clear-cell rather than the high-grade serous cancers of BRCA carriers, so clear-cell ovarian cancer in a young woman can flag mismatch-repair deficiency."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Why its tumours invite immunotherapy: mismatch-repair-deficient Lynch cancers accumulate frameshift neoantigens and draw dense lymphocytic infiltrates with germinal-centre-like tertiary lymphoid structures—the immune richness behind their response to checkpoint blockade."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "The recessive extreme (CMMRD): biallelic loss of a Lynch mismatch-repair gene causes constitutional MMR deficiency, a childhood syndrome with brain tumours including medulloblastoma and glioma."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "CMMRD leukaemia: constitutional mismatch-repair deficiency from biallelic Lynch-gene loss predisposes children to leukaemia and lymphoma alongside the brain and gut tumours."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatobiliary spread: Lynch raises the risk of biliary-tract cancer, and mismatch-repair-deficient tumours metastasise to the liver, seeding the hepatic lobule."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "When both copies fail: constitutional mismatch-repair deficiency (biallelic Lynch genes) causes a childhood-cancer syndrome with café-au-lait macules that closely mimics neurofibromatosis type 1, a key diagnostic pitfall."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "A different polyposis pathway: Peutz-Jeghers (STK11) produces hamartomatous gut polyps and high GI cancer risk, contrasting with the mismatch-repair-driven adenoma-carcinoma route of Lynch in the differential of hereditary GI cancer."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Overlapping endometrial and colon risk: Cowden syndrome (PTEN) independently raises the risk of endometrial and colorectal cancer, a PTEN/mTOR-driven syndrome to distinguish from Lynch in women with these tumours."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "A distinct pathway: unlike chromosomally unstable colorectal cancers driven by p53 loss, Lynch (MSI) tumours arise from mismatch-repair failure and frameshift mutations, often retaining wild-type p53."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Hypermutated activation: the mismatch-repair-deficient tumours of Lynch syndrome accumulate activating PIK3CA and frameshift mutations across their hypermutated genomes."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: like other cancers, Lynch-associated tumours reactivate TERT to maintain telomeres, sustaining the unlimited division enabled by mismatch-repair loss."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT activation: frameshift and PIK3CA mutations in the hypermutated Lynch tumours activate AKT, driving growth alongside the mismatch-repair defect."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Wnt-driven oncogene: APC/Wnt activation common in Lynch colorectal cancers upregulates MYC, driving the proliferation of these mismatch-repair-deficient tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in growing Lynch-associated tumours drives the angiogenesis that supports their expansion, complementing their high immunogenicity."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immunogenic MSI tumours: the frameshift neoantigens of mismatch-repair-deficient Lynch tumours provoke a brisk IFN-γ-driven T-cell infiltrate, the basis of their exceptional response to checkpoint immunotherapy."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Tumour-suppressor loss: CDKN2A inactivation accompanies progression of Lynch-associated adenomas to carcinoma, releasing the cell-cycle brake in these mismatch-repair-deficient tumours."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into Lynch tumours, part of the rich immune microenvironment that shapes their response to immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate immune sensing: the microsatellite-instable tumours of Lynch accumulate cytosolic DNA from their genomic instability, engaging cGAS-STING — an innate-immune arm of the immunogenicity behind their dramatic checkpoint-inhibitor response."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: the frameshift neoantigens of dMMR Lynch tumours drive CD8 T cells to deploy perforin against them, the cytotoxic killing that checkpoint blockade unleashes in microsatellite-instable cancers."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: CXCR4-CXCL12 signalling drives the metastasis of the colorectal, endometrial and other Lynch-spectrum cancers, the chemokine route to spread when these tumours are not caught early by surveillance."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Aspirin chemoprevention: the CAPP2 trial showed that long-term aspirin, by inhibiting COX-derived prostaglandins, substantially reduces colorectal-cancer incidence in Lynch syndrome, an evidence-based chemoprevention recommended for carriers."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Endometrial cancer: endometrial cancer is the commonest extracolonic Lynch tumour and often the first to present in women, an oestrogen-responsive cancer for which risk-reducing hysterectomy is offered once childbearing is complete."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Neoantigen vaccine: the mismatch-repair deficiency of Lynch tumours generates recurrent frameshift-peptide neoantigens, the basis for shared cancer-prevention vaccines being trialled to prime antibody and T-cell immunity before tumours arise."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK driver: KRAS and BRAF (both already mapped) signal through MAPK-ERK in Lynch-associated colorectal cancer, with BRAF testing used to distinguish sporadic MSI-high tumours from true Lynch syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) active in the colorectal and endometrial cancers of Lynch syndrome."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "Wnt initiation: APC inactivation activates Wnt/β-catenin (mapped) to initiate the adenoma-carcinoma sequence in Lynch colorectal cancer, on which the mismatch-repair defect then layers rapid mutation accumulation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Immunogenic interferon response: the high neoantigen load of MMR-deficient Lynch tumours drives an interferon-rich microenvironment signalling through JAK-STAT (IFN-γ already mapped), underlying their responsiveness to checkpoint immunotherapy."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota inflammation: gut-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides an inflammatory cofactor in the colorectal carcinogenesis of Lynch syndrome."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cancer progression: loss of the RB1-E2F checkpoint cooperates with mismatch-repair deficiency in the progression of Lynch-syndrome adenomas to carcinoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "MMR-deficient tumours frequently acquire TGFBR2 frameshift mutations that cripple TGF-β-SMAD signalling (TGF-β mapped), removing a growth-suppressive brake in Lynch-syndrome cancers."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates tumour-cell adhesion and the immune microenvironment of the colorectal and endometrial cancers of Lynch syndrome."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) cooperates with mismatch-repair deficiency in Lynch-syndrome tumorigenesis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "The high neoantigen load of mismatch-repair-deficient Lynch tumours drives IFN-STAT1 signalling, underlying their marked responsiveness to checkpoint immunotherapy."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (CDKN2A and RB1 already mapped) drives the cell-cycle progression of the colorectal and endometrial cancers of Lynch syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by PI3K-AKT signalling, is lost in the malignant progression of Lynch-syndrome tumours."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the mismatch-repair-deficient cancers of Lynch syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory, neoantigen-rich microenvironment of the MSI-high tumors of Lynch syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of the colorectal and endometrial cancers of Lynch syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the progression of the MSI-high tumors of Lynch syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation, alongside MLH1 promoter hypermethylation, participates in the epigenetic component of the mismatch-repair-deficient tumors of Lynch syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the hypermutated MSI-high tumor cells of Lynch syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of Lynch syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immune microenvironment of the MMR-deficient tumors of Lynch syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Lynch syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the cancers of Lynch syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of Lynch syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Lynch syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Lynch syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of Lynch syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of Lynch syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "MSI neoantigens: mismatch-repair deficiency generates abundant frameshift neoantigens presented on MHC, making Lynch tumours highly immunogenic and checkpoint-responsive (PD-1/CTLA-4 already mapped), and the rationale for shared frameshift-neoantigen vaccines."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2-driven proliferation of the tumour-infiltrating T cells underlies the strong immune response to the microsatellite-instable cancers of Lynch syndrome, the basis of their responsiveness to immunotherapy."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 antitumour immunity: the microsatellite-instable tumours of Lynch syndrome elicit a brisk Th1 and cytotoxic infiltrate, and IL-12-driven Th1 polarisation (interferon-gamma already mapped) is part of the antitumour immunity that immunotherapy amplifies."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Occult bleeding: the right-sided colorectal cancers of Lynch syndrome bleed chronically, and the resulting iron-deficiency anaemia lowering haemoglobin is often the sign that brings the tumour, or the syndrome, to attention."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th1 orchestration: CD4 helper T cells polarised to Th1 (IL-12 and interferon-gamma already mapped) coordinate the brisk antitumour infiltrate of the microsatellite-instable Lynch cancers, supporting the CD8 (already mapped) response that immunotherapy amplifies."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive counter-regulation: IL-10 in the tumour microenvironment restrains the strong Th1 and cytotoxic response (PD-1 already mapped) to the microsatellite-instable Lynch tumours, one brake on the immunity that checkpoint blockade releases."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage counterbalance: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) that counterbalances the strong Th1 infiltrate (interferon-gamma already mapped) of the microsatellite-instable Lynch tumours."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile acids and chemoprevention: dietary fat and the bile acids derived from cholesterol promote colonic carcinogenesis, and this modifiable influence, alongside aspirin (prostaglandins already mapped), informs the risk reduction in Lynch syndrome."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic colonic inflammation generates oxidative stress, to which xanthine oxidase contributes, adding DNA damage that, atop the mismatch-repair defect (already mapped), speeds the carcinogenesis of Lynch syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the Lynch-associated cancers, balanced against the strong anti-tumour immunity of the MSI-high tumours."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and cancer risk: the adipokine leptin links obesity to colorectal carcinogenesis (Wnt already mapped), a modifiable factor modulating the penetrance of the cancer risk in Lynch syndrome."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Dietary chemoprevention: dietary calcium reduces colorectal adenoma recurrence, binding the bile acids (cholesterol already mapped) that promote carcinogenesis, a modifiable factor in the risk reduction of Lynch syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity-cancer adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related modifiable colorectal-cancer risk of Lynch syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related modifiable cancer risk of Lynch syndrome."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MSI-high immunogenicity: the MSI-high, MMR-deficient (already mapped) Lynch tumours activate the cGAS-STING (already mapped) pathway to produce the type-I interferon that drives the immunogenicity and the checkpoint (PD-1 already mapped) response."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Peritumoral eosinophilia: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the prognostically favourable peritumoral infiltrate of the MSI-high Lynch tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23/Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune infiltrate implicated in the colorectal carcinogenesis of Lynch syndrome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell infiltrate: the mast cells and histamine are part of the dense immune microenvironment of the MSI-high (MMR-deficient already mapped) Lynch tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell infiltrate: the mast cells (the histamine already mapped source) populate the dense immune microenvironment of the MSI-high Lynch tumours."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophil infiltrate: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are part of the highly immune-infiltrated MSI-high Lynch tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the Lynch tumours."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in immunogenic tumours: the complement C5 and its C5a (with C3 already mapped) shape the innate inflammation of the highly immune-infiltrated MSI-high Lynch tumours."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Chemoprevention vitamin: the vitamin D status modulates the colorectal-cancer (already mapped) risk and, with aspirin, is part of the chemoprevention landscape of Lynch syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the antioxidant micronutrient dimension studied in the colorectal-cancer (already mapped) chemoprevention of Lynch syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the immune-rich stroma of the MSI-high Lynch-syndrome tumours."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the MMR-deficient Lynch tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack against the highly immunogenic MSI-high tumours."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Bleeding iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia from the occult gastrointestinal blood loss that often heralds the colorectal cancer (already mapped) of Lynch syndrome."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Colorectal mucosal alarmin: TSLP from the intestinal epithelium (already mapped) activates dendritic cells (already mapped) and mast cells (already mapped), shaping the mucosal type-2 immune environment of the MSI-H colorectal and endometrial Lynch-spectrum cancers."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Pericolorectal stroma: periostin, a SMAD4-downstream ECM protein (SMAD4 already mapped), drives cancer-associated fibroblast activation in the Lynch colorectal stroma; elevated tumour-adjacent periostin correlates with invasiveness of Lynch-spectrum cancers."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Inflammation-pain axis: bradykinin activates B2 receptors in the colorectal mucosa, amplifying prostaglandin (already mapped) and NF-kB (already mapped) signalling in the Lynch tumour microenvironment and contributing to neuropathic pain (already mapped) and inflammatory flares."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: C1-INH controls the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) that contribute to anti-tumour immunity against the highly immunogenic MSI-H Lynch-spectrum colorectal and endometrial cancers."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia-of-cancer correction: erythropoietin, rising in response to the anaemia of chronic disease (already mapped) and iron-deficiency anaemia (already mapped) from occult GI bleeding, guides transfusion decisions in Lynch colorectal cancer chemotherapy (already mapped)."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Anti-colorectal-cancer melatonin: melatonin suppresses Wnt/β-catenin (wnt-beta-catenin already mapped) and NF-kB (already mapped) in Lynch MMR-deficient colorectal cells, reducing proliferation and potentiating the anti-tumour immune response of MSI-H tumours."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-MMR axis: testosterone, via androgen receptor on Lynch MMR-deficient colorectal and endometrial cells (endometrial cancer already mapped), modulates MMR gene expression and promotes the androgen-driven tumour proliferation contributing to sex-dependent Lynch cancer risk."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Gut neuroendocrine modulation: serotonin from enterochromaffin cells in Lynch MMR-deficient colorectal mucosa regulates bowel motility and mucosal immune responses (already mapped) that shape the MSI-H tumour microenvironment of Lynch syndrome."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Tumour-promoting prolactin: prolactin, via PRL-R on Lynch MMR-deficient endometrial (already mapped) and colorectal cells, activates JAK2/STAT5 proliferative signalling and contributes to the endometrial cancer penetrance of Lynch syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Lynch oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Lynch syndrome."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Lynch vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the tumour; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Lynch syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Lynch iodine: iodine, via thyroid hormone biosynthesis, modulates intestinal epithelial (already mapped) and macrophage (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Lynch syndrome."
---

# Lynch Syndrome

## Overview

**Lynch syndrome** (historically called hereditary nonpolyposis colorectal cancer, HNPCC) is the most common inherited cancer predisposition syndrome in adults, caused by germline pathogenic variants in the **DNA mismatch repair (MMR) genes**: **MLH1** (~50%), **MSH2** (~31%), **MSH6** (~13%), and **PMS2** (~6%), plus EPCAM 3' deletions that epigenetically silence MSH2 (~2%). Lynch syndrome confers markedly elevated lifetime risks for colorectal, endometrial, ovarian, gastric, urothelial, and other cancers. Lynch syndrome tumors are uniformly **deficient MMR (dMMR)** and **microsatellite instability-high (MSI-H)**, generating abundant frameshift neoantigens and constitutive PD-L1 expression — making Lynch tumors exquisitely sensitive to immune checkpoint blockade. Pembrolizumab (any dMMR/MSI-H solid tumor, 2020) and dostarlimab (dMMR endometrial, 2021) are FDA-approved, representing the first tissue-agnostic cancer therapy approval. Estimated prevalence: 1 in 280 individuals in the general population carry a Lynch syndrome pathogenic variant, most undiagnosed [^bonadona-2011-lynch-risks] [^lynch-2015-lynch-review].

**Epidemiology:**
- Prevalence: ~1/280 in general population; ~1/35-40 among all CRC patients; ~1/50-70 among all endometrial cancer patients
- Inheritance: autosomal dominant; 50% transmission rate per child of carrier; penetrance is incomplete and gene-specific
- Age of onset: CRC median age ~44-50 years (vs ~68 years sporadic); younger onset with MLH1/MSH2 vs MSH6/PMS2
- Proportion of CRC attributable to Lynch: ~3-5% of all CRC; ~10-15% of all early-onset CRC (< age 50)
- Proportion of endometrial cancer: ~3% of all endometrial cancer; higher in MSI-H endometrial (~25-30%)

**Gene-specific cancer risk summary (Bonadona 2011):** [^bonadona-2011-lynch-risks]

| Cancer | MLH1 (80 yr cumulative) | MSH2 (80 yr cumulative) | MSH6 | PMS2 |
|---|---|---|---|---|
| Colorectal | 41% | 48% | 10-22% | <15% |
| Endometrial | 54% | 21% | 16-26% | <15% |
| Ovarian | 20% | 24% | <1% | <1% |
| Gastric | 13% | 13% | <5% | <5% |
| Urothelial | ~4% | ~12% | <5% | <1% |
| Pancreatic | ~4% | ~5% | <3% | <1% |
| Brain (Turcot) | ~1-3% | ~1-2% | rare | rare |

## Structure

### MMR complex architecture in Lynch syndrome

**The four MMR proteins:**
- **MLH1**: obligate component of MutLα (MLH1-PMS2) and MutLβ (MLH1-PMS1) and MutLγ (MLH1-MLH3); MutLα is the primary repair-competent complex; PMS2 endonuclease nicks the daughter strand, enabling ExoI-mediated excision; MLH1 is the scaffold partner of all MutL complexes — MLH1 LOF eliminates all three
- **MSH2**: obligate scaffold for MutSα (MSH2-MSH6) and MutSβ (MSH2-MSH3); MutSα (base-base mismatches, +1 IDLs) and MutSβ (+2 to +8 IDLs) both require MSH2
- **MSH6**: mismatch-contacting subunit of MutSα; F432 Phe-loop directly contacts mispaired base; MSH6 protein is unstable without MSH2 → MSH2 LOF → MSH6 co-loss by IHC
- **PMS2**: endonuclease in MutLα; requires MLH1 for stability → PMS2 loss with MLH1 LOF; isolated PMS2 loss → PMS2 pathogenic variant

**MMR mechanism:**
1. Replication slippage at microsatellite → single base mismatch or IDL
2. MutSα/MutSβ binds mismatch → ATP-loaded sliding clamp
3. MutLα recruited via MSH2-MLH1 protein interaction
4. PCNA (RFC) → MutLα PMS2 endonuclease → nicks newly synthesized strand
5. Exonuclease I (ExoI) degrades from nick to mismatch
6. RPA + Polδ + PCNA → gap resynthesis → Ligase I sealing

**EPCAM deletion mechanism:**
EPCAM gene (2p21) is directly upstream of MSH2; 3' end deletions of EPCAM → abnormal transcriptional read-through → EPCAM-MSH2 fusion RNA → CpG island methylation of MSH2 promoter in epithelial tissues → MSH2 silencing; detected by MLPA or aCGH (not NGS sequencing); MSH2 and MSH6 IHC: both lost (same as germline MSH2 mutation)

### MSI and TMB in Lynch tumors

**Microsatellite instability:**
dMMR Lynch tumors accumulate frameshift mutations at coding microsatellite sequences (mononucleotide repeats in TGFBR2, MSH3, ACVR2, BAX, RIZ, and others) → truncated/non-functional proteins from these secondary "passenger" TSG hits; Bethesda panel (5 microsatellite loci): MSI-H = ≥2 unstable; modern NGS: MSI score computed from thousands of microsatellite loci simultaneously (tumor-only or matched) — more sensitive and specific

**TMB landscape:**
Lynch CRC: TMB ~50-100 mut/Mb; Lynch endometrial: TMB ~100-200 mut/Mb; neoantigen burden: hundreds to thousands of novel peptides from frameshift mutations → MHC-I/II presentation → T cell priming; TILs (tumor-infiltrating lymphocytes): marked lymphocytic infiltrate in Lynch CRC (Crohn-like reaction) → prognostic (better OS stage-for-stage vs MSS CRC); PD-L1 expression: IFN-γ from TILs → JAK-STAT → PD-L1 → adaptive immune resistance

## Function

### Carcinogenesis in Lynch syndrome

**Two-hit model:**
Lynch syndrome follows Knudson's two-hit tumor suppressor paradigm:
1. **First hit**: germline pathogenic variant (one allele non-functional at birth)
2. **Second hit**: somatic LOH (loss of heterozygosity), somatic mutation, or epigenetic silencing of the remaining wild-type allele → complete dMMR in tumor cell
- MLH1 promoter methylation on the remaining wild-type allele: ~30% of Lynch MLH1-mutant tumors acquire this as the second hit
- Somatic LOH at 2p21 (MSH2 locus) in Lynch MSH2 tumors
- Missense pathogenic variant + somatic frameshift = compound heterozygosity (rare second hit)

**Tumor type specificity:**
Lynch syndrome cancers predominantly arise from tissues with high MMR demand:
- Colorectal mucosa: highest replication rate of any epithelium → highest microsatellite mutation rate → CRC most frequent
- Endometrial glands: rapid hormonal cycling → high replication → second most common
- Gastric mucosa, urothelium: epithelial cycling
- Glioblastoma (Turcot variant, MLH1): brain tumors in Lynch — rare; MLH1 LOF → GBM-like tumor with MSI-H

**Lynch vs sporadic MSI-H:**
Important distinction:
- **Lynch MSI-H**: germline MMR gene mutation → constitutional dMMR → younger age at diagnosis; MMR IHC loss in normal colon crypts (if testing is performed)
- **Sporadic MSI-H**: MLH1 promoter methylation (somatic, both alleles) → acquired dMMR in that tumor only; MSH2 LOF almost never causes sporadic MSI-H; older age, predominantly right colon, BRAF V600E mutation (~50% sporadic MSI-H CRC); MLH1 methylation in sporadic MSI-H → MLH1/PMS2 IHC co-loss
- IHC pattern distinguishes:
  - MLH1 + PMS2 co-loss → reflexive MLH1 methylation PCR → if methylated = sporadic; if unmethylated = germline MLH1 or MSH2 variant (exceptional)
  - MSH2 + MSH6 co-loss → MSH2 or EPCAM germline (essentially never sporadic)
  - MSH6 loss alone → MSH6 germline; isolated PMS2 → PMS2 germline

## Pathology

### Diagnosis and universal tumor testing

**Universal MMR testing (recommended by NCCN, ACS, ASCCP):**
All newly diagnosed CRC and endometrial cancers should undergo MMR IHC (MLH1, PMS2, MSH2, MSH6) or tumor MSI testing; this identifies Lynch syndrome patients AND guides immunotherapy (dMMR/MSI-H → pembrolizumab first-line) and adjuvant therapy decisions (MSI-H stage II CRC: no 5-FU benefit); IHC more widely available; MSI PCR or NGS confirms

**Germline testing criteria:**
Individuals with dMMR/MSI-H tumor + age <50 (or proximal colon + positive family history) → germline MMR gene sequencing + deletion analysis (MLPA); Amsterdam II criteria: 3 relatives with Lynch-associated cancer, 2 successive generations, 1 patient <50 at diagnosis — now largely replaced by universal tumor testing as the trigger; Bethesda guidelines (revised) — similarly superseded by universal testing in guidelines

**Clinical genetic evaluation:**
- Probands: full MMR gene panel (MLH1, MSH2, MSH6, PMS2) + EPCAM deletion analysis
- First-degree relatives: cascade testing for identified variant
- Variant of uncertain significance (VUS): functional assay, co-segregation with disease in family, computational tools (align-GVGD, Bayesian methods)
- Pathogenic MMR variant confirmed → surveillance + prophylactic surgery discussion

### Treatment

**Surveillance protocols (NCCN):**
CRC surveillance:
- MLH1/MSH2 carriers: colonoscopy every 1-2 years from age 20-25
- MSH6 carriers: colonoscopy every 1-2 years from age 25-30
- PMS2 carriers: colonoscopy every 1-3 years from age 30-35

Endometrial/gynecologic:
- Annual endometrial sampling + TVUS from age 30-35
- Risk-reducing hysterectomy + bilateral salpingo-oophorectomy (RRBSO) after childbearing: reduces endometrial and ovarian cancer risk by ~85%; timing: ~35-40 years, after surveillance period
- RRBSO discussion: major quality-of-life implications (surgical menopause); individualized decision

Urothelial (especially MSH2):
- Annual urinalysis + urine cytology from age 25-30
- Cystoscopy: reserved for abnormal cytology or hematuria; no evidence for routine cystoscopy

**Chemoprevention:**
- **Aspirin**: CAPP2 trial (600 mg/day × 2 years): Lynch syndrome patients; 10-year follow-up: HR for CRC 0.63 (statistically significant at long-term follow-up); CRC incidence reduction ~50% for polypectomy interval cohort; mechanism: COX-2/prostaglandin pathway modulation; NCCN recommends aspirin discussion for Lynch syndrome CRC prevention
- Aspirin dose debate: ongoing CAPP3 trial compares 100 mg vs 300 mg vs 600 mg in Lynch; current recommendation based on 600 mg CAPP2 data

**Immunotherapy in Lynch tumors:**
First-line metastatic CRC (dMMR/MSI-H): [^lynch-2015-lynch-review]
- **KEYNOTE-177** (pembrolizumab vs FOLFOX/FOLFIRI ± bevacizumab): mPFS 16.5 vs 8.2 months (HR 0.60); OS HR 0.74; pembrolizumab first-line standard for dMMR/MSI-H mCRC since 2020
- **CheckMate 142** (nivolumab + ipilimumab): ORR 55%; mPFS 12.4 months; FDA-approved second-line dMMR/MSI-H mCRC
- **Any dMMR/MSI-H solid tumor** (KEYNOTE-158): pembrolizumab ORR 36% (range 20-57% across tumor types); FDA-approved June 2020 tissue-agnostic indication

Endometrial (dMMR):
- **RUBY Phase 3** (dostarlimab + carboplatin/paclitaxel): dMMR/MSI-H subgroup: PFS HR 0.28; FDA-approved November 2023 for first-line dMMR advanced endometrial cancer
- **KEYNOTE-868** (pembrolizumab + carboplatin/paclitaxel): similar benefit in dMMR advanced endometrial; FDA-approved 2023

**Adjuvant chemotherapy decisions:**
MSI-H stage II CRC: adjuvant 5-FU/leucovorin does NOT improve OS (may be harmful); mechanism: functional MMR required for 5-FU-induced mismatch-mediated apoptosis; MSS stage II CRC benefits from 5-FU; MSI-H stage III CRC: FOLFOX preferred (oxaliplatin mechanism is MMR-independent); important biomarker-directed adjuvant decision

**Prognosis:**
- Lynch CRC stage-for-stage: better 5-year OS than MSS CRC (Lynch ~15-20% OS advantage per stage); high TIL density → favorable immune microenvironment
- Lynch endometrial cancer: generally favorable (MSI-H endometrioid type); early-stage predominance
- MSI-H dMMR tumors: paradoxically best immunotherapy responders among all solid tumors

## Connections

- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — Germline MSH2 mutation causes ~31% of Lynch syndrome; MSH2 IHC loss indicates MSH2 or EPCAM mutation; MSH2-MSH6 (MutSα) detects base-base mismatches; MSH2 LOF → MSI-H → elevated TMB → immunotherapy sensitivity in Lynch tumors
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MLH1 germline mutation causes ~50% of Lynch syndrome; MLH1-PMS2 (MutLα) recruited by MutS complexes → MMR strand excision; MLH1 promoter methylation causes sporadic MSI-H CRC (not Lynch); MLH1 + PMS2 IHC co-loss indicates MLH1 mutation or methylation
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — dMMR Lynch tumors are highly immunogenic → MSI-H → elevated TMB → PD-L1 high; pembrolizumab FDA-approved for dMMR/MSI-H solid tumors (KEYNOTE-158, 2020); dostarlimab for dMMR endometrial; Lynch tumors were the first tissue-agnostic immunotherapy indication
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — Lynch CRC: most common Lynch-associated cancer; lifetime risk with MLH1/MSH2: ~40-80%; proximal colon predominance, mucinous histology, tumor-infiltrating lymphocytes; Lynch CRC has good prognosis; colonoscopy from age 25-30 recommended
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Endometrial cancer is the second most common Lynch cancer and the sentinel tumor in many women (54% with MLH1); usually dMMR/MSI-H endometrioid; risk-reducing hysterectomy plus BSO after childbearing is offered, and dostarlimab (RUBY) is approved for advanced dMMR disease.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Lynch confers a ~13% lifetime gastric cancer risk (MLH1/MSH2) — the main hereditary cause of intestinal-type (not diffuse) gastric cancer; these dMMR/MSI-H tumors have high TIL density, contrasting with CDH1-driven diffuse HDGC; upper endoscopy is offered to carriers.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Colorectal mucosa is the highest-turnover epithelium, so its microsatellites accumulate the most replication errors when MMR fails — why CRC is the commonest Lynch cancer; Lynch CRC favors the proximal colon, is mucinous with brisk lymphocytic infiltrate, screened from age 20-25.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Lynch and juvenile polyposis are both dominant hereditary colorectal cancer syndromes but opposite: Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas, JPS is TGF-β/BMP loss making many hamartomatous polyps — repair defect versus stromal overgrowth.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Lynch and FAP are the two major hereditary colorectal cancer syndromes but differ starkly: FAP (germline APC) carpets the colon with thousands of adenomas and near-100% cancer risk, while Lynch (MMR genes) makes few polyps but fast MSI-high tumors via accelerated mutation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Lynch tumors are the prototype of immunotherapy response: mismatch-repair deficiency generates thousands of frameshift neoantigens that draw dense cytotoxic CD8+ T cells, so dMMR/MSI-H cancers respond strongly to anti-PD-1 — the basis of pembrolizumab's tissue-agnostic approval.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Ovarian cancer is part of the Lynch syndrome tumor spectrum: mismatch-repair deficiency raises the lifetime risk of (usually endometrioid or clear-cell) ovarian cancer alongside endometrial and colorectal cancer, so risk-reducing salpingo-oophorectomy is offered to carriers.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Lynch syndrome extends to the urinary tract: MSH2 carriers especially face raised risk of upper-tract urothelial carcinoma (renal pelvis, ureter) and bladder cancer, so urine surveillance is considered; these MSI-high tumors respond to checkpoint immunotherapy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Lynch syndrome cancers are the paradigm of immunotherapy-responsive tumors: mismatch-repair deficiency generates a high microsatellite-instability mutational load and abundant neoantigens, making MSI-high/dMMR tumors—wherever they arise—exquisitely sensitive to PD-1 blockade.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Pancreatic cancer is part of the Lynch spectrum: mismatch-repair deficiency raises pancreatic adenocarcinoma risk, and rare MMR-deficient pancreatic tumors are hypermutated and respond to checkpoint therapy—unlike most pancreatic cancers, which resist immunotherapy.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Cholangiocarcinoma belongs to the Lynch tumor spectrum: mismatch-repair loss predisposes to biliary-tract cancers, and like other Lynch tumors these are microsatellite-unstable and hypermutated—candidates for checkpoint immunotherapy exploiting their neoantigens.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Lynch syndrome can cause brain tumors as Turcot syndrome: mismatch-repair loss predisposes to gliomas including glioblastoma, and biallelic MMR deficiency gives childhood high-grade gliomas—linking a DNA-repair defect in the gut to tumors in the brain.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Lynch syndrome's Muir-Torre variant shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so a sebaceous skin tumor can be the first clue prompting Lynch testing and colon surveillance.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Lynch syndrome raises small-bowel cancer risk: mismatch-repair deficiency predisposes to small-intestinal adenocarcinoma—rare in the general population—so surveillance and a low threshold for investigating GI symptoms extend beyond the colon.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Lynch tumors still travel the Wnt road to cancer: mismatch-repair loss accelerates mutation, but colorectal carcinogenesis still typically requires Wnt/beta-catenin activation via APC—so MMR failure speeds, rather than replaces, the adenoma-carcinoma sequence.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Lynch syndrome predisposes across the digestive system: mismatch-repair loss most often causes colorectal cancer but also stomach, small-bowel, pancreatic and biliary tumors, so broad GI surveillance anchors management of the commonest hereditary cancer syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Lynch syndrome heavily affects the female reproductive system: endometrial cancer rivals colorectal as the most common Lynch tumor and is often the sentinel cancer, and ovarian cancer risk is raised too—so gynecologic surveillance and risk-reducing surgery matter.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The Muir-Torre variant of Lynch syndrome shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so these uncommon skin tumors can be the first clue prompting Lynch genetic testing.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Lynch syndrome reaches the urinary tract above the bladder: MMR deficiency raises the risk of urothelial cancer in the renal pelvis and ureter, so surveillance and any blood in the urine prompt imaging of the upper tracts, not just cystoscopy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Prostate cancer is a lower-penetrance Lynch tumor: MMR-gene carriers face a modestly increased, sometimes more aggressive prostate cancer, so family history of Lynch is weighed alongside PSA in deciding screening for these men.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Lynch tumors are immunotherapy-responsive because they are hypermutated: MMR loss spawns countless neoantigens that dendritic cells present to prime T cells, explaining why checkpoint blockade works so well in mismatch-repair-deficient cancers.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — A BRAF test separates Lynch from look-alike sporadic cancers: sporadic MSI-high colon tumors usually carry a BRAF V600E mutation, while Lynch tumors are BRAF-wild-type, so BRAF status is a key reflex test before diagnosing the inherited syndrome.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Lynch tumors' flood of mutations alerts NK cells: mismatch-repair failure makes hypermutated cells display stress signals and odd peptides that natural killer cells (and T cells) can attack—part of why these cancers are so immunotherapy-sensitive.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Lynch (MSI-high) tumors often form B-cell-rich lymphoid structures: clusters of B cells and tertiary lymphoid organs inside these hypermutated cancers help mount the immune response, and their presence predicts better checkpoint-therapy results.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Lynch tumors often knock out the TGF-beta brake: the mismatch-repair defect causes frameshift mutations in TGFBR2, a coding microsatellite, so the colorectal cancers escape TGF-beta's growth restraint—a signature lesion of MSI-high disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Lynch syndrome can reach the brain in its Turcot variant: mismatch-repair loss raises the risk of gliomas including glioblastoma, so brain tumors join the colorectal and endometrial cancers in the syndrome's spectrum.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Even Lynch's hot tumors recruit regulatory T cells: the hypermutated, neoantigen-rich cancers draw a strong immune response, but Tregs in the infiltrate restrain it—part of why checkpoint blockade, which lifts that brake, works so well here.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Lynch colorectal tumors bleed iron away: the cancer oozes blood into the gut, so an unexplained iron-deficiency anemia can be the first clue that prompts the colonoscopy which finds it.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Lynch cancers spring from the gut's epithelium: with mismatch repair broken, mutations pile up in the colonic and endometrial lining, so the epithelium turns malignant faster than in sporadic disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Lynch's hypermutated tumors draw macrophages: the neoantigen-rich cancers attract a dense immune infiltrate including macrophages, part of the inflamed microenvironment behind their strong response to immunotherapy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Lynch is managed by light: frequent colonoscopy from young adulthood catches and removes the fast-arising colorectal cancers, the surveillance that most reduces deaths in carriers.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Lynch raises gastric cancer risk: mismatch-repair-deficient stomach cancers occur, especially in MLH1 and MSH2 carriers, so upper endoscopy joins surveillance in high-incidence regions.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Lynch's Turcot variant strikes the brain: mismatch-repair loss raises the risk of gliomas, extending the syndrome's reach to the neurons of the central nervous system.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Lynch syndrome cannot proofread its DNA: losing a mismatch-repair gene lets tiny errors accumulate at repetitive sequences — microsatellite instability — so its tumors carry a huge mutation load that makes them strikingly responsive to immunotherapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Lynch reaches the liver and bile ducts: it raises the risk of cholangiocarcinoma, and its colorectal cancers spread there, so the liver is both a primary site and the commonest destination of its tumors.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Inheriting two faulty copies is far worse: constitutional mismatch-repair deficiency, the biallelic form, causes childhood leukemias and lymphomas, the marrow joining the syndrome's cancer spectrum in its most severe variant.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Mismatch-repair loss is read off the slide: an antibody panel staining for MLH1, MSH2, MSH6, and PMS2 by immunohistochemistry shows which protein has gone missing in the tumor, the first-line screen that flags Lynch before confirmatory germline sequencing.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Slow tumor bleeding shows up in the red cells: a Lynch colorectal or gastric cancer often declares itself first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic occult blood loss that should prompt early colonoscopy.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas falls within the spectrum: Lynch raises the lifetime risk of pancreatic cancer several-fold, and because such tumors are mismatch-repair-deficient and MSI-high, they are among the rare pancreatic cancers that can respond to checkpoint immunotherapy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Aspirin earns its place in Lynch through platelets: the CAPP2 trial showed daily aspirin sharply cuts colorectal cancer in carriers, an effect tied partly to blocking platelet COX-1 and the tumor-promoting signals activated platelets release.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Lynch tumors teem with immune cells: their mismatch-repair defect spawns countless neoantigens that draw in B cells and plasma cells forming tertiary lymphoid structures, a brisk immune response that underlies their striking sensitivity to checkpoint therapy.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — The mutation count runs high: mismatch-repair failure lets mutations accumulate across genes including KRAS, shaping the tumor's behavior and, with RAS status, guiding which targeted drugs can be added to its treatment.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — The hypermutated tumors are immunotherapy magnets: mismatch-repair loss spawns countless neoantigens, so blocking CTLA-4 alongside PD-1 can unleash a strong T-cell attack, making Lynch cancers among the most checkpoint-responsive of all solid tumors.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Two great hereditary-cancer syndromes sit side by side: where BRCA-driven HBOC fails DNA double-strand repair, Lynch fails mismatch repair — both flagged by family history, but each needing its own gene panel, surveillance plan, and tumor-specific therapies.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — The brain is on the tumor list too: in the Turcot variant, mismatch-repair failure drives gliomas arising from astrocytes, so the same defect that floods the colon with mutations can also seed aggressive brain tumors.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Occult bleeding announces the colon cancer: a Lynch-associated colorectal tumor often bleeds slowly, so unexplained iron-deficiency anemia in a carrier prompts the colonoscopy that finds it.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its cancers clot and its surgery adds risk: the colorectal and other adenocarcinomas of Lynch syndrome carry a raised venous thromboembolism risk, compounded by the resections used to treat them.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery opens the door to infection: the colectomy and other resections that Lynch cancers require can be complicated by anastomotic leak and intra-abdominal sepsis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Inflammation feeds the mismatch-repair-deficient tumor: IL-6-driven STAT3 signaling promotes proliferation and survival in the inflamed Lynch colorectal cancer, a node alongside the heavy immune infiltrate of these MSI-high tumors.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation pushes the polyp to cancer: NF-κB activation in the colonic mucosa adds pro-survival, pro-proliferative signals that, layered on mismatch-repair loss, speed the adenoma-to-carcinoma progression in Lynch syndrome.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor bleeding and inflammation drain the blood: beyond the iron loss of bleeding Lynch colorectal cancers, their inflammatory cytokines suppress erythropoiesis, adding an anemia of chronic disease to the iron deficiency.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its urinary-tract cancers can block the kidneys: Lynch syndrome predisposes to upper-tract urothelial carcinoma, which obstructs the ureters into hydronephrosis, and the platinum chemo for its cancers adds nephrotoxicity threatening chronic kidney disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its colorectal-cancer chemo can wound the heart: the 5-fluorouracil and oxaliplatin used against Lynch-associated colorectal cancer cause coronary vasospasm and cardiotoxicity that can precipitate cardiac dysfunction.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong cancer surveillance weighs on the mind: living with a high inherited risk of multiple cancers, frequent colonoscopies and the threat of new diagnoses gives Lynch syndrome carriers a substantial burden of depression.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Constant cancer surveillance breeds worry: the lifelong colonoscopic and multi-organ screening and inherited multi-cancer risk of Lynch syndrome foster chronic health anxiety alongside depression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemotherapy injures the nerves: the oxaliplatin used for the colorectal cancers of Lynch syndrome causes a cold-triggered, chronic peripheral neuropathy with neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from chemotherapy for the colorectal and other cancers of Lynch syndrome can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It targets the upper urinary tract: Lynch syndrome causes urothelial carcinoma of the ureter and renal pelvis, a recognised part of its tumour spectrum requiring urinary surveillance.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Risk-reducing and cancer surgery means many wounds: colectomy and prophylactic hysterectomy-oophorectomy in Lynch syndrome leave abdominal wounds and anastomoses that must heal.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Immunotherapy for its MSI-high tumours inflames glands: because Lynch cancers are mismatch-repair-deficient, checkpoint inhibitors are highly effective but trigger endocrine irAEs like thyroiditis and hypophysitis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the brain in the Turcot variant: Lynch carriers have a raised risk of glioblastoma and other brain tumours, and biallelic constitutional MMR deficiency causes childhood brain tumours.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its immunotherapy can inflame the lungs: checkpoint inhibitors, highly effective against its MSI-high cancers, can cause immune-related pneumonitis as an adverse effect.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its immunotherapy can inflame joints and muscle: checkpoint-inhibitor therapy for Lynch-related cancers can trigger inflammatory arthritis and myositis among its immune-related adverse events.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Aspirin lowers its cancer risk: the CAPP2 trial showed regular aspirin substantially reduces colorectal cancer in Lynch syndrome, now offered as chemoprevention.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet supports the at-risk bowel: a high-fibre diet aids colorectal health, complementing the intensive colonoscopic surveillance that Lynch syndrome requires.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment can reach the heart: chemotherapy for Lynch-related cancers, including platinum and fluoropyrimidines, carries cardiotoxic and thrombotic risk.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Mismatch-repair loss makes it immunotherapy-sensitive: Lynch tumours are microsatellite-unstable with a high mutational burden, responding dramatically to PD-1 inhibitors like pembrolizumab, which has tissue-agnostic approval for MSI-high cancer.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo with a twist: Lynch-associated colorectal cancers are treated with chemotherapy, though MSI-high tumours respond poorly to fluorouracil alone, favouring immunotherapy.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — The two great hereditary cancer syndromes: Lynch syndrome (mismatch-repair loss) and Li-Fraumeni (germline TP53) are the archetypal autosomal-dominant multi-cancer predispositions with distinct mechanisms and spectra.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Two DNA-repair colorectal syndromes: Lynch arises from dominant mismatch-repair loss causing microsatellite instability, while MUTYH-associated polyposis comes from recessive base-excision-repair loss causing G:C→T:A mutations—different defects, overlapping colorectal risk.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Its ovarian cancers favour a histology: Lynch-associated ovarian tumours are predominantly endometrioid and clear-cell rather than the high-grade serous cancers of BRCA carriers, so clear-cell ovarian cancer in a young woman can flag mismatch-repair deficiency.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Why its tumours invite immunotherapy: mismatch-repair-deficient Lynch cancers accumulate frameshift neoantigens and draw dense lymphocytic infiltrates with germinal-centre-like tertiary lymphoid structures—the immune richness behind their response to checkpoint blockade.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — The recessive extreme (CMMRD): biallelic loss of a Lynch mismatch-repair gene causes constitutional MMR deficiency, a childhood syndrome with brain tumours including medulloblastoma and glioma.
- `connects-to` → **[ALL](../all/README.md)** — CMMRD leukaemia: constitutional mismatch-repair deficiency from biallelic Lynch-gene loss predisposes children to leukaemia and lymphoma alongside the brain and gut tumours.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatobiliary spread: Lynch raises the risk of biliary-tract cancer, and mismatch-repair-deficient tumours metastasise to the liver, seeding the hepatic lobule.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — When both copies fail: constitutional mismatch-repair deficiency (biallelic Lynch genes) causes a childhood-cancer syndrome with café-au-lait macules that closely mimics neurofibromatosis type 1, a key diagnostic pitfall.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — A different polyposis pathway: Peutz-Jeghers (STK11) produces hamartomatous gut polyps and high GI cancer risk, contrasting with the mismatch-repair-driven adenoma-carcinoma route of Lynch in the differential of hereditary GI cancer.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Overlapping endometrial and colon risk: Cowden syndrome (PTEN) independently raises the risk of endometrial and colorectal cancer, a PTEN/mTOR-driven syndrome to distinguish from Lynch in women with these tumours.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — A distinct pathway: unlike chromosomally unstable colorectal cancers driven by p53 loss, Lynch (MSI) tumours arise from mismatch-repair failure and frameshift mutations, often retaining wild-type p53.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Hypermutated activation: the mismatch-repair-deficient tumours of Lynch syndrome accumulate activating PIK3CA and frameshift mutations across their hypermutated genomes.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: like other cancers, Lynch-associated tumours reactivate TERT to maintain telomeres, sustaining the unlimited division enabled by mismatch-repair loss.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT activation: frameshift and PIK3CA mutations in the hypermutated Lynch tumours activate AKT, driving growth alongside the mismatch-repair defect.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Wnt-driven oncogene: APC/Wnt activation common in Lynch colorectal cancers upregulates MYC, driving the proliferation of these mismatch-repair-deficient tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in growing Lynch-associated tumours drives the angiogenesis that supports their expansion, complementing their high immunogenicity.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Immunogenic MSI tumours: the frameshift neoantigens of mismatch-repair-deficient Lynch tumours provoke a brisk IFN-γ-driven T-cell infiltrate, the basis of their exceptional response to checkpoint immunotherapy.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Tumour-suppressor loss: CDKN2A inactivation accompanies progression of Lynch-associated adenomas to carcinoma, releasing the cell-cycle brake in these mismatch-repair-deficient tumours.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into Lynch tumours, part of the rich immune microenvironment that shapes their response to immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The microsatellite-instable tumors of Lynch accumulate cytosolic DNA from their genomic instability, engaging cGAS-STING—an innate-immune arm of the immunogenicity that, with their neoantigen load, drives the dramatic checkpoint-inhibitor response.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The frameshift neoantigens of mismatch-repair-deficient Lynch tumors drive CD8 T cells to deploy perforin against them, the cytotoxic killing that checkpoint blockade unleashes to such effect in microsatellite-instable cancers.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling drives the metastasis of the colorectal, endometrial, and other Lynch-spectrum cancers, the chemokine route to spread when these tumors escape the intensive surveillance that defines Lynch management.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — The CAPP2 trial showed that long-term aspirin, by inhibiting COX-derived prostaglandins, substantially reduces colorectal-cancer incidence in Lynch syndrome, an evidence-based chemoprevention recommended for carriers.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Endometrial cancer is the commonest extracolonic Lynch tumor and often the first to present in women, an estrogen-responsive cancer for which risk-reducing hysterectomy is offered once childbearing is complete.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — The mismatch-repair deficiency of Lynch tumors generates recurrent frameshift-peptide neoantigens, the basis for shared cancer-prevention vaccines being trialled to prime antibody and T-cell immunity before tumors arise.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS and BRAF (both already mapped) signal through MAPK-ERK in Lynch-associated colorectal cancer, with BRAF testing used to distinguish sporadic MSI-high tumors from true Lynch syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) active in the colorectal and endometrial cancers of Lynch syndrome.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC inactivation activates Wnt/β-catenin (mapped) to initiate the adenoma-carcinoma sequence in Lynch colorectal cancer, on which the mismatch-repair defect then layers rapid mutation accumulation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The high neoantigen load of MMR-deficient Lynch tumors drives an interferon-rich microenvironment signaling through JAK-STAT (IFN-γ already mapped), underlying their responsiveness to checkpoint immunotherapy.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides an inflammatory cofactor in the colorectal carcinogenesis of Lynch syndrome.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Loss of the RB1-E2F checkpoint cooperates with mismatch-repair deficiency in the progression of Lynch-syndrome adenomas to carcinoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — MMR-deficient tumors frequently acquire TGFBR2 frameshift mutations that cripple TGF-β-SMAD signaling (TGF-β mapped), removing a growth-suppressive brake in Lynch-syndrome cancers.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates tumor-cell adhesion and the immune microenvironment of the colorectal and endometrial cancers of Lynch syndrome.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) cooperates with mismatch-repair deficiency in Lynch-syndrome tumorigenesis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The high neoantigen load of mismatch-repair-deficient Lynch tumors drives IFN-STAT1 signaling, underlying their marked responsiveness to checkpoint immunotherapy.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (CDKN2A and RB1 already mapped) drives the cell-cycle progression of the colorectal and endometrial cancers of Lynch syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by PI3K-AKT signaling, is lost in the malignant progression of Lynch-syndrome tumors.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the mismatch-repair-deficient cancers of Lynch syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory, neoantigen-rich microenvironment of the MSI-high tumors of Lynch syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of the colorectal and endometrial cancers of Lynch syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the progression of the MSI-high tumors of Lynch syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation, alongside MLH1 promoter hypermethylation, participates in the epigenetic component of the mismatch-repair-deficient tumors of Lynch syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the hypermutated MSI-high tumor cells of Lynch syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of Lynch syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immune microenvironment of the MMR-deficient tumors of Lynch syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Lynch syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the cancers of Lynch syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of Lynch syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Lynch syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Lynch syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of Lynch syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of Lynch syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — MSI neoantigens: mismatch-repair deficiency generates abundant frameshift neoantigens presented on MHC, making Lynch tumours highly immunogenic and checkpoint-responsive (PD-1/CTLA-4 already mapped), and the rationale for shared frameshift-neoantigen vaccines.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2-driven proliferation of the tumour-infiltrating T cells underlies the strong immune response to the microsatellite-instable cancers of Lynch syndrome, the basis of their responsiveness to immunotherapy.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 antitumour immunity: the microsatellite-instable tumours of Lynch syndrome elicit a brisk Th1 and cytotoxic infiltrate, and IL-12-driven Th1 polarisation (interferon-gamma already mapped) is part of the antitumour immunity that immunotherapy amplifies.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Occult bleeding: the right-sided colorectal cancers of Lynch syndrome bleed chronically, and the resulting iron-deficiency anaemia lowering haemoglobin is often the sign that brings the tumour, or the syndrome, to attention.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Th1 orchestration: CD4 helper T cells polarised to Th1 (IL-12 and interferon-gamma already mapped) coordinate the brisk antitumour infiltrate of the microsatellite-instable Lynch cancers, supporting the CD8 (already mapped) response that immunotherapy amplifies.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive counter-regulation: IL-10 in the tumour microenvironment restrains the strong Th1 and cytotoxic response (PD-1 already mapped) to the microsatellite-instable Lynch tumours, one brake on the immunity that checkpoint blockade releases.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage counterbalance: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) that counterbalances the strong Th1 infiltrate (interferon-gamma already mapped) of the microsatellite-instable Lynch tumours.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile acids and chemoprevention: dietary fat and the bile acids derived from cholesterol promote colonic carcinogenesis, and this modifiable influence, alongside aspirin (prostaglandins already mapped), informs the risk reduction in Lynch syndrome.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic colonic inflammation generates oxidative stress, to which xanthine oxidase contributes, adding DNA damage that, atop the mismatch-repair defect (already mapped), speeds the carcinogenesis of Lynch syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the Lynch-associated cancers, balanced against the strong anti-tumour immunity of the MSI-high tumours.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and cancer risk: the adipokine leptin links obesity to colorectal carcinogenesis (Wnt already mapped), a modifiable factor modulating the penetrance of the cancer risk in Lynch syndrome.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary chemoprevention: dietary calcium reduces colorectal adenoma recurrence, binding the bile acids (cholesterol already mapped) that promote carcinogenesis, a modifiable factor in the risk reduction of Lynch syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity-cancer adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related modifiable colorectal-cancer risk of Lynch syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity-related modifiable cancer risk of Lynch syndrome.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — MSI-high immunogenicity: the MSI-high, MMR-deficient (already mapped) Lynch tumours activate the cGAS-STING (already mapped) pathway to produce the type-I interferon that drives the immunogenicity and the checkpoint (PD-1 already mapped) response.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Peritumoral eosinophilia: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils of the prognostically favourable peritumoral infiltrate of the MSI-high Lynch tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23/Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune infiltrate implicated in the colorectal carcinogenesis of Lynch syndrome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell infiltrate: the mast cells and histamine are part of the dense immune microenvironment of the MSI-high (MMR-deficient already mapped) Lynch tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell infiltrate: the mast cells (the histamine already mapped source) populate the dense immune microenvironment of the MSI-high Lynch tumours.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophil infiltrate: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are part of the highly immune-infiltrated MSI-high Lynch tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the Lynch tumours.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in immunogenic tumours: the complement C5 and its C5a (with C3 already mapped) shape the innate inflammation of the highly immune-infiltrated MSI-high Lynch tumours.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Chemoprevention vitamin: the vitamin D status modulates the colorectal-cancer (already mapped) risk and, with aspirin, is part of the chemoprevention landscape of Lynch syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the antioxidant micronutrient dimension studied in the colorectal-cancer (already mapped) chemoprevention of Lynch syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment into the immune-rich stroma of the MSI-high Lynch-syndrome tumours.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the MMR-deficient Lynch tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack against the highly immunogenic MSI-high tumours.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Bleeding iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia from the occult gastrointestinal blood loss that often heralds the colorectal cancer (already mapped) of Lynch syndrome.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Colorectal mucosal alarmin: TSLP from the intestinal epithelium (already mapped) activates dendritic cells (already mapped) and mast cells (already mapped), shaping the mucosal type-2 immune environment of the MSI-H colorectal and endometrial Lynch-spectrum cancers.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Pericolorectal stroma: periostin, a SMAD4-downstream ECM protein (SMAD4 already mapped), drives cancer-associated fibroblast activation in the Lynch colorectal stroma; elevated tumour-adjacent periostin correlates with invasiveness of Lynch-spectrum cancers.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Inflammation-pain axis: bradykinin activates B2 receptors in the colorectal mucosa, amplifying prostaglandin (already mapped) and NF-κB (already mapped) signalling in the Lynch tumour microenvironment and contributing to neuropathic pain (already mapped) and inflammatory flares.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: C1-INH controls the classical and lectin complement pathways (C3, C5, C5aR1 and factor H already mapped) that contribute to anti-tumour immunity against the highly immunogenic MSI-H Lynch-spectrum colorectal and endometrial cancers.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia-of-cancer correction: erythropoietin, rising in response to the anaemia of chronic disease (already mapped) and iron-deficiency anaemia (already mapped) from occult GI bleeding, guides transfusion decisions in Lynch colorectal cancer chemotherapy (already mapped).
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Anti-colorectal-cancer melatonin: melatonin suppresses Wnt/β-catenin (wnt-beta-catenin already mapped) and NF-κB (already mapped) in Lynch MMR-deficient colorectal cells, reducing proliferation and potentiating the anti-tumour immune response of MSI-H tumours.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-MMR axis: testosterone, via androgen receptor on Lynch MMR-deficient colorectal and endometrial cells (endometrial cancer already mapped), modulates MMR gene expression and promotes the androgen-driven tumour proliferation contributing to sex-dependent Lynch cancer risk.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gut neuroendocrine modulation: serotonin from enterochromaffin cells in Lynch MMR-deficient colorectal mucosa regulates bowel motility and mucosal immune responses (already mapped) that shape the MSI-H tumour microenvironment of Lynch syndrome.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Tumour-promoting prolactin: prolactin, via PRL-R on Lynch MMR-deficient endometrial (already mapped) and colorectal cells, activates JAK2/STAT5 proliferative signalling and contributes to the endometrial cancer penetrance of Lynch syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Lynch oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Lynch syndrome.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Lynch vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the tumour; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Lynch syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Lynch iodine: iodine, via thyroid hormone biosynthesis, modulates intestinal epithelial (already mapped) and macrophage (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Lynch syndrome.

[^bonadona-2011-lynch-risks]: Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. *JAMA.* 2011;305(22):2304-2310. [doi:10.1001/jama.2011.743](https://doi.org/10.1001/jama.2011.743) · [PubMed 21642683](https://pubmed.ncbi.nlm.nih.gov/21642683/)
[^lynch-2015-lynch-review]: Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. *Nat Rev Cancer.* 2015;15(3):181-194. [doi:10.1038/nrc3878](https://doi.org/10.1038/nrc3878) · [PubMed 25673086](https://pubmed.ncbi.nlm.nih.gov/25673086/)
