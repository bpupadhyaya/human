---
schema: human-scale-entry/v1
id: calr
name: CALR
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "CALR encodes calreticulin (ER chaperone); exon 9 frameshift mutations generate a novel C-terminus that activates MPL → constitutive JAK-STAT signaling; CALR mutations occur in ~25% ET and ~20-25% PMF; type 1 del52 → PMF phenotype; type 2 ins5 → ET phenotype."
aliases: ["CALR", "calreticulin", "CALR exon 9 mutation", "CALR type 1", "CALR type 2", "CALR MPN", "calreticulin MPN", "calreticulin myelofibrosis"]
sources:
  - id: klampfl-2013-calr
    type: peer-reviewed
    cite: "Klampfl T, Gisslinger H, Harutyunyan AS, et al. Somatic mutations of calreticulin in myeloproliferative neoplasms. N Engl J Med. 2013;369(25):2379-2390."
    doi: "10.1056/NEJMoa1311347"
    pmid: "24325356"
    url: "https://doi.org/10.1056/NEJMoa1311347"
  - id: nangalia-2013-calr
    type: peer-reviewed
    cite: "Nangalia J, Massie CE, Baxter EJ, et al. Somatic CALR mutations in myeloproliferative neoplasms with nonmutated JAK2. N Engl J Med. 2013;369(25):2391-2405."
    doi: "10.1056/NEJMoa1312542"
    pmid: "24325359"
    url: "https://doi.org/10.1056/NEJMoa1312542"
cross_links:
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F and CALR exon 9 mutations are mutually exclusive MPN drivers; CALR-mutant MPL activates JAK2 → downstream STAT5/STAT3 signaling; ruxolitinib (JAK1/2 inhibitor) is effective in both JAK2-mutant and CALR-mutant MPN."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "CALR-mutant calreticulin activates MPL receptor → JAK1/JAK2 heterodimerization → STAT5 phosphorylation → MPN proliferation; ruxolitinib (JAK1/2 inhibitor) reduces spleen volume and symptoms in CALR-mutant myelofibrosis similarly to JAK2 V617F disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "CALR-mutant MPL-JAK2 axis constitutively activates STAT3 and STAT5; STAT5 drives megakaryocyte proliferation and platelet hyperproduction in CALR-type 2 ET; STAT3 promotes cytokine-driven fibroblast activation and TGF-β production → bone marrow fibrosis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "JAK-STAT activation in CALR-mutant MPN cross-activates PI3K-AKT-mTOR; mTOR inhibition (everolimus) reduces megakaryocyte proliferation in MPN preclinically; mTOR pathway co-activation contributes to resistance to JAK inhibitor monotherapy in myelofibrosis."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "CALR-mutant calreticulin gains a positively charged C-terminal peptide that aberrantly binds MPL (thrombopoietin receptor) ECD → constitutive MPL dimerization → JAK2-STAT5 activation without TPO; this CALR-mutant:MPL interaction is the oncogenic mechanism of CALR-mutant MPN."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "CALR type 1 (del52bp) drives PMF-like myelofibrosis; CALR-mutant megakaryocytes produce TGF-β → bone marrow fibrosis; ruxolitinib reduces spleen volume comparably to JAK2 V617F MF; CALR type 1 carries higher AML transformation risk (~12-15% at 15y) than type 2."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "CALR type 2 (ins5bp) drives ET-like phenotype with isolated thrombocytosis; CALR mutations are found in ~25% of ET (vs JAK2 V617F ~55%); CALR-mutant ET has lower cardiovascular risk than JAK2-mutant ET (no erythrocytosis); CALR VAF monitoring guides cytoreduction decisions."
---

# CALR

## Overview

**CALR (Calreticulin)** is a multifunctional ER-resident chaperone protein ubiquitously expressed across human tissues, responsible for glycoprotein quality control, calcium homeostasis, and immune peptide loading onto MHC class I molecules. In 2013, two independent groups simultaneously discovered that **somatic exon 9 frameshift mutations** in CALR are the driver mutation in the majority of JAK2-wild-type essential thrombocythemia (ET) and primary myelofibrosis (PMF), establishing CALR as the second major driver of myeloproliferative neoplasms (MPN) after JAK2 V617F [^klampfl-2013-calr][^nangalia-2013-calr]. Unlike CALR's normal function as a chaperone, CALR mutant proteins gain a novel C-terminal positively charged peptide sequence that specifically and aberrantly binds the extracellular domain of **MPL (thrombopoietin receptor)** → constitutive JAK2-STAT5 activation → megakaryocyte/platelet clonal expansion without thrombopoietin (TPO) ligand. CALR mutations are detected in **~25% of ET** and **~20-25% of PMF**; they are notably absent in polycythemia vera (PV), where JAK2 V617F is essentially universal.

**CALR mutation landscape in MPN:**
- **Essential thrombocythemia (ET):** JAK2 V617F ~55%, CALR ~25%, MPL ~3%, triple-negative ~17%
- **Primary myelofibrosis (PMF):** JAK2 V617F ~60%, CALR ~20-25%, MPL ~8%, triple-negative ~8-10%
- **Polycythemia vera (PV):** JAK2 V617F >99%; CALR absent
- **Post-ET/Post-PV MF:** CALR-driven ET transforms to MF at lower rates than JAK2-driven ET; CALR type 1 specifically associated with PMF phenotype and MF transformation risk

## Structure

### Calreticulin protein architecture

Wild-type calreticulin is a 417-amino-acid, 46 kDa ER-lumenal protein with three structural domains:

**N-domain (1-180, globular lectin-like):**
- Conserved N-terminal signal peptide (cleaved); forms compact β-sandwich fold
- Lectin binding site for mono-glucosylated N-linked glycans (Glc₁Man₅-9GlcNAc₂) on unfolded glycoproteins → calreticulin cycle with calnexin for glycoprotein quality control
- Contains two Zn²⁺-binding sites that modulate chaperone activity
- Exon 9 frameshift mutations affect the C-domain boundary region encoded downstream

**P-domain (180-290, proline-rich arm):**
- Extended hairpin structure; interacts with ERp57 (disulfide isomerase) → coordinates oxidative folding of glycoproteins; contains high-affinity Ca²⁺-binding sites (Kd ~1 μM)

**C-domain (290-417, acidic Ca²⁺-binding):**
- Intrinsically disordered; contains poly-Asp/Glu Ca²⁺-binding motifs (Kd ~1 mM; high capacity); ER retention signal KDEL at C-terminus
- **Exon 9 frameshift mutations occur in the C-domain coding region (aa 367-417):** The frameshift deletes the poly-Asp/Glu region and KDEL → replaces with novel positively charged peptide (net charge ~+22 to +30) → this unique C-terminus mediates aberrant MPL binding

### Exon 9 mutation types

**Type 1 mutation (del52bp, c.1092_1143del, L367fs*46):**
- 52-bp deletion in exon 9 → frameshift → novel 46-aa C-terminal peptide; positive-charge net ~+32
- **Clinical phenotype: PMF-like** — higher megakaryocyte clustering, higher fibrosis grade, higher AML transformation risk (~12-15% at 15 years) vs. type 2
- Stronger MPL activation than type 2; more potent HSC self-renewal
- Most common type in PMF; ~50% of all CALR mutations

**Type 2 mutation (ins5bp, c.1154_1155insTTGTC, K385fs*47):**
- 5-bp insertion in exon 9 → frameshift → novel 47-aa C-terminal peptide; net charge ~+22
- **Clinical phenotype: ET-like** — isolated thrombocytosis; lower fibrosis risk; better prognosis
- Most common type in ET; ~30% of all CALR mutations
- 5-year overall survival equivalent to JAK2-mutant ET; lower cardiovascular event rate than JAK2 V617F ET (no erythrocytosis)

**Other mutations (type 3-5 and rare):**
- ~15-20% of CALR mutations; all produce the positively charged novel C-terminus; most cluster near type 1/2 biologically; clinical phenotypes intermediate

### CALR mutant protein mechanism of MPL activation

1. CALR mutant protein is expressed in ER lumen but escapes quality control (truncated KDEL → reduced ER retention)
2. CALR mutant transits to Golgi and is secreted and/or displayed on cell surface
3. Positively charged novel C-terminal peptide directly contacts the extracellular domain of MPL (thrombopoietin receptor) → forms stable CALR-mutant:MPL complex
4. CALR-mutant:MPL complex dimerizes → conformational change mimics TPO-bound MPL → constitutive JAK2 activation → STAT5 phosphorylation → megakaryocyte proliferation, platelet production, and HSC self-renewal without TPO ligand
5. This interaction is **CALR-mutant-specific** (wild-type CALR does not activate MPL); driven entirely by the novel C-terminal peptide
6. CALR-mutant:MPL complex is immunogenic → can be targeted by antibodies or vaccines (clinical trials underway)

## Function

### Normal calreticulin roles

**Glycoprotein quality control (calreticulin-calnexin cycle):**
Newly synthesized N-linked glycoproteins in ER are modified to Glc₁Man₉GlcNAc₂ by glucosidase II → recognized by calreticulin (soluble) and calnexin (membrane) lectin domains → ERp57 oxidizes disulfide bonds → correctly folded glycoproteins released; misfolded glycoproteins retained and re-glucosylated by UGGT → recycled through chaperone cycle until folded or targeted for ERAD.

**Calcium homeostasis:**
Calreticulin is the major Ca²⁺ buffer in the ER lumen (stores ~50% of ER Ca²⁺); P-domain: high-affinity/low-capacity; C-domain: low-affinity/high-capacity; regulates ER Ca²⁺ release via IP₃R and SERCA pump interactions; cytosolic Ca²⁺ transients that drive cellular signaling.

**MHC class I peptide loading:**
Calreticulin participates in the peptide-loading complex (PLC: TAP1/2 + tapasin + ERp57 + calreticulin) → calreticulin stabilizes empty MHC class I molecules → peptide loaded → calreticulin released → MHC class I-peptide complex exported to cell surface. Calreticulin exposure on the surface of stressed/dying cells (immunogenic cell death) acts as an "eat me" signal for dendritic cells → promotes anti-tumor immunity.

### Hematopoietic progenitor effects of CALR mutations

**Megakaryocyte bias:** CALR-mutant MPL-JAK2-STAT5 constitutively activates megakaryocyte progenitor (MkP) proliferation → thrombocytosis (platelets often >600-1000×10⁹/L in ET); CALR-mutant megakaryocytes are hyperlobulated and hypersegmented.

**HSC self-renewal:** CALR-mutant HSCs have competitive advantage over wild-type HSCs in mouse transplant models; type 1 CALR confers greater self-renewal than type 2 → explains higher PMF penetrance with type 1.

**Immune evasion:** CALR-mutant cells express less surface calreticulin than expected (mutant protein sequestered by MPL binding) → may reduce immunogenic cell death signaling; paradoxically, CALR-mutant peptides are immunogenic → cytotoxic T-cell responses detectable in patients.

## Mechanism

### CALR mutations as therapeutic targets

**JAK inhibitors (indirect CALR targeting):**
CALR-mutant MPN is fully dependent on JAK2 downstream signaling → ruxolitinib (JAK1/2 inhibitor) reduces spleen volume ~42% and improves symptoms in CALR-mutant MF comparably to JAK2-mutant MF (COMFORT trials; CALR subgroups had comparable response rates); ruxolitinib does NOT eradicate the CALR clone.

**Allele burden monitoring:**
CALR exon 9 mutation allele burden (variant allele frequency, VAF) is tracked by digital PCR or NGS; declining VAF correlates with response; rising VAF predicts progression; CALR VAF monitoring is integral to MPN treatment response assessment.

**CALR-specific immunotherapy (investigational):**
- CALR-mutant C-terminal peptide is a tumor-specific neoantigen → CD4+ and CD8+ T cells recognizing CALR-mutant peptides detectable in ~50% of patients
- CALR mutant-specific vaccines (SL-401 derivative, peptide vaccines) in early trials
- Anti-CALR-mutant:MPL complex antibodies: preclinical activity; induce apoptosis of CALR-mutant MPN cells
- CAR-T targeting CALR-mutant:MPL complex: preclinical concept

**Combination strategies:**
- Ruxolitinib + navitoclax (BCL-2/BCL-XL inhibitor): REFINE trial; platelet-sparing dose found; CALR-mutant MF included; SVR35 ~63% vs ruxolitinib monotherapy ~38%
- Ruxolitinib + pelabresib (BET inhibitor): MANIFEST-2; primary endpoint SVR35 met; CALR-mutant subgroup benefit
- Imetelstat (telomerase inhibitor): IMpact-MF trial for ruxolitinib-relapsed MF; CALR-mutant subset

**Prognosis:**
- CALR type 1: adverse prognosis within CALR-mutant MPN (closer to JAK2 V617F MF); higher MF transformation, higher AML risk
- CALR type 2: favorable; ET prognosis comparable to JAK2 V617F ET
- High-risk co-mutations (ASXL1, SRSF2, IDH1/2, EZH2) — "MIPSS70" molecular adverse factors — worsen CALR-mutant MF prognosis; indicate earlier allo-SCT consideration

## Connections

- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F and CALR exon 9 mutations are mutually exclusive MPN drivers; CALR-mutant MPL activates JAK2 → downstream STAT5/STAT3 signaling; ruxolitinib (JAK1/2 inhibitor) is effective in both JAK2-mutant and CALR-mutant MPN.
- `connects-to` → **[JAK1-2](../../03-molecular/jak1-2/README.md)** — CALR-mutant calreticulin activates MPL receptor → JAK1/JAK2 heterodimerization → STAT5 phosphorylation → MPN proliferation; ruxolitinib (JAK1/2 inhibitor) reduces spleen volume and symptoms in CALR-mutant myelofibrosis similarly to JAK2 V617F disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — CALR-mutant MPL-JAK2 axis constitutively activates STAT3 and STAT5; STAT5 drives megakaryocyte proliferation and platelet hyperproduction in CALR-type 2 ET; STAT3 promotes cytokine-driven fibroblast activation and TGF-β production → bone marrow fibrosis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — JAK-STAT activation in CALR-mutant MPN cross-activates PI3K-AKT-mTOR; mTOR inhibition (everolimus) reduces megakaryocyte proliferation in MPN preclinically; mTOR pathway co-activation contributes to resistance to JAK inhibitor monotherapy in myelofibrosis.
- `connects-to` → **[MPL](../mpl/README.md)** — CALR-mutant calreticulin gains a positively charged C-terminal peptide that aberrantly binds MPL (thrombopoietin receptor) ECD → constitutive MPL dimerization → JAK2-STAT5 activation without TPO; this CALR-mutant:MPL interaction is the oncogenic mechanism of CALR-mutant MPN.
- `connects-to` → **[Myelofibrosis](../../07-system/myelofibrosis/README.md)** — CALR type 1 (del52bp) drives PMF-like myelofibrosis; CALR-mutant megakaryocytes produce TGF-β → bone marrow fibrosis; ruxolitinib reduces spleen volume comparably to JAK2 V617F MF; CALR type 1 carries higher AML transformation risk (~12-15% at 15y) than type 2.
- `connects-to` → **[Essential Thrombocythemia](../../07-system/essential-thrombocythemia/README.md)** — CALR type 2 (ins5bp) drives ET-like phenotype with isolated thrombocytosis; CALR mutations are found in ~25% of ET (vs JAK2 V617F ~55%); CALR-mutant ET has lower cardiovascular risk than JAK2-mutant ET (no erythrocytosis); CALR VAF monitoring guides cytoreduction decisions.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^klampfl-2013-calr]: Klampfl T, Gisslinger H, Harutyunyan AS, et al. Somatic mutations of calreticulin in myeloproliferative neoplasms. *N Engl J Med.* 2013;369(25):2379-2390. [doi:10.1056/NEJMoa1311347](https://doi.org/10.1056/NEJMoa1311347) · [PubMed 24325356](https://pubmed.ncbi.nlm.nih.gov/24325356/)
[^nangalia-2013-calr]: Nangalia J, Massie CE, Baxter EJ, et al. Somatic CALR mutations in myeloproliferative neoplasms with nonmutated JAK2. *N Engl J Med.* 2013;369(25):2391-2405. [doi:10.1056/NEJMoa1312542](https://doi.org/10.1056/NEJMoa1312542) · [PubMed 24325359](https://pubmed.ncbi.nlm.nih.gov/24325359/)
