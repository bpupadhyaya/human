---
schema: human-scale-entry/v1
id: neurofibromatosis-type-1
name: Neurofibromatosis Type 1
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Neurofibromatosis type 1 (NF1) is caused by germline NF1 mutations; café-au-lait macules, neurofibromas, Lisch nodules, optic pathway gliomas; ~10% lifetime MPNST risk; 1/3000; selumetinib FDA-approved for NF1-associated plexiform neurofibromas in children (2020)."
aliases: ["NF1", "neurofibromatosis type 1", "von Recklinghausen disease", "NF1 syndrome", "NF1 germline", "NF1 plexiform neurofibroma", "NF1 MPNST", "neurofibromatosis cancer risk", "NF1 selumetinib"]
sources:
  - id: gutmann-2017-nf1-primer
    type: peer-reviewed
    cite: "Gutmann DH, Ferner RE, Listernick RH, et al. Neurofibromatosis type 1. Nat Rev Dis Primers. 2017;3:17004."
    doi: "10.1038/nrdp.2017.4"
    pmid: "28230061"
    url: "https://doi.org/10.1038/nrdp.2017.4"
  - id: dombi-2016-selumetinib
    type: peer-reviewed
    cite: "Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. N Engl J Med. 2016;375(26):2550-2560."
    doi: "10.1056/NEJMoa1605943"
    pmid: "28029918"
    url: "https://doi.org/10.1056/NEJMoa1605943"
cross_links:
  - target: 01-human/03-molecular/spred1
    relation: connects-to
    note: "Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "Neurofibromin (NF1) is a RAS-GAP; NF1 LOF → sustained RAS-GTP → MAPK/PI3K/mTOR activation → NF1 syndrome manifestations including neurofibromas, MPNST, optic gliomas; selumetinib (MEK1/2 inhibitor) FDA-approved for NF1-associated plexiform neurofibromas in children."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "NF1 LOF activates the same RAS-MAPK pathway as oncogenic KRAS mutations; both result in sustained RAS-GTP → MEK/ERK activation → proliferation; MEK inhibitors (selumetinib, trametinib) are active in NF1-deficient and KRAS-mutant tumors via the shared MAPK pathway."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "MPNST arises in ~10% of NF1 patients from plexiform neurofibromas; NF1-MPNST is more aggressive than sporadic MPNST; NF1 LOF → RAS-MAPK/CDK4 → malignant transformation; selumetinib shrinks plexiform precursors; surgical resection primary for overt MPNST."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "NF1 neurofibromas — cutaneous, subcutaneous, and plexiform — grow from Schwann cells of peripheral nerves after a somatic second hit knocks out the remaining NF1 allele; plexiform neurofibromas are the precursor lesion that can transform into MPNST in ~10-15%."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Neurofibroma growth depends on its microenvironment: NF1-haploinsufficient mast cells and fibroblasts secrete stem-cell factor (SCF/KIT ligand) that drives proliferation of the NF1-null Schwann cells — a paracrine loop explored therapeutically with imatinib (anti-KIT)."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "GIST occurs in ~3-5% of NF1 patients but is biologically distinct from sporadic GIST: NF1-associated GISTs are KIT/PDGFRA wild-type (driven instead by NF1 loss → RAS-MAPK), so they respond poorly to imatinib, with sunitinib or regorafenib used in later lines."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF1 and NF2 share a name and dominant inheritance but are unrelated diseases: NF1 (neurofibromin, a RAS-GAP) drives café-au-lait spots and neurofibromas, while NF2 (merlin, a Hippo regulator) drives bilateral vestibular schwannomas and meningiomas — different genes and pathways."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin shows NF1's earliest and most reliable signs: six or more café-au-lait macules and axillary/inguinal freckling appear in childhood, followed by cutaneous and plexiform neurofibromas; these criteria often establish the diagnosis before nerve or brain tumors appear."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The optic pathway glioma is NF1's signature brain tumor: a low-grade pilocytic astrocytoma of the optic nerve/chiasm in ~15% of children, often indolent but able to threaten vision; NF1 also raises risk of other gliomas, with MEK inhibitors (selumetinib) used for progression."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "NF1 predisposes to pheochromocytoma: loss of neurofibromin's RAS-GAP activity in adrenal-medullary chromaffin cells drives catecholamine-secreting tumors in ~1-5% of NF1 patients, so unexplained hypertension in NF1 warrants plasma metanephrine screening."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "NF1 and Noonan syndrome are both RASopathies—germline disorders of the RAS-MAPK pathway—and overlap clinically: a 'neurofibromatosis-Noonan' phenotype exists, with short stature, learning issues, and cardiac or pigmentary signs blurring the two."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Women with NF1 carry roughly double the breast cancer risk with worse outcomes, especially before age 50: neurofibromin loss disinhibits RAS-MAPK in breast epithelium, so NF1 guidelines recommend earlier, enhanced mammographic and MRI screening."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "NF1-associated and IDH-mutant gliomas are two distinct molecular routes to glioma: NF1's neurofibromin loss disinhibits Ras, driving optic-pathway gliomas, while sporadic adult gliomas are often IDH-mutant—Ras-pathway versus metabolic-epigenetic routes."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Rhabdomyosarcoma is part of the NF1 tumor spectrum: neurofibromin loss disinhibiting Ras predisposes children with NF1 to this skeletal-muscle sarcoma (often embryonal subtype), adding a soft-tissue cancer to NF1's neurofibromas, optic gliomas and MPNSTs."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "NF1 and Gorlin are both autosomal-dominant tumor-predisposition phakomatoses driven by loss of a single pathway brake: NF1's neurofibromin loss unleashes Ras, Gorlin's PTCH1 loss unleashes Hedgehog—two pathways, one syndromic logic."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neurofibromas grow on the nerves NF1 affects: loss of neurofibromin in Schwann-cell-lineage cells lets benign neurofibromas form along peripheral nerves enveloping their neurons, causing the skin nodules and plexiform tumors that define neurofibromatosis type 1."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "NF1 predisposes to gliomas from optic pathway to high-grade: neurofibromin normally restrains RAS, so its loss drives childhood optic pathway gliomas and, less often, glioblastoma—linking the syndrome's RAS-pathway defect to brain as well as nerve tumors."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye gives diagnostic clues to NF1: Lisch nodules (iris hamartomas) are a near-universal diagnostic criterion, and optic pathway gliomas threaten vision—so ophthalmologic exam is central to diagnosing and monitoring neurofibromatosis type 1."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "NF1 is fundamentally a tumor-prone disorder of the nervous system: loss of neurofibromin unleashes RAS in nerve-sheath cells, producing neurofibromas, optic gliomas and learning difficulties—so the nervous system bears both the benign tumors and the cognitive features."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin announces NF1: café-au-lait macules, axillary freckling and cutaneous neurofibromas are diagnostic criteria usually present from childhood, so the integumentary system gives the earliest and most accessible signs of the syndrome."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "NF1 also affects the skeleton: scoliosis, sphenoid-wing dysplasia and tibial pseudarthrosis (a non-healing congenital fracture) are recognized bony features, so the musculoskeletal system is part of this multisystem RAS-pathway disorder."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "NF1 is a treatable cause of secondary hypertension in the young: renal-artery stenosis from arterial dysplasia and catecholamine-secreting pheochromocytomas both raise blood pressure, so hypertension in an NF1 patient triggers a search for these causes."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "NF1's signature brain tumor is an astrocyte glioma: optic pathway and other low-grade pilocytic astrocytomas arise when neurofibromin loss unleashes RAS in glial cells, so children with NF1 are screened for vision-threatening optic gliomas."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF1 is a RASopathy driven through ERK: neurofibromin normally switches off RAS, so its loss leaves RAS-RAF-MEK-ERK signaling stuck on—the rationale for MEK inhibitors like selumetinib that shrink inoperable plexiform neurofibromas."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "NF1 loss feeds the mTOR growth engine: without neurofibromin's brake on RAS, the PI3K-AKT-mTOR arm runs high alongside the MAPK pathway, so mTOR inhibitors like sirolimus are tested to shrink plexiform neurofibromas."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "NF1 weakens bone through its osteoblasts: neurofibromin loss disrupts these bone-building cells, causing scoliosis, sphenoid-wing dysplasia, and the hard-to-heal tibial pseudarthrosis that are skeletal hallmarks of the syndrome."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "NF1's optic pathway gliomas can disturb growth hormone: tumors near the hypothalamus and pituitary derail the growth axis, causing precocious puberty or growth-hormone problems—why NF1 children need growth and endocrine monitoring."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Neurofibromas are built with macrophages: alongside the mast cells that drive their itch, macrophages make up much of the tumor and secrete factors that help the Schwann-cell tumors grow—a stromal target in this nerve disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "NF1 loss unleashes growth through AKT: without neurofibromin's brake on Ras, signaling pours into the PI3K-AKT-mTOR pathway as well as ERK, so AKT-mTOR inhibitors join MEK inhibitors as strategies against the tumors."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "NF1 predisposes to adrenal pheochromocytoma: loss of neurofibromin in adrenal medullary cells drives catecholamine-secreting tumors, so unexplained hypertension in NF1 prompts a hunt for a pheochromocytoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NF1's café-au-lait spots are painted with copper: the flat brown macules and skinfold freckling come from excess melanin, built by the copper-dependent enzyme tyrosinase in pigment cells."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "NF1 vasculopathy chokes the kidney's arteries: neurofibromin loss in vessel walls narrows the renal arteries, a cause of the hypertension that, with pheochromocytoma, must be sought in NF1."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "NF1 weakens the blood-vessel lining: loss of neurofibromin in endothelial and smooth-muscle cells drives a vasculopathy of stenoses and aneurysms, behind the strokes and renovascular disease of the syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons watch NF1 unfold: MRI tracks optic-pathway gliomas and plexiform neurofibromas, whole-body MRI gauges tumor burden, and slit-lamp light spots the Lisch nodules on the iris that help clinch the diagnosis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Neurofibromas are mixed tumors, and fibroblasts are part of the mix: alongside Schwann cells, perineurial cells, and mast cells, fibroblasts lay down the loose collagenous matrix that gives these soft, fleshy nodules their texture."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "NF1 can be born into the heart: like the related RASopathies, it raises the risk of congenital heart disease — pulmonary valve stenosis most of all — so children are screened for structural defects alongside their tumors."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy dissects the neurofibroma: it is a mix of Schwann cells, perineurial cells, fibroblasts, and mast cells loosely wrapped in collagen, the heterogeneous tangle that distinguishes it from a pure schwannoma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "NF1 distorts the growing skeleton: sphenoid-wing dysplasia, scoliosis, and the non-healing tibial pseudarthrosis reflect a bone-forming defect, warping the marrow-bearing bones from birth."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "NF1 can scar the lungs: a diffuse interstitial lung disease with basal fibrosis and upper-lobe bullae develops in some adults, adding pulmonary disease to the syndrome's tumors and skeletal changes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Biopsy reads the tumors by antibody: S100 and SOX10 stains confirm a neurofibroma's Schwann-cell origin, and as a benign lesion transforms toward MPNST the loss of H3K27me3 staining flags the dangerous change."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "NF1 reaches the bowel several ways: intestinal neurofibromas and ganglioneuromatosis stud the gut wall, and the syndrome's GISTs and periampullary neuroendocrine tumors can bleed or obstruct, making GI symptoms a reason to look harder."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "NF1 quietly weakens bone: patients run low on vitamin D with reduced bone mineral density and more fractures, an osteopenia that compounds the syndrome's scoliosis and dysplasia and is watched and supplemented in their care."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "NF1 is autosomal dominant with a striking twist: each child of a carrier has a 50% risk, yet about half of all cases are new de novo mutations, so genetic counseling and preimplantation options matter even in families with no prior history."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "The commonest NF1 complication is in the mind, not the nerves: learning disabilities and ADHD affect most children with the syndrome, as loss of neurofibromin's RAS control disturbs the signaling that underpins attention and learning."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Bone fails to knit in NF1: losing neurofibromin tips bone remodeling toward overactive osteoclast resorption, which underlies the non-healing pseudarthrosis of the tibia and the dysplasia and scoliosis that mark the skeleton."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "The same RAS overdrive reaches the blood: NF1 children have a strong predisposition to juvenile myelomonocytic leukemia, the pediatric cousin of CMML, because losing neurofibromin unleashes RAS signaling in myeloid progenitors just as it does in nerve sheath cells."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "NF1 is a disease of blood vessels too: neurofibromin loss weakens and narrows arteries into a vasculopathy, including moyamoya-like cerebral vessel disease, so children and adults face an elevated risk of stroke beyond their tumor burden."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "The brain wiring is affected from the start: beyond the learning difficulties and ADHD, a substantial share of children with NF1 meet criteria for autism spectrum disorder, reflecting how RAS-pathway signaling shapes synapse formation and cognition."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "NF1 brains spark seizures: cortical malformations, gliomas, and the disease's own neuronal effects make epilepsy more common in NF1 than the general population, adding to its neurological burden."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "A second hit turns a benign tumor deadly: CDKN2A loss is a key step when a plexiform neurofibroma transforms into MPNST, the malignant change that is the leading cause of death in NF1."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "The nerve tumors hurt: plexiform and spinal neurofibromas compress and infiltrate nerves, producing chronic neuropathic pain that is one of the most disabling everyday symptoms of NF1."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Loss of neurofibromin routes RAS into NF-κB: with the RAS brake gone, NF1 cells engage NF-κB-driven survival and inflammatory signaling among the pathways feeding their many tumors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A visible lifelong disease weighs on the mind: NF1's disfiguring tumors, pain and learning difficulties drive high rates of depression, part of the substantial psychosocial burden of the syndrome."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its vasculopathy and surgery raise clot risk: NF1 arteriopathy plus the major operations to debulk plexiform tumors predispose to venous thromboembolism alongside the disease's better-known arterial disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Loss of neurofibromin weakens the skeleton: NF1 disturbs bone remodeling, and patients show reduced bone mineral density, osteopenia, and an elevated fracture risk beyond the focal dysplasias and scoliosis."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its RAS overactivity tilts marrow toward leukemia: with neurofibromin lost, hyperactive RAS signaling predisposes NF1 children to juvenile myelomonocytic leukemia and other myeloid neoplasms that can evolve toward acute myeloid leukemia."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "NF1 loss is itself a melanoma driver: inactivating NF1 unleashes RAS-MAPK signaling, defining a recognized genomic subtype of cutaneous melanoma and adding to the cancer burden these patients carry."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "RAS dysregulation also seeds gut endocrine tumours: NF1 predisposes to duodenal/periampullary somatostatinomas and other gastroenteropancreatic neuroendocrine tumours, part of its wide neoplastic spectrum."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Debulking neurofibromas heals poorly: the highly vascular plexiform neurofibromas of NF1 bleed and recur, and their surgical resection leaves wounds prone to slow, complicated closure."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong cancer risk and disfigurement breed worry: the visible skin tumours, malignant-transformation surveillance and unpredictable course of NF1 foster chronic health anxiety alongside low mood."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "RAS dysregulation disturbs growth and glands: NF1 optic-pathway gliomas near the hypothalamus cause precocious puberty and growth-hormone problems, and NF1 predisposes to phaeochromocytoma and somatostatinoma."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It is a vasculopathy too: NF1 causes a distinctive arteriopathy with renal-artery stenosis driving hypertension, plus aneurysms and a moyamoya-like cerebral vasculopathy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Neurofibromas and tumours stud the gut: NF1 causes gastrointestinal neurofibromas that can bleed or obstruct, and predisposes to GIST and duodenal somatostatinoma along the digestive tract."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its vasculopathy narrows the renal artery: NF1 causes renal artery stenosis, a treatable cause of renovascular hypertension that is important to find in young patients with high blood pressure."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can scar the lungs and crowd the chest: NF1 is associated with a diffuse interstitial lung disease with bullae, and plexiform neurofibromas can involve the chest wall and airway."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mast cells feed its tumours and it predisposes to leukaemia: mast cells recruited into neurofibromas drive their growth and itch, and NF1 children have a raised risk of juvenile myelomonocytic leukaemia."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A MEK inhibitor shrinks its tumours: selumetinib, targeting the hyperactive RAS-MEK pathway of NF1, is approved to reduce inoperable plexiform neurofibromas in children."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A fellow neurocutaneous syndrome: like tuberous sclerosis, NF1 combines skin signs with nervous-system tumours in an autosomal-dominant pattern, both converging on mTOR-pathway dysregulation."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "A spectrum cousin: schwannomatosis joins NF1 and NF2 among the neurofibromatosis-spectrum disorders, all causing multiple nerve-sheath tumours from different genes."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for the cancers it breeds: NF1 predisposes to MPNST, juvenile myelomonocytic leukaemia, glioma and rhabdomyosarcoma, treated with chemotherapy when they arise."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It dysplastically shapes the skeleton: NF1 causes sphenoid-wing dysplasia, scoliosis, tibial pseudarthrosis and reduced cortical bone density, distinctive skeletal features of the disease."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "A fellow endocrine-tumour predisposition: like MEN1, NF1 raises the risk of phaeochromocytoma and duodenal neuroendocrine tumours, overlapping the inherited tumour-syndrome spectrum."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is also a vasculopathy: neurofibromin loss in vascular smooth muscle and endothelium causes an NF1 arteriopathy—renal-artery stenosis, aneurysms and moyamoya—an under-recognised cause of the hypertension and stroke that shorten NF1 lifespan."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "A RAS-pathway neural-crest tumour: NF1 loss removes a brake on RAS-MAPK in neural-crest cells, and NF1 modestly predisposes to neuroblastoma, the embryonal sympathetic-nervous-system cancer of childhood."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Two great childhood cancer-predisposition syndromes: NF1 (neurofibromin/RAS) and Li-Fraumeni (germline TP53) both commit children to lifelong tumour surveillance, predisposing to overlapping CNS tumours and sarcomas via different pathways."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Learning and cognition: NF1 causes learning disabilities, ADHD and autism features, as excess RAS-driven GABAergic signalling impairs hippocampal long-term potentiation and memory."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "NF1 gliomas: NF1 predisposes to optic-pathway and other childhood gliomas, some high-grade and midline, RAS-driven counterparts to the H3K27M-driven sporadic diffuse midline glioma."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "RASopathy cardiac involvement: NF1 carries congenital heart disease (pulmonary stenosis) and a vasculopathy, and dysregulated RAS signalling underlies the cardiomyopathies of the RASopathies it overlaps."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "The café-au-lait mimic: constitutional mismatch-repair deficiency (biallelic Lynch genes) produces café-au-lait macules and childhood cancers that closely imitate NF1, a critical distinction since the two demand entirely different surveillance."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Two phakomatoses, one shared tumour: NF1 and von Hippel-Lindau are both neurocutaneous tumour-suppressor syndromes that predispose to pheochromocytoma, though NF1 dysregulates RAS while VHL drives HIF and angiogenesis."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "The learning gene: neurofibromin restrains RAS at the synapse, and its loss raises GABAergic inhibition and impairs synaptic plasticity, underlying the learning disabilities and attention problems common in NF1."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "RAF down the cascade: NF1 loss unleashes RAS into the BRAF-MEK-ERK cascade, the pathway targeted by MEK inhibitors such as selumetinib for NF1 plexiform neurofibromas."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle in transformation: CDKN2A loss with CDK4/6 activation drives the malignant transformation of NF1 neurofibromas to MPNST and the growth of high-grade NF1 gliomas."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Tumour microenvironment: PDGF signalling promotes neurofibroma growth and recruits the supportive stroma around the Schwann-cell tumours of NF1."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "RAS-driven oncogene: unrestrained RAS signalling from NF1 loss upregulates MYC, driving the proliferation behind neurofibroma growth and malignant transformation."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Plexiform angiogenesis: VEGF drives the rich vascularisation of the plexiform neurofibromas of NF1, supporting their growth and the bleeding risk of these tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in growing NF1 tumours drives the angiogenesis and metabolic adaptation that accompany their transformation to MPNST."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell recruitment: KIT-driven mast cells recruited to NF1 neurofibromas secrete factors that promote Schwann-cell proliferation, a microenvironmental engine of neurofibroma growth."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Cognitive deficits: excess RAS signalling from neurofibromin loss raises GABA-mediated inhibition in the brain, the mechanism behind the learning disabilities common in NF1."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Bone dysplasia: NF1 loss dysregulates RANKL-driven osteoclast activity, contributing to the tibial pseudarthrosis, scoliosis and low bone density of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage-rich niche: NF1 neurofibromas are heavily infiltrated by CCL2-recruited macrophages whose growth factors sustain the Schwann-cell tumour, the inflammatory niche from which plexiform neurofibromas can progress to MPNST."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "MPNST spread: CXCR4-CXCL12 signalling drives the metastasis of the malignant peripheral nerve sheath tumours that arise from NF1 plexiform neurofibromas, the leading cause of NF1-related death."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurofibroma pain: substance P from the sensory nerve fibres entangled within plexiform neurofibromas mediates the chronic neurogenic pain that is a major source of morbidity in neurofibromatosis type 1."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Phaeochromocytoma: NF1 predisposes to adrenal phaeochromocytomas that secrete catecholamines including norepinephrine, a cause of secondary hypertension that should be excluded in an NF1 patient with paroxysmal symptoms."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Cognitive deficits: RAS-MAPK signalling is the effector arm of BDNF-TrkB synaptic plasticity, and its constitutive dysregulation in NF1 disrupts hippocampal learning, underlying the learning difficulties and ADHD that are the commonest NF1 complications in children."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Malignant-transformation epigenetics: progression of plexiform neurofibroma to MPNST involves loss of PRC2 (EZH2/SUZ12) and accompanying DNA-methylation changes, the epigenetic catastrophe layered on the NF1-driven RAS activation in the malignant nerve-sheath tumour."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: loss of neurofibromin's RAS-GAP activity hyperactivates RAS, which engages PI3K-AKT-mTOR (AKT and mTOR already mapped) alongside the RAS-MAPK cascade in NF1-driven tumours."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Malignant transformation: TP53 inactivation is a key event driving the progression of a plexiform neurofibroma into malignant peripheral nerve sheath tumour in NF1."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle progression: with CDKN2A loss and CDK4/6 activity (both mapped), E2F1 is released to drive the proliferation that accompanies malignant transformation in NF1-associated tumours."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "MPNST transformation: loss of the RB1-E2F checkpoint (CDK4/6, CDKN2A and E2F1 already mapped) is a cooperating event in the transformation of plexiform neurofibroma to malignant peripheral nerve sheath tumour in NF1."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2-mediated p53 inactivation (p53 already mapped) contributes to the malignant transformation of NF1 neurofibromas to MPNST."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "PRC2 loss: loss of PRC2 components (EZH2/SUZ12) marks the malignant transformation of NF1 plexiform neurofibroma to MPNST, the resulting H3K27me3 loss being diagnostic of this aggressive sarcoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in neurofibromas and contributes to the tumour-microenvironment interactions of NF1-associated tumours."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling shapes the Schwann-cell and inflammatory microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 signalling provides a proliferative and inflammatory input to the tumours of neurofibromatosis type 1."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the neurofibromas and the MPNSTs that arise in neurofibromatosis type 1."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the NF1-driven tumours."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, antagonised by NF1-loss-driven RAS-PI3K-AKT signalling, modulate the survival of the Schwann-cell-lineage tumours of neurofibromatosis type 1."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt signaling downstream of NF1-loss-driven RAS activation in neurofibromatosis type 1."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of receptor tyrosine kinases (KIT and PDGFR already mapped) drives the invasive signaling of the plexiform neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins, alongside mast-cell recruitment, shape the inflammatory microenvironment that promotes neurofibroma growth in neurofibromatosis type 1."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the malignant-transformation risk of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the NF1/neurofibromin-deficient, RAS-hyperactive cells of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the RAS-driven cells of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment (including tumor-associated macrophages) shapes the microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory tumor-microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment (including mast-cell-rich neurofibromas) of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the mast-cell and immune microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ptpn11
    relation: connects-to
    note: "RASopathy convergence: PTPN11/SHP2 sits directly upstream of RAS, and because neurofibromin is a RAS-GAP, NF1 and PTPN11-driven Noonan syndrome converge on the same hyperactive RAS-MAPK pathway (ERK already mapped), making SHP2 inhibitors a rational shared therapeutic node."
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "RAS-dosage regulator: LZTR1 controls RAS ubiquitination and degradation, so its loss (schwannomatosis, Noonan spectrum) raises RAS output much as neurofibromin loss removes RAS-GAP braking, placing NF1 among disorders that dysregulate RAS abundance, not only its activation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "NF1 vasculopathy: neurofibromin is expressed in vascular smooth muscle and endothelium, and its loss drives neointimal proliferation with impaired nitric-oxide vasodilation, the basis for the renal artery stenosis, moyamoya and hypertension that complicate NF1."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal neurofibroma growth: neurofibromas often enlarge during puberty and pregnancy, implicating estrogen and the reproductive-hormone surge in the growth of these tumours, which express hormone receptors."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy growth: progesterone receptors are expressed on many NF1 neurofibromas, and the progesterone rise of pregnancy is associated with their accelerated growth, part of the hormonal influence (estrogen already mapped) on the disease."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Renovascular hypertension: NF1 vasculopathy (nitric oxide already mapped) causes renal artery stenosis that activates the renin-angiotensin system, and angiotensin II drives the resulting renovascular hypertension seen in affected children and adults."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Neurofibroma matrix: neurofibromas are composed of Schwann cells, fibroblasts (already mapped) and mast cells in a loose, collagen-rich myxoid stroma, the abundant extracellular matrix giving these NF1 tumours their soft texture."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Tumour microenvironment: IL-10 among the cytokines of the neurofibroma microenvironment, with the mast cells (already mapped) and macrophages, shapes the immune milieu that supports the growth of these NF1 nerve-sheath tumours."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac involvement: NF1 carries congenital heart disease (heart already mapped), hypertrophic cardiomyopathy and vasculopathy, and troponin elevation can mark the myocardial injury of these cardiovascular manifestations."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell pruritus: the mast cells (already mapped) infiltrating the neurofibromas release histamine, driving the itch characteristic of the growing tumours and part of the mast-cell-rich microenvironment that supports them."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 mast-cell milieu: IL-4 supports the mast cells (already mapped) and polarises macrophages toward an M2 phenotype (IL-10 already mapped) in the neurofibroma microenvironment, part of the type-2 immune milieu that fosters tumour growth."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the mast cells (already mapped) and inflammatory infiltrate (IL-6 and IL-1 already mapped) of the neurofibroma microenvironment contribute to its inflammation, part of the stroma that supports the NF1 tumours."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 milieu: IL-13, with IL-4 (already mapped), supports the mast-cell (already mapped) and M2 macrophage type-2 milieu of the neurofibroma microenvironment that fosters the NF1 tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell recruitment: the mast cells, releasing histamine (already mapped) and type-2 (IL-4 already mapped) signals, infiltrate the neurofibromas and are essential to the microenvironment that drives their growth in neurofibromatosis type 1."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "NF1-associated GIST: neurofibromatosis type 1 predisposes to multiple wild-type small-bowel gastrointestinal stromal tumours, part of the tumour spectrum of the syndrome beyond the nerve-sheath tumours."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Growth-metabolic adipokine: leptin reflects the distinctive growth pattern (short stature and macrocephaly, growth hormone already mapped) and the metabolic profile of neurofibromatosis type 1."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic profile of neurofibromatosis type 1."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Neurofibroma-microenvironment adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neurofibroma microenvironment (mast cell and IL-4 already mapped) of neurofibromatosis type 1."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune microenvironment of the neurofibromas (mast cell already mapped) of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mast-cell (already mapped)-rich neurofibroma microenvironment of neurofibromatosis type 1."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neurofibroma microenvironment of neurofibromatosis type 1."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the mast cells (already mapped), reflects the type-2 immune dimension of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) of the neurofibroma microenvironment provide the adaptive immune surveillance against the malignant transformation to MPNST (already mapped) in neurofibromatosis type 1."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the mast-cell-rich (already mapped) neurofibroma microenvironment of neurofibromatosis type 1."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the adaptive immune response within the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response within the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the malignant (MPNST already mapped) transformation of the neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Neurofibroma complement: the complement C3 activation contributes to the inflammatory dimension of the mast-cell-rich (already mapped) neurofibroma microenvironment of neurofibromatosis type 1."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "NF1 nerve stroma alarmin: TSLP from the NF1-deficient peripheral nerve stroma activates mast cells (already mapped) and modulates the type-2 inflammatory microenvironment of the plexiform neurofibromas; TSLP-driven mast-cell activation promotes the NF1 neurofibroma growth."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Neurofibroma pain: bradykinin activates B2 receptors on NF1 neurofibroma cells and peripheral sensory neurons, amplifying the neuropathic pain (already mapped) and mechanical allodynia of the plexiform and dermal neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Neurofibroma ECM: periostin secreted by the NF1 neurofibroma-associated fibroblasts (already mapped) and mast cells (already mapped) promotes the integrin αV-mediated invasion and the fibrous matrix accumulation of the plexiform neurofibromas of neurofibromatosis type 1."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "NF1 complement regulation: C1-INH controls the classical complement pathway in the NF1 neurofibroma stroma, limiting complement-mediated lysis of mast cells (already mapped) and Schwann cells (already mapped) and dampening the NF1 (already mapped) inflammatory progression."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "NF1 EPO signalling: erythropoietin receptor (EPOR) on NF1 neurofibroma Schwann cells activates JAK2/STAT3 pro-survival signalling, amplifying the NF1 (already mapped) loss-driven RAS/MAPK hyperactivation and the VEGF-driven (already mapped) neurofibroma angiogenesis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Neurofibroma complement C5: complement C5 and its C5a effector amplify the mast-cell (already mapped) and macrophage (already mapped) driven inflammatory cascade in the NF1 neurofibroma stroma; C5a recruits the myeloid cells that sustain the plexiform neurofibroma growth."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "NF1 antioxidant protection: melatonin receptor activation in NF1 neurofibroma cells suppresses the RAS/MAPK (NF1 already mapped)-driven oxidative stress by upregulating GPX and SOD antioxidant enzymes, attenuating neurofibromatosis-type-1 neurofibroma proliferation."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "NF1 androgen modulation: testosterone via androgen receptor signalling modulates NF1 neurofibroma mast-cell (already mapped) infiltration and the neurofibromin (NF1 already mapped) loss-driven RAS hyperactivation, influencing sex-dimorphic severity in neurofibromatosis type 1."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "NF1 serotonin axis: serotonin via 5-HT receptors on NF1 Schwann cells and mast cells (already mapped) modulates cAMP-PKA signalling and amplifies the NF1 (already mapped) loss-driven RAS/MAPK proliferative cascade in the neurofibromatosis-type-1 tumour microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "NF1 prolactin signalling: prolactin via JAK2/STAT5 activates NF1 neurofibroma Schwann cells and mast cells (already mapped), augmenting the neurofibromin (already mapped) loss-driven RAS/MAPK (already mapped) proliferative cascade."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NF1 oxytocin: oxytocin receptors on NF1 Schwann cells couple to Gαq-PKC, converging on the RAS/MAPK (already mapped) cascade downstream of neurofibromin (already mapped) loss, augmenting neurofibroma proliferation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NF1 vasopressin: vasopressin via V1a receptors on NF1 neurofibroma stroma activates Gαq-PKC signalling that converges on RAS/MAPK (already mapped), amplifying neurofibromin (already mapped) loss-driven progression and mast-cell (already mapped) infiltration."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "NF1 selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the NF1 tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "NF1 iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of neurofibromatosis type 1."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NF1 sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of NF1."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NF1 magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and fibroblasts (already mapped), attenuates oxidative stress; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "NF1 zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix remodelling; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour cascade of NF1."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "NF1 potassium: potassium channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the NF1 tumour microenvironment; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of neurofibromatosis type 1."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "NF1 calcium: calcium as second messenger in Schwann cells (already mapped) and macrophages (already mapped) modulates RAS/ERK signalling; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour cascade of NF1."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "NF1 carbon: carbon as backbone of neurofibromin and NF-κB (already mapped) structural proteins in Schwann cells (already mapped) sustains RAS-GTPase suppression; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "NF1 chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the NF1 tumour microenvironment; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "NF1 hydrogen: hydrogen, via redox homeostasis in Schwann cells (already mapped) and macrophages (already mapped), supports neurofibromin-mediated RAS suppression; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "NF1 iron: iron in haem and iron-sulfur clusters of Schwann cells (already mapped) and macrophages (already mapped) sustains mitochondrial function; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "NF1 nitrogen: nitrogen in amino-acid scaffold of neurofibromin and NF-κB (already mapped) proteins in Schwann cells (already mapped) sustains RAS-GTPase function; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "NF1 pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) modulates neurofibroma immune evasion; pd-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "NF1 glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "NF1 wnt-beta-catenin: WNT/β-catenin on fibroblasts (already mapped) and macrophages (already mapped) regulates neurofibroma stromal expansion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) cascade of NF1."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "NF1 smad4: SMAD4 in fibroblasts (already mapped) and macrophages (already mapped) mediates neurofibroma TGF-β signalling; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "NF1 il-2: IL-2 from t-cytotoxic cells (already mapped) and macrophages (already mapped) regulates neurofibroma immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "NF1 fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) promotes neurofibroma ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NF1 notch: Notch signalling on fibroblasts (already mapped) and macrophages (already mapped) regulates neurofibroma cell fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "NF1 igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes neurofibroma cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "NF1 activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives neurofibroma fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1."
---

# Neurofibromatosis Type 1

## Overview

**Neurofibromatosis type 1 (NF1)**, also called **von Recklinghausen disease**, is an autosomal dominant hereditary tumor predisposition and RASopathy caused by germline pathogenic variants in the **NF1** tumor suppressor gene (chromosome 17q11.2, encodes neurofibromin, a RAS-GAP). With a prevalence of approximately **1 in 3,000** (one of the most common single-gene disorders), NF1 is the **most frequently diagnosed single-gene cancer predisposition syndrome** in humans. NF1 syndrome features a broad spectrum of manifestations including café-au-lait macules, cutaneous and plexiform neurofibromas, Lisch nodules, optic pathway gliomas, and cardiovascular abnormalities, as well as a significantly elevated lifetime risk of malignant tumors including **malignant peripheral nerve sheath tumor (MPNST)** (~10%), glioma, leukemia, and gastrointestinal stromal tumor (GIST) [^gutmann-2017-nf1-primer] [^dombi-2016-selumetinib].

**NF1 syndrome prevalence among hereditary cancer syndromes:**

NF1 is unique in being among both the most common and most mutated single-gene cancer syndromes. Half of all NF1 cases arise from de novo mutations (no family history), reflecting the NF1 gene's large target size (350 kb, 60 exons — one of the largest human genes) and correspondingly high spontaneous mutation rate.

**NIH Diagnostic Criteria for NF1 (1988, still in clinical use; 2021 revised criteria available):**
Two or more of:
1. ≥6 café-au-lait macules (≥5 mm pre-pubertal; ≥15 mm post-pubertal)
2. ≥2 cutaneous or subcutaneous neurofibromas, or ≥1 plexiform neurofibroma
3. Freckling in axilla or groin (Crowe's sign)
4. Optic pathway glioma
5. ≥2 Lisch nodules (iris hamartomas)
6. Distinctive bony lesion: sphenoid wing dysplasia, pseudarthrosis of long bone
7. First-degree relative with NF1 by these criteria

**2021 Updated criteria add:** heterotopic/ectopic spleen, moyamoya syndrome, NF1-associated GIST

## Structure

### Genetic basis

- **NF1 gene**: 17q11.2; 350 kb; 60 exons; encodes 2818 aa neurofibromin
- **Inheritance**: autosomal dominant; 50% offspring risk
- **De novo rate**: ~50% of NF1 cases; among the highest de novo rates of any monogenic condition (due to large gene size → high target for new mutations)
- **Mutation spectrum**: diverse; >3,500 unique pathogenic variants; frameshift + nonsense + splice (~60%), missense (~20%), large deletions (~10%, often severe phenotype), deep intronic variants
- **Severe/atypical phenotype**: large genomic deletions (>1 Mb) encompassing NF1 and flanking genes → more neurofibromas, cognitive effects, dysmorphic features, vasculopathy
- **Genotype-phenotype**: generally poor; same mutation can produce highly variable phenotype even within families; exceptions: c.2970-2972delAAT (in-frame exon 17 deletion) = milder, CALM only; c.5543C>T (Arg1849Trp) = spinal neurofibromas; large deletions = severe
- **Somatic mosaicism**: ~5-10% of apparent NF1; detected by deep sequencing (VAF <30%)

### Two-hit model in NF1 tumors

NF1 follows a modified two-hit tumor suppressor model:
1. **Germline first hit**: one pathogenic NF1 allele inactivated in every cell
2. **Somatic second hit (LOH at 17q11.2)**: in Schwann cells (neurofibromas) and mast cells; LOH detected in >95% of individual neurofibroma Schwann cells
3. **Neurofibroma microenvironment**: NF1+/− mast cells and fibroblasts in the neurofibroma stroma produce KIT ligand (SCF) and other factors that promote NF1−/− Schwann cell proliferation; haploinsufficiency of flanking cells is required, not just the tumor-initiating Schwann cell

In glioma and MPNST: additional alterations required — MPNST requires CDKN2A/2B loss (cyclin-CRK4 pathway) and sometimes EGFR amplification or TP53 mutation beyond NF1 biallelic LOH.

## Function

### NF1 syndrome manifestations

**Skin (café-au-lait macules and neurofibromas):**
- Café-au-lait macules (CALM): uniform tan spots; arise in infancy; increase throughout childhood; benign; present in >99% of NF1 patients; also present in Legius syndrome, McCune-Albright, and normal population (<5 CALMs is normal)
- Axillary/inguinal freckling (Crowe's sign): pathognomonic in combination with CALMs; develops in ~65% of NF1 patients in early childhood
- Cutaneous neurofibromas: soft flesh-colored papules, may be hundreds to thousands; increase with age; benign but cosmetically significant; arise from skin Schwann cells; typically puberty-onset
- Subcutaneous neurofibromas: deeper, firmer, often painful; arise from deeper nerve sheaths
- **Plexiform neurofibromas (PNF)**: large diffuse tumors arising from major nerve plexuses; present in ~30-50% of NF1 patients; often disfiguring; can be life-threatening if near airway; the precursor lesion for MPNST (malignant transformation in ~10-15%)

**Eye (Lisch nodules and optic glioma):**
- Lisch nodules: iris melanocytic hamartomas; slit-lamp examination required; present in >90% of NF1 adults; benign; pathognomonic for NF1; absent in NF2, Legius, and most other syndromes
- Optic pathway glioma (OPG): usually low-grade pilocytic astrocytoma (WHO grade 1) involving optic nerves, chiasm, or tracts; ~15% of NF1 patients; mostly asymptomatic; symptomatic OPG (~6%): visual acuity loss, proptosis, precocious puberty (if hypothalamic involvement); treatment: carboplatin + vincristine (CV) first-line; MEK inhibitors (selumetinib/trametinib) increasingly used; rarely requires surgery

**Bone:**
- Sphenoid wing dysplasia: congenital absence/hypoplasia of the sphenoid bone; rare; can cause pulsatile exophthalmos
- Tibial pseudarthrosis (bowed tibia, fracture risk): congenital; rare; difficult to treat; associated with young age
- Short stature, scoliosis, reduced bone density: common

**Cardiovascular:**
- Congenital heart disease (pulmonary stenosis, ASD): ~2-3%
- **NF1-associated vasculopathy**: RAS-MAPK dysregulation in vascular smooth muscle → stenosis, aneurysm; renovascular hypertension, moyamoya syndrome; often in children
- Hypertension: ~20% of NF1 patients; renovascular or essential

**CNS (learning/cognition):**
- Learning disabilities: ~50-60% of NF1 patients (most common complication)
- Attention-deficit disorder (ADHD): ~50%
- Autism spectrum features: ~30%
- Lower IQ on average (~10-15 points below population mean); rarely severe intellectual disability
- T2 hyperintense foci (UBOs — unidentified bright objects) on brain MRI: common; significance unclear; may correlate with cognitive issues
- Epilepsy: ~5-7%

**Malignant complications:**
- **MPNST**: lifetime risk ~10-15%; arises from plexiform neurofibromas; if size >3 cm + rapid growth + pain + new neurological deficit → suspicious for MPNST; FDG-PET (SUV >3.5) distinguishes from benign PNF; poor prognosis (5-year OS ~40-50%)
- **Optic pathway glioma**: low-grade but may be visually threatening
- **Low-grade glioma (pilocytic)**: brain tumors common in NF1; usually low-grade; BRAF internal duplication (KIAA1549-BRAF fusion) drives NF1-associated LGG; MEK inhibitors (trametinib, dabrafenib) active in BRAF-fusion NF1 LGG
- **JMML (juvenile myelomonocytic leukemia)**: RAS-MAPK pathway in hematopoiesis; NF1 infants at elevated JMML risk; PTPN11, NRAS, KRAS, NF1 mutations all cause JMML
- **Pheochromocytoma/paraganglioma**: slightly elevated risk (~3-4%)
- **Breast cancer**: modest elevation (~10-15% lifetime vs ~13% population; age-dependent elevated risk at 40-50)
- **GIST**: ~3-5% of NF1 patients; distinct from KIT/PDGFRA-mutant sporadic GIST; NF1-GIST is KIT/PDGFRA wildtype; imatinib less effective; sunitinib or regorafenib second-line

## Pathology

### Surveillance and management

**Annual surveillance:**
- Annual clinical assessment: neurological exam, skin survey, ophthalmology (children — annual until age 6; then as needed), blood pressure
- **Brain MRI**: recommended for any new neurological symptom; periodic in children with known OPG
- **Whole-body MRI (WB-MRI)**: recommended for NF1 patients, especially to monitor known PNF and detect MPNST; frequency guided by clinical risk

**Selumetinib (Koselugo) for NF1-associated PNF:**
- MEK1/2 inhibitor; oral; pediatric use for symptomatic/progressive inoperable PNF
- SPRINT Phase 2 trial (Dombi 2016, NEJM): 20 of 24 patients had ≥20% tumor volume reduction; confirmed in Phase 2b expansion; FDA Breakthrough Therapy; FDA-approved April 2020 for pediatric NF1 with inoperable PNF (≥2 years)
- Adult NF1-PNF: trials ongoing (SPRINT extension, RENEW trial)
- MEK inhibitor toxicity: acneiform rash, GI toxicity, cardiac (LVEF monitoring), retinal vein occlusion; dose adjustments; teratogenic → contraception required

**MPNST management:**
- Surgical resection with wide margins: primary curative intent; R0 resection goal
- Adjuvant RT: used in R1/R2 resection or high-grade MPNST (same RT-second cancer concern as hereditary RB — less prominent in NF1 context but considered)
- Systemic chemotherapy: no FDA-approved agent; doxorubicin ± ifosfamide (standard soft tissue sarcoma regimen); limited responses
- CDK4/6 inhibitors + MEK inhibitors: clinical trials in MPNST (CDK4 pathway co-activated with NF1 LOF)

**Pregnancy in NF1:**
- Neurofibroma proliferation can increase during pregnancy (estrogen effect on neurofibroma Schwann cells)
- Preconception: 50% offspring risk; preimplantation genetic testing (PGT-M) available

## Connections

- `connects-to` → **[SPRED1](../../03-molecular/spred1/README.md)** — Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — Neurofibromin (NF1) is a RAS-GAP; NF1 LOF → sustained RAS-GTP → MAPK/PI3K/mTOR activation → NF1 syndrome manifestations including neurofibromas, MPNST, optic gliomas; selumetinib (MEK1/2 inhibitor) FDA-approved for NF1-associated plexiform neurofibromas in children.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — NF1 LOF activates the same RAS-MAPK pathway as oncogenic KRAS mutations; both result in sustained RAS-GTP → MEK/ERK activation → proliferation; MEK inhibitors (selumetinib, trametinib) are active in NF1-deficient and KRAS-mutant tumors via the shared MAPK pathway.
- `connects-to` → **[MPNST](../../07-system/mpnst/README.md)** — MPNST arises in ~10% of NF1 patients from plexiform neurofibromas; NF1-MPNST is more aggressive than sporadic MPNST; NF1 LOF → RAS-MAPK/CDK4 → malignant transformation; selumetinib shrinks plexiform precursors; surgical resection primary for overt MPNST.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — NF1 neurofibromas — cutaneous, subcutaneous, and plexiform — grow from Schwann cells of peripheral nerves after a somatic second hit knocks out the remaining NF1 allele; plexiform neurofibromas are the precursor lesion that can transform into MPNST in ~10-15%.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Neurofibroma growth depends on its microenvironment: NF1-haploinsufficient mast cells and fibroblasts secrete stem-cell factor (SCF/KIT ligand) that drives proliferation of the NF1-null Schwann cells — a paracrine loop explored therapeutically with imatinib (anti-KIT).
- `connects-to` → **[GIST](../gist/README.md)** — GIST occurs in ~3-5% of NF1 patients but is biologically distinct from sporadic GIST: NF1-associated GISTs are KIT/PDGFRA wild-type (driven instead by NF1 loss → RAS-MAPK), so they respond poorly to imatinib, with sunitinib or regorafenib used in later lines.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — NF1 and NF2 share a name and dominant inheritance but are unrelated diseases: NF1 (neurofibromin, a RAS-GAP) drives café-au-lait spots and neurofibromas, while NF2 (merlin, a Hippo regulator) drives bilateral vestibular schwannomas and meningiomas — different genes and pathways.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin shows NF1's earliest and most reliable signs: six or more café-au-lait macules and axillary/inguinal freckling appear in childhood, followed by cutaneous and plexiform neurofibromas; these criteria often establish the diagnosis before nerve or brain tumors appear.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The optic pathway glioma is NF1's signature brain tumor: a low-grade pilocytic astrocytoma of the optic nerve/chiasm in ~15% of children, often indolent but able to threaten vision; NF1 also raises risk of other gliomas, with MEK inhibitors (selumetinib) used for progression.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — NF1 predisposes to pheochromocytoma: loss of neurofibromin's RAS-GAP activity in adrenal-medullary chromaffin cells drives catecholamine-secreting tumors in ~1-5% of NF1 patients, so unexplained hypertension in NF1 warrants plasma metanephrine screening.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — NF1 and Noonan syndrome are both RASopathies—germline disorders of the RAS-MAPK pathway—and overlap clinically: a 'neurofibromatosis-Noonan' phenotype exists, with short stature, learning issues, and cardiac or pigmentary signs blurring the two.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Women with NF1 carry roughly double the breast cancer risk with worse outcomes, especially before age 50: neurofibromin loss disinhibits RAS-MAPK in breast epithelium, so NF1 guidelines recommend earlier, enhanced mammographic and MRI screening.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — NF1-associated and IDH-mutant gliomas are two distinct molecular routes to glioma: NF1's neurofibromin loss disinhibits Ras, driving optic-pathway gliomas, while sporadic adult gliomas are often IDH-mutant—Ras-pathway versus metabolic-epigenetic routes.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Rhabdomyosarcoma is part of the NF1 tumor spectrum: neurofibromin loss disinhibiting Ras predisposes children with NF1 to this skeletal-muscle sarcoma (often embryonal subtype), adding a soft-tissue cancer to NF1's neurofibromas, optic gliomas and MPNSTs.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — NF1 and Gorlin are both autosomal-dominant tumor-predisposition phakomatoses driven by loss of a single pathway brake: NF1's neurofibromin loss unleashes Ras, Gorlin's PTCH1 loss unleashes Hedgehog—two pathways, one syndromic logic.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neurofibromas grow on the nerves NF1 affects: loss of neurofibromin in Schwann-cell-lineage cells lets benign neurofibromas form along peripheral nerves enveloping their neurons, causing the skin nodules and plexiform tumors that define neurofibromatosis type 1.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — NF1 predisposes to gliomas from optic pathway to high-grade: neurofibromin normally restrains RAS, so its loss drives childhood optic pathway gliomas and, less often, glioblastoma—linking the syndrome's RAS-pathway defect to brain as well as nerve tumors.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye gives diagnostic clues to NF1: Lisch nodules (iris hamartomas) are a near-universal diagnostic criterion, and optic pathway gliomas threaten vision—so ophthalmologic exam is central to diagnosing and monitoring neurofibromatosis type 1.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — NF1 is fundamentally a tumor-prone disorder of the nervous system: loss of neurofibromin unleashes RAS in nerve-sheath cells, producing neurofibromas, optic gliomas and learning difficulties—so the nervous system bears both the benign tumors and the cognitive features.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin announces NF1: café-au-lait macules, axillary freckling and cutaneous neurofibromas are diagnostic criteria usually present from childhood, so the integumentary system gives the earliest and most accessible signs of the syndrome.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — NF1 also affects the skeleton: scoliosis, sphenoid-wing dysplasia and tibial pseudarthrosis (a non-healing congenital fracture) are recognized bony features, so the musculoskeletal system is part of this multisystem RAS-pathway disorder.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — NF1 is a treatable cause of secondary hypertension in the young: renal-artery stenosis from arterial dysplasia and catecholamine-secreting pheochromocytomas both raise blood pressure, so hypertension in an NF1 patient triggers a search for these causes.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — NF1's signature brain tumor is an astrocyte glioma: optic pathway and other low-grade pilocytic astrocytomas arise when neurofibromin loss unleashes RAS in glial cells, so children with NF1 are screened for vision-threatening optic gliomas.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF1 is a RASopathy driven through ERK: neurofibromin normally switches off RAS, so its loss leaves RAS-RAF-MEK-ERK signaling stuck on—the rationale for MEK inhibitors like selumetinib that shrink inoperable plexiform neurofibromas.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — NF1 loss feeds the mTOR growth engine: without neurofibromin's brake on RAS, the PI3K-AKT-mTOR arm runs high alongside the MAPK pathway, so mTOR inhibitors like sirolimus are tested to shrink plexiform neurofibromas.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — NF1 weakens bone through its osteoblasts: neurofibromin loss disrupts these bone-building cells, causing scoliosis, sphenoid-wing dysplasia, and the hard-to-heal tibial pseudarthrosis that are skeletal hallmarks of the syndrome.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — NF1's optic pathway gliomas can disturb growth hormone: tumors near the hypothalamus and pituitary derail the growth axis, causing precocious puberty or growth-hormone problems—why NF1 children need growth and endocrine monitoring.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Neurofibromas are built with macrophages: alongside the mast cells that drive their itch, macrophages make up much of the tumor and secrete factors that help the Schwann-cell tumors grow—a stromal target in this nerve disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — NF1 loss unleashes growth through AKT: without neurofibromin's brake on Ras, signaling pours into the PI3K-AKT-mTOR pathway as well as ERK, so AKT-mTOR inhibitors join MEK inhibitors as strategies against the tumors.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — NF1 predisposes to adrenal pheochromocytoma: loss of neurofibromin in adrenal medullary cells drives catecholamine-secreting tumors, so unexplained hypertension in NF1 prompts a hunt for a pheochromocytoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NF1's café-au-lait spots are painted with copper: the flat brown macules and skinfold freckling come from excess melanin, built by the copper-dependent enzyme tyrosinase in pigment cells.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — NF1 vasculopathy chokes the kidney's arteries: neurofibromin loss in vessel walls narrows the renal arteries, a cause of the hypertension that, with pheochromocytoma, must be sought in NF1.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — NF1 weakens the blood-vessel lining: loss of neurofibromin in endothelial and smooth-muscle cells drives a vasculopathy of stenoses and aneurysms, behind the strokes and renovascular disease of the syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons watch NF1 unfold: MRI tracks optic-pathway gliomas and plexiform neurofibromas, whole-body MRI gauges tumor burden, and slit-lamp light spots the Lisch nodules on the iris that help clinch the diagnosis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Neurofibromas are mixed tumors, and fibroblasts are part of the mix: alongside Schwann cells, perineurial cells, and mast cells, fibroblasts lay down the loose collagenous matrix that gives these soft, fleshy nodules their texture.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — NF1 can be born into the heart: like the related RASopathies, it raises the risk of congenital heart disease — pulmonary valve stenosis most of all — so children are screened for structural defects alongside their tumors.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy dissects the neurofibroma: it is a mix of Schwann cells, perineurial cells, fibroblasts, and mast cells loosely wrapped in collagen, the heterogeneous tangle that distinguishes it from a pure schwannoma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — NF1 distorts the growing skeleton: sphenoid-wing dysplasia, scoliosis, and the non-healing tibial pseudarthrosis reflect a bone-forming defect, warping the marrow-bearing bones from birth.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — NF1 can scar the lungs: a diffuse interstitial lung disease with basal fibrosis and upper-lobe bullae develops in some adults, adding pulmonary disease to the syndrome's tumors and skeletal changes.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Biopsy reads the tumors by antibody: S100 and SOX10 stains confirm a neurofibroma's Schwann-cell origin, and as a benign lesion transforms toward MPNST the loss of H3K27me3 staining flags the dangerous change.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — NF1 reaches the bowel several ways: intestinal neurofibromas and ganglioneuromatosis stud the gut wall, and the syndrome's GISTs and periampullary neuroendocrine tumors can bleed or obstruct, making GI symptoms a reason to look harder.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — NF1 quietly weakens bone: patients run low on vitamin D with reduced bone mineral density and more fractures, an osteopenia that compounds the syndrome's scoliosis and dysplasia and is watched and supplemented in their care.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — NF1 is autosomal dominant with a striking twist: each child of a carrier has a 50% risk, yet about half of all cases are new de novo mutations, so genetic counseling and preimplantation options matter even in families with no prior history.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — The commonest NF1 complication is in the mind, not the nerves: learning disabilities and ADHD affect most children with the syndrome, as loss of neurofibromin's RAS control disturbs the signaling that underpins attention and learning.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Bone fails to knit in NF1: losing neurofibromin tips bone remodeling toward overactive osteoclast resorption, which underlies the non-healing pseudarthrosis of the tibia and the dysplasia and scoliosis that mark the skeleton.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — The same RAS overdrive reaches the blood: NF1 children have a strong predisposition to juvenile myelomonocytic leukemia, the pediatric cousin of CMML, because losing neurofibromin unleashes RAS signaling in myeloid progenitors just as it does in nerve sheath cells.
- `connects-to` → **[Stroke](../stroke/README.md)** — NF1 is a disease of blood vessels too: neurofibromin loss weakens and narrows arteries into a vasculopathy, including moyamoya-like cerebral vessel disease, so children and adults face an elevated risk of stroke beyond their tumor burden.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — The brain wiring is affected from the start: beyond the learning difficulties and ADHD, a substantial share of children with NF1 meet criteria for autism spectrum disorder, reflecting how RAS-pathway signaling shapes synapse formation and cognition.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — NF1 brains spark seizures: cortical malformations, gliomas, and the disease's own neuronal effects make epilepsy more common in NF1 than the general population, adding to its neurological burden.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — A second hit turns a benign tumor deadly: CDKN2A loss is a key step when a plexiform neurofibroma transforms into MPNST, the malignant change that is the leading cause of death in NF1.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — The nerve tumors hurt: plexiform and spinal neurofibromas compress and infiltrate nerves, producing chronic neuropathic pain that is one of the most disabling everyday symptoms of NF1.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Loss of neurofibromin routes RAS into NF-κB: with the RAS brake gone, NF1 cells engage NF-κB-driven survival and inflammatory signaling among the pathways feeding their many tumors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A visible lifelong disease weighs on the mind: NF1's disfiguring tumors, pain and learning difficulties drive high rates of depression, part of the substantial psychosocial burden of the syndrome.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its vasculopathy and surgery raise clot risk: NF1 arteriopathy plus the major operations to debulk plexiform tumors predispose to venous thromboembolism alongside the disease's better-known arterial disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Loss of neurofibromin weakens the skeleton: NF1 disturbs bone remodeling, and patients show reduced bone mineral density, osteopenia, and an elevated fracture risk beyond the focal dysplasias and scoliosis.
- `connects-to` → **[Acute Myeloid Leukemia](../aml/README.md)** — Its RAS overactivity tilts marrow toward leukemia: with neurofibromin lost, hyperactive RAS signaling predisposes NF1 children to juvenile myelomonocytic leukemia and other myeloid neoplasms that can evolve toward acute myeloid leukemia.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — NF1 loss is itself a melanoma driver: inactivating NF1 unleashes RAS-MAPK signaling, defining a recognized genomic subtype of cutaneous melanoma and adding to the cancer burden these patients carry.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — RAS dysregulation also seeds gut endocrine tumours: NF1 predisposes to duodenal/periampullary somatostatinomas and other gastroenteropancreatic neuroendocrine tumours, part of its wide neoplastic spectrum.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Debulking neurofibromas heals poorly: the highly vascular plexiform neurofibromas of NF1 bleed and recur, and their surgical resection leaves wounds prone to slow, complicated closure.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong cancer risk and disfigurement breed worry: the visible skin tumours, malignant-transformation surveillance and unpredictable course of NF1 foster chronic health anxiety alongside low mood.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — RAS dysregulation disturbs growth and glands: NF1 optic-pathway gliomas near the hypothalamus cause precocious puberty and growth-hormone problems, and NF1 predisposes to phaeochromocytoma and somatostatinoma.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It is a vasculopathy too: NF1 causes a distinctive arteriopathy with renal-artery stenosis driving hypertension, plus aneurysms and a moyamoya-like cerebral vasculopathy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Neurofibromas and tumours stud the gut: NF1 causes gastrointestinal neurofibromas that can bleed or obstruct, and predisposes to GIST and duodenal somatostatinoma along the digestive tract.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its vasculopathy narrows the renal artery: NF1 causes renal artery stenosis, a treatable cause of renovascular hypertension that is important to find in young patients with high blood pressure.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can scar the lungs and crowd the chest: NF1 is associated with a diffuse interstitial lung disease with bullae, and plexiform neurofibromas can involve the chest wall and airway.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mast cells feed its tumours and it predisposes to leukaemia: mast cells recruited into neurofibromas drive their growth and itch, and NF1 children have a raised risk of juvenile myelomonocytic leukaemia.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A MEK inhibitor shrinks its tumours: selumetinib, targeting the hyperactive RAS-MEK pathway of NF1, is approved to reduce inoperable plexiform neurofibromas in children.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A fellow neurocutaneous syndrome: like tuberous sclerosis, NF1 combines skin signs with nervous-system tumours in an autosomal-dominant pattern, both converging on mTOR-pathway dysregulation.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — A spectrum cousin: schwannomatosis joins NF1 and NF2 among the neurofibromatosis-spectrum disorders, all causing multiple nerve-sheath tumours from different genes.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for the cancers it breeds: NF1 predisposes to MPNST, juvenile myelomonocytic leukaemia, glioma and rhabdomyosarcoma, treated with chemotherapy when they arise.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It dysplastically shapes the skeleton: NF1 causes sphenoid-wing dysplasia, scoliosis, tibial pseudarthrosis and reduced cortical bone density, distinctive skeletal features of the disease.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — A fellow endocrine-tumour predisposition: like MEN1, NF1 raises the risk of phaeochromocytoma and duodenal neuroendocrine tumours, overlapping the inherited tumour-syndrome spectrum.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is also a vasculopathy: neurofibromin loss in vascular smooth muscle and endothelium causes an NF1 arteriopathy—renal-artery stenosis, aneurysms and moyamoya—an under-recognised cause of the hypertension and stroke that shorten NF1 lifespan.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — A RAS-pathway neural-crest tumour: NF1 loss removes a brake on RAS-MAPK in neural-crest cells, and NF1 modestly predisposes to neuroblastoma, the embryonal sympathetic-nervous-system cancer of childhood.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Two great childhood cancer-predisposition syndromes: NF1 (neurofibromin/RAS) and Li-Fraumeni (germline TP53) both commit children to lifelong tumour surveillance, predisposing to overlapping CNS tumours and sarcomas via different pathways.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Learning and cognition: NF1 causes learning disabilities, ADHD and autism features, as excess RAS-driven GABAergic signalling impairs hippocampal long-term potentiation and memory.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — NF1 gliomas: NF1 predisposes to optic-pathway and other childhood gliomas, some high-grade and midline, RAS-driven counterparts to the H3K27M-driven sporadic diffuse midline glioma.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — RASopathy cardiac involvement: NF1 carries congenital heart disease (pulmonary stenosis) and a vasculopathy, and dysregulated RAS signalling underlies the cardiomyopathies of the RASopathies it overlaps.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — The café-au-lait mimic: constitutional mismatch-repair deficiency (biallelic Lynch genes) produces café-au-lait macules and childhood cancers that closely imitate NF1, a critical distinction since the two demand entirely different surveillance.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Two phakomatoses, one shared tumour: NF1 and von Hippel-Lindau are both neurocutaneous tumour-suppressor syndromes that predispose to pheochromocytoma, though NF1 dysregulates RAS while VHL drives HIF and angiogenesis.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — The learning gene: neurofibromin restrains RAS at the synapse, and its loss raises GABAergic inhibition and impairs synaptic plasticity, underlying the learning disabilities and attention problems common in NF1.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — RAF down the cascade: NF1 loss unleashes RAS into the BRAF-MEK-ERK cascade, the pathway targeted by MEK inhibitors such as selumetinib for NF1 plexiform neurofibromas.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle in transformation: CDKN2A loss with CDK4/6 activation drives the malignant transformation of NF1 neurofibromas to MPNST and the growth of high-grade NF1 gliomas.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Tumour microenvironment: PDGF signalling promotes neurofibroma growth and recruits the supportive stroma around the Schwann-cell tumours of NF1.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — RAS-driven oncogene: unrestrained RAS signalling from NF1 loss upregulates MYC, driving the proliferation behind neurofibroma growth and malignant transformation.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Plexiform angiogenesis: VEGF drives the rich vascularisation of the plexiform neurofibromas of NF1, supporting their growth and the bleeding risk of these tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in growing NF1 tumours drives the angiogenesis and metabolic adaptation that accompany their transformation to MPNST.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Mast-cell recruitment: KIT-driven mast cells recruited to NF1 neurofibromas secrete factors that promote Schwann-cell proliferation, a microenvironmental engine of neurofibroma growth.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Cognitive deficits: excess RAS signalling from neurofibromin loss raises GABA-mediated inhibition in the brain, the mechanism behind the learning disabilities common in NF1.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Bone dysplasia: NF1 loss dysregulates RANKL-driven osteoclast activity, contributing to the tibial pseudarthrosis, scoliosis and low bone density of neurofibromatosis type 1.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — NF1 neurofibromas are heavily infiltrated by CCL2-recruited macrophages whose growth factors sustain the Schwann-cell tumor—the inflammatory niche from which plexiform neurofibromas can progress to malignant peripheral nerve sheath tumor.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling drives the metastasis of the malignant peripheral nerve sheath tumors that arise from NF1 plexiform neurofibromas, the transformation that is the leading cause of NF1-related death.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P from the sensory nerve fibers entangled within plexiform neurofibromas mediates the chronic neurogenic pain that is a major and under-treated source of morbidity in neurofibromatosis type 1.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — NF1 predisposes to adrenal pheochromocytomas that secrete catecholamines including norepinephrine, a cause of secondary hypertension that should be excluded in an NF1 patient with paroxysmal symptoms.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — RAS-MAPK signaling is the effector arm of BDNF-TrkB synaptic plasticity, and its constitutive dysregulation in NF1 disrupts hippocampal learning, underlying the learning difficulties and ADHD that are the commonest NF1 complications in children.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Progression of plexiform neurofibroma to MPNST involves loss of PRC2 (EZH2/SUZ12) and accompanying DNA-methylation changes, the epigenetic catastrophe layered on the NF1-driven RAS activation in the malignant nerve-sheath tumor.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Loss of neurofibromin's RAS-GAP activity hyperactivates RAS, which engages PI3K-AKT-mTOR (AKT and mTOR already mapped) alongside the RAS-MAPK cascade in NF1-driven tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 inactivation is a key event driving the progression of a plexiform neurofibroma into malignant peripheral nerve sheath tumor in NF1.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — With CDKN2A loss and CDK4/6 activity (both mapped), E2F1 is released to drive the proliferation that accompanies malignant transformation in NF1-associated tumors.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Loss of the RB1-E2F checkpoint (CDK4/6, CDKN2A and E2F1 already mapped) is a cooperating event in the transformation of plexiform neurofibroma to malignant peripheral nerve sheath tumor in NF1.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 inactivation (p53 already mapped) contributes to the malignant transformation of NF1 neurofibromas to MPNST.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Loss of PRC2 components (EZH2/SUZ12) marks the malignant transformation of NF1 plexiform neurofibroma to MPNST, the resulting H3K27me3 loss being diagnostic of this aggressive sarcoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in neurofibromas and contributes to the tumor-microenvironment interactions of NF1-associated tumors.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling shapes the Schwann-cell and inflammatory microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 signaling provides a proliferative and inflammatory input to the tumors of neurofibromatosis type 1.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the neurofibromas and the MPNSTs that arise in neurofibromatosis type 1.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory microenvironment of the NF1-driven tumors.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, antagonized by NF1-loss-driven RAS-PI3K-AKT signaling, modulate the survival of the Schwann-cell-lineage tumors of neurofibromatosis type 1.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt signaling downstream of NF1-loss-driven RAS activation in neurofibromatosis type 1.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of receptor tyrosine kinases (KIT and PDGFR already mapped) drives the invasive signaling of the plexiform neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins, alongside mast-cell recruitment, shape the inflammatory microenvironment that promotes neurofibroma growth in neurofibromatosis type 1.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the malignant-transformation risk of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the NF1/neurofibromin-deficient, RAS-hyperactive cells of neurofibromatosis type 1.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the RAS-driven cells of neurofibromatosis type 1.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment (including tumor-associated macrophages) shapes the microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of neurofibromatosis type 1.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory tumor-microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment (including mast-cell-rich neurofibromas) of neurofibromatosis type 1.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the mast-cell and immune microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of neurofibromatosis type 1.
- `connects-to` → **[PTPN11 (SHP2)](../../03-molecular/ptpn11/README.md)** — RASopathy convergence: PTPN11/SHP2 sits directly upstream of RAS, and because neurofibromin is a RAS-GAP, NF1 and PTPN11-driven Noonan syndrome converge on the same hyperactive RAS-MAPK pathway (ERK already mapped), making SHP2 inhibitors a rational shared therapeutic node.
- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — RAS-dosage regulator: LZTR1 controls RAS ubiquitination and degradation, so its loss (schwannomatosis, Noonan spectrum) raises RAS output much as neurofibromin loss removes RAS-GAP braking, placing NF1 among disorders that dysregulate RAS abundance, not only its activation.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — NF1 vasculopathy: neurofibromin is expressed in vascular smooth muscle and endothelium, and its loss drives neointimal proliferation with impaired nitric-oxide vasodilation, the basis for the renal artery stenosis, moyamoya and hypertension that complicate NF1.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormonal neurofibroma growth: neurofibromas often enlarge during puberty and pregnancy, implicating estrogen and the reproductive-hormone surge in the growth of these tumours, which express hormone receptors.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy growth: progesterone receptors are expressed on many NF1 neurofibromas, and the progesterone rise of pregnancy is associated with their accelerated growth, part of the hormonal influence (estrogen already mapped) on the disease.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Renovascular hypertension: NF1 vasculopathy (nitric oxide already mapped) causes renal artery stenosis that activates the renin-angiotensin system, and angiotensin II drives the resulting renovascular hypertension seen in affected children and adults.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Neurofibroma matrix: neurofibromas are composed of Schwann cells, fibroblasts (already mapped) and mast cells in a loose, collagen-rich myxoid stroma, the abundant extracellular matrix giving these NF1 tumours their soft texture.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Tumour microenvironment: IL-10 among the cytokines of the neurofibroma microenvironment, with the mast cells (already mapped) and macrophages, shapes the immune milieu that supports the growth of these NF1 nerve-sheath tumours.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac involvement: NF1 carries congenital heart disease (heart already mapped), hypertrophic cardiomyopathy and vasculopathy, and troponin elevation can mark the myocardial injury of these cardiovascular manifestations.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell pruritus: the mast cells (already mapped) infiltrating the neurofibromas release histamine, driving the itch characteristic of the growing tumours and part of the mast-cell-rich microenvironment that supports them.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 mast-cell milieu: IL-4 supports the mast cells (already mapped) and polarises macrophages toward an M2 phenotype (IL-10 already mapped) in the neurofibroma microenvironment, part of the type-2 immune milieu that fosters tumour growth.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the mast cells (already mapped) and inflammatory infiltrate (IL-6 and IL-1 already mapped) of the neurofibroma microenvironment contribute to its inflammation, part of the stroma that supports the NF1 tumours.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 milieu: IL-13, with IL-4 (already mapped), supports the mast-cell (already mapped) and M2 macrophage type-2 milieu of the neurofibroma microenvironment that fosters the NF1 tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell recruitment: the mast cells, releasing histamine (already mapped) and type-2 (IL-4 already mapped) signals, infiltrate the neurofibromas and are essential to the microenvironment that drives their growth in neurofibromatosis type 1.
- `connects-to` → **[GIST](../gist/README.md)** — NF1-associated GIST: neurofibromatosis type 1 predisposes to multiple wild-type small-bowel gastrointestinal stromal tumours, part of the tumour spectrum of the syndrome beyond the nerve-sheath tumours.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Growth-metabolic adipokine: leptin reflects the distinctive growth pattern (short stature and macrocephaly, growth hormone already mapped) and the metabolic profile of neurofibromatosis type 1.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic profile of neurofibromatosis type 1.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Neurofibroma-microenvironment adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the neurofibroma microenvironment (mast cell and IL-4 already mapped) of neurofibromatosis type 1.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune microenvironment of the neurofibromas (mast cell already mapped) of neurofibromatosis type 1.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the mast-cell (already mapped)-rich neurofibroma microenvironment of neurofibromatosis type 1.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the neurofibroma microenvironment of neurofibromatosis type 1.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped) and the mast cells (already mapped), reflects the type-2 immune dimension of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) of the neurofibroma microenvironment provide the adaptive immune surveillance against the malignant transformation to MPNST (already mapped) in neurofibromatosis type 1.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the mast-cell-rich (already mapped) neurofibroma microenvironment of neurofibromatosis type 1.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the adaptive immune response within the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response within the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance against the malignant (MPNST already mapped) transformation of the neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Neurofibroma complement: the complement C3 activation contributes to the inflammatory dimension of the mast-cell-rich (already mapped) neurofibroma microenvironment of neurofibromatosis type 1.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — NF1 nerve stroma alarmin: TSLP from the NF1-deficient peripheral nerve stroma activates mast cells (already mapped) and modulates the type-2 inflammatory microenvironment of the plexiform neurofibromas; TSLP-driven mast-cell activation promotes the NF1 neurofibroma growth.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Neurofibroma pain: bradykinin activates B2 receptors on NF1 neurofibroma cells and peripheral sensory neurons, amplifying the neuropathic pain (already mapped) and mechanical allodynia of the plexiform and dermal neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Neurofibroma ECM: periostin secreted by the NF1 neurofibroma-associated fibroblasts (already mapped) and mast cells (already mapped) promotes the integrin αV-mediated invasion and the fibrous matrix accumulation of the plexiform neurofibromas of neurofibromatosis type 1.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — NF1 complement regulation: C1-INH controls the classical complement pathway in the NF1 neurofibroma stroma, limiting complement-mediated lysis of mast cells (already mapped) and Schwann cells (already mapped) and dampening the NF1 (already mapped) inflammatory progression.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — NF1 EPO signalling: erythropoietin receptor (EPOR) on NF1 neurofibroma Schwann cells activates JAK2/STAT3 pro-survival signalling, amplifying the NF1 (already mapped) loss-driven RAS/MAPK hyperactivation and the VEGF-driven (already mapped) neurofibroma angiogenesis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Neurofibroma complement C5: complement C5 and its C5a effector amplify the mast-cell (already mapped) and macrophage (already mapped) driven inflammatory cascade in the NF1 neurofibroma stroma; C5a recruits the myeloid cells that sustain the plexiform neurofibroma growth.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — NF1 antioxidant protection: melatonin receptor activation in NF1 neurofibroma cells suppresses the RAS/MAPK (NF1 already mapped)-driven oxidative stress by upregulating GPX and SOD antioxidant enzymes, attenuating neurofibromatosis-type-1 neurofibroma proliferation.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — NF1 androgen modulation: testosterone via androgen receptor signalling modulates NF1 neurofibroma mast-cell (already mapped) infiltration and the neurofibromin (NF1 already mapped) loss-driven RAS hyperactivation, influencing sex-dimorphic severity in neurofibromatosis type 1.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — NF1 serotonin axis: serotonin via 5-HT receptors on NF1 Schwann cells and mast cells (already mapped) modulates cAMP-PKA signalling and amplifies the NF1 (already mapped) loss-driven RAS/MAPK proliferative cascade in the neurofibromatosis-type-1 tumour microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — NF1 prolactin signalling: prolactin via JAK2/STAT5 activates NF1 neurofibroma Schwann cells and mast cells (already mapped), augmenting the neurofibromin (already mapped) loss-driven RAS/MAPK (already mapped) proliferative cascade.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NF1 oxytocin: oxytocin receptors on NF1 Schwann cells couple to Gαq-PKC, converging on the RAS/MAPK (already mapped) cascade downstream of neurofibromin (already mapped) loss, augmenting neurofibroma proliferation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NF1 vasopressin: vasopressin via V1a receptors on NF1 neurofibroma stroma activates Gαq-PKC signalling that converges on RAS/MAPK (already mapped), amplifying neurofibromin (already mapped) loss-driven progression and mast-cell (already mapped) infiltration.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — NF1 selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the NF1 tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — NF1 iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of neurofibromatosis type 1.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NF1 sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of NF1.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NF1 magnesium: magnesium, as cofactor of antioxidant enzymes in macrophages (already mapped) and fibroblasts (already mapped), attenuates oxidative stress; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — NF1 zinc: zinc, as cofactor of metalloproteinases in macrophages (already mapped) and fibroblasts (already mapped), modulates matrix remodelling; zinc depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour cascade of NF1.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — NF1 potassium: potassium channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the NF1 tumour microenvironment; potassium depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of neurofibromatosis type 1.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — NF1 calcium: calcium as second messenger in Schwann cells (already mapped) and macrophages (already mapped) modulates RAS/ERK signalling; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour cascade of NF1.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — NF1 carbon: carbon as backbone of neurofibromin and NF-κB (already mapped) structural proteins in Schwann cells (already mapped) sustains RAS-GTPase suppression; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — NF1 chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the NF1 tumour microenvironment; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — NF1 hydrogen: hydrogen, via redox homeostasis in Schwann cells (already mapped) and macrophages (already mapped), supports neurofibromin-mediated RAS suppression; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — NF1 iron: iron in haem and iron-sulfur clusters of Schwann cells (already mapped) and macrophages (already mapped) sustains mitochondrial function; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of NF1.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — NF1 nitrogen: nitrogen in amino-acid scaffold of neurofibromin and NF-κB (already mapped) proteins in Schwann cells (already mapped) sustains RAS-GTPase function; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neurofibroma cascade of NF1.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — NF1 pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) modulates neurofibroma immune evasion; pd-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — NF1 glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — NF1 wnt-beta-catenin: WNT/β-catenin on fibroblasts (already mapped) and macrophages (already mapped) regulates neurofibroma stromal expansion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) cascade of NF1.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — NF1 smad4: SMAD4 in fibroblasts (already mapped) and macrophages (already mapped) mediates neurofibroma TGF-β signalling; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — NF1 il-2: IL-2 from t-cytotoxic cells (already mapped) and macrophages (already mapped) regulates neurofibroma immune surveillance; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — NF1 fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) promotes neurofibroma ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — NF1 notch: Notch signalling on fibroblasts (already mapped) and macrophages (already mapped) regulates neurofibroma cell fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — NF1 igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes neurofibroma cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — NF1 activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives neurofibroma fibrosis; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and mtor (already mapped) tumour cascade of NF1.

[^gutmann-2017-nf1-primer]: Gutmann DH, Ferner RE, Listernick RH, et al. Neurofibromatosis type 1. *Nat Rev Dis Primers.* 2017;3:17004. [doi:10.1038/nrdp.2017.4](https://doi.org/10.1038/nrdp.2017.4) · [PubMed 28230061](https://pubmed.ncbi.nlm.nih.gov/28230061/)
[^dombi-2016-selumetinib]: Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. *N Engl J Med.* 2016;375(26):2550-2560. [doi:10.1056/NEJMoa1605943](https://doi.org/10.1056/NEJMoa1605943) · [PubMed 28029918](https://pubmed.ncbi.nlm.nih.gov/28029918/)
