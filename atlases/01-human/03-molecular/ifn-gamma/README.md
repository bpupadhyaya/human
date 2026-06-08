---
schema: human-scale-entry/v1
id: ifn-gamma
name: IFN-gamma
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Primary Th1 cytokine produced by CD4+ Th1, CD8+ CTLs, and NK cells; binds IFNGR1/2 → JAK1/2 → STAT1 → MHC-II, IDO1, and antimicrobial gene induction. Central mediator of adaptive cellular immunity and antitumor immunosurveillance; evaded by PD-L1 upregulation in tumors."
aliases: ["interferon-gamma", "IFNG", "type II interferon", "immune interferon", "IFN-γ", "T cell interferon"]
sources:
  - id: schroder-2004-ifng-review
    type: peer-reviewed
    cite: "Schroder K, Hertzog PJ, Ravasi T, Hume DA. Interferon-gamma: an overview of signals, mechanisms and functions. J Leukoc Biol. 2004;75(2):163-189."
    doi: "10.1189/jlb.0603252"
    pmid: "14525967"
    url: "https://doi.org/10.1189/jlb.0603252"
  - id: platanias-2005-jak-stat-ifn
    type: peer-reviewed
    cite: "Platanias LC. Mechanisms of type-I- and type-II-interferon-mediated signalling. Nat Rev Immunol. 2005;5(5):375-386."
    doi: "10.1038/nri1604"
    pmid: "15864272"
    url: "https://doi.org/10.1038/nri1604"
  - id: pitt-2016-ifng-cancer
    type: peer-reviewed
    cite: "Pitt JM, Vétizou M, Daillère R, et al. Resistance mechanisms to immune-checkpoint blockade in cancer: tumor-intrinsic and -extrinsic factors. Immunity. 2016;44(6):1255-1269."
    doi: "10.1016/j.immuni.2016.06.001"
    pmid: "27332732"
    url: "https://doi.org/10.1016/j.immuni.2016.06.001"
cross_links:
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IFN-gamma binds IFNGR1/2 → JAK1 (on IFNGR1) and JAK2 (on IFNGR2) → STAT1 Tyr701 phosphorylation → STAT1 homodimers (GAF) → GAS elements → MHC-II, CXCL9/10/11, IDO1 transcription; JAK1/2 inhibitors (ruxolitinib) potently block IFN-gamma signaling."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "IFN-gamma primes NLRP3 inflammasome expression via STAT1 → transcriptional upregulation of NLRP3 and pro-IL-1beta; synergizes with LPS or ATP → amplified IL-1beta; IFN-gamma + NLRP3 cooperation amplifies inflammation in gout, atherosclerosis, and anti-tumor immunity."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "IFN-gamma activates NF-kB via STAT1-IRF1 → iNOS, TNF-alpha, IL-12 → M1 macrophage polarization; IFN-gamma + TLR4 (LPS) → synergistic NF-kB → M1 effector functions; sustained IFN-gamma + NF-kB drives macrophage-mediated autoimmune tissue injury."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "IFN-gamma is the dominant inducer of MHC class II expression via STAT1 → CIITA transcription → MHC-II upregulation on macrophages, DCs, and non-professional APCs; tumor cell MHC-II upregulation by IFN-gamma → T helper cell recognition → anti-tumor immune activation."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 is the upstream inducer of IFN-γ via JAK2/TYK2/STAT4/T-bet axis; IL-12-deficient patients (IL12B, IL12RB1 mutations) have markedly reduced IFN-γ production → MSMD; therapeutic IL-12 blockade (ustekinumab) reduces IFN-γ output and raises TB reactivation risk."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "IFN-γ is essential for macrophage activation and MTB killing (phagosome acidification, ROS, cathelicidin); IFN-γ from MTB-sensitized T cells is the basis of IGRA tests; IFNGR1/IFNGR2 mutations → MSMD with disseminated MTB/BCG; IFN-γ release drives TB-related ACD."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "IFN-γ is the critical anti-Leishmania effector: Th1 CD4+ and NK cells produce IFN-γ → macrophage iNOS → NO → kills intracellular amastigotes; IFNGR1/2 deficiency (MSMD) → disseminated VL; IFN-γ is used adjunctively in refractory VL; IL-12 drives IFN-γ in Th1 priming."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ → IFNGR1/2 → JAK1/JAK2 → STAT1 homodimer (GAF) → GAS elements → IRF1, iNOS, MHC-II; STAT1 GOF (R274Q, C324Y) → impaired Th17 → CMC; STAT1 LOF → MSMD — disseminated BCG and NTM; STAT1 is the non-redundant transducer of IFN-γ antimicrobial signaling."
---

# IFN-gamma

## Overview

**IFN-gamma (interferon-gamma, IFNG)** is the **sole type II interferon** — a pleiotropic cytokine and the defining signature cytokine of the **Th1 adaptive immune response**. Unlike type I interferons (IFN-alpha/beta, antiviral innate immunity) which use the IFNAR receptor, IFN-gamma signals through a distinct **IFNGR1/IFNGR2 heterodimeric receptor** and primarily activates **STAT1** (as opposed to STAT2 for type I IFNs) [^platanias-2005-jak-stat-ifn].

**Sources of IFN-gamma:**
- **CD4+ Th1 cells:** Major adaptive source; IL-12 + IL-18 (from DCs and macrophages) → Th1 differentiation → sustained IFN-gamma production during adaptive immune responses
- **CD8+ cytotoxic T lymphocytes (CTLs):** Both effector function (TCR-induced) and independent of killing; critical for anti-viral and anti-tumor IFN-gamma production
- **NK cells:** Innate source; IL-12 + IL-18 (from macrophages) → rapid IFN-gamma secretion; important early in infection before adaptive immunity is primed
- **NKT cells, gamma-delta T cells:** Additional innate-like IFN-gamma producers at mucosal surfaces
- **Innate ILC1 (type 1 innate lymphoid cells):** Tissue-resident IFN-gamma producers analogous to NK cells; important in gut and liver

**Biological roles of IFN-gamma:**

1. **Macrophage activation (M1 polarization):** IFN-gamma + LPS → classically activated macrophage → high bactericidal activity (iNOS → nitric oxide, NADPH oxidase → ROS), IL-12 production (amplifying Th1), MHC-II upregulation → enhanced antigen presentation
2. **Adaptive immune amplification:** MHC-I and MHC-II upregulation on APCs → improved antigen presentation → stronger CTL and Th1 priming; CXCL9/10/11 chemokine induction → T cell recruitment to inflamed tissue
3. **Antitumor immunity:** IFN-gamma is the dominant effector mechanism of T cell-mediated tumor killing beyond direct perforin/granzyme; IFN-gamma → tumor cell MHC-I restoration → CTL recognition; IFN-gamma → tumor cell CXCL9/10 → further T cell recruitment
4. **Antimicrobial:** IDO1 (indoleamine-2,3-dioxygenase 1) induction → tryptophan depletion → inhibits intracellular pathogens (Toxoplasma, Chlamydia, Mycobacterium); iNOS → NO → anti-mycobacterial
5. **Immune regulation:** Paradoxically, sustained IFN-gamma → PD-L1 upregulation on tumor cells and DCs → negative feedback on T cells; IDO1 → kynurenine → Treg differentiation → immune suppression in chronic settings

## Structure

### IFN-gamma protein and receptor [^schroder-2004-ifng-review]

**IFN-gamma protein:**
- Homodimer; each chain ~16.8 kDa; non-covalent antiparallel dimer required for activity (~34 kDa active form)
- Alpha-helical bundle structure (6 helices per monomer) — distinct from type I IFNs (which are monomers with slightly different helical topology)
- **Highly basic C-terminal tail:** Heparin-binding; facilitates binding to IFNGR on cell surfaces; proteolytic removal abolishes activity
- Not glycosylated at Asn25 in some isoforms (does not affect activity)

**IFNGR receptor complex:**
- **IFNGR1 (CD119):** Ligand-binding chain; two per homodimer; low affinity for IFN-gamma alone; extracellular IgG-fold domain
- **IFNGR2 (CD118):** Signaling chain; pre-associated with JAK2; two per complex; forms ternary hexameric complex with IFNGR1 and IFN-gamma homodimer
- **Signaling complex:** IFN-gamma → IFNGR1-IFNGR2 dimerization → JAK1 (IFNGR1) and JAK2 (IFNGR2) transphosphorylation → STAT1 Tyr701 phosphorylation → STAT1 homodimerization → nuclear translocation → GAS (gamma-activated sequence) element binding → target gene transcription

**IFNGR expression:**
- Ubiquitously expressed (unlike IFNAR, which is restricted in expression in some contexts); all nucleated cells can respond to IFN-gamma; expression downregulated by IFN-gamma itself (ligand-induced receptor internalization and downregulation → limiting sustained signaling)

### JAK-STAT1 signaling specificity [^platanias-2005-jak-stat-ifn]

IFN-gamma uniquely activates **STAT1 homodimers (GAF, gamma-activated factor)** binding **GAS (gamma-activated site)** elements (TTCnnnGAA). This distinguishes IFN-gamma from:
- Type I IFNs (STAT1-STAT2 heterodimers + IRF9 → ISGF3 → ISRE elements)
- IL-6 (STAT3 homodimers → APRE elements)
- IL-2 (STAT5 homodimers)

**Key IFN-gamma/STAT1 target genes:**
- **MHC-I heavy chains (HLA-A, -B, -C):** STAT1 → IRF1 → beta-2-microglobulin and MHC-I → enhanced CTL killing of infected/malignant cells
- **CIITA (MHC-II transactivator):** STAT1 → CIITA transcription → MHC-II, HLA-DM, invariant chain → enhanced CD4+ T cell priming
- **CXCL9, CXCL10, CXCL11 (T cell chemokines):** Recruit CXCR3+ effector T cells and NK cells to sites of inflammation; "hot" tumor microenvironment signature
- **IDO1:** Tryptophan catabolism → immunosuppressive kynurenine; dual role (antimicrobial vs. immune suppressive)
- **IRF1:** Transcription factor → amplifier of IFN-gamma responses; triggers additional antiviral and antitumor genes; also activates NOS2 (iNOS)
- **NOS2 (iNOS):** Nitric oxide synthase → NO production → macrophage bactericidal activity; also anti-tumor activity
- **PD-L1 (CD274):** STAT1 → IRF1 → PD-L1 → adaptive immune resistance; IFN-gamma is the primary inducer of adaptive PD-L1 expression in tumors and APCs; this feedback is the molecular basis for PD-1/PD-L1 blockade efficacy in IFN-gamma-rich "hot" tumors

**IFN-gamma resistance mechanisms in cancer:**
- **JAK1/JAK2 loss-of-function mutations:** Tumor cells with JAK1/JAK2 loss cannot respond to IFN-gamma → cannot upregulate MHC-I → resistant to CTL killing and to anti-PD-1 (because response to checkpoint blockade requires IFN-gamma signaling)
- **STAT1 loss or inactivation:** Less common than JAK loss
- **STATs transcriptional silencing:** DNMT3a → STATs promoter methylation → IFN-gamma unresponsiveness
- **IFNGR1/2 downregulation:** Reduced receptor surface expression; occurs in some tumors selected under immunotherapy pressure
- **IRF2 inactivation:** IRF2 (interferon regulatory factor 2) activates CXCL9/10 → IRF2 loss → T cell exclusion; IRF2BP2 → IRF2 → CXCL10 reduction in immune-excluded tumor phenotype

## Function

### IFN-gamma in anti-tumor immunity [^pitt-2016-ifng-cancer]

IFN-gamma is the central cytokine connecting innate immune recognition and adaptive tumor killing:

**"Hot" vs. "Cold" tumor paradigm:**
- **Hot tumors (IFN-gamma-rich):** High CXCL9/10/11, MHC-I/II, PD-L1; high TIL density; respond to anti-PD-1/PD-L1 therapy; the IFN-gamma signature is the strongest predictor of checkpoint blockade response across tumor types
- **Cold tumors (IFN-gamma-poor):** T cell excluded or depleted; low CXCL9/10; non-immunogenic; resist checkpoint blockade; strategies: STING agonists, oncolytic viruses, CXCL9/10 inducers to convert cold → hot

**IFN-gamma in checkpoint immunotherapy response:**
- Anti-PD-1/PD-L1 works by releasing IFN-gamma-producing T cells from PD-1-mediated exhaustion → restored IFN-gamma → MHC-I upregulation → tumor cell killing amplification → positive feedback loop
- **IFN-gamma resistance = checkpoint blockade resistance:** Tumors that acquire JAK1/JAK2 mutations or downregulate IFNGR cannot respond to IFN-gamma → MHC-I stays low → CTL cannot kill → acquired resistance to nivolumab, pembrolizumab
- IFN-gamma → PD-L1 upregulation (adaptive resistance) = why PD-L1 IHC is used as a predictive biomarker for PD-1 blockade response; PD-L1 expression is a surrogate marker for ongoing IFN-gamma signaling → immunologically active tumor microenvironment

**IFN-gamma in autoimmunity:**
- Type 1 diabetes: IFN-gamma-producing CD4+ Th1 and CD8+ CTLs infiltrate pancreatic islets → insulitis; IFN-gamma + iNOS in beta cells → NO-mediated injury
- Rheumatoid arthritis: IFN-gamma activates synovial macrophages → TNF-alpha, IL-6 → synovitis; JAK inhibitors (baricitinib, tofacitinib) broadly suppress IFN-gamma downstream signaling
- Systemic lupus: IFN-gamma levels correlate with SLE disease activity; paradoxically, type I IFNs (IFN-alpha) are the dominant drivers of SLE pathogenesis

**IFN-gamma in infectious disease:**
- Essential for defense against intracellular pathogens: Mycobacterium tuberculosis (IFN-gamma → iNOS → NO → bacterial killing; IFN-gamma-null mice succumb to TB rapidly), Salmonella, Toxoplasma gondii, Leishmania, Listeria
- **Hemophagocytic lymphohistiocytosis (HLH):** IFN-gamma storm (extreme elevation from uncontrolled T cell/NK cell activation) → macrophage activation syndrome → cytopenias, organ failure; emapalumab (anti-IFN-gamma antibody) approved for primary HLH
- **Secondary HLH / MAS (macrophage activation syndrome):** In sJIA, SLE, COVID-19, EBV; IFN-gamma blockade with emapalumab or JAK inhibitors

## Mechanism

### Therapeutic implications

**IFN-gamma as therapeutic target in HLH/MAS:**
- **Emapalumab (Gamifant, anti-IFN-gamma monoclonal antibody):** FDA approved 2018 for primary HLH refractory to standard therapy; blocks IFN-gamma → reduces macrophage hyperactivation → cytopenias, organ failure improvement

**IFN-gamma pathway modulation in autoimmunity:**
- JAK1/2 inhibitors (ruxolitinib, baricitinib) block IFNGR → JAK → STAT1 → broadly suppress IFN-gamma responses; approved for RA (baricitinib), MF (ruxolitinib), and JIA/pJIA; also used off-label for severe COVID-19 cytokine storm and MAS

**IFN-gamma as predictive biomarker:**
- IFN-gamma signature gene expression (CXCL9, CXCL10, IDO1, HLA-DRA, STAT1) — collectively the "IFN-gamma gene expression profile" — predicts response to pembrolizumab across tumor types; used in clinical decision-making for checkpoint inhibitor therapy (especially in MSS CRC, NSCLC without other biomarkers)

**IFN-gamma in cancer immunotherapy augmentation:**
- Recombinant IFN-gamma (Actimmune): Approved for chronic granulomatous disease (CGD) and severe malignant osteopetrosis; tried but modest effects in cancer (too toxic at doses needed)
- Engineering tumor-infiltrating T cells to produce more IFN-gamma (ACT strategies) and combining IFN-gamma pathway enhancers with checkpoint blockade are active areas

## Connections

- `connects-to` → **[JAK1/2](../jak1-2/README.md)** — IFN-gamma binds IFNGR1/2 → JAK1 and JAK2 transphosphorylation → STAT1 Tyr701 phosphorylation → STAT1 homodimers (GAF) → GAS elements → MHC-II, CXCL9/10/11, IDO1 transcription; JAK1/2 inhibitors potently block IFN-gamma signaling.
- `connects-to` → **[NLRP3 Inflammasome](../nlrp3-inflammasome/README.md)** — IFN-gamma primes NLRP3 inflammasome expression via STAT1 → transcriptional upregulation of NLRP3 and pro-IL-1beta; synergizes with LPS or ATP → amplified IL-1beta; IFN-gamma + NLRP3 cooperation amplifies inflammation in gout, atherosclerosis, and anti-tumor immunity.
- `connects-to` → **[NF-kB](../nf-kb/README.md)** — IFN-gamma activates NF-kB in macrophages via STAT1-IRF1 → iNOS, TNF-alpha, IL-12 → M1 macrophage polarization; IFN-gamma + TLR4 → synergistic NF-kB → M1 effector functions; sustained IFN-gamma + NF-kB drives macrophage-mediated autoimmune tissue injury.
- `connects-to` → **[MHC Class II](../mhc-class-ii/README.md)** — IFN-gamma is the dominant inducer of MHC class II expression via STAT1 → CIITA transcription → MHC-II on macrophages, DCs, and non-professional APCs; tumor cell MHC-II induction by IFN-gamma enables T helper cell recognition and anti-tumor immune activation.
- `connects-to` → **[Giant Cell Arteritis](../../07-system/giant-cell-arteritis/README.md)** — IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically.
- `connects-to` → **[IL-12](../il-12/README.md)** — IL-12 is the primary upstream inducer of IFN-γ: DC-derived IL-12 → JAK2/TYK2/STAT4 → T-bet → IFN-γ from NK cells and Th1 T cells; IFN-γ feeds back to induce more IL-12 from macrophages (positive amplification loop); IL-12 deficiency (IL12B, IL12RB1 mutations) causes MSMD with absent IFN-γ responses and susceptibility to mycobacteria.
- `connects-to` → **[Tuberculosis](../../07-system/tuberculosis/README.md)** — IFN-γ is the central effector cytokine for MTB control: activates macrophage bactericidal programs (phagosome acidification, NO, ROS, cathelicidin); IFN-γ from MTB-sensitised T cells in response to ESAT-6/CFP-10 is the molecular basis of IGRA diagnostic tests; IFNGR1/IFNGR2 mutations → MSMD with disseminated MTB/BCG disease.
- `connects-to` → **[Leishmaniasis](../../07-system/leishmaniasis/README.md)** — IFN-γ is the critical anti-Leishmania effector: Th1 CD4+ and NK cells produce IFN-γ → macrophage iNOS → NO → kills intracellular amastigotes; IFNGR1/2 deficiency (MSMD) → disseminated VL; IFN-γ is used adjunctively in refractory VL; IL-12 drives IFN-γ in Th1 priming.
- `connects-to` → **[STAT1](../stat1/README.md)** — IFN-γ → IFNGR1/2 → JAK1/JAK2 → STAT1 homodimer (GAF) → GAS elements → IRF1, iNOS, MHC-II; STAT1 GOF (R274Q, C324Y) → impaired Th17 → CMC; STAT1 LOF → MSMD — disseminated BCG and NTM; STAT1 is the non-redundant transducer of IFN-γ antimicrobial signaling.

[^schroder-2004-ifng-review]: Schroder K, Hertzog PJ, Ravasi T, Hume DA. Interferon-gamma: an overview of signals, mechanisms and functions. *J Leukoc Biol.* 2004;75(2):163-189. [doi:10.1189/jlb.0603252](https://doi.org/10.1189/jlb.0603252) · [PubMed 14525967](https://pubmed.ncbi.nlm.nih.gov/14525967/)
[^platanias-2005-jak-stat-ifn]: Platanias LC. Mechanisms of type-I- and type-II-interferon-mediated signalling. *Nat Rev Immunol.* 2005;5(5):375-386. [doi:10.1038/nri1604](https://doi.org/10.1038/nri1604) · [PubMed 15864272](https://pubmed.ncbi.nlm.nih.gov/15864272/)
[^pitt-2016-ifng-cancer]: Pitt JM, Vétizou M, Daillère R, et al. Resistance mechanisms to immune-checkpoint blockade in cancer: tumor-intrinsic and -extrinsic factors. *Immunity.* 2016;44(6):1255-1269. [doi:10.1016/j.immuni.2016.06.001](https://doi.org/10.1016/j.immuni.2016.06.001) · [PubMed 27332732](https://pubmed.ncbi.nlm.nih.gov/27332732/)
