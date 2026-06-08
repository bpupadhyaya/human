---
schema: human-scale-entry/v1
id: ige
name: IgE
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IgE is the lowest-abundance but highest-affinity immunoglobulin; allergen-specific IgE binds FcεRI on mast cells → cross-linking by allergen → degranulation → histamine, leukotrienes, and PGD2; omalizumab (anti-IgE) reduces severe allergic asthma exacerbations and anaphylaxis."
aliases: ["IgE", "immunoglobulin E", "IGHE", "FcεRI", "FcεRII", "CD23", "omalizumab", "anti-IgE", "allergic sensitization", "atopic", "anaphylaxis"]
cross_links:
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Allergen-specific IgE binds FcεRI on airway mast cells → allergen cross-linking → degranulation → acute bronchoconstriction; omalizumab (anti-IgE mAb) binds free IgE → reduces FcεRI expression → 26-50% fewer exacerbations in severe allergic asthma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "IgE bound to FcεRI on mast cells persists for weeks-months (sensitized mast cell); allergen cross-links IgE → Syk/Lyn kinase → Ca2+ release → degranulation (histamine, heparin, tryptase) + prostaglandin and leukotriene synthesis; FcεRI density is upregulated by IgE itself."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "IgE-mediated mast cell degranulation releases histamine → H1R bronchoconstriction, vasodilation, and pruritus; H1 antihistamines relieve allergic rhinitis and urticaria; in asthma, histamine is one of several bronchoconstricting mediators alongside leukotrienes and PGD2."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "IgE-mediated mast cell activation → phospholipase A2 → arachidonic acid → COX → PGD2 (major mast cell prostanoid); PGD2 → DP1/CRTH2 receptors → bronchoconstriction, eosinophil recruitment, and mucus secretion; PGD2 mediates the late-phase allergic response."
sources:
  - id: gould-2008-ige-review
    type: peer-reviewed
    cite: "Gould HJ, Sutton BJ. IgE in allergy and asthma today. Nat Rev Immunol. 2008;8(3):205-217."
    doi: "10.1038/nri2273"
    pmid: "18301424"
    url: "https://doi.org/10.1038/nri2273"
  - id: busse-2001-omalizumab
    type: peer-reviewed
    cite: "Busse W, Corren J, Lanier BQ, et al. Omalizumab, anti-IgE recombinant humanized monoclonal antibody, for the treatment of severe allergic asthma. J Allergy Clin Immunol. 2001;108(2):184-190."
    doi: "10.1067/mai.2001.117880"
    pmid: "11496232"
    url: "https://doi.org/10.1067/mai.2001.117880"
---

# IgE

## Overview

**IgE** (immunoglobulin E; gene cluster *IGHE* at chromosome 14q32.33 in the immunoglobulin heavy chain locus) is the **least abundant immunoglobulin in circulation** (~100–400 ng/mL, normal serum total IgE <100 kIU/L) yet mediates some of the most potent immune responses known. IgE is the principal antibody isotype of **type 2 (allergic) immunity**, evolved for helminth defense but pathologically activated against environmental allergens (pollen, dust mite, food proteins, insect venom) in atopic individuals.

The critical feature of IgE biology is its **exceptionally high-affinity binding to FcεRI** (the high-affinity IgE receptor; Kd ~10⁻¹⁰ M — 1000× tighter than IgG-FcγR interactions) on **mast cells and basophils**. This allows minuscule amounts of allergen-specific IgE to sensitize mast cells for months; subsequent allergen exposure cross-links FcεRI-bound IgE → immediate mast cell degranulation → **allergic reaction** (asthma, rhinitis, urticaria, anaphylaxis). Omalizumab (Xolair) — a humanized anti-IgE monoclonal antibody — binds the Cε3 domain (FcεRI-binding site) of free IgE → prevents FcεRI loading → reduces mast cell sensitivity → FDA approved for severe allergic asthma and chronic idiopathic urticaria [^busse-2001-omalizumab].

**Conditions associated with elevated IgE:**

| Condition | IgE level | Mechanism |
|---|---|---|
| Atopic asthma | ↑ (100–1000 kIU/L) | Allergen-driven Th2 → B cell IgE class switch |
| Atopic dermatitis | ↑↑ | IL-4/IL-13-driven; barrier defect → sensitization |
| Allergic rhinitis | ↑ | Mucosal IgE; local FcεRI activation |
| Food allergy | ↑ | Gut barrier dysfunction; food antigen sensitization |
| Helminth infection | ↑↑↑ (>1000 kIU/L) | Th2/ILC2 response; protective against parasites |
| Hyper-IgE syndrome | ↑↑↑↑ (>2000 kIU/L) | STAT3 (AD-HIES) or DOCK8 mutations |
| IgE myeloma | ↑ (monoclonal) | Rare plasma cell neoplasm; <0.1% of myeloma |

## Structure

IgE is a **monomeric glycoprotein** (~190 kDa) — uniquely, IgE does not form dimers, polymers, or secretory forms (unlike IgA/IgM):

**Heavy chain (ε chain; 72 kDa):**
- Four constant domains: **Cε1, Cε2, Cε3, Cε4** (IgE lacks the hinge region present in IgG and IgA)
- **Cε3 domain:** Primary FcεRI-binding site; the core interaction involves a specific surface on Cε3 inserting into the α-subunit of FcεRI; omalizumab binds Cε3 competitively with FcεRI
- **Cε2 domain:** Mediates FcεRII (CD23) binding; target of allergen immunotherapy-related IgE regulation
- Heavy N-glycosylation (~12% carbohydrate) — required for proper folding and receptor binding

**Light chain:** κ or λ (as with all immunoglobulins)

**FcεRI (High-affinity receptor):**
- **α subunit:** Extracellular; IgE-binding via two Ig-like domains; the primary affinity determinant
- **β subunit:** Single transmembrane span; acts as signal amplifier (contains ITAM)
- **γ₂ dimer:** Signal-transducing ITAMs; recruits Syk, Lyn, and LAT after IgE cross-linking
- Expressed: mast cells (10⁴–10⁵ receptors/cell), basophils (10⁵–10⁶/cell), Langerhans cells, DCs
- IgE binding stabilizes FcεRI on the surface → upregulates FcεRI expression: the "priming" effect; omalizumab reduces free IgE → FcεRI surface density decreases 95% over months [^gould-2008-ige-review]

**FcεRII (CD23, Low-affinity receptor; Kd ~10⁻⁷ M):**
- Type II transmembrane C-type lectin trimer; shed as **sCD23** by ADAM10
- Expressed: B cells, monocytes, dendritic cells, eosinophils, platelets
- Functions: negative feedback regulation of IgE synthesis (IgE-CD23-B cell loop); antigen-focusing (captures IgE-allergen complexes for presentation to T cells); sCD23 in serum → promotes IgE synthesis (amplification loop in atopy)

## Function

**Allergen sensitization phase:**
1. Epithelial barrier disruption (genetic, environmental) → allergen penetration → DC uptake → Th2 cytokine milieu (IL-4, IL-33, TSLP, IL-25)
2. Th2 cells produce IL-4 and IL-13 → activate B cells via CD40L (Th2) + IL-4 → **class switch recombination** to IgE (Cε locus); germinal center reaction → B cell affinity maturation → high-affinity allergen-specific IgE-secreting plasma cells
3. Circulating allergen-specific IgE binds FcεRI on tissue mast cells (skin, mucosa, lung) → **sensitized mast cell** (IgE-loaded for weeks to months)

**Allergen challenge (effector phase):**
1. Re-exposure to allergen → allergen bridges adjacent FcεRI-bound IgE molecules (cross-linking ≥2 IgE molecules required) → FcεRI aggregation
2. **Lyn** (Src kinase) phosphorylates ITAM tyrosines on γ and β chains → **Syk** (ZAP70 homologue) recruitment → LAT phosphorylation → PLC-γ1 activation
3. PLC-γ1 → IP₃ → ER Ca²⁺ release + DAG → PKC → transcription factor activation (NFAT, AP-1, NF-κB)
4. **Degranulation** (0-30 min): Preformed mediators released — histamine (H1R/H2R → bronchoconstriction, vasodilation, mucus), tryptase (activates PAR-2 → inflammation), heparin, chymase
5. **Lipid mediators** (newly synthesized, 0-2h): PLA₂ → arachidonic acid → COX-2 → PGD2 (DP1/CRTH2 → bronchoconstriction, Th2 recruitment); 5-LOX → LTC4 → LTD4, LTE4 (cysteinyl leukotrienes → CysLT1R bronchoconstriction)
6. **Cytokine secretion** (2-8h, late phase): IL-4, IL-5, IL-13, TNF-α, IL-8 → eosinophil/neutrophil recruitment → late-phase allergic reaction

**IgE independent of mast cells:**
- IgE on circulating basophils → activation in blood → amplifies systemic allergic response
- IgE-DC complexes (via FcεRI on DCs) → direct antigen presentation → Th2 amplification
- IgE → FcεRI on epithelial cells in barrier tissues → transcytosis of IgE-allergen complexes → luminal surveillance

## Mechanism

**Omalizumab (anti-IgE) pharmacology:**
- **Target:** Free (unbound) IgE — specifically the Cε3 domain; cannot bind IgE already bound to FcεRI (avoids risk of cross-linking on mast cells)
- **Mechanism:** Free IgE sequestration → FcεRI cannot be loaded → sensitized mast cells eventually lose surface IgE as it turns over → FcεRI density falls ~97% → greatly diminished allergen response
- **Dosing:** Weight- and total IgE-based dosing (75-375 mg SC every 2-4 weeks)
- **Clinical efficacy in severe allergic asthma:** 26-50% reduction in asthma exacerbations; reduces systemic corticosteroid use; improves quality of life and FeNO
- **Chronic idiopathic urticaria:** Omalizumab dramatically effective (∼50% complete response) — mechanism may involve IgE-mediated autoimmune activation of skin mast cells; approved at 300 mg SC Q4W
- **Emerging indications:** Peanut allergy desensitization (adjunct to OIT), ABPA, eosinophilic esophagitis

**Allergen immunotherapy (AIT) — IgE modulation:**
- Subcutaneous immunotherapy (SCIT) or sublingual immunotherapy (SLIT) → progressive allergen exposure → **Treg induction** (IL-10, TGF-β) → allergen-specific IgG4 blocking antibodies → reduced IgE/FcεRI signaling
- Increases allergen-specific IgG4 (blocking antibody) → competes with IgE for allergen binding; reduces mast cell activation
- Over years: reduces allergen-specific IgE; induces immune tolerance; disease-modifying (prevents sensitization to new allergens in children; reduces asthma risk)

**Hyper-IgE Syndromes:**
- **AD-HIES (Autosomal dominant; STAT3 loss-of-function):** IgE >2000 kIU/L, recurrent Staphylococcal/fungal infections, skeletal abnormalities, retained primary teeth, eczema; STAT3 is normally required for Th17 differentiation → Th17 deficiency → susceptibility to bacterial infections; simultaneously, STAT3 loss → dysregulated IgE production
- **AR-HIES (DOCK8 deficiency):** IgE elevation, severe atopy, recurrent infections, CNS vasculitis; DOCK8 defects impair T cell migration and survival
- Paradox: very high IgE does NOT confer extra allergic protection; IgE functions are hijacked by defective immune regulation

## Connections

Allergen-specific IgE binds FcεRI on airway mast cells → allergen cross-linking → degranulation → acute bronchoconstriction; omalizumab (anti-IgE mAb) binds free IgE → reduces FcεRI expression → 26-50% fewer exacerbations in severe allergic asthma.

IgE bound to FcεRI on mast cells persists for weeks-months (sensitized mast cell); allergen cross-links IgE → Syk/Lyn kinase → Ca2+ release → degranulation (histamine, heparin, tryptase) + prostaglandin and leukotriene synthesis; FcεRI density is upregulated by IgE itself.

IgE-mediated mast cell degranulation releases histamine → H1R bronchoconstriction, vasodilation, and pruritus; H1 antihistamines relieve allergic rhinitis and urticaria; in asthma, histamine is one of several bronchoconstricting mediators alongside leukotrienes and PGD2.

IgE-mediated mast cell activation → phospholipase A2 → arachidonic acid → COX → PGD2 (major mast cell prostanoid); PGD2 → DP1/CRTH2 receptors → bronchoconstriction, eosinophil recruitment, and mucus secretion; PGD2 mediates the late-phase allergic response.

[^gould-2008-ige-review]: Gould HJ, Sutton BJ. IgE in allergy and asthma today. *Nat Rev Immunol.* 2008;8(3):205-217. [doi:10.1038/nri2273](https://doi.org/10.1038/nri2273) · [PubMed 18301424](https://pubmed.ncbi.nlm.nih.gov/18301424/)
[^busse-2001-omalizumab]: Busse W, Corren J, Lanier BQ, et al. Omalizumab, anti-IgE recombinant humanized monoclonal antibody, for the treatment of severe allergic asthma. *J Allergy Clin Immunol.* 2001;108(2):184-190. [doi:10.1067/mai.2001.117880](https://doi.org/10.1067/mai.2001.117880) · [PubMed 11496232](https://pubmed.ncbi.nlm.nih.gov/11496232/)
