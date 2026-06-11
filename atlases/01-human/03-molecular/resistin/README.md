---
schema: human-scale-entry/v1
id: resistin
name: Resistin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Resistin is a monocyte-secreted cytokine (RETN) that activates NF-κB → insulin resistance, endothelial dysfunction, and hepatic VLDL secretion; elevated in NASH, T2D, and rheumatoid arthritis; inhibits adiponectin signaling and promotes pro-inflammatory macrophage activation."
aliases: ["resistin", "RETN", "ADSF", "FIZZ3", "resistin-like molecule", "adipokine", "adipocytokine", "hyperresistinemia", "CAP1"]
cross_links:
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Resistin impairs insulin signaling via IKK activation → IRS-1 Ser307 phosphorylation → insulin resistance; resistin inhibits AMPK in liver → increased gluconeogenesis; serum resistin is inversely correlated with adiponectin and positively correlated with insulin resistance."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Elevated resistin promotes endothelial VCAM-1 and endothelin-1 → monocyte adhesion and foam cell formation; resistin activates hepatic VLDL production → atherogenic dyslipidemia; serum resistin predicts incident coronary heart disease and heart failure in prospective cohorts."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Resistin is markedly elevated in synovial fluid and blood in RA; drives synovial macrophage NF-κB → TNF-α and IL-6 → joint inflammation and destruction; correlates with RA disease activity (DAS28) and joint damage scores."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Resistin and adiponectin are opposing adipokines: adiponectin activates AMPK → insulin sensitivity; resistin suppresses adiponectin expression and impairs AMPK → insulin resistance; resistin:adiponectin ratio is a composite marker of metabolic and inflammatory disease severity."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Resistin → CAP1/NF-κB → TNF-α from macrophages; TNF-α induces resistin → feedforward inflammation; both signal via IRS-1 Ser307 phosphorylation → insulin resistance; anti-TNF (infliximab) reduces serum resistin in RA — confirming TNF drives resistin production in inflammation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Resistin activates Kupffer cell NF-κB → IL-6; IL-6 → STAT3 → hepatic stellate cells → TGF-β → fibrosis in NASH; resistin-IL-6 axis correlates with NASH fibrosis stage; IL-6 induces resistin from monocytes → feedforward loop; IL-6 + resistin co-elevation predicts CVD events."
sources:
  - id: steppan-2001-resistin-discovery
    type: peer-reviewed
    cite: "Steppan CM, Bailey ST, Bhat S, et al. The hormone resistin links obesity to diabetes. Nature. 2001;409(6818):307-312."
    doi: "10.1038/35053000"
    pmid: "11201732"
    url: "https://doi.org/10.1038/35053000"
  - id: lehrke-2004-resistin-human
    type: peer-reviewed
    cite: "Lehrke M, Reilly MP, Millington SC, Iqbal N, Rader DJ, Lazar MA. An inflammatory cascade leading to hyperresistinemia in humans. PLoS Med. 2004;1(2):e45."
    doi: "10.1371/journal.pmed.0010045"
    pmid: "15526055"
    url: "https://doi.org/10.1371/journal.pmed.0010045"
---

# Resistin

## Overview

**Resistin** (gene *RETN*, chromosome 19p13.3; also known as ADSF — Adipose tissue-Specific Secretory Factor, or FIZZ3) is a **cysteine-rich, disulfide bond-stabilized cytokine** with fundamentally different biology in rodents versus humans. In mice, resistin is expressed exclusively by adipocytes and links obesity to insulin resistance. In **humans**, resistin is produced predominantly by **peripheral blood monocytes and macrophages** (not adipocytes) and functions primarily as a **pro-inflammatory mediator** — making it an adipokine by discovery but a monocytokine by primary mechanism [^lehrke-2004-resistin-human].

Resistin was originally named for its role in "**resisting**" insulin signaling: administration of recombinant mouse resistin to lean mice caused insulin resistance, while resistin-deficient mice were protected from high-fat diet-induced glucose intolerance [^steppan-2001-resistin-discovery]. In humans, serum resistin correlates with inflammatory markers (CRP, IL-6) and metabolic disease severity (NASH, T2D, metabolic syndrome), and is elevated in autoimmune disease (RA, SLE, IBD), supporting its role as an inflammatory rather than purely metabolic hormone.

**Species comparison: rodent vs. human resistin:**

| Feature | Mouse/Rat | Human |
|---|---|---|
| Primary source | Adipocytes | Monocytes/macrophages |
| Adipose expression | High | Very low |
| Role in insulin resistance | Direct, established | Indirect via inflammation |
| Serum levels correlate with | Fat mass/adiposity | Inflammation (CRP, TNF-α) |
| Induction signals | Feeding, insulin, thiazolidinediones ↓ | LPS, TNF-α, IL-6, NF-κB |
| PPARγ agonist effect | Reduces resistin | Variable/complex |

## Structure

Resistin is a **108-amino acid (mature protein)** with:

**Structural domains:**
- **N-terminal signal peptide (18 aa):** Directs secretory pathway processing
- **C-terminal globular head domain:** β-sandwich fold homologous to C1q/TNF superfamily; responsible for receptor binding and bioactivity; 10 conserved cysteines form intramolecular and intermolecular disulfide bonds
- **N-terminal α-helical coiled-coil domain:** Drives oligomerization; required for stability

**Oligomeric forms:**
- Resistin circulates as **trimers** (low-molecular-weight form, ~45 kDa) and **hexamers** (high-molecular-weight form, ~90 kDa), linked by interchain disulfide bonds at Cys26
- Higher-order complexes (up to 12-mers) have been reported in some tissues
- The trimeric form is more bioactive in most assays; hexameric forms may have modified receptor-binding properties

**Proposed receptor:**
- **CAP1 (Adenylyl cyclase-associated protein 1):** Identified as a human resistin receptor on macrophages; resistin-CAP1 interaction activates cAMP signaling → PKA → NF-κB activation; this differs from rodent resistin receptor (still uncertain)
- Rodent resistin may act via TLR4 (shared with LPS) on adipocytes; whether human resistin uses TLR4 directly is debated

## Function

**Pro-inflammatory signaling (primary function in humans):**
- Resistin → CAP1 → cAMP → PKA → IKKβ → IκBα phosphorylation → **NF-κB** nuclear translocation → TNF-α, IL-1β, IL-6, IL-12 → amplified inflammatory response
- Resistin → monocyte/macrophage M1 polarization; activates NLRP3 inflammasome (via NF-κB → pro-IL-1β priming + ROS-driven NLRP3 activation)
- Resistin promotes **CC chemokine receptor upregulation** on monocytes → increased recruitment to inflammatory sites

**Insulin resistance mechanisms:**
- Resistin → IKKβ → IRS-1 Ser307 phosphorylation → impaired PI3K/Akt signaling → reduced GLUT4 translocation in muscle
- Resistin → hepatic AMPK inhibition → increased PEPCK and G6Pase expression → enhanced gluconeogenesis → hyperglycemia
- Resistin → TNF-α secretion → TNF-α-mediated IRS-1 Ser307 phosphorylation (amplification via paracrine loop)
- Resistin → direct suppression of adiponectin gene expression → reduced AMPK activation → further insulin resistance (opposing adipokine axis)

**Hepatic lipid metabolism:**
- Resistin activates hepatic SREBP-1c → de novo lipogenesis
- Stimulates VLDL assembly and secretion (MTP upregulation) → hypertriglyceridemia → atherogenic dyslipidemia
- Inhibits lipoprotein lipase on endothelium → reduced VLDL clearance → combined hyperlipidemia pattern

**Endothelial effects:**
- Resistin → endothelial VCAM-1, ICAM-1 → monocyte adhesion
- Increases endothelin-1 production (vasoconstrictor) and reduces eNOS expression → endothelial dysfunction + vasoconstriction
- Promotes vascular smooth muscle cell proliferation and migration → intimal thickening

## Mechanism

**Resistin in NASH:**
1. Adipose tissue macrophage and liver-resident Kupffer cell resistin production increases with obesity and lipotoxic stress
2. Resistin → NF-κB in Kupffer cells → TNF-α and IL-6 → hepatocyte NF-κB → inflammatory gene induction (amplification loop)
3. Resistin suppresses adiponectin → impairs hepatic AMPK → reduces β-oxidation → steatosis worsens
4. Resistin-driven IL-6 → STAT3 → hepatic stellate cell activation → TGF-β production → collagen deposition → fibrosis
5. Serum resistin correlates with NASH histological activity score (NAS), hepatic inflammation grade, and fibrosis stage

**Resistin in rheumatoid arthritis:**
- Synovial fluid resistin is 5–10× higher than serum in active RA
- Source: synovial tissue macrophages (M1-polarized) and fibroblast-like synoviocytes under TNF-α/IL-1β stimulation
- Resistin → synovial macrophage NF-κB → TNF-α, IL-6, IL-8 → pannus formation and cartilage destruction; DAS28 correlates with synovial resistin
- Pioglitazone (PPARγ agonist) reduces synovial resistin and has some anti-inflammatory effects in RA

**Resistin as a biomarker:**
- EPIC-Norfolk prospective cohort: serum resistin in the top quartile → 2.1-fold increased risk of coronary heart disease (independent of BMI, CRP, and lipids)
- Resistin predicts all-cause mortality in hemodialysis patients (independent of CRP)
- NASH fibrosis staging: resistin + AST/ALT ratio = validated for non-invasive NASH fibrosis prediction
- RA disease monitoring: synovial resistin responsive to anti-TNF therapy (infliximab) — falls with treatment, correlating with clinical improvement

**PPARγ agonist effects:**
- Rosiglitazone and pioglitazone reduce resistin in rodents (suppress the adipocyte RETN promoter)
- In humans, PPARγ agonists have inconsistent effects on serum resistin — supporting the different cell-of-origin (monocyte vs. adipocyte) between species
- Pioglitazone reduces hepatic inflammation in NASH partly via adiponectin upregulation, but whether resistin suppression contributes directly in humans is uncertain

## Connections

- `connects-to` → **[NASH](../../07-system/nash/README.md)** — Resistin (primarily monocyte/macrophage-derived in humans) activates NF-κB in Kupffer cells → TNF-α and IL-6 → NASH inflammation; resistin correlates with NASH histological severity; resistin inhibits adiponectin → impairs hepatic AMPK → steatosis and fibrosis.
- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — Resistin impairs insulin signaling via IKK activation → IRS-1 Ser307 phosphorylation → insulin resistance; resistin inhibits AMPK in liver → increased gluconeogenesis; serum resistin is inversely correlated with adiponectin and positively correlated with insulin resistance.
- `connects-to` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — Elevated resistin promotes endothelial VCAM-1 and endothelin-1 → monocyte adhesion and foam cell formation; resistin activates hepatic VLDL production → atherogenic dyslipidemia; serum resistin predicts incident coronary heart disease and heart failure in prospective cohorts.
- `connects-to` → **[Rheumatoid Arthritis](../../07-system/rheumatoid-arthritis/README.md)** — Resistin is markedly elevated in synovial fluid and blood in RA; drives synovial macrophage NF-κB → TNF-α and IL-6 → joint inflammation and destruction; correlates with RA disease activity (DAS28) and joint damage scores.
- `connects-to` → **[Adiponectin](../adiponectin/README.md)** — Resistin and adiponectin are opposing adipokines: adiponectin activates AMPK → insulin sensitivity; resistin suppresses adiponectin expression and impairs AMPK → insulin resistance; resistin:adiponectin ratio is a composite marker of metabolic and inflammatory disease severity.
- `connects-to` → **[TNF-α](../tnf-alpha/README.md)** — Resistin → CAP1/NF-κB → TNF-α from macrophages; TNF-α induces resistin → feedforward inflammation; both signal via IRS-1 Ser307 phosphorylation → insulin resistance; anti-TNF (infliximab) reduces serum resistin in RA — confirming TNF drives resistin production in inflammation.
- `connects-to` → **[IL-6](../il-6/README.md)** — Resistin activates Kupffer cell NF-κB → IL-6; IL-6 → STAT3 → hepatic stellate cells → TGF-β → fibrosis in NASH; resistin-IL-6 axis correlates with NASH fibrosis stage; IL-6 induces resistin from monocytes → feedforward loop; IL-6 + resistin co-elevation predicts CVD events.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^steppan-2001-resistin-discovery]: Steppan CM, Bailey ST, Bhat S, et al. The hormone resistin links obesity to diabetes. *Nature.* 2001;409(6818):307-312. [doi:10.1038/35053000](https://doi.org/10.1038/35053000) · [PubMed 11201732](https://pubmed.ncbi.nlm.nih.gov/11201732/)
[^lehrke-2004-resistin-human]: Lehrke M, Reilly MP, Millington SC, Iqbal N, Rader DJ, Lazar MA. An inflammatory cascade leading to hyperresistinemia in humans. *PLoS Med.* 2004;1(2):e45. [doi:10.1371/journal.pmed.0010045](https://doi.org/10.1371/journal.pmed.0010045) · [PubMed 15526055](https://pubmed.ncbi.nlm.nih.gov/15526055/)
