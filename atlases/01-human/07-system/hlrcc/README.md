---
schema: human-scale-entry/v1
id: hlrcc
name: Hereditary Leiomyomatosis and Renal Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary leiomyomatosis and renal cell carcinoma (HLRCC) is caused by germline FH mutations; cutaneous and uterine leiomyomas + aggressive FH-deficient RCC; collecting duct-like histology; fumarate drives HIF-1α + immune evasion; bevacizumab + erlotinib standard."
aliases: ["HLRCC", "hereditary leiomyomatosis renal cell carcinoma", "FH syndrome", "Reed syndrome", "FH-deficient RCC", "HLRCC RCC", "FH leiomyoma", "fumarate hydratase deficiency", "FH hereditary cancer", "leiomyomatosis RCC"]
sources:
  - id: tomlinson-2002-fh
    type: peer-reviewed
    cite: "Tomlinson IP, Alam NA, Rowan AJ, et al. Germline mutations in FH predispose to dominantly inherited uterine fibroids, skin leiomyomata and papillary renal cell cancer. Nat Genet. 2002;30(4):406-410."
    doi: "10.1038/ng849"
    pmid: "11865300"
    url: "https://doi.org/10.1038/ng849"
  - id: linehan-2013-fh-review
    type: peer-reviewed
    cite: "Linehan WM, Rouault TA. Molecular pathways: fumarate hydratase-deficient kidney cancer — targeting the Warburg effect in cancer. Clin Cancer Res. 2013;19(13):3345-3352."
    doi: "10.1158/1078-0432.CCR-13-0304"
    pmid: "23836472"
    url: "https://doi.org/10.1158/1078-0432.CCR-13-0304"
cross_links:
  - target: 01-human/03-molecular/fh
    relation: connects-to
    note: "Germline FH mutations cause HLRCC (autosomal dominant); FH LOF → fumarate accumulation; 2SC IHC (anti-2-succino-cysteine) positive in FH-deficient tumors; FH IHC loss diagnostic; somatic second hit (LOH or second mutation) in each HLRCC leiomyoma or RCC"
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HLRCC-associated RCC driven by HIF-1α pseudohypoxia (FH LOF → PHD inhibition → HIF-1α stabilized); VEGF/HIF-1α pathway active; bevacizumab (anti-VEGF) + erlotinib standard for HLRCC RCC; HIF-2α inhibitor belzutifan being explored in FH-deficient RCC"
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "HLRCC-associated RCC is pseudohypoxic similar to VHL-mutant ccRCC (both have HIF-1α and VEGF overexpression); histologically distinct (type 2B papillary/collecting duct-like, NOT clear cell); anti-VEGF therapies active in both; belzutifan explored in FH-deficient RCC"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "HLRCC-associated RCC: most aggressive hereditary RCC; collecting duct-like/papillary type 2B; often metastatic at diagnosis; FH IHC loss + 2SC positivity diagnostic; bevacizumab + erlotinib standard (NCI Phase 2, ORR ~64%, mPFS 21 months); sunitinib/pazopanib insufficient"
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "HLRCC produces multiple smooth muscle tumors (leiomyomas): painful cutaneous nodules from arrector pili muscle and early-onset, large, multiple uterine fibroids; biallelic FH loss drives them, and FH-/2SC+ immunostaining distinguishes HLRCC leiomyomas from sporadic ones."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Fumarate accumulation stabilizes HIF-1α (pseudohypoxia) → VEGF transcription → tumor angiogenesis; this is the therapeutic handle in FH-deficient RCC — bevacizumab (anti-VEGF) plus erlotinib (anti-EGFR) achieves ~65% response, far exceeding VEGFR-TKIs like sunitinib."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "HLRCC causes the most aggressive hereditary kidney cancer — collecting-duct-like/type-2B papillary RCC that can metastasize even at 1-2 cm; radical (not partial) nephrectomy with lymphadenectomy is preferred, and annual renal MRI surveillance starts at genetic diagnosis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The uterus is often where HLRCC declares itself: women develop numerous, large, early-onset uterine leiomyomas (fibroids), frequently needing myomectomy or hysterectomy before age 30 — so multiple early fibroids with cutaneous leiomyomas should prompt FH testing."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous leiomyomas are the 'L' of HLRCC and its visible clue: firm, often painful skin-colored papules from arrector pili smooth muscle appearing in the 20s-30s; their recognition (with FH/2SC staining) flags the syndrome years before the aggressive kidney cancer."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "HLRCC's FH belongs to the same Krebs-cycle, pseudohypoxia family (SDHx, FH) that causes hereditary pheochromocytoma/paraganglioma: FH loss accumulates fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF — so rare FH-mutant PPGLs occur, sharing fumarate-driven biology."
---

# Hereditary Leiomyomatosis and Renal Cell Carcinoma

## Overview

**Hereditary leiomyomatosis and renal cell carcinoma (HLRCC)**, also known as **Reed syndrome**, is an autosomal dominant hereditary cancer syndrome caused by germline pathogenic variants in **FH** (fumarate hydratase), the TCA cycle enzyme that converts fumarate to malate. HLRCC is characterized by a triad of manifestations: (1) **cutaneous leiomyomas** — benign piloerector smooth muscle tumors presenting as painful nodular skin lesions; (2) **uterine leiomyomas** (fibroids) — typically early onset (<30 years), symptomatic, large, and multiple, often requiring myomectomy or hysterectomy; and (3) **HLRCC-associated RCC** — an aggressive FH-deficient kidney cancer with distinctive collecting duct-like histology, early metastatic spread, and a prognosis that is dramatically worse than sporadic clear cell RCC. HLRCC-associated RCC is driven by fumarate-mediated pseudohypoxia (HIF-1α activation) and epigenetic reprogramming (TET2/KDM inhibition → DNA and histone hypermethylation). The current standard of care for HLRCC-associated metastatic RCC is **bevacizumab + erlotinib**, which achieves remarkable response rates (~65%) in this otherwise chemotherapy-resistant tumor [^tomlinson-2002-fh] [^linehan-2013-fh-review].

**Epidemiology:**
- Prevalence: very rare; estimated 1/200,000; ~1,500-2,000 HLRCC families worldwide
- Inheritance: autosomal dominant; 50% penetrance per generation; near-complete penetrance for cutaneous leiomyomas; incomplete penetrance for RCC
- FH germline pathogenic variant: identified in ~94% of clinically diagnosed HLRCC families; ~6% testing-negative families may have deep intronic or non-coding variants missed by standard testing
- Penetrance: cutaneous leiomyomas ~85-90% of carriers; uterine leiomyomas: ~90% of female carriers; HLRCC-associated RCC: ~15-20% of FH carriers (lifetime)
- Age of RCC: median age ~37 years (vs ~64 for sporadic ccRCC); RCC can occur in 2nd-3rd decade; early-onset RCC in a young person with cutaneous leiomyomas = pathognomonic for HLRCC

## Structure

### HLRCC clinical phenotype components

**Cutaneous leiomyomas:**
- Derived from arrector pili muscle (piloerector smooth muscle in hair follicle); NOT subcutaneous leiomyomas (from dartos muscle or blood vessel smooth muscle)
- Morphology: firm, skin-colored to brownish-red papules/nodules; 0.5-2 cm; dome-shaped
- Distribution: trunk (most common), extremities, face; frequently multiple (5-100 lesions)
- Symptoms: PAIN is the cardinal feature — spontaneous or triggered by pressure, cold, or anxiety; due to smooth muscle contraction; differentiates cutaneous leiomyoma from other skin lesions
- Histology: intersecting bundles of smooth muscle cells (cigar-shaped nuclei, eosinophilic cytoplasm) in dermis; Masson trichrome stain confirms smooth muscle; IHC: smooth muscle actin (SMA) and desmin positive
- FH IHC on leiomyoma: protein loss + 2SC positivity = FH-deficient leiomyoma = HLRCC

**Uterine leiomyomas (fibroids):**
- Hallmark features distinguishing HLRCC from sporadic fibroids:
  - Age of onset: typically age 20-30 (vs >35 for sporadic)
  - Number: multiple (often 5-20 or more)
  - Size: large (5-10 cm or greater)
  - Symptoms: menorrhagia, dysmenorrhea, infertility, pelvic pressure — often severe enough to require surgery by age 30-35
- Pathology: HLRCC fibroids are histologically identical to sporadic fibroids (smooth muscle fascicles); but FH IHC: loss + 2SC positivity distinguishes HLRCC from sporadic (sporadic: FH intact, 2SC negative)
- Somatic HLRCC fibroids: ~50% of all uterine fibroids have somatic FH biallelic LOF; this means routine fibroid pathology would identify FH-deficient tumors; not all FH-deficient fibroids arise from germline — most are sporadic somatic events

**HLRCC-associated RCC:**
- Histology: collecting duct-like carcinoma (formerly called type 2B papillary RCC); large cells with prominent macronucleoli surrounded by a clear halo ("owl eye" nuclei); papillary, tubulopapillary, or solid growth patterns; stroma with abundant desmoplasia
- IHC: FH-/2SC+ (diagnostic); CK7+, PAX8+, CD10 variable; WT1 negative; CK20 negative; tethered to renal medulla/collecting duct area
- Molecular: biallelic FH LOF (germline + somatic, or two somatic events); no VHL mutation; VEGFR and EGFR overexpressed; HIF-1α and HIF-2α nuclear; GLUT1 high
- Aggressive behavior: often presents at Stage IV (metastatic) — nodal and distant metastases; even small primary tumors can metastasize; unlike ccRCC where a 2 cm tumor is almost always cured by nephrectomy, FH-deficient RCC can metastasize at 1-2 cm

## Function

### Fumarate-driven oncogenesis in HLRCC

**Pseudohypoxic signaling:** [^linehan-2013-fh-review]
FH LOF → fumarate accumulates → inhibits PHD1/2/3 (prolyl hydroxylase domain enzymes; normally hydroxylate HIF-1α at Pro-402, Pro-564 using α-KG and O2) → HIF-1α not hydroxylated → VHL E3 ligase cannot bind → HIF-1α escapes proteasomal degradation → HIF-1α nuclear (pseudohypoxic regardless of O2 tension) → transcriptional activation of HIF target genes:
- **VEGF/VEGFA**: angiogenesis → tumor vasculature → therapeutic target (bevacizumab)
- **GLUT1 (SLC2A1)**: glucose transporter → aerobic glycolysis (Warburg effect)
- **PDK1**: pyruvate dehydrogenase kinase 1 → blocks pyruvate entry into TCA → lactate instead of oxidative phosphorylation
- **LDHA**: lactate dehydrogenase A → lactate production → acidic microenvironment
- **CA9**: carbonic anhydrase 9 → pH regulation

**Epigenetic reprogramming:**
Fumarate competitive inhibition of α-KG-dependent dioxygenases:
- TET2 inhibition → 5mC not converted to 5hmC → progressive DNA methylation → CIMP-like → silencing of immune checkpoint genes, tumor suppressors, MMR genes
- KDM4A (H3K9me3), KDM5C (H3K4me3), KDM6A (H3K27me3) inhibition → heterochromatin expansion → gene silencing
- Consequence: FH-deficient tumors have a "cold" immune microenvironment (low TIL density, low PD-L1) due to epigenetic silencing of innate immune genes (STING, IFN pathway)

**KEAP1-NRF2 pathway activation:**
Fumarate succination of KEAP1 cysteines (C273, C288) → conformational change → KEAP1 cannot present NRF2 for CUL3-RBX1 E3 ubiquitination → NRF2 nuclear → antioxidant response element (ARE) genes: NQO1, GCLC, HMOX1, TXN, G6PD; NRF2 activation protects FH-deficient cells from oxidative stress; NRF2 also promotes pentose phosphate pathway (PPP) → NADPH production → reductive biosynthesis; NRF2 nuclear staining by IHC is a secondary marker of FH deficiency (not as specific as 2SC)

**Two-hit tumorigenesis:**
Germline FH pathogenic variant (first hit) → somatic LOH or second truncating mutation in a single renal tubular epithelial cell (second hit) → biallelic FH LOF → fumarate accumulation → tumorigenesis; LOH at 1q43 (FH locus) is the most common second hit in HLRCC RCC (~70%); somatic truncating mutation: ~25%; somatic FH missense: rare

## Pathology

### Diagnosis and genetic evaluation

**Clinical diagnostic criteria:**
Definite HLRCC: any of:
1. Cutaneous leiomyoma (histologically confirmed) + first-degree relative with HLRCC
2. Cutaneous leiomyoma + HLRCC-associated RCC
3. HLRCC-associated RCC + pathogenic FH germline variant
4. Multiple cutaneous leiomyomas with FH IHC loss + 2SC positivity on skin biopsy

Probable HLRCC:
- Multiple painful cutaneous leiomyomas alone (in the absence of FH testing)
- Early-onset symptomatic uterine fibroids in young woman with cutaneous leiomyomas
- Type 2B papillary/collecting duct-like RCC in a young patient → reflexively test FH IHC + 2SC

**Molecular diagnostic workup:**
1. FH germline sequencing (full coding + splice sites) + MLPA: preferred first-line
2. Tumor FH IHC + 2SC IHC: FH-/2SC+ confirms FH deficiency; triggers germline testing
3. FH enzyme activity assay (lymphocytes or fibroblasts): reduced activity confirms FH LOF; used when genetic testing inconclusive

**Surveillance recommendations (NCCN/ESMO 2024):**

Renal:
- Annual abdominal MRI (superior to CT for soft tissue characterization, avoids radiation) from time of genetic diagnosis
- Any renal mass ≥1 cm in FH carrier: biopsy vs immediate surgery (surgery preferred due to aggressive behavior; "see and treat" policy)
- Rationale: early detection is critical because even small tumors can metastasize in HLRCC

Uterine:
- Annual pelvic TVUS from age 20-25 in female FH carriers
- Symptom management: hormonal (OCP, progestins, GnRH agonists), surgical (myomectomy, hysterectomy)
- Fertility preservation: discussion with reproductive endocrinologist; early myomectomy before fibroids cause infertility may be appropriate
- Uterine fibroid embolization: generally avoided in HLRCC carriers (concerns about residual viable fibroid tissue)

Cutaneous:
- Dermatology evaluation: document and photograph skin lesions; confirm diagnosis by biopsy of most symptomatic lesion
- Pain management: calcium channel blockers (nifedipine, 10-30 mg/day: relaxes smooth muscle → reduces leiomyoma contraction pain); gabapentin for neuropathic pain component; topical nitroglycerin (vasodilation → reduced piloerector spasm); local excision for isolated symptomatic lesions

### Treatment of HLRCC-associated RCC

**Surgical management:**
- Localized HLRCC RCC: radical nephrectomy preferred (NOT partial nephrectomy); rationale: multifocal micrometastases may be present even in small tumor; wide excision
- Role of lymphadenectomy: recommended given high nodal metastasis rate
- Metastatic disease: cytoreductive nephrectomy benefit unclear in HLRCC (as in clear cell RCC); decision individualized; systemic therapy primary for Stage IV

**Bevacizumab + erlotinib (standard of care):** [^linehan-2013-fh-review]
- NCI HRCC Phase 2 trial (Srinivasan et al., updated 2021): N=43 HLRCC-associated and sporadic FH-deficient RCC; bevacizumab 15 mg/kg IV q21d + erlotinib 150 mg PO daily
- ORR: ~64-70% (predominantly partial responses by RECIST); DCR: ~90%
- mPFS: ~21.1 months; mOS: ~30 months (far exceeding historical controls on sunitinib/pazopanib where mPFS ~3-5 months in FH-deficient RCC)
- Mechanism: bevacizumab (anti-VEGF antibody) blocks VEGF-A → anti-angiogenic; erlotinib (EGFR-TKI) inhibits EGFR-driven VEGF production and cell proliferation; synergy: erlotinib reduces tumor-intrinsic VEGF secretion → enhances bevacizumab efficacy
- Toxicity: hypertension (~35%), proteinuria, GI (diarrhea, rash); erlotinib skin rash often precedes response
- Standard of care recommendation: per NCI/NCCN for HLRCC-associated metastatic RCC

**Alternative/investigational therapies:**
- **Sunitinib, pazopanib**: VEGFR-TKIs; inadequate in FH-deficient RCC (ORR ~10-15%, mPFS ~3-5 months); inferior to bevacizumab + erlotinib
- **Nivolumab + ipilimumab**: checkpoint inhibitor combination; being evaluated in FH-deficient RCC (NCI basket trial); rationale: despite cold baseline tumor, IO combinations may overcome epigenetic immunosuppression
- **Belzutifan (HIF-2α inhibitor)**: FDA-approved for VHL-associated ccRCC; Phase 2 in FH-deficient RCC (NCT04895748): early response data pending; HIF-2α active in HLRCC RCC alongside HIF-1α
- **PARP inhibitors**: FH-deficient cells may have HR deficiency (cytosolic FH at DSBs → fumarate → KDM2A inhibition → HR/NHEJ imbalance); olaparib explored in FH-deficient tumor basket
- **mTOR inhibitors**: fumarate → HIF-1α → mTOR signaling; everolimus not well-studied in HLRCC RCC specifically; less potent than bevacizumab + erlotinib

**Prognosis:**
- Localized HLRCC RCC (Stage I-II): surgical cure achievable; ~60-70% 5-year survival with nephrectomy + surveillance
- Locally advanced/Stage III: 5-year survival ~30-40% with surgery; adjuvant systemic therapy role uncertain
- Metastatic HLRCC RCC (Stage IV): historically median OS <12 months; with bevacizumab + erlotinib: median OS ~30 months; responses can be durable (some patients >5 years on treatment); treatment-free interval difficult as off-treatment disease progression is rapid

## Connections

- `connects-to` → **[FH](../../03-molecular/fh/README.md)** — Germline FH mutations cause HLRCC (autosomal dominant); FH LOF → fumarate accumulation; 2SC IHC (anti-2-succino-cysteine) positive in FH-deficient tumors; FH IHC loss diagnostic; somatic second hit (LOH or second mutation) in each HLRCC leiomyoma or RCC
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — HLRCC-associated RCC driven by HIF-1α pseudohypoxia (FH LOF → PHD inhibition → HIF-1α stabilized); VEGF/HIF-1α pathway active; bevacizumab (anti-VEGF) + erlotinib standard for HLRCC RCC; HIF-2α inhibitor belzutifan being explored in FH-deficient RCC
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — HLRCC-associated RCC is pseudohypoxic similar to VHL-mutant ccRCC (both have HIF-1α and VEGF overexpression); histologically distinct (type 2B papillary/collecting duct-like, NOT clear cell); anti-VEGF therapies active in both; belzutifan explored in FH-deficient RCC
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — HLRCC-associated RCC: most aggressive hereditary RCC; collecting duct-like/papillary type 2B; often metastatic at diagnosis; FH IHC loss + 2SC positivity diagnostic; bevacizumab + erlotinib standard (NCI Phase 2, ORR ~64%, mPFS 21 months); sunitinib/pazopanib insufficient
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — HLRCC produces multiple smooth muscle tumors (leiomyomas): painful cutaneous nodules from arrector pili muscle and early-onset, large, multiple uterine fibroids; biallelic FH loss drives them, and FH-/2SC+ immunostaining distinguishes HLRCC leiomyomas from sporadic ones.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Fumarate accumulation stabilizes HIF-1α (pseudohypoxia) → VEGF transcription → tumor angiogenesis; this is the therapeutic handle in FH-deficient RCC — bevacizumab (anti-VEGF) plus erlotinib (anti-EGFR) achieves ~65% response, far exceeding VEGFR-TKIs like sunitinib.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — HLRCC causes the most aggressive hereditary kidney cancer — collecting-duct-like/type-2B papillary RCC that can metastasize even at 1-2 cm; radical (not partial) nephrectomy with lymphadenectomy is preferred, and annual renal MRI surveillance starts at genetic diagnosis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The uterus is often where HLRCC declares itself: women develop numerous, large, early-onset uterine leiomyomas (fibroids), frequently needing myomectomy or hysterectomy before age 30 — so multiple early fibroids with cutaneous leiomyomas should prompt FH testing.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous leiomyomas are the 'L' of HLRCC and its visible clue: firm, often painful skin-colored papules from arrector pili smooth muscle appearing in the 20s-30s; their recognition (with FH/2SC staining) flags the syndrome years before the aggressive kidney cancer.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — HLRCC's FH belongs to the same Krebs-cycle, pseudohypoxia family (SDHx, FH) that causes hereditary pheochromocytoma/paraganglioma: FH loss accumulates fumarate, inhibits HIF prolyl-hydroxylases, and stabilizes HIF — so rare FH-mutant PPGLs occur, sharing fumarate-driven biology.

[^tomlinson-2002-fh]: Tomlinson IP, Alam NA, Rowan AJ, et al. Germline mutations in FH predispose to dominantly inherited uterine fibroids, skin leiomyomata and papillary renal cell cancer. *Nat Genet.* 2002;30(4):406-410. [doi:10.1038/ng849](https://doi.org/10.1038/ng849) · [PubMed 11865300](https://pubmed.ncbi.nlm.nih.gov/11865300/)
[^linehan-2013-fh-review]: Linehan WM, Rouault TA. Molecular pathways: fumarate hydratase-deficient kidney cancer — targeting the Warburg effect in cancer. *Clin Cancer Res.* 2013;19(13):3345-3352. [doi:10.1158/1078-0432.CCR-13-0304](https://doi.org/10.1158/1078-0432.CCR-13-0304) · [PubMed 23836472](https://pubmed.ncbi.nlm.nih.gov/23836472/)
