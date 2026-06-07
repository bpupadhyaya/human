---
schema: human-scale-entry/v1
id: nf2
name: NF2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "NF2 (merlin) is a FERM-domain tumor suppressor; LOF → Hippo pathway loss → YAP/TAZ nuclear → TEAD-driven proliferation; biallelic NF2 LOF in ~50-60% meningioma and ~50% mesothelioma; germline NF2 syndrome — bilateral VS, meningiomas, ependymomas; mTOR inhibitors active in VS."
aliases: ["NF2", "merlin", "schwannomin", "NF2 tumor suppressor", "NF2 syndrome", "neurofibromatosis type 2", "vestibular schwannoma", "NF2 meningioma", "NF2 mesothelioma", "Hippo pathway NF2"]
sources:
  - id: rouleau-1993-nf2-gene
    type: peer-reviewed
    cite: "Rouleau GA, Merel P, Lutchman M, et al. Alteration in a new gene encoding a putative membrane-organizing protein causes neuro-fibromatosis type 2. Nature. 1993;363(6429):515-521."
    doi: "10.1038/363515a0"
    pmid: "8379998"
    url: "https://doi.org/10.1038/363515a0"
  - id: zhao-2007-yap-hippo
    type: peer-reviewed
    cite: "Zhao B, Wei X, Li W, et al. Inactivation of YAP oncoprotein by the Hippo pathway is involved in cell contact inhibition and tissue growth control. Genes Dev. 2007;21(21):2747-2761."
    doi: "10.1101/gad.1602907"
    pmid: "17974916"
    url: "https://doi.org/10.1101/gad.1602907"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "NF2/merlin activates LATS1/2 (Hippo) → YAP/TAZ cytoplasmic; YAP/TAZ nuclear → CTGF/CYR61 → mTORC1 activation; mTOR inhibitors (everolimus, sirolimus) reduce schwannoma volume in NF2 syndrome (Phase 2 REACT trial); rapalogs partially reverse NF2-driven growth."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Merlin promotes EGFR endocytosis and lysosomal degradation; NF2 loss → EGFR/ErbB2/ErbB3 surface accumulation → sustained PI3K/AKT and MAPK; anti-ErbB2 antibodies (lapatinib) explored in NF2-associated schwannoma; partial activity in Phase 2 trials."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "NF2/merlin and PTEN both restrain PI3K/AKT/mTOR; NF2 loss → AKT hyperactivation independent of PTEN; NF2+PTEN co-loss is synergistic in meningioma and mesothelioma; PTEN loss in ~10-15% meningioma; mTOR inhibitors target the convergent PI3K/mTOR axis in NF2-null tumors."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Merlin suppresses RAS/MAPK by promoting EGFR endocytosis → reduced ERK1/2 activation; NF2-null schwannoma and meningioma show ERK1/2 hyperphosphorylation; MEK inhibitors (trametinib, binimetinib) and FAK inhibitors are being evaluated in NF2-deficient tumors."
---

# NF2

## Overview

**NF2** encodes **merlin** (moesin-ezrin-radixin-like protein, also called schwannomin), a 595-amino-acid tumor suppressor that is the founding member of the **band 4.1 superfamily**. Merlin functions as a critical node linking extracellular cell-contact signals to growth suppression via the **Hippo signaling pathway** and EGFR downregulation. NF2 loss results in constitutive YAP/TAZ nuclear activity and EGFR/ErbB overexpression — both driving proliferation and survival [^rouleau-1993-nf2-gene].

**NF2 biallelic LOF occurs in:**
- **Meningioma**: ~50-60% sporadic (most frequent alteration; chromosome 22q loss); correlates with WHO grade 1 convexity meningiomas
- **Schwannoma**: ~100% of sporadic (all VS carry NF2 LOF); bilateral VS = pathognomonic for germline NF2 syndrome
- **Mesothelioma** (~40-50%): second most common alteration after BAP1; both NF2 and BAP1 loss frequently co-occur
- **Clear cell meningioma** (~100%): spinal variant; pediatric; aggressive despite grade 1-2 appearance
- **Ependymoma** (spinal): ~15-20%; NF2 LOF in spinal ependymoma; distinct from cerebral ependymoma (not NF2-driven)
- **Hepatocellular carcinoma** (~10-15%): NF2 secondary alteration; Hippo-YAP axis activated

**Germline NF2 — NF2 syndrome (Neurofibromatosis type 2):**
Autosomal dominant; incidence ~1:25,000; nearly complete penetrance (>95% by age 60). Features:
- **Bilateral vestibular schwannomas (VS)** — pathognomonic; median onset age ~20; progressive hearing loss, tinnitus, facial nerve palsy
- **Meningiomas** (~50%): often multiple; occur at younger age than sporadic; skull base and spinal meningiomas
- **Ependymomas** (~33%): primarily spinal; multiple; may cause myelopathy
- **Cataracts** (posterior subscapular): ~75%; early-onset lens changes
- **Cutaneous schwannomas** (~67%): multiple; intracutaneous plaques; peripheral nerve tumors
- Genotype-phenotype correlations: truncating mutations → severe (bilateral VS at mean age 18-20); missense mutations → attenuated NF2 phenotype; mosaic NF2 → variable, often milder

## Structure

### Merlin protein architecture

**N-terminal FERM domain (aa 1-302):**
Three sub-domains (F1/F2/F3); F1 and F2 pack against each other; F3 contains the actin-binding site and integrin-binding interface; the FERM domain of merlin differs from radixin/moesin at ~35% of residues → unique surface topology → merlin interacts with distinct binding partners

Key FERM interactions:
- CD44 (hyaluronic acid receptor): contact inhibition signal → merlin activation
- EGFR/ErbB intracellular C-terminus: merlin promotes EGFR endocytosis
- Integrins (β1, αvβ3): merlin links integrin-ECM signals to growth suppression
- Spectrin (βII): cytoskeletal anchoring of merlin at adherens junctions
- CRL4-DCAF1 E3 ligase: nuclear merlin binds DCAF1 → inhibits CRL4 activity → histone H2B monoubiquitination regulation

**C-terminal tail (aa 450-595):**
α-helical; required for self-association; contains the **Ser518 phosphorylation site** (PAK1-mediated → "open" inactive conformation) and the C-terminal actin-binding region; the tail folds back onto the FERM domain in "closed" active conformation → FERM surface sterically available for tumor suppressor interactions

**Conformational switching:**
- **"Closed" (active)**: FERM domain contacts C-terminal tail intramolecularly → tumor-suppressive conformation; dominant at high cell density
- **"Open" (inactive)**: PAK1 phosphorylates Ser518 → electrostatic repulsion opens FERM-tail interface → EGFR endocytosis impaired, LATS kinase not activated; CDK1/cyclin B1 also phosphorylates Ser518 during M-phase

### Hippo pathway overview

Merlin activates the Hippo kinase cassette:
MST1/2 (STE20-family) → MOB1 → LATS1/2 (NDR-family) → phosphorylates YAP at Ser127 and TAZ at Ser89 → 14-3-3 binding → cytoplasmic retention → YAP/TAZ cannot enter nucleus

NF2 LOF → LATS1/2 not activated → YAP/TAZ unphosphorylated → nuclear import → interaction with TEAD1-4 TFs → transcriptional activation of CTGF, CYR61, BIRC5 (survivin), CCND1, MYC, AREG → proliferation, anti-apoptosis [^zhao-2007-yap-hippo]

## Function

### Normal NF2 roles

**Contact inhibition of proliferation:**
At confluent cell density, extracellular contacts (E-cadherin, CD44-hyaluronan, AJUBA/LIM proteins) → activate LATS1/2 (NF2-dependent) → YAP/TAZ cytoplasmic; NF2 is the mechanosensor that converts cell-cell contact signals into Hippo activation; NF2-null cells lack contact inhibition → grow to unlimited density (hallmark assay for NF2 tumor suppression)

**EGFR/ErbB receptor downregulation:**
Merlin binds EGFR intracellular domain → promotes clathrin-coated pit endocytosis → lysosomal degradation → reduced EGFR dwell time at plasma membrane; NF2-null → EGFR accumulates at surface → sustained MAPK, PI3K → growth without growth factor limitation

**Nuclear CRL4-DCAF1 axis:**
In nucleus, merlin binds and inhibits CRL4-DCAF1 E3 ubiquitin ligase → controls ubiquitination of LATS kinases and other substrates; merlin nuclear localization regulated by phospho-Ser518 (cytoplasmic when phosphorylated); this provides a second, cytoplasm-independent tumor suppressor mechanism

**Actin cytoskeleton:**
Merlin co-localizes with F-actin and β-spectrin at cell-cell junctions; coordinates Rho GTPase signaling (suppresses RAC1/PAK1 → prevents Ser518 auto-phosphorylation); NF2-null cells show disorganized cortical actin, increased motility, and invasive phenotype

## Mechanism

### Therapeutic targeting in NF2-null tumors

**mTOR inhibitors (everolimus, sirolimus):**
Rationale: NF2 loss → Hippo off → YAP/TAZ → CTGF/VEGF → mTORC1 activation; also direct AKT signaling from EGFR overexpression → mTOR

REACT trial (Goutagny 2015): N=10 NF2 patients; sirolimus for 12 months; VS volume stabilized or reduced in 70%; median tumor volume change −9.5%; progression-free at 12 months 70% vs 0% historical; FDA approval not achieved (too small; current practice: sirolimus/everolimus off-label in NF2 syndrome with growing VS not amenable to surgery).

**FAK inhibitors (defactinib, VS-6063):**
Merlin-null mesothelioma and schwannoma are dependent on FAK for survival (FAK supports adhesion signaling in absence of merlin-mediated cytoskeletal regulation); defactinib Phase 2 (COMMAND): no OS benefit in unselected mesothelioma; NF2-null enriched subset analysis ongoing

**MEK/ERK inhibitors:**
Merlin-null → sustained EGFR/RAS/MAPK → ERK1/2 hyperactivation; selumetinib Phase 2 in NF2 schwannoma (VS): modest volumetric reduction in ~25-30% of VS; ORR by hearing improvement modest but some responses noted

**TEAD inhibitors (VT3989, TED-347, IAG933):**
Directly disrupt YAP/TAZ-TEAD interaction or bind TEAD lipid pocket → TEAD TF complex destabilized; preclinical NF2-null mesothelioma: strong anti-tumor activity; Phase 1-2 trials ongoing for NF2-null tumors (mesothelioma, meningioma, schwannoma)

**Bevacizumab (anti-VEGF):**
NF2-null VS secrete VEGF (YAP target) → endolymphatic hydrops and tumor vascularity; bevacizumab reduces VS vascularity and hearing deterioration; hearing improvement in ~55% in small series; used off-label in NF2 syndrome for hearing preservation; no OS benefit proven

**Verteporfin:**
Benzoporphyrin derivative; clinical use: photodynamic therapy for AMD; incidentally found to disrupt YAP-TEAD binding in cell-based assays → used extensively as preclinical YAP inhibitor; local intratumoral delivery in meningioma models → YAP target gene suppression; not in clinical trials for CNS tumors (photosensitivity limits systemic use)

## Connections

- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — NF2/merlin activates LATS1/2 (Hippo) → YAP/TAZ cytoplasmic; YAP/TAZ nuclear → CTGF/CYR61 → mTORC1 activation; mTOR inhibitors (everolimus, sirolimus) reduce schwannoma volume in NF2 syndrome (Phase 2 REACT trial); rapalogs partially reverse NF2-driven growth.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Merlin promotes EGFR endocytosis and lysosomal degradation; NF2 loss → EGFR/ErbB2/ErbB3 surface accumulation → sustained PI3K/AKT and MAPK; anti-ErbB2 antibodies (lapatinib) explored in NF2-associated schwannoma; partial activity in Phase 2 trials.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — NF2/merlin and PTEN both restrain PI3K/AKT/mTOR; NF2 loss → AKT hyperactivation independent of PTEN; NF2+PTEN co-loss is synergistic in meningioma and mesothelioma; PTEN loss in ~10-15% meningioma; mTOR inhibitors target the convergent PI3K/mTOR axis in NF2-null tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Merlin suppresses RAS/MAPK by promoting EGFR endocytosis → reduced ERK1/2 activation; NF2-null schwannoma and meningioma show ERK1/2 hyperphosphorylation; MEK inhibitors (trametinib, binimetinib) and FAK inhibitors are being evaluated in NF2-deficient tumors.

[^rouleau-1993-nf2-gene]: Rouleau GA, Merel P, Lutchman M, et al. Alteration in a new gene encoding a putative membrane-organizing protein causes neuro-fibromatosis type 2. *Nature.* 1993;363(6429):515-521. [doi:10.1038/363515a0](https://doi.org/10.1038/363515a0) · [PubMed 8379998](https://pubmed.ncbi.nlm.nih.gov/8379998/)
[^zhao-2007-yap-hippo]: Zhao B, Wei X, Li W, et al. Inactivation of YAP oncoprotein by the Hippo pathway is involved in cell contact inhibition and tissue growth control. *Genes Dev.* 2007;21(21):2747-2761. [doi:10.1101/gad.1602907](https://doi.org/10.1101/gad.1602907) · [PubMed 17974916](https://pubmed.ncbi.nlm.nih.gov/17974916/)
