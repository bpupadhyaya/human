---
schema: medicine-entry/v1
id: checkpoint-inhibitors
name: Checkpoint Inhibitors
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Monoclonal antibodies blocking immune checkpoint receptors (PD-1, PD-L1, CTLA-4) that tumors exploit to suppress T cell killing. Nobel Prize 2018 (Allison & Honjo). Transform survival in melanoma, NSCLC, MSI-H tumors, and 15+ cancer types."
aliases: ["immune checkpoint inhibitors", "ICI", "anti-PD-1", "anti-PD-L1", "anti-CTLA-4", "pembrolizumab", "nivolumab", "ipilimumab", "atezolizumab", "durvalumab", "Keytruda", "Opdivo", "Yervoy"]
drug_class: immune checkpoint inhibitor monoclonal antibody
modality: biologic / monoclonal antibody
key_agents:
  - pembrolizumab (Keytruda) — anti-PD-1 IgG4
  - nivolumab (Opdivo) — anti-PD-1 IgG4
  - ipilimumab (Yervoy) — anti-CTLA-4 IgG1
  - atezolizumab (Tecentriq) — anti-PD-L1 IgG1
  - durvalumab (Imfinzi) — anti-PD-L1 IgG1
  - avelumab (Bavencio) — anti-PD-L1 IgG1
sources:
  - id: brahmer-2012-pd-l1
    type: peer-reviewed
    cite: "Brahmer JR, Tykodi SS, Chow LQ, et al. Safety and activity of anti-PD-L1 antibody in patients with advanced cancer. N Engl J Med. 2012;366(26):2455-65."
    doi: "10.1056/NEJMoa1200694"
    pmid: "22658128"
    url: "https://doi.org/10.1056/NEJMoa1200694"
  - id: robert-2015-pembrolizumab
    type: peer-reviewed
    cite: "Robert C, Schachter J, Long GV, et al. Pembrolizumab versus ipilimumab in advanced melanoma. N Engl J Med. 2015;372(26):2521-32."
    doi: "10.1056/NEJMoa1503093"
    pmid: "25891173"
    url: "https://doi.org/10.1056/NEJMoa1503093"
  - id: hodi-2010-ipilimumab
    type: peer-reviewed
    cite: "Hodi FS, O'Day SJ, McDermott DF, et al. Improved survival with ipilimumab in patients with metastatic melanoma. N Engl J Med. 2010;363(8):711-23."
    doi: "10.1056/NEJMoa1003466"
    pmid: "20525992"
    url: "https://doi.org/10.1056/NEJMoa1003466"
cross_links:
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: targets
    evidence: brahmer-2012-pd-l1
    note: "Checkpoint inhibitors block inhibitory receptors (PD-1, CTLA-4) on CD8+ T cells that tumors exploit to suppress cytotoxic killing; blockade reinvigorates exhausted tumour-infiltrating CTLs, restoring perforin/granzyme cytotoxicity and IFN-γ production in the tumour microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: targets
    evidence: hodi-2010-ipilimumab
    note: "CTLA-4 blockade primarily acts on CD4+ T helper cells (both effector and regulatory T cells) in lymph nodes, amplifying the early priming phase of anti-tumour immune responses and depleting intratumoral Tregs via ADCC (for IgG1 ipilimumab)."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    evidence: brahmer-2012-pd-l1
    note: "Immune checkpoint blockade unleashes T cell cytokine production including TNF-α and IFN-γ; elevated TNF-α mediates anti-tumour effects but also contributes to immune-related adverse events (irAEs) including colitis and hepatitis; TNF blockade (infliximab) can rescue severe checkpoint inhibitor toxicity."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: robert-2015-pembrolizumab
    note: "Systemic PD-1/PD-L1 or CTLA-4 blockade removes peripheral immune tolerance mechanisms; broadly activates auto-reactive T cells → immune-related adverse events (irAEs) affecting skin, gut, liver, endocrine glands, lungs — managed with corticosteroids and organ-specific immunosuppression."
  - target: 01-human/07-system/melanoma
    relation: treats
    note: "Checkpoint inhibitors transformed metastatic melanoma: pembrolizumab vs. ipilimumab (KEYNOTE-006) ORR 33.7% vs. 11.9%; nivolumab + ipilimumab (CheckMate 067) 5-year OS 52%; adjuvant PD-1 blockade reduces recurrence; BRAF-mutant tumors benefit from ICI + targeted therapy."
  - target: 01-human/03-molecular/pd-1
    relation: targets
    note: "PD-1/PD-L1 blockade is the primary checkpoint inhibitor mechanism: pembrolizumab and nivolumab block PD-1 → release SHP-2-mediated T cell suppression; PD-L1 IHC (CPS/TPS) guides pembrolizumab eligibility in NSCLC, gastric, cervical, HNC; PD-1 + CTLA-4 blockade is synergistic."
  - target: 01-human/03-molecular/ctla-4
    relation: targets
    note: "CTLA-4 blockade (ipilimumab) acts during T cell priming: outcompetes CD28 for CD80/CD86 → amplifies early anti-tumor responses; IgG1 isotype enables ADCC-mediated intratumoral Treg depletion; nivolumab + ipilimumab doubles melanoma efficacy with ~55% severe irAE rate."
---

# Checkpoint Inhibitors

## Overview

Immune checkpoint inhibitors (ICIs) are **monoclonal antibodies** that block inhibitory receptor-ligand interactions that cancer cells exploit to evade destruction by the immune system. Healthy tissues express checkpoint ligands (PD-L1, PD-L2, CD80/CD86) to protect themselves from autoimmune attack by dampening T cell activation — a physiological tolerance mechanism. Tumors co-opt this system to escape immune surveillance by upregulating these ligands, particularly PD-L1, creating an immunosuppressed tumour microenvironment.

The conceptual foundation was laid by **James P. Allison** (University of Texas MD Anderson Cancer Center) and **Tasuku Honjo** (Kyoto University), who independently identified CTLA-4 and PD-1 as brake mechanisms on T cell activation and proposed their blockade as cancer therapy. Both received the **Nobel Prize in Physiology or Medicine in 2018** for this discovery.

Ipilimumab (anti-CTLA-4) became the **first FDA-approved checkpoint inhibitor in March 2011**, demonstrating the first-ever improvement in overall survival in metastatic melanoma — a disease with median survival of 6–9 months that became, in some patients, **durably curable** [^hodi-2010-ipilimumab]. Pembrolizumab and nivolumab (anti-PD-1) followed in 2014 with superior efficacy and tolerability profiles. ICIs have since transformed the treatment landscape of melanoma, non-small cell lung cancer (NSCLC), renal cell carcinoma, bladder cancer, Hodgkin lymphoma, MSI-H/dMMR solid tumors, and 15+ other indications.

## Mechanism

### The Checkpoint Biology

**PD-1/PD-L1 Axis:**
- **PD-1 (Programmed Death-1, CD279):** Type I transmembrane receptor expressed on activated T cells, B cells, NK cells, and tumour-infiltrating lymphocytes (TILs); has two cytoplasmic immunoreceptor tyrosine-based inhibitory motifs (ITIMs) that recruit SHP-1/SHP-2 phosphatases upon PD-L1/PD-L2 binding
- **PD-L1 (Programmed Death Ligand-1, CD274, B7-H1):** IFN-γ-inducible glycoprotein expressed on cancer cells, tumour-associated macrophages, DCs, and stromal cells; normal function: peripheral tolerance and protection of fetal trophoblast from maternal T cells
- **Signaling:** PD-1:PD-L1 → SHP-2 dephosphorylates CD3ζ, ZAP-70, and CD28 → blocks PI3K-Akt-mTOR (survival/proliferation) and PLCγ1-NFAT (effector cytokines) → T cell exhaustion/anergy → tumour escape

**CTLA-4 Axis:**
- **CTLA-4 (Cytotoxic T-Lymphocyte Antigen-4, CD152):** Structural homologue of CD28 costimulatory receptor; binds CD80/CD86 with ~100-fold higher affinity than CD28; recruited from intracellular vesicles to immunological synapse upon T cell activation
- **Mechanism:** CTLA-4 outcompetes CD28 for B7 ligands → removes Signal 2 from the T cell → impaired early T cell priming in lymph nodes; also causes transendocytosis and degradation of CD80/86 from APCs; Tregs constitutively express CTLA-4 — ipilimumab (IgG1) depletes intratumoral Tregs via ADCC

### Drug Mechanisms of Action

| Agent | Target | Isotype | Mechanism |
|:---|:---|:---|:---|
| **Pembrolizumab** | PD-1 | IgG4 (stabilised hinge) | Blocks PD-1:PD-L1/PD-L2 interaction → prevents SHP-2 recruitment → restores T cell signaling, proliferation, IFN-γ production |
| **Nivolumab** | PD-1 | IgG4 | Same as pembrolizumab; different epitope; FDA approved for broader indications including HCC, NSCLC, RCC, squamous HNC |
| **Ipilimumab** | CTLA-4 | IgG1 | Blocks CTLA-4:CD80/86 → removes a brake during T cell priming; IgG1 Fc → ADCC-mediated Treg depletion in tumour; distinct from PD-1 mechanism — synergistic with nivolumab |
| **Atezolizumab** | PD-L1 | IgG1 (Fc-engineered, no ADCC) | Blocks PD-L1:PD-1 and PD-L1:CD80 interaction; preserves PD-L2:PD-1 interaction (may reduce autoimmune toxicity) |
| **Durvalumab** | PD-L1 | IgG1 (Fc mutant) | Blocks PD-L1:PD-1 and PD-L1:CD80; approved for unresectable Stage III NSCLC (PACIFIC trial) and biliary tract cancer |

### Biomarkers of Response

| Biomarker | Significance |
|:---|:---|
| **PD-L1 expression (IHC TPS or CPS)** | Predictive for pembrolizumab in NSCLC (TPS ≥50%), head and neck, gastric cancers; imperfect — ~30% of PD-L1-low patients still respond |
| **Tumour Mutational Burden (TMB)** | High TMB (≥10 mut/Mb; FDA-approved companion diagnostic) — more neoantigens → higher T cell recognition; pan-tumour pembrolizumab approval |
| **MSI-H / dMMR** | Microsatellite instability-high / mismatch repair deficient tumours — pan-tumour pembrolizumab approval (FDA 2017); first tissue-agnostic oncology approval |
| **EBV+ / PD-L1+ gastric cancer** | Strong predictor of anti-PD-1 response |
| **Tumour-infiltrating lymphocytes (TILs)** | High TIL density correlates with response |

## Clinical Use

### Major Approved Indications and Survival Outcomes

| Tumour | Agent(s) | Key Outcome | Trial |
|:---|:---|:---|:---|
| **Metastatic melanoma** | Nivolumab + ipilimumab | 5-year OS: 52% (vs. 6–8% historical) | CheckMate 067 |
| **Metastatic melanoma** | Pembrolizumab vs. ipilimumab | ORR 33.7% vs. 11.9%; superior PFS and OS [^robert-2015-pembrolizumab] | KEYNOTE-006 |
| **NSCLC (PD-L1 ≥50%)** | Pembrolizumab 1st line | PFS 10.3 vs. 6.0 months chemo; OS benefit | KEYNOTE-024 |
| **Bladder cancer** | Atezolizumab / pembrolizumab | ORR ~20%; OS benefit in cisplatin-ineligible | Multiple |
| **Hodgkin lymphoma** | Nivolumab / pembrolizumab | ORR 65–70% in R/R after ASCT + brentuximab | Multiple |
| **MSI-H/dMMR solid tumors** | Pembrolizumab (pan-tumour) | ORR ~40%; durable responses | KEYNOTE-158 |
| **Hepatocellular carcinoma** | Nivolumab + ipilimumab | ORR 32%; 22% complete response | CheckMate 040 |
| **Stage III NSCLC** | Durvalumab (consolidation) | 3-year OS 57% vs. 48% chemo alone | PACIFIC |

### Immune-Related Adverse Events (irAEs)

Checkpoint inhibitor toxicity is distinct from chemotherapy toxicity — it is **immune-mediated** and can affect any organ:

| System | irAE | Frequency | Management |
|:---|:---|:---|:---|
| **Skin** | Maculopapular rash, vitiligo, pruritus | ~30–40% | Topical/oral corticosteroids; withhold for grade 3 |
| **Gastrointestinal** | Immune colitis (diarrhoea, bloody stool) | ~10–20% (higher with CTLA-4) | Oral/IV steroids; infliximab for steroid-refractory |
| **Liver** | Immune hepatitis (↑ALT/AST) | ~5–10% | Hold drug; steroids; mycophenolate mofetil |
| **Endocrine** | Thyroiditis → hypo/hyperthyroid; hypophysitis; adrenal insufficiency; T1DM | ~10–20% | Hormone replacement; steroids for hypophysitis |
| **Pulmonary** | Immune pneumonitis (dyspnoea, cough, infiltrates) | ~3–5% | Hold drug; high-dose steroids; infliximab/MMF |
| **Neurological** | Peripheral neuropathy, Guillain-Barré, myasthenia gravis, encephalitis | <1% | Hold drug; high-dose IVIG; steroids |
| **Cardiac** | Immune myocarditis (rare but life-threatening) | <1% | Immediate high-dose steroids; cardiac monitoring |

Combination ipilimumab + nivolumab doubles efficacy in many tumors but increases severe irAEs to ~55–60% (vs. 20–25% for anti-PD-1 monotherapy).

**irAE management principles:** Grade 1 — continue ICI with monitoring; Grade 2 — hold ICI, start steroids (prednisone 0.5–1 mg/kg/day); Grade 3–4 — permanently discontinue, high-dose steroids (methylprednisolone 1–2 mg/kg/day IV); steroid-refractory: infliximab, mycophenolate mofetil, IVIG, tacrolimus (organ-dependent).

## Evidence

### Ipilimumab OS Benefit in Melanoma (Hodi 2010)

The landmark phase 3 trial by Hodi et al. [^hodi-2010-ipilimumab] randomised 676 patients with previously treated metastatic melanoma to ipilimumab ± gp100 vaccine vs. gp100 alone:

- **Median OS: 10.1 months (ipilimumab) vs. 6.4 months (gp100 alone)** — HR 0.68, p<0.001
- **3-year OS: ~21%** — remarkable tail on the survival curve indicating durable long-term survival in a subset, unprecedented in metastatic melanoma
- Toxicity: grade 3–4 immune-related events in 10–15%; 14 drug-related deaths (2.1%)
- **FDA approval granted March 2011** — first drug ever to demonstrate OS benefit in metastatic melanoma

### Pembrolizumab vs. Ipilimumab in Melanoma (KEYNOTE-006)

Robert et al. [^robert-2015-pembrolizumab] randomised 834 treatment-naive advanced melanoma patients to pembrolizumab Q2W, pembrolizumab Q3W, or ipilimumab Q3W:

- **6-month PFS: 47.3%/46.4% (pembrolizumab) vs. 26.5% (ipilimumab)**
- **ORR: 33.7% (pembrolizumab) vs. 11.9% (ipilimumab)**
- Grade 3–5 drug-related toxicity: 13.3%/10.1% vs. 19.9% — pembrolizumab better tolerated
- Established pembrolizumab as preferred frontline therapy, superseding ipilimumab in untreated melanoma

### Brahmer et al. — First Clinical Proof of PD-L1 Inhibition (2012)

Brahmer et al. [^brahmer-2012-pd-l1] phase 1 trial of anti-PD-L1 (BMS-936559) in 207 patients with advanced solid tumors:

- Objective responses in patients with NSCLC (10%), melanoma (17%), renal cell carcinoma (12%), colorectal (3%), ovarian (6%)
- Absence of severe pulmonary toxicity (compared to anti-CTLA-4), suggesting PD-L1 pathway blockade was better tolerated
- Established clinical proof of anti-PD-L1 as a viable drug class and stimulated broad development of the current agents

## Connections

- `targets` → **[Cytotoxic T Cell](../../../../01-human/04-cellular/t-cytotoxic-cell/README.md)** — PD-1 blockade reinvigorates exhausted tumour-infiltrating CD8+ T cells, restoring cytotoxic capacity (perforin/granzyme, IFN-γ) in the tumour microenvironment; CTLA-4 blockade acts earlier, amplifying T cell priming in lymph nodes.
- `targets` → **[T Helper Cell](../../../../01-human/04-cellular/t-helper-cell/README.md)** — CTLA-4 is primarily expressed on CD4+ T cells; ipilimumab blocks CTLA-4 on both effector and regulatory CD4+ T cells, amplifying anti-tumor help and (via IgG1 ADCC) depleting intratumoral Tregs.
- `modulates` → **[TNF-α](../../../../01-human/03-molecular/tnf-alpha/README.md)** — Checkpoint blockade unleashes T cell TNF-α production; elevated TNF-α contributes to both anti-tumour efficacy and irAEs including colitis and hepatitis; infliximab (TNF blockade) rescues severe steroid-refractory immune colitis without abrogating anti-tumour responses.
- `modulates` → **[Immune System](../../../../01-human/07-system/immune-system/README.md)** — Systemic removal of peripheral tolerance checkpoints activates autoreactive T cell clones → irAEs spanning skin, gut, liver, lung, and endocrine systems; managed with corticosteroids and targeted immunosuppression without fully ablating anti-tumour immunity.
- `treats` → **[Melanoma](../../../../01-human/07-system/melanoma/README.md)** — Checkpoint inhibitors transformed metastatic melanoma: pembrolizumab vs. ipilimumab (KEYNOTE-006) ORR 33.7% vs. 11.9%; nivolumab + ipilimumab (CheckMate 067) 5-year OS 52%; adjuvant PD-1 blockade reduces recurrence; BRAF-mutant tumors benefit from ICI + targeted therapy.
- `targets` → **[PD-1](../../../../01-human/03-molecular/pd-1/README.md)** — PD-1/PD-L1 blockade is the primary checkpoint inhibitor mechanism: pembrolizumab and nivolumab block PD-1 → release SHP-2-mediated T cell suppression; PD-L1 IHC (CPS/TPS) guides pembrolizumab eligibility in NSCLC, gastric, cervical, HNC; PD-1 + CTLA-4 blockade is synergistic.
- `targets` → **[CTLA-4](../../../../01-human/03-molecular/ctla-4/README.md)** — CTLA-4 blockade (ipilimumab) acts during T cell priming: outcompetes CD28 for CD80/CD86 → amplifies early anti-tumor responses; IgG1 isotype enables ADCC-mediated intratumoral Treg depletion; nivolumab + ipilimumab doubles melanoma efficacy with ~55% severe irAE rate.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^brahmer-2012-pd-l1]: Brahmer JR, Tykodi SS, Chow LQ, et al. Safety and activity of anti-PD-L1 antibody in patients with advanced cancer. *N Engl J Med.* 2012;366(26):2455-65. [doi:10.1056/NEJMoa1200694](https://doi.org/10.1056/NEJMoa1200694) · [PubMed 22658128](https://pubmed.ncbi.nlm.nih.gov/22658128/)
[^robert-2015-pembrolizumab]: Robert C, Schachter J, Long GV, et al. Pembrolizumab versus ipilimumab in advanced melanoma. *N Engl J Med.* 2015;372(26):2521-32. [doi:10.1056/NEJMoa1503093](https://doi.org/10.1056/NEJMoa1503093) · [PubMed 25891173](https://pubmed.ncbi.nlm.nih.gov/25891173/)
[^hodi-2010-ipilimumab]: Hodi FS, O'Day SJ, McDermott DF, et al. Improved survival with ipilimumab in patients with metastatic melanoma. *N Engl J Med.* 2010;363(8):711-23. [doi:10.1056/NEJMoa1003466](https://doi.org/10.1056/NEJMoa1003466) · [PubMed 20525992](https://pubmed.ncbi.nlm.nih.gov/20525992/)
