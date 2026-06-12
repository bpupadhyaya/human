---
schema: human-scale-entry/v1
id: medulloblastoma
name: Medulloblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Medulloblastoma is the most common pediatric brain tumor; 4 molecular subgroups: WNT (~10%, OS ~95%), SHH (~38%), Group 3 (~25%, MYC-amplified, worst prognosis), Group 4 (~35%); surgery + CSI + chemotherapy; SHH MB responsive to SMO inhibitors; infant MB: chemo without radiation."
aliases: ["medulloblastoma", "MB", "pediatric medulloblastoma", "SHH medulloblastoma", "WNT medulloblastoma", "Group 3 medulloblastoma", "cerebellar medulloblastoma", "MBEN"]
sources:
  - id: packer-2006-std-risk-mb
    type: peer-reviewed
    cite: "Packer RJ, Gajjar A, Vezina G, et al. Phase III study of craniospinal radiation therapy followed by adjuvant chemotherapy for newly diagnosed average-risk medulloblastoma. J Clin Oncol. 2006;24(25):4202-4208."
    doi: "10.1200/JCO.2006.06.4980"
    pmid: "16943538"
    url: "https://doi.org/10.1200/JCO.2006.06.4980"
  - id: taylor-2012-mb-subgroups
    type: peer-reviewed
    cite: "Taylor MD, Northcott PA, Korshunov A, et al. Molecular subgroups of medulloblastoma: the current consensus. Acta Neuropathol. 2012;123(4):465-472."
    doi: "10.1007/s00401-011-0922-z"
    pmid: "22134537"
    url: "https://doi.org/10.1007/s00401-011-0922-z"
cross_links:
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "PTCH1/SMO/SUFU/GLI2 mutations define SHH-activated MB (~38%); germline PTCH1 → Gorlin syndrome + infant/adult SHH-MB; SHH-MB in adults is the primary indication for vismodegib in MB trials; desmoplastic/nodular histology is the hallmark of SHH-MB with PTCH1 LOF."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification (~17%) defines the most aggressive Group 3 MB (5-year OS ~45%); MYCN amplification in SHH-MB + TP53 mutation = highest-risk SHH-MB; MYC drives extreme proliferative rate; BET inhibitors suppress MYC in Group 3/4 MB preclinically."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "WNT-activated MB (~10%) carries CTNNB1 activating mutations + monosomy 6 + nuclear β-catenin; WNT-MB has near-universal cure (5-year OS ~95%); de-escalation trials (reduced CSI 18 Gy) ongoing; CTNNB1 mutations are absent in SHH/Group 3/Group 4 MB."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "SHH-activated/TP53-mutant MB: MYCN amplification + TP53 mutation → 5-year OS ~40%; TP53 mutations are germline in Li-Fraumeni syndrome → elevated MB risk; Group 3 MYC-amplified MB acquires TP53 at relapse; p53 IHC (>10% nuclear) is a surrogate marker in MB."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Medulloblastoma is the most common pediatric brain tumor, arising in the cerebellum (posterior fossa) where it obstructs the 4th ventricle → hydrocephalus; maximal safe resection risks cerebellar mutism syndrome, and craniospinal irradiation drives neurocognitive late effects."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Gorlin syndrome (germline PTCH1 loss) predisposes to SHH-activated medulloblastoma, typically the desmoplastic/nodular infant form; because these children are radiation-hypersensitive (PTCH1 carriers get RT-field basal cell carcinomas), radiation-sparing strategies are favored."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Germline TP53 (Li-Fraumeni) defines the SHH-activated/TP53-mutant subgroup — often MYCN-amplified, large-cell/anaplastic, ~40% 5-year OS; TP53 germline testing is mandatory for all SHH-MB aged 3-17, and craniospinal irradiation is avoided given LFS radiation sensitivity."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Medulloblastoma and IDH-mutant glioma are both molecularly classified brain tumors but opposite poles: medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC), while IDH-mutant glioma is a slow diffuse hemispheric tumor of adults driven by 2-HG epigenetics."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Atypical teratoid/rhabdoid tumor is the key infant mimic of medulloblastoma: both are small-round-blue-cell posterior-fossa tumors, but ATRT is defined by SMARCB1 (INI1) loss and far more aggressive — INI1 immunostaining (kept in MB, lost in ATRT) distinguishes them."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "SHH-activated medulloblastoma arises from cerebellar granule neuron precursors of the external granular layer, whose normal proliferation depends on Sonic hedgehog from Purkinje neurons; a PTCH1/SMO lesion locks this hedgehog program on, driving the desmoplastic/nodular tumor."
---

# Medulloblastoma

## Overview

**Medulloblastoma (MB)** is the most common malignant **pediatric brain tumor**, comprising ~20% of all pediatric CNS tumors and ~40% of pediatric posterior fossa tumors. MB arises in the cerebellum from aberrant progenitor cell proliferation and is classified into **four molecular subgroups** by the WHO (2021) — WNT-activated, SHH-activated, and non-WNT/non-SHH (Group 3 and Group 4) — with profoundly different biological mechanisms, treatment responses, and prognoses [^taylor-2012-mb-subgroups]. Modern treatment for standard-risk MB involves maximal surgical resection followed by **craniospinal irradiation (CSI) and adjuvant chemotherapy** (vincristine+CCNU+cisplatin × 8 cycles), achieving 5-year event-free survival (EFS) of ~81% in standard-risk disease [^packer-2006-std-risk-mb]; high-risk MB requires escalated CSI (36 Gy) and intensified chemotherapy. Key challenges include: (1) devastating neurocognitive late effects of irradiation (IQ loss, endocrinopathy, secondary tumors); (2) extreme heterogeneity in prognosis across subgroups (WNT-MB OS ~95% vs Group 3 MYC-amplified OS ~45%); and (3) lack of approved targeted therapies beyond SMO inhibitors for SHH-MB.

**Epidemiology:**
- ~500-600 cases/year in the USA; ~15,000-20,000/year globally
- Median age at diagnosis: 6-7 years; peak 3-9 years; bimodal distribution with adult peak 25-40 years
- Male predominance 2:1 for Group 3/4; female predominance for WNT-MB
- Almost universal cerebellar location; ~5-10% spinal seeding at diagnosis; ~20-30% metastatic disease overall (M+)

## Structure

### WHO 2021 molecular subgroups

**1. WNT-activated MB (~10%):**
- **Molecular:** CTNNB1 (β-catenin) activating mutations (~85%); SMARCA4 mutations (~20%); monosomy 6 (pathognomonic); isochromosome 17q absent; nuclear β-catenin by IHC confirms WNT activation
- **Histology:** Classic MB (most); large cell/anaplastic extremely rare
- **Demographics:** Peak age 10-15 years; adults; male = female
- **Prognosis:** 5-year OS ~95% — best of all subgroups; highly curable; near-zero mortality with standard therapy in classic WNT-MB; de-escalation is the major research priority
- **Cell of origin:** Dorsal brainstem progenitors (lower rhombic lip near 4th ventricle roof)

**2. SHH-activated/TP53-wildtype MB (~28%):**
- **Molecular:** PTCH1 LOF (~55%), SUFU LOF (~10%), SMO GOF (~5%), GLI2 amplification (~10%); TERT promoter mutations (~80% of adult SHH-MB); 9q loss
- **Histology:** Desmoplastic/nodular (infants — excellent prognosis), medulloblastoma with extensive nodularity (MBEN, infants — best prognosis), classic
- **Demographics:** Infants (<3 years) and adults (>17 years); bimodal; rare in 3-17-year age range
- **Prognosis:** Highly variable — infants with MBEN: 5-year OS ~90-100%; infants with SHH non-MBEN: ~70-80%; adults: ~75-80%; worse with MYCN amplification
- **Cell of origin:** Cerebellar granule cell progenitors (GCPs) in external granule layer

**3. SHH-activated/TP53-mutant MB (~10%):**
- **Molecular:** MYCN amplification (~50%); TP53 mutations (~100% by definition); GLI2 amplification; predominantly germline TP53 in ~50% (Li-Fraumeni syndrome)
- **Histology:** Large cell/anaplastic predominantly
- **Demographics:** Children 3-17 years; male predominance
- **Prognosis:** 5-year OS ~40-60% — worst SHH subgroup; high-risk treatment regardless of M-staging
- **Significance:** Mandatory TP53 germline testing for all SHH-activated children aged 3-17 years

**4. Non-WNT/Non-SHH MB — Group 3 (~25%):**
- **Molecular:** MYC amplification (~17%); OTX2 overexpression (~65%); GFI1/GFI1B enhancer hijacking with MYC; SMARCA4 mutations; isochromosome 17q
- **Histology:** Classic, large cell/anaplastic (MYC-amplified often LCA)
- **Demographics:** Infants and young children (<10 years); male predominance; highest rate of M+ disease (~45%)
- **Prognosis:** 5-year OS ~45-60% (worst non-SHH group); MYC-amplified Group 3: OS ~40%
- **Cell of origin:** Progenitors near rhombic lip (same as WNT but different activation)

**5. Non-WNT/Non-SHH MB — Group 4 (~35%):**
- **Molecular:** CDK6 amplification; MYCN amplification (~5%); SNCAIP duplication (tandem duplication); KDM6A/KDM6B mutations; isochromosome 17q
- **Histology:** Classic predominantly; rare large cell/anaplastic
- **Demographics:** Most common MB; all ages (peak 10-17 years); male predominance ~3:1
- **Prognosis:** 5-year OS ~75-85% (intermediate)
- **Cell of origin:** Unipolar brush cells (glutamatergic cerebellar interneurons)

### Histological classification

**Classic (most common, ~72%):** Densely packed, uniform small round cells with scant cytoplasm; Homer-Wright rosettes (~40%); high mitotic rate.

**Desmoplastic/Nodular (DN, ~15%):** Nodular pale islands (reticulin-free zones) surrounded by dense reticulin-rich desmoplastic stroma; characteristic of SHH-MB in infants; favorable prognosis even with leptomeningeal spread in infants.

**Medulloblastoma with Extensive Nodularity (MBEN, ~5%):** Extreme version of DN; >50% nodular architecture; SHH-MB in infants; best prognosis (5-year OS ~100% with some protocols).

**Large Cell/Anaplastic (LCA, ~8%):** Nuclear enlargement (large cell) and nuclear molding, apoptosis, prominent mitoses (anaplastic); marks highest-risk histology; MYC-amplified Group 3 MB often LCA; adverse prognosis regardless of molecular subgroup.

## Function

### Biology of medulloblastoma subgroups

**WNT-MB biology:**
CTNNB1 mutation → β-catenin accumulates in nucleus → TCF/LEF target gene activation → WNT target program; the WNT pathway in rhombic lip progenitors drives cell proliferation; nuclear β-catenin in MB cells is sufficient for transformation; Gorlin syndrome (PTCH1 germline) does NOT predispose to WNT-MB; Li-Fraumeni (TP53) can occasionally produce WNT-activated tumors; WNT-MB uniquely lacks isochromosome 17q and monosomy 6 is present → monosomy 6 is the cytogenetic signature.

**SHH-MB biology:**
Purkinje cells express SHH → activates PTCH1 on GCPs → normally drives transient proliferation during cerebellar development (neonatal) → GCPs differentiate and migrate to form internal granular layer; PTCH1 LOF in GCPs → constitutive SMO → GLI2 → CCND2 (cyclin D2) → persistent GCP proliferation → tumor; adult SHH-MB: TERT promoter activation (~80%) → telomere maintenance → enables transformation in older, less proliferative progenitor pool.

**Group 3 MB biology:**
MYC amplification → extreme transcriptional activation → LCA-phenotype rapid cycling → pro-apoptotic stress countered by GFI1/GFI1B (oncogene enhancer hijacking) and OTX2 (neural stem cell TF); highest rate of leptomeningeal dissemination at diagnosis; resistant to standard chemotherapy when MYC-amplified; BET inhibitors (JQ1) suppress MYC expression in Group 3 MB preclinically.

**Group 4 MB biology:**
CDK6 amplification → constitutive CDK6 kinase → RB phosphorylation → E2F → proliferative gene program; KDM6A/KDM6B (histone H3K27 demethylases) — LOF → H3K27me3 accumulation → epigenetic silencing of differentiating genes; SNCAIP (synuclein alpha-interacting protein) tandem duplication is a unique chromatin regulatory alteration; methylation profiling is essential to distinguish from SHH/WNT.

## Pathology

### Staging — Chang classification (updated)

| Stage | Definition |
|-------|-----------|
| M0 | No metastases |
| M1 | Microscopic tumor cells found in CSF cytology |
| M2 | Gross nodular seeding in cerebellar/cerebral subarachnoid space or in third/fourth ventricles |
| M3 | Gross nodular seeding in spinal subarachnoid space |
| M4 | Extraneuraxial metastases |

**Risk stratification:**
- **Standard risk:** Localized (M0), ≤3 years old not eligible (infant protocols), resected (<1.5 cm² residual), non-LCA histology, WNT or SHH-TP53wt or Group 4 (with MYC-negative)
- **High risk:** M1-M4, residual tumor >1.5 cm², LCA histology, MYC amplification, SHH-TP53-mutant, or Group 3

### Treatment

**Surgery (maximal safe resection):**
Gross or near-total resection (NTR, ≤1.5 cm² residual) → significantly improved EFS; median resection achieves NTR/GTR in ~70-80% with modern neuro-navigation; posterior fossa craniotomy with tumor in 4th ventricle; hydrocephalus management (ventriculostomy/EVD during surgery, ETV or shunt for refractory hydrocephalus); cerebellar mutism syndrome (CMS, ~25% of posterior fossa surgery): transient inability to speak, ataxia, emotional lability → majority recover over months; risk reduction: approach via telovelar vs midline vermian splitting.

**Craniospinal irradiation (CSI):**
- **Standard risk:** CSI 23.4 Gy + posterior fossa boost to 54-55.8 Gy total; proton beam preferred (reduces integral dose to developing CNS and off-target organs); 5-year EFS ~81% [^packer-2006-std-risk-mb]
- **High risk:** CSI 36 Gy + posterior fossa 55.8 Gy ± spinal metastatic site boosts
- **WNT-MB de-escalation:** ACNS1422 (CSI 18 Gy reduced): results pending; MBWNT-3 (omit radiation in CSF-negative WNT-MB): ongoing; chemotherapy intensification may offset reduced RT
- **Infants (<3 years):** Radiation causes catastrophic neurotoxicity in developing brain → CSI deferred/avoided; HD chemotherapy induction (carboplatin+vincristine+cyclophosphamide+methotrexate or HDCT+auto-SCT); SHH-MBEN infants: induction + maintenance without RT achieves ~100% EFS; Head-start III: HDCT+auto-SCT for poor-risk infant MB

**Adjuvant chemotherapy (standard risk):**
Packer/CCSG-923: vincristine during RT → 8 cycles of CCNU+cisplatin+vincristine (weekly × 8 courses over ~16 months); 5-year EFS ~81% [^packer-2006-std-risk-mb]; major toxicities: ototoxicity (cisplatin, ~30% requiring hearing aids), myelosuppression, neurotoxicity (vincristine neuropathy).

**High-risk MB chemotherapy:**
COG ACNS0332: standard vs carboplatin+thiotepa induction → CCNU+cisplatin+vincristine maintenance; carboplatin during radiation improved EFS (62.3% vs 59.3%) but increased hematologic toxicity; HDCT + auto-SCT: used in some high-risk protocols (particularly Group 3 MYC-amplified); tandem HDCT in Group 3/4 high-risk explored in cooperative group studies.

**Targeted therapy:**
- **SMO inhibitors in SHH-MB:** Sonidegib + craniospinal radiation: Phase 2 (PBTC-039): for adult/pediatric SHH-MB; vismodegib single-agent in adult SHH-MB (PBTC-025B): ORR ~41%; ongoing frontline Phase 3 trials combining SMO inhibitors with standard therapy in SHH-MB
- **Pemetrexed + gemcitabine:** Active in R/R pediatric MB across subgroups (ORR ~40%); now incorporated in some maintenance protocols for high-risk Group 3/4
- **ONC201 (dopamine receptor D2 antagonist):** Group 4 MB with SNCAIP or H3K27me3 markers → active in R/R Group 4 (unique mechanism); Phase 1/2 data showing ORR ~20-40% in H3-altered/Group 4 MB
- **PLK4 inhibitor (CFI-400945):** Centrosome amplification in LCA MB → Phase 1 in pediatric solid tumors
- **Immunotherapy (pembrolizumab, nivolumab):** Limited activity in MB (low mutational burden, immunologically cold); ongoing trials with combination strategies

### Long-term effects

MB survivors face substantial late effects — inversely proportional to age at irradiation:
- **Neurocognitive:** IQ decline 1-2 points/year post-CSI in young children; processing speed, working memory, attention most affected; proton beam reduces dose to hippocampus → preserves verbal memory better than photon CSI; executive function impairment limits academic/vocational achievement
- **Endocrine:** GH deficiency (~80%); hypothyroidism; precocious or delayed puberty; obesity; GH supplementation recommended; monitor TSH, FSH/LH annually
- **Second malignancies:** CSI field → radiation-induced glioma, meningioma (10-20 years post-irradiation); chemotherapy → secondary AML/MDS (alkylators)
- **Hearing loss:** Cisplatin ototoxicity (~30-40%); proton beam reduces cochlear dose; sodium thiosulfate amifostine protective in some trials
- **Cardiovascular:** Radiation-induced vasculopathy, moyamoya syndrome (radiation to circle of Willis); metabolic syndrome
- **Quality of life:** Social isolation, reduced independence, impaired quality of life in a substantial minority of survivors; neurocognitive rehabilitation programs beneficial

## Connections

- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — PTCH1/SMO/SUFU/GLI2 mutations define SHH-activated MB (~38%); germline PTCH1 → Gorlin syndrome + infant/adult SHH-MB; SHH-MB in adults is the primary indication for vismodegib in MB trials; desmoplastic/nodular histology is the hallmark of SHH-MB with PTCH1 LOF.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification (~17%) defines the most aggressive Group 3 MB (5-year OS ~45%); MYCN amplification in SHH-MB + TP53 mutation = highest-risk SHH-MB; MYC drives extreme proliferative rate; BET inhibitors suppress MYC in Group 3/4 MB preclinically.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — WNT-activated MB (~10%) carries CTNNB1 activating mutations + monosomy 6 + nuclear β-catenin; WNT-MB has near-universal cure (5-year OS ~95%); de-escalation trials (reduced CSI 18 Gy) ongoing; CTNNB1 mutations are absent in SHH/Group 3/Group 4 MB.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — SHH-activated/TP53-mutant MB: MYCN amplification + TP53 mutation → 5-year OS ~40%; TP53 mutations are germline in Li-Fraumeni syndrome → elevated MB risk; Group 3 MYC-amplified MB acquires TP53 at relapse; p53 IHC (>10% nuclear) is a surrogate marker in MB.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Medulloblastoma is the most common pediatric brain tumor, arising in the cerebellum (posterior fossa) where it obstructs the 4th ventricle → hydrocephalus; maximal safe resection risks cerebellar mutism syndrome, and craniospinal irradiation drives neurocognitive late effects.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Gorlin syndrome (germline PTCH1 loss) predisposes to SHH-activated medulloblastoma, typically the desmoplastic/nodular infant form; because these children are radiation-hypersensitive (PTCH1 carriers get RT-field basal cell carcinomas), radiation-sparing strategies are favored.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Germline TP53 (Li-Fraumeni) defines the SHH-activated/TP53-mutant subgroup — often MYCN-amplified, large-cell/anaplastic, ~40% 5-year OS; TP53 germline testing is mandatory for all SHH-MB aged 3-17, and craniospinal irradiation is avoided given LFS radiation sensitivity.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Medulloblastoma and IDH-mutant glioma are both molecularly classified brain tumors but opposite poles: medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC), while IDH-mutant glioma is a slow diffuse hemispheric tumor of adults driven by 2-HG epigenetics.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Atypical teratoid/rhabdoid tumor is the key infant mimic of medulloblastoma: both are small-round-blue-cell posterior-fossa tumors, but ATRT is defined by SMARCB1 (INI1) loss and far more aggressive — INI1 immunostaining (kept in MB, lost in ATRT) distinguishes them.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — SHH-activated medulloblastoma arises from cerebellar granule neuron precursors of the external granular layer, whose normal proliferation depends on Sonic hedgehog from Purkinje neurons; a PTCH1/SMO lesion locks this hedgehog program on, driving the desmoplastic/nodular tumor.

[^packer-2006-std-risk-mb]: Packer RJ, Gajjar A, Vezina G, et al. Phase III study of craniospinal radiation therapy followed by adjuvant chemotherapy for newly diagnosed average-risk medulloblastoma. *J Clin Oncol.* 2006;24(25):4202-4208. [doi:10.1200/JCO.2006.06.4980](https://doi.org/10.1200/JCO.2006.06.4980) · [PubMed 16943538](https://pubmed.ncbi.nlm.nih.gov/16943538/)
[^taylor-2012-mb-subgroups]: Taylor MD, Northcott PA, Korshunov A, et al. Molecular subgroups of medulloblastoma: the current consensus. *Acta Neuropathol.* 2012;123(4):465-472. [doi:10.1007/s00401-011-0922-z](https://doi.org/10.1007/s00401-011-0922-z) · [PubMed 22134537](https://pubmed.ncbi.nlm.nih.gov/22134537/)
