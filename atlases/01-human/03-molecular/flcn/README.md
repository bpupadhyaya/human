---
schema: human-scale-entry/v1
id: flcn
name: FLCN
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "FLCN (folliculin) forms the FLCN-FNIP complex acting as a GAP for RagC/D GTPases on lysosomes to regulate mTORC1 amino acid sensing; LOF → mTOR dysregulation and mitochondrial biogenesis; germline FLCN = Birt-Hogg-Dubé syndrome; chromophobe and hybrid oncocytic RCC."
aliases: ["FLCN", "folliculin", "FLCN mutation", "FLCN BHD", "folliculin Birt-Hogg-Dubé", "FLCN RCC", "FLCN mTOR", "FNIP FLCN", "FLCN chromophobe", "BHD folliculin"]
sources:
  - id: nickerson-2002-flcn-bhd
    type: peer-reviewed
    cite: "Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. Cancer Cell. 2002;2(2):157-164."
    doi: "10.1016/s1535-6108(02)00104-6"
    pmid: "12204536"
    url: "https://doi.org/10.1016/s1535-6108(02)00104-6"
  - id: tsun-2013-flcn-rag
    type: peer-reviewed
    cite: "Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. Mol Cell. 2013;52(4):495-505."
    doi: "10.1016/j.molcel.2013.09.016"
    pmid: "24095279"
    url: "https://doi.org/10.1016/j.molcel.2013.09.016"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "FLCN-FNIP is a GAP for RagC/D → promotes amino acid-stimulated mTORC1 lysosomal recruitment; FLCN LOF → impaired Rag GTPase function → mTORC1 dysregulation; BHD-associated RCC often shows mTORC1 hyperactivation via feedback; everolimus explored in BHD-associated RCC"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "FNIP1/FNIP2 (FLCN-interacting proteins) co-bind AMPK β-subunit; FLCN-FNIP-AMPK complex links folliculin to energy sensing; FLCN LOF → altered AMPK activity; AMPK-FLCN axis controls energy sensing at the lysosome; metformin explored in FLCN-deficient RCC"
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "VHL LOF (ccRCC) and FLCN LOF (chromophobe/hybrid RCC) cause hereditary RCC by distinct mechanisms; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD-associated RCC is NOT HIF-1α-driven unlike VHL ccRCC; chromophobe RCC has distinct perinuclear halo histology"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "BHD-associated RCC: chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%"
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "STK11-AMPK and FLCN-FNIP-AMPK are parallel tumor suppressor pathways converging on mTORC1; both link energy sensing (AMPK) to growth suppression via mTOR; STK11 LOF (Peutz-Jeghers) and FLCN LOF (BHD) cause distinct hereditary tumor syndromes both exploitable with mTOR inhibitors."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "FLCN-deficient BHD RCC is not HIF-1α-driven unlike VHL ccRCC; FLCN LOF → mTOR/4EBP1 → HIF-2α translation → partial HIF activity; belzutifan (HIF-2α inhibitor, FDA for VHL) explored in BHD chromophobe RCC; HIF-1α and HIF-2α share some but not all transcriptional targets."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT and FLCN-FNIP-AMPK converge on mTORC1: AKT → TSC2 Ser939 → Rheb-GTP → mTOR on; AMPK → TSC2 Ser1387 → Rheb-GDP → mTOR off; FLCN modulates the RagC/D arm; in BHD RCC, PI3K/AKT inhibitors complement mTOR inhibitors; AKT S473 is elevated in FLCN-deficient RCC cell lines."
---

# FLCN

## Overview

**FLCN** (folliculin) encodes a 579-amino-acid (~68 kDa) protein with no strong homology to previously characterized protein families, but with a C-terminal **DENN/MADD-like domain** that confers **GTPase-activating protein (GAP) activity** toward the **RagC and RagD GTPases** on the lysosomal surface — key components of the amino acid sensing pathway that recruits and activates mTORC1. FLCN forms a stable complex with **FNIP1** (folliculin-interacting protein 1) and **FNIP2** (folliculin-interacting protein 2), which serve as adaptor proteins; FNIP1/2 independently bind the β-subunit of **AMPK** (AMP-activated protein kinase), linking FLCN to the cellular energy sensing apparatus. FLCN is a classical tumor suppressor: biallelic inactivation of FLCN causes loss of Rag GTPase regulation on lysosomes and dysregulation of mTORC1, mTORC2, and **TFE3/TFEB** transcription factors (master regulators of lysosomal biogenesis and autophagy). Germline pathogenic variants in FLCN cause **Birt-Hogg-Dubé (BHD) syndrome**, characterized by cutaneous fibrofolliculomas, pulmonary cysts (spontaneous pneumothorax), and bilateral multifocal kidney tumors with chromophobe and hybrid oncocytic histology [^nickerson-2002-flcn-bhd] [^tsun-2013-flcn-rag].

**FLCN in cancer and disease:**

| Context | Frequency | Notes |
|---|---|---|
| BHD syndrome (germline) | ~100% of FLCN-positive BHD families | Autosomal dominant; fibrofolliculoma + pulmonary cyst + RCC |
| Chromophobe RCC (sporadic) | ~20-25% somatic | FLCN LOF; same histology as BHD-associated RCC |
| Hybrid oncocytic/chromophobe RCC | ~30% | Sporadic; FLCN LOF frequent |
| Clear cell RCC (sporadic) | ~2-5% | Less common; FLCN LOF in rare ccRCC |
| Pancreatic cancer | ~1-2% | Very rare somatic FLCN LOF |

## Structure

### FLCN protein architecture

**N-terminal domain (aa 1-~300; longin-like domain):**
Longin domain fold (DENN domain N-lobe); binds FNIP1 and FNIP2 (N-terminal and C-terminal FNIP segments); FLCN homodimerizes via this region; longin domains are found in SNAREs and regulators of vesicular trafficking; FLCN N-terminal domain participates in lysosomal membrane anchoring via interaction with LAMTOR complex; pathogenic missense variants in this region disrupt FNIP binding → loss of complex formation

**C-terminal domain (aa ~300-579; DENN/MADD-like):**
RagC/D-specific GAP activity; catalytic arginine finger (R527) accelerates RagC/D GTPase activity → RagC/D-GDP; RagC/D-GDP is the mTOR-activating Rag configuration (RagA/B-GTP + RagC/D-GDP = mTORC1 recruited to lysosome); FLCN acts as a "RagC/D inactivator" to set RagC/D into the GDP state appropriate for mTOR activation; FLCN LOF → RagC/D remains GTP-loaded → impaired Rag signaling → altered mTORC1 lysosomal docking; FLCN C-terminal missense variants are often functionally null

**FNIP1/FNIP2 scaffold:**
FNIP1 (1166 aa) and FNIP2 (1170 aa) are paralogs; both bridge FLCN and AMPK (via FNIP β-subunit binding region at C-terminal residues 1050-1166); FNIP1/2 are not directly GAP-active; they scaffold the ternary FLCN-FNIP-AMPK complex that responds to energy status; AMPK-phosphorylated FNIP1 (at Ser938/S948) modulates FLCN-FNIP complex localization

### FLCN mutation patterns

**Germline BHD mutations:**
- Frameshift insertions/deletions in coding microsatellites (especially poly-C tracts in exons 5, 6, 11): ~50% of BHD germline pathogenic variants; particularly intragenic repeat c.1285dupC (exon 11) is the most common single mutation in BHD
- Truncating (nonsense, splice-site): ~30%
- Missense: ~10-15%; functional impact variable; pathogenic missense targets the RagGAP domain
- Large deletions: ~5-10%; MLPA required
- De novo mutations: ~10% of BHD families
- Mosaicism: ~5% of BHD patients without identifiable germline variant; somatic mosaicism

**Second hit in BHD tumors:**
Biallelic FLCN LOF required in each kidney tumor: somatic LOH at 17p11.2 (~70% of BHD RCC) or somatic truncating mutation of the second allele; fibrofolliculomas in BHD skin: also show second-hit LOH; pulmonary cysts in BHD: FLCN second hit found in some cyst-lining cells; not all cyst cells are FLCN-deficient (heterogeneous)

## Function

### FLCN-FNIP-AMPK complex and the Rag GTPase-mTORC1 axis

**Rag GTPase amino acid sensing:** [^tsun-2013-flcn-rag]
At the lysosomal surface: the Ragulator complex (LAMTOR1-5) anchors RagA/B-RagC/D heterodimers; amino acid sufficiency signal → RagA/B loaded with GTP + RagC/D loaded with GDP = mTORC1-activating configuration; RagA/B-GTP recruits mTOR (via RAPTOR/mTORC1 association) to the lysosomal surface where Rheb (TSC1/TSC2 substrate) activates mTOR catalysis; the two Rag GTPases act in opposition: RagA/B-GTP and RagC/D-GDP both required

**FLCN as RagC/D GAP:**
FLCN DENN domain GAP activity: accelerates RagC/D GTP hydrolysis (RagC/D-GTP → RagC/D-GDP); when amino acids are present, Ragulator activates FLCN → FLCN converts RagC/D-GTP → RagC/D-GDP → mTOR-activating Rag configuration → mTORC1 recruited to lysosome → activated; FLCN LOF → RagC/D remains GTP-loaded (constitutively non-signaling configuration) → paradoxically, impairs amino acid stimulation of mTORC1 in isolation; however, in BHD RCC cells, other mTOR activating signals (RTKs, AKT, ERK) predominate → mTORC1 still hyperactive in net; the FLCN loss also activates TFE3/TFEB (see below)

**TFE3/TFEB nuclear translocation:**
FLCN LOF → RagC/D cannot inactivate RagA/B → mTORC1 not fully lysosomal → reduced mTORC1-mediated phosphorylation of TFE3/TFEB → TFE3/TFEB escapes 14-3-3 sequestration → nuclear translocation → lysosomal biogenesis and autophagy gene upregulation; nuclear TFE3 is a hallmark of FLCN-deficient RCC (IHC: nuclear TFE3 staining in BHD-associated chromophobe RCC and sporadic FLCN-deficient RCC)

**AMPK connection:**
FNIP1/2 bind AMPK β-subunit → FLCN-FNIP is physically associated with AMPK at the lysosome; when cellular energy is low (AMP:ATP ratio high) → AMPK activated → AMPK phosphorylates FNIP1 → FLCN-FNIP complex relocalized → FLCN RagC/D-GAP activity modulated; this connects AMPK (energy sensor) to mTOR (growth sensor) via FLCN-FNIP at the lysosomal surface, acting in parallel to the STK11-AMPK-TSC2 pathway

### FLCN LOF in kidney tumorigenesis

**Chromophobe RCC specificity:**
BHD-associated RCC is predominantly chromophobe (~50%) and hybrid oncocytic (~33%), with rare clear cell (~5%) and papillary (<5%); chromophobe RCC arises from the collecting duct intercalated cell lineage (type B); FLCN LOF in intercalated cells → mTOR dysregulation + mitochondrial accumulation (TFE3-driven mitochondrial biogenesis) → oncocytic morphology; this explains why FLCN LOF produces chromophobe/oncocytic tumors rather than clear cell (which is VHL/HIF-1α-driven in proximal tubular cells)

**Mitochondrial biogenesis:**
FLCN LOF → TFE3 nuclear → PGC-1α and TFAM upregulation → mitochondrial biogenesis → mitochondrial mass accumulation → oncocytic granular cytoplasm (dense mitochondria = eosinophilic granular cytoplasm on H&E); the oncocytic appearance of BHD-associated hybrid tumors reflects FLCN's role in mitochondrial metabolism regulation

**Histology of BHD-associated RCC:**
- **Chromophobe RCC**: large cells with abundant pale cytoplasm + perinuclear halo (condensed mitochondria) + raisinoid hyperchromatic nuclei; Hale's colloidal iron stain: diffuse cytoplasmic positivity; IHC: CK7++, CD117+, parvalbumin+, CAIX−, CD10−, RCC marker−
- **Hybrid oncocytic/chromophobe RCC**: features of both chromophobe and oncocytoma; oncocytic foci + chromophobe foci; IHC: mixed; may be FLCN-deficient
- **Renal oncocytoma**: mahogany-brown, homogeneous; mitochondria-packed cells; IHC: CD117+, CK7 focal; generally benign; FLCN LOF found in ~25% of sporadic oncocytoma → relationship with BHD

## Mechanism

### Therapeutic implications of FLCN loss

**mTOR inhibitors in BHD-associated RCC:**
- Everolimus (mTOR inhibitor): theoretical rationale (FLCN LOF → mTOR dysregulation); small case series show activity in metastatic BHD-associated RCC; no Phase 3 data; being explored in BHD-specific registry trials
- Temsirolimus: less commonly used; similar mechanism
- Limitation: FLCN LOF mTOR dysregulation is more complex than TSC1/2 LOF (Rheb pathway); rapalogue response in FLCN-deficient tumors is incomplete

**VEGFR-TKIs in metastatic BHD RCC:**
- Sunitinib, pazopanib, cabozantinib: VEGFR-TKIs; used for metastatic chromophobe RCC (BHD or sporadic); chromophobe RCC is less VEGF-driven than ccRCC → lower ORR (~5-10% vs ~30% in ccRCC); cabozantinib (VEGFR+MET+AXL) has better activity than sunitinib in non-ccRCC
- Checkpoint inhibitors: nivolumab + ipilimumab explored in BHD RCC; limited data; chromophobe RCC is TMB-low and PD-L1-low → less ICB responsive than ccRCC

**Belzutifan (HIF-2α inhibitor):**
- FDA-approved for VHL-associated ccRCC; being explored in FLCN-deficient chromophobe RCC (BHD and sporadic); rationale: FLCN LOF in some tumors activates HIF-2α via mTOR/4EBP1; early-phase data for belzutifan in chromophobe RCC (BHD: NCT04924075); mechanism is distinct from VHL-associated HIF-2α activation

**Nephron-sparing approach in BHD:**
Given bilateral, multifocal RCC in BHD, nephron preservation is critical — lifelong kidney function must be maintained as new tumors will emerge on both sides; active surveillance until tumor reaches 3 cm threshold; then partial nephrectomy or thermal ablation (radiofrequency/cryoablation) rather than radical nephrectomy; lifetime monitoring with annual MRI alternating with US every 6 months

## Connections

- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — FLCN-FNIP is a GAP for RagC/D → promotes amino acid-stimulated mTORC1 lysosomal recruitment; FLCN LOF → impaired Rag GTPase function → mTORC1 dysregulation; BHD-associated RCC often shows mTORC1 hyperactivation via feedback; everolimus explored in BHD-associated RCC
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — FNIP1/FNIP2 (FLCN-interacting proteins) co-bind AMPK β-subunit; FLCN-FNIP-AMPK complex links folliculin to energy sensing; FLCN LOF → altered AMPK activity; AMPK-FLCN axis controls energy sensing at the lysosome; metformin explored in FLCN-deficient RCC
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — VHL LOF (ccRCC) and FLCN LOF (chromophobe/hybrid RCC) cause hereditary RCC by distinct mechanisms; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD-associated RCC is NOT HIF-1α-driven unlike VHL ccRCC; chromophobe RCC has distinct perinuclear halo histology
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — BHD-associated RCC: chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%
- `connects-to` → **[STK11](../stk11/README.md)** — STK11-AMPK and FLCN-FNIP-AMPK are parallel tumor suppressor pathways converging on mTORC1; both link energy sensing (AMPK) to growth suppression via mTOR; STK11 LOF (Peutz-Jeghers) and FLCN LOF (BHD) cause distinct hereditary tumor syndromes both exploitable with mTOR inhibitors.
- `connects-to` → **[HIF-1α](../hif-1alpha/README.md)** — FLCN-deficient BHD RCC is not HIF-1α-driven unlike VHL ccRCC; FLCN LOF → mTOR/4EBP1 → HIF-2α translation → partial HIF activity; belzutifan (HIF-2α inhibitor, FDA for VHL) explored in BHD chromophobe RCC; HIF-1α and HIF-2α share some but not all transcriptional targets.
- `connects-to` → **[Akt](../akt/README.md)** — AKT and FLCN-FNIP-AMPK converge on mTORC1: AKT → TSC2 Ser939 → Rheb-GTP → mTOR on; AMPK → TSC2 Ser1387 → Rheb-GDP → mTOR off; FLCN modulates the RagC/D arm; in BHD RCC, PI3K/AKT inhibitors complement mTOR inhibitors; AKT S473 is elevated in FLCN-deficient RCC cell lines.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nickerson-2002-flcn-bhd]: Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. *Cancer Cell.* 2002;2(2):157-164. [doi:10.1016/s1535-6108(02)00104-6](https://doi.org/10.1016/s1535-6108(02)00104-6) · [PubMed 12204536](https://pubmed.ncbi.nlm.nih.gov/12204536/)
[^tsun-2013-flcn-rag]: Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. *Mol Cell.* 2013;52(4):495-505. [doi:10.1016/j.molcel.2013.09.016](https://doi.org/10.1016/j.molcel.2013.09.016) · [PubMed 24095279](https://pubmed.ncbi.nlm.nih.gov/24095279/)
