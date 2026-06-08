---
schema: human-scale-entry/v1
id: hiv-gp120
name: HIV gp120
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "HIV gp120 (surface subunit of Env; ~120 kDa; 27 N-linked glycans) binds CD4 (Phe43 cavity) then CCR5/CXCR4 to trigger gp41 fusion; glycan shield conceals bNAb epitopes; CD4-binding site, V1V2 apex, and MPER are targets of VRC01, PG9, and SOSIP vaccine immunogens."
aliases: ["HIV gp120", "HIV envelope glycoprotein", "HIV Env", "gp120", "gp160", "HIV gp41", "broadly neutralizing antibody HIV", "bNAb", "SOSIP", "VRC01", "CD4-binding site antibody", "HIV vaccine gp120"]
sources:
  - id: kwong-1998-gp120-structure
    type: peer-reviewed
    cite: "Kwong PD, Wyatt R, Robinson J, et al. Structure of an HIV gp120 envelope glycoprotein in complex with the CD4 receptor and a neutralizing human antibody. Nature. 1998;393(6686):648-659."
    doi: "10.1038/31405"
    pmid: "9641677"
    url: "https://doi.org/10.1038/31405"
    accessed: "2026-06-08"
  - id: walker-2011-broadly-neutralizing
    type: peer-reviewed
    cite: "Walker LM, Huber M, Doores KJ, et al. Broad neutralization coverage of HIV by multiple highly potent antibodies. Nature. 2011;477(7365):466-470."
    doi: "10.1038/nature10373"
    pmid: "21849977"
    url: "https://doi.org/10.1038/nature10373"
    accessed: "2026-06-08"
  - id: sanders-2013-sosip-trimer
    type: peer-reviewed
    cite: "Sanders RW, Derking R, Cupo A, et al. A next-generation cleaved, soluble HIV-1 Env Trimer, BG505 SOSIP.664 gp140, expresses multiple epitopes for broadly neutralizing but not non-neutralizing antibodies. PLoS Pathog. 2013;9(9):e1003618."
    doi: "10.1371/journal.ppat.1003618"
    pmid: "24068931"
    url: "https://doi.org/10.1371/journal.ppat.1003618"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "gp120/gp41 constitutes the HIV Env trimer (~14 spikes/virion); gp120 CD4 + CCR5/CXCR4 binding defines HIV tropism; gp41 six-helix bundle executes membrane fusion; Env is the sole surface target of neutralizing antibodies; SOSIP stabilization is the central HIV vaccine strategy."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "HIV ssRNA/dsRNA intermediates activate RIG-I/MDA5 → MAVS → IRF3 → IFN-β after gp120-mediated entry; Vif degrades APOBEC3G; HIV capsid-CPSF6 nuclear pore threading evades cytosolic sensing before MAVS activation; Vpx (HIV-2) degrades SAMHD1."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic HIV dsDNA from reverse transcription activates cGAS → cGAMP → STING → IFN-β after gp120/gp41 entry; HIV capsid shields DNA during nuclear import; TREX1 degrades incomplete RT products; SAMHD1 blocks reverse transcription upstream of cGAS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "IFN-α (pDC TLR7/9) and ISGs restrict HIV post-entry: BST-2/tetherin tethers budding virions (Vpu counteracts); IFITM3 restricts gp41-mediated fusion; APOBEC3G hypermutates proviral DNA; IFN-α is amplified by gp120-containing virions engaging endosomal TLR7/9 in pDCs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "gp120 binding to CD4 on T cells activates NF-κB → T cell activation → permissive environment for HIV replication; HIV-1 LTR κB sites require NF-κB p65/p50 for proviral transcription; Tat + NF-κB cooperate at LTR for maximal HIV gene expression."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "gp41 (triggered by gp120-CD4 binding) is a class I fusogen — HR1/HR2 six-helix bundle analogous to RSV-F and SARS-CoV-2 S2; gp41 MPER targeted by 10E8/4E10 bNAbs analogous to anti-preF site Ø; SOSIP IP proline stabilization parallels DS-Cav1 RSV-F locking."
---

# HIV gp120

## Overview

**HIV gp120** is the surface-exposed glycoprotein subunit of the **HIV envelope (Env) trimer** — the sole virally-encoded surface antigen on HIV virions and therefore the exclusive target of **neutralizing antibodies**. Together with the transmembrane subunit **gp41**, gp120 forms a non-covalently associated trimeric spike (gp120/gp41)₃ of which approximately **14 copies** are incorporated per virion. This remarkably sparse display (compared to influenza's ~500 HA trimers or coronavirus' ~25 spike trimers) reflects the Env trimer's strategy of **antigenic concealment** — protecting conserved functional sites from antibody recognition while retaining receptor-binding competency.

The molecular structure of gp120 was first determined at atomic resolution by Kwong et al. in 1998 [^kwong-1998-gp120-structure], revealing the critical CD4-binding interface and the basis for **antibody evasion through conformational masking**. Two decades of bNAb (broadly neutralizing antibody) discovery — VRC01, PG9, PGT121, 10E8, and others [^walker-2011-broadly-neutralizing] — have defined the vulnerable epitopes on gp120/gp41 that are being targeted by SOSIP-based vaccine immunogens [^sanders-2013-sosip-trimer].

**Key insight for vaccine design:** Unlike measles (one effective antigen — H) or influenza (HA), HIV gp120's extreme sequence diversity across clades (~35% amino acid variation in variable loops) combined with its dense **N-glycan shield** (~27 N-linked glycans representing ~50% of gp120 molecular weight) have frustrated conventional vaccine approaches. Structural stabilization of the native trimer (SOSIP) and mosaic antigen design represent the current best strategies for eliciting cross-reactive neutralizing antibodies.

## Structure

### Biosynthesis and proteolytic processing

HIV **gp160** (160 kDa) is synthesized in the endoplasmic reticulum as a type I transmembrane precursor, heavily glycosylated in transit through the Golgi, and cleaved by **furin** (or furin-like proprotein convertase) in the trans-Golgi to generate:
- **gp120** (surface unit, ~120 kDa): Receptor binding; remains non-covalently attached to gp41 after cleavage; can be shed as decoy
- **gp41** (transmembrane unit, ~41 kDa): Membrane anchor; fusion machinery; cytoplasmic tail (~150 aa) interacts with MA

Three gp120/gp41 heterodimers associate non-covalently as a **trimeric spike** — the native-like functional structure essential for receptor engagement and fusion. The trimer is metastable: receptor binding triggers irreversible refolding.

### gp120 domain architecture

The gp120 ectodomain (~480 aa) contains [^kwong-1998-gp120-structure]:

**Core protein structure:**
- **Outer domain**: β-barrel fold; faces away from gp41; contains the **N-glycan shield** (dense glycan coverage masking antibody access) and the V1V2 and V4 loops
- **Inner domain**: α-helical; faces gp41/trimeric axis; undergoes major conformational change on CD4 binding
- **Bridging sheet**: Four-stranded β-sheet connecting inner and outer domains; forms part of the **co-receptor binding site** (exposed only after CD4 engagement)

**Variable loops (immunodominant, highly mutable):**

| Loop | Location | Function | Length variability |
|:---|:---|:---|:---|
| **V1** (aa ~131-156) | N-terminal of outer domain | Glycan-shielded; co-receptor modulation | 15-35 aa |
| **V2** (aa ~157-196) | Outer domain | V1V2 apex epitope (PG9 class); CCR5 binding modulation | 20-50 aa |
| **V3** (aa ~296-331) | Outer domain | **Co-receptor binding determinant**: V3 tip determines CCR5 vs CXCR4 tropism; crown exposed post-CD4 binding; immunodominant but high variability → type-specific neutralization | 34 aa (conserved length) |
| **V4** (aa ~385-418) | Outer domain | Glycan-shielded; less characterized | 15-30 aa |
| **V5** (aa ~460-470) | Outer domain | CD4-binding site accessory | Short |

### CD4-binding site (CD4bs)

The **CD4-binding site** is the most conserved region of gp120 and the primary target of **broadly neutralizing CD4bs antibodies** (VRC01, 3BNC117, N6LS):
- **CD4 contact residues**: D368, E370 (outer domain); the **Phe43 cavity** — a hydrophobic depression in gp120 that accommodates CD4's Phe43 sidechain
- Primary CD4 receptor contacts: Phe43 (CD4) → Asp368 (gp120); Arg59 (CD4) → Asp457 (gp120); Asn63 (CD4) → Glu370 (gp120)
- Conservation: ~80% amino acid identity across clades — the functional constraint of CD4 binding preserves this site
- Accessible to only a small fraction of natural antibodies because of glycan shielding and the inherent conformational flexibility of the unliganded trimer (the CD4bs is occluded in the pre-engagement closed state)

### N-glycan shield

gp120 contains **~27 N-linked glycosylation sequons** (NXS/T; X ≠ Pro) — with glycan density among the highest of any known glycoprotein:
- **~50% of gp120 molecular weight** is glycan
- Glycans are almost entirely **complex-type and high-mannose** (the high-mannose glycans form the "intrinsic mannose patch" targeted by 2G12 and PGT128 class bNAbs)
- The glycan shield evolved progressively: each subtype has distinct glycan positions; viral escape from bNAbs frequently adds new glycans to occlude antibody footprints
- Paradoxically, **some bNAbs use glycans as part of their epitope** (PG9, PG16, PGT121 — the "glycan-reactive bNAbs")

### gp41 — the fusion executor

gp41 contains:
- **Fusion peptide (FP)**: N-terminal ~25 aa; inserts into target membrane after triggering; indispensable for membrane merger
- **HR1 (heptad repeat 1/NHR)**: α-helix; forms coiled-coil trimer in the post-fusion six-helix bundle (6-HB)
- **HR2 (heptad repeat 2/CHR)**: α-helix; packs antiparallel into grooves of HR1 trimer → six-helix bundle (thermodynamic driving force for membrane fusion)
- **MPER (membrane-proximal external region)**: Connects HR2 to transmembrane domain; target of 10E8 and 4E10 bNAbs — the broadest-neutralizing antibodies known
- **Transmembrane domain**: Single-pass helix anchors gp41 in the viral/cell membrane
- **Cytoplasmic tail (~150 aa)**: Longest of any viral glycoprotein; contains endocytosis signals; interacts with MA and Gag during virion assembly

## Function

### CD4 binding and co-receptor engagement

**Stage 1 — CD4 binding:**
gp120 binds CD4 domain 1 (D1) via the **Phe43 cavity** → massive conformational rearrangement of gp120: bridging sheet repositions, V1V2 and V3 loops shift outward, a newly formed **coreceptor binding site** is exposed (spanning V3 base, bridging sheet, and elements of C4)

**Stage 2 — Co-receptor engagement:**
The exposed coreceptor binding site engages either:
- **CCR5** (M-tropic; CXCR4-negative strains): V3 loop tip binds CCR5 N-terminal ECL2; associated with macrophage/dendritic cell tropism; sexually transmitted strains are predominantly R5-tropic
- **CXCR4** (T-tropic; X4 strains): V3 positively charged residues bind CXCR4; emerge in ~50% of patients with advanced disease; associated with rapid CD4+ T cell decline

**Stage 3 — gp41 triggering and fusion:**
CD4 + co-receptor binding → gp120 dissociates (or repositions) → gp41 **spring-loaded** hairpin refolds: HR1 trimeric coiled-coil extends, fusion peptide inserts into target cell membrane, HR2 folds antiparallel against HR1 → six-helix bundle (6-HB) formation pulls viral and cellular membranes together → fusion pore → nucleocapsid enters

**Pharmacological targets of the entry process:**
- **Maraviroc**: CCR5 antagonist; allosteric; prevents gp120-CCR5 engagement; FDA-approved 2007; requires tropism testing (only for R5-tropic HIV)
- **Ibalizumab**: Anti-CD4 mAb that binds D2 of CD4 (not blocking gp120 binding but preventing co-receptor engagement); FDA-approved 2018 for MDR HIV
- **Enfuvirtide (T-20)**: Synthetic 36-aa HR2-mimetic peptide; competitively inhibits HR1/HR2 interaction → prevents 6-HB formation; first fusion inhibitor (2003); requires SC injection

### CCR5 tropism and transmission

Virtually all **sexually transmitted HIV strains are CCR5-tropic (R5)**. This tropism bottleneck occurs because:
- **Mucosal dendritic cells (Langerhans cells and sub-epithelial DCs) express CCR5** but not CXCR4 → first infected cells
- **Mucosal memory CD4+ T cells (CCR5+, CD45RO+)** are the primary initial targets (not naive T cells)
- CXCR4-tropic (X4) variants emerge during HIV disease progression, coinciding with depletion of CCR5+ memory T cells

## Mechanism

### Broadly neutralizing antibodies (bNAbs)

Years of antigen discovery identified ~8 distinct bNAb classes targeting conserved epitopes:

| bNAb class | Epitope | Representative antibodies | Neutralization breadth |
|:---|:---|:---|:---|
| **CD4-binding site (CD4bs)** | Conserved CD4-contact gp120 residues | VRC01, 3BNC117, N6LS, VRC07-523LS | ~90% of clades |
| **V1V2 glycan apex** | V1V2 tip + glycan N160 on gp120 trimer | PG9, PG16, VRC26, CAP256-VRC26 | ~80-90% of clades |
| **V3/glycan base (N332)** | N332 high-mannose + V3 base | PGT121, PGT128, 10-1074 | ~80-90% of clades |
| **Outer domain glycan** | High-mannose patch | 2G12 | ~40% (clade B focused) |
| **gp120/gp41 interface** | Cross-subunit epitope | 35O22 | Moderate breadth |
| **Fusion peptide (FP)** | gp41 N-terminal fusion peptide | VRC34, ACS202 | Broad |
| **gp41 MPER** | Membrane-proximal region of gp41 | 10E8, 4E10 | >95% of clades (ultra-broad) |
| **CD4-induced (CD4i)** | Co-receptor binding site (exposed after CD4 binding) | 17b, 48d | Narrow; not naturally elicited |

**N6LS clinical status**: Long-acting anti-CD4bs bNAb (N6 with LS mutation M428L/N434S → extended half-life ~70 days); Phase 3 trials for HIV prevention and viremic control; showed >96% protection in macaque models; combined with cabotegravir LA for long-acting HIV prevention regimen.

### SOSIP trimer — the native-like immunogen

The **BG505 SOSIP.664** (Sanders et al. 2013 [^sanders-2013-sosip-trimer]) is a stabilized, soluble, cleaved HIV-1 Env trimer that authentically displays bNAb epitopes:
- **SOS disulfide** (A501C in gp120 + T605C in gp41): Inter-subunit disulfide prevents gp120 shedding; maintains gp120-gp41 association
- **IP mutation** (I559P in gp41 HR1): Proline destabilizes the extended coiled-coil conformation → locks trimer in pre-fusion state (analogous to DS-Cav1 proline in RSV-F)
- **.664 truncation**: Removes the long gp41 cytoplasmic tail → enables secretion as soluble trimer
- **SOSIP result**: BG505 SOSIP displays V1V2 apex, CD4bs, V3/N332, and MPER epitopes authentically → strongly recognized by all major bNAb classes; does **not** display poorly neutralizing immunodominant epitopes (on gp41 ectodomain or non-native Env forms) → key advantage over monomeric gp120

### HIV vaccine — historical failures and current approaches

| Vaccine strategy | Trial | Result | Lesson |
|:---|:---|:---|:---|
| **Monomeric gp120 (VAX003/VAX004)** | Phase 3, 1998-2003 | 0% efficacy | Monomeric gp120 generates strain-specific non-neutralizing antibodies; does not elicit bNAbs |
| **ALVAC prime + gp120 boost (RV144)** | Phase 3 Thailand, 2009 | 31.2% efficacy (early) | Protective correlate: IgG anti-V1V2 + low IgA; boosters required |
| **Adenovirus-5 (STEP/Phambili)** | Phase 2b, 2007 | 0% efficacy; possible harm | T cell-only vaccines insufficient; Adeno5 pre-existing immunity problematic |
| **Mosaic Env + SOSIP trimer** | Phase 2b/3 (ongoing) | In progress | Mosaic = consensus sequence design covering global diversity; SOSIP displays native-like epitopes |

**Current leading approach (2024-2026)**: Mosaic HIV-1 trivalent vaccine (BG505 + AD26/BG505/APCF) in efficacy trials; mRNA-based SOSIP immunogen (Moderna mRNA-1644) in Phase 1/2; germline-targeting immunogens designed to activate VRC01-like precursor B cells from non-immune individuals.

## Connections

**→ [HIV](../../../07-system/hiv/)**: gp120 (with gp41) constitutes the HIV Env trimer (~14 spikes/virion); gp120 CD4 + CCR5/CXCR4 binding sequence defines HIV tropism; gp41 six-helix bundle executes membrane fusion; Env is the sole surface target of neutralizing antibodies; SOSIP trimer stabilization is the central HIV vaccine immunogen strategy.

**→ [MAVS](../mavs/)**: HIV ssRNA/dsRNA intermediates activate RIG-I/MDA5 → MAVS → IRF3 → IFN-β downstream of gp120-mediated entry; APOBEC3G (targeted by Vif) restricts reverse transcription; HIV capsid-CPSF6 nuclear pore threading evades cytosolic sensing before MAVS activation; Vpx (HIV-2) degrades SAMHD1.

**→ [cGAS-STING](../cgas-sting/)**: Cytosolic HIV dsDNA from reverse transcription (after gp120/gp41-mediated entry) activates cGAS → cGAMP → STING → IFN-β; HIV capsid shields DNA during nuclear import to limit cGAS sensing; TREX1 degrades incomplete RT products; SAMHD1 blocks reverse transcription upstream of cGAS.

**→ [Type I Interferon](../type-i-interferon/)**: Type I IFN restricts HIV at multiple post-entry steps: BST-2/tetherin tethers budding virions (gp120/gp41 Env enables Vpu escape); IFITM3 restricts gp41-mediated fusion; APOBEC3G mutates proviral DNA; IFN-α upregulated by gp120 binding to pDC TLR7/9 via endosomal uptake of virions.

**→ [NF-κB](../nf-kb/)**: gp120 binding to CD4 on uninfected T cells activates NF-κB signaling → T cell activation state → permissive environment for productive HIV infection; HIV-1 LTR κB sites (×2) require NF-κB p65/p50 for proviral transcription; Tat + NF-κB cooperate at LTR for maximal HIV gene expression.

**→ [RSV F Protein](../rsv-f-protein/)**: gp41 (triggered by gp120-CD4 binding) is a class I viral fusogen with HR1/HR2 forming a six-helix bundle, analogous to RSV-F and SARS-CoV-2 S2 fusion machinery; prefusion gp41 is the functional homologue of prefusion RSV-F; MPER of gp41 = analogue of fusion peptide proximal region; both are targets of the broadest neutralizing antibodies.

[^kwong-1998-gp120-structure]: Kwong PD, Wyatt R, Robinson J, et al. Structure of an HIV gp120 envelope glycoprotein in complex with the CD4 receptor and a neutralizing human antibody. *Nature.* 1998;393(6686):648-659. [doi:10.1038/31405](https://doi.org/10.1038/31405) · [PubMed 9641677](https://pubmed.ncbi.nlm.nih.gov/9641677/)
[^walker-2011-broadly-neutralizing]: Walker LM, Huber M, Doores KJ, et al. Broad neutralization coverage of HIV by multiple highly potent antibodies. *Nature.* 2011;477(7365):466-470. [doi:10.1038/nature10373](https://doi.org/10.1038/nature10373) · [PubMed 21849977](https://pubmed.ncbi.nlm.nih.gov/21849977/)
[^sanders-2013-sosip-trimer]: Sanders RW, Derking R, Cupo A, et al. A next-generation cleaved, soluble HIV-1 Env Trimer, BG505 SOSIP.664 gp140, expresses multiple epitopes for broadly neutralizing but not non-neutralizing antibodies. *PLoS Pathog.* 2013;9(9):e1003618. [doi:10.1371/journal.ppat.1003618](https://doi.org/10.1371/journal.ppat.1003618) · [PubMed 24068931](https://pubmed.ncbi.nlm.nih.gov/24068931/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
