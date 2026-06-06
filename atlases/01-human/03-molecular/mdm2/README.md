---
schema: human-scale-entry/v1
id: mdm2
name: MDM2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "E3 ubiquitin ligase and primary p53 negative regulator; MDM2 ubiquitinates p53 for proteasomal degradation. Amplified in ~7% of cancers, especially well-differentiated liposarcoma. MDM2 inhibitors (AMG-232, milademetan) restore p53 activity in TP53 wild-type tumors."
aliases: ["HDM2", "MDM2 proto-oncogene", "HDMX", "p53 E3 ligase", "mouse double minute 2"]
sources:
  - id: lane-1993-mdm2-p53
    type: peer-reviewed
    cite: "Lane DP, Hall PA. MDM2 — arbiter of p53's destruction. Trends Biochem Sci. 1997;22(10):372-374."
    doi: "10.1016/S0968-0004(97)01119-5"
    pmid: "9357318"
    url: "https://doi.org/10.1016/S0968-0004(97)01119-5"
  - id: vassilev-2004-nutlin
    type: peer-reviewed
    cite: "Vassilev LT, Vu BT, Graves B, et al. In vivo activation of the p53 pathway by small-molecule antagonists of MDM2. Science. 2004;303(5659):844-848."
    doi: "10.1126/science.1092472"
    pmid: "14704432"
    url: "https://doi.org/10.1126/science.1092472"
  - id: de-waal-2018-liposarcoma
    type: peer-reviewed
    cite: "Ray-Coquard I, Blay JY, Italiano A, et al. Effect of the MDM2 antagonist RG7112 on the P53 pathway in patients with MDM2-amplified, well-differentiated or dedifferentiated liposarcoma. J Clin Oncol. 2012;30(32):3980-3987."
    doi: "10.1200/JCO.2012.41.6925"
    pmid: "23032616"
    url: "https://doi.org/10.1200/JCO.2012.41.6925"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MDM2 is the primary p53 negative regulator; p53 induces MDM2 → MDM2 ubiquitinates p53 → degradation, forming an autoregulatory loop; MDM2 amplification mimics TP53 mutation; MDM2 inhibitors (nutlin-3, AMG-232) restore p53 in TP53-wild-type tumors."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT phosphorylates MDM2 Ser166 → nuclear translocation → accelerated p53 degradation; PI3K-AKT hyperactivation via PIK3CA mutation or PTEN loss is a major non-mutational p53 inactivation mechanism; AKT inhibitors partially restore p53 by reducing MDM2 nuclear localization."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC triggers oncogene-induced senescence via ARF (p14ARF) upregulation → ARF sequesters MDM2 in the nucleolus → p53 stabilization; cancer cells with MYC amplification co-select MDM2 amplification or TP53 mutation to bypass ARF-p53 apoptosis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "MDM2 inhibitors restore p53 → PUMA/NOXA upregulation → BCL-2/BCL-XL antagonism; combining MDM2 inhibitors with venetoclax (BCL-2 inhibitor) shows synergistic killing in AML and CLL with TP53-wild-type and BCL-2 dependence."
---

# MDM2

## Overview

**MDM2 (murine double minute 2, HDM2 in humans)** is a **RING-finger E3 ubiquitin ligase** and the principal endogenous negative regulator of the **p53 tumor suppressor**. MDM2 maintains p53 at low levels in unstressed cells by: (1) binding to the p53 transactivation domain → blocking p53 transcriptional activity, (2) ubiquitinating p53 Lys residues → proteasomal degradation, and (3) facilitating p53 nuclear export. MDM2 and p53 form an **autoregulatory feedback loop** — p53 transcriptionally activates MDM2, and MDM2 in turn inactivates p53 — the central mechanism of p53 self-limitation after stress responses [^lane-1993-mdm2-p53].

MDM2 is a proto-oncogene: its amplification or overexpression effectively phenocopies TP53 mutation by neutralizing p53 tumor suppressor function. In clinical oncology:
- **MDM2 amplification** occurs in ~7% of all cancers; highest in **well-differentiated/dedifferentiated liposarcoma** (WDLPS/DDLPS, ~90%; chromosome 12q15 amplification of MDM2+CDK4 locus) — the most common soft tissue sarcoma subtype
- **MDM2 overexpression** (without amplification) occurs via promoter variants (SNP309 — Tsp I/Sp1 binding site), protein stabilization, or translational upregulation; seen in many cancers with TP53 wild-type
- **MDM4 (MDMX):** Homolog; lacks intrinsic ubiquitin ligase activity; dimerizes with MDM2 via RING domains → enhances MDM2 activity; binds p53 transactivation domain independently; amplified or overexpressed in some TP53-WT tumors; MDM2+MDMX co-inhibition (RO6839921) under investigation

**Therapeutic principle (nutlin era):** Because ~50% of cancers retain wild-type TP53, MDM2 inhibition to restore p53 activity represents a precision oncology approach to induce p53-dependent apoptosis selectively in tumor cells (higher MDM2 levels) vs. normal cells. Discovered in 2004 by Vassilev et al. [^vassilev-2004-nutlin].

## Structure

### MDM2 protein domains

MDM2 is a **491 amino acid** multidomain protein:

**N-terminal p53-binding domain (aa 19-101):**
- Hydrophobic cleft that accommodates the N-terminal transactivation helix of p53 (Phe19, Trp23, Leu26 of p53 insert into MDM2 cleft)
- **Drug target:** Nutlin-3, AMG-232, milademetan (DS-3032b), BI-907828 all occupy this same p53-binding cleft → competitive displacement of p53 → p53 accumulates → apoptosis
- MDMX has a similar but subtly distinct N-terminal cleft → some MDM2-specific inhibitors (nutlin-3) have reduced MDMX binding → MDMX escapes inhibition

**Central acid domain (aa 237-288):**
- Binds ribosomal proteins (L5, L11, L23) and rRNA → ribosomal stress sensor; when ribosome biogenesis is disrupted → L11 binds MDM2 acid domain → sequesters MDM2 → p53 stabilization; mechanism of p53 activation by 5-fluorouracil, actinomycin D at low doses

**Zinc finger (aa 289-331):**
- Binds RNA and DNA; function in nuclear-cytoplasmic trafficking; mutations in this domain impair MDM2-ribosomal protein interaction; also mediates interaction with ARF (see below)

**RING domain (aa 437-491):**
- E3 ubiquitin ligase activity; forms homodimer or heterodimer with MDMX RING domain (required for full MDM2 E3 ligase activity in vivo); ubiquitinates p53 and MDM2 itself (autoubiquitination → MDM2 self-degradation)
- Non-p53 substrates: MDM2 ubiquitinates PCNA, MDMX, RB, IGF1R, FOXO3a — context-dependent activities

### Regulation of MDM2

**p53 → MDM2 transcription:**
- MDM2 promoter contains two p53 response elements (P1 and P2); p53 binds P2 → MDM2 mRNA transcription → negative feedback loop closure

**ARF (Alternative Reading Frame, p14ARF/p19Arf) pathway:**
- ARF is a tumor suppressor encoded by the **CDKN2A/INK4a locus** (shares locus with p16/CDKN2A via alternate reading frame)
- ARF binds MDM2 zinc finger → sequesters MDM2 in the nucleolus → prevents MDM2-mediated p53 ubiquitination → p53 stabilization
- **Oncogene-induced ARF activation:** MYC, RAS, E2F1 → ARF → p53 stabilization → oncogene-induced senescence (OIS); cancer must inactivate this ARF-MDM2-p53 axis to escape OIS → either ARF deletion or MDM2 amplification or TP53 mutation

**Post-translational regulation of MDM2:**
- **AKT phosphorylation (Ser166/186):** Promotes MDM2 nuclear localization and stability → enhanced p53 degradation (PI3K-AKT hyperactivation → p53 inactivation)
- **ATM/CHK2 (DNA damage response):** Phosphorylates p53 N-terminus → prevents MDM2 binding → p53 stabilization (DNA damage stabilizes p53 upstream of MDM2 inhibition)
- **MDM2 Ser395 (ATM):** ATM phosphorylates MDM2 at Ser395 → reduced MDM2 activity → p53 accumulation after DNA DSBs
- **HAUSP (ubiquitin-specific protease 7):** De-ubiquitinates MDM2 → MDM2 stabilization (counterintuitively, HAUSP depletion → MDM2 auto-degradation → paradoxical p53 activation)

## Function

### MDM2 mechanisms of p53 inhibition [^lane-1993-mdm2-p53]

**1. Transcriptional repression:**
MDM2 binds p53 N-terminal transactivation domain (TAD, aa 14-35) → blocks interaction of p53 with TAFII250, CBP/p300, and Med25 → prevents co-activator recruitment → p53 cannot activate target genes (p21, PUMA, NOXA, BAX, MDM2 itself)

**2. Nuclear export and cytoplasmic sequestration:**
MDM2 has a nuclear export signal (NES) and a nuclear localization signal (NLS); MDM2-p53 complex → NES-dependent export → cytoplasmic p53 → inaccessible to nuclear transcription machinery

**3. Proteasomal degradation:**
MDM2 RING domain → E2 ubiquitin conjugating enzyme (UbcH5) → poly-ubiquitylation of p53 at Lys370, 372, 373, 381, 382, 386 → 26S proteasome degradation; MDM2-MDMX RING heterodimer is required for full MDM2 E3 activity in vivo

**4. Non-p53 substrate ubiquitination:**
MDM2 ubiquitinates and regulates: RB (pro-cell-cycle; reduces RB tumor suppressor activity), IGF1R (reduces growth factor receptor), FOXO3a (cytoplasmic localization), and PCNA (regulates DNA repair)

### MDM2 amplification in cancer

**Well-differentiated/dedifferentiated liposarcoma (WDLPS/DDLPS):**
- ~90% have chromosome 12q15 amplification → supernumerary ring chromosomes or giant marker chromosomes containing MDM2 + CDK4 amplicons
- TP53 is almost always wild-type in WDLPS/DDLPS → MDM2 amplification is the functional TP53 inactivation mechanism
- MDM2/CDK4 FISH or MDM2/CDK4 IHC is used diagnostically to distinguish WDLPS/DDLPS from other lipomatous tumors
- MDM2 inhibitors (RG7112, AMG-232, milademetan) show clinical activity in WDLPS — response rates ~10-20% in Phase I/II; combined MDM2+CDK4 inhibition under active investigation

**Other MDM2-amplified cancers:**
- **Osteosarcoma:** 16% MDM2 amplification
- **Uterine carcinosarcoma, intimal sarcoma:** High rate MDM2 amplification
- **Glioblastoma:** ~14% MDM2 amplification; usually mutually exclusive with TP53 mutation

**MDM2 SNP309 (T>G, rs2279744):**
- G allele → increased Sp1 transcription factor binding → elevated MDM2 mRNA and protein → moderately attenuated p53 response; contributes to soft tissue sarcoma and other cancer risk, particularly in women (estrogen receptor α also activates MDM2 promoter)

## Mechanism

### MDM2 inhibitors (nutlins and beyond) [^vassilev-2004-nutlin]

**Nutlin-3 (proof-of-concept, Roche):** First small-molecule MDM2 inhibitor; cis-imidazoline scaffold; occupies hydrophobic p53-binding cleft of MDM2 via mimicry of p53 Trp23/Phe19/Leu26 residues; restores p53 nuclear accumulation → p21, PUMA, NOXA, BAX upregulation → G1 arrest and apoptosis in MDM2-overexpressing, TP53-wild-type cancer cell lines

**Clinical MDM2 inhibitors:**
- **AMG-232 (karremide):** Piperidinone scaffold; most potent MDM2 inhibitor in clinical trials; Phase I/II in AML, myeloma, WDLPS; DLT: thrombocytopenia (p53 activation in platelet precursors → thrombopoiesis impaired); dose-limiting toxicity
- **Milademetan (DS-3032b, Daiichi-Sankyo):** Spirooxindole scaffold; Phase II in WDLPS: ORR 22%, DCR 70%; pivotal Phase III MANTRA trial in WDLPS/DDLPS ongoing
- **BI-907828 (Boehringer Ingelheim):** Once-weekly dosing (half-life advantage); Phase I/II in solid tumors; ongoing
- **RG7112 (Roche):** First nutlin-class in clinical trials; Phase I in AML/sarcoma; showed p53 pathway activation (p21 induction) and MDM2 protein increase in tumor (p53 induces MDM2 — paradoxically elevated MDM2 protein confirms p53 activation, not resistance) [^de-waal-2018-liposarcoma]

**Key challenges and resistance mechanisms:**
- **TP53 mutation selection:** Acquired TP53 mutations are the dominant resistance mechanism (50-70% of relapsed cases in MDM2i trials); tumors with low-frequency TP53 mutant subclones at baseline rapidly enrich → loss of response; ctDNA TP53 monitoring during therapy required
- **MDM2 feedback amplification:** p53 → MDM2 → p53 degradation — when p53 is activated by MDM2i, MDM2 transcription rises further → "catch up" → partial p53 inactivation; some MDM2i show sustained response only at higher doses that overcome feedback
- **MDMX escape:** Tumors with MDMX overexpression can partially bypass MDM2 inhibition (MDMX independently binds and represses p53 TAD); MDM2+MDMX dual inhibitors (RO6839921 — MDM2/MDMX PROTAC) in development
- **Cell cycle arrest vs. apoptosis:** p53 activation by MDM2i preferentially induces senescence/arrest in some cancer types rather than apoptosis → combination with CDK4/6 inhibitors or pro-apoptotic BCL-2 family inhibitors (venetoclax) to enhance apoptotic response

## Connections

- `connects-to` → **[p53](../p53/README.md)** — MDM2 is the primary p53 negative regulator forming an autoregulatory loop; MDM2 ubiquitinates p53 for proteasomal degradation; MDM2 amplification functionally mimics TP53 mutation; MDM2 inhibitors (nutlin-3, AMG-232) restore p53 activity in TP53-wild-type tumors — the basis for MDM2-targeted oncology.
- `connects-to` → **[AKT](../akt/README.md)** — AKT phosphorylates MDM2 at Ser166/186 → nuclear translocation → enhanced p53 degradation; PI3K-AKT hyperactivation from PIK3CA mutation or PTEN loss is a non-mutational p53 inactivation mechanism; AKT inhibitors partially restore p53 by reducing MDM2 nuclear translocation.
- `connects-to` → **[MYC](../myc/README.md)** — MYC overexpression induces ARF (p14ARF from CDKN2A locus) → ARF sequesters MDM2 in nucleolus → p53 stabilization → oncogene-induced senescence; MYC-amplified cancers co-select MDM2 amplification or TP53 mutation to bypass ARF-mediated senescence and escape apoptosis.
- `connects-to` → **[BCL-2](../bcl-2/README.md)** — MDM2 inhibitors restore p53 → transcriptional activation of PUMA and NOXA (BH3-only proteins) → BCL-2/BCL-XL antagonism → apoptosis; combining MDM2 inhibitors with venetoclax (BCL-2 inhibitor) shows synergistic killing in AML and CLL with TP53-wild-type and BCL-2 dependence.

[^lane-1993-mdm2-p53]: Lane DP, Hall PA. MDM2 — arbiter of p53's destruction. *Trends Biochem Sci.* 1997;22(10):372-374. [doi:10.1016/S0968-0004(97)01119-5](https://doi.org/10.1016/S0968-0004(97)01119-5) · [PubMed 9357318](https://pubmed.ncbi.nlm.nih.gov/9357318/)
[^vassilev-2004-nutlin]: Vassilev LT, Vu BT, Graves B, et al. In vivo activation of the p53 pathway by small-molecule antagonists of MDM2. *Science.* 2004;303(5659):844-848. [doi:10.1126/science.1092472](https://doi.org/10.1126/science.1092472) · [PubMed 14704432](https://pubmed.ncbi.nlm.nih.gov/14704432/)
[^de-waal-2018-liposarcoma]: Ray-Coquard I, Blay JY, Italiano A, et al. Effect of the MDM2 antagonist RG7112 on the P53 pathway in patients with MDM2-amplified, well-differentiated or dedifferentiated liposarcoma. *J Clin Oncol.* 2012;30(32):3980-3987. [doi:10.1200/JCO.2012.41.6925](https://doi.org/10.1200/JCO.2012.41.6925) · [PubMed 23032616](https://pubmed.ncbi.nlm.nih.gov/23032616/)
