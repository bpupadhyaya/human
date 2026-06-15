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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hahn-1996-gorlin-ptch1]: Hahn H, Wicking C, Zaphiropoulos PG, et al. Mutations of the human homolog of Drosophila patched in the nevoid basal cell carcinoma syndrome. *Cell.* 1996;85(6):841-851. [doi:10.1016/S0092-8674(00)81268-4](https://doi.org/10.1016/S0092-8674(00)81268-4) · [PubMed 8681379](https://pubmed.ncbi.nlm.nih.gov/8681379/)
[^bree-2011-gorlin-guidelines]: Bree AF, Shah MR; BCNS Colloquium Group. Consensus statement from the first international colloquium on basal cell nevus syndrome (BCNS). *Am J Med Genet A.* 2011;155A(9):2091-2097. [doi:10.1002/ajmg.a.34128](https://doi.org/10.1002/ajmg.a.34128) · [PubMed 21834026](https://pubmed.ncbi.nlm.nih.gov/21834026/)
