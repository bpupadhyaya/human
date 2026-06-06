---
schema: medicine-entry/v1
id: dexamethasone
name: Dexamethasone
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Potent synthetic glucocorticoid (25× cortisol potency); GR-mediated genomic suppression of NF-κB/AP-1 → ↓ IL-1/6/8/TNF. Zero mineralocorticoid activity. RECOVERY trial: 17% mortality ↓ in severe COVID-19. Also used for cerebral edema, anaphylaxis, adrenal crisis, antiemesis."
aliases: ["dexamethasone", "Decadron", "Dexasone", "Maxidex", "dexamethasone sodium phosphate", "9α-fluoro-16α-methylprednisolone"]
sources:
  - id: horby-2021-recovery
    type: peer-reviewed
    cite: "RECOVERY Collaborative Group; Horby P, Lim WS, et al. Dexamethasone in Hospitalized Patients with Covid-19. N Engl J Med. 2021;384(8):693-704."
    doi: "10.1056/NEJMoa2021436"
    pmid: "32678530"
    url: "https://doi.org/10.1056/NEJMoa2021436"
  - id: vandewalle-2018-glucocorticoid-mechanism
    type: peer-reviewed
    cite: "Vandewalle J, Luypaert A, De Bosscher K, Libert C. Therapeutic Mechanisms of Glucocorticoids. Trends Endocrinol Metab. 2018;29(1):42-54."
    doi: "10.1016/j.tem.2017.10.010"
    pmid: "29162310"
    url: "https://doi.org/10.1016/j.tem.2017.10.010"
  - id: rhen-2005-glucocorticoids
    type: peer-reviewed
    cite: "Rhen T, Cidlowski JA. Antiinflammatory action of glucocorticoids — new mechanisms for old drugs. N Engl J Med. 2005;353(16):1711-23."
    doi: "10.1056/NEJMra050541"
    pmid: "16236742"
    url: "https://doi.org/10.1056/NEJMra050541"
  - id: vecht-1994-dex-cerebral-edema
    type: peer-reviewed
    cite: "Vecht CJ, Hovestadt A, Verbiest HB, van Vliet JJ, van Putten WL. Dose-effect relationship of dexamethasone on Karnofsky performance in metastatic brain tumors. Neurology. 1994;44(4):675-80."
    doi: "10.1212/wnl.44.4.675"
    pmid: "8164826"
    url: "https://doi.org/10.1212/WNL.44.4.675"
cross_links:
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: targets
    evidence: rhen-2005-glucocorticoids
    note: "Dexamethasone binds cytoplasmic GR (NR3C1) with high affinity → GR:GRE transactivation (anti-inflammatory genes: lipocortin-1/ANXA1, IL-10, MKP-1) + GR tethering to NF-κB/AP-1 → transrepression of pro-inflammatory cytokine genes (IL-1β, TNFα, IL-6, IL-8, COX-2)."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    evidence: rhen-2005-glucocorticoids
    note: "A primary mechanism of glucocorticoid anti-inflammatory action is physical protein-protein interaction between GR and the p65 (RelA) subunit of NF-κB → mutual repression without direct DNA binding (transrepression) → reduced IL-1β, TNFα, IL-6, CXCL8, VCAM-1 gene transcription."
---

# Dexamethasone

## Overview

**Dexamethasone** (Decadron) is a synthetic **fluorinated glucocorticoid** with approximately **25–30 times the anti-inflammatory potency** of cortisol (hydrocortisone) and, crucially, **zero mineralocorticoid activity** — making it the preferred glucocorticoid when sodium retention and fluid overload would be problematic. It was first synthesized in 1957 and has been on the WHO Essential Medicines List since 1977.

Dexamethasone's clinical landscape spans from acute emergencies (cerebral edema, anaphylaxis, acute adrenal crisis, spinal cord compression) to chronic disease management (inflammatory disorders, hematological malignancies), perioperative care, and cancer supportive care (chemotherapy-induced nausea/vomiting, pain). Its 2020 moment came with the **RECOVERY trial**, which demonstrated a 17% reduction in 28-day mortality in hospitalized COVID-19 patients requiring oxygen — establishing it as the first treatment proven to save lives in COVID-19 [^horby-2021-recovery].

## Mechanism

**Glucocorticoid receptor (GR) signaling — two major pathways:**

**1. Genomic transactivation (GRE-dependent):**
- Dexamethasone (lipophilic, MW 392 Da) crosses the cell membrane and binds cytoplasmic **GR (glucocorticoid receptor, NR3C1)** with high affinity (Ki ~5 nM; ~10× higher than cortisol)
- GR:dexamethasone complex dissociates from Hsp90/Hsp70/FKBP51 chaperone complex → nuclear translocation
- GR homodimer binds **GREs (glucocorticoid response elements)** in promoters of target genes → transactivation of:
  - **Annexin A1 (ANXA1/Lipocortin-1):** Inhibits phospholipase A2 → ↓ arachidonic acid release → ↓ prostaglandin/leukotriene synthesis
  - **DUSP1/MKP-1 (MAP kinase phosphatase-1):** Inactivates JNK and p38 MAPK → ↓ AP-1 activity
  - **IκBα:** Inhibitor of NF-κB; dexamethasone upregulates IκBα → sequesters NF-κB in cytoplasm
  - **IL-10:** Anti-inflammatory cytokine upregulation [^vandewalle-2018-glucocorticoid-mechanism]

**2. Genomic transrepression (tethering to NF-κB/AP-1):**
- GR physically interacts with **NF-κB (RelA/p65)** and **AP-1 (c-Fos/c-Jun)** via protein-protein tethering — without direct DNA binding
- Mutual inhibition: GR suppresses NF-κB-driven gene transcription; this is the dominant mechanism of anti-inflammatory cytokine suppression
- Genes repressed: IL-1β, TNFα, IL-6, IL-8 (CXCL8), COX-2, iNOS, ICAM-1, MMP-9 [^rhen-2005-glucocorticoids]

**3. Non-genomic effects (rapid, minutes):**
- Membrane-associated GR and direct physicochemical membrane effects
- Rapid inhibition of arachidonic acid release (seconds-minutes, before transcriptional effects)
- Important for clinical effects seen within minutes of IV dexamethasone (e.g., airway edema reduction)

**Potency comparison (anti-inflammatory / mineralocorticoid):**

| Glucocorticoid | Anti-inflammatory potency | Mineralocorticoid potency | Plasma t½ | Biological t½ |
|:---|:---|:---|:---|:---|
| Hydrocortisone (cortisol) | 1× | 1× | 1.5 h | 8–12 h |
| Prednisolone | 4× | 0.8× | 3 h | 12–36 h |
| Methylprednisolone | 5× | 0.5× | 3 h | 12–36 h |
| **Dexamethasone** | **25–30×** | **~0** | **3.5–4.5 h** | **36–72 h** |

The long biological half-life (36–72 h) allows once-daily (or less frequent) dosing.

## Clinical Use

**Cerebral edema (tumor/abscess/radiation):**
- Mechanism: reduces tumor vasogenic edema by decreasing VEGF expression in tumor cells and restoring blood-brain barrier integrity
- Dose: 10 mg IV loading → 4 mg IV/IM q6h; taper over weeks as tumor treated [^vecht-1994-dex-cerebral-edema]

**COVID-19 (severe/critical):**
- RECOVERY trial: 6 mg OD PO/IV × 10 days in hospitalized patients requiring oxygen
- 28-day mortality: 22.9% vs 25.7% (RR 0.83, 95% CI 0.74–0.93) — 17% relative mortality reduction [^horby-2021-recovery]
- Greatest benefit in ventilated patients (29% mortality reduction); no benefit in those not requiring oxygen (possibly harmful)
- Mechanism: suppresses cytokine storm (late-stage immunopathological injury) in severe COVID-19

**Croup (laryngotracheobronchitis):**
- Single dose 0.15–0.6 mg/kg PO/IM (max 10 mg); reduces return visits, hospitalization, and stridor within 2–4 hours; most cost-effective intervention in croup

**Anaphylaxis/severe allergic reactions:**
- Adjunct to epinephrine (not first-line); prevents biphasic anaphylaxis; typical 8–10 mg IV/IM

**Chemotherapy antiemesis:**
- 8–20 mg IV before chemotherapy; synergizes with 5-HT3 antagonists (ondansetron) for complete emesis prevention; essential component of high-emetogenic chemotherapy regimens

**Adrenal crisis / adrenal insufficiency:**
- High-stress dosing (surgery, critical illness): 100 mg hydrocortisone equivalent (4 mg dexamethasone × 25); or switch to hydrocortisone 100 mg IV

**Adverse effects — dose and duration dependent:**
- Short-term (days): hyperglycemia (up to 10 mmol/L BG rise; requires insulin in diabetics), insomnia, mood changes (euphoria/dysphoria), increased appetite, immunosuppression
- Long-term (weeks-months): Cushing's syndrome (moon face, truncal obesity, striae), osteoporosis (bone loss 5–10% in first year), adrenal suppression (HPA axis), cataracts, glaucoma, avascular necrosis (femoral head), myopathy, peptic ulceration (especially with NSAIDs)
- Dexamethasone suppression test: 1 mg overnight → used to screen for Cushing's syndrome (suppresses ACTH; cortisol should fall <50 nmol/L in normal subjects)

## Evidence

| Trial / Study | Key Finding |
|:---|:---|
| RECOVERY (Horby 2021) [^horby-2021-recovery] | 6 mg OD × 10 days: 28-day mortality 22.9% vs 25.7% (RR 0.83); greatest benefit in mechanically ventilated patients |
| Croup RCT meta-analysis | Single oral dexamethasone 0.15–0.6 mg/kg: significantly reduces severity score, hospitalization rate, and return visits vs placebo; equivalent to nebulized budesonide |
| Cerebral edema series (Vecht 1994) [^vecht-1994-dex-cerebral-edema] | Dexamethasone 4 mg q6h vs 8 mg q6h: equivalent efficacy for cerebral edema from metastatic tumors; supports lower dosing |
| Mechanism reviews (Rhen 2005, Vandewalle 2018) [^rhen-2005-glucocorticoids] [^vandewalle-2018-glucocorticoid-mechanism] | GR transactivation + transrepression dual mechanism established as basis of anti-inflammatory action |

## Connections

- **Targets** → [Glucocorticoid Receptor (GR)](../../../../../01-human/03-molecular/glucocorticoid-receptor/README.md): High-affinity GR agonist → homodimerization → GRE transactivation (ANXA1, DUSP1, IκBα, IL-10) + NF-κB/AP-1 transrepression.
- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): GR tethers to RelA/p65, mutually inhibiting NF-κB-driven transcription of IL-1β, TNFα, IL-6, IL-8, COX-2 — the primary mechanism of clinical anti-inflammatory effect.
