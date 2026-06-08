---
schema: human-scale-entry/v1
id: von-willebrand-factor
name: Von Willebrand Factor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Von Willebrand factor (VWF; chr12p13.3) is a plasma glycoprotein that bridges platelet GPIb to subendothelial collagen at sites of injury; carries FVIII in circulation; deficiency → VWD; ULVWF → TTP. Emicizumab bridges FIXa/FX bypassing FVIII in hemophilia A."
aliases: ["VWF", "von Willebrand factor", "vWF", "VWD antigen", "factor VIII carrier", "ULVWF", "ultra-large von Willebrand factor", "vWF multimers"]
sources:
  - id: sadler-1998-vwf-review
    type: peer-reviewed
    cite: "Sadler JE. Biochemistry and genetics of von Willebrand factor. Annu Rev Biochem. 1998;67:395-424."
    doi: "10.1146/annurev.biochem.67.1.395"
    pmid: "9759493"
    url: "https://doi.org/10.1146/annurev.biochem.67.1.395"
  - id: lillicrap-2013-vwf-review
    type: peer-reviewed
    cite: "Lillicrap D. von Willebrand disease: advances in pathogenetic understanding, diagnosis, and therapy. Blood. 2013;122(23):3735-3740."
    doi: "10.1182/blood-2013-06-498303"
    pmid: "24100444"
    url: "https://doi.org/10.1182/blood-2013-06-498303"
  - id: federici-2006-vwd-treatment
    type: peer-reviewed
    cite: "Federici AB, Mannucci PM, Castaman G, et al. Clinical and molecular predictors of thrombocytopenia and risk of bleeding in patients with von Willebrand disease type 2B: a cohort study of 67 patients. Blood. 2009;113(3):526-534."
    doi: "10.1182/blood-2008-04-152280"
    pmid: "18805967"
    url: "https://doi.org/10.1182/blood-2008-04-152280"
cross_links:
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "ADAMTS13 cleaves ULVWF at Tyr1605-Met1606 in the VWF A2 domain; ADAMTS13 deficiency → ULVWF accumulation on endothelium → platelet microthrombi → TTP; caplacizumab blocks VWF A1 domain → prevents GPIb-mediated platelet tethering to ULVWF strings."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation in iTTP."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "VWF carries and protects FVIII from proteolytic degradation in plasma (t½ FVIII ~2 h vs. ~12 h VWF-bound); VWF deficiency → secondary FVIII deficiency (VWD type 3 = severe VWD with FVIII <10 IU/dL); emicizumab (bispecific FIXa/FX antibody) bypasses FVIII dependence on VWF."
---

# Von Willebrand Factor

## Overview

**Von Willebrand factor (VWF)** is a large multimeric plasma glycoprotein (gene *VWF*, chromosome 12p13.3) that performs two essential hemostatic functions: **primary hemostasis** (bridging activated platelets to injured subendothelium via GPIb/VWF A1 and collagen/VWF A3 domain interactions) and **FVIII chaperone** (binding and protecting coagulation factor VIII in plasma, prolonging its half-life from ~2 hours to ~12 hours) [^sadler-1998-vwf-review].

VWF is synthesized in **endothelial cells** (principal source; stored in Weibel-Palade bodies) and **megakaryocytes** (stored in platelet alpha-granules) and circulates as an enormous range of multimers (from dimers to ultra-large multimers of >10 MDa). The largest multimers — ultra-large VWF (ULVWF) — are the most thrombogenic, with the greatest number of GPIb-binding A1 domains per molecule. Under normal conditions, **ADAMTS13** cleaves newly released ULVWF to maintain a controlled multimer distribution. When ADAMTS13 is deficient (<10% activity), ULVWF accumulates → **thrombotic thrombocytopenic purpura (TTP)**.

**Clinical diseases affecting VWF:**
- **Von Willebrand disease (VWD):** Most common inherited bleeding disorder (~1% of population); caused by VWF deficiency (quantitative: types 1, 3) or dysfunction (qualitative: type 2); presents as mucocutaneous bleeding, epistaxis, menorrhagia
- **Thrombotic thrombocytopenic purpura (TTP):** ADAMTS13 deficiency → ULVWF-platelet microthrombi → TMA
- **Acquired VWF syndrome:** VWF degradation by proteases in high-shear states (aortic stenosis → Heyde's syndrome; LVAD; severe aortic regurgitation)
- **Hemophilia A carrier effect:** VWF deficiency causes secondary FVIII reduction (VWD type 3: FVIII <10 IU/dL)

## Structure

### Protein architecture

| Feature | Detail |
|:--------|:-------|
| Gene | *VWF*, chromosome 12p13.3; 178 kb, 52 exons |
| Pre-pro-VWF | 2813 aa; signal peptide (22 aa) + propeptide (763 aa) + mature VWF (2050 aa) |
| Mature VWF | ~220 kDa monomer; heavily glycosylated (~22% carbohydrate by mass); N-linked and O-linked glycans |
| Multimers | Dimers → tetramers → ULVWF (>50 monomers; >10 MDa); largest found on endothelial surface |
| Key domains | D1-D2 (propeptide; for dimerization) → D'-D3 (FVIII binding; propeptide cleavage site Arg763) → A1 (GPIb + heparin binding; botrocetin/ristocetin-binding site) → A2 (ADAMTS13 cleavage site Tyr1605-Met1606) → A3 (collagen I/III binding) → D4-B1-B3-C1-C2 (integrin αIIbβ3 binding) → CK (C-terminal cysteines; dimerization) |

### Weibel-Palade bodies and secretion

- Endothelial Weibel-Palade bodies (WPBs) are specialized secretory organelles that store ULVWF in a helical, tubular conformation stabilized by P-selectin
- **Constitutive secretion:** Low-level continuous VWF release into plasma
- **Regulated secretion (stimulated exocytosis):** Triggered by thrombin, histamine, vasopressin (DDAVP/desmopressin), epinephrine, shear stress → rapid ULVWF release from WPBs → strings of ULVWF on endothelial surface anchored by P-selectin → platelet recruitment

### Conformational states and shear-dependent function

**Globular conformation (low shear):** VWF A1 domain is shielded by flanking D'D3 and A2 domains + autoinhibitory interaction of D4 with A1 → GPIb binding masked; prevents spontaneous platelet adhesion

**Extended conformation (high shear ≥50-70 dyne/cm²):** Shear force stretches VWF → D4-A1 interaction broken → A1 domain exposed → GPIb binding enabled → platelet tethering and rolling. Simultaneously, A2 domain unfolds → exposes Tyr1605-Met1606 for ADAMTS13 cleavage — a mechanoregulatory feedback loop

## Function

### Primary hemostasis — platelet bridging

At sites of vessel injury, the subendothelial matrix (collagen I, III; fibronectin; heparan sulfate) is exposed → VWF A3 domain binds collagen → immobilized VWF undergoes shear-induced conformational extension → A1 domain exposed → **platelet GPIbα** (von Willebrand receptor) tethers platelet to VWF → rolling and firm adhesion → platelet activation → GPIIbIIIa (αIIbβ3) engagement of VWF C1-C2 domain → stable platelet plug. Under high shear conditions (arterioles, stenotic vessels), VWF-GPIb is the primary adhesion mechanism — fibrinogen-GPIIbIIIa interactions dominate at lower shear.

### FVIII chaperone

VWF binds FVIII at the VWF D'D3 domain (via FVIII light chain C1-C2 domain). The VWF-FVIII complex:
- Protects FVIII from premature proteolysis (by thrombin, APC, FXa) and clearance via LRP1
- Prolongs FVIII plasma half-life from ~2 hours (unbound) to ~12 hours (VWF-bound)
- Delivers FVIII to sites of vascular injury (released from VWF when platelet GPIb competes for VWF binding or thrombin cleaves VWF)
- **Clinical consequence:** VWD type 3 (VWF <1 IU/dL) → secondary FVIII deficiency (FVIII 1-10 IU/dL) → bleeding phenotype resembling mild hemophilia A

### ULVWF regulation by ADAMTS13

Immediately after ULVWF release from Weibel-Palade bodies, ADAMTS13 cleaves ULVWF at the Tyr1605-Met1606 peptide bond in the A2 domain (exposed under shear) → generates smaller VWF multimers with fewer platelet-binding A1 domains → reduced thrombogenic potential. Without ADAMTS13: ULVWF strings persist on endothelium → capture platelets → microvascular platelet thrombi → **TTP** (see: TTP entry).

## Mechanism

### VWF A1 domain — drug target

The VWF A1 domain is the target of **caplacizumab** (Sanofi/Ablynx) — a bivalent nanobody (VHH single-domain antibody fragment) that binds VWF A1 with high affinity:
- Blocks GPIbα-A1 interaction → prevents platelet tethering to ULVWF
- Does NOT cleave ULVWF (ADAMTS13-independent mechanism)
- Reverses platelet microthrombus formation rapidly (platelet count rises within 1-2 days in iTTP) while plasma exchange (PEX) removes anti-ADAMTS13 antibodies and restores ADAMTS13 activity

**Ristocetin co-factor assay:** Ristocetin (a former antibiotic) binds VWF A1 domain → forces VWF-GPIb interaction → induces platelet agglutination *in vitro*; VWF ristocetin co-factor activity (VWF:RCo) assesses functional VWF A1 domain integrity; VWD type 2B (gain-of-function A1 domain mutation) → enhanced ristocetin-induced platelet aggregation (RIPA) at low ristocetin concentrations.

### Von Willebrand disease — molecular classification

**VWD Type 1 (quantitative mild, ~75% of VWD):**
- Partial VWF deficiency: VWF:Ag 20-50 IU/dL (normal: 50-150 IU/dL); all multimers present
- Mechanism: Heterozygous *VWF* mutations → haploinsufficiency; increased VWF clearance (group O blood type: ~25% lower VWF due to increased A1 domain glycan cleavage)
- Treatment: DDAVP (desmopressin; releases VWF from endothelial WPBs; effective in type 1)

**VWD Type 2 (qualitative):**
- **Type 2A:** Loss of high-molecular-weight multimers; A2 domain mutations → enhanced ADAMTS13 cleavage or impaired multimerization
- **Type 2B:** Gain-of-function A1 domain mutations → spontaneous GPIb binding → thrombocytopenia + loss of HMWM; DDAVP contraindicated (worsens thrombocytopenia)
- **Type 2M:** Decreased VWF-GPIb interaction without loss of HMWM; VWF:RCo/VWF:Ag ratio <0.6
- **Type 2N (Normandy):** FVIII-binding domain mutations (D'D3) → secondary FVIII deficiency; resembles hemophilia A (autosomal inheritance; can be missed)

**VWD Type 3 (quantitative severe, <1% of VWD):**
- VWF:Ag <1 IU/dL; FVIII 1-10 IU/dL; absent VWF multimers; biallelic *VWF* mutations
- Severe mucocutaneous bleeding + joint/muscle bleeding (FVIII-dependent)
- Treatment: VWF/FVIII concentrate (Humate-P, Wilate) — DDAVP ineffective

### Treatment of VWD

**DDAVP (desmopressin; vasopressin V2R agonist):**
- Releases VWF from endothelial Weibel-Palade bodies via V2R → cAMP → WPB exocytosis
- 3-5× VWF increase within 30-60 minutes; most effective in type 1 VWD
- IV: 0.3 µg/kg over 30 min; intranasal: 150-300 µg/dose (Stimate; high-concentration DDAVP)
- Tachyphylaxis: WPB stores depleted after 2-3 doses; 24-hour refractory period

**VWF concentrate (purified from plasma):**
- Humate-P (VWF:FVIII ~2.4:1), Alphanate, Wilate — for surgical prophylaxis, type 2B, type 3
- Vonvendi (recombinant VWF; rVWF; FDA 2015): plasma-derived FVIII-free; used with/without FVIII; type 3 VWD major bleeding

**Antifibrinolytics:**
- Tranexamic acid: Inhibits plasminogen → fibrin stabilization; adjunctive for mucosal bleeding (dental, menorrhagia)
- Aminocaproic acid: Similar mechanism; alternative

## Connections

- `connects-to` → **[ADAMTS13](../adamts13/README.md)** — ADAMTS13 cleaves ULVWF at Tyr1605-Met1606 in the VWF A2 domain; ADAMTS13 deficiency → ULVWF accumulation → platelet microthrombi → TTP; caplacizumab blocks VWF A1 domain → prevents GPIb-mediated platelet tethering to ULVWF strings.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../../07-system/thrombotic-thrombocytopenic-purpura/README.md)** — ULVWF from Weibel-Palade bodies accumulates in TTP (ADAMTS13 deficiency) → GPIb-mediated platelet aggregation → microthrombi; caplacizumab (anti-VWF A1 nanobody; FDA 2019) blocks ULVWF-platelet tethering → fastest reversal of acute microthrombus formation in iTTP.
- `connects-to` → **[Hemophilia A](../../07-system/hemophilia-a/README.md)** — VWF carries and protects FVIII from proteolytic degradation in plasma (t½ FVIII alone ~2 h vs. ~12 h bound to VWF); VWF deficiency → secondary FVIII deficiency (VWD type 3 = severe VWD with FVIII <10 IU/dL); emicizumab (bispecific FIXa/FX antibody) bypasses FVIII dependence on VWF.

[^sadler-1998-vwf-review]: Sadler JE. Biochemistry and genetics of von Willebrand factor. *Annu Rev Biochem.* 1998;67:395-424. [doi:10.1146/annurev.biochem.67.1.395](https://doi.org/10.1146/annurev.biochem.67.1.395) · [PubMed 9759493](https://pubmed.ncbi.nlm.nih.gov/9759493/)
[^lillicrap-2013-vwf-review]: Lillicrap D. von Willebrand disease: advances in pathogenetic understanding, diagnosis, and therapy. *Blood.* 2013;122(23):3735-3740. [doi:10.1182/blood-2013-06-498303](https://doi.org/10.1182/blood-2013-06-498303) · [PubMed 24100444](https://pubmed.ncbi.nlm.nih.gov/24100444/)
[^federici-2006-vwd-treatment]: Federici AB, Mannucci PM, Castaman G, et al. Clinical and molecular predictors of thrombocytopenia and risk of bleeding in patients with von Willebrand disease type 2B. *Blood.* 2009;113(3):526-534. [doi:10.1182/blood-2008-04-152280](https://doi.org/10.1182/blood-2008-04-152280) · [PubMed 18805967](https://pubmed.ncbi.nlm.nih.gov/18805967/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
