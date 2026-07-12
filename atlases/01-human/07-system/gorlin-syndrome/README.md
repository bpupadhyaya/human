---
schema: human-scale-entry/v1
id: gorlin-syndrome
name: Gorlin Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Gorlin syndrome (NBCCS) is caused by germline PTCH1 (~85%) or SUFU (~2%) mutations; multiple BCCs, odontogenic keratocysts, calcified falx cerebri, medulloblastoma (~5%); radiation avoidance is critical; vismodegib FDA-approved to reduce BCC burden in Gorlin patients."
aliases: ["Gorlin syndrome", "NBCCS", "nevoid basal cell carcinoma syndrome", "Basal Cell Nevus Syndrome", "PTCH1 Gorlin", "Gorlin-Goltz syndrome", "Gorlin medulloblastoma", "hereditary BCC", "Gorlin PTCH1 SUFU"]
sources:
  - id: hahn-1996-gorlin-ptch1
    type: peer-reviewed
    cite: "Hahn H, Wicking C, Zaphiropoulos PG, et al. Mutations of the human homolog of Drosophila patched in the nevoid basal cell carcinoma syndrome. Cell. 1996;85(6):841-851."
    doi: "10.1016/S0092-8674(00)81268-4"
    pmid: "8681379"
    url: "https://doi.org/10.1016/S0092-8674(00)81268-4"
  - id: bree-2011-gorlin-guidelines
    type: peer-reviewed
    cite: "Bree AF, Shah MR; BCNS Colloquium Group. Consensus statement from the first international colloquium on basal cell nevus syndrome (BCNS). Am J Med Genet A. 2011;155A(9):2091-2097."
    doi: "10.1002/ajmg.a.34128"
    pmid: "21834026"
    url: "https://doi.org/10.1002/ajmg.a.34128"
cross_links:
  - target: 01-human/03-molecular/sufu
    relation: connects-to
    note: "Germline SUFU causes Gorlin-like syndrome: desmoplastic/nodular medulloblastoma risk (SHH subgroup, age <5) is higher than PTCH1-Gorlin; BCC and OKC are less penetrant; radiation avoidance is critical; SUFU loss releases GLI constitutively in cerebellar granule progenitors."
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "Germline PTCH1 loss causes Gorlin syndrome via constitutive Hedgehog pathway activation; PTCH1 normally inhibits SMO; loss → SMO constitutively active → GLI1/2 nuclear → BCC, OKC, calcified falx, rib anomalies; somatic PTCH1 mutation is the most common driver of sporadic BCC."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "Vismodegib and sonidegib (SMO inhibitors) are FDA-approved for Gorlin-syndrome BCC; SMO constitutively active in PTCH1/SUFU-mutant tumors; GLI1 suppression → BCC regression; acquired SMO resistance mutations (D473H) occur with extended vismodegib therapy."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Gorlin patients develop BCCs early (teens-20s in sun-exposed skin); ionizing and UV radiation dramatically accelerate BCC; vismodegib reduces BCC from 2-4/month to near-zero (STEVIE/BOLT trials); radiation avoidance is critical to prevent radiation field BCC induction."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Gorlin syndrome confers ~5% medulloblastoma risk (SHH desmoplastic/nodular subtype); median age 2-3 years vs 7-8 for sporadic SHH-MB; EBRT contraindicated (radiation-induced BCC proliferation); SMO inhibitors active in relapsed PTCH1-mutant SHH-MB; chemotherapy-only standard."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "GLI1/2 transcribe VEGF-A in BCC → tumour angiogenesis; BCC is among the most vascularised skin tumours; vismodegib (SMO inhibitor) reduces GLI → ↓VEGF-A → ↓tumour vascularity; bevacizumab shows limited single-agent BCC activity; VEGF-C/D also upregulated in BCC microenvironment."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "BCCs arise from basal keratinocytes (hair follicle bulge stem cells) with PTCH1-constrained hedgehog; UV/radiation exposure → PTCH1 somatic second hits → BCC induction at highest rates in sun-exposed skin; rigorous sun protection is primary prevention in Gorlin syndrome."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Beyond skin and brain, Gorlin syndrome produces benign fibroblastic tumors — cardiac fibromas and ovarian fibromas — reflecting Hedgehog's role in mesenchymal cell fate; these fibromas, with calcified falx and jaw keratocysts, are part of the diagnostic criteria."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 cooperates with Hedgehog activation in Gorlin tumorigenesis: germline PTCH1 loss derepresses SMO/GLI, but UV-induced TP53 mutation removes the apoptotic brake, accelerating the basal cell carcinomas — the same two-hit cooperation seen in sporadic BCC."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Hedgehog hyperactivation links Gorlin syndrome to rare childhood mesenchymal tumors: fetal rhabdomyoma and embryonal rhabdomyosarcoma occur at elevated rates, since GLI drive promotes myogenic progenitor proliferation — part of the developmental-tumor spectrum of PTCH1 loss."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Gorlin syndrome predisposes to meningioma: constitutive hedgehog activation from germline PTCH1 loss—the same pathway driving its basal cell carcinomas and medulloblastomas—also raises meningioma risk, compounded by any prior craniospinal radiotherapy."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Gorlin syndrome's skeletal stigmata reflect hedgehog control of osteoblasts: bifid/splayed ribs, vertebral anomalies, frontal bossing, and a calcified falx cerebri arise because PTCH1 loss dysregulates the hedgehog signaling that patterns bone, aiding radiographic diagnosis."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Cardiac fibroma is a hallmark Gorlin tumor: a benign fibrous mass growing within the myocardium among cardiomyocytes, it is the commonest heart tumor of childhood and, when present, strongly suggests an underlying PTCH1 hedgehog-pathway syndrome."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Gorlin and Li-Fraumeni are both dominant cancer-predisposition syndromes via different pathways: Gorlin from PTCH1/Hedgehog loss (BCCs, medulloblastoma), Li-Fraumeni from germline TP53 loss (sarcomas, breast, brain)—one disinhibits Hedgehog, the other removes p53."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Gorlin and neurofibromatosis type 1 are both dominant phakomatoses where a tumor-suppressor loss causes multisystem tumors: Gorlin's PTCH1 loss unleashes Hedgehog (BCCs, jaw cysts), NF1's neurofibromin loss unleashes Ras (neurofibromas, optic glioma)—similar logic."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian fibromas are a diagnostic feature of Gorlin syndrome: PTCH1 loss and unchecked Hedgehog signaling spur these benign, often bilateral calcified ovarian tumors—reminding that Hedgehog dysregulation drives growths well beyond skin and brain."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiation is hazardous in Gorlin syndrome: because PTCH1 loss primes skin to hedgehog-driven tumors, radiotherapy triggers hundreds of basal cell carcinomas in the treated field, so X-ray exposure is minimized—a sharp caution when these patients have medulloblastoma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Gorlin's hedgehog defect intersects with Wnt in medulloblastoma: SHH-subtype medulloblastoma (driven by PTCH1/SMO) is distinct from the Wnt-subtype, and pathway crosstalk shapes which tumors arise—so Gorlin predisposes specifically to SHH, not Wnt, medulloblastoma."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Gorlin syndrome causes congenital eye anomalies: hypertelorism, congenital cataracts, colobomas and strabismus are part of the developmental phenotype of PTCH1 loss, reflecting hedgehog signaling's role in eye morphogenesis alongside the syndrome's tumor risk."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Gorlin syndrome floods the skin with basal cell carcinomas: PTCH1 loss unleashes Hedgehog signaling so that dozens to hundreds of BCCs arise from youth, plus palmar-plantar pits—making the integumentary system the syndrome's most visible burden."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Gorlin syndrome leaves skeletal fingerprints: odontogenic keratocysts of the jaw, bifid ribs, vertebral anomalies and a calcified falx are diagnostic skeletal features, so a dental or skeletal survey often helps confirm this Hedgehog-pathway syndrome."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Gorlin syndrome predisposes the developing nervous system to medulloblastoma: Hedgehog-pathway activation drives this childhood cerebellar tumor, so affected infants need brain surveillance—and radiation must be used cautiously given their extreme BCC radiosensitivity."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium deposits are a Gorlin diagnostic clue: lamellar calcification of the falx cerebri and other ectopic calcifications are among its major criteria, reflecting how disrupted hedgehog signaling alters bone and soft-tissue mineralization."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Gorlin syndrome reaches the reproductive system: bilateral ovarian fibromas—often calcified—are characteristic, so a young woman with ovarian masses plus skin and jaw findings may carry the PTCH1 mutation behind the syndrome."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Gorlin syndrome shapes the brain structurally: macrocephaly with frontal bossing, a bridged sella turcica, and developmental anomalies accompany the tumor risk, so congenital brain malformations are part of the syndrome alongside its cancers."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "Gorlin's tumors grow because Hedgehog switches on MYCN: unchecked PTCH1/SMO signaling activates GLI, which drives MYCN to fuel the SHH-subtype medulloblastomas and basal cell carcinomas that define the syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Gorlin's basal cell carcinomas escape Hedgehog blockers via mTOR: when vismodegib shuts down smoothened, tumors can reactivate growth through mTOR and other bypass pathways, a key reason these cancers eventually resist targeted therapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Gorlin's many basal cell carcinomas exploit regulatory T cells: Tregs help the tumors evade immune clearance, which is why PD-1 checkpoint therapy (cemiplimab) is used for advanced BCCs that progress despite Hedgehog inhibitors."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Hedgehog signaling teams with NF-kB in Gorlin's tumors: the constitutive Hedgehog drive cooperates with NF-kB inflammatory signaling to promote the survival and growth of the syndrome's many basal cell carcinomas."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill the stroma of Gorlin's basal cell carcinomas: tumor-associated macrophages support angiogenesis and dampen immunity around the Hedgehog-driven skin tumors, helping the lesions persist and recur."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Ultraviolet oxygen chemistry compounds Gorlin's tumor risk: on top of the inherited Hedgehog defect, sun-driven reactive oxygen species damage skin-cell DNA, so UV exposure markedly multiplies the basal cell carcinomas these patients develop."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Gorlin syndrome can grow tumors in the heart: cardiac fibromas, benign fibrous masses, are a recognized feature, sometimes found in childhood and occasionally disturbing the heart's rhythm or flow."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Gorlin's benign tumors are made of fibrous tissue: cardiac and ovarian fibromas are overgrowths of fibroblasts and collagen, part of the syndrome's broad tendency to form hamartomatous fibrous masses."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Gorlin syndrome calcifies with calcium phosphate: a calcified falx cerebri, along with skeletal anomalies like bifid ribs, are diagnostic clues, the mineral laid down where it should not be."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Gorlin's brain tumor is medulloblastoma: it arises from cerebellar granule-neuron precursors that depend on the very Hedgehog signal the syndrome unleashes, so children are screened with brain MRI."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Unleashed Hedgehog drives Gorlin's tumors through cyclin D1: the pathway switches on this cell-cycle gene, pushing basal cells and granule precursors to proliferate into BCCs and medulloblastomas."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Gorlin sprouts cysts beyond the jaw: mesenteric and other abdominal cysts occur alongside its odontogenic keratocysts, part of the syndrome's broad tendency to form benign cavities."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads Gorlin's lesions: the palisaded basaloid cells of its many basal cell carcinomas and the thin, corrugated lining of its odontogenic keratocysts both reflect the runaway Hedgehog signaling that PTCH1 loss unleashes."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Gorlin warps the bones: odontogenic keratocysts hollow out the jaw, and bifid ribs, vertebral anomalies, and a calcified falx betray the syndrome on a skeletal survey of the marrow-bearing bones."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Gorlin's skeletal defects reach the chest: bifid, splayed, or fused ribs deform the thoracic cage around the lungs, one of the bony anomalies that, with jaw cysts and skin signs, point to the diagnosis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Immunotherapy helps the heaviest BCC burden: when Gorlin patients sprout too many basal cell carcinomas for surgery, the anti-PD-1 antibody cemiplimab can be used alongside the hedgehog-pathway inhibitors that target the underlying defect."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Gorlin grows collagen-rich fibrous tumors: the cardiac fibroma and ovarian fibroma characteristic of the syndrome are dense whorls of fibroblasts and collagen, benign masses found on the imaging screening it requires."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The hedgehog-blocking drugs upset the gut: vismodegib and sonidegib commonly cause nausea, loss of appetite, and taste change, side effects that — with muscle cramps and hair loss — limit how long patients can take them."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Tumors escape hedgehog blockade through other pathways: PI3K-AKT signaling crosstalks with the hedgehog axis and helps Gorlin's basal cell carcinomas grow resistant to SMO inhibitors like vismodegib, a route to relapse being targeted with combination therapy."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "The jaw cysts eat into bone: Gorlin's odontogenic keratocysts expand through the mandible and maxilla by recruiting osteoclasts to resorb bone, the painless swellings that often bring a young patient to diagnosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy is a fallback for the rare aggressive case: when a basal cell carcinoma turns advanced or metastatic and outruns hedgehog inhibitors, anti-PD-1 drugs like cemiplimab unleash cytotoxic T cells against it."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Hedgehog keeps the tumor cell from dying: unchecked GLI signaling raises the anti-apoptotic protein BCL-2 in Gorlin's basal cell carcinomas and medulloblastomas, helping the cells survive that the syndrome's mutation sets loose."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Hedgehog also builds the tumor's blood supply: SHH signaling drives endothelial recruitment and angiogenesis, feeding the basal cell carcinomas and the cardiac and ovarian fibromas that stud the syndrome."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "It joins the inherited tumor-and-skin syndromes: like Cowden, Gorlin is a single-gene disorder announced by characteristic skin and developmental signs and a lifelong, organ-spanning tumor risk, distinguished by its gene and its tumor pattern."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "A second hit speeds the basal cell carcinoma: CDKN2A loss is among the cooperating mutations, beyond the germline PTCH1 defect, that let Gorlin's basal cell carcinomas progress to invasive tumors."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Gorlin grows a tumor in the heart: cardiac fibromas are a recognized feature, and a large one can obstruct flow or trigger arrhythmia and heart failure, so cardiac imaging is part of the syndrome's surveillance."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Radiation is hazardous in Gorlin: these patients are radiosensitive, and radiotherapy — whether photon or proton — can induce a crop of new basal cell carcinomas in the treated field, so it is avoided where possible (notably for their medulloblastomas)."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Hedgehog and STAT3 cooperate in its tumors: the unrestrained Hedgehog signaling of Gorlin engages STAT3 among the pathways that drive its basal cell carcinomas and medulloblastomas."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Jaw cysts and skin surgery invite infection: the odontogenic keratocysts of Gorlin can become infected, and the many excisions and reconstructions for recurrent basal cell carcinomas carry wound-infection and sepsis risk."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "The Hedgehog pathway shapes the developing brain: a subset of Gorlin patients have developmental delay and autistic features, reflecting Sonic Hedgehog's role in neurodevelopment alongside the syndrome's structural brain anomalies."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "A lifetime of skin surgery scars the body: recurrent basal cell carcinomas demand endless excisions and grafts, and radiotherapy must be avoided because it triggers more tumors, so chronic surgical wounds and poor healing accumulate."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Disfigurement and endless surveillance weigh on mood: the cumulative facial scarring from hundreds of basal cell carcinoma excisions and lifelong cancer surveillance give Gorlin syndrome a substantial psychological burden."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Repeated surgery raises the clot risk: the many operations for skin cancers, jaw cysts and any deeper tumors that Gorlin syndrome requires bring cumulative perioperative venous thromboembolism risk."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Its CNS lesions can spark seizures: Gorlin syndrome causes falx calcification and predisposes to medulloblastoma, and these intracranial abnormalities can underlie seizures."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Medulloblastoma chemo opens the lung to mold: the ~5% of Gorlin patients who develop medulloblastoma need chemotherapy whose neutropenia can let inhaled Aspergillus invade."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Endless skin-cancer surveillance breeds worry: the lifelong development of new basal cell carcinomas, the need for sun and radiation avoidance and constant monitoring foster chronic health anxiety in Gorlin syndrome."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It afflicts the jaws and its drug the gut: Gorlin syndrome causes recurrent odontogenic keratocysts of the jaws, and the hedgehog inhibitor vismodegib for multiple BCCs causes severe dysgeusia, nausea and weight loss."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its targeted drug forbids use in children: the hedgehog-pathway inhibitor vismodegib used in Gorlin syndrome causes premature epiphyseal growth-plate fusion in children and amenorrhoea in women."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can grow a tumour in the heart: Gorlin syndrome causes cardiac fibromas that, beyond heart failure, can obstruct flow and trigger arrhythmias, requiring cardiac surveillance."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Radiation is hazardous to its chest: radiotherapy induces a shower of basal cell carcinomas in the field, so it is avoided where possible, and benign lung and pleural cysts occur in the syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It seeds cysts in the kidney: renal cysts and developmental renal-tract anomalies are among the structural malformations of Gorlin syndrome."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It forms cysts in the mesentery: lymphatic and mesenteric cysts occur among the developmental anomalies of Gorlin syndrome alongside its many other lesions."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "A reciprocal childhood-brain-tumour syndrome: like DICER1 syndrome, Gorlin syndrome predisposes to medulloblastoma, the two sharing the differential of inherited paediatric brain tumours."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "A fellow skin-marker tumour syndrome: both Gorlin and Birt-Hogg-Dubé are autosomal-dominant disorders whose characteristic facial skin lesions flag an inherited tumour predisposition."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A comparator neurocutaneous syndrome: like tuberous sclerosis, Gorlin syndrome combines distinctive skin signs with brain and skeletal lesions in an autosomal-dominant pattern."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hedgehog inhibitors treat its many tumours: vismodegib and sonidegib block SMO in the constitutively active Hedgehog pathway, shrinking the multiple basal cell carcinomas of Gorlin syndrome."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It carves cysts into bone: Gorlin syndrome produces odontogenic keratocysts that erode the jaw and skeletal anomalies like bifid ribs, hallmarks alongside its skin tumours."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Radiation must be avoided: because Gorlin patients are radiosensitive and radiation induces new basal cell carcinomas, chemotherapy is preferred for their medulloblastomas."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "When Hedgehog blockade fails the skin: cemiplimab and other PD-1 checkpoint inhibitors are used for advanced basal cell carcinoma that progresses on or cannot tolerate Hedgehog inhibitors—an option relevant to Gorlin patients with many aggressive BCCs."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Two routes to skin cancer: Gorlin syndrome drives countless basal cell carcinomas through germline PTCH1/Hedgehog activation largely independent of sun exposure, unlike melanoma, whose UV-driven mutational burden makes it immunotherapy-responsive."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Two dominant hamartoma syndromes, two pathways: Gorlin (PTCH1, Hedgehog) and Peutz-Jeghers (STK11, mTOR) are both autosomal-dominant cancer-predisposition syndromes with distinctive lesions, showing how separate developmental pathways each predispose to tumours."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Two medulloblastoma syndromes: Gorlin syndrome causes SHH-subgroup medulloblastoma while FAP (via Turcot) causes the WNT subgroup—two germline routes to the same childhood brain tumour through different pathways."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Cardiac fibroma: Gorlin syndrome causes benign fibromas within the myocardium, a characteristic if uncommon feature detected on cardiac imaging."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Inherited cardiac-tumour syndromes: Gorlin causes cardiac fibromas and Carney complex causes cardiac myxomas—two autosomal-dominant syndromes each marked by a benign heart tumour."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Inherited skin-cancer syndromes: like Bloom syndrome, Gorlin predisposes to numerous skin cancers (basal cell carcinomas), though through Hedgehog activation rather than Bloom's defective DNA repair."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Cognition after childhood brain tumour: Gorlin's medulloblastoma and the craniospinal radiation treating it injure the hippocampus, deficits worsened by Gorlin's radiation hypersensitivity—so RT is avoided when possible."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Cancer-predisposing genodermatoses: Gorlin and the progeroid Werner syndrome both raise cancer risk with characteristic skin findings, examples of single-gene disorders that reshape lifelong tumour surveillance."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Hedgehog-Notch crosstalk: Notch signalling intersects with the Hedgehog pathway in Gorlin's basal cell carcinomas and medulloblastomas, where it can act as a context-dependent tumour suppressor."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo cooperation: the Hippo effector YAP cooperates with constitutive Hedgehog signalling to drive proliferation in the basal cell carcinomas and medulloblastomas of Gorlin syndrome."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K crosstalk and resistance: PTEN loss activates PI3K-AKT signalling that cooperates with Hedgehog and contributes to resistance against SMO inhibitors in Gorlin-related tumours."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Hedgehog target: GLI-driven Hedgehog signalling from PTCH1 loss upregulates MYC (and MYCN), driving the proliferation of the basal cell carcinomas and medulloblastomas of Gorlin syndrome."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic cooperation: EZH2-mediated PRC2 silencing of tumour-suppressor genes cooperates with Hedgehog activation in the tumours of Gorlin syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the growing tumours of Gorlin syndrome drives the VEGF angiogenesis that supports their expansion."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibroma fibroblasts: PDGF-driven fibroblast proliferation underlies the cardiac and ovarian fibromas characteristic of Gorlin syndrome, the benign mesenchymal tumours beyond its Hedgehog-driven cancers."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK crosstalk: RAS-RAF-ERK signalling cross-talks with the Hedgehog pathway in Gorlin tumours and is a bypass route to resistance when SMO inhibitors are used for its basal cell carcinomas."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor cooperation: IGF-1 signalling cooperates with Hedgehog activation in the SHH-subgroup medulloblastomas of Gorlin syndrome, supporting their proliferation."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radiation paradox: Hedgehog-driven BCL-2 suppresses caspase-3 apoptosis in Gorlin tumours, and radiotherapy is avoided because it paradoxically induces hundreds of new basal cell carcinomas within the radiation field."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Medulloblastoma RB pathway: the SHH-subgroup medulloblastomas of Gorlin children engage the RB cell-cycle pathway, the proliferative machinery downstream of the constitutive Hedgehog signalling that PTCH1 loss unleashes."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Keratocyst epithelium: EGFR-driven epithelial proliferation underlies the odontogenic keratocysts of the jaw that are an early and characteristic manifestation of Gorlin syndrome, alongside its basal cell carcinomas."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Ectopic calcification: lamellar calcification of the falx cerebri and other ectopic calcification, along with skeletal anomalies like bifid ribs, are diagnostic features of Gorlin syndrome, reflecting the role of Hedgehog signalling in skeletal patterning."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy for BCC: when the multiple basal cell carcinomas of Gorlin syndrome become advanced or Hedgehog-inhibitor-resistant, the PD-1 inhibitor cemiplimab unleashes perforin-mediated cytotoxic T-cell killing of the UV-mutated tumours."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Jaw bone remodelling: the odontogenic keratocysts of Gorlin syndrome expand by RANKL-driven osteoclastic resorption of the surrounding jaw bone, the bone destruction that makes them locally aggressive and prone to recurrence."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Hedgehog-driven cycle: GLI transactivates cyclin-D (cyclin-D1 already mapped), which partners CDK4/6 to drive the proliferation of the basal-cell carcinomas and medulloblastomas of Gorlin syndrome."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Restriction-point release: CDK4/6-cyclin-D1 phosphorylates RB (mapped) to free E2F1, the proliferative output of constitutive Hedgehog signalling in Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Pathway cooperation: PI3K-AKT-mTOR signalling (AKT, mTOR and PTEN already mapped) cooperates with Hedgehog activation and contributes to resistance to SMO inhibitors such as vismodegib in Gorlin basal-cell carcinomas."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Hedgehog crosstalk: RAS-MAPK signalling (ERK1/2 already mapped) crosstalks with the Hedgehog pathway and is implicated in resistance to SMO inhibitors in the basal-cell carcinomas of Gorlin syndrome."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "UV oxidative defence: NRF2 antioxidant defence counters the ultraviolet oxidative stress that, with constitutive Hedgehog signalling, drives the multiple basal-cell carcinomas of Gorlin syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Tumour-promoting inflammation: IL-6-STAT3 signalling (STAT3 already mapped) contributes a tumour-promoting inflammatory input to the neoplasms of Gorlin syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), providing a proliferative and inflammatory input to the tumours of Gorlin syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling crosstalks with Hedgehog (PTCH1/SMO/SUFU mapped) and shapes the stroma of the basal cell carcinomas and odontogenic keratocysts of Gorlin syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates tumour-cell survival and the stromal microenvironment of the neoplasms of Gorlin syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the basal cell carcinomas and medulloblastomas of Gorlin syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the Hedgehog-driven tumours of Gorlin syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the survival and oxidative-stress signalling of the proliferating cells of the Hedgehog-driven tumours of Gorlin syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates GLI and β-catenin stability (SHH/SMO and WNT-β-catenin already mapped), modulating the Hedgehog-driven tumorigenesis of Gorlin syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the basal cell carcinomas and medulloblastomas of Gorlin syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory stroma of the Hedgehog-driven tumors of Gorlin syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the Hedgehog-driven tumors of Gorlin syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of Gorlin syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of the Hedgehog-driven cells of Gorlin syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of Gorlin syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of Gorlin syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Gorlin syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of Gorlin syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Gorlin syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of Gorlin syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Gorlin syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of Gorlin syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment of Gorlin syndrome (calcineurin-inhibitor immunosuppression is a recognized basal-cell-carcinoma risk factor)."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune surveillance: MHC class II-restricted T-cell surveillance limits the many basal cell carcinomas of Gorlin syndrome, and immunosuppression (calcineurin already mapped) accelerates them, while antigen presentation underlies checkpoint therapy of advanced tumours."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint therapy: the numerous basal cell carcinomas of Gorlin syndrome that resist or escape Hedgehog inhibitors (SMO already mapped) can respond to PD-1 checkpoint blockade, offering an alternative for advanced disease."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Hedgehog-inhibitor resistance: the AXL receptor tyrosine kinase and other non-canonical signalling can bypass SMO blockade, contributing to the vismodegib resistance that limits Hedgehog-inhibitor therapy of Gorlin-syndrome basal cell carcinomas."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the microenvironment of the many basal cell carcinomas of Gorlin syndrome dampens anti-tumour immunity (PD-1 already mapped), part of the immune evasion relevant to the checkpoint therapy of advanced lesions."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac fibromas: benign cardiac fibromas are a feature of Gorlin syndrome, and when they involve the myocardium or provoke arrhythmia, troponin elevation can mark the associated cardiac injury."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying the basal cell carcinomas and other tumours of Gorlin syndrome, part of their stromal microenvironment."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Hedgehog-lipid link: cholesterol and its oxysterol derivatives activate Smoothened (already mapped), the driver of the Hedgehog pathway (PTCH1 already mapped) whose constitutive activity from PTCH1 loss causes the tumours of Gorlin syndrome."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative UV damage: ultraviolet exposure generates reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage exacerbates the basal cell carcinomas of the sun-exposed skin in Gorlin syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the stroma of the basal cell carcinomas of Gorlin syndrome, part of their immune-evasive niche."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the stroma of the multiple basal cell carcinomas of Gorlin syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and skin: copper is the cofactor of lysyl oxidase that cross-links the dermal collagen (already mapped), part of the skin biology disturbed by the multiple basal cell carcinomas of Gorlin syndrome."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "UV eicosanoids: ultraviolet exposure induces cyclooxygenase-2 and prostaglandin E2 in the skin, promoting the inflammation and immunosuppression of the photocarcinogenesis that drives the basal cell carcinomas of Gorlin syndrome."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and cutaneous defence: zinc supports the immune and antioxidant function of the skin against the UV (prostaglandins already mapped) photocarcinogenesis that drives the multiple basal cell carcinomas of Gorlin syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium antioxidant defence: selenium supports the antioxidant selenoprotein defence of the skin against the UV oxidative (NFE2L2 already mapped) photocarcinogenesis of Gorlin syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Overgrowth adipokine: leptin reflects the macrosomia and large body habitus (with the macrocephaly) that are part of the developmental overgrowth phenotype of Gorlin syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Overgrowth adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the macrosomia and overgrowth phenotype of Gorlin syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic/overgrowth phenotype of Gorlin syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "BCC antigen presentation: the dendritic cells present the UV-neoantigens of the multiple basal cell carcinomas (already mapped) of Gorlin syndrome, the immune surveillance of the Hedgehog (SMO already mapped)-driven tumours."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity against the multiple BCCs (already mapped) and medulloblastoma of Gorlin syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Hedgehog-driven Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Hedgehog-driven Gorlin-syndrome tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the Gorlin-syndrome tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the Hedgehog-driven Gorlin-syndrome tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the Gorlin-syndrome tumour stroma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the Gorlin-syndrome tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the Gorlin-syndrome tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the SHH-driven (PTCH1/SMO already mapped) proliferating cells of the Gorlin-syndrome tumours."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-Gorlin axis: TSLP, from PTCH1-mutant (already mapped) skin and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the SHH-driven BCCs (already mapped) of Gorlin syndrome."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-Gorlin axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies vascular permeability and the inflammatory stroma of the BCCs (already mapped) and odontogenic keratocysts of Gorlin syndrome."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-Gorlin axis: erythropoietin, via the EPOR on the PTCH1-mutant (already mapped) tumour cells, activates the PI3K/AKT (already mapped) survival axis and modulates macrophage (already mapped) polarisation in the tumour microenvironment of Gorlin-syndrome basal-cell carcinomas."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-Gorlin axis: histamine, released by mast cells in the BCC and odontogenic-keratocyst stroma of Gorlin syndrome, signals via H1/H2 receptors on PTCH1-mutant (already mapped) tumour cells, promoting SHH-driven (already mapped) proliferation and angiogenesis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-Gorlin axis: melatonin, via MT1/MT2 receptors on PTCH1-mutant (already mapped) tumour cells, suppresses SHH/GLI (already mapped) signalling, promotes apoptosis, and modulates the DNA-repair response to the UV-induced (already mapped) mutagenesis of Gorlin-syndrome BCCs."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-Gorlin axis: testosterone, via androgen receptor signalling on PTCH1-mutant (already mapped) BCC and medulloblastoma (already mapped) cells, modulates SHH-driven (already mapped) proliferation and the male sex bias in Gorlin-syndrome tumour burden and aggressiveness."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Gorlin prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Gorlin oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Gorlin vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Gorlin serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Gorlin iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Gorlin sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Gorlin magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Gorlin potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Gorlin iron: iron, via ferritin in macrophages (already mapped) and mast cells (already mapped), fuels cell proliferation; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Gorlin chloride: chloride channels on macrophages (already mapped) and mast cells (already mapped) regulate ionic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Gorlin sulfur: glutathione from sulfur amino acids in macrophages (already mapped) and mast cells (already mapped) counters ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Gorlin nitrogen: nitric oxide from iNOS in macrophages (already mapped) and mast cells (already mapped) modulates tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Gorlin carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels Hedgehog-driven proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Gorlin hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Gorlin pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses Hedgehog-driven tumour immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Gorlin glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Gorlin angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Gorlin smad4: SMAD4 in macrophages (already mapped) and fibroblasts (already mapped) mediates TGF-β signalling; smad4 dysregulation amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome."
---

# Gorlin Syndrome

## Overview

**Gorlin syndrome** (also called **Nevoid Basal Cell Carcinoma Syndrome, NBCCS**, or **Basal Cell Nevus Syndrome, BCNS**) is an autosomal dominant hereditary cancer predisposition syndrome caused by germline pathogenic variants in **PTCH1** (~85% of cases), **PTCH2** (~5%), or **SUFU** (~2%). PTCH1 (Patched 1) was identified as the Gorlin syndrome gene by Hahn et al. and Johnson et al. in 1996. Gorlin syndrome is characterized by a triad of **multiple basal cell carcinomas (BCCs)** (appearing from puberty in sun-exposed skin), **odontogenic keratocysts (OKCs)** of the jaw, and skeletal anomalies. Additional features include **calcification of the falx cerebri**, rib anomalies, macrocephaly, and a ~5% lifetime risk of **medulloblastoma** (particularly the desmoplastic/nodular subtype). Gorlin syndrome affects approximately **1 in 40,000-60,000** individuals globally [^hahn-1996-gorlin-ptch1] [^bree-2011-gorlin-guidelines].

**Gorlin syndrome diagnostic criteria (Kimonis 1997 modified by Evans 2010) — requires 2 major or 1 major + 2 minor:**

**Major criteria:**
1. ≥5 BCCs before age 30 (or ≥1 BCC before age 20)
2. Odontogenic keratocyst (OKC) of the jaw (histologically confirmed)
3. ≥3 palmar/plantar pits
4. Ectopic calcification of falx cerebri (in patient <20 years)
5. Bilamellar calcification of falx cerebri (any age)
6. Medulloblastoma (desmoplastic/nodular type)
7. First-degree relative with Gorlin syndrome

**Minor criteria:**
- Rib anomalies (bifid, fused, splayed, missing)
- Other skeletal anomalies: macrocephaly, frontal bossing, Sprengel deformity, short 4th metacarpal
- Congenital malformations: cleft lip/palate, polydactyly, cardiac fibroma
- Lymphomesenteric/pleural cysts
- Falx cerebri calcification (>age 20, early age strengthens specificity)
- Ovarian fibroma

## Structure

### Genetic basis

- **PTCH1 gene** (chromosome 9q22.32): 23 exons; transmembrane receptor with sterol-sensing domain; 1447 aa
- **Mutation spectrum**: truncating variants (~65%: frameshift, nonsense, splice); missense (~25%); large deletions (~10%); essentially all pathogenic variants cause LOF
- **De novo rate**: ~40-50% of Gorlin cases arise from de novo PTCH1 mutations
- **Penetrance**: nearly complete for BCCs (in skin-exposed population, especially Caucasians); OKC ~70%; falx calcification ~80% by 40; medulloblastoma ~5% overall
- **Phenotypic variability**: within families, BCC number ranges from 1 to thousands; modifier genes and UV exposure modify BCC penetrance dramatically; ethnic variation: Gorlin in Black/Asian patients has fewer BCCs but same OKC/medulloblastoma risk
- **SUFU germline**: see SUFU entry; mainly desmoplastic medulloblastoma predisposition with fewer BCCs

### NF1-PTCH1 pathway in HH signaling

The NF1 (Neurofibromin) and PTCH1 pathways are analogous suppressors:
- NF1: suppresses RAS-MAPK via RAS-GAP
- PTCH1: suppresses Hedgehog pathway by inhibiting SMO

Both are two-hit tumor suppressors: germline heterozygous LOF + somatic second hit in tumor cell. Somatic LOH at 9q22 (PTCH1) detectable in OKC, BCCs, and medulloblastoma from Gorlin patients.

## Function

### Clinical manifestations

**Basal cell carcinomas (BCCs):**
- In PTCH1-Gorlin patients: onset in 2nd-3rd decade; hundreds to thousands of BCCs in fair-skinned individuals; BCCs are morphologically similar to sporadic BCC (nodular, superficial, basosquamous); rarely metastatic (<0.1%) but locally destructive
- Distribution: sun-exposed skin (face, chest, back); but also periorbital (non-sun-exposed) and on palm/sole skin (uncommon in sporadic BCC)
- Radiation-induced BCCs: ionizing radiation (even diagnostic X-ray) can induce massive BCC proliferation in Gorlin patients (>50× increase); medulloblastoma treatment with EBRT historically caused devastating facial BCC induction → now EBRT avoided in Gorlin patients
- UV radiation: accelerates BCC formation; rigorous sun protection (SPF 50+, UV clothing) is primary prevention

**Odontogenic keratocysts (OKCs) / Keratocystic odontogenic tumors (KCOTs):**
- Present in ~70% of Gorlin patients; often the first or only manifestation
- Location: typically maxilla/mandible; multilocular; contain keratinized contents; recur after simple enucleation (~60% recurrence rate); treatment: curettage + peripheral ostectomy, or Carnoy's solution devitalization, or marsupialization
- OKC cell of origin: odontogenic epithelium; driven by HH pathway activation; GLI1 overexpression in OKC lining
- OKC vs dentigerous cyst vs lateral periodontal cyst: histological distinction requires biopsy; Gorlin-associated OKC has same histology as sporadic OKC but more likely to be multiple

**Calcification of falx cerebri:**
- Present in ~80% of Gorlin adults; often radiographic hallmark; bilateral, "eggshell" or lamellar pattern; can appear in teenagers; falx calcification itself is benign (no neurological consequence) but is a diagnostic clue; also seen in tuberous sclerosis, pseudohypoparathyroidism, Sturge-Weber — but pattern in Gorlin is distinct (bilateral, early, lamellar)

**Skeletal anomalies:**
- Rib anomalies (bifid, fused, splayed): ~60% — best visualized on chest PA radiograph
- Macrocephaly with frontal/temporal bossing: ~50%
- Short 4th metacarpal (Gorlin's anomaly): ~50%; can be mistaken for pseudopseudohypoparathyroidism
- Kyphoscoliosis: ~10-15%

**Cardiac fibroma:**
- Benign cardiac tumor (fibroblastic, non-contractile); ~2-3% of Gorlin patients; may cause arrhythmia or heart failure; found in infants and children; treated by surgical resection when symptomatic; rare: cardiac rhabdomyoma (more TSC-associated)

**Ovarian fibroma:**
- ~20% of female Gorlin patients; bilateral (pathognomonic); calcified; distinct from sporadic ovarian fibroma; benign (fibroma, not fibrosarcoma) but may cause Meigs syndrome (ascites, pleural effusion)

**Medulloblastoma:**
- ~5% of Gorlin patients; the desmoplastic/nodular histologic subtype predominates (SHH subgroup); typically early childhood (median age 2-3 years for Gorlin-associated MB vs 7-8 years for sporadic MB)
- PTCH1-Gorlin MB: responds to HH pathway inhibition (vismodegib — pediatric trials); but avoid RT → EBRT now contraindicated in young children with Gorlin-associated MB → CSF chemotherapy (high-dose vincristine/cisplatin/etoposide-based protocols used instead)
- SUFU-germline MB: same SHH-desmoplastic/nodular; similar avoidance of RT; SMO inhibitors not effective in SUFU-null tumors

## Pathology

### Surveillance and management

**BCC management:**
- Annual full-skin exam by dermatologist from puberty (or earlier if BCCs present)
- Topical treatments: imiquimod (toll-like receptor agonist → immune activation → BCC regression); topical 5-fluorouracil; photodynamic therapy (PDT)
- **Vismodegib (Erivedge)**: FDA-approved for locally advanced or metastatic BCC; approved for reducing BCC burden in Gorlin syndrome patients (STEVIE trial: 28% complete response, median duration ~3 months after discontinuation; maintenance dosing explored); teratogenic (Category X); drug holiday protocols; sonidegib (Odomzo) also approved for locally advanced BCC
- Hedgehog inhibitor adverse effects: muscle cramps (~70%), alopecia, dysgeusia, weight loss, GI; teratogenicity → strict contraception required
- Surgery: excision, Mohs micrographic surgery for periocular and high-risk areas
- Radiation: absolutely contraindicated in Gorlin patients (even palliative RT) due to massive radiation-induced BCC induction

**Medulloblastoma in Gorlin:**
- MRI brain at diagnosis and annually in childhood (if desmoplastic/nodular MB in family → intensified protocol)
- Treatment of Gorlin-MB: surgery + chemotherapy (avoid EBRT); infant MB protocols; HH inhibitors in relapsed/refractory PTCH1-mutant SHH-MB

**OKC surveillance:**
- Annual or biannual panoramic dental X-rays (OPG) from age 8 until 40-50
- Orthopantomogram starting early in pediatric patients

**Skeletal/eye:**
- Chest X-ray: rib anomalies (single study at diagnosis)
- Ophthalmologic exam: coloboma, glaucoma (uncommon but reported)

**Genetic:**
- 50% offspring risk; prenatal/preimplantation testing available
- Testing: PTCH1 + PTCH2 + SUFU sequencing + MLPA for large deletions

## Connections

- `connects-to` → **[SUFU](../../03-molecular/sufu/README.md)** — Germline SUFU causes Gorlin-like syndrome: desmoplastic/nodular medulloblastoma risk (SHH subgroup, age <5) is higher than PTCH1-Gorlin; BCC and OKC are less penetrant; radiation avoidance is critical; SUFU loss releases GLI constitutively in cerebellar granule progenitors.
- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — Germline PTCH1 loss causes Gorlin syndrome via constitutive Hedgehog pathway activation; PTCH1 normally inhibits SMO; loss → SMO constitutively active → GLI1/2 nuclear → BCC, OKC, calcified falx, rib anomalies; somatic PTCH1 mutation is the most common driver of sporadic BCC.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — Vismodegib and sonidegib (SMO inhibitors) are FDA-approved for Gorlin-syndrome BCC; SMO constitutively active in PTCH1/SUFU-mutant tumors; GLI1 suppression → BCC regression; acquired SMO resistance mutations (D473H) occur with extended vismodegib therapy.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Gorlin patients develop BCCs early (teens-20s in sun-exposed skin); ionizing and UV radiation dramatically accelerate BCC; vismodegib reduces BCC from 2-4/month to near-zero (STEVIE/BOLT trials); radiation avoidance is critical to prevent radiation field BCC induction.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Gorlin syndrome confers ~5% medulloblastoma risk (SHH desmoplastic/nodular subtype); median age 2-3 years vs 7-8 for sporadic SHH-MB; EBRT contraindicated (radiation-induced BCC proliferation); SMO inhibitors active in relapsed PTCH1-mutant SHH-MB; chemotherapy-only standard.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — GLI1/2 transcribe VEGF-A in BCC → tumour angiogenesis; BCC is among the most vascularised skin tumours; vismodegib (SMO inhibitor) reduces GLI → ↓VEGF-A → ↓tumour vascularity; bevacizumab shows limited single-agent BCC activity; VEGF-C/D also upregulated in BCC microenvironment.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — BCCs arise from basal keratinocytes (hair follicle bulge stem cells) with PTCH1-constrained hedgehog; UV/radiation exposure → PTCH1 somatic second hits → BCC induction at highest rates in sun-exposed skin; rigorous sun protection is primary prevention in Gorlin syndrome.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Beyond skin and brain, Gorlin syndrome produces benign fibroblastic tumors — cardiac fibromas and ovarian fibromas — reflecting Hedgehog's role in mesenchymal cell fate; these fibromas, with calcified falx and jaw keratocysts, are part of the diagnostic criteria.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 cooperates with Hedgehog activation in Gorlin tumorigenesis: germline PTCH1 loss derepresses SMO/GLI, but UV-induced TP53 mutation removes the apoptotic brake, accelerating the basal cell carcinomas — the same two-hit cooperation seen in sporadic BCC.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Hedgehog hyperactivation links Gorlin syndrome to rare childhood mesenchymal tumors: fetal rhabdomyoma and embryonal rhabdomyosarcoma occur at elevated rates, since GLI drive promotes myogenic progenitor proliferation — part of the developmental-tumor spectrum of PTCH1 loss.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Gorlin syndrome predisposes to meningioma: constitutive hedgehog activation from germline PTCH1 loss—the same pathway driving its basal cell carcinomas and medulloblastomas—also raises meningioma risk, compounded by any prior craniospinal radiotherapy.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Gorlin syndrome's skeletal stigmata reflect hedgehog control of osteoblasts: bifid/splayed ribs, vertebral anomalies, frontal bossing, and a calcified falx cerebri arise because PTCH1 loss dysregulates the hedgehog signaling that patterns bone, aiding radiographic diagnosis.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Cardiac fibroma is a hallmark Gorlin tumor: a benign fibrous mass growing within the myocardium among cardiomyocytes, it is the commonest heart tumor of childhood and, when present, strongly suggests an underlying PTCH1 hedgehog-pathway syndrome.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Gorlin and Li-Fraumeni are both dominant cancer-predisposition syndromes via different pathways: Gorlin from PTCH1/Hedgehog loss (BCCs, medulloblastoma), Li-Fraumeni from germline TP53 loss (sarcomas, breast, brain)—one disinhibits Hedgehog, the other removes p53.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Gorlin and neurofibromatosis type 1 are both dominant phakomatoses where a tumor-suppressor loss causes multisystem tumors: Gorlin's PTCH1 loss unleashes Hedgehog (BCCs, jaw cysts), NF1's neurofibromin loss unleashes Ras (neurofibromas, optic glioma)—similar logic.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Ovarian fibromas are a diagnostic feature of Gorlin syndrome: PTCH1 loss and unchecked Hedgehog signaling spur these benign, often bilateral calcified ovarian tumors—reminding that Hedgehog dysregulation drives growths well beyond skin and brain.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiation is hazardous in Gorlin syndrome: because PTCH1 loss primes skin to hedgehog-driven tumors, radiotherapy triggers hundreds of basal cell carcinomas in the treated field, so X-ray exposure is minimized—a sharp caution when these patients have medulloblastoma.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Gorlin's hedgehog defect intersects with Wnt in medulloblastoma: SHH-subtype medulloblastoma (driven by PTCH1/SMO) is distinct from the Wnt-subtype, and pathway crosstalk shapes which tumors arise—so Gorlin predisposes specifically to SHH, not Wnt, medulloblastoma.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Gorlin syndrome causes congenital eye anomalies: hypertelorism, congenital cataracts, colobomas and strabismus are part of the developmental phenotype of PTCH1 loss, reflecting hedgehog signaling's role in eye morphogenesis alongside the syndrome's tumor risk.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Gorlin syndrome floods the skin with basal cell carcinomas: PTCH1 loss unleashes Hedgehog signaling so that dozens to hundreds of BCCs arise from youth, plus palmar-plantar pits—making the integumentary system the syndrome's most visible burden.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Gorlin syndrome leaves skeletal fingerprints: odontogenic keratocysts of the jaw, bifid ribs, vertebral anomalies and a calcified falx are diagnostic skeletal features, so a dental or skeletal survey often helps confirm this Hedgehog-pathway syndrome.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Gorlin syndrome predisposes the developing nervous system to medulloblastoma: Hedgehog-pathway activation drives this childhood cerebellar tumor, so affected infants need brain surveillance—and radiation must be used cautiously given their extreme BCC radiosensitivity.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium deposits are a Gorlin diagnostic clue: lamellar calcification of the falx cerebri and other ectopic calcifications are among its major criteria, reflecting how disrupted hedgehog signaling alters bone and soft-tissue mineralization.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Gorlin syndrome reaches the reproductive system: bilateral ovarian fibromas—often calcified—are characteristic, so a young woman with ovarian masses plus skin and jaw findings may carry the PTCH1 mutation behind the syndrome.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Gorlin syndrome shapes the brain structurally: macrocephaly with frontal bossing, a bridged sella turcica, and developmental anomalies accompany the tumor risk, so congenital brain malformations are part of the syndrome alongside its cancers.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — Gorlin's tumors grow because Hedgehog switches on MYCN: unchecked PTCH1/SMO signaling activates GLI, which drives MYCN to fuel the SHH-subtype medulloblastomas and basal cell carcinomas that define the syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Gorlin's basal cell carcinomas escape Hedgehog blockers via mTOR: when vismodegib shuts down smoothened, tumors can reactivate growth through mTOR and other bypass pathways, a key reason these cancers eventually resist targeted therapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Gorlin's many basal cell carcinomas exploit regulatory T cells: Tregs help the tumors evade immune clearance, which is why PD-1 checkpoint therapy (cemiplimab) is used for advanced BCCs that progress despite Hedgehog inhibitors.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Hedgehog signaling teams with NF-kB in Gorlin's tumors: the constitutive Hedgehog drive cooperates with NF-kB inflammatory signaling to promote the survival and growth of the syndrome's many basal cell carcinomas.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill the stroma of Gorlin's basal cell carcinomas: tumor-associated macrophages support angiogenesis and dampen immunity around the Hedgehog-driven skin tumors, helping the lesions persist and recur.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Ultraviolet oxygen chemistry compounds Gorlin's tumor risk: on top of the inherited Hedgehog defect, sun-driven reactive oxygen species damage skin-cell DNA, so UV exposure markedly multiplies the basal cell carcinomas these patients develop.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Gorlin syndrome can grow tumors in the heart: cardiac fibromas, benign fibrous masses, are a recognized feature, sometimes found in childhood and occasionally disturbing the heart's rhythm or flow.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Gorlin's benign tumors are made of fibrous tissue: cardiac and ovarian fibromas are overgrowths of fibroblasts and collagen, part of the syndrome's broad tendency to form hamartomatous fibrous masses.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Gorlin syndrome calcifies with calcium phosphate: a calcified falx cerebri, along with skeletal anomalies like bifid ribs, are diagnostic clues, the mineral laid down where it should not be.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Gorlin's brain tumor is medulloblastoma: it arises from cerebellar granule-neuron precursors that depend on the very Hedgehog signal the syndrome unleashes, so children are screened with brain MRI.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Unleashed Hedgehog drives Gorlin's tumors through cyclin D1: the pathway switches on this cell-cycle gene, pushing basal cells and granule precursors to proliferate into BCCs and medulloblastomas.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Gorlin sprouts cysts beyond the jaw: mesenteric and other abdominal cysts occur alongside its odontogenic keratocysts, part of the syndrome's broad tendency to form benign cavities.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads Gorlin's lesions: the palisaded basaloid cells of its many basal cell carcinomas and the thin, corrugated lining of its odontogenic keratocysts both reflect the runaway Hedgehog signaling that PTCH1 loss unleashes.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Gorlin warps the bones: odontogenic keratocysts hollow out the jaw, and bifid ribs, vertebral anomalies, and a calcified falx betray the syndrome on a skeletal survey of the marrow-bearing bones.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Gorlin's skeletal defects reach the chest: bifid, splayed, or fused ribs deform the thoracic cage around the lungs, one of the bony anomalies that, with jaw cysts and skin signs, point to the diagnosis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Immunotherapy helps the heaviest BCC burden: when Gorlin patients sprout too many basal cell carcinomas for surgery, the anti-PD-1 antibody cemiplimab can be used alongside the hedgehog-pathway inhibitors that target the underlying defect.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Gorlin grows collagen-rich fibrous tumors: the cardiac fibroma and ovarian fibroma characteristic of the syndrome are dense whorls of fibroblasts and collagen, benign masses found on the imaging screening it requires.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The hedgehog-blocking drugs upset the gut: vismodegib and sonidegib commonly cause nausea, loss of appetite, and taste change, side effects that — with muscle cramps and hair loss — limit how long patients can take them.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Tumors escape hedgehog blockade through other pathways: PI3K-AKT signaling crosstalks with the hedgehog axis and helps Gorlin's basal cell carcinomas grow resistant to SMO inhibitors like vismodegib, a route to relapse being targeted with combination therapy.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — The jaw cysts eat into bone: Gorlin's odontogenic keratocysts expand through the mandible and maxilla by recruiting osteoclasts to resorb bone, the painless swellings that often bring a young patient to diagnosis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy is a fallback for the rare aggressive case: when a basal cell carcinoma turns advanced or metastatic and outruns hedgehog inhibitors, anti-PD-1 drugs like cemiplimab unleash cytotoxic T cells against it.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Hedgehog keeps the tumor cell from dying: unchecked GLI signaling raises the anti-apoptotic protein BCL-2 in Gorlin's basal cell carcinomas and medulloblastomas, helping the cells survive that the syndrome's mutation sets loose.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Hedgehog also builds the tumor's blood supply: SHH signaling drives endothelial recruitment and angiogenesis, feeding the basal cell carcinomas and the cardiac and ovarian fibromas that stud the syndrome.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — It joins the inherited tumor-and-skin syndromes: like Cowden, Gorlin is a single-gene disorder announced by characteristic skin and developmental signs and a lifelong, organ-spanning tumor risk, distinguished by its gene and its tumor pattern.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — A second hit speeds the basal cell carcinoma: CDKN2A loss is among the cooperating mutations, beyond the germline PTCH1 defect, that let Gorlin's basal cell carcinomas progress to invasive tumors.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Gorlin grows a tumor in the heart: cardiac fibromas are a recognized feature, and a large one can obstruct flow or trigger arrhythmia and heart failure, so cardiac imaging is part of the syndrome's surveillance.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Radiation is hazardous in Gorlin: these patients are radiosensitive, and radiotherapy — whether photon or proton — can induce a crop of new basal cell carcinomas in the treated field, so it is avoided where possible (notably for their medulloblastomas).
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Hedgehog and STAT3 cooperate in its tumors: the unrestrained Hedgehog signaling of Gorlin engages STAT3 among the pathways that drive its basal cell carcinomas and medulloblastomas.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Jaw cysts and skin surgery invite infection: the odontogenic keratocysts of Gorlin can become infected, and the many excisions and reconstructions for recurrent basal cell carcinomas carry wound-infection and sepsis risk.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — The Hedgehog pathway shapes the developing brain: a subset of Gorlin patients have developmental delay and autistic features, reflecting Sonic Hedgehog's role in neurodevelopment alongside the syndrome's structural brain anomalies.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — A lifetime of skin surgery scars the body: recurrent basal cell carcinomas demand endless excisions and grafts, and radiotherapy must be avoided because it triggers more tumors, so chronic surgical wounds and poor healing accumulate.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Disfigurement and endless surveillance weigh on mood: the cumulative facial scarring from hundreds of basal cell carcinoma excisions and lifelong cancer surveillance give Gorlin syndrome a substantial psychological burden.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Repeated surgery raises the clot risk: the many operations for skin cancers, jaw cysts and any deeper tumors that Gorlin syndrome requires bring cumulative perioperative venous thromboembolism risk.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Its CNS lesions can spark seizures: Gorlin syndrome causes falx calcification and predisposes to medulloblastoma, and these intracranial abnormalities can underlie seizures.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Medulloblastoma chemo opens the lung to mold: the ~5% of Gorlin patients who develop medulloblastoma need chemotherapy whose neutropenia can let inhaled Aspergillus invade.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Endless skin-cancer surveillance breeds worry: the lifelong development of new basal cell carcinomas, the need for sun and radiation avoidance and constant monitoring foster chronic health anxiety in Gorlin syndrome.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It afflicts the jaws and its drug the gut: Gorlin syndrome causes recurrent odontogenic keratocysts of the jaws, and the hedgehog inhibitor vismodegib for multiple BCCs causes severe dysgeusia, nausea and weight loss.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its targeted drug forbids use in children: the hedgehog-pathway inhibitor vismodegib used in Gorlin syndrome causes premature epiphyseal growth-plate fusion in children and amenorrhoea in women.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can grow a tumour in the heart: Gorlin syndrome causes cardiac fibromas that, beyond heart failure, can obstruct flow and trigger arrhythmias, requiring cardiac surveillance.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Radiation is hazardous to its chest: radiotherapy induces a shower of basal cell carcinomas in the field, so it is avoided where possible, and benign lung and pleural cysts occur in the syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It seeds cysts in the kidney: renal cysts and developmental renal-tract anomalies are among the structural malformations of Gorlin syndrome.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It forms cysts in the mesentery: lymphatic and mesenteric cysts occur among the developmental anomalies of Gorlin syndrome alongside its many other lesions.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — A reciprocal childhood-brain-tumour syndrome: like DICER1 syndrome, Gorlin syndrome predisposes to medulloblastoma, the two sharing the differential of inherited paediatric brain tumours.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — A fellow skin-marker tumour syndrome: both Gorlin and Birt-Hogg-Dubé are autosomal-dominant disorders whose characteristic facial skin lesions flag an inherited tumour predisposition.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A comparator neurocutaneous syndrome: like tuberous sclerosis, Gorlin syndrome combines distinctive skin signs with brain and skeletal lesions in an autosomal-dominant pattern.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hedgehog inhibitors treat its many tumours: vismodegib and sonidegib block SMO in the constitutively active Hedgehog pathway, shrinking the multiple basal cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It carves cysts into bone: Gorlin syndrome produces odontogenic keratocysts that erode the jaw and skeletal anomalies like bifid ribs, hallmarks alongside its skin tumours.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Radiation must be avoided: because Gorlin patients are radiosensitive and radiation induces new basal cell carcinomas, chemotherapy is preferred for their medulloblastomas.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — When Hedgehog blockade fails the skin: cemiplimab and other PD-1 checkpoint inhibitors are used for advanced basal cell carcinoma that progresses on or cannot tolerate Hedgehog inhibitors—an option relevant to Gorlin patients with many aggressive BCCs.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Two routes to skin cancer: Gorlin syndrome drives countless basal cell carcinomas through germline PTCH1/Hedgehog activation largely independent of sun exposure, unlike melanoma, whose UV-driven mutational burden makes it immunotherapy-responsive.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Two dominant hamartoma syndromes, two pathways: Gorlin (PTCH1, Hedgehog) and Peutz-Jeghers (STK11, mTOR) are both autosomal-dominant cancer-predisposition syndromes with distinctive lesions, showing how separate developmental pathways each predispose to tumours.
- `connects-to` → **[FAP](../fap/README.md)** — Two medulloblastoma syndromes: Gorlin syndrome causes SHH-subgroup medulloblastoma while FAP (via Turcot) causes the WNT subgroup—two germline routes to the same childhood brain tumour through different pathways.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Cardiac fibroma: Gorlin syndrome causes benign fibromas within the myocardium, a characteristic if uncommon feature detected on cardiac imaging.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Inherited cardiac-tumour syndromes: Gorlin causes cardiac fibromas and Carney complex causes cardiac myxomas—two autosomal-dominant syndromes each marked by a benign heart tumour.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — Inherited skin-cancer syndromes: like Bloom syndrome, Gorlin predisposes to numerous skin cancers (basal cell carcinomas), though through Hedgehog activation rather than Bloom's defective DNA repair.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Cognition after childhood brain tumour: Gorlin's medulloblastoma and the craniospinal radiation treating it injure the hippocampus, deficits worsened by Gorlin's radiation hypersensitivity—so RT is avoided when possible.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Cancer-predisposing genodermatoses: Gorlin and the progeroid Werner syndrome both raise cancer risk with characteristic skin findings, examples of single-gene disorders that reshape lifelong tumour surveillance.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Hedgehog-Notch crosstalk: Notch signalling intersects with the Hedgehog pathway in Gorlin's basal cell carcinomas and medulloblastomas, where it can act as a context-dependent tumour suppressor.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo cooperation: the Hippo effector YAP cooperates with constitutive Hedgehog signalling to drive proliferation in the basal cell carcinomas and medulloblastomas of Gorlin syndrome.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PI3K crosstalk and resistance: PTEN loss activates PI3K-AKT signalling that cooperates with Hedgehog and contributes to resistance against SMO inhibitors in Gorlin-related tumours.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Hedgehog target: GLI-driven Hedgehog signalling from PTCH1 loss upregulates MYC (and MYCN), driving the proliferation of the basal cell carcinomas and medulloblastomas of Gorlin syndrome.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic cooperation: EZH2-mediated PRC2 silencing of tumour-suppressor genes cooperates with Hedgehog activation in the tumours of Gorlin syndrome.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the growing tumours of Gorlin syndrome drives the VEGF angiogenesis that supports their expansion.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Fibroma fibroblasts: PDGF-driven fibroblast proliferation underlies the cardiac and ovarian fibromas characteristic of Gorlin syndrome, the benign mesenchymal tumours beyond its Hedgehog-driven cancers.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK crosstalk: RAS-RAF-ERK signalling cross-talks with the Hedgehog pathway in Gorlin tumours and is a bypass route to resistance when SMO inhibitors are used for its basal cell carcinomas.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor cooperation: IGF-1 signalling cooperates with Hedgehog activation in the SHH-subgroup medulloblastomas of Gorlin syndrome, supporting their proliferation.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Hedgehog-driven BCL-2 suppresses caspase-3 apoptosis in Gorlin tumors, and radiotherapy is specifically avoided because it paradoxically induces hundreds of new basal cell carcinomas within the irradiated field.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The SHH-subgroup medulloblastomas of Gorlin children engage the RB cell-cycle pathway, the proliferative machinery downstream of the constitutive Hedgehog signaling that germline PTCH1 loss unleashes in the cerebellum.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR-driven epithelial proliferation underlies the odontogenic keratocysts of the jaw that are an early and characteristic manifestation of Gorlin syndrome, often preceding the basal cell carcinomas.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Lamellar calcification of the falx cerebri and other ectopic calcification, along with skeletal anomalies like bifid ribs, are diagnostic features of Gorlin syndrome, reflecting the role of Hedgehog signaling in skeletal patterning.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — When the multiple basal cell carcinomas of Gorlin syndrome become advanced or Hedgehog-inhibitor-resistant, the PD-1 inhibitor cemiplimab unleashes perforin-mediated cytotoxic T-cell killing of the UV-mutated tumors.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — The odontogenic keratocysts of Gorlin syndrome expand by RANKL-driven osteoclastic resorption of the surrounding jaw bone, the bone destruction that makes them locally aggressive and prone to recurrence.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — GLI transactivates cyclin-D (cyclin-D1 already mapped), which partners CDK4/6 to drive the proliferation of the basal-cell carcinomas and medulloblastomas of Gorlin syndrome.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — CDK4/6-cyclin-D1 phosphorylates RB (mapped) to free E2F1, the proliferative output of constitutive Hedgehog signaling in Gorlin-syndrome tumors.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT, mTOR and PTEN already mapped) cooperates with Hedgehog activation and contributes to resistance to SMO inhibitors such as vismodegib in Gorlin basal-cell carcinomas.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) crosstalks with the Hedgehog pathway and is implicated in resistance to SMO inhibitors in the basal-cell carcinomas of Gorlin syndrome.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the ultraviolet oxidative stress that, with constitutive Hedgehog signaling, drives the multiple basal-cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) contributes a tumor-promoting inflammatory input to the neoplasms of Gorlin syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), providing a proliferative and inflammatory input to the tumors of Gorlin syndrome.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling crosstalks with Hedgehog (PTCH1/SMO/SUFU mapped) and shapes the stroma of the basal cell carcinomas and odontogenic keratocysts of Gorlin syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates tumor-cell survival and the stromal microenvironment of the neoplasms of Gorlin syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the basal cell carcinomas and medulloblastomas of Gorlin syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the Hedgehog-driven tumors of Gorlin syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the survival and oxidative-stress signaling of the proliferating cells of the Hedgehog-driven tumors of Gorlin syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates GLI and β-catenin stability (SHH/SMO and WNT-β-catenin already mapped), modulating the Hedgehog-driven tumorigenesis of Gorlin syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the basal cell carcinomas and medulloblastomas of Gorlin syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory stroma of the Hedgehog-driven tumors of Gorlin syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the Hedgehog-driven tumors of Gorlin syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of Gorlin syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of the Hedgehog-driven cells of Gorlin syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of Gorlin syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of Gorlin syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Gorlin syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of Gorlin syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Gorlin syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of Gorlin syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Gorlin syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of Gorlin syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment of Gorlin syndrome (calcineurin-inhibitor immunosuppression is a recognized basal-cell-carcinoma risk factor).
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune surveillance: MHC class II-restricted T-cell surveillance limits the many basal cell carcinomas of Gorlin syndrome, and immunosuppression (calcineurin already mapped) accelerates them, while antigen presentation underlies checkpoint therapy of advanced tumours.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint therapy: the numerous basal cell carcinomas of Gorlin syndrome that resist or escape Hedgehog inhibitors (SMO already mapped) can respond to PD-1 checkpoint blockade, offering an alternative for advanced disease.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Hedgehog-inhibitor resistance: the AXL receptor tyrosine kinase and other non-canonical signalling can bypass SMO blockade, contributing to the vismodegib resistance that limits Hedgehog-inhibitor therapy of Gorlin-syndrome basal cell carcinomas.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the microenvironment of the many basal cell carcinomas of Gorlin syndrome dampens anti-tumour immunity (PD-1 already mapped), part of the immune evasion relevant to the checkpoint therapy of advanced lesions.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac fibromas: benign cardiac fibromas are a feature of Gorlin syndrome, and when they involve the myocardium or provoke arrhythmia, troponin elevation can mark the associated cardiac injury.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying the basal cell carcinomas and other tumours of Gorlin syndrome, part of their stromal microenvironment.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Hedgehog-lipid link: cholesterol and its oxysterol derivatives activate Smoothened (already mapped), the driver of the Hedgehog pathway (PTCH1 already mapped) whose constitutive activity from PTCH1 loss causes the tumours of Gorlin syndrome.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative UV damage: ultraviolet exposure generates reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage exacerbates the basal cell carcinomas of the sun-exposed skin in Gorlin syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the stroma of the basal cell carcinomas of Gorlin syndrome, part of their immune-evasive niche.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the stroma of the multiple basal cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and skin: copper is the cofactor of lysyl oxidase that cross-links the dermal collagen (already mapped), part of the skin biology disturbed by the multiple basal cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — UV eicosanoids: ultraviolet exposure induces cyclooxygenase-2 and prostaglandin E2 in the skin, promoting the inflammation and immunosuppression of the photocarcinogenesis that drives the basal cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and cutaneous defence: zinc supports the immune and antioxidant function of the skin against the UV (prostaglandins already mapped) photocarcinogenesis that drives the multiple basal cell carcinomas of Gorlin syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium antioxidant defence: selenium supports the antioxidant selenoprotein defence of the skin against the UV oxidative (NFE2L2 already mapped) photocarcinogenesis of Gorlin syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Overgrowth adipokine: leptin reflects the macrosomia and large body habitus (with the macrocephaly) that are part of the developmental overgrowth phenotype of Gorlin syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Overgrowth adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the macrosomia and overgrowth phenotype of Gorlin syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic/overgrowth phenotype of Gorlin syndrome.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — BCC antigen presentation: the dendritic cells present the UV-neoantigens of the multiple basal cell carcinomas (already mapped) of Gorlin syndrome, the immune surveillance of the Hedgehog (SMO already mapped)-driven tumours.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity against the multiple BCCs (already mapped) and medulloblastoma of Gorlin syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Hedgehog-driven Gorlin-syndrome tumours.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the Gorlin-syndrome tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Gorlin-syndrome tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Hedgehog-driven Gorlin-syndrome tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the Gorlin-syndrome tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the Hedgehog-driven Gorlin-syndrome tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the Gorlin-syndrome tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the Gorlin-syndrome tumour stroma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the Gorlin-syndrome tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the Gorlin-syndrome tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the SHH-driven (PTCH1/SMO already mapped) proliferating cells of the Gorlin-syndrome tumours.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-Gorlin axis: TSLP, from the PTCH1-mutant (already mapped) skin and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the SHH-driven basal-cell carcinomas (already mapped) and medulloblastomas (already mapped) of Gorlin syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-Gorlin axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the inflammatory stromal milieu of the basal-cell carcinomas (already mapped) and the odontogenic keratocysts of Gorlin syndrome.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-Gorlin axis: erythropoietin, via the EPOR on the PTCH1-mutant (already mapped) tumour cells, activates the PI3K/AKT (already mapped) survival axis and modulates macrophage (already mapped) polarisation in the tumour microenvironment of Gorlin-syndrome basal-cell carcinomas.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-Gorlin axis: histamine, released by mast cells in the BCC and odontogenic-keratocyst stroma of Gorlin syndrome, signals via H1/H2 receptors on PTCH1-mutant (already mapped) tumour cells, promoting SHH-driven (already mapped) proliferation and angiogenesis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-Gorlin axis: melatonin, via MT1/MT2 receptors on PTCH1-mutant (already mapped) tumour cells, suppresses SHH/GLI (already mapped) signalling, promotes apoptosis, and modulates the DNA-repair response to the UV-induced (already mapped) mutagenesis of Gorlin-syndrome BCCs.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-Gorlin axis: testosterone, via androgen receptor signalling on PTCH1-mutant (already mapped) BCC and medulloblastoma (already mapped) cells, modulates SHH-driven (already mapped) proliferation and the male sex bias in Gorlin-syndrome tumour burden and aggressiveness.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Gorlin prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Gorlin oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the TME inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Gorlin vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gorlin serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Gorlin iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Gorlin sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Gorlin magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Gorlin potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Gorlin iron: iron, via ferritin in macrophages (already mapped) and mast cells (already mapped), fuels cell proliferation; iron dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Gorlin chloride: chloride channels on macrophages (already mapped) and mast cells (already mapped) regulate ionic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Gorlin sulfur: glutathione from sulfur amino acids in macrophages (already mapped) and mast cells (already mapped) counters ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Gorlin nitrogen: nitric oxide from iNOS in macrophages (already mapped) and mast cells (already mapped) modulates tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Gorlin carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels Hedgehog-driven proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Gorlin hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Gorlin pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses Hedgehog-driven tumour immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Gorlin glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Gorlin angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Gorlin smad4: SMAD4 in macrophages (already mapped) and fibroblasts (already mapped) mediates TGF-β signalling; smad4 dysregulation amplifies Hedgehog (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of Gorlin syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hahn-1996-gorlin-ptch1]: Hahn H, Wicking C, Zaphiropoulos PG, et al. Mutations of the human homolog of Drosophila patched in the nevoid basal cell carcinoma syndrome. *Cell.* 1996;85(6):841-851. [doi:10.1016/S0092-8674(00)81268-4](https://doi.org/10.1016/S0092-8674(00)81268-4) · [PubMed 8681379](https://pubmed.ncbi.nlm.nih.gov/8681379/)
[^bree-2011-gorlin-guidelines]: Bree AF, Shah MR; BCNS Colloquium Group. Consensus statement from the first international colloquium on basal cell nevus syndrome (BCNS). *Am J Med Genet A.* 2011;155A(9):2091-2097. [doi:10.1002/ajmg.a.34128](https://doi.org/10.1002/ajmg.a.34128) · [PubMed 21834026](https://pubmed.ncbi.nlm.nih.gov/21834026/)
