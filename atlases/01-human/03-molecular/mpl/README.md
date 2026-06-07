---
schema: human-scale-entry/v1
id: mpl
name: MPL
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "MPL (CD110) is the thrombopoietin receptor; pre-formed homodimer recruits JAK2 upon TPO binding → STAT5/STAT3 → megakaryopoiesis; MPL W515L/K mutations drive ET (~5-8%) and PMF (~8%); LOF mutations cause congenital amegakaryocytic thrombocytopenia; TPO-mimetics target MPL."
aliases: ["MPL", "CD110", "thrombopoietin receptor", "TPOR", "MPL W515L", "c-mpl", "TPO receptor", "MPL mutation MPN"]
sources:
  - id: pikman-2006-mpl-w515l
    type: peer-reviewed
    cite: "Pikman Y, Lee BH, Mercher T, et al. MPLW515L is a novel somatic activating mutation in myelofibrosis with myeloid metaplasia. PLoS Med. 2006;3(7):e270."
    doi: "10.1371/journal.pmed.0030270"
    pmid: "16834459"
    url: "https://doi.org/10.1371/journal.pmed.0030270"
  - id: ballmaier-2001-camt-mpl
    type: peer-reviewed
    cite: "Ballmaier M, Germeshausen M, Schulze H, et al. c-mpl mutations are the cause of congenital amegakaryocytic thrombocytopenia. Blood. 2001;97(1):139-146."
    doi: "10.1182/blood.V97.1.139"
    pmid: "11133753"
    url: "https://doi.org/10.1182/blood.V97.1.139"
cross_links:
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "TPO binds MPL → JAK2 homodimerization → JAK2/STAT5 in megakaryopoiesis; MPL W515L/K mutations (~5-8% ET, ~8% PMF) cause constitutive JAK2 activation without TPO; ruxolitinib is active in MPL-mutant ET/PMF via JAK1/2 inhibition."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "CALR-mutant protein (frameshift C-terminus) binds MPL extracellular domain → constitutive JAK2/STAT5; CALR and MPL mutations are mutually exclusive MPN drivers; both target the TPO-MPL-JAK2 axis; CALR type 2 → ET phenotype, CALR type 1 → PMF phenotype."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "MPL-expressing megakaryocytes release TGF-β1 upon activation; megakaryocytic hyperplasia in ET/PMF → increased TGF-β1 → reticulin/collagen fibrosis; JAK inhibitors reduce megakaryocyte burden and TGF-β-driven fibrosis in post-ET/post-PV MF."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "MPL→JAK2→STAT5 (primary) and STAT3 (secondary) signaling drive MPN; STAT3 promotes survival and cytokine production in MPN clones; persistent STAT3 activation correlates with inflammation in PV/ET/PMF; JAK inhibitors suppress both STAT5 and STAT3 phosphorylation."
---

# MPL

## Overview

**MPL (Myeloproliferative Leukemia protein, CD110)** is the **thrombopoietin receptor (TPOR)**, a type I cytokine receptor that transduces the primary megakaryopoietic and thrombopoietic signal from thrombopoietin (TPO). MPL is expressed on hematopoietic stem cells (HSCs), megakaryocyte progenitors, and platelets; it exists as a pre-formed homodimer on the cell surface and activates **JAK2→STAT5/STAT3→PI3K-AKT and MAPK** pathways upon TPO binding, driving megakaryocyte proliferation, maturation, and platelet release. MPL gained oncological significance when **somatic MPL gain-of-function mutations** (W515L, W515K) were identified in ~5-8% of essential thrombocythemia (ET) and ~8% of primary myelofibrosis (PMF) — these mutations constitutively activate JAK2 independently of TPO and phenocopy CALR mutations in their biology [^pikman-2006-mpl-w515l]. Conversely, **germline MPL loss-of-function mutations** cause **congenital amegakaryocytic thrombocytopenia (CAMT)** — a life-threatening neonatal thrombocytopenia that evolves to aplastic anemia due to complete absence of megakaryopoiesis [^ballmaier-2001-camt-mpl]. MPL is also the physiological target of **TPO-receptor agonists** (eltrombopag, romiplostim, avatrombopag) used in aplastic anemia, immune thrombocytopenia (ITP), and liver disease-associated thrombocytopenia.

**MPL in disease:**
- **ET:** MPL W515L/K ~5-8%; clinically similar to CALR-mutant ET (lower thrombosis risk than JAK2 V617F); first described in myelofibrosis but also found in ET
- **PMF:** MPL W515L/K ~8%; can also present with exon 10 mutations (S505, Y591, A506)
- **CAMT type I (null mutations):** Neonatal thrombocytopenia → aplasia in infancy; allo-SCT curative; MPL protein absent
- **CAMT type II (missense mutations):** Partial MPL function → milder thrombocytopenia presenting later; may not evolve to aplasia
- **Secondary cytopenia treatment:** Eltrombopag (Promacta) and romiplostim (Nplate) are non-peptide/peptide TPO-receptor agonists approved for aplastic anemia and ITP; avatrombopag (Doptelet) and lusutrombopag (Mulpleta) for liver disease thrombocytopenia

## Structure

### MPL protein architecture

MPL is a 635-amino-acid type I transmembrane glycoprotein with four disulfide-bonded fibronectin type III (FN III) repeats in the extracellular domain:

**Extracellular domain (ECD, 1-491):**
- **Domain 1 (D1, ~1-240):** N-terminal cytokine-binding homology module (CHM); contains the WSXWS motif (Trp-Ser-Xaa-Trp-Ser, critical for proper folding and surface expression); primary TPO-binding site
- **Domain 2 (D2, ~241-491):** Second FN III repeat; co-receptor stabilization; additional TPO contact surface
- **Pre-formed homodimer:** MPL exists as a homodimer on the cell surface prior to TPO binding (unlike some cytokine receptors that dimerize upon ligand binding); TPO binding induces a conformational change in the pre-formed dimer → activates JAK2 in trans

**Transmembrane domain (492-513):**
Contains **Trp515** — the site of pathogenic GOF mutations; Trp515 is in the juxtatransmembrane/intracellular boundary; W515L or W515K removes a critical bulky aromatic residue → allows constitutive transmembrane domain dimerization in the active conformation → JAK2 activation without TPO; the Trp515 residue is conserved across mammals and is part of an amphipathic helix that regulates MPL dimer angle.

**Intracellular domain (514-635):**
- **Box 1/Box 2 motifs:** JAK2 binding sequences; Box 1 (Pro-X-Pro, ~519-524) recruits JAK2 JH7 domain; Box 2 (~535-548) stabilizes JAK2 association; JAK2 binds constitutively to resting MPL even without TPO (ligand-independent association)
- **STAT5 docking sites:** Y599/Y600 → phosphorylated by JAK2 → STAT5 SH2 docking → STAT5 phosphorylation → dimerization → nuclear translocation → BCL-XL, CCND1, MYC gene expression
- **Ubiquitin ligase recruitment:** LNK (SH2B3) adaptor protein → recruited to phosphorylated MPL → recruits CBL/c-CBL → MPL ubiquitination → internalization → lysosomal degradation; LNK mutations occur in ~6% MPN → prolonged MPL surface expression → enhanced JAK2/STAT5 signaling

### TPO-receptor agonist structure (therapeutic implications)

**Eltrombopag (Promacta):** Non-peptide small molecule; binds transmembrane domain of MPL (not ECD) — different from TPO binding site → agonist activity; species-specific (active on human/chimpanzee MPL only); oral; FDA approved for ITP, aplastic anemia (with ATG+CsA), thrombocytopenia after HCV treatment.

**Romiplostim (Nplate):** Fc-peptide fusion protein (peptibody); four TPO-mimetic peptides fused to IgG1 Fc → binds MPL ECD (overlaps with TPO binding site); weekly SC injection; FDA approved for ITP and aplastic anemia.

**Avatrombopag:** Oral small molecule; binds MPL transmembrane similar to eltrombopag; FDA approved for liver disease-associated thrombocytopenia (not requiring dose adjustment in renal/hepatic impairment); does NOT require strict food restrictions (unlike eltrombopag which requires 2-hour food avoidance).

## Function

### Normal TPO-MPL-JAK2 axis in megakaryopoiesis

**Physiological regulation:**
TPO (THPO) is produced constitutively by liver and kidney; circulating TPO level is regulated by platelet and megakaryocyte mass (platelets and megakaryocytes express MPL → bind and internalize TPO → reduce free TPO level → inverse TPO-platelet relationship). Normal platelet count → high TPO consumption → lower free TPO. Thrombocytopenia → reduced TPO clearance → elevated free TPO → megakaryocyte stimulation → platelet production restoration.

**Megakaryocyte development:**
TPO→MPL→JAK2/STAT5→PI3K-AKT:
- **Proliferation:** STAT5 → CCND1 (cyclin D1) → S-phase entry; BFU-MK and CFU-MK expansion
- **Endomitosis:** Megakaryocytes undergo 4N-128N polyploidization (re-replication without cytokinesis) → large polyploid megakaryocytes; TPO-MPL promotes endomitosis; larger megakaryocytes produce more pro-platelets and platelets
- **Proplatelet formation:** Megakaryocytes extend cytoplasmic projections (proplatelets) through sinusoidal endothelium → platelet release; CXCL12/CXCR4 directs megakaryocyte migration to sinusoids; TPO-MPL supports survival throughout
- **HSC maintenance:** MPL is expressed on long-term HSCs; TPO-MPL maintains HSC quiescence in the bone marrow niche; TPO-receptor agonists can activate HSC expansion (mechanism of aplastic anemia recovery with eltrombopag)

### MPL in CALR-mutant MPN

CALR-mutant protein has an abnormal positively charged C-terminus (frameshift neoepitope); this CALR mutant C-terminus specifically binds the MPL ECD (domain D2/D3 region) → forms a CALR-MPL complex → constitutive JAK2 signaling even without TPO; the binding is highly selective for MPL (CALR mutant does not activate other type I cytokine receptors efficiently); elucidates why CALR mutations are functionally equivalent to MPL W515 mutations in their JAK2 activation phenotype.

## Mechanism

### MPL W515 gain-of-function mechanism

**W515L/K structural consequence:**
Trp515 at the juxtatransmembrane boundary normally maintains the MPL homodimer in a "resting" angular conformation through its bulky indole side chain; W515L (Leu) or W515K (Lys) → removal of steric/aromatic constraint → transmembrane helices adopt active rotational angle → JAK2 transphosphorylation occurs constitutively → STAT5/STAT3/PI3K activation without TPO; similar mechanism to other transmembrane-domain GOF mutations (e.g., FLT3-D835, EGFR L858R alter kinase conformation, though JAK2 activation here is indirect via MPL conformational change) [^pikman-2006-mpl-w515l].

**Disease phenotype:**
MPL W515L primary myelofibrosis: JAK2 V617F-negative PMF with megakaryocytic hyperplasia, reticulin fibrosis, splenomegaly; responds to ruxolitinib similarly to JAK2 V617F PMF (fedratinib, pacritinib, momelotinib also active); allele burden monitoring by targeted sequencing; MPL W515 allele burden correlates with marrow fibrosis grade.

### CAMT — MPL loss of function

**CAMT type I (complete LOF):**
Frameshift/nonsense mutations → truncated/absent MPL → no TPO signaling → megakaryocyte progenitors cannot receive survival signal → megakaryocyte and platelet aplasia from birth; neonatal thrombocytopenia (<50 × 10⁹/L); BM biopsy: absent megakaryocytes; evolves to trilineage aplasia (HSC pool depends on MPL for maintenance) → pancytopenia by age 3-5; treatment: allo-SCT (only curative); TPO-receptor agonists non-functional (receptor absent); supportive platelet transfusions pre-SCT [^ballmaier-2001-camt-mpl].

**CAMT type II (partial LOF):**
Missense mutations that partially preserve MPL function → delayed onset thrombocytopenia (months to years); some megakaryocyte function retained; aplasia less common or delayed; may respond partially to eltrombopag (if some receptor function preserved); genetic testing critical for family counseling.

### Therapeutic MPL activation

**Aplastic anemia — eltrombopag:**
Severe aplastic anemia (SAA): horse ATG + cyclosporine + eltrombopag (starting Day 1) → CR rate improved vs horse ATG+CsA alone (~94% hematologic response vs ~74%); eltrombopag acts on MPL on HSCs → stimulates HSC self-renewal → multilineage recovery; somatic cytogenetic abnormalities can emerge with eltrombopag (~6-7%, particularly del(7) and trisomy 8); hematologic monitoring essential.

**Immune thrombocytopenia (ITP):**
Eltrombopag or romiplostim: overcome immune destruction by stimulating megakaryocyte output; 2nd-line after corticosteroids; platelet response in ~70-80%; dose-dependent; continue until durable off-therapy remission; romiplostim may be preferred in certain patient populations (once weekly vs daily oral).

## Connections

- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — TPO binds MPL → JAK2 homodimerization → JAK2/STAT5 in megakaryopoiesis; MPL W515L/K mutations (~5-8% ET, ~8% PMF) cause constitutive JAK2 activation without TPO; ruxolitinib is active in MPL-mutant ET/PMF via JAK1/2 inhibition.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — CALR-mutant protein (frameshift C-terminus) binds MPL extracellular domain → constitutive JAK2/STAT5; CALR and MPL mutations are mutually exclusive MPN drivers; both target the TPO-MPL-JAK2 axis; CALR type 2 → ET phenotype, CALR type 1 → PMF phenotype.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — MPL-expressing megakaryocytes release TGF-β1 upon activation; megakaryocytic hyperplasia in ET/PMF → increased TGF-β1 → reticulin/collagen fibrosis; JAK inhibitors reduce megakaryocyte burden and TGF-β-driven fibrosis in post-ET/post-PV MF.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — MPL→JAK2→STAT5 (primary) and STAT3 (secondary) signaling drive MPN; STAT3 promotes survival and cytokine production in MPN clones; persistent STAT3 activation correlates with inflammation in PV/ET/PMF; JAK inhibitors suppress both STAT5 and STAT3 phosphorylation.

[^pikman-2006-mpl-w515l]: Pikman Y, Lee BH, Mercher T, et al. MPLW515L is a novel somatic activating mutation in myelofibrosis with myeloid metaplasia. *PLoS Med.* 2006;3(7):e270. [doi:10.1371/journal.pmed.0030270](https://doi.org/10.1371/journal.pmed.0030270) · [PubMed 16834459](https://pubmed.ncbi.nlm.nih.gov/16834459/)
[^ballmaier-2001-camt-mpl]: Ballmaier M, Germeshausen M, Schulze H, et al. c-mpl mutations are the cause of congenital amegakaryocytic thrombocytopenia. *Blood.* 2001;97(1):139-146. [doi:10.1182/blood.V97.1.139](https://doi.org/10.1182/blood.V97.1.139) · [PubMed 11133753](https://pubmed.ncbi.nlm.nih.gov/11133753/)
