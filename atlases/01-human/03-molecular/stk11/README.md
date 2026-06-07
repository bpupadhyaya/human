---
schema: human-scale-entry/v1
id: stk11
name: STK11
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "STK11 (LKB1) is a master serine/threonine kinase activating AMPK and 12 related kinases; LOF → mTOR hyperactivation + loss of STING innate immunity; germline STK11 = Peutz-Jeghers syndrome; somatic STK11 in KRAS-mutant NSCLC → immunotherapy resistance (cold tumor)."
aliases: ["STK11", "LKB1", "STK11 mutation", "STK11 NSCLC", "LKB1 NSCLC", "STK11 Peutz-Jeghers", "STK11 immunotherapy resistance", "LKB1 AMPK", "STK11 tumor suppressor", "STK11 KRAS NSCLC"]
sources:
  - id: shaw-2004-stk11-ampk
    type: peer-reviewed
    cite: "Shaw RJ, Kosmatka M, Bardeesy N, et al. The tumor suppressor LKB1 kinase directly activates AMP-activated kinase and regulates apoptosis in response to energy stress. Proc Natl Acad Sci USA. 2004;101(10):3329-3335."
    doi: "10.1073/pnas.0308061100"
    pmid: "14985505"
    url: "https://doi.org/10.1073/pnas.0308061100"
  - id: skoulidis-2018-stk11-nsclc
    type: peer-reviewed
    cite: "Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. Cancer Cell. 2018;34(3):412-424."
    doi: "10.1016/j.ccell.2018.08.013"
    pmid: "30174241"
    url: "https://doi.org/10.1016/j.ccell.2018.08.013"
cross_links:
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "STK11/LKB1 → AMPK (Thr172) → mTORC1 inhibition via raptor S792 → cell cycle arrest; LKB1-STRAD-MO25 ternary complex required for full AMPK activation; STK11 LOF → AMPK loss → mTOR hyperactivation; LKB1-AMPK-mTOR axis is the primary metabolic tumor suppressor pathway"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "STK11 → AMPK → raptor phosphorylation (S792) → mTORC1 inhibition; STK11 LOF → mTOR hyperactivation → S6K1, 4EBP1 → anabolic proliferation; STK11-mutant NSCLC: mTOR-dependent; rapalogues may have activity; KRAS + STK11 LOF co-mutation → dual MAPK+mTOR activation"
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "STK11 LOF + KRAS mutation defines the most immunotherapy-resistant NSCLC subgroup; KRAS-mutant NSCLC with STK11 LOF: STING suppressed → innate immunity lost → cold tumor; STK11+KRAS co-mutation accounts for ~15-20% of LUAD; adagrasib activity reduced in STK11-mutant NSCLC"
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "STK11 LOF → STING pathway suppression → reduced innate immune activation → PD-L1 not induced despite KRAS mutation → ICB resistance; pembrolizumab fails to overcome STK11 LOF in KRAS-mutant NSCLC; STK11 mutation is the strongest predictor of ICB failure in KRAS-mutant LUAD"
---

# STK11

## Overview

**STK11** (Serine/Threonine Kinase 11; also **LKB1**, Liver Kinase B1) encodes a 433-amino-acid (48 kDa) serine/threonine kinase that functions as the upstream master activator of the **AMPK family** — directly phosphorylating and activating AMPK (AMP-activated protein kinase) and 12 AMPK-related kinases (MARK1-4, SIK1-3, BRSK1/2, NUAK1/2). Through AMPK, STK11 is the primary kinase linking cellular energy sensing to mTOR suppression, cell polarity, and autophagy. STK11 is a classical tumor suppressor: germline pathogenic variants cause **Peutz-Jeghers syndrome (PJS)**, an autosomal dominant condition featuring GI hamartomatous polyps, mucocutaneous pigmentation, and markedly elevated cancer risks (breast, pancreatic, CRC). Somatic STK11 loss occurs in ~15-20% of lung adenocarcinoma (LUAD), where it is the strongest molecular predictor of **immune checkpoint blockade (ICB) resistance** in KRAS-mutant tumors — driven by suppression of the cGAS-STING innate immune pathway [^shaw-2004-stk11-ampk] [^skoulidis-2018-stk11-nsclc].

**STK11 alterations across tumor types:**

| Tumor type | Frequency | Clinical significance |
|---|---|---|
| Lung adenocarcinoma (LUAD) | ~15-20% | KRAS+STK11 = ICB-resistant; cold tumor; mTOR-driven |
| Cervical adenocarcinoma | ~20% | STK11 somatic; uncommon cervical adenoma malignum context |
| Pancreatic adenocarcinoma | ~5-10% | Co-mutation with KRAS; metabolic reprogramming |
| Peutz-Jeghers syndrome | ~94% (germline) | Hamartomatous polyps; elevated cancer risk across 8 sites |
| Breast cancer | ~5% | No clear targeted therapy; HER2-negative enriched |
| Colorectal cancer | ~5-8% | Mostly microsatellite stable; mTOR-driven subset |

**STK11 in NSCLC molecular subgroups (Skoulidis 2018):** [^skoulidis-2018-stk11-nsclc]

| KRAS-mutant LUAD subgroup | STK11 status | KEAP1 status | ICB response |
|---|---|---|---|
| KL (KRAS + STK11 LOF) | LOF | Intact | Low (ORR ~5-7%) |
| KP (KRAS + TP53 mutation) | Intact | Intact | Moderate (ORR ~15-25%) |
| KC (KRAS + CDKN2A/KEAP1) | Intact | LOF | Low-moderate |
| EMD biomarker (STK11+KEAP1+TP53) | — | — | Predicts ICB failure |

## Structure

### STK11 protein architecture

**N-terminal regulatory domain (aa 1~1-43):**
Kinase-independent regulatory region; proline-rich sequences; mediates interaction with LIP1 (LKB1-interacting protein 1) and 14-3-3 proteins; S31 phosphorylation by PKA (cAMP-dependent) → nuclear export → cytoplasmic LKB1-STRAD-MO25 complex formation; nuclear STK11 is kinase-inactive (STRAD is cytoplasmic)

**Catalytic kinase domain (aa 44~44-309):**
Serine/threonine kinase; activation loop phosphorylation at T183 (auto-phosphorylation with STRAD → full activation); STRAD (STE20-related pseudokinase) acts as allosteric activator: STRAD binds the C-lobe of STK11 kinase domain → induces active conformation → LKB1-STRAD-MO25 ternary complex; MO25 (mouse protein 25) stabilizes the STRAD-STK11 interaction; STK11 kinase domain directly contacts and phosphorylates AMPK α-subunit activation loop Thr172 — the rate-limiting step for AMPK activation

**C-terminal regulatory domain (aa 310-433):**
STK11 contains a C-terminal farnesylation/prenylation motif (CAAX box in some species; palmitoylation in human) → membrane anchoring; LKB1 interactions with HAD (haploinsufficiency-associated domain) proteins; mutations in C-terminal domain in PJS (especially exon 8 missense variants) affect protein stability and kinase activity; LKB1 is the only kinase in the AMPK superfamily known to require an obligate activating partner (STRAD-MO25)

### STK11 mutation patterns

**Germline PJS mutations:**
- Truncating (frameshift, nonsense, splice): ~70-80% of PJS pathogenic variants; protein absent or truncated; most severe functional consequence
- Missense: ~20-30%; predominantly in kinase domain; kinase-dead missense variants (D194A equivalent) are diagnostic; some missense variants have partial activity
- Large genomic deletions: ~5-10%; detected by MLPA; underdetected by NGS sequencing alone
- Genotype-phenotype: truncating mutations → higher cancer risk and more polyps than missense (Hearle 2006); however, significant intra-family variability

**Somatic NSCLC mutations:**
- Truncating: ~60% of somatic STK11 NSCLC mutations
- Homozygous deletion: ~15-20%; STK11 at chromosome 19p13.3; co-deletion with nearby tumor suppressors
- Loss of heterozygosity (LOH): ~20%; hemizygous LOF
- Missense: ~20-25% somatic; validated kinase-inactivating variants; TCGA lung cohort

## Function

### AMPK pathway activation by STK11

**LKB1-STRAD-MO25 ternary complex:**
In cytoplasm: STK11 (kinase) + STRAD-α/β (pseudokinase, no catalytic activity) + MO25-α/β (scaffold) → ternary complex; STRAD binding to STK11 C-lobe → active conformation; MO25 reinforces STRAD-STK11 contact; complex is constitutively active when assembled; no upstream kinase needed — STK11 is at the apex of the energy sensing cascade; LKB1 T183 auto-phosphorylation within complex completes activation [^shaw-2004-stk11-ampk]

**AMPK activation:**
STK11-STRAD-MO25 directly phosphorylates AMPK α-subunit Thr172 → AMPK fully activated; AMPK then: (1) phosphorylates raptor at S792 → mTORC1 dissociates → mTOR kinase separated from substrate-targeting raptor; (2) phosphorylates TSC2 (tuberous sclerosis complex 2) at T1462 → TSC1/2 complex activated → Rheb-GTPase inhibited → mTORC1 further inhibited; (3) phosphorylates ULK1 → autophagy initiation; (4) phosphorylates ACC1/2 (acetyl-CoA carboxylase) → fatty acid synthesis inhibited

**AMPK-related kinase cascade:**
STK11 also activates 12 AMPK-family kinases:
- MARK1/2/3/4 (microtubule affinity-regulating kinases): regulate microtubule dynamics, cell polarity, neuronal function; MARK phosphorylates Tau (important in neurodegeneration)
- SIK1/2/3 (salt-inducible kinases): phosphorylate CRTC2 (CREB-regulated transcription coactivator) → nuclear export → CREB-target gene suppression (gluconeogenesis, lipid metabolism)
- BRSK1/2 (brain-specific kinases): axon specification, neuronal polarity
- NUAK1/2: cell attachment, survival

**STK11 tumor suppressor functions:**
1. **mTOR suppression** (via AMPK): prevents nutrient-independent growth; starvation resistance
2. **Cell polarity**: STK11-MARK → LGL/PAR/Scribble polarity complex maintenance; STK11 LOF → loss of apical-basal polarity → epithelial-mesenchymal transition-like state
3. **Mitotic checkpoint**: STK11 required for spindle assembly checkpoint; STK11 LOF → chromosomal instability
4. **STING pathway**: STK11 required for cGAS-STING-TBK1-IRF3 innate immune signaling; STK11 LOF → STING suppression → loss of type I IFN → cold tumor

### STK11 LOF → immunotherapy resistance in NSCLC [^skoulidis-2018-stk11-nsclc]

**STING pathway suppression:**
Normally: cytosolic dsDNA (from replication stress, viral, or mitochondrial DNA) → cGAS → cGAMP → STING → TBK1 → IRF3 → type I IFN (IFN-α/β) → dendritic cell maturation → T cell priming → anti-tumor immunity; STK11/LKB1 LOF → STING expression suppressed transcriptionally → pathway inactive → no IFN-I production → cold tumor microenvironment (sparse TILs, low PD-L1, low MHC-I)

**Immunotherapy resistance mechanism:**
KRAS-mutant LUAD with STK11 LOF (the KL subgroup): PD-L1 expression LOW despite KRAS mutation (contrast: KRAS-only mutant tumors have moderate PD-L1); TIL density: very low (cold); ORR to pembrolizumab monotherapy: ~5-7% (vs ~25% in KRAS-mutant, STK11-intact tumors); mechanism: without STING, there is no IFN-I signal to upregulate PD-L1 or recruit T cells → pembrolizumab has no T cells to reinvigorate

**KRAS-STK11 combination therapy:**
- Adagrasib (KRAS G12C inhibitor): KRYSTAL-1 trial subgroup — STK11-mutant NSCLC showed lower ORR vs STK11-wildtype (~19% vs ~32%)
- Sotorasib + STK11 LOF: similar reduced ORR in STK11-mutant subgroup
- Proposed combinations: STING agonists + KRAS G12C inhibitor in STK11-mutant NSCLC (ongoing trials)
- mTOR inhibitors in STK11-mutant NSCLC: rationale for combination with KRAS inhibitor

## Mechanism

### Therapeutic strategies for STK11-mutant cancers

**Peutz-Jeghers syndrome:**
- mTOR inhibition: rapamycin reduces polyp burden in STK11+/- mice; sirolimus + metformin pilot study in PJS (NCT03943992): tolerable, modest polyp reduction
- Metformin (indirect AMPK activator via mitochondrial complex I inhibition): AMPK activation bypasses STK11 LOF (acts downstream); explored in PJS patients as polyp chemoprevention; clinical data limited
- Endoscopic polypectomy: mainstay of management; small bowel video capsule endoscopy annually; intraoperative enteroscopy for inaccessible polyps

**STK11-mutant NSCLC:**
- No FDA-approved STK11-targeted therapy
- STING agonists (ADU-S100, SR-717, diABZI): being tested in combination with ICB in STK11-mutant NSCLC; rationale: restore innate immunity that STK11 LOF has suppressed; Phase 1/2 combinations with pembrolizumab ongoing
- Chemotherapy: STK11-mutant NSCLC remains chemotherapy-sensitive (carboplatin/paclitaxel ± bevacizumab); pemetrexed + platinum for non-squamous; ICB + chemotherapy (carboplatin/paclitaxel/pembrolizumab) may partially overcome STK11 LOF
- CDK4/6 inhibitors: STK11 LOF + AMPK loss → CDKN2A downregulation → CDK4/6 hyperactivity; palbociclib explored in STK11-mutant NSCLC
- Everolimus (mTOR inhibitor): STK11 LOF → mTOR hyperactive; rapalogue + KRAS G12C inhibitor combination in preclinical development

## Connections

- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — STK11/LKB1 → AMPK (Thr172) → mTORC1 inhibition via raptor S792 → cell cycle arrest; LKB1-STRAD-MO25 ternary complex required for full AMPK activation; STK11 LOF → AMPK loss → mTOR hyperactivation; LKB1-AMPK-mTOR axis is the primary metabolic tumor suppressor pathway
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — STK11 → AMPK → raptor phosphorylation (S792) → mTORC1 inhibition; STK11 LOF → mTOR hyperactivation → S6K1, 4EBP1 → anabolic proliferation; STK11-mutant NSCLC: mTOR-dependent; rapalogues may have activity; KRAS + STK11 LOF co-mutation → dual MAPK+mTOR activation
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — STK11 LOF + KRAS mutation defines the most immunotherapy-resistant NSCLC subgroup; KRAS-mutant NSCLC with STK11 LOF: STING suppressed → innate immunity lost → cold tumor; STK11+KRAS co-mutation accounts for ~15-20% of LUAD; adagrasib activity reduced in STK11-mutant NSCLC
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — STK11 LOF → STING pathway suppression → reduced innate immune activation → PD-L1 not induced despite KRAS mutation → ICB resistance; pembrolizumab fails to overcome STK11 LOF in KRAS-mutant NSCLC; STK11 mutation is the strongest predictor of ICB failure in KRAS-mutant LUAD

[^shaw-2004-stk11-ampk]: Shaw RJ, Kosmatka M, Bardeesy N, et al. The tumor suppressor LKB1 kinase directly activates AMP-activated kinase and regulates apoptosis in response to energy stress. *Proc Natl Acad Sci USA.* 2004;101(10):3329-3335. [doi:10.1073/pnas.0308061100](https://doi.org/10.1073/pnas.0308061100) · [PubMed 14985505](https://pubmed.ncbi.nlm.nih.gov/14985505/)
[^skoulidis-2018-stk11-nsclc]: Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. *Cancer Cell.* 2018;34(3):412-424. [doi:10.1016/j.ccell.2018.08.013](https://doi.org/10.1016/j.ccell.2018.08.013) · [PubMed 30174241](https://pubmed.ncbi.nlm.nih.gov/30174241/)
