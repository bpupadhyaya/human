---
schema: human-scale-entry/v1
id: intestinal-epithelium
name: Intestinal Epithelium
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Single-layer columnar epithelium lining the small and large intestine. Largest surface area in the body (~32 m² via villi and microvilli). Absorbs nutrients and water; secrets mucus (goblet cells); transduces microbial signals to gut-associated lymphoid tissue (GALT)."
aliases: ["gut epithelium", "intestinal mucosa", "enteric epithelium", "intestinal lining", "GALT-associated epithelium"]
sources:
  - id: clevers-2013-intestinal-crypt
    type: peer-reviewed
    cite: "Clevers H. The intestinal crypt, a prototype stem cell compartment. Cell. 2013;154(2):274-84."
    doi: "10.1016/j.cell.2013.07.004"
    pmid: "23870119"
    url: "https://doi.org/10.1016/j.cell.2013.07.004"
  - id: artis-2008-epithelial-microbiota
    type: peer-reviewed
    cite: "Artis D. Epithelial-cell recognition of commensal bacteria and maintenance of immune homeostasis in the gut. Nat Rev Immunol. 2008;8(6):411-20."
    doi: "10.1038/nri2316"
    pmid: "18469830"
    url: "https://doi.org/10.1038/nri2316"
  - id: turner-2009-intestinal-barrier
    type: peer-reviewed
    cite: "Turner JR. Intestinal mucosal barrier function in health and disease. Nat Rev Immunol. 2009;9(11):799-809."
    doi: "10.1038/nri2653"
    pmid: "19855405"
    url: "https://doi.org/10.1038/nri2653"
  - id: barker-2014-intestinal-stem-cells
    type: peer-reviewed
    cite: "Barker N. Adult intestinal stem cells: critical drivers of epithelial homeostasis and regeneration. Nat Rev Mol Cell Biol. 2014;15(1):19-33."
    doi: "10.1038/nrm3721"
    pmid: "24326621"
    url: "https://doi.org/10.1038/nrm3721"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: part-of
    note: "The intestinal epithelium is the primary functional surface of the digestive system, responsible for nutrient absorption across the ~8 m length of the small intestine and water/electrolyte recovery in the ~1.5 m colon."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: ">70% of the body's immune cells reside in gut-associated lymphoid tissue (GALT); the intestinal epithelium is the primary interface between luminal microbiota and host immunity, transducing microbial signals via PRRs and cytokine secretion."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Intestinal epithelial cells secrete CSF1, IL-34, and TSLP that maintain and polarise intestinal macrophages (CX₃CR1⁺) toward anti-inflammatory phenotypes; conversely, macrophage-derived IL-10 and PGE₂ support epithelial barrier integrity."
  - target: 01-human/04-cellular/b-cell
    relation: modulates
    note: "Intestinal epithelial cells produce APRIL (TNFSF13), BAFF (TNFSF13B), and TGF-β to support IgA class switching in lamina propria B cells; IgA is transcytosed through the epithelium by the polymeric Ig receptor (pIgR) into the gut lumen."
  - target: 01-human/04-cellular/dendritic-cell
    relation: modulates
    note: "Intestinal epithelial cells signal to sub-epithelial DCs via TSLP, IL-25, and IL-33, conditioning DCs toward tolerogenic (RA-producing, IDO-expressing) rather than immunogenic phenotypes."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The intestinal epithelium is the largest mucosal surface in the human body; it separates the ~38 trillion microorganisms of the gut microbiome from the host's sterile internal compartments."
  - target: 01-human/06-organ/small-intestine
    relation: part-of
    note: "Part Of by Small Intestine."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: infected-by
    note: "Infected by Clostridioides difficile."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: infected-by
    note: "C. albicans Als3 adhesin binds enterocyte E-cadherin/N-cadherin; candidalysin disrupts tight junctions enabling hyphal penetration; antibiotic dysbiosis enables Candida overgrowth; gut translocation is the primary candidemia source in neutropenic patients."
---

# Intestinal Epithelium

## Overview

The intestinal epithelium is the single-cell-thick columnar epithelial lining of the small intestine (duodenum, jejunum, ileum) and large intestine (caecum, colon, rectum). Despite its minimal thickness (~20–25 µm per cell height), it fulfils extraordinary physiological roles: nutrient and water absorption, mucus secretion, microbial sensing, and immune education. It presents the largest mucosal surface in the human body — approximately 32 m² when fully extended by villi and microvilli — far exceeding skin (~1.7 m²) or the lung epithelium (~70 m²).

The gut epithelium is the most rapidly renewing tissue in the adult human body, with a complete cellular turnover every 3–5 days in the small intestine and 5–7 days in the colon. This turnover is driven by intestinal stem cells (ISCs) residing at the base of crypts of Lieberkühn, which continuously generate the full spectrum of differentiated epithelial cell types. Approximately 10¹⁰ epithelial cells are shed into the intestinal lumen per day.

Crucially, the intestinal epithelium forms the primary barrier separating ~38 trillion luminal microorganisms (gut microbiome) and their metabolites from the sterile internal milieu. Barrier breach — via tight junction dysregulation, cell death, or mucus layer disruption — triggers inflammatory responses, and chronic dysfunction underlies conditions ranging from inflammatory bowel disease to systemic endotoxaemia.

## Structure

**Villus-crypt axis (small intestine).** The small intestinal mucosa is organised into finger-like projections (villi, 0.5–1.5 mm in height) interspersed with tubular invaginations (crypts of Lieberkühn, ~100–300 µm deep). This geometry amplifies absorptive surface area ~7-fold over a flat tube. Each villus is covered by a monolayer of terminally differentiated enterocytes, goblet cells, and enteroendocrine cells migrating upward from the crypt; worn cells are shed at the villus tip. The crypt bottom houses stem cells, Paneth cells, and transit-amplifying progenitors.

**Apical surface amplification.** Enterocytes bear densely packed microvilli (brush border; 1–3 µm tall, ~3,000 per cell), increasing apical surface ~30-fold over a flat membrane. Microvilli are stabilised by a core of F-actin filaments cross-linked by villin, fimbrin, and eps8. The brush border glycocalyx (thick, fibrous, 400–500 nm) contains digestive enzymes (sucrase-isomaltase, lactase-phlorizin hydrolase, aminopeptidase N, dipeptidyl peptidase IV) anchored in the apical membrane.

**Tight junctions and the paracellular barrier.** Adjacent epithelial cells are sealed by apical junctional complexes: tight junctions (claudins 1, 2, 3, 4, 5, 7, 8, 15; occludin; tricellulin; junction adhesion molecules), adherens junctions (E-cadherin–β-catenin–α-catenin), and desmosomes. Claudin-2 forms leaky cation channels (increased in inflammatory states and Th2 conditions); other claudins form tight barriers. ZO-1, ZO-2, ZO-3 scaffold proteins link tight-junction strands to the perijunctional actomyosin ring. Myosin light chain kinase (MLCK) phosphorylation contracts this ring → junction opening (major mechanism of inflammatory barrier dysfunction).

**Mucus layers.** Goblet cells secrete MUC2 mucin (colon) and MUC5AC (stomach), forming a stratified mucus layer. The colon has two mucus layers: a dense, sterile inner layer (~150 µm, impenetrable to most bacteria due to CRS-FCGBP cross-linking) and a loose, bacteria-permissive outer layer (~700 µm) serving as a microbial habitat. The small intestine has a thinner, single mucus layer and a comparatively open architecture permissive to luminal sampling.

**Specialised epithelial cell types.**
- *Enterocytes* (~80%): principal absorptive cells; covered by brush border; express SGLT1 (glucose), GLUT5 (fructose), PepT1 (dipeptides), NPC1L1 (cholesterol), and fatty acid-binding proteins (FABPs).
- *Goblet cells* (~10–15%): mucin-secreting; express Atoh1 (Math1), Klf4, and Spdef; regulated by Notch (off → goblet fate).
- *Enteroendocrine cells* (~1%): >20 subtypes producing gut hormones: GLP-1 (L cells; glucagon-like peptide-1; incretins), GIP, CCK, serotonin (5-HT), secretin, ghrelin, PYY. Major endocrine interface of the gut-brain axis.
- *Paneth cells* (small intestine crypts): long-lived (21–60 days) secretory cells producing antimicrobial peptides (defensins α, cryptdins), lysozyme, phospholipase A2, and RegIII proteins. Provide niche signals (EGF, Wnt3) to support Lgr5⁺ ISCs.
- *Microfold (M) cells* (follicle-associated epithelium over Peyer's patches): transcytose luminal antigens and microorganisms to sub-epithelial DCs and macrophages for immune surveillance. Basolateral pocket contains DCs, macrophages, and lymphocytes.
- *Tuft cells* (~0.4%): chemosensory; express taste transduction machinery (α-gustducin, TRPM5); produce IL-25 (IL-17E) that drives type-2 immune responses to helminths and protozoa.

## Function

**Nutrient absorption.** The small intestine absorbs ~9 litres of fluid/day (2 L dietary, 7 L secreted by GI glands). Carbohydrates: brush-border enzymes hydrolyse starch and disaccharides → monosaccharides absorbed by SGLT1 (Na⁺-coupled) and GLUT5/GLUT2. Proteins: pancreatic proteases + brush-border peptidases → amino acids and dipeptides; PepT1 co-transports di/tripeptides. Lipids: bile acid micelles → monoglycerides/fatty acids absorbed by passive diffusion + FATP4; reassembled into chylomicrons in the ER → secreted via exocytosis into lacteals. Vitamins: B12–intrinsic factor complex via cubam receptor; fat-soluble vitamins (A, D, E, K) in micelles.

**Barrier function.** The epithelium + mucus + secretory IgA form a physical and chemical barrier to luminal antigens. Barrier integrity is maintained by constitutive tight-junction complex renewal, apical-out membrane polarity (separating absorptive and signalling domains), and continuous replacement of cells. Pattern recognition receptors — basolaterally expressed TLR4 (LPS), TLR2 (peptidoglycan), TLR5 (flagellin), NOD1, NOD2 — are positioned to detect microbial penetration without responding to the luminal microbiome (reducing constitutive activation).

**Immune education and tolerance.** The intestinal epithelium actively conditions the underlying immune compartment toward tolerance to commensals and dietary antigens. Mechanisms include:
- TSLP secretion → DCs acquire retinoic acid (RA)-producing, IDO-expressing, tolerogenic phenotype → Treg induction.
- IL-25 (tuft cells) + IL-33 (epithelial alarmin) → ILC2 activation → Th2 responses (helminth expulsion) and tissue repair.
- APRIL, BAFF, TGF-β secretion → IgA class-switching in lamina propria B cells → secretory IgA (SIgA) transcytosed by pIgR → luminal coating of commensal bacteria (immune exclusion without inflammation).
- RALDH2-expressing epithelial cells convert dietary retinol → retinoic acid → imprints gut-homing (α4β7 integrin, CCR9) on T and B cells.

**Enteroendocrine signalling.** Enteroendocrine cells collectively constitute the largest endocrine organ in the body by cell number. L-cell-derived GLP-1 and GIP are released post-prandially → stimulate pancreatic β-cell insulin secretion (incretin effect, ~50–70% of post-meal insulin response) → targets of GLP-1 receptor agonists (liraglutide, semaglutide). Serotonin (5-HT) from enterochromaffin cells: ~95% of body's 5-HT; activates intrinsic sensory neurons of the enteric nervous system to initiate peristaltic reflex.

## Connections

- **Upstream signals to epithelium:** Wnt (crypt-base Paneth cells, sub-epithelial myofibroblasts → ISC maintenance); EGF (Paneth cells, salivary glands); Notch (lateral inhibition → enterocyte vs. secretory fate); BMP2/4 (villus differentiation gradient); luminal microbiota (TLR/NLR signalling, metabolites: short-chain fatty acids, secondary bile acids, indoles); inflammatory cytokines (TNF-α, IL-1β → NF-κB → barrier disruption; IL-22 → STAT3 → barrier repair).
- **Outputs from epithelium to immune system:** TSLP, IL-25, IL-33 (epithelial alarmins); SIgA (via pIgR); defensins/Reg proteins (antimicrobial); antigen transcytosis (M cells); cytokines (IL-1β, IL-6, IL-8/CXCL8, CCL20 → neutrophil/DC recruitment).
- **Gut microbiome interactions:** ~38 trillion bacteria, archaea, fungi, and viruses coat the apical epithelial surface (outer mucus layer). Short-chain fatty acids (butyrate, propionate, acetate) from microbial fermentation of dietary fibre: butyrate is the primary energy source for colonocytes (70% of oxidative fuel); activates GPR41/GPR109A → immune tolerance; inhibits HDAC → anti-inflammatory epigenetic effects.
- **Stem cell niche.** Lgr5⁺ crypt-base columnar cells are the active intestinal stem cells; ~5–10 per crypt base. Paneth cell-derived EGF, Wnt3, Notch ligands (Dll4) are the niche. +4 position cells (quiescent reserve ISCs, Bmi1⁺ or Lrig1⁺) are activated by injury. Organoid technology exploiting ISC properties revolutionised gut biology research and holds therapeutic potential for intestinal repair.
- **Pathological conditions:** Coeliac disease (gliadin peptides → HLA-DQ2/8 → adaptive immune attack on enterocytes → villous atrophy); Crohn's disease and ulcerative colitis (barrier dysfunction, dysbiosis, aberrant immune activation); colorectal cancer (APC/β-catenin → KRAS → TP53 mutational sequence in the crypt stem cell); infectious diarrhoea (Vibrio cholerae CFTR chloride secretion; enterotoxigenic E. coli; rotavirus tight-junction disruption); short bowel syndrome; necrotising enterocolitis (premature infants, barrier immaturity + microbial translocation).
- `infected-by` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — C. albicans Als3 adhesin binds enterocyte E-cadherin/N-cadherin; candidalysin disrupts tight junctions enabling hyphal penetration; antibiotic dysbiosis enables Candida overgrowth; gut translocation is the primary candidemia source in neutropenic patients.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
