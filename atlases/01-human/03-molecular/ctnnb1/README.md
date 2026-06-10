---
schema: human-scale-entry/v1
id: ctnnb1
name: CTNNB1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CTNNB1 encodes β-catenin (Wnt effector and adherens junction scaffold); activating mutations (S45F/T41A) → nuclear β-catenin → TCF/LEF target genes (MYC, CCND1, VEGFA); ~80% desmoid tumors harbor CTNNB1 mutations; nirogacestat FDA-approved for desmoid; HCC and endometrial cancer."
aliases: ["CTNNB1", "beta-catenin", "β-catenin", "CTNNB1 mutation", "Wnt beta-catenin mutation", "beta-catenin activating mutation", "CTNNB1 desmoid", "CTNNB1 colorectal", "CTNNB1 hepatocellular", "CTNNB1 endometrial"]
sources:
  - id: morin-1997-ctnnb1-colorectal
    type: peer-reviewed
    cite: "Morin PJ, Sparks AB, Korinek V, et al. Activation of beta-catenin-Tcf signaling in colon cancer by mutations in beta-catenin or APC. Science. 1997;275(5307):1787-1790."
    doi: "10.1126/science.275.5307.1787"
    pmid: "9065402"
    url: "https://doi.org/10.1126/science.275.5307.1787"
  - id: lazar-2008-ctnnb1-desmoid
    type: peer-reviewed
    cite: "Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. Am J Pathol. 2008;173(5):1518-1527."
    doi: "10.2353/ajpath.2008.080475"
    pmid: "18832571"
    url: "https://doi.org/10.2353/ajpath.2008.080475"
cross_links:
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "CTNNB1-mutant nuclear β-catenin activates MYC via TCF/LEF-binding elements in the MYC promoter; MYC is the primary proliferative driver downstream of CTNNB1 in desmoid and colorectal cancer; MYC amplification confers resistance to β-catenin-targeted therapy in desmoid."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13)."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "APC LOF (>80% of CRC) or direct CTNNB1 exon 3 mutations (~5-10%) both activate nuclear β-catenin → TCF/LEF-driven MYC and CCND1 → adenoma-carcinoma sequence; CTNNB1 is the effector of APC tumor suppressor; aspirin reduces CRC risk partly via Wnt pathway suppression."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "~80% of sporadic desmoid fibromatosis harbor CTNNB1 exon 3 mutations (S45F most aggressive, T41A intermediate); mutation site predicts recurrence risk; nirogacestat (FDA-approved Nov 2023, DeFi trial: PFS HR 0.29) targets Notch-Wnt crosstalk in CTNNB1-mutant desmoid."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "CTNNB1 activating mutations in ~30-40% of HCC (2nd most common driver after TERT); nuclear β-catenin IHC positive (GS+, AFP-low); CTNNB1-mutant HCC has immune-excluded TME with poor ICI response; WNT inhibitors (WNT974, RXC004) under investigation in CTNNB1-mutant HCC."
---

# CTNNB1

## Overview

**CTNNB1** (catenin beta-1) encodes **β-catenin** (781 amino acids, 88 kDa), a dual-function protein that serves as both the terminal effector of the **Wnt/β-catenin signaling pathway** and a critical structural component of **adherens junctions** (cadherin-catenin complex). At plasma membranes, β-catenin links E-cadherin/N-cadherin to α-catenin and the actin cytoskeleton; in the nucleus, β-catenin acts as a transcriptional co-activator with TCF/LEF transcription factors, driving target genes including MYC, CCND1, VEGFA, MMP7, and AXIN2. Activating mutations in CTNNB1 — predominantly clustered in exon 3 at the GSK-3β/CK1α phosphodegron — create a protein that cannot be phosphorylated and targeted for proteasomal degradation, resulting in constitutive nuclear β-catenin accumulation independent of Wnt ligand [^morin-1997-ctnnb1-colorectal].

**CTNNB1 mutations across tumor types:**

| Tumor type | CTNNB1 alteration | Frequency | Clinical significance |
|---|---|---|---|
| Desmoid fibromatosis | Gain-of-function point mutation (exon 3) | ~80% sporadic | Nirogacestat FDA-approved; mutation site predicts recurrence risk |
| Hepatocellular carcinoma | Gain-of-function point mutation | ~30-40% | CTNNB1-mutant HCC: GS+, AFP low, β-catenin nuclear; poor ICI response |
| Endometrial cancer | Gain-of-function mutation | ~15-20% | Associated with microsatellite stable, favorable histology |
| Medulloblastoma | Gain-of-function mutation | ~10-15% | WNT subgroup medulloblastoma; best prognosis (~95% cure rate) |
| Colorectal cancer | Gain-of-function (rare; APC LOF more common) | ~5-10% | APC LOF → same phenotypic consequence; direct CTNNB1 mutation rarer |
| Ovarian clear cell | Gain-of-function | ~15-20% | Associated with endometriosis |
| Pilomatricoma/pilomatrixoma | Gain-of-function | >90% | Benign adnexal tumor; prototypical CTNNB1 mutation model |

**Loss-of-function CTNNB1:** associated with CDH1 (E-cadherin) mutations → disrupted adherens junction → invasive lobular breast carcinoma phenotype (loss of adhesion); rare compared to GOF variants

## Structure

### β-catenin protein architecture

**N-terminal domain (aa 1-130):**
Contains the phosphodegron (serine/threonine residues S33, S37, T41, S45 in exon 3); site of sequential phosphorylation by CK1α (S45) then GSK-3β (T41→S37→S33) → β-TrCP E3 ligase recognition → K48-polyubiquitination → 26S proteasome degradation; activating CTNNB1 mutations cluster here, particularly at S45 and T41; these prevent phosphorylation → protein accumulates

**Armadillo repeat domain (aa 131-665):**
12 imperfect 42-amino acid armadillo repeats; forms a superhelix creating a positive groove; mediates binding to >50 interaction partners including E-cadherin (cytoplasmic tail), α-catenin, APC, TCF/LEF, and AXIN; R2 and R3 (armadillo repeats 2-3) interact with TCF/LEF; C-helix of arm repeat 10 binds APC

**C-terminal domain (aa 666-781):**
Transactivation domain (TAD); recruits co-activators p300/CBP (histone acetyltransferases), BRG1 (SWI/SNF), and MED12 (Mediator complex) → transcriptional activation at TCF/LEF target gene promoters; PDZ-binding motif at C-terminus recruits DLG family scaffolds → membrane-associated β-catenin pool at epithelial lateral membranes

### Oncogenic CTNNB1 mutations

**Exon 3 phosphodegron mutations:**
The phosphodegron contains serine/threonine residues sequentially phosphorylated by the destruction complex:
- **S45F/Y**: most common in desmoid (especially S45F → high recurrence risk); CK1α cannot phosphorylate → GSK-3β cascade blocked → protein stable
- **T41A**: second most common in desmoid; moderate recurrence risk; better prognosis than S45F [^lazar-2008-ctnnb1-desmoid]
- **S33F/C/Y**: colorectal cancer-associated; complete phosphodegron ablation
- **G34E/V/R**: same exon; loss of β-TrCP recognition; associated with colorectal and HCC

**IHC:**
Nuclear β-catenin IHC: pathognomonic for CTNNB1 gain-of-function; sensitivity ~90% for desmoid; also positive in medulloblastoma WNT subgroup; cytoplasmic+nuclear positivity in CTNNB1-mutant HCC; membrane-only positivity = normal

### CTNNB1 mutation-specific prognosis in desmoid [^lazar-2008-ctnnb1-desmoid]

| CTNNB1 mutation | Recurrence risk | Behavior |
|---|---|---|
| S45F | High (~50-70% recurrence) | Most aggressive; rapid regrowth |
| S45Y | High (~50-60%) | Similar to S45F |
| T41A | Intermediate (~25-40%) | Most common; intermediate prognosis |
| S33C/F | Variable | Colorectal-like mutation; rare in desmoid |
| APC germline (FAP) | Variable by location | FAP-associated desmoid: mesenteric > abdominal wall |

## Function

### Dual roles of β-catenin

**Adherens junction function (membrane β-catenin):**
E-cadherin cytoplasmic tail (encoded by CDH1) binds armadillo repeats R1-R4 → β-catenin bridges E-cadherin to α-catenin → α-catenin binds F-actin → stable adherens junction; β-catenin pool at membrane is in equilibrium with cytoplasmic pool; E-cadherin stabilizes membrane β-catenin and limits its availability for nuclear signaling; CDH1 loss (lobular breast cancer, invasive gastric cancer) → membrane β-catenin freed → nuclear translocation

**Wnt effector function (nuclear β-catenin):**
In Wnt-OFF state: APC + AXIN + CK1α + GSK-3β form destruction complex → β-catenin phosphorylated → β-TrCP → proteasomal degradation → TCF/LEF repressed by GROUCHO/TLE
In Wnt-ON state: FZD + LRP5/6 + Wnt ligand → DVL recruitment → AXIN sequestration → destruction complex dissolved → β-catenin accumulates → enters nucleus → displaces GROUCHO from TCF/LEF → recruits p300/BCL9/PYGO → target gene transcription (MYC, CCND1, AXIN2, VEGFA, DKK1, LGR5, CD44)

**Key CTNNB1 target genes:**
- **MYC**: primary proliferative driver; TCF binding site in c-MYC intron 1; highest-confidence β-catenin target
- **CCND1** (cyclin D1): G1/S cell cycle progression → Rb phosphorylation
- **AXIN2**: negative feedback regulator of β-catenin (constitutes a negative feedback loop)
- **LGR5**: intestinal stem cell marker; Wnt/β-catenin target; stem cell maintenance
- **VEGFA**: angiogenesis; explains vascular density in β-catenin-mutant tumors
- **MMP7**: matrix metalloproteinase → invasion; colorectal cancer invasion
- **TCF7 (TCF1)**: positive autoregulatory loop

## Mechanism

### Desmoid tumor — CTNNB1 as primary driver

Desmoid fibromatosis is the clearest model of CTNNB1 addiction:
- Sporadic desmoid (~80%): single CTNNB1 exon 3 point mutation; heterozygous; one mutant allele sufficient for nuclear accumulation (haploinsufficiency of destruction is not the mechanism — rather, mutant protein outcompetes wild-type for nuclear entry as destruction complex cannot process it fast enough)
- FAP-associated desmoid (~20%): germline APC truncation → insufficient APC to constitute destruction complex → β-catenin accumulates; APC mutations at codons 1310-2011 (3' of codon 1061) predispose to mesenteric desmoid
- Mesenteric desmoid (FAP): most aggressive; encases small bowel mesentery; major mortality cause in FAP post-colectomy

**Nirogacestat mechanism in desmoid:**
γ-secretase (presenilin-1/2 protease complex) cleaves Notch1 (and other substrates including APP, E-cadherin) → releases Notch1 intracellular domain (NICD1) → nuclear → HES/HEY target gene transcription; in CTNNB1-mutant desmoid, Notch1-NICD1 cooperates with β-catenin/TCF to drive MYC and other proliferative targets; nirogacestat → γ-secretase inhibition → NICD1 suppression → MYC reduction → G1 arrest → desmoid cell apoptosis; Wnt and Notch pathways are co-activated and mutually reinforcing in desmoid stroma

**DeFi Phase 3 trial (Gounder 2023):** N=142 adult patients with progressing desmoid tumors; nirogacestat 150 mg BID vs placebo; primary endpoint: PFS; nirogacestat PFS HR 0.29 (p<0.0001); ORR 41% vs 8%; time to response ~3-6 months; most responses durable; FDA approved November 2023 for adults with progressing desmoid tumors; grade 3/4 toxicity: diarrhea ~10%, rash ~5%, fatigue ~5%; unique toxicity: ovarian toxicity (FSH elevation, amenorrhea) in women — requires hormonal monitoring

**Sorafenib:**
DESMOID Phase 2 (no randomized data initially; subsequent Phase 2): sorafenib (VEGFR/PDGFR/BRAF/RAF inhibitor) 400 mg daily; ORR ~15-20% in sporadic desmoid; PFS HR 0.13 in comparison to historical control; mechanism may include VEGFR blockade (reduces tumor vascular supply) and direct PDGFR/RAF signaling suppression; used as alternative systemic therapy when nirogacestat unavailable or contraindicated

**Targeted CTNNB1 inhibition:**
Direct TCF/β-catenin inhibition: BC2059 (β-catenin/TNKS inhibitor), PRI-724 (CBP/β-catenin inhibitor), CWP232291 → early-phase clinical trials; TNKS1/2 inhibitors (OMP-54F28, XAV939) → destabilize β-catenin by stabilizing AXIN → preclinical desmoid and colorectal activity; resistance: CTNNB1 mutations in phosphodegron are absolute — no degree of upstream Wnt blockade can rescue destruction

## Connections

- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — CTNNB1-mutant nuclear β-catenin activates MYC via TCF/LEF-binding elements in the MYC promoter; MYC is the primary proliferative driver downstream of CTNNB1 in desmoid and colorectal cancer; MYC amplification confers resistance to β-catenin-targeted therapy in desmoid.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13).
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — APC LOF (>80% of CRC) or direct CTNNB1 exon 3 mutations (~5-10%) both activate nuclear β-catenin → TCF/LEF-driven MYC and CCND1 → adenoma-carcinoma sequence; CTNNB1 is the effector of APC tumor suppressor function in colorectal carcinogenesis.
- `connects-to` → **[Desmoid Tumor](../../07-system/desmoid-tumor/README.md)** — ~80% of sporadic desmoid fibromatosis harbor CTNNB1 exon 3 mutations; S45F is most aggressive, T41A intermediate; nirogacestat (FDA-approved Nov 2023, DeFi trial: PFS HR 0.29, ORR 41%) targets Notch-Wnt crosstalk in CTNNB1-mutant desmoid.
- `connects-to` → **[HCC](../../07-system/hcc/README.md)** — CTNNB1 activating mutations in ~30-40% of HCC (2nd most common driver after TERT); nuclear β-catenin IHC positive (GS+, AFP-low phenotype); CTNNB1-mutant HCC has immune-excluded TME with poor ICI response; WNT inhibitors under investigation.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^morin-1997-ctnnb1-colorectal]: Morin PJ, Sparks AB, Korinek V, et al. Activation of beta-catenin-Tcf signaling in colon cancer by mutations in beta-catenin or APC. *Science.* 1997;275(5307):1787-1790. [doi:10.1126/science.275.5307.1787](https://doi.org/10.1126/science.275.5307.1787) · [PubMed 9065402](https://pubmed.ncbi.nlm.nih.gov/9065402/)
[^lazar-2008-ctnnb1-desmoid]: Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. *Am J Pathol.* 2008;173(5):1518-1527. [doi:10.2353/ajpath.2008.080475](https://doi.org/10.2353/ajpath.2008.080475) · [PubMed 18832571](https://pubmed.ncbi.nlm.nih.gov/18832571/)
