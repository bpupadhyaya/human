---
schema: human-scale-entry/v1
id: retinoblastoma
name: Retinoblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Retinoblastoma is the most common intraocular childhood tumor (1/15,000); bilateral = germline RB1; unilateral = usually somatic; leukocoria is the classic presentation; intra-arterial/intravitreal chemotherapy preserves vision; hereditary RB1 confers osteosarcoma risk."
aliases: ["retinoblastoma", "RB1 tumor", "bilateral retinoblastoma", "hereditary retinoblastoma", "RBL", "retinoblastoma leukocoria", "intraocular tumor child", "retinoblastoma treatment", "retinoblastoma genetics"]
sources:
  - id: shields-2008-retinoblastoma
    type: peer-reviewed
    cite: "Shields CL, Shields JA. Retinoblastoma management: advances in enucleation, intravenous chemoreduction, and intra-arterial chemotherapy. Curr Opin Ophthalmol. 2010;21(3):203-212."
    doi: "10.1097/ICU.0b013e328338676a"
    pmid: "20224400"
    url: "https://doi.org/10.1097/ICU.0b013e328338676a"
  - id: knudson-1971-two-hit
    type: peer-reviewed
    cite: "Knudson AG Jr. Mutation and cancer: statistical study of retinoblastoma. Proc Natl Acad Sci USA. 1971;68(4):820-823."
    doi: "10.1073/pnas.68.4.820"
    pmid: "5279523"
    url: "https://doi.org/10.1073/pnas.68.4.820"
cross_links:
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Biallelic RB1 loss is the universal initiating event in retinoblastoma; hereditary (bilateral) = germline RB1 + somatic LOH; sporadic (unilateral) = two somatic RB1 hits; MYCN amplification is an alternative RB-independent driver in a rare subset."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 pathway is bypassed in retinoblastoma via MDM2 amplification, MDM4 overexpression, or MYCN amplification; p53 pathway loss allows retinal progenitors to survive RB1 LOF-driven E2F1 pro-apoptotic signaling; TP53 mutations are rare in primary retinoblastoma."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Hereditary RB1 carriers have 30-50× risk of osteosarcoma as a second malignancy; radiation exposure dramatically amplifies this risk — external beam RT now avoided in hereditary RB; germline RB1 is found in ~3-5% of sporadic osteosarcomas."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Retinoblastoma is the most common intraocular tumor of childhood, presenting as leukocoria (white pupillary reflex) or strabismus; globe-sparing therapy — intra-arterial and intravitreal chemotherapy — salvages most eyes, reserving enucleation for advanced (Group E) disease."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "A small (~2%) RB1-wildtype subset of retinoblastoma is instead driven by massive MYCN amplification, which raises CCNE1/CDK2 to hyperphosphorylate Rb and release E2F1 despite intact RB1; these aggressive, non-hereditary tumors are harder to salvage than RB1-mutant ones."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Retinoblastoma must neutralize the p53 apoptosis that RB1 loss would otherwise trigger: MDM2 amplification (~4%) and MDM4 overexpression (~65%) degrade or inhibit p53, so TP53 itself is rarely mutated — making MDM2/MDM4 antagonists a rational therapeutic strategy."
---

# Retinoblastoma

## Overview

**Retinoblastoma** is the most common primary **intraocular malignancy of childhood**, arising from immature retinal progenitor cells of the inner nuclear layer. It occurs in approximately **1 in 15,000-20,000** live births worldwide and accounts for ~3% of all childhood cancers. Retinoblastoma is the paradigmatic tumor for **Knudson's two-hit hypothesis** (1971): the observation that bilateral (hereditary) retinoblastoma required both germline and somatic RB1 inactivation, while unilateral (sporadic) retinoblastoma required two independent somatic hits in the same cell, established the concept of tumor suppressor gene LOF. Retinoblastoma occurs in two forms: **bilateral/hereditary (~40%)** from germline RB1 pathogenic variants, and **unilateral/sporadic (~60%)** from somatic biallelic RB1 inactivation. Modern therapy has transformed retinoblastoma from a blinding and frequently lethal disease to one with >95% overall survival and high rates of globe salvage [^knudson-1971-two-hit] [^shields-2008-retinoblastoma].

**Retinoblastoma characteristics by hereditary status:**

| Feature | Bilateral (hereditary) | Unilateral (usually sporadic) |
|---|---|---|
| Genetic basis | Germline RB1 + somatic LOH | Two somatic RB1 hits |
| Frequency | ~40% of all retinoblastoma | ~60% of all retinoblastoma |
| Age at diagnosis | Median 12-15 months | Median 24-30 months |
| Laterality | Bilateral, often multifocal | Unilateral, unifocal |
| Second malignancy risk | 30-50× elevated | Not elevated above population |
| De novo germline | ~25% of hereditary cases | — |
| Offspring risk | 50% (autosomal dominant) | <1% (germline test negative) |

## Structure

### RB1 gene and protein biology

**RB1 gene (13q14.2):**
- 200 kb, 27 exons; encodes 928 aa (110 kDa) pRb protein
- Germline pathogenic variant spectrum: truncating variants (frameshift ~35%, nonsense ~20%, splice ~15%); missense in conserved pocket residues (~20%); large deletions (MLPA required, ~10%)
- De novo germline: ~25% of bilateral cases; test both parents
- Penetrance: nearly 100% for bilateral retinoblastoma in germline RB1 carriers; ~10% of germline RB1 carriers develop only unilateral (incomplete penetrance)
- Low-penetrance alleles: missense at Arg552 (R552Q), splice-site variants with partial exon skipping, deep intronic variants → reduced pRb expression → incomplete penetrance; risk of unilateral retinoblastoma + reduced second cancer risk

**MYCN-amplified retinoblastoma:**
- ~2% of retinoblastoma (predominantly unilateral sporadic); RB1 wildtype at diagnosis; MYCN amplification (50-200× copies) drives retinal progenitor proliferation via a different mechanism; aggressive histology; less globe-salvageable than RB1-mutant tumors; genetic counseling: not hereditary (germline MYCN not found)
- Represents an RB-independent mechanism of retinoblastoma: CDK2-CyclinE hyperactivation secondary to MYCN (which activates CCNE1) → Rb hyperphosphorylation → E2F1 release despite intact RB1

### Tumor biology

**Cell of origin:** inner nuclear layer retinal progenitor cells (RPC) in the retina; these mitotically active cells in fetal/early postnatal retina require Rb for exit from the cell cycle; Rb depletion → RPCs cannot exit proliferation → tumor formation. Specifically, cone precursors (identified by Rb−/− mouse models and gene expression) appear most susceptible; human retinoblastoma expresses cone photoreceptor markers (RXRγ, IRBPα, OPN1MW/LW).

**Molecular alterations beyond RB1:**
- **MDM2 amplification** (~4%): suppresses E2F1-induced p53-dependent apoptosis
- **MDM4 overexpression** (~65%): MDM4 (MDMX) inhibits p53 independently of MDM2; the most common mechanism by which retinoblastoma bypasses E2F1-induced apoptosis
- **MYCN amplification** (~2%; see above)
- **CDK4 amplification** (~2%): bypasses Rb if RB1 wild-type
- Genome is otherwise relatively quiet (few mutations); retinoblastoma is genomically simple compared to adult carcinomas; anaplastic retinoblastoma (rare) has copy number gains in 2p, 6p, 13q gain with additional TP53 mutations

## Function

### Clinical presentation and staging

**Leukocoria (white pupillary reflex):** the classic presenting sign; caused by the white tumor mass seen through the pupil; first noticed in photographs (loss of red-eye reflex on one side); median age at diagnosis ~12-18 months (bilateral) or ~24-30 months (unilateral)

**Other presentations:**
- Strabismus (esotropia or exotropia): tumor disrupts foveal fixation
- Vision loss: less commonly noticed in infants; detected on developmental assessment
- Proptosis: indicates extraocular extension; poor prognostic sign
- Glaucoma, uveitis: late or advanced presentation
- Orbital and systemic metastasis: bone marrow, CSF, lymph nodes — uncommon in high-income countries but common at diagnosis in resource-limited settings (presenting with systemic disease in ~10% globally)

**International Intraocular Retinoblastoma Classification (IIRC), Groups A-E:**
- **Group A**: small tumors (≤3 mm), away from fovea and disc, no vitreous/subretinal seeding → focal therapy (laser, cryotherapy)
- **Group B**: larger tumors or subfoveal/juxtapapillary location, no seeding → primary chemotherapy + focal
- **Group C**: focal vitreous or subretinal seeding → systemic or intra-arterial chemotherapy
- **Group D**: diffuse vitreous or subretinal seeding → intra-arterial + intravitreal chemotherapy; globe salvage possible but challenging
- **Group E**: extensive tumor, neovascular glaucoma, opaque media, tumor anterior to anterior vitreous face → enucleation often required

## Pathology

### Treatment modalities

**1. Systemic chemotherapy (chemoreduction):**
Standard regimen: **vincristine + carboplatin + etoposide (VCE)**, 6 cycles; reduces tumor size → enables focal consolidation; primary treatment for bilateral disease; long-term ototoxicity risk from carboplatin (audiologic monitoring)

**2. Intra-arterial chemotherapy (IAC) — ophthalmic artery chemosurgery:**
- Interventional neuroradiology: selective catheterization of ophthalmic artery via femoral approach → melphalan ± carboplatin ± topotecan infused directly into the eye
- Globe salvage rates: Group D eyes: ~60-80% globe retention with IAC vs ~30-40% historically; transformative advance since ~2008
- Advantages: high intravitreal drug concentration, minimal systemic exposure; Disadvantages: arterial risk (stroke, occlusion, rare); radiation exposure of procedure; not suitable for all anatomies
- Bilateral IAC: sequential sessions, one eye per session

**3. Intravitreal chemotherapy (IVitC):**
- Direct injection into vitreous: melphalan (20-30 μg) ± topotecan; specifically treats vitreous seeding (Group C/D)
- Historically avoided due to extraocular spread risk → now performed with safety protocols (avoidance of reflux, immediate cryotherapy of injection site)
- Melphalan kills both clonal and floating seed tumor cells in vitreous cavity
- Combined with IAC for vitreous disease: highest salvage for Group D

**4. Focal therapy (consolidation):**
- **Laser photocoagulation (diode laser, 810 nm)**: direct ablation of small tumors + tumoral blood supply; used after chemoreduction
- **Transpupillary thermotherapy (TTT)**: lower energy laser → hyperthermia → tumor cell death
- **Cryotherapy**: double freeze-thaw cycles; for anterior tumors ≤4 mm

**5. External beam radiotherapy (EBRT):**
- Highly effective (95%+ local control) but **avoided in hereditary retinoblastoma** due to dramatically increased second malignancy risk in the radiation field (20-50× osteosarcoma/STS in irradiated orbits in hereditary RB patients)
- Reserved for: failed all globe-preserving options, unresectable extraocular extension; only when absolutely necessary
- Proton therapy: can minimize scatter to orbit, reducing but not eliminating secondary cancer risk

**6. Enucleation:**
- Removal of the globe; curative for the treated eye; standard for Group E, unilateral disease with no useful vision, or failed globe-preserving therapy
- High-quality prosthetic eye; no visual rehabilitation possible in enucleated eye
- Pathological examination of enucleation specimen: assess optic nerve resection margin, choroidal invasion (>3 mm), scleral invasion → high-risk features → adjuvant systemic chemotherapy

### Hereditary retinoblastoma long-term management

**Second malignancy surveillance:**
- Risk: hereditary RB1 carriers have ~50-fold elevated lifetime risk of second malignancies, predominantly in bone (osteosarcoma), soft tissue (sarcoma), CNS, and melanoma
- Without prior EBRT: ~40% lifetime second malignancy risk (cumulative by age 50)
- With prior EBRT: ~80%+ risk in irradiated field; EBRT dramatically amplifies second cancer risk → primary reason EBRT is now avoided
- Surveillance: annual whole-body MRI from age 5-7 onward; clinical exam; no established consensus but NCCN and international groups recommend continued lifelong surveillance

**Genetic counseling for offspring:**
- Hereditary RB1 carrier: 50% risk to each child; recommend: ophthalmologic exam under anesthesia (EUA) for all infants of carriers beginning at birth/1 month; germline RB1 testing of infant before EUA allows stratification
- EUA schedule (hereditary risk): every 3-4 weeks under anesthesia during first 12-18 months of life; frequency reduced after age 3-4 (when retinal progenitors differentiate and risk window closes); continue annually until age 7

## Connections

- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Biallelic RB1 loss is the universal initiating event in retinoblastoma; hereditary (bilateral) = germline RB1 + somatic LOH; sporadic (unilateral) = two somatic RB1 hits; MYCN amplification is an alternative RB-independent driver in a rare subset.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 pathway is bypassed in retinoblastoma via MDM2 amplification, MDM4 overexpression, or MYCN amplification; p53 pathway loss allows retinal progenitors to survive RB1 LOF-driven E2F1 pro-apoptotic signaling; TP53 mutations are rare in primary retinoblastoma.
- `connects-to` → **[Osteosarcoma](../../07-system/osteosarcoma/README.md)** — Hereditary RB1 carriers have 30-50× risk of osteosarcoma as a second malignancy; radiation exposure dramatically amplifies this risk — external beam RT now avoided in hereditary RB; germline RB1 is found in ~3-5% of sporadic osteosarcomas.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Retinoblastoma is the most common intraocular tumor of childhood, presenting as leukocoria (white pupillary reflex) or strabismus; globe-sparing therapy — intra-arterial and intravitreal chemotherapy — salvages most eyes, reserving enucleation for advanced (Group E) disease.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — A small (~2%) RB1-wildtype subset of retinoblastoma is instead driven by massive MYCN amplification, which raises CCNE1/CDK2 to hyperphosphorylate Rb and release E2F1 despite intact RB1; these aggressive, non-hereditary tumors are harder to salvage than RB1-mutant ones.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Retinoblastoma must neutralize the p53 apoptosis that RB1 loss would otherwise trigger: MDM2 amplification (~4%) and MDM4 overexpression (~65%) degrade or inhibit p53, so TP53 itself is rarely mutated — making MDM2/MDM4 antagonists a rational therapeutic strategy.

[^knudson-1971-two-hit]: Knudson AG Jr. Mutation and cancer: statistical study of retinoblastoma. *Proc Natl Acad Sci USA.* 1971;68(4):820-823. [doi:10.1073/pnas.68.4.820](https://doi.org/10.1073/pnas.68.4.820) · [PubMed 5279523](https://pubmed.ncbi.nlm.nih.gov/5279523/)
[^shields-2008-retinoblastoma]: Shields CL, Shields JA. Retinoblastoma management: advances in enucleation, intravenous chemoreduction, and intra-arterial chemotherapy. *Curr Opin Ophthalmol.* 2010;21(3):203-212. [doi:10.1097/ICU.0b013e328338676a](https://doi.org/10.1097/ICU.0b013e328338676a) · [PubMed 20224400](https://pubmed.ncbi.nlm.nih.gov/20224400/)
