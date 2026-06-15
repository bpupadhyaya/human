---
schema: human-scale-entry/v1
id: iga-nephropathy
name: IgA Nephropathy
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "IgA nephropathy is the most common primary glomerulonephritis globally; galactose-deficient IgA1 (Gd-IgA1) → mesangial immune complex deposition → complement + CCL2 → macrophage infiltration → fibrosis; sparsentan, iptacopan, and budesonide (Tarpeyo) are recently approved."
aliases: ["IgAN", "Berger disease", "IgA glomerulonephritis", "mesangial IgA nephropathy", "IgA vasculitis nephritis", "HSP nephritis"]
sources:
  - id: barratt-2017-igan-review
    type: peer-reviewed
    cite: "Barratt J, Feehally J. IgA nephropathy. J Am Soc Nephrol. 2005;16(7):2088-2097."
    doi: "10.1681/ASN.2005020134"
    pmid: "15987751"
    url: "https://doi.org/10.1681/ASN.2005020134"
  - id: heerspink-2023-sparsentan-protect
    type: peer-reviewed
    cite: "Heerspink HJL, Radhakrishnan J, Alpers CE, et al. Sparsentan in patients with IgA nephropathy: a prespecified interim analysis from a randomised, double-blind, active-controlled clinical trial. Lancet. 2023;401(10388):1584-1594."
    doi: "10.1016/S0140-6736(23)00569-X"
    pmid: "37062299"
    url: "https://doi.org/10.1016/S0140-6736(23)00569-X"
cross_links:
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Mesangial IgA immune complex deposition → complement + cytokine activation → CCL2 from mesangial cells + tubular epithelial cells → CCR2+ monocyte/macrophage infiltration → tubulointerstitial inflammation → fibrosis → CKD progression; urine CCL2 tracks IgAN disease activity."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "IgA nephropathy is a leading cause of CKD and ESRD in young adults; proteinuria >1 g/day + HTN + GFR decline = high-risk for CKD progression; 20-40% reach ESRD within 20 years; SGLT2 inhibitors (dapagliflozin) and RAS blockade slow IgAN-associated CKD progression."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Mesangial IgA immune complexes → lectin pathway C4 deposition → C3 → alternative pathway amplification → MAC; iptacopan (factor B inhibitor, APPLAUSE-IgAN 2024) reduces proteinuria 44% vs. 9% placebo; complement activation in IgA nephropathy is a validated therapeutic target."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Aberrant O-glycosylation of IgA1 hinge region → galactose-deficient IgA1 (Gd-IgA1) → anti-Gd-IgA1 IgG autoantibodies → immune complexes → mesangial deposition → complement activation → IgAN; Gd-IgA1 from mucosal plasma cells is the primary disease-causing immunoglobulin in IgAN."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Lectin + alternative pathway → C3b deposition in mesangium is the IgAN complement hallmark; C3 IF on biopsy is pathognomonic; iptacopan (factor B inhibitor) targets upstream of C3 → prevents C3b + MAC; C3 deposit intensity correlates with IgAN disease activity."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Mesangial IgA IC deposition → TGF-β1 in mesangial cells → collagen IV + fibronectin → progressive glomerulosclerosis and tubulointerstitial fibrosis; urinary TGF-β1 correlates with Oxford T score; TGF-β mediates the inflammation-to-fibrosis transition in IgAN-CKD."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "APRIL and BAFF drive IgA1 class switching in mucosal plasma cells and sustain Gd-IgA1 production; atacicept (APRIL+BAFF dual inhibitor, ORIGIN trial): 58% vs 0% proteinuria reduction; zigakimab (anti-APRIL, SPARK trial) in Phase 2/3; APRIL overexpressed in Peyer patches in IgAN."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "IgA nephropathy and immune thrombocytopenia are both antibody-driven autoimmune diseases: IgAN from galactose-deficient IgA1 complexes in the kidney mesangium, ITP from anti-platelet IgG marking platelets for splenic destruction — both treated by depleting the driving B cells."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "IgA nephropathy is the most common primary glomerulonephritis worldwide and a top cause of kidney failure in young adults: galactose-deficient IgA1 complexes lodge in the glomerular mesangium, triggering complement and inflammation that scar the kidney, often after a sore throat."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "IgA nephropathy's disease-causing molecule comes from plasma cells: mucosal plasma cells (Peyer patches) overproduce galactose-deficient IgA1 under APRIL/BAFF drive, and others make the anti-Gd-IgA1 autoantibody — so therapies increasingly target plasma cells and APRIL signaling."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "IgA nephropathy is fundamentally a glomerular disease: galactose-deficient IgA1 immune complexes deposit in the glomerular mesangium, activating complement and mesangial proliferation that cause hematuria and proteinuria; diagnosis rests on mesangial IgA on glomerular biopsy."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "IgA nephropathy is linked to gut mucosal immunity and IBD: it reflects aberrant mucosal IgA1 production, is over-represented in inflammatory bowel and celiac disease, and gut-targeted budesonide (Nefecon) reduces proteinuria—evidence the gut-kidney axis drives it."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "IgA nephropathy is the world's commonest primary glomerulonephritis and a major cause of kidney failure: despite an often indolent course of hematuria, up to 30-40% progress to end-stage renal disease over decades, making it a leading reason younger adults need renal replacement."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "IgA nephropathy and lupus nephritis are both immune-complex glomerulonephritides: IgAN deposits galactose-deficient IgA1 in the mesangium, while lupus nephritis deposits nuclear complexes—immunofluorescence (IgA versus 'full house') tells them apart."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "IgA nephropathy ultimately injures podocytes: mesangial IgA1 deposits and complement drive cytokines that damage the glomerular filter, so podocyte loss and proteinuria mark progression to chronic kidney disease—podocyte injury predicts a worse course."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "IgA nephropathy and ANCA vasculitis can both cause crescentic glomerulonephritis: severe IgAN with crescents mimics ANCA-associated GN, so a crescentic biopsy needs immunofluorescence and ANCA testing to tell IgA deposition from pauci-immune disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Aberrant B cells drive IgA nephropathy: mucosal B cells overproduce galactose-deficient IgA1 that forms immune complexes depositing in the glomerular mesangium, so B-cell-targeted and APRIL/BAFF-blocking therapies are emerging treatments."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome helps trigger IgA nephropathy: mucosal immune responses to gut flora drive production of the abnormal IgA1 that injures the kidney, so the gut-kidney axis explains flares after infections and the interest in microbiome-directed therapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver disease causes secondary IgA nephropathy: cirrhosis impairs hepatic clearance of IgA, so IgA immune complexes accumulate and deposit in the kidney—hepatic IgA nephropathy showing how the liver normally protects the glomerulus from IgA overload."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "IgA nephropathy is an immune-complex kidney disease: the immune system makes galactose-deficient IgA1 and antibodies against it, forming complexes that lodge in the glomerular mesangium and activate complement—a misdirected mucosal immune response striking the kidney."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "IgA nephropathy classically flares with infection: gross hematuria appears within a day or two of a sore throat (synpharyngitic), unlike post-streptococcal glomerulonephritis weeks later—reflecting how mucosal infection ramps up the pathogenic IgA response."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "IgA nephropathy drives hypertension and is worsened by it: glomerular injury and proteinuria raise blood pressure, which in turn accelerates renal scarring, so strict blood-pressure and proteinuria control with RAS blockade is the cornerstone of slowing progression."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "IgA nephropathy begins with dysregulated T-helper cells at mucosal sites: Th2 and Th17 skewing drives B cells to overproduce galactose-deficient IgA1, the autoantigen whose immune complexes deposit in the glomerulus—linking mucosal T-cell help to kidney injury."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Outcome in IgA nephropathy is written in fibrosis: tubulointerstitial fibrosis and tubular atrophy (the 'T' of the MEST-C score) predict progression to kidney failure better than the glomerular lesions, so preserving nephrons is the long-term goal."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Glomerular endothelium marks active IgA nephropathy: endocapillary hypercellularity (the 'E' score) reflects inflammation of capillary endothelial cells and signals a lesion that may respond to immunosuppression—shaping who gets steroids."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "IgA nephropathy is first treated by blocking angiotensin II: ACE inhibitors and ARBs lower the glomerular pressure that angiotensin II drives, cutting the proteinuria that predicts kidney decline—the cornerstone of slowing this disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "IgA nephropathy classically leaks red cells: immune-complex injury to the glomerulus lets erythrocytes spill into the urine, often as visible hematuria a day or two after a sore throat (synpharyngitic), a hallmark that points to the diagnosis."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "SGLT2 inhibitors now help protect kidneys in IgA nephropathy: blocking this glucose transporter lowers glomerular pressure and proteinuria independent of blood sugar, adding to RAAS blockade as a pillar of slowing progression to kidney failure."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "IgA nephropathy starts in the gut, not the kidney: the abnormal galactose-deficient IgA1 that lands in the glomerulus is made by the small intestine's mucosal immune system, so the gut-kidney axis is central—and a target of gut-release budesonide."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive the kidney damage in IgA nephropathy: drawn into the glomerulus by IgA-immune-complex deposits, they release cytokines and enzymes that inflame and scar the filter, helping turn deposition into progressive kidney injury."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Salt handling shapes IgA nephropathy's course: as the disease scars the kidney, sodium retention worsens hypertension and proteinuria, so dietary salt restriction supports the RAAS-blocking drugs that slow its progression."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "IgA nephropathy has a skin-and-systemic cousin: IgA vasculitis (Henoch-Schönlein purpura) deposits the same IgA complexes in the skin's small vessels, causing the palpable purpura that often accompanies the kidney disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "IgA nephropathy bleeds into the urine: episodes of visible hematuria, classically after a sore throat, plus the anemia of progressing kidney disease, can drain the body's iron over time."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Severe IgA nephropathy recruits neutrophils: in crescentic, rapidly progressive disease they flood the inflamed glomerulus, helping build the cellular crescents that signal aggressive kidney injury."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "IgA nephropathy is diagnosed on the biopsy: immunofluorescence under the microscope lights up the IgA deposits in the glomerular mesangium, the finding that defines the disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Treating IgA nephropathy risks high potassium: the ACE inhibitors and ARBs that protect the kidney by blocking angiotensin also raise potassium, which must be monitored."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "IgA nephropathy may start in the gut: mucosal immunity in the intestinal epithelium produces the galactose-deficient IgA1 that ends up clogging the kidney, the gut-kidney axis behind the disease."
---

# IgA Nephropathy

## Overview

**IgA nephropathy (IgAN)**, also called **Berger disease**, is the **most common primary glomerulonephritis worldwide**, accounting for approximately 25-30% of all primary glomerulonephritis diagnoses. It is defined by the **predominant mesangial deposition of immunoglobulin A (IgA)** — specifically galactose-deficient IgA1 (Gd-IgA1) — accompanied by complement and other immunoglobulins, detected by immunofluorescence microscopy on kidney biopsy [^barratt-2017-igan-review].

IgAN is a **multi-hit disease** described by the Oxford Four-Hit Model:
1. **Hit 1:** Overproduction of **galactose-deficient IgA1 (Gd-IgA1)** in the bone marrow/mucosa (aberrant O-glycosylation of the IgA1 hinge-region → exposed N-acetylgalactosamine [GalNAc] residues); elevated serum Gd-IgA1 is the primary biomarker
2. **Hit 2:** Formation of **anti-Gd-IgA1 IgG autoantibodies** that recognize the aberrant GalNAc epitopes
3. **Hit 3:** **Immune complex (IC) formation** — Gd-IgA1 + anti-Gd-IgA1 IgG → large, poorly soluble ICs circulate in blood
4. **Hit 4:** **Mesangial IC deposition** → mesangial cell activation → complement (lectin pathway C4 → alternative amplification → C3b + MAC) + cytokine (IL-6, TNF-α, TGF-β) → CCL2-mediated macrophage recruitment → tubulointerstitial injury → fibrosis → CKD

**Epidemiology:**
- Most common primary glomerulonephritis globally; prevalence ~130 cases per million in Western countries; higher in East Asia (Japan, China, Korea: 30-40% of all biopsied glomerulonephritis)
- Peak onset 20-30 years; male predominance (2:1 in most series)
- **Prognosis:** 20-40% of patients develop ESRD within 20 years; predictors of progression: persistent proteinuria >1 g/day, hypertension, reduced eGFR at diagnosis, Oxford MEST-C score (Mesangial, Endocapillary, Segmental, Tubular atrophy/interstitial fibrosis, Crescents)
- **IgA vasculitis (Henoch-Schönlein purpura/IgAV):** Systemic form of IgA-mediated vasculitis; identical renal histology to IgAN; additionally involves skin (palpable purpura), joints, and GI tract; commoner in children

## Structure

**Gd-IgA1 and mesangial deposition:**
- IgA1 (not IgA2) has a 13-23 aa hinge region between Cα1 and Cα2 with multiple O-linked glycosylation sites (9 possible sites; typically 6-7 are glycosylated); normal O-glycans: GalNAc-Gal-Sialic acid core; in IgAN: deficient galactosylation (C1GALT1 transferase underactivity or aberrant Cosmc chaperone) → truncated GalNAc (asialo-Gd-IgA1) or GalNAc-SA (poorly galactosylated IgA1) exposed
- **Mesangium:** The mesangium contains specialized mesangial cells (contractile, phagocytic, produce ECM, cytokines) and the mesangial matrix; mesangial cells express IgA Fc receptors (FcαRI/CD89 soluble form, possibly transferrin receptor CD71 — TfR1 — which binds polymeric IgA1); IgA-IgA1 immune complex deposition in the mesangial matrix (not capillary loops — differentiated from membranous nephropathy and lupus nephritis by distribution)
- **Complement activation pattern:** IgAN: predominant lectin pathway (MBL/MASP binds Gd-IgA1 GalNAc → C4 deposition → C4b2a → C3 cleavage) + alternative pathway amplification → C3d deposition in mesangium; MAC formation → mesangial lysis + sublytic MAC → IL-1β production; C3, C4c, and sometimes IgM co-deposit

**Oxford MEST-C histological score:**
- **M (Mesangial hypercellularity):** M0 <50%, M1 ≥50% of glomeruli; associated with poor prognosis
- **E (Endocapillary hypercellularity):** E0 absent, E1 present; responsive to immunosuppression
- **S (Segmental glomerulosclerosis):** S0 absent, S1 present; chronic injury marker
- **T (Tubular atrophy/Interstitial fibrosis):** T0 <25%, T1 25-50%, T2 >50%; strongest predictor of renal outcome
- **C (Crescents):** C0 absent, C1 <25%, C2 ≥25%; therapeutic target for immunosuppression

## Function

**Clinical presentation:**
- **Macroscopic hematuria (gross hematuria):** 40-50% of patients; classically synpharyngitic (concurrent with upper respiratory infection within 24-48h, vs. postinfectious GN which occurs 1-3 weeks later); usually resolves but marks disease activity
- **Microscopic hematuria ± proteinuria:** 30-40% at diagnosis; detected on urinalysis; may be asymptomatic for years; discovered on screening or during investigation of other conditions
- **Nephrotic-range proteinuria (>3.5 g/day):** Minority; associated with focal glomerulosclerosis (FSGS) lesion on biopsy — poorer prognosis
- **Hypertension:** Common, especially with CKD progression; contributes to glomerular hyperfiltration and further injury
- **Rarely:** Rapidly progressive GN (RPGN) with crescents — acute deterioration in eGFR requiring emergency immunosuppression

**Diagnosis:**
- **Kidney biopsy:** Required for definitive diagnosis; immunofluorescence showing dominant or co-dominant IgA deposits in the mesangium (with or without IgG, IgM, C3, C1q); mesangial hypercellularity on light microscopy; electron microscopy shows electron-dense mesangial deposits
- **Serum Gd-IgA1 levels:** Elevated in ~70% of IgAN patients vs. ~10% of controls; not yet a validated clinical diagnostic test (variability between assay platforms); potential future biomarker
- **Urine biomarkers:** Spot UPCR (urine protein-to-creatinine ratio) — key monitoring parameter; urine CCL2, CXCL8, NGAL (neutrophil gelatinase-associated lipocalin) — research biomarkers correlating with disease activity

## Pathology

**Treatment:**

*Supportive care (all patients):*
- **RAS blockade:** ACEi or ARB (maximize to the maximum tolerated dose) → reduces intraglomerular pressure + anti-proteinuric effect; first-line for patients with proteinuria >0.5-1 g/day; dual ACEi + ARB increases hyperkalemia risk (generally avoided)
- **Blood pressure control:** Target <125/75 mmHg with significant proteinuria (AHA/ACC hypertension guidelines for CKD)
- **SGLT2 inhibitors:** Dapagliflozin (DAPA-CKD: 29% risk reduction in composite kidney endpoint in IgAN subgroup, N=270); canagliflozin (CREDENCE), empagliflozin (EMPA-KIDNEY) — broad CKD protection; now recommended in IgAN with eGFR ≥25 mL/min/1.73m²

*Targeted therapies (newer approvals):*

**Sparsentan (Filspari; dual ETA/AT1R antagonist; Travere) [^heerspink-2023-sparsentan-protect]:**
- First-in-class dual blocker: endothelin-1 ETA receptor + angiotensin II AT1R antagonism → additive anti-proteinuric effect beyond RAS blockade alone
- **PROTECT trial:** 404 patients with IgAN + proteinuria ≥1 g/day; sparsentan 400 mg QD vs. irbesartan 300 mg QD; primary endpoint (proteinuria change at 36 weeks): sparsentan –49.8% vs. irbesartan –15.1% (p<0.001); kidney histology improvement (MEST-C) at 110 weeks: preliminary positive signal
- FDA accelerated approval February 2023 for IgAN; FDA full approval expected based on confirmatory eGFR endpoint from PROTECT

**Iptacopan (Fabhalta; factor B inhibitor; Novartis):**
- FDA accelerated approval August 2024 for IgAN; oral QD; targets alternative pathway complement upstream of C3/C5 → prevents C3b opsonization + MAC formation in mesangium
- **APPLAUSE-IgAN:** Interim results: iptacopan → proteinuria reduction –44% vs. –9% placebo; eGFR slope improvement expected at 2-year primary endpoint

**Targeted-release budesonide (Tarpeyo/Nefecon; Calliditas):**
- Oral mucosal-targeted glucocorticoid; releases in the distal ileum/proximal colon → suppresses Peyer's patches IgA1 production (the overproduction site for Gd-IgA1); significantly less systemic steroid exposure vs. systemic prednisone
- **NefIgArd (Phase 3):** Budesonide 16 mg QD × 9 months; proteinuria reduction –34% vs. –6% placebo at 9 months; eGFR benefit at 2 years; FDA accelerated approval 2021; full approval 2023 based on 2-year eGFR endpoint

**Systemic immunosuppression (selective use):**
- Systemic corticosteroids (prednisone): 0.5-1 mg/kg/day taper × 6 months; STOP-IgAN and TESTING trials show limited benefit and significant adverse effects (infection, metabolic) in unselected patients; currently reserved for E1 (endocapillary proliferation) or crescentic IgAN with rapidly declining eGFR
- **SGLT2i preference over steroids** for most patients with eGFR 25-70 mL/min and proteinuria <3.5 g/day

**Experimental:**
- **Atacicept (APRIL/BAFF dual inhibitor):** ORIGIN Phase 2 trial: 58% vs. 0% reduction in proteinuria; APRIL drives IgA class switching and B cell survival — promising mechanism; Phase 3 underway
- **Zigakimab (anti-APRIL):** Phase 2/3 SPARK trial

## Connections

- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Mesangial IgA immune complex deposition → complement + cytokine activation → CCL2 from mesangial cells + tubular epithelial cells → CCR2+ monocyte/macrophage infiltration → tubulointerstitial inflammation → fibrosis → CKD progression; urine CCL2 tracks IgAN disease activity.
- `connects-to` → **[CKD](../ckd/README.md)** — IgA nephropathy is a leading cause of CKD and ESRD in young adults; proteinuria >1 g/day + HTN + GFR decline = high-risk for CKD progression; 20-40% reach ESRD within 20 years; SGLT2 inhibitors (dapagliflozin) and RAS blockade slow IgAN-associated CKD progression.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Mesangial IgA immune complexes → lectin pathway C4 deposition → C3 → alternative pathway amplification → MAC; iptacopan (factor B inhibitor, APPLAUSE-IgAN 2024) reduces proteinuria 44% vs. 9% placebo; complement activation in IgA nephropathy is a validated therapeutic target.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Aberrant O-glycosylation of IgA1 hinge region → galactose-deficient IgA1 (Gd-IgA1) → anti-Gd-IgA1 IgG autoantibodies → immune complexes → mesangial deposition → complement activation → IgAN; Gd-IgA1 from mucosal plasma cells is the primary disease-causing immunoglobulin in IgAN.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — lectin + alternative pathway → C3b deposition in mesangium is the IgAN complement hallmark; C3 IF on biopsy is pathognomonic; iptacopan (factor B inhibitor) targets upstream of C3 → prevents C3b + MAC; C3 deposit intensity correlates with IgAN disease activity.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — mesangial IgA IC deposition → TGF-β1 in mesangial cells → collagen IV + fibronectin → progressive glomerulosclerosis and tubulointerstitial fibrosis; urinary TGF-β1 correlates with Oxford T score; TGF-β mediates the inflammation-to-fibrosis transition in IgAN-CKD.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — APRIL and BAFF drive IgA1 class switching in mucosal plasma cells and sustain Gd-IgA1 production; atacicept (APRIL+BAFF dual inhibitor, ORIGIN trial): 58% vs 0% proteinuria reduction; zigakimab (anti-APRIL, SPARK trial) in Phase 2/3; APRIL overexpressed in Peyer patches in IgAN.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — IgA nephropathy and immune thrombocytopenia are both antibody-driven autoimmune diseases: IgAN from galactose-deficient IgA1 complexes in the kidney mesangium, ITP from anti-platelet IgG marking platelets for splenic destruction — both treated by depleting the driving B cells.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — IgA nephropathy is the most common primary glomerulonephritis worldwide and a top cause of kidney failure in young adults: galactose-deficient IgA1 complexes lodge in the glomerular mesangium, triggering complement and inflammation that scar the kidney, often after a sore throat.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — IgA nephropathy's disease-causing molecule comes from plasma cells: mucosal plasma cells (Peyer patches) overproduce galactose-deficient IgA1 under APRIL/BAFF drive, and others make the anti-Gd-IgA1 autoantibody — so therapies increasingly target plasma cells and APRIL signaling.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — IgA nephropathy and immune thrombocytopenia are both antibody-driven autoimmune diseases: IgAN from galactose-deficient IgA1 complexes in the kidney mesangium, ITP from anti-platelet IgG marking platelets for splenic destruction — both treated by depleting the driving B cells.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — IgA nephropathy is the most common primary glomerulonephritis worldwide and a top cause of kidney failure in young adults: galactose-deficient IgA1 complexes lodge in the glomerular mesangium, triggering complement and inflammation that scar the kidney, often after a sore throat.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — IgA nephropathy's disease-causing molecule comes from plasma cells: mucosal plasma cells (Peyer patches) overproduce galactose-deficient IgA1 under APRIL/BAFF drive, and others make the anti-Gd-IgA1 autoantibody — so therapies increasingly target plasma cells and APRIL signaling.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — IgA nephropathy is fundamentally a glomerular disease: galactose-deficient IgA1 immune complexes deposit in the glomerular mesangium, activating complement and mesangial proliferation that cause hematuria and proteinuria; diagnosis rests on mesangial IgA on glomerular biopsy.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — IgA nephropathy is linked to gut mucosal immunity and IBD: it reflects aberrant mucosal IgA1 production, is over-represented in inflammatory bowel and celiac disease, and gut-targeted budesonide (Nefecon) reduces proteinuria—evidence the gut-kidney axis drives it.
- `connects-to` → **[Renal System](../renal-system/README.md)** — IgA nephropathy is the world's commonest primary glomerulonephritis and a major cause of kidney failure: despite an often indolent course of hematuria, up to 30-40% progress to end-stage renal disease over decades, making it a leading reason younger adults need renal replacement.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — IgA nephropathy and lupus nephritis are both immune-complex glomerulonephritides: IgAN deposits galactose-deficient IgA1 in the mesangium, while lupus nephritis deposits nuclear complexes—immunofluorescence (IgA versus 'full house') tells them apart.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — IgA nephropathy ultimately injures podocytes: mesangial IgA1 deposits and complement drive cytokines that damage the glomerular filter, so podocyte loss and proteinuria mark progression to chronic kidney disease—podocyte injury predicts a worse course.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — IgA nephropathy and ANCA vasculitis can both cause crescentic glomerulonephritis: severe IgAN with crescents mimics ANCA-associated GN, so a crescentic biopsy needs immunofluorescence and ANCA testing to tell IgA deposition from pauci-immune disease.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Aberrant B cells drive IgA nephropathy: mucosal B cells overproduce galactose-deficient IgA1 that forms immune complexes depositing in the glomerular mesangium, so B-cell-targeted and APRIL/BAFF-blocking therapies are emerging treatments.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome helps trigger IgA nephropathy: mucosal immune responses to gut flora drive production of the abnormal IgA1 that injures the kidney, so the gut-kidney axis explains flares after infections and the interest in microbiome-directed therapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Liver disease causes secondary IgA nephropathy: cirrhosis impairs hepatic clearance of IgA, so IgA immune complexes accumulate and deposit in the kidney—hepatic IgA nephropathy showing how the liver normally protects the glomerulus from IgA overload.
- `connects-to` → **[Immune System](../immune-system/README.md)** — IgA nephropathy is an immune-complex kidney disease: the immune system makes galactose-deficient IgA1 and antibodies against it, forming complexes that lodge in the glomerular mesangium and activate complement—a misdirected mucosal immune response striking the kidney.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — IgA nephropathy classically flares with infection: gross hematuria appears within a day or two of a sore throat (synpharyngitic), unlike post-streptococcal glomerulonephritis weeks later—reflecting how mucosal infection ramps up the pathogenic IgA response.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — IgA nephropathy drives hypertension and is worsened by it: glomerular injury and proteinuria raise blood pressure, which in turn accelerates renal scarring, so strict blood-pressure and proteinuria control with RAS blockade is the cornerstone of slowing progression.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — IgA nephropathy begins with dysregulated T-helper cells at mucosal sites: Th2 and Th17 skewing drives B cells to overproduce galactose-deficient IgA1, the autoantigen whose immune complexes deposit in the glomerulus—linking mucosal T-cell help to kidney injury.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Outcome in IgA nephropathy is written in fibrosis: tubulointerstitial fibrosis and tubular atrophy (the 'T' of the MEST-C score) predict progression to kidney failure better than the glomerular lesions, so preserving nephrons is the long-term goal.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Glomerular endothelium marks active IgA nephropathy: endocapillary hypercellularity (the 'E' score) reflects inflammation of capillary endothelial cells and signals a lesion that may respond to immunosuppression—shaping who gets steroids.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — IgA nephropathy is first treated by blocking angiotensin II: ACE inhibitors and ARBs lower the glomerular pressure that angiotensin II drives, cutting the proteinuria that predicts kidney decline—the cornerstone of slowing this disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — IgA nephropathy classically leaks red cells: immune-complex injury to the glomerulus lets erythrocytes spill into the urine, often as visible hematuria a day or two after a sore throat (synpharyngitic), a hallmark that points to the diagnosis.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — SGLT2 inhibitors now help protect kidneys in IgA nephropathy: blocking this glucose transporter lowers glomerular pressure and proteinuria independent of blood sugar, adding to RAAS blockade as a pillar of slowing progression to kidney failure.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — IgA nephropathy starts in the gut, not the kidney: the abnormal galactose-deficient IgA1 that lands in the glomerulus is made by the small intestine's mucosal immune system, so the gut-kidney axis is central—and a target of gut-release budesonide.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive the kidney damage in IgA nephropathy: drawn into the glomerulus by IgA-immune-complex deposits, they release cytokines and enzymes that inflame and scar the filter, helping turn deposition into progressive kidney injury.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Salt handling shapes IgA nephropathy's course: as the disease scars the kidney, sodium retention worsens hypertension and proteinuria, so dietary salt restriction supports the RAAS-blocking drugs that slow its progression.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — IgA nephropathy has a skin-and-systemic cousin: IgA vasculitis (Henoch-Schönlein purpura) deposits the same IgA complexes in the skin's small vessels, causing the palpable purpura that often accompanies the kidney disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — IgA nephropathy bleeds into the urine: episodes of visible hematuria, classically after a sore throat, plus the anemia of progressing kidney disease, can drain the body's iron over time.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Severe IgA nephropathy recruits neutrophils: in crescentic, rapidly progressive disease they flood the inflamed glomerulus, helping build the cellular crescents that signal aggressive kidney injury.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — IgA nephropathy is diagnosed on the biopsy: immunofluorescence under the microscope lights up the IgA deposits in the glomerular mesangium, the finding that defines the disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Treating IgA nephropathy risks high potassium: the ACE inhibitors and ARBs that protect the kidney by blocking angiotensin also raise potassium, which must be monitored.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — IgA nephropathy may start in the gut: mucosal immunity in the intestinal epithelium produces the galactose-deficient IgA1 that ends up clogging the kidney, the gut-kidney axis behind the disease.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^barratt-2017-igan-review]: Barratt J, Feehally J. IgA nephropathy. *J Am Soc Nephrol.* 2005;16(7):2088-2097. [doi:10.1681/ASN.2005020134](https://doi.org/10.1681/ASN.2005020134) · [PubMed 15987751](https://pubmed.ncbi.nlm.nih.gov/15987751/)
[^heerspink-2023-sparsentan-protect]: Heerspink HJL, Radhakrishnan J, Alpers CE, et al. Sparsentan in patients with IgA nephropathy: a prespecified interim analysis from a randomised, double-blind, active-controlled clinical trial. *Lancet.* 2023;401(10388):1584-1594. [doi:10.1016/S0140-6736(23)00569-X](https://doi.org/10.1016/S0140-6736(23)00569-X) · [PubMed 37062299](https://pubmed.ncbi.nlm.nih.gov/37062299/)
