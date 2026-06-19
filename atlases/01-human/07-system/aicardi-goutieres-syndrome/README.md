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

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
