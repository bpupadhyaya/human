---
schema: human-scale-entry/v1
id: thrombopoietin
name: Thrombopoietin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Thrombopoietin (TPO; THPO, chr3q27.3) is the master regulator of megakaryopoiesis; binds c-Mpl → JAK2/STAT5 → platelet production. Levels inversely correlate with platelet count via Mpl absorption. TPO-receptor agonists (romiplostim, eltrombopag) treat ITP and aplastic anemia."
aliases: ["TPO", "THPO", "c-Mpl ligand", "thrombopoiesis-stimulating factor", "romiplostim target", "eltrombopag target"]
sources:
  - id: desauvage-1994-tpo-discovery
    type: peer-reviewed
    cite: "de Sauvage FJ, Hass PE, Spencer SD, et al. Stimulation of megakaryocytopoiesis and thrombopoiesis by the c-Mpl ligand. Nature. 1994;369(6481):533-538."
    doi: "10.1038/369533a0"
    pmid: "8202154"
  - id: bussel-2006-romiplostim-itp
    type: peer-reviewed
    cite: "Bussel JB, Kuter DJ, George JN, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. N Engl J Med. 2006;355(16):1672-1681."
    doi: "10.1056/NEJMoa054626"
    pmid: "17050891"
  - id: cheng-2011-eltrombopag-raise
    type: peer-reviewed
    cite: "Cheng G, Saleh MN, Marcher C, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE): a 6-month, randomised, phase 3 study. Lancet. 2011;377(9763):393-402."
    doi: "10.1016/S0140-6736(10)60959-2"
    pmid: "21237459"
  - id: kuter-2013-tpo-review
    type: peer-reviewed
    cite: "Kuter DJ. The biology of thrombopoietin and thrombopoietin receptor agonists. Int J Hematol. 2013;98(1):10-23."
    doi: "10.1007/s12185-013-1382-0"
    pmid: "23821195"
cross_links:
  - target: 01-human/04-cellular/platelet
    relation: modulates
    note: "TPO drives megakaryocyte proliferation and proplatelet formation via c-Mpl → JAK2/STAT5 → GATA-1/FOG-1; platelet count inversely regulates TPO via Mpl absorption; elevated TPO in thrombocytopenia drives compensatory thrombopoiesis."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "In ITP, anti-platelet IgG destroys platelets faster than bone marrow can compensate despite elevated TPO; romiplostim (AMG 531; FDA Aug 2008) and eltrombopag (RAISE; FDA Nov 2008) bypass anti-platelet antibody destruction by stimulating megakaryocytes directly via c-Mpl."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn recycles anti-platelet IgG sustaining pathogenic titers in ITP; efgartigimod (FcRn inhibitor; FDA Jun 2023) and TPO-RAs (romiplostim, eltrombopag) address complementary mechanisms — IgG catabolism vs. platelet production; their combination is under investigation."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "MPL W515L/K mutation constitutively activates JAK2 independent of TPO → megakaryocyte dysplasia → marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia limits JAK inhibitor dosing in high-risk MF; pacritinib/momelotinib address MF+thrombocytopenia."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "In severe AA, T-cell HSC destruction → thrombocytopenia; TPO rises but megakaryocyte progenitors are depleted; eltrombopag added to hATG+CsA (triple IST) improves overall response; eltrombopag uniquely expands HSCs via c-Mpl independent of megakaryopoiesis drive."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "TPO is produced by hepatocytes (70-80%) and bone marrow osteoblasts → c-Mpl on megakaryocyte progenitors → JAK2/STAT5 → megakaryopoiesis; bone marrow is the primary TPO-sensing organ via c-Mpl absorption; CAMT results from MPL LOF → absent megakaryocytes from birth."
---

# Thrombopoietin

## Overview

Thrombopoietin (TPO), encoded by the *THPO* gene on chromosome 3q27.3, is the primary cytokine regulating platelet production. It was the final member of the haematopoietic growth factor family to be cloned, identified simultaneously in 1994 by five independent groups — including de Sauvage et al. at Genentech — as the ligand for the orphan receptor c-Mpl [^desauvage-1994-tpo-discovery]. The discovery established the molecular basis of megakaryopoiesis regulation and ultimately led to a class of drugs — **thrombopoietin receptor agonists (TPO-RAs)** — that have transformed the treatment of chronic immune thrombocytopenia (ITP), aplastic anemia, and thrombocytopenia in chronic liver disease.

## Structure

### Protein Architecture

The *THPO* gene encodes a 332-amino acid precursor (353 aa including signal peptide in some references) that is processed to a mature secreted glycoprotein of approximately **60–80 kDa**. TPO contains two structurally and functionally distinct domains:

| Domain | Size | Structure | Function |
|:-------|:-----|:----------|:---------|
| **N-terminal (EPO-like domain)** | ~164 aa | 4-helix bundle; homologous to erythropoietin | Receptor binding; sufficient for full signaling |
| **C-terminal (glycosylated domain)** | ~168 aa | Heavily O-glycosylated; no known homology | Required for protein stability and circulatory half-life; not required for signaling |

The N-terminal domain binds the **c-Mpl receptor** (also termed CD110, MPL; encoded by *MPL* on chr1p34.2). c-Mpl is a homodimeric type I cytokine receptor with two fibronectin type III domains in its extracellular region. Binding of one TPO molecule to two c-Mpl chains induces receptor dimerization and trans-phosphorylation.

### TPO Receptor (c-Mpl) Signaling

TPO → c-Mpl homodimerization → JAK2 trans-phosphorylation → multiple downstream cascades:

1. **JAK2/STAT5**: Principal signaling arm → STAT5 homodimers → nuclear translocation → transcription of BCL-XL (anti-apoptotic), cyclin D1 (proliferation), GATA-1/FOG-1 (megakaryocyte differentiation)
2. **PI3K/Akt**: Promotes megakaryocyte survival and endomitosis
3. **MAPK (ERK1/2)**: Proliferative signal in megakaryocyte progenitors
4. **mTORC1**: Megakaryocyte polyploidization and proplatelet formation

Negative regulation: SOCS1 and SOCS3 (STAT-induced STAT inhibitors) are upregulated by TPO signaling → JAK2 inhibition → feedback attenuation.

## Function

### Megakaryopoiesis Regulation

TPO drives the entire megakaryocyte developmental cascade: HSC → megakaryocyte-erythroid progenitor (MEP) → BFU-Mk → CFU-Mk → megakaryoblast → promegakaryocyte → **megakaryocyte** (high-ploidy, 8N–128N) → proplatelet formation → **platelets** (250–400 × 10⁹/L normal range).

The key platelet transcription factors — **GATA-1**, **FOG-1** (ZFPM1), **NF-E2** (p45/p18), and **FLI-1** — are all downstream of JAK2/STAT5 activation by TPO.

### Inverse Regulation by Platelet Count

TPO is constitutively produced by **hepatocytes** (70–80% of circulating TPO) and to a lesser extent by kidneys, bone marrow stromal cells, and smooth muscle. Unlike most cytokines, TPO is not regulated at the transcriptional level in response to platelet count; instead, **circulating levels are set by c-Mpl-mediated absorption**:

- Platelets and megakaryocytes bear high c-Mpl density → when platelet count is normal, c-Mpl absorbs TPO continuously → low free TPO
- Thrombocytopenia → fewer c-Mpl receptors → reduced TPO absorption → elevated free TPO → megakaryocyte stimulation → compensatory platelet production
- In ITP: platelet count is low but TPO is only modestly elevated — because megakaryocyte mass (and c-Mpl on MKs) is actually increased, blunting the TPO rise; this explains why exogenous TPO-RAs can still further stimulate platelet production despite elevated endogenous TPO

This "c-Mpl sponge" homeostatic model is distinct from the feedback mechanisms of other haematopoietic cytokines [^kuter-2013-tpo-review].

## Mechanism

### TPO-Receptor Agonists (TPO-RAs)

Three classes of TPO-RAs have been developed:

**Peptibodies (Fc-peptide fusions):**
- **Romiplostim** (Nplate; Amgen) — Four copies of a 14-amino acid TPO-mimetic peptide fused to the Fc region of IgG1; binds c-Mpl at the same site as endogenous TPO; **not** homologous to TPO in sequence. FDA approved **August 2008** for chronic ITP in adults who have had an insufficient response to corticosteroids, IVIG, or splenectomy. The pivotal trial (Bussel 2006) showed platelet response in 88% vs 14% placebo [^bussel-2006-romiplostim-itp].

**Non-peptide small molecules:**
- **Eltrombopag** (Promacta/Revolade; Novartis/GSK) — Biarylhydrazone compound that binds the **transmembrane domain of c-Mpl** (a unique mechanism distinct from the extracellular ligand-binding domain); activates JAK2/STAT5 signaling; oral bioavailability; also enhances intestinal iron absorption by blocking ferroportin internalization. FDA approved **November 2008** for chronic ITP. The RAISE trial (Cheng 2011) showed platelet response in 59% vs 16% placebo at 6 months [^cheng-2011-eltrombopag-raise]. Also approved for aplastic anemia (with horse-ATG + cyclosporine → improved response rates), hepatitis C-associated thrombocytopenia, and severe aplastic anemia refractory to IST.
- **Avatrombopag** (Doptelet; AkaRx) — Orally bioavailable; also binds TM domain of c-Mpl; approved for chronic ITP (adult) and thrombocytopenia in adults with chronic liver disease (CLD) undergoing planned procedures (ADAPT-1/2 trials).
- **Lusutrombopag** (Mulpleta; Shionogi) — c-Mpl TM domain agonist; approved for CLD thrombocytopenia.

### Pathological c-Mpl Mutations

| Mutation | Context | Effect |
|:---------|:--------|:-------|
| MPL W515L/K | Essential thrombocythaemia, primary myelofibrosis | Constitutive JAK2/STAT5 → thrombocytosis |
| MPL S505N | Familial thrombocythaemia | Gain-of-function; hereditary |
| MPL LOF | Congenital amegakaryocytic thrombocytopenia (CAMT) | Absent megakaryocytes → severe thrombocytopenia from birth |

JAK2 V617F (somatic; found in ~95% of polycythemia vera, ~50-60% of ET, ~50% of PMF) does not directly alter MPL but creates a TPO-independent constitutively active JAK2 — functionally mimicking continuous TPO stimulation.

## Connections

- `modulates` → **[Platelet](../../04-cellular/platelet/README.md)** — TPO drives megakaryocyte proliferation and platelet shedding via c-Mpl → JAK2/STAT5 → GATA-1/FOG-1; platelet count inversely controls free TPO via Mpl-mediated absorption; elevated TPO in thrombocytopenia drives compensatory thrombopoiesis.
- `connects-to` → **[Immune Thrombocytopenia](../../07-system/immune-thrombocytopenia/README.md)** — In ITP, anti-platelet IgG destroys platelets despite elevated TPO; romiplostim and eltrombopag bypass anti-platelet immunity by directly stimulating c-Mpl on megakaryocyte progenitors; both FDA-approved 2008 as second-line ITP therapy.
- `connects-to` → **[FcRn](../fcrn/README.md)** — FcRn recycles anti-platelet IgG, sustaining pathogenic titers in ITP; efgartigimod (anti-FcRn; FDA 2023) reduces anti-platelet antibody burden; TPO-RAs and FcRn inhibitors address complementary ITP mechanisms — increasing production vs. reducing antibody-mediated destruction.
- `connects-to` → **[Myelofibrosis](../../07-system/myelofibrosis/README.md)** — MPL W515L/K mutation constitutively activates JAK2 independent of TPO → megakaryocyte dysplasia → marrow fibrosis; ruxolitinib suppresses JAK-STAT; thrombocytopenia limits JAK inhibitor dosing in high-risk MF; pacritinib/momelotinib address MF+thrombocytopenia.
- `connects-to` → **[Aplastic Anemia](../../07-system/aplastic-anemia/README.md)** — In severe AA, T-cell HSC destruction → thrombocytopenia; TPO rises but megakaryocyte progenitors are depleted; eltrombopag added to hATG+CsA (triple IST) improves overall response; eltrombopag uniquely expands HSCs via c-Mpl independent of megakaryopoiesis drive.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — TPO is produced by hepatocytes (70-80%) and bone marrow osteoblasts → c-Mpl on megakaryocyte progenitors → JAK2/STAT5 → megakaryopoiesis; bone marrow is the primary TPO-sensing organ via c-Mpl absorption; CAMT results from MPL LOF → absent megakaryocytes from birth.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^desauvage-1994-tpo-discovery]: de Sauvage FJ, et al. Stimulation of megakaryocytopoiesis and thrombopoiesis by the c-Mpl ligand. *Nature.* 1994;369(6481):533-538. [doi:10.1038/369533a0](https://doi.org/10.1038/369533a0) · [PubMed 8202154](https://pubmed.ncbi.nlm.nih.gov/8202154/)
[^bussel-2006-romiplostim-itp]: Bussel JB, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. *N Engl J Med.* 2006;355(16):1672-1681. [doi:10.1056/NEJMoa054626](https://doi.org/10.1056/NEJMoa054626) · [PubMed 17050891](https://pubmed.ncbi.nlm.nih.gov/17050891/)
[^cheng-2011-eltrombopag-raise]: Cheng G, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE). *Lancet.* 2011;377(9763):393-402. [doi:10.1016/S0140-6736(10)60959-2](https://doi.org/10.1016/S0140-6736(10)60959-2) · [PubMed 21237459](https://pubmed.ncbi.nlm.nih.gov/21237459/)
[^kuter-2013-tpo-review]: Kuter DJ. The biology of thrombopoietin and thrombopoietin receptor agonists. *Int J Hematol.* 2013;98(1):10-23. [doi:10.1007/s12185-013-1382-0](https://doi.org/10.1007/s12185-013-1382-0) · [PubMed 23821195](https://pubmed.ncbi.nlm.nih.gov/23821195/)
