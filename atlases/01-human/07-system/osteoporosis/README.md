---
schema: human-scale-entry/v1
id: osteoporosis
name: Osteoporosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Skeletal disease of low bone density and microarchitectural deterioration → fragility fractures. Driven by estrogen deficiency and osteoclast-osteoblast uncoupling; bisphosphonates, denosumab (RANKL inhibitor), and romosozumab (anti-sclerostin) reduce fracture risk."
aliases: ["osteopenia", "metabolic bone disease", "fragility fracture", "postmenopausal osteoporosis", "glucocorticoid-induced osteoporosis", "secondary osteoporosis"]
sources:
  - id: kanis-2019-who-osteoporosis
    type: peer-reviewed
    cite: "Kanis JA, Cooper C, Rizzoli R, Reginster JY; Scientific Advisory Board of the European Society for Clinical and Economic Aspects of Osteoporosis (ESCEO) and Committees of Scientific Advisors and National Societies of the International Osteoporosis Foundation (IOF). European guidance for the diagnosis and management of osteoporosis in postmenopausal women. Osteoporos Int. 2019;30(1):3-44."
    doi: "10.1007/s00198-018-4704-5"
    pmid: "30324412"
    url: "https://doi.org/10.1007/s00198-018-4704-5"
  - id: cosman-2016-romosozumab
    type: peer-reviewed
    cite: "Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. N Engl J Med. 2016;375(16):1532-1543."
    doi: "10.1056/NEJMoa1607948"
    pmid: "27641143"
    url: "https://doi.org/10.1056/NEJMoa1607948"
  - id: cummings-2009-denosumab-freedom
    type: peer-reviewed
    cite: "Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. N Engl J Med. 2009;361(8):756-765."
    doi: "10.1056/NEJMoa0809493"
    pmid: "19671655"
    url: "https://doi.org/10.1056/NEJMoa0809493"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta released from bone matrix during osteoclastic resorption → chemoattractant for osteoblast precursors → bone formation coupling signal; excess TGF-beta (PTH-driven or tumor-derived) → uncoupled osteoclast activation → metastasis-associated bone destruction."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives RANKL-independent osteoclastogenesis via JAK-STAT3 → osteoclast precursor differentiation; elevated IL-6 in postmenopausal women, RA, and multiple myeloma → accelerated bone loss; tocilizumab reduces bone erosion in RA as a bone-protective effect."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen type I is the dominant organic bone matrix component; osteoblasts synthesize type I collagen → osteoid → mineralization; osteoclastic resorption → CTX and NTX (collagen telopeptides) → serum biomarkers of bone resorption used to monitor osteoporosis therapy."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteoclasts are the primary drivers of bone loss: RANKL (from osteoblasts/stromal cells) → RANK on osteoclast precursors → differentiation and lacunar resorption → BMD loss; denosumab (anti-RANKL) neutralizes RANKL → osteoclast suppression → fracture risk reduction."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Calcitonin → CTR → cAMP → osteoclast cytoskeletal collapse → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; reserved for acute pain of recent vertebral fracture."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "RANKL (TNFSF11) from osteoblasts/T cells → RANK on osteoclast precursors → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG decoy ratio governs bone mass; denosumab (anti-RANKL) → 68% vertebral and 40% hip fracture risk reduction (FREEDOM trial)."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Sclerostin (SOST) from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → net bone loss; mechanical loading suppresses sclerostin → anabolic response; romosozumab (anti-sclerostin) → +13% lumbar spine BMD at 12 months; 73% vertebral fracture RRR (FRAME)."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Hyperthyroidism accelerates bone remodeling → 10-20% BMD loss at trabecular sites; TSH receptors on osteoblasts exert bone-protective effects; Graves disease → osteoporosis risk; anti-thyroid treatment normalizes bone loss; bisphosphonates co-administered when BMD is low."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Osteoporosis is a failure of the osteoblast-osteoclast balance: bone-resorbing osteoclasts outpace bone-forming osteoblasts (estrogen loss, aging, steroids), so bone mass and microarchitecture deteriorate—anabolic drugs reverse it by favoring osteoblasts."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Osteoporosis is the commonest disease of the aging musculoskeletal system: silent bone loss until a fragility fracture (hip, vertebra, wrist) reveals it, and because fractures cause disability and death, bone-density screening and antiresorptives are core to skeletal health."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Menopause is the leading cause of osteoporosis: the sharp fall in ovarian estrogen accelerates osteoclast-driven bone resorption, so women lose bone rapidly after menopause—linking the reproductive system's hormonal shift to skeletal fragility and fracture risk."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is the mineral osteoporosis depletes: bone is the body's calcium reservoir, and when intake or absorption falls, parathyroid hormone pulls calcium from bone to keep blood levels constant—so chronic deficiency drives the net bone loss that weakens the skeleton."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D is essential to prevent osteoporosis: it drives intestinal calcium absorption, so deficiency causes secondary hyperparathyroidism that strips bone, and adequate vitamin D plus calcium is the foundation on which osteoporosis drug therapy is built."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol excess is a major cause of osteoporosis: glucocorticoids suppress osteoblasts, promote osteoclast survival and reduce calcium absorption, so both Cushing's syndrome and long-term steroid therapy cause rapid bone loss—the most common drug-induced osteoporosis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone is remodeled in concert with the marrow it houses: osteoporosis reflects an imbalance between osteoclasts and osteoblasts at the bone-marrow interface, and with age red marrow gives way to fat as bone is lost—linking declining marrow and skeletal mass."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium is an underappreciated factor in bone health: about half the body's magnesium sits in bone, and it is needed for vitamin D activation and PTH secretion, so chronic magnesium deficiency impairs mineralization and contributes to osteoporosis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Osteoporosis is largely an endocrine disease: estrogen, testosterone, thyroid hormone, parathyroid hormone and cortisol all govern bone turnover, so hormonal shifts (menopause, hyperthyroidism, steroid excess) are leading causes of bone loss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Bone is calcium-phosphate crystal, so phosphorus is as structural as calcium: hydroxyapatite needs balanced phosphate, and disordered phosphate handling—too little (osteomalacia) or the excess of kidney disease—weakens or distorts bone alongside calcium loss."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Rheumatoid arthritis is a double hit to bone: chronic inflammation (and RANKL) accelerates bone loss, and the glucocorticoids used to treat it cause steroid-induced osteoporosis—so inflammatory arthritis is a leading secondary cause of fragile bones."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Healthy bone depends on the gut: the intestine absorbs the calcium and vitamin D bone needs, so malabsorption from celiac disease, inflammatory bowel disease, or bariatric surgery is an under-recognized cause of osteoporosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Bone loss in aging tips marrow toward fat: the mesenchymal stem cells that should become bone-building osteoblasts instead become adipocytes, so marrow fills with fat as bone thins—linking the adipocyte-osteoblast balance to osteoporosis."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Multiple myeloma masquerades as severe osteoporosis: malignant plasma cells activate osteoclasts (via RANKL) to carve lytic lesions and cause fractures, so unexplained bone loss with anemia or high calcium prompts a myeloma workup."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Failing kidneys weaken bone—renal osteodystrophy: CKD disturbs phosphate, vitamin D and PTH, deranging bone turnover into a complex osteoporosis-plus-osteomalacia that standard bone drugs can worsen, so diagnosis must come first."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Bone formation runs on Wnt signaling, the lever osteoporosis drugs pull: Wnt/beta-catenin tells osteoblasts to build bone, and because sclerostin blocks it, antibodies against sclerostin (romosozumab) unleash Wnt to grow new bone."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine supplies the calcium that bone needs: it absorbs dietary calcium under vitamin D's control, so malabsorption from celiac disease or bypass surgery starves bone of calcium and accelerates osteoporosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Gut-made serotonin puts a brake on bone building: serotonin from the intestine circulates and tells osteoblasts to slow down, an unexpected gut-bone axis that helps explain why some serotonin-active drugs affect bone density."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Bone health is read and built with photons: a DXA scan uses low-dose X-ray photons to measure bone density and diagnose osteoporosis, while sunlight's photons make the vitamin D that lets bone absorb calcium."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach quietly guards bone: its acid frees calcium from food for absorption, so long-term acid-suppressing drugs (PPIs) can reduce calcium uptake and are linked to a higher fracture risk."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Too much salt thins the bones: high dietary sodium makes the kidneys excrete more calcium in urine, and that ongoing calcium drain pulls mineral from bone, quietly worsening osteoporosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Bone-eating osteoclasts arise from macrophages: the monocyte-macrophage lineage fuses into the osteoclasts that resorb bone, so inflammation that recruits macrophages accelerates bone loss."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver takes the first step in activating vitamin D: it hydroxylates it to 25-OH-D, the stored form measured in blood, before the kidney finishes the job, so liver disease can starve bone of usable vitamin D."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc helps build bone: it is a cofactor for the enzymes that lay down collagen matrix and for osteoblast activity, so zinc deficiency contributes to low bone mass."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows osteoporosis as a hollowing-out: the bone's trabecular lattice thins, and its struts perforate and disconnect, so the same amount of mineral is spread over a flimsier scaffold that cracks under everyday loads."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Spinal fractures steal the breath: as osteoporotic vertebrae crush and the spine curves into a stooped kyphosis, the chest cavity shrinks, restricting the lungs and leaving severe sufferers short of breath."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Gut disease quietly thins bone: celiac disease and inflammatory bowel disease impair calcium and vitamin D absorption from the intestine, a common hidden cause of secondary osteoporosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Osteoporosis is silent until the bone breaks: vertebral compression fractures crush forward into kyphosis and height loss, and can pinch the spinal nerves, while a hip fracture's pain and immobility cascade into decline."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Bone and artery trade calcium in a paradox: as the skeleton demineralizes, the same calcium hardens blood-vessel walls, and shared regulators like RANKL/OPG tie low bone density to a higher burden of vascular calcification."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin mirrors the thinning bone: both are built on type I collagen, so its age- and steroid-driven loss shows as fragile, thin skin that tracks with low bone density — the skin a visible clue to the silent skeleton."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies are now bone drugs: denosumab is a monoclonal antibody against RANKL that halts osteoclasts, and romosozumab blocks sclerostin to build bone — biologics that join the bisphosphonates against fracture."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Starvation devastates the young skeleton: anorexia nervosa's low weight, amenorrhea-driven estrogen loss, high cortisol, and low IGF-1 cause severe early osteoporosis that often does not fully recover even after weight is regained."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Excess cortisol crumbles bone: Cushing's syndrome and the adrenal-mimicking steroid drugs suppress osteoblasts and calcium absorption, making glucocorticoid-induced osteoporosis one of the commonest secondary causes."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys derange the bone: CKD's retained phosphate, low active vitamin D, and high PTH and FGF23 produce renal osteodystrophy, a complex mineral-bone disease that weakens the skeleton beyond ordinary osteoporosis."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Growth hormone keeps building bone through life: GH and the IGF-1 it drives stimulate osteoblasts and bone turnover, so the decline of the GH axis with age and adult GH deficiency contributes to thinning bone."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immune cells join the bone-loss circuit: in osteoimmunology, activated T cells secrete RANKL and inflammatory cytokines that spur osteoclasts, part of why chronic inflammation and estrogen loss accelerate bone resorption."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Type 1 diabetes weakens bone early: insulin and IGF-1 deficiency starve osteoblasts and high glucose stiffens collagen, so patients reach lower peak bone mass and fracture more often despite often-normal bone density."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fat talks to bone through leptin: the adipocyte hormone both restrains bone formation via a hypothalamic relay and supports it peripherally, helping explain why very low body fat (and marrow fat gain) tracks with osteoporosis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Bone is built around its blood supply: specialized type-H endothelial cells couple angiogenesis to osteogenesis, and their age-related decline starves the niche of osteoblast progenitors, contributing to the bone loss of osteoporosis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "It is the master switch that makes bone-eating cells: RANKL signals through NF-κB to drive osteoclast differentiation and activity, the central pathway whose unchecked activity tips the balance toward bone loss in osteoporosis."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Lung disease quietly thins the skeleton: COPD drives secondary osteoporosis through systemic inflammation, inactivity, low vitamin D and the corticosteroids used to treat it, so fractures are a common comorbidity."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "An inflamed gut weakens the bones: inflammatory bowel disease causes osteoporosis via chronic inflammation, malabsorption of calcium and vitamin D, and repeated courses of corticosteroids."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Androgen deprivation strips male bone: the testosterone withdrawal of ADT for prostate cancer accelerates bone loss, making osteoporosis and fragility fracture a major survivorship concern in treated men."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Anti-estrogen therapy thins the bone: aromatase inhibitors and ovarian suppression for breast cancer sharply lower estrogen, driving accelerated bone loss that requires monitoring and bone-protective treatment."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Antiseizure drugs erode the skeleton: enzyme-inducing antiepileptics accelerate vitamin D metabolism and impair bone mineralization, so long-term epilepsy treatment is a recognized cause of osteoporosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes weakens bone quality: type 2 diabetes raises fracture risk despite often-normal bone density through poor bone quality, while some glucose-lowering drugs accelerate bone loss."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "A broken bone is a wound to heal: osteoporotic fractures set off the repair process, and the impaired healing of the elderly and chronically ill slows their union, prolonging immobility."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Bone and mood influence each other: a fragility fracture brings pain, disability and loss of independence that drive depression, while depression and its SSRIs are themselves associated with lower bone density."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immune signals govern bone turnover: the RANK-RANKL-OPG axis links the immune and skeletal systems, so the chronic inflammation of immune and rheumatic disease drives the osteoclast activity that thins bone."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stroke and weak bone form a vicious circle: post-stroke immobility and disuse accelerate bone loss on the paretic side, and the resulting osteoporosis plus fall risk makes hip fracture far more likely."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Its transplant survivors lose bone: the prolonged high-dose corticosteroids used to control chronic graft-versus-host disease cause steroid-induced osteoporosis and avascular necrosis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Spinal fractures crush the chest: multiple thoracic vertebral compression fractures cause kyphosis that restricts lung expansion, reducing vital capacity and worsening breathlessness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Collapsing vertebrae reach the nerves: vertebral fractures cause chronic back pain and can compress the spinal cord or nerve roots, while fall-related fractures risk head injury."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Bone loss and vessel calcification track together: low bone density and vascular calcification share mechanisms in the 'calcification paradox', linking osteoporosis to atherosclerotic disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney governs the minerals bone needs: chronic kidney disease disturbs calcium, phosphate and vitamin D activation, producing renal osteodystrophy and accelerating bone loss."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "A mineral for the matrix: magnesium is needed for healthy bone mineralisation and parathyroid function, and chronic deficiency contributes to osteoporosis alongside calcium and vitamin D."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Bone and skin thin together: oestrogen loss and ageing reduce both bone density and dermal collagen, so skin thinning broadly tracks with osteoporosis risk."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "The commonest drug-induced cause: long-term corticosteroids suppress bone formation and raise resorption, making glucocorticoid-induced osteoporosis the leading secondary cause of fragility fractures."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Inflammation paradoxically thins bone: despite the new bone that fuses the spine, ankylosing spondylitis causes systemic osteoporosis and a high vertebral-fracture risk through chronic inflammatory cytokines."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "The virus and its drugs weaken bone: HIV infection and antiretroviral therapy, tenofovir in particular, accelerate bone loss, giving people with HIV markedly higher rates of osteoporosis and fracture."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Monoclonal antibodies rebuild bone: denosumab blocks RANKL to halt bone resorption and romosozumab blocks sclerostin to drive bone formation — antibody therapies targeting the exact pathways that govern osteoporosis."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It thins the bone itself: osteoporosis erodes cortical and trabecular bone as resorption outpaces formation, lowering bone density and strength until the hip, wrist and vertebrae fracture under minimal load."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cancer treatment strips bone: aromatase inhibitors, androgen-deprivation therapy and cytotoxic chemotherapy cause accelerated cancer-treatment-induced bone loss, making osteoporosis monitoring routine in cancer survivors."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "The calcification paradox: as bone loses mineral in osteoporosis, calcium deposits in the arterial wall, so low bone density and vascular calcification often coexist through shared inflammatory and vitamin-K and D pathways."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: connects-to
    note: "Acid suppression and fracture: long-term proton-pump inhibitors reduce calcium absorption and are linked to a modestly higher risk of hip and spine fractures, a caution in osteoporotic patients."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Opioids thin bone: chronic opioids suppress sex hormones (opioid-induced hypogonadism) and raise fall and fracture risk, a reciprocal link between addiction and bone loss."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol thins and breaks bone: chronic heavy drinking suppresses osteoblasts, impairs calcium and vitamin D handling and raises fall risk, making alcohol a major modifiable cause of osteoporosis and fractures."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Immobility meets falls: Parkinson's disease lowers bone density through immobility, low vitamin D and weight loss, and its falls turn that osteoporosis into hip and vertebral fractures."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Premature bone loss: Werner syndrome and other progeroid disorders cause early osteoporosis as part of accelerated ageing, the skeleton thinning decades ahead of schedule."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Thalassaemia bone disease: marrow expansion, hypogonadism, iron overload and chelation cause a severe osteoporosis, one of the commonest non-haematologic complications of transfusion-dependent thalassaemia."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Where calcium enters: the intestinal epithelium absorbs dietary calcium under vitamin D control, so malabsorption from coeliac or bariatric surgery starves the skeleton and drives osteoporosis."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Hyperparathyroid bone loss: primary hyperparathyroidism—as in MEN1—raises PTH that resorbs bone, causing osteoporosis and the classic subperiosteal resorption of excess parathyroid activity."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Bone anabolism: IGF-1, driven by growth hormone, stimulates osteoblast bone formation, and its decline with age contributes to the failure to maintain bone mass in osteoporosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory resorption: TNF-α promotes osteoclast differentiation and activity, the mechanism by which chronic inflammation and oestrogen loss accelerate the bone loss of osteoporosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Osteoclast activation: IL-1β stimulates RANKL-driven osteoclastogenesis, a key inflammatory cytokine linking immune activation and oestrogen deficiency to bone resorption."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Steroid-induced bone loss: glucocorticoids acting through their receptor suppress osteoblasts and promote osteoclast survival, making glucocorticoid-induced osteoporosis the commonest drug-related secondary cause."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Matrix and resorption: osteopontin anchors osteoclasts to the bone surface and regulates mineralisation, so its role in bone remodelling ties into the resorption-formation imbalance of osteoporosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis-osteogenesis coupling: VEGF links blood-vessel growth to bone formation, and the decline in skeletal angiogenesis with ageing contributes to the impaired bone renewal of osteoporosis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Osteocyte apoptosis: oestrogen deficiency and glucocorticoids trigger caspase-3-mediated apoptosis of osteocytes, disrupting the mechanosensory network that directs bone repair and weakening bone in osteoporosis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Remodelling mediator: prostaglandin E2 modulates both bone formation and resorption and participates in the response to mechanical loading, part of the eicosanoid control of the remodelling balance lost in osteoporosis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Mechanotransduction: osteocytes release nitric oxide in response to mechanical load to stimulate bone formation, so the loss of this signal during disuse and immobilisation accelerates bone loss in osteoporosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mineral substrate: calcium stored as hydroxyapatite gives bone its strength, and inadequate calcium and vitamin D — or its withdrawal from bone to maintain serum levels — undermines bone mineral density, the foundation of calcium-and-vitamin-D therapy in osteoporosis."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "Muscle-bone unit: the muscle-derived growth inhibitor myostatin restrains both muscle and bone mass, and the sarcopenia of ageing closely tracks osteoporosis, the basis for myostatin inhibition being explored to treat the combined loss of muscle and bone."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine regulation: adipose-derived adiponectin influences bone remodelling, part of the fat-bone endocrine crosstalk — alongside leptin — through which body composition and energy balance shape bone density and fracture risk."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Remodelling balance: NOTCH signalling regulates the differentiation balance of osteoblasts and osteoclasts from their progenitors, tuning the bone-remodelling equilibrium whose disruption produces osteoporosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Angiogenesis-osteogenesis coupling: HIF-driven coupling of blood-vessel formation to bone formation (VEGF already mapped) declines with age, contributing to the impaired bone formation of osteoporosis."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative bone loss: oxidative stress promotes osteoclast activity and osteoblast/osteocyte apoptosis, and a declining NRF2 antioxidant defence with ageing tips the balance toward the bone loss of osteoporosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Inflammatory resorption: Th17-derived IL-17A promotes osteoclastogenesis by upregulating RANKL (already mapped), driving the inflammatory bone loss that links autoimmunity and oestrogen deficiency to osteoporosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Osteoblast formation: PI3K-AKT signalling mediates osteoblast survival and bone formation downstream of IGF-1 and Wnt (both already mapped), and its decline contributes to the impaired formation arm of osteoporosis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate osteoclastogenesis: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) promotes osteoclast differentiation and the inflammatory bone resorption that accelerates age-related and postmenopausal bone loss."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signalling regulates the balance of osteoblast and osteoclast activity, influencing bone mass and the remodelling imbalance that drives osteoporosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK mechanotransduction in osteoblasts couples mechanical loading to bone formation, a pathway whose decline contributes to disuse and age-related osteoporosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-family JAK-STAT signalling (IL-6 mapped) promotes osteoclastogenesis, contributing to the bone resorption of inflammatory and postmenopausal osteoporosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates osteoclast and osteoblast activity, influencing the bone-remodelling imbalance of osteoporosis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (JAK1/2 already mapped) drives the osteoclastogenesis underlying the bone loss of inflammatory and postmenopausal osteoporosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β/BMP-SMAD signalling (TGF-β already mapped) governs osteoblast differentiation and the bone-formation arm of remodelling that fails in osteoporosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate osteoblast oxidative-stress defense and the osteoblast-osteoclast balance whose decline drives the bone loss of osteoporosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling modulates osteoclastogenesis and the inflammatory bone resorption of osteoporosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links cellular senescence to the inflammaging that promotes age-related bone loss in osteoporosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt/β-catenin signaling that governs osteoblast differentiation (Wnt and sclerostin already mapped), regulates the bone-formation side of the remodeling imbalance of osteoporosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the osteoblast and osteoclast survival that determines bone mass in osteoporosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins participate in the inflammatory osteoclast activation that contributes to the bone loss of osteoporosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the osteoblast and osteoclast energy metabolism that shapes bone remodeling in osteoporosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the osteocyte, osteoblast, and osteoclast homeostasis whose decline contributes to osteoporosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling is essential for osteoclast function and bone resorption, a validated therapeutic target in osteoporosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the osteoblast and osteoclast differentiation programs of osteoporosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte and osteoclast-precursor recruitment participates in the bone-resorption processes of osteoporosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the osteoclast-precursor and mesenchymal-stem-cell recruitment in the bone remodeling of osteoporosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the bone-remodeling immune microenvironment of osteoporosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the osteoclast differentiation and inflammatory bone loss of osteoporosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the osteogenic and osteoclast gene programs of osteoporosis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Matrix cofactor: zinc is a cofactor for alkaline phosphatase and the collagen-processing enzymes of bone formation and favours osteoblasts over osteoclasts, so zinc deficiency impairs bone accrual and quality."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Osteoclast apoptosis: bisphosphonates reduce bone resorption by shortening osteoclast lifespan, tipping the anti-apoptotic BCL-2 balance toward osteoclast death, one mechanistic basis of the mainstay antiresorptive therapy."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Diabetic bone fragility: type 2 diabetes paradoxically raises fracture risk despite normal density, as impaired insulin signalling and advanced glycation degrade bone quality, linking metabolic disease to skeletal fragility."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Osteoblast stimulation: progesterone acts on osteoblasts to promote bone formation, complementing estrogen's restraint of resorption (estrogen and testosterone already mapped), so the postmenopausal loss of both sex steroids drives bone loss."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative bone loss: reactive oxygen species from xanthine oxidase promote osteoclast differentiation and activity while impairing osteoblasts (NRF2 already mapped), so oxidative stress tips the balance toward the bone loss of osteoporosis."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Fracture pain: osteoporotic vertebral and hip fractures cause severe pain often managed with opioids acting on the mu-opioid receptor, whose sedative and fall-risk effects are themselves a hazard in the elderly osteoporotic population."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Gut-bone axis: the incretin GLP-1, released after eating, links nutrient intake to bone remodelling (insulin already mapped), part of the enteroendocrine regulation of the postprandial suppression of bone resorption relevant to osteoporosis."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid bone loss: activation of the mineralocorticoid receptor by aldosterone promotes bone resorption and calcium loss, and primary aldosteronism is associated with osteoporosis and fracture, an endocrine driver of bone loss."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Osteoimmune balance: the anti-inflammatory IL-10 restrains the inflammatory osteoclastogenesis driven by TNF, IL-6, IL-1 and IL-17 (already mapped), so the cytokine balance of osteoimmunology shapes the bone loss of osteoporosis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Marrow adiposity: with ageing and oestrogen (already mapped) loss the marrow stromal cells shift from osteoblast (already mapped) toward adipocyte differentiation (leptin and adiponectin already mapped), the fatty marrow accompanying the bone loss of osteoporosis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and bone quality: magnesium is a structural mineral of the bone matrix and a cofactor for the PTH and vitamin-D (already mapped) function, so its deficiency impairs bone quality and contributes to osteoporosis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Osteoimmune type-2 arm: IL-4, with IL-10 (already mapped), restrains the inflammatory osteoclastogenesis (RANKL, TNF and IL-17 already mapped), part of the osteoimmune cytokine balance that shapes the bone loss of osteoporosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Collagen cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) of the bone matrix, and copper deficiency (as in Menkes) causes a bone fragility, part of the trace-metal contribution to bone quality."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Osteoimmune type-2 cytokine: IL-13, with IL-4 (already mapped), is part of the type-2 arm that restrains the inflammatory osteoclastogenesis (RANKL, TNF and IL-17 already mapped) of the bone loss of osteoporosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine bone loss: resistin, with leptin and adiponectin (already mapped), promotes the osteoclastogenesis (RANKL already mapped) and the inflammatory bone loss, part of the adipokine influence on the skeleton in osteoporosis."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone-mass loss: the cortical and trabecular bone loses the mass and the microarchitecture in osteoporosis, the fragility fractures the consequence of the impaired bone tissue."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Bone phosphate: the phosphate (with the calcium already mapped) forms the hydroxyapatite mineral, and the FGF23 and PTH (already mapped) phosphate axis governs the bone-mineral balance of osteoporosis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin-D mineralisation: vitamin D drives the calcium (already mapped) absorption and the bone mineralisation; its deficiency causes the osteomalacia and worsens osteoporosis, the foundation of the supplementation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Osteoimmunology Th1: the IFN-γ of the T cells is the type-II interferon arm of the osteoimmune modulation of the RANKL (already mapped)-driven osteoclast (already mapped) bone loss of osteoporosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-bone crosstalk contributing to the bone loss of osteoporosis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate osteoimmune interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, modulates the osteoclast (already mapped) differentiation in the osteoimmunology of osteoporosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 osteoimmune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the osteoimmune crosstalk that modulates the bone loss of osteoporosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 osteoclast axis: IL-23 sustains the Th17 (IL-17 already mapped) cells that drive the RANKL (already mapped)-mediated osteoclast (already mapped) bone resorption of osteoporosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune-bone crosstalk of osteoporosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 osteoimmunology: the CD4 T-helper cells, the source of the Th17 (IL-17 and IL-23 already mapped) cytokines, drive the RANKL (already mapped)-mediated osteoclast (already mapped) bone resorption of osteoporosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell osteoporosis: the mast cells, via their histamine and cytokines, promote the osteoclast (already mapped) resorption, a link seen most starkly in the systemic-mastocytosis osteoporosis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Immunoporosis: the B cells are a source of the RANKL (already mapped) and osteoprotegerin that tune the osteoclast (already mapped) balance of the immune-bone crosstalk of osteoporosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory osteoclastogenesis of the immune-bone crosstalk of osteoporosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) promotes the osteoclast (already mapped) differentiation of the inflammatory bone loss of osteoporosis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-bone axis: transferrin, the iron carrier, reflects the disordered iron handling whose overload impairs the osteoblast (already mapped) function and drives the bone loss of osteoporosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-osteoclast axis: TSLP, from skin (already mapped) and mucosal barriers, primes dendritic cells (already mapped) and mast cells (already mapped) and activates the RANKL-osteoclast (already mapped) axis contributing to the bone loss of osteoporosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-bone axis: bradykinin, via B2R on osteoblasts (already mapped) and osteoclasts (already mapped), modulates the bone remodelling balance, with B2R activation promoting osteoclastogenesis and the bone resorption of osteoporosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Bone-marrow EPO axis: erythropoietin, via EpoR on osteoblast progenitors in the bone marrow (already mapped), modulates the osteoblast-erythroid lineage competition and the bone formation relevant to the bone loss of osteoporosis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Bone-protective chronobiology: melatonin, produced by bone-marrow (already mapped) stromal cells, acts on MT2 receptors on osteoblasts (already mapped) to stimulate bone formation and inhibit osteoclast (already mapped) resorption, directly opposing the bone loss of osteoporosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-bone axis: C1-esterase inhibitor regulates the classical-complement (complement C5 already mapped) activation in the bone microenvironment, tempering complement-driven osteoclast (already mapped) recruitment and the inflammatory bone resorption of osteoporosis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation in bone: factor H limits alternative-pathway activation on the bone-marrow (already mapped) surface and osteoclast (already mapped) progenitors, regulating the complement (complement C5 already mapped) contribution to the bone resorption of osteoporosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Osteoporosis prolactin: prolactin, via PRLR on osteoblasts (already mapped), modulates bone formation; hyperprolactinaemia suppresses estrogen (already mapped) and testosterone (already mapped), amplifying RANKL (already mapped)-driven osteoclastogenesis of osteoporosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Osteoporosis oxytocin: oxytocin, via OXTR on osteoblasts (already mapped) and osteoclasts (already mapped), promotes bone formation and inhibits resorption; oxytocin deficiency amplifies RANKL (already mapped) and TNF-α (already mapped) bone loss of osteoporosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Osteoporosis vasopressin: vasopressin, via V1aR on osteoblasts (already mapped) and osteoclasts (already mapped), modulates bone density; vasopressin dysregulation amplifies RANKL (already mapped) and IL-6 (already mapped) osteoclast resorption of osteoporosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Osteoporosis selenium: selenium, as selenoprotein antioxidant in osteoblasts (already mapped) and osteoclasts (already mapped), limits the ROS-driven RANKL (already mapped) and TNF-α (already mapped) signalling of the bone-resorption cascade of osteoporosis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Osteoporosis iodine: iodine-dependent thyroid hormones regulate osteoblast (already mapped) activity and bone mineral density; iodine deficiency amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclast resorption of osteoporosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Osteoporosis potassium: potassium alkalinity buffers the acid load that drives osteoclast (already mapped) RANKL (already mapped)-mediated bone resorption; potassium deficiency amplifies the acid-driven IL-6 (already mapped) and TNF-α (already mapped) bone loss of osteoporosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "OP iron: iron supports macrophage (already mapped) and osteoclast (already mapped) regulation; iron deficiency amplifies NF-κB (already mapped) and RANKL (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) driven osteoclastic bone resorption in osteoporosis."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Osteoporosis chloride: chloride, via osteoclast (already mapped) V-type H⁺-ATPase, acidifies the resorption lacuna; chloride imbalance amplifies the RANKL (already mapped) and NF-κB (already mapped) osteoclast drive and IL-6 (already mapped) bone-loss cascade of osteoporosis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Osteoporosis sulfur: sulfur-containing GAGs form the proteoglycan matrix anchoring osteoblast (already mapped) mineralisation; sulfur deficiency amplifies the RANKL (already mapped) and TNF-α (already mapped) osteoclastic bone resorption cascade of osteoporosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Osteoporosis nitrogen: nitrogen is the backbone of collagen (already mapped) and proteoglycan in bone; nitrogen deficiency (protein malnutrition) amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclastic cascade and impairs osteoblast (already mapped) repair."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Osteoporosis carbon: carbon as backbone of collagen (already mapped) and proteoglycan scaffold in bone sustains osteoblast (already mapped) matrix production; carbon depletion amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclastic cascade of osteoporosis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Osteoporosis hydrogen: hydrogen, via redox homeostasis in osteoblasts (already mapped) and osteoclasts, supports collagen (already mapped) cross-linking; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) bone resorption cascade of osteoporosis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Osteoporosis oxygen: oxygen availability in bone marrow drives osteoblast (already mapped) energy metabolism via mitochondrial oxidative phosphorylation; hypoxia amplifies RANKL (already mapped) and NF-κB (already mapped) osteoclastic resorption cascade of osteoporosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Osteoporosis PD-1: PD-1 on T-cells (already mapped) in bone marrow suppresses osteoclast (already mapped)-activating immune responses; PD-1 dysregulation amplifies RANKL (already mapped) and NF-κB (already mapped) bone resorption cascade of osteoporosis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Osteoporosis angiotensin-II: angiotensin-II in bone marrow vasculature modulates osteoblast (already mapped) and osteoclast differentiation; angiotensin-II excess amplifies RANKL (already mapped) and NF-κB (already mapped) bone loss cascade of osteoporosis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Osteoporosis IL-2: IL-2 from T-cells (already mapped) in bone marrow regulates osteoclast (already mapped) precursor expansion; IL-2 excess amplifies RANKL (already mapped) and NF-κB (already mapped) and TNF-α (already mapped) bone resorption cascade of osteoporosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Osteoporosis wnt-beta-catenin: WNT/β-catenin on osteoblasts (already mapped) and macrophages (already mapped) drives bone anabolic balance; wnt-beta-catenin loss amplifies rankl (already mapped) and nf-kb (already mapped) and tnf-alpha (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Osteoporosis rankl: RANKL from osteoblasts (already mapped) and macrophages (already mapped) drives osteoclast bone resorption; rankl excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and il-6 (already mapped) bone resorption cascade of osteoporosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Osteoporosis smad4: SMAD4 in osteoblasts (already mapped) and macrophages (already mapped) mediates TGF-β bone repair signalling; smad4 dysregulation amplifies rankl (already mapped) and nf-kb (already mapped) and tnf-alpha (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Osteoporosis fibronectin: fibronectin in osteoblasts (already mapped) and osteoclasts (already mapped) promotes bone ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Osteoporosis activin-a: activin-A from osteoblasts (already mapped) and osteoclasts (already mapped) drives bone resorption; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Osteoporosis cgrp: CGRP from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone vascular tone; cgrp dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Osteoporosis substance-p: substance-P from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone immune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Osteoporosis insulin-receptor: insulin receptor on osteoblasts (already mapped) and osteoclasts (already mapped) drives bone metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "OP androgen-receptor: androgen receptor on osteoblasts (already mapped) and osteoclasts (already mapped) modulates steroid signalling; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "OP norepinephrine: Norepinephrine from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone stress tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "OP adrenomedullin: Adrenomedullin from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone vascular tone; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "OP bdnf: BDNF from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone neural tone; bdnf excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "OP fgfr: FGFR signalling on osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone proliferation; fgfr excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "OP epinephrine: epinephrine from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "OP renin: renin from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone RAAS activation; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis."
---

# Osteoporosis

## Overview

**Osteoporosis** is a **systemic skeletal disease** characterized by **low bone mineral density (BMD)** and **microarchitectural deterioration of bone tissue** leading to enhanced bone fragility and susceptibility to **fragility fractures** — fractures that occur with minimal trauma (fall from standing height or less). It represents an imbalance in bone remodeling where **osteoclast-mediated resorption exceeds osteoblast-mediated formation**, resulting in net bone loss [^kanis-2019-who-osteoporosis].

**Definition:**
- WHO diagnostic criteria: BMD T-score ≤ −2.5 standard deviations below the young adult mean (peak bone mass) at the lumbar spine, femoral neck, or total hip by DXA (dual-energy X-ray absorptiometry); T-score −1.0 to −2.5 = osteopenia; T-score ≤ −2.5 = osteoporosis
- **Clinical (operational) definition:** Fragility fracture in the absence of an alternative cause (metastatic disease, multiple myeloma, Paget's disease) regardless of T-score

**Epidemiology:**
- **Burden:** Affects ~200 million people worldwide; 1 in 3 women and 1 in 5 men over age 50 will sustain an osteoporotic fracture in their lifetime; 8.9 million fractures per year globally; hip fractures are the most severe (30-40% 1-year mortality in the elderly; 50% never return to pre-fracture ambulatory status)
- **Geography and risk factors:**
  - Peak bone mass achieved at ~25-30 years; determined by genetics (~60-80%), nutrition (calcium, vitamin D), physical activity, and hormonal factors
  - Bone loss begins in the 4th decade; accelerates sharply at menopause (women lose 3-5% trabecular bone/year in first 5-10 years post-menopause)
  - **FRAX (WHO Fracture Risk Assessment Tool):** 10-year probability of major osteoporotic fracture (MOF) — hip, clinical spine, forearm, humerus — from 12 clinical risk factors ± BMD; threshold-based treatment recommendations by country (UK NICE/NOGG, US NOF)

**Risk factors:**
- **Major:** Prior fragility fracture (strongest predictor — 2-3× increased risk for subsequent fracture), family history of hip fracture, glucocorticoid use ≥5 mg prednisolone ≥3 months, early menopause (<45 years), hypogonadism (male), malabsorption (celiac disease, inflammatory bowel disease), low BMI (<20 kg/m²)
- **Modifiable:** Smoking (increases bone resorption, reduces bone formation), alcohol >3 units/day, low calcium/vitamin D intake, physical inactivity, low body weight
- **Secondary causes:** Glucocorticoid-induced osteoporosis (GIO, most common secondary cause), hyperparathyroidism (PTH → RANKL → osteoclast activation), hyperthyroidism (thyroid hormones → accelerated bone turnover), multiple myeloma (RANK-L overproduction by plasma cells → osteolysis), CKD-MBD, rheumatoid arthritis, liver cirrhosis

**Types:**
- **Primary:** Type 1 (postmenopausal — high turnover, trabecular bone predominantly): estrogen deficiency → increased RANKL expression → osteoclast hyperactivation; Type 2 (age-related/senile — both sexes, 70+ years): reduced osteoblast number and function, reduced intestinal calcium absorption, secondary hyperparathyroidism → cortical + trabecular bone loss
- **Secondary:** GIO (glucocorticoids → Wnt inhibition via DKK-1, sclerostin → reduced osteoblast function + increased RANKL → dual anabolic + anti-resorptive impairment)

## Structure

### Bone remodeling — cellular biology of bone loss

**Bone remodeling units (BMUs):**
- Bone is continuously remodeled — ~10% of adult skeleton replaced per year; individual remodeling cycles take ~3-6 months; BMUs consist of osteoclasts and osteoblasts working in sequence on bone surfaces

**Remodeling sequence:**
1. **Activation:** Mechanical strain, microdamage, paracrine signals → osteocyte (mechanosensor, 90% of bone cells, embedded in mineralized matrix) → signaling via RANKL, sclerostin (Wnt inhibitor), DKK-1 → osteoclast precursor recruitment
2. **Resorption (osteoclast phase):** Monocyte-derived osteoclast precursors → RANKL (on osteoblast/stromal cell surface) → RANK (on osteoclast precursor) → TRAF6 → NF-kB, AP-1, NFATc1 → osteoclast differentiation → polarized multinucleated osteoclast → ruffled border → V-ATPase → H⁺ → acidification of resorption lacuna → dissolution of hydroxyapatite → cathepsin K → collagen type I degradation → CTX, NTX release → lacunar pit formation (3-4 weeks)
3. **Reversal phase:** Osteoclast apoptosis; reversal cells (monocytes/macrophages) clean lacunar surface; bone lining cells prepare surface for osteoblast attachment; coupling signals released from bone matrix: TGF-beta, IGF-1, BMP2/4/7 → osteoblast precursor recruitment
4. **Formation (osteoblast phase):** MSC-derived osteoblast precursors → Wnt-beta-catenin signaling → osteoblast differentiation → RUNX2, SP7/Osterix → collagen I synthesis, osteocalcin, bone sialoprotein → osteoid → mineralization (3-4 months) → some osteoblasts become osteocytes (embedded), some become bone lining cells, some undergo apoptosis
5. **Quiescence:** Mineralized bone; osteocytes monitor mechanical loading via lacuno-canalicular network

**RANKL-RANK-OPG axis (master regulator):**
- **RANKL (TNFSF11, expressed by osteoblasts, stromal cells, T cells, osteocytes):** Binds RANK on osteoclast precursors → osteoclast differentiation, activation, and survival
- **OPG (osteoprotegerin, TNFRSF11B, secreted by osteoblasts):** Decoy receptor for RANKL → binds RANKL → blocks RANK binding → inhibits osteoclastogenesis; OPG/RANKL ratio determines bone resorption rate; estrogen → OPG expression → anti-resorptive; estrogen deficiency → reduced OPG → increased RANKL/OPG ratio → osteoclast hyperactivation
- **Denosumab:** Fully human anti-RANKL monoclonal antibody → mimics OPG → blocks RANKL → osteoclast suppression

**Sclerostin-Wnt axis (bone formation master regulator):**
- **Sclerostin (SOST, secreted by osteocytes):** Binds LRP5/6 co-receptors → blocks Wnt-beta-catenin in osteoblasts → inhibits osteoblast differentiation, proliferation, and survival → net anti-anabolic; sclerostin is the brake on bone formation
- Mechanical loading → suppresses sclerostin → Wnt de-repression → bone formation at sites of load; immobilization → sclerostin → bone loss
- **Romosozumab (Evenity):** Anti-sclerostin monoclonal antibody → de-represses Wnt in osteoblasts → increased bone formation + modest anti-resorptive effect (via increased OPG from osteoblasts) → dual anabolic + anti-resorptive; unique mechanism among osteoporosis drugs

## Function

### Clinical presentation and fractures

**Fragility fracture sites (in order of clinical impact):**
- **Hip fracture (femoral neck, intertrochanteric):** Most severe; 30-40% 1-year mortality in elderly; 50% lose prior ambulatory function; ~1.5 million/year globally; requires surgery (hip replacement or ORIF); osteoporosis is the dominant modifiable risk factor
- **Vertebral fractures:** Most common osteoporotic fracture (~700,000/year in US); often asymptomatic ("silent fractures" — only 30% come to clinical attention); progressive vertebral collapse → kyphosis (Dowager's hump), height loss, restrictive lung disease, chronic pain; each vertebral fracture increases risk of subsequent vertebral fracture 5×
- **Distal radius fracture (Colles fracture):** Common in perimenopausal women; fall on outstretched hand; "sentinel fracture" signaling developing osteoporosis; often under-evaluated for bone health
- **Humerus fracture:** Fall on outstretched arm; surgical neck most common; 1-2% of fragility fractures

**Diagnosis:**
- **DXA scan:** Gold standard for BMD; lumbar spine L1-L4 and hip (femoral neck, total hip); peripheral DXA (wrist, calcaneus) less accurate for treatment decisions
- **FRAX:** WHO tool integrating clinical risk factors → 10-year fracture probability; triggers treatment at country-specific intervention thresholds (e.g., US: FRAX ≥20% MOF or ≥3% hip → treatment)
- **Trabecular bone score (TBS):** DXA-derived microarchitectural assessment; adds information beyond T-score alone; useful in secondary osteoporosis (e.g., GIO)
- **Bone turnover markers:** CTX (resorption), P1NP/osteocalcin (formation) → monitor treatment response and adherence; fastest response within 3-6 months of initiating therapy

## Pathology

### Secondary causes — screening

All newly diagnosed osteoporosis should be evaluated for secondary causes: CBC (myeloma, anemia), CMP (calcium, phosphate, renal function, liver function), TSH (hyperthyroidism), serum PTH and calcium (hyperparathyroidism), 25-OH vitamin D (deficiency), celiac antibodies (if indicated), serum/urine protein electrophoresis (myeloma), sex hormones (premature hypogonadism), 24h urine calcium (hypercalciuria — consider thiazide diuretics).

### Treatment [^cosman-2016-romosozumab] [^cummings-2009-denosumab-freedom]

**Non-pharmacological:**
- **Calcium:** 1000-1200 mg/day total (food + supplement); supplements associated with modest GI side effects and possible CV risk (controversial) — prefer dietary sources; dairy, fortified foods, leafy greens
- **Vitamin D:** 800-2000 IU/day to maintain 25-OH-D >30 ng/mL; critical for calcium absorption; cholecalciferol (D3) preferred; deficiency common in elderly, northern latitudes, institutionalized
- **Weight-bearing exercise:** Reduces fall risk, improves balance and muscle mass; resistance training → mechanical loading → sclerostin suppression → bone formation; no direct fracture prevention evidence from exercise RCTs but strong observational data
- **Fall prevention:** Home assessment, PT/balance training, vision correction, medication review (sedatives, antihypertensives → orthostatic hypotension), vitamin D supplementation → reduces fall risk ~20%

**Antiresorptive therapy:**

*Bisphosphonates (first-line):*
- **Alendronate (Fosamax), risedronate (Actonel):** Weekly oral; nitrogen-containing bisphosphonates → farnesyl pyrophosphate synthase inhibition → prenylation failure → osteoclast apoptosis; reduce vertebral fracture ~50%, hip fracture ~40-50%; FIT trial (alendronate: hip fracture RR 0.49); generally well tolerated; GI side effects (esophageal irritation → take upright, 30 min before food); musculoskeletal pain
- **Zoledronic acid (Reclast, Zometa):** IV annually; HORIZON-PFT trial: vertebral fracture RR 0.30, hip RR 0.59, all clinical fracture RR 0.67; also reduces mortality in hip fracture patients; acute phase reaction (flu-like symptoms after first infusion, pretreat with acetaminophen)
- **Adverse effects (rare):** ONJ (osteonecrosis of the jaw) — primarily with high-dose IV bisphosphonates in cancer patients; atypical femur fractures — subtrochanteric or femoral shaft stress fractures with prodromal thigh pain; risk increases with >5-10 years use; drug holiday (2-5 years) after 5 years oral/3 years IV bisphosphonate considered for low-risk patients

*Denosumab (Prolia, 60 mg SC every 6 months):*
- Anti-RANKL monoclonal antibody → osteoclast suppression; FREEDOM trial: vertebral fracture RR 0.32, hip fracture RR 0.60; superior to alendronate in head-to-head (DECIDE trial); can use in CKD (no renal dosing adjustment unlike bisphosphonates); **critical: rebound resorption on discontinuation** → bone loss accelerates and multiple vertebral fractures can occur rapidly if denosumab stopped without transition to bisphosphonate — must transition [^cummings-2009-denosumab-freedom]

*SERMs (selective estrogen receptor modulators):*
- **Raloxifene (Evista):** ER agonist in bone → reduces vertebral fracture ~36% (MORE trial); no hip fracture benefit; reduces invasive breast cancer risk (off-label prevention); increases VTE and hot flashes; NOT for primary hip fracture prevention

**Anabolic therapy (for severe osteoporosis, ≥2 vertebral fractures, or very low T-score):**

*PTH analogues (stimulate osteoblasts):*
- **Teriparatide (Forteo, PTH 1-34):** SC daily × max 2 years; stimulates bone formation > resorption; FPT trial: vertebral fracture RR 0.35, non-vertebral fracture RR 0.47; must transition to antiresorptive after completing course (bone resorbs rapidly without maintenance); risk: osteosarcoma (Sprague-Dawley rats at high doses — black box warning; not confirmed in humans); contraindicated in Paget's disease, prior bone radiation
- **Abaloparatide (Tymlos, PTHrP 1-34):** Similar efficacy and mechanism; ACTIVE trial; slightly different receptor selectivity from teriparatide

*Romosozumab (Evenity, anti-sclerostin):*
- 210 mg SC monthly × 12 months; ARCH trial vs. alendronate: vertebral fracture RR 0.27, hip RR 0.38 vs. alendronate; FRAME trial vs. placebo: vertebral RR 0.27; dual anabolic + anti-resorptive mechanism; **black box warning: possible increased CV risk** (ARCH trial: non-significant increase in MACE vs. alendronate); contraindicated within 12 months of MI or stroke; must transition to antiresorptive after 12 months [^cosman-2016-romosozumab]

**Treatment sequencing:**
- Severe osteoporosis: romosozumab or teriparatide → bisphosphonate or denosumab (anabolic then antiresorptive = anabolic first paradigm → greater BMD gain than antiresorptive first)
- Moderate osteoporosis: bisphosphonate or denosumab first-line
- Denosumab → must transition to bisphosphonate on stopping (rebound fracture risk)

## Connections

- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta released from bone matrix during osteoclastic resorption → chemoattractant for osteoblast precursors → bone formation coupling signal; excess TGF-beta (PTH-driven or tumor-derived) → uncoupled osteoclast activation → metastasis-associated bone destruction.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives RANKL-independent osteoclastogenesis via JAK-STAT3 → osteoclast precursor differentiation; elevated IL-6 in postmenopausal women, RA, and multiple myeloma → accelerated bone loss; tocilizumab reduces bone erosion in RA as a secondary bone-protective effect.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen type I is the dominant organic bone matrix component; osteoblasts synthesize type I collagen → osteoid → mineralization; osteoclastic resorption → CTX and NTX (type I collagen telopeptides) → serum biomarkers of bone resorption used to monitor osteoporosis therapy.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Osteoclasts are the primary drivers of bone loss: RANKL → RANK on osteoclast precursors → differentiation and lacunar resorption → BMD loss; denosumab (anti-RANKL) neutralizes RANKL → osteoclast suppression → fracture risk reduction 40-60%.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — calcitonin inhibits osteoclast activity → CTR → cAMP → cytoskeletal collapse and loss of ruffled border → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; now reserved for acute pain of recent vertebral fracture.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — RANKL (TNFSF11) from osteoblasts/T cells → RANK on osteoclast precursors → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG decoy ratio governs bone mass; denosumab (anti-RANKL) → 68% vertebral and 40% hip fracture risk reduction (FREEDOM trial).
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Sclerostin (SOST) from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → net bone loss; mechanical loading suppresses sclerostin → anabolic response; romosozumab (anti-sclerostin) → +13% lumbar spine BMD at 12 months; 73% vertebral fracture RRR (FRAME).
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — Hyperthyroidism accelerates bone remodeling → 10-20% BMD loss at trabecular sites; TSH receptors on osteoblasts exert bone-protective effects; Graves disease → osteoporosis risk; anti-thyroid treatment normalizes bone loss; bisphosphonates co-administered when BMD is low.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Osteoporosis is a failure of the osteoblast-osteoclast balance: bone-resorbing osteoclasts outpace bone-forming osteoblasts (estrogen loss, aging, steroids), so bone mass and microarchitecture deteriorate—anabolic drugs reverse it by favoring osteoblasts.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Osteoporosis is the commonest disease of the aging musculoskeletal system: silent bone loss until a fragility fracture (hip, vertebra, wrist) reveals it, and because fractures cause disability and death, bone-density screening and antiresorptives are core to skeletal health.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Menopause is the leading cause of osteoporosis: the sharp fall in ovarian estrogen accelerates osteoclast-driven bone resorption, so women lose bone rapidly after menopause—linking the reproductive system's hormonal shift to skeletal fragility and fracture risk.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the mineral osteoporosis depletes: bone is the body's calcium reservoir, and when intake or absorption falls, parathyroid hormone pulls calcium from bone to keep blood levels constant—so chronic deficiency drives the net bone loss that weakens the skeleton.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D is essential to prevent osteoporosis: it drives intestinal calcium absorption, so deficiency causes secondary hyperparathyroidism that strips bone, and adequate vitamin D plus calcium is the foundation on which osteoporosis drug therapy is built.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol excess is a major cause of osteoporosis: glucocorticoids suppress osteoblasts, promote osteoclast survival and reduce calcium absorption, so both Cushing's syndrome and long-term steroid therapy cause rapid bone loss—the most common drug-induced osteoporosis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone is remodeled in concert with the marrow it houses: osteoporosis reflects an imbalance between osteoclasts and osteoblasts at the bone-marrow interface, and with age red marrow gives way to fat as bone is lost—linking declining marrow and skeletal mass.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium is an underappreciated factor in bone health: about half the body's magnesium sits in bone, and it is needed for vitamin D activation and PTH secretion, so chronic magnesium deficiency impairs mineralization and contributes to osteoporosis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Osteoporosis is largely an endocrine disease: estrogen, testosterone, thyroid hormone, parathyroid hormone and cortisol all govern bone turnover, so hormonal shifts (menopause, hyperthyroidism, steroid excess) are leading causes of bone loss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Bone is calcium-phosphate crystal, so phosphorus is as structural as calcium: hydroxyapatite needs balanced phosphate, and disordered phosphate handling—too little (osteomalacia) or the excess of kidney disease—weakens or distorts bone alongside calcium loss.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Type 1 diabetes weakens bone early: insulin and IGF-1 deficiency starve osteoblasts and high glucose stiffens collagen, so patients reach lower peak bone mass and fracture more often despite often-normal bone density.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fat talks to bone through leptin: the adipocyte hormone both restrains bone formation via a hypothalamic relay and supports it peripherally, helping explain why very low body fat (and marrow fat gain) tracks with osteoporosis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Bone is built around its blood supply: specialized type-H endothelial cells couple angiogenesis to osteogenesis, and their age-related decline starves the niche of osteoblast progenitors, contributing to the bone loss of osteoporosis.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Rheumatoid arthritis is a double hit to bone: chronic inflammation (and RANKL) accelerates bone loss, and the glucocorticoids used to treat it cause steroid-induced osteoporosis—so inflammatory arthritis is a leading secondary cause of fragile bones.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Healthy bone depends on the gut: the intestine absorbs the calcium and vitamin D bone needs, so malabsorption from celiac disease, inflammatory bowel disease, or bariatric surgery is an under-recognized cause of osteoporosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Bone loss in aging tips marrow toward fat: the mesenchymal stem cells that should become bone-building osteoblasts instead become adipocytes, so marrow fills with fat as bone thins—linking the adipocyte-osteoblast balance to osteoporosis.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Multiple myeloma masquerades as severe osteoporosis: malignant plasma cells activate osteoclasts (via RANKL) to carve lytic lesions and cause fractures, so unexplained bone loss with anemia or high calcium prompts a myeloma workup.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Failing kidneys weaken bone—renal osteodystrophy: CKD disturbs phosphate, vitamin D and PTH, deranging bone turnover into a complex osteoporosis-plus-osteomalacia that standard bone drugs can worsen, so diagnosis must come first.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Bone formation runs on Wnt signaling, the lever osteoporosis drugs pull: Wnt/beta-catenin tells osteoblasts to build bone, and because sclerostin blocks it, antibodies against sclerostin (romosozumab) unleash Wnt to grow new bone.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine supplies the calcium that bone needs: it absorbs dietary calcium under vitamin D's control, so malabsorption from celiac disease or bypass surgery starves bone of calcium and accelerates osteoporosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gut-made serotonin puts a brake on bone building: serotonin from the intestine circulates and tells osteoblasts to slow down, an unexpected gut-bone axis that helps explain why some serotonin-active drugs affect bone density.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Bone health is read and built with photons: a DXA scan uses low-dose X-ray photons to measure bone density and diagnose osteoporosis, while sunlight's photons make the vitamin D that lets bone absorb calcium.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach quietly guards bone: its acid frees calcium from food for absorption, so long-term acid-suppressing drugs (PPIs) can reduce calcium uptake and are linked to a higher fracture risk.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Too much salt thins the bones: high dietary sodium makes the kidneys excrete more calcium in urine, and that ongoing calcium drain pulls mineral from bone, quietly worsening osteoporosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Bone-eating osteoclasts arise from macrophages: the monocyte-macrophage lineage fuses into the osteoclasts that resorb bone, so inflammation that recruits macrophages accelerates bone loss.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver takes the first step in activating vitamin D: it hydroxylates it to 25-OH-D, the stored form measured in blood, before the kidney finishes the job, so liver disease can starve bone of usable vitamin D.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc helps build bone: it is a cofactor for the enzymes that lay down collagen matrix and for osteoblast activity, so zinc deficiency contributes to low bone mass.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows osteoporosis as a hollowing-out: the bone's trabecular lattice thins, and its struts perforate and disconnect, so the same amount of mineral is spread over a flimsier scaffold that cracks under everyday loads.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Spinal fractures steal the breath: as osteoporotic vertebrae crush and the spine curves into a stooped kyphosis, the chest cavity shrinks, restricting the lungs and leaving severe sufferers short of breath.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Gut disease quietly thins bone: celiac disease and inflammatory bowel disease impair calcium and vitamin D absorption from the intestine, a common hidden cause of secondary osteoporosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Osteoporosis is silent until the bone breaks: vertebral compression fractures crush forward into kyphosis and height loss, and can pinch the spinal nerves, while a hip fracture's pain and immobility cascade into decline.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Bone and artery trade calcium in a paradox: as the skeleton demineralizes, the same calcium hardens blood-vessel walls, and shared regulators like RANKL/OPG tie low bone density to a higher burden of vascular calcification.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin mirrors the thinning bone: both are built on type I collagen, so its age- and steroid-driven loss shows as fragile, thin skin that tracks with low bone density — the skin a visible clue to the silent skeleton.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies are now bone drugs: denosumab is a monoclonal antibody against RANKL that halts osteoclasts, and romosozumab blocks sclerostin to build bone — biologics that join the bisphosphonates against fracture.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — Starvation devastates the young skeleton: anorexia nervosa's low weight, amenorrhea-driven estrogen loss, high cortisol, and low IGF-1 cause severe early osteoporosis that often does not fully recover even after weight is regained.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Excess cortisol crumbles bone: Cushing's syndrome and the adrenal-mimicking steroid drugs suppress osteoblasts and calcium absorption, making glucocorticoid-induced osteoporosis one of the commonest secondary causes.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys derange the bone: CKD's retained phosphate, low active vitamin D, and high PTH and FGF23 produce renal osteodystrophy, a complex mineral-bone disease that weakens the skeleton beyond ordinary osteoporosis.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Growth hormone keeps building bone through life: GH and the IGF-1 it drives stimulate osteoblasts and bone turnover, so the decline of the GH axis with age and adult GH deficiency contributes to thinning bone.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immune cells join the bone-loss circuit: in osteoimmunology, activated T cells secrete RANKL and inflammatory cytokines that spur osteoclasts, part of why chronic inflammation and estrogen loss accelerate bone resorption.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — It is the master switch that makes bone-eating cells: RANKL signals through NF-κB to drive osteoclast differentiation and activity, the central pathway whose unchecked activity tips the balance toward bone loss in osteoporosis.
- `connects-to` → **[COPD](../copd/README.md)** — Lung disease quietly thins the skeleton: COPD drives secondary osteoporosis through systemic inflammation, inactivity, low vitamin D and the corticosteroids used to treat it, so fractures are a common comorbidity.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — An inflamed gut weakens the bones: inflammatory bowel disease causes osteoporosis via chronic inflammation, malabsorption of calcium and vitamin D, and repeated courses of corticosteroids.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Androgen deprivation strips male bone: the testosterone withdrawal of ADT for prostate cancer accelerates bone loss, making osteoporosis and fragility fracture a major survivorship concern in treated men.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Anti-estrogen therapy thins the bone: aromatase inhibitors and ovarian suppression for breast cancer sharply lower estrogen, driving accelerated bone loss that requires monitoring and bone-protective treatment.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Antiseizure drugs erode the skeleton: enzyme-inducing antiepileptics accelerate vitamin D metabolism and impair bone mineralization, so long-term epilepsy treatment is a recognized cause of osteoporosis.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes weakens bone quality: type 2 diabetes raises fracture risk despite often-normal bone density through poor bone quality, while some glucose-lowering drugs accelerate bone loss.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — A broken bone is a wound to heal: osteoporotic fractures set off the repair process, and the impaired healing of the elderly and chronically ill slows their union, prolonging immobility.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Bone and mood influence each other: a fragility fracture brings pain, disability and loss of independence that drive depression, while depression and its SSRIs are themselves associated with lower bone density.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immune signals govern bone turnover: the RANK-RANKL-OPG axis links the immune and skeletal systems, so the chronic inflammation of immune and rheumatic disease drives the osteoclast activity that thins bone.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stroke and weak bone form a vicious circle: post-stroke immobility and disuse accelerate bone loss on the paretic side, and the resulting osteoporosis plus fall risk makes hip fracture far more likely.
- `connects-to` → **[Graft-versus-Host Disease](../gvhd/README.md)** — Its transplant survivors lose bone: the prolonged high-dose corticosteroids used to control chronic graft-versus-host disease cause steroid-induced osteoporosis and avascular necrosis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Spinal fractures crush the chest: multiple thoracic vertebral compression fractures cause kyphosis that restricts lung expansion, reducing vital capacity and worsening breathlessness.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Collapsing vertebrae reach the nerves: vertebral fractures cause chronic back pain and can compress the spinal cord or nerve roots, while fall-related fractures risk head injury.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Bone loss and vessel calcification track together: low bone density and vascular calcification share mechanisms in the 'calcification paradox', linking osteoporosis to atherosclerotic disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney governs the minerals bone needs: chronic kidney disease disturbs calcium, phosphate and vitamin D activation, producing renal osteodystrophy and accelerating bone loss.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — A mineral for the matrix: magnesium is needed for healthy bone mineralisation and parathyroid function, and chronic deficiency contributes to osteoporosis alongside calcium and vitamin D.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Bone and skin thin together: oestrogen loss and ageing reduce both bone density and dermal collagen, so skin thinning broadly tracks with osteoporosis risk.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — The commonest drug-induced cause: long-term corticosteroids suppress bone formation and raise resorption, making glucocorticoid-induced osteoporosis the leading secondary cause of fragility fractures.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Inflammation paradoxically thins bone: despite the new bone that fuses the spine, ankylosing spondylitis causes systemic osteoporosis and a high vertebral-fracture risk through chronic inflammatory cytokines.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — The virus and its drugs weaken bone: HIV infection and antiretroviral therapy, tenofovir in particular, accelerate bone loss, giving people with HIV markedly higher rates of osteoporosis and fracture.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Monoclonal antibodies rebuild bone: denosumab blocks RANKL to halt bone resorption and romosozumab blocks sclerostin to drive bone formation — antibody therapies targeting the exact pathways that govern osteoporosis.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It thins the bone itself: osteoporosis erodes cortical and trabecular bone as resorption outpaces formation, lowering bone density and strength until the hip, wrist and vertebrae fracture under minimal load.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cancer treatment strips bone: aromatase inhibitors, androgen-deprivation therapy and cytotoxic chemotherapy cause accelerated cancer-treatment-induced bone loss, making osteoporosis monitoring routine in cancer survivors.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — The calcification paradox: as bone loses mineral in osteoporosis, calcium deposits in the arterial wall, so low bone density and vascular calcification often coexist through shared inflammatory and vitamin-K and D pathways.
- `connects-to` → **[Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md)** — Acid suppression and fracture: long-term proton-pump inhibitors reduce calcium absorption and are linked to a modestly higher risk of hip and spine fractures, a caution in osteoporotic patients.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Opioids thin bone: chronic opioids suppress sex hormones (opioid-induced hypogonadism) and raise fall and fracture risk, a reciprocal link between addiction and bone loss.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol thins and breaks bone: chronic heavy drinking suppresses osteoblasts, impairs calcium and vitamin D handling and raises fall risk, making alcohol a major modifiable cause of osteoporosis and fractures.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Immobility meets falls: Parkinson's disease lowers bone density through immobility, low vitamin D and weight loss, and its falls turn that osteoporosis into hip and vertebral fractures.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Premature bone loss: Werner syndrome and other progeroid disorders cause early osteoporosis as part of accelerated ageing, the skeleton thinning decades ahead of schedule.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Thalassaemia bone disease: marrow expansion, hypogonadism, iron overload and chelation cause a severe osteoporosis, one of the commonest non-haematologic complications of transfusion-dependent thalassaemia.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Where calcium enters: the intestinal epithelium absorbs dietary calcium under vitamin D control, so malabsorption from coeliac or bariatric surgery starves the skeleton and drives osteoporosis.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Hyperparathyroid bone loss: primary hyperparathyroidism—as in MEN1—raises PTH that resorbs bone, causing osteoporosis and the classic subperiosteal resorption of excess parathyroid activity.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Bone anabolism: IGF-1, driven by growth hormone, stimulates osteoblast bone formation, and its decline with age contributes to the failure to maintain bone mass in osteoporosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory resorption: TNF-α promotes osteoclast differentiation and activity, the mechanism by which chronic inflammation and oestrogen loss accelerate the bone loss of osteoporosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Osteoclast activation: IL-1β stimulates RANKL-driven osteoclastogenesis, a key inflammatory cytokine linking immune activation and oestrogen deficiency to bone resorption.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Steroid-induced bone loss: glucocorticoids acting through their receptor suppress osteoblasts and promote osteoclast survival, making glucocorticoid-induced osteoporosis the commonest drug-related secondary cause.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Matrix and resorption: osteopontin anchors osteoclasts to the bone surface and regulates mineralisation, so its role in bone remodelling ties into the resorption-formation imbalance of osteoporosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Angiogenesis-osteogenesis coupling: VEGF links blood-vessel growth to bone formation, and the decline in skeletal angiogenesis with ageing contributes to the impaired bone renewal of osteoporosis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Estrogen deficiency and glucocorticoids trigger caspase-3-mediated apoptosis of osteocytes, disrupting the mechanosensory network that directs targeted bone repair and weakening bone independent of changes in bone density.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandin E2 modulates both bone formation and resorption and participates in the skeletal response to mechanical loading, part of the eicosanoid control of the remodeling balance that tips toward loss in osteoporosis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Osteocytes release nitric oxide in response to mechanical load to stimulate bone formation, so the loss of this signal during disuse, immobilization, and spaceflight accelerates the bone loss of osteoporosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium stored as hydroxyapatite gives bone its strength, and inadequate calcium and vitamin D—or its withdrawal from bone to maintain serum levels—undermines bone mineral density, the foundation of calcium-and-vitamin-D therapy in osteoporosis.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — The muscle-derived growth inhibitor myostatin restrains both muscle and bone mass, and the sarcopenia of aging closely tracks osteoporosis, the basis for myostatin inhibition being explored to treat the combined loss of muscle and bone.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipose-derived adiponectin influences bone remodeling, part of the fat-bone endocrine crosstalk—alongside leptin—through which body composition and energy balance shape bone density and fracture risk.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling regulates the differentiation balance of osteoblasts and osteoclasts from their progenitors, tuning the bone-remodeling equilibrium whose disruption produces osteoporosis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-driven coupling of blood-vessel formation to bone formation (VEGF already mapped) declines with age, contributing to the impaired bone formation of osteoporosis.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oxidative stress promotes osteoclast activity and osteoblast/osteocyte apoptosis, and a declining NRF2 antioxidant defense with aging tips the balance toward the bone loss of osteoporosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17-derived IL-17A promotes osteoclastogenesis by upregulating RANKL (already mapped), driving the inflammatory bone loss that links autoimmunity and estrogen deficiency to osteoporosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling mediates osteoblast survival and bone formation downstream of IGF-1 and Wnt (both already mapped), and its decline contributes to the impaired formation arm of osteoporosis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) promotes osteoclast differentiation and the inflammatory bone resorption that accelerates age-related and postmenopausal bone loss.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates the balance of osteoblast and osteoclast activity, influencing bone mass and the remodeling imbalance that drives osteoporosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK mechanotransduction in osteoblasts couples mechanical loading to bone formation, a pathway whose decline contributes to disuse and age-related osteoporosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-family JAK-STAT signaling (IL-6 mapped) promotes osteoclastogenesis, contributing to the bone resorption of inflammatory and postmenopausal osteoporosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates osteoclast and osteoblast activity, influencing the bone-remodeling imbalance of osteoporosis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (JAK1/2 already mapped) drives the osteoclastogenesis underlying the bone loss of inflammatory and postmenopausal osteoporosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β/BMP-SMAD signaling (TGF-β already mapped) governs osteoblast differentiation and the bone-formation arm of remodeling that fails in osteoporosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate osteoblast oxidative-stress defense and the osteoblast-osteoclast balance whose decline drives the bone loss of osteoporosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling modulates osteoclastogenesis and the inflammatory bone resorption of osteoporosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING links cellular senescence to the inflammaging that promotes age-related bone loss in osteoporosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, within the Wnt/β-catenin signaling that governs osteoblast differentiation (Wnt and sclerostin already mapped), regulates the bone-formation side of the remodeling imbalance of osteoporosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) regulates the osteoblast and osteoclast survival that determines bone mass in osteoporosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins participate in the inflammatory osteoclast activation that contributes to the bone loss of osteoporosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the osteoblast and osteoclast energy metabolism that shapes bone remodeling in osteoporosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the osteocyte, osteoblast, and osteoclast homeostasis whose decline contributes to osteoporosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling is essential for osteoclast function and bone resorption, a validated therapeutic target in osteoporosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the osteoblast and osteoclast differentiation programs of osteoporosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte and osteoclast-precursor recruitment participates in the bone-resorption processes of osteoporosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the osteoclast-precursor and mesenchymal-stem-cell recruitment in the bone remodeling of osteoporosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the bone-remodeling immune microenvironment of osteoporosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the osteoclast differentiation and inflammatory bone loss of osteoporosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the osteogenic and osteoclast gene programs of osteoporosis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Matrix cofactor: zinc is a cofactor for alkaline phosphatase and the collagen-processing enzymes of bone formation and favours osteoblasts over osteoclasts, so zinc deficiency impairs bone accrual and quality.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Osteoclast apoptosis: bisphosphonates reduce bone resorption by shortening osteoclast lifespan, tipping the anti-apoptotic BCL-2 balance toward osteoclast death, one mechanistic basis of the mainstay antiresorptive therapy.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Diabetic bone fragility: type 2 diabetes paradoxically raises fracture risk despite normal density, as impaired insulin signalling and advanced glycation degrade bone quality, linking metabolic disease to skeletal fragility.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Osteoblast stimulation: progesterone acts on osteoblasts to promote bone formation, complementing estrogen's restraint of resorption (estrogen and testosterone already mapped), so the postmenopausal loss of both sex steroids drives bone loss.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative bone loss: reactive oxygen species from xanthine oxidase promote osteoclast differentiation and activity while impairing osteoblasts (NRF2 already mapped), so oxidative stress tips the balance toward the bone loss of osteoporosis.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Fracture pain: osteoporotic vertebral and hip fractures cause severe pain often managed with opioids acting on the mu-opioid receptor, whose sedative and fall-risk effects are themselves a hazard in the elderly osteoporotic population.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Gut-bone axis: the incretin GLP-1, released after eating, links nutrient intake to bone remodelling (insulin already mapped), part of the enteroendocrine regulation of the postprandial suppression of bone resorption relevant to osteoporosis.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid bone loss: activation of the mineralocorticoid receptor by aldosterone promotes bone resorption and calcium loss, and primary aldosteronism is associated with osteoporosis and fracture, an endocrine driver of bone loss.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Osteoimmune balance: the anti-inflammatory IL-10 restrains the inflammatory osteoclastogenesis driven by TNF, IL-6, IL-1 and IL-17 (already mapped), so the cytokine balance of osteoimmunology shapes the bone loss of osteoporosis.
- `connects-to` → **[Bone marrow](../../05-tissue/bone-marrow/README.md)** — Marrow adiposity: with ageing and oestrogen (already mapped) loss the marrow stromal cells shift from osteoblast (already mapped) toward adipocyte differentiation (leptin and adiponectin already mapped), the fatty marrow accompanying the bone loss of osteoporosis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and bone quality: magnesium is a structural mineral of the bone matrix and a cofactor for the PTH and vitamin-D (already mapped) function, so its deficiency impairs bone quality and contributes to osteoporosis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Osteoimmune type-2 arm: IL-4, with IL-10 (already mapped), restrains the inflammatory osteoclastogenesis (RANKL, TNF and IL-17 already mapped), part of the osteoimmune cytokine balance that shapes the bone loss of osteoporosis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Collagen cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) of the bone matrix, and copper deficiency (as in Menkes) causes a bone fragility, part of the trace-metal contribution to bone quality.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Osteoimmune type-2 cytokine: IL-13, with IL-4 (already mapped), is part of the type-2 arm that restrains the inflammatory osteoclastogenesis (RANKL, TNF and IL-17 already mapped) of the bone loss of osteoporosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine bone loss: resistin, with leptin and adiponectin (already mapped), promotes the osteoclastogenesis (RANKL already mapped) and the inflammatory bone loss, part of the adipokine influence on the skeleton in osteoporosis.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Bone-mass loss: the cortical and trabecular bone loses the mass and the microarchitecture in osteoporosis, the fragility fractures the consequence of the impaired bone tissue.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Bone phosphate: the phosphate (with the calcium already mapped) forms the hydroxyapatite mineral, and the FGF23 and PTH (already mapped) phosphate axis governs the bone-mineral balance of osteoporosis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin-D mineralisation: vitamin D drives the calcium (already mapped) absorption and the bone mineralisation; its deficiency causes the osteomalacia and worsens osteoporosis, the foundation of the supplementation.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Osteoimmunology Th1: the IFN-γ of the T cells is the type-II interferon arm of the osteoimmune modulation of the RANKL (already mapped)-driven osteoclast (already mapped) bone loss of osteoporosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-bone crosstalk contributing to the bone loss of osteoporosis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate osteoimmune interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, modulates the osteoclast (already mapped) differentiation in the osteoimmunology of osteoporosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 osteoimmune arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the osteoimmune crosstalk that modulates the bone loss of osteoporosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 osteoclast axis: IL-23 sustains the Th17 (IL-17 already mapped) cells that drive the RANKL (already mapped)-mediated osteoclast (already mapped) bone resorption of osteoporosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune-bone crosstalk of osteoporosis.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Th17 osteoimmunology: the CD4 T-helper cells, the source of the Th17 (IL-17 and IL-23 already mapped) cytokines, drive the RANKL (already mapped)-mediated osteoclast (already mapped) bone resorption of osteoporosis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell osteoporosis: the mast cells, via their histamine and cytokines, promote the osteoclast (already mapped) resorption, a link seen most starkly in the systemic-mastocytosis osteoporosis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Immunoporosis: the B cells are a source of the RANKL (already mapped) and osteoprotegerin that tune the osteoclast (already mapped) balance of the immune-bone crosstalk of osteoporosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory osteoclastogenesis of the immune-bone crosstalk of osteoporosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) promotes the osteoclast (already mapped) differentiation of the inflammatory bone loss of osteoporosis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron-bone axis: transferrin, the iron carrier, reflects the disordered iron handling whose overload impairs the osteoblast (already mapped) function and drives the bone loss of osteoporosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-osteoclast axis: TSLP, from skin (already mapped) and mucosal barriers, primes dendritic cells (already mapped) and mast cells (already mapped) and activates the RANKL-osteoclast (already mapped) axis contributing to the bone loss of osteoporosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-bone axis: bradykinin, via B2R on osteoblasts (already mapped) and osteoclasts (already mapped), modulates the bone remodelling balance, with B2R activation promoting osteoclastogenesis and the bone resorption of osteoporosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Bone-marrow EPO axis: erythropoietin, via EpoR on osteoblast progenitors in the bone marrow (already mapped), modulates the osteoblast-erythroid lineage competition and the bone formation relevant to the bone loss of osteoporosis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Bone-protective chronobiology: melatonin, produced by bone-marrow (already mapped) stromal cells, acts on MT2 receptors on osteoblasts (already mapped) to stimulate bone formation and inhibit osteoclast (already mapped) resorption, directly opposing the bone loss of osteoporosis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-bone axis: C1-esterase inhibitor regulates the classical-complement (complement C5 already mapped) activation in the bone microenvironment, tempering complement-driven osteoclast (already mapped) recruitment and the inflammatory bone resorption of osteoporosis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation in bone: factor H limits alternative-pathway activation on the bone-marrow (already mapped) surface and osteoclast (already mapped) progenitors, regulating the complement (complement C5 already mapped) contribution to the bone resorption of osteoporosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Bone-remodelling neuroendocrine: prolactin, via PRLR on osteoblasts (already mapped), modulates bone formation; hyperprolactinaemia suppresses estrogen (already mapped) and testosterone (already mapped), amplifying RANKL (already mapped)-driven osteoclastogenesis of osteoporosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Bone formation promoter: oxytocin, via OXTR on osteoblasts (already mapped) and osteoclasts (already mapped), promotes bone formation and inhibits resorption; oxytocin deficiency amplifies RANKL (already mapped) and TNF-α (already mapped) bone loss of osteoporosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Bone density modulator: vasopressin, via V1aR on osteoblasts (already mapped) and osteoclasts (already mapped), modulates bone density; vasopressin dysregulation amplifies RANKL (already mapped) and IL-6 (already mapped) osteoclast resorption of osteoporosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant bone-remodelling: selenium, as selenoprotein antioxidant in osteoblasts (already mapped) and osteoclasts (already mapped), limits the ROS-driven RANKL (already mapped) and TNF-α (already mapped) signalling of the bone-resorption cascade of osteoporosis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-bone axis: iodine-dependent thyroid hormones regulate osteoblast (already mapped) activity and bone mineral density; iodine deficiency amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclast resorption of osteoporosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Acid-buffering bone protection: potassium alkalinity buffers the acid load that drives osteoclast (already mapped) RANKL (already mapped)-mediated bone resorption; potassium deficiency amplifies the acid-driven IL-6 (already mapped) and TNF-α (already mapped) bone loss of osteoporosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — OP iron: iron supports macrophage (already mapped) and osteoclast (already mapped) regulation; iron deficiency amplifies NF-κB (already mapped) and RANKL (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) driven osteoclastic bone resorption in osteoporosis.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Osteoporosis chloride: chloride, via osteoclast (already mapped) V-type H⁺-ATPase, acidifies the resorption lacuna; chloride imbalance amplifies the RANKL (already mapped) and NF-κB (already mapped) osteoclast drive and IL-6 (already mapped) bone-loss cascade of osteoporosis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Osteoporosis sulfur: sulfur-containing GAGs form the proteoglycan matrix anchoring osteoblast (already mapped) mineralisation; sulfur deficiency amplifies the RANKL (already mapped) and TNF-α (already mapped) osteoclastic bone resorption cascade of osteoporosis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Osteoporosis nitrogen: nitrogen is the backbone of collagen (already mapped) and proteoglycan in bone; nitrogen deficiency (protein malnutrition) amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclastic cascade and impairs osteoblast (already mapped) repair.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Osteoporosis carbon: carbon as backbone of collagen (already mapped) and proteoglycan scaffold in bone sustains osteoblast (already mapped) matrix production; carbon depletion amplifies the RANKL (already mapped) and IL-6 (already mapped) osteoclastic cascade of osteoporosis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Osteoporosis hydrogen: hydrogen, via redox homeostasis in osteoblasts (already mapped) and osteoclasts, supports collagen (already mapped) cross-linking; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) bone resorption cascade of osteoporosis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Osteoporosis oxygen: oxygen availability in bone marrow drives osteoblast (already mapped) energy metabolism via mitochondrial oxidative phosphorylation; hypoxia amplifies RANKL (already mapped) and NF-κB (already mapped) osteoclastic resorption cascade of osteoporosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Osteoporosis PD-1: PD-1 on T-cells (already mapped) in bone marrow suppresses osteoclast (already mapped)-activating immune responses; PD-1 dysregulation amplifies RANKL (already mapped) and NF-κB (already mapped) bone resorption cascade of osteoporosis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Osteoporosis angiotensin-II: angiotensin-II in bone marrow vasculature modulates osteoblast (already mapped) and osteoclast differentiation; angiotensin-II excess amplifies RANKL (already mapped) and NF-κB (already mapped) bone loss cascade of osteoporosis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Osteoporosis IL-2: IL-2 from T-cells (already mapped) in bone marrow regulates osteoclast (already mapped) precursor expansion; IL-2 excess amplifies RANKL (already mapped) and NF-κB (already mapped) and TNF-α (already mapped) bone resorption cascade of osteoporosis.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Osteoporosis wnt-beta-catenin: WNT/β-catenin on osteoblasts (already mapped) and macrophages (already mapped) drives bone anabolic balance; wnt-beta-catenin loss amplifies rankl (already mapped) and nf-kb (already mapped) and tnf-alpha (already mapped) cascade of osteoporosis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Osteoporosis rankl: RANKL from osteoblasts (already mapped) and macrophages (already mapped) drives osteoclast bone resorption; rankl excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and il-6 (already mapped) bone resorption cascade of osteoporosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Osteoporosis smad4: SMAD4 in osteoblasts (already mapped) and macrophages (already mapped) mediates TGF-β bone repair signalling; smad4 dysregulation amplifies rankl (already mapped) and nf-kb (already mapped) and tnf-alpha (already mapped) cascade of osteoporosis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Osteoporosis fibronectin: fibronectin in osteoblasts (already mapped) and osteoclasts (already mapped) promotes bone ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Osteoporosis activin-a: activin-A from osteoblasts (already mapped) and osteoclasts (already mapped) drives bone resorption; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Osteoporosis cgrp: CGRP from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone vascular tone; cgrp dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Osteoporosis substance-p: substance-P from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone immune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) bone-loss cascade of osteoporosis.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Osteoporosis insulin-receptor: insulin receptor on osteoblasts (already mapped) and osteoclasts (already mapped) drives bone metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — OP androgen-receptor: androgen receptor on osteoblasts (already mapped) and osteoclasts (already mapped) modulates steroid signalling; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — OP norepinephrine: Norepinephrine from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone stress tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — OP adrenomedullin: Adrenomedullin from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone vascular tone; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — OP bdnf: BDNF from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone neural tone; bdnf excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — OP fgfr: FGFR signalling on osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone proliferation; fgfr excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — OP epinephrine: epinephrine from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — OP renin: renin from osteoblasts (already mapped) and osteoclasts (already mapped) modulates bone RAAS activation; renin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and rankl (already mapped) cascade of osteoporosis.

[^kanis-2019-who-osteoporosis]: Kanis JA, Cooper C, Rizzoli R, Reginster JY. European guidance for the diagnosis and management of osteoporosis in postmenopausal women. *Osteoporos Int.* 2019;30(1):3-44. [doi:10.1007/s00198-018-4704-5](https://doi.org/10.1007/s00198-018-4704-5) · [PubMed 30324412](https://pubmed.ncbi.nlm.nih.gov/30324412/)
[^cosman-2016-romosozumab]: Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. *N Engl J Med.* 2016;375(16):1532-1543. [doi:10.1056/NEJMoa1607948](https://doi.org/10.1056/NEJMoa1607948) · [PubMed 27641143](https://pubmed.ncbi.nlm.nih.gov/27641143/)
[^cummings-2009-denosumab-freedom]: Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. *N Engl J Med.* 2009;361(8):756-765. [doi:10.1056/NEJMoa0809493](https://doi.org/10.1056/NEJMoa0809493) · [PubMed 19671655](https://pubmed.ncbi.nlm.nih.gov/19671655/)
