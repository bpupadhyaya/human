---
schema: human-scale-entry/v1
id: cccdna
name: cccDNA
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "HBV cccDNA (covalently closed circular DNA; 3.2 kb) forms in hepatocyte nucleus as a minichromosome; template for all HBV RNAs; persists decades; not cleared by NRTIs; HBx transactivates cccDNA; cGAS senses HBV DNA; curative therapy requires cccDNA elimination."
aliases: ["cccDNA", "covalently closed circular DNA", "HBV cccDNA", "HBV minichromosome", "HBV nuclear reservoir", "HBV persistence", "HBV epigenome", "hepatitis B cccDNA"]
sources:
  - id: nassal-2015-cccdna-review
    type: peer-reviewed
    cite: "Nassal M. HBV cccDNA: viral persistence reservoir and key obstacle for a cure of chronic hepatitis B. Gut. 2015;64(12):1972-1984."
    doi: "10.1136/gutjnl-2015-309809"
    pmid: "26048673"
    url: "https://doi.org/10.1136/gutjnl-2015-309809"
    accessed: "2026-06-08"
  - id: levrero-2009-cccdna-minichromosome
    type: peer-reviewed
    cite: "Levrero M, Pollicino T, Petersen J, Belloni L, Raimondo G, Dandri M. Control of cccDNA function in hepatitis B virus infection. J Hepatol. 2009;51(3):581-592."
    doi: "10.1016/j.jhep.2009.05.022"
    pmid: "19616344"
    url: "https://doi.org/10.1016/j.jhep.2009.05.022"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HBV cccDNA is the nuclear replication reservoir driving chronicity; formed from RC-DNA by host enzymes → chromatinized minichromosome; transcribes pgRNA, preC, and subgenomic RNAs; not cleared by NRTIs; elimination is the definition of functional cure."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HBV RC-DNA and cccDNA activate cGAS → STING → IFN-β; HBx binds and inhibits STING → suppresses innate sensing of cccDNA; APOBEC3A/3B deaminate cccDNA → cGAS recognition; cGAS-STING agonists are investigated as curative approaches to eliminate cccDNA-containing hepatocytes."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HBx binds p53 DNA-binding domain → prevents PUMA/BAX transcription → HBV-infected hepatocytes resist apoptosis; HBV integration generates HBx-p53 chimeric proteins; TP53 R249S hotspot (aflatoxin B1) is characteristic of HBV-HCC; p53 LOF enables cccDNA hepatocyte survival."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "HBx activates Wnt/β-catenin by inhibiting GSK-3β → nuclear β-catenin → MYC/CCND1; HBV integration near TERT promoter activates telomerase; CTNNB1 activating mutations in ~25% of HBV-HCC; β-catenin/TCF enhances cccDNA transcription in infected hepatocytes."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "HBV pgRNA reverse transcription generates dsRNA intermediates → RIG-I/MDA5 → MAVS → IFN-β; HBV evades MAVS by confining replication to nucleocapsid; HBx inhibits MAVS-dependent signaling; low MAVS activation during chronic HBV contributes to T cell exhaustion."
---

# cccDNA

## Overview

**cccDNA** (covalently closed circular DNA) is the **episomal nuclear reservoir** of hepatitis B virus (HBV) in infected hepatocytes. Upon HBV infection, the incoming relaxed circular DNA (RC-DNA) genome is converted by host DNA repair machinery into a supercoiled, protein-free cccDNA molecule (~3.2 kb) in the hepatocyte nucleus [^nassal-2015-cccdna-review]. This cccDNA then becomes a **chromatinized minichromosome**, wrapped around histone octamers and decorated with transcription factor binding sites, from which all HBV RNA transcripts — including the pregenomic RNA (pgRNA), the HBeAg precursor, and subgenomic RNAs for HBsAg and HBx — are transcribed by the host RNA polymerase II.

The central biological challenge of HBV is that **cccDNA is not a target of nucleoside reverse transcriptase inhibitors (NRTIs)** — the backbone of current antiviral therapy. Tenofovir and entecavir suppress HBV DNA to undetectable levels by inhibiting the viral reverse transcriptase, preventing new RC-DNA synthesis. But established cccDNA is entirely unaffected: it persists in hepatocyte nuclei for months to years, serving as a template the moment antiviral pressure is removed. This is why HBV therapy is lifelong in most patients, and why **cccDNA elimination is the molecular definition of functional cure** [^levrero-2009-cccdna-minichromosome].

Approximately **5–50 cccDNA copies** exist per hepatocyte in chronic HBV infection. The pool is stable in quiescent hepatocytes (no cell division to dilute episomal copies), and each nuclear recycling of a newly formed nucleocapsid replenishes it. In rapidly dividing hepatocytes (e.g., regeneration after liver injury), cccDNA can be diluted and partially lost — but under normal conditions it persists indefinitely.

## Structure

### Molecular architecture of cccDNA

**From RC-DNA to cccDNA** — a host-enzyme-dependent repair process:

1. **Nucleocapsid → nuclear pore**: Nucleocapsid with RC-DNA traffics to nuclear pore complex; RC-DNA is delivered to the nucleus while the capsid remains at the cytoplasmic face
2. **(-) strand nicking repair**: Topoisomerase I (TOP1) nicks the 5′ end of the (-) strand; the covalently attached terminal protein (Pol) is removed — this requires ATAD5 (RFC-like complex) and TDP2 (tyrosyl-DNA phosphodiesterase 2) to cleave the tyrosyl-phosphate bond
3. **(+) strand completion**: PCNA-associated DNA polymerase δ fills the incomplete (+) strand gap; RNase H activity (cellular) removes the 5′ RNA cap and internal RNA primer on the (+) strand
4. **Ligation**: DNA ligase I or III seals the remaining nicks → covalently closed circular DNA
5. **Supercoiling**: Topoisomerase II introduces negative supercoils → cccDNA
6. **Chromatinization**: Histone octamers (H2A, H2B, H3, H4) assemble on cccDNA within minutes; histone H3.3 is enriched; HELLS (SMARCA6 chromatin remodeler) and DNMT3a facilitate nucleosome positioning

### cccDNA as a minichromosome

Once formed, cccDNA behaves as a cellular episome:
- **Length**: ~3.2 kb; ~3.3 nucleosomes/kilobase → approximately 10-11 nucleosomes total
- **Transcription factor binding sites**: Multiple binding motifs for CREB, C/EBPα, NF-κB, AP-1, HNF4α, RXRα → hijacks hepatocyte transcriptional machinery
- **HBx requirement**: HBx protein is required for productive cccDNA transcription; HBx degrades the Smc5/6 SMC complex that otherwise restricts cccDNA transcription — this is the principal mechanism by which HBx enables cccDNA to function as a viral transcription template within the nucleus

### Transcripts from cccDNA

| Transcript | Size | Product | Function |
|-----------|------|---------|---------|
| pgRNA | 3.5 kb | HBcAg + Pol | Template for reverse transcription; encapsidated with Pol |
| preC RNA | 3.5 kb | HBeAg | Secreted immunomodulatory protein; 5′ preC leader → ER signal |
| 2.4 kb | L-HBsAg | Large surface antigen (preS1+preS2+S) |
| 2.1 kb | M/S-HBsAg | Medium and small surface antigens |
| 0.7 kb | HBx | Transactivator protein |

## Function

### Why cccDNA persists

1. **Stable episome**: cccDNA is a closed circular episome, not integrated; stable in non-dividing hepatocytes (liver is a predominantly post-mitotic organ); T½ estimated at weeks to months in vivo
2. **Nuclear recycling**: After reverse transcription, ~30-50% of newly made RC-DNA nucleocapsids are recycled to the nucleus → new cccDNA copies rather than exiting as virions; this replenishes cccDNA pool continuously during active replication
3. **Not a substrate for NRTI inhibition**: NRTIs incorporate into the reverse transcriptase reaction product (new RC-DNA), terminating chain elongation. They have no access to pre-formed nuclear cccDNA
4. **Epigenetic maintenance**: cccDNA chromatin undergoes active epigenetic maintenance — H3K4me3 (active) at promoters during high replication phases; H3K27me3 (repressive) during immune clearance phases
5. **HBx dependency**: cccDNA is transcriptionally inactive without HBx (Smc5/6 restriction); but HBx itself is encoded by cccDNA → autocatalytic loop for persistence

### Non-cytolytic cccDNA clearance mechanisms

In the immune-active phase, cccDNA can be reduced non-cytolytically:
- **APOBEC3A/3B (cytidine deaminases)**: Induce C→U hypermutation in cccDNA cytosines → non-functional cccDNA; IFN-α upregulates APOBEC3 expression; APOBEC3-induced cccDNA degradation is the primary non-cytolytic clearance mechanism
- **IFN-α/γ effect on HBx**: Reduce HBx levels → Smc5/6 no longer degraded → cccDNA transcription repressed (transcriptional silencing without DNA destruction)
- **Epigenetic silencing**: DNMT3a-mediated CpG methylation of cccDNA promoters in resolved infection → epigenetically silenced occult HBV

### Approaches to eliminate cccDNA (therapeutic frontier)

| Strategy | Mechanism | Stage |
|----------|----------|-------|
| **CRISPR/Cas9** | sgRNA targeting cccDNA → DSBs → NHEJ → inactivation | Preclinical; delivery to hepatocytes is challenge |
| **TLR7/8 agonists** | Activate innate immunity → IFN-α → APOBEC3A → cccDNA deamination | Clinical trials (selgantolimod, RO7020531) |
| **cGAS-STING agonists** | Stimulate innate IFN response + APOBEC3 → cccDNA degradation | Investigational (DMXAA analogues) |
| **CAMs (capsid assembly modulators)** | Block pgRNA packaging → no new RC-DNA → no new cccDNA formation; reduces cccDNA pool by attrition | Clinical (JNJ-6379, ABI-H0731) |
| **siRNA/ASO (HBx targeting)** | Reduce HBx → cccDNA transcriptionally silenced (Smc5/6 restriction) | Clinical component of combination strategies |
| **LHBsAg inhibitors (entry inhibitors)** | Block NTCP receptor → no new infection of adjacent cells → cccDNA diluted by cell division | Bulevirtide (approved for HBV+HDV) |
| **Zinc finger nucleases** | Sequence-specific DSBs in cccDNA | Preclinical |

## Mechanism

### cccDNA → transcription → reverse transcription cycle

The complete HBV replication cycle organized around cccDNA:

```
cccDNA (nucleus)
  ↓ RNA Pol II
pgRNA (3.5 kb)
  ↓ packaged with Pol
Cytoplasmic nucleocapsid
  ↓ RT-mediated reverse transcription
RC-DNA (new)
  ↓ [branch point]
  ├── Nuclear recycling → new cccDNA (replenishes pool)
  └── Envelopment → Dane particle → secretion
```

**Key kinetic parameters:**
- Time to cccDNA formation after NTCP-mediated entry: ~24 hours
- Half-life of cccDNA in non-dividing hepatocytes: estimated 33–50 days (studies in HBV-infected chimpanzees and humanized mice)
- Average cccDNA copies per hepatocyte: 5–50 in CHB; < 5 in inactive carrier; > 50 in immune-tolerant phase

### Epigenetic regulation of cccDNA

**Active HBV replication state** (immune tolerant/immune active phases):
- cccDNA histone marks: H3K4me3 (promoter activation), H3K9ac, H3K27ac
- HBx present → Smc5/6 degraded → unconstrained cccDNA transcription
- CREB, C/EBPα, HNF4α, NF-κB bound to cccDNA regulatory elements

**Epigenetically silenced state** (inactive carrier/resolved infection):
- H3K27me3, H3K9me2/me3 — Polycomb-mediated repression
- DNA methylation (CpG islands on cccDNA, induced by DNMT3a)
- APOBEC3G deaminase → C→U mutations in silenced cccDNA (occult HBV)
- HBx absent → Smc5/6 present → cccDNA transcription repressed

## Connections

**→ [Hepatitis B](../../../07-system/hepatitis-b/)**: HBV cccDNA is the nuclear replication reservoir that drives HBV chronicity; formed from RC-DNA by host enzymes including TDP2, PCNA/pol δ, and DNA ligase → supercoiled episome chromatinized by histones H3/H4; transcribes pgRNA, preC, and subgenomic RNAs; not cleared by NRTIs; elimination of cccDNA constitutes functional HBV cure.

**→ [cGAS-STING](../cgas-sting/)**: HBV RC-DNA and cccDNA activate cGAS in cytoplasm and nucleus → cGAMP → STING → TBK1/IRF3 → IFN-β; HBx binds and inhibits STING to prevent innate sensing of cccDNA; APOBEC3A/3B deaminate cccDNA cytosines enabling cGAS recognition; cGAS-STING agonists are being investigated as curative approaches to eliminate cccDNA-containing hepatocytes via innate immune activation.

**→ [p53](../p53/)**: HBx binds p53 DNA-binding domain → prevents p53 transcription of PUMA/BAX → HBV-infected hepatocytes resist apoptosis; HBV integration generates HBx-p53 chimeric proteins with altered function; TP53 R249S hotspot caused by aflatoxin B1 adducts is characteristic of HBV-HCC in endemic regions; p53 LOF enables cccDNA-containing hepatocyte survival and HCC development.

**→ [Wnt/β-catenin](../wnt-beta-catenin/)**: HBx activates Wnt/β-catenin by inhibiting GSK-3β and potentially degrading AXIN1 → β-catenin nuclear accumulation → TCF/LEF → MYC, cyclin D1; HBV integration near TERT promoter (the most frequent HBV integration site) activates telomerase; CTNNB1 activating mutations occur in ~25% of HBV-HCC; β-catenin/TCF binding sites on cccDNA promoters enhance HBV transcription in infected hepatocytes.

**→ [MAVS](../mavs/)**: HBV pgRNA reverse transcription in cytoplasmic nucleocapsids generates dsRNA intermediates → RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; HBV largely evades MAVS by confining replication products within the nucleocapsid, limiting dsRNA exposure; HBx also inhibits MAVS-dependent IFN signaling; the chronically low MAVS/IFN-β activation during HBV infection contributes to progressive T cell exhaustion and immune tolerance.
