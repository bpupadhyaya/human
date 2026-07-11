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
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy clinches IgA nephropathy on biopsy: electron-dense immune-complex deposits sit in the mesangium of the glomerulus, the IgA-laden clumps that incite the inflammation scarring the kidney."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Its vasculitic cousin attacks the gut: IgA vasculitis (Henoch-Schönlein), driven by the same IgA, inflames the bowel's small vessels to cause abdominal pain, bleeding, and even intussusception in children."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Rarely the IgA disease bleeds into the lungs: diffuse alveolar hemorrhage is an uncommon but life-threatening extension of IgA vasculitis, the immune complexes inflaming pulmonary as well as renal capillaries."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The disease is autoantibody-driven: glycan-specific IgG and IgA antibodies recognize the galactose-deficient IgA1 hinge, and the resulting antibody–antigen immune complexes lodge in the mesangium — a mechanism that B-cell-depleting and complement antibodies now aim to interrupt."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Damaged glomeruli leak protein: heavier IgA nephropathy spills albumin into the urine, and the degree of proteinuria — alongside falling serum albumin in nephrotic-range cases — is the single strongest predictor of progression to kidney failure."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Failing kidneys cannot finish vitamin D: as IgA nephropathy advances to chronic kidney disease, the kidney's activation of vitamin D falters, driving the low calcium and secondary hyperparathyroidism of renal bone disease."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "A scarred liver can flood the kidney with IgA: cirrhosis — including from NASH — clears IgA poorly, so immune complexes build up and deposit in the mesangium, producing a secondary IgA nephropathy distinct from the primary mucosal-driven disease."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 inflames the glomerulus: the cytokine drives mesangial cells to proliferate and helps B cells churn out the galactose-deficient IgA1 that starts the disease, making the IL-6 axis both a marker and a target in IgA nephropathy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "A failure of immune restraint underlies it: a shortfall of regulatory T cells lets the Th17 and mucosal B-cell responses run unchecked, tipping the balance toward overproduction of the abnormal IgA that drives the nephropathy."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "The faulty antibody is born in germinal centers: it is in these B-cell training grounds, especially at mucosal sites, that class switching to IgA and the affinity maturation go awry, churning out the galactose-deficient IgA1 that later lodges in the glomerulus."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells set the response in motion: mucosal dendritic cells sampling gut and airway antigens drive the IgA class switch and B-cell help, so an exaggerated dendritic-cell signal helps explain the overproduction of pathogenic IgA after infections."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen and other secondary lymphoid organs harbor the long-lived plasma cells that keep secreting galactose-deficient IgA1, a reservoir that sustains the disease and that B-cell-depleting and plasma-cell-targeted therapies aim to empty."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17 arm drives the mucosal overreaction: IL-17A from mucosal helper T cells promotes the aberrant IgA response and renal inflammation of IgA nephropathy, part of the gut-kidney immune axis behind the disease."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Spondyloarthritis carries the nephropathy with it: IgA nephropathy is the commonest glomerulonephritis in ankylosing spondylitis, reflecting the shared dysregulated mucosal IgA immunity of these HLA-linked diseases."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells mark the progressing kidney: their accumulation in the renal interstitium of IgA nephropathy correlates with fibrosis and worse outcome, contributing to the scarring that drives chronic kidney disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Deposited immune complexes inflame the mesangium through NF-κB: galactose-deficient IgA1 complexes activate NF-κB in mesangial cells, driving the cytokine and chemokine output that recruits inflammation and scars the glomerulus."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Heavy proteinuria clots the blood: when IgA nephropathy reaches nephrotic-range protein loss, urinary loss of anticoagulant proteins creates a hypercoagulable state prone to renal vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Immunosuppression and protein loss invite infection: corticosteroids and immunosuppressants for progressive IgA nephropathy, plus urinary immunoglobulin loss in nephrotic disease, predispose to serious infection and sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Declining kidneys and inflammation lower the count: as IgA nephropathy erodes renal function, lost erythropoietin and chronic inflammation produce a renal anemia-of-chronic-disease that worsens as it progresses to CKD."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its immunosuppression opens the lung: the corticosteroids and mycophenolate used for progressive IgA nephropathy deplete T-cell defenses, raising Pneumocystis pneumonia risk enough to warrant prophylaxis in intensive regimens."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Steroids and renal bone disease thin the skeleton: prolonged corticosteroids for IgA nephropathy, compounded by the mineral and vitamin-D derangements of declining kidney function, accelerate bone loss and fracture risk."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Failing kidneys overload the heart: as IgA nephropathy progresses to chronic kidney disease, fluid retention, hypertension and uremic cardiomyopathy strain the heart toward failure."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its immunosuppression opens the lung to mold: the corticosteroids and immunosuppressants used for progressive IgA nephropathy blunt immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic kidney disease weighs on mood: the slow march of IgA nephropathy toward dialysis or transplant, with its dietary restrictions and fatigue, carries a substantial burden of depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its systemic form erupts on the skin: IgA vasculitis (Henoch-Schönlein purpura), the systemic counterpart of IgA nephropathy, causes a palpable purpuric rash over the legs and buttocks."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The same IgA deposits inflame the gut and liver: IgA vasculitis causes colicky abdominal pain, GI bleeding and intussusception, and IgA nephropathy is strongly associated with cirrhosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It inflames the joints: IgA vasculitis, the systemic form of the disease, causes a transient arthritis and arthralgia of the large joints alongside its skin, gut and kidney involvement."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Colds set off its bleeding kidney: IgA nephropathy classically flares with visible haematuria during or just after an upper respiratory infection — 'synpharyngitic' haematuria — reflecting its mucosal-immune origin."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It is born in mucosal lymphoid tissue: the galactose-deficient IgA1 that drives the disease is produced by tonsillar and gut-associated lymphoid tissue, which is why tonsillectomy is sometimes used."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its vasculitic form can reach the brain: rare central-nervous-system involvement of IgA vasculitis causes seizures, headache and intracerebral haemorrhage."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "First-line slows the proteinuria: ACE inhibitors and ARBs reduce intraglomerular pressure and proteinuria in IgA nephropathy, the foundation of conservative treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It carries cardiovascular risk through the kidney: the hypertension and progressive chronic kidney disease of IgA nephropathy markedly raise cardiovascular morbidity."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids target the immune drive: corticosteroids and targeted budesonide are used in progressive IgA nephropathy to suppress the mucosal IgA response damaging the glomeruli."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "Antiproteinuric blockade is foundational: angiotensin-receptor blockers, like ACE inhibitors, lower glomerular pressure and proteinuria to slow IgA nephropathy, the cornerstone of supportive care."
  - target: 01-human/05-tissue/peyers-patches
    relation: connects-to
    note: "Its abnormal antibody is born in the gut: galactose-deficient IgA1 arises from mucosal plasma cells in Peyer's patches and other gut-associated lymphoid tissue, the origin of the immune complexes that deposit in the kidney."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cytotoxic immunosuppression for crescentic disease: cyclophosphamide with steroids is used in rapidly progressive crescentic IgA nephropathy to halt aggressive glomerular injury."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "The kidney disease kills through the arteries: IgA nephropathy drives hypertension and chronic kidney disease that accelerate arterial-wall atherosclerosis and stiffening, making cardiovascular events—not kidney failure alone—a leading cause of death in patients with IgAN."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "A shared mucocutaneous IgA immune axis: IgA nephropathy is associated with psoriasis, and the TNF inhibitors used to treat psoriasis can themselves trigger new-onset IgA nephropathy—linking skin inflammation to glomerular IgA deposition."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Chronic inflammation scars the kidney too: long-standing rheumatoid arthritis can drive secondary renal disease—reactive mesangial IgA deposition and AA amyloidosis from sustained acute-phase IL-6 and serum amyloid A—so a systemic joint disease becomes a glomerular one."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "A new drug target: endothelin-1 drives proteinuria and fibrosis in IgA nephropathy, and the dual endothelin/angiotensin blocker sparsentan reduces proteinuria—a recent therapeutic advance."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Secondary IgA nephropathy: a cirrhotic, failing liver cannot clear IgA immune complexes, so they deposit in the kidney—the gut-liver-kidney axis producing IgAN as a complication of liver disease."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "The spondyloarthropathy link: IgA nephropathy is over-represented in spondyloarthropathies such as psoriatic arthritis and ankylosing spondylitis, reflecting shared mucosal-immune dysregulation."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A mucosal trigger: SARS-CoV-2 infection and, less often, its vaccines can provoke episodes of gross-haematuria IgA nephropathy, a striking example of mucosal immune activation flaring the disease."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "B-cell autoimmunity overlap: Sjogren's syndrome shares the polyclonal B-cell activation and hypergammaglobulinaemia of IgA nephropathy and can itself cause glomerulonephritis, reflecting common mucosal autoimmune drivers."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Cirrhotic glomerulonephritis: chronic hepatitis C and the cirrhosis it causes impair hepatic clearance of IgA immune complexes, producing secondary IgA deposition in the glomerulus that mimics primary IgA nephropathy."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 mucosal axis: the IL-23/Th17 pathway dysregulates mucosal IgA responses and is implicated in IgA nephropathy and its overlap with spondyloarthritis and inflammatory bowel disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Mesangial proliferation: PDGF drives the mesangial cell proliferation and matrix expansion that are the histological hallmark of IgA nephropathy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Podocyte and glomerular injury: dysregulated VEGF signalling at the glomerular filtration barrier contributes to the proteinuria and podocyte injury of progressive IgA nephropathy."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory amplification: TNF-α released in the inflamed glomerulus amplifies the mesangial and tubulointerstitial injury that drives IgA nephropathy toward kidney failure."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: complement and immune-complex deposition activate the NLRP3 inflammasome in IgA nephropathy, whose IL-1β output worsens glomerular inflammation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tubulointerstitial hypoxia: as IgA nephropathy scars the kidney, HIF-1α stabilised in the hypoxic tubulointerstitium drives the fibrosis that predicts progression to renal failure."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Alternative-pathway complement: factor H regulates the alternative complement pathway that is activated by mesangial IgA1 deposits, and CFH-region variants are genetic modifiers of IgA nephropathy."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA genetic risk: MHC class II (HLA-DQ/DR) loci are the strongest genetic associations of IgA nephropathy, linking antigen presentation to the dysregulated mucosal immunity behind the disease."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil alarmin: S100A8/A9 from neutrophils infiltrating the inflamed glomerulus amplifies the mesangioproliferative injury of IgA nephropathy and serves as a marker of activity."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "Mucosal B-cell signalling: BTK transduces the B-cell-receptor signals in the mucosal B cells that produce galactose-deficient IgA1, the founding abnormality of IgA nephropathy and a target of B-cell-directed therapy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Mucosal infection trigger: TLR sensing of mucosal infection drives the IgA response that elevates galactose-deficient IgA1, explaining the synpharyngitic haematuria in which gross haematuria flares with respiratory infections."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Autoantibody recycling: the neonatal Fc receptor protects the anti-glycan IgG autoantibodies that bind galactose-deficient IgA1 to form pathogenic immune complexes, the rationale for FcRn antagonists tested in IgA nephropathy."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Gut-targeted steroid: the targeted-release budesonide Nefecon acts through the glucocorticoid receptor on the gut-associated lymphoid tissue of the distal ileum, reducing production of the galactose-deficient IgA1 at its mucosal source — a first targeted IgA-nephropathy therapy."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Glomerulosclerosis: chronic mesangial immune-complex deposition drives matrix expansion and collagen deposition, the glomerulosclerosis and tubulointerstitial fibrosis that progress to the end-stage kidney failure of advanced IgA nephropathy."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Fibrosis driver: galectin-3 released by infiltrating macrophages promotes the renal interstitial fibrosis of progressive IgA nephropathy, a profibrotic lectin that helps convert the immune injury into irreversible scarring."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement amplification: C5a acting through C5aR1 (complement C5, C3 and factor-H already mapped) amplifies the glomerular inflammation of IgA nephropathy, a target of the emerging complement-directed therapies for the disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Mucosal balance: regulatory IL-10 modulates the mucosal IgA response, and its balance against the Th17/IL-23 axis (mapped) shapes production of the galactose-deficient IgA1 that initiates IgA nephropathy."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome injury: NLRP3 inflammasome activation (mapped) generates IL-1β that drives the glomerular and tubulointerstitial inflammation of progressive IgA nephropathy."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Mucosal IgA trigger: mucosal TLR-MyD88 signalling (TLR4 already mapped) drives the dysregulated IgA response and the synpharyngitic flares characteristic of IgA nephropathy."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Mesangial inflammation: IL-6 signalling through JAK-STAT (IL-6 already mapped) promotes mesangial-cell proliferation and the inflammatory injury of IgA nephropathy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Glomerulosclerosis: TGF-β-SMAD signalling (TGF-β already mapped) drives the mesangial matrix expansion and glomerulosclerosis that determine progression to kidney failure in IgA nephropathy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Galactose-deficient IgA1 immune complexes activate mesangial-cell ERK-MAPK signalling, driving the proliferation and matrix production of IgA nephropathy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling sustains mesangial-cell proliferation and survival in response to the IgA1 immune-complex deposits of IgA nephropathy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling (IL-6 mapped) amplifies the mesangial inflammatory response to IgA1 deposition in IgA nephropathy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory amplification of mesangial injury in IgA nephropathy."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon component of the immune response to mucosal triggers in IgA nephropathy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) drives the mesangial-cell proliferation that follows galactose-deficient IgA1 deposition in IgA nephropathy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the mesangial-cell and immune-cell oxidative-stress responses relevant to the glomerular injury of IgA nephropathy."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the podocyte and mesangial signaling that drives the proteinuria and glomerulosclerosis of IgA nephropathy."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic T-cell activity contributes to the cellular immune injury of crescentic IgA nephropathy."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the podocyte and mesangial-cell stress responses of IgA nephropathy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling in mesangial and immune cells participates in the proliferative response to IgA immune-complex deposition in IgA nephropathy."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the podocyte survival and mesangial-cell responses to immune-complex-driven injury in IgA nephropathy."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the mesangial-cell activation and proliferation of IgA nephropathy."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the glomerular and tubulointerstitial inflammation of IgA nephropathy."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the IgA1-glycosylation and immune abnormalities of IgA nephropathy."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and mesangial interactions of IgA nephropathy."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the mucosal and renal immune responses of IgA nephropathy."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20-expressing B cells contribute to the production of the galactose-deficient IgA1 and autoantibodies of IgA nephropathy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the mucosal-immune and B-cell gene programs of IgA nephropathy."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of IgA nephropathy, and calcineurin inhibitors are used in its treatment."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation and renal responses of IgA nephropathy."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-glycan autoantibodies: the four-hit pathogenesis of IgA nephropathy involves IgG (and IgA) autoantibodies against galactose-deficient IgA1 (secretory IgA already mapped), forming the immune complexes that deposit in the glomerular mesangium."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Haematuria: mesangial injury in IgA nephropathy lets red cells escape into the urine, and episodic visible or persistent microscopic haematuria (often after mucosal infection) is the cardinal clinical sign, with haemoglobin appearing in the urine."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Mucosal IgA dysregulation: Th2 cytokines including IL-4 promote IgA class-switching and the aberrant mucosal-type IgA response that, when galactose-deficient, drives IgA nephropathy, linking the gut-associated immune system to the kidney."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid blockade: aldosterone drives the fibrosis and proteinuria of progressive IgA nephropathy, and mineralocorticoid-receptor antagonists add to the RAAS blockade (angiotensin II already mapped) that slows its decline."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 IgA drive: IL-13, with the IL-4 (already mapped) type-2 response, promotes the aberrant mucosal IgA class-switching that generates the galactose-deficient IgA1 initiating IgA nephropathy."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Renal anaemia: as IgA nephropathy progresses to chronic kidney disease (already mapped), failing erythropoietin production lowers red-cell production, adding the anaemia of renal failure to the haematuria (haemoglobin already mapped)."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Glomerular haemodynamics: renal prostaglandins modulate the glomerular blood flow and inflammation of IgA nephropathy (IL-6 and TNF already mapped), and NSAIDs that block them affect proteinuria and renal function."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: nitric oxide regulates the glomerular endothelial function and vascular tone, and its impairment in IgA nephropathy (endothelin-1 already mapped) contributes to the hypertension and progression of the disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative glomerular injury: oxidative stress, to which xanthine oxidase contributes, damages the mesangium and glomerulus in IgA nephropathy, and the associated hyperuricaemia adds to the renal injury of progressive disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of CKD: as IgA nephropathy progresses, the IL-6-driven (already mapped) hepcidin and the failing erythropoietin (already mapped) production cause the anaemia of chronic kidney disease (haemoglobin already mapped)."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "CKD-mineral-bone disorder: the declining renal function of progressive IgA nephropathy drives the secondary hyperparathyroidism (raised PTH) of the CKD-mineral-bone disorder, disturbing calcium and phosphate balance."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Hyperkalaemia: the falling glomerular filtration of progressive IgA nephropathy, worsened by the RAAS blockade (angiotensin-II and aldosterone already mapped) that treats it, raises the risk of hyperkalaemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "CKD-mineral-bone calcium: the hypocalcaemia and disturbed calcium-phosphate balance of the CKD-mineral-bone disorder (PTH already mapped) of progressive IgA nephropathy."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "CKD hyperphosphataemia: the hyperphosphataemia of the CKD-mineral-bone disorder (PTH already mapped) of the declining renal function of progressive IgA nephropathy, driving the secondary hyperparathyroidism."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Uraemic adipokine: leptin accumulates with the declining renal clearance of progressive IgA nephropathy, part of the metabolic and appetite disturbance of the uraemic state."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Uraemic adipokine: adiponectin, with leptin (already mapped), accumulates and is dysregulated with the declining renal clearance of progressive IgA nephropathy."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Uraemic-retention adipokine: resistin, with leptin and adiponectin (already mapped), is a uraemic-retention and inflammatory (IL-6 already mapped) adipokine of the progressive IgA nephropathy."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Mucosal-trigger interferon: the type-I interferon of the innate mucosal (secretory-IgA already mapped) antiviral response to the upper-respiratory infections triggers the synpharyngitic IgA flares of IgA nephropathy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the T-cell-mediated glomerular inflammation, complementing the Th17 (IL-17 and IL-23 already mapped) drive of IgA nephropathy."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response of IgA nephropathy."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension shaping the mucosal IgA (secretory-IgA already mapped) response of IgA nephropathy."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mucosal arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 mucosal immune dimension that parallels the dysregulated IgA (already mapped) response of IgA nephropathy."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate arm: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the gut-kidney (already mapped) axis of IgA nephropathy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Tubulointerstitial infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the tubulointerstitium and contribute to the progression of IgA nephropathy."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Lectin/classical regulation: the C1-esterase inhibitor regulates the lectin and classical complement pathways (with factor H, C3, C5 and C5aR1 already mapped) whose activation on the mesangial IgA immune complexes drives IgA nephropathy."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Renal fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator and biomarker of the tubulointerstitial fibrosis and progression of IgA nephropathy."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "CKD iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and erythropoietin already mapped) of the anaemia of the chronic kidney disease of IgA nephropathy."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP from intestinal epithelium (already mapped) and tonsil drives IgA class-switching (secretory IgA already mapped) and mucosal B-cell (already mapped) priming that underlies galactose-deficient IgA1 production in IgA nephropathy."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator: histamine from renal mast cells (already mapped) increases vascular permeability and amplifies mesangial IgA (secretory IgA already mapped) deposition and complement (C3 already mapped) activation in IgA nephropathy."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin system: bradykinin activates podocytes (already mapped) and endothelial cells (already mapped) via B2 receptors, amplifying proteinuria and glomerular (already mapped) inflammation; ACE inhibitors (already mapped) reduce its catabolism, potentiating renoprotection in IgAN."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Mesangial antioxidant: melatonin scavenges reactive oxygen species and suppresses NF-kB (already mapped) and NLRP3 (already mapped) inflammasome in mesangial cells, limiting the oxidative-stress component of the IgA immune-complex injury at the glomerulus (already mapped)."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immunostimulatory prolactin: prolactin acts on its receptor (PRL-R) on B cells (already mapped) and lymphocytes, potentiating the mucosal immunity and IgA class-switching (secretory IgA already mapped) that underlies the galactose-deficient IgA1 production of IgA nephropathy."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Renoprotective oxytocin: oxytocin, released from the posterior pituitary, attenuates renal NF-kB (already mapped) signalling and mast-cell (already mapped) activation, reducing proteinuria and the inflammatory injury at the glomerulus (already mapped) of IgA nephropathy."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-IgAN axis: testosterone, via androgen receptor signalling on mesangial cells (already mapped) and B cells (already mapped), modulates IgA class-switching, galactose-deficient IgA1 production, and the well-established male sex predominance of IgA nephropathy."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin-IgAN axis: serotonin, released by platelets (already mapped) activated during IgA1-IC mesangial deposition, amplifies the mesangial cell (already mapped) proliferation, complement activation (already mapped), and the glomerular haematuria of IgA nephropathy."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Vasopressin-IgAN axis: vasopressin, via V2 receptors on the renal collecting duct, modulates water reabsorption and urinary IgA excretion, and its dysregulation contributes to the hypertension (already mapped) and renal progression of IgA nephropathy."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "IgAN selenium: selenium, as a cofactor for glutathione peroxidases and thioredoxin reductases, attenuates glomerular oxidative stress; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) podocyte (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "IgAN iodine: iodine, via thyroid hormone biosynthesis, modulates podocyte (already mapped) barrier function and renal filtration; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) glomerular (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "IgAN magnesium: magnesium, as an essential cofactor for complement regulation and endothelial (already mapped) function, attenuates glomerular (already mapped) injury; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "IgAN copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises glomerular ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of IgA nephropathy."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "IgAN zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and mast cells (already mapped), attenuates glomerular oxidative stress; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "IgAN chloride: chloride, regulating NKCC1-mediated ion transport in macrophages (already mapped) and neutrophils (already mapped), maintains renal homeostasis; chloride dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "IgAN sulfur: sulfur, as hydrogen sulfide and cysteine in macrophages (already mapped) and neutrophils (already mapped), modulates renal oxidative stress; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "IgAN nitrogen: nitrogen, as reactive nitrogen species in macrophages (already mapped) and neutrophils (already mapped), modulates renal inflammation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "IgAN oxygen: oxygen, via ROS in macrophages (already mapped) and neutrophils (already mapped), drives mesangial and tubular oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "IgAN carbon: carbon backbone of IgA molecules and cytokines (already mapped) sustains mesangial immune-complex signalling; carbon metabolites in macrophages (already mapped) and neutrophils (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in IgAN."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "IgAN hydrogen: hydrogen as proton gradient in mesangial and tubular mitochondria drives ATP synthesis; hydrogen-ion acidosis amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) glomerular and tubulointerstitial injury in IgA nephropathy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "IgAN PD-1: PD-1-mediated checkpoint restrains T-cytotoxic-cell (already mapped) mesangial cytotoxicity; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immune-complex-driven glomerulonephritis in IgA nephropathy."
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
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy clinches IgA nephropathy on biopsy: electron-dense immune-complex deposits sit in the mesangium of the glomerulus, the IgA-laden clumps that incite the inflammation scarring the kidney.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Its vasculitic cousin attacks the gut: IgA vasculitis (Henoch-Schönlein), driven by the same IgA, inflames the bowel's small vessels to cause abdominal pain, bleeding, and even intussusception in children.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Rarely the IgA disease bleeds into the lungs: diffuse alveolar hemorrhage is an uncommon but life-threatening extension of IgA vasculitis, the immune complexes inflaming pulmonary as well as renal capillaries.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The disease is autoantibody-driven: glycan-specific IgG and IgA antibodies recognize the galactose-deficient IgA1 hinge, and the resulting antibody–antigen immune complexes lodge in the mesangium — a mechanism that B-cell-depleting and complement antibodies now aim to interrupt.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Damaged glomeruli leak protein: heavier IgA nephropathy spills albumin into the urine, and the degree of proteinuria — alongside falling serum albumin in nephrotic-range cases — is the single strongest predictor of progression to kidney failure.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Failing kidneys cannot finish vitamin D: as IgA nephropathy advances to chronic kidney disease, the kidney's activation of vitamin D falters, driving the low calcium and secondary hyperparathyroidism of renal bone disease.
- `connects-to` → **[NASH](../nash/README.md)** — A scarred liver can flood the kidney with IgA: cirrhosis — including from NASH — clears IgA poorly, so immune complexes build up and deposit in the mesangium, producing a secondary IgA nephropathy distinct from the primary mucosal-driven disease.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 inflames the glomerulus: the cytokine drives mesangial cells to proliferate and helps B cells churn out the galactose-deficient IgA1 that starts the disease, making the IL-6 axis both a marker and a target in IgA nephropathy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — A failure of immune restraint underlies it: a shortfall of regulatory T cells lets the Th17 and mucosal B-cell responses run unchecked, tipping the balance toward overproduction of the abnormal IgA that drives the nephropathy.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — The faulty antibody is born in germinal centers: it is in these B-cell training grounds, especially at mucosal sites, that class switching to IgA and the affinity maturation go awry, churning out the galactose-deficient IgA1 that later lodges in the glomerulus.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells set the response in motion: mucosal dendritic cells sampling gut and airway antigens drive the IgA class switch and B-cell help, so an exaggerated dendritic-cell signal helps explain the overproduction of pathogenic IgA after infections.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen and other secondary lymphoid organs harbor the long-lived plasma cells that keep secreting galactose-deficient IgA1, a reservoir that sustains the disease and that B-cell-depleting and plasma-cell-targeted therapies aim to empty.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17 arm drives the mucosal overreaction: IL-17A from mucosal helper T cells promotes the aberrant IgA response and renal inflammation of IgA nephropathy, part of the gut-kidney immune axis behind the disease.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Spondyloarthritis carries the nephropathy with it: IgA nephropathy is the commonest glomerulonephritis in ankylosing spondylitis, reflecting the shared dysregulated mucosal IgA immunity of these HLA-linked diseases.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells mark the progressing kidney: their accumulation in the renal interstitium of IgA nephropathy correlates with fibrosis and worse outcome, contributing to the scarring that drives chronic kidney disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Deposited immune complexes inflame the mesangium through NF-κB: galactose-deficient IgA1 complexes activate NF-κB in mesangial cells, driving the cytokine and chemokine output that recruits inflammation and scars the glomerulus.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Heavy proteinuria clots the blood: when IgA nephropathy reaches nephrotic-range protein loss, urinary loss of anticoagulant proteins creates a hypercoagulable state prone to renal vein thrombosis and pulmonary embolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Immunosuppression and protein loss invite infection: corticosteroids and immunosuppressants for progressive IgA nephropathy, plus urinary immunoglobulin loss in nephrotic disease, predispose to serious infection and sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Declining kidneys and inflammation lower the count: as IgA nephropathy erodes renal function, lost erythropoietin and chronic inflammation produce a renal anemia-of-chronic-disease that worsens as it progresses to CKD.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its immunosuppression opens the lung: the corticosteroids and mycophenolate used for progressive IgA nephropathy deplete T-cell defenses, raising Pneumocystis pneumonia risk enough to warrant prophylaxis in intensive regimens.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Steroids and renal bone disease thin the skeleton: prolonged corticosteroids for IgA nephropathy, compounded by the mineral and vitamin-D derangements of declining kidney function, accelerate bone loss and fracture risk.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Failing kidneys overload the heart: as IgA nephropathy progresses to chronic kidney disease, fluid retention, hypertension and uremic cardiomyopathy strain the heart toward failure.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its immunosuppression opens the lung to mold: the corticosteroids and immunosuppressants used for progressive IgA nephropathy blunt immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic kidney disease weighs on mood: the slow march of IgA nephropathy toward dialysis or transplant, with its dietary restrictions and fatigue, carries a substantial burden of depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its systemic form erupts on the skin: IgA vasculitis (Henoch-Schönlein purpura), the systemic counterpart of IgA nephropathy, causes a palpable purpuric rash over the legs and buttocks.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The same IgA deposits inflame the gut and liver: IgA vasculitis causes colicky abdominal pain, GI bleeding and intussusception, and IgA nephropathy is strongly associated with cirrhosis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It inflames the joints: IgA vasculitis, the systemic form of the disease, causes a transient arthritis and arthralgia of the large joints alongside its skin, gut and kidney involvement.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Colds set off its bleeding kidney: IgA nephropathy classically flares with visible haematuria during or just after an upper respiratory infection — 'synpharyngitic' haematuria — reflecting its mucosal-immune origin.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It is born in mucosal lymphoid tissue: the galactose-deficient IgA1 that drives the disease is produced by tonsillar and gut-associated lymphoid tissue, which is why tonsillectomy is sometimes used.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its vasculitic form can reach the brain: rare central-nervous-system involvement of IgA vasculitis causes seizures, headache and intracerebral haemorrhage.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — First-line slows the proteinuria: ACE inhibitors and ARBs reduce intraglomerular pressure and proteinuria in IgA nephropathy, the foundation of conservative treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It carries cardiovascular risk through the kidney: the hypertension and progressive chronic kidney disease of IgA nephropathy markedly raise cardiovascular morbidity.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids target the immune drive: corticosteroids and targeted budesonide are used in progressive IgA nephropathy to suppress the mucosal IgA response damaging the glomeruli.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — Antiproteinuric blockade is foundational: angiotensin-receptor blockers, like ACE inhibitors, lower glomerular pressure and proteinuria to slow IgA nephropathy, the cornerstone of supportive care.
- `connects-to` → **[Peyer's Patches](../../05-tissue/peyers-patches/README.md)** — Its abnormal antibody is born in the gut: galactose-deficient IgA1 arises from mucosal plasma cells in Peyer's patches and other gut-associated lymphoid tissue, the origin of the immune complexes that deposit in the kidney.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cytotoxic immunosuppression for crescentic disease: cyclophosphamide with steroids is used in rapidly progressive crescentic IgA nephropathy to halt aggressive glomerular injury.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — The kidney disease kills through the arteries: IgA nephropathy drives hypertension and chronic kidney disease that accelerate arterial-wall atherosclerosis and stiffening, making cardiovascular events—not kidney failure alone—a leading cause of death in patients with IgAN.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — A shared mucocutaneous IgA immune axis: IgA nephropathy is associated with psoriasis, and the TNF inhibitors used to treat psoriasis can themselves trigger new-onset IgA nephropathy—linking skin inflammation to glomerular IgA deposition.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Chronic inflammation scars the kidney too: long-standing rheumatoid arthritis can drive secondary renal disease—reactive mesangial IgA deposition and AA amyloidosis from sustained acute-phase IL-6 and serum amyloid A—so a systemic joint disease becomes a glomerular one.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — A new drug target: endothelin-1 drives proteinuria and fibrosis in IgA nephropathy, and the dual endothelin/angiotensin blocker sparsentan reduces proteinuria—a recent therapeutic advance.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Secondary IgA nephropathy: a cirrhotic, failing liver cannot clear IgA immune complexes, so they deposit in the kidney—the gut-liver-kidney axis producing IgAN as a complication of liver disease.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — The spondyloarthropathy link: IgA nephropathy is over-represented in spondyloarthropathies such as psoriatic arthritis and ankylosing spondylitis, reflecting shared mucosal-immune dysregulation.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A mucosal trigger: SARS-CoV-2 infection and, less often, its vaccines can provoke episodes of gross-haematuria IgA nephropathy, a striking example of mucosal immune activation flaring the disease.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — B-cell autoimmunity overlap: Sjogren's syndrome shares the polyclonal B-cell activation and hypergammaglobulinaemia of IgA nephropathy and can itself cause glomerulonephritis, reflecting common mucosal autoimmune drivers.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Cirrhotic glomerulonephritis: chronic hepatitis C and the cirrhosis it causes impair hepatic clearance of IgA immune complexes, producing secondary IgA deposition in the glomerulus that mimics primary IgA nephropathy.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 mucosal axis: the IL-23/Th17 pathway dysregulates mucosal IgA responses and is implicated in IgA nephropathy and its overlap with spondyloarthritis and inflammatory bowel disease.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Mesangial proliferation: PDGF drives the mesangial cell proliferation and matrix expansion that are the histological hallmark of IgA nephropathy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Podocyte and glomerular injury: dysregulated VEGF signalling at the glomerular filtration barrier contributes to the proteinuria and podocyte injury of progressive IgA nephropathy.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory amplification: TNF-α released in the inflamed glomerulus amplifies the mesangial and tubulointerstitial injury that drives IgA nephropathy toward kidney failure.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: complement and immune-complex deposition activate the NLRP3 inflammasome in IgA nephropathy, whose IL-1β output worsens glomerular inflammation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tubulointerstitial hypoxia: as IgA nephropathy scars the kidney, HIF-1α stabilised in the hypoxic tubulointerstitium drives the fibrosis that predicts progression to renal failure.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Alternative-pathway complement: factor H regulates the alternative complement pathway that is activated by mesangial IgA1 deposits, and CFH-region variants are genetic modifiers of IgA nephropathy.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — HLA genetic risk: MHC class II (HLA-DQ/DR) loci are the strongest genetic associations of IgA nephropathy, linking antigen presentation to the dysregulated mucosal immunity behind the disease.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil alarmin: S100A8/A9 from neutrophils infiltrating the inflamed glomerulus amplifies the mesangioproliferative injury of IgA nephropathy and serves as a marker of activity.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK transduces the B-cell-receptor signals in the mucosal B cells that produce galactose-deficient IgA1, the founding abnormality of IgA nephropathy and an emerging target of B-cell-directed therapy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR sensing of mucosal infection drives the IgA response that elevates galactose-deficient IgA1, explaining the synpharyngitic hematuria in which visible bleeding flares concurrently with respiratory or gut infections.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The neonatal Fc receptor protects the anti-glycan IgG autoantibodies that bind galactose-deficient IgA1 to form the pathogenic mesangial immune complexes—the rationale for FcRn antagonists now being tested in IgA nephropathy.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — The targeted-release budesonide Nefecon acts through the glucocorticoid receptor on the gut-associated lymphoid tissue of the distal ileum, reducing production of the galactose-deficient IgA1 at its mucosal source—a first targeted IgA-nephropathy therapy.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Chronic mesangial immune-complex deposition drives matrix expansion and collagen deposition, the glomerulosclerosis and tubulointerstitial fibrosis that progress to the end-stage kidney failure of advanced IgA nephropathy.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by infiltrating macrophages promotes the renal interstitial fibrosis of progressive IgA nephropathy, a profibrotic lectin that helps convert the immune injury into irreversible scarring.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a acting through C5aR1 (complement C5, C3 and factor-H already mapped) amplifies the glomerular inflammation of IgA nephropathy, a target of the emerging complement-directed therapies for the disease.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Regulatory IL-10 modulates the mucosal IgA response, and its balance against the Th17/IL-23 axis (mapped) shapes production of the galactose-deficient IgA1 that initiates IgA nephropathy.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — NLRP3 inflammasome activation (mapped) generates IL-1β that drives the glomerular and tubulointerstitial inflammation of progressive IgA nephropathy.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Mucosal TLR-MyD88 signaling (TLR4 already mapped) drives the dysregulated IgA response and the synpharyngitic flares characteristic of IgA nephropathy.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 signaling through JAK-STAT (IL-6 already mapped) promotes mesangial-cell proliferation and the inflammatory injury of IgA nephropathy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the mesangial matrix expansion and glomerulosclerosis that determine progression to kidney failure in IgA nephropathy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Galactose-deficient IgA1 immune complexes activate mesangial-cell ERK-MAPK signaling, driving the proliferation and matrix production of IgA nephropathy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling sustains mesangial-cell proliferation and survival in response to the IgA1 immune-complex deposits of IgA nephropathy.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (IL-6 mapped) amplifies the mesangial inflammatory response to IgA1 deposition in IgA nephropathy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory amplification of mesangial injury in IgA nephropathy.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon component of the immune response to mucosal triggers in IgA nephropathy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) drives the mesangial-cell proliferation that follows galactose-deficient IgA1 deposition in IgA nephropathy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the mesangial-cell and immune-cell oxidative-stress responses relevant to the glomerular injury of IgA nephropathy.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the podocyte and mesangial signaling that drives the proteinuria and glomerulosclerosis of IgA nephropathy.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic T-cell activity contributes to the cellular immune injury of crescentic IgA nephropathy.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the podocyte and mesangial-cell stress responses of IgA nephropathy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling in mesangial and immune cells participates in the proliferative response to IgA immune-complex deposition in IgA nephropathy.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the podocyte survival and mesangial-cell responses to immune-complex-driven injury in IgA nephropathy.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the mesangial-cell activation and proliferation of IgA nephropathy.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the glomerular and tubulointerstitial inflammation of IgA nephropathy.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the IgA1-glycosylation and immune abnormalities of IgA nephropathy.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and mesangial interactions of IgA nephropathy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the mucosal and renal immune responses of IgA nephropathy.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20-expressing B cells contribute to the production of the galactose-deficient IgA1 and autoantibodies of IgA nephropathy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the mucosal-immune and B-cell gene programs of IgA nephropathy.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of IgA nephropathy, and calcineurin inhibitors are used in its treatment.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation and renal responses of IgA nephropathy.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-glycan autoantibodies: the four-hit pathogenesis of IgA nephropathy involves IgG (and IgA) autoantibodies against galactose-deficient IgA1 (secretory IgA already mapped), forming the immune complexes that deposit in the glomerular mesangium.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Haematuria: mesangial injury in IgA nephropathy lets red cells escape into the urine, and episodic visible or persistent microscopic haematuria (often after mucosal infection) is the cardinal clinical sign, with haemoglobin appearing in the urine.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Mucosal IgA dysregulation: Th2 cytokines including IL-4 promote IgA class-switching and the aberrant mucosal-type IgA response that, when galactose-deficient, drives IgA nephropathy, linking the gut-associated immune system to the kidney.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid blockade: aldosterone drives the fibrosis and proteinuria of progressive IgA nephropathy, and mineralocorticoid-receptor antagonists add to the RAAS blockade (angiotensin II already mapped) that slows its decline.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 IgA drive: IL-13, with the IL-4 (already mapped) type-2 response, promotes the aberrant mucosal IgA class-switching that generates the galactose-deficient IgA1 initiating IgA nephropathy.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Renal anaemia: as IgA nephropathy progresses to chronic kidney disease (already mapped), failing erythropoietin production lowers red-cell production, adding the anaemia of renal failure to the haematuria (haemoglobin already mapped).
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Glomerular haemodynamics: renal prostaglandins modulate the glomerular blood flow and inflammation of IgA nephropathy (IL-6 and TNF already mapped), and NSAIDs that block them affect proteinuria and renal function.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: nitric oxide regulates the glomerular endothelial function and vascular tone, and its impairment in IgA nephropathy (endothelin-1 already mapped) contributes to the hypertension and progression of the disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative glomerular injury: oxidative stress, to which xanthine oxidase contributes, damages the mesangium and glomerulus in IgA nephropathy, and the associated hyperuricaemia adds to the renal injury of progressive disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of CKD: as IgA nephropathy progresses, the IL-6-driven (already mapped) hepcidin and the failing erythropoietin (already mapped) production cause the anaemia of chronic kidney disease (haemoglobin already mapped).
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — CKD-mineral-bone disorder: the declining renal function of progressive IgA nephropathy drives the secondary hyperparathyroidism (raised PTH) of the CKD-mineral-bone disorder, disturbing calcium and phosphate balance.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Hyperkalaemia: the falling glomerular filtration of progressive IgA nephropathy, worsened by the RAAS blockade (angiotensin-II and aldosterone already mapped) that treats it, raises the risk of hyperkalaemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — CKD-mineral-bone calcium: the hypocalcaemia and disturbed calcium-phosphate balance of the CKD-mineral-bone disorder (PTH already mapped) of progressive IgA nephropathy.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — CKD hyperphosphataemia: the hyperphosphataemia of the CKD-mineral-bone disorder (PTH already mapped) of the declining renal function of progressive IgA nephropathy, driving the secondary hyperparathyroidism.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Uraemic adipokine: leptin accumulates with the declining renal clearance of progressive IgA nephropathy, part of the metabolic and appetite disturbance of the uraemic state.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Uraemic adipokine: adiponectin, with leptin (already mapped), accumulates and is dysregulated with the declining renal clearance of progressive IgA nephropathy.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Uraemic-retention adipokine: resistin, with leptin and adiponectin (already mapped), is a uraemic-retention and inflammatory (IL-6 already mapped) adipokine of the progressive IgA nephropathy.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Mucosal-trigger interferon: the type-I interferon of the innate mucosal (secretory-IgA already mapped) antiviral response to the upper-respiratory infections triggers the synpharyngitic IgA flares of IgA nephropathy.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the T-cell-mediated glomerular inflammation, complementing the Th17 (IL-17 and IL-23 already mapped) drive of IgA nephropathy.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune response of IgA nephropathy.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension shaping the mucosal IgA (secretory-IgA already mapped) response of IgA nephropathy.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mucosal arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 mucosal immune dimension that parallels the dysregulated IgA (already mapped) response of IgA nephropathy.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate arm: the NK cells (perforin already mapped) are part of the innate immune dysregulation of the gut-kidney (already mapped) axis of IgA nephropathy.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Tubulointerstitial infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the tubulointerstitium and contribute to the progression of IgA nephropathy.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Lectin/classical regulation: the C1-esterase inhibitor regulates the lectin and classical complement pathways (with factor H, C3, C5 and C5aR1 already mapped) whose activation on the mesangial IgA immune complexes drives IgA nephropathy.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Renal fibrosis: periostin, downstream of the TGF-β (already mapped) signalling, is a matricellular mediator and biomarker of the tubulointerstitial fibrosis and progression of IgA nephropathy.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — CKD iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and erythropoietin already mapped) of the anaemia of the chronic kidney disease of IgA nephropathy.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP from intestinal epithelium (already mapped) and tonsil drives IgA class-switching (secretory IgA already mapped) and mucosal B-cell (already mapped) priming that underlies galactose-deficient IgA1 production in IgA nephropathy.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator: histamine from renal mast cells (already mapped) increases vascular permeability and amplifies mesangial IgA (secretory IgA already mapped) deposition and complement (C3 already mapped) activation in IgA nephropathy.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin system: bradykinin activates podocytes (already mapped) and endothelial cells (already mapped) via B2 receptors, amplifying proteinuria and glomerular (already mapped) inflammation; ACE inhibitors (already mapped) reduce its catabolism, potentiating renoprotection in IgAN.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Mesangial antioxidant: melatonin scavenges reactive oxygen species and suppresses NF-κB (already mapped) and NLRP3 (already mapped) inflammasome in mesangial cells, limiting the oxidative-stress component of the IgA immune-complex injury at the glomerulus (already mapped).
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immunostimulatory prolactin: prolactin acts on its receptor (PRL-R) on B cells (already mapped) and lymphocytes, potentiating the mucosal immunity and IgA class-switching (secretory IgA already mapped) that underlies the galactose-deficient IgA1 production of IgA nephropathy.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Renoprotective oxytocin: oxytocin, released from the posterior pituitary, attenuates renal NF-κB (already mapped) signalling and mast-cell (already mapped) activation, reducing proteinuria and the inflammatory injury at the glomerulus (already mapped) of IgA nephropathy.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-IgAN axis: testosterone, via androgen receptor signalling on mesangial cells (already mapped) and B cells (already mapped), modulates IgA class-switching, galactose-deficient IgA1 production, and the well-established male sex predominance of IgA nephropathy.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin-IgAN axis: serotonin, released by platelets (already mapped) activated during IgA1-IC mesangial deposition, amplifies the mesangial cell (already mapped) proliferation, complement activation (already mapped), and the glomerular haematuria of IgA nephropathy.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Vasopressin-IgAN axis: vasopressin, via V2 receptors on the renal collecting duct, modulates water reabsorption and urinary IgA excretion, and its dysregulation contributes to the hypertension (already mapped) and renal progression of IgA nephropathy.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — IgAN selenium: selenium, as a cofactor for glutathione peroxidases and thioredoxin reductases, attenuates glomerular oxidative stress; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) podocyte (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — IgAN iodine: iodine, via thyroid hormone biosynthesis, modulates podocyte (already mapped) barrier function and renal filtration; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) glomerular (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — IgAN magnesium: magnesium, as an essential cofactor for complement regulation and endothelial (already mapped) function, attenuates glomerular (already mapped) injury; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — IgAN copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises glomerular ROS; copper deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of IgA nephropathy.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — IgAN zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and mast cells (already mapped), attenuates glomerular oxidative stress; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — IgAN chloride: chloride, regulating NKCC1-mediated ion transport in macrophages (already mapped) and neutrophils (already mapped), maintains renal homeostasis; chloride dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — IgAN sulfur: sulfur, as hydrogen sulfide and cysteine in macrophages (already mapped) and neutrophils (already mapped), modulates renal oxidative stress; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — IgAN nitrogen: nitrogen, as reactive nitrogen species in macrophages (already mapped) and neutrophils (already mapped), modulates renal inflammation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — IgAN oxygen: oxygen, via ROS in macrophages (already mapped) and neutrophils (already mapped), drives mesangial and tubular oxidative stress; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of IgA nephropathy.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — IgAN carbon: carbon backbone of IgA molecules and cytokines (already mapped) sustains mesangial immune-complex signalling; carbon metabolites in macrophages (already mapped) and neutrophils (already mapped) amplify NF-κB (already mapped) and IL-6 (already mapped) in IgAN.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — IgAN hydrogen: hydrogen as proton gradient in mesangial and tubular mitochondria drives ATP synthesis; hydrogen-ion acidosis amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) glomerular and tubulointerstitial injury in IgA nephropathy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — IgAN PD-1: PD-1-mediated checkpoint restrains T-cytotoxic-cell (already mapped) mesangial cytotoxicity; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immune-complex-driven glomerulonephritis in IgA nephropathy.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^barratt-2017-igan-review]: Barratt J, Feehally J. IgA nephropathy. *J Am Soc Nephrol.* 2005;16(7):2088-2097. [doi:10.1681/ASN.2005020134](https://doi.org/10.1681/ASN.2005020134) · [PubMed 15987751](https://pubmed.ncbi.nlm.nih.gov/15987751/)
[^heerspink-2023-sparsentan-protect]: Heerspink HJL, Radhakrishnan J, Alpers CE, et al. Sparsentan in patients with IgA nephropathy: a prespecified interim analysis from a randomised, double-blind, active-controlled clinical trial. *Lancet.* 2023;401(10388):1584-1594. [doi:10.1016/S0140-6736(23)00569-X](https://doi.org/10.1016/S0140-6736(23)00569-X) · [PubMed 37062299](https://pubmed.ncbi.nlm.nih.gov/37062299/)
