---
schema: human-scale-entry/v1
id: il-33
name: IL-33
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-33 (IL33, chr9p24.1) is a nuclear alarmin of the IL-1 family released by necrotic barrier cells; ST2/IL-1RAcP → MyD88 → NF-κB activates ILC2 and mast cells; IL-33 drives asthma eosinophilia and the atopic march; serum sST2 (decoy receptor) predicts heart failure mortality."
aliases: ["IL-33", "interleukin-33", "IL33", "NF-HEV", "DVS27-related protein", "NFHEV"]
cross_links:
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "IL-33 from damaged bronchial epithelium → ST2+ ILC2 and mast cells → IL-5/IL-13 → eosinophilia and mucus; works synergistically with TSLP and IL-25 as the three-alarmin cascade; itepekimab (anti-IL-33) reduced asthma exacerbations in Phase 2/3 trials."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-33 from damaged keratinocytes → ST2+ mast cells and ILC2 → Th2 priming and histamine release; TSLP + IL-33 + IL-25 cooperate as the three-alarmin cascade; scratching-induced epidermal damage releases IL-33 from keratinocyte nuclei and amplifies itch-scratch cycles."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Serum soluble ST2 (sST2, decoy IL-33 receptor) >35 ng/mL predicts HF mortality independent of BNP; IL-33/ST2 signaling in cardiomyocytes is cardioprotective against pressure overload; sST2 is FDA-cleared for HF risk stratification and monitoring response to therapy."
sources:
  - id: schmitz-2005-il33
    type: peer-reviewed
    cite: "Schmitz J, Owyang A, Oldham E, et al. IL-33, an interleukin-1-like cytokine that signals via the IL-1 receptor-related protein ST2 and induces T helper type 2-associated cytokines. Immunity. 2005;23(5):479-490."
    doi: "10.1016/j.immuni.2005.09.015"
    pmid: "16286016"
    url: "https://doi.org/10.1016/j.immuni.2005.09.015"
  - id: wechsler-2021-itepekimab
    type: peer-reviewed
    cite: "Wechsler ME, Ruddy MK, Pavord ID, et al. Efficacy and Safety of Itepekimab in Patients with Moderate-to-Severe Asthma. N Engl J Med. 2021;385(18):1656-1668."
    doi: "10.1056/NEJMoa2024257"
    pmid: "34706177"
    url: "https://doi.org/10.1056/NEJMoa2024257"
---

# IL-33

## Overview

**Interleukin-33 (IL-33)** (gene *IL33*, chromosome 9p24.1) is a **nuclear alarmin** belonging to the IL-1 cytokine superfamily — constitutively expressed in the **nuclei of barrier epithelial cells** (keratinocytes, bronchial epithelium, intestinal epithelium, vascular endothelium) where it serves as a **sentinel danger signal** released upon cellular necrosis or barrier disruption. Unlike most secreted cytokines, IL-33 is NOT processed through the classical secretory pathway; instead, it is sequestered in the nucleus where it binds chromatin, and is released into the extracellular space upon **cell death, trauma, or mechanical damage** — a passive alarmin release mechanism shared with HMGB1 and IL-1α.

Once released, IL-33 signals through the **ST2/IL-1RAcP heterodimeric receptor** → MyD88 → IRAK4 → TRAF6 → NF-κB, activating ILC2 (type 2 innate lymphoid cells), mast cells, Th2 cells, and basophils to rapidly produce IL-5 and IL-13 — driving eosinophilia, mucus secretion, and the full type 2 allergic response **without requiring antigen-specific T cell priming**. This makes IL-33 a critical **initiator of innate type 2 immunity** alongside its partner alarmins TSLP and IL-25 (IL-17E).

**Two seemingly contradictory roles of IL-33/ST2 in different disease contexts:**
1. **Pro-allergic (epithelial contexts):** Released by damaged airway/skin epithelium → activates ILC2/mast cells → type 2 inflammation in asthma, atopic dermatitis, EoE
2. **Cardioprotective (cardiac context):** Cardiomyocyte-derived IL-33, signaling through transmembrane ST2 on cardiomyocytes and fibroblasts → anti-hypertrophic, anti-fibrotic effects; BUT **soluble ST2 (sST2)** acts as a decoy — sequesters IL-33 → prevents ST2 signaling → high sST2 = more HF mortality; this paradox explains why sST2 is a biomarker of worse outcomes despite cardioprotective IL-33/ST2 signaling

## Structure

**IL-33 protein isoforms:**
Full-length IL-33 is a **270-amino acid protein** with two functional domains:
- **N-terminal chromatin-binding domain (aa 1–111):** Contains an acidic LANA-like domain + homeodomain-like helix-turn-helix; binds histones H2A/H2B → chromatin association → nuclear retention in living cells; full-length IL-33 is constitutively active (biologically active without processing, unlike IL-1β)
- **C-terminal IL-1 superfamily cytokine domain (aa 112–270):** The β-trefoil fold characteristic of IL-1 family members; contains all receptor-binding determinants; active fragment is aa 99–270 or aa 109–270

**Processing — unique IL-33 biology:**
- **Caspase-3/7 cleavage** (at Asp178): produces inactive fragments — IL-33 is INACTIVATED by apoptotic caspases (opposite of IL-1β which requires caspase-1 for activation); this prevents pro-inflammatory IL-33 release during programmed apoptosis (homeostatic cell death)
- **Proteolytic activation by mast cell chymase and neutrophil elastase:** cleave IL-33 at aa 99–111 → 10–30× more potent mature fragments; relevant during allergic inflammation where mast cells are already activated
- **NLRP3 inflammasome / gasdermin D / pyroptosis:** IL-33 released during pyroptosis → most potent alarmin context in bacterial sepsis and viral infections
- **Mechanical release:** Exercise, stretch, injury → passive nuclear IL-33 release from necrotic epithelial cells

**ST2 receptor system:**
- **Transmembrane ST2 (ST2L; IL1RL1 gene, chr2q12.1):** IL-33-specific receptor chain; contains three extracellular Ig domains; forms heterodimer with IL-1RAcP (IL1RAP); signals via MyD88 → IRAK4 → TRAF6 → TAK1 → **NF-κB** + **MAPK (ERK, p38, JNK)**; IKK → IκBα phosphorylation → NF-κB nuclear translocation → IL-5, IL-13, IL-4, IL-6, GM-CSF gene transcription
- **Soluble ST2 (sST2):** Alternatively spliced shorter isoform; secreted; contains only the extracellular Ig domains (no TM or intracellular); acts as **decoy receptor** — binds IL-33 with affinity comparable to ST2L → prevents ST2L signaling; serum sST2 levels inversely predict IL-33 biological activity in heart tissue
- **IL-1RAcP (IL-1 receptor accessory protein):** Shared with IL-1α/β receptor (IL-1R1/IL-1RAcP) and IL-18 receptor (IL-18Rα/IL-18Rβ); constitutes the signaling competent heterodimer

## Function

**ILC2 activation (innate type 2 immunity):**
- ILC2 express the highest density of ST2 among immune cells; single IL-33 stimulus → ILC2 activation within minutes → **IL-5 + IL-13 + IL-9 + amphiregulin** secretion
- IL-33 + IL-25 + TSLP cooperate: IL-33 is most potent for ILC2 activation per se; IL-25 (IL-17E via IL-17RB/IL-17RA) preferentially induces ILC2 proliferation; TSLP activates DCs and extends ILC2 activity
- During viral respiratory infections (RSV, rhinovirus): epithelial necrosis → IL-33 → ILC2 → IL-5/IL-13 → eosinophilia despite no allergen — explains post-viral asthma exacerbations
- Exercise-induced asthma: mechanical airway stress → IL-33 → ILC2 → rapid bronchospasm onset

**Mast cell activation:**
- Mast cells express both ST2 and TSLPR; IL-33 alone → mast cell cytokine production without degranulation (non-degranulating activation pathway)
- IL-33 synergizes with IgE-mediated degranulation: IL-33 → PKC activation → lower threshold for FcεRI-triggered histamine release
- Chronic mast cell IL-33 exposure → increased FcεRI expression → sensitized to lower IgE concentrations

**Cardiac IL-33/ST2 biology:**
- Cardiac fibroblasts constitutively express and secrete IL-33 → paracrine signaling to adjacent cardiomyocytes
- **Cardiomyocyte ST2L signaling:** IL-33 → ST2L → IRAK4 → NF-κB → PI3K/Akt → **anti-apoptotic** (BCL-2 upregulation); also suppresses TGF-β/SMAD signaling in cardiomyocytes → **anti-hypertrophic** (PI3K/Akt → phospho-GATA4 inhibition); net: IL-33/ST2L is protective against hypertrophy and pressure-overload remodeling
- **Cardiac fibroblast ST2L signaling:** IL-33 → fibroblast ST2L → NF-κB → reduced TGF-β1 secretion → anti-fibrotic; IL-33 limits pathological collagen deposition post-myocardial infarction
- **Elevated sST2:** Released by cardiac fibroblasts under biomechanical stress (stretch → sST2 upregulation → sequesters IL-33 → less cardioprotective ST2L signaling); sST2 >35 ng/mL = 2-3× higher 1-year HF mortality in multiple cohorts; FDA-approved in vitro diagnostic (Presage ST2 assay)

**Helminth immunity (type 2 protective immunity):**
- Intestinal injury from helminths → IL-33 from epithelium → ILC2 → IL-4/IL-13 → tuft cell expansion → IL-25 amplification (tuft cell → IL-25 → ILC2 positive loop); goblet cell hyperplasia → mucus → parasite expulsion; basophil activation → anti-parasite antibodies
- IL-33 is the critical initiating signal for protective type 2 anti-helminth immunity; IL-33-deficient mice fail to expel Nippostrongylus brasiliensis or Trichuris muris

## Mechanism

**Itepekimab (anti-IL-33) in asthma [^wechsler-2021-itepekimab]:**
- Itepekimab (REGN3500/SAR440340): human IgG4 mAb; high-affinity IL-33 binding → blocks ST2 receptor interaction; co-developed by Regeneron and Sanofi
- **Phase 2b dose-finding trial (Wechsler et al. 2021):** 308 patients with moderate-severe asthma; itepekimab 75 or 300 mg SC Q2W; primary endpoint: loss-of-asthma-control events during steroid taper
- In patients NOT on background dupilumab: itepekimab 300 mg → **69% reduction** in loss-of-control events vs. placebo; eosinophils reduced ~50%, FeNO reduced ~35%
- In patients ON dupilumab + itepekimab: reduced efficacy (possible redundancy — dupilumab already suppresses IL-4/IL-13 downstream of IL-33)
- Phase 3 (NAVIGATOR-IL33) ongoing; FDA Breakthrough Therapy Designation

**Biomarker applications:**
- **Serum sST2 for HF:** Best HF risk in acute decompensated HF; sST2 >35 ng/mL → higher mortality in PRIDE study; complementary to BNP (different biology — BNP reflects hemodynamic stretch, sST2 reflects fibrosis/inflammation)
- **Serum sST2 with serial measurements:** Rising sST2 with HF therapy → may indicate treatment failure; normalization with sacubitril-valsartan and β-blockers correlates with improved HF outcomes
- **IL-33 in serum (active):** Difficult to measure reliably; bioactive IL-33 low in circulation due to rapid sST2 capture and proteolytic degradation; tissue IL-33 staining is more informative

## Connections

IL-33 from damaged bronchial epithelium → ST2+ ILC2 and mast cells → IL-5/IL-13 → eosinophilia and mucus; works synergistically with TSLP and IL-25 as the three-alarmin cascade; itepekimab (anti-IL-33) reduced asthma exacerbations in Phase 2/3 trials.

IL-33 from damaged keratinocytes → ST2+ mast cells and ILC2 → Th2 priming and histamine release; TSLP + IL-33 + IL-25 cooperate as the three-alarmin cascade; scratching-induced epidermal damage releases IL-33 from keratinocyte nuclei and amplifies itch-scratch cycles.

Serum soluble ST2 (sST2, decoy IL-33 receptor) >35 ng/mL predicts HF mortality independent of BNP; IL-33/ST2 signaling in cardiomyocytes is cardioprotective against pressure overload; sST2 is FDA-cleared for HF risk stratification and monitoring response to therapy.

[^schmitz-2005-il33]: Schmitz J, Owyang A, Oldham E, et al. IL-33, an interleukin-1-like cytokine that signals via the IL-1 receptor-related protein ST2 and induces T helper type 2-associated cytokines. *Immunity.* 2005;23(5):479-490. [doi:10.1016/j.immuni.2005.09.015](https://doi.org/10.1016/j.immuni.2005.09.015) · [PubMed 16286016](https://pubmed.ncbi.nlm.nih.gov/16286016/)
[^wechsler-2021-itepekimab]: Wechsler ME, Ruddy MK, Pavord ID, et al. Efficacy and Safety of Itepekimab in Patients with Moderate-to-Severe Asthma. *N Engl J Med.* 2021;385(18):1656-1668. [doi:10.1056/NEJMoa2024257](https://doi.org/10.1056/NEJMoa2024257) · [PubMed 34706177](https://pubmed.ncbi.nlm.nih.gov/34706177/)
