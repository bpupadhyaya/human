---
schema: human-scale-entry/v1
id: ankylosing-spondylitis
name: Ankylosing Spondylitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Ankylosing spondylitis (AS; radiographic axSpA) is a chronic inflammatory spondyloarthropathy with sacroiliitis and spinal ankylosis; HLA-B27+ in ~90%; IL-17A/IL-23 and TNF pathways drive enthesitis; anti-TNF and anti-IL-17A (secukinumab, ixekizumab) are first-line therapy."
aliases: ["AS", "ankylosing spondylitis", "axial spondyloarthritis", "axSpA", "radiographic axSpA", "r-axSpA", "non-radiographic axSpA", "nr-axSpA", "Bechterew disease", "Marie-Strümpell disease", "spondyloarthropathy", "SpA", "BASDAI", "ASDAS", "bamboo spine"]
sources:
  - id: sieper-2015-ankylosing-spondylitis-review
    type: peer-reviewed
    cite: "Sieper J, Poddubnyy D. Ankylosing spondylitis. Lancet. 2017;390(10089):73-84."
    doi: "10.1016/S0140-6736(16)31591-4"
    pmid: "28110981"
    url: "https://doi.org/10.1016/S0140-6736(16)31591-4"
  - id: baeten-2015-secukinumab-as
    type: peer-reviewed
    cite: "Baeten D, Sieper J, Braun J, et al. Secukinumab, an Interleukin-17A Inhibitor, in Ankylosing Spondylitis. N Engl J Med. 2015;373(26):2534-2548."
    doi: "10.1056/NEJMoa1505066"
    pmid: "26699169"
    url: "https://doi.org/10.1056/NEJMoa1505066"
  - id: van-der-heijde-2018-adalimumab-as
    type: peer-reviewed
    cite: "van der Heijde D, Ramiro S, Landewé R, et al. 2016 update of the ASAS-EULAR management recommendations for axial spondyloarthritis. Ann Rheum Dis. 2017;76(6):978-991."
    doi: "10.1136/annrheumdis-2016-210770"
    pmid: "28087505"
    url: "https://doi.org/10.1136/annrheumdis-2016-210770"
cross_links:
  - target: 01-human/03-molecular/hla-b27
    relation: connects-to
    note: "HLA-B27 is the strongest genetic risk factor for AS (carried in ~90% of AS patients vs. 8% of Europeans); B*27:05 confers highest AS risk; HLA-B27 misfolding in ER → UPR → IL-23 → Th17/ILC3 → IL-17A → enthesitis; HLA-B27 also predicts uveitis and familial clustering."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is the central effector cytokine in AS enthesitis: ILC3 and Th17 cells at entheses produce IL-17A → RANKL + MMP → bone erosion + osteoblast activation → new bone (syndesmophytes); secukinumab (MEASURE-1) achieved ASAS20 ~61% vs. 29% placebo; ixekizumab also approved."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Entheseal IL-17A + TNF-α → RANKL on stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral corners; new bone formation (syndesmophytes) follows via WNT pathway; denosumab (anti-RANKL) reduces erosion but does not halt new bone formation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) achieve ASAS40 ~50-60% in active AS; TNF inhibition reduces MRI inflammation but does not halt radiographic progression (new bone)."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Axial PsA and AS share HLA-B27, sacroiliitis imaging, and IL-17A/TNF-α pathobiology; distinguished by concurrent psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF are effective in both; IL-23 inhibitors diverge in efficacy."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Acute anterior uveitis is the most common extra-articular manifestation of ankylosing spondylitis, affecting 20-30% over a lifetime and tracking with HLA-B27; it presents as a painful, red, photophobic eye that recurs and alternates between eyes."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Ankylosing spondylitis and IBD are two faces of the gut-joint axis: ~60% of AS patients have subclinical gut inflammation and 5-10% develop overt Crohn's or colitis, reflecting shared IL-23R genetics; anti-TNF treats both, but IL-17 blockade can flare IBD."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "HLA-B27 misfolding in the ER triggers an unfolded-protein response that ramps up IL-23, driving entheseal ILC3 and Th17 cells to pour out IL-17A; paradoxically, IL-23 blockade fails in AS despite this upstream role — likely because ILC3s make IL-17A independently of IL-23."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "AS and psoriasis lie on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis; IL-17 inhibitors (secukinumab, ixekizumab) treat both and psoriasis is a common AS comorbidity—yet IL-23 blockade helps psoriasis but failed in axial AS, hinting at divergent biology."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "AS is the prototypical axial spondyloarthritis: enthesitis and sacroiliitis at the spine and SI joints → inflammatory back pain → syndesmophytes and bony ankylosis ('bamboo spine'); IL-17-driven new-bone formation and erosion reshape the axial skeleton and reduce spinal mobility."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "AS uniquely couples inflammation to bone formation: at entheses IL-17A/TNF and Wnt (low DKK-1/sclerostin) activate osteoblasts → syndesmophytes and ankylosis, even as RANKL drives co-existing erosion; this osteoproliferation distinguishes AS from erosive rheumatoid arthritis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Ankylosing spondylitis paradoxically combines bone formation and bone loss: while syndesmophytes fuse the spine, systemic inflammation drives vertebral osteoporosis beneath, so a rigid 'bamboo spine' is brittle and prone to fracture from even minor trauma."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Ankylosing spondylitis has cardiac complications beyond the spine: inflammation causes aortitis with aortic-root dilatation and regurgitation, conduction disease and heart block, and accelerated atherosclerosis—a major driver of its excess mortality."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Ankylosing spondylitis is linked to IgA nephropathy, its commonest renal complication: both share HLA-B27-associated, IL-23-driven mucosal immunity with elevated serum IgA, so hematuria or proteinuria in AS prompts evaluation for IgA nephropathy or secondary AA amyloidosis."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Ankylosing spondylitis and rheumatoid arthritis are the major chronic inflammatory arthritides but opposite: AS is a seronegative, HLA-B27-linked, IL-17/23-driven spondyloarthritis of the axial skeleton, while RA is a seropositive peripheral synovitis with erosion."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells, especially the Th17 lineage, drive ankylosing spondylitis: IL-23 expands IL-17-producing T cells at entheses and the sacroiliac joints, fueling inflammation and new bone formation—so IL-17 and IL-23 blockers (secukinumab) target this T-cell axis."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Ankylosing spondylitis and gout are both inflammatory arthritides but different in cause: AS is an autoimmune HLA-B27 spondyloarthritis of the spine, while gout is crystal-driven innate inflammation of peripheral joints—axial autoimmunity versus crystal arthropathy."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Enthesis fibroblasts build the bony fusion of ankylosing spondylitis: at sites where tendon meets bone, inflammation drives fibroblasts and osteoblasts to lay down new bone (syndesmophytes), so the spine gradually ossifies into the rigid bamboo spine."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Ankylosing spondylitis reaches the heart: chronic inflammation can cause aortitis with aortic-root dilation and regurgitation plus conduction block, so cardiac evaluation is part of long-standing AS—an extra-articular manifestation beyond the spine."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Ankylosing spondylitis restricts and scars the lungs: fusion of the rib-spine joints stiffens the chest wall limiting expansion, and apical pulmonary fibrosis develops in advanced disease—so breathing is impaired both mechanically and by lung scarring."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Ankylosing spondylitis is tied to the gut: most patients have subclinical bowel inflammation, and a dysbiotic microbiome in HLA-B27 carriers is thought to drive the IL-23/IL-17 axis—linking gut bacteria to spinal disease along the gut-joint axis."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "AS damages and remakes collagen-rich tissue: chronic enthesitis erodes the collagen anchors where ligaments meet bone, then heals by ossification, so syndesmophytes bridge vertebrae—turning the spine's flexible collagen attachments into rigid bone."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "AS creates a calcium paradox in the skeleton: ligaments ossify and deposit calcium into rigid syndesmophytes while the vertebral bodies inside lose mineral and become osteoporotic—so the stiff bamboo spine is brittle and prone to fracture."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Ankylosing spondylitis fuses the spine via Wnt-driven bone formation: inflammation shifts the Wnt/sclerostin balance to activate osteoblasts, building the syndesmophytes that bridge vertebrae into a 'bamboo spine'—why anti-inflammatories don't fully stop fusion."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "HLA-B27 ties ankylosing spondylitis to cytotoxic T cells: the class I molecule presents peptides to CD8 T cells, and the leading 'arthritogenic peptide' hypothesis holds that this drives the autoimmune attack on the spine and joints."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors are a newer ankylosing spondylitis therapy: oral drugs like upadacitinib block JAK signaling downstream of inflammatory cytokines, controlling axial disease in patients who fail or can't take TNF and IL-17 biologics."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Ankylosing spondylitis fuses the spine by silencing sclerostin: this Wnt-pathway brake on bone formation falls in AS, so unopposed Wnt drives the new bone (syndesmophytes) that bridges vertebrae into a bamboo spine."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D shapes ankylosing spondylitis: deficiency is common and may worsen both the bone loss and the IL-17-driven inflammation, so vitamin D status is watched in a disease that paradoxically erodes and overgrows bone."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Ankylosing spondylitis may ignite from dendritic cells: sensing gut microbes and HLA-B27-presented peptides, they secrete IL-23 that drives the IL-17 response attacking entheses, linking the gut to the inflamed spine."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "A gut-joint axis drives ankylosing spondylitis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that attacks the spine, linking the large intestine to the disease and its overlap with IBD."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Ankylosing spondylitis both erodes and fuses bone: osteoclasts carve early erosions at inflamed entheses even as new bone later bridges the joints, so the same disease that destroys bone ends by welding the spine rigid."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages bridge gut and spine in ankylosing spondylitis: activated in the inflamed bowel and at the entheses, they pour out TNF and other cytokines that drive the inflammation, making them a hub of the IL-23/IL-17-fed disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The earliest AS lesion lives in bone: marrow edema (osteitis) in the sacroiliac joints is the MRI hallmark that lets doctors catch axial disease years before X-rays show fusion."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "AS is defined by what X-ray photons reveal: radiographic sacroiliitis and the fused bamboo spine confirm the disease, while MRI catches the earlier inflammation that plain films miss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The syndesmophytes that weld the AS spine are built of bone mineral: new bone formation lays down calcium-phosphate hydroxyapatite, so phosphate as well as calcium feeds the pathological fusion."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Decades of inflammation can poison the kidney: AS is a classic cause of secondary AA amyloidosis, where serum amyloid protein deposits in the kidney and triggers a slow slide into renal failure, alongside its links to IgA nephropathy."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "AS quietly scars the top of the lungs: a hallmark extra-articular finding is fibrobullous disease of the upper lobes, where progressive apical fibrosis stiffens the chest already restricted by the fused, rigid rib cage."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "AS sits in a family of skin-linked diseases: it overlaps the spondyloarthritis spectrum with psoriasis, so the same HLA-B27-associated, IL-17-driven inflammation that fuses the spine often shows as scaly plaques on the skin."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A fused spine is a brittle one: the rigid bamboo spine of AS fractures from minor trauma, and these unstable breaks can crush the spinal cord, while chronic arachnoid scarring rarely produces a cauda equina syndrome of leg weakness and bladder loss."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Chronic inflammation thins the blood: like other rheumatic diseases, active AS drives the anemia of chronic disease, with inflammatory hepcidin locking iron away from the red cells and leaving patients tired beyond their joint pain."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Treating AS means watching the liver: before starting the TNF-blocking biologics that calm the spine, patients are screened for hepatitis B to avoid reactivating it, and long-term NSAID use adds its own hepatic and GI risks."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "AS is seronegative yet treated with antibodies: rheumatoid factor and anti-CCP are absent, marking it apart from RA, while monoclonal antibodies against TNF and IL-17 are the mainstay that calms the spine when NSAIDs fall short."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The inflammation creeps toward the heart's core: AS causes aortic-root inflammation with regurgitation and conduction disease, fibrosis invading the valve and the AV node so the cardiomyocytes' wiring blocks and the rhythm slows."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Disease and drugs touch reproduction: AS strikes men in their reproductive prime, and family planning weighs the safety of NSAIDs and biologics in pregnancy, while severe spinal fusion can complicate the mechanics of conception and delivery."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "NSAIDs are AS's first-line drug: by blocking COX and the prostaglandins that mediate the inflammatory pain, they relieve symptoms and, taken continuously, may even slow the spinal new-bone formation that fuses the spine."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the enthesis: resident at the tendon-and-ligament insertions where AS begins, they are a major innate source of IL-17, helping ignite the enthesitis that is the disease's defining lesion."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Chronic inflammation hardens the arteries: AS raises cardiovascular risk through accelerated atherosclerosis, so heart attack and stroke become important causes of death and disease control doubles as cardiovascular protection."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 fuels both the inflammation and its toll: this cytokine helps drive the Th17 axis and the systemic acute-phase response of AS, contributing to the chronic-disease anemia and fatigue that accompany the spinal disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The brakes on inflammation slip: a relative shortfall of regulatory T cells lets the IL-23/Th17 response run unchecked at the entheses, tilting the balance toward the IL-17-driven inflammation that ossifies the spine."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Inflammation reaches the heart's structure: AS can inflame the aortic root into regurgitation and scar the conduction system, valve and conduction disease that, on top of the cardiovascular risk, can drift into heart failure."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 carries the IL-23 signal into Th17 cells: it is the transcription factor that drives the IL-17-producing T cells central to AS, which is why STAT3-dependent cytokine pathways are prime drug targets in the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB transmits the TNF signal: at the inflamed entheses, TNF acts largely through NF-κB to sustain the inflammatory and bone-remodeling programs, the pathway that anti-TNF biologics interrupt to calm AS."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Chronic inflammation raises the clot risk: ankylosing spondylitis carries an increased rate of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic tendency shared across the systemic inflammatory diseases."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its TNF biologics can wake latent TB: the anti-TNF agents that transformed AS treatment disable the granuloma containing Mycobacterium tuberculosis, so latent-TB screening and treatment precede therapy to prevent reactivation."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Sustained inflammation dulls the marrow: the chronic IL-6 drive of active ankylosing spondylitis raises hepcidin and blunts erythropoiesis, producing the anemia of chronic disease that tracks with disease activity."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Decades of inflammation can scar the kidney: long-standing AS can deposit secondary AA amyloid in the kidney and, alongside its associated IgA nephropathy, progress to chronic kidney disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Chronic systemic inflammation accelerates the arteries: the sustained inflammatory burden of ankylosing spondylitis speeds atherosclerosis and, with reduced mobility, raises the long-term risk of ischemic stroke."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Its TNF inhibitors can reactivate hepatitis B: the anti-TNF biologics central to treating AS can reawaken a dormant hepatitis B virus, so serologic screening and antiviral prophylaxis precede therapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relentless pain and stiffening wear on mood: the chronic back pain, fatigue, poor sleep and progressive loss of mobility in ankylosing spondylitis contribute to markedly elevated rates of depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "A fused chest cannot breathe freely: ankylosis of the costovertebral joints and thoracic spine stiffens the rib cage into restrictive lung disease, and apical pulmonary fibrosis adds to the burden."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunomodulatory drugs reawaken shingles: the TNF, IL-17 and JAK inhibitors used for AS blunt antiviral immunity and raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A painful, progressive, lifelong disease breeds worry: the chronic pain, stiffening and uncertainty of disease progression in ankylosing spondylitis foster chronic health anxiety alongside its depression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its fused, brittle spine endangers the cord: an ankylosed spine fractures with minor trauma and can injure the spinal cord, while long-standing disease can cause cauda equina syndrome from dural ectasia."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an HLA-B27-linked autoinflammatory disease: IL-17/IL-23 and TNF signalling drive the enthesitis and new bone formation, which is why TNF and IL-17 biologics are central to its treatment."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Decades of inflammation can poison the kidney: sustained systemic inflammation in ankylosing spondylitis can deposit secondary AA amyloid in the kidneys, causing proteinuria and progressive renal failure."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It begins in the gut: most patients with ankylosing spondylitis have subclinical microscopic gut inflammation reflecting a shared gut-joint axis, and a minority develop overt inflammatory bowel disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Skin overlaps and reacts: as a spondyloarthritis it overlaps with psoriasis, and the TNF inhibitors used to treat it can paradoxically trigger psoriasiform skin eruptions."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Chronic inflammation thins bone and disturbs hormones: sustained inflammation and reduced mobility drive secondary osteoporosis, and the inflammatory state can suppress the gonadal axis."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Biologics control the spine: anti-TNF agents like adalimumab, and IL-17 inhibitors, suppress the axial inflammation of ankylosing spondylitis when NSAIDs are insufficient."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "NSAIDs are first-line: continuous NSAIDs like ibuprofen relieve the inflammatory back pain and may slow radiographic progression of ankylosing spondylitis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids have a limited, local role: unlike in rheumatoid arthritis, systemic steroids help little in axial disease, but local injections treat enthesitis, peripheral arthritis and acute uveitis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics target its cytokines: when NSAIDs fail, ankylosing spondylitis responds to anti-TNF and IL-17 inhibitors like secukinumab, and to JAK inhibitors — agents hitting the IL-23/IL-17 axis that drives the spinal inflammation."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It both fuses and weakens bone: ankylosing spondylitis paradoxically lays down syndesmophytes that bridge vertebrae into a bamboo spine while the trapped, inflamed bone becomes osteoporotic — a rigid spine prone to fracture from minor trauma."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It inflames the aortic root: chronic inflammation in ankylosing spondylitis causes aortitis and aortic-root dilatation, producing aortic regurgitation and conduction block as the disease reaches the wall of the great vessel."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A caution for its TNF blockers: the anti-TNF biologics central to ankylosing spondylitis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—one cytokine blockade easing the spine yet harming nerves."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "A gut-joint axis: most people with ankylosing spondylitis have subclinical inflammation of the intestinal epithelium, and the same IL-23/IL-17 mucosal immunity links the gut microbiome to the inflamed spine."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "A confounding comorbidity: fibromyalgia is common in ankylosing spondylitis and inflates composite disease-activity scores with widespread pain, so distinguishing it from active inflammation guides whether to escalate biologics."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Conduction disease and aortitis: ankylosing spondylitis inflames the aortic root and the cardiac conduction system, causing aortic regurgitation and atrioventricular block independent of atherosclerosis."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Apical lung fibrosis: long-standing ankylosing spondylitis produces upper-lobe fibrobullous disease in the alveoli, restricting an already rigid, fused thoracic cage and risking secondary aspergillus colonisation."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Secondary amyloidosis: decades of uncontrolled inflammation in ankylosing spondylitis can deposit AA amyloid in the glomerulus, causing proteinuria and renal failure—now rare in the biologic era."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Aortitis and valve disease: ankylosing spondylitis inflames the aortic root and valve, causing aortic regurgitation and scarring of the endocardium alongside the conduction-system disease it is better known for."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Apical fibrobullous disease: the upper lobes in long-standing ankylosing spondylitis develop fibrocavitary change that can become colonised by Aspergillus, forming an aspergilloma within the cavity."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Cauda equina syndrome: a rare late complication of ankylosing spondylitis is arachnoiditis and dural ectasia in the rigid lumbar spine that compresses the cauda equina nerve roots, causing bladder, bowel and leg dysfunction."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Pathological new bone: TGF-β and BMP signalling drive the abnormal ossification that fuses the spine in ankylosing spondylitis, forming the bridging syndesmophytes."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis at entheses: VEGF-driven new-vessel growth accompanies the enthesitis and new bone formation of ankylosing spondylitis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Recruiting inflammation: CCL2 draws monocytes and macrophages to the inflamed entheses and sacroiliac joints that characterise ankylosing spondylitis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Innate enthesitis: IL-1β contributes to the innate immune activation at entheses that drives the inflammation and new bone formation of ankylosing spondylitis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that adds to the IL-23/IL-17-driven inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 contribution: IFN-γ from Th1 cells participates in the mixed cytokine milieu of the inflamed sacroiliac joints and spine in ankylosing spondylitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Alarmin biomarker: calprotectin (S100A8/A9) from activated neutrophils is elevated in both the gut and joints of ankylosing spondylitis, serving as a biomarker that tracks disease activity and the subclinical bowel inflammation common in the disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Gut-joint axis: TLR4 sensing of a dysbiotic microbiome in the subclinically inflamed gut is proposed to seed the IL-23/IL-17 response that drives the spinal and sacroiliac inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Inflammation-to-bone link: osteopontin is elevated in ankylosing spondylitis and connects the entheseal inflammation to the abnormal new-bone formation (syndesmophytes) that fuses the spine, correlating with radiographic progression."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Entheseal alarmin: IL-33 released from mechanically stressed entheseal cells activates innate lymphoid and γδ T cells to make IL-17, an upstream alarmin feeding the IL-23/IL-17 axis that drives the enthesitis at the root of ankylosing spondylitis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and comorbidity: leptin is elevated in ankylosing spondylitis and promotes Th17 responses, linking the systemic inflammation to the metabolic and cardiovascular comorbidity that accompanies the spinal disease."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic enthesitis: substance P from the sensory nerves richly supplying entheses contributes to the neurogenic inflammation and inflammatory back pain of ankylosing spondylitis, linking nociceptive innervation to the entheseal disease."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Syndesmophyte formation: FGF/FGFR signalling drives the pathological osteoblast activity that builds the syndesmophytes bridging and fusing the vertebrae, the defining new-bone phenotype of ankylosing spondylitis."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Enthesitis stroma: PDGF activates entheseal fibroblasts and the angiogenesis that accompanies the enthesitis of ankylosing spondylitis, contributing to the inflamed, vascularised insertion sites."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/23 axis: IL-12 shares its p40 subunit with the IL-23 already mapped, and this type-3-skewing IL-12/23 axis underlies the immune response targeting the entheses in ankylosing spondylitis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Gut-joint innate signalling: TLR signalling (TLR4 mapped) through MyD88 to NF-κB (mapped), driven by the dysbiotic gut in the gut-joint axis, helps initiate the inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Entheseal neuro-immunity: sensory CGRP at entheses links neurogenic signalling to the enthesitis and new-bone formation (syndesmophytes) that characterise ankylosing spondylitis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory balance: a relative shortfall of anti-inflammatory IL-10 against the dominant IL-23/IL-17 axis (mapped) contributes to the persistent spinal and entheseal inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Th17 immunometabolism: mTOR-driven metabolic activation of Th17 cells and entheseal stromal cells sustains the IL-23/IL-17 inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Inflammation and osteoproliferation: PI3K-AKT signalling participates in both the inflammatory-cell survival and the osteoblast-driven new-bone formation that characterise the spinal ankylosis of ankylosing spondylitis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "HLA-B27 cytotoxicity: HLA-B27-restricted CD8 cytotoxic T cells deploy perforin in the entheseal and synovial inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling in the Th1 arm of the inflammatory response shapes the entheseal and axial inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the pathological new bone formation and syndesmophyte growth that fuse the spine in ankylosing spondylitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the innate inflammation and tissue remodelling of the enthesis in ankylosing spondylitis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of TNF and IL-17 (both mapped) couples entheseal inflammation to the osteoblast differentiation that drives new bone in ankylosing spondylitis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate osteoblast differentiation and oxidative-stress balance relevant to the pathologic bone formation of ankylosing spondylitis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic inflamed enthesis promotes angiogenesis and osteogenic differentiation, contributing to syndesmophyte formation in ankylosing spondylitis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory and Wnt-dependent osteoproliferative signaling of ankylosing spondylitis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the enthesis in ankylosing spondylitis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling in osteoblasts and immune cells contributes to the pathological new-bone formation and inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the immune cells and osteoprogenitors of ankylosing spondylitis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the T-cell activation and osteogenic metabolism of ankylosing spondylitis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy, linked to HLA-B27 misfolding and ER stress, participates in the immune activation of ankylosing spondylitis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the entheses and axial joints contributes to the inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of ankylosing spondylitis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte recruitment and new-bone-formation (enthesis) processes of ankylosing spondylitis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of ankylosing spondylitis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of ankylosing spondylitis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the innate immune activation of ankylosing spondylitis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Cardiovascular risk: the chronic systemic inflammation of ankylosing spondylitis impairs endothelial nitric-oxide function, accelerating atherosclerosis and raising the cardiovascular mortality that accompanies the axial disease."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Gut-joint axis: subclinical gut inflammation with an altered secretory IgA response is part of the spondyloarthritis gut-joint axis, linking the intestinal microbiome and mucosal immunity to the enthesitis and sacroiliitis of ankylosing spondylitis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Entheseal neovascularisation: inflamed entheses in ankylosing spondylitis show increased vascularity on Doppler imaging, driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the angiogenic response accompanying the enthesitis before new bone forms."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of inflammation: sustained systemic inflammation in active ankylosing spondylitis suppresses erythropoiesis, and a normocytic anaemia lowering haemoglobin is a common systemic feature that tracks with disease activity."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac involvement: ankylosing spondylitis causes aortitis, aortic-root disease and atrioventricular conduction block (heart already mapped), and troponin elevation can mark the myocardial injury of its cardiovascular manifestations."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: although the risk allele HLA-B27 is class I, MHC class II presentation and the broader HLA landscape shape the autoreactive and IL-17-driven T-cell response of ankylosing spondylitis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Cardiovascular risk: the chronic systemic inflammation of ankylosing spondylitis alters cholesterol handling and accelerates atherosclerosis (nitric oxide already mapped), raising the cardiovascular risk that adds to its aortitis and conduction disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative enthesitis: reactive oxygen species generated in the inflamed entheses, to which xanthine oxidase contributes, amplify the tissue injury, and the associated hyperuricaemia links ankylosing spondylitis to coexisting gout."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine inflammation: adiponectin and other adipokines (leptin already mapped) modulate the inflammation of ankylosing spondylitis, part of the metabolic-immune crosstalk shaping disease activity and its cardiovascular comorbidity."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of ankylosing spondylitis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) seen in active disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron sequestration: the systemic inflammation of ankylosing spondylitis sequesters iron through hepcidin (already mapped), causing the anaemia of chronic disease, part of its systemic haematological involvement."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: the systemic inflammation (TNF and IL-6 already mapped) of ankylosing spondylitis and the reduced mobility promote insulin resistance (leptin and adiponectin already mapped), contributing to its metabolic and cardiovascular comorbidity."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 counter-regulation: IL-4 and the Th2 arm (IL-10 already mapped) oppose the Th17/IL-23 (IL-17 and IL-23 already mapped) drive of the enthesitis, the anti-inflammatory balance in ankylosing spondylitis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory Th17 axis shapes the spondyloarthritis of ankylosing spondylitis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Gut-joint axis: the subclinical terminal-ileal (Crohn's-like) inflammation of the small intestine (secretory-IgA already mapped) is characteristic of the gut-joint axis of the IL-23/IL-17 spondyloarthritis of ankylosing spondylitis."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Syndesmophyte new bone: the Wnt and sclerostin (already mapped)-regulated osteoblasts form the pathological new bone (the syndesmophytes; cortical bone already mapped) that fuses the spine of ankylosing spondylitis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Bone-mineral paradox: the calcium and bone-mineral metabolism of the paradoxical osteoporosis-with-new-bone (RANKL and sclerostin already mapped) of ankylosing spondylitis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of ankylosing spondylitis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophilic enthesitis: the neutrophils, recruited by the IL-17 (already mapped) axis, drive the acute entheseal and axial inflammation of ankylosing spondylitis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension of the gut-joint (secretory-IgA already mapped) axis of ankylosing spondylitis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the dominant Th17 (IL-17 already mapped) drive of ankylosing spondylitis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the innate immune dysregulation of the gut-joint axis of ankylosing spondylitis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (immunoglobulin already mapped), a humoral component increasingly recognised in the axial spondyloarthritis of ankylosing spondylitis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension balancing the dominant Th17 axis of ankylosing spondylitis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Entheseal alarmin: TSLP, an epithelial/stromal alarmin, is part of the alarmin (IL-33 already mapped) signalling of the enthesis that contributes to the barrier-immune crosstalk of ankylosing spondylitis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Entheseal matricellular: periostin is part of the matricellular remodelling of the enthesis that accompanies the pathological new-bone formation (sclerostin and Wnt already mapped) of ankylosing spondylitis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the neutrophil recruitment in the inflamed entheses and joints of ankylosing spondylitis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) active in the inflamed synovium and entheses of ankylosing spondylitis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical/lectin regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways contributing to the innate inflammation of the entheses of ankylosing spondylitis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of chronic disease of ankylosing spondylitis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Nociceptive kinin: bradykinin, generated by kallikrein activation in the inflamed sacroiliac joints and entheses of ankylosing spondylitis, activates B1/B2 receptors on nociceptive fibres (peripheral nerve already mapped), amplifying the axial pain and morning stiffness."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia support: erythropoietin corrects the normocytic anaemia of chronic inflammation (hepcidin and transferrin already mapped) that accompanies active ankylosing spondylitis and contributes to the fatigue burden of the disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: complement C5, upstream of C5aR1 (already mapped), is activated by the anti-HLA-B27 (MHC-II already mapped) immune response at the entheses and sacroiliac joints of ankylosing spondylitis, amplifying the innate-driven inflammation."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell enthesitis: histamine, released by mast cells (already mapped) infiltrating the inflamed entheses of ankylosing spondylitis, amplifies the local vascular permeability and nociceptive signalling (bradykinin already mapped) of the enthesitis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian–immune axis: melatonin modulates the Th17/Treg balance (IL-17 and TGF-β already mapped) and exhibits anti-inflammatory effects that may influence the nocturnal pain pattern of ankylosing spondylitis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during chronic inflammation, potentiates B-cell and T-cell activation (IL-17 and TNF already mapped) and may amplify the systemic immune dysregulation of ankylosing spondylitis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "AS testosterone: testosterone suppresses IL-17A (already mapped) and TNF-α (already mapped) driven inflammation, partially explaining male-sex protection in ankylosing spondylitis; androgen deficiency promotes bone-marrow (already mapped) driven osteoproliferation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "AS serotonin: serotonin modulates the pain sensitisation of ankylosing spondylitis via 5-HT receptors on the dorsal horn; serotonin also influences the Th17/Treg balance (IL-17A and TGF-β already mapped) and bone-marrow (already mapped) immune dysregulation."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "AS oxytocin: oxytocin exerts anti-inflammatory effects by suppressing NF-κB-driven TNF-α (already mapped) and IL-23 (already mapped) production; oxytocin receptor on osteoblasts promotes cortical bone (already mapped) formation, countering the ankylosing structural damage."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AS vasopressin: vasopressin V1A receptors on entheseal cells modulate pain sensitisation and inflammation in ankylosing spondylitis; AVP signalling intersects NF-κB (already mapped) and IL-17A (already mapped) driven pro-inflammatory cascades in axial spondyloarthritis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "AS selenium: selenium-dependent GPX antioxidant activity counters the oxidative stress driving NF-κB (already mapped) and TNF-α (already mapped) mediated entheseal inflammation and bone-marrow (already mapped) osteoproliferation in ankylosing spondylitis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "AS iodine: iodine-dependent thyroid hormones modulate NF-κB (already mapped) and IL-17A (already mapped) entheseal inflammation in ankylosing spondylitis; hypothyroidism (autoimmune-thyroid comorbidity) amplifies musculoskeletal pain and the osteoproliferative structural damage."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "AS sodium: excess sodium promotes macrophage (already mapped) and t-helper-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-17A (already mapped) amplify TNF-α (already mapped) and IL-6 (already mapped) osteoproliferative cascade of AS."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "AS magnesium: magnesium, as cofactor for osteoblast (already mapped) mineralisation, supports bone formation; magnesium deficiency amplifies osteoclast (already mapped) RANKL and NF-κB (already mapped) and TNF-α (already mapped) osteoproliferative structural damage cascade of AS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "AS potassium: potassium regulates macrophage (already mapped) and osteoblast (already mapped) membrane function; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) and IL-6 (already mapped) cascade in AS."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "AS zinc: zinc cofactors macrophage (already mapped) anti-inflammatory function and osteoblast (already mapped) mineralisation; zinc deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade in AS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "AS copper: copper, via SOD in macrophages (already mapped) and osteoblasts (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) and NLRP3 (already mapped) and TNF-α (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on macrophages (already mapped) and osteoblasts (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in macrophages (already mapped) and osteoblasts (already mapped) promotes cytoprotection; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in macrophages (already mapped) and osteoblasts (already mapped) modulates bone turnover; nitrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) and TNF-α (already mapped) spondylitic cascade in AS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "AS carbon: carbon, as metabolic backbone of collagen and osteoproliferative cytokines in osteoblasts (already mapped) and macrophages (already mapped), drives entheseal remodelling; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) in AS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "AS hydrogen: hydrogen, via redox homeostasis in osteoblasts (already mapped) and macrophages (already mapped), quenches ROS-driven entheseal damage; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) cascade in AS."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "AS oxygen: mitochondrial oxygen in osteoblasts (already mapped) and macrophages (already mapped) sustains ATP for bone remodelling; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "AS PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates entheseal immune homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "AS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and osteoblasts (already mapped) modulates metabolic bone homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade in AS."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "AS angiotensin-II: angiotensin-II in macrophages (already mapped) and osteoblasts (already mapped) promotes entheseal inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of ankylosing spondylitis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "AS IL-2: IL-2 in t-helper-cell (already mapped) and macrophages (already mapped) modulates entheseal immune tolerance; IL-2 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "AS fibronectin: fibronectin in macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal extracellular matrix; fibronectin dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade in AS."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "AS notch: Notch in macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal cell fate; Notch dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "AS igf-1: IGF-1 from macrophages (already mapped) and osteoblasts (already mapped) promotes entheseal bone formation; IGF-1 excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade of AS."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "AS activin-a: activin-A from macrophages (already mapped) and osteoblasts (already mapped) regulates entheseal immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "AS calcitonin: calcitonin from macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "AS insulin-receptor: insulin receptor on macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal metabolic axis; insulin-receptor dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "AS aldosterone: aldosterone from macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal fluid balance; aldosterone excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "AS androgen-receptor: androgen receptor on macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS."
---

# Ankylosing Spondylitis

## Overview

**Ankylosing spondylitis (AS)** — also termed **radiographic axial spondyloarthritis (r-axSpA)** in current classification — is a chronic, progressive, inflammatory arthritis primarily affecting the **axial skeleton** (sacroiliac joints and spine), leading to characteristic spinal fusion ("bamboo spine") in advanced disease [^sieper-2015-ankylosing-spondylitis-review]. AS is the prototypical member of the **spondyloarthropathy (SpA)** family, which also includes reactive arthritis, psoriatic arthritis (PsA), enteropathic arthritis (IBD-SpA), and undifferentiated SpA — united by shared genetic associations (HLA-B27), enthesitis, and characteristic extra-articular manifestations.

**Epidemiology:**
- Prevalence: 0.1-1.4% in European populations (population prevalence depends on HLA-B27 frequency)
- Male predominance: ~2-3:1 M:F (though females are often underdiagnosed with less classic radiographic changes)
- Age of onset: typically teens to 30s (90% of patients have symptom onset before age 45)
- The broader category of **axial SpA (axSpA)** includes non-radiographic axSpA (nr-axSpA) — active sacroiliac inflammation on MRI without established radiographic changes; prevalence ~0.5-1.5%

**Current classification framework:**
- **ASAS (Assessment of SpondyloArthritis international Society) axSpA criteria:** Imaging arm (sacroiliitis on MRI or X-ray + ≥1 SpA feature) OR clinical arm (HLA-B27+ + ≥2 SpA features); SpA features include IBP, arthritis, enthesitis, uveitis, dactylitis, psoriasis, IBD, family history, HLA-B27, elevated CRP, sacroiliitis
- **Modified New York criteria (for radiographic AS):** Sacroiliitis grade ≥2 bilateral or ≥3 unilateral PLUS ≥1 of: IBP ≥3 months (improves with exercise, not rest), restricted lumbar spine movement, limited chest expansion

## Structure

### Pathogenesis — enthesitis as the disease origin

AS originates at the **enthesis** — the site where tendons, ligaments, and joint capsules attach to bone. Enthesitis (entheseal inflammation) is the pathognomonic lesion of SpA and explains the clinical distribution of disease (sacroiliac joints, discovertebral junctions, Achilles tendon, plantar fascia).

**Enthesis anatomy and vulnerability:**
- Fibrocartilaginous entheses at the sacroiliac joint and discovertebral junction are anatomically avascular zones → normally immune-privileged
- Mechanical micro-trauma at entheses → local DAMP release → activation of resident macrophages and ILC3 cells
- Gut microbiome dysbiosis (60% of AS patients have subclinical intestinal inflammation) → bacterial antigen translocation → entheseal innate immune activation

**Cellular pathogenesis:**
1. HLA-B27 ER misfolding (in macrophages/DCs) → UPR → ↑IL-23 production
2. Gut dysbiosis → mucosal ILC3 and Th17 cell activation → systemic IL-17A and IL-22
3. Entheseal resident ILC3 cells (IL-17A+ CD3−) respond to IL-23 → local IL-17A/IL-22 burst
4. IL-17A + TNF-α → RANKL upregulation on bone stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral "corners" (Romanus lesions)
5. Paradoxically, post-erosion repair drives osteoblast-mediated new bone formation via **WNT pathway** (DKK1 suppression + WNT ligand upregulation) → syndesmophytes → eventual spinal fusion

**Radiographic progression:** Vertebral corner erosion → sclerosis (shiny corners) → ossification → syndesmophyte formation → spinal ankylosis ("bamboo spine" on plain film). TNF and IL-17A inhibition reduces inflammation markers but has less certain effect on radiographic progression — possibly because bone formation has its own autonomous WNT-driven program.

### Genetic architecture

- **HLA-B27:** >70% of AS heritability; OR ~90 — dominant genetic risk
- **ERAP1 and ERAP2:** ER aminopeptidases that trim peptides for HLA-I loading; ERAP1 polymorphisms modify AS risk specifically in HLA-B27+ background (epistasis)
- **IL23R, STAT3, TYK2, PTPN22, TNFRSF1A:** Additional GWAS loci confirming IL-23/Th17 and TNF pathway centrality
- Concordance in identical twins: ~60-65% (suggesting additional environmental factors, particularly gut microbiome)

## Function

### Clinical features

**Axial disease:**
- **Inflammatory back pain (IBP):** Insidious onset, age <45, morning stiffness >30 min, improves with exercise, worsens with rest; nocturnal pain waking patient in second half of night — characteristic SpA feature
- **Sacroiliitis:** Bilateral symmetric (AS) vs. asymmetric/unilateral (ReA, PsA); buttock pain; positive FABER/FADIR tests; MRI detects pre-radiographic bone marrow edema at SI joints
- **Spinal involvement:** Restriction of lumbar flexion (Schober test: <5 cm increase from 15 cm mark in full forward flexion is abnormal); cervical restriction; kyphotic deformity in advanced disease
- **Chest expansion:** Costovertebral joint involvement → restricted chest expansion (<5 cm in men); lung function may be mildly reduced

**Extra-articular manifestations (EAMs):**

| Manifestation | Prevalence | HLA-B27 relationship |
|---|---|---|
| **Anterior uveitis (AU)** | 20-30% lifetime | HLA-B27+ patients have more AU episodes; AU is the most common EAM |
| **Psoriasis** | 10% | Some HLA overlap with PsA; skin disease often mild |
| **IBD (Crohn's, UC)** | 5-10% overt; 60% subclinical | Subclinical gut inflammation in majority of AS; axSpA and IBD share IL-23R and other GWAS loci |
| **Cardiac** | ~2-10% | Aortic regurgitation (aortitis); conduction abnormalities (AV block) |
| **Respiratory** | <5% | Apical lung fibrosis (very late disease); restricted ventilation |
| **Osteoporosis** | 30-50% | Inflammation + immobility → vertebral fragility fractures (Anderson lesions) |

**Disease activity scores:**
- **BASDAI (Bath AS Disease Activity Index):** 0-10; based on patient-reported pain, fatigue, peripheral joint symptoms, enthesitis, morning stiffness; ≥4 = active disease requiring biologic therapy
- **ASDAS (AS Disease Activity Score):** Incorporates CRP (or ESR); ASDAS-CRP >2.1 = high disease activity; >3.5 = very high; preferred for clinical trials and biologic therapy decisions

**Imaging:**
- **Plain radiograph:** Gold standard for radiographic AS (sacroiliac grading, syndesmophytes, bamboo spine)
- **MRI sacroiliac joints (STIR or T2 fat-sat):** Active inflammation = bone marrow edema (BME) at SI joints — detects pre-radiographic disease; SPARCC score quantifies activity
- **Low-dose CT:** Precise structural damage assessment at SI joints (erosions, sclerosis, ankylosis)

## Pathology

### Therapies

**NSAIDs (first-line, all patients):**
- COX-1/COX-2 inhibition → ↓prostaglandin-driven entheseal inflammation; diclofenac, naproxen, indomethacin, celecoxib
- Continuous NSAID use associated with slowing of radiographic progression in some studies (controversial)
- Gastric protection (PPI) with non-selective NSAIDs

**Physical therapy:**
- Essential; maintains spinal mobility; swimming and extension exercises; disease-specific PT programs reduce BASDAI and improve function

**Anti-TNF biologics (biologic first-line):**
- **Indications:** BASDAI ≥4 + inadequate NSAID response ×2 NSAIDs over 4 weeks
- **Agents:** Adalimumab (Humira), etanercept (Enbrel), infliximab (Remicade), certolizumab pegol (Cimzia), golimumab (Simponi)
- **Efficacy:** ASAS40 response ~45-55%; rapid MRI inflammation reduction within weeks
- **Limitation:** Does not clearly reduce radiographic progression (new bone); reactivation of latent TB (screen before initiation)

**Anti-IL-17A biologics:**
- **Secukinumab (Cosentyx; anti-IL-17A mAb; Novartis):** MEASURE-1 (n=371): ASAS20 at 16 weeks — 61% (10 mg/kg IV load) vs. 29% placebo; ASAS40 ~41% vs. 12%; FDA approved 2016 for AS [^baeten-2015-secukinumab-as]
- **Ixekizumab (Taltz; anti-IL-17A mAb; Eli Lilly):** COAST-V (biologic-naive AS): ASAS40 52% vs. 18% placebo at week 16; FDA approved 2019 for AS
- **Bimekizumab (anti-IL-17A/F dual mAb):** Superior to secukinumab in PsA; Phase 3 in AS completed (higher ASAS40 responses)

**Anti-IL-23 biologics:**
- Risankizumab, guselkumab: approved in PsA; **disappointing results in AS** — SURPASS trial (risankizumab) did not meet primary endpoint at week 16; ongoing research into why IL-23 blockade is less effective despite its upstream role (possible IL-23-independent ILC3 IL-17A production at entheses)

**JAK inhibitors:**
- **Tofacitinib (Xeljanz; JAK1/3):** SELECT-AXIS-1: ASAS40 52% vs. 26% at week 16 in biologic-naive AS; FDA approved 2021 for AS
- **Upadacitinib (Rinvoq; JAK1):** SELECT-AXIS-2: ASAS40 64% vs. 44% (anti-TNF failure); FDA approved 2022 for AS; particularly useful for IL-17A/anti-TNF dual failures

**Biologic monitoring:**
- Screen for TB (IGRA/Mantoux), HBV, HCV, HIV before initiating biologics
- No live vaccines while on biologics
- Pregnancy: certolizumab pegol (anti-TNF) is preferred (minimal placental transfer); biologics generally held in 3rd trimester for other agents

## Connections

- `connects-to` → **[HLA-B27](../../03-molecular/hla-b27/README.md)** — HLA-B27 is the strongest genetic risk factor for AS (carried in ~90% of AS patients vs. 8% of Europeans); B*27:05 confers highest AS risk; HLA-B27 misfolding in ER → UPR → IL-23 → Th17/ILC3 → IL-17A → enthesitis; HLA-B27 also predicts uveitis and familial clustering.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is the central effector cytokine in AS enthesitis: ILC3 and Th17 cells at entheses produce IL-17A → RANKL + MMP → bone erosion + osteoblast activation → new bone (syndesmophytes); secukinumab (MEASURE-1) achieved ASAS20 ~61% vs. 29% placebo; ixekizumab also approved.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Entheseal IL-17A + TNF-α → RANKL on stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral corners; new bone formation (syndesmophytes) follows via WNT pathway; denosumab (anti-RANKL) reduces erosion but does not halt new bone formation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) achieve ASAS40 ~50-60% in active AS; TNF inhibition reduces MRI inflammation but does not halt radiographic progression (new bone).
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Axial PsA and AS share HLA-B27, sacroiliitis imaging, and IL-17A/TNF-α pathobiology; distinguished by concurrent psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF are effective in both; IL-23 inhibitors diverge in efficacy.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Acute anterior uveitis is the most common extra-articular manifestation of ankylosing spondylitis, affecting 20-30% over a lifetime and tracking with HLA-B27; it presents as a painful, red, photophobic eye that recurs and alternates between eyes.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Ankylosing spondylitis and IBD are two faces of the gut-joint axis: ~60% of AS patients have subclinical gut inflammation and 5-10% develop overt Crohn's or colitis, reflecting shared IL-23R genetics; anti-TNF treats both, but IL-17 blockade can flare IBD.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — HLA-B27 misfolding in the ER triggers an unfolded-protein response that ramps up IL-23, driving entheseal ILC3 and Th17 cells to pour out IL-17A; paradoxically, IL-23 blockade fails in AS despite this upstream role — likely because ILC3s make IL-17A independently of IL-23.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — AS and psoriasis lie on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis; IL-17 inhibitors (secukinumab, ixekizumab) treat both and psoriasis is a common AS comorbidity—yet IL-23 blockade helps psoriasis but failed in axial AS, hinting at divergent biology.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — AS is the prototypical axial spondyloarthritis: enthesitis and sacroiliitis at the spine and SI joints → inflammatory back pain → syndesmophytes and bony ankylosis ('bamboo spine'); IL-17-driven new-bone formation and erosion reshape the axial skeleton and reduce spinal mobility.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — AS uniquely couples inflammation to bone formation: at entheses IL-17A/TNF and Wnt (low DKK-1/sclerostin) activate osteoblasts → syndesmophytes and ankylosis, even as RANKL drives co-existing erosion; this osteoproliferation distinguishes AS from erosive rheumatoid arthritis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Ankylosing spondylitis paradoxically combines bone formation and bone loss: while syndesmophytes fuse the spine, systemic inflammation drives vertebral osteoporosis beneath, so a rigid 'bamboo spine' is brittle and prone to fracture from even minor trauma.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Ankylosing spondylitis has cardiac complications beyond the spine: inflammation causes aortitis with aortic-root dilatation and regurgitation, conduction disease and heart block, and accelerated atherosclerosis—a major driver of its excess mortality.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Ankylosing spondylitis is linked to IgA nephropathy, its commonest renal complication: both share HLA-B27-associated, IL-23-driven mucosal immunity with elevated serum IgA, so hematuria or proteinuria in AS prompts evaluation for IgA nephropathy or secondary AA amyloidosis.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Ankylosing spondylitis and rheumatoid arthritis are the major chronic inflammatory arthritides but opposite: AS is a seronegative, HLA-B27-linked, IL-17/23-driven spondyloarthritis of the axial skeleton, while RA is a seropositive peripheral synovitis with erosion.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells, especially the Th17 lineage, drive ankylosing spondylitis: IL-23 expands IL-17-producing T cells at entheses and the sacroiliac joints, fueling inflammation and new bone formation—so IL-17 and IL-23 blockers (secukinumab) target this T-cell axis.
- `connects-to` → **[Gout](../gout/README.md)** — Ankylosing spondylitis and gout are both inflammatory arthritides but different in cause: AS is an autoimmune HLA-B27 spondyloarthritis of the spine, while gout is crystal-driven innate inflammation of peripheral joints—axial autoimmunity versus crystal arthropathy.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Enthesis fibroblasts build the bony fusion of ankylosing spondylitis: at sites where tendon meets bone, inflammation drives fibroblasts and osteoblasts to lay down new bone (syndesmophytes), so the spine gradually ossifies into the rigid bamboo spine.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Ankylosing spondylitis reaches the heart: chronic inflammation can cause aortitis with aortic-root dilation and regurgitation plus conduction block, so cardiac evaluation is part of long-standing AS—an extra-articular manifestation beyond the spine.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Ankylosing spondylitis restricts and scars the lungs: fusion of the rib-spine joints stiffens the chest wall limiting expansion, and apical pulmonary fibrosis develops in advanced disease—so breathing is impaired both mechanically and by lung scarring.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Ankylosing spondylitis is tied to the gut: most patients have subclinical bowel inflammation, and a dysbiotic microbiome in HLA-B27 carriers is thought to drive the IL-23/IL-17 axis—linking gut bacteria to spinal disease along the gut-joint axis.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — AS damages and remakes collagen-rich tissue: chronic enthesitis erodes the collagen anchors where ligaments meet bone, then heals by ossification, so syndesmophytes bridge vertebrae—turning the spine's flexible collagen attachments into rigid bone.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — AS creates a calcium paradox in the skeleton: ligaments ossify and deposit calcium into rigid syndesmophytes while the vertebral bodies inside lose mineral and become osteoporotic—so the stiff bamboo spine is brittle and prone to fracture.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Ankylosing spondylitis fuses the spine via Wnt-driven bone formation: inflammation shifts the Wnt/sclerostin balance to activate osteoblasts, building the syndesmophytes that bridge vertebrae into a 'bamboo spine'—why anti-inflammatories don't fully stop fusion.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — HLA-B27 ties ankylosing spondylitis to cytotoxic T cells: the class I molecule presents peptides to CD8 T cells, and the leading 'arthritogenic peptide' hypothesis holds that this drives the autoimmune attack on the spine and joints.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors are a newer ankylosing spondylitis therapy: oral drugs like upadacitinib block JAK signaling downstream of inflammatory cytokines, controlling axial disease in patients who fail or can't take TNF and IL-17 biologics.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Ankylosing spondylitis fuses the spine by silencing sclerostin: this Wnt-pathway brake on bone formation falls in AS, so unopposed Wnt drives the new bone (syndesmophytes) that bridges vertebrae into a bamboo spine.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D shapes ankylosing spondylitis: deficiency is common and may worsen both the bone loss and the IL-17-driven inflammation, so vitamin D status is watched in a disease that paradoxically erodes and overgrows bone.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Ankylosing spondylitis may ignite from dendritic cells: sensing gut microbes and HLA-B27-presented peptides, they secrete IL-23 that drives the IL-17 response attacking entheses, linking the gut to the inflamed spine.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — A gut-joint axis drives ankylosing spondylitis: subclinical bowel inflammation and a disturbed microbiome prime the IL-23/IL-17 response that attacks the spine, linking the large intestine to the disease and its overlap with IBD.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Ankylosing spondylitis both erodes and fuses bone: osteoclasts carve early erosions at inflamed entheses even as new bone later bridges the joints, so the same disease that destroys bone ends by welding the spine rigid.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages bridge gut and spine in ankylosing spondylitis: activated in the inflamed bowel and at the entheses, they pour out TNF and other cytokines that drive the inflammation, making them a hub of the IL-23/IL-17-fed disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The earliest AS lesion lives in bone: marrow edema (osteitis) in the sacroiliac joints is the MRI hallmark that lets doctors catch axial disease years before X-rays show fusion.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — AS is defined by what X-ray photons reveal: radiographic sacroiliitis and the fused bamboo spine confirm the disease, while MRI catches the earlier inflammation that plain films miss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — The syndesmophytes that weld the AS spine are built of bone mineral: new bone formation lays down calcium-phosphate hydroxyapatite, so phosphate as well as calcium feeds the pathological fusion.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Decades of inflammation can poison the kidney: AS is a classic cause of secondary AA amyloidosis, where serum amyloid protein deposits in the kidney and triggers a slow slide into renal failure, alongside its links to IgA nephropathy.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — AS quietly scars the top of the lungs: a hallmark extra-articular finding is fibrobullous disease of the upper lobes, where progressive apical fibrosis stiffens the chest already restricted by the fused, rigid rib cage.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — AS sits in a family of skin-linked diseases: it overlaps the spondyloarthritis spectrum with psoriasis, so the same HLA-B27-associated, IL-17-driven inflammation that fuses the spine often shows as scaly plaques on the skin.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A fused spine is a brittle one: the rigid bamboo spine of AS fractures from minor trauma, and these unstable breaks can crush the spinal cord, while chronic arachnoid scarring rarely produces a cauda equina syndrome of leg weakness and bladder loss.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Chronic inflammation thins the blood: like other rheumatic diseases, active AS drives the anemia of chronic disease, with inflammatory hepcidin locking iron away from the red cells and leaving patients tired beyond their joint pain.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Treating AS means watching the liver: before starting the TNF-blocking biologics that calm the spine, patients are screened for hepatitis B to avoid reactivating it, and long-term NSAID use adds its own hepatic and GI risks.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — AS is seronegative yet treated with antibodies: rheumatoid factor and anti-CCP are absent, marking it apart from RA, while monoclonal antibodies against TNF and IL-17 are the mainstay that calms the spine when NSAIDs fall short.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The inflammation creeps toward the heart's core: AS causes aortic-root inflammation with regurgitation and conduction disease, fibrosis invading the valve and the AV node so the cardiomyocytes' wiring blocks and the rhythm slows.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Disease and drugs touch reproduction: AS strikes men in their reproductive prime, and family planning weighs the safety of NSAIDs and biologics in pregnancy, while severe spinal fusion can complicate the mechanics of conception and delivery.
- `connects-to` → **[Prostaglandins (Eicosanoids)](../../03-molecular/prostaglandins/README.md)** — NSAIDs are AS's first-line drug: by blocking COX and the prostaglandins that mediate the inflammatory pain, they relieve symptoms and, taken continuously, may even slow the spinal new-bone formation that fuses the spine.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the enthesis: resident at the tendon-and-ligament insertions where AS begins, they are a major innate source of IL-17, helping ignite the enthesitis that is the disease's defining lesion.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Chronic inflammation hardens the arteries: AS raises cardiovascular risk through accelerated atherosclerosis, so heart attack and stroke become important causes of death and disease control doubles as cardiovascular protection.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 fuels both the inflammation and its toll: this cytokine helps drive the Th17 axis and the systemic acute-phase response of AS, contributing to the chronic-disease anemia and fatigue that accompany the spinal disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The brakes on inflammation slip: a relative shortfall of regulatory T cells lets the IL-23/Th17 response run unchecked at the entheses, tilting the balance toward the IL-17-driven inflammation that ossifies the spine.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Inflammation reaches the heart's structure: AS can inflame the aortic root into regurgitation and scar the conduction system, valve and conduction disease that, on top of the cardiovascular risk, can drift into heart failure.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 carries the IL-23 signal into Th17 cells: it is the transcription factor that drives the IL-17-producing T cells central to AS, which is why STAT3-dependent cytokine pathways are prime drug targets in the disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB transmits the TNF signal: at the inflamed entheses, TNF acts largely through NF-κB to sustain the inflammatory and bone-remodeling programs, the pathway that anti-TNF biologics interrupt to calm AS.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Chronic inflammation raises the clot risk: ankylosing spondylitis carries an increased rate of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic tendency shared across the systemic inflammatory diseases.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its TNF biologics can wake latent TB: the anti-TNF agents that transformed AS treatment disable the granuloma containing Mycobacterium tuberculosis, so latent-TB screening and treatment precede therapy to prevent reactivation.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Sustained inflammation dulls the marrow: the chronic IL-6 drive of active ankylosing spondylitis raises hepcidin and blunts erythropoiesis, producing the anemia of chronic disease that tracks with disease activity.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Decades of inflammation can scar the kidney: long-standing AS can deposit secondary AA amyloid in the kidney and, alongside its associated IgA nephropathy, progress to chronic kidney disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — Chronic systemic inflammation accelerates the arteries: the sustained inflammatory burden of ankylosing spondylitis speeds atherosclerosis and, with reduced mobility, raises the long-term risk of ischemic stroke.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Its TNF inhibitors can reactivate hepatitis B: the anti-TNF biologics central to treating AS can reawaken a dormant hepatitis B virus, so serologic screening and antiviral prophylaxis precede therapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relentless pain and stiffening wear on mood: the chronic back pain, fatigue, poor sleep and progressive loss of mobility in ankylosing spondylitis contribute to markedly elevated rates of depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — A fused chest cannot breathe freely: ankylosis of the costovertebral joints and thoracic spine stiffens the rib cage into restrictive lung disease, and apical pulmonary fibrosis adds to the burden.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunomodulatory drugs reawaken shingles: the TNF, IL-17 and JAK inhibitors used for AS blunt antiviral immunity and raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A painful, progressive, lifelong disease breeds worry: the chronic pain, stiffening and uncertainty of disease progression in ankylosing spondylitis foster chronic health anxiety alongside its depression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its fused, brittle spine endangers the cord: an ankylosed spine fractures with minor trauma and can injure the spinal cord, while long-standing disease can cause cauda equina syndrome from dural ectasia.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an HLA-B27-linked autoinflammatory disease: IL-17/IL-23 and TNF signalling drive the enthesitis and new bone formation, which is why TNF and IL-17 biologics are central to its treatment.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Decades of inflammation can poison the kidney: sustained systemic inflammation in ankylosing spondylitis can deposit secondary AA amyloid in the kidneys, causing proteinuria and progressive renal failure.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It begins in the gut: most patients with ankylosing spondylitis have subclinical microscopic gut inflammation reflecting a shared gut-joint axis, and a minority develop overt inflammatory bowel disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Skin overlaps and reacts: as a spondyloarthritis it overlaps with psoriasis, and the TNF inhibitors used to treat it can paradoxically trigger psoriasiform skin eruptions.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Chronic inflammation thins bone and disturbs hormones: sustained inflammation and reduced mobility drive secondary osteoporosis, and the inflammatory state can suppress the gonadal axis.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Biologics control the spine: anti-TNF agents like adalimumab, and IL-17 inhibitors, suppress the axial inflammation of ankylosing spondylitis when NSAIDs are insufficient.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs are first-line: continuous NSAIDs like ibuprofen relieve the inflammatory back pain and may slow radiographic progression of ankylosing spondylitis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids have a limited, local role: unlike in rheumatoid arthritis, systemic steroids help little in axial disease, but local injections treat enthesitis, peripheral arthritis and acute uveitis.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics target its cytokines: when NSAIDs fail, ankylosing spondylitis responds to anti-TNF and IL-17 inhibitors like secukinumab, and to JAK inhibitors — agents hitting the IL-23/IL-17 axis that drives the spinal inflammation.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It both fuses and weakens bone: ankylosing spondylitis paradoxically lays down syndesmophytes that bridge vertebrae into a bamboo spine while the trapped, inflamed bone becomes osteoporotic — a rigid spine prone to fracture from minor trauma.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It inflames the aortic root: chronic inflammation in ankylosing spondylitis causes aortitis and aortic-root dilatation, producing aortic regurgitation and conduction block as the disease reaches the wall of the great vessel.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A caution for its TNF blockers: the anti-TNF biologics central to ankylosing spondylitis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—one cytokine blockade easing the spine yet harming nerves.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — A gut-joint axis: most people with ankylosing spondylitis have subclinical inflammation of the intestinal epithelium, and the same IL-23/IL-17 mucosal immunity links the gut microbiome to the inflamed spine.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — A confounding comorbidity: fibromyalgia is common in ankylosing spondylitis and inflates composite disease-activity scores with widespread pain, so distinguishing it from active inflammation guides whether to escalate biologics.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Conduction disease and aortitis: ankylosing spondylitis inflames the aortic root and the cardiac conduction system, causing aortic regurgitation and atrioventricular block independent of atherosclerosis.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Apical lung fibrosis: long-standing ankylosing spondylitis produces upper-lobe fibrobullous disease in the alveoli, restricting an already rigid, fused thoracic cage and risking secondary aspergillus colonisation.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Secondary amyloidosis: decades of uncontrolled inflammation in ankylosing spondylitis can deposit AA amyloid in the glomerulus, causing proteinuria and renal failure—now rare in the biologic era.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Aortitis and valve disease: ankylosing spondylitis inflames the aortic root and valve, causing aortic regurgitation and scarring of the endocardium alongside the conduction-system disease it is better known for.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Apical fibrobullous disease: the upper lobes in long-standing ankylosing spondylitis develop fibrocavitary change that can become colonised by Aspergillus, forming an aspergilloma within the cavity.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Cauda equina syndrome: a rare late complication of ankylosing spondylitis is arachnoiditis and dural ectasia in the rigid lumbar spine that compresses the cauda equina nerve roots, causing bladder, bowel and leg dysfunction.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Pathological new bone: TGF-β and BMP signalling drive the abnormal ossification that fuses the spine in ankylosing spondylitis, forming the bridging syndesmophytes.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Angiogenesis at entheses: VEGF-driven new-vessel growth accompanies the enthesitis and new bone formation of ankylosing spondylitis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Recruiting inflammation: CCL2 draws monocytes and macrophages to the inflamed entheses and sacroiliac joints that characterise ankylosing spondylitis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Innate enthesitis: IL-1β contributes to the innate immune activation at entheses that drives the inflammation and new bone formation of ankylosing spondylitis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: NLRP3-inflammasome activation matures the IL-1β that adds to the IL-23/IL-17-driven inflammation of ankylosing spondylitis.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 contribution: IFN-γ from Th1 cells participates in the mixed cytokine milieu of the inflamed sacroiliac joints and spine in ankylosing spondylitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) from activated neutrophils is elevated in both the gut and the joints of ankylosing spondylitis, a biomarker that tracks disease activity and reflects the subclinical bowel inflammation present in most patients.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of a dysbiotic microbiome in the subclinically inflamed gut is proposed to seed the IL-23/IL-17 response that drives the spinal and sacroiliac inflammation of ankylosing spondylitis—the molecular core of the gut-joint axis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin is elevated in ankylosing spondylitis and links the entheseal inflammation to the abnormal new-bone formation (syndesmophytes) that progressively fuses the spine, correlating with the radiographic progression that defines structural damage.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from mechanically stressed entheseal cells activates innate lymphoid and γδ T cells to make IL-17, an upstream alarmin feeding the IL-23/IL-17 axis that drives the enthesitis at the root of ankylosing spondylitis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Leptin is elevated in ankylosing spondylitis and promotes Th17 responses, linking the systemic inflammation to the metabolic and cardiovascular comorbidity that accompanies the spinal disease.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P from the sensory nerves richly supplying entheses contributes to the neurogenic inflammation and inflammatory back pain of ankylosing spondylitis, linking nociceptive innervation to the entheseal disease.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF/FGFR signaling drives the pathological osteoblast activity that builds the syndesmophytes bridging and fusing the vertebrae, the defining new-bone phenotype of ankylosing spondylitis.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF activates entheseal fibroblasts and the angiogenesis that accompanies the enthesitis of ankylosing spondylitis, contributing to the inflamed, vascularized insertion sites.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 shares its p40 subunit with the IL-23 already mapped, and this type-3-skewing IL-12/23 axis underlies the immune response targeting the entheses in ankylosing spondylitis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR signaling (TLR4 mapped) through MyD88 to NF-κB (mapped), driven by the dysbiotic gut in the gut-joint axis, helps initiate the inflammation of ankylosing spondylitis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Sensory CGRP at entheses links neurogenic signaling to the enthesitis and new-bone formation (syndesmophytes) that characterize ankylosing spondylitis.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative shortfall of anti-inflammatory IL-10 against the dominant IL-23/IL-17 axis (mapped) contributes to the persistent spinal and entheseal inflammation of ankylosing spondylitis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-driven metabolic activation of Th17 cells and entheseal stromal cells sustains the IL-23/IL-17 inflammation of ankylosing spondylitis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling participates in both the inflammatory-cell survival and the osteoblast-driven new-bone formation that characterize the spinal ankylosis of ankylosing spondylitis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — HLA-B27-restricted CD8 cytotoxic T cells deploy perforin in the entheseal and synovial inflammation of ankylosing spondylitis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling in the Th1 arm of the inflammatory response shapes the entheseal and axial inflammation of ankylosing spondylitis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the pathological new bone formation and syndesmophyte growth that fuse the spine in ankylosing spondylitis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the innate inflammation and tissue remodeling of the enthesis in ankylosing spondylitis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of TNF and IL-17 (both mapped) couples entheseal inflammation to the osteoblast differentiation that drives new bone in ankylosing spondylitis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate osteoblast differentiation and oxidative-stress balance relevant to the pathologic bone formation of ankylosing spondylitis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic inflamed enthesis promotes angiogenesis and osteogenic differentiation, contributing to syndesmophyte formation in ankylosing spondylitis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory and Wnt-dependent osteoproliferative signaling of ankylosing spondylitis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the enthesis in ankylosing spondylitis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling in osteoblasts and immune cells contributes to the pathological new-bone formation and inflammation of ankylosing spondylitis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the immune cells and osteoprogenitors of ankylosing spondylitis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the T-cell activation and osteogenic metabolism of ankylosing spondylitis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy, linked to HLA-B27 misfolding and ER stress, participates in the immune activation of ankylosing spondylitis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the entheses and axial joints contributes to the inflammation of ankylosing spondylitis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the immune responses of ankylosing spondylitis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte recruitment and new-bone-formation (enthesis) processes of ankylosing spondylitis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of ankylosing spondylitis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of ankylosing spondylitis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the innate immune activation of ankylosing spondylitis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Cardiovascular risk: the chronic systemic inflammation of ankylosing spondylitis impairs endothelial nitric-oxide function, accelerating atherosclerosis and raising the cardiovascular mortality that accompanies the axial disease.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Gut-joint axis: subclinical gut inflammation with an altered secretory IgA response is part of the spondyloarthritis gut-joint axis, linking the intestinal microbiome and mucosal immunity to the enthesitis and sacroiliitis of ankylosing spondylitis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Entheseal neovascularisation: inflamed entheses in ankylosing spondylitis show increased vascularity on Doppler imaging, driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the angiogenic response accompanying the enthesitis before new bone forms.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of inflammation: sustained systemic inflammation in active ankylosing spondylitis suppresses erythropoiesis, and a normocytic anaemia lowering haemoglobin is a common systemic feature that tracks with disease activity.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac involvement: ankylosing spondylitis causes aortitis, aortic-root disease and atrioventricular conduction block (heart already mapped), and troponin elevation can mark the myocardial injury of its cardiovascular manifestations.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: although the risk allele HLA-B27 is class I, MHC class II presentation and the broader HLA landscape shape the autoreactive and IL-17-driven T-cell response of ankylosing spondylitis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Cardiovascular risk: the chronic systemic inflammation of ankylosing spondylitis alters cholesterol handling and accelerates atherosclerosis (nitric oxide already mapped), raising the cardiovascular risk that adds to its aortitis and conduction disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative enthesitis: reactive oxygen species generated in the inflamed entheses, to which xanthine oxidase contributes, amplify the tissue injury, and the associated hyperuricaemia links ankylosing spondylitis to coexisting gout.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine inflammation: adiponectin and other adipokines (leptin already mapped) modulate the inflammation of ankylosing spondylitis, part of the metabolic-immune crosstalk shaping disease activity and its cardiovascular comorbidity.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the chronic IL-6 (already mapped) inflammation of ankylosing spondylitis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) seen in active disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron sequestration: the systemic inflammation of ankylosing spondylitis sequesters iron through hepcidin (already mapped), causing the anaemia of chronic disease, part of its systemic haematological involvement.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: the systemic inflammation (TNF and IL-6 already mapped) of ankylosing spondylitis and the reduced mobility promote insulin resistance (leptin and adiponectin already mapped), contributing to its metabolic and cardiovascular comorbidity.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 counter-regulation: IL-4 and the Th2 arm (IL-10 already mapped) oppose the Th17/IL-23 (IL-17 and IL-23 already mapped) drive of the enthesitis, the anti-inflammatory balance in ankylosing spondylitis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory Th17 axis shapes the spondyloarthritis of ankylosing spondylitis.
- `connects-to` → **[Small intestine](../../06-organ/small-intestine/README.md)** — Gut-joint axis: the subclinical terminal-ileal (Crohn's-like) inflammation of the small intestine (secretory-IgA already mapped) is characteristic of the gut-joint axis of the IL-23/IL-17 spondyloarthritis of ankylosing spondylitis.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Syndesmophyte new bone: the Wnt and sclerostin (already mapped)-regulated osteoblasts form the pathological new bone (the syndesmophytes; cortical bone already mapped) that fuses the spine of ankylosing spondylitis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Bone-mineral paradox: the calcium and bone-mineral metabolism of the paradoxical osteoporosis-with-new-bone (RANKL and sclerostin already mapped) of ankylosing spondylitis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of ankylosing spondylitis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophilic enthesitis: the neutrophils, recruited by the IL-17 (already mapped) axis, drive the acute entheseal and axial inflammation of ankylosing spondylitis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension of the gut-joint (secretory-IgA already mapped) axis of ankylosing spondylitis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the dominant Th17 (IL-17 already mapped) drive of ankylosing spondylitis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the innate immune dysregulation of the gut-joint axis of ankylosing spondylitis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (immunoglobulin already mapped), a humoral component increasingly recognised in the axial spondyloarthritis of ankylosing spondylitis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension balancing the dominant Th17 axis of ankylosing spondylitis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Entheseal alarmin: TSLP, an epithelial/stromal alarmin, is part of the alarmin (IL-33 already mapped) signalling of the enthesis that contributes to the barrier-immune crosstalk of ankylosing spondylitis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Entheseal matricellular: periostin is part of the matricellular remodelling of the enthesis that accompanies the pathological new-bone formation (sclerostin and Wnt already mapped) of ankylosing spondylitis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the neutrophil recruitment in the inflamed entheses and joints of ankylosing spondylitis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) active in the inflamed synovium and entheses of ankylosing spondylitis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical/lectin regulation: the C1-esterase inhibitor regulates the classical and lectin complement pathways contributing to the innate inflammation of the entheses of ankylosing spondylitis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of chronic disease of ankylosing spondylitis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Nociceptive kinin: bradykinin, generated by kallikrein activation in the inflamed sacroiliac joints and entheses of ankylosing spondylitis, activates B1/B2 receptors on nociceptive fibres (peripheral nerve already mapped), amplifying the axial pain and morning stiffness.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia support: erythropoietin corrects the normocytic anaemia of chronic inflammation (hepcidin and transferrin already mapped) that accompanies active ankylosing spondylitis and contributes to the fatigue burden of the disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: complement C5, upstream of C5aR1 (already mapped), is activated by the anti-HLA-B27 (MHC-II already mapped) immune response at the entheses and sacroiliac joints of ankylosing spondylitis, amplifying the innate-driven inflammation.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell enthesitis: histamine, released by mast cells (already mapped) infiltrating the inflamed entheses of ankylosing spondylitis, amplifies the local vascular permeability and nociceptive signalling (bradykinin already mapped) of the enthesitis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian–immune axis: melatonin modulates the Th17/Treg balance (IL-17 and TGF-β already mapped) and exhibits anti-inflammatory effects that may influence the nocturnal pain pattern of ankylosing spondylitis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during chronic inflammation, potentiates B-cell and T-cell activation (IL-17 and TNF already mapped) and may amplify the systemic immune dysregulation of ankylosing spondylitis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — AS testosterone: testosterone suppresses IL-17A (already mapped) and TNF-α (already mapped) driven inflammation, partially explaining male-sex protection in ankylosing spondylitis; androgen deficiency promotes bone-marrow (already mapped) driven osteoproliferation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — AS serotonin: serotonin modulates the pain sensitisation of ankylosing spondylitis via 5-HT receptors on the dorsal horn; serotonin also influences the Th17/Treg balance (IL-17A and TGF-β already mapped) and bone-marrow (already mapped) immune dysregulation.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — AS oxytocin: oxytocin exerts anti-inflammatory effects by suppressing NF-κB-driven TNF-α (already mapped) and IL-23 (already mapped) production; oxytocin receptor on osteoblasts promotes cortical bone (already mapped) formation, countering the ankylosing structural damage.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — AS vasopressin: vasopressin V1A receptors on entheseal cells modulate pain sensitisation and inflammation in ankylosing spondylitis; AVP signalling intersects NF-κB (already mapped) and IL-17A (already mapped) driven pro-inflammatory cascades in axial spondyloarthritis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — AS selenium: selenium-dependent GPX antioxidant activity counters the oxidative stress driving NF-κB (already mapped) and TNF-α (already mapped) mediated entheseal inflammation and bone-marrow (already mapped) osteoproliferation in ankylosing spondylitis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — AS iodine: iodine-dependent thyroid hormones modulate NF-κB (already mapped) and IL-17A (already mapped) entheseal inflammation in ankylosing spondylitis; hypothyroidism (autoimmune-thyroid comorbidity) amplifies musculoskeletal pain and the osteoproliferative structural damage.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — AS sodium: excess sodium promotes macrophage (already mapped) and t-helper-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-17A (already mapped) amplify TNF-α (already mapped) and IL-6 (already mapped) osteoproliferative cascade of AS.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — AS magnesium: magnesium, as cofactor for osteoblast (already mapped) mineralisation, supports bone formation; magnesium deficiency amplifies osteoclast (already mapped) RANKL and NF-κB (already mapped) and TNF-α (already mapped) osteoproliferative structural damage cascade of AS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — AS potassium: potassium regulates macrophage (already mapped) and osteoblast (already mapped) membrane function; potassium dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) and IL-6 (already mapped) cascade in AS.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — AS zinc: zinc cofactors macrophage (already mapped) anti-inflammatory function and osteoblast (already mapped) mineralisation; zinc deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade in AS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — AS copper: copper, via SOD in macrophages (already mapped) and osteoblasts (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-17A (already mapped) and NLRP3 (already mapped) and TNF-α (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on macrophages (already mapped) and osteoblasts (already mapped) regulate intracellular pH; chloride dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in macrophages (already mapped) and osteoblasts (already mapped) promotes cytoprotection; sulfur deficiency amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in macrophages (already mapped) and osteoblasts (already mapped) modulates bone turnover; nitrogen excess amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) and TNF-α (already mapped) spondylitic cascade in AS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — AS carbon: carbon, as metabolic backbone of collagen and osteoproliferative cytokines in osteoblasts (already mapped) and macrophages (already mapped), drives entheseal remodelling; carbon dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) in AS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — AS hydrogen: hydrogen, via redox homeostasis in osteoblasts (already mapped) and macrophages (already mapped), quenches ROS-driven entheseal damage; hydrogen dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) cascade in AS.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — AS oxygen: mitochondrial oxygen in osteoblasts (already mapped) and macrophages (already mapped) sustains ATP for bone remodelling; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — AS PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates entheseal immune homeostasis; PD-1 dysregulation amplifies NLRP3 (already mapped) and NF-κB (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — AS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and osteoblasts (already mapped) modulates metabolic bone homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade in AS.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — AS angiotensin-II: angiotensin-II in macrophages (already mapped) and osteoblasts (already mapped) promotes entheseal inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of ankylosing spondylitis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — AS IL-2: IL-2 in t-helper-cell (already mapped) and macrophages (already mapped) modulates entheseal immune tolerance; IL-2 dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — AS fibronectin: fibronectin in macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal extracellular matrix; fibronectin dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade in AS.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — AS notch: Notch in macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal cell fate; Notch dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade in AS.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — AS igf-1: IGF-1 from macrophages (already mapped) and osteoblasts (already mapped) promotes entheseal bone formation; IGF-1 excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) osteoproliferative cascade of AS.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — AS activin-a: activin-A from macrophages (already mapped) and osteoblasts (already mapped) regulates entheseal immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — AS calcitonin: calcitonin from macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — AS insulin-receptor: insulin receptor on macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal metabolic axis; insulin-receptor dysregulation amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — AS aldosterone: aldosterone from macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal fluid balance; aldosterone excess amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — AS androgen-receptor: androgen receptor on macrophages (already mapped) and osteoblasts (already mapped) modulates entheseal sex tone; androgen-receptor loss amplifies NF-κB (already mapped) and NLRP3 (already mapped) and IL-17A (already mapped) cascade of AS.

[^sieper-2015-ankylosing-spondylitis-review]: Sieper J, Poddubnyy D. Ankylosing spondylitis. *Lancet.* 2017;390(10089):73-84. [doi:10.1016/S0140-6736(16)31591-4](https://doi.org/10.1016/S0140-6736(16)31591-4) · [PubMed 28110981](https://pubmed.ncbi.nlm.nih.gov/28110981/)
[^baeten-2015-secukinumab-as]: Baeten D, Sieper J, Braun J, et al. Secukinumab, an Interleukin-17A Inhibitor, in Ankylosing Spondylitis. *N Engl J Med.* 2015;373(26):2534-2548. [doi:10.1056/NEJMoa1505066](https://doi.org/10.1056/NEJMoa1505066) · [PubMed 26699169](https://pubmed.ncbi.nlm.nih.gov/26699169/)
[^van-der-heijde-2018-adalimumab-as]: van der Heijde D, Ramiro S, Landewé R, et al. 2016 update of the ASAS-EULAR management recommendations for axial spondyloarthritis. *Ann Rheum Dis.* 2017;76(6):978-991. [doi:10.1136/annrheumdis-2016-210770](https://doi.org/10.1136/annrheumdis-2016-210770) · [PubMed 28087505](https://pubmed.ncbi.nlm.nih.gov/28087505/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
