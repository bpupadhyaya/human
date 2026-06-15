---
schema: human-scale-entry/v1
id: lynch-syndrome
name: Lynch Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Lynch syndrome is the most common inherited cancer predisposition syndrome; germline MMR gene mutations (MLH1, MSH2, MSH6, PMS2) → MSI-H tumors; CRC lifetime risk ~40-80%; pembrolizumab/dostarlimab FDA-approved for dMMR tumors; universal tumor MMR testing recommended."
aliases: ["Lynch syndrome", "HNPCC", "hereditary nonpolyposis colorectal cancer", "MMR Lynch", "dMMR Lynch", "MLH1 Lynch", "MSH2 Lynch", "MSI-H Lynch", "Lynch colon cancer", "Lynch endometrial"]
sources:
  - id: bonadona-2011-lynch-risks
    type: peer-reviewed
    cite: "Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. JAMA. 2011;305(22):2304-2310."
    doi: "10.1001/jama.2011.743"
    pmid: "21642683"
    url: "https://doi.org/10.1001/jama.2011.743"
  - id: lynch-2015-lynch-review
    type: peer-reviewed
    cite: "Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. Nat Rev Cancer. 2015;15(3):181-194."
    doi: "10.1038/nrc3878"
    pmid: "25673086"
    url: "https://doi.org/10.1038/nrc3878"
cross_links:
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Germline MSH2 mutation causes ~31% of Lynch syndrome; MSH2 IHC loss indicates MSH2 or EPCAM mutation; MSH2-MSH6 (MutSα) detects base-base mismatches; MSH2 LOF → MSI-H → elevated TMB → immunotherapy sensitivity in Lynch tumors"
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "MLH1 germline mutation causes ~50% of Lynch syndrome; MLH1-PMS2 (MutLα) recruited by MutS complexes → MMR strand excision; MLH1 promoter methylation causes sporadic MSI-H CRC (not Lynch); MLH1 + PMS2 IHC co-loss indicates MLH1 mutation or methylation"
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "dMMR Lynch tumors are highly immunogenic → MSI-H → elevated TMB → PD-L1 high; pembrolizumab FDA-approved for dMMR/MSI-H solid tumors (KEYNOTE-158, 2020); dostarlimab for dMMR endometrial; Lynch tumors were the first tissue-agnostic immunotherapy indication"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Lynch CRC: most common Lynch-associated cancer; lifetime risk with MLH1/MSH2: ~40-80%; proximal colon predominance, mucinous histology, tumor-infiltrating lymphocytes; Lynch CRC has good prognosis; colonoscopy from age 25-30 recommended"
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Endometrial cancer is the second most common Lynch cancer and the sentinel tumor in many women (54% with MLH1); usually dMMR/MSI-H endometrioid; risk-reducing hysterectomy plus BSO after childbearing is offered, and dostarlimab (RUBY) is approved for advanced dMMR disease."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Lynch confers a ~13% lifetime gastric cancer risk (MLH1/MSH2) — the main hereditary cause of intestinal-type (not diffuse) gastric cancer; these dMMR/MSI-H tumors have high TIL density, contrasting with CDH1-driven diffuse HDGC; upper endoscopy is offered to carriers."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Colorectal mucosa is the highest-turnover epithelium, so its microsatellites accumulate the most replication errors when MMR fails — why CRC is the commonest Lynch cancer; Lynch CRC favors the proximal colon, is mucinous with brisk lymphocytic infiltrate, screened from age 20-25."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Lynch and juvenile polyposis are both dominant hereditary colorectal cancer syndromes but opposite: Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas, JPS is TGF-β/BMP loss making many hamartomatous polyps — repair defect versus stromal overgrowth."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Lynch and FAP are the two major hereditary colorectal cancer syndromes but differ starkly: FAP (germline APC) carpets the colon with thousands of adenomas and near-100% cancer risk, while Lynch (MMR genes) makes few polyps but fast MSI-high tumors via accelerated mutation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Lynch tumors are the prototype of immunotherapy response: mismatch-repair deficiency generates thousands of frameshift neoantigens that draw dense cytotoxic CD8+ T cells, so dMMR/MSI-H cancers respond strongly to anti-PD-1 — the basis of pembrolizumab's tissue-agnostic approval."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian cancer is part of the Lynch syndrome tumor spectrum: mismatch-repair deficiency raises the lifetime risk of (usually endometrioid or clear-cell) ovarian cancer alongside endometrial and colorectal cancer, so risk-reducing salpingo-oophorectomy is offered to carriers."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Lynch syndrome extends to the urinary tract: MSH2 carriers especially face raised risk of upper-tract urothelial carcinoma (renal pelvis, ureter) and bladder cancer, so urine surveillance is considered; these MSI-high tumors respond to checkpoint immunotherapy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Lynch syndrome cancers are the paradigm of immunotherapy-responsive tumors: mismatch-repair deficiency generates a high microsatellite-instability mutational load and abundant neoantigens, making MSI-high/dMMR tumors—wherever they arise—exquisitely sensitive to PD-1 blockade."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Pancreatic cancer is part of the Lynch spectrum: mismatch-repair deficiency raises pancreatic adenocarcinoma risk, and rare MMR-deficient pancreatic tumors are hypermutated and respond to checkpoint therapy—unlike most pancreatic cancers, which resist immunotherapy."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Cholangiocarcinoma belongs to the Lynch tumor spectrum: mismatch-repair loss predisposes to biliary-tract cancers, and like other Lynch tumors these are microsatellite-unstable and hypermutated—candidates for checkpoint immunotherapy exploiting their neoantigens."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Lynch syndrome can cause brain tumors as Turcot syndrome: mismatch-repair loss predisposes to gliomas including glioblastoma, and biallelic MMR deficiency gives childhood high-grade gliomas—linking a DNA-repair defect in the gut to tumors in the brain."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Lynch syndrome's Muir-Torre variant shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so a sebaceous skin tumor can be the first clue prompting Lynch testing and colon surveillance."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Lynch syndrome raises small-bowel cancer risk: mismatch-repair deficiency predisposes to small-intestinal adenocarcinoma—rare in the general population—so surveillance and a low threshold for investigating GI symptoms extend beyond the colon."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Lynch tumors still travel the Wnt road to cancer: mismatch-repair loss accelerates mutation, but colorectal carcinogenesis still typically requires Wnt/beta-catenin activation via APC—so MMR failure speeds, rather than replaces, the adenoma-carcinoma sequence."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Lynch syndrome predisposes across the digestive system: mismatch-repair loss most often causes colorectal cancer but also stomach, small-bowel, pancreatic and biliary tumors, so broad GI surveillance anchors management of the commonest hereditary cancer syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Lynch syndrome heavily affects the female reproductive system: endometrial cancer rivals colorectal as the most common Lynch tumor and is often the sentinel cancer, and ovarian cancer risk is raised too—so gynecologic surveillance and risk-reducing surgery matter."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The Muir-Torre variant of Lynch syndrome shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so these uncommon skin tumors can be the first clue prompting Lynch genetic testing."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Lynch syndrome reaches the urinary tract above the bladder: MMR deficiency raises the risk of urothelial cancer in the renal pelvis and ureter, so surveillance and any blood in the urine prompt imaging of the upper tracts, not just cystoscopy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Prostate cancer is a lower-penetrance Lynch tumor: MMR-gene carriers face a modestly increased, sometimes more aggressive prostate cancer, so family history of Lynch is weighed alongside PSA in deciding screening for these men."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Lynch tumors are immunotherapy-responsive because they are hypermutated: MMR loss spawns countless neoantigens that dendritic cells present to prime T cells, explaining why checkpoint blockade works so well in mismatch-repair-deficient cancers."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "A BRAF test separates Lynch from look-alike sporadic cancers: sporadic MSI-high colon tumors usually carry a BRAF V600E mutation, while Lynch tumors are BRAF-wild-type, so BRAF status is a key reflex test before diagnosing the inherited syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Lynch tumors' flood of mutations alerts NK cells: mismatch-repair failure makes hypermutated cells display stress signals and odd peptides that natural killer cells (and T cells) can attack—part of why these cancers are so immunotherapy-sensitive."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Lynch (MSI-high) tumors often form B-cell-rich lymphoid structures: clusters of B cells and tertiary lymphoid organs inside these hypermutated cancers help mount the immune response, and their presence predicts better checkpoint-therapy results."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Lynch tumors often knock out the TGF-beta brake: the mismatch-repair defect causes frameshift mutations in TGFBR2, a coding microsatellite, so the colorectal cancers escape TGF-beta's growth restraint—a signature lesion of MSI-high disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Lynch syndrome can reach the brain in its Turcot variant: mismatch-repair loss raises the risk of gliomas including glioblastoma, so brain tumors join the colorectal and endometrial cancers in the syndrome's spectrum."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Even Lynch's hot tumors recruit regulatory T cells: the hypermutated, neoantigen-rich cancers draw a strong immune response, but Tregs in the infiltrate restrain it—part of why checkpoint blockade, which lifts that brake, works so well here."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Lynch colorectal tumors bleed iron away: the cancer oozes blood into the gut, so an unexplained iron-deficiency anemia can be the first clue that prompts the colonoscopy which finds it."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Lynch cancers spring from the gut's epithelium: with mismatch repair broken, mutations pile up in the colonic and endometrial lining, so the epithelium turns malignant faster than in sporadic disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Lynch's hypermutated tumors draw macrophages: the neoantigen-rich cancers attract a dense immune infiltrate including macrophages, part of the inflamed microenvironment behind their strong response to immunotherapy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Lynch is managed by light: frequent colonoscopy from young adulthood catches and removes the fast-arising colorectal cancers, the surveillance that most reduces deaths in carriers."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Lynch raises gastric cancer risk: mismatch-repair-deficient stomach cancers occur, especially in MLH1 and MSH2 carriers, so upper endoscopy joins surveillance in high-incidence regions."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Lynch's Turcot variant strikes the brain: mismatch-repair loss raises the risk of gliomas, extending the syndrome's reach to the neurons of the central nervous system."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Lynch syndrome cannot proofread its DNA: losing a mismatch-repair gene lets tiny errors accumulate at repetitive sequences — microsatellite instability — so its tumors carry a huge mutation load that makes them strikingly responsive to immunotherapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Lynch reaches the liver and bile ducts: it raises the risk of cholangiocarcinoma, and its colorectal cancers spread there, so the liver is both a primary site and the commonest destination of its tumors."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Inheriting two faulty copies is far worse: constitutional mismatch-repair deficiency, the biallelic form, causes childhood leukemias and lymphomas, the marrow joining the syndrome's cancer spectrum in its most severe variant."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Mismatch-repair loss is read off the slide: an antibody panel staining for MLH1, MSH2, MSH6, and PMS2 by immunohistochemistry shows which protein has gone missing in the tumor, the first-line screen that flags Lynch before confirmatory germline sequencing."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Slow tumor bleeding shows up in the red cells: a Lynch colorectal or gastric cancer often declares itself first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic occult blood loss that should prompt early colonoscopy."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas falls within the spectrum: Lynch raises the lifetime risk of pancreatic cancer several-fold, and because such tumors are mismatch-repair-deficient and MSI-high, they are among the rare pancreatic cancers that can respond to checkpoint immunotherapy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Aspirin earns its place in Lynch through platelets: the CAPP2 trial showed daily aspirin sharply cuts colorectal cancer in carriers, an effect tied partly to blocking platelet COX-1 and the tumor-promoting signals activated platelets release."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Lynch tumors teem with immune cells: their mismatch-repair defect spawns countless neoantigens that draw in B cells and plasma cells forming tertiary lymphoid structures, a brisk immune response that underlies their striking sensitivity to checkpoint therapy."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "The mutation count runs high: mismatch-repair failure lets mutations accumulate across genes including KRAS, shaping the tumor's behavior and, with RAS status, guiding which targeted drugs can be added to its treatment."
---

# Lynch Syndrome

## Overview

**Lynch syndrome** (historically called hereditary nonpolyposis colorectal cancer, HNPCC) is the most common inherited cancer predisposition syndrome in adults, caused by germline pathogenic variants in the **DNA mismatch repair (MMR) genes**: **MLH1** (~50%), **MSH2** (~31%), **MSH6** (~13%), and **PMS2** (~6%), plus EPCAM 3' deletions that epigenetically silence MSH2 (~2%). Lynch syndrome confers markedly elevated lifetime risks for colorectal, endometrial, ovarian, gastric, urothelial, and other cancers. Lynch syndrome tumors are uniformly **deficient MMR (dMMR)** and **microsatellite instability-high (MSI-H)**, generating abundant frameshift neoantigens and constitutive PD-L1 expression — making Lynch tumors exquisitely sensitive to immune checkpoint blockade. Pembrolizumab (any dMMR/MSI-H solid tumor, 2020) and dostarlimab (dMMR endometrial, 2021) are FDA-approved, representing the first tissue-agnostic cancer therapy approval. Estimated prevalence: 1 in 280 individuals in the general population carry a Lynch syndrome pathogenic variant, most undiagnosed [^bonadona-2011-lynch-risks] [^lynch-2015-lynch-review].

**Epidemiology:**
- Prevalence: ~1/280 in general population; ~1/35-40 among all CRC patients; ~1/50-70 among all endometrial cancer patients
- Inheritance: autosomal dominant; 50% transmission rate per child of carrier; penetrance is incomplete and gene-specific
- Age of onset: CRC median age ~44-50 years (vs ~68 years sporadic); younger onset with MLH1/MSH2 vs MSH6/PMS2
- Proportion of CRC attributable to Lynch: ~3-5% of all CRC; ~10-15% of all early-onset CRC (< age 50)
- Proportion of endometrial cancer: ~3% of all endometrial cancer; higher in MSI-H endometrial (~25-30%)

**Gene-specific cancer risk summary (Bonadona 2011):** [^bonadona-2011-lynch-risks]

| Cancer | MLH1 (80 yr cumulative) | MSH2 (80 yr cumulative) | MSH6 | PMS2 |
|---|---|---|---|---|
| Colorectal | 41% | 48% | 10-22% | <15% |
| Endometrial | 54% | 21% | 16-26% | <15% |
| Ovarian | 20% | 24% | <1% | <1% |
| Gastric | 13% | 13% | <5% | <5% |
| Urothelial | ~4% | ~12% | <5% | <1% |
| Pancreatic | ~4% | ~5% | <3% | <1% |
| Brain (Turcot) | ~1-3% | ~1-2% | rare | rare |

## Structure

### MMR complex architecture in Lynch syndrome

**The four MMR proteins:**
- **MLH1**: obligate component of MutLα (MLH1-PMS2) and MutLβ (MLH1-PMS1) and MutLγ (MLH1-MLH3); MutLα is the primary repair-competent complex; PMS2 endonuclease nicks the daughter strand, enabling ExoI-mediated excision; MLH1 is the scaffold partner of all MutL complexes — MLH1 LOF eliminates all three
- **MSH2**: obligate scaffold for MutSα (MSH2-MSH6) and MutSβ (MSH2-MSH3); MutSα (base-base mismatches, +1 IDLs) and MutSβ (+2 to +8 IDLs) both require MSH2
- **MSH6**: mismatch-contacting subunit of MutSα; F432 Phe-loop directly contacts mispaired base; MSH6 protein is unstable without MSH2 → MSH2 LOF → MSH6 co-loss by IHC
- **PMS2**: endonuclease in MutLα; requires MLH1 for stability → PMS2 loss with MLH1 LOF; isolated PMS2 loss → PMS2 pathogenic variant

**MMR mechanism:**
1. Replication slippage at microsatellite → single base mismatch or IDL
2. MutSα/MutSβ binds mismatch → ATP-loaded sliding clamp
3. MutLα recruited via MSH2-MLH1 protein interaction
4. PCNA (RFC) → MutLα PMS2 endonuclease → nicks newly synthesized strand
5. Exonuclease I (ExoI) degrades from nick to mismatch
6. RPA + Polδ + PCNA → gap resynthesis → Ligase I sealing

**EPCAM deletion mechanism:**
EPCAM gene (2p21) is directly upstream of MSH2; 3' end deletions of EPCAM → abnormal transcriptional read-through → EPCAM-MSH2 fusion RNA → CpG island methylation of MSH2 promoter in epithelial tissues → MSH2 silencing; detected by MLPA or aCGH (not NGS sequencing); MSH2 and MSH6 IHC: both lost (same as germline MSH2 mutation)

### MSI and TMB in Lynch tumors

**Microsatellite instability:**
dMMR Lynch tumors accumulate frameshift mutations at coding microsatellite sequences (mononucleotide repeats in TGFBR2, MSH3, ACVR2, BAX, RIZ, and others) → truncated/non-functional proteins from these secondary "passenger" TSG hits; Bethesda panel (5 microsatellite loci): MSI-H = ≥2 unstable; modern NGS: MSI score computed from thousands of microsatellite loci simultaneously (tumor-only or matched) — more sensitive and specific

**TMB landscape:**
Lynch CRC: TMB ~50-100 mut/Mb; Lynch endometrial: TMB ~100-200 mut/Mb; neoantigen burden: hundreds to thousands of novel peptides from frameshift mutations → MHC-I/II presentation → T cell priming; TILs (tumor-infiltrating lymphocytes): marked lymphocytic infiltrate in Lynch CRC (Crohn-like reaction) → prognostic (better OS stage-for-stage vs MSS CRC); PD-L1 expression: IFN-γ from TILs → JAK-STAT → PD-L1 → adaptive immune resistance

## Function

### Carcinogenesis in Lynch syndrome

**Two-hit model:**
Lynch syndrome follows Knudson's two-hit tumor suppressor paradigm:
1. **First hit**: germline pathogenic variant (one allele non-functional at birth)
2. **Second hit**: somatic LOH (loss of heterozygosity), somatic mutation, or epigenetic silencing of the remaining wild-type allele → complete dMMR in tumor cell
- MLH1 promoter methylation on the remaining wild-type allele: ~30% of Lynch MLH1-mutant tumors acquire this as the second hit
- Somatic LOH at 2p21 (MSH2 locus) in Lynch MSH2 tumors
- Missense pathogenic variant + somatic frameshift = compound heterozygosity (rare second hit)

**Tumor type specificity:**
Lynch syndrome cancers predominantly arise from tissues with high MMR demand:
- Colorectal mucosa: highest replication rate of any epithelium → highest microsatellite mutation rate → CRC most frequent
- Endometrial glands: rapid hormonal cycling → high replication → second most common
- Gastric mucosa, urothelium: epithelial cycling
- Glioblastoma (Turcot variant, MLH1): brain tumors in Lynch — rare; MLH1 LOF → GBM-like tumor with MSI-H

**Lynch vs sporadic MSI-H:**
Important distinction:
- **Lynch MSI-H**: germline MMR gene mutation → constitutional dMMR → younger age at diagnosis; MMR IHC loss in normal colon crypts (if testing is performed)
- **Sporadic MSI-H**: MLH1 promoter methylation (somatic, both alleles) → acquired dMMR in that tumor only; MSH2 LOF almost never causes sporadic MSI-H; older age, predominantly right colon, BRAF V600E mutation (~50% sporadic MSI-H CRC); MLH1 methylation in sporadic MSI-H → MLH1/PMS2 IHC co-loss
- IHC pattern distinguishes:
  - MLH1 + PMS2 co-loss → reflexive MLH1 methylation PCR → if methylated = sporadic; if unmethylated = germline MLH1 or MSH2 variant (exceptional)
  - MSH2 + MSH6 co-loss → MSH2 or EPCAM germline (essentially never sporadic)
  - MSH6 loss alone → MSH6 germline; isolated PMS2 → PMS2 germline

## Pathology

### Diagnosis and universal tumor testing

**Universal MMR testing (recommended by NCCN, ACS, ASCCP):**
All newly diagnosed CRC and endometrial cancers should undergo MMR IHC (MLH1, PMS2, MSH2, MSH6) or tumor MSI testing; this identifies Lynch syndrome patients AND guides immunotherapy (dMMR/MSI-H → pembrolizumab first-line) and adjuvant therapy decisions (MSI-H stage II CRC: no 5-FU benefit); IHC more widely available; MSI PCR or NGS confirms

**Germline testing criteria:**
Individuals with dMMR/MSI-H tumor + age <50 (or proximal colon + positive family history) → germline MMR gene sequencing + deletion analysis (MLPA); Amsterdam II criteria: 3 relatives with Lynch-associated cancer, 2 successive generations, 1 patient <50 at diagnosis — now largely replaced by universal tumor testing as the trigger; Bethesda guidelines (revised) — similarly superseded by universal testing in guidelines

**Clinical genetic evaluation:**
- Probands: full MMR gene panel (MLH1, MSH2, MSH6, PMS2) + EPCAM deletion analysis
- First-degree relatives: cascade testing for identified variant
- Variant of uncertain significance (VUS): functional assay, co-segregation with disease in family, computational tools (align-GVGD, Bayesian methods)
- Pathogenic MMR variant confirmed → surveillance + prophylactic surgery discussion

### Treatment

**Surveillance protocols (NCCN):**
CRC surveillance:
- MLH1/MSH2 carriers: colonoscopy every 1-2 years from age 20-25
- MSH6 carriers: colonoscopy every 1-2 years from age 25-30
- PMS2 carriers: colonoscopy every 1-3 years from age 30-35

Endometrial/gynecologic:
- Annual endometrial sampling + TVUS from age 30-35
- Risk-reducing hysterectomy + bilateral salpingo-oophorectomy (RRBSO) after childbearing: reduces endometrial and ovarian cancer risk by ~85%; timing: ~35-40 years, after surveillance period
- RRBSO discussion: major quality-of-life implications (surgical menopause); individualized decision

Urothelial (especially MSH2):
- Annual urinalysis + urine cytology from age 25-30
- Cystoscopy: reserved for abnormal cytology or hematuria; no evidence for routine cystoscopy

**Chemoprevention:**
- **Aspirin**: CAPP2 trial (600 mg/day × 2 years): Lynch syndrome patients; 10-year follow-up: HR for CRC 0.63 (statistically significant at long-term follow-up); CRC incidence reduction ~50% for polypectomy interval cohort; mechanism: COX-2/prostaglandin pathway modulation; NCCN recommends aspirin discussion for Lynch syndrome CRC prevention
- Aspirin dose debate: ongoing CAPP3 trial compares 100 mg vs 300 mg vs 600 mg in Lynch; current recommendation based on 600 mg CAPP2 data

**Immunotherapy in Lynch tumors:**
First-line metastatic CRC (dMMR/MSI-H): [^lynch-2015-lynch-review]
- **KEYNOTE-177** (pembrolizumab vs FOLFOX/FOLFIRI ± bevacizumab): mPFS 16.5 vs 8.2 months (HR 0.60); OS HR 0.74; pembrolizumab first-line standard for dMMR/MSI-H mCRC since 2020
- **CheckMate 142** (nivolumab + ipilimumab): ORR 55%; mPFS 12.4 months; FDA-approved second-line dMMR/MSI-H mCRC
- **Any dMMR/MSI-H solid tumor** (KEYNOTE-158): pembrolizumab ORR 36% (range 20-57% across tumor types); FDA-approved June 2020 tissue-agnostic indication

Endometrial (dMMR):
- **RUBY Phase 3** (dostarlimab + carboplatin/paclitaxel): dMMR/MSI-H subgroup: PFS HR 0.28; FDA-approved November 2023 for first-line dMMR advanced endometrial cancer
- **KEYNOTE-868** (pembrolizumab + carboplatin/paclitaxel): similar benefit in dMMR advanced endometrial; FDA-approved 2023

**Adjuvant chemotherapy decisions:**
MSI-H stage II CRC: adjuvant 5-FU/leucovorin does NOT improve OS (may be harmful); mechanism: functional MMR required for 5-FU-induced mismatch-mediated apoptosis; MSS stage II CRC benefits from 5-FU; MSI-H stage III CRC: FOLFOX preferred (oxaliplatin mechanism is MMR-independent); important biomarker-directed adjuvant decision

**Prognosis:**
- Lynch CRC stage-for-stage: better 5-year OS than MSS CRC (Lynch ~15-20% OS advantage per stage); high TIL density → favorable immune microenvironment
- Lynch endometrial cancer: generally favorable (MSI-H endometrioid type); early-stage predominance
- MSI-H dMMR tumors: paradoxically best immunotherapy responders among all solid tumors

## Connections

- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — Germline MSH2 mutation causes ~31% of Lynch syndrome; MSH2 IHC loss indicates MSH2 or EPCAM mutation; MSH2-MSH6 (MutSα) detects base-base mismatches; MSH2 LOF → MSI-H → elevated TMB → immunotherapy sensitivity in Lynch tumors
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MLH1 germline mutation causes ~50% of Lynch syndrome; MLH1-PMS2 (MutLα) recruited by MutS complexes → MMR strand excision; MLH1 promoter methylation causes sporadic MSI-H CRC (not Lynch); MLH1 + PMS2 IHC co-loss indicates MLH1 mutation or methylation
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — dMMR Lynch tumors are highly immunogenic → MSI-H → elevated TMB → PD-L1 high; pembrolizumab FDA-approved for dMMR/MSI-H solid tumors (KEYNOTE-158, 2020); dostarlimab for dMMR endometrial; Lynch tumors were the first tissue-agnostic immunotherapy indication
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — Lynch CRC: most common Lynch-associated cancer; lifetime risk with MLH1/MSH2: ~40-80%; proximal colon predominance, mucinous histology, tumor-infiltrating lymphocytes; Lynch CRC has good prognosis; colonoscopy from age 25-30 recommended
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Endometrial cancer is the second most common Lynch cancer and the sentinel tumor in many women (54% with MLH1); usually dMMR/MSI-H endometrioid; risk-reducing hysterectomy plus BSO after childbearing is offered, and dostarlimab (RUBY) is approved for advanced dMMR disease.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Lynch confers a ~13% lifetime gastric cancer risk (MLH1/MSH2) — the main hereditary cause of intestinal-type (not diffuse) gastric cancer; these dMMR/MSI-H tumors have high TIL density, contrasting with CDH1-driven diffuse HDGC; upper endoscopy is offered to carriers.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Colorectal mucosa is the highest-turnover epithelium, so its microsatellites accumulate the most replication errors when MMR fails — why CRC is the commonest Lynch cancer; Lynch CRC favors the proximal colon, is mucinous with brisk lymphocytic infiltrate, screened from age 20-25.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Lynch and juvenile polyposis are both dominant hereditary colorectal cancer syndromes but opposite: Lynch is mismatch-repair deficiency making few MSI-high adenocarcinomas, JPS is TGF-β/BMP loss making many hamartomatous polyps — repair defect versus stromal overgrowth.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Lynch and FAP are the two major hereditary colorectal cancer syndromes but differ starkly: FAP (germline APC) carpets the colon with thousands of adenomas and near-100% cancer risk, while Lynch (MMR genes) makes few polyps but fast MSI-high tumors via accelerated mutation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Lynch tumors are the prototype of immunotherapy response: mismatch-repair deficiency generates thousands of frameshift neoantigens that draw dense cytotoxic CD8+ T cells, so dMMR/MSI-H cancers respond strongly to anti-PD-1 — the basis of pembrolizumab's tissue-agnostic approval.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Ovarian cancer is part of the Lynch syndrome tumor spectrum: mismatch-repair deficiency raises the lifetime risk of (usually endometrioid or clear-cell) ovarian cancer alongside endometrial and colorectal cancer, so risk-reducing salpingo-oophorectomy is offered to carriers.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Lynch syndrome extends to the urinary tract: MSH2 carriers especially face raised risk of upper-tract urothelial carcinoma (renal pelvis, ureter) and bladder cancer, so urine surveillance is considered; these MSI-high tumors respond to checkpoint immunotherapy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Lynch syndrome cancers are the paradigm of immunotherapy-responsive tumors: mismatch-repair deficiency generates a high microsatellite-instability mutational load and abundant neoantigens, making MSI-high/dMMR tumors—wherever they arise—exquisitely sensitive to PD-1 blockade.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Pancreatic cancer is part of the Lynch spectrum: mismatch-repair deficiency raises pancreatic adenocarcinoma risk, and rare MMR-deficient pancreatic tumors are hypermutated and respond to checkpoint therapy—unlike most pancreatic cancers, which resist immunotherapy.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Cholangiocarcinoma belongs to the Lynch tumor spectrum: mismatch-repair loss predisposes to biliary-tract cancers, and like other Lynch tumors these are microsatellite-unstable and hypermutated—candidates for checkpoint immunotherapy exploiting their neoantigens.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Lynch syndrome can cause brain tumors as Turcot syndrome: mismatch-repair loss predisposes to gliomas including glioblastoma, and biallelic MMR deficiency gives childhood high-grade gliomas—linking a DNA-repair defect in the gut to tumors in the brain.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Lynch syndrome's Muir-Torre variant shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so a sebaceous skin tumor can be the first clue prompting Lynch testing and colon surveillance.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Lynch syndrome raises small-bowel cancer risk: mismatch-repair deficiency predisposes to small-intestinal adenocarcinoma—rare in the general population—so surveillance and a low threshold for investigating GI symptoms extend beyond the colon.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Lynch tumors still travel the Wnt road to cancer: mismatch-repair loss accelerates mutation, but colorectal carcinogenesis still typically requires Wnt/beta-catenin activation via APC—so MMR failure speeds, rather than replaces, the adenoma-carcinoma sequence.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Lynch syndrome predisposes across the digestive system: mismatch-repair loss most often causes colorectal cancer but also stomach, small-bowel, pancreatic and biliary tumors, so broad GI surveillance anchors management of the commonest hereditary cancer syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Lynch syndrome heavily affects the female reproductive system: endometrial cancer rivals colorectal as the most common Lynch tumor and is often the sentinel cancer, and ovarian cancer risk is raised too—so gynecologic surveillance and risk-reducing surgery matter.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The Muir-Torre variant of Lynch syndrome shows in the skin: mismatch-repair loss produces sebaceous adenomas, sebaceous carcinomas and keratoacanthomas, so these uncommon skin tumors can be the first clue prompting Lynch genetic testing.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Lynch syndrome reaches the urinary tract above the bladder: MMR deficiency raises the risk of urothelial cancer in the renal pelvis and ureter, so surveillance and any blood in the urine prompt imaging of the upper tracts, not just cystoscopy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Prostate cancer is a lower-penetrance Lynch tumor: MMR-gene carriers face a modestly increased, sometimes more aggressive prostate cancer, so family history of Lynch is weighed alongside PSA in deciding screening for these men.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Lynch tumors are immunotherapy-responsive because they are hypermutated: MMR loss spawns countless neoantigens that dendritic cells present to prime T cells, explaining why checkpoint blockade works so well in mismatch-repair-deficient cancers.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — A BRAF test separates Lynch from look-alike sporadic cancers: sporadic MSI-high colon tumors usually carry a BRAF V600E mutation, while Lynch tumors are BRAF-wild-type, so BRAF status is a key reflex test before diagnosing the inherited syndrome.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Lynch tumors' flood of mutations alerts NK cells: mismatch-repair failure makes hypermutated cells display stress signals and odd peptides that natural killer cells (and T cells) can attack—part of why these cancers are so immunotherapy-sensitive.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Lynch (MSI-high) tumors often form B-cell-rich lymphoid structures: clusters of B cells and tertiary lymphoid organs inside these hypermutated cancers help mount the immune response, and their presence predicts better checkpoint-therapy results.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Lynch tumors often knock out the TGF-beta brake: the mismatch-repair defect causes frameshift mutations in TGFBR2, a coding microsatellite, so the colorectal cancers escape TGF-beta's growth restraint—a signature lesion of MSI-high disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Lynch syndrome can reach the brain in its Turcot variant: mismatch-repair loss raises the risk of gliomas including glioblastoma, so brain tumors join the colorectal and endometrial cancers in the syndrome's spectrum.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Even Lynch's hot tumors recruit regulatory T cells: the hypermutated, neoantigen-rich cancers draw a strong immune response, but Tregs in the infiltrate restrain it—part of why checkpoint blockade, which lifts that brake, works so well here.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Lynch colorectal tumors bleed iron away: the cancer oozes blood into the gut, so an unexplained iron-deficiency anemia can be the first clue that prompts the colonoscopy which finds it.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Lynch cancers spring from the gut's epithelium: with mismatch repair broken, mutations pile up in the colonic and endometrial lining, so the epithelium turns malignant faster than in sporadic disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Lynch's hypermutated tumors draw macrophages: the neoantigen-rich cancers attract a dense immune infiltrate including macrophages, part of the inflamed microenvironment behind their strong response to immunotherapy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Lynch is managed by light: frequent colonoscopy from young adulthood catches and removes the fast-arising colorectal cancers, the surveillance that most reduces deaths in carriers.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Lynch raises gastric cancer risk: mismatch-repair-deficient stomach cancers occur, especially in MLH1 and MSH2 carriers, so upper endoscopy joins surveillance in high-incidence regions.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Lynch's Turcot variant strikes the brain: mismatch-repair loss raises the risk of gliomas, extending the syndrome's reach to the neurons of the central nervous system.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Lynch syndrome cannot proofread its DNA: losing a mismatch-repair gene lets tiny errors accumulate at repetitive sequences — microsatellite instability — so its tumors carry a huge mutation load that makes them strikingly responsive to immunotherapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Lynch reaches the liver and bile ducts: it raises the risk of cholangiocarcinoma, and its colorectal cancers spread there, so the liver is both a primary site and the commonest destination of its tumors.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Inheriting two faulty copies is far worse: constitutional mismatch-repair deficiency, the biallelic form, causes childhood leukemias and lymphomas, the marrow joining the syndrome's cancer spectrum in its most severe variant.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Mismatch-repair loss is read off the slide: an antibody panel staining for MLH1, MSH2, MSH6, and PMS2 by immunohistochemistry shows which protein has gone missing in the tumor, the first-line screen that flags Lynch before confirmatory germline sequencing.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Slow tumor bleeding shows up in the red cells: a Lynch colorectal or gastric cancer often declares itself first as unexplained microcytic anemia, the pale, undersized erythrocytes of chronic occult blood loss that should prompt early colonoscopy.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas falls within the spectrum: Lynch raises the lifetime risk of pancreatic cancer several-fold, and because such tumors are mismatch-repair-deficient and MSI-high, they are among the rare pancreatic cancers that can respond to checkpoint immunotherapy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Aspirin earns its place in Lynch through platelets: the CAPP2 trial showed daily aspirin sharply cuts colorectal cancer in carriers, an effect tied partly to blocking platelet COX-1 and the tumor-promoting signals activated platelets release.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Lynch tumors teem with immune cells: their mismatch-repair defect spawns countless neoantigens that draw in B cells and plasma cells forming tertiary lymphoid structures, a brisk immune response that underlies their striking sensitivity to checkpoint therapy.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — The mutation count runs high: mismatch-repair failure lets mutations accumulate across genes including KRAS, shaping the tumor's behavior and, with RAS status, guiding which targeted drugs can be added to its treatment.

[^bonadona-2011-lynch-risks]: Bonadona V, Bonaïti B, Olschwang S, et al. Cancer risks associated with germline mutations in MLH1, MSH2, and MSH6 genes in Lynch syndrome. *JAMA.* 2011;305(22):2304-2310. [doi:10.1001/jama.2011.743](https://doi.org/10.1001/jama.2011.743) · [PubMed 21642683](https://pubmed.ncbi.nlm.nih.gov/21642683/)
[^lynch-2015-lynch-review]: Lynch HT, Snyder CL, Shaw TG, et al. Milestones of Lynch syndrome: 1895-2015. *Nat Rev Cancer.* 2015;15(3):181-194. [doi:10.1038/nrc3878](https://doi.org/10.1038/nrc3878) · [PubMed 25673086](https://pubmed.ncbi.nlm.nih.gov/25673086/)
