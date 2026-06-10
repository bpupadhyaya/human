---
schema: human-scale-entry/v1
id: inflammatory-bowel-disease
name: Inflammatory Bowel Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic intestinal inflammation: Crohn's disease (transmural, any GI) and ulcerative colitis (mucosal, colon only). TNF-alpha, IL-12/23, and JAK-STAT drive inflammation. Anti-TNF (infliximab), anti-IL-23 (risankizumab), and anti-integrin (vedolizumab) are mainstay biologics."
aliases: ["IBD", "Crohn's disease", "ulcerative colitis", "UC", "CD", "inflammatory bowel disease"]
sources:
  - id: ng-2017-ibd-epidemiology
    type: peer-reviewed
    cite: "Ng SC, Shi HY, Hamidi N, et al. Worldwide incidence and prevalence of inflammatory bowel disease in the 21st century: a systematic review of population-based studies. Lancet. 2018;390(10114):2769-2778."
    doi: "10.1016/S0140-6736(17)32448-0"
    pmid: "29050646"
    url: "https://doi.org/10.1016/S0140-6736(17)32448-0"
  - id: sandborn-2012-vedolizumab
    type: peer-reviewed
    cite: "Feagan BG, Rutgeerts P, Sands BE, et al. Vedolizumab as induction and maintenance therapy for ulcerative colitis. N Engl J Med. 2013;369(8):699-710."
    doi: "10.1056/NEJMoa1215734"
    pmid: "23964932"
    url: "https://doi.org/10.1056/NEJMoa1215734"
  - id: sands-2019-ustekinumab-uc
    type: peer-reviewed
    cite: "Sands BE, Sandborn WJ, Panaccione R, et al. Ustekinumab as Induction and Maintenance Therapy for Ulcerative Colitis. N Engl J Med. 2019;381(13):1201-1214."
    doi: "10.1056/NEJMoa1900750"
    pmid: "31553834"
    url: "https://doi.org/10.1056/NEJMoa1915765"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha is the primary IBD effector cytokine; macrophage TNF drives NF-kB-mediated epithelial apoptosis and barrier disruption; infliximab, adalimumab, certolizumab, and golimumab provide remission in moderate-severe CD and UC refractory to corticosteroids."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "IBD is defined by dysregulated immune response to commensal bacteria; dysbiosis (reduced Bacteroidetes, Faecalibacterium prausnitzii; increased Proteobacteria) is universal; gut microbiome composition predicts treatment response; FMT induces remission in UC in ~30-50% in trials."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "TNF-alpha and IL-13 in IBD disrupt intestinal epithelial tight junctions → increased permeability → bacterial translocation → amplified immune response; mucosal healing (endoscopic) is now the primary therapeutic target — correlates with reduced hospitalization and surgery."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are dominant IBD innate effectors; colonic macrophages normally tolerogenic (CD33+, anti-inflammatory) become pro-inflammatory (TNF-alpha, IL-1beta, IL-23) in IBD under dysbiosis; macrophage polarization is the target of JAK inhibitors and IL-12/23 blockade."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "H4R on mucosal mast cells and Tregs modulates gut inflammation; enterochromaffin-like cells secrete histamine → parietal HCl; H1R/H4R amplify epithelial cytokine release; H4R blockade reduces experimental colitis; histamine levels correlate with IBD disease activity."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 is the primary mucosal immunoregulatory cytokine; IL-10R mutations cause VEO-IBD (infantile perianal fistulizing Crohn's) curable by HSCT; IL-10 KO mice develop spontaneous microbiota-driven colitis; anti-TNF and JAK inhibitors partially restore IL-10 signaling in IBD."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: treated-by
    note: "Adalimumab achieves 52-week remission in 36% of Crohn's (CHARM trial) and 16.5% in UC (ULTRA-2); blocks mucosal macrophage TNFα → reduces NF-κB-driven epithelial apoptosis; both induction and maintenance approved; perianal fistula closure benefit confirmed."
---

# Inflammatory Bowel Disease

## Overview

**Inflammatory bowel disease (IBD)** encompasses two major chronic, relapsing-remitting intestinal inflammatory conditions — **Crohn's disease (CD)** and **ulcerative colitis (UC)** — characterized by dysregulated mucosal immunity against the intestinal microbiome in genetically susceptible individuals. IBD affects approximately **6.8 million people worldwide** (prevalence highest in North America and Europe, rapidly increasing in Asia, Africa, and South America) [^ng-2017-ibd-epidemiology].

IBD is distinct from infectious colitis, ischemic colitis, and irritable bowel syndrome (IBS, functional — no inflammation). The chronic nature, unpredictable relapse, colorectal cancer risk, and systemic manifestations make IBD a major cause of disability in young adults.

**Crohn's disease vs. ulcerative colitis:**

| Feature | Crohn's Disease (CD) | Ulcerative Colitis (UC) |
|:---|:---|:---|
| Location | Any GI segment (mouth to anus); ileum + right colon most common | Colon only; rectum always involved; continuous proximal extension |
| Depth | Transmural inflammation | Mucosal/submucosal only |
| Distribution | Skip lesions (patchy) | Continuous |
| Complications | Fistulae, abscesses, strictures, bowel obstruction | Toxic megacolon, massive hemorrhage |
| Cancer risk | Slightly elevated (small bowel CD) | Increased with extent and duration (surveillance colonoscopy) |
| Surgery | Resection (not curative — recurrence at anastomosis) | Colectomy is curative |
| Serology | ASCA+ (Saccharomyces cerevisiae antibodies) ~50% | pANCA+ ~65% |

**Classification (UC extent — Montreal Classification):**
- E1 (proctitis): Disease limited to rectum; managed with topical 5-ASA
- E2 (left-sided): Extends to splenic flexure; systemic therapy often needed
- E3 (extensive/pancolitis): Proximal to splenic flexure; highest cancer and complication risk

**CD classification (Montreal — location, behavior, perianal):**
- L1 (ileal), L2 (colonic), L3 (ileocolonic), L4 (upper GI)
- B1 (non-stricturing, non-penetrating), B2 (stricturing), B3 (penetrating/fistulizing)
- Perianal disease: p (+perianal) modifier

## Structure

### Genetic architecture of IBD

IBD is a complex polygenic disease with >240 susceptibility loci (GWAS):
- **NOD2 (CARD15):** First IBD gene (Hugot and Ogura 2001); variants (Arg702Trp, Gly908Arg, Leu1007fsX; 3 major; allele frequency 8-15% Caucasian) → impaired bacterial peptidoglycan sensing → defective mucosal immunity → ileal Crohn's; homozygous NOD2 variants → 40× increased CD risk
- **ATG16L1 T300A:** Autophagy pathway → impaired bacterial clearance and Paneth cell function → CD susceptibility
- **IL23R R381Q:** Protective loss-of-function variant; IL-23R signaling required for Th17 differentiation → IL-23 pathway variants among strongest IBD loci; basis for ustekinumab (anti-IL-12/23) and mirikizumab (anti-IL-23p19) therapy
- **HLA region:** Complex IBD associations; HLA-DRB1*01:03 strongly associated with extensive UC
- **CARD9, JAK2, STAT3:** Multiple inflammatory pathway variants in IBD GWAS

### Mucosal immune dysregulation

**Normal gut immunity:** Lamina propria macrophages (tolerogenic CD33+, IL-10-producing) and Tregs maintain homeostasis to commensal bacteria; IgA secretion (plasma cells → secretory IgA → bacterial coating → immune exclusion); epithelial barrier (tight junctions: claudins, occludin, ZO-1) + mucus layer → physical separation

**IBD pathogenesis:**
1. **Epithelial barrier disruption:** Genetic (NOD2, ATG16L1) or environmental (antibiotics, NSAIDs, Western diet → reduced Bacteroidetes) → altered microbiome → intestinal permeability → bacterial/LPS translocation into lamina propria
2. **Innate immune activation:** Pattern recognition receptors (TLR4, NOD2) on macrophages and dendritic cells → NF-kB → TNF-alpha, IL-1beta, IL-6, IL-12, IL-23
3. **Adaptive immune dysregulation:**
   - **Crohn's:** Th1 (IFN-gamma, IL-2) and Th17 (IL-17A/F, IL-22) dominant; driven by IL-12 (Th1) and IL-23 (Th17/Th1) from DCs
   - **UC:** Th2 (IL-5, IL-13) pattern in some patients; atypical Th2 (non-classical NKT cells → IL-13); IL-13 → epithelial apoptosis and barrier dysfunction; eosinophilic infiltration
4. **Treg deficiency:** Reduced FoxP3+ Tregs in IBD mucosa → insufficient immunosuppression; impaired IL-10 signaling (IL-10 knockout → colitis in mice; IL-10R mutations → neonatal IBD)
5. **Microbiome dysbiosis:** Reduced diversity, reduced short-chain fatty acid (SCFA) producers (Faecalibacterium prausnitzii, Roseburia), increased mucosa-adherent bacteria (adherent-invasive E. coli, AIEC) → epithelial invasion and inflammatory amplification

## Function

### Clinical presentation

**Ulcerative colitis symptoms:**
- **Bloody diarrhea** (cardinal symptom): Mucopurulent bloody stool, ≥6 stools/day in severe disease
- Urgency, tenesmus (rectal inflammation), nocturnal diarrhea
- Cramps, lower abdominal pain
- **Acute severe UC (Truelove-Witts criteria):** ≥6 bloody stools/day + at least one systemic feature (HR >90, fever >37.8°C, Hb <10.5 g/dL, ESR >30) → inpatient IV corticosteroids; if no response in 72h → infliximab or colectomy

**Crohn's disease symptoms:**
- Right lower quadrant pain (ileitis → terminal ileum), diarrhea (often non-bloody), weight loss
- **Strictures:** Colicky obstructive pain (post-prandial), early satiety
- **Fistulae:** Entero-enteric (asymptomatic), entero-vesicular (pneumaturia, fecaluria), entero-vaginal (fecal vaginal discharge), perianal (complex anal fistulae with abscesses → significant morbidity)
- **Abscesses:** Psoas abscess, intra-abdominal → fever, mass; drain + antibiotics

**Extra-intestinal manifestations (EIMs, 25-40% of IBD):**
- **Joints:** Peripheral arthritis (pauciarticular — correlates with gut disease activity; polyarticular — independent); axial arthropathy (sacroiliitis, IBD-associated AS — independent of gut activity)
- **Skin:** Erythema nodosum (correlates with activity), pyoderma gangrenosum (independent, treat with biologics)
- **Eyes:** Episcleritis (activity-correlated), uveitis (independent — requires ophthalmology)
- **Liver/biliary:** Primary sclerosing cholangitis (PSC) — almost exclusively UC (~5%); increased cholangiocarcinoma risk; no effective medical therapy; liver transplant if end-stage; increased colorectal cancer risk in PSC-UC (annual surveillance colonoscopy regardless of UC extent)

### Biomarkers

- **Fecal calprotectin:** Neutrophil cytosolic protein; correlates with endoscopic inflammation; ≥150 μg/g = active mucosal disease; used to monitor therapy response and guide endoscopy scheduling
- **CRP:** Non-specific but elevated in CD (especially ileal disease); may be normal in UC with mild activity
- **Serology:** ASCA (Crohn's) and pANCA (UC) — distinguish CD from UC in indeterminate colitis (~70% sensitivity, >90% specificity)
- **Endoscopy:** Gold standard; direct visualization + biopsy; mucosal healing (Mayo score 0-1 in UC, SES-CD in CD) is the therapeutic target

## Pathology

### Treatment [^sandborn-2012-vedolizumab] [^sands-2019-ustekinumab-uc]

**Step-up vs. early aggressive (top-down) strategy:**
- **Step-up (conventional):** 5-ASA → corticosteroids → thiopurines → anti-TNF → combination
- **Top-down (early biologic):** Anti-TNF ± thiopurine from diagnosis in high-risk patients (deep ulcers, fistulizing, steroid-dependent, high CRP, extensive disease) → superior mucosal healing and steroid-free remission (SONIC trial: infliximab + azathioprine superior to monotherapy in CD)

**Aminosalicylates (5-ASA):**
- Mesalamine (UC first-line, mild-moderate): Mucosal anti-inflammatory (NF-kB inhibition, prostaglandin modulation); oral + rectal formulations for UC; proctitis treated with suppository only; NOT effective in CD (Cochrane review: no benefit over placebo)
- Sulfasalazine: 5-ASA prodrug; folate supplementation required

**Corticosteroids:**
- Prednisone/methylprednisolone: Rapid induction (40-60 mg/day PO or IV) for moderate-severe flares; NOT maintenance therapy (bone loss, HPA suppression, complications)
- **Budesonide (oral controlled-ileal release, Entocort):** Ileal/right colonic CD induction; 90% first-pass hepatic metabolism → limited systemic effects; 9 mg daily; gentler than prednisone but not for severe disease

**Immunomodulators:**
- **Azathioprine/6-mercaptopurine (6-MP):** Purine antimetabolite → lymphocyte antiproliferation; TPMT/NUDT15 genotyping before initiation (rapid metabolizers → myelosuppression); used as maintenance alone or in combination with anti-TNF (reduces antibody formation to biologic); 3-6 months to full effect
- **Methotrexate (IM/SC, Crohn's only):** Anti-inflammatory + immunomodulatory; second-line immunomodulator if azathioprine intolerant; not used in UC (less evidence)

**Anti-TNF biologics (first-line biologic for moderate-severe IBD):**
- **Infliximab (Remicade, chimeric anti-TNF):** IV infusion; highly effective in CD and UC; mucosal healing ~40% in CD; first biologic approved for fistulizing CD; SONIC trial: infliximab + azathioprine → 57% clinical remission in CD vs. 30% azathioprine alone; scheduled maintenance superior to episodic
- **Adalimumab (Humira, human anti-TNF):** SC biweekly; CLASSIC-I/II in CD; ULTRA in UC; preferred for patients with injection-site preference or infusion reaction to infliximab
- **Certolizumab pegol (Cimzia, PEGylated anti-TNF Fab):** SC; CD (not UC); no Fc → no complement, minimal placental transfer → safe in pregnancy
- **Golimumab (Simponi):** SC monthly; UC only (PURSUIT trial)
- **Anti-TNF monitoring:** Therapeutic drug monitoring (TDM) — trough levels (infliximab ≥5 μg/mL, adalimumab ≥7.5 μg/mL); anti-drug antibodies (ADA) → loss of response; dose optimization or switch based on TDM

**Anti-integrin biologics (gut-selective):**
- **Vedolizumab (Entyvio, anti-alpha-4-beta-7 integrin):** Prevents lymphocyte trafficking to the gut (MAdCAM-1 binding on gut endothelium); approved UC and CD; GEMINI I (UC) and II (CD); gut-selective → fewer systemic infections than anti-TNF; PML not reported (vs. natalizumab, which blocks alpha-4 globally) [^sandborn-2012-vedolizumab]; preferred in elderly, immunocompromised, or post-transplant IBD
- **Ozanimod (sphingosine-1-phosphate modulator):** Retains lymphocytes in lymph nodes → prevents gut trafficking; oral; approved UC; mild side effects (bradycardia at initiation, ophthalmic assessment)

**Anti-IL-12/23 and anti-IL-23:**
- **Ustekinumab (Stelara, anti-IL-12/23 p40 subunit):** IV induction, SC maintenance; approved CD (UNIFI Phase III) and UC (STELARA-UC) [^sands-2019-ustekinumab-uc]; excellent safety; preferred in patients with psoriasis comorbidity (dual indication); ORR ~60% induction
- **Risankizumab (Skyrizi, anti-IL-23 p19):** Selective IL-23 blockade (spares IL-12 → preserves IFN-gamma-mediated immunity); approved CD 2022 and UC 2024; ADVANCE/MOTIVATE (CD), INSPIRE (UC): superior remission rates vs. placebo; also approved for psoriasis and PsA
- **Mirikizumab (Omvoh, anti-IL-23 p19):** Approved UC 2023 (LUCENT-1/2); Crohn's filed

**JAK inhibitors (IBD):**
- **Tofacitinib (Xeljanz, JAK1/3):** Approved UC (OCTAVE I/II); 18.5% remission vs. 8.2% placebo at week 8; effective in anti-TNF-refractory UC; VTE boxed warning limits use in older/high-CV-risk patients
- **Upadacitinib (Rinvoq, JAK1):** Approved UC (2022) and CD (2023); ULTA II (CD): 45.5% remission vs 13.1% placebo at week 12; SELECT UC I/II; superior to adalimumab in UC head-to-head; JAK1 selectivity reduces anemia/cytopenias vs. tofacitinib
- **Filgotinib (Jyseleca, JAK1, EU only):** Approved UC in EU; SELECTION trial

**Surgery:**
- **UC:** Proctocolectomy (total colectomy + rectal excision); curative; options: permanent end ileostomy or J-pouch ileal-anal anastomosis (IPAA, restorative — preferred when feasible); pouchitis (antibiotic/probiotic/biologic)
- **CD:** Resection for obstruction, perforation, fistula, or medically refractory disease; does NOT cure — disease recurs at anastomosis (~50% endoscopic recurrence at 1 year post-resection); post-operative prophylaxis with anti-TNF or immunomodulator recommended

## Connections

- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha is the primary effector cytokine in IBD; mucosal macrophages produce TNF → NF-kB-mediated epithelial apoptosis and barrier disruption; anti-TNF biologics (infliximab, adalimumab) are the backbone of moderate-severe IBD therapy and achieve mucosal healing in ~40% of CD and UC.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — IBD is fundamentally a dysregulated immune response to commensal bacteria in susceptible hosts; dysbiosis (loss of Faecalibacterium prausnitzii and Bacteroidetes) is universal; gut microbiome composition predicts treatment response; FMT induces UC remission in ~30-50% of patients in clinical trials.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — TNF-alpha and IL-13 in IBD disrupt tight junction proteins → increased permeability → bacterial translocation; mucosal healing (endoscopic Mayo 0-1 in UC) is now the primary therapeutic target — associated with sustained remission and reduced surgical risk.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — colonic macrophages shift from tolerogenic (CD33+, IL-10-producing) to pro-inflammatory (TNF-alpha, IL-1beta, IL-23) in IBD; macrophage IL-23 production drives Th17 differentiation; anti-IL-12/23 (ustekinumab, risankizumab) and JAK inhibitors target macrophage-driven intestinal inflammation.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — H4R on mucosal mast cells and Tregs modulates gut inflammation; enterochromaffin-like cells secrete histamine → parietal HCl; H1R/H4R amplify epithelial cytokine release; H4R blockade reduces experimental colitis; histamine levels correlate with IBD disease activity.
- `treated-by` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — approved for Crohn's disease (CHARM trial: 36% vs 12% 52-week remission) and ulcerative colitis (ULTRA-2: 16.5% vs 9.3%); blocks mucosal macrophage TNFα → reduces epithelial apoptosis; perianal fistula closure benefit; induction and maintenance approved.

[^ng-2017-ibd-epidemiology]: Ng SC, Shi HY, Hamidi N, et al. Worldwide incidence and prevalence of inflammatory bowel disease in the 21st century: a systematic review of population-based studies. *Lancet.* 2018;390(10114):2769-2778. [doi:10.1016/S0140-6736(17)32448-0](https://doi.org/10.1016/S0140-6736(17)32448-0) · [PubMed 29050646](https://pubmed.ncbi.nlm.nih.gov/29050646/)
[^sandborn-2012-vedolizumab]: Feagan BG, Rutgeerts P, Sands BE, et al. Vedolizumab as induction and maintenance therapy for ulcerative colitis. *N Engl J Med.* 2013;369(8):699-710. [doi:10.1056/NEJMoa1215734](https://doi.org/10.1056/NEJMoa1215734) · [PubMed 23964932](https://pubmed.ncbi.nlm.nih.gov/23964932/)
[^sands-2019-ustekinumab-uc]: Sands BE, Sandborn WJ, Panaccione R, et al. Ustekinumab as Induction and Maintenance Therapy for Ulcerative Colitis. *N Engl J Med.* 2019;381(13):1201-1214. [doi:10.1056/NEJMoa1900750](https://doi.org/10.1056/NEJMoa1900750) · [PubMed 31553834](https://pubmed.ncbi.nlm.nih.gov/31553834/)
