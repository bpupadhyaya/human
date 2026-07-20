---
schema: human-scale-entry/v1
id: hlrcc
name: Hereditary Leiomyomatosis and Renal Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary leiomyomatosis and renal cell carcinoma (HLRCC) is caused by germline FH mutations; cutaneous and uterine leiomyomas + aggressive FH-deficient RCC; collecting duct-like histology; fumarate drives HIF-1α + immune evasion; bevacizumab + erlotinib standard."
aliases: ["HLRCC", "hereditary leiomyomatosis renal cell carcinoma", "FH syndrome", "Reed syndrome", "FH-deficient RCC", "HLRCC RCC", "FH leiomyoma", "fumarate hydratase deficiency", "FH hereditary cancer", "leiomyomatosis RCC"]
sources:
  - id: tomlinson-2002-fh
    type: peer-reviewed
    cite: "Tomlinson IP, Alam NA, Rowan AJ, et al. Germline mutations in FH predispose to dominantly inherited uterine fibroids, skin leiomyomata and papillary renal cell cancer. Nat Genet. 2002;30(4):406-410."
    doi: "10.1038/ng849"
    pmid: "11865300"
    url: "https://doi.org/10.1038/ng849"
  - id: linehan-2013-fh-review
    type: peer-reviewed
    cite: "Linehan WM, Rouault TA. Molecular pathways: fumarate hydratase-deficient kidney cancer — targeting the Warburg effect in cancer. Clin Cancer Res. 2013;19(13):3345-3352."
    doi: "10.1158/1078-0432.CCR-13-0304"
    pmid: "23836472"
    url: "https://doi.org/10.1158/1078-0432.CCR-13-0304"
cross_links:
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Germline FH mutations cause HLRCC (autosomal dominant); FH LOF → fumarate accumulation; 2SC IHC (anti-2-succino-cysteine) positive in FH-deficient tumors; FH IHC loss diagnostic; somatic second hit (LOH or second mutation) in each HLRCC leiomyoma or RCC"
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HLRCC-associated RCC driven by HIF-1α pseudohypoxia (FH LOF → PHD inhibition → HIF-1α stabilized); VEGF/HIF-1α pathway active; bevacizumab (anti-VEGF) + erlotinib standard for HLRCC RCC; HIF-2α inhibitor belzutifan being explored in FH-deficient RCC"
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "HLRCC-associated RCC is pseudohypoxic similar to VHL-mutant ccRCC (both have HIF-1α and VEGF overexpression); histologically distinct (type 2B papillary/collecting duct-like, NOT clear cell); anti-VEGF therapies active in both; belzutifan explored in FH-deficient RCC"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "HLRCC-associated RCC: most aggressive hereditary RCC; collecting duct-like/papillary type 2B; often metastatic at diagnosis; FH IHC loss + 2SC positivity diagnostic; bevacizumab + erlotinib standard (NCI Phase 2, ORR ~64%, mPFS 21 months); sunitinib/pazopanib insufficient"
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "HLRCC produces multiple smooth muscle tumors (leiomyomas): painful cutaneous nodules from arrector pili muscle and early-onset, large, multiple uterine fibroids; biallelic FH loss drives them, and FH-/2SC+ immunostaining distinguishes HLRCC leiomyomas from sporadic ones."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Fumarate accumulation stabilizes HIF-1α (pseudohypoxia) → VEGF transcription → tumor angiogenesis; this is the therapeutic handle in FH-deficient RCC — bevacizumab (anti-VEGF) plus erlotinib (anti-EGFR) achieves ~65% response, far exceeding VEGFR-TKIs like sunitinib."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "HLRCC causes the most aggressive hereditary kidney cancer — collecting-duct-like/type-2B papillary RCC that can metastasize even at 1-2 cm; radical (not partial) nephrectomy with lymphadenectomy is preferred, and annual renal MRI surveillance starts at genetic diagnosis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The uterus is often where HLRCC declares itself: women develop numerous, large, early-onset uterine leiomyomas (fibroids), frequently needing myomectomy or hysterectomy before age 30 — so multiple early fibroids with cutaneous leiomyomas should prompt FH testing."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous leiomyomas are the 'L' of HLRCC and its visible clue: firm, often painful skin-colored papules from arrector pili smooth muscle appearing in the 20s-30s; their recognition (with FH/2SC staining) flags the syndrome years before the aggressive kidney cancer."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "HLRCC's FH belongs to the same Krebs-cycle, pseudohypoxia family (SDHx, FH) that causes hereditary pheochromocytoma/paraganglioma: FH loss accumulates fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF — so rare FH-mutant PPGLs occur, sharing fumarate-driven biology."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "HLRCC and VHL disease are both hereditary kidney-cancer syndromes converging on pseudohypoxia: VHL loss stabilizes HIF directly, while HLRCC's FH loss raises fumarate that blocks the HIF prolyl-hydroxylases. HLRCC papillary RCC is far more aggressive than VHL clear-cell tumors."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "HLRCC and tuberous sclerosis are inherited syndromes that both cause renal tumors and smooth-muscle lesions: TSC drives angiomyolipomas and renal cysts via mTOR, while HLRCC's FH loss drives aggressive papillary RCC plus cutaneous and uterine leiomyomas."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "HLRCC illustrates pseudohypoxia's effect on red cells: fumarate accumulation stabilizes HIF as if oxygen were low, and HIF transcribes erythropoietin—so FH-deficient and other TCA-cycle tumors can drive secondary polycythemia and a raised erythrocyte mass."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "HLRCC and Birt-Hogg-Dubé are both hereditary kidney-cancer syndromes with distinct genes: HLRCC's FH loss yields type 2 papillary RCC and cutaneous/uterine leiomyomas, while BHD's FLCN loss gives chromophobe/oncocytic tumors, lung cysts and skin fibrofolliculomas."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "HLRCC's FH defect strikes the uterus as well as the kidney: fumarate-hydratase loss drives the cutaneous and uterine leiomyomas of the syndrome, and FH-deficient uterine tumors and endometrial cancers can arise—so gynecologic surveillance complements renal screening."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "HLRCC and Cowden syndrome are both dominant syndromes raising kidney cancer risk via different pathways: HLRCC from FH loss (a Krebs-cycle/pseudohypoxia defect), Cowden from PTEN loss (PI3K-AKT)—each adds a distinct extrarenal tumor spectrum."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "HLRCC tumors fake hypoxia: accumulated fumarate from FH loss inhibits the oxygen-sensing prolyl hydroxylases, so HIF stabilizes as if oxygen were scarce—this pseudohypoxia drives VEGF and the aggressive angiogenic type-2 papillary kidney cancers of the syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "HLRCC cancers lean on mTOR and angiogenesis for growth: fumarate-driven pseudohypoxia and metabolic rewiring activate growth signaling, which is why advanced HLRCC renal cancer is treated with combined VEGF and EGFR/mTOR-pathway-directed therapy rather than standard regimens."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HLRCC shows how a metabolic gene becomes oncogenic: fumarate accumulation inactivates proteins and impairs DNA-damage responses including p53, so a Krebs-cycle enzyme defect causes genomic instability—an oncometabolite route to cancer."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Skin tumors are usually the first sign of HLRCC: FH loss causes multiple cutaneous piloleiomyomas—firm, sometimes painful smooth-muscle nodules—so a dermatologist often flags the syndrome before its aggressive kidney cancer appears."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "HLRCC is a disease of carbon metabolism gone wrong: losing fumarate hydratase stalls the Krebs cycle so the carbon metabolite fumarate piles up as an oncometabolite, stabilizing HIF and modifying proteins to drive cancer—linking a metabolic enzyme to malignancy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "FH-deficient HLRCC kidney cancer engages the immune system: these aggressive tumors are often treated with combinations of immune checkpoint inhibitors and anti-angiogenic agents, reflecting how the metabolic defect reshapes the tumor's vasculature and immune milieu."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "HLRCC is an oncometabolite cancer like IDH-mutant glioma: loss of fumarate hydratase floods cells with fumarate which—like glioma's 2-hydroxyglutarate—inhibits dioxygenases, stabilizes HIF, and rewires epigenetics, so two enzymes converge on metabolite-driven cancer."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "HLRCC kidney cancer spreads early to the lung: its type 2 papillary renal cell carcinoma is unusually aggressive and metastasizes while small, often to the lungs—so HLRCC carriers need vigilant renal surveillance and prompt surgery."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "HLRCC's cutaneous leiomyomas are firm, collagen-rich nodules: smooth-muscle tumors set in dense dermal collagen form papules that hurt with cold or touch, so these tender skin lumps are often the first sign pointing to an FH mutation."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "HLRCC tumors survive by hijacking NRF2: accumulated fumarate chemically modifies KEAP1, freeing the antioxidant master switch NRF2 to shield the cancer from oxidative stress—a key vulnerability being targeted in FH-deficient kidney cancer."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "FH loss forces HLRCC cells to make ATP by glycolysis: with the Krebs cycle broken, the tumor can't run normal oxidative phosphorylation, so it shifts to aerobic glycolysis (the Warburg effect) for energy—a metabolic weakness drugs aim to exploit."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "HLRCC's aggressive kidney cancer is met with immunotherapy: because FH-deficient tumors are highly angiogenic and immune-active, regimens combining checkpoint drugs (engaging NK and T cells) with anti-angiogenics are used against this hard-to-treat cancer."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "HLRCC kidney cancer leans on the AKT-mTOR growth axis: FH loss and its metabolic stress activate AKT and mTOR signaling, so this pathway joins the pseudohypoxic HIF program in driving the tumor, and is probed as a drug target."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages crowd HLRCC's tumor microenvironment: tumor-associated macrophages promote angiogenesis and immune suppression around the FH-deficient kidney cancer, shaping a stroma that the immunotherapy combinations try to flip."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are key to attacking HLRCC: because FH-deficient tumors are immune-active and antigen-rich, antigen-presenting dendritic cells help prime the T-cell response that checkpoint and vaccine strategies aim to unleash."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "FH mutations can sprout adrenal tumors: beyond skin and uterine leiomyomas and aggressive kidney cancer, the same fumarate-hydratase defect predisposes to pheochromocytomas and paragangliomas, including in the adrenal glands."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "HLRCC's kidney cancer bleeds iron away: the aggressive renal tumor causes blood in the urine, so hematuria and the iron-deficiency anemia it brings can be the warning that prompts imaging."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "HLRCC tumors are intensely vascular: losing FH stabilizes HIF, which drives VEGF and pushes endothelial cells to build a rich blood supply, the angiogenesis that anti-VEGF therapy targets."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "HLRCC demands aggressive imaging surveillance: because its kidney cancer spreads early, MRI and CT photons screen carriers from young adulthood to catch the tumor before it metastasizes."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "HLRCC's renal tumor builds a desmoplastic stroma: its aggressive type-2 papillary cancer grows amid dense fibrous tissue, alongside the firm collagen-rich leiomyomas of skin and uterus."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "HLRCC's kidney cancer spreads far and fast: its early, aggressive metastasis can reach the brain along with bone and lung, a grim contrast to the indolent renal tumors of related syndromes."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "HLRCC poisons the cell with an oncometabolite: losing fumarate hydratase backs up fumarate, which jams the enzymes that sense oxygen and edit DNA — the metabolic short-circuit driving its leiomyomas and aggressive kidney cancer."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "HLRCC's renal cancer races to the skeleton: unlike the indolent tumors of related syndromes, its type-2 papillary RCC metastasizes early to bone and the marrow within, alongside lung and brain."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The aggressive kidney cancer also seeds the liver: HLRCC's renal tumors spread hematogenously to multiple organs, the liver among the sites that mark its grim, fast-moving metastatic course."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody both diagnoses and treats HLRCC: the 2SC immunostain marks the fumarate-modified proteins that betray FH loss, while the anti-VEGF antibody bevacizumab — with erlotinib — is a mainstay against its kidney cancer."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "HLRCC's skin tumors hurt through nerves: the cutaneous leiomyomas are richly innervated piloleiomyomas that fire painfully with cold and touch, a distinctive symptom that flags the syndrome."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Its targeted therapy reaches the gut: the erlotinib paired with bevacizumab for HLRCC kidney cancer causes diarrhea and an acneiform rash, while bevacizumab itself carries a risk of bowel perforation."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The pseudo-hypoxia can overfill the blood: FH loss stabilizes HIF, which switches on erythropoietin, so HLRCC kidney tumors can drive a paraneoplastic erythrocytosis — too many red cells from a falsely sensed lack of oxygen."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "HLRCC sits opposite the other inherited papillary kidney cancer: its FH-driven type 2 papillary RCC contrasts with MET-activated hereditary papillary RCC type 1, so the gene at fault tells which papillary syndrome — and which course — a patient has."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy joins the HLRCC toolkit: its aggressive FH-deficient kidney cancers can respond to checkpoint inhibitors that unleash cytotoxic T cells, used alongside the bevacizumab-erlotinib backbone against this hard-to-treat tumor."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The benign tumors are mesenchymal: HLRCC's hallmark cutaneous and uterine leiomyomas are smooth-muscle and fibroblast-like growths of FH-deficient cells, the skin nodules and fibroids that flag the syndrome before the kidney cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "A blocked Krebs cycle starves the cell of energy: FH loss stalls the TCA cycle and forces a Warburg shift, a metabolic stress sensed by AMPK as the FH-deficient cell rewires its metabolism to survive."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "It joins the multisystem tumor-suppressor syndromes: like neurofibromatosis type 1, HLRCC is a single-gene disorder with cutaneous tumors and a predisposition to renal and adrenal/paraganglionic tumors, distinguished by its gene and metabolic mechanism."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "FH and SDH are sister Krebs-cycle tumor suppressors: like SDHB loss, FH loss floods the cell with an oncometabolite (fumarate) that stabilizes HIF and reprograms the epigenome — a shared pseudo-hypoxic mechanism across the metabolic cancer syndromes."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "The uterine leiomyomas bleed: women with HLRCC develop numerous, often symptomatic uterine fibroids whose heavy menstrual bleeding causes iron-deficiency anemia, frequently the first sign that brings them to attention."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its renal cancer is aggressive and clot-prone: HLRCC-associated renal cell carcinoma metastasizes early, and like other advanced cancers it carries a raised risk of venous thromboembolism through surgery and treatment."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "An oncometabolite rewires the cell's signaling: fumarate accumulating from FH loss succinates proteins and, alongside its activation of NRF2 and HIF, engages NF-κB-linked survival and inflammatory signaling in HLRCC tumors."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Saving the kidney costs function: the aggressive renal cell carcinoma of HLRCC demands prompt, sometimes radical surgery, and the loss of renal tissue across a lifetime of surveillance can drift toward chronic kidney disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Advanced renal cancer and its therapy invite infection: metastatic HLRCC kidney cancer and the systemic treatment it requires can cause the immune compromise and complications that lead to sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its aggressive kidney cancer drags the count down: the inflammatory burden of HLRCC's early-metastasizing renal cell carcinoma, with nephron loss and surgery, contributes an anemia of chronic disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its antiangiogenic therapy strains the heart: the bevacizumab-erlotinib and VEGF-targeted regimens used for HLRCC-associated renal cancer cause hypertension and cardiotoxicity that can contribute to heart failure."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive hereditary cancer weighs on the mind: living with the high risk of an early, aggressive kidney cancer and the demands of lifelong surveillance imposes a substantial psychological burden in HLRCC."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its leiomyomas are notoriously painful: the cutaneous leiomyomas of HLRCC cause cold- and touch-triggered pain, and uterine fibroids add severe pelvic pain, together producing chronic neuropathic and nociceptive pain."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Repeated tumor surgery taxes healing: the excisions of multiple cutaneous leiomyomas and nephron-sparing or radical kidney surgery in HLRCC leave recurrent wounds to heal."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Aggressive cancer risk and surveillance breed worry: the threat of an early, aggressive type 2 papillary kidney cancer and the lifelong imaging surveillance of HLRCC foster chronic health anxiety."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It seeds smooth-muscle tumours: HLRCC causes multiple painful cutaneous and uterine leiomyomas — benign tumours of smooth muscle — its defining non-renal feature."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones feed its fibroids and metabolism runs awry: the uterine leiomyomas of HLRCC are oestrogen-sensitive, and loss of fumarate hydratase reroutes Krebs-cycle metabolism toward a pseudohypoxic state."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its kidney cancer is aggressive and early: HLRCC causes a particularly aggressive type 2 papillary renal cell carcinoma that metastasises early, demanding prompt nephrectomy and close surveillance."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its kidney cancer races to the lungs: the aggressive type 2 papillary renal cell carcinoma of HLRCC metastasises early and frequently to the lungs, so chest imaging is part of surveillance."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads early to the nodes: HLRCC renal cell carcinoma involves regional and retroperitoneal lymph nodes early, a marker of its unusual aggressiveness among kidney cancers."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its metabolic defect drives tumour vessels: fumarate hydratase loss stabilises HIF in a pseudohypoxic state that boosts VEGF and tumour vascularity, the rationale for anti-VEGF bevacizumab-based therapy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It needs a tailored regimen: the aggressive type-2 papillary RCC of HLRCC is treated by combining anti-VEGF and EGFR-targeted agents (bevacizumab plus erlotinib) rather than the standard kidney-cancer drugs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its kidney cancer spreads early and far: the type-2 papillary RCC of HLRCC metastasises rapidly, including to the brain, even from small primary tumours."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It reaches the liver and reshapes metabolism: HLRCC's renal cancer commonly metastasises to the liver, and the fumarate-hydratase defect drives a Warburg-like metabolic shift in its cells."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy enters its treatment: like other renal cell cancers, the FH-deficient RCC of HLRCC is treated with PD-1 checkpoint inhibitors, usually combined with anti-angiogenic kinase inhibitors."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Two routes to too many red cells: HLRCC's HIF stabilisation can drive erythropoietin-mediated secondary erythrocytosis, the differential of the primary, JAK2-driven erythrocytosis of polycythaemia vera."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "A fellow autosomal-dominant tumour syndrome: like MEN1, HLRCC is an inherited predisposition to characteristic tumours, here uterine and skin leiomyomas with aggressive kidney cancer."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Krebs-cycle enzymes as tumour suppressors: HLRCC loses fumarate hydratase while SDH-deficient GIST and paraganglioma lose succinate dehydrogenase—each crippled TCA enzyme floods the cell with an oncometabolite and a pseudohypoxic, angiogenic phenotype."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "The tumour hijacks the antioxidant switch: accumulated fumarate succinates KEAP1, constitutively activating NRF2 in HLRCC—the very transcription factor dietary sulforaphane induces—so the cancer permanently turns on the protective programme broccoli only transiently mimics."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Sharing a hijacked NRF2 pathway: HLRCC switches on NRF2 through fumarate, while squamous non-small-cell lung cancer activates the same antioxidant programme via NFE2L2/KEAP1 mutations—both gaining oxidative-stress resistance and chemoresistance from one pathway."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Oncometabolite cancers: HLRCC's fumarate, like the 2-hydroxyglutarate of IDH-mutant cholangiocarcinoma and glioma, is an oncometabolite that reprograms the epigenome and stabilises HIF—a shared metabolic route to cancer."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Early lung metastasis: the type-2 papillary renal cancer of HLRCC is aggressive and metastasises early, seeding the lungs and the alveolar capillary bed even from small primaries."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Painful skin tumours: the cutaneous leiomyomas of HLRCC are characteristically tender, painful to cold and touch, a clinical clue rooted in their nerve-rich smooth-muscle origin."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A hypervascular cancer: FH loss stabilises HIF, so HLRCC's type-2 papillary kidney cancer is intensely angiogenic, building abnormal vasculature targeted by VEGF/EGFR therapy (bevacizumab-erlotinib)."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Aggressive bone metastasis: HLRCC's type-2 papillary renal cancer spreads early and aggressively, seeding the cortical bone among lung and liver as it disseminates."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: the aggressive renal cancer of HLRCC readily spreads to the liver, seeding the hepatic lobules, part of its tendency to metastasise even from a small primary."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "Oncometabolite epigenetics: fumarate accumulating from FH loss inhibits TET DNA-demethylases, causing the DNA hypermethylation that silences tumour-suppressor genes in HLRCC."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Shared oncometabolite mechanism: like IDH-mutant cancers making 2-hydroxyglutarate, FH-deficient HLRCC accumulates fumarate—both oncometabolites that inhibit the same α-ketoglutarate-dependent enzymes."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Reinforced silencing: the histone hypermethylation driven by fumarate, together with polycomb/EZH2 activity, locks in the repressed, dedifferentiated state of HLRCC tumour cells."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Metabolic-oncogene cooperation: the pseudohypoxic, fumarate-driven state of HLRCC upregulates MYC, fuelling the biosynthesis and proliferation of its aggressive type-2 papillary renal tumours."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: HIF-driven and growth-factor signalling in FH-deficient HLRCC upregulates cyclin D1, pushing the renal tumour cells through the G1 checkpoint."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in HLRCC renal tumours, enabling the limitless proliferation of this notably aggressive hereditary kidney cancer."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Pseudohypoxia mechanism: fumarate accumulating from FH loss competitively inhibits the EGLN/PHD prolyl hydroxylases, blocking HIF degradation to create the pseudohypoxic, angiogenic state that drives HLRCC."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: RAS-RAF-ERK signalling, alongside the MET pathway, drives the proliferation of the aggressive type 2 papillary renal cancer of HLRCC."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into HLRCC renal tumours, shaping the microenvironment of this metabolically reprogrammed, immunologically active cancer."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Fumarate-driven HR defect: accumulating fumarate suppresses homologous-recombination repair by inhibiting RAD51-pathway function, creating a 'BRCAness'-like state in FH-deficient HLRCC tumours that may confer PARP-inhibitor sensitivity."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Aggressive metastasis: CXCR4 on the type 2 papillary renal cancer of HLRCC follows CXCL12 gradients to drive the early, aggressive metastasis that distinguishes this hereditary kidney cancer from indolent ones."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis resistance: the metabolic reprogramming of FH-deficient HLRCC cells confers resistance to caspase-3-mediated apoptosis, part of the survival advantage that makes these tumours so aggressive and treatment-resistant."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Hypermethylator phenotype: accumulated fumarate in FH-deficient HLRCC inhibits the TET DNA-demethylases, producing a globally hypermethylated genome that silences tumour-suppressor genes — the epigenetic consequence of the oncometabolite."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Targeted regimen: the combination of the anti-VEGF antibody bevacizumab with the EGFR inhibitor erlotinib is an effective regimen for HLRCC-associated papillary renal cell carcinoma, hitting the angiogenic and growth-factor arms of these aggressive tumours."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Uterine leiomyomas: HLRCC causes oestrogen-dependent uterine fibroids that are typically numerous, early-onset and symptomatic, often the first manifestation of the syndrome in affected women and a clue to the FH mutation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-mTOR target: PIK3CA drives the PI3K-AKT-mTOR axis (AKT, mTOR and AMPK already mapped) active in HLRCC renal cancer, a rationale for the bevacizumab-erlotinib and mTOR-directed regimens used in this aggressive papillary RCC."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: the cyclin-D1 axis (mapped) drives RB phosphorylation that releases E2F1, powering the cell-cycle entry of the aggressive type-2 papillary renal cancer of HLRCC."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brake: CDKN2A loss removes restraint on the cyclin-D-CDK4/6 axis, a cooperating lesion in the malignant progression of HLRCC renal tumours."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Renal-tumour angiogenesis: the VEGF/PDGF angiogenic axis (VEGF already mapped) drives the highly vascular type-2 papillary renal cell carcinoma of HLRCC and is targeted by the tyrosine-kinase inhibitors used in its treatment."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-MAPK signalling (ERK1/2 already mapped) provides a proliferative input downstream of MET and EGFR in the aggressive renal tumours of HLRCC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint loss: the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) restrains proliferation, and its disruption contributes to the aggressive growth of HLRCC-associated renal cancer."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Fumarate accumulation inhibits prolyl hydroxylases (EGLN1 mapped) and stabilises HIF-2α (EPAS1), the pseudohypoxic driver of the renal cancers of HLRCC."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates survival and the microenvironment of the aggressive type-2 papillary renal cancers of HLRCC."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) shapes proliferation in HLRCC-associated tumours."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of the aggressive FH-deficient renal cancer of HLRCC."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Fumarate accumulation and mitochondrial dysfunction from FH loss release cytosolic DNA that can engage cGAS-STING in the tumours of HLRCC."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of the HLRCC-associated tumours."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a pro-apoptotic brake in the aggressive renal carcinoma of HLRCC."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-treated HLRCC renal carcinoma must evade."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the HLRCC-associated tumors."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the NRF2 and survival signaling (NFE2L2 already mapped) that the fumarate accumulation of HLRCC dysregulates."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the FH-deficient cells of HLRCC under metabolic and oxidative stress."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the aggressive type 2 papillary renal tumors of HLRCC."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the renal tumors of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of MET and other receptor tyrosine kinases (MET already mapped) participates in the invasive signaling of the renal tumors of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling participates in the tumor-microenvironment and survival signaling of the aggressive renal cancer of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary leiomyomatosis and renal cell cancer."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Uterine leiomyoma hormones: the uterine smooth-muscle tumours of HLRCC, like common fibroids, are hormone-responsive, so progesterone and estrogen (already mapped) drive the growth that causes heavy bleeding and often early hysterectomy in affected women."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "RCC immunotherapy: MHC class II antigen presentation shapes the T-cell response to the aggressive FH-deficient renal cell carcinoma of HLRCC, whose systemic treatment increasingly combines antiangiogenics with immune checkpoint blockade."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2-driven T-cell expansion underlies the immunotherapy of the metastatic renal cell carcinoma that makes HLRCC dangerous, complementing the bevacizumab-erlotinib regimen aimed at its pseudohypoxic biology (HIF already mapped)."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Polycythaemia and haematuria: the pseudohypoxic HIF and erythropoietin drive (already mapped) can raise haemoglobin, while the renal cell carcinoma of HLRCC causes haematuria and, later, the anaemia of advanced disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with the strongly upregulated VEGF (already mapped) supports the rich angiogenesis of the pseudohypoxic FH-deficient renal cell carcinoma, part of the vascular biology targeted by antiangiogenic therapy."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and antioxidant stress: fumarate accumulation succinates KEAP1 to activate NRF2 (already mapped), a response to the oxidative stress, to which xanthine oxidase contributes, of the metabolically rewired FH-deficient cell."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the aggressive FH-deficient renal cell carcinoma dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion relevant to its immunotherapy."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the HLRCC tumour stroma, part of its immune-evasive microenvironment."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Leiomyoma pain and inflammation: prostaglandins contribute to the pain of the cutaneous piloleiomyomas and to the inflammatory microenvironment of the FH-deficient tumours of HLRCC."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the FH-deficient tumours of HLRCC."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "Hereditary-RCC syndromes: HLRCC sits among the hereditary renal cell carcinoma syndromes with Birt-Hogg-Dubé and VHL (already mapped), the group of germline predispositions to distinct renal cancers requiring surveillance."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haematuria and anaemia: the aggressive type-2 papillary renal cancer of HLRCC can bleed, causing the haematuria and iron-deficiency anaemia (haemoglobin already mapped) that reflect the renal tumour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic reprogramming adipokine: leptin connects to the FH-driven metabolic reprogramming (AMPK already mapped) of HLRCC, part of the adipokine dimension of its altered energy metabolism."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "AMPK-linked adipokine: adiponectin, with leptin (already mapped), activates the AMPK (already mapped) energy metabolism disturbed by the fumarate-hydratase loss of HLRCC."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of HLRCC."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the aggressive HLRCC papillary renal cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the HLRCC renal cancer."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Prognostic neutrophils: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are prognostic in the aggressive renal cancer of HLRCC."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-tumour immune microenvironment of the HLRCC renal cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of the HLRCC tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of HLRCC."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of HLRCC."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells infiltrate the leiomyomas and the papillary-RCC stroma and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of HLRCC."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HLRCC tumours."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the FH-deficient HLRCC renal tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the HLRCC tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the FH-deficient, pseudohypoxic (HIF-1α already mapped) HLRCC papillary renal tumours."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) amplify the myeloid recruitment and the tumour-microenvironment inflammation in the FH-mutant HLRCC renal tumours."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: FH-mutant HLRCC renal tumour cells upregulate factor H to bind C3b and block the alternative pathway (C3, C5 and C5aR1 already mapped), escaping complement-mediated lysis."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Desmoplastic stroma: TGF-beta drives the fibroblast and collagen deposition (both already mapped) of the desmoplastic stroma of the HLRCC type-2 papillary renal tumours, promoting invasion."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin in leiomyomas: TSLP secreted by the uterine smooth-muscle cells (already mapped) of HLRCC leiomyomas primes the mast cells (already mapped) to sustain the type-2 inflammatory stromal microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vasoactive kinin in pseudohypoxic tumours: bradykinin promotes vasodilation and VEGF-driven angiogenesis (VEGF already mapped) in the pseudohypoxic (HIF-1α already mapped) HLRCC papillary renal tumours."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical pathway regulation: C1-INH controls the classical-pathway arm (C3, C5, C5aR1 and factor H already mapped) of the complement cascade activated against the FH-deficient HLRCC renal tumour cells, limiting complement-mediated lysis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-HLRCC axis: histamine, released by mast cells in the HLRCC tumour microenvironment, signals via H1/H2 receptors on FH-mutant (already mapped) tumour cells and endothelium, modulating angiogenesis and the immunosuppressive milieu of HLRCC renal cancers."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-HLRCC axis: melatonin, via MT1/MT2 receptors on FH-mutant (already mapped) HLRCC cells, modulates the HIF-1α-driven (already mapped) pseudohypoxic metabolism, suppresses Warburg-effect-dependent proliferation, and enhances apoptotic sensitivity."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-HLRCC axis: testosterone, via androgen receptor signalling on FH-mutant (already mapped) renal and uterine tumour cells, modulates HIF-1α (already mapped) target-gene expression and the sex-biased aggressiveness of HLRCC-associated renal cell carcinoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "HLRCC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "HLRCC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the tumour inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HLRCC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the tumour; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "HLRCC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "HLRCC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of HLRCC."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HLRCC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of HLRCC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HLRCC sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and T-cytotoxic (already mapped) suppression; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HLRCC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HLRCC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "HLRCC chloride: chloride channels regulate macrophage (already mapped) and T-cytotoxic (already mapped) volume during tumour-microenvironment stress; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade in HLRCC."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "HLRCC nitrogen: nitrogen as backbone of oncoproteins and cytokines (already mapped) sustains tumour signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting inflammatory cascade in HLRCC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "HLRCC potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "HLRCC calcium: calcium signals macrophage (already mapped) and T-cytotoxic (already mapped) immune activation in tumour microenvironment; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "HLRCC hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HLRCC phosphorus: phosphorus as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of HLRCC."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "HLRCC pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses FH-deficient tumour immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "HLRCC glp-1: GLP-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) tumour cascade of HLRCC."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "HLRCC angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "HLRCC wnt-beta-catenin: WNT/β-catenin on endothelial cells (already mapped) and macrophages (already mapped) regulates tumour vascularisation; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "HLRCC rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) modulates immune-vascular crosstalk; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "HLRCC smad4: SMAD4 in macrophages (already mapped) and endothelial cells (already mapped) mediates TGF-β vascular signalling; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "HLRCC fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "HLRCC notch: NOTCH on macrophages (already mapped) and endothelial cells (already mapped) regulates vascular-tumour lineage commitment; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "HLRCC igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes tumour metabolic growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "HLRCC activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes tumour fibrosis; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "HLRCC cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "HLRCC calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "HLRCC substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour neuroimmune tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "HLRCC insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "HLRCC aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "HLRCC androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "HLRCC norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "HLRCC adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC."
---

# Hereditary Leiomyomatosis and Renal Cell Carcinoma

## Overview

**Hereditary leiomyomatosis and renal cell carcinoma (HLRCC)**, also known as **Reed syndrome**, is an autosomal dominant hereditary cancer syndrome caused by germline pathogenic variants in **FH** (fumarate hydratase), the TCA cycle enzyme that converts fumarate to malate. HLRCC is characterized by a triad of manifestations: (1) **cutaneous leiomyomas** — benign piloerector smooth muscle tumors presenting as painful nodular skin lesions; (2) **uterine leiomyomas** (fibroids) — typically early onset (<30 years), symptomatic, large, and multiple, often requiring myomectomy or hysterectomy; and (3) **HLRCC-associated RCC** — an aggressive FH-deficient kidney cancer with distinctive collecting duct-like histology, early metastatic spread, and a prognosis that is dramatically worse than sporadic clear cell RCC. HLRCC-associated RCC is driven by fumarate-mediated pseudohypoxia (HIF-1α activation) and epigenetic reprogramming (TET2/KDM inhibition → DNA and histone hypermethylation). The current standard of care for HLRCC-associated metastatic RCC is **bevacizumab + erlotinib**, which achieves remarkable response rates (~65%) in this otherwise chemotherapy-resistant tumor [^tomlinson-2002-fh] [^linehan-2013-fh-review].

**Epidemiology:**
- Prevalence: very rare; estimated 1/200,000; ~1,500-2,000 HLRCC families worldwide
- Inheritance: autosomal dominant; 50% penetrance per generation; near-complete penetrance for cutaneous leiomyomas; incomplete penetrance for RCC
- FH germline pathogenic variant: identified in ~94% of clinically diagnosed HLRCC families; ~6% testing-negative families may have deep intronic or non-coding variants missed by standard testing
- Penetrance: cutaneous leiomyomas ~85-90% of carriers; uterine leiomyomas: ~90% of female carriers; HLRCC-associated RCC: ~15-20% of FH carriers (lifetime)
- Age of RCC: median age ~37 years (vs ~64 for sporadic ccRCC); RCC can occur in 2nd-3rd decade; early-onset RCC in a young person with cutaneous leiomyomas = pathognomonic for HLRCC

## Structure

### HLRCC clinical phenotype components

**Cutaneous leiomyomas:**
- Derived from arrector pili muscle (piloerector smooth muscle in hair follicle); NOT subcutaneous leiomyomas (from dartos muscle or blood vessel smooth muscle)
- Morphology: firm, skin-colored to brownish-red papules/nodules; 0.5-2 cm; dome-shaped
- Distribution: trunk (most common), extremities, face; frequently multiple (5-100 lesions)
- Symptoms: PAIN is the cardinal feature — spontaneous or triggered by pressure, cold, or anxiety; due to smooth muscle contraction; differentiates cutaneous leiomyoma from other skin lesions
- Histology: intersecting bundles of smooth muscle cells (cigar-shaped nuclei, eosinophilic cytoplasm) in dermis; Masson trichrome stain confirms smooth muscle; IHC: smooth muscle actin (SMA) and desmin positive
- FH IHC on leiomyoma: protein loss + 2SC positivity = FH-deficient leiomyoma = HLRCC

**Uterine leiomyomas (fibroids):**
- Hallmark features distinguishing HLRCC from sporadic fibroids:
  - Age of onset: typically age 20-30 (vs >35 for sporadic)
  - Number: multiple (often 5-20 or more)
  - Size: large (5-10 cm or greater)
  - Symptoms: menorrhagia, dysmenorrhea, infertility, pelvic pressure — often severe enough to require surgery by age 30-35
- Pathology: HLRCC fibroids are histologically identical to sporadic fibroids (smooth muscle fascicles); but FH IHC: loss + 2SC positivity distinguishes HLRCC from sporadic (sporadic: FH intact, 2SC negative)
- Somatic HLRCC fibroids: ~50% of all uterine fibroids have somatic FH biallelic LOF; this means routine fibroid pathology would identify FH-deficient tumors; not all FH-deficient fibroids arise from germline — most are sporadic somatic events

**HLRCC-associated RCC:**
- Histology: collecting duct-like carcinoma (formerly called type 2B papillary RCC); large cells with prominent macronucleoli surrounded by a clear halo ("owl eye" nuclei); papillary, tubulopapillary, or solid growth patterns; stroma with abundant desmoplasia
- IHC: FH-/2SC+ (diagnostic); CK7+, PAX8+, CD10 variable; WT1 negative; CK20 negative; tethered to renal medulla/collecting duct area
- Molecular: biallelic FH LOF (germline + somatic, or two somatic events); no VHL mutation; VEGFR and EGFR overexpressed; HIF-1α and HIF-2α nuclear; GLUT1 high
- Aggressive behavior: often presents at Stage IV (metastatic) — nodal and distant metastases; even small primary tumors can metastasize; unlike ccRCC where a 2 cm tumor is almost always cured by nephrectomy, FH-deficient RCC can metastasize at 1-2 cm

## Function

### Fumarate-driven oncogenesis in HLRCC

**Pseudohypoxic signaling:** [^linehan-2013-fh-review]
FH LOF → fumarate accumulates → inhibits PHD1/2/3 (prolyl hydroxylase domain enzymes; normally hydroxylate HIF-1α at Pro-402, Pro-564 using α-KG and O2) → HIF-1α not hydroxylated → VHL E3 ligase cannot bind → HIF-1α escapes proteasomal degradation → HIF-1α nuclear (pseudohypoxic regardless of O2 tension) → transcriptional activation of HIF target genes:
- **VEGF/VEGFA**: angiogenesis → tumor vasculature → therapeutic target (bevacizumab)
- **GLUT1 (SLC2A1)**: glucose transporter → aerobic glycolysis (Warburg effect)
- **PDK1**: pyruvate dehydrogenase kinase 1 → blocks pyruvate entry into TCA → lactate instead of oxidative phosphorylation
- **LDHA**: lactate dehydrogenase A → lactate production → acidic microenvironment
- **CA9**: carbonic anhydrase 9 → pH regulation

**Epigenetic reprogramming:**
Fumarate competitive inhibition of α-KG-dependent dioxygenases:
- TET2 inhibition → 5mC not converted to 5hmC → progressive DNA methylation → CIMP-like → silencing of immune checkpoint genes, tumor suppressors, MMR genes
- KDM4A (H3K9me3), KDM5C (H3K4me3), KDM6A (H3K27me3) inhibition → heterochromatin expansion → gene silencing
- Consequence: FH-deficient tumors have a "cold" immune microenvironment (low TIL density, low PD-L1) due to epigenetic silencing of innate immune genes (STING, IFN pathway)

**KEAP1-NRF2 pathway activation:**
Fumarate succination of KEAP1 cysteines (C273, C288) → conformational change → KEAP1 cannot present NRF2 for CUL3-RBX1 E3 ubiquitination → NRF2 nuclear → antioxidant response element (ARE) genes: NQO1, GCLC, HMOX1, TXN, G6PD; NRF2 activation protects FH-deficient cells from oxidative stress; NRF2 also promotes pentose phosphate pathway (PPP) → NADPH production → reductive biosynthesis; NRF2 nuclear staining by IHC is a secondary marker of FH deficiency (not as specific as 2SC)

**Two-hit tumorigenesis:**
Germline FH pathogenic variant (first hit) → somatic LOH or second truncating mutation in a single renal tubular epithelial cell (second hit) → biallelic FH LOF → fumarate accumulation → tumorigenesis; LOH at 1q43 (FH locus) is the most common second hit in HLRCC RCC (~70%); somatic truncating mutation: ~25%; somatic FH missense: rare

## Pathology

### Diagnosis and genetic evaluation

**Clinical diagnostic criteria:**
Definite HLRCC: any of:
1. Cutaneous leiomyoma (histologically confirmed) + first-degree relative with HLRCC
2. Cutaneous leiomyoma + HLRCC-associated RCC
3. HLRCC-associated RCC + pathogenic FH germline variant
4. Multiple cutaneous leiomyomas with FH IHC loss + 2SC positivity on skin biopsy

Probable HLRCC:
- Multiple painful cutaneous leiomyomas alone (in the absence of FH testing)
- Early-onset symptomatic uterine fibroids in young woman with cutaneous leiomyomas
- Type 2B papillary/collecting duct-like RCC in a young patient → reflexively test FH IHC + 2SC

**Molecular diagnostic workup:**
1. FH germline sequencing (full coding + splice sites) + MLPA: preferred first-line
2. Tumor FH IHC + 2SC IHC: FH-/2SC+ confirms FH deficiency; triggers germline testing
3. FH enzyme activity assay (lymphocytes or fibroblasts): reduced activity confirms FH LOF; used when genetic testing inconclusive

**Surveillance recommendations (NCCN/ESMO 2024):**

Renal:
- Annual abdominal MRI (superior to CT for soft tissue characterization, avoids radiation) from time of genetic diagnosis
- Any renal mass ≥1 cm in FH carrier: biopsy vs immediate surgery (surgery preferred due to aggressive behavior; "see and treat" policy)
- Rationale: early detection is critical because even small tumors can metastasize in HLRCC

Uterine:
- Annual pelvic TVUS from age 20-25 in female FH carriers
- Symptom management: hormonal (OCP, progestins, GnRH agonists), surgical (myomectomy, hysterectomy)
- Fertility preservation: discussion with reproductive endocrinologist; early myomectomy before fibroids cause infertility may be appropriate
- Uterine fibroid embolization: generally avoided in HLRCC carriers (concerns about residual viable fibroid tissue)

Cutaneous:
- Dermatology evaluation: document and photograph skin lesions; confirm diagnosis by biopsy of most symptomatic lesion
- Pain management: calcium channel blockers (nifedipine, 10-30 mg/day: relaxes smooth muscle → reduces leiomyoma contraction pain); gabapentin for neuropathic pain component; topical nitroglycerin (vasodilation → reduced piloerector spasm); local excision for isolated symptomatic lesions

### Treatment of HLRCC-associated RCC

**Surgical management:**
- Localized HLRCC RCC: radical nephrectomy preferred (NOT partial nephrectomy); rationale: multifocal micrometastases may be present even in small tumor; wide excision
- Role of lymphadenectomy: recommended given high nodal metastasis rate
- Metastatic disease: cytoreductive nephrectomy benefit unclear in HLRCC (as in clear cell RCC); decision individualized; systemic therapy primary for Stage IV

**Bevacizumab + erlotinib (standard of care):** [^linehan-2013-fh-review]
- NCI HRCC Phase 2 trial (Srinivasan et al., updated 2021): N=43 HLRCC-associated and sporadic FH-deficient RCC; bevacizumab 15 mg/kg IV q21d + erlotinib 150 mg PO daily
- ORR: ~64-70% (predominantly partial responses by RECIST); DCR: ~90%
- mPFS: ~21.1 months; mOS: ~30 months (far exceeding historical controls on sunitinib/pazopanib where mPFS ~3-5 months in FH-deficient RCC)
- Mechanism: bevacizumab (anti-VEGF antibody) blocks VEGF-A → anti-angiogenic; erlotinib (EGFR-TKI) inhibits EGFR-driven VEGF production and cell proliferation; synergy: erlotinib reduces tumor-intrinsic VEGF secretion → enhances bevacizumab efficacy
- Toxicity: hypertension (~35%), proteinuria, GI (diarrhea, rash); erlotinib skin rash often precedes response
- Standard of care recommendation: per NCI/NCCN for HLRCC-associated metastatic RCC

**Alternative/investigational therapies:**
- **Sunitinib, pazopanib**: VEGFR-TKIs; inadequate in FH-deficient RCC (ORR ~10-15%, mPFS ~3-5 months); inferior to bevacizumab + erlotinib
- **Nivolumab + ipilimumab**: checkpoint inhibitor combination; being evaluated in FH-deficient RCC (NCI basket trial); rationale: despite cold baseline tumor, IO combinations may overcome epigenetic immunosuppression
- **Belzutifan (HIF-2α inhibitor)**: FDA-approved for VHL-associated ccRCC; Phase 2 in FH-deficient RCC (NCT04895748): early response data pending; HIF-2α active in HLRCC RCC alongside HIF-1α
- **PARP inhibitors**: FH-deficient cells may have HR deficiency (cytosolic FH at DSBs → fumarate → KDM2A inhibition → HR/NHEJ imbalance); olaparib explored in FH-deficient tumor basket
- **mTOR inhibitors**: fumarate → HIF-1α → mTOR signaling; everolimus not well-studied in HLRCC RCC specifically; less potent than bevacizumab + erlotinib

**Prognosis:**
- Localized HLRCC RCC (Stage I-II): surgical cure achievable; ~60-70% 5-year survival with nephrectomy + surveillance
- Locally advanced/Stage III: 5-year survival ~30-40% with surgery; adjuvant systemic therapy role uncertain
- Metastatic HLRCC RCC (Stage IV): historically median OS <12 months; with bevacizumab + erlotinib: median OS ~30 months; responses can be durable (some patients >5 years on treatment); treatment-free interval difficult as off-treatment disease progression is rapid

## Connections

- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — Germline FH mutations cause HLRCC (autosomal dominant); FH LOF → fumarate accumulation; 2SC IHC (anti-2-succino-cysteine) positive in FH-deficient tumors; FH IHC loss diagnostic; somatic second hit (LOH or second mutation) in each HLRCC leiomyoma or RCC
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — HLRCC-associated RCC driven by HIF-1α pseudohypoxia (FH LOF → PHD inhibition → HIF-1α stabilized); VEGF/HIF-1α pathway active; bevacizumab (anti-VEGF) + erlotinib standard for HLRCC RCC; HIF-2α inhibitor belzutifan being explored in FH-deficient RCC
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — HLRCC-associated RCC is pseudohypoxic similar to VHL-mutant ccRCC (both have HIF-1α and VEGF overexpression); histologically distinct (type 2B papillary/collecting duct-like, NOT clear cell); anti-VEGF therapies active in both; belzutifan explored in FH-deficient RCC
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — HLRCC-associated RCC: most aggressive hereditary RCC; collecting duct-like/papillary type 2B; often metastatic at diagnosis; FH IHC loss + 2SC positivity diagnostic; bevacizumab + erlotinib standard (NCI Phase 2, ORR ~64%, mPFS 21 months); sunitinib/pazopanib insufficient
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — HLRCC produces multiple smooth muscle tumors (leiomyomas): painful cutaneous nodules from arrector pili muscle and early-onset, large, multiple uterine fibroids; biallelic FH loss drives them, and FH-/2SC+ immunostaining distinguishes HLRCC leiomyomas from sporadic ones.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Fumarate accumulation stabilizes HIF-1α (pseudohypoxia) → VEGF transcription → tumor angiogenesis; this is the therapeutic handle in FH-deficient RCC — bevacizumab (anti-VEGF) plus erlotinib (anti-EGFR) achieves ~65% response, far exceeding VEGFR-TKIs like sunitinib.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — HLRCC causes the most aggressive hereditary kidney cancer — collecting-duct-like/type-2B papillary RCC that can metastasize even at 1-2 cm; radical (not partial) nephrectomy with lymphadenectomy is preferred, and annual renal MRI surveillance starts at genetic diagnosis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The uterus is often where HLRCC declares itself: women develop numerous, large, early-onset uterine leiomyomas (fibroids), frequently needing myomectomy or hysterectomy before age 30 — so multiple early fibroids with cutaneous leiomyomas should prompt FH testing.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous leiomyomas are the 'L' of HLRCC and its visible clue: firm, often painful skin-colored papules from arrector pili smooth muscle appearing in the 20s-30s; their recognition (with FH/2SC staining) flags the syndrome years before the aggressive kidney cancer.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — HLRCC's FH belongs to the same Krebs-cycle, pseudohypoxia family (SDHx, FH) that causes hereditary pheochromocytoma/paraganglioma: FH loss accumulates fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF — so rare FH-mutant PPGLs occur, sharing fumarate-driven biology.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — HLRCC and VHL disease are both hereditary kidney-cancer syndromes converging on pseudohypoxia: VHL loss stabilizes HIF directly, while HLRCC's FH loss raises fumarate that blocks the HIF prolyl-hydroxylases. HLRCC papillary RCC is far more aggressive than VHL clear-cell tumors.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — HLRCC and tuberous sclerosis are inherited syndromes that both cause renal tumors and smooth-muscle lesions: TSC drives angiomyolipomas and renal cysts via mTOR, while HLRCC's FH loss drives aggressive papillary RCC plus cutaneous and uterine leiomyomas.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — HLRCC illustrates pseudohypoxia's effect on red cells: fumarate accumulation stabilizes HIF as if oxygen were low, and HIF transcribes erythropoietin—so FH-deficient and other TCA-cycle tumors can drive secondary polycythemia and a raised erythrocyte mass.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — HLRCC and Birt-Hogg-Dubé are both hereditary kidney-cancer syndromes with distinct genes: HLRCC's FH loss yields type 2 papillary RCC and cutaneous/uterine leiomyomas, while BHD's FLCN loss gives chromophobe/oncocytic tumors, lung cysts and skin fibrofolliculomas.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — HLRCC's FH defect strikes the uterus as well as the kidney: fumarate-hydratase loss drives the cutaneous and uterine leiomyomas of the syndrome, and FH-deficient uterine tumors and endometrial cancers can arise—so gynecologic surveillance complements renal screening.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — HLRCC and Cowden syndrome are both dominant syndromes raising kidney cancer risk via different pathways: HLRCC from FH loss (a Krebs-cycle/pseudohypoxia defect), Cowden from PTEN loss (PI3K-AKT)—each adds a distinct extrarenal tumor spectrum.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — HLRCC tumors fake hypoxia: accumulated fumarate from FH loss inhibits the oxygen-sensing prolyl hydroxylases, so HIF stabilizes as if oxygen were scarce—this pseudohypoxia drives VEGF and the aggressive angiogenic type-2 papillary kidney cancers of the syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — HLRCC cancers lean on mTOR and angiogenesis for growth: fumarate-driven pseudohypoxia and metabolic rewiring activate growth signaling, which is why advanced HLRCC renal cancer is treated with combined VEGF and EGFR/mTOR-pathway-directed therapy rather than standard regimens.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HLRCC shows how a metabolic gene becomes oncogenic: fumarate accumulation inactivates proteins and impairs DNA-damage responses including p53, so a Krebs-cycle enzyme defect causes genomic instability—an oncometabolite route to cancer.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Skin tumors are usually the first sign of HLRCC: FH loss causes multiple cutaneous piloleiomyomas—firm, sometimes painful smooth-muscle nodules—so a dermatologist often flags the syndrome before its aggressive kidney cancer appears.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — HLRCC is a disease of carbon metabolism gone wrong: losing fumarate hydratase stalls the Krebs cycle so the carbon metabolite fumarate piles up as an oncometabolite, stabilizing HIF and modifying proteins to drive cancer—linking a metabolic enzyme to malignancy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — FH-deficient HLRCC kidney cancer engages the immune system: these aggressive tumors are often treated with combinations of immune checkpoint inhibitors and anti-angiogenic agents, reflecting how the metabolic defect reshapes the tumor's vasculature and immune milieu.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — HLRCC is an oncometabolite cancer like IDH-mutant glioma: loss of fumarate hydratase floods cells with fumarate which—like glioma's 2-hydroxyglutarate—inhibits dioxygenases, stabilizes HIF, and rewires epigenetics, so two enzymes converge on metabolite-driven cancer.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — HLRCC kidney cancer spreads early to the lung: its type 2 papillary renal cell carcinoma is unusually aggressive and metastasizes while small, often to the lungs—so HLRCC carriers need vigilant renal surveillance and prompt surgery.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — HLRCC's cutaneous leiomyomas are firm, collagen-rich nodules: smooth-muscle tumors set in dense dermal collagen form papules that hurt with cold or touch, so these tender skin lumps are often the first sign pointing to an FH mutation.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — HLRCC tumors survive by hijacking NRF2: accumulated fumarate chemically modifies KEAP1, freeing the antioxidant master switch NRF2 to shield the cancer from oxidative stress—a key vulnerability being targeted in FH-deficient kidney cancer.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — FH loss forces HLRCC cells to make ATP by glycolysis: with the Krebs cycle broken, the tumor can't run normal oxidative phosphorylation, so it shifts to aerobic glycolysis (the Warburg effect) for energy—a metabolic weakness drugs aim to exploit.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — HLRCC's aggressive kidney cancer is met with immunotherapy: because FH-deficient tumors are highly angiogenic and immune-active, regimens combining checkpoint drugs (engaging NK and T cells) with anti-angiogenics are used against this hard-to-treat cancer.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — HLRCC kidney cancer leans on the AKT-mTOR growth axis: FH loss and its metabolic stress activate AKT and mTOR signaling, so this pathway joins the pseudohypoxic HIF program in driving the tumor, and is probed as a drug target.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages crowd HLRCC's tumor microenvironment: tumor-associated macrophages promote angiogenesis and immune suppression around the FH-deficient kidney cancer, shaping a stroma that the immunotherapy combinations try to flip.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are key to attacking HLRCC: because FH-deficient tumors are immune-active and antigen-rich, antigen-presenting dendritic cells help prime the T-cell response that checkpoint and vaccine strategies aim to unleash.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — FH mutations can sprout adrenal tumors: beyond skin and uterine leiomyomas and aggressive kidney cancer, the same fumarate-hydratase defect predisposes to pheochromocytomas and paragangliomas, including in the adrenal glands.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — HLRCC's kidney cancer bleeds iron away: the aggressive renal tumor causes blood in the urine, so hematuria and the iron-deficiency anemia it brings can be the warning that prompts imaging.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — HLRCC tumors are intensely vascular: losing FH stabilizes HIF, which drives VEGF and pushes endothelial cells to build a rich blood supply, the angiogenesis that anti-VEGF therapy targets.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — HLRCC demands aggressive imaging surveillance: because its kidney cancer spreads early, MRI and CT photons screen carriers from young adulthood to catch the tumor before it metastasizes.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — HLRCC's renal tumor builds a desmoplastic stroma: its aggressive type-2 papillary cancer grows amid dense fibrous tissue, alongside the firm collagen-rich leiomyomas of skin and uterus.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — HLRCC's kidney cancer spreads far and fast: its early, aggressive metastasis can reach the brain along with bone and lung, a grim contrast to the indolent renal tumors of related syndromes.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — HLRCC poisons the cell with an oncometabolite: losing fumarate hydratase backs up fumarate, which jams the enzymes that sense oxygen and edit DNA — the metabolic short-circuit driving its leiomyomas and aggressive kidney cancer.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — HLRCC's renal cancer races to the skeleton: unlike the indolent tumors of related syndromes, its type-2 papillary RCC metastasizes early to bone and the marrow within, alongside lung and brain.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The aggressive kidney cancer also seeds the liver: HLRCC's renal tumors spread hematogenously to multiple organs, the liver among the sites that mark its grim, fast-moving metastatic course.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody both diagnoses and treats HLRCC: the 2SC immunostain marks the fumarate-modified proteins that betray FH loss, while the anti-VEGF antibody bevacizumab — with erlotinib — is a mainstay against its kidney cancer.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — HLRCC's skin tumors hurt through nerves: the cutaneous leiomyomas are richly innervated piloleiomyomas that fire painfully with cold and touch, a distinctive symptom that flags the syndrome.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Its targeted therapy reaches the gut: the erlotinib paired with bevacizumab for HLRCC kidney cancer causes diarrhea and an acneiform rash, while bevacizumab itself carries a risk of bowel perforation.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — The pseudo-hypoxia can overfill the blood: FH loss stabilizes HIF, which switches on erythropoietin, so HLRCC kidney tumors can drive a paraneoplastic erythrocytosis — too many red cells from a falsely sensed lack of oxygen.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — HLRCC sits opposite the other inherited papillary kidney cancer: its FH-driven type 2 papillary RCC contrasts with MET-activated hereditary papillary RCC type 1, so the gene at fault tells which papillary syndrome — and which course — a patient has.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy joins the HLRCC toolkit: its aggressive FH-deficient kidney cancers can respond to checkpoint inhibitors that unleash cytotoxic T cells, used alongside the bevacizumab-erlotinib backbone against this hard-to-treat tumor.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The benign tumors are mesenchymal: HLRCC's hallmark cutaneous and uterine leiomyomas are smooth-muscle and fibroblast-like growths of FH-deficient cells, the skin nodules and fibroids that flag the syndrome before the kidney cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — A blocked Krebs cycle starves the cell of energy: FH loss stalls the TCA cycle and forces a Warburg shift, a metabolic stress sensed by AMPK as the FH-deficient cell rewires its metabolism to survive.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — It joins the multisystem tumor-suppressor syndromes: like neurofibromatosis type 1, HLRCC is a single-gene disorder with cutaneous tumors and a predisposition to renal and adrenal/paraganglionic tumors, distinguished by its gene and metabolic mechanism.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — FH and SDH are sister Krebs-cycle tumor suppressors: like SDHB loss, FH loss floods the cell with an oncometabolite (fumarate) that stabilizes HIF and reprograms the epigenome — a shared pseudo-hypoxic mechanism across the metabolic cancer syndromes.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — The uterine leiomyomas bleed: women with HLRCC develop numerous, often symptomatic uterine fibroids whose heavy menstrual bleeding causes iron-deficiency anemia, frequently the first sign that brings them to attention.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its renal cancer is aggressive and clot-prone: HLRCC-associated renal cell carcinoma metastasizes early, and like other advanced cancers it carries a raised risk of venous thromboembolism through surgery and treatment.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — An oncometabolite rewires the cell's signaling: fumarate accumulating from FH loss succinates proteins and, alongside its activation of NRF2 and HIF, engages NF-κB-linked survival and inflammatory signaling in HLRCC tumors.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Saving the kidney costs function: the aggressive renal cell carcinoma of HLRCC demands prompt, sometimes radical surgery, and the loss of renal tissue across a lifetime of surveillance can drift toward chronic kidney disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Advanced renal cancer and its therapy invite infection: metastatic HLRCC kidney cancer and the systemic treatment it requires can cause the immune compromise and complications that lead to sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its aggressive kidney cancer drags the count down: the inflammatory burden of HLRCC's early-metastasizing renal cell carcinoma, with nephron loss and surgery, contributes an anemia of chronic disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its antiangiogenic therapy strains the heart: the bevacizumab-erlotinib and VEGF-targeted regimens used for HLRCC-associated renal cancer cause hypertension and cardiotoxicity that can contribute to heart failure.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive hereditary cancer weighs on the mind: living with the high risk of an early, aggressive kidney cancer and the demands of lifelong surveillance imposes a substantial psychological burden in HLRCC.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its leiomyomas are notoriously painful: the cutaneous leiomyomas of HLRCC cause cold- and touch-triggered pain, and uterine fibroids add severe pelvic pain, together producing chronic neuropathic and nociceptive pain.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Repeated tumor surgery taxes healing: the excisions of multiple cutaneous leiomyomas and nephron-sparing or radical kidney surgery in HLRCC leave recurrent wounds to heal.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Aggressive cancer risk and surveillance breed worry: the threat of an early, aggressive type 2 papillary kidney cancer and the lifelong imaging surveillance of HLRCC foster chronic health anxiety.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It seeds smooth-muscle tumours: HLRCC causes multiple painful cutaneous and uterine leiomyomas — benign tumours of smooth muscle — its defining non-renal feature.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones feed its fibroids and metabolism runs awry: the uterine leiomyomas of HLRCC are oestrogen-sensitive, and loss of fumarate hydratase reroutes Krebs-cycle metabolism toward a pseudohypoxic state.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its kidney cancer is aggressive and early: HLRCC causes a particularly aggressive type 2 papillary renal cell carcinoma that metastasises early, demanding prompt nephrectomy and close surveillance.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its kidney cancer races to the lungs: the aggressive type 2 papillary renal cell carcinoma of HLRCC metastasises early and frequently to the lungs, so chest imaging is part of surveillance.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads early to the nodes: HLRCC renal cell carcinoma involves regional and retroperitoneal lymph nodes early, a marker of its unusual aggressiveness among kidney cancers.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its metabolic defect drives tumour vessels: fumarate hydratase loss stabilises HIF in a pseudohypoxic state that boosts VEGF and tumour vascularity, the rationale for anti-VEGF bevacizumab-based therapy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It needs a tailored regimen: the aggressive type-2 papillary RCC of HLRCC is treated by combining anti-VEGF and EGFR-targeted agents (bevacizumab plus erlotinib) rather than the standard kidney-cancer drugs.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its kidney cancer spreads early and far: the type-2 papillary RCC of HLRCC metastasises rapidly, including to the brain, even from small primary tumours.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It reaches the liver and reshapes metabolism: HLRCC's renal cancer commonly metastasises to the liver, and the fumarate-hydratase defect drives a Warburg-like metabolic shift in its cells.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy enters its treatment: like other renal cell cancers, the FH-deficient RCC of HLRCC is treated with PD-1 checkpoint inhibitors, usually combined with anti-angiogenic kinase inhibitors.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Two routes to too many red cells: HLRCC's HIF stabilisation can drive erythropoietin-mediated secondary erythrocytosis, the differential of the primary, JAK2-driven erythrocytosis of polycythaemia vera.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — A fellow autosomal-dominant tumour syndrome: like MEN1, HLRCC is an inherited predisposition to characteristic tumours, here uterine and skin leiomyomas with aggressive kidney cancer.
- `connects-to` → **[GIST](../gist/README.md)** — Krebs-cycle enzymes as tumour suppressors: HLRCC loses fumarate hydratase while SDH-deficient GIST and paraganglioma lose succinate dehydrogenase—each crippled TCA enzyme floods the cell with an oncometabolite and a pseudohypoxic, angiogenic phenotype.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — The tumour hijacks the antioxidant switch: accumulated fumarate succinates KEAP1, constitutively activating NRF2 in HLRCC—the very transcription factor dietary sulforaphane induces—so the cancer permanently turns on the protective programme broccoli only transiently mimics.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Sharing a hijacked NRF2 pathway: HLRCC switches on NRF2 through fumarate, while squamous non-small-cell lung cancer activates the same antioxidant programme via NFE2L2/KEAP1 mutations—both gaining oxidative-stress resistance and chemoresistance from one pathway.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Oncometabolite cancers: HLRCC's fumarate, like the 2-hydroxyglutarate of IDH-mutant cholangiocarcinoma and glioma, is an oncometabolite that reprograms the epigenome and stabilises HIF—a shared metabolic route to cancer.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Early lung metastasis: the type-2 papillary renal cancer of HLRCC is aggressive and metastasises early, seeding the lungs and the alveolar capillary bed even from small primaries.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Painful skin tumours: the cutaneous leiomyomas of HLRCC are characteristically tender, painful to cold and touch, a clinical clue rooted in their nerve-rich smooth-muscle origin.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A hypervascular cancer: FH loss stabilises HIF, so HLRCC's type-2 papillary kidney cancer is intensely angiogenic, building abnormal vasculature targeted by VEGF/EGFR therapy (bevacizumab-erlotinib).
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Aggressive bone metastasis: HLRCC's type-2 papillary renal cancer spreads early and aggressively, seeding the cortical bone among lung and liver as it disseminates.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: the aggressive renal cancer of HLRCC readily spreads to the liver, seeding the hepatic lobules, part of its tendency to metastasise even from a small primary.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — Oncometabolite epigenetics: fumarate accumulating from FH loss inhibits TET DNA-demethylases, causing the DNA hypermethylation that silences tumour-suppressor genes in HLRCC.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — Shared oncometabolite mechanism: like IDH-mutant cancers making 2-hydroxyglutarate, FH-deficient HLRCC accumulates fumarate—both oncometabolites that inhibit the same α-ketoglutarate-dependent enzymes.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Reinforced silencing: the histone hypermethylation driven by fumarate, together with polycomb/EZH2 activity, locks in the repressed, dedifferentiated state of HLRCC tumour cells.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Metabolic-oncogene cooperation: the pseudohypoxic, fumarate-driven state of HLRCC upregulates MYC, fuelling the biosynthesis and proliferation of its aggressive type-2 papillary renal tumours.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: HIF-driven and growth-factor signalling in FH-deficient HLRCC upregulates cyclin D1, pushing the renal tumour cells through the G1 checkpoint.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in HLRCC renal tumours, enabling the limitless proliferation of this notably aggressive hereditary kidney cancer.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — Pseudohypoxia mechanism: fumarate accumulating from FH loss competitively inhibits the EGLN/PHD prolyl hydroxylases, blocking HIF degradation to create the pseudohypoxic, angiogenic state that drives HLRCC.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK proliferation: RAS-RAF-ERK signalling, alongside the MET pathway, drives the proliferation of the aggressive type 2 papillary renal cancer of HLRCC.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into HLRCC renal tumours, shaping the microenvironment of this metabolically reprogrammed, immunologically active cancer.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Accumulating fumarate suppresses homologous-recombination repair by impairing RAD51-pathway function, creating a "BRCAness"-like state in FH-deficient HLRCC tumors that may confer sensitivity to PARP inhibitors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on the type 2 papillary renal cancer of HLRCC follows CXCL12 gradients to drive the early, aggressive metastasis that distinguishes this hereditary kidney cancer from the indolent tumors of other syndromes.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The metabolic reprogramming of FH-deficient HLRCC cells confers resistance to caspase-3-mediated apoptosis, part of the survival advantage that makes these tumors so aggressive and treatment-resistant.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Accumulated fumarate in FH-deficient HLRCC inhibits the TET DNA-demethylases, producing a globally hypermethylated genome that silences tumor-suppressor genes—the epigenetic consequence of the oncometabolite.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — The combination of the anti-VEGF antibody bevacizumab with the EGFR inhibitor erlotinib is an effective regimen for HLRCC-associated papillary renal cell carcinoma, hitting the angiogenic and growth-factor arms of these aggressive tumors.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — HLRCC causes estrogen-dependent uterine fibroids that are typically numerous, early-onset and symptomatic, often the first manifestation of the syndrome in affected women and a clue to the FH mutation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR axis (AKT, mTOR and AMPK already mapped) active in HLRCC renal cancer, a rationale for the bevacizumab-erlotinib and mTOR-directed regimens used in this aggressive papillary RCC.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1 axis (mapped) drives RB phosphorylation that releases E2F1, powering the cell-cycle entry of the aggressive type-2 papillary renal cancer of HLRCC.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss removes restraint on the cyclin-D-CDK4/6 axis, a cooperating lesion in the malignant progression of HLRCC renal tumors.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — The VEGF/PDGF angiogenic axis (VEGF already mapped) drives the highly vascular type-2 papillary renal cell carcinoma of HLRCC and is targeted by the tyrosine-kinase inhibitors used in its treatment.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) provides a proliferative input downstream of MET and EGFR in the aggressive renal tumors of HLRCC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) restrains proliferation, and its disruption contributes to the aggressive growth of HLRCC-associated renal cancer.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — Fumarate accumulation inhibits prolyl hydroxylases (EGLN1 mapped) and stabilizes HIF-2α (EPAS1), the pseudohypoxic driver of the renal cancers of HLRCC.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates survival and the microenvironment of the aggressive type-2 papillary renal cancers of HLRCC.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) shapes proliferation in HLRCC-associated tumors.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of the aggressive FH-deficient renal cancer of HLRCC.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Fumarate accumulation and mitochondrial dysfunction from FH loss release cytosolic DNA that can engage cGAS-STING in the tumors of HLRCC.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of the HLRCC-associated tumors.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a pro-apoptotic brake in the aggressive renal carcinoma of HLRCC.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-treated HLRCC renal carcinoma must evade.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the HLRCC-associated tumors.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the NRF2 and survival signaling (NFE2L2 already mapped) that the fumarate accumulation of HLRCC dysregulates.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the FH-deficient cells of HLRCC under metabolic and oxidative stress.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the aggressive type 2 papillary renal tumors of HLRCC.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the renal tumors of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of MET and other receptor tyrosine kinases (MET already mapped) participates in the invasive signaling of the renal tumors of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling participates in the tumor-microenvironment and survival signaling of the aggressive renal cancer of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary leiomyomatosis and renal cell cancer.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Uterine leiomyoma hormones: the uterine smooth-muscle tumours of HLRCC, like common fibroids, are hormone-responsive, so progesterone and estrogen (already mapped) drive the growth that causes heavy bleeding and often early hysterectomy in affected women.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — RCC immunotherapy: MHC class II antigen presentation shapes the T-cell response to the aggressive FH-deficient renal cell carcinoma of HLRCC, whose systemic treatment increasingly combines antiangiogenics with immune checkpoint blockade.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2-driven T-cell expansion underlies the immunotherapy of the metastatic renal cell carcinoma that makes HLRCC dangerous, complementing the bevacizumab-erlotinib regimen aimed at its pseudohypoxic biology (HIF already mapped).
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Polycythaemia and haematuria: the pseudohypoxic HIF and erythropoietin drive (already mapped) can raise haemoglobin, while the renal cell carcinoma of HLRCC causes haematuria and, later, the anaemia of advanced disease.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with the strongly upregulated VEGF (already mapped) supports the rich angiogenesis of the pseudohypoxic FH-deficient renal cell carcinoma, part of the vascular biology targeted by antiangiogenic therapy.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and antioxidant stress: fumarate accumulation succinates KEAP1 to activate NRF2 (already mapped), a response to the oxidative stress, to which xanthine oxidase contributes, of the metabolically rewired FH-deficient cell.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment of the aggressive FH-deficient renal cell carcinoma dampens the anti-tumour T-cell response (CD8 already mapped), part of the immune evasion relevant to its immunotherapy.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the HLRCC tumour stroma, part of its immune-evasive microenvironment.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Leiomyoma pain and inflammation: prostaglandins contribute to the pain of the cutaneous piloleiomyomas and to the inflammatory microenvironment of the FH-deficient tumours of HLRCC.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the FH-deficient tumours of HLRCC.
- `connects-to` → **[Birt-Hogg-Dubé syndrome](../birt-hogg-dube-syndrome/README.md)** — Hereditary-RCC syndromes: HLRCC sits among the hereditary renal cell carcinoma syndromes with Birt-Hogg-Dubé and VHL (already mapped), the group of germline predispositions to distinct renal cancers requiring surveillance.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haematuria and anaemia: the aggressive type-2 papillary renal cancer of HLRCC can bleed, causing the haematuria and iron-deficiency anaemia (haemoglobin already mapped) that reflect the renal tumour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic reprogramming adipokine: leptin connects to the FH-driven metabolic reprogramming (AMPK already mapped) of HLRCC, part of the adipokine dimension of its altered energy metabolism.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — AMPK-linked adipokine: adiponectin, with leptin (already mapped), activates the AMPK (already mapped) energy metabolism disturbed by the fumarate-hydratase loss of HLRCC.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of HLRCC.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of the aggressive HLRCC papillary renal cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the HLRCC renal cancer.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Prognostic neutrophils: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are prognostic in the aggressive renal cancer of HLRCC.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-tumour immune microenvironment of the HLRCC renal cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of the HLRCC tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of HLRCC.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of HLRCC.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells infiltrate the leiomyomas and the papillary-RCC stroma and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of HLRCC.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HLRCC tumours.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the FH-deficient HLRCC renal tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the HLRCC tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the FH-deficient, pseudohypoxic (HIF-1α already mapped) HLRCC papillary renal tumours.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) amplify the myeloid recruitment and the tumour-microenvironment inflammation in the FH-mutant HLRCC renal tumours.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: FH-mutant HLRCC renal tumour cells upregulate factor H to bind C3b and block the alternative pathway (C3, C5 and C5aR1 already mapped), escaping complement-mediated lysis.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Desmoplastic stroma: TGF-β drives the fibroblast and collagen deposition (both already mapped) of the desmoplastic stroma of the HLRCC type-2 papillary renal tumours, promoting invasion.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin in leiomyomas: TSLP secreted by the uterine smooth-muscle cells (already mapped) of HLRCC leiomyomas primes the mast cells (already mapped) to sustain the type-2 inflammatory stromal microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vasoactive kinin in pseudohypoxic tumours: bradykinin promotes vasodilation and VEGF-driven angiogenesis (VEGF already mapped) in the pseudohypoxic (HIF-1α already mapped) HLRCC papillary renal tumours.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical pathway regulation: C1-INH controls the classical-pathway arm (C3, C5, C5aR1 and factor H already mapped) of the complement cascade activated against the FH-deficient HLRCC renal tumour cells, limiting complement-mediated lysis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-HLRCC axis: histamine, released by mast cells in the HLRCC tumour microenvironment, signals via H1/H2 receptors on FH-mutant (already mapped) tumour cells and endothelium, modulating angiogenesis and the immunosuppressive milieu of HLRCC renal cancers.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-HLRCC axis: melatonin, via MT1/MT2 receptors on FH-mutant (already mapped) HLRCC cells, modulates the HIF-1α-driven (already mapped) pseudohypoxic metabolism, suppresses Warburg-effect-dependent proliferation, and enhances apoptotic sensitivity.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-HLRCC axis: testosterone, via androgen receptor signalling on FH-mutant (already mapped) renal and uterine tumour cells, modulates HIF-1α (already mapped) target-gene expression and the sex-biased aggressiveness of HLRCC-associated renal cell carcinoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — HLRCC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — HLRCC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the tumour inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HLRCC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the tumour; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of HLRCC.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — HLRCC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of HLRCC.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — HLRCC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of HLRCC.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HLRCC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of HLRCC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HLRCC sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and T-cytotoxic (already mapped) suppression; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies tumour-promoting cascade of HLRCC.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HLRCC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HLRCC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — HLRCC chloride: chloride channels regulate macrophage (already mapped) and T-cytotoxic (already mapped) volume during tumour-microenvironment stress; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade in HLRCC.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — HLRCC nitrogen: nitrogen as backbone of oncoproteins and cytokines (already mapped) sustains tumour signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting inflammatory cascade in HLRCC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — HLRCC potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — HLRCC calcium: calcium signals macrophage (already mapped) and T-cytotoxic (already mapped) immune activation in tumour microenvironment; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — HLRCC hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of HLRCC.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HLRCC phosphorus: phosphorus as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of HLRCC.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — HLRCC pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses FH-deficient tumour immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — HLRCC glp-1: GLP-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) tumour cascade of HLRCC.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — HLRCC angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[WNT/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — HLRCC wnt-beta-catenin: WNT/β-catenin on endothelial cells (already mapped) and macrophages (already mapped) regulates tumour vascularisation; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — HLRCC rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) modulates immune-vascular crosstalk; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — HLRCC smad4: SMAD4 in macrophages (already mapped) and endothelial cells (already mapped) mediates TGF-β vascular signalling; smad4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — HLRCC fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — HLRCC notch: NOTCH on macrophages (already mapped) and endothelial cells (already mapped) regulates vascular-tumour lineage commitment; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — HLRCC igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes tumour metabolic growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — HLRCC activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes tumour fibrosis; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — HLRCC cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — HLRCC calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — HLRCC substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour neuroimmune tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — HLRCC insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — HLRCC aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — HLRCC androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — HLRCC norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — HLRCC adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and HIF-1α (already mapped) cascade of HLRCC.

[^tomlinson-2002-fh]: Tomlinson IP, Alam NA, Rowan AJ, et al. Germline mutations in FH predispose to dominantly inherited uterine fibroids, skin leiomyomata and papillary renal cell cancer. *Nat Genet.* 2002;30(4):406-410. [doi:10.1038/ng849](https://doi.org/10.1038/ng849) · [PubMed 11865300](https://pubmed.ncbi.nlm.nih.gov/11865300/)
[^linehan-2013-fh-review]: Linehan WM, Rouault TA. Molecular pathways: fumarate hydratase-deficient kidney cancer — targeting the Warburg effect in cancer. *Clin Cancer Res.* 2013;19(13):3345-3352. [doi:10.1158/1078-0432.CCR-13-0304](https://doi.org/10.1158/1078-0432.CCR-13-0304) · [PubMed 23836472](https://pubmed.ncbi.nlm.nih.gov/23836472/)
