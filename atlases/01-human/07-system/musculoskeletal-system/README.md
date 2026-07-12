---
schema: human-scale-entry/v1
id: musculoskeletal-system
name: Musculoskeletal System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "206 bones and ~600 skeletal muscles providing support, movement, haematopoiesis, mineral homeostasis, thermogenesis, and endocrine signaling via osteocalcin and myokines (IL-6, irisin, BDNF)."
aliases: ["locomotor system", "skeletal system", "muscular system", "myoskeletal system"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: contains
    note: "Red bone marrow (flat bones, vertebrae, proximal femur/humerus in adults) is the primary haematopoietic organ; osteoblasts regulate the HSC niche via CXCL12, SCF, and angiopoietin-1."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Skeletal muscle exercise drives cardiac output (↑HR, ↑SV, ↑CO); metabolites (CO₂, H⁺, K⁺, adenosine) trigger local vasodilation; myokines (IL-6, VEGF) promote capillary angiogenesis."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Bone marrow is the site of HSC haematopoiesis producing all immune cells; exercise-induced IL-6 from muscle induces anti-inflammatory IL-10/IL-1RA; muscle wasting in cachexia is driven by TNF-α/IL-6."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Motor neurons innervate skeletal muscle via NMJ (ACh/nicotinic); sensory innervation via muscle spindles (Ia), Golgi tendon organs (Ib); spinal reflexes and cerebellar coordination govern muscle tone."
  - target: 03-medicine/03-food/vitamin-d
    relation: modulated-by
    note: "Modulated by Vitamin D (Calciferol)."
  - target: 03-medicine/03-food/zinc-dietary
    relation: modulated-by
    note: "Modulated by Dietary Zinc."
  - target: 01-human/03-molecular/myostatin
    relation: modulated-by
    note: "Myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA."
  - target: 01-human/03-molecular/igf-1
    relation: modulated-by
    note: "IGF-1 → IGF-1R → IRS-1 → PI3K/Akt/mTOR → skeletal muscle protein synthesis and satellite cell activation; opposes myostatin/SMAD2/3 atrophy signaling; IGF-1 drives osteoblast bone matrix synthesis; declining IGF-1 with aging contributes to sarcopenia and osteoporosis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The musculoskeletal and integumentary systems form the body's structural exterior: skin, fascia, tendon, muscle and bone are a continuum of collagen-based connective tissue sharing vitamin D dependence, so heritable collagen disorders (Ehlers-Danlos, Marfan) affect both."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Osteoblasts build the skeleton of the musculoskeletal system: they deposit and mineralize bone's collagen matrix, balance osteoclast resorption via RANKL/OPG, and help regulate the marrow niche; their decline with age and estrogen loss underlies osteoporosis and fracture."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is foundational to the musculoskeletal system at two scales: hydroxyapatite gives bone its hardness and the skeleton stores 99% of body calcium, while calcium influx drives actin-myosin cross-bridge cycling in muscle contraction; PTH and vitamin D balance this reservoir."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Sex hormones from the reproductive system build the musculoskeletal system: testosterone and estrogen drive the pubertal growth spurt, muscle mass, and peak bone density, while menopausal estrogen loss accelerates osteoporosis—tying gonadal function to skeletal health."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The musculoskeletal system is under tight endocrine control: growth hormone/IGF-1, thyroid hormone, PTH, vitamin D, and sex steroids govern bone and muscle, while bone itself secretes osteocalcin and FGF23—so endocrine disease often presents as fractures or weakness."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Bone is continuously remodeled by the osteoclast-osteoblast balance: osteoclasts resorb old bone while osteoblasts rebuild it, and tipping toward resorption (estrogen loss, RANKL excess) causes osteoporosis—the target of bisphosphonates and denosumab."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Osteoporosis is the commonest disease of the musculoskeletal system's bone: an imbalance favoring osteoclast resorption over osteoblast formation thins the skeleton, so fractures of the hip, spine and wrist are the system's leading cause of disability in older adults."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Osteosarcoma is the principal primary bone cancer of the musculoskeletal system: malignant osteoblasts produce disorganized bone, striking the metaphyses of growing adolescents—turning the system's bone-building machinery into an aggressive, lung-metastasizing tumor."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Rheumatoid arthritis is the archetypal autoimmune disease of the musculoskeletal system's joints: immune attack on the synovium forms an invasive pannus that erodes cartilage and bone, deforming joints—autoimmunity striking the skeleton's moving parts."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen is the musculoskeletal system's structural protein: type I gives bone and tendon tensile strength while type II builds cartilage, so collagen defects cause brittle bones (osteogenesis imperfecta) and fragile joints across the whole framework."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts knit the musculoskeletal system's soft framework: they build and repair the collagen of tendons, ligaments and fascia that transmit muscle force to bone, so their activity governs healing of sprains and the integrity of connective tissue."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Gout is a musculoskeletal disease of crystals: monosodium urate deposits in joints trigger acute inflammatory arthritis and, over years, erode bone and form tophi—linking purine metabolism to destructive joint and bone disease."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Bone is built of calcium phosphate, so phosphorus is as essential as calcium to the skeleton: it forms hydroxyapatite crystals that harden bone, and disturbed phosphate handling—as in rickets and renal osteodystrophy—softens and deforms it."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Ankylosing spondylitis attacks the musculoskeletal system: inflammation at entheses where ligaments meet bone heals by ossification, fusing the spine into a rigid 'bamboo' column—showing how the skeleton's response to inflammation can be new bone, not just erosion."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Fibromyalgia presents as a musculoskeletal disease without musculoskeletal damage: widespread muscle and joint pain and tenderness arise from amplified central pain processing, not inflammation or structural injury—so the muscles and bones ache while tests stay normal."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Parathyroid hormone is the master switch of bone remodeling: PTH pulls calcium from bone when blood levels fall, yet given intermittently it builds bone—so the musculoskeletal skeleton doubles as the body's calcium bank under PTH control."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium is essential to bone and muscle: about half the body's magnesium sits in bone as a mineral reservoir, and it is required for muscle contraction and relaxation—so deficiency causes cramps, weakness and impairs bone quality."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Osteocytes tune bone strength through sclerostin: this Wnt-pathway inhibitor brakes bone formation, and mechanical loading lowers it to build bone—so blocking sclerostin (romosozumab) is a potent way to rebuild the osteoporotic skeleton."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Every muscle move starts with acetylcholine: motor neurons release it at the neuromuscular junction to depolarize muscle fibers, so this transmitter is the on-switch that turns nerve commands into the musculoskeletal system's movement."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "The musculoskeletal system runs on ATP: muscle contraction and—crucially—relaxation both burn ATP to cycle myosin and pump calcium, which is why energy failure causes cramps and why rigor mortis sets in when ATP runs out after death."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Muscle and nerve excitability ride on potassium: the ion sets the resting membrane potential that lets muscle fibers fire, so potassium swings cause the weakness or paralysis of periodic paralysis and dangerous arrhythmias."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bone depends on the kidney: it activates vitamin D and balances calcium and phosphate, so kidney failure starves bone of minerals and unleashes parathyroid hormone, crumbling the skeleton in renal osteodystrophy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The skeleton is built with help from photons: ultraviolet light striking the skin makes vitamin D, the hormone that lets the gut absorb the calcium needed to mineralize bone, linking sunlight to skeletal strength."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen guards the skeleton: it restrains the osteoclasts that resorb bone, so the sharp loss of estrogen at menopause speeds bone breakdown and is the leading driver of osteoporosis in women."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Muscle obeys peripheral nerves: motor fibers carry the command to contract while sensory fibers report position, so nerve injury denervates muscle and wastes it, severing the skeleton from its control."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver fuels muscle and bone growth: under growth-hormone control it makes IGF-1, the systemic signal that drives the building of skeletal muscle and the lengthening of bone."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Muscle stores its own oxygen on iron: myoglobin, an iron-containing protein, holds oxygen inside muscle fibers for the bursts of work that movement demands, tinting muscle red."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals how the body moves and stands: muscle's interdigitating actin and myosin filaments sliding past their Z-discs, and bone's collagen fibrils studded with hydroxyapatite crystals around osteocytes in their lacunae."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium fires the command to move: a nerve impulse floods sodium into the muscle membrane, and the spreading depolarization sweeps down the T-tubules to release the calcium that triggers each contraction."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Troponin is the switch that lets muscle pull: when calcium binds it, the complex shifts tropomyosin off the actin filament, baring the sites where myosin grabs on — the molecular trigger that turns a calcium signal into force."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Growth hormone builds the system in childhood and maintains it after: it lengthens bone at the growth plates, spurs muscle protein synthesis through IGF-1, and its lifelong decline contributes to the muscle and bone loss of aging."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Testosterone is the body's chief anabolic signal for muscle and bone: it enlarges muscle fibers and raises bone density, so its fall with age or hypogonadism drives the sarcopenia and osteoporosis of the aging skeleton."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol is the catabolic counterweight: chronic excess — from disease or steroid drugs — breaks down muscle protein into a proximal myopathy and strips bone into osteoporosis, the opposite of the anabolic hormones' effects."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies can turn on muscle and joint: anti-acetylcholine-receptor antibodies weaken the neuromuscular junction in myasthenia gravis, and myositis-specific autoantibodies attack muscle directly, the immune system mistaking the motor system for the enemy."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Muscle is the body's main glucose sink: insulin drives sugar uptake into muscle and stimulates its protein synthesis, so insulin resistance both raises blood glucose and accelerates the muscle loss of aging and metabolic disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Working muscle is hungry for oxygen the red cells carry: exercise raises oxygen demand and stimulates erythropoietin, while the marrow that makes erythrocytes sits inside the very bones the system is built from."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Bone is rebuilt by a molecular tug-of-war: osteoblasts release RANKL to wake the osteoclasts that resorb bone, and decoy osteoprotegerin restrains them, so this RANKL/OPG balance sets whether the skeleton thickens or thins."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Muscle is only as strong as its nerve signal: in myasthenia gravis antibodies block the acetylcholine receptors at the neuromuscular junction, so intact muscle fatigues and fails despite its machinery, the system crippled at its electrical switch."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The skeleton is mineralized from the gut: the small intestine absorbs dietary calcium and phosphate under vitamin D's control, so malabsorption starves bone of its raw material and drives osteomalacia and fracture."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Bone is built on a Wnt switch: Wnt/β-catenin signaling drives osteoblasts to lay down bone, which is why the natural Wnt-brake sclerostin restrains it and why blocking sclerostin builds bone in osteoporosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat infiltrates the aging frame: marrow fills with adipocytes as bone is lost, and fat marbles aging muscle as myosteatosis, so the same shift toward fat weakens both bone and muscle in sarcopenic obesity."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys derange the skeleton: chronic kidney disease disrupts the phosphate, vitamin D and PTH balance, producing renal osteodystrophy — the brittle, painful bone disease of CKD-mineral and bone disorder."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "A small-round-cell cancer arises in its bones: Ewing sarcoma, driven by the EWSR1-FLI1 fusion, grows in the long bones and pelvis of children and young adults, a distinct primary bone malignancy alongside osteosarcoma."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Its muscle precursors can turn malignant: rhabdomyosarcoma arises from cells of the skeletal-muscle lineage, the most common soft-tissue sarcoma of childhood and the muscular counterpart to the system's bone cancers."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "A cytokine couples inflammation to wasting: IL-6 promotes osteoclast-driven bone resorption and muscle catabolism, so chronic elevations drive the bone loss and sarcopenia seen in aging and inflammatory disease — yet exercise releases it transiently as a beneficial myokine."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "It is the classic invader of bone and joint: Staphylococcus aureus is the leading cause of osteomyelitis and septic arthritis, seeding bone and synovium through the blood or open wounds to destroy musculoskeletal tissue."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Immune attack inflames its joints and entheses: psoriatic arthritis is an inflammatory disease of the musculoskeletal system, damaging joints and the tendon-bone insertions through IL-17/IL-23-driven inflammation."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Autoimmunity attacks the muscle itself: dermatomyositis is an inflammatory myopathy of the musculoskeletal system, with immune-mediated injury to skeletal muscle producing the proximal weakness that defines it."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Muscle is the body's main glucose sink: skeletal muscle takes up most insulin-stimulated glucose, so its mass and insulin sensitivity drive metabolic health, while diabetes in turn causes sarcopenia and stiff-joint syndromes."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess load wears the joints: obesity mechanically overloads weight-bearing joints toward osteoarthritis, and adipose-muscle crosstalk worsens the sarcopenia and inflammation of the musculoskeletal system."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic pain and disability weigh on mood: persistent musculoskeletal pain and the loss of mobility and independence it brings are strongly tied to depression, each amplifying the other."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Bone and muscle depend on what the gut absorbs: calcium and vitamin D uptake builds bone, and protein absorption sustains muscle, so malabsorption causes osteomalacia and sarcopenia."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Muscles and the rib cage power breathing: the diaphragm and intercostals drive ventilation, so neuromuscular weakness and chest-wall deformities like scoliosis cause restrictive respiratory failure."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Bones house the blood-and-immune factory: the marrow within the skeleton is where haematopoiesis and B-cell development occur, making the musculoskeletal system a primary site of the lymphatic and immune system."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney governs bone mineral: by controlling calcium, phosphate and active vitamin D, the kidneys keep the skeleton mineralised, so renal failure causes renal osteodystrophy with weakened, painful bones."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis can erode the skeleton: spinal TB (Pott's disease) destroys vertebrae and can cause gibbus deformity and cord compression, while tuberculous arthritis attacks large joints."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Magnesium underpins bone: most body magnesium is stored in bone, and it is required to activate vitamin D and regulate parathyroid hormone, so deficiency contributes to weak bones and muscle cramps."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "NSAIDs are its mainstay painkiller: drugs like ibuprofen relieve the pain and inflammation of arthritis and injury, though gastric and renal side effects limit long-term use."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Strep attacks muscle and joints: Streptococcus pyogenes causes necrotising fasciitis and pyomyositis, and triggers post-streptococcal reactive arthritis and rheumatic fever."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 fats calm inflamed joints: their anti-inflammatory effects are studied for joint pain and stiffness in rheumatoid and osteoarthritis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids both treat and harm it: intra-articular and systemic corticosteroids relieve inflammatory joint and muscle disease, but long-term use causes osteoporosis, avascular necrosis and a proximal myopathy."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "A virus that inflames muscle: Coxsackievirus B causes Bornholm disease (epidemic pleurodynia) with severe muscle pain, and viral myositis more broadly."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: connects-to
    note: "A classic cause of bone infection: Salmonella is a characteristic cause of osteomyelitis in sickle cell disease, alongside the more common staphylococcal bone and joint infections."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "The hard substance of the skeleton: dense cortical bone gives the musculoskeletal system its strength and lever arms, continuously remodelled by osteoblasts and osteoclasts under load (Wolff's law), and failing as fractures when it thins."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Where nerve commands muscle: the neuromuscular junction translates motor-nerve impulses into contraction via acetylcholine, the synapse whose failure — in myasthenia gravis or with paralytics — silences the musculoskeletal system."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "A common cause of muscle complaints: statins are the most frequent drug cause of myalgia and, rarely, rhabdomyolysis, making muscle symptoms a routine consideration whenever the musculoskeletal system is assessed in statin users."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "A heritable connective-tissue disorder of the frame: Marfan syndrome's fibrillin-1 defect lengthens the limbs (arachnodactyly, tall stature) and brings scoliosis, pectus deformity and joint laxity—the skeleton built on faulty connective tissue."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "A cancer that dissolves bone: myeloma plasma cells activate osteoclasts via RANKL while suppressing osteoblasts, carving the lytic lesions, pathological fractures and hypercalcaemia that make it a disease of the skeleton."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "When the nerve dies, the muscle wastes: amyotrophic lateral sclerosis kills the motor neurons driving skeletal muscle, so progressive denervation atrophy and weakness destroy the musculoskeletal system's power despite initially healthy muscle fibres."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Bone as a target of sickling: vaso-occlusion causes painful bone infarcts, avascular necrosis of the femoral head and childhood dactylitis, and raises the risk of Salmonella osteomyelitis in the skeleton."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Bleeding into the joints: recurrent haemarthrosis in haemophilia A destroys cartilage and synovium, producing a crippling chronic arthropathy that is a major musculoskeletal burden of the disease."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "A soft-tissue cancer near the joints: synovial sarcoma arises in the limbs around joints and tendons (despite its name, not from synovium), a malignant counterpart to the system's many benign soft-tissue tumours."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Bone as a metastatic home: the skeleton is the dominant site of prostate cancer spread, forming characteristic osteoblastic lesions and skeletal-related events—pain, fractures and cord compression—that define the disease's course."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Lytic bone metastases: breast cancer seeds the skeleton with osteolytic and mixed lesions that fracture and release calcium, making bone a sanctuary site and a major source of morbidity treated with bone-targeted agents."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Muscle and the virus: COVID-19 causes myalgia, occasional rhabdomyolysis and post-viral myositis, and the prolonged muscle weakness and pain of long COVID are a notable musculoskeletal legacy."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Bone's phosphate hormone: FGF23 secreted by bone osteocytes is the master regulator of phosphate balance, linking the skeleton to the kidney and disturbed in chronic kidney-mineral-bone disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fat-bone-muscle crosstalk: leptin from adipose tissue regulates bone mass and muscle through central and peripheral pathways, linking adiposity to musculoskeletal health."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Matrix coupling factor: TGF-β stored in bone matrix couples resorption to formation and orchestrates the repair of muscle, tendon and bone after injury."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Bone matrix glue: osteopontin in the mineralised matrix anchors osteoclasts to bone for resorption and regulates mineralisation, a key non-collagenous protein of skeletal remodelling."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Turnover and muscle tone: thyroid hormones set the pace of bone remodelling and skeletal-muscle metabolism, so thyroid excess accelerates bone loss and causes myopathy across the musculoskeletal system."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Skeletal angiogenesis: VEGF couples blood-vessel growth to endochondral ossification and fracture repair, and supplies the capillary network that sustains skeletal muscle."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Osteoclast brake: calcitonin from thyroid C cells directly inhibits osteoclast bone resorption and lowers serum calcium, a counterweight to PTH in the calcium and bone-remodelling balance of the skeleton."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Remodelling and repair: prostaglandins (PGE2) regulate bone formation and resorption and are essential for fracture healing, which is why NSAIDs that block their synthesis can impair bone union."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Mechanotransduction: osteocytes release nitric oxide in response to mechanical loading, the signal that translates weight-bearing exercise into the bone formation that maintains skeletal strength."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Shared currency of bone and muscle: calcium is the mineral stored as hydroxyapatite that gives bone its rigidity and the ion that triggers skeletal-muscle contraction through troponin, linking the skeleton's structural and the muscle's contractile roles."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Avascular cartilage: articular cartilage has no blood supply, so its chondrocytes survive on HIF-1α-driven anaerobic glycolysis, the hypoxic adaptation that maintains the joint surface and whose failure contributes to osteoarthritis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Bone-muscle-fat axis: adipose-derived adiponectin signals to bone and muscle, part of the endocrine crosstalk by which fat mass, bone remodelling and muscle metabolism are coordinated, integrating the musculoskeletal system with whole-body energy balance."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Progenitor fate: NOTCH signalling controls mesenchymal-progenitor commitment in bone and the satellite-cell self-renewal that regenerates skeletal muscle, a core developmental pathway of the musculoskeletal system."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Growth-plate biology: FGF/FGFR signalling regulates the chondrocyte proliferation of the growth plate that lengthens long bones, the pathway whose constitutive activation causes achondroplasia."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Repair recruitment: PDGF recruits the mesenchymal and perivascular progenitor cells that build and repair bone, muscle and connective tissue after injury throughout the musculoskeletal system."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Muscle hypertrophy: the IGF-1-AKT-mTOR pathway (IGF-1 mapped) drives the protein synthesis underlying skeletal-muscle hypertrophy, the anabolic switch that builds muscle in response to load."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Fiber-type specification: the calcium-activated phosphatase calcineurin drives NFAT-dependent slow-twitch fiber-type programming and muscle adaptation to endurance activity."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Steroid catabolism: glucocorticoids acting through the glucocorticoid receptor (cortisol mapped) cause both skeletal-muscle atrophy and osteoporosis, the dual musculoskeletal toxicity of steroid excess."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "IGF-1/insulin signalling through PI3K-AKT-mTOR (IGF-1 and mTOR mapped) governs skeletal-muscle hypertrophy and bone anabolic responses."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is a potent osteoclastogenic and catabolic cytokine driving bone resorption and muscle wasting in inflammatory and age-related musculoskeletal disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A links immune activation to bone and joint pathology, driving osteoclastogenesis and the enthesitis of spondyloarthritis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β/BMP-SMAD signalling (TGF-β already mapped) governs bone and cartilage formation and the matrix homeostasis of the musculoskeletal system."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling drives the muscle wasting and bone remodelling shared across catabolic and inflammatory disorders of the musculoskeletal system."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates chondrocyte and osteoclast biology and the inflammatory matrix remodelling of the musculoskeletal system."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the osteoblast-osteoclast balance, the atrogene muscle-atrophy program, and oxidative-stress defense across the musculoskeletal system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of growth factors (FGFR and IGF-1 already mapped) drives osteoblast and myocyte proliferation and differentiation in the musculoskeletal system."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling modulates osteoclastogenesis and the inflammatory regulation of bone and muscle in the musculoskeletal system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt/β-catenin signaling that governs osteoblast differentiation (Wnt already mapped), regulates the bone formation and remodeling of the musculoskeletal system."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins participate in the inflammatory signaling of bone and joint tissue in the musculoskeletal system."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Connexin-43 gap junctions mediate the osteocyte-network and muscle intercellular communication that coordinates mechanotransduction in the musculoskeletal system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the osteoblast, chondrocyte, and myocyte growth and survival of the musculoskeletal system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK integrates the energy status of muscle and bone, coupling metabolism to musculoskeletal adaptation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB signaling drives the osteoclastogenesis (RANKL already mapped) and inflammatory remodeling of the musculoskeletal system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the myofiber, chondrocyte, and osteocyte homeostasis of the musculoskeletal system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the osteoclast function and mechanotransduction of the musculoskeletal system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the osteogenic, chondrogenic, and myogenic differentiation of the musculoskeletal system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the immune-cell trafficking within the bone and muscle tissues of the musculoskeletal system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the bone-marrow-niche, osteogenic, and muscle-stem-cell interactions of the musculoskeletal system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the bone and joint remodeling of the musculoskeletal system."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Bone and muscle mineral: roughly 60% of body magnesium is stored in bone, and magnesium is essential for neuromuscular excitability and as an enzyme cofactor, so deficiency produces cramps, weakness and impaired bone quality."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Muscle excitability: potassium gradients set the resting membrane potential of skeletal muscle, and hypo- or hyperkalaemia cause the weakness and paralysis that link electrolyte balance directly to musculoskeletal function."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Gut-bone axis: gut-derived serotonin acts on osteoblasts to restrain bone formation, a systemic regulator of skeletal mass that connects the musculoskeletal system to enteric endocrine signalling beyond the local bone factors."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Matrix and cartilage: zinc is a cofactor for the collagen-processing and matrix metalloproteinase enzymes of bone and cartilage (collagen already mapped), and its deficiency impairs growth and skeletal development."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Inflammatory arthritis: rheumatoid arthritis attacks the synovial joints of the musculoskeletal system, with immune-driven synovitis eroding cartilage and bone (RANKL already mapped) to cause the joint destruction and deformity of the disease."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Musculoskeletal pain: pain from bones, joints and muscles is among the leading reasons for analgesic use, and opioids acting on the mu-opioid receptor are used, with well-known risks, for severe musculoskeletal pain."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Nociceptive innervation: substance P released by the sensory nerves of bone, joint and muscle signals the pain of musculoskeletal injury and inflammation (mu-opioid receptor already mapped), and it also participates in the neural regulation of bone remodelling."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Skeletal sensory nerves: CGRP-containing sensory fibres richly innervate the periosteum and bone, contributing to musculoskeletal pain (substance P already mapped) and to the regulation of bone formation and blood flow."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate and oxidative joint injury: xanthine oxidase produces the uric acid whose crystals cause gout in the joints, and the reactive oxygen species it generates add to the oxidative damage of inflammatory and degenerative musculoskeletal disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Motor innervation: the motor neurons drive skeletal muscle at the neuromuscular junction (acetylcholine already mapped), and the sensory neurons carry the proprioception and pain (substance P and CGRP already mapped) of the musculoskeletal system."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Osteoclasts and muscle repair: the macrophage lineage gives rise to the bone-resorbing osteoclasts (RANKL already mapped) and to the muscle-repair macrophages, central to remodelling and regeneration in the musculoskeletal system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 tissue repair: IL-4 drives the M2 macrophages (already mapped) that support muscle regeneration and resolve inflammation, part of the type-2 immunity that shapes repair in the musculoskeletal system."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Connective-tissue cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) and elastin of bone, tendon and ligament, and its deficiency (as in Menkes) causes bone fragility and connective-tissue weakness."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Muscle antioxidant defence: selenium is essential for the selenoprotein antioxidant defence of muscle, and severe deficiency causes a myopathy (as in Keshan disease) of the musculoskeletal system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine-bone crosstalk: resistin, with leptin and adiponectin (already mapped) from the marrow adipocytes (already mapped), is part of the adipokine influence on the bone and muscle metabolism of the musculoskeletal system."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Marrow adipocytes: the marrow adipocytes (the source of leptin, adiponectin and resistin already mapped) of the musculoskeletal system's bone marrow influence the bone and haematopoiesis, expanding with age and osteoporosis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Bone mineralisation: vitamin D drives the intestinal calcium (already mapped) absorption and the bone mineralisation (PTH already mapped); its deficiency causes the rickets and osteomalacia of the musculoskeletal system."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Connective-tissue fibroblasts: the fibroblasts of the tendons, ligaments and fascia synthesise the collagen (already mapped) matrix of the musculoskeletal system's soft connective tissues."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Inflammatory myopathy: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated inflammatory myopathies and arthritides of the musculoskeletal system."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 muscle immunity: IL-13, with IL-4 (already mapped), is the type-2 immune arm implicated in the muscle repair and the eosinophilic/fibrosing myopathies of the musculoskeletal system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the eosinophilic myositis and fasciitis of the musculoskeletal system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory myopathies and arthritides of the musculoskeletal system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the spondyloarthritis and the enthesitis of the musculoskeletal system."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon myopathy: the type-I interferon signature drives the inflammatory myopathies (the dermatomyositis) of the musculoskeletal system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory and allergic disorders of the musculoskeletal system."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Synovial/bone mast cells: the mast cells of the synovium, bone and muscle contribute to the inflammation and the tissue remodelling of the musculoskeletal system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the autoimmune arthritis and myositis of the musculoskeletal system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Joint/bone complement: the complement C3 activation contributes to the inflammatory dimension of the synovium, cartilage and bone in the arthritides of the musculoskeletal system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the neutrophil recruitment and promotes the osteoclast (already mapped) differentiation in the inflamed joints of the musculoskeletal system."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Synovial antigen presentation: the dendritic cells present antigen to the T cells (already mapped) in the autoimmune arthritis of the musculoskeletal system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Synovial alarmin: TSLP, released from synovial fibroblasts under mechanical and inflammatory stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the immune-driven joint and bone inflammation of the musculoskeletal system."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Joint kinin pain: bradykinin, generated by the kallikrein-kinin system activated in the inflamed synovium, amplifies the nociception via B1/B2 receptors on the peripheral nerves (already mapped) and the vascular permeability of the arthritic joints of the musculoskeletal system."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Bone-EPO axis: erythropoietin, acting on EPOR-expressing osteoblasts (already mapped) and osteoclasts (already mapped), modulates bone remodelling (RANKL already mapped) and supports the haematopoietic niche of the bone marrow (already mapped) of the musculoskeletal system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Joint complement/kinin regulator: the C1-esterase inhibitor limits the classical complement and contact-kinin (bradykinin already mapped) pathways activated in the inflamed synovium, moderating the cartilage-destructive complement cascade of the musculoskeletal system."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell joint effector: histamine, released by mast cells (already mapped) in the synovium and periosteum, amplifies the vascular permeability, nociception and the inflammatory cytokine cascade (IL-1/TNF already mapped) of the musculoskeletal system."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Periosteal and tendon ECM: periostin, expressed in the periosteum, tendons and entheses, maintains the structural integrity of these fibrous connective tissues and promotes bone remodelling (RANKL and osteoblast already mapped) of the musculoskeletal system."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "MS melatonin: melatonin, via MT1/MT2 receptors on osteoblasts (already mapped), attenuates RANKL (already mapped) osteoclastogenesis and promotes bone anabolism; melatonin also modulates the bone-marrow (already mapped) haematopoietic niche and reduces musculoskeletal pain."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "MS prolactin: prolactin, via prolactin receptors on osteoblasts (already mapped), promotes bone anabolism and muscle protein synthesis; prolactin modulates the reproductive (already mapped) and immune (already mapped) crosstalk of the musculoskeletal system."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MS vasopressin: vasopressin, acting on V1/V2 receptors on smooth-muscle cells, modulates the vascular tone in the musculoskeletal system; vasopressin also regulates sodium (already mapped) and water balance that affects synovial fluid composition and joint lubrication."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MS oxytocin: oxytocin receptors on osteoblasts (already mapped) suppress NF-κB (already mapped) and promote bone anabolism; oxytocin also modulates muscle regeneration and collagen (already mapped) synthesis via IL-6 (already mapped) and TNF-α (already mapped) signalling."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MS iodine: thyroid-hormone signalling drives bone-turnover balance (osteoblast/already mapped vs osteoclast/already mapped) and muscle protein synthesis; iodine deficiency impairs collagen (already mapped) synthesis and amplifies NF-κB (already mapped) inflammatory remodelling."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MS sulfur: sulfur-containing amino acids are essential for collagen (already mapped) cross-linking and cartilage proteoglycan synthesis; sulfur deficiency impairs musculoskeletal repair and amplifies NF-κB (already mapped) and TNF-α (already mapped) driven catabolic signalling."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MSK nitrogen: nitric oxide (NO, nitrogen-derived) in osteoblasts (already mapped) and macrophages (already mapped) regulates bone remodelling and skeletal vasodilation; NO imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) osteoclast-driven resorption."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MSK chloride: chloride channels on osteoclasts (already mapped) and fibroblasts (already mapped) maintain pH homeostasis for bone resorption; chloride dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) musculoskeletal remodelling."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MSK oxygen: oxygen drives aerobic energy in osteoblasts (already mapped) and macrophages (already mapped); oxygen deprivation activates HIF-1α, amplifying NF-κB (already mapped) and IL-6 (already mapped) osteoclast-driven bone resorption cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "MSK carbon: carbon, as backbone of collagen (already mapped) and proteoglycans, forms the organic matrix of bone and cartilage; carbon metabolism in osteoblasts (already mapped) shapes NF-κB (already mapped) and IL-6 (already mapped) repair cascade."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MSK hydrogen: hydrogen, as water in cartilage matrix and H₂ in synovial joints, maintains viscoelastic properties; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) musculoskeletal inflammatory cascade."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MSK PD-1: PD-1 checkpoint on T-regulatory (already mapped) and cytotoxic T-cells (already mapped) in the musculoskeletal microenvironment modulates autoimmune joint inflammation; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) erosive cascade."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "MSK GLP-1: GLP-1 receptor agonism on osteoblasts (already mapped) and macrophages (already mapped) promotes bone mineral density; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) bone-resorption cascade of musculoskeletal disease."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "MSK angiotensin-II: angiotensin-II via AT1R on osteoblasts (already mapped) and macrophages (already mapped) modulates bone remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "MSK IL-2: IL-2 from activated T-cells (already mapped) in synovium (already mapped) drives cytotoxic and T-regulatory cell expansion; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of musculoskeletal disease."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "MSK fibronectin: fibronectin in cartilage (already mapped) and synovium (already mapped) scaffolds chondrocyte adhesion and repair; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) matrix-degradation cascade of musculoskeletal disease."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "MSK activin-A: activin-A from myoblasts (already mapped) and synoviocytes (already mapped) regulates bone formation and muscle repair; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of musculoskeletal disease."
---

# Musculoskeletal System

## Overview

The musculoskeletal system encompasses the body's load-bearing framework — 206 bones in the adult skeleton — together with approximately 600 skeletal muscles (~40% of body mass), their associated tendons and ligaments, the articular cartilages of ~400 joints, and the connective tissue matrices that bind these structures together [^guyton-hall]. Far from merely providing mechanical support, this system is a major metabolic, endocrine, haematopoietic, and thermogenic organ that communicates bidirectionally with virtually every other system through circulating signals.

Key integrative roles include:
- **Mineral homeostasis**: the skeleton holds 99% of body calcium and 85% of inorganic phosphate in hydroxyapatite [Ca₁₀(PO₄)₆(OH)₂], releasing them under PTH and 1,25(OH)₂D₃ control
- **Haematopoiesis**: red bone marrow (axial skeleton and proximal long bones in adults) continuously produces all blood cell lineages
- **Endocrine**: osteocalcin from osteoblasts enters the circulation to promote insulin secretion and muscle glucose uptake; skeletal muscle secretes myokines (IL-6, irisin, BDNF, VEGF, FGF21) that coordinate whole-body metabolism
- **Thermogenesis**: shivering thermogenesis via rapid, oscillatory skeletal muscle contraction generates the majority of metabolic heat during cold exposure

## Structure

### Bone

Bones are classified by shape — long (femur, humerus), short (carpals, tarsals), flat (skull, scapula, sternum, ribs), irregular (vertebrae, facial bones), and sesamoid (patella) — and by architecture: compact (cortical) bone in diaphyses and flat bone surfaces, and cancellous (trabecular) bone at epiphyses and flat bone interiors [^guyton-hall].

The long bone anatomy:
- **Diaphysis** — shaft of compact cortical bone surrounding the medullary canal
- **Epiphyses** — expanded ends, covered by articular hyaline cartilage
- **Metaphysis** — flared junction between diaphysis and epiphysis
- **Growth plate (physis)** — hyaline cartilage disk present until skeletal maturity (~18–25 years); chondrocyte proliferation and hypertrophy, followed by vascular invasion and ossification, drive longitudinal growth under GH/IGF-1 and sex steroid control
- **Periosteum** — fibrous + cambial outer layer; osteoprogenitor cells for appositional growth and fracture repair
- **Endosteum** — inner trabecular and medullary surface; osteoprogenitor niche

**Bone cells**:
| Cell | Origin | Function |
|:---|:---|:---|
| Osteoblasts | Mesenchymal stem cells | Bone matrix synthesis (type I collagen, osteocalcin, osteopontin, bone sialoprotein); mineralization; HSC niche regulation (CXCL12, SCF, Angpt-1) |
| Osteocytes | Osteoblasts embedded in matrix | Mechanosensing via canalicular network; produce sclerostin (Wnt/LRP5 antagonist) to locally suppress formation; FGF-23 (phosphatonin) to regulate kidney Pi excretion |
| Osteoclasts | Monocyte-macrophage lineage (RANKL-driven) | Bone resorption via ruffled border proton pump (V-ATPase) + cathepsin K + MMPs; create Howship's lacunae; controlled by RANKL/RANK/OPG triad |
| Bone lining cells | Quiescent osteoblasts | Surface coverage of resting bone; activated by mechanical stimuli or PTH |

**Bone remodelling (Basic Multicellular Units)**:
The remodelling cycle continuously renews ~10% of the skeleton per year through tightly coupled osteoclast–osteoblast activity [^guyton-hall]:
1. **Activation** — osteocyte mechanosensing or systemic signals (PTH, cytokines) recruit osteoclast precursors; RANKL (from osteoblasts/osteocytes) binds RANK; OPG acts as decoy receptor, antagonizing RANKL
2. **Resorption** — osteoclasts acidify the lacunar space (V-ATPase H⁺ pumping → pH ~4.5) and secrete cathepsin K → dissolve mineral then matrix; takes 2–4 weeks
3. **Reversal** — mononuclear cells prepare the surface; coupling factors released from resorbed matrix (TGF-β, IGF-1, BMP) recruit osteoblasts
4. **Formation** — osteoblasts synthesize osteoid (type I collagen matrix), then deposit hydroxyapatite; takes 3–4 months
5. **Mineralization and rest** — mature bone; lining cells quiesce

**Regulatory signals**:
- **PTH** (parathyroid): ↑osteoclastogenesis via ↑RANKL/↓OPG; also anabolic at intermittent doses (teriparatide mechanism)
- **1,25(OH)₂D₃** (calcitriol): ↑calcium absorption (gut), ↑osteoclast differentiation; indirect anabolic effects
- **Oestrogen**: ↑OPG → ↓RANKL → ↓bone resorption; deficiency at menopause → rapid bone loss → osteoporosis
- **Testosterone**: anabolic via aromatisation to oestradiol (bone density) and direct AR-mediated effects on periosteal expansion
- **Sclerostin (SOST gene)**: Wnt/LRP5/6 antagonist from osteocytes; inhibits osteoblast bone formation; mechanically loaded bone suppresses sclerostin → localised anabolic response; target of romosozumab

### Skeletal Muscle

Each of the ~600 skeletal muscles contains bundles (fascicles) of muscle fibres (myocytes), each a multinucleated cell (10–100 μm diameter; up to 30 cm long in large muscles) derived from fusion of myoblasts during development. Each fibre is subdivided into **myofibrils** composed of sarcomeres in series (Z-disk to Z-disk, ~2.2 μm at rest) — the repeating contractile unit [^alberts-mol-cell-biology].

**Sarcomere structure**:
- **Thin filaments**: actin (F-actin, double helix), tropomyosin, troponin complex (TnC [Ca²⁺ sensor], TnI [inhibitory], TnT [tropomyosin-binding]) — anchored to Z-disk
- **Thick filaments**: myosin II hexamers (2 MHC heavy chains + 4 MLCs light chains); myosin heads (S1 subdomain) are the ATPases and actin-binding motors; arranged in A-band
- **Titin**: giant elastic protein (3.7 MDa) spanning from M-band to Z-disk; molecular spring providing passive tension in stretched sarcomeres
- **Nebulin**: actin filament length ruler in thin filaments

**Fibre types**:
| Type | Metabolism | Myosin isoform | Fatigue resistance | Function |
|:---|:---|:---|:---|:---|
| I (slow oxidative) | Oxidative; high mitochondria; myoglobin-rich (red) | MHC-I (slow, high ATPase efficiency) | Very high | Posture, prolonged low-intensity activity |
| IIa (fast oxidative-glycolytic) | Mixed | MHC-IIa | Intermediate | Intermediate activities |
| IIx/IIb (fast glycolytic) | Glycolytic; low mitochondria; pale | MHC-IIx (humans) | Low | Explosive movements, sprinting |

**Excitation-contraction (EC) coupling**:
1. Somatic motor neuron fires → ACh released at NMJ → nAChR (Nm) → end-plate potential → propagating action potential along sarcolemma
2. AP enters T-tubules → activates voltage-sensor **DHPR (L-type Ca²⁺ channel)** in T-tubule membrane
3. DHPR mechanically gates **RyR1** in sarcoplasmic reticulum (SR) → massive Ca²⁺ release from SR (cytosolic [Ca²⁺] rises from 100 nM to 10–100 μM)
4. Ca²⁺ binds troponin C → conformational change → tropomyosin shifts off actin's myosin-binding sites
5. Myosin S1 binds actin → ATP hydrolysis → power stroke (pulling thin filament toward M-line, shortening sarcomere) → ADP+Pi release → rigor state → new ATP resets
6. Relaxation: SERCA1a (sarcoplasmic/endoplasmic reticulum Ca²⁺-ATPase 1a) pumps Ca²⁺ back into SR; phospholamban (PLN) modulates SERCA; ATP-dependent

**Motor unit recruitment (Henneman's size principle)**:
Small motor units (slow type I fibres) have small, low-threshold motoneurons and are recruited first; large motor units (fast type IIx) have large, high-threshold motoneurons recruited last. This ensures smooth gradation of force and energy-efficient use of fatigue-resistant fibres for low-intensity tasks.

### Joints

| Classification | Examples | Mobility |
|:---|:---|:---|
| Fibrous (sutures) | Skull sutures, distal tibiofibular | Fixed (synarthrosis) |
| Cartilaginous (synchondrosis/symphysis) | Pubic symphysis, intervertebral discs | Slightly movable (amphiarthrosis) |
| Synovial | Knee, hip, shoulder, elbow, wrist, facets | Freely movable (diarthrosis) |

**Synovial joints** consist of articular hyaline cartilage (type II collagen, aggrecan proteoglycan — avascular, aneural; nutrition by diffusion from synovial fluid), a synovial membrane (type A macrophage-like cells + type B fibroblast-like synoviocytes secreting hyaluronic acid and lubricin for boundary lubrication), joint capsule (fibrous layer reinforced by intrinsic and extrinsic ligaments), and in some joints menisci (fibrocartilage, type I/II collagen) or labra (fibrocartilage rings increasing socket depth) [^guyton-hall].

**Cartilage types**:
- **Hyaline** (articular, growth plate, costal, tracheal): type II collagen, aggrecan; translucent; no intrinsic repair capacity once injured
- **Fibrocartilage** (menisci, IVD annulus fibrosus, pubic symphysis): type I + II collagen; tensile + compressive loading
- **Elastic** (auricle, epiglottis, larynx): type II collagen + elastin; resilient

### Tendons, Ligaments, and Entheses

**Tendons** transmit muscle force to bone. Composed predominantly of type I collagen (~65–80% dry weight), organized in a hierarchical crimp structure: collagen molecules → fibrils → fibres → fascicles → tendon. The crimp (sinusoidal waviness) provides the characteristic toe region (low stiffness at small strains) followed by the linear region (high stiffness); failure occurs at strains >8–10% [^guyton-hall].

**Ligaments** stabilize joints; type I + III collagen, slightly lower collagen density than tendons, containing more elastin; allow controlled mobility while preventing abnormal translation.

**Enthesis** — the bone-tendon/ligament insertion — is a fibrocartilaginous gradient zone (unmineralized fibrocartilage → mineralized fibrocartilage → cortical bone) that dissipates the abrupt mechanical discontinuity between compliant tendon and stiff bone. Enthesopathy (inflammation at enthesis) is a hallmark of seronegative spondyloarthropathies (e.g., ankylosing spondylitis, psoriatic arthritis).

## Function

### Mechanical and Protective Functions

- **Support and posture**: the skeleton provides the rigid framework resisting gravitational loading; continuous tonic motor unit firing in postural muscles (erector spinae, soleus) maintains upright stance
- **Locomotion**: coordinated voluntary contraction of agonist/antagonist/synergist muscle groups, controlled by descending motor pathways (corticospinal tract), basal ganglia (movement initiation and smoothing), and cerebellum (coordination and error correction)
- **Protection**: the skull (brain), vertebral column (spinal cord), ribcage (heart, lungs), and pelvis (pelvic viscera) are protective bony enclosures

### Metabolic and Endocrine Functions

**Mineral homeostasis**: the skeleton is the body's calcium reservoir; osteoclastic resorption and osteoblastic formation are continuously balanced to maintain serum ionized Ca²⁺ at 1.1–1.3 mM; regulated jointly with the kidneys and gut by PTH, calcitriol, and calcitonin [^guyton-hall].

**Haematopoiesis**: in adults, red (haematopoietically active) marrow is confined to flat bones (sternum, skull, scapulae, ribs), vertebrae, and the proximal ends of long bones (femur, humerus). Osteoblasts are essential niche cells regulating HSC quiescence and mobilisation via CXCL12/CXCR4, SCF/c-Kit, Angpt-1/Tie2, and OPN/CD44 interactions.

**Skeletal muscle as metabolic organ**: at rest, skeletal muscle accounts for ~20% of resting O₂ consumption; during maximal exercise, this rises to ~80–90%. Muscle is the dominant insulin-stimulated glucose disposal tissue (~80% of postprandial glucose uptake via GLUT4 translocation, driven by insulin → PI3K → AKT → TBC1D4 → GLUT4 exocytosis). Exercise activates AMPK → independent GLUT4 translocation (insulin-independent pathway — relevant for T2D management) [^alberts-mol-cell-biology].

**Myokines** — exercise-induced secretory proteins from contracting muscle:
| Myokine | Trigger | Key effects |
|:---|:---|:---|
| IL-6 | Muscle contraction (AMPK); glycogen depletion | Hepatic gluconeogenesis; induces anti-inflammatory IL-10 and IL-1RA; insulin-sensitising; lipolysis in adipose |
| Irisin (FNDC5 cleavage product) | Exercise via PGC-1α | Browning of white adipose tissue (↑UCP1 in subcutaneous fat); ↑BDNF in hippocampus → memory; ↑bone density |
| BDNF | Endurance exercise | Hippocampal neurogenesis; memory; motor learning |
| VEGF | Hypoxia, exercise | Angiogenesis; ↑capillary density in trained muscle |
| FGF21 | Prolonged exercise/fasting | ↑fatty acid oxidation; ↑ketogenesis; ↑insulin sensitivity |

**Thermogenesis**: shivering (involuntary rapid oscillatory skeletal muscle contractions, controlled by anterior hypothalamic cold sensors → dorsomedial hypothalamus → rostral ventromedial medulla → motor neurons) generates heat by ATP hydrolysis without net mechanical work; major source of heat production in cold exposure in adults. Non-shivering thermogenesis (BAT, UCP1) predominates in neonates and cold-adapted individuals.

### Exercise Adaptation

Chronic exercise drives profound musculoskeletal remodelling [^guyton-hall]:
- **Myofibre hypertrophy**: resistance training → mechanical stretch + mTORC1 activation → ↑muscle protein synthesis; satellite cell (muscle stem cell) activation → myonuclei addition to existing fibres
- **Mitochondrial biogenesis**: endurance training → Ca²⁺ transients + AMPK → PGC-1α → TFAM → ↑mitochondrial DNA + protein synthesis; ↑oxidative capacity, VO₂max
- **GLUT4 upregulation**: both resistance and endurance training → ↑total GLUT4 protein (greater insulin-stimulated glucose uptake at rest)
- **Capillary density**: VEGF secretion → angiogenesis → ↓O₂ diffusion distance to mitochondria
- **Bone density**: mechanical loading → osteocyte mechanosensing → ↓sclerostin → ↑Wnt → ↑bone formation; weight-bearing exercise is the most effective non-pharmacologic intervention for osteoporosis prevention

## Connections

- **Contains:** [bone-marrow](../../05-tissue/bone-marrow/README.md) — red marrow within the skeleton is the primary haematopoietic site; osteoblasts regulate the HSC niche
- **Modulates:** [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — exercise drives cardiac output; metabolites trigger vasodilation; myokines promote angiogenesis
- **Modulates:** [immune-system](../../07-system/immune-system/README.md) — bone marrow produces all immune cells; exercise myokines (IL-6) induce anti-inflammatory responses
- **Modulates:** [nervous-system](../../07-system/nervous-system/README.md) — motor neurons innervate muscle via NMJ; spinal reflexes and cerebellar coordination control movement
- `modulated-by` → **[Myostatin](../../03-molecular/myostatin/README.md)** — myostatin is the primary negative regulator of skeletal muscle mass; aging → elevated myostatin → sarcopenia; cachexia → tumor-induced myostatin → muscle wasting; anti-myostatin biologics (bimagrumab, apitegromab) restore lean mass in sarcopenia and SMA.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The musculoskeletal and integumentary systems form the body's structural exterior: skin, fascia, tendon, muscle and bone are a continuum of collagen-based connective tissue sharing vitamin D dependence, so heritable collagen disorders (Ehlers-Danlos, Marfan) affect both.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — A small-round-cell cancer arises in its bones: Ewing sarcoma, driven by the EWSR1-FLI1 fusion, grows in the long bones and pelvis of children and young adults, a distinct primary bone malignancy alongside osteosarcoma.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Its muscle precursors can turn malignant: rhabdomyosarcoma arises from cells of the skeletal-muscle lineage, the most common soft-tissue sarcoma of childhood and the muscular counterpart to the system's bone cancers.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — A cytokine couples inflammation to wasting: IL-6 promotes osteoclast-driven bone resorption and muscle catabolism, so chronic elevations drive the bone loss and sarcopenia seen in aging and inflammatory disease — yet exercise releases it transiently as a beneficial myokine.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Osteoblasts build the skeleton of the musculoskeletal system: they deposit and mineralize bone's collagen matrix, balance osteoclast resorption via RANKL/OPG, and help regulate the marrow niche; their decline with age and estrogen loss underlies osteoporosis and fracture.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is foundational to the musculoskeletal system at two scales: hydroxyapatite gives bone its hardness and the skeleton stores 99% of body calcium, while calcium influx drives actin-myosin cross-bridge cycling in muscle contraction; PTH and vitamin D balance this reservoir.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Sex hormones from the reproductive system build the musculoskeletal system: testosterone and estrogen drive the pubertal growth spurt, muscle mass, and peak bone density, while menopausal estrogen loss accelerates osteoporosis—tying gonadal function to skeletal health.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The musculoskeletal system is under tight endocrine control: growth hormone/IGF-1, thyroid hormone, PTH, vitamin D, and sex steroids govern bone and muscle, while bone itself secretes osteocalcin and FGF23—so endocrine disease often presents as fractures or weakness.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Bone is continuously remodeled by the osteoclast-osteoblast balance: osteoclasts resorb old bone while osteoblasts rebuild it, and tipping toward resorption (estrogen loss, RANKL excess) causes osteoporosis—the target of bisphosphonates and denosumab.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Osteoporosis is the commonest disease of the musculoskeletal system's bone: an imbalance favoring osteoclast resorption over osteoblast formation thins the skeleton, so fractures of the hip, spine and wrist are the system's leading cause of disability in older adults.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Osteosarcoma is the principal primary bone cancer of the musculoskeletal system: malignant osteoblasts produce disorganized bone, striking the metaphyses of growing adolescents—turning the system's bone-building machinery into an aggressive, lung-metastasizing tumor.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Rheumatoid arthritis is the archetypal autoimmune disease of the musculoskeletal system's joints: immune attack on the synovium forms an invasive pannus that erodes cartilage and bone, deforming joints—autoimmunity striking the skeleton's moving parts.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen is the musculoskeletal system's structural protein: type I gives bone and tendon tensile strength while type II builds cartilage, so collagen defects cause brittle bones (osteogenesis imperfecta) and fragile joints across the whole framework.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts knit the musculoskeletal system's soft framework: they build and repair the collagen of tendons, ligaments and fascia that transmit muscle force to bone, so their activity governs healing of sprains and the integrity of connective tissue.
- `connects-to` → **[Gout](../gout/README.md)** — Gout is a musculoskeletal disease of crystals: monosodium urate deposits in joints trigger acute inflammatory arthritis and, over years, erode bone and form tophi—linking purine metabolism to destructive joint and bone disease.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Bone is built of calcium phosphate, so phosphorus is as essential as calcium to the skeleton: it forms hydroxyapatite crystals that harden bone, and disturbed phosphate handling—as in rickets and renal osteodystrophy—softens and deforms it.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Ankylosing spondylitis attacks the musculoskeletal system: inflammation at entheses where ligaments meet bone heals by ossification, fusing the spine into a rigid 'bamboo' column—showing how the skeleton's response to inflammation can be new bone, not just erosion.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Fibromyalgia presents as a musculoskeletal disease without musculoskeletal damage: widespread muscle and joint pain and tenderness arise from amplified central pain processing, not inflammation or structural injury—so the muscles and bones ache while tests stay normal.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Parathyroid hormone is the master switch of bone remodeling: PTH pulls calcium from bone when blood levels fall, yet given intermittently it builds bone—so the musculoskeletal skeleton doubles as the body's calcium bank under PTH control.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium is essential to bone and muscle: about half the body's magnesium sits in bone as a mineral reservoir, and it is required for muscle contraction and relaxation—so deficiency causes cramps, weakness and impairs bone quality.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Osteocytes tune bone strength through sclerostin: this Wnt-pathway inhibitor brakes bone formation, and mechanical loading lowers it to build bone—so blocking sclerostin (romosozumab) is a potent way to rebuild the osteoporotic skeleton.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Every muscle move starts with acetylcholine: motor neurons release it at the neuromuscular junction to depolarize muscle fibers, so this transmitter is the on-switch that turns nerve commands into the musculoskeletal system's movement.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — The musculoskeletal system runs on ATP: muscle contraction and—crucially—relaxation both burn ATP to cycle myosin and pump calcium, which is why energy failure causes cramps and why rigor mortis sets in when ATP runs out after death.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Muscle and nerve excitability ride on potassium: the ion sets the resting membrane potential that lets muscle fibers fire, so potassium swings cause the weakness or paralysis of periodic paralysis and dangerous arrhythmias.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bone depends on the kidney: it activates vitamin D and balances calcium and phosphate, so kidney failure starves bone of minerals and unleashes parathyroid hormone, crumbling the skeleton in renal osteodystrophy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — The skeleton is built with help from photons: ultraviolet light striking the skin makes vitamin D, the hormone that lets the gut absorb the calcium needed to mineralize bone, linking sunlight to skeletal strength.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen guards the skeleton: it restrains the osteoclasts that resorb bone, so the sharp loss of estrogen at menopause speeds bone breakdown and is the leading driver of osteoporosis in women.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Muscle obeys peripheral nerves: motor fibers carry the command to contract while sensory fibers report position, so nerve injury denervates muscle and wastes it, severing the skeleton from its control.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver fuels muscle and bone growth: under growth-hormone control it makes IGF-1, the systemic signal that drives the building of skeletal muscle and the lengthening of bone.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Muscle stores its own oxygen on iron: myoglobin, an iron-containing protein, holds oxygen inside muscle fibers for the bursts of work that movement demands, tinting muscle red.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals how the body moves and stands: muscle's interdigitating actin and myosin filaments sliding past their Z-discs, and bone's collagen fibrils studded with hydroxyapatite crystals around osteocytes in their lacunae.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium fires the command to move: a nerve impulse floods sodium into the muscle membrane, and the spreading depolarization sweeps down the T-tubules to release the calcium that triggers each contraction.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Troponin is the switch that lets muscle pull: when calcium binds it, the complex shifts tropomyosin off the actin filament, baring the sites where myosin grabs on — the molecular trigger that turns a calcium signal into force.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Growth hormone builds the system in childhood and maintains it after: it lengthens bone at the growth plates, spurs muscle protein synthesis through IGF-1, and its lifelong decline contributes to the muscle and bone loss of aging.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Testosterone is the body's chief anabolic signal for muscle and bone: it enlarges muscle fibers and raises bone density, so its fall with age or hypogonadism drives the sarcopenia and osteoporosis of the aging skeleton.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol is the catabolic counterweight: chronic excess — from disease or steroid drugs — breaks down muscle protein into a proximal myopathy and strips bone into osteoporosis, the opposite of the anabolic hormones' effects.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies can turn on muscle and joint: anti-acetylcholine-receptor antibodies weaken the neuromuscular junction in myasthenia gravis, and myositis-specific autoantibodies attack muscle directly, the immune system mistaking the motor system for the enemy.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Muscle is the body's main glucose sink: insulin drives sugar uptake into muscle and stimulates its protein synthesis, so insulin resistance both raises blood glucose and accelerates the muscle loss of aging and metabolic disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Working muscle is hungry for oxygen the red cells carry: exercise raises oxygen demand and stimulates erythropoietin, while the marrow that makes erythrocytes sits inside the very bones the system is built from.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Bone is rebuilt by a molecular tug-of-war: osteoblasts release RANKL to wake the osteoclasts that resorb bone, and decoy osteoprotegerin restrains them, so this RANKL/OPG balance sets whether the skeleton thickens or thins.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Muscle is only as strong as its nerve signal: in myasthenia gravis antibodies block the acetylcholine receptors at the neuromuscular junction, so intact muscle fatigues and fails despite its machinery, the system crippled at its electrical switch.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The skeleton is mineralized from the gut: the small intestine absorbs dietary calcium and phosphate under vitamin D's control, so malabsorption starves bone of its raw material and drives osteomalacia and fracture.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Bone is built on a Wnt switch: Wnt/β-catenin signaling drives osteoblasts to lay down bone, which is why the natural Wnt-brake sclerostin restrains it and why blocking sclerostin builds bone in osteoporosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat infiltrates the aging frame: marrow fills with adipocytes as bone is lost, and fat marbles aging muscle as myosteatosis, so the same shift toward fat weakens both bone and muscle in sarcopenic obesity.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys derange the skeleton: chronic kidney disease disrupts the phosphate, vitamin D and PTH balance, producing renal osteodystrophy — the brittle, painful bone disease of CKD-mineral and bone disorder.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — It is the classic invader of bone and joint: Staphylococcus aureus is the leading cause of osteomyelitis and septic arthritis, seeding bone and synovium through the blood or open wounds to destroy musculoskeletal tissue.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Immune attack inflames its joints and entheses: psoriatic arthritis is an inflammatory disease of the musculoskeletal system, damaging joints and the tendon-bone insertions through IL-17/IL-23-driven inflammation.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Autoimmunity attacks the muscle itself: dermatomyositis is an inflammatory myopathy of the musculoskeletal system, with immune-mediated injury to skeletal muscle producing the proximal weakness that defines it.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Muscle is the body's main glucose sink: skeletal muscle takes up most insulin-stimulated glucose, so its mass and insulin sensitivity drive metabolic health, while diabetes in turn causes sarcopenia and stiff-joint syndromes.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess load wears the joints: obesity mechanically overloads weight-bearing joints toward osteoarthritis, and adipose-muscle crosstalk worsens the sarcopenia and inflammation of the musculoskeletal system.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic pain and disability weigh on mood: persistent musculoskeletal pain and the loss of mobility and independence it brings are strongly tied to depression, each amplifying the other.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Bone and muscle depend on what the gut absorbs: calcium and vitamin D uptake builds bone, and protein absorption sustains muscle, so malabsorption causes osteomalacia and sarcopenia.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Muscles and the rib cage power breathing: the diaphragm and intercostals drive ventilation, so neuromuscular weakness and chest-wall deformities like scoliosis cause restrictive respiratory failure.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Bones house the blood-and-immune factory: the marrow within the skeleton is where haematopoiesis and B-cell development occur, making the musculoskeletal system a primary site of the lymphatic and immune system.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney governs bone mineral: by controlling calcium, phosphate and active vitamin D, the kidneys keep the skeleton mineralised, so renal failure causes renal osteodystrophy with weakened, painful bones.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis can erode the skeleton: spinal TB (Pott's disease) destroys vertebrae and can cause gibbus deformity and cord compression, while tuberculous arthritis attacks large joints.
- `connects-to` → **[Magnesium (Dietary)](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Magnesium underpins bone: most body magnesium is stored in bone, and it is required to activate vitamin D and regulate parathyroid hormone, so deficiency contributes to weak bones and muscle cramps.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs are its mainstay painkiller: drugs like ibuprofen relieve the pain and inflammation of arthritis and injury, though gastric and renal side effects limit long-term use.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Strep attacks muscle and joints: Streptococcus pyogenes causes necrotising fasciitis and pyomyositis, and triggers post-streptococcal reactive arthritis and rheumatic fever.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 fats calm inflamed joints: their anti-inflammatory effects are studied for joint pain and stiffness in rheumatoid and osteoarthritis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids both treat and harm it: intra-articular and systemic corticosteroids relieve inflammatory joint and muscle disease, but long-term use causes osteoporosis, avascular necrosis and a proximal myopathy.
- `connects-to` → **[Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md)** — A virus that inflames muscle: Coxsackievirus B causes Bornholm disease (epidemic pleurodynia) with severe muscle pain, and viral myositis more broadly.
- `connects-to` → **[Salmonella typhi](../../../02-pathogen/02-bacteria/salmonella-typhi/README.md)** — A classic cause of bone infection: Salmonella is a characteristic cause of osteomyelitis in sickle cell disease, alongside the more common staphylococcal bone and joint infections.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — The hard substance of the skeleton: dense cortical bone gives the musculoskeletal system its strength and lever arms, continuously remodelled by osteoblasts and osteoclasts under load (Wolff's law), and failing as fractures when it thins.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Where nerve commands muscle: the neuromuscular junction translates motor-nerve impulses into contraction via acetylcholine, the synapse whose failure — in myasthenia gravis or with paralytics — silences the musculoskeletal system.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — A common cause of muscle complaints: statins are the most frequent drug cause of myalgia and, rarely, rhabdomyolysis, making muscle symptoms a routine consideration whenever the musculoskeletal system is assessed in statin users.
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — A heritable connective-tissue disorder of the frame: Marfan syndrome's fibrillin-1 defect lengthens the limbs (arachnodactyly, tall stature) and brings scoliosis, pectus deformity and joint laxity—the skeleton built on faulty connective tissue.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — A cancer that dissolves bone: myeloma plasma cells activate osteoclasts via RANKL while suppressing osteoblasts, carving the lytic lesions, pathological fractures and hypercalcaemia that make it a disease of the skeleton.
- `connects-to` → **[ALS](../als/README.md)** — When the nerve dies, the muscle wastes: amyotrophic lateral sclerosis kills the motor neurons driving skeletal muscle, so progressive denervation atrophy and weakness destroy the musculoskeletal system's power despite initially healthy muscle fibres.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Bone as a target of sickling: vaso-occlusion causes painful bone infarcts, avascular necrosis of the femoral head and childhood dactylitis, and raises the risk of Salmonella osteomyelitis in the skeleton.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Bleeding into the joints: recurrent haemarthrosis in haemophilia A destroys cartilage and synovium, producing a crippling chronic arthropathy that is a major musculoskeletal burden of the disease.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — A soft-tissue cancer near the joints: synovial sarcoma arises in the limbs around joints and tendons (despite its name, not from synovium), a malignant counterpart to the system's many benign soft-tissue tumours.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Bone as a metastatic home: the skeleton is the dominant site of prostate cancer spread, forming characteristic osteoblastic lesions and skeletal-related events—pain, fractures and cord compression—that define the disease's course.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Lytic bone metastases: breast cancer seeds the skeleton with osteolytic and mixed lesions that fracture and release calcium, making bone a sanctuary site and a major source of morbidity treated with bone-targeted agents.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Muscle and the virus: COVID-19 causes myalgia, occasional rhabdomyolysis and post-viral myositis, and the prolonged muscle weakness and pain of long COVID are a notable musculoskeletal legacy.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — Bone's phosphate hormone: FGF23 secreted by bone osteocytes is the master regulator of phosphate balance, linking the skeleton to the kidney and disturbed in chronic kidney-mineral-bone disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fat-bone-muscle crosstalk: leptin from adipose tissue regulates bone mass and muscle through central and peripheral pathways, linking adiposity to musculoskeletal health.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Matrix coupling factor: TGF-β stored in bone matrix couples resorption to formation and orchestrates the repair of muscle, tendon and bone after injury.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Bone matrix glue: osteopontin in the mineralised matrix anchors osteoclasts to bone for resorption and regulates mineralisation, a key non-collagenous protein of skeletal remodelling.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — Turnover and muscle tone: thyroid hormones set the pace of bone remodelling and skeletal-muscle metabolism, so thyroid excess accelerates bone loss and causes myopathy across the musculoskeletal system.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Skeletal angiogenesis: VEGF couples blood-vessel growth to endochondral ossification and fracture repair, and supplies the capillary network that sustains skeletal muscle.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Calcitonin from thyroid C cells directly inhibits osteoclast bone resorption and lowers serum calcium, the physiological counterweight to PTH in the calcium and bone-remodeling balance that maintains the skeleton.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins (PGE2) regulate bone formation and resorption and are essential for fracture healing, which is why NSAIDs that block their synthesis can impair bone union and are used cautiously after fractures.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Osteocytes release nitric oxide in response to mechanical loading, the signal that translates weight-bearing exercise into the bone formation maintaining skeletal strength—and whose loss with disuse drives bone loss.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the mineral stored as hydroxyapatite that gives bone its rigidity and the ion that triggers skeletal-muscle contraction through troponin, linking the skeleton's structural and the muscle's contractile roles.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Articular cartilage has no blood supply, so its chondrocytes survive on HIF-1α-driven anaerobic glycolysis, the hypoxic adaptation that maintains the joint surface and whose failure contributes to osteoarthritis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipose-derived adiponectin signals to bone and muscle, part of the endocrine crosstalk by which fat mass, bone remodeling and muscle metabolism are coordinated, integrating the musculoskeletal system with whole-body energy balance.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling controls mesenchymal-progenitor commitment in bone and the satellite-cell self-renewal that regenerates skeletal muscle, a core developmental pathway of the musculoskeletal system.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF/FGFR signaling regulates the chondrocyte proliferation of the growth plate that lengthens long bones, the pathway whose constitutive activation causes achondroplasia.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF recruits the mesenchymal and perivascular progenitor cells that build and repair bone, muscle and connective tissue after injury throughout the musculoskeletal system.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The IGF-1-AKT-mTOR pathway (IGF-1 mapped) drives the protein synthesis underlying skeletal-muscle hypertrophy, the anabolic switch that builds muscle in response to load.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — The calcium-activated phosphatase calcineurin drives NFAT-dependent slow-twitch fiber-type programming and muscle adaptation to endurance activity.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Glucocorticoids acting through the glucocorticoid receptor (cortisol mapped) cause both skeletal-muscle atrophy and osteoporosis, the dual musculoskeletal toxicity of steroid excess.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — IGF-1/insulin signaling through PI3K-AKT-mTOR (IGF-1 and mTOR mapped) governs skeletal-muscle hypertrophy and bone anabolic responses.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is a potent osteoclastogenic and catabolic cytokine driving bone resorption and muscle wasting in inflammatory and age-related musculoskeletal disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A links immune activation to bone and joint pathology, driving osteoclastogenesis and the enthesitis of spondyloarthritis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β/BMP-SMAD signaling (TGF-β already mapped) governs bone and cartilage formation and the matrix homeostasis of the musculoskeletal system.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling drives the muscle wasting and bone remodeling shared across catabolic and inflammatory disorders of the musculoskeletal system.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates chondrocyte and osteoclast biology and the inflammatory matrix remodeling of the musculoskeletal system.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the osteoblast-osteoclast balance, the atrogene muscle-atrophy program, and oxidative-stress defense across the musculoskeletal system.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of growth factors (FGFR and IGF-1 already mapped) drives osteoblast and myocyte proliferation and differentiation in the musculoskeletal system.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling modulates osteoclastogenesis and the inflammatory regulation of bone and muscle in the musculoskeletal system.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, within the Wnt/β-catenin signaling that governs osteoblast differentiation (Wnt already mapped), regulates the bone formation and remodeling of the musculoskeletal system.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins participate in the inflammatory signaling of bone and joint tissue in the musculoskeletal system.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Connexin-43 gap junctions mediate the osteocyte-network and muscle intercellular communication that coordinates mechanotransduction in the musculoskeletal system.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the osteoblast, chondrocyte, and myocyte growth and survival of the musculoskeletal system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK integrates the energy status of muscle and bone, coupling metabolism to musculoskeletal adaptation.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB signaling drives the osteoclastogenesis (RANKL already mapped) and inflammatory remodeling of the musculoskeletal system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy maintains the myofiber, chondrocyte, and osteocyte homeostasis of the musculoskeletal system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the osteoclast function and mechanotransduction of the musculoskeletal system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the osteogenic, chondrogenic, and myogenic differentiation of the musculoskeletal system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the immune-cell trafficking within the bone and muscle tissues of the musculoskeletal system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the bone-marrow-niche, osteogenic, and muscle-stem-cell interactions of the musculoskeletal system.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the bone and joint remodeling of the musculoskeletal system.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Bone and muscle mineral: roughly 60% of body magnesium is stored in bone, and magnesium is essential for neuromuscular excitability and as an enzyme cofactor, so deficiency produces cramps, weakness and impaired bone quality.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Muscle excitability: potassium gradients set the resting membrane potential of skeletal muscle, and hypo- or hyperkalaemia cause the weakness and paralysis that link electrolyte balance directly to musculoskeletal function.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gut-bone axis: gut-derived serotonin acts on osteoblasts to restrain bone formation, a systemic regulator of skeletal mass that connects the musculoskeletal system to enteric endocrine signalling beyond the local bone factors.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Matrix and cartilage: zinc is a cofactor for the collagen-processing and matrix metalloproteinase enzymes of bone and cartilage (collagen already mapped), and its deficiency impairs growth and skeletal development.
- `connects-to` → **[Rheumatoid arthritis](../rheumatoid-arthritis/README.md)** — Inflammatory arthritis: rheumatoid arthritis attacks the synovial joints of the musculoskeletal system, with immune-driven synovitis eroding cartilage and bone (RANKL already mapped) to cause the joint destruction and deformity of the disease.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Musculoskeletal pain: pain from bones, joints and muscles is among the leading reasons for analgesic use, and opioids acting on the mu-opioid receptor are used, with well-known risks, for severe musculoskeletal pain.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Nociceptive innervation: substance P released by the sensory nerves of bone, joint and muscle signals the pain of musculoskeletal injury and inflammation (mu-opioid receptor already mapped), and it also participates in the neural regulation of bone remodelling.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Skeletal sensory nerves: CGRP-containing sensory fibres richly innervate the periosteum and bone, contributing to musculoskeletal pain (substance P already mapped) and to the regulation of bone formation and blood flow.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Urate and oxidative joint injury: xanthine oxidase produces the uric acid whose crystals cause gout in the joints, and the reactive oxygen species it generates add to the oxidative damage of inflammatory and degenerative musculoskeletal disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Motor innervation: the motor neurons drive skeletal muscle at the neuromuscular junction (acetylcholine already mapped), and the sensory neurons carry the proprioception and pain (substance P and CGRP already mapped) of the musculoskeletal system.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Osteoclasts and muscle repair: the macrophage lineage gives rise to the bone-resorbing osteoclasts (RANKL already mapped) and to the muscle-repair macrophages, central to remodelling and regeneration in the musculoskeletal system.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 tissue repair: IL-4 drives the M2 macrophages (already mapped) that support muscle regeneration and resolve inflammation, part of the type-2 immunity that shapes repair in the musculoskeletal system.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Connective-tissue cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) and elastin of bone, tendon and ligament, and its deficiency (as in Menkes) causes bone fragility and connective-tissue weakness.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Muscle antioxidant defence: selenium is essential for the selenoprotein antioxidant defence of muscle, and severe deficiency causes a myopathy (as in Keshan disease) of the musculoskeletal system.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine-bone crosstalk: resistin, with leptin and adiponectin (already mapped) from the marrow adipocytes (already mapped), is part of the adipokine influence on the bone and muscle metabolism of the musculoskeletal system.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Marrow adipocytes: the marrow adipocytes (the source of leptin, adiponectin and resistin already mapped) of the musculoskeletal system's bone marrow influence the bone and haematopoiesis, expanding with age and osteoporosis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Bone mineralisation: vitamin D drives the intestinal calcium (already mapped) absorption and the bone mineralisation (PTH already mapped); its deficiency causes the rickets and osteomalacia of the musculoskeletal system.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Connective-tissue fibroblasts: the fibroblasts of the tendons, ligaments and fascia synthesise the collagen (already mapped) matrix of the musculoskeletal system's soft connective tissues.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Inflammatory myopathy: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune-mediated inflammatory myopathies and arthritides of the musculoskeletal system.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 muscle immunity: IL-13, with IL-4 (already mapped), is the type-2 immune arm implicated in the muscle repair and the eosinophilic/fibrosing myopathies of the musculoskeletal system.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the eosinophilic myositis and fasciitis of the musculoskeletal system.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory myopathies and arthritides of the musculoskeletal system.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the spondyloarthritis and the enthesitis of the musculoskeletal system.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon myopathy: the type-I interferon signature drives the inflammatory myopathies (the dermatomyositis) of the musculoskeletal system.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory and allergic disorders of the musculoskeletal system.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Synovial/bone mast cells: the mast cells of the synovium, bone and muscle contribute to the inflammation and the tissue remodelling of the musculoskeletal system.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the autoimmune arthritis and myositis of the musculoskeletal system.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Joint/bone complement: the complement C3 activation contributes to the inflammatory dimension of the synovium, cartilage and bone in the arthritides of the musculoskeletal system.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the neutrophil recruitment and promotes the osteoclast (already mapped) differentiation in the inflamed joints of the musculoskeletal system.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Synovial antigen presentation: the dendritic cells present antigen to the T cells (already mapped) in the autoimmune arthritis of the musculoskeletal system.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Synovial alarmin: TSLP, released from synovial fibroblasts under mechanical and inflammatory stress, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the immune-driven joint and bone inflammation of the musculoskeletal system.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Joint kinin pain: bradykinin, generated by the kallikrein-kinin system activated in the inflamed synovium, amplifies the nociception via B1/B2 receptors on the peripheral nerves (already mapped) and the vascular permeability of the arthritic joints of the musculoskeletal system.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Bone-EPO axis: erythropoietin, acting on EPOR-expressing osteoblasts (already mapped) and osteoclasts (already mapped), modulates bone remodelling (RANKL already mapped) and supports the haematopoietic niche of the bone marrow (already mapped) of the musculoskeletal system.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Joint complement/kinin regulator: the C1-esterase inhibitor limits the classical complement and contact-kinin (bradykinin already mapped) pathways activated in the inflamed synovium, moderating the cartilage-destructive complement cascade of the musculoskeletal system.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell joint effector: histamine, released by mast cells (already mapped) in the synovium and periosteum, amplifies the vascular permeability, nociception and the inflammatory cytokine cascade (IL-1/TNF already mapped) of the musculoskeletal system.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periosteal and tendon ECM: periostin, expressed in the periosteum, tendons and entheses, maintains the structural integrity of these fibrous connective tissues and promotes bone remodelling (RANKL and osteoblast already mapped) of the musculoskeletal system.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — MS melatonin: melatonin, via MT1/MT2 receptors on osteoblasts (already mapped), attenuates RANKL (already mapped) osteoclastogenesis and promotes bone anabolism; melatonin also modulates the bone-marrow (already mapped) haematopoietic niche and reduces musculoskeletal pain.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — MS prolactin: prolactin, via prolactin receptors on osteoblasts (already mapped), promotes bone anabolism and muscle protein synthesis; prolactin modulates the reproductive (already mapped) and immune (already mapped) crosstalk of the musculoskeletal system.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MS vasopressin: vasopressin, acting on V1/V2 receptors on smooth-muscle cells, modulates the vascular tone in the musculoskeletal system; vasopressin also regulates sodium (already mapped) and water balance that affects synovial fluid composition and joint lubrication.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — MS oxytocin: oxytocin receptors on osteoblasts (already mapped) suppress NF-κB (already mapped) and promote bone anabolism; oxytocin also modulates muscle regeneration and collagen (already mapped) synthesis via IL-6 (already mapped) and TNF-α (already mapped) signalling.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MS iodine: thyroid-hormone signalling drives bone-turnover balance (osteoblast/already mapped vs osteoclast/already mapped) and muscle protein synthesis; iodine deficiency impairs collagen (already mapped) synthesis and amplifies NF-κB (already mapped) inflammatory remodelling.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MS sulfur: sulfur-containing amino acids are essential for collagen (already mapped) cross-linking and cartilage proteoglycan synthesis; sulfur deficiency impairs musculoskeletal repair and amplifies NF-κB (already mapped) and TNF-α (already mapped) driven catabolic signalling.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MSK nitrogen: nitric oxide (NO, nitrogen-derived) in osteoblasts (already mapped) and macrophages (already mapped) regulates bone remodelling and skeletal vasodilation; NO imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) osteoclast-driven resorption.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MSK chloride: chloride channels on osteoclasts (already mapped) and fibroblasts (already mapped) maintain pH homeostasis for bone resorption; chloride dysregulation amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) musculoskeletal remodelling.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MSK oxygen: oxygen drives aerobic energy in osteoblasts (already mapped) and macrophages (already mapped); oxygen deprivation activates HIF-1α, amplifying NF-κB (already mapped) and IL-6 (already mapped) osteoclast-driven bone resorption cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — MSK carbon: carbon, as backbone of collagen (already mapped) and proteoglycans, forms the organic matrix of bone and cartilage; carbon metabolism in osteoblasts (already mapped) shapes NF-κB (already mapped) and IL-6 (already mapped) repair cascade.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MSK hydrogen: hydrogen, as water in cartilage matrix and H₂ in synovial joints, maintains viscoelastic properties; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) musculoskeletal inflammatory cascade.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MSK PD-1: PD-1 checkpoint on T-regulatory (already mapped) and cytotoxic T-cells (already mapped) in the musculoskeletal microenvironment modulates autoimmune joint inflammation; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) erosive cascade.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — MSK GLP-1: GLP-1 receptor agonism on osteoblasts (already mapped) and macrophages (already mapped) promotes bone mineral density; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) bone-resorption cascade of musculoskeletal disease.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — MSK angiotensin-II: angiotensin-II via AT1R on osteoblasts (already mapped) and macrophages (already mapped) modulates bone remodelling; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — MSK IL-2: IL-2 from activated T-cells (already mapped) in synovium (already mapped) drives cytotoxic and T-regulatory cell expansion; IL-2 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) autoimmune cascade of musculoskeletal disease.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — MSK fibronectin: fibronectin in cartilage (already mapped) and synovium (already mapped) scaffolds chondrocyte adhesion and repair; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) matrix-degradation cascade of musculoskeletal disease.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — MSK activin-A: activin-A from myoblasts (already mapped) and synoviocytes (already mapped) regulates bone formation and muscle repair; activin-A excess amplifies NF-κB (already mapped) and IL-6 (already mapped) fibrotic cascade of musculoskeletal disease.

## Pathology

### Osteoporosis

Imbalanced remodelling with net resorption exceeding formation leads to reduced bone mineral density (BMD), microarchitectural deterioration, and fragility fractures [^guyton-hall]. The most common cause is oestrogen deficiency at menopause (postmenopausal osteoporosis) — oestrogen normally suppresses RANKL-driven osteoclastogenesis. Secondary causes include glucocorticoid excess (suppresses OPG, impairs collagen synthesis, decreases intestinal Ca²⁺ absorption → steroid-induced osteoporosis), hyperparathyroidism, hypogonadism, and malabsorption (vitamin D/Ca²⁺ deficiency).

**Fracture risk (FRAX score)**: BMD T-score ≤ −2.5 defines osteoporosis; T-score −1.0 to −2.5 is osteopenia.

**Treatment**: Antiresorptives (bisphosphonates [alendronate: inhibit osteoclast FPP synthase → ↑apoptosis], denosumab [anti-RANKL mAb]), anabolic agents (teriparatide [intermittent PTH 1-34], abaloparatide, romosozumab [anti-sclerostin mAb → ↑Wnt → ↑formation + ↓resorption]).

### Osteoarthritis (OA)

Progressive breakdown of articular cartilage (↑MMP-1/3/13, ADAMTS-4/5, ↓aggrecan, ↓type II collagen synthesis by chondrocytes), subchondral bone remodelling (sclerosis + osteophyte formation), and synovial inflammation (↑IL-1β, TNF-α, IL-6 from synoviocytes). Risk factors: aging, obesity (mechanical loading + adipokine-mediated inflammation), female sex, previous joint injury. Management: exercise (most effective intervention), weight loss, NSAIDs, intra-articular corticosteroids, and ultimately total joint arthroplasty.

### Rheumatoid Arthritis (RA)

Autoimmune synovitis driven by anti-citrullinated protein antibodies (ACPA) and rheumatoid factor against synovial joints. Pathology: Th17 and macrophage-driven pannus formation → cartilage and bone erosion via RANKL-mediated osteoclast activation and MMPs. Systemic effects (cardiovascular risk, anaemia of chronic disease). Treatment: DMARDs (methotrexate, hydroxychloroquine), biologics (anti-TNF [etanercept, adalimumab], anti-IL-6R [tocilizumab], abatacept [CTLA4-Ig], rituximab [anti-CD20]).

### Sarcopenia

Age-related loss of skeletal muscle mass and function (muscle loss ~1%/year after age 30; accelerates after 60). Pathophysiology: ↓satellite cell pool, ↓anabolic sensitivity (anabolic resistance to protein/leucine and insulin), ↑myostatin (TGF-β family → Smad2/3 → ↓protein synthesis), chronic low-grade inflammation (inflammaging — IL-6, TNF-α → ↑ubiquitin-proteasome degradation), ↓motor unit innervation. Clinical: falls, disability, ↑mortality in frail elderly. Treatment: resistance exercise + adequate protein (1.2–1.6 g/kg/day); leucine supplementation; vitamin D; investigational myostatin inhibitors.

### Duchenne Muscular Dystrophy (DMD)

X-linked frameshift mutation in dystrophin gene (Xp21.2) — largest human gene. Dystrophin connects the actin cytoskeleton to the extracellular matrix (laminin) via the dystrophin-associated protein complex (DAPC). Absence → mechanical fragility → repeated contraction-induced membrane damage → Ca²⁺ overload → necrosis → replacement with fibrotic/fatty tissue. Progressive: loss of ambulation by ~12 years, respiratory failure by 20s without ventilatory support. Exon-skipping therapies (eteplirsen, golodirsen for specific exon mutations), micro-dystrophin gene therapy, glucocorticoids (standard of care — slow progression).

### Rhabdomyolysis

Massive skeletal muscle necrosis releasing myoglobin into blood → myoglobin precipitates in renal tubules (at acid pH) + direct tubular toxicity → acute kidney injury. Causes: extreme exertion, crush injury, seizures, statins (in CYP3A4 interactions), viral myositis. Hallmark: markedly elevated CK (>5,000 IU/L), myoglobinuria (urine dipstick positive for blood, microscopy negative for RBCs). Treatment: aggressive IV fluid resuscitation → alkalinise urine → protect kidneys.

### Fracture Healing

Four overlapping phases [^guyton-hall]:
1. **Haematoma** (hours–days): fracture disrupts periosteal vasculature; haematoma forms; hypoxic environment → macrophage/monocyte infiltration → inflammatory cytokines (IL-1, IL-6, TNF-α) → angiogenesis
2. **Soft callus** (days 1–3 weeks): periosteal osteoprogenitors + mesenchymal stem cells → fibrocartilaginous callus (type II collagen + proteoglycans); stabilizes fracture
3. **Hard callus** (weeks 3–12): chondrocytes hypertrophy → vascular invasion (VEGF) → endochondral ossification → woven bone callus
4. **Remodelling** (months–years): woven bone remodelled to lamellar cortical/trabecular bone by coupled BMU activity; restoration of medullary canal; final structure reflects mechanical loading environment (Wolff's law)

## See Also

- [bone-marrow](../../05-tissue/bone-marrow/README.md) — haematopoietic niche within the musculoskeletal system
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — exercise-muscle-heart crosstalk
- [immune-system](../../07-system/immune-system/README.md) — haematopoiesis, myokine immunomodulation
- [nervous-system](../../07-system/nervous-system/README.md) — motor control, NMJ, reflexes
- [collagen](../../03-molecular/collagen/README.md) — structural backbone of bone, tendon, cartilage, ligament
- [il-6](../../03-molecular/il-6/README.md) — key exercise myokine from skeletal muscle
- [insulin](../../03-molecular/insulin/README.md) — key anabolic hormone for muscle glucose uptake via GLUT4

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
