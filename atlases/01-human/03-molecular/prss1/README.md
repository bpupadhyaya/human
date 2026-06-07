---
schema: human-scale-entry/v1
id: prss1
name: PRSS1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PRSS1 (cationic trypsinogen) is the predominant pancreatic zymogen; R122H blocks autolytic self-inactivation and N29I disrupts calcium stabilization → both cause premature/persistent trypsin activation → hereditary pancreatitis; PRSS1 GOF mutations are autosomal dominant."
aliases: ["PRSS1", "cationic trypsinogen", "trypsinogen 1", "PRSS1 hereditary pancreatitis", "PRSS1 R122H", "PRSS1 N29I", "PRSS1 pancreatitis", "trypsinogen PRSS1", "cationic trypsinogen R122H"]
sources:
  - id: whitcomb-1996-prss1
    type: peer-reviewed
    cite: "Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. Nat Genet. 1996;14(2):141-145."
    doi: "10.1038/ng1096-141"
    pmid: "8841182"
    url: "https://doi.org/10.1038/ng1096-141"
  - id: gorry-1997-prss1-n29i
    type: peer-reviewed
    cite: "Gorry MC, Gabbaizedeh D, Furey W, et al. Mutations in the cationic trypsinogen gene are associated with recurrent acute and chronic pancreatitis. Gastroenterology. 1997;113(4):1063-1068."
    doi: "10.1053/gast.1997.v113.pm9322498"
    pmid: "9322498"
    url: "https://doi.org/10.1053/gast.1997.v113.pm9322498"
cross_links:
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes."
---

# PRSS1

## Overview

**PRSS1** (Protease, Serine 1; **cationic trypsinogen**; also Trypsinogen 1) is a 247 amino acid (26 kDa) **serine protease zymogen** and the most abundantly expressed trypsinogen isoform in human pancreatic acinar cells (~65-70% of total trypsinogen secretion). PRSS1 is synthesized as an inactive zymogen → secreted into the pancreatic duct system → activated in the duodenum by enterokinase (TMPRSS15) cleavage of the N-terminal trypsinogen activation peptide (TAP) → mature trypsin. Intrapancreatic activation of trypsinogen (premature trypsin production within acinar cells) is prevented by multiple protective mechanisms: the N-terminal TAP peptide sterically occludes the active site; SPINK1 (pancreatic secretory trypsin inhibitor) inhibits nascent trypsin; and crucially, trypsin autolytically inactivates itself by cleaving the critical **Arg122-Val123 bond** (self-inactivation). PRSS1 gain-of-function germline mutations — most prominently **R122H** and **N29I** — overcome these protective mechanisms, causing persistent intrapancreatic trypsin activity → pancreatic autodigestion → hereditary pancreatitis. Hereditary pancreatitis was the first condition for which a specific gene mutation was identified in pancreatitis, established by Whitcomb et al. in 1996 [^whitcomb-1996-prss1] [^gorry-1997-prss1-n29i].

**PRSS1 germline mutations — summary:**

| Variant | Prevalence | Mechanism | Clinical feature |
|---|---|---|---|
| R122H (Arg122His) | ~65-70% of HP families | Blocks Arg122 autolysis → persistent active trypsin | Classic hereditary pancreatitis; high penetrance |
| N29I (Asn29Ile) | ~20-25% of HP families | Disrupts Ca²⁺ binding loop → early trypsin activation | Less penetrant than R122H; similar chronic pancreatitis |
| A16V (Ala16Val) | ~5% | TAP peptide variant → enhanced premature activation | Modifier; may need cofactor |
| Other (D22G, K23R, etc.) | Rare | Various; TAP region or Ca²⁺ binding | Rare families; incomplete data |

**SPINK1 N34S** is a separate, more common variant (~1-2% population) in the trypsin inhibitor gene — acts as a disease modifier/recessive susceptibility allele (alone insufficient to cause pancreatitis; in combination with other genetic/environmental factors raises risk; not the primary gene for hereditary pancreatitis).

## Structure

### PRSS1 protein domains

**Signal peptide (aa 1-15):**
- Directs PRSS1 to the ER lumen → Golgi → zymogen granule → exocytosis into pancreatic duct; cleaved during processing

**Trypsinogen activation peptide (TAP; aa 16-23):**
- PRSS1 zymogen form: TAP covers the active site, keeping the enzyme in the inactive state until it is cleaved by enterokinase (duodenal enzyme, cuts after Lys23) or by trypsin itself (autocatalytic activation — can also be initiated in the pancreatic duct)
- A16V variant: alters TAP conformation → promotes premature activation within acinar cells

**Catalytic domain (aa 24-247):**
- Trypsin fold (two β-barrel lobes connected by a linker); classical Ser/His/Asp catalytic triad: Ser195/His57/Asp102 (chymotrypsin numbering); cleaves peptide bonds after Arg or Lys (trypsin-like specificity)
- **Arg122-Val123 autolysis site**: after activation, active trypsin cleaves this bond → trypsin fragmented → inactivated; this is the key autoregulatory mechanism preventing persistent trypsin activity in the pancreas
  - **R122H mutation**: substitutes Arg with His at position 122; His is NOT cleaved by trypsin (trypsin specificity for Arg/Lys); trypsin cannot autolyze → persistent active trypsin → ongoing pancreatic autodigestion
- **Calcium (Ca²⁺) binding loop (around Asn29):**
  - Trypsin (cationic) has a high-affinity Ca²⁺ binding site; Ca²⁺ binds → stabilizes trypsinogen in the inactive conformation and stabilizes active trypsin against acid/pH-mediated unfolding
  - Ca²⁺ also protects the Arg122-Val123 bond from cleavage (Ca²⁺ binding changes the conformation of the autolysis loop)
  - **N29I mutation**: Asn29 is part of the Ca²⁺ binding loop; Ile substitution → disrupts Ca²⁺ binding affinity → trypsinogen less stable in zymogen form → lower activation threshold → premature activation inside acinar cells at lower Ca²⁺ concentrations; also reduces Ca²⁺ protection of the Arg122 loop → faster autolysis of already-active trypsin (this reduces R122H benefit, but premature activation is the dominant N29I mechanism)

**SPINK1 interaction:**
- SPINK1 (Serine Protease Inhibitor Kazal-type 1; also PSTI, pancreatic secretory trypsin inhibitor): 56 aa inhibitor secreted by pancreatic acinar cells into lumen; binds trypsin with Ki ~1 nM; inhibits ~20% of total trypsin capacity (not complete inhibitor); serves as a first-line buffer against premature activation
- SPINK1 N34S: reduces SPINK1 expression by ~20-30% (affects mRNA stability); alone insufficient to cause pancreatitis; acts as disease modifier in compound heterozygotes with CFTR, PRSS1, or CTRC variants

**CTRC (chymotrypsin C, CELA3B/CTRC):**
- CTRC: a chymotrypsin isoform that cleaves the Arg122 site to promote trypsin inactivation (independent of trypsin autolysis); also cleaves trypsinogen at Leu81 → trypsinogen degradation
- CTRC loss-of-function mutations (R254W, K247_R254del) impair trypsin inactivation → pancreatitis; CTRC thus works in parallel with PRSS1 autolysis to control active trypsin levels

## Function

### PRSS1 in normal pancreatic physiology

**Exocrine pancreas secretion:**
1. Acinar cell stimulates: CCK (from duodenal I-cells) → CCK-A receptor → Ca²⁺ surge → zymogen granule exocytosis → trypsinogen, chymotrypsinogen, elastase, lipase, amylase, phospholipase A2 → released into pancreatic duct
2. Ductal bicarbonate (stimulated by secretin → CFTR chloride → bicarbonate secretion): alkalinizes duct, inhibiting premature trypsin activation (trypsin optimal pH ~8; pancreatic juice pH ~8.2)
3. Duodenum: enterokinase (TMPRSS15) cleaves Lys23-Ile24 bond of trypsinogen → trypsin; once any trypsin forms → autocatalytic activation cascade (trypsin activates more trypsinogen → cascades to chymotrypsin, elastase, procarboxypeptidase activation)
4. Food digestion: trypsin cleaves proteins at Arg/Lys; with chymotrypsin (Phe/Trp/Tyr) and elastase (Ala/Val) → complete protein hydrolysis in small intestine

**Trypsin protective mechanisms in normal pancreas:**
- TAP peptide: zymogen occlusion → no activity until enterokinase cleavage in duodenum
- SPINK1: buffer inhibitor in acinar cell and duct lumen
- CTRC: cleaves and inactivates trypsin and trypsinogen
- Autolysis at Arg122: trypsin self-destructs after activation
- Ca²⁺ stabilization: calcium keeps trypsinogen in inactive conformation; ductal Ca²⁺ is actively kept low (Ca²⁺ secreted with zymogen granules → precipitates in alkaline duct → calcifications in chronic pancreatitis)

**PRSS1 GOF → pancreatitis mechanism:**
R122H (dominant mechanism in most HP families):
1. Acinar cell Ca²⁺ surge (physiological or pathological) → small amount of trypsinogen autoactivates inside acinar cell
2. Nascent trypsin → attempts to autolyze at Arg122 → CANNOT (Arg122His blocks) → trypsin persists
3. Persistent trypsin activates more trypsinogen → chain reaction inside acinar cells
4. Cytosolic trypsin activates downstream zymogens → acinar cell autodigestion → cell death → acute pancreatitis episode
5. Repeated episodes → permanent parenchymal destruction → fibrosis

### PRSS1 and the SPINK1/CFTR/CTRC modifier system

Hereditary pancreatitis is not purely monogenic — the phenotype severity is influenced by:
- SPINK1 N34S: if co-inherited with R122H → more severe and earlier-onset chronic pancreatitis; SPINK1 N34S alone → susceptibility allele (10x risk vs population, still ~1% absolute lifetime risk); compound heterozygosity (PRSS1 + SPINK1) → more severe
- CFTR variants: CFTR controls pancreatic duct bicarbonate/fluid secretion; CFTR mutations → low pH duct fluid → trypsin more active → compounds PRSS1 R122H; PRSS1 R122H + CFTR mutation → especially severe disease
- CTRC mutations: impaired trypsin clearance → compound with PRSS1 GOF

## Mechanism

### Molecular mechanism of PRSS1 gain-of-function

**R122H — resistance to autolysis:**
- Crystal structure of bovine trypsin shows Arg122 (equivalent position) in the autolysis loop, accessible to trypsin active site cleft
- Trypsin cleaves Arg122-Val123 in wild-type (cis-autolysis): inactivated trypsin accumulates
- R122H: Arg→His substitution prevents this cleavage (trypsin cuts Arg/Lys, not His); trypsin accumulates → pancreatic autodigestion
- CTRC also cleaves the Arg122 site (independently): but CTRC activity is insufficient to compensate alone when autolysis site is destroyed; CTRC also can cleave Leu81 to degrade trypsinogen, maintaining this as a partial backup

**N29I — Ca²⁺ binding disruption:**
- Ca²⁺ coordination in trypsin involves Glu70, Asn72, Thr73, Val75, Glu80, and a structural water around the Ca²⁺ ion
- Asn29 is part of a neighboring loop; N29I → structural perturbation of the calcium-binding loop → lower Ca²⁺ affinity → trypsinogen unstable at low Ca²⁺ (as occurs in acinar cell cytoplasm) → premature activation
- Additionally, Ca²⁺ stabilizes the Arg122 loop in a conformation less accessible to autolysis; without Ca²⁺ → Arg122 loop more exposed → faster autolysis (but R122H abolishes this; N29I works primarily through premature activation, not autolysis resistance)

**Therapeutic opportunities:**
- No PRSS1-specific inhibitors in clinical use; trypsin is essential for digestion — cannot be globally inhibited
- Enzyme replacement therapy (Creon, Zenpep): for exocrine pancreatic insufficiency once parenchyma is destroyed; supplements lipase, protease, amylase
- Insulin therapy: for pancreatogenic diabetes mellitus (Type 3c diabetes) following endocrine parenchymal loss
- Endoscopic/surgical decompression: for main pancreatic duct dilation (Puestow/Partington-Rochelle lateral pancreaticojejunostomy); reduces recurrent acute episodes
- Total pancreatectomy with islet autotransplantation (TPIAT): for refractory pain with diffuse disease; removes the entire PRSS1-carrying organ; transplanted islets prevent surgical diabetes; quality-of-life improvement; PDAC risk effectively eliminated (no pancreas = no PDAC)
- PDAC surveillance: annual CA19-9 (sensitivity limited); annually EUS or MRCP from ~40y in HP patients; EUS is most sensitive for early PanIN

## Connections

- `connects-to` → **[Hereditary Pancreatitis](../../07-system/hereditary-pancreatitis/README.md)** — PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes.

[^whitcomb-1996-prss1]: Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. *Nat Genet.* 1996;14(2):141-145. [doi:10.1038/ng1096-141](https://doi.org/10.1038/ng1096-141) · [PubMed 8841182](https://pubmed.ncbi.nlm.nih.gov/8841182/)
[^gorry-1997-prss1-n29i]: Gorry MC, Gabbaizedeh D, Furey W, et al. Mutations in the cationic trypsinogen gene are associated with recurrent acute and chronic pancreatitis. *Gastroenterology.* 1997;113(4):1063-1068. [doi:10.1053/gast.1997.v113.pm9322498](https://doi.org/10.1053/gast.1997.v113.pm9322498) · [PubMed 9322498](https://pubmed.ncbi.nlm.nih.gov/9322498/)
