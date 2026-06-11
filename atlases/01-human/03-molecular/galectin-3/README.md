---
schema: human-scale-entry/v1
id: galectin-3
name: Galectin-3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Galectin-3 (LGALS3) is a β-galactoside lectin secreted by macrophages driving TGF-β-amplified cardiac and hepatic fibrosis; elevated serum galectin-3 predicts HFpEF, HF mortality, and NASH fibrosis stage; galectin-3 inhibitors (belapectin) are in Phase 2 trials."
aliases: ["galectin-3", "LGALS3", "Mac-2", "CBP35", "galactose-binding lectin", "galectin", "fibrosis biomarker", "MFC", "modified citrus pectin"]
cross_links:
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Galectin-3 secreted by cardiac macrophages activates cardiac fibroblasts → collagen synthesis → myocardial fibrosis and diastolic dysfunction; serum galectin-3 ≥17.8 ng/mL is an FDA-approved HF biomarker predicting mortality; galectin-3 predicts incident HFpEF."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Galectin-3 is secreted by activated Kupffer cells and hepatic macrophages → activates stellate cells and promotes TGF-β-driven fibrosis; serum galectin-3 correlates with NASH fibrosis stage (F2-F4); galectin-3 inhibition (GR-MD-02) reduced fibrosis in Phase 2 NASH trials."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Galectin-3 amplifies TGF-β fibrogenic signaling: galectin-3 binds TGF-β receptors → enhances SMAD2/3 phosphorylation; galectin-3-knockout mice show reduced TGF-β-driven fibrosis; galectin-3 also promotes myofibroblast differentiation independently of canonical TGF-β/SMAD."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Galectin-3 activates macrophage NLRP3 inflammasome via lysosomal damage → IL-1β secretion; conversely, IL-1β promotes galectin-3 secretion — positive feedback loop; galectin-3 integrates DAMP sensing with fibrosis in chronic inflammatory organ damage."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Galectin-3 activates macrophage NF-κB → TNF-α secretion; TNF-α induces galectin-3 transcription → feedforward amplification in chronic inflammatory fibrosis; galectin-3+TNF-α co-elevation predicts worse HF and NASH outcomes; galectin-3 inhibitors reduce TNF-α in fibrosis models."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Galectin-3 promotes adipose macrophage crown-like structures → chronic inflammation → insulin resistance, opposing adiponectin; galectin-3 KO mice are protected from high-fat diet-induced adipose fibrosis; galectin-3:adiponectin ratio tracks metabolic syndrome and NASH severity."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Galectin-3 drives cross-organ fibrosis: macrophage-secreted galectin-3 → integrin αvβ6 → TGF-β activation → myofibroblast → ECM deposition; drives cardiac, hepatic, renal, and pulmonary fibrosis; galectin-3 KO mice show reduced fibrosis across multiple organ injury models."
sources:
  - id: de-boer-2011-galectin3-hf
    type: peer-reviewed
    cite: "de Boer RA, Lok DJ, Jaarsma T, et al. Predictive value of plasma galectin-3 levels in heart failure with reduced and preserved ejection fraction. Ann Med. 2011;43(1):60-68."
    doi: "10.3109/07853890.2010.538080"
    pmid: "21189092"
    url: "https://doi.org/10.3109/07853890.2010.538080"
  - id: sharma-2004-galectin3-fibrosis
    type: peer-reviewed
    cite: "Sharma UC, Pokharel S, van Brakel TJ, et al. Galectin-3 marks activated macrophages in failure-prone hypertrophied hearts and contributes to cardiac dysfunction. Circulation. 2004;110(19):3121-3128."
    doi: "10.1161/01.CIR.0000147181.65298.4D"
    pmid: "15520318"
    url: "https://doi.org/10.1161/01.CIR.0000147181.65298.4D"
---

# Galectin-3

## Overview

**Galectin-3** (gene *LGALS3*, chromosome 14q22.3; also Mac-2, CBP35) is a **25 kDa β-galactoside-binding lectin** — the only chimeric galectin, combining an N-terminal regulatory domain with a C-terminal carbohydrate recognition domain (CRD). It is secreted by **activated macrophages, monocytes, and fibroblasts** in response to tissue injury and is the **principal galectin mediating organ fibrosis**.

Unlike most lectins (which are typically intracellular or membrane-anchored), galectin-3 is unusual in its ability to:
1. Exist intracellularly (nucleus, cytoplasm) — where it modulates apoptosis (anti-apoptotic, binds Bcl-2)
2. Be secreted by a non-classical pathway into the extracellular space
3. Act as a soluble bridging molecule — binding glycosylated receptors on multiple cell types simultaneously (galectin-3 lattice formation)

**Galectin-3 as a cardiac biomarker:**
The FDA cleared galectin-3 in 2010 as a biomarker for risk stratification in acute decompensated and chronic heart failure. A serum galectin-3 ≥17.8 ng/mL (or >25.9 ng/mL in some cutoffs) is associated with elevated 60-day and 1-year mortality in HF patients across HFrEF and HFpEF phenotypes [^de-boer-2011-galectin3-hf]. Unlike NT-proBNP (which reflects hemodynamic load), galectin-3 primarily reflects **fibrotic activity** — making it a complementary rather than redundant biomarker in HF management.

**Galectin-3 inhibitors in development:**
- **Modified citrus pectin (MFC/GCS-100):** Polysaccharide-based galectin-3 inhibitor; anti-fibrotic in CKD (COMET trial data mixed); early HF data
- **Belapectin (GR-MD-02):** Galactosylated polysaccharide IV infusion; Phase 2 NASH (NASH-CX trial): did not meet primary fibrosis endpoint overall, but reduced portal hypertension and cirrhosis complications in the non-varices subgroup
- **GB0139 (TD139):** Inhaled galectin-3 inhibitor for idiopathic pulmonary fibrosis — Phase 2 showed biomarker reduction

## Structure

Galectin-3 is the only **chimeric galectin** with a unique bipartite structure:

**N-terminal domain (NTD; ~12 kDa):**
- Contains 9 repeats of a proline-glycine-alanine (PGA) collagen-like motif → enables self-aggregation at physiological concentrations
- Facilitates galectin-3 oligomerization (pentamers and higher-order lattices) → crosslinks glycoproteins → stable cell-surface patches
- Target of MMP cleavage (MMP-2, -9, -14 nick the NTD → releases CRD from oligomerization)

**C-terminal carbohydrate recognition domain (CRD; ~13 kDa):**
- β-sandwich fold (Trp-His-Arg-Leu-Tyr residues form the canonical galactose-binding site)
- Binds terminal β-galactosides with highest affinity for LacNAc (N-acetyllactosamine) on N- and O-linked glycans
- Key interacting glycoproteins: integrin αvβ6, TGF-β receptor, fibronectin, laminin, AGEs (via galactose-containing AGE glycoforms), MUC1/5B

**Oligomerization and lattice formation:**
- At extracellular concentrations (>1 μM), galectin-3 forms **pentamers** (5:1 complex via NTD interactions) → can crosslink up to 5 different glycoproteins simultaneously → receptor clustering → sustained signaling
- Galectin-3 lattices regulate receptor endocytosis (slow it down → prolonged surface signaling), which amplifies TGF-β receptor and integrin αvβ6 pro-fibrotic signaling

## Function

**Pro-fibrotic functions:**
- **Macrophage secretion → fibroblast activation:** Tissue-injured macrophages (M2-like, alternatively activated) secrete galectin-3 → galectin-3 binds integrin αvβ6 on quiescent fibroblasts → αvβ6 activates latent TGF-β → SMAD2/3 → myofibroblast differentiation → collagen I/III synthesis → fibrosis
- **Direct fibroblast activation:** Galectin-3 → PI3K → Akt → mTORC1 → protein synthesis → collagen mRNA translation (SMAD-independent pathway)
- **Cardiac fibrosis:** Galectin-3 from cardiac macrophages drives myocardial fibrosis → reduced compliance → diastolic dysfunction → HFpEF; treatment with anti-galectin-3 antibodies or modified citrus pectin reduces cardiac fibrosis in pressure overload models [^sharma-2004-galectin3-fibrosis]

**Inflammatory functions:**
- **Macrophage NLRP3 activation:** Galectin-3 binds and damages lysosomes → cathepsin B leak → NLRP3 assembly → IL-1β; conversely, galectin-3 can signal through TLR4 → NF-κB → galectin-3 gene transcription (autocrine amplification)
- **Neutrophil chemoattractant:** Galectin-3 gradients recruit neutrophils via Mac-1 (CD11b/CD18) binding
- **Mast cell degranulation:** Galectin-3 binds IgE-FcεRI complexes on mast cells → triggers degranulation independent of IgE cross-linking (relevant in allergy and tissue fibrosis)

**Anti-apoptotic functions (intracellular):**
- Nuclear galectin-3 → binds Bcl-2 homologue proteins → prevents cytochrome c release → blocks apoptosis
- Galectin-3 is upregulated in many cancers → promotes tumor survival, proliferation, and metastasis (tumor cell galectin-3 binds T cell surface glycans → T cell apoptosis → immune evasion)

**Metabolic functions:**
- In adipose tissue: galectin-3 promotes crown-like structure formation and adipose macrophage activation → chronic low-grade inflammation → insulin resistance
- Galectin-3 knockout mice are protected from high-fat diet-induced adipose fibrosis and metabolic syndrome

## Mechanism

**Galectin-3 in heart failure — cardiac fibrosis pathway:**

1. Chronic pressure overload (hypertension, AS) or volume overload (MR, DCM) → mechanical stress → cardiac macrophage activation
2. Activated M2-like cardiac macrophages secrete galectin-3 into myocardial interstitium
3. Galectin-3 → integrin αvβ6 on cardiac fibroblasts → αvβ6 cleaves LAP (latency-associated peptide) from large latent TGF-β complex → active TGF-β1 release
4. TGF-β1 → SMAD2/3 → collagen I, III, fibronectin, and tissue inhibitor of metalloproteinases (TIMP-1) → ECM deposition
5. Galectin-3 also directly activates cardiac fibroblast Akt/mTOR → enhanced collagen translation
6. Interstitial fibrosis → impaired LV relaxation → elevated LVEDP → HFpEF phenotype
7. Serum galectin-3 levels reflect the cardiac fibrotic burden → biomarker for HFpEF risk and prognosis

**Galectin-3 in HFpEF vs. HFrEF:**
- HFpEF: galectin-3 is particularly elevated (reflects the predominantly fibrotic/stiff phenotype); predicts outcomes better than in HFrEF; limited therapeutic targets for HFpEF make galectin-3 inhibition attractive
- HFrEF: galectin-3 still elevated but NT-proBNP/BNP are the primary hemodynamic markers; galectin-3 adds prognostic value as a fibrosis-specific marker independent of loading conditions

**Galectin-3 in liver fibrosis (NASH):**
1. Lipotoxic hepatocytes → HMGB1/DAMPs → Kupffer cell M2 activation → galectin-3 secretion
2. Galectin-3 → hepatic stellate cell (HSC) → integrin αvβ6 → TGF-β activation → stellate cell → α-SMA, collagen I deposition
3. Galectin-3 reinforces the NASH inflammatory→fibrotic progression independently of adiponectin/leptin pathways
4. Galectin-3 serum levels correlate with NASH NAS and fibrosis stage (ROC AUC 0.65-0.75 for F2+ fibrosis); combined with serum CK18 fragments improves non-invasive fibrosis assessment
5. **Belapectin (GR-MD-02, NASH-CX trial):** IV galectin-3 inhibitor; Phase 2 → no benefit on primary histologic endpoints; reduced portal hypertension events in patients without esophageal varices at baseline — possible niche indication for portal hypertension prevention

## Connections

- `connects-to` → **[Heart Failure](../../07-system/heart-failure/README.md)** — Galectin-3 secreted by cardiac macrophages activates cardiac fibroblasts → collagen synthesis → myocardial fibrosis and diastolic dysfunction; serum galectin-3 ≥17.8 ng/mL is an FDA-approved HF biomarker predicting mortality; galectin-3 predicts incident HFpEF.
- `connects-to` → **[NASH](../../07-system/nash/README.md)** — Galectin-3 is secreted by activated Kupffer cells and hepatic macrophages → activates stellate cells and promotes TGF-β-driven fibrosis; serum galectin-3 correlates with NASH fibrosis stage (F2-F4); galectin-3 inhibition (GR-MD-02) reduced fibrosis in Phase 2 NASH trials.
- `connects-to` → **[TGF-β](../tgf-beta/README.md)** — Galectin-3 amplifies TGF-β fibrogenic signaling: galectin-3 binds TGF-β receptors → enhances SMAD2/3 phosphorylation; galectin-3-knockout mice show reduced TGF-β-driven fibrosis; galectin-3 also promotes myofibroblast differentiation independently of canonical TGF-β/SMAD.
- `connects-to` → **[NLRP3 Inflammasome](../nlrp3-inflammasome/README.md)** — Galectin-3 activates macrophage NLRP3 inflammasome via lysosomal damage → IL-1β secretion; conversely, IL-1β promotes galectin-3 secretion — positive feedback loop; galectin-3 integrates DAMP sensing with fibrosis in chronic inflammatory organ damage.
- `connects-to` → **[TNF-α](../tnf-alpha/README.md)** — Galectin-3 activates macrophage NF-κB → TNF-α secretion; TNF-α induces galectin-3 transcription → feedforward amplification in chronic inflammatory fibrosis; galectin-3+TNF-α co-elevation predicts worse HF and NASH outcomes; galectin-3 inhibitors reduce TNF-α in fibrosis models.
- `connects-to` → **[Adiponectin](../adiponectin/README.md)** — Galectin-3 promotes adipose macrophage crown-like structures → chronic inflammation → insulin resistance, opposing adiponectin; galectin-3 KO mice are protected from high-fat diet-induced adipose fibrosis; galectin-3:adiponectin ratio tracks metabolic syndrome and NASH severity.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Galectin-3 drives cross-organ fibrosis: macrophage-secreted galectin-3 → integrin αvβ6 → TGF-β activation → myofibroblast → ECM deposition; drives cardiac, hepatic, renal, and pulmonary fibrosis; galectin-3 KO mice show reduced fibrosis across multiple organ injury models.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^de-boer-2011-galectin3-hf]: de Boer RA, Lok DJ, Jaarsma T, et al. Predictive value of plasma galectin-3 levels in heart failure with reduced and preserved ejection fraction. *Ann Med.* 2011;43(1):60-68. [doi:10.3109/07853890.2010.538080](https://doi.org/10.3109/07853890.2010.538080) · [PubMed 21189092](https://pubmed.ncbi.nlm.nih.gov/21189092/)
[^sharma-2004-galectin3-fibrosis]: Sharma UC, Pokharel S, van Brakel TJ, et al. Galectin-3 marks activated macrophages in failure-prone hypertrophied hearts and contributes to cardiac dysfunction. *Circulation.* 2004;110(19):3121-3128. [doi:10.1161/01.CIR.0000147181.65298.4D](https://doi.org/10.1161/01.CIR.0000147181.65298.4D) · [PubMed 15520318](https://pubmed.ncbi.nlm.nih.gov/15520318/)
