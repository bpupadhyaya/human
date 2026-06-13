---
schema: human-scale-entry/v1
id: desmoid-tumor
name: Desmoid Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Desmoid tumor (aggressive fibromatosis) is a locally invasive spindle cell neoplasm; ~80% harbor CTNNB1 activating mutations; no metastatic potential; nirogacestat (gamma-secretase inhibitor, DeFi trial) FDA-approved 2023; sorafenib active; watch-and-wait for stable disease."
aliases: ["desmoid tumor", "aggressive fibromatosis", "desmoid fibromatosis", "deep fibromatosis", "desmoid CTNNB1", "FAP desmoid", "mesenteric fibromatosis", "sporadic desmoid", "beta-catenin fibromatosis", "APC desmoid"]
sources:
  - id: gounder-2023-nirogacestat-desmoid
    type: peer-reviewed
    cite: "Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a gamma-secretase inhibitor, for desmoid tumors. N Engl J Med. 2023;388(10):898-912."
    doi: "10.1056/NEJMoa2209457"
    pmid: "36884316"
    url: "https://doi.org/10.1056/NEJMoa2209457"
  - id: lazar-2008-ctnnb1-desmoid
    type: peer-reviewed
    cite: "Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. Am J Pathol. 2008;173(5):1518-1527."
    doi: "10.2353/ajpath.2008.080475"
    pmid: "18832571"
    url: "https://doi.org/10.2353/ajpath.2008.080475"
cross_links:
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "CTNNB1 activating mutations (S45F, T41A, S33C) in ~80% sporadic desmoid tumors → nuclear β-catenin → TCF/LEF-dependent transcription → MYC, CCND1 → desmoid fibroblast proliferation; APC germline mutations (FAP) account for ~20%; CTNNB1 T41A predicts best prognosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13)."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC germline truncating mutations (codons 1310-2011) cause FAP; ~20% of desmoid tumors arise in FAP via APC LOF → insufficient β-catenin destruction → nuclear β-catenin → Wnt targets; FAP mesenteric desmoid is the leading non-cancer cause of death post-colectomy in FAP patients."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "FAP (germline APC) carries ~10-20% lifetime desmoid tumor risk; FAP mesenteric desmoid is the leading non-cancer cause of mortality in post-colectomy FAP; laparotomy wound triggers mesenteric desmoid; prophylactic sulindac and close surveillance are standard at FAP centers."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Desmoid tumor arises from fibroblastic/myofibroblastic progenitors in CTNNB1-mutant cells triggered by trauma or surgery; desmoid myofibroblasts (αSMA+, nuclear β-catenin) secrete dense collagen and resist apoptosis; TGF-β amplifies myofibroblastic activation in desmoid stroma."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Desmoid tumors and GISTs are intra-abdominal mesenchymal tumors often confused on imaging but molecularly opposite: desmoid is a non-metastasizing fibroblastic proliferation driven by CTNNB1/APC-Wnt, while GIST is a KIT/PDGFRA-driven Cajal-cell tumor that can metastasize."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Mesenteric desmoid tumors arise in the small-bowel mesentery, especially after abdominal surgery in FAP, encasing mesenteric vessels and bowel; this infiltrative, non-metastasizing growth causes obstruction, ischemia, and fistulae — a leading non-cancer cause of death in FAP."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Extra-abdominal desmoids (aggressive fibromatosis) of the shoulder, abdominal wall, and limbs are locally infiltrative soft-tissue tumors that recur after resection but never metastasize; since surgery often triggers regrowth, surveillance and systemic drugs are first-line."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Desmoid tumors are a hallmark of familial adenomatous polyposis (Gardner syndrome), the same APC/Wnt disorder that causes colorectal cancer: ~10-15% of FAP patients develop desmoids, often intra-abdominal and triggered by colectomy, where they become a leading cause of death."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Desmoid tumors are frequently hormone-responsive: many express estrogen receptors, can grow during pregnancy or with oral contraceptives and regress after menopause, so anti-estrogens (tamoxifen) with NSAIDs are an established option for these non-metastasizing fibromatoses."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Desmoid tumors are driven by a profibrotic program in which TGF-β is central: alongside constitutive Wnt/β-catenin, TGF-β stimulates myofibroblasts to lay down the dense collagenous matrix that makes desmoids infiltrative and locally destructive—the hallmark of fibromatosis."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Desmoid tumor and synovial sarcoma are both deep soft-tissue tumors but biologically apart: desmoid is a locally aggressive fibroblastic proliferation driven by CTNNB1/Wnt that never metastasizes, while synovial sarcoma is a malignant SS18-SSX sarcoma that does."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Desmoid tumor and Ewing sarcoma both arise in young people but differ: desmoid is a non-metastasizing fibromatosis often managed by active surveillance, whereas Ewing is an aggressive EWSR1-FLI1 small-round-cell sarcoma needing intensive chemo and radiation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Desmoid tumors are linked to the reproductive system through estrogen and pregnancy: many are estrogen-responsive and can grow during or after pregnancy, and abdominal-wall desmoids classically follow childbirth—so hormonal therapy is one treatment option."
---

# Desmoid Tumor

## Overview

**Desmoid tumor** (deep/aggressive fibromatosis) is a rare, locally invasive, clonally derived spindle cell neoplasm of fibroblastic/myofibroblastic origin that lacks the capacity for metastasis but causes significant morbidity through relentless local infiltration and destruction of adjacent structures. Desmoid tumors are driven in ~80% of sporadic cases by **activating mutations in CTNNB1 (exon 3)**, resulting in constitutive nuclear β-catenin accumulation and TCF/LEF-driven transcription; in ~20%, they arise from **germline APC mutations** in the setting of familial adenomatous polyposis (FAP). Despite being classified as low-grade neoplasms (WHO soft tissue 2020: intermediate — locally aggressive), desmoid tumors cause significant morbidity from infiltration of bowel, mesentery, abdominal wall, extremity musculature, and neurovascular structures [^lazar-2008-ctnnb1-desmoid].

**Epidemiology:**
- Incidence: ~2-4 per million/year; ~900-1,200 cases/year USA
- Age: median 30-40 years; wide range (pediatric to elderly); F:M ~2-3:1 in sporadic cases (hormonal influence — regression during menopause; worsening with estrogen)
- Pregnancy: desmoids can appear or accelerate during pregnancy (estrogen-mediated); post-pregnancy regression possible
- FAP-associated: ~10-20% of FAP patients develop desmoid; FAP desmoid typically mesenteric; accounts for ~15-20% of desmoid morbidity/mortality in FAP post-colectomy era

**Anatomic locations:**

| Location | Frequency | Key features |
|---|---|---|
| Abdominal wall | ~40% | Sporadic; often post-surgical/post-trauma; best prognosis; wide excision usually feasible |
| Mesenteric/intraabdominal | ~35% | FAP>sporadic; encases bowel mesentery; ureteral obstruction; small bowel obstruction; high morbidity |
| Extra-abdominal (extremity, trunk, chest wall) | ~25% | Infiltrates muscle compartments; neurovascular encasement; limb function impaired; recurrence common |
| Head and neck | ~5% | Airway compromise; CN involvement; disfiguring; surgical approach challenging |

**Natural history:**
- Highly variable: ~20-30% of desmoids demonstrate spontaneous regression without treatment
- ~30-40% remain stable for months to years
- ~30-50% progress locally; rapid early progression (first 6-12 months) predicts more aggressive behavior
- No metastatic potential; desmoid is not malignant in the classical oncologic sense
- Local recurrence: ~25-60% after surgery; positive margins not clearly associated with recurrence (controversial)
- Pregnancy-associated: may regress postpartum or after menopause; progesterone may accelerate growth

## Structure

### Histology

**Classic desmoid histology:**
- Uniform bland spindle cells (fibroblasts/myofibroblasts) arranged in long fascicles sweeping in parallel arrays or storiform pattern
- Abundant collagen matrix (pale pink on H&E); "keloid-like" collagen bands
- Elongated bipolar nuclei with vesicular chromatin; 1-2 inconspicuous nucleoli
- Very low mitotic rate (<2/10 HPF); NO atypical mitoses; NO pleomorphism
- Keloid-like hypocellular zones adjacent to hypercellular zones
- Infiltrative borders — tendrils of tumor cells penetrate surrounding fat and muscle (histological hallmark)

**IHC panel:**
- **β-catenin (nuclear)**: nuclear positivity ~85-90% in CTNNB1-mutant sporadic desmoid; weak or membrane-only in FAP-associated (where APC is truncated but CTNNB1 is WT); most specific desmoid marker
- **SMA (smooth muscle actin)**: positive in ~80-90%; myofibroblastic differentiation
- **MSA (muscle-specific actin)**: positive ~70%
- **Vimentin**: diffusely positive
- **Desmin**: focal positive ~10-20%
- **S100**: negative (helpful to exclude nerve sheath tumors)
- **CD34**: negative (helpful to exclude SFT)
- **STAT6**: negative (helps exclude SFT)
- **SOX10**: negative

**Molecular confirmation:**
- CTNNB1 Sanger sequencing (exon 3) or NGS panel: mandatory for ambiguous cases
- APC germline testing: offered to all desmoid patients <40 years, mesenteric location, family history
- CTNNB1 S45F/Y → higher recurrence risk; T41A → lower risk [^lazar-2008-ctnnb1-desmoid]

## Function

### CTNNB1-driven oncogenesis in desmoid

Desmoid tumors arise from fibroblastic/myofibroblastic mesenchymal progenitors in response to triggering events:

**Sporadic desmoid triggers:**
- Trauma/surgery (~40% of cases have history of prior trauma/surgery at the site): physical disruption → fibroblast proliferation → in cells harboring CTNNB1 mutation, proliferative signal persists
- Estrogen: desmoid fibroblasts express estrogen receptor α; estrogen → ERα → β-catenin nuclear translocation amplification; pregnancy-associated growth; anti-estrogen therapy (tamoxifen, toremifene) exploits this

**FAP-associated desmoid:**
- Germline APC truncation (especially codons 1310-2011) → insufficient APC → increased β-catenin; colectomy trigger → laparotomy wound → desmoid at abdominal wall or mesentery; risk: APC genotype (specific mutation sites predispose to mesenteric vs abdominal wall)

**β-catenin/TCF target program in desmoid cells:**
- MYC → drives fibroblast proliferation
- CCND1 (cyclin D1) → CDK4/6 → cell cycle
- VEGFA → angiogenesis (explains vascularity visible on MRI)
- MMP2/9 → matrix degradation → invasion
- DKK1 (secreted Wnt inhibitor) → negative feedback (often silenced in CTNNB1-mutant desmoid, removing the brake)
- AXIN2 → negative feedback (partially functional; explains why some desmoids stabilize)

## Pathology

### Staging and risk stratification

**No standard TNM staging** for desmoid; no metastases possible; risk stratified by:
- **Mutation type** (CTNNB1 S45F > T41A for recurrence)
- **Location** (mesenteric worst; abdominal wall best prognosis)
- **Size**: larger tumors (>10 cm) behave more aggressively
- **Age**: younger patients (<30) have higher recurrence rates
- **FAP vs sporadic**: FAP mesenteric desmoid particularly aggressive and difficult to resect
- **Rate of growth**: rapid early growth → poor prognosis; initial stability → may spontaneously plateau

### Treatment

**Watch and wait (active surveillance):**
Standard initial approach for newly diagnosed desmoid without symptoms or rapid growth; ~20-30% regress spontaneously; monthly or bi-monthly MRI surveillance; intervention deferred until progression, pain, or functional compromise; evidence: prospective observational data from DESMOID-1 (N=439) showed 46% had no treatment in first 3 years; 28-month progression-free rate ~59%

**Nirogacestat (gamma-secretase/Notch inhibitor) — FDA-approved November 2023:** [^gounder-2023-nirogacestat-desmoid]
- **DeFi Phase 3** (Gounder 2023): N=142 adults with progressing desmoid; nirogacestat 150 mg BID vs placebo; primary endpoint PFS; PFS HR 0.29 (95% CI 0.15-0.55, p<0.0001); median PFS not reached vs 15.1 months placebo; ORR 41% vs 8%; time to response median ~5.5 months; most responses durable; OS benefit trending
- Toxicity: diarrhea (grade 3: 12%), ovarian toxicity (amenorrhea, elevated FSH in premenopausal women: ~75% → reversible in most after discontinuation), rash (~35%), fatigue (~30%)
- FDA approved for adults with progressing desmoid tumors; pediatric approval pending
- First FDA-approved drug for desmoid tumors

**Sorafenib:**
- Phase 2 SARC026 (Gounder 2018, N=87): sorafenib 400 mg/day vs placebo; PFS HR 0.13 (p<0.0001); ORR 33% vs 20% at 6 months; widely used off-label for progressive desmoid prior to nirogacestat approval; toxicity: hand-foot syndrome (~40%), fatigue, hypertension

**Hormonal therapy:**
- Tamoxifen 40-120 mg/day or toremifene: ER-based strategy; ORR ~10-15% single agent; widely used in combination with NSAIDs (sulindac); desmoid regression reported especially in post-menopausal patients; safe long-term; low-cost option for stable/slowly growing disease
- NSAID (sulindac 300-400 mg/day): anti-inflammatory → reduces desmoid vascularity; ORR ~10-15% as monotherapy; synergizes with anti-estrogen; mechanism: COX-2 → PGE2 → β-catenin stabilization loop; sulindac breaks this

**Chemotherapy:**
- Methotrexate + vinca alkaloid (vinblastine or vinorelbine): ORR ~40-50% in pediatric/young adult progressive desmoid; used as cytotoxic-sparing protocol; weekly administration; main toxicity: myelosuppression, neuropathy; also used in adult FAP-associated mesenteric disease
- Doxorubicin + dacarbazine: ORR ~20-30%; for rapidly progressive, large-burden, or life-threatening desmoid (mesenteric encasement, ureteral obstruction); similar to soft tissue sarcoma chemotherapy approach
- Pegylated liposomal doxorubicin: ORR ~15-25%; less cardiotoxicity; used in patients who need prolonged doxorubicin

**Surgery:**
- Historically first-line; now reserved for specific indications: abdominal wall desmoid (easily resectable, low recurrence), symptomatic bowel obstruction, failed systemic therapy with isolated resectable disease
- Wide negative margin surgery: recurrence rates ~25-60% regardless of margin status (controversy: positive margins may not increase recurrence in desmoid)
- Surgery CONTRAINDICATED as first-line for: mesenteric desmoid (high morbidity, high recurrence), large extremity/trunk desmoid (amputation not justified for non-malignant tumor), rapidly growing desmoid (active systemic therapy preferred)
- Post-operative stimulus: surgery itself can trigger desmoid growth at anastomosis/scar sites in FAP patients

**Radiation therapy:**
- Used for unresectable, chemotherapy-refractory, or post-surgical recurrence
- 50-56 Gy in 25-28 fractions; local control ~70-80% at 5 years in resectable desmoid; 50-60% in unresectable
- Long-term radiation toxicity concerns (secondary malignancy, fibrosis, neuropathy) limit use; not for young patients or mesenteric disease

**Prognosis:**
- No disease-specific mortality from desmoid in most cases (no metastases); mortality from local complications (bowel obstruction, ureteral obstruction, superior mesenteric artery encasement in FAP mesenteric desmoid)
- Abdominal wall: 5-year recurrence-free survival after resection ~60-75%
- Mesenteric/FAP: most clinically challenging; leading non-cancer cause of mortality in FAP patients post-colectomy; multiple surgical procedures often needed
- Spontaneous regression: ~20-30% (best outcome); regression may take 3-5 years
- Nirogacestat era: median PFS not reached in responders; 2-year PFS ~70% in nirogacestat arm

## Connections

- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — CTNNB1 activating mutations (S45F, T41A, S33C) in ~80% sporadic desmoid tumors → nuclear β-catenin → TCF/LEF-dependent transcription → MYC, CCND1 → desmoid fibroblast proliferation; APC germline mutations (FAP) account for ~20%; CTNNB1 T41A predicts best prognosis.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13).
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC germline truncating mutations (codons 1310-2011) cause FAP; ~20% of desmoid tumors arise in FAP via APC LOF → insufficient β-catenin destruction → nuclear β-catenin → Wnt targets; FAP mesenteric desmoid is the leading non-cancer cause of death post-colectomy in FAP patients.
- `connects-to` → **[FAP](../fap/README.md)** — FAP (germline APC) carries ~10-20% lifetime desmoid tumor risk; FAP mesenteric desmoid is the leading non-cancer cause of mortality in post-colectomy FAP; laparotomy wound triggers mesenteric desmoid; prophylactic sulindac and close surveillance are standard at FAP centers.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Desmoid tumor arises from fibroblastic/myofibroblastic progenitors in CTNNB1-mutant cells triggered by trauma or surgery; desmoid myofibroblasts (αSMA+, nuclear β-catenin) secrete dense collagen and resist apoptosis; TGF-β amplifies myofibroblastic activation in desmoid stroma.
- `connects-to` → **[GIST](../gist/README.md)** — Desmoid tumors and GISTs are intra-abdominal mesenchymal tumors often confused on imaging but molecularly opposite: desmoid is a non-metastasizing fibroblastic proliferation driven by CTNNB1/APC-Wnt, while GIST is a KIT/PDGFRA-driven Cajal-cell tumor that can metastasize.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Mesenteric desmoid tumors arise in the small-bowel mesentery, especially after abdominal surgery in FAP, encasing mesenteric vessels and bowel; this infiltrative, non-metastasizing growth causes obstruction, ischemia, and fistulae — a leading non-cancer cause of death in FAP.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Extra-abdominal desmoids (aggressive fibromatosis) of the shoulder, abdominal wall, and limbs are locally infiltrative soft-tissue tumors that recur after resection but never metastasize; since surgery often triggers regrowth, surveillance and systemic drugs are first-line.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Desmoid tumors are a hallmark of familial adenomatous polyposis (Gardner syndrome), the same APC/Wnt disorder that causes colorectal cancer: ~10-15% of FAP patients develop desmoids, often intra-abdominal and triggered by colectomy, where they become a leading cause of death.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Desmoid tumors are frequently hormone-responsive: many express estrogen receptors, can grow during pregnancy or with oral contraceptives and regress after menopause, so anti-estrogens (tamoxifen) with NSAIDs are an established option for these non-metastasizing fibromatoses.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Desmoid tumors are driven by a profibrotic program in which TGF-β is central: alongside constitutive Wnt/β-catenin, TGF-β stimulates myofibroblasts to lay down the dense collagenous matrix that makes desmoids infiltrative and locally destructive—the hallmark of fibromatosis.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Desmoid tumor and synovial sarcoma are both deep soft-tissue tumors but biologically apart: desmoid is a locally aggressive fibroblastic proliferation driven by CTNNB1/Wnt that never metastasizes, while synovial sarcoma is a malignant SS18-SSX sarcoma that does.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Desmoid tumor and Ewing sarcoma both arise in young people but differ: desmoid is a non-metastasizing fibromatosis often managed by active surveillance, whereas Ewing is an aggressive EWSR1-FLI1 small-round-cell sarcoma needing intensive chemo and radiation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Desmoid tumors are linked to the reproductive system through estrogen and pregnancy: many are estrogen-responsive and can grow during or after pregnancy, and abdominal-wall desmoids classically follow childbirth—so hormonal therapy is one treatment option.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^gounder-2023-nirogacestat-desmoid]: Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a gamma-secretase inhibitor, for desmoid tumors. *N Engl J Med.* 2023;388(10):898-912. [doi:10.1056/NEJMoa2209457](https://doi.org/10.1056/NEJMoa2209457) · [PubMed 36884316](https://pubmed.ncbi.nlm.nih.gov/36884316/)
[^lazar-2008-ctnnb1-desmoid]: Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. *Am J Pathol.* 2008;173(5):1518-1527. [doi:10.2353/ajpath.2008.080475](https://doi.org/10.2353/ajpath.2008.080475) · [PubMed 18832571](https://pubmed.ncbi.nlm.nih.gov/18832571/)
