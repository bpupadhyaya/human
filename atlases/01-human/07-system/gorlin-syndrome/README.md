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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hahn-1996-gorlin-ptch1]: Hahn H, Wicking C, Zaphiropoulos PG, et al. Mutations of the human homolog of Drosophila patched in the nevoid basal cell carcinoma syndrome. *Cell.* 1996;85(6):841-851. [doi:10.1016/S0092-8674(00)81268-4](https://doi.org/10.1016/S0092-8674(00)81268-4) · [PubMed 8681379](https://pubmed.ncbi.nlm.nih.gov/8681379/)
[^bree-2011-gorlin-guidelines]: Bree AF, Shah MR; BCNS Colloquium Group. Consensus statement from the first international colloquium on basal cell nevus syndrome (BCNS). *Am J Med Genet A.* 2011;155A(9):2091-2097. [doi:10.1002/ajmg.a.34128](https://doi.org/10.1002/ajmg.a.34128) · [PubMed 21834026](https://pubmed.ncbi.nlm.nih.gov/21834026/)
