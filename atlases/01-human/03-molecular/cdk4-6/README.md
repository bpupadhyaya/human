---
schema: human-scale-entry/v1
id: cdk4-6
name: CDK4/6
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Cyclin D-dependent kinases; phosphorylate Rb to release E2F transcription factors → G1→S cell cycle entry. Amplified or activated in HR+ breast cancer, melanoma (CDKN2A loss), and others. Palbociclib, ribociclib, abemaciclib block CDK4/6 → Rb hypophosphorylation → G1 arrest."
aliases: ["CDK4", "CDK6", "cyclin-dependent kinase 4", "cyclin-dependent kinase 6", "CDK4/6 inhibitor"]
sources:
  - id: sherr-2016-cdk4-rb
    type: peer-reviewed
    cite: "Sherr CJ, Beach D, Shapiro GI. Targeting CDK4 and CDK6: From Discovery to Therapy. Cancer Discov. 2016;6(4):353-367."
    doi: "10.1158/2159-8290.CD-15-0894"
    pmid: "26658964"
    url: "https://doi.org/10.1158/2159-8290.CD-15-0894"
  - id: finn-2016-palbociclib
    type: peer-reviewed
    cite: "Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. N Engl J Med. 2016;375(20):1925-1936."
    doi: "10.1056/NEJMoa1607303"
    pmid: "27959613"
    url: "https://doi.org/10.1056/NEJMoa1607303"
  - id: roberts-1994-cdk4
    type: peer-reviewed
    cite: "Serrano M, Hannon GJ, Beach D. A new regulatory motif in cell-cycle control causing specific inhibition of cyclin D/CDK4. Nature. 1993;366(6456):704-707."
    doi: "10.1038/366704a0"
    pmid: "8259214"
    url: "https://doi.org/10.1038/366704a0"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 induces p21 (CDKN1A) → inhibits CDK4/6-cyclin D → Rb stays hypophosphorylated → G1 arrest; this p53→p21→CDK4/6 axis is the G1 DNA damage checkpoint; p53 loss or CDK4/6 amplification both bypass this checkpoint, enabling proliferation despite DNA damage."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC upregulates cyclin D2/D3 and suppresses p21/p27 → activates CDK4/6 → Rb phosphorylation → E2F S-phase entry; MYC and CDK4/6 amplifications cooperate to maximally accelerate G1→S; CDK4/6 is a key effector of MYC-driven proliferation in cancer."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTORC1 drives cyclin D1 and CDK4 expression via 4E-BP1 → cap-dependent translation; CDK4/6 inhibition and mTOR inhibition synergize in ER+ breast cancer — CDK4/6i relieves mTOR-mediated IRS-1 feedback inhibition, and CDK4/6i+mTORi is active in palbociclib-resistant disease."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS-MEK-ERK promotes cyclin D1 synthesis and CDK4/6 activity → drives G1→S in RAS-mutant cancers; CDKN2A (encoding p16 CDK4/6 inhibitor) is frequently co-deleted with KRAS pathway activation in PDAC and NSCLC; CDK4/6 inhibitors show modest activity in KRAS-mutant lung cancer."
---

# CDK4/6

## Overview

**CDK4 and CDK6 (cyclin-dependent kinases 4 and 6)** are the gatekeepers of the G1→S phase transition in the mammalian cell cycle — the fundamental decision point where quiescent cells commit to DNA replication and cell division. They function as the kinase subunits of **cyclin D-CDK4/6 holoenzyme complexes** (cyclin D1, D2, or D3 paired with CDK4 or CDK6), activated by mitogenic signaling to **phosphorylate and inactivate the retinoblastoma tumor suppressor (Rb)**.

The **Rb phosphorylation cascade** — the central event in CDK4/6-driven cell cycle progression:
1. Cyclin D-CDK4/6 → monoPhosphorylates Rb at multiple sites (14 CDK consensus sites) → partial inactivation
2. Cyclin E-CDK2 → hyperphosphorylates Rb → complete inactivation
3. HyperPhospho-Rb → releases E2F transcription factors (E2F1, E2F2, E2F3) → E2F-dependent transcription: DNA replication machinery (MCM2-7, Cdc6, PCNA), cyclin E, cyclin A → irreversible S-phase commitment

**Restriction point:** Mammalian cells pass the "restriction point" in mid-to-late G1 — the point beyond which cells are committed to division regardless of mitogen withdrawal. This point corresponds to the switch from Rb-repressed to E2F-activated state, driven by CDK4/6 and CDK2.

**Oncogenic deregulation of CDK4/6:**
- **CDKN2A (p16^INK4a) deletion:** Encodes p16, the specific endogenous CDK4/6 inhibitor; deleted in melanoma (~50%), PDAC (~90%), NSCLC (~25%), GBM (~50%), bladder cancer, HNSCC — one of the most frequently deleted tumor suppressors in human cancer
- **CDK4 amplification (12q14):** Melanoma (~10%), sarcoma, glioblastoma
- **CDK6 amplification (7q21):** Lymphoma, AML, T-ALL (~30%)
- **Cyclin D1 (CCND1) amplification/overexpression:** Mantle cell lymphoma (100%, t(11;14)), HNSCC (~40%), ER+ breast cancer (~25%), esophageal cancer
- **Rb1 loss:** Retinoblastoma (100%), SCLC (~90%), triple-negative breast cancer, bladder cancer → when Rb is lost, CDK4/6 inhibitors cannot function (no target) → primary resistance

## Structure

### CDK4/6 protein structure [^sherr-2016-cdk4-rb]

CDK4 (303 aa) and CDK6 (326 aa) share ~71% sequence identity and nearly identical functions in the cell cycle, though with distinct tissue expression patterns and inhibitor sensitivities:

- **PSTAIRE helix (CDK4/6 equivalent: PISTVRE for CDK4):** The cyclin-binding helix in the N-lobe; cyclin D binding activates the kinase by repositioning the activation loop
- **T-loop (activation loop):** Contains Thr172 (CDK4)/Thr177 (CDK6); CDK-activating kinase (CAK = CDK7/cyclin H/MAT1) phosphorylates T-loop → full kinase activation; unlike CDK1/2, CDK4/6 can be partially active without T-loop phosphorylation when complexed with cyclin D
- **ATP-binding cleft:** Hinge region between N- and C-lobes; site of pharmacological CDK4/6 inhibitor binding (palbociclib, ribociclib, abemaciclib occupy ATP binding pocket with high selectivity)
- **INK4 binding surface:** p16^INK4a and other INK4 proteins (p15, p18, p19) bind CDK4/6 at the D-helix in the N-lobe and T-loop in the C-lobe → distort the cyclin D binding site → displace cyclin D → inactivate kinase; INK4 proteins are specific CDK4/6 inhibitors (CIP/KIP family = p21, p27, p57 inhibit CDK1/2/4/6)

### INK4-CIP/KIP inhibitor families

**INK4 family (CDK4/6-specific):** p16^INK4a (CDKN2A), p15^INK4b (CDKN2B), p18^INK4c (CDKN2C), p19^INK4d (CDKN2D)
- Bind only CDK4/6 (not CDK1/2)
- Compete with cyclin D for CDK4/6 binding
- Tumor suppressive: p16 is the most commonly deleted CDK4/6 inhibitor

**CIP/KIP family (broad CDK inhibitors):** p21^CIP1 (CDKN1A), p27^KIP1 (CDKN1B), p57^KIP2 (CDKN1C)
- Inhibit CDK1, 2, 4, and 6
- Also required in specific stoichiometry for CDK4/6-cyclin D assembly (paradoxically, low p21/p27 promote CDK4/6 assembly while high p21/p27 inhibit)
- p27 levels controlled by mitogens → Skp2 F-box protein (Skp2 amplification → p27 degradation → CDK2 activation → cancer)

## Function

### The G1/S checkpoint and Rb tumor suppression

The retinoblastoma protein (Rb, 928 aa) is the **master tumor suppressor of the G1/S checkpoint**:

**Rb in quiescent cells (hypophosphorylated):**
- Binds E2F (via E2F transactivation domain) → masks the E2F activation domain → represses E2F target genes (actively represses via HDAC and NuRD complex recruitment)
- Maintains cells in G0/G1; loss of Rb → constitutive E2F → uncontrolled proliferation

**Mitogen-induced Rb inactivation:**
1. Mitogen → RTK → Ras-ERK + PI3K → cyclin D1 synthesis ↑ + CDK4/6 assembly
2. CDK4/6-cyclin D → Rb Ser780, Ser795, Ser807/811 phosphorylation → partial E2F release
3. CDK2-cyclin E → Rb Ser612, Thr350, Ser788 phosphorylation → complete E2F release → irreversible S-phase commitment
4. E2F1 → cyclin E and CDC25A → positive feedback → CDK2 activation → restriction point

**Rb family:** Rb (RB1), p107 (RBL1), p130 (RBL2) — "pocket proteins"; all are CDK substrates; p107/p130 also involved in G1 control but with different E2F binding specificities; CDK4/6 inhibitors also inactivate p107/p130-E2F4/5 complexes.

### CDK4/6 in specific cancer contexts

**ER+ HER2- breast cancer:**
- ER signaling → cyclin D1 transcription → CDK4/6 → Rb phosphorylation → proliferation
- CCND1 amplification in ~25%; CDK4/6 is the central kinase of estrogen-driven proliferation
- **CDK4/6 inhibitors + aromatase inhibitors (first-line):** Standard of care for ER+HER2- metastatic breast cancer

**Melanoma:**
- CDKN2A deletion in ~50%; CDK4 amplification in ~10%; near-universal CDK4/6 activation
- CDK4/6 inhibitors (palbociclib) show modest melanoma activity as single agents but are studied in combination with BRAF inhibitors and anti-PD-1

**Mantle cell lymphoma (MCL):**
- t(11;14) → cyclin D1 overexpression → CDK4/6 constitutive activation
- Abemaciclib shows activity in relapsed/refractory MCL

## Mechanism

### CDK4/6 inhibitors: mechanism and clinical data [^finn-2016-palbociclib]

Three approved CDK4/6 inhibitors (all ATP-competitive, CDK4/6-selective):

| Drug | Trade name | CDK4 IC₅₀ | CDK6 IC₅₀ | Selectivity | Route | Key toxicity |
|:---|:---|:---|:---|:---|:---|:---|
| Palbociclib | Ibrance | 11 nM | 15 nM | ~1000× over CDK1/2 | Oral QD × 21/28d | Neutropenia (dose-limiting) |
| Ribociclib | Kisqali | 10 nM | 39 nM | High CDK4/6 selectivity | Oral QD × 21/28d | Neutropenia, QTc prolongation |
| Abemaciclib | Verzenio | 2 nM | 10 nM | High; also inhibits CDK9 | Oral BID continuous | Diarrhea (CDK9 effect), neutropenia |

**Mechanism of inhibition:**
- All three occupy the ATP-binding cleft of CDK4/6, forming hydrogen bonds with the hinge region
- Palbociclib: pyridopyrimidine core; two H-bonds to Leu147 (hinge); hydrophobic pocket contacts
- Inhibit CDK4/6-cyclin D → Rb remains hypophosphorylated → E2F repressed → G1 arrest

**PALOMA-2 trial (palbociclib, 2016):** Palbociclib + letrozole vs letrozole alone in 1st-line ER+HER2- metastatic breast cancer: PFS 24.8 vs 14.5 months (HR 0.58); no OS benefit yet demonstrated (ongoing) [^finn-2016-palbociclib]

**MONALEESA-2 (ribociclib):** Ribociclib + letrozole vs letrozole: PFS 25.3 vs 16.0 months; OS benefit demonstrated (MONALEESA-7: OS 58.7 vs 48.0 months in premenopausal women — first CDK4/6i with OS benefit in pre/perimenopause)

**MONARCH-3 (abemaciclib):** Abemaciclib + AI: PFS 28.2 vs 14.8 months; also approved as adjuvant (monarchE trial: abemaciclib + ET for high-risk early-stage HR+ breast cancer — reduces invasive DFS events ~30%)

### Resistance to CDK4/6 inhibitors

**Primary resistance:**
- **Rb1 loss:** No CDK4/6i target; Rb-negative tumors are inherently resistant
- **Cyclin E amplification:** Cyclin E-CDK2 bypasses Rb phosphorylation (CDK2 is not inhibited by CDK4/6i); CCNE1 amplification is a major primary resistance mechanism
- **CDK4/6 amplification:** Overcome by high kinase concentration even in presence of inhibitor

**Acquired resistance:**
- **Rb1 loss** (also acquired: ~30% of CDK4/6i-resistant tumors)
- **CCNE1 amplification** (CDK2-driven Rb phosphorylation bypass)
- **CDK2 activation via loss of p21/p27:** SKP2 amplification → p27 degradation
- **PI3K/Akt pathway activation:** Promotes cyclin D1 synthesis
- **FAK (focal adhesion kinase) activation:** Promotes cell cycle via non-Rb mechanisms

**Post-progression strategies:**
- **Abemaciclib after palbociclib/ribociclib:** Partial cross-resistance; some activity due to CDK9 inhibition
- **Chemotherapy:** Capecitabine, eribulin, ixabepilone
- **Alpelisib (PI3K inhibitor):** For PIK3CA-mutant post-CDK4/6i (SOLAR-1 trial)
- **CDK2 inhibitors:** In clinical trials (PF-06873600, INCB123667) for CDK4/6i-resistant disease with cyclin E upregulation

## Connections

- `connects-to` → **[p53](../p53/README.md)** — p53→p21→CDK4/6 is the primary G1 checkpoint after DNA damage; p53 loss or CDK4/6 amplification both bypass this checkpoint; CDK4/6 inhibitors restore Rb tumor suppressor function, and thus depend on an intact Rb pathway.
- `connects-to` → **[MYC](../myc/README.md)** — MYC upregulates cyclin D and suppresses p21/p27 → activates CDK4/6; CDK4/6 is a major downstream effector of MYC-driven proliferation; MYC amplification and CDK4/6 activation cooperate in cancer.
- `connects-to` → **[mTOR](../mtor/README.md)** — mTORC1 drives cyclin D1/CDK4 expression; combined CDK4/6i + mTORi is active in palbociclib-resistant ER+ breast cancer; the two pathways have complementary roles in G1→S control and anabolic growth.
- `connects-to` → **[KRAS](../kras/README.md)** — KRAS-ERK promotes cyclin D1 and CDK4/6 → G1→S in RAS-mutant cancers; CDKN2A (p16) is co-deleted with KRAS pathway activation in PDAC and NSCLC, enabling maximally active CDK4/6.

[^sherr-2016-cdk4-rb]: Sherr CJ, Beach D, Shapiro GI. Targeting CDK4 and CDK6: From Discovery to Therapy. *Cancer Discov.* 2016;6(4):353-367. [doi:10.1158/2159-8290.CD-15-0894](https://doi.org/10.1158/2159-8290.CD-15-0894) · [PubMed 26658964](https://pubmed.ncbi.nlm.nih.gov/26658964/)
[^finn-2016-palbociclib]: Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. *N Engl J Med.* 2016;375(20):1925-1936. [doi:10.1056/NEJMoa1607303](https://doi.org/10.1056/NEJMoa1607303) · [PubMed 27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/)
[^roberts-1994-cdk4]: Serrano M, Hannon GJ, Beach D. A new regulatory motif in cell-cycle control causing specific inhibition of cyclin D/CDK4. *Nature.* 1993;366(6456):704-707. [doi:10.1038/366704a0](https://doi.org/10.1038/366704a0) · [PubMed 8259214](https://pubmed.ncbi.nlm.nih.gov/8259214/)
