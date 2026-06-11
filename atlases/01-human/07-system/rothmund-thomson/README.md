---
schema: human-scale-entry/v1
id: rothmund-thomson
name: Rothmund-Thomson Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Rothmund-Thomson syndrome is caused by biallelic RECQL4 mutations; poikiloderma (onset 3-6 months), skeletal abnormalities, juvenile cataracts; ~30% osteosarcoma risk (peak age 11-14 years); SCE not elevated; management centers on osteosarcoma surveillance."
aliases: ["Rothmund-Thomson syndrome", "Rothmund-Thomson", "RTS syndrome", "RECQL4 syndrome", "Rothmund Thomson poikiloderma", "Rothmund-Thomson osteosarcoma", "RTS osteosarcoma", "Rothmund-Thomson RECQL4", "poikiloderma with osteosarcoma"]
sources:
  - id: kitao-1999-recql4-rts
    type: peer-reviewed
    cite: "Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. Nat Genet. 1999;22(1):82-84."
    doi: "10.1038/8788"
    pmid: "10319867"
    url: "https://doi.org/10.1038/8788"
  - id: wang-2003-rts-cancer
    type: peer-reviewed
    cite: "Wang LL, Gannavarapu A, Kozinetz CA, et al. Association between osteosarcoma and deleterious mutations in the RECQL4 gene in Rothmund-Thomson syndrome. J Natl Cancer Inst. 2003;95(9):669-674."
    doi: "10.1093/jnci/95.9.669"
    pmid: "12734318"
    url: "https://doi.org/10.1093/jnci/95.9.669"
cross_links:
  - target: 01-human/03-molecular/recql4
    relation: connects-to
    note: "Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma)."
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Rothmund-Thomson syndrome (RECQL4 LOF) and Werner syndrome (WRN LOF) are both RecQ helicase disorders: Rothmund-Thomson presents in infancy with poikiloderma and osteosarcoma risk; Werner syndrome presents in the 3rd decade with progeroid features, sarcomas, and atherosclerosis."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Rothmund-Thomson type II carries a ~30% lifetime osteosarcoma risk peaking at age 11-14; RECQL4 replication stress accelerates the same RB1 and TP53 loss that causes sporadic OS, so whole-body MRI surveillance runs through skeletal maturity."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Poikiloderma is the defining feature of Rothmund-Thomson, beginning at 3-6 months as cheek erythema then evolving into mottled pigmentation, telangiectasia, and atrophy; it is photo-exacerbated (sun protection) but, unlike xeroderma pigmentosum, does not cause skin cancer."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "RECQL4 loss inflicts replication stress on the rapidly dividing osteoblast precursors of the adolescent growth plate → double-strand breaks → biallelic RB1 and TP53 inactivation → osteosarcoma, the same transformation as sporadic OS but reached one to two decades early."
---

# Rothmund-Thomson Syndrome

## Overview

**Rothmund-Thomson syndrome (RTS)** is a rare autosomal recessive **chromosomal instability and cancer predisposition syndrome** caused by biallelic loss-of-function mutations in **RECQL4** (8q24.12), encoding a RecQ helicase required for DNA replication initiation and mitochondrial DNA integrity. RTS was first described by August Rothmund in 1868 (poikiloderma congenitale with juvenile cataracts) and by Matthew Thomson in 1936 (congenital poikiloderma). The RECQL4 gene was identified as the cause by Kitao et al. in 1999. RTS is classified into two types based on the presence of osteosarcoma risk: **RTS type II** (biallelic RECQL4 mutations; poikiloderma + osteosarcoma risk) is the classic form, while **RTS type I** (no RECQL4 mutations; poikiloderma without osteosarcoma) has incompletely characterized genetics [^kitao-1999-recql4-rts].

The cardinal features of RTS type II are: (1) **poikiloderma** — the defining skin eruption — beginning as erythema and edema of the cheeks at 3-6 months of age, progressing to mottled hypo/hyperpigmentation, telangiectasias, and skin atrophy over the face, extremities, and buttocks; (2) **skeletal abnormalities**, particularly radial ray defects (hypoplastic or absent radius/thumb) and short stature; (3) **juvenile cataracts** (bilateral, cortical/posterior subcapsular, onset in first decade); and (4) **~30% lifetime osteosarcoma risk**, the dominant life-threatening feature. Unlike Bloom syndrome (SCE elevated ~10x) and Werner syndrome (SCE elevated ~2-3x), **SCE is NOT elevated** in RTS — a key cytogenetic distinguishing feature. Worldwide prevalence is <1/500,000; approximately 300 patients have been documented in the literature [^wang-2003-rts-cancer].

**RTS vs. related RecQ helicase syndromes:**

| Feature | RTS (RECQL4) | Bloom Syndrome (BLM) | Werner Syndrome (WRN) |
|---|---|---|---|
| Onset | Infancy (3-6 months) | Birth | 3rd decade |
| SCE | Not elevated | ~10x elevated | ~2-3x elevated |
| Skin | Poikiloderma | Sun-sensitive telangiectasia | Scleroderma-like, ulcers |
| Cancer risk | Osteosarcoma (~30%) | Pan-cancer | Sarcomas, melanoma, thyroid |
| Skeletal | Radial ray defects, short stature | Short stature (uniform) | Osteoporosis (adult) |
| Cataracts | Juvenile (1st decade) | Not typical | Adult (3rd decade, diagnostic) |
| Immunodeficiency | No | Yes (IgA/IgM low) | Mild |

## Structure

### Genetic basis of Rothmund-Thomson syndrome

**RECQL4 gene (8q24.12):**
- 21 exons; 1,208 aa; 133 kDa; ubiquitously expressed in proliferating tissues
- All RTS-causing mutations are biallelic LOF: nonsense, frameshift, missense in the helicase core (abolish ATPase/helicase activity), and splice site mutations
- No clear hot spot; mutations distributed throughout the helicase domain; compound heterozygotes predominate in non-consanguineous families
- Genotype-phenotype correlation is imperfect: mutations in the helicase core are most consistently associated with osteosarcoma risk; mutations closer to N-terminus or C-terminus may have less severe helicase LOF

**RECQL4 mutation spectrum and associated syndromes:**
- RTS type II: helicase core missense, truncating mutations → classic syndrome with poikiloderma + osteosarcoma
- RAPADILINO syndrome: splice site c.1390+2T>C (Finnish founder) → exon 7 skipping → partial LOF → radial/patellar anomalies without poikiloderma; lower osteosarcoma risk (~8%)
- Baller-Gerold syndrome: some cases with RECQL4 biallelic mutations → craniosynostosis + radial aplasia; poikiloderma may or may not be present
- These three syndromes form an allelic spectrum; phenotypic overlap is substantial

**Cellular pathology of RECQL4 LOF:**
- Replication defect: RECQL4-deficient cells show reduced origin firing → compensatory activation of dormant origins → prolonged S-phase → sensitivity to replication stress (hydroxyurea, aphidicolin)
- Chromosomal instability: elevated chromosomal rearrangements (deletions, translocations) without elevated SCE (distinguishes from BLM/WRN)
- Mitochondrial dysfunction: reduced mtDNA copy number; elevated mitochondrial ROS → accelerated mitochondrial aging; contributes to premature aging features in older RTS patients
- SCE: NOT elevated (distinguishing from BLM where SCE ~10x; from WRN where SCE ~2-3x); normal SCE rules out Bloom syndrome and substantially against Werner syndrome as the diagnosis in an RTS-like presentation

## Function

### Clinical features of Rothmund-Thomson syndrome

**Poikiloderma — the defining feature:**
- Onset at 3-6 months of age as erythema and bullae/edema on the cheeks; often initially mistaken for contact dermatitis or systemic lupus
- Over 1-2 years: progresses to classic **poikiloderma**: triad of skin atrophy, mottled hypo- and hyperpigmentation (giving a "marbled" or "mottled" appearance), and telangiectasias
- Distribution: face (cheeks, nose, forehead, chin); spreads to arms, hands, legs; trunk and torso less commonly affected; palms/soles often spared
- Photo-exacerbated: UVA and UVB exposure worsens erythema and telangiectasias; photoprotection from infancy
- NOT associated with photodamage (no actinic keratosis, no basal/squamous cell carcinoma from UV); distinguish from xeroderma pigmentosum and Cockayne syndrome
- Poikiloderma is stable or slowly progressive after childhood; not life-threatening but can be cosmetically significant

**Skeletal abnormalities:**
- **Radial ray defects**: hypoplasia or aplasia of the radius; hypoplastic or absent thumb; may be unilateral or bilateral; often the presenting birth defect; range from mild radial hypoplasia to complete absence with distal limb involvement
- **Short stature**: below 3rd percentile in most RTS patients; intrauterine growth restriction in some; NOT growth hormone-deficient; GH treatment rarely effective
- **Osteoporosis/osteopenia**: premature bone loss in adolescence and adulthood; vertebral compression fractures in some; replication defect in osteoblast precursors → reduced bone accretion
- Patellar hypoplasia/aplasia: seen in RAPADILINO overlap; may occur in RTS
- Dental anomalies: microdontia, malformed crowns, delayed eruption

**Juvenile bilateral cataracts:**
- Onset in first decade (earlier than Werner syndrome which presents in 3rd decade; earlier than normal aging cataracts)
- Cortical or posterior subcapsular pattern; bilateral; can cause significant visual impairment by adolescence
- Management: phacoemulsification + IOL implantation; excellent visual outcomes
- Present in ~50% of classic RTS type II patients; absence does not exclude diagnosis

**Other features:**
- Hair and adnexal: sparse scalp hair, eyebrows, and eyelashes; may be patchy; alopecia in some
- Nail dystrophy: brittle, hypoplastic nails
- Normal intelligence: cognitive development typically unaffected
- Hypogonadism: reduced fertility in females; males typically fertile (contrast with Bloom syndrome where male azoospermia is near-universal)
- No immunodeficiency: serum immunoglobulins normal; T-cell function intact (contrast with Bloom syndrome)

### Osteosarcoma in Rothmund-Thomson syndrome

**Epidemiology:**
- **~30% lifetime osteosarcoma risk** in RTS type II (RECQL4 biallelic LOF) — among the highest for any single-gene cancer predisposition syndrome for osteosarcoma
- Wang et al. (2003) systematic analysis: 41% of RTS patients with helicase-domain RECQL4 mutations developed osteosarcoma vs. 0% with non-helicase-domain mutations [^wang-2003-rts-cancer]
- Peak age of diagnosis: **11-14 years** (during the adolescent growth spurt — parallel to sporadic osteosarcoma peak)
- Sites: distal femur, proximal tibia, proximal humerus — same distribution as sporadic osteosarcoma
- Often **multifocal** at presentation; metastatic disease at diagnosis (~20-25%)

**Pathogenesis:**
- RECQL4 LOF → replication stress in rapidly proliferating osteoblast precursors → DSBs → LOH at RB1 and TP53 → biallelic inactivation → osteoblast transformation
- Same molecular events (RB1 LOH, TP53 mutation) as sporadic osteosarcoma — RECQL4 LOF accelerates their occurrence by 10-20 years
- Osteosarcoma histology: high-grade osteoblastic, chondroblastic, or fibroblastic; indistinguishable from sporadic on pathology; requires RECQL4 germline testing for RTS diagnosis

**Treatment:**
- Standard MAP chemotherapy regimen (methotrexate, doxorubicin, cisplatin) + surgical resection with limb salvage where possible
- Chemotherapy in RTS: RECQL4 LOF may alter drug sensitivity (unvalidated in clinical trials); consult sarcoma oncology center with RTS expertise
- Radiation: avoid if possible (underlying chromosomal instability may increase radiation sensitivity)
- Prognosis: 5-year OS ~60-70% (comparable to sporadic osteosarcoma); multifocal disease carries worse prognosis
- Recurrence after primary resection: same surveillance as sporadic osteosarcoma (CT chest every 3 months for 2 years)

## Pathology

### Diagnosis

**Diagnostic approach:**
1. **Clinical**: poikiloderma with classic onset (3-6 months), radial ray defects, juvenile cataracts, short stature, family history → suspect RTS
2. **Cytogenetics**: SCE assay — NOT elevated (normal SCE rules out Bloom syndrome; ~2-3x elevated would suggest Werner syndrome)
3. **Molecular confirmation**: RECQL4 sequencing + MLPA; compound heterozygous LOF mutations in helicase domain = RTS type II; confirm with parental testing
4. **Skin biopsy**: characteristic poikilodermatous changes (dermal fibrosis, epidermal atrophy, dermal hemosiderin, dilated superficial vessels); supports but does not confirm diagnosis

**Diagnostic criteria (Vennos & James 1995, modified):**
- **Required**: poikiloderma (onset in infancy/early childhood)
- **Supporting**: RECQL4 biallelic mutations; osteosarcoma; radial ray defect; juvenile cataracts; short stature; sparse hair; normal SCE

**Differential diagnosis:**
- Bloom syndrome: SCE ~10x elevated, NO poikiloderma (telangiectatic erythema different pattern), no skeletal malformations
- Werner syndrome: adult onset, scleroderma-like (not classic poikiloderma), cataracts in 3rd decade
- Kindler syndrome (FERMT1): acral blistering in infancy → poikiloderma; photosensitivity; no osteosarcoma
- Dyskeratosis congenita (DKC1/TERT/TERC): reticulate skin pigmentation (not classic poikiloderma), nail dystrophy, oral leukoplakia, bone marrow failure; telomere shortening
- Fanconi anemia: café-au-lait spots, bone marrow failure, FA gene panel; radial ray defects overlap
- IBIDS/PIBI(D)S (trichothiodystrophy, ERCC2/3): tiger-tail hair (sulfur-poor), ichthyosis, brittle hair; poikiloderma not typical
- Poikiloderma of Kindler vs. RTS: FERMT1 sequencing; onset pattern; blistering
- Ataxia-telangiectasia: cerebellar ataxia, IgA deficiency, telangiectasias of conjunctivae (not skin poikiloderma); ATM mutations

**Cancer surveillance protocol:**
- **Osteosarcoma**: clinical assessment at every visit (bone pain, joint swelling, limp) — from diagnosis; annual whole-body MRI from time of RTS diagnosis (~6 months) until skeletal maturity (~18-20 years); then symptom-directed evaluation
- **Skin**: annual dermatological exam; photoprotection advice and SPF 50+ sunscreen
- **Ophthalmology**: annual eye exam from diagnosis; cataract management
- Avoid excessive radiation exposure: minimize diagnostic CT; use MRI for osteosarcoma surveillance
- No proven benefit of routine cross-sectional imaging for non-osteosarcoma cancers in RTS (other cancer risks are lower than osteosarcoma)

**Management:**
- Photoprotection: strict UVA/UVB protection (SPF 50+ sunscreen, UPF clothing, sun avoidance) from infancy; reduces poikiloderma progression and sun-induced erythema
- Orthopedics: radial ray malformations → occupational therapy, adaptive devices; surgical correction in severe radial aplasia (centralization procedures); fracture management for osteoporosis
- Ophthalmology: phacoemulsification for cataracts; prompt referral at first sign of visual impairment
- Dental: dental anomaly monitoring; early orthodontic evaluation
- Genetic counseling: AR inheritance; sibling recurrence 1/4; prenatal diagnosis by CVS/amniocentesis; cascade testing for siblings; no current role for RECQL4 carrier screening in general population
- Research registries: International Rothmund-Thomson Syndrome Registry (biolgen.com); multi-institutional collaboration for rare syndrome research

## Connections

- `connects-to` → **[RECQL4](../../03-molecular/recql4/README.md)** — Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma).
- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma.
- `connects-to` → **[Werner Syndrome](../../07-system/werner-syndrome/README.md)** — Rothmund-Thomson syndrome (RECQL4 LOF) and Werner syndrome (WRN LOF) are both RecQ helicase disorders: Rothmund-Thomson presents in infancy with poikiloderma and osteosarcoma risk; Werner syndrome presents in the 3rd decade with progeroid features, sarcomas, and atherosclerosis.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Rothmund-Thomson type II carries a ~30% lifetime osteosarcoma risk peaking at age 11-14; RECQL4 replication stress accelerates the same RB1 and TP53 loss that causes sporadic OS, so whole-body MRI surveillance runs through skeletal maturity.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Poikiloderma is the defining feature of Rothmund-Thomson, beginning at 3-6 months as cheek erythema then evolving into mottled pigmentation, telangiectasia, and atrophy; it is photo-exacerbated (sun protection) but, unlike xeroderma pigmentosum, does not cause skin cancer.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — RECQL4 loss inflicts replication stress on the rapidly dividing osteoblast precursors of the adolescent growth plate → double-strand breaks → biallelic RB1 and TP53 inactivation → osteosarcoma, the same transformation as sporadic OS but reached one to two decades early.

[^kitao-1999-recql4-rts]: Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. *Nat Genet.* 1999;22(1):82-84. [doi:10.1038/8788](https://doi.org/10.1038/8788) · [PubMed 10319867](https://pubmed.ncbi.nlm.nih.gov/10319867/)
[^wang-2003-rts-cancer]: Wang LL, Gannavarapu A, Kozinetz CA, et al. Association between osteosarcoma and deleterious mutations in the RECQL4 gene in Rothmund-Thomson syndrome. *J Natl Cancer Inst.* 2003;95(9):669-674. [doi:10.1093/jnci/95.9.669](https://doi.org/10.1093/jnci/95.9.669) · [PubMed 12734318](https://pubmed.ncbi.nlm.nih.gov/12734318/)
