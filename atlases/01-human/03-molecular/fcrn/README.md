---
schema: human-scale-entry/v1
id: fcrn
name: FcRn
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "FcRn (neonatal Fc receptor; FCGRT gene; chr19q13.32) recycles IgG and albumin by pH-dependent binding in endosomes → pH 6 binding rescues from lysosomal degradation → IgG t½ ~21 days. FcRn inhibitors (efgartigimod, rozanolixizumab) reduce pathogenic IgG in autoimmune diseases."
aliases: ["FcRn", "neonatal Fc receptor", "FCGRT", "FcRn receptor", "FcRn inhibitor", "efgartigimod", "rozanolixizumab", "nipocalimab", "batoclimab", "IgG recycling", "IgG half-life", "Fc recycling", "albumin recycling", "maternal-fetal IgG transfer"]
sources:
  - id: roopenian-2007-fcrn-review
    type: peer-reviewed
    cite: "Roopenian DC, Akilesh S. FcRn: the neonatal Fc receptor comes of age. Nat Rev Immunol. 2007;7(9):715-725."
    doi: "10.1038/nri2155"
    pmid: "17703228"
    url: "https://doi.org/10.1038/nri2155"
  - id: howard-2021-efgartigimod-adapt
    type: peer-reviewed
    cite: "Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT): a multicentre, randomised, placebo-controlled, phase 3 trial. Lancet Neurol. 2021;20(7):526-536."
    doi: "10.1016/S1474-4422(21)00159-9"
    pmid: "34146511"
    url: "https://doi.org/10.1016/S1474-4422(21)00159-9"
  - id: ward-2015-fcrn-albumin
    type: peer-reviewed
    cite: "Ward ES, Devanaboyina SC, Ober RJ. Targeting FcRn for the treatment of autoimmune diseases and alloantibody-mediated conditions. Trends Biotechnol. 2015;33(11):657-664."
    doi: "10.1016/j.tibtech.2015.09.005"
    pmid: "26476627"
    url: "https://doi.org/10.1016/j.tibtech.2015.09.005"
cross_links:
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Efgartigimod (Fc fragment competitor) and rozanolixizumab (anti-FcRn mAb) block FcRn → accelerated IgG catabolism including pathogenic anti-AChR IgG → 68-75% IgG reduction; efgartigimod FDA 2021 (ADAPT trial: 68% vs. 30% minimal symptom expression at week 12 in AChR+ MG)."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Anti-dsDNA and other pathogenic SLE autoantibodies are IgG → recycled by FcRn; FcRn blockade (efgartigimod, nipocalimab) reduces SLE autoantibody titers ~60-70%; efgartigimod Phase 3 in SLE ongoing; FcRn blockade complements BLyS/BAFF inhibition by targeting IgG homeostasis."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "FcRn binds IgG Fc (CH2-CH3 interface) at pH <6.5 in endosomes → prevents lysosomal degradation → IgG transcytosed back to cell surface and released at neutral pH; IgG t½ ~21 days vs. ~1-2 days without FcRn; efgartigimod saturates FcRn → accelerates IgG catabolism."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "FcRn recycles anti-GPIIb/IIIa IgG sustaining pathogenic platelet antibody titers in ITP; efgartigimod (ADVANCE-SC: sustained platelet response ~22% vs ~5%; FDA Jun 2023) accelerates IgG catabolism; rozanolixizumab under investigation in MYRIAD trial."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "TPO-RAs (romiplostim, eltrombopag) and FcRn inhibitors (efgartigimod) target complementary ITP mechanisms — stimulating c-Mpl → platelet production vs. blocking FcRn → anti-platelet IgG catabolism; their combination is under clinical investigation."
---

# FcRn

## Overview

**FcRn** (neonatal Fc receptor; also Brambell receptor) is an **MHC Class I–like heterodimer** that functions as a pH-sensitive transporter and homeostatic regulator of **IgG** and **albumin** — the two most abundant proteins in human plasma [^roopenian-2007-fcrn-review]. Unlike classical MHC Class I molecules, FcRn does not present peptides to T cells; instead, its peptide-binding groove is occupied by conserved residues that block antigen presentation while allowing pH-dependent ligand binding.

FcRn is encoded by:
- **α-chain (FcRn heavy chain):** *FCGRT* gene, chromosome 19q13.32; ~45 kDa; MHC-like α1/α2/α3 domain structure
- **β-chain:** **β2-microglobulin** (*B2M*, chromosome 15q21.1) — the same invariant subunit shared with all MHC Class I molecules and HLA-B27

FcRn was originally discovered in neonatal rodent gut, where it mediates uptake of maternal IgG from milk — hence "neonatal." In humans, its physiological roles span virtually all tissues (intestinal epithelium, vascular endothelium, hepatocytes, macrophages, dendritic cells, placenta) and include:
1. **IgG homeostasis** — rescuing IgG from lysosomal degradation → IgG half-life ~21 days
2. **Albumin homeostasis** — parallel rescue of albumin → t½ ~19 days
3. **Maternal-fetal IgG transfer** — via placental syncytiotrophoblast (human passive immunity in utero and post-partum via colostrum)
4. **Transcytosis** — apical-to-basolateral transport at mucosal surfaces (IgG surveillance)

**Therapeutic significance:** FcRn is the therapeutic target of a rapidly expanding class of **FcRn inhibitors** designed to reduce pathogenic IgG levels in autoimmune diseases. Unlike broad immunosuppressants, FcRn inhibitors selectively accelerate IgG catabolism — reducing all IgG subclasses (IgG1-4) by ~60-80% within weeks. This strategy is particularly effective in diseases driven by pathogenic IgG autoantibodies [^howard-2021-efgartigimod-adapt].

## Structure

### Domain architecture

**FcRn α-chain (FCGRT):** Three extracellular domains:
- **α1 domain** (aa ~1-90): first segment of the "peptide-binding groove" — but groove is narrow and occupied by conserved residues (Trp87, Lys88 in human) that prevent peptide binding
- **α2 domain** (aa ~91-180): second segment of the groove; contains the IgG-binding interface
- **α3 domain** (aa ~181-274): immunoglobulin-like; CD8 binding in classical Class I — in FcRn, mediates β2m interaction

**FcRn/IgG interaction (pH-dependent):**
- FcRn binds the **Fc region** (CH2-CH3 interface) of **IgG heavy chains** at the site involving **Ile253-Ser254-Arg255** and **His310** on IgG (His = histidine, pKa ~6)
- At **pH ≤6.5** (endosomal): His310 on IgG is protonated (+) → forms salt bridge with Glu117 and Glu135 on FcRn α2 domain → high-affinity binding (Kd ~0.1-1 µM at pH 6)
- At **pH 7.4** (plasma/extracellular): His310 is unprotonated (neutral) → electrostatic interaction lost → IgG released (Kd ~10-100 µM at pH 7.4)
- This simple pH switch is the molecular basis of IgG recycling

**FcRn/albumin interaction:**
- FcRn binds albumin at a distinct site from IgG — on the albumin surface near the **DIII subdomain** (albumin domain III)
- Also pH-dependent (binds at pH 6, releases at 7.4) with similar kinetics
- Albumin and IgG can **simultaneously** bind FcRn on opposite faces → co-rescue and co-transport
- Albumin t½ would be ~5 days without FcRn (vs. ~19 days with FcRn rescue)

### FcRn tissue distribution

| Tissue | Functional role |
|---|---|
| Vascular endothelium | Primary IgG recycling compartment; pinocytosis → endosome → FcRn → transcytosis or surface release |
| Intestinal epithelium (neonatal) | Milk IgG uptake from gut lumen (neonatal/rodent) |
| Placental syncytiotrophoblasts | Maternal-to-fetal IgG transfer; begins ~13 weeks gestation; peaks near term |
| Macrophages/monocytes | IgG recycling and transcytosis; FcRn competes with FcγRs for IgG uptake |
| Hepatocytes | Albumin rescue from Kupffer/sinusoidal degradation; VEGF-driven redistribution in liver disease |
| Dendritic cells | Antigen presentation enhancement via FcRn-mediated IgG immune complex uptake |

## Function

### IgG homeostasis — the recycling cycle

1. IgG in plasma → pinocytosed by vascular endothelial cells (non-specific fluid-phase endocytosis; also by macrophages, monocytes)
2. Endosome acidifies (pH 5.5-6.5 via V-ATPase) → FcRn on endosomal membrane binds IgG Fc at high affinity
3. FcRn-IgG complex protected from lysosomal delivery → vesicle traffics to cell surface
4. At plasma membrane (pH 7.4): IgG released from FcRn → returns to circulation
5. IgG not captured by FcRn → proceeds to lysosome → degraded
6. Net: **IgG t½ ~21 days** (IgG1, IgG2, IgG4), **~7 days** (IgG3, which has a His435→Arg mutation reducing FcRn affinity)
7. In FcRn-deficient mice: IgG t½ drops to ~1-2 days → demonstrates FcRn essentiality

### Maternal-fetal IgG transfer

- **Timing:** Active FcRn-mediated transfer begins at week 13-17 gestation; increases exponentially through 3rd trimester; neonatal IgG at birth may equal or exceed maternal levels for some specificities
- **Selectivity:** IgG1 > IgG4 > IgG3 > IgG2 in terms of transfer efficiency (correlates with FcRn binding affinity)
- **Clinical implication:** Pathogenic maternal IgG crosses to fetus:
  - Anti-Ro/La (SSA/SSB) → neonatal lupus, congenital complete heart block
  - Anti-AChR → transient neonatal myasthenia gravis (~12% of infants born to MG mothers)
  - Anti-RhD → hemolytic disease of the newborn (HDN; treated with anti-D prophylaxis in Rh-negative mothers)
  - Anti-HPA-1a (anti-platelet) → neonatal alloimmune thrombocytopenia (NAIT)
- **Protective transfer:** Maternal vaccine responses (COVID-19, tetanus, influenza, pertussis) → IgG crosses via FcRn → protects neonate before own immune development

### Antibody engineering using FcRn knowledge

FcRn biology has enabled rational antibody engineering to extend or shorten therapeutic antibody t½:
- **Extended t½:** YTE mutation (M252Y/S254T/T256E in IgG Fc) → 3-4× increased FcRn affinity at pH 6 → 3-4× longer IgG t½; used in motavizumab, imalumab, nirsevimab (anti-RSV; given once to neonates)
- **Shortened t½:** IgG4 (naturally lower FcRn binding), IgG3 (His435Arg → reduced binding); relevant for rapid-clearance therapeutics
- **FcRn saturation for IgG reduction:** Competitive inhibition with engineered Fc fragments (efgartigimod) or anti-FcRn antibodies → all endosomal FcRn occupied → IgG degraded → ~60-80% total IgG reduction

## Mechanism

### FcRn inhibitor mechanism of action

**Efgartigimod (Vyvgart; argenx):**
- Structure: Human IgG1 Fc fragment engineered with ABDEG mutations (M428L/N434S; also N297A for aglycosylation) → pH 6 FcRn binding affinity enhanced ~60-fold vs. WT IgG; pH 7.4 affinity unchanged → FcRn occupied in endosomes → endogenous IgG displaced → degraded
- Route: IV infusion 10 mg/kg weekly ×4 (1 cycle); subcutaneous formulation (PH20 hyaluronidase-mediated) approved 2023
- **ADAPT trial** (generalized AChR+ MG, n=167): 68% vs. 30% minimal symptom expression rate at week 12 in AChR+ subgroup; FDA approved December 2021
- Additional approvals: ADVANCE-SC (ITP, 2022 SC formulation), ADDRESS-sc (CIDP), ADHERE (pemphigus vulgaris)

**Rozanolixizumab (Rystiggo; UCB):**
- Humanized anti-FcRn mAb (IgG4); SC weekly ×6 cycles; ~70% IgG reduction
- **MG0002** Phase 3 trial (MG): primary endpoint met (QMG improvement); FDA approved June 2023

**Nipocalimab (Janssen):**
- Human anti-FcRn mAb (IgG1); in trials for MG, warm AIHA, neonatal alloimmune conditions
- Unique application: reduce maternal pathogenic IgG transfer (blocking FcRn in syncytiotrophoblast) → prevent NAIT, hemolytic disease of newborn from alloimmune causes

**Batoclimab (IMVT-1401; Immunovant):**
- Fully human anti-FcRn mAb; SC administration; ADHERE trial (thyroid eye disease) ongoing

## Connections

- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — Efgartigimod (Fc fragment competitor) and rozanolixizumab (anti-FcRn mAb) block FcRn → accelerated IgG catabolism including pathogenic anti-AChR IgG → 68-75% IgG reduction; efgartigimod FDA 2021 (ADAPT trial: 68% vs. 30% minimal symptom expression at week 12 in AChR+ MG).
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — Anti-dsDNA and other pathogenic SLE autoantibodies are IgG → recycled by FcRn; FcRn blockade (efgartigimod, nipocalimab) reduces SLE autoantibody titers ~60-70%; efgartigimod Phase 3 in SLE ongoing; FcRn blockade complements BLyS/BAFF inhibition by targeting IgG homeostasis.
- `connects-to` → **[IgG](../immunoglobulin-g/README.md)** — FcRn binds IgG Fc (CH2-CH3 interface) at pH <6.5 in endosomes → prevents lysosomal degradation → IgG transcytosed back to cell surface and released at neutral pH; IgG t½ ~21 days vs. ~1-2 days without FcRn; efgartigimod saturates FcRn → accelerates IgG catabolism.
- `connects-to` → **[Immune Thrombocytopenia](../../07-system/immune-thrombocytopenia/README.md)** — FcRn recycles anti-GPIIb/IIIa IgG sustaining pathogenic platelet antibody titers in ITP; efgartigimod (ADVANCE-SC: ~22% vs ~5% sustained platelet response; FDA Jun 2023) accelerates IgG catabolism; rozanolixizumab under investigation.
- `connects-to` → **[Thrombopoietin](../thrombopoietin/README.md)** — TPO-RAs (romiplostim, eltrombopag) and FcRn inhibitors (efgartigimod) target complementary ITP mechanisms — stimulating c-Mpl → platelet production vs. blocking FcRn → anti-platelet IgG catabolism; combination under clinical investigation.

[^roopenian-2007-fcrn-review]: Roopenian DC, Akilesh S. FcRn: the neonatal Fc receptor comes of age. *Nat Rev Immunol.* 2007;7(9):715-725. [doi:10.1038/nri2155](https://doi.org/10.1038/nri2155) · [PubMed 17703228](https://pubmed.ncbi.nlm.nih.gov/17703228/)
[^howard-2021-efgartigimod-adapt]: Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT). *Lancet Neurol.* 2021;20(7):526-536. [doi:10.1016/S1474-4422(21)00159-9](https://doi.org/10.1016/S1474-4422(21)00159-9) · [PubMed 34146511](https://pubmed.ncbi.nlm.nih.gov/34146511/)
[^ward-2015-fcrn-albumin]: Ward ES, Devanaboyina SC, Ober RJ. Targeting FcRn for the treatment of autoimmune diseases and alloantibody-mediated conditions. *Trends Biotechnol.* 2015;33(11):657-664. [doi:10.1016/j.tibtech.2015.09.005](https://doi.org/10.1016/j.tibtech.2015.09.005) · [PubMed 26476627](https://pubmed.ncbi.nlm.nih.gov/26476627/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
