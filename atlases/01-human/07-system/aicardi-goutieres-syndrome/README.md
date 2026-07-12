---
schema: human-scale-entry/v1
id: aicardi-goutieres-syndrome
name: Aicardi-Goutières Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Aicardi-Goutières syndrome (AGS) is a genetic interferonopathy caused by LOF mutations in nucleic acid metabolism genes (TREX1, RNASEH2A/B/C, SAMHD1, ADAR1, IFIH1) → cytosolic nucleic acid accumulation → cGAS-STING activation → chronic IFN-α/β → progressive encephalopathy."
aliases: ["AGS", "Aicardi-Goutieres syndrome", "Cree encephalitis", "pseudo-TORCH syndrome", "interferonopathy", "TREX1 deficiency", "RNASEH2 deficiency", "SAMHD1 deficiency", "ADAR1 deficiency", "IFIH1 deficiency", "familial chilblain lupus"]
sources:
  - id: crow-2015-ags-phenotype
    type: peer-reviewed
    cite: "Crow YJ, Chase DS, Lowenstein Schmidt J, et al. Characterization of human disease phenotypes associated with mutations in TREX1, RNASEH2A, RNASEH2B, RNASEH2C, SAMHD1, ADAR, and IFIH1. Am J Med Genet A. 2015;167A(2):296-312."
    doi: "10.1002/ajmg.a.36887"
    pmid: "25604658"
    url: "https://doi.org/10.1002/ajmg.a.36887"
    accessed: "2026-06-08"
  - id: crow-2014-ags-review
    type: peer-reviewed
    cite: "Crow YJ. Aicardi-Goutières syndrome. Handb Clin Neurol. 2013;113:1629-1635."
    doi: "10.1016/B978-0-444-59565-2.00031-9"
    pmid: "23622387"
    url: "https://doi.org/10.1016/B978-0-444-59565-2.00031-9"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING is the central effector of AGS: undigested nucleic acids (TREX1/RNASEH2 substrates) activate cytosolic cGAS → cGAMP → STING → TBK1 → IRF3 → IFN-β; SAMHD1 dNTPase and ADAR1 A-to-I editing prevent inappropriate cGAS-STING activation by self-nucleic acids."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "TREX1 LOF mutations cause both AGS and familial SLE — demonstrating that the same cGAS-STING pathway underlies both monogenic (AGS) and polygenic (SLE) interferonopathies; ANA and anti-dsDNA occur in TREX1 mutation carriers; type I IFN signature drives both diseases."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "AGS is a chronic interferonopathy: dysfunctional nucleases → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; ISG score (blood interferon-stimulated gene signature) is elevated; reverse transcriptase inhibitors reduce IFN-α."
  - target: 01-human/06-organ/microcephaly
    relation: connects-to
    note: "AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "STING → TBK1 activates both IRF3 (IFN-β) and IKKβ/NF-κB; chronic NF-κB in AGS drives TNF-α/IL-6 from microglia independent of IFN; NF-κB upregulation amplifies neuroinflammation; baricitinib (JAK1/2 inhibitor) reduces ISG and NF-κB-driven inflammation in AGS."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "In Aicardi-Goutières syndrome the chronic type I interferon flooding the brain activates microglia, which attack neurons and cerebral vessels — producing the progressive encephalopathy, white-matter disease, and basal-ganglia calcification of AGS."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Aicardi-Goutières syndrome is driven by type I interferon through the IFNAR-JAK-STAT pathway, so JAK1/2 inhibitors like baricitinib are the leading treatment: they lower the interferon signature and can stabilize disease, but rarely reverse established neurological damage."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AGS is fundamentally a brain disease: constitutive interferon causes an inflammatory encephalopathy with intracranial calcifications and acquired microcephaly that mimics congenital TORCH infection — but with sterile CSF lymphocytosis and high CSF interferon-α."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "AGS and dermatomyositis are both type I interferonopathies: AGS is a monogenic constitutive activation of nucleic-acid sensing (cGAS-STING/RIG-I), DM an acquired interferon signature; both show high interferon scores and chilblain-like lesions, and both respond to JAK inhibition."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin reveals Aicardi-Goutières syndrome: chronic type I interferon drives chilblain lesions—painful red-purple acral swellings on fingers, toes and ears that worsen in cold—mirroring chilblain lupus; these signs reflect the interferon vasculopathy that also injures the brain."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes are central to Aicardi-Goutières brain disease: they are a major source of the excess intracerebral type I interferon, and interferon-driven microangiopathy drives the basal-ganglia calcification and white-matter loss that mimic congenital infection."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Aicardi-Goutières syndrome injures neurons through chronic interferon: misprocessed self-nucleic acids drive a type-I-interferon response that damages the developing brain, causing basal-ganglia calcification and an encephalopathy that mimics TORCH infection."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells amplify Aicardi-Goutières syndrome: defective nucleic-acid sensors let self-DNA/RNA accumulate and trigger pDCs to pour out type I interferon—the same axis overactive in lupus, making AGS a monogenic interferonopathy."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Aicardi-Goutières syndrome and Sjögren's both run on a type-I-interferon signature: AGS is the monogenic, infantile extreme of interferon-driven disease, while Sjögren's is its acquired adult counterpart—one cytokine pathway across rare genetic and common illness."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Aicardi-Goutières syndrome and multiple sclerosis sit at opposite ends of the type-I-interferon story: AGS is a genetic interferonopathy where excess interferon damages the brain, while MS is treated with interferon-β—pathogenic in AGS, therapeutic in MS."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "STAT1 carries the interferon signal driving Aicardi-Goutières syndrome: defective nucleic-acid sensing triggers chronic type-I interferon, which signals through JAK-STAT1 to inflame the brain—so JAK inhibitors blocking this pathway are emerging therapy."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Aicardi-Goutières syndrome presents as an early encephalopathy with seizures: interferon-driven inflammation, basal-ganglia calcification and white-matter injury cause developmental regression and epilepsy in infancy—mimicking congenital infection."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "One AGS subtype is a disease of MAVS signaling: gain-of-function in the MDA5 sensor (IFIH1) makes it misread the body's own RNA, firing MAVS-driven type I interferon—so AGS is a Mendelian interferonopathy mimicking congenital infection."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "AGS is fundamentally an interferon assault on the developing nervous system: chronic intrathecal type I interferon causes a leukodystrophy with brain calcification, white-matter loss and severe encephalopathy, mimicking a TORCH congenital infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "AGS is a prototype autoinflammatory interferonopathy: inherited defects in nucleic-acid metabolism trip innate immune sensors to overproduce interferon against self, so it overlaps with lupus and is now treated by damping that pathway with JAK inhibitors."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Brain calcium deposits are an AGS hallmark: chronic type-I interferon inflammation calcifies the basal ganglia and white matter, so CT shows intracranial calcifications that—alongside CSF changes—help distinguish this genetic interferonopathy from congenital infection."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "AGS keeps the brain's immune effectors switched on: persistent interferon recruits cytotoxic T cells and lymphocytes into the CSF, producing a chronic sterile lymphocytosis that mimics a never-ending viral encephalitis—inflammation aimed at the body's own nucleic acids."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "AGS is the antiviral defense misfiring without a virus: the same type-I interferon program that fights infections like West Nile is chronically triggered by the patient's own DNA/RNA, so AGS resembles a congenital infection that never actually occurred."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Aicardi-Goutieres is a type I interferonopathy of nucleic-acid sensing: defective clearance of self DNA/RNA lets sensors like RIG-I (and cGAS-STING) fire, flooding the brain with interferon as if fighting a chronic virus that isn't there."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "AGS reflects broken immune tolerance to self nucleic acids: the relentless interferon and autoimmunity (overlapping lupus) point to failed regulation, and regulatory T cells that should restrain anti-self responses are part of the disturbed balance."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "AGS mimics congenital infection beyond the brain: hepatosplenomegaly, hepatitis and elevated liver enzymes accompany the interferon surge, so the liver shows the systemic reach of this interferonopathy that imitates a TORCH infection."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "AGS is a leukodystrophy that wounds the myelin-makers: chronic type I interferon and microglial activation injure oligodendrocytes, so the white matter fails to myelinate and breaks down, producing the diffuse leukodystrophy seen on MRI."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "AGS's brain calcifications are mineral deposits: in the basal ganglia and deep white matter, calcium combines with phosphate to form the calcifications seen on CT, a hallmark that with the interferon signature sets AGS apart from acquired infection."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "AGS can drop the platelet count: in the neonatal form thrombocytopenia accompanies the interferon surge alongside hepatosplenomegaly, part of the picture that mimics a congenital TORCH infection at birth."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Some AGS damages the blood-vessel endothelium: SAMHD1-type disease causes a cerebral vasculopathy with stenoses and aneurysms, so the interferon attack on endothelial cells can bring strokes on top of the encephalopathy."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Newborn AGS can swell the liver and spleen: alongside the interferon surge, hepatosplenomegaly, thrombocytopenia, and rash make the neonatal form mimic a congenital TORCH infection, sending the search for a microbe that is not there."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "AGS may injure the brain at its synapses: chronic interferon activates microglia that prune synapses during development, so the antiviral response misfiring on the body's own nucleic acids disturbs how the young brain wires itself."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "AGS is recognized on brain imaging: CT photons reveal its hallmark basal-ganglia calcifications, while MRI shows the white-matter disease and brain atrophy that mimic a congenital infection."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Neonatal AGS can suppress the bone marrow: thrombocytopenia and anemia accompany the interferon surge, part of the picture that makes the newborn form look like a congenital TORCH infection."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "AGS can reach the eyes: congenital glaucoma and other ocular problems are recognized, adding to the brain, skin and systemic features of this interferon-driven disorder."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "AGS is a failure to clear the cell's own genetic debris: the mutated nucleases let stray DNA and RNA pile up in the cytoplasm, where sensors mistake them for a virus and switch on a relentless type-I-interferon alarm."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Some AGS genotypes scar the heart and great vessels: SAMHD1 mutations in particular bring a cerebral and cardiac vasculopathy of aneurysms and stenoses, extending the inflammatory damage to the circulation."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "AGS shades into lupus, kidney and all: its overlap with systemic lupus means some patients develop a lupus-like glomerulonephritis, the shared interferon excess attacking the kidney's filters."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "AGS blurs into autoimmunity: its chronic type-I-interferon excess — the same signature as lupus — drives autoantibodies including ANA, so many patients carry a lupus-like serology alongside the neurologic disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "AGS masquerades as a congenital infection: newborns can present with thrombocytopenia and anemia alongside the brain calcification, a TORCH-mimic picture of cytopenias that misleads toward an infection that is not there."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The liver joins the pseudo-infection picture: AGS infants often show hepatomegaly and raised transaminases from hepatocyte involvement, part of the systemic interferon storm that imitates congenital cytomegalovirus."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The motor toll is severe: AGS leaves children with profound spasticity, dystonia, and contractures from the damaged motor pathways, a fixed motor disability that dominates the chronic phase after the early encephalopathy."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "The interferon storm drives autoimmunity: chronic type-I-interferon overactivation pushes B cells to make autoantibodies, so AGS overlaps with lupus and can show the antinuclear antibodies and chilblains of an interferon-driven autoimmune disease."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Autoimmune thyroid disease keeps company: the sustained interferon signature of AGS predisposes to autoimmune hypothyroidism, one of the endocrine autoimmunities that can accumulate in these interferonopathy patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Interferon-stoked macrophages help wreck the brain: activated alongside microglia, they pour out inflammatory mediators that injure white matter and feed the calcification of the basal ganglia seen in AGS."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "AGS shares its interferon fingerprint with scleroderma: both carry a strong type-I-interferon signature and the chilblains and Raynaud-like vascular skin changes, placing them on the broad interferonopathy spectrum."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Beyond interferon, IL-6 stokes the neuroinflammation: it rises in the spinal fluid of AGS alongside the interferon signature, adding to the chronic brain inflammation that damages the developing nervous system."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "The disease is a sensor stuck on: accumulated self nucleic acids that the broken enzymes fail to clear trip the innate sensors, and IRF3 drives the relentless type I interferon that defines this interferonopathy."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It can scar the brain's arteries: some forms, especially SAMHD1-related, cause a cerebral large-vessel vasculopathy with aneurysms and moyamoya-like narrowing, putting affected children at risk of stroke."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Skin cells reveal the signature: the chilblain lesions and the diagnostic interferon signature both surface in fibroblasts, where the unchecked nucleic-acid sensing drives local interferon production."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "More than interferon inflames the brain: alongside the dominant type I interferon, TNF and other inflammatory cytokines are elevated in AGS, adding to the neuroinflammation that damages the developing white matter."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "A second interferon joins the assault: beyond the type I interferon signature, IFN-γ is also raised in AGS, broadening the interferon-driven inflammation that scars the brain and triggers chilblains."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "It masquerades as congenital infection: the neonatal AGS picture of irritability, fever, CSF pleocytosis and brain calcification mimics intrauterine infection and sepsis, so the diagnosis is often reached only after an exhaustive infection workup is negative."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The interferon vasculopathy reaches the lungs: like other type I interferonopathies, AGS can damage the pulmonary vasculature, and pulmonary arterial hypertension is a recognized severe systemic manifestation."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its lupus-overlap can scar the kidney: AGS sits on the interferonopathy-lupus spectrum and can feature an immune-complex glomerulonephritis that, over time, threatens chronic kidney disease."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic interferon inflammation blunts the marrow: the relentless type I interferon signature of AGS, alongside its thrombocytopenia and cytopenias, can suppress erythropoiesis into an anemia of chronic disease."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its JAK-inhibitor therapy opens the door to mold: baricitinib and other JAK inhibitors used to dampen the interferon signature of AGS suppress immunity, raising the risk of invasive infections such as aspergillosis."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Its interferon excess can attack the islets: as a type I interferonopathy with autoimmune features, AGS shares the interferon-driven mechanisms that destroy pancreatic beta cells in type 1 diabetes."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its brain injury leaves the body in pain: the spasticity, dystonia and painful chilblains of AGS, on top of damaged sensory pathways, produce chronic neuropathic and nociceptive pain that is hard to control."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its interferon excess inflames the skin: AGS characteristically causes painful chilblain lesions on the fingers, toes and ears, a cutaneous hallmark shared with the type I interferonopathies and lupus."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It swells the liver and disrupts feeding: AGS can mimic congenital infection with hepatosplenomegaly and deranged liver function, and its severe encephalopathy causes dysphagia needing gastrostomy feeding."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Severe neurodisability endangers the lungs: the bulbar dysfunction and immobility of AGS lead to recurrent aspiration and chest infections, a leading cause of respiratory morbidity and death."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its interferon state damages vessels: SAMHD1-related AGS causes a systemic vasculopathy with intracranial large-vessel disease, aneurysms and a moyamoya-like arteriopathy that can cause stroke."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Chronic interferon fosters autoimmune endocrinopathy: AGS is associated with autoimmune thyroid disease and the type 1 diabetes its interferon signature shares with other interferonopathies."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The newborn form mimics congenital infection: AGS can present at birth with hepatosplenomegaly, thrombocytopenia and raised liver enzymes — a 'TORCH-negative' picture from sterile interferon-driven inflammation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its interferon autoimmunity can hit the kidney: AGS overlaps systemic lupus, and the resulting immune-complex nephritis can damage the kidney alongside its chilblain and CNS features."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It declares itself before or at birth: AGS presents in the newborn mimicking an in-utero infection, raising prenatal diagnosis and genetic-counselling questions for affected families."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "It is the classic 'TORCH-negative' mimic: AGS reproduces the intracranial calcification and white-matter disease of congenital toxoplasmosis and CMV without any infection, from sterile interferon excess."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A shared interferon axis: severe COVID-19 turns on — or, through autoantibodies, blocks — the same type I interferon pathway that runs unchecked in AGS, showing how dysregulated interferon drives disease in both directions."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Interferon arms the neutrophil: chronic type I interferon in AGS primes neutrophils toward NET formation, contributing to the small-vessel vasculopathy and tissue damage characteristic of interferonopathies."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: connects-to
    note: "An emerging infectious mimic: congenital Zika syndrome, recognised since 2015, joins the older TORCH infections as a brain-injuring newborn condition that must now be excluded before AGS is diagnosed."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibitors quiet the interferon: because AGS is driven by excess type I interferon signalling, JAK inhibitors like baricitinib that block the JAK-STAT pathway reduce the interferon signature and can improve skin and systemic disease."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "It mimics congenital CMV: AGS is a 'pseudo-TORCH' whose intracranial calcifications, CSF lymphocytosis and white-matter disease imitate congenital cytomegalovirus, the herpesvirus that is its central diagnostic differential."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Some forms attack the arteries: SAMHD1-related AGS causes a cerebral large-vessel vasculopathy with arterial-wall disease, aneurysms and moyamoya-like stenoses, adding stroke risk to the leukodystrophy."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "An SLE-like kidney overlap: as a monogenic type-I-interferonopathy that mimics lupus, Aicardi-Goutières (especially SAMHD1) can deposit immune complexes in the glomerulus, causing a lupus-like nephritis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It mimics congenital infection in the liver: neonatal Aicardi-Goutières causes hepatosplenomegaly and a hepatitis with raised transaminases that imitate congenital CMV or toxoplasmosis, inflaming the hepatic lobule."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "A shared type-I-interferon signature: Aicardi-Goutières is the prototype interferonopathy with constitutive type-I-IFN, the same plasmacytoid-dendritic-cell IFN axis that helps initiate psoriasis—linking a brain disease to a skin one."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "JAK inhibition across diseases: the JAK inhibitors (baricitinib) that calm the type-I-interferon storm of Aicardi-Goutières also treat rheumatoid arthritis, a pharmacologic bridge from a monogenic to a common autoimmune disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Innate disease, adaptive autoantibodies: though driven by innate type-I-interferon, Aicardi-Goutières often shows lupus-like autoantibodies arising from germinal-centre B-cell activation, blurring innate and adaptive autoimmunity."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Interferon reaches the skeleton: the related interferonopathy SPENCD (spondyloenchondrodysplasia) couples an AGS-like type-I-IFN signature with metaphyseal and vertebral lesions of cortical bone, tying innate immunity to the skeleton."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "A genetic leukodystrophy: chronic type-I interferon in Aicardi-Goutières damages cerebral white matter and the oligodendrocytes that myelinate it, disrupting the myelinated axons and their transport across the developing brain."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "One gene, two diseases: SAMHD1, an Aicardi-Goutières gene, is also a recurrently mutated tumour suppressor in chronic lymphocytic leukaemia, so the same DNA-metabolism enzyme links an interferonopathy to a B-cell cancer."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Interferon in neurodegeneration: as a pure type-I-interferonopathy of the brain driven by cGAS-STING sensing of self-DNA, Aicardi-Goutières informs the emerging role of the same innate-immune pathway in Alzheimer's neuroinflammation."
  - target: 01-human/03-molecular/tbk1
    relation: connects-to
    note: "Interferon switch: TBK1 sits downstream of the cGAS-STING and RIG-I sensors that are dysregulated in Aicardi-Goutières, phosphorylating IRF3 to drive the chronic type-I interferon production that defines the disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammatory amplification: the chronic innate-immune activation of Aicardi-Goutières recruits microglia that release IL-1β, adding to the inflammatory injury of the developing brain."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Nucleic-acid-driven inflammasome: the self-DNA and self-RNA that accumulate in Aicardi-Goutières can also engage the NLRP3 inflammasome, broadening the innate response beyond the interferon axis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Interferon-induced chemokine: the sustained type I interferon of Aicardi-Goutières drives CCL2 that recruits monocytes and lymphocytes into the brain, contributing to the white-matter injury and calcification."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic neuroinflammation: CD8 T cells activated by the chronic interferon milieu use perforin-mediated cytotoxicity within the Aicardi-Goutières brain, adding adaptive injury to the innate-driven damage."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Defective nucleic-acid clearance: autophagy normally degrades cytosolic DNA and damaged organelles that activate cGAS-STING, so impaired autophagic clearance amplifies the self-nucleic-acid sensing central to Aicardi-Goutières."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Interferon neurotoxicity: chronic type I interferon is directly toxic to neurons and oligodendrocytes, driving caspase-3-mediated apoptosis that underlies the progressive microcephaly and white-matter loss of Aicardi-Goutières."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Cerebral vasculopathy: the interferon-driven small-vessel disease of Aicardi-Goutières — especially SAMHD1-related cerebral vasculopathy and aneurysms — involves dysregulated VEGF-dependent angiogenesis in the brain."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Autoimmune bridging: sustained type I interferon upregulates MHC class II and primes adaptive autoimmunity, consistent with the chilblain lupus and SLE-overlap features that accompany Aicardi-Goutières."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Intracranial calcification: bilateral basal-ganglia and white-matter calcification is a radiological hallmark of Aicardi-Goutières, calcium deposition in the chronically interferon-inflamed brain that helps distinguish it from acquired congenital infection."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Lupus overlap: the sustained type-I-interferon state of Aicardi-Goutières drives complement activation and the chilblain-lupus and SLE-overlap autoimmunity that mark the disorder as a monogenic interferonopathy bridging to lupus."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Inflammatory amplification: S100A8/A9 released by activated myeloid cells in the interferon-driven inflammation of Aicardi-Goutières feeds the chronic neuroinflammation injuring the developing brain."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Autophagy regulation: mTOR restrains the autophagy (already mapped) that clears endogenous nucleic acids, and insufficient clearance in Aicardi-Goutières lets self-DNA/RNA accumulate and feed the cytosolic sensors driving the interferon response."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT transmission: alongside the STAT1 already mapped, JAK-STAT3 signalling transmits the chronic type-I interferon stimulus of Aicardi-Goutières syndrome, part of the axis blocked therapeutically by JAK inhibitors."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Excitotoxic injury: excitotoxic glutamate signalling contributes to the neuronal injury and seizures of Aicardi-Goutières syndrome, compounding the interferon-driven neurodegeneration of the developing brain."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Neuronal apoptosis: type-I-interferon-driven apoptosis of neurons and glia (caspase-3 mapped), set against anti-apoptotic BCL-2, contributes to the progressive encephalopathy of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR nucleic-acid sensing: endosomal TLRs sensing the accumulated nucleic acids of AGS signal through MyD88 to NF-κB (mapped), adding to the cGAS-STING/RIG-I-driven interferon response (both mapped)."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Interferon vasculopathy: the type-I-interferon vasculopathy of AGS — chilblains and cerebral small-vessel disease with calcification — involves endothelial dysfunction with dysregulated endothelin signalling."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 is induced by the chronic type-I-interferon milieu, amplifying the reactive microgliosis that drives the neuroinflammatory brain injury of AGS."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling shapes the survival and inflammatory responses of neurons and glia exposed to the sustained interferon and cytokine environment of AGS."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling transduces the interferon/cytokine milieu (IFN-γ mapped) into the glial inflammatory activation underlying AGS encephalopathy."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF signalling in pericytes and vascular smooth muscle contributes to the cerebral microangiopathy and intracranial calcification characteristic of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in the developing brain shapes the neurodevelopmental trajectory disrupted by the chronic interferon toxicity of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling modulates the cerebral vascular and glial responses that shape the leukodystrophy of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates neuronal and glial oxidative-stress responses to the chronic type-I interferon milieu of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses in the inflamed, calcifying CNS tissue contribute to the neurovascular pathology of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement activation through C5 amplifies the neuroinflammatory tissue damage of Aicardi-Goutières syndrome (complement C3 already mapped)."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the interferon-driven immune cells of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the immune-cell activation of the type-I-interferon-driven neuroinflammation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, coupled to autophagy (autophagy already mapped), participates in the clearance of the endogenous nucleic acids whose accumulation drives the interferonopathy of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation and the broader epigenetic control of interferon-stimulated genes shape the interferon signature of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the neuroinflammation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling participates in the cellular stress and apoptosis responses to the chronic interferon activation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and interferon-driven neuroinflammation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10-mediated immunoregulation participates in the balance of the chronic interferon-driven inflammation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory response of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the interferon-driven gene programs of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell and immune activation of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Vasculopathy: the small-vessel inflammatory vasculopathy of Aicardi-Goutières, which causes chilblain skin lesions and cerebral vascular changes, involves endothelial dysfunction with impaired nitric-oxide signalling (endothelin-1 already mapped)."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Lupus-like autoantibodies: many patients with Aicardi-Goutières develop antinuclear and other IgG autoantibodies, reflecting the shared type I interferon signature (already mapped) that links this monogenic interferonopathy to systemic lupus."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Encephalopathy: the chronic type I interferon-driven neuroinflammation of Aicardi-Goutières damages white matter and neurons, and loss of neurotrophic BDNF support contributes to the developmental regression and progressive encephalopathy."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative injury: reactive oxygen species from xanthine oxidase and other sources add oxidative stress to the type I interferon-driven neuroinflammation (already mapped) that damages the developing brain in Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 amplification: IL-12 driving interferon-gamma (already mapped) production adds a type-1 inflammatory arm to the dominant type I interferon signature, amplifying the immune dysregulation of this monogenic interferonopathy."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Neonatal presentation: the congenital-infection-mimicking form of Aicardi-Goutières presents with thrombocytopenia, anaemia lowering haemoglobin and hepatosplenomegaly (liver already mapped), the haematological picture of the systemic interferonopathy."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the interferon-activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) of the Aicardi-Goutières encephalopathy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Basal-ganglia mineralisation: iron, alongside the calcium (already mapped), deposits in the basal ganglia and white matter of Aicardi-Goutières, part of the mineralising vascular and tissue injury of the chronic interferonopathy."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-1/type-2 balance: IL-4 and the type-2 response counter the dominant type-1 interferon and Th1 (IL-12 already mapped) signature of Aicardi-Goutières, and the imbalance toward type-1 immunity shapes the severity of the interferonopathy."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine arm: IL-13, with IL-4 (already mapped), forms the type-2 response that counters the dominant type-I interferon signature of Aicardi-Goutières, the balance between the two shaping the severity of the interferonopathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that injures the neurons (already mapped) of the Aicardi-Goutières encephalopathy, a neuroprotective ion."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and nucleic-acid metabolism: zinc is a cofactor of many nucleases and antiviral proteins, and its role in the nucleic-acid sensing (cGAS-STING already mapped) and metabolism disrupted in Aicardi-Goutières links it to the interferonopathy."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis and vasculopathy: TGF-β and its SMAD4 (already mapped) signalling shape the tissue response and the small-vessel vasculopathy (PDGF and endothelin already mapped) of the interferon-injured brain in Aicardi-Goutières."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Autoimmune B cells: BAFF supports the B cells (already mapped) that produce the autoantibodies (immunoglobulin already mapped) of the SLE-like autoimmunity that accompanies the interferonopathy of Aicardi-Goutières."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell dysregulation: IL-2 signalling in the regulatory T cells (already mapped) is part of the immune dysregulation of the type-I interferonopathy (already mapped) of Aicardi-Goutières."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Interferonopathy-autoimmune overlap: Aicardi-Goutières, like systemic lupus (already mapped) and neuromyelitis optica, features the type-I interferon (already mapped) and autoimmune (BAFF already mapped) dysregulation."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu of the type-I interferonopathy (already mapped) of Aicardi-Goutières."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of Aicardi-Goutières."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of the type-I interferonopathy (already mapped) of Aicardi-Goutières."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Interferon-activated NK: the NK cells (perforin already mapped), activated by the chronic type-I interferon (already mapped), contribute to the immune dysregulation of Aicardi-Goutières."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of Aicardi-Goutières."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation complementing the type-I interferon (already mapped) drive of Aicardi-Goutières."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Aicardi-Goutières."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immune dysregulation driven by the chronic interferon (already mapped) of Aicardi-Goutières."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the innate inflammatory dimension of the interferon-driven (already mapped) immune dysregulation of Aicardi-Goutières."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral/autoimmune arm: the plasma cells secrete the antibodies (already mapped), including the autoantibodies of the lupus-overlap (SLE already mapped) that accompanies the type-I interferonopathy of Aicardi-Goutières."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Tissue mast cells: the mast cells contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension of the immune dysregulation of Aicardi-Goutières."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement activation accompanying the type-I interferonopathy and lupus-overlap (SLE already mapped) of Aicardi-Goutières."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the autoantibody immune complexes (immunoglobulin already mapped) of the lupus-overlap of Aicardi-Goutières."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "CNS iron: transferrin, the iron carrier, reflects the disordered iron handling of the basal-ganglia mineralisation and the CNS injury of Aicardi-Goutières."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-IFN axis: TSLP, from inflamed skin (already mapped) and mucosa, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the type-I-interferon (already mapped) and cGAS-STING (already mapped) neuroinflammation of Aicardi-Goutières."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-vascular axis: bradykinin, generated by the contact system activated during the complement (C3, C5, C5aR1 and factor H already mapped) and innate-immune activation of Aicardi-Goutières, augments vascular permeability and amplifies the CNS oedema of the disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective signal: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the progressive neurodegeneration driven by the type-I-interferon (already mapped) burden of Aicardi-Goutières."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell CNS effector: histamine, released by mast cells (already mapped) in the neuroinflamed CNS of AGS, amplifies blood-brain-barrier disruption and the leukocyte infiltration that compounds the type-I-interferon (already mapped) mediated neurodegeneration of AGS."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Neuroinflammatory ECM remodelling: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) under the type-I-interferon (already mapped) burden of AGS, modulates the extracellular matrix of the white matter lesions of Aicardi-Goutières syndrome."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian neuroprotection: melatonin, via MT1/MT2 receptors on neurons (already mapped) and astrocytes (already mapped), scavenges ROS and suppresses the NLRP3-inflammasome and type-I-IFN (already mapped) amplification of the neuroinflammatory burden of Aicardi-Goutières."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "AGS testosterone: testosterone suppresses type-I interferon (already mapped) and cGAS-STING (already mapped) innate immune activation; androgens attenuate JAK1-2 (already mapped)/STAT1 (already mapped) neuroinflammation and microglia (already mapped) IFN-driven injury in AGS."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "AGS serotonin: serotonin, via 5-HT receptors on microglia (already mapped) and astrocyte (already mapped), modulates neuroinflammation; 5-HT also attenuates the type-I interferon (already mapped) and NF-κB (already mapped) IFN-driven injury of AGS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "AGS prolactin: prolactin, via PRLR/JAK1-2 (already mapped), amplifies STAT1 (already mapped) and type-I interferon (already mapped); prolactin drives B-cell (already mapped) autoreactive expansion and macrophage (already mapped) NF-κB (already mapped) neuroinflammation in AGS."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "AGS oxytocin: oxytocin, via OXTR on microglia (already mapped) and astrocytes (already mapped), attenuates cGAS-STING (already mapped) and type-I interferon (already mapped) neuroinflammation; oxytocin promotes regulatory T-cell (already mapped) tolerance in AGS."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AGS vasopressin: vasopressin modulates the NF-κB (already mapped) and STAT1 (already mapped) cytokine-driven encephalopathic state; vasopressin also interacts with the brain (already mapped) fluid and type-I interferon (already mapped) cerebrospinal-fluid dysregulation of AGS."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "AGS selenium: selenium-dependent GPx in neurons (already mapped) and astrocytes (already mapped) quenches ROS amplifying cGAS-STING (already mapped) and NF-κB (already mapped); selenium deficiency worsens the type-I IFN (already mapped) neuroinflammatory burden of AGS."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "AGS iodine: thyroid hormones regulate microglia (already mapped) and astrocyte (already mapped) neuroinflammatory activation; thyroid deficiency amplifies cGAS-STING (already mapped) and type-I IFN (already mapped) and NF-κB (already mapped) interferonopathy cascade of AGS."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "AGS sodium: sodium dysregulation in neurons (already mapped) and astrocytes (already mapped) amplifies ionic stress; osmotic disturbances worsen cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "AGS potassium: potassium regulates neuronal (already mapped) and microglial (already mapped) membrane excitability; potassium dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "AGS copper: copper, via ceruloplasmin and SOD in neurons (already mapped) and astrocytes (already mapped), quenches ROS amplifying cGAS-STING (already mapped); copper deficiency amplifies NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride via KCC2 on neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "H2S from sulfur-amino acids in neurons (already mapped) and astrocytes (already mapped) modulates GABA-inhibitory tone; sulfur deficiency amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in microglia (already mapped) and neurons (already mapped) modulates glutamate (already mapped) excitatory tone; nitrogen excess amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "AGS carbon: carbon backbone of nucleotides in neurons (already mapped) and microglia (already mapped) drives cGAS-STING (already mapped) ligand accumulation; carbon dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy of AGS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "AGS hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and astrocytes (already mapped), quenches ROS-driven cGAS-STING (already mapped) activation; hydrogen dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "AGS oxygen: mitochondrial oxygen in neurons (already mapped) and microglia (already mapped) sustains mtDNA integrity; hypoxia amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "AGS PD-1: PD-1 on microglia (already mapped) and T-cells (already mapped) modulates interferon-driven neuroinflammation; PD-1 dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "AGS GLP-1: GLP-1 receptor signalling in microglia (already mapped) and neurons (already mapped) modulates metabolic neuroinflammation; GLP-1 dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) and cGAS-STING (already mapped) cascade of AGS."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "AGS angiotensin-II: angiotensin-II signalling in microglia (already mapped) and neurons (already mapped) promotes neuroinflammation; angiotensin-II excess amplifies NF-κB (already mapped) and cGAS-STING (already mapped) and type-I interferon (already mapped) cascade of AGS."
---

# Aicardi-Goutières Syndrome

## Overview

**Aicardi-Goutières syndrome (AGS)** is a rare genetic interferonopathy — a progressive inflammatory encephalopathy caused by constitutional activation of the **cGAS-STING innate immune sensing pathway** due to inherited loss-of-function mutations in genes encoding nucleic acid metabolism enzymes. First described by Aicardi and Goutières in 1984 as a "pseudo-TORCH" syndrome (resembling congenital infection but with negative viral cultures), AGS is now recognized as the founding member of the **type I interferonopathies** — a group of genetic disorders characterized by chronic, constitutive type I interferon production.

AGS affects approximately 1 in 100,000 individuals, with equal sex distribution. Most cases present in infancy or early childhood with progressive neurological deterioration, though later-onset presentations are recognized. The molecular mechanism — undigested nucleic acid substrates accumulating in the cytosol → activating cGAS-STING → chronic IFN-α/β production — directly links AGS to acquired autoimmune diseases (particularly SLE), providing fundamental insights into how self-nucleic acids trigger autoimmunity.

## Structure

### Genetic architecture (7 causal genes)

| Gene | Product | Function | % AGS cases |
|------|---------|----------|-------------|
| RNASEH2B | RNase H2 subunit B | Degrades RNA:DNA hybrids; removes ribonucleotides from genomic DNA | ~36% |
| TREX1 | DNase III (3′→5′ exonuclease) | Degrades cytosolic ssDNA and dsDNA from apoptosis, retroelements | ~25% |
| RNASEH2A | RNase H2 subunit A (catalytic) | Ribonucleotide excision repair | ~10% |
| RNASEH2C | RNase H2 subunit C | Structural | ~10% |
| SAMHD1 | dNTP triphosphohydrolase | Depletes dNTP pool; restricts HIV-1 reverse transcription | ~7% |
| ADAR1 | Adenosine deaminase RNA-specific | A-to-I editing of dsRNA → prevents MDA5/cGAS recognition | ~6% |
| IFIH1 (MDA5) | Innate RNA helicase | *Gain-of-function* mutations → hyperactive MDA5 sensing | ~4% |

**Inheritance**: Most genes cause AR (autosomal recessive) AGS; TREX1, ADAR1, and IFIH1 can also cause AD (autosomal dominant) disease via haploinsufficiency or gain-of-function.

### Molecular substrates and cGAS-STING activation

Each gene loss leads to accumulation of specific nucleic acid substrates that activate cGAS-STING or RIG-I/MDA5:
- **TREX1 deficiency**: Accumulation of cytosolic ssDNA/dsDNA from: (1) aberrant processing of DNA replication intermediates; (2) L1 retrotransposon reverse-transcribed cDNA → cGAS activation
- **RNASEH2 deficiency**: Ribonucleotides misincorporated during replication are not removed → RNA:DNA hybrid accumulation → genome instability → cytosolic DNA → cGAS
- **SAMHD1 deficiency**: Elevated dNTP pool → enhanced reverse transcription of LINE-1 elements → L1 cDNA → cGAS; also restricts HIV-1 in non-dividing cells
- **ADAR1 deficiency**: Unedited endogenous dsRNA (Alu/SINE inverted repeats) → MDA5/RIG-I activation → type I IFN (downstream of cGAS-STING-independent pathway)
- **IFIH1 (MDA5) GOF**: Constitutively active MDA5 → MAVS → IRF3 → IFN-β without ligand stimulus

## Function

The AGS genes collectively function as the **nucleic acid surveillance system** that prevents inappropriate innate immune activation by endogenous nucleic acids:

1. **Nuclease degradation**: TREX1 and RNASEH2 complex remove DNA/RNA:DNA hybrids before they reach the cytosol
2. **dNTP regulation**: SAMHD1 depletes the dNTP pool needed for reverse transcription of retrotransposons
3. **Nucleic acid camouflage**: ADAR1 A-to-I editing changes dsRNA structure → prevents MDA5 recognition
4. **Signaling threshold**: Together, these enzymes maintain cytosolic nucleic acid concentrations below the threshold for cGAS/MDA5 activation

When any one of these checkpoints fails (by mutation), the threshold is breached → cGAS-STING/MDA5 activation → chronic type I IFN production → progressive neurovascular inflammation.

## Pathology

### Clinical presentation

**Typical AGS (infantile onset; RNASEH2B, TREX1 mutations)**:
- Normal at birth; developmental regression at 4 months to 1 year
- **Irritability**, poor feeding, fever-like episodes without infection
- **Progressive microcephaly**, spastic quadriplegia, dystonia
- **Intracranial calcifications**: Basal ganglia and deep white matter (bilateral, symmetric; on CT — classic "salt-and-pepper" appearance; present in ~80% of AGS cases)
- **White matter abnormalities**: Periventricular and subcortical (MRI: T2-FLAIR signal abnormality)
- **CSF lymphocytosis**: 10–50 cells/μL (lymphocytes > 5/μL in >80% early AGS); CSF IFN-α elevated >2 IU/mL (diagnostic threshold)
- **Chilblain lesions**: Acral skin lesions (fingers, toes, ears) from vasculopathy; particularly TREX1, SAMHD1 mutations

**Attenuated/late-onset AGS (IFIH1 GOF, ADAR1)**:
- Spastic diplegia, intellectual disability without rapid regression
- Systemic lupus-like features (arthritis, malar rash, ANA) 
- Aicardi-Goutières syndrome / Singleton-Merten overlap syndrome (IFIH1 GOF: dental dysplasia, aortic calcification)

### Laboratory findings

- **ISG score (interferon-stimulated gene signature)**: Elevated in peripheral blood; panel of 6 ISGs (MX1, IFI44L, IFI27, RSAD2, SIGLEC1, IFIT1) scoring > 2.466 in AGS; used for diagnosis and treatment monitoring
- **CSF IFN-α**: >2 IU/mL diagnostic; available in reference labs; elevated in ~70% of cases (higher early)
- **ANA, anti-dsDNA**: Positive in ~25% (particularly TREX1 mutations) — AGS-SLE overlap
- **Low platelets, lymphopenia**: ~20% of cases (systemic immune activation)

### Treatment

**No disease-modifying therapy is FDA-approved** for AGS. Active areas:

| Strategy | Rationale | Status |
|----------|-----------|--------|
| Reverse transcriptase inhibitors (RTIs): abacavir + zidovudine + lamivudine (AZA) | TREX1-deficient cells have excess L1 reverse transcripts → RTIs block L1 cDNA generation → less cGAS substrate | Phase II (PROTECT trial; Crow lab) — ISG score reduced; functional benefit modest |
| JAK inhibitors (ruxolitinib, baricitinib) | Block downstream IFNAR-JAK1/TYK2-STAT1/2 signaling → suppress ISG expression | Case series positive; Phase II ongoing in LIBERATE trial |
| STING inhibitors (H-151, SN-011) | Block STING directly → prevent IFN-β induction | Preclinical only |
| Anti-IFNAR1 (anifrolumab) | Block type I IFN receptor → suppress all IFN-α/β effects | Investigational; compassionate use cases reported |

**Supportive care**: Spasticity management (baclofen, botulinum toxin), anticonvulsants for seizures, enteral nutrition for failure-to-thrive, speech and physiotherapy, chilblain wound care.

### Prognosis

Severe early-onset AGS (TREX1 homozygous, RNASEH2A): death in childhood from respiratory failure or aspiration; most surviving patients have severe disability. Attenuated IFIH1/ADAR1 phenotypes may have near-normal lifespan with moderate disability. RTI trials show stabilization of ISG scores with limited functional recovery — suggesting early intervention (neonatal screening?) may be needed.

## Connections

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: cGAS-STING is the central effector of AGS: undigested nucleic acids (TREX1/RNASEH2 substrates) activate cytosolic cGAS → cGAMP → STING → TBK1 → IRF3 → IFN-β; SAMHD1 dNTPase and ADAR1 A-to-I editing prevent inappropriate cGAS-STING activation by self-nucleic acids.

**→ [Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/)**: TREX1 LOF mutations cause both AGS and familial SLE — demonstrating that the same cGAS-STING pathway underlies both monogenic (AGS) and polygenic (SLE) interferonopathies; ANA and anti-dsDNA occur in TREX1 mutation carriers; type I IFN signature drives both diseases.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: AGS is a chronic interferonopathy: dysfunctional nucleases → nucleic acid accumulation → cGAS-STING → constitutive IFN-α/β; CSF IFN-α >2 IU/mL is diagnostic; ISG score (blood interferon-stimulated gene signature) is elevated; reverse transcriptase inhibitors reduce IFN-α.

**→ [Microcephaly](../../../06-organ/microcephaly/)**: AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging.

**→ [HIV-1](../../../../02-pathogen/01-viruses/hiv-1/)**: SAMHD1 (AGS gene) is the principal HIV-1 restriction factor: dNTP hydrolase depletes viral dNTP pool → inhibits reverse transcription; HIV-2/SIVsm Vpx degrades SAMHD1; SAMHD1-LOF in AGS links innate antiviral immunity to monogenic neuroinflammation.

**→ [NF-κB](../../../03-molecular/nf-kb/)**: STING → TBK1 activates both IRF3 (IFN-β) and IKKβ/NF-κB; chronic NF-κB in AGS drives TNF-α/IL-6 from microglia independent of IFN; NF-κB upregulation amplifies neuroinflammation; baricitinib (JAK1/2 inhibitor) reduces ISG and NF-κB-driven inflammation in AGS.

- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — In Aicardi-Goutières syndrome the chronic type I interferon flooding the brain activates microglia, which attack neurons and cerebral vessels — producing the progressive encephalopathy, white-matter disease, and basal-ganglia calcification of AGS.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Aicardi-Goutières syndrome is driven by type I interferon through the IFNAR-JAK-STAT pathway, so JAK1/2 inhibitors like baricitinib are the leading treatment: they lower the interferon signature and can stabilize disease, but rarely reverse established neurological damage.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AGS is fundamentally a brain disease: constitutive interferon causes an inflammatory encephalopathy with intracranial calcifications and acquired microcephaly that mimics congenital TORCH infection — but with sterile CSF lymphocytosis and high CSF interferon-α.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — AGS and dermatomyositis are both type I interferonopathies: AGS is a monogenic constitutive activation of nucleic-acid sensing (cGAS-STING/RIG-I), DM an acquired interferon signature; both show high interferon scores and chilblain-like lesions, and both respond to JAK inhibition.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin reveals Aicardi-Goutières syndrome: chronic type I interferon drives chilblain lesions—painful red-purple acral swellings on fingers, toes and ears that worsen in cold—mirroring chilblain lupus; these signs reflect the interferon vasculopathy that also injures the brain.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes are central to Aicardi-Goutières brain disease: they are a major source of the excess intracerebral type I interferon, and interferon-driven microangiopathy drives the basal-ganglia calcification and white-matter loss that mimic congenital infection.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Aicardi-Goutières syndrome injures neurons through chronic interferon: misprocessed self-nucleic acids drive a type-I-interferon response that damages the developing brain, causing basal-ganglia calcification and an encephalopathy that mimics TORCH infection.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells amplify Aicardi-Goutières syndrome: defective nucleic-acid sensors let self-DNA/RNA accumulate and trigger pDCs to pour out type I interferon—the same axis overactive in lupus, making AGS a monogenic interferonopathy.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Aicardi-Goutières syndrome and Sjögren's both run on a type-I-interferon signature: AGS is the monogenic, infantile extreme of interferon-driven disease, while Sjögren's is its acquired adult counterpart—one cytokine pathway across rare genetic and common illness.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Aicardi-Goutières syndrome and multiple sclerosis sit at opposite ends of the type-I-interferon story: AGS is a genetic interferonopathy where excess interferon damages the brain, while MS is treated with interferon-β—pathogenic in AGS, therapeutic in MS.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — STAT1 carries the interferon signal driving Aicardi-Goutières syndrome: defective nucleic-acid sensing triggers chronic type-I interferon, which signals through JAK-STAT1 to inflame the brain—so JAK inhibitors blocking this pathway are emerging therapy.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Aicardi-Goutières syndrome presents as an early encephalopathy with seizures: interferon-driven inflammation, basal-ganglia calcification and white-matter injury cause developmental regression and epilepsy in infancy—mimicking congenital infection.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — One AGS subtype is a disease of MAVS signaling: gain-of-function in the MDA5 sensor (IFIH1) makes it misread the body's own RNA, firing MAVS-driven type I interferon—so AGS is a Mendelian interferonopathy mimicking congenital infection.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — AGS is fundamentally an interferon assault on the developing nervous system: chronic intrathecal type I interferon causes a leukodystrophy with brain calcification, white-matter loss and severe encephalopathy, mimicking a TORCH congenital infection.
- `connects-to` → **[Immune System](../immune-system/README.md)** — AGS is a prototype autoinflammatory interferonopathy: inherited defects in nucleic-acid metabolism trip innate immune sensors to overproduce interferon against self, so it overlaps with lupus and is now treated by damping that pathway with JAK inhibitors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Brain calcium deposits are an AGS hallmark: chronic type-I interferon inflammation calcifies the basal ganglia and white matter, so CT shows intracranial calcifications that—alongside CSF changes—help distinguish this genetic interferonopathy from congenital infection.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — AGS keeps the brain's immune effectors switched on: persistent interferon recruits cytotoxic T cells and lymphocytes into the CSF, producing a chronic sterile lymphocytosis that mimics a never-ending viral encephalitis—inflammation aimed at the body's own nucleic acids.
- `connects-to` → **[West Nile Virus](../west-nile-virus/README.md)** — AGS is the antiviral defense misfiring without a virus: the same type-I interferon program that fights infections like West Nile is chronically triggered by the patient's own DNA/RNA, so AGS resembles a congenital infection that never actually occurred.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — Aicardi-Goutieres is a type I interferonopathy of nucleic-acid sensing: defective clearance of self DNA/RNA lets sensors like RIG-I (and cGAS-STING) fire, flooding the brain with interferon as if fighting a chronic virus that isn't there.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — AGS reflects broken immune tolerance to self nucleic acids: the relentless interferon and autoimmunity (overlapping lupus) point to failed regulation, and regulatory T cells that should restrain anti-self responses are part of the disturbed balance.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — AGS mimics congenital infection beyond the brain: hepatosplenomegaly, hepatitis and elevated liver enzymes accompany the interferon surge, so the liver shows the systemic reach of this interferonopathy that imitates a TORCH infection.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — AGS is a leukodystrophy that wounds the myelin-makers: chronic type I interferon and microglial activation injure oligodendrocytes, so the white matter fails to myelinate and breaks down, producing the diffuse leukodystrophy seen on MRI.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — AGS's brain calcifications are mineral deposits: in the basal ganglia and deep white matter, calcium combines with phosphate to form the calcifications seen on CT, a hallmark that with the interferon signature sets AGS apart from acquired infection.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — AGS can drop the platelet count: in the neonatal form thrombocytopenia accompanies the interferon surge alongside hepatosplenomegaly, part of the picture that mimics a congenital TORCH infection at birth.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Some AGS damages the blood-vessel endothelium: SAMHD1-type disease causes a cerebral vasculopathy with stenoses and aneurysms, so the interferon attack on endothelial cells can bring strokes on top of the encephalopathy.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Newborn AGS can swell the liver and spleen: alongside the interferon surge, hepatosplenomegaly, thrombocytopenia, and rash make the neonatal form mimic a congenital TORCH infection, sending the search for a microbe that is not there.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — AGS may injure the brain at its synapses: chronic interferon activates microglia that prune synapses during development, so the antiviral response misfiring on the body's own nucleic acids disturbs how the young brain wires itself.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — AGS is recognized on brain imaging: CT photons reveal its hallmark basal-ganglia calcifications, while MRI shows the white-matter disease and brain atrophy that mimic a congenital infection.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Neonatal AGS can suppress the bone marrow: thrombocytopenia and anemia accompany the interferon surge, part of the picture that makes the newborn form look like a congenital TORCH infection.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — AGS can reach the eyes: congenital glaucoma and other ocular problems are recognized, adding to the brain, skin and systemic features of this interferon-driven disorder.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — AGS is a failure to clear the cell's own genetic debris: the mutated nucleases let stray DNA and RNA pile up in the cytoplasm, where sensors mistake them for a virus and switch on a relentless type-I-interferon alarm.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Some AGS genotypes scar the heart and great vessels: SAMHD1 mutations in particular bring a cerebral and cardiac vasculopathy of aneurysms and stenoses, extending the inflammatory damage to the circulation.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — AGS shades into lupus, kidney and all: its overlap with systemic lupus means some patients develop a lupus-like glomerulonephritis, the shared interferon excess attacking the kidney's filters.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — AGS blurs into autoimmunity: its chronic type-I-interferon excess — the same signature as lupus — drives autoantibodies including ANA, so many patients carry a lupus-like serology alongside the neurologic disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — AGS masquerades as a congenital infection: newborns can present with thrombocytopenia and anemia alongside the brain calcification, a TORCH-mimic picture of cytopenias that misleads toward an infection that is not there.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The liver joins the pseudo-infection picture: AGS infants often show hepatomegaly and raised transaminases from hepatocyte involvement, part of the systemic interferon storm that imitates congenital cytomegalovirus.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The motor toll is severe: AGS leaves children with profound spasticity, dystonia, and contractures from the damaged motor pathways, a fixed motor disability that dominates the chronic phase after the early encephalopathy.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — The interferon storm drives autoimmunity: chronic type-I-interferon overactivation pushes B cells to make autoantibodies, so AGS overlaps with lupus and can show the antinuclear antibodies and chilblains of an interferon-driven autoimmune disease.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Autoimmune thyroid disease keeps company: the sustained interferon signature of AGS predisposes to autoimmune hypothyroidism, one of the endocrine autoimmunities that can accumulate in these interferonopathy patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Interferon-stoked macrophages help wreck the brain: activated alongside microglia, they pour out inflammatory mediators that injure white matter and feed the calcification of the basal ganglia seen in AGS.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — AGS shares its interferon fingerprint with scleroderma: both carry a strong type-I-interferon signature and the chilblains and Raynaud-like vascular skin changes, placing them on the broad interferonopathy spectrum.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Beyond interferon, IL-6 stokes the neuroinflammation: it rises in the spinal fluid of AGS alongside the interferon signature, adding to the chronic brain inflammation that damages the developing nervous system.
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — The disease is a sensor stuck on: accumulated self nucleic acids that the broken enzymes fail to clear trip the innate sensors, and IRF3 drives the relentless type I interferon that defines this interferonopathy.
- `connects-to` → **[Stroke](../stroke/README.md)** — It can scar the brain's arteries: some forms, especially SAMHD1-related, cause a cerebral large-vessel vasculopathy with aneurysms and moyamoya-like narrowing, putting affected children at risk of stroke.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Skin cells reveal the signature: the chilblain lesions and the diagnostic interferon signature both surface in fibroblasts, where the unchecked nucleic-acid sensing drives local interferon production.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — More than interferon inflames the brain: alongside the dominant type I interferon, TNF and other inflammatory cytokines are elevated in AGS, adding to the neuroinflammation that damages the developing white matter.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — A second interferon joins the assault: beyond the type I interferon signature, IFN-γ is also raised in AGS, broadening the interferon-driven inflammation that scars the brain and triggers chilblains.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — It masquerades as congenital infection: the neonatal AGS picture of irritability, fever, CSF pleocytosis and brain calcification mimics intrauterine infection and sepsis, so the diagnosis is often reached only after an exhaustive infection workup is negative.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The interferon vasculopathy reaches the lungs: like other type I interferonopathies, AGS can damage the pulmonary vasculature, and pulmonary arterial hypertension is a recognized severe systemic manifestation.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its lupus-overlap can scar the kidney: AGS sits on the interferonopathy-lupus spectrum and can feature an immune-complex glomerulonephritis that, over time, threatens chronic kidney disease.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic interferon inflammation blunts the marrow: the relentless type I interferon signature of AGS, alongside its thrombocytopenia and cytopenias, can suppress erythropoiesis into an anemia of chronic disease.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its JAK-inhibitor therapy opens the door to mold: baricitinib and other JAK inhibitors used to dampen the interferon signature of AGS suppress immunity, raising the risk of invasive infections such as aspergillosis.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Its interferon excess can attack the islets: as a type I interferonopathy with autoimmune features, AGS shares the interferon-driven mechanisms that destroy pancreatic beta cells in type 1 diabetes.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its brain injury leaves the body in pain: the spasticity, dystonia and painful chilblains of AGS, on top of damaged sensory pathways, produce chronic neuropathic and nociceptive pain that is hard to control.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its interferon excess inflames the skin: AGS characteristically causes painful chilblain lesions on the fingers, toes and ears, a cutaneous hallmark shared with the type I interferonopathies and lupus.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It swells the liver and disrupts feeding: AGS can mimic congenital infection with hepatosplenomegaly and deranged liver function, and its severe encephalopathy causes dysphagia needing gastrostomy feeding.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Severe neurodisability endangers the lungs: the bulbar dysfunction and immobility of AGS lead to recurrent aspiration and chest infections, a leading cause of respiratory morbidity and death.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its interferon state damages vessels: SAMHD1-related AGS causes a systemic vasculopathy with intracranial large-vessel disease, aneurysms and a moyamoya-like arteriopathy that can cause stroke.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Chronic interferon fosters autoimmune endocrinopathy: AGS is associated with autoimmune thyroid disease and the type 1 diabetes its interferon signature shares with other interferonopathies.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The newborn form mimics congenital infection: AGS can present at birth with hepatosplenomegaly, thrombocytopenia and raised liver enzymes — a 'TORCH-negative' picture from sterile interferon-driven inflammation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its interferon autoimmunity can hit the kidney: AGS overlaps systemic lupus, and the resulting immune-complex nephritis can damage the kidney alongside its chilblain and CNS features.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It declares itself before or at birth: AGS presents in the newborn mimicking an in-utero infection, raising prenatal diagnosis and genetic-counselling questions for affected families.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — It is the classic 'TORCH-negative' mimic: AGS reproduces the intracranial calcification and white-matter disease of congenital toxoplasmosis and CMV without any infection, from sterile interferon excess.
- `connects-to` → **[COVID-19](../covid-19-disease/README.md)** — A shared interferon axis: severe COVID-19 turns on — or, through autoantibodies, blocks — the same type I interferon pathway that runs unchecked in AGS, showing how dysregulated interferon drives disease in both directions.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Interferon arms the neutrophil: chronic type I interferon in AGS primes neutrophils toward NET formation, contributing to the small-vessel vasculopathy and tissue damage characteristic of interferonopathies.
- `connects-to` → **[Zika Virus](../../../02-pathogen/01-viruses/zika-virus/README.md)** — An emerging infectious mimic: congenital Zika syndrome, recognised since 2015, joins the older TORCH infections as a brain-injuring newborn condition that must now be excluded before AGS is diagnosed.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibitors quiet the interferon: because AGS is driven by excess type I interferon signalling, JAK inhibitors like baricitinib that block the JAK-STAT pathway reduce the interferon signature and can improve skin and systemic disease.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — It mimics congenital CMV: AGS is a 'pseudo-TORCH' whose intracranial calcifications, CSF lymphocytosis and white-matter disease imitate congenital cytomegalovirus, the herpesvirus that is its central diagnostic differential.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Some forms attack the arteries: SAMHD1-related AGS causes a cerebral large-vessel vasculopathy with arterial-wall disease, aneurysms and moyamoya-like stenoses, adding stroke risk to the leukodystrophy.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — An SLE-like kidney overlap: as a monogenic type-I-interferonopathy that mimics lupus, Aicardi-Goutières (especially SAMHD1) can deposit immune complexes in the glomerulus, causing a lupus-like nephritis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It mimics congenital infection in the liver: neonatal Aicardi-Goutières causes hepatosplenomegaly and a hepatitis with raised transaminases that imitate congenital CMV or toxoplasmosis, inflaming the hepatic lobule.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — A shared type-I-interferon signature: Aicardi-Goutières is the prototype interferonopathy with constitutive type-I-IFN, the same plasmacytoid-dendritic-cell IFN axis that helps initiate psoriasis—linking a brain disease to a skin one.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — JAK inhibition across diseases: the JAK inhibitors (baricitinib) that calm the type-I-interferon storm of Aicardi-Goutières also treat rheumatoid arthritis, a pharmacologic bridge from a monogenic to a common autoimmune disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Innate disease, adaptive autoantibodies: though driven by innate type-I-interferon, Aicardi-Goutières often shows lupus-like autoantibodies arising from germinal-centre B-cell activation, blurring innate and adaptive autoimmunity.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Interferon reaches the skeleton: the related interferonopathy SPENCD (spondyloenchondrodysplasia) couples an AGS-like type-I-IFN signature with metaphyseal and vertebral lesions of cortical bone, tying innate immunity to the skeleton.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — A genetic leukodystrophy: chronic type-I interferon in Aicardi-Goutières damages cerebral white matter and the oligodendrocytes that myelinate it, disrupting the myelinated axons and their transport across the developing brain.
- `connects-to` → **[CLL](../cll/README.md)** — One gene, two diseases: SAMHD1, an Aicardi-Goutières gene, is also a recurrently mutated tumour suppressor in chronic lymphocytic leukaemia, so the same DNA-metabolism enzyme links an interferonopathy to a B-cell cancer.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Interferon in neurodegeneration: as a pure type-I-interferonopathy of the brain driven by cGAS-STING sensing of self-DNA, Aicardi-Goutières informs the emerging role of the same innate-immune pathway in Alzheimer's neuroinflammation.
- `connects-to` → **[TBK1](../../03-molecular/tbk1/README.md)** — Interferon switch: TBK1 sits downstream of the cGAS-STING and RIG-I sensors that are dysregulated in Aicardi-Goutières, phosphorylating IRF3 to drive the chronic type-I interferon production that defines the disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammatory amplification: the chronic innate-immune activation of Aicardi-Goutières recruits microglia that release IL-1β, adding to the inflammatory injury of the developing brain.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Nucleic-acid-driven inflammasome: the self-DNA and self-RNA that accumulate in Aicardi-Goutières can also engage the NLRP3 inflammasome, broadening the innate response beyond the interferon axis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Interferon-induced chemokine: the sustained type I interferon of Aicardi-Goutières drives CCL2 that recruits monocytes and lymphocytes into the brain, contributing to the white-matter injury and calcification.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic neuroinflammation: CD8 T cells activated by the chronic interferon milieu use perforin-mediated cytotoxicity within the Aicardi-Goutières brain, adding adaptive injury to the innate-driven damage.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Defective nucleic-acid clearance: autophagy normally degrades cytosolic DNA and damaged organelles that activate cGAS-STING, so impaired autophagic clearance amplifies the self-nucleic-acid sensing central to Aicardi-Goutières.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Chronic type I interferon is directly toxic to neurons and oligodendrocytes, driving caspase-3-mediated apoptosis that underlies the progressive microcephaly and white-matter loss defining the neurological devastation of Aicardi-Goutières.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The interferon-driven small-vessel disease of Aicardi-Goutières—especially the SAMHD1-related cerebral vasculopathy and intracranial aneurysms—involves dysregulated VEGF-dependent angiogenesis contributing to the characteristic intracranial calcification.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Sustained type I interferon upregulates MHC class II and primes adaptive autoimmunity, consistent with the chilblain lupus and systemic-lupus-overlap features that frequently accompany the interferonopathy of Aicardi-Goutières.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Bilateral basal-ganglia and white-matter calcification is a radiological hallmark of Aicardi-Goutières, calcium deposition in the chronically interferon-inflamed brain that helps distinguish it from acquired congenital infection.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The sustained type-I-interferon state of Aicardi-Goutières drives complement activation and the chilblain-lupus and SLE-overlap autoimmunity that mark the disorder as a monogenic interferonopathy bridging to lupus.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 released by activated myeloid cells in the interferon-driven inflammation of Aicardi-Goutières feeds the chronic neuroinflammation injuring the developing brain.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR restrains the autophagy (already mapped) that clears endogenous nucleic acids, and insufficient clearance in Aicardi-Goutières lets self-DNA/RNA accumulate and feed the cytosolic sensors driving the interferon response.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Alongside the STAT1 already mapped, JAK-STAT3 signaling transmits the chronic type-I interferon stimulus of Aicardi-Goutières syndrome, part of the axis blocked therapeutically by JAK inhibitors.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Excitotoxic glutamate signaling contributes to the neuronal injury and seizures of Aicardi-Goutières syndrome, compounding the interferon-driven neurodegeneration of the developing brain.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Type-I-interferon-driven apoptosis of neurons and glia (caspase-3 mapped), set against anti-apoptotic BCL-2, contributes to the progressive encephalopathy of Aicardi-Goutières syndrome.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Endosomal TLRs sensing the accumulated nucleic acids of AGS signal through MyD88 to NF-κB (mapped), adding to the cGAS-STING/RIG-I-driven interferon response (both mapped).
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — The type-I-interferon vasculopathy of AGS—chilblains and cerebral small-vessel disease with calcification—involves endothelial dysfunction with dysregulated endothelin signaling.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 is induced by the chronic type-I-interferon milieu, amplifying the reactive microgliosis that drives the neuroinflammatory brain injury of AGS.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling shapes the survival and inflammatory responses of neurons and glia exposed to the sustained interferon and cytokine environment of AGS.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the interferon/cytokine milieu (IFN-γ mapped) into the glial inflammatory activation underlying AGS encephalopathy.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling in pericytes and vascular smooth muscle contributes to the cerebral microangiopathy and intracranial calcification characteristic of Aicardi-Goutières syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in the developing brain shapes the neurodevelopmental trajectory disrupted by the chronic interferon toxicity of Aicardi-Goutières syndrome.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling modulates the cerebral vascular and glial responses that shape the leukodystrophy of Aicardi-Goutières syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates neuronal and glial oxidative-stress responses to the chronic type-I interferon milieu of Aicardi-Goutières syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses in the inflamed, calcifying CNS tissue contribute to the neurovascular pathology of Aicardi-Goutières syndrome.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation through C5 amplifies the neuroinflammatory tissue damage of Aicardi-Goutières syndrome (complement C3 already mapped).
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the interferon-driven immune cells of Aicardi-Goutières syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the immune-cell activation of the type-I-interferon-driven neuroinflammation of Aicardi-Goutières syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, coupled to autophagy (autophagy already mapped), participates in the clearance of the endogenous nucleic acids whose accumulation drives the interferonopathy of Aicardi-Goutières syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation and the broader epigenetic control of interferon-stimulated genes shape the interferon signature of Aicardi-Goutières syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the neuroinflammation of Aicardi-Goutières syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling participates in the cellular stress and apoptosis responses to the chronic interferon activation of Aicardi-Goutières syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and interferon-driven neuroinflammation of Aicardi-Goutières syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses of Aicardi-Goutières syndrome.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10-mediated immunoregulation participates in the balance of the chronic interferon-driven inflammation of Aicardi-Goutières syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory response of Aicardi-Goutières syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the interferon-driven gene programs of Aicardi-Goutières syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell and immune activation of Aicardi-Goutières syndrome.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Vasculopathy: the small-vessel inflammatory vasculopathy of Aicardi-Goutières, which causes chilblain skin lesions and cerebral vascular changes, involves endothelial dysfunction with impaired nitric-oxide signalling (endothelin-1 already mapped).
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Lupus-like autoantibodies: many patients with Aicardi-Goutières develop antinuclear and other IgG autoantibodies, reflecting the shared type I interferon signature (already mapped) that links this monogenic interferonopathy to systemic lupus.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Encephalopathy: the chronic type I interferon-driven neuroinflammation of Aicardi-Goutières damages white matter and neurons, and loss of neurotrophic BDNF support contributes to the developmental regression and progressive encephalopathy.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative injury: reactive oxygen species from xanthine oxidase and other sources add oxidative stress to the type I interferon-driven neuroinflammation (already mapped) that damages the developing brain in Aicardi-Goutières syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 amplification: IL-12 driving interferon-gamma (already mapped) production adds a type-1 inflammatory arm to the dominant type I interferon signature, amplifying the immune dysregulation of this monogenic interferonopathy.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Neonatal presentation: the congenital-infection-mimicking form of Aicardi-Goutières presents with thrombocytopenia, anaemia lowering haemoglobin and hepatosplenomegaly (liver already mapped), the haematological picture of the systemic interferonopathy.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the interferon-activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) of the Aicardi-Goutières encephalopathy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Basal-ganglia mineralisation: iron, alongside the calcium (already mapped), deposits in the basal ganglia and white matter of Aicardi-Goutières, part of the mineralising vascular and tissue injury of the chronic interferonopathy.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-1/type-2 balance: IL-4 and the type-2 response counter the dominant type-1 interferon and Th1 (IL-12 already mapped) signature of Aicardi-Goutières, and the imbalance toward type-1 immunity shapes the severity of the interferonopathy.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine arm: IL-13, with IL-4 (already mapped), forms the type-2 response that counters the dominant type-I interferon signature of Aicardi-Goutières, the balance between the two shaping the severity of the interferonopathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that injures the neurons (already mapped) of the Aicardi-Goutières encephalopathy, a neuroprotective ion.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and nucleic-acid metabolism: zinc is a cofactor of many nucleases and antiviral proteins, and its role in the nucleic-acid sensing (cGAS-STING already mapped) and metabolism disrupted in Aicardi-Goutières links it to the interferonopathy.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Fibrosis and vasculopathy: TGF-β and its SMAD4 (already mapped) signalling shape the tissue response and the small-vessel vasculopathy (PDGF and endothelin already mapped) of the interferon-injured brain in Aicardi-Goutières.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Autoimmune B cells: BAFF supports the B cells (already mapped) that produce the autoantibodies (immunoglobulin already mapped) of the SLE-like autoimmunity that accompanies the interferonopathy of Aicardi-Goutières.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell dysregulation: IL-2 signalling in the regulatory T cells (already mapped) is part of the immune dysregulation of the type-I interferonopathy (already mapped) of Aicardi-Goutières.
- `connects-to` → **[NMO](../nmo/README.md)** — Interferonopathy-autoimmune overlap: Aicardi-Goutières, like systemic lupus (already mapped) and neuromyelitis optica, features the type-I interferon (already mapped) and autoimmune (BAFF already mapped) dysregulation.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu of the type-I interferonopathy (already mapped) of Aicardi-Goutières.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of Aicardi-Goutières.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of the type-I interferonopathy (already mapped) of Aicardi-Goutières.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Interferon-activated NK: the NK cells (perforin already mapped), activated by the chronic type-I interferon (already mapped), contribute to the immune dysregulation of Aicardi-Goutières.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of Aicardi-Goutières.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune dysregulation complementing the type-I interferon (already mapped) drive of Aicardi-Goutières.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Aicardi-Goutières.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immune dysregulation driven by the chronic interferon (already mapped) of Aicardi-Goutières.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the innate inflammatory dimension of the interferon-driven (already mapped) immune dysregulation of Aicardi-Goutières.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral/autoimmune arm: the plasma cells secrete the antibodies (already mapped), including the autoantibodies of the lupus-overlap (SLE already mapped) that accompanies the type-I interferonopathy of Aicardi-Goutières.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Tissue mast cells: the mast cells contribute to the neuroinflammation and the type-2 (IgE already mapped) dimension of the immune dysregulation of Aicardi-Goutières.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement activation accompanying the type-I interferonopathy and lupus-overlap (SLE already mapped) of Aicardi-Goutières.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the autoantibody immune complexes (immunoglobulin already mapped) of the lupus-overlap of Aicardi-Goutières.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — CNS iron: transferrin, the iron carrier, reflects the disordered iron handling of the basal-ganglia mineralisation and the CNS injury of Aicardi-Goutières.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-IFN axis: TSLP, from inflamed skin (already mapped) and mucosa, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the type-I-interferon (already mapped) and cGAS-STING (already mapped) neuroinflammation of Aicardi-Goutières.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-vascular axis: bradykinin, generated by the contact system activated during the complement (C3, C5, C5aR1 and factor H already mapped) and innate-immune activation of Aicardi-Goutières, augments vascular permeability and amplifies the CNS oedema of the disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective signal: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), promotes neuronal survival and limits the progressive neurodegeneration driven by the type-I-interferon (already mapped) burden of Aicardi-Goutières.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell CNS effector: histamine, released by mast cells (already mapped) in the neuroinflamed CNS of AGS, amplifies blood-brain-barrier disruption and the leukocyte infiltration that compounds the type-I-interferon (already mapped) mediated neurodegeneration of AGS.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Neuroinflammatory ECM remodelling: periostin, expressed by astrocytes (already mapped) and microglia (already mapped) under the type-I-interferon (already mapped) burden of AGS, modulates the extracellular matrix of the white matter lesions of Aicardi-Goutières syndrome.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian neuroprotection: melatonin, via MT1/MT2 receptors on neurons (already mapped) and astrocytes (already mapped), scavenges ROS and suppresses the NLRP3-inflammasome and type-I-IFN (already mapped) amplification of the neuroinflammatory burden of Aicardi-Goutières.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen IFN suppression: testosterone suppresses type-I interferon (already mapped) and cGAS-STING (already mapped) innate immune activation; androgens attenuate JAK1-2 (already mapped)/STAT1 (already mapped) neuroinflammation and microglia (already mapped) IFN-driven injury in AGS.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Neuroimmune modulation: serotonin, via 5-HT receptors on microglia (already mapped) and astrocyte (already mapped), modulates neuroinflammation; 5-HT also attenuates the type-I interferon (already mapped) and NF-κB (already mapped) IFN-driven injury of AGS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — IFN-amplifying hormone: prolactin, via PRLR/JAK1-2 (already mapped), amplifies STAT1 (already mapped) and type-I interferon (already mapped); prolactin drives B-cell (already mapped) autoreactive expansion and macrophage (already mapped) NF-κB (already mapped) neuroinflammation in AGS.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — AGS oxytocin: oxytocin, via OXTR on microglia (already mapped) and astrocytes (already mapped), attenuates cGAS-STING (already mapped) and type-I interferon (already mapped) neuroinflammation; oxytocin promotes regulatory T-cell (already mapped) tolerance in AGS.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — AGS vasopressin: vasopressin modulates the NF-κB (already mapped) and STAT1 (already mapped) cytokine-driven encephalopathic state; vasopressin also interacts with the brain (already mapped) fluid and type-I interferon (already mapped) cerebrospinal-fluid dysregulation of AGS.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — AGS selenium: selenium-dependent GPx in neurons (already mapped) and astrocytes (already mapped) quenches ROS amplifying cGAS-STING (already mapped) and NF-κB (already mapped); selenium deficiency worsens the type-I IFN (already mapped) neuroinflammatory burden of AGS.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — AGS iodine: thyroid hormones regulate microglia (already mapped) and astrocyte (already mapped) neuroinflammatory activation; thyroid deficiency amplifies cGAS-STING (already mapped) and type-I IFN (already mapped) and NF-κB (already mapped) interferonopathy cascade of AGS.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — AGS sodium: sodium dysregulation in neurons (already mapped) and astrocytes (already mapped) amplifies ionic stress; osmotic disturbances worsen cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — AGS potassium: potassium regulates neuronal (already mapped) and microglial (already mapped) membrane excitability; potassium dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — AGS copper: copper, via ceruloplasmin and SOD in neurons (already mapped) and astrocytes (already mapped), quenches ROS amplifying cGAS-STING (already mapped); copper deficiency amplifies NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride via KCC2 on neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — H2S from sulfur-amino acids in neurons (already mapped) and astrocytes (already mapped) modulates GABA-inhibitory tone; sulfur deficiency amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in microglia (already mapped) and neurons (already mapped) modulates glutamate (already mapped) excitatory tone; nitrogen excess amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — AGS carbon: carbon backbone of nucleotides in neurons (already mapped) and microglia (already mapped) drives cGAS-STING (already mapped) ligand accumulation; carbon dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy of AGS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — AGS hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and astrocytes (already mapped), quenches ROS-driven cGAS-STING (already mapped) activation; hydrogen dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — AGS oxygen: mitochondrial oxygen in neurons (already mapped) and microglia (already mapped) sustains mtDNA integrity; hypoxia amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) interferonopathy cascade of AGS.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — AGS PD-1: PD-1 on microglia (already mapped) and T-cells (already mapped) modulates interferon-driven neuroinflammation; PD-1 dysregulation amplifies cGAS-STING (already mapped) and NF-κB (already mapped) and type-I interferon (already mapped) cascade of AGS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — AGS GLP-1: GLP-1 receptor signalling in microglia (already mapped) and neurons (already mapped) modulates metabolic neuroinflammation; GLP-1 dysregulation amplifies NF-κB (already mapped) and type-I interferon (already mapped) and cGAS-STING (already mapped) cascade of AGS.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — AGS angiotensin-II: angiotensin-II signalling in microglia (already mapped) and neurons (already mapped) promotes neuroinflammation; angiotensin-II excess amplifies NF-κB (already mapped) and cGAS-STING (already mapped) and type-I interferon (already mapped) cascade of AGS.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
