---
schema: human-scale-entry/v1
id: bladder-cancer
name: Bladder Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Urothelial carcinoma of the bladder; FGFR3 mutations in ~25-35% and TERT promoter mutations in ~75%; PD-L1 expression guides immunotherapy. BCG is standard for non-muscle-invasive disease; enfortumab vedotin + pembrolizumab is first-line for metastatic urothelial carcinoma."
aliases: ["urothelial carcinoma", "bladder urothelial carcinoma", "transitional cell carcinoma", "NMIBC", "MIBC", "metastatic urothelial carcinoma", "mUC", "bladder TCC"]
sources:
  - id: bellmunt-2017-keynote045
    type: peer-reviewed
    cite: "Bellmunt J, de Wit R, Vaughn DJ, et al. Pembrolizumab as second-line therapy for advanced urothelial carcinoma. N Engl J Med. 2017;376(11):1015-1026."
    doi: "10.1056/NEJMoa1613683"
    pmid: "28212060"
    url: "https://doi.org/10.1056/NEJMoa1613683"
  - id: powles-2024-ev302
    type: peer-reviewed
    cite: "Powles T, Valderrama BP, Gupta S, et al. Enfortumab vedotin and pembrolizumab in untreated advanced urothelial cancer. N Engl J Med. 2024;390(10):875-888."
    doi: "10.1056/NEJMoa2312117"
    pmid: "38261487"
    url: "https://doi.org/10.1056/NEJMoa2312117"
  - id: loriot-2019-erdafitinib
    type: peer-reviewed
    cite: "Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. N Engl J Med. 2019;381(4):338-348."
    doi: "10.1056/NEJMoa1817323"
    pmid: "31340094"
    url: "https://doi.org/10.1056/NEJMoa1817323"
cross_links:
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR3 is mutated or fused in ~25-35% of urothelial carcinoma (S249C, FGFR3-TACC3 common); mutated FGFR3 drives proliferation and is enriched in low-grade NMIBC; erdafitinib (THOR trial: OS 12.1 vs. 7.8 months vs. pembrolizumab) is FDA-approved for FGFR-altered bladder cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-L1 drives immune evasion in urothelial carcinoma; pembrolizumab improves OS vs. chemotherapy in post-platinum mUC (KEYNOTE-045: OS 10.3 vs. 7.4 months); enfortumab vedotin + pembrolizumab (EV-302) is now first-line standard for metastatic urothelial carcinoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations (C228T/C250T) occur in ~75% of urothelial carcinoma — among the highest frequencies in any cancer; TERT mutation is one of the earliest carcinogenic events (present in dysplasia and NMIBC); urine TERT mutation detection enables non-invasive surveillance."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 loss occurs in ~20% of muscle-invasive bladder cancer (MIBC), co-occurring with TP53 mutation; RB1 deletion correlates with basal-squamous MIBC subtype and poor prognosis; RB pathway disruption also mediated by CDKN2A homozygous deletion in ~30% of MIBC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 is mutated in ~48% of MIBC; co-deletion with RB1 defines the basal/squamous MIBC subtype (high PD-L1, cisplatin-sensitive); TERT promoter + TP53 mutations co-occur in high-grade UC; TP53 mutation in CIS is an early checkpoint failure enabling invasive progression."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome (germline MLH1/MSH2) confers ~5× lifetime bladder UC risk; dMMR bladder cancer (~3-4% of UC) has high TMB → pembrolizumab active regardless of PD-L1 (KEYNOTE-158); dMMR IHC/MSI-H testing recommended for early-onset or Lynch-suspected urothelial carcinoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A mutations in ~25% of MIBC; SWI/SNF chromatin remodeler; ARID1A LOF → impaired nucleosome remodeling at tumor suppressor promoters; co-mutated with TP53 and KDM6A; ARID1A-mutant MIBC may have synthetic lethality with EZH2 inhibition (tazemetostat combinations under study)."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Bladder cancer is one disease across the whole urinary-tract lining: the same urothelium covers the renal pelvis and ureters, so ~5% of bladder-cancer patients harbour synchronous upper-tract urothelial carcinoma, and a tumour obstructing a ureter causes hydronephrosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Bladder cancer pioneered immunotherapy: intravesical BCG provokes a Th1 response that recruits CD8+ cytotoxic T cells to patrol the urothelium and prevent recurrence of non-muscle-invasive disease — and the same T cells are reactivated by PD-1/PD-L1 checkpoint blockade."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Cervical and bladder cancer are linked through the pelvis: pelvic radiotherapy for cervical cancer is itself a risk factor for later bladder cancer, both are strongly smoking- or carcinogen-associated, and both are driven by insults delivered to a vulnerable epithelium."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Bladder and prostate cancers are the commonest genitourinary malignancies and frequent neighbors: they co-occur in older men, share smoking and age risk, and locally advanced disease of one can invade the other; pelvic surgery and shared follow-up imaging link their care."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Bladder cancer is a disease of the whole urothelial lining: the same field-effect carcinogens (smoking, aromatic amines) that transform the bladder can produce synchronous or metachronous tumors of the renal pelvis and ureter, so the entire upper urinary tract needs surveillance."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Bladder cancer is the birthplace of cancer immunotherapy: intravesical BCG—live attenuated mycobacteria—triggers a local immune response that has prevented recurrence of non-muscle-invasive bladder cancer for decades, and PD-1/PD-L1 inhibitors now treat advanced disease."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Bladder and renal cell carcinoma are the two major urologic cancers but differ in cell and cause: bladder cancer is a smoking-linked urothelial tumor with painless hematuria, while RCC arises from renal tubular epithelium—both can shed cells detectable in urine."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Bladder cancer and lung cancer are the paradigm smoking-caused epithelial cancers: tobacco carcinogens excreted in urine bathe and transform the bladder urothelium just as inhaled smoke transforms the bronchus, so the two often coexist and both are reshaped by immunotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Bladder cancer pioneered macrophage-based immunotherapy: intravesical BCG provokes a local immune response in which macrophages and T cells attack residual tumor, making early non-muscle-invasive bladder cancer one of the first cancers cured by harnessing innate immunity."
---

# Bladder Cancer

## Overview

**Bladder cancer** is the most common malignancy of the urinary tract and the **fourth most common cancer in men** in the United States (~82,000 new cases and ~17,000 deaths annually). Approximately **90% are urothelial carcinoma (UC)**, arising from the urothelium lining the bladder; the remainder include squamous cell carcinoma (SCC), adenocarcinoma, and small cell/neuroendocrine carcinoma. The disease spans two biologically distinct entities: **non-muscle-invasive bladder cancer (NMIBC)** — highly recurrent but rarely lethal, and **muscle-invasive bladder cancer (MIBC)** — life-threatening with ~50% 5-year OS after radical cystectomy [^powles-2024-ev302].

**Incidence and risk factors:**
- **Smoking:** The dominant risk factor (~50% of bladder cancers attributable to tobacco); tobacco carcinogens (polycyclic aromatic hydrocarbons, aromatic amines) are excreted in urine → prolonged urothelial exposure; risk 2-4× vs. non-smokers; cessation reduces but does not eliminate risk
- **Occupational exposures:** Aromatic amines (benzidine, beta-naphthylamine) in dye, rubber, leather, paint, and hairdressing industries; latency period of 20-40 years; OSHA regulations have reduced but not eliminated occupational risk
- **Chronic bladder irritation:** Schistosoma haematobium infection → squamous cell carcinoma (endemic in sub-Saharan Africa and Egypt; ~50% of bladder cancers in high-prevalence regions are SCC)
- **Radiation:** Prior pelvic radiotherapy (cervical, prostate cancer) → increased bladder cancer risk (latency 10-20 years)
- **Cyclophosphamide:** Alkylating agent → acrolein (toxic metabolite) accumulates in urine → urothelial DNA damage; MESNA (2-mercaptoethane sulfonate) administered with cyclophosphamide to prevent urothelial acrolein exposure
- **Arsenic in drinking water:** Strong epidemiological association, particularly in areas with high well-water arsenic
- **Hereditary:** Lynch syndrome (*MLH1, MSH2* mutations) → ~5× lifetime bladder cancer risk; otherwise hereditary risk is rare and not well-defined

**Molecular subtypes:**

NMIBC and MIBC have distinct molecular landscapes:

*NMIBC molecular features:*
- **FGFR3 mutation (~60% of low-grade NMIBC):** FGFR3 S249C (most common), R248C, Y375C → constitutive homodimerization; FGFR3 mutation is a low-grade feature (inversely correlated with grade); FGFR3 and RAS/MAPK mutations are largely mutually exclusive
- **TERT promoter mutation (~75% of all UC):** C228T and C250T; the most frequent alteration across all stages; telomerase reactivation → cellular immortalization; detectable in urine → liquid biopsy potential
- **CCND1 amplification:** ~10-15% of NMIBC; cyclin D1 overexpression → CDK4/6-RB → E2F-driven proliferation

*MIBC molecular subtypes (TCGA 2017):*
- **Luminal papillary (35%):** FGFR3 fusions, FGFR3/ERB-B2 alterations; Wnt pathway active; best prognosis; responds to FGFR inhibitors and anti-PD-L1 (though lower TIL density)
- **Luminal unstable (5%):** RB1 alterations, highly genomically unstable; intermediate
- **Luminal non-specified (6%):** High immune infiltration
- **Stroma-rich (15%):** PDGFRA/DGK signatures; smooth muscle and stroma dominant; resistant to chemotherapy and immunotherapy
- **Basal/squamous (35%):** TP53 + RB1 co-deletion; high squamous differentiation; high PD-L1; high TIL; high cisplatin sensitivity; responds well to neoadjuvant chemotherapy
- **Neuronal (5%):** Neuroendocrine features; SCLC-like; worst prognosis; platinum + etoposide

**Key somatic alterations in MIBC (TCGA):**
- *TERT* promoter: ~75%
- *TP53*: ~48%
- *KDM6A*: ~26% (lysine demethylase; chromatin regulator; the most common tumor suppressor in UC after TP53)
- *FGFR3* (mutation + fusion): ~20%
- *RB1*: ~20%
- *CDKN2A*: ~31% (homozygous deletion)
- *ERBB2 (HER2)*: ~11% amplification; ~6% mutation
- *PIK3CA*: ~22%
- *MLL2/KMT2D*: ~27%
- *ARID1A*: ~25%

## Structure

### Bladder anatomy and urothelial biology

**Bladder anatomy:**
- Hollow muscular organ (~500 mL capacity) in the pelvis; collects and stores urine from the ureters; three layers: **urothelium** (transitional epithelium, the target of UC), **lamina propria** (vascular/connective tissue; muscularis mucosae — a thin muscle layer used for staging), **muscularis propria (detrusor muscle)** — invasion of detrusor = muscle-invasive
- **Trigone:** Base of bladder; ureteral orifices and urethral opening; cancers here are common (intersection of urine flow); proximal ureter/UPJ may be involved

**Urothelium histology:**
- 3-7 cell layers; **umbrella cells** (superficial; binucleated; glycocalyx-rich); **intermediate cells**; **basal cells** (stem cell compartment; KRT5+/KRT14+/TP63+)
- **Urothelial differentiation markers:** FOXA1, GATA3 (transcription factors); uroplakins (UPKI/II/III) → tight junctions and impermeability; cytokeratin 20 (KRT20) — luminal marker
- **Carcinogenesis:** Two parallel pathways: (1) FGFR3-activated → papillary low-grade NMIBC (high recurrence, low invasion risk); (2) TP53/RB1-disrupted → flat high-grade CIS → MIBC (high invasion, poor prognosis)

**Staging (TNM, 8th edition):**
- **Ta:** Non-invasive papillary (urothelium only); NMIBC
- **Tis (CIS):** Flat high-grade carcinoma in situ; not papillary; NMIBC but aggressive
- **T1:** Invades lamina propria (not muscularis propria); NMIBC
- **T2:** Invades muscularis propria (inner T2a, outer T2b); MIBC — key threshold
- **T3:** Perivesical fat (T3a microscopic, T3b macroscopic); MIBC
- **T4:** Adjacent organ invasion (T4a prostate/uterus/vagina; T4b pelvic/abdominal wall)
- **N:** Regional lymph nodes
- **M:** Distant metastasis

## Function

### Clinical presentation and diagnosis

**Presentation:**
- **Hematuria:** The hallmark of bladder cancer; gross (visible) or microscopic; painless gross hematuria requires cystoscopy; microscopic hematuria (≥3 RBC/HPF) in a patient >35 with risk factors → evaluation; hematuria is intermittent — a "negative" episode does not rule out cancer
- **Irritative symptoms (CIS):** Urgency, frequency, dysuria without UTI — classic presentation of bladder CIS (carcinoma in situ); often misdiagnosed as recurrent UTI; urine cytology → atypical or malignant cells → cystoscopy
- **Obstructive symptoms:** Ureteral involvement → hydronephrosis; urethral involvement → urinary retention; advanced MIBC/metastatic symptoms (flank pain, lower extremity edema from lymph node involvement)

**Diagnostic workup:**
- **Cystoscopy:** The definitive diagnostic tool; flexible cystoscopy (outpatient) → evaluate bladder mucosa; lesion identified → rigid cystoscopy under anesthesia → transurethral resection of bladder tumor (TURBT)
- **Urine cytology:** High sensitivity for high-grade UC and CIS (sensitivity ~70-80%); low sensitivity for low-grade papillary tumors (~20-30%); used for surveillance and initial evaluation; Paris System for Reporting Urinary Cytology standardizes reporting (atypical urothelial cells, SHGUC, HGUC, etc.)
- **Urine-based biomarkers:** FDA-approved tests (UroVysion FISH, NMP22, BTA test); NMP22 (nuclear matrix protein 22) — elevated in UC; none are sensitive enough to replace cystoscopy; urine TERT mutation PCR assay (clinical research) — high sensitivity/specificity for UC detection and surveillance
- **CT urography (CTU):** Contrast CT evaluating upper urinary tract + bladder; recommended for all new UC diagnosis to exclude upper tract UC (UTUC) — 5% of bladder UC patients have synchronous UTUC; also evaluates lymphadenopathy and metastases in MIBC

**TURBT (transurethral resection of bladder tumor):**
- Diagnostic and therapeutic for NMIBC; complete TURBT with muscularis propria in specimen critical (absence of muscularis propria → re-TURBT required); 2nd TURBT at 4-6 weeks for high-grade T1 disease to rule out understaging
- Histopathology: Grade (WHO 2004: low-grade/high-grade; or PUNLMP [papillary urothelial neoplasm of low malignant potential]), depth of invasion (Ta/Tis/T1/T2+), muscularis propria presence, lymphovascular invasion, variant histology (SCC, micropapillary, plasmacytoid, nested — all high-risk)

## Pathology

### Diagnosis and risk stratification (NMIBC)

**NMIBC risk stratification (EAU guidelines):**
- **Low risk:** Single, Ta, LG, <3 cm, no prior recurrence
- **Intermediate risk:** Ta/T1 LG, multifocal, >3 cm, or recurrence
- **High risk:** High-grade Ta/T1, CIS, T1HG with multiple/large/recurrent lesions, variant histology

**BCG (Bacillus Calmette-Guérin) immunotherapy for NMIBC:**
- Intravesical BCG (Connaught, TICE strains) is standard for intermediate-high risk NMIBC after TURBT; induction 6 weeks → maintenance (3-year schedule: 3 weeks at 3, 6, 12, 18, 24, 30, 36 months); BCG activates Th1 immune response → NK cells and CD8+ T cells → anti-urothelial immune surveillance
- BCG-unresponsive NMIBC (recurrence within 6 months of adequate BCG): **Pembrolizumab** (KEYNOTE-057: ORR 41%, CR 20% — FDA approved 2020); **nadofaragene firadenovec** (rAd-IFN/Syn3; intravesical adenovirus vector expressing IFN-alpha2b — FDA approved 2023 for BCG-unresponsive CIS); **nogapendekin alfa inbakicept** (IL-15 superagonist + pembrolizumab, LIO-1 trial — approved 2024 for BCG-unresponsive NMIBC)

### Treatment (MIBC and metastatic)

**Muscle-invasive bladder cancer (MIBC, T2-T4a) — localized:**
- **Neoadjuvant cisplatin-based chemotherapy (NAC) → radical cystectomy:** Standard for cisplatin-eligible MIBC; MVAC (methotrexate, vinblastine, doxorubicin, cisplatin) or GC (gemcitabine + cisplatin) → 5% absolute OS improvement (SWOG S8710); pathological complete response (pT0) is the strongest predictor of cure
- **Radical cystectomy:** Gold standard — cystoprostatectomy in men, anterior pelvic exenteration in women; extended lymph node dissection → ≥16 nodes; urinary diversion (ileal conduit or orthotopic neobladder); robotic-assisted increasingly used
- **Bladder preservation (TMT):** Trimodal therapy = maximal TURBT + concurrent chemoradiation (cisplatin or 5-FU + mitomycin + EBRT); for selected patients (unifocal T2, no CIS, complete TURBT, normal upper tracts); TMT-10 trial: 5-year OS ~57%; cystoscopy + biopsy to confirm complete response
- **Adjuvant nivolumab (CheckMate 274):** Pathological high-risk stage (pT3/T4 or pN+) after cystectomy; DFS benefit (HR 0.70); FDA approved 2021 for PD-L1 ≥1% and for cisplatin-ineligible patients regardless of PD-L1

**Metastatic urothelial carcinoma (mUC):**
- **First-line cisplatin-eligible:** Gemcitabine + cisplatin (GC; OS 14 months) OR dose-dense MVAC + G-CSF; **maintenance avelumab** after platinum-based chemotherapy (JAVELIN Bladder 100: OS benefit in PD-L1+ disease; FDA approved 2020) — now standard first-line approach after 4-6 cycles of GC
- **First-line enfortumab vedotin + pembrolizumab (EV-302) — NEW STANDARD [^powles-2024-ev302]:** Phase 3 trial in cisplatin-eligible and ineligible mUC; OS 31.5 vs. 16.1 months; PFS 12.5 vs. 6.3 months; ORR 67.7% vs. 44.4% vs. platinum + gemcitabine; FDA-approved December 2023; now the **preferred first-line regimen** for most patients with metastatic UC regardless of cisplatin eligibility or PD-L1 status
  - **Enfortumab vedotin (EV, Padcev):** Anti-Nectin-4 ADC; Nectin-4 is highly expressed on urothelial carcinoma; MMAE (monomethyl auristatin E) payload → microtubule disruption; hyperglycemia and peripheral neuropathy are key toxicities; skin rash (Nectin-4 expressed in skin)
- **Second-line pembrolizumab (KEYNOTE-045) [^bellmunt-2017-keynote045]:** OS 10.3 vs. 7.4 months vs. chemotherapy in post-platinum UC; FDA-approved 2017; now largely superseded by earlier pembrolizumab use in the EV-302 era
- **Erdafitinib (FGFR-altered mUC) [^loriot-2019-erdafitinib]:** Pan-FGFR1-4 inhibitor; THOR trial (2023): erdafitinib vs. pembrolizumab in FGFR3/2-altered cisplatin-pretreated UC → OS 12.1 vs. 7.8 months; FDA-approved; FGFR testing required (PCR or NGS for FGFR3 mutations/fusions, FGFR2 fusions)
- **Sacituzumab govitecan (Trodelvy):** Anti-Trop-2 ADC; SN-38 payload; TROPiCS-04 trial: OS benefit vs. chemotherapy in post-platinum/post-checkpoint mUC; FDA-approved
- **Cisplatin-ineligible first-line alternatives (pre-EV-302 era):** Carboplatin + gemcitabine; atezolizumab or pembrolizumab (accelerated approval withdrawn for PD-L1-unselected in 2021, retained for cisplatin-ineligible/PD-L1+ subsets)

**Upper tract urothelial carcinoma (UTUC):**
- Renal pelvis and ureter; managed with nephroureterectomy (gold standard); PYELOVAR trial: pemetrexed + cisplatin neoadjuvant for UTUC; adjuvant nivolumab (TCGA data) not yet standard; erdafitinib active (FGFR3 alterations in ~35% of UTUC)
- **Mitomycin C endoluminal delivery (Jelmyto):** FDA-approved 2020 for low-grade UTUC; novel silicone gel formulation allows prolonged upper tract contact

## Connections

- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR3 is mutated or fused in ~25-35% of urothelial carcinoma (S249C, FGFR3-TACC3 common); mutated FGFR3 drives proliferation and is enriched in low-grade NMIBC; erdafitinib (THOR trial: OS 12.1 vs. 7.8 months vs. pembrolizumab) is FDA-approved for FGFR-altered bladder cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-L1 drives immune evasion in urothelial carcinoma; pembrolizumab improves OS vs. chemotherapy in post-platinum mUC (KEYNOTE-045: OS 10.3 vs. 7.4 months); enfortumab vedotin + pembrolizumab (EV-302) is now first-line standard for metastatic urothelial carcinoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations (C228T/C250T) occur in ~75% of urothelial carcinoma — among the highest frequencies in any cancer; TERT mutation is one of the earliest carcinogenic events (present in dysplasia and NMIBC); urine TERT mutation detection enables non-invasive surveillance.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 loss occurs in ~20% of muscle-invasive bladder cancer (MIBC), co-occurring with TP53 mutation; RB1 deletion correlates with basal-squamous MIBC subtype and poor prognosis; RB pathway disruption also mediated by CDKN2A homozygous deletion in ~30% of MIBC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 is mutated in ~48% of MIBC; co-deletion with RB1 defines the basal/squamous MIBC subtype (high PD-L1, cisplatin-sensitive); TERT promoter + TP53 mutations co-occur in high-grade UC; TP53 mutation in flat CIS is an early checkpoint failure enabling invasive progression.
- `connects-to` → **[Lynch Syndrome](../../07-system/lynch-syndrome/README.md)** — Lynch syndrome (germline MLH1/MSH2) confers ~5× lifetime bladder UC risk; dMMR bladder cancer (~3-4% of UC) has high TMB → pembrolizumab active regardless of PD-L1 (KEYNOTE-158); dMMR IHC/MSI-H testing recommended for early-onset or Lynch-suspected urothelial carcinoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A mutations in ~25% of MIBC; SWI/SNF chromatin remodeler; ARID1A LOF → impaired nucleosome remodeling at tumor suppressor promoters; co-mutated with TP53 and KDM6A; ARID1A-mutant MIBC may have synthetic lethality with EZH2 inhibition (tazemetostat combinations under study).
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Bladder cancer is one disease across the whole urinary-tract lining: the same urothelium covers the renal pelvis and ureters, so ~5% of bladder-cancer patients harbour synchronous upper-tract urothelial carcinoma, and a tumour obstructing a ureter causes hydronephrosis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Bladder cancer pioneered immunotherapy: intravesical BCG provokes a Th1 response that recruits CD8+ cytotoxic T cells to patrol the urothelium and prevent recurrence of non-muscle-invasive disease — and the same T cells are reactivated by PD-1/PD-L1 checkpoint blockade.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Cervical and bladder cancer are linked through the pelvis: pelvic radiotherapy for cervical cancer is itself a risk factor for later bladder cancer, both are strongly smoking- or carcinogen-associated, and both are driven by insults delivered to a vulnerable epithelium.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Bladder and prostate cancers are the commonest genitourinary malignancies and frequent neighbors: they co-occur in older men, share smoking and age risk, and locally advanced disease of one can invade the other; pelvic surgery and shared follow-up imaging link their care.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Bladder cancer is a disease of the whole urothelial lining: the same field-effect carcinogens (smoking, aromatic amines) that transform the bladder can produce synchronous or metachronous tumors of the renal pelvis and ureter, so the entire upper urinary tract needs surveillance.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Bladder cancer is the birthplace of cancer immunotherapy: intravesical BCG—live attenuated mycobacteria—triggers a local immune response that has prevented recurrence of non-muscle-invasive bladder cancer for decades, and PD-1/PD-L1 inhibitors now treat advanced disease.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Bladder and renal cell carcinoma are the two major urologic cancers but differ in cell and cause: bladder cancer is a smoking-linked urothelial tumor with painless hematuria, while RCC arises from renal tubular epithelium—both can shed cells detectable in urine.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Bladder cancer and lung cancer are the paradigm smoking-caused epithelial cancers: tobacco carcinogens excreted in urine bathe and transform the bladder urothelium just as inhaled smoke transforms the bronchus, so the two often coexist and both are reshaped by immunotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Bladder cancer pioneered macrophage-based immunotherapy: intravesical BCG provokes a local immune response in which macrophages and T cells attack residual tumor, making early non-muscle-invasive bladder cancer one of the first cancers cured by harnessing innate immunity.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bellmunt-2017-keynote045]: Bellmunt J, de Wit R, Vaughn DJ, et al. Pembrolizumab as second-line therapy for advanced urothelial carcinoma. *N Engl J Med.* 2017;376(11):1015-1026. [doi:10.1056/NEJMoa1613683](https://doi.org/10.1056/NEJMoa1613683) · [PubMed 28212060](https://pubmed.ncbi.nlm.nih.gov/28212060/)
[^powles-2024-ev302]: Powles T, Valderrama BP, Gupta S, et al. Enfortumab vedotin and pembrolizumab in untreated advanced urothelial cancer. *N Engl J Med.* 2024;390(10):875-888. [doi:10.1056/NEJMoa2312117](https://doi.org/10.1056/NEJMoa2312117) · [PubMed 38261487](https://pubmed.ncbi.nlm.nih.gov/38261487/)
[^loriot-2019-erdafitinib]: Loriot Y, Necchi A, Park SH, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. *N Engl J Med.* 2019;381(4):338-348. [doi:10.1056/NEJMoa1817323](https://doi.org/10.1056/NEJMoa1817323) · [PubMed 31340094](https://pubmed.ncbi.nlm.nih.gov/31340094/)
