---
schema: human-scale-entry/v1
id: gut-microbiome
name: Gut Microbiome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "~10¹³ microorganisms (Firmicutes, Bacteroidetes, Actinobacteria) colonizing the GI tract. Functions: SCFA production (butyrate, propionate), vitamin synthesis, colonization resistance, immune education, bile acid metabolism, gut-brain axis serotonin."
aliases: ["gut microbiome", "gut microbiota", "intestinal microbiome", "gut flora", "microbiota", "human microbiome"]
sources:
  - id: sender-2016-microbiome-census
    type: peer-reviewed
    cite: "Sender R, Fuchs S, Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. Cell. 2016;164(3):337-340."
    doi: "10.1016/j.cell.2016.01.013"
    pmid: "26824647"
    url: "https://doi.org/10.1016/j.cell.2016.01.013"
  - id: turnbaugh-2006-microbiome-nature
    type: peer-reviewed
    cite: "Turnbaugh PJ, Ley RE, Mahowald MA, Magrini V, Mardis ER, Gordon JI. An obesity-associated gut microbiome with increased capacity for energy harvest. Nature. 2006;444(7122):1027-1031."
    doi: "10.1038/nature05414"
    pmid: "17183312"
    url: "https://doi.org/10.1038/nature05414"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "The gut microbiome is the primary educator of the mucosal and systemic immune system: drives IgA production, Treg induction, colonization resistance, and patterns innate immune responses; dysbiosis leads to immune dysregulation and susceptibility to inflammatory diseases."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: contains
    note: "Bacteroides fragilis (non-toxigenic strains) is a key Bacteroidetes member; polysaccharide A (PSA) drives Treg induction and IL-10 production; ETBF toxin disrupts epithelial barrier and promotes dysbiosis."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: contains
    note: "Akkermansia muciniphila is a mucin-degrading Verrucomicrobia member of the gut microbiome associated with metabolic health; reduced in obesity and T2DM; its Amuc_1100 outer membrane protein activates TLR2, improving gut barrier integrity and insulin sensitivity."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Dysbiosis in obesity — increased Firmicutes/Bacteroidetes, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Microbiome dysbiosis → LPS → TLR4 → TNF-α/IL-6 → adiponectin suppression; butyrate-producing bacteria (Akkermansia, Bifidobacterium) → SCFA → PPARγ → ADIPOQ induction; probiotics and prebiotics modestly raise adiponectin in metabolic syndrome and obesity trials."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: modulated-by
    note: "Chronic PPI (omeprazole) → suppressed gastric acid → altered upper GI microbiome: ↑ Streptococcus/Rothia/Veillonella colonize stomach; ↑ SIBO; disrupts lower GI microbiome; reversible on discontinuation; contributes to pneumonia and C. diff risk."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: modulated-by
    note: "Oral vancomycin dramatically disrupts gut anaerobes (Bacteroidetes, Bifidobacterium, Lactobacillus) while sparing aerobic gram-positive cocci; microbiome recovery takes 3–6 months; vancomycin-driven dysbiosis increases VRE and C. diff colonization risk in hospital settings."
---

# Gut Microbiome

## Overview

The gut microbiome is the **vast ecological community of microorganisms** inhabiting the human gastrointestinal tract — comprising approximately **10¹³ bacterial cells** (comparable to human somatic cell number [^sender-2016-microbiome-census]), plus archaea, fungi (mycobiome), viruses (virome), and protozoa. The collective genome of these microorganisms — the **metagenome** — encodes approximately 150-fold more genes than the human genome, providing metabolic capabilities that human enzymes cannot perform independently.

The microbiome is not uniformly distributed: microbial density increases dramatically from stomach (~10¹–10³ cells/mL) to terminal ileum (~10⁷–10⁸/mL) to colon (~10¹¹–10¹²/mL), where the vast majority of the microbiome resides. The colon is dominated by **obligate anaerobes** from two major phyla: **Firmicutes** (~60%, includes Clostridia, Lactobacillus, Ruminococcus) and **Bacteroidetes** (~30%, includes Bacteroides, Prevotella). Actinobacteria (Bifidobacterium), Proteobacteria, and Verrucomicrobia (Akkermansia) comprise smaller but functionally important fractions.

The microbiome is now recognized as an integral functional organ, contributing to digestion, immune education, metabolic homeostasis, and even neurological function (gut-brain axis). Dysbiosis — compositional or functional disruption of the microbiome — is associated with inflammatory bowel disease, obesity, type 2 diabetes, colorectal cancer, depression, and Clostridioides difficile infection.

## Structure

### Microbial Composition and Ecology

**Major phyla and representative genera:**

| Phylum | % Gut | Key genera | Functions |
|:---|:---|:---|:---|
| **Firmicutes** | ~60% | Ruminococcus, Faecalibacterium, Clostridium, Lactobacillus, Enterococcus | Butyrate production (F. prausnitzii); starch fermentation; colonization resistance |
| **Bacteroidetes** | ~25–30% | Bacteroides (B. thetaiotaomicron), Prevotella | Polysaccharide degradation; propionate and acetate production; PSA immunomodulation |
| **Actinobacteria** | ~5–10% | Bifidobacterium | HMO utilization (infants); IgA stimulation; butyrate precursors |
| **Verrucomicrobia** | ~1–3% | Akkermansia muciniphila | Mucin degradation; gut barrier maintenance; metabolic health |
| **Proteobacteria** | ~1–2% | E. coli, Helicobacter, Salmonella | Mostly minor commensals; can bloom in dysbiosis (bloom = overgrowth) |

**Biogeographic compartments:**
- **Mucosa-associated microbiome**: Lactobacillus, Bifidobacterium, Akkermansia — direct interaction with epithelium; shapes mucosal immunity
- **Luminal microbiome**: dominated by Bacteroides, Ruminococcus, Faecalibacterium — primary fermenters
- **Spatial gradients**: crypts are largely microorganism-free (antimicrobial peptides from Paneth cells); villi and crypts differ in microbial composition

### Microbiome Development

The microbiome undergoes characteristic developmental phases:
1. **Neonatal colonization** — seeded by maternal vaginal/fecal microbiota (vaginal birth) or skin/environment (C-section); cord microbiome is essentially sterile
2. **First 3 years** — most critical window; composition influenced by birth mode, breastfeeding (HMO → Bifidobacterium enrichment), antibiotics, and diet; period of immune system "programming"
3. **Adult microbiome** — relatively stable "core" composition; resilient to perturbation but recovers slowly from antibiotics
4. **Elderly microbiome** — reduced diversity, reduced Firmicutes/Bacteroidetes ratio, increased Proteobacteria; associated with inflammaging

## Function

### Short-Chain Fatty Acid (SCFA) Production

The signature metabolic output of gut fermentation: dietary fiber → anaerobic fermentation → SCFAs (predominantly butyrate, propionate, acetate in ~3:1:6 ratio):

| SCFA | Primary producer organisms | Primary functions |
|:---|:---|:---|
| **Butyrate** | Faecalibacterium prausnitzii, Roseburia, Eubacterium rectale | Primary fuel for colonocytes (~70% of colonocyte energy from butyrate); HDAC inhibitor → anti-inflammatory gene expression; strengthens tight junctions; suppresses colorectal cancer cell proliferation |
| **Propionate** | Bacteroides, Veillonella, Phascolarctobacterium | Gluconeogenesis substrate in liver; promotes satiety via free fatty acid receptor (FFAR3) on enteroendocrine cells; reduces hepatic lipogenesis |
| **Acetate** | Bifidobacterium, Akkermansia, many species | Systemic energy substrate; lipogenesis in adipose; conversion to butyrate by cross-feeding species; signaling via FFAR2 |

SCFAs are absorbed by SMCT1 (sodium-coupled monocarboxylate transporter) and MCT4 on colonocytes. Systemic SCFA levels (portal and systemic) regulate adipose, liver, muscle, and immune function.

### Immune System Education

The gut microbiome is the **primary driver of postnatal immune development**:

- **IgA production**: Microbiota-induced germinal center reactions in Peyer's patches and isolated lymphoid follicles → lamina propria IgA-committed plasma cells → 3–5 g/day SIgA secreted into gut lumen; IgA repertoire shaped by commensal antigens
- **Treg induction**: Clostridium clusters IV and XIVa produce SCFAs and other factors that induce colonic Foxp3+ Treg differentiation (butyrate → HDAC inhibition → Foxp3 gene induction); PSA from B. fragilis induces IL-10-producing Tregs
- **Innate priming**: LPS and flagellin from commensals set baseline TLR signaling thresholds; germ-free animals have hypersensitive innate responses
- **Colonization resistance**: competitive exclusion of pathogens via physical (niche occupancy) and chemical (bacteriocins, SCFAs, secondary bile acids) mechanisms — loss of colonization resistance after antibiotics → C. difficile bloom

### Bile Acid Metabolism

Gut bacteria perform critical modifications of host-derived primary bile acids:
- **Primary bile acids** (cholic acid, chenodeoxycholic acid) → secreted into gut → **7α-dehydroxylation** by Clostridium scindens and related Firmicutes → secondary bile acids (deoxycholic acid, lithocholic acid)
- Secondary bile acids activate **FXR** (farnesoid X receptor) and **TGR5** on intestinal and hepatic cells → regulate bile acid synthesis (FXR-FGF-19 feedback), glucagon-like peptide-1 (GLP-1) secretion (TGR5 on L-cells), and innate immunity
- Bile acid dysmetabolism in dysbiosis → Clostridioides difficile susceptibility (secondary bile acids are bacteriostatic for C. diff spore germination)

### Gut-Brain Axis

The microbiome influences CNS function via multiple pathways:
- **Serotonin production**: ~90% of body serotonin is produced in the gut; colonic enterochromaffin cells produce serotonin in response to SCFA/tryptophan signals from microbiota; affects intestinal motility and vagal signaling
- **Tryptophan metabolism**: Gut bacteria convert tryptophan to indole and indole derivatives → aryl hydrocarbon receptor (AhR) agonists → mucosal immune regulation
- **Vagal nerve signaling**: SCFA-activated FFAR3 on enteroendocrine cells → afferent vagal signals → hypothalamus; germ-free animals show altered vagal tone
- **Systemic metabolites**: TMAO (trimethylamine N-oxide) from choline/carnitine fermentation → systemic circulation → cardiovascular risk; uremic toxins (indoxyl sulfate, p-cresyl sulfate) in CKD

## Connections

- `modulates` → **[Immune System](../immune-system/README.md)** — primary educator of mucosal and systemic immunity via IgA induction, Treg programming, innate immune threshold-setting, and colonization resistance
- `contains` → **[Bacteroides fragilis](../../../../02-pathogen/06-microbiome/bacteroides-fragilis/README.md)** — key Bacteroidetes member; PSA from commensal B. fragilis induces Treg and IL-10 (immunoprotective); ETBF toxin disrupts epithelial barrier
- `contains` → **[Akkermansia muciniphila](../../../../02-pathogen/06-microbiome/akkermansia-muciniphila/README.md)** — mucin-degrading species associated with metabolic health; reduced in obesity and T2DM; Amuc_1100 strengthens gut barrier via TLR2
- `connects-to` → **[Obesity](../obesity/README.md)** — dysbiosis in obesity — increased Firmicutes/Bacteroidetes, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype.
- `connects-to` → **[Adiponectin](../../../03-molecular/adiponectin/README.md)** — Microbiome dysbiosis → LPS → TLR4 → TNF-α/IL-6 → adiponectin suppression; butyrate-producing bacteria (Akkermansia, Bifidobacterium) → SCFA → PPARγ → ADIPOQ induction; probiotics and prebiotics modestly raise adiponectin in metabolic syndrome and obesity trials.
- `connects-to` → **[Secretory IgA](../../../03-molecular/secretory-iga/README.md)** — SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals.
- `modulated-by` → **[Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md)** — Chronic PPI → suppressed gastric acid → altered upper GI microbiome: ↑ Streptococcus/Rothia/Veillonella colonize stomach; ↑ SIBO; disrupts lower GI microbiome; reversible on discontinuation; contributes to pneumonia and C. diff risk.
- `modulated-by` → **[Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md)** — Oral vancomycin dramatically disrupts gut anaerobes (Bacteroidetes, Bifidobacterium, Lactobacillus) while sparing gram-positive cocci; microbiome recovery takes 3–6 months; vancomycin-driven dysbiosis increases VRE and C. diff colonization risk in hospital settings.

## Pathology

### Dysbiosis

Dysbiosis — the pathological alteration of microbiome composition or function — is associated with multiple diseases:

**Inflammatory Bowel Disease (IBD — Crohn's and UC):**
- Reduced microbial diversity; loss of Faecalibacterium prausnitzii (primary butyrate producer)
- Increased Proteobacteria (E. coli, Bacteroides fragilis ETBF)
- CARD15/NOD2 mutations impair innate sensing of muramyl dipeptide → Paneth cell dysfunction → antimicrobial peptide deficiency → microbial invasion of epithelium
- FMT (fecal microbiota transplant) can achieve remission in UC; limited efficacy in Crohn's

**Clostridioides difficile Infection (CDI):**
- Antibiotics destroy colonization resistance → C. difficile spore germination (secondary bile acid loss)
- Toxin A (TcdA) and Toxin B (TcdB) → glucosylation of Rho GTPases → epithelial cytoskeletal disruption → pseudomembranous colitis
- FMT: ~90% efficacy for recurrent CDI — the highest-evidence microbiome intervention; now FDA-approved (RBX2660, SER-109)

**Metabolic Disease:**
- Turnbaugh et al. (2006) demonstrated that obesity-associated microbiomes have increased capacity for dietary energy harvest [^turnbaugh-2006-microbiome-nature]
- Reduced butyrate producers → impaired gut barrier → metabolic endotoxemia (low-level LPS translocation → chronic low-grade inflammation → insulin resistance)
- TMAO from Prevotella/Fusobacterium fermentation of dietary choline → enhanced platelet aggregation → cardiovascular risk

**Dysbiosis and CNS:**
- Reduced Lactobacillus and Bifidobacterium associated with depression and anxiety (bidirectional causality uncertain)
- Germ-free rodents show reduced neurogenesis, abnormal HPA axis reactivity, and social behavior deficits reversed by microbiome colonization

### Microbiome-Based Therapeutics

| Intervention | Target | Mechanism | Evidence |
|:---|:---|:---|:---|
| **FMT (Fecal Microbiota Transplant)** | Recurrent CDI; UC | Restoration of colonization resistance + diverse microbiome | ~90% CDI cure; ~30% UC remission |
| **Live biotherapeutics (SER-109)** | Recurrent CDI | Spore-forming Firmicutes consortium restores colonization resistance | Phase III: ~68% efficacy vs. ~58% placebo (ECOSPOR IV) |
| **Probiotics (Lactobacillus, Bifidobacterium)** | IBD, IBS, CDI prevention | Colonization resistance, mucosal IgA, Treg induction | Moderate evidence in UC, IBS; limited in Crohn's |
| **Dietary fiber (prebiotic)** | Metabolic disease, IBD | Selective enrichment of SCFA producers; butyrate → colonocyte health | Strong mechanistic; emerging clinical evidence |

[^sender-2016-microbiome-census]: Sender R, Fuchs S, Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. *Cell.* 2016;164(3):337-340. [doi:10.1016/j.cell.2016.01.013](https://doi.org/10.1016/j.cell.2016.01.013) · [PubMed 26824647](https://pubmed.ncbi.nlm.nih.gov/26824647/)
[^turnbaugh-2006-microbiome-nature]: Turnbaugh PJ et al. An obesity-associated gut microbiome with increased capacity for energy harvest. *Nature.* 2006;444(7122):1027-1031. [doi:10.1038/nature05414](https://doi.org/10.1038/nature05414) · [PubMed 17183312](https://pubmed.ncbi.nlm.nih.gov/17183312/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
