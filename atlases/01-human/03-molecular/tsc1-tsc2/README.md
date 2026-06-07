---
schema: human-scale-entry/v1
id: tsc1-tsc2
name: TSC1-TSC2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "TSC1-TSC2 complex (hamartin-tuberin) is a GTPase-activating protein for Rheb; LOF → mTORC1 hyperactivation → S6K1/4EBP1 → hamartoma growth; germline TSC1/TSC2 = tuberous sclerosis complex; everolimus FDA-approved for TSC-associated renal angiomyolipoma, SEGA, and LAM."
aliases: ["TSC1", "TSC2", "TSC1-TSC2", "hamartin", "tuberin", "TSC complex", "TSC1 TSC2 mTOR", "TSC1 tuberous sclerosis", "TSC2 tuberous sclerosis", "TSC2 RCC"]
sources:
  - id: crino-2006-tsc-review
    type: peer-reviewed
    cite: "Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. N Engl J Med. 2006;355(13):1345-1356."
    doi: "10.1056/NEJMra055323"
    pmid: "17005952"
    url: "https://doi.org/10.1056/NEJMra055323"
  - id: northrup-2013-tsc-consensus
    type: peer-reviewed
    cite: "Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. Pediatr Neurol. 2013;49(4):243-254."
    doi: "10.1016/j.pediatrneurol.2013.08.001"
    pmid: "24053982"
    url: "https://doi.org/10.1016/j.pediatrneurol.2013.08.001"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "TSC1-TSC2 complex inactivates Rheb (GTPase); TSC1/TSC2 LOF → Rheb-GTP → mTORC1 hyperactivation → S6K1 + 4EBP1 → ribosome biogenesis and cell growth; everolimus + sirolimus are first-line systemic therapy in TSC; TSC1/TSC2 LOF is the defining mTOR pathway tumor suppressor event"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK phosphorylates TSC2 at T1462 → TSC1-TSC2 activation → Rheb inhibition → mTORC1 OFF; STK11-AMPK-TSC2-mTOR is the energy sensing pathway; AMPK activation (metformin, AICAR) → TSC2 → mTOR suppression; TSC2 is the node linking energy status to mTOR via AMPK"
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "mTOR hyperactivation in TSC → 4EBP1/eIF4E → increased HIF-1α translation → VEGF → angiomyolipoma vascularity; anti-VEGF therapies explored in TSC-LAM; HIF-1α contributes to tumor growth in angiomyolipomas and SEGA; HIF-1α mRNA translation is a key mTORC1 output"
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "TSC → mTOR → 4EBP1 → eIF4E → HIF-1α translation → VEGF secretion → angiogenesis in TSC hamartomas (angiomyolipoma, SEGA); bevacizumab explored in TSC-LAM; VEGF expression correlates with angiomyolipoma growth in TSC; VEGF-A is the dominant angiogenic driver in TSC"
---

# TSC1-TSC2

## Overview

**TSC1** (tuberous sclerosis complex 1; hamartin; 1,164 aa; 130 kDa) and **TSC2** (tuberous sclerosis complex 2; tuberin; 1,807 aa; 198 kDa) form an obligate heterodimeric **GTPase-activating protein (GAP) complex** that functions as the primary brake on **mTORC1** (mechanistic target of rapamycin complex 1) activity. The TSC1-TSC2 complex inactivates **Rheb** (Ras homolog enriched in brain), a small GTPase that directly activates the mTOR kinase within mTORC1: TSC2 acts as the catalytic GAP subunit (stimulating Rheb GTPase activity → Rheb-GDP → inactive), while TSC1 acts as the scaffold stabilizing TSC2 from proteasomal degradation. Loss of TSC1 or TSC2 function → Rheb constitutively GTP-loaded → mTORC1 permanently active → S6K1, 4EBP1, SREBP, HIF-1α translation → uncontrolled cell growth, proliferation, and protein synthesis. Germline pathogenic variants in either TSC1 or TSC2 cause **tuberous sclerosis complex (TSC)**, an autosomal dominant hamartoma syndrome affecting brain, kidney, lung, skin, heart, and eye. TSC1-TSC2 also integrates signals from multiple upstream pathways: AMPK (energy sensor, activates TSC2 via phosphorylation), AKT (growth factor, inhibits TSC2), ERK, and GSK-3β all converge on TSC2 to modulate mTORC1 in response to nutrient and growth factor status [^crino-2006-tsc-review] [^northrup-2013-tsc-consensus].

**TSC1-TSC2 in cancer:**

| Tumor type | Gene | Frequency | Notes |
|---|---|---|---|
| Clear cell RCC (sporadic) | TSC1 or TSC2 | ~5-10% | mTOR-sensitive; everolimus; associated with chromophobe RCC also |
| Bladder transitional cell carcinoma | TSC1 | ~8-15% | TSC1 LOF; everolimus explored |
| Tuberous sclerosis complex (germline) | TSC1 or TSC2 | ~100% | Hamartomas; benign; mTOR-driven |
| Hepatocellular carcinoma | TSC1/TSC2 | ~5-8% | mTOR pathway; somatic |
| Chromophobe RCC (sporadic) | TSC1/TSC2 | ~20% | mTOR-enriched subtype |

**TSC1 vs TSC2 phenotype comparison:**

| Feature | TSC1 germline | TSC2 germline |
|---|---|---|
| Frequency | ~33% of TSC | ~67% of TSC |
| Clinical severity | Milder | More severe |
| Cognitive impairment | Less frequent | More frequent |
| Seizures | Less severe | More severe |
| Renal angiomyolipoma | ~65% | ~85% |
| LAM | ~40% (women) | ~60-80% (women) |
| Cortical tubers | Fewer, smaller | More, larger |

## Structure

### TSC1 protein (hamartin)

**N-terminal dimerization domain (aa 1-302):**
Coiled-coil domain; TSC1 homodimerization; required for TSC1 stability; TSC1 is the scaffold subunit — it does not have intrinsic enzymatic activity; TSC1-TSC1 homodimer allows nucleation of higher-order TSC1-TSC2 assemblies

**TSC2-binding domain (aa 302-430):**
Coiled-coil; binds TSC2 N-terminal region; TSC1-TSC2 heterodimerization is essential — TSC2 is unstable without TSC1; TSC1 protects TSC2 from HERC1-mediated ubiquitination and proteasomal degradation; when TSC1 is lost, TSC2 is degraded → functional loss of the complex even though TSC2 gene is intact

**ERM-binding (ezrin-radixin-moesin) domain (C-terminal):**
TSC1 interacts with ERM proteins at the plasma membrane; anchors the TSC1-TSC2 complex to membranes where Rheb is localized; membrane targeting ensures TSC2 GAP activity is positioned near Rheb

### TSC2 protein (tuberin)

**Rap-GAP domain (aa 1517-1674; C-terminal):**
Ras superfamily GAP (GTPase-activating protein); specifically activates Rheb GTPase → converts Rheb-GTP → Rheb-GDP → inactive; arginine finger (Arg1743) critical for catalysis; mutations in Rap-GAP domain → loss of Rheb-GAP activity without disrupting TSC1 binding; highly penetrant pathogenic variants cluster here

**HEAT repeats (aa 1-984):**
Huntingtin, EF3, A subunit of PP2A, TOR repeats; protein-protein interaction scaffold; HEAT repeats of TSC2 bind GABARAP (autophagy receptor), CLIP-170, and multiple other interactors; HEAT repeats also interact with AKT binding proteins

**Phosphorylation-regulation domain:**
Multiple serine/threonine phosphorylation sites that integrate upstream signals:
- **T1462**: phosphorylated by AMPK → ACTIVATES TSC2 GAP activity → mTORC1 inhibition (energy depletion signal)
- **S939, S981, T1462**: phosphorylated by AKT → INHIBITS TSC2 → mTORC1 activation (growth factor signal)
- **S664**: phosphorylated by ERK → inhibits TSC2 → mTORC1 activation (MAPK-to-mTOR crosstalk)
- **S1387**: phosphorylated by AMPK → ACTIVATES TSC2 → additional energy-sensing site
- Net result: TSC2 integrates AMPK (energy), AKT (growth), ERK (proliferation), and GSK-3β (Wnt) signals into a unified mTORC1 output

### TSC1-TSC2 mutation patterns

**Germline pathogenic variants:**
- TSC1: truncating > missense; pathogenic missense uncommon for TSC1 (mostly at conserved interfaces); splice-site mutations ~15%
- TSC2: broader missense pathogenicity; Rap-GAP domain missense variants are pathogenic; large deletions/rearrangements ~5-10%; contiguous deletion syndrome (TSC2-PKD1 contiguous gene deletion on 16p13.3) → TSC + polycystic kidney disease simultaneously
- De novo mutations: ~66-75% of TSC cases are de novo (no family history); autosomal dominant with high penetrance but frequently arising de novo
- Mosaicism: ~15-20% of TSC patients without identifiable germline variant have somatic mosaicism in TSC1 or TSC2; detected by sensitive NGS (allele fraction 2-15%) in saliva, skin, or blood

**Somatic two-hit model:**
Each individual TSC hamartoma (cortical tuber, angiomyolipoma, SEGA) requires biallelic inactivation of TSC1 or TSC2: germline first hit + somatic second hit (LOH or somatic mutation) in the progenitor cell of each lesion; this accounts for the mosaic distribution of hamartomas (not all cells affected); somatic TSC2 mutation (second hit) found in TSC-associated angiomyolipoma cancer regions when malignant transformation occurs

## Function

### TSC1-TSC2 as mTORC1 regulator

**The Rheb-mTOR axis:** [^crino-2006-tsc-review]
Rheb (Ras homolog enriched in brain): small GTPase; in GTP-bound form → directly activates mTOR kinase within mTORC1 (via FKBP38/RHEB interaction with mTOR FAT domain); GTP-loading of Rheb → mTOR catalytic activation → substrate phosphorylation; TSC2 GAP (arginine finger R1743 mechanism): positions Rheb Gln64 water molecule → accelerates GTP hydrolysis 1000-fold → Rheb-GDP → mTOR inactive

**mTORC1 outputs:**
When TSC1-TSC2 LOF → Rheb-GTP → mTORC1 constitutively active:
1. **S6K1 (ribosomal protein S6 kinase 1) phosphorylation at T389**: → S6K1 active → phosphorylates ribosomal protein S6 (rpS6/S6) and eIF4B → ribosome biogenesis → increased translational capacity → cell growth
2. **4EBP1 (eIF4E-binding protein 1) phosphorylation at T37/T46/S65/T70**: → 4EBP1 releases eIF4E → eIF4E joins eIF4F complex → cap-dependent mRNA translation enhanced; HIF-1α mRNA and VEGF mRNA are cap-dependent → increased translation → angiogenesis, Warburg metabolism
3. **ULK1 phosphorylation at S758**: → ULK1 inhibited → autophagy suppressed → protein accumulation
4. **TFEB phosphorylation at S211**: → 14-3-3 sequesters TFEB → nuclear TFEB suppressed → lysosomal biogenesis reduced
5. **Lipin 1 phosphorylation**: → promotes lipid synthesis → phospholipid and fatty acid production for membrane biogenesis

**Upstream pathway integration:**
Multiple oncogenic inputs converge on TSC1-TSC2 to release mTORC1:
- **Growth factors → RTK → PI3K → AKT**: AKT phosphorylates TSC2 at S939/S981 → TSC2 inactivated → mTOR ON; this is how PTEN LOF activates mTOR
- **KRAS/BRAF → MEK → ERK**: ERK phosphorylates TSC2 at S664 → mTOR ON; KRAS-mutant tumors have partial mTOR activation through this pathway
- **Amino acids**: Ragulator-Rag GTPase complex senses amino acids → Rag-A/B-GTP recruits mTORC1 to lysosomal surface → activates mTOR independently of TSC2
- **Energy → AMPK**: AMPK phosphorylates TSC2 at T1462 → TSC2 activated → mTOR OFF; AMPK directly phosphorylates raptor (mTORC1 subunit) at S792 → raptor-14-3-3 sequestration → additional mTORC1 inhibition

## Mechanism

### Therapeutic targeting of TSC1-TSC2 LOF

**Rapalogues in TSC:**
- **Everolimus** (RAD001; 10 mg/day PO): FDA-approved for:
  - TSC-associated renal angiomyolipoma (AML) ≥3 cm (FDA 2012): EXIST-2 Phase 3 (N=118): AML response rate 42% vs 0% placebo; AML volume reduction sustained; PFS significantly improved; reduces hemorrhage risk (AML >4 cm at high risk for spontaneous hemorrhage, Wunderlich syndrome)
  - TSC-associated SEGA (subependymal giant cell astrocytoma) (FDA 2012): EXIST-1 Phase 3: 35% reduction in SEGA volume vs 0% placebo; prevents progressive hydrocephalus
  - TSC-associated pulmonary LAM (FDA 2018): EXIST-2 subgroup; LAM volume stabilized; FEV1 preserved
  - Adjunctive therapy for TSC-associated partial-onset seizures (FDA 2018): EXIST-3 Phase 3: median seizure frequency reduction 29% vs 0% placebo
- **Sirolimus** (rapamycin): predecessor mTORC1 inhibitor; used off-label in TSC-associated LAM; MILES trial (sirolimus in LAM): FEV1 improved during treatment but returned to baseline after stopping; sirolimus is the current standard for LAM; FDA-approved for LAM (not TSC-specific)

**Rapalogue mechanism:**
Rapamycin (sirolimus) and everolimus bind FKBP12 → FKBP12-rapamycin complex binds mTOR FKBP-rapamycin-binding (FRB) domain → allosteric inhibition of mTORC1 kinase → partial S6K1 inhibition (nearly complete) + partial 4EBP1 inhibition (incomplete); this incompleteness of 4EBP1 inhibition explains limited anti-proliferative effect in many tumors; rapalogues are cytostatic (stop growth) not cytotoxic (do not kill cells) → regrowth on discontinuation → lifelong therapy often required

**Rapalogue side effects:**
- Class effects: stomatitis/mucositis (~30%), infections (~30%), hyperlipidemia (~30%), hyperglycemia (~15%), pneumonitis (~5-10%)
- TSC-specific concern: neuropsychiatric — rare cases of psychiatric deterioration on everolimus; monitoring required
- Drug interactions: CYP3A4 substrate; avoid strong inhibitors (azole antifungals, HIV PIs) or inducers (rifampin, carbamazepine)

**mTOR kinase inhibitors (next generation):**
- Torin1, PP242 (INK128): catalytic mTOR kinase inhibitors; inhibit both mTORC1 AND mTORC2; complete 4EBP1 inhibition (unlike rapalogues); superior pre-clinical anti-tumor activity in TSC models; clinical development ongoing
- AZD8055, AZD2014 (vistusertib): mTOR kinase inhibitors in Phase 1/2 for TSC-associated tumors; greater 4EBP1 inhibition; exploration in refractory TSC-AML and SEGA

**Seizure management in TSC:**
- First-line antiepileptics: vigabatrin (GABA transaminase inhibitor) — first-line for infantile spasms in TSC (70-80% response); carbamazepine, valproate, levetiracetam for focal seizures
- mTOR-targeted epilepsy: EXIST-3 trial established everolimus as adjunctive treatment for TSC-associated refractory seizures; Brambler trial ongoing
- Surgical: cortical tuber resection if epileptogenic zone identified by MEG/EEG dipole mapping; seizure freedom in ~50% of well-selected TSC patients with resectable tubers

## Connections

- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TSC1-TSC2 complex inactivates Rheb (GTPase); TSC1/TSC2 LOF → Rheb-GTP → mTORC1 hyperactivation → S6K1 + 4EBP1 → ribosome biogenesis and cell growth; everolimus + sirolimus are first-line systemic therapy in TSC; TSC1/TSC2 LOF is the defining mTOR pathway tumor suppressor event
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK phosphorylates TSC2 at T1462 → TSC1-TSC2 activation → Rheb inhibition → mTORC1 OFF; STK11-AMPK-TSC2-mTOR is the energy sensing pathway; AMPK activation (metformin, AICAR) → TSC2 → mTOR suppression; TSC2 is the node linking energy status to mTOR via AMPK
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — mTOR hyperactivation in TSC → 4EBP1/eIF4E → increased HIF-1α translation → VEGF → angiomyolipoma vascularity; anti-VEGF therapies explored in TSC-LAM; HIF-1α contributes to tumor growth in angiomyolipomas and SEGA; HIF-1α mRNA translation is a key mTORC1 output
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — TSC → mTOR → 4EBP1 → eIF4E → HIF-1α translation → VEGF secretion → angiogenesis in TSC hamartomas (angiomyolipoma, SEGA); bevacizumab explored in TSC-LAM; VEGF expression correlates with angiomyolipoma growth in TSC; VEGF-A is the dominant angiogenic driver in TSC

[^crino-2006-tsc-review]: Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. *N Engl J Med.* 2006;355(13):1345-1356. [doi:10.1056/NEJMra055323](https://doi.org/10.1056/NEJMra055323) · [PubMed 17005952](https://pubmed.ncbi.nlm.nih.gov/17005952/)
[^northrup-2013-tsc-consensus]: Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. *Pediatr Neurol.* 2013;49(4):243-254. [doi:10.1016/j.pediatrneurol.2013.08.001](https://doi.org/10.1016/j.pediatrneurol.2013.08.001) · [PubMed 24053982](https://pubmed.ncbi.nlm.nih.gov/24053982/)
