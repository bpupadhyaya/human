---
schema: human-scale-entry/v1
id: akt
name: AKT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "PI3K-AKT-mTOR pathway kinase; PIP3-activated by PDK1 and mTORC2 downstream of PIK3CA. Phosphorylates BAD/FOXO/MDM2 to promote survival and activates mTORC1 for growth. Capivasertib (pan-AKT inhibitor) approved 2023 for PIK3CA/AKT/PTEN-altered HR+/HER2- breast cancer."
aliases: ["protein kinase B", "PKB", "AKT1", "AKT2", "AKT3", "AKT serine/threonine kinase"]
sources:
  - id: bellacosa-1991-akt-oncogene
    type: peer-reviewed
    cite: "Bellacosa A, Testa JR, Staal SP, Tsichlis PN. A retroviral oncogene, akt, encoding a serine-threonine kinase containing an SH2-like region. Science. 1991;254(5029):274-277."
    doi: "10.1126/science.254.5029.274"
    pmid: "1833819"
    url: "https://doi.org/10.1126/science.254.5029.274"
  - id: manning-2007-akt-review
    type: peer-reviewed
    cite: "Manning BD, Cantley LC. AKT/PKB Signaling: Navigating Downstream. Cell. 2007;129(7):1261-1274."
    doi: "10.1016/j.cell.2007.06.009"
    pmid: "17604717"
    url: "https://doi.org/10.1016/j.cell.2007.06.009"
  - id: turner-2023-capivasertib
    type: peer-reviewed
    cite: "Turner NC, Oliveira M, Howell SJ, et al. Capivasertib in Hormone Receptor-Positive Advanced Breast Cancer. N Engl J Med. 2023;388(22):2058-2070."
    doi: "10.1056/NEJMoa2214131"
    pmid: "37256976"
    url: "https://doi.org/10.1056/NEJMoa2214131"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "AKT→TSC1/2 phosphorylation → Rheb-GTP → mTORC1 activation → S6K1 and 4EBP1 → protein synthesis and cell growth; mTORC2 (rapamycin-insensitive) phosphorylates AKT Ser473 → full AKT activation; mTOR and AKT form a feedback loop where S6K suppresses IRS-1 → AKT."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA (PI3K-alpha) generates PIP3 from PIP2 → PIP3 recruits AKT via PH domain → PDK1 phosphorylates AKT Thr308; PIK3CA gain-of-function mutations constitute the most common upstream AKT activator in cancer; PTEN loss has the same effect by preventing PIP3 dephosphorylation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "AKT phosphorylates BAD Ser136 → BAD dissociates from BCL-2/BCL-XL → BCL-2 free to sequester BIM/BAX → apoptosis suppressed; AKT also phosphorylates MDM2 → p53 degradation; dual pathway promotes cancer cell survival and resistance to genotoxic therapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "AKT phosphorylates MDM2 at Ser166 → MDM2 nuclear translocation → p53 ubiquitination and degradation; p53 activates PTEN transcription creating a negative feedback loop; AKT-MDM2-p53 axis is disrupted in most cancers with PIK3CA mutation, PTEN loss, or AKT amplification."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "PIK3CA mutations (H1047R, E545K) in 35-40% of HR+ breast cancer activate AKT; AKT1 E17K in ~5%; PTEN loss predicts trastuzumab resistance; capivasertib (pan-AKT) FDA approved 2023 for PIK3CA/AKT/PTEN-altered HR+/HER2- breast cancer (CAPItello-291 PFS 7.3 vs 3.1 months)."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN converts PIP3→PIP2 → terminates AKT activation; PTEN loss (40% endometrial, 30% GBM, 20% prostate) → constitutive AKT activation; PTEN is the second most commonly altered tumor suppressor after TP53; germline PTEN mutations → Cowden syndrome with multi-organ cancer risk."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "AKT2 mediates insulin-stimulated GLUT4 vesicle translocation in adipocytes and muscle via AS160/TBC1D4 phosphorylation; AKT2 loss-of-function mutations → autosomal dominant severe insulin resistance and T2DM; PPARγ agonists (TZDs) activate PI3K-AKT during adipogenesis."
---

# AKT

## Overview

**AKT (AKT serine/threonine kinase, protein kinase B, PKB)** is the central downstream effector of the **PI3K-AKT-mTOR signaling axis** — one of the most frequently activated oncogenic pathways in human cancer. A member of the AGC kinase family, AKT integrates extracellular growth signals (insulin, EGF, IGF-1, VEGF) received by receptor tyrosine kinases and relayed through PI3K/PIP3 into an extensive intracellular kinase program controlling **cell survival, growth, metabolism, motility, and cell cycle progression** [^manning-2007-akt-review].

AKT was identified as the transforming oncogene of the murine AKT8 retrovirus in 1991 [^bellacosa-1991-akt-oncogene]; the corresponding human kinase was characterized as a serine/threonine kinase with PH domain-mediated membrane localization. AKT has **three highly homologous isoforms** (AKT1, AKT2, AKT3) encoded by distinct genes — ~80% identity in kinase domain but distinct tissue expression and substrate preferences:
- **AKT1:** Ubiquitous; promotes cell survival and inhibits apoptosis; AKT1 activation → cell growth without transformation in epithelial cells; AKT1 E17K gain-of-function mutation in ~4-8% of breast, bladder, CRC, and other cancers
- **AKT2:** Insulin signaling in metabolic tissues (liver, muscle, adipose); required for glucose uptake (GLUT4 translocation); AKT2 amplification in ovarian (30%) and pancreatic cancer; metabolic syndrome with AKT2 loss-of-function
- **AKT3:** Brain-enriched expression; AKT3 amplification in melanoma (50%) and triple-negative breast cancer; focal cortical dysplasia (somatic AKT3 mutations → PI3K pathway gain-of-function → neuronal overgrowth)

**AKT activation in cancer:**
- **Upstream:** PIK3CA gain-of-function mutation (35-40% breast, 15-20% CRC), PTEN loss (40% endometrial, 30% glioblastoma, 20% prostate), RTK amplification (HER2, EGFR, IGF-1R), RAS/KRAS mutation
- **AKT itself:** AKT1 E17K (pleckstrin homology domain mutation → constitutive membrane localization → ligand-independent activation; 5% breast/bladder/CRC); AKT amplification (10-20% pancreatic, gastric)
- **Downstream:** mTORC1 pathway mutations (TSC1/TSC2 loss, RHEB amplification); NF1 loss (negative RAS regulator → RAS→PI3K)

## Structure

### AKT protein domains [^manning-2007-akt-review]

AKT is a **480 amino acid** serine/threonine kinase with three structural modules:

**N-terminal PH domain (aa 1-107):**
- Binds **PIP3** (phosphatidylinositol-3,4,5-trisphosphate) and PIP2 with high specificity via basic residue patch (Arg23, Arg25, Lys30)
- PH domain membrane anchoring is the primary mechanism of AKT activation — PIP3 generation by PI3K recruits AKT from cytosol to plasma membrane
- **AKT1 E17K mutation:** Enhances PH domain binding to PIP2 (not just PIP3) → constitutive plasma membrane localization → AKT activation without upstream PI3K activation

**Kinase domain (aa 150-408):**
- Typical bilobed AGC kinase fold; N-lobe (5 beta strands) + C-lobe (8 alpha helices)
- **Activation loop (A-loop) Thr308:** Phosphorylated by PDK1 (phosphoinositide-dependent kinase 1, itself recruited to membrane by PIP3 via its own PH domain) → AKT partial activation (~20-30% max activity)
- **αC helix:** Contains regulatory inputs from N-lobe — Glu-Lys salt bridge required for ATP catalysis in active conformation
- **ATP binding pocket:** Targeted by catalytic AKT inhibitors (GSK690693, capivasertib); also targeted allosterically (MK-2206, allosteric — binds PH-kinase domain interface)

**C-terminal regulatory domain/hydrophobic motif (aa 408-480):**
- **Ser473 in hydrophobic motif:** Phosphorylated by **mTORC2** (rapamycin-insensitive mTOR complex) → maximizes AKT activation (~100-fold increase above Thr308 alone)
- S473 phosphorylation is the primary **pharmacodynamic biomarker** for PI3K/AKT pathway inhibition in tumor tissue and phosphoflow in clinical trials

### AKT activation mechanism

**Canonical activation sequence:**
1. Ligand (EGF, insulin, IGF-1) → RTK autophosphorylation → p85 SH2 binding → PI3K membrane recruitment → PIP2 → **PIP3**
2. **PTEN** (phosphatase) converts PIP3 → PIP2 (negative regulation); PTEN loss → constitutive PIP3 elevation
3. PIP3 → recruits AKT (PH domain) and PDK1 (PH domain) to plasma membrane
4. **PDK1 → phosphorylates AKT Thr308** → partial activation
5. **mTORC2 → phosphorylates AKT Ser473** → full activation (mTORC2 constitutively active at plasma membrane in most cell types; regulated by nutrient status and mechanical signals)
6. Fully active AKT → dissociates from membrane → phosphorylates cytoplasmic and nuclear substrates

## Function

### AKT substrates and downstream effects [^manning-2007-akt-review]

AKT has **>100 validated substrates** with the canonical phosphorylation motif: R-x-R-x-x-S/T (RXRXXS/T):

**Cell survival:**
- **BAD (BCL-2 antagonist of cell death):** AKT phosphorylates BAD Ser136 → BAD sequestered by 14-3-3 proteins → BCL-2 and BCL-XL freed to sequester BIM/BAX/BAK → apoptosis suppressed; critical survival signal in growth-factor-stimulated cells
- **FOXO1/3/4 (forkhead box O transcription factors):** AKT phosphorylates FOXO at 3 sites → cytoplasmic sequestration (by 14-3-3) → nuclear exclusion → prevents FOXO transcription of pro-apoptotic genes (BIM, FasL, PUMA, Sestrin3) and cell cycle arrest genes (p27Kip1, p21); FOXO nuclear localization is tumor-suppressive → AKT inhibition restores FOXO nuclear activity → apoptosis

**Cell growth and protein synthesis:**
- **TSC2 (tuberin):** AKT phosphorylates TSC2 → GAP toward Rheb (GTPase-activating protein) inactivation → Rheb-GTP accumulates → **mTORC1** activation → S6K1 and 4EBP1 phosphorylation → ribosome biogenesis and cap-dependent translation
- **GSK-3beta (glycogen synthase kinase 3 beta):** AKT phosphorylates GSK-3beta Ser9 → GSK-3beta inactivation → glycogen synthase dephosphorylated → glycogen synthesis; GSK-3beta normally phosphorylates and destabilizes cyclin D1 and c-MYC → AKT inhibits GSK-3beta → stabilizes both → G1 progression and transcriptional amplification

**Cell cycle:**
- **p21Cip1/p27Kip1:** AKT phosphorylates these CDK inhibitors → cytoplasmic sequestration → loss of CDK2 inhibition → S-phase entry; contributes to AKT's mitogenic effects
- **MDM2 (p53 ubiquitin ligase):** AKT phosphorylates MDM2 Ser166/186 → MDM2 nuclear translocation → p53 Lys48-polyubiquitination → proteasomal p53 degradation → p53 tumor suppressor lost; cancer with both PIK3CA mutation and wild-type p53 benefits from AKT inhibition reactivating p53

**Metabolism:**
- **PFKFB2 (PFK-2/FBPase-2):** AKT phosphorylation → increased PFK-2 activity → elevated fructose-2,6-bisphosphate → enhanced glycolysis (Warburg effect); AKT is a central driver of aerobic glycolysis in cancer
- **Hexokinase-II:** AKT promotes HK-II expression and mitochondrial binding → glucose phosphorylation → enhanced glucose consumption and apoptosis resistance (HK-II binding to VDAC blocks cytochrome c release)
- **GLUT4 trafficking (AKT2):** Insulin → AKT2 → AS160/TBC1D4 phosphorylation → GLUT4 vesicle fusion with plasma membrane → glucose uptake in muscle/adipose; AKT2 loss-of-function → type 2 diabetes phenotype

**Angiogenesis:**
- **eNOS:** AKT phosphorylates eNOS Ser1177 → increased NO production → vasodilation and angiogenesis; AKT in endothelial cells downstream of VEGFR2 → PI3K → AKT → eNOS → tumor angiogenesis

### AKT and cancer drug resistance

AKT hyperactivation is a pan-cancer resistance mechanism:
- **Anti-HER2 resistance:** PIK3CA mutation or PTEN loss → persistent AKT → trastuzumab resistance in HER2+ breast cancer (PTEN loss in ~20% of HER2+ tumors predicts inferior response)
- **Anti-EGFR resistance:** In EGFR-mutant NSCLC, PTEN loss → PI3K-AKT bypass of EGFR inhibition
- **Anti-estrogen resistance:** AKT phosphorylates ER Ser167 → ligand-independent ER transcription → tamoxifen/aromatase inhibitor resistance
- **Chemotherapy resistance:** AKT → BCL-2 pathway → anoikis resistance, reduced apoptotic response to cisplatin, doxorubicin, taxanes

## Mechanism

### AKT inhibitors: allosteric vs. catalytic [^turner-2023-capivasertib]

**Allosteric AKT inhibitors (PH domain-kinase domain interface):**
- **MK-2206 (Merck):** Binds PH domain-kinase domain junction in inactive DFG-out conformation → prevents Thr308 phosphorylation by PDK1 AND Ser473 phosphorylation by mTORC2; disadvantage: E17K AKT1 mutation confers some resistance (altered PH domain conformation); Phase 2 trials (limited single-agent activity)

**Catalytic (ATP-competitive) AKT inhibitors:**
- **Capivasertib (AZD5363, AstraZeneca):** Pan-AKT1/2/3 catalytic inhibitor; achieves >95% AKT inhibition at trough; **CAPItello-291 Phase 3 trial** (capivasertib + fulvestrant vs. fulvestrant in PIK3CA/AKT/PTEN-altered HR+/HER2- advanced breast cancer post-AI): PFS 7.3 vs 3.1 months (altered cohort); 10.3 vs 4.4 months (altered biomarker subgroup) → FDA approved November 2023 [^turner-2023-capivasertib]
- **Ipatasertib (Genentech/Roche):** Pan-AKT catalytic inhibitor; IPATunity130 (TNBC with PTEN loss): negative primary endpoint; IPATunity150 (HR+/HER2-): positive in PIK3CA/AKT/PTEN-altered subgroup; Phase 3 ongoing

**Combination strategies:**
- AKT inhibitor + CDK4/6 inhibitor: RB pathway co-activation in ER+ breast cancer; rational combination (FAKTION-UC trial: capivasertib + palbociclib)
- AKT + anti-HER2: Overcome PTEN loss-mediated trastuzumab resistance
- AKT + PARP inhibitor: BRCA1/2-mutant tumors with PI3K pathway co-activation

**Toxicity:**
- Hyperglycemia (on-target: AKT2 loss → insulin resistance in muscle; AKT1 → pancreatic beta-cell insulin secretion impaired); manage with low-carbohydrate diet, metformin; grade 3 hyperglycemia in ~8-15%
- Diarrhea, rash (class effects of PI3K pathway inhibition); generally less than alpelisib (which also inhibits beta-cell AKT)

## Connections

- `connects-to` → **[mTOR](../mtor/README.md)** — AKT phosphorylates TSC2 → Rheb-GTP → mTORC1 → S6K/4EBP1 → protein synthesis and cell growth; mTORC2 feeds back by phosphorylating AKT Ser473 for full activation; the AKT-mTOR feedback loop is the central growth signaling cascade dysregulated in most solid tumors.
- `connects-to` → **[PIK3CA](../pik3ca/README.md)** — PIK3CA generates PIP3 → activates AKT via PH domain membrane recruitment and PDK1-mediated Thr308 phosphorylation; PIK3CA gain-of-function mutations (H1047R, E545K) are the primary upstream AKT activators in breast, CRC, and ovarian cancer.
- `connects-to` → **[BCL-2](../bcl-2/README.md)** — AKT phosphorylates BAD → releases BCL-2/BCL-XL from BAD complex → anti-apoptotic survival signal; AKT hyperactivation in cancer creates BCL-2 dependence, providing rationale for combining AKT inhibitors with venetoclax (BCL-2 inhibitor) in hematologic malignancies.
- `connects-to` → **[p53](../p53/README.md)** — AKT phosphorylates MDM2 → nuclear translocation → p53 ubiquitination and degradation; p53 activates PTEN transcription → reduces PIP3 → negative AKT feedback; AKT-MDM2-p53 axis is disrupted in most PIK3CA-mutant or PTEN-null cancers, and AKT inhibition can reactivate p53 in WT-p53 tumors.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — PIK3CA mutations in 35-40% of HR+ breast cancer activate AKT; AKT1 E17K in ~5%; PTEN loss predicts trastuzumab resistance; capivasertib (pan-AKT) FDA approved 2023 for PIK3CA/AKT/PTEN-altered HR+/HER2- breast cancer (CAPItello-291 PFS 7.3 vs 3.1 months).
- `connects-to` → **[PTEN](../pten/README.md)** — PTEN phosphatase converts PIP3→PIP2 → terminates AKT activation; PTEN loss (40% endometrial, 30% GBM, 20% prostate) → constitutive AKT; PTEN is the second most commonly altered tumor suppressor after TP53; germline PTEN mutations cause Cowden syndrome.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — AKT2 mediates insulin-stimulated GLUT4 translocation in adipocytes and muscle via AS160/TBC1D4 phosphorylation; AKT2 loss-of-function → autosomal dominant severe insulin resistance and T2DM; PPARγ agonists (TZDs) activate PI3K-AKT during adipogenesis.

[^bellacosa-1991-akt-oncogene]: Bellacosa A, Testa JR, Staal SP, Tsichlis PN. A retroviral oncogene, akt, encoding a serine-threonine kinase containing an SH2-like region. *Science.* 1991;254(5029):274-277. [doi:10.1126/science.254.5029.274](https://doi.org/10.1126/science.254.5029.274) · [PubMed 1833819](https://pubmed.ncbi.nlm.nih.gov/1833819/)
[^manning-2007-akt-review]: Manning BD, Cantley LC. AKT/PKB Signaling: Navigating Downstream. *Cell.* 2007;129(7):1261-1274. [doi:10.1016/j.cell.2007.06.009](https://doi.org/10.1016/j.cell.2007.06.009) · [PubMed 17604717](https://pubmed.ncbi.nlm.nih.gov/17604717/)
[^turner-2023-capivasertib]: Turner NC, Oliveira M, Howell SJ, et al. Capivasertib in Hormone Receptor-Positive Advanced Breast Cancer. *N Engl J Med.* 2023;388(22):2058-2070. [doi:10.1056/NEJMoa2214131](https://doi.org/10.1056/NEJMoa2214131) · [PubMed 37256976](https://pubmed.ncbi.nlm.nih.gov/37256976/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
