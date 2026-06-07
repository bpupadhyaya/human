---
schema: human-scale-entry/v1
id: cdkn1a
name: CDKN1A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CDKN1A (p21/WAF1/CIP1) is the primary p53 transcriptional target that inhibits CDK2-CyclinE and CDK4/6-CyclinD to block G1/S and G2/M transitions; PCNA-binding C-terminus halts DNA replication; key mediator of growth arrest, senescence, and DNA damage checkpoint."
aliases: ["CDKN1A", "p21", "WAF1", "CIP1", "p21WAF1", "p21CIP1", "CDKN1A p53 target", "cyclin-dependent kinase inhibitor 1A", "p21 senescence", "p21 PCNA"]
sources:
  - id: el-deiry-1993-waf1
    type: peer-reviewed
    cite: "el-Deiry WS, Tokino T, Velculescu VE, et al. WAF1, a potential mediator of p53 tumor suppression. Cell. 1993;75(4):817-825."
    doi: "10.1016/0092-8674(93)90500-p"
    pmid: "8242752"
    url: "https://doi.org/10.1016/0092-8674(93)90500-p"
  - id: harper-1993-cip1
    type: peer-reviewed
    cite: "Harper JW, Adami GR, Wei N, Keyomarsi K, Elledge SJ. The p21 Cdk-interacting protein Cip1 is a potent inhibitor of G1 cyclin-dependent kinases. Cell. 1993;75(4):805-816."
    doi: "10.1016/0092-8674(93)90499-g"
    pmid: "8211136"
    url: "https://doi.org/10.1016/0092-8674(93)90499-g"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 directly transcribes CDKN1A from two p53-response elements (5'RE ~2.4 kb and 3'RE ~1.3 kb upstream); p21 induction occurs within 2 hours of p53 activation; p21 is the primary mediator of p53-induced G1 cell cycle arrest; p21 levels parallel p53 activity in DNA damage."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "p21 inhibits CDK2-CyclinE and CDK4/6-CyclinD → Rb remains hypophosphorylated → E2F1/2/3 repressed → S-phase entry blocked; p21 is the upstream enforcer of Rb-mediated G1 arrest; Rb LOF bypasses p21-mediated cell cycle arrest."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2 ubiquitinates p21 (Lys161/163) for proteasomal degradation, counteracting p53-induced p21 accumulation; MDM2 also inhibits p53 → reduces p21 transcription; MDM2 inhibitors (nutlin-3/AMG-232) stabilize p53 → p21 induction → cell cycle arrest in MDM2-amplified tumors."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "In LFS (germline TP53), p53-driven p21 induction is severely impaired → cells fail to arrest at G1/S after DNA damage → accelerated cell cycle progression → malignant transformation; p21 loss contributes to genomic instability in TP53-mutant LFS tumors."
---

# CDKN1A

## Overview

**CDKN1A** (Cyclin-Dependent Kinase Inhibitor 1A; also p21, WAF1, CIP1, SDI1) encodes a 164 amino acid (21 kDa) protein that functions as the **primary transcriptional target of p53** and a multi-CDK inhibitor. CDKN1A was independently discovered as WAF1 (Wild-type p53-Activated Fragment 1, el-Deiry 1993) and CIP1 (CDK-Interacting Protein 1, Harper 1993) and is located at chromosome **6p21.2**. p21 belongs to the CIP/KIP family of CDK inhibitors (with CDKN1B/p27 and CDKN1C/p57) and restrains both G1/S and G2/M cell cycle transitions. A unique **PCNA-interacting domain** at the C-terminus allows p21 to directly halt DNA replication at replication forks. p21 is also a critical mediator of **oncogene-induced senescence (OIS)** and **replicative senescence**, making it a central node in tumor suppression independent of direct CDK inhibition [^el-deiry-1993-waf1] [^harper-1993-cip1].

**CDKN1A induction contexts:**

| Stimulus | Upstream signal | Mechanism |
|---|---|---|
| DNA damage (DSB, SSB) | ATM/ATR → CHK1/2 → p53 | p53 transcription of CDKN1A |
| Oncogene activation (RAS, MYC) | ARF/p14 → MDM2 inhibition → p53 | p53 transcription of CDKN1A; RAS also directly activates p21 via ERK-SP1 |
| Growth factor withdrawal | p53-independent pathways | SP1/SP3, FOXO3 transcription of p21 |
| Differentiation signals | TGF-β SMAD → p21 promoter | SMAD3-SP1 complex → p21 |
| Replicative senescence | p53/p16-Rb axis | Both p53→p21 and p16→Rb accumulate |
| Cytotoxic drugs | p53-dependent or independent | Doxorubicin (p53); 5-azacytidine (p21 demethylation) |

## Structure

### CDKN1A protein domains

**CDK-inhibitory (KID) domain (aa 1-71):**
- N-terminal inhibitory domain; contains ~4 CDK-binding elements
- Inhibits CDK2 (CyclinA/E) and CDK4/6 (CyclinD) by inserting into CDK active site cleft
- KID domain contacts CDK ATP-binding site and Thr160 activation loop → blocks substrate access
- One p21 molecule inhibits one CDK-cyclin complex; no stoichiometric requirement for full inhibition at physiological concentrations
- Specificity: KID domain shows broader CDK specificity than p27 KID; p21 inhibits CDK1, CDK2, CDK4, CDK5, CDK6

**Linker region (aa 72-143):**
- Flexible; nuclear localization sequence (NLS at aa 141-160 approximately); contains STAT3-binding motif
- Nuclear vs. cytoplasmic localization: nuclear p21 → CDK inhibition → growth arrest; cytoplasmic p21 → anti-apoptotic function (binds and inhibits procaspase-3, ASK1, RAFTK/Pyk2); cytoplasmic p21 accumulation is oncogenic in some contexts (AKT phosphorylates p21 at Thr145 → cytoplasmic retention)

**PCNA-binding domain (PIP box, aa 144-164):**
- C-terminal; consensus PIP box: Qxx(h)(h)xx(a)(a) (Q144LxxLF148FF motif in p21)
- Binds interdomain connecting loop (IDCL) of proliferating cell nuclear antigen (PCNA) homotrimeric sliding clamp
- p21-PCNA interaction: stoichiometric; p21 outcompetes DNA polymerase δ for PCNA binding → blocks replication fork progression → DNA synthesis arrest at S-phase
- p21 also blocks translesion synthesis (TLS) polymerases (Pol η, Pol κ) from accessing PCNA → prevents mutagenic bypass of lesions

**Regulatory modifications:**
- **Phosphorylation**: Thr145 (AKT → cytoplasmic), Ser146 (PKC), Ser130 (CDK2 → marks p21 for ubiquitination)
- **Ubiquitination**: MDM2 (Lys161/163), CRL4-Cdt2 (requires PCNA chromatin loading), SCFSKP2 → all target p21 for proteasomal degradation
- **Sumoylation**: SUMO-1 conjugation at Lys161 → blocks MDM2-mediated ubiquitination → p21 stabilization in some contexts

## Function

### G1/S checkpoint: p53→p21→Rb→E2F axis

Upon DNA double-strand break (DSB):
1. ATM kinase activated → phosphorylates CHK2 (Thr68) → CHK2 phosphorylates CDC25A → CDC25A ubiquitinated → CDK2 not activated (fast response)
2. ATM phosphorylates p53 (Ser15) → p53 released from MDM2 → p53 tetramers bind CDKN1A p53-response elements → p21 mRNA transcribed within 2 hours (slow but sustained response)
3. p21 protein accumulates → inhibits CDK2-CyclinE and CDK4/6-CyclinD → Rb remains hypophosphorylated → Rb-E2F1/2/3 complexes stay intact → E2F target genes (CCNE, CCNA, DHFR, thymidine kinase) repressed → G1 arrest maintained

### G2/M checkpoint

p21 also inhibits **CDK1-CyclinB** (the mitotic kinase):
- CDK1-CyclinB (MPF, M-phase Promoting Factor) is required for mitotic entry
- p21 inhibition of CDK1-CyclinB → cells arrested at G2/M (prevents mitosis following DNA damage)
- This G2/M arrest is particularly important in cells with defective G1 checkpoint (e.g., Rb-deficient cells)

### Senescence

**Oncogene-induced senescence (OIS):**
RAS/BRAF activation → ARF (p14/p19) → MDM2 sequestration → p53 accumulation → sustained p21 transcription → CDK2/4/6 inhibition → persistent Rb hypophosphorylation → E2F gene silencing → stable exit from cell cycle → OIS. p21 is sustained high in OIS (days to weeks), unlike transient p21 in DNA damage checkpoint recovery.

**Replicative senescence:**
Progressive telomere shortening → ATM/ATR activation → p53 → p21 + parallel accumulation of p16/INK4A → both p21 (via CDK2) and p16 (via CDK4/6) keep Rb hypophosphorylated → permanent cell cycle arrest = replicative senescence.

### p21 in DNA replication (PCNA axis)

During unperturbed S-phase: low-level p21 does not accumulate on chromatin (CRL4-Cdt2 degrades p21 when it binds PCNA on chromatin, ensuring replication can proceed). After DNA damage: p21 accumulates rapidly and overwhelms CRL4-Cdt2 degradation → PCNA binding → replication fork stalling → time for repair before re-start.

## Mechanism

### p21 in cancer contexts

**p21 as tumor suppressor:**
p21 LOF (uncommon by point mutation; more often silenced by methylation or upstream p53 LOF) → impaired G1/S checkpoint → accumulation of mutations → tumor initiation. CDKN1A is rarely directly mutated in cancer (<2% across cancer types); upstream p53 loss achieves p21 depletion indirectly.

**p21 as oncogene (cytoplasmic context):**
In some cancers (breast, gastric), cytoplasmic p21 accumulates (AKT → Thr145 phosphorylation → cytoplasmic retention) → p21 binds and inhibits procaspase-3 → apoptosis resistance; cytoplasmic p21 also binds ASK1 → blocks JNK/p38 stress-induced apoptosis. High cytoplasmic p21 IHC paradoxically correlates with poor prognosis in ER+ breast cancer.

**p21 and CDK4/6 inhibitors:**
In CDK4/6 inhibitor (palbociclib/ribociclib/abemaciclib)-treated cells: drug blocks CDK4/6 → Rb hypophosphorylation → G1 arrest; p21 plays a complementary role by further inhibiting residual CDK2 activity; tumors with p21 depletion (via p53 LOF) may have reduced sensitivity to CDK4/6i because the p21-CDK2 arm is absent.

**p21 and chemotherapy:**
p21-high tumors may be relatively resistant to cytotoxic chemotherapy (requires S-phase for efficacy): 5-FU, gemcitabine, platinum require cycling cells; p21-induced arrest removes cells from drug-sensitive phases. However, p21 also ensures subsequent apoptosis-competent repair; context-dependent.

## Connections

- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53 directly transcribes CDKN1A from two p53-response elements (5'RE ~2.4 kb and 3'RE ~1.3 kb upstream); p21 induction occurs within 2 hours of p53 activation; p21 is the primary mediator of p53-induced G1 cell cycle arrest; p21 levels parallel p53 activity in DNA damage.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — p21 inhibits CDK2-CyclinE and CDK4/6-CyclinD → Rb remains hypophosphorylated → E2F1/2/3 repressed → S-phase entry blocked; p21 is the upstream enforcer of Rb-mediated G1 arrest; Rb LOF bypasses p21-mediated cell cycle arrest.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 ubiquitinates p21 (Lys161/163) for proteasomal degradation, counteracting p53-induced p21 accumulation; MDM2 also inhibits p53 → reduces p21 transcription; MDM2 inhibitors (nutlin-3/AMG-232) stabilize p53 → p21 induction → cell cycle arrest in MDM2-amplified tumors.
- `connects-to` → **[Li-Fraumeni Syndrome](../../07-system/li-fraumeni-syndrome/README.md)** — In LFS (germline TP53), p53-driven p21 induction is severely impaired → cells fail to arrest at G1/S after DNA damage → accelerated cell cycle progression → malignant transformation; p21 loss contributes to genomic instability in TP53-mutant LFS tumors.

[^el-deiry-1993-waf1]: el-Deiry WS, Tokino T, Velculescu VE, et al. WAF1, a potential mediator of p53 tumor suppression. *Cell.* 1993;75(4):817-825. [doi:10.1016/0092-8674(93)90500-p](https://doi.org/10.1016/0092-8674(93)90500-p) · [PubMed 8242752](https://pubmed.ncbi.nlm.nih.gov/8242752/)
[^harper-1993-cip1]: Harper JW, Adami GR, Wei N, Keyomarsi K, Elledge SJ. The p21 Cdk-interacting protein Cip1 is a potent inhibitor of G1 cyclin-dependent kinases. *Cell.* 1993;75(4):805-816. [doi:10.1016/0092-8674(93)90499-g](https://doi.org/10.1016/0092-8674(93)90499-g) · [PubMed 8211136](https://pubmed.ncbi.nlm.nih.gov/8211136/)
