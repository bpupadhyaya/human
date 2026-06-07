---
schema: human-scale-entry/v1
id: sf3b1
name: SF3B1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SF3B1 encodes a U2 snRNP scaffold protein; K700E hotspot activates cryptic 3' splice sites → aberrant ABCB7 splicing → mitochondrial iron → ring sideroblasts; SF3B1 K700E is in ~80-90% MDS-RS (favorable), ~15-20% uveal melanoma (Class 1B), ~10-15% CLL (favorable)."
aliases: ["SF3B1", "SF3B1 K700E", "splicing factor 3B1", "SF3B1 MDS", "SF3B1 ring sideroblasts", "SF3B1 uveal melanoma", "MDS-RS mutation", "U2 snRNP mutation"]
sources:
  - id: papaemmanuil-2011-sf3b1-mds
    type: peer-reviewed
    cite: "Papaemmanuil E, Cazzola M, Boultwood J, et al. Somatic SF3B1 mutation in myelodysplasia with ring sideroblasts. N Engl J Med. 2011;365(15):1384-1395."
    doi: "10.1056/NEJMoa1103283"
    pmid: "21998202"
    url: "https://doi.org/10.1056/NEJMoa1103283"
  - id: harbour-2013-sf3b1-uveal
    type: peer-reviewed
    cite: "Harbour JW, Roberson ED, Anbunathan H, et al. Recurrent mutations at codon 625 of the splicing factor SF3B1 in uveal melanoma. Nat Genet. 2013;45(2):133-135."
    doi: "10.1038/ng.2523"
    pmid: "23313955"
    url: "https://doi.org/10.1038/ng.2523"
cross_links:
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "SF3B1 and SRSF2 are both spliceosome mutations in MDS; SF3B1 K700E activates cryptic 3' splice sites (favorable prognosis MDS-RS) while SRSF2 P95H alters ESE recognition (adverse prognosis CMML/MDS); the two mutations are mutually exclusive; H3B-8800 targets both."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "SF3B1 and BAP1 are the two major recurrent mutations in uveal melanoma; SF3B1 → Class 1B (intermediate prognosis, late relapse); BAP1 loss → Class 2 (high metastatic risk, early liver relapse); SF3B1 and BAP1 mutations are mutually exclusive."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "SF3B1 K700E induces R-loops → replication stress → TP53 pathway activation; SF3B1 mutations in MDS rarely co-occur with TP53; SF3B1-mutant MDS has better prognosis than TP53-mutant MDS; TP53 acquisition signals AML transformation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "SF3B1 K700E in CLL alters BCL2 family member splicing; SF3B1-mutant CLL is associated with favorable prognosis (IGHV mutated, indolent); venetoclax (BCL-2 inhibitor) is active in CLL regardless of SF3B1 status; SF3B1 mutation may influence BCL2 vs MCL1 splice isoform balance."
---

# SF3B1

## Overview

**SF3B1 (Splicing Factor 3B Subunit 1)** is the largest component of the U2 snRNP-associated SF3b complex and a core structural scaffold of the spliceosome's branch point recognition machinery. SF3B1 forms a horseshoe-shaped HEAT repeat structure that cradles the intronic RNA near the branch point adenosine, positioning U2 snRNA to base-pair with the branch point sequence (BPS) and thereby defining the **3' splice site**. SF3B1 was identified as a recurrently mutated gene in myelodysplastic syndrome with ring sideroblasts (MDS-RS) in 2011, establishing it as the most prevalent splicing factor mutation in this favorable MDS subtype [^papaemmanuil-2011-sf3b1-mds]. The canonical **K700E hotspot** impairs normal BPS recognition → activation of **cryptic 3' splice sites** (upstream of canonical SS) → widespread alternative splicing → aberrant ABCB7 iron transporter splicing → mitochondrial iron accumulation → ring sideroblast formation. SF3B1 K700E is uniquely associated with **favorable prognosis** across its disease contexts — in contrast to SRSF2 P95H, which is adverse — making it a diagnostically and prognostically critical mutation [^harbour-2013-sf3b1-uveal].

**SF3B1 mutation landscape:**
- **MDS with ring sideroblasts (MDS-RS):** K700E in ~80-90%; essentially defines MDS-RS; WHO 2022 criteria include SF3B1 as molecular criterion for MDS-RS; favorable prognosis category (best outcome among MDS subtypes); luspatercept approved (MEDALIST/COMMANDS trials)
- **CLL:** SF3B1 mutations in ~10-15%; K700E most common but K666N, K666R, R625C also occur; independently associated with favorable overall prognosis (usually IGHV-mutated CLL); del(11q) or unmutated IGHV co-occurring with SF3B1 → less favorable
- **Uveal melanoma:** SF3B1 R625C/H (note: codon 625, not 700 — same HEAT repeat region) in ~15-20%; associated with Class 1B molecular subtype; intermediate prognosis; late metastatic relapses (10+ years after primary treatment)
- **Breast cancer:** SF3B1 mutations in ~2-5%; E902K and K700E in ER+ luminal breast cancer; prognostic significance uncertain
- **Cholangiocarcinoma:** SF3B1 mutations in ~2-5% iCCA; rare; splicing-dependent mechanism
- **AML:** SF3B1 mutations in ~1-2%; typically from pre-existing MDS-RS clone; rare de novo

## Structure

### SF3B1 protein architecture

SF3B1 is a 1304-amino-acid, 145 kDa protein:

**N-terminal ULM-binding domain (1-463):**
Contains unstructured regions with ULM (U2AF ligand motif) — binds UHM (U2AF homology motif) domains of U2AF65 and U2AF35 → bridges U2 snRNP recruitment to the branch point; interacts with PHF5A/SF3B14b (integral part of SF3b complex critical for cryptic SS suppression).

**HEAT domain (463-1304, 22 HEAT repeats):**
Tandem HEAT (Huntingtin-Elongation-A subunit-TOR) repeats form a right-handed superhelix; the concave inner surface contacts the intronic branch point region RNA; **K700 is in HEAT repeat 15**, making direct contact with the branch point adenosine and upstream intronic sequence; **K700E** substitution (Lys → Glu; positive → negative charge) → altered electrostatic interaction with RNA phosphate backbone → changes branch point sequence preference → activation of upstream cryptic BPS with shifted 3' SS selection; SF3B1 K700E shifts 3' SS usage ~12-50 nt upstream → inclusion of short alternative exon sequences → often triggers NMD or generates truncated/altered proteins.

### SF3B1 K700E mechanism of cryptic splice site activation

**Normal branch point recognition:**
SF3B1 HEAT repeats + PHF5A form the branch point capture module → U2 snRNA base-pairs with BPS (typically YNYURAY, 18-40 nt upstream of 3' AG) → 2'-OH of branch point A attacks the 5' splice site → lariat intermediate formed → exon ligation.

**SF3B1 K700E altered recognition:**
K700E disrupts SF3B1-PHF5A interaction at the branch point capture interface → reduced fidelity of canonical BPS recognition → upstream cryptic BPS (14-30 nt further upstream) now used → 3' SS shifts upstream → novel AG dinucleotide used → aberrant exon junction → truncated/altered mRNA products.

**Key downstream targets:**
- **ABCB7 (ABC transporter, mitochondrial iron export):** Cryptic 3' SS in ABCB7 intron 9 → ABCB7 exon 10 partial skipping → truncated ABCB7 → impaired iron export from mitochondria → iron accumulates in mitochondria → mitochondrial ferritin aggregates → **ring sideroblasts** (>15% of erythroblasts with ≥5 mitochondrial iron granules in perinuclear ring)
- **MAP3K7 (TAK1):** Cryptic splicing → truncated TAK1 → impaired NF-κB and MAPK signaling; may contribute to impaired immune signaling in SF3B1-mutant cells
- **SUGP1 (SURP and G patch domain containing 1):** SUGP1 normally suppresses cryptic SS alongside SF3B1; SF3B1 K700E reduces SUGP1 co-suppression → cryptic SS derepressed

## Function

### Normal SF3B1 roles in hematopoiesis

SF3B1 is essential for pre-mRNA splicing of all mammalian transcripts; germline loss is lethal at gastrulation. In erythroid progenitors, SF3B1 cooperates with SUGP1 to maintain precise 3' splice site fidelity for ABCB7, TMEM14C, and other mitochondrial iron metabolism genes critical for heme synthesis. SF3B1-wild-type erythroblasts complete differentiation through erythroblast → reticulocyte → mature erythrocyte without mitochondrial iron excess; SF3B1 K700E → ABCB7 aberrant splicing → sideroblastic anemia with specific ring sideroblast morphology.

### Spliceosome target (H3B-8800) rationale

Spliceosome-mutant cells (SF3B1, SRSF2, U2AF1 mutations) develop hypersensitivity to further spliceosome inhibition relative to wild-type cells — proposed mechanism: pre-existing splicing stress renders spliceosome-mutant cells closer to a threshold of intolerable splicing burden. H3B-8800 (spliceosome modulator targeting the SF3b complex) exploits this vulnerability → selectively kills spliceosome-mutant cells; Phase 1 data in MDS/AML/CMML: ORR ~12-15%; best benefit in SF3B1 and SRSF2-mutant patients.

### Prognostic impact in MDS

SF3B1 K700E in MDS defines a favorable subtype:
- WHO 2022: SF3B1 mutation with ≥5% ring sideroblasts OR ring sideroblasts ≥15% without SF3B1 = MDS-RS
- IPSS-M: SF3B1 as favorable molecular marker (independent of ring sideroblast morphology)
- Median OS: MDS-RS ~69-75 months vs. higher-risk MDS ~15-30 months
- AML transformation rate: <2%/year (lowest among MDS subtypes)
- However, SF3B1 mutation does NOT guarantee favorable prognosis if co-mutated with ASXL1, RUNX1, or TP53 → IPSS-M adjusts upward

### Luspatercept and SF3B1

Luspatercept (ACVR2B-Fc trap) inhibits TGF-β superfamily signaling → promotes late-stage erythroid maturation; particularly active in SF3B1-mutant MDS-RS (MEDALIST trial: transfusion independence 38% vs 13%, FDA 2020; COMMANDS trial: 1st-line luspatercept superior to epoetin alfa for LR-MDS with RS, FDA 2023). The selectivity of luspatercept for SF3B1-mutant MDS reflects the dominant role of aberrant late-stage erythropoiesis in ring sideroblastic anemia.

## Mechanism

### SF3B1 in uveal melanoma (distinct codon)

Uveal melanoma SF3B1 mutations predominantly affect **codon 625** (R625C/H, R625S) rather than K700E. Codon 625 is in HEAT repeat 12, adjacent to HEAT repeat 15 (K700) in the 3D structure — both contact the branch point capture region with similar functional consequences (cryptic 3' SS activation). SF3B1-mutant uveal melanoma shows:
- Altered splicing of CENPN, ABCB7, and other transcripts
- Class 1B molecular profile: Chromosome 6p gain, 8q gain patterns distinct from BAP1-loss Class 2
- Intermediate prognosis with propensity for late relapses (>10 years post-enucleation) — likely reflecting slow-growing micrometastases that escape early detection
- Different mutational mechanism from MDS (different codon, but same functional effect on the spliceosome)

## Connections

- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — SF3B1 and SRSF2 are both spliceosome mutations in MDS; SF3B1 K700E activates cryptic 3' splice sites (favorable prognosis MDS-RS) while SRSF2 P95H alters ESE recognition (adverse prognosis CMML/MDS); the two mutations are mutually exclusive; H3B-8800 targets both.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — SF3B1 and BAP1 are the two major recurrent mutations in uveal melanoma; SF3B1 → Class 1B (intermediate prognosis, late relapse); BAP1 loss → Class 2 (high metastatic risk, early liver relapse); SF3B1 and BAP1 mutations are mutually exclusive.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — SF3B1 K700E induces R-loops → replication stress → TP53 pathway activation; SF3B1 mutations in MDS rarely co-occur with TP53; SF3B1-mutant MDS has better prognosis than TP53-mutant MDS; TP53 acquisition signals AML transformation.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — SF3B1 K700E in CLL alters BCL2 family member splicing; SF3B1-mutant CLL is associated with favorable prognosis (IGHV mutated, indolent); venetoclax (BCL-2 inhibitor) is active in CLL regardless of SF3B1 status; SF3B1 mutation may influence BCL2 vs MCL1 splice isoform balance.

[^papaemmanuil-2011-sf3b1-mds]: Papaemmanuil E, Cazzola M, Boultwood J, et al. Somatic SF3B1 mutation in myelodysplasia with ring sideroblasts. *N Engl J Med.* 2011;365(15):1384-1395. [doi:10.1056/NEJMoa1103283](https://doi.org/10.1056/NEJMoa1103283) · [PubMed 21998202](https://pubmed.ncbi.nlm.nih.gov/21998202/)
[^harbour-2013-sf3b1-uveal]: Harbour JW, Roberson ED, Anbunathan H, et al. Recurrent mutations at codon 625 of the splicing factor SF3B1 in uveal melanoma. *Nat Genet.* 2013;45(2):133-135. [doi:10.1038/ng.2523](https://doi.org/10.1038/ng.2523) · [PubMed 23313955](https://pubmed.ncbi.nlm.nih.gov/23313955/)
