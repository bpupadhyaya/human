---
schema: human-scale-entry/v1
id: renal-system
name: Renal System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "Two kidneys, two ureters, bladder, and urethra. Filters 180 L plasma/day, maintains fluid/electrolyte/acid-base homeostasis, excretes nitrogenous waste, and produces EPO, renin, and calcitriol. Tightly coupled to cardiovascular system via RAAS."
aliases: ["urinary system", "renal-urinary system", "excretory system"]
sources:
  - id: hall-guyton-14
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 26-32."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: vanholder-2017-ckd-costs
    type: peer-reviewed
    cite: "Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care: a call to action. Nat Rev Nephrol. 2017;13(7):393-409."
    doi: "10.1038/nrneph.2017.63"
    pmid: "28479604"
    url: "https://doi.org/10.1038/nrneph.2017.63"
  - id: kdigo-2012-ckd
    type: regulatory
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int Suppl. 2013;3(1):1-150."
    url: "https://kdigo.org/guidelines/ckd-evaluation-and-management/"
    accessed: "2026-06-04"
  - id: openstax-anatomy-ch25
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 25: The Urinary System."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/25-introduction"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The renal system is one of the major organ systems of the integrated human body."
  - target: 01-human/06-organ/kidney
    relation: contains
    note: "The kidneys are the primary functional organs of the renal system — housing nephrons, performing filtration, reabsorption, secretion, and endocrine functions."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "RAAS (renin-angiotensin-aldosterone system) bidirectionally couples renal function to cardiac output and systemic BP; ANP/BNP natriuretic peptides from the heart modulate renal Na⁺ handling."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: treated-by
    note: "ACE inhibitors are first-line renoprotective therapy in diabetic and non-diabetic CKD; they reduce intraglomerular pressure and proteinuria by blocking Ang II."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: treated-by
    note: "Loop diuretics block NKCC2 in the thick ascending limb; cornerstone of fluid management in AKI, CKD-associated edema, and nephrotic syndrome."
  - target: 01-human/05-tissue/glomerulus
    relation: contains
    note: "The glomerulus is the tissue-level filtration structure within each nephron of the kidney."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Renal and intestinal Na⁺/H₂O handling are complementary; aldosterone and ANP coordinate gut and kidney fluid reabsorption; hepatorenal interactions include shared RAAS regulation."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: treated-by
    note: "ARBs are first-line renoprotective therapy in diabetic and non-diabetic CKD; AT1 blockade dilates the efferent arteriole, reducing intraglomerular pressure, proteinuria, and CKD progression (RENAAL, IDNT trials)."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: modulated-by
    note: "RAAS blockade by ARBs reduces angiotensin II–driven efferent vasoconstriction, decreasing glomerular hypertension and filtration of albumin; also reduces aldosterone-driven Na⁺ retention and tubular fibrosis."
  - target: 01-human/03-molecular/vasopressin
    relation: modulated-by
    note: "Modulated by Vasopressin."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: damaged-by
    note: "Damaged by Streptococcus pyogenes."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic kidney disease is the renal system's common end state: progressive nephron loss from diabetes, hypertension, or glomerular disease reduces GFR, so the kidney fails its fluid, electrolyte, acid-base, waste, and endocrine roles—ending in dialysis or transplant."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The renal system is also an endocrine organ within the endocrine system: the kidney secretes erythropoietin and renin and activates vitamin D, while responding to aldosterone, ADH, and PTH—so kidney disease causes anemia, bone disease, and blood-pressure dysregulation."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "IgA nephropathy is the world's commonest primary glomerulonephritis, a core renal-system disease: galactose-deficient IgA1 immune complexes deposit in the mesangium, causing hematuria (often after mucosal infection) and, in many, progression to chronic kidney disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The renal system is an endocrine organ via erythropoietin: peritubular cells sense low oxygen and secrete EPO to drive red-cell production, so kidney disease causes anemia while EPO excess causes polycythemia—linking renal function to oxygen-carrying capacity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium balance is a core renal-system job: the kidney tunes potassium excretion under aldosterone, so renal failure causes life-threatening hyperkalemia while diuretics cause hypokalemia—small shifts in this ion can stop the heart, making renal K+ handling vital."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Renal cell carcinoma is the principal cancer of the renal system: arising from tubular epithelium, it can secrete erythropoietin or renin (paraneoplastic syndromes) and presents late with hematuria or a mass—turning the kidney's own physiology into its tumor's behavior."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "Podocytes are the renal system's filtration gatekeepers: their interlocking foot processes form the slit diaphragm that holds protein back, so podocyte injury causes proteinuria and nephrotic syndrome—a frequent first step toward chronic kidney disease."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Renin launches the renal system's blood-pressure axis: juxtaglomerular cells release it when renal perfusion or sodium falls, triggering angiotensin and aldosterone to retain salt and water—so the kidney is the body's master regulator of volume and pressure."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium handling is the renal system's central task: the nephron filters and precisely reabsorbs sodium to set extracellular volume and blood pressure, so disordered renal sodium balance drives both hypertension and edema, and is the target of most diuretics."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Aldosterone is the kidney's salt-retaining hormone: released via the renin axis, it makes the distal nephron reabsorb sodium and excrete potassium, so it sets blood volume and pressure—and blocking it (spironolactone) treats resistant hypertension and heart failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "The kidney is central to calcium balance: it activates vitamin D to absorb calcium, fine-tunes calcium excretion under PTH, and when it fails, disturbed calcium-phosphate handling drives the bone disease and stones of kidney disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Kidney and blood pressure are locked in a two-way grip: the kidney sets long-term pressure through salt and the renin system, yet high pressure also damages its vessels—so hypertension is both a leading cause and a consequence of kidney disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "The kidney is where vitamin D becomes active: it performs the final 1-alpha-hydroxylation to calcitriol, so kidney failure causes vitamin D deficiency and the bone disease of CKD—one of the organ's vital endocrine, non-excretory jobs."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The renal system is the body's phosphate gatekeeper: kidneys excrete phosphate under FGF23 and PTH control, so failing kidneys retain it, driving the calcium-phosphate imbalance and vascular calcification of CKD-mineral bone disorder."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "The kidney and PTH run the calcium-phosphate axis together: failing kidneys retain phosphate and underproduce active vitamin D, driving secondary hyperparathyroidism in which PTH soars to defend calcium—at the cost of the bones."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "The kidney is the body's slow acid-base regulator through hydrogen: it excretes hydrogen ions and regenerates bicarbonate to hold blood pH steady, so kidney failure or tubular defects cause the metabolic acidosis (renal tubular acidosis) of renal disease."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "The kidney's filter is judged by albumin: a healthy glomerulus keeps this protein in the blood, so albumin leaking into urine (albuminuria) is the earliest, most sensitive sign of kidney damage and a marker that guides treatment."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "The renal system controls blood pressure through angiotensin II: the kidney's renin launches the cascade that makes angiotensin II to constrict vessels and tune filtration, the loop that ACE inhibitors and ARBs block to protect the kidney."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The filtration barrier is built on endothelial cells: the glomerulus's fenestrated endothelium, with podocytes and the basement membrane, sieves the blood, so endothelial injury (as in preeclampsia or microangiopathy) leaks protein and crashes filtration."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "The kidney is the body's oxygen gauge: cells sensing low oxygen release erythropoietin to make red cells, while the medulla works on the edge of hypoxia, which is why poor perfusion so readily causes acute tubular injury."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart and kidney rise or fall together: in cardiorenal syndrome a failing heart starves and congests the kidney while fluid overload and neurohormones strain the heart, a vicious loop central to managing heart failure."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The kidney is read by imaging: ultrasound and CT photons reveal stones, obstruction and cysts, while nuclear renography traces how well each kidney filters and drains."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The kidney commands the bone marrow: its erythropoietin tells the marrow how many red cells to make, so kidney failure starves the marrow of that signal and causes the anemia of chronic kidney disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Kidney and brain share fate: uremic toxins cloud the mind, the kidney's blood-pressure control guards against stroke, and rapid dialysis can swell the brain in disequilibrium syndrome."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the kidney's exquisite filter: podocyte foot processes interdigitate over the slit diaphragm above a basement membrane and fenestrated endothelium — the three-layer barrier that holds back protein while letting water and salts pass."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "The kidney is the body's magnesium thermostat: it finely tunes how much of the mineral is reabsorbed or spilled into urine, so renal and tubular disorders are a leading cause of both magnesium deficiency and excess."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Kidney and lung jointly hold the body's pH steady: the lungs blow off carbon dioxide while the kidney adjusts bicarbonate and acid, and when the kidney fails to clear fluid, the backed-up water floods the lungs as pulmonary edema."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver and kidney share the work of detox: the liver turns ammonia into urea that the kidney then excretes, the two clear many drugs in tandem, and a failing liver can drag the kidney down with it in the hepatorenal syndrome."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The nervous system tunes the kidney minute to minute: sympathetic nerves and baroreceptors adjust renal blood flow and renin release to defend blood pressure, while the buildup of wastes in kidney failure clouds the brain into uremic encephalopathy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The kidney is a frequent immune battleground: circulating immune complexes and complement lodge in the glomerulus to cause the many glomerulonephritides, making renal biopsy a window onto systemic autoimmune disease like lupus."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Specific autoantibodies name the kidney's diseases: anti-GBM antibodies attack the glomerular basement membrane in Goodpasture, ANCA drives the small-vessel vasculitides, and these blood tests pinpoint which glomerulonephritis is at work."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "The kidney sets the body's urate: it excretes most uric acid, so impaired renal handling raises blood urate into gout and urate stones, while gout's crystals and its drugs in turn injure the kidney — a two-way burden."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Failing kidneys show on the skin: uremia brings relentless itch and a sallow hue, disturbed calcium-phosphate balance calcifies skin vessels into deadly calciphylaxis, and the skin's vitamin D awaits the kidney's final activating step."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The kidney and adrenal run the salt axis together: the kidney's renin triggers the adrenal cortex to release aldosterone, which acts back on the nephron to retain sodium and excrete potassium, closing the loop that sets blood volume and pressure."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading destroyer of the renal system: chronic high glucose thickens and scars the glomerulus into diabetic nephropathy, the single biggest cause of kidney failure and dialysis worldwide."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Bone signals the kidney about phosphate: FGF23 from bone tells the nephron to dump phosphate and curb active vitamin D, and as kidneys fail FGF23 climbs early, an opening move in the mineral-bone disorder of CKD."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "The proximal tubule reclaims the body's sugar: SGLT2 there reabsorbs nearly all filtered glucose, and blocking it spills glucose into the urine — drugs that lower sugar while unexpectedly protecting the kidney and heart."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "One kidney cell wears two hats: peritubular fibroblasts make the erythropoietin that drives red-cell production, yet when injured they transform into myofibroblasts that lay down the scar of chronic kidney disease."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Autoimmunity often lands on the kidney: lupus nephritis, where immune complexes inflame the glomeruli, is among the most serious manifestations of SLE and a leading reason the disease becomes life-threatening."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "The developing kidney can spawn a cancer: Wilms tumor (nephroblastoma) arises from embryonic renal precursor cells, the most common kidney cancer of childhood and the pediatric counterpart to adult renal cell carcinoma."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The kidney is both a source and a casualty of sepsis: urinary infection ascending to pyelonephritis can seed urosepsis, while severe sepsis in turn starves the kidneys into acute kidney injury."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Leaky kidneys clot the blood: nephrotic syndrome spills anticoagulant proteins into the urine, leaving a hypercoagulable state prone to renal vein thrombosis and pulmonary embolism."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Its commonest infection ascends from below: uropathogenic E. coli climbs the urinary tract to cause cystitis and pyelonephritis, the renal system's most frequent infection and a leading cause of urosepsis."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "A blood cancer can clog the nephrons: multiple myeloma floods the filtrate with light chains that precipitate into casts, causing myeloma cast nephropathy — a classic route to kidney failure."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Heart and kidney rise and fall together: in cardiorenal syndrome, a failing heart's low output and venous congestion impair renal perfusion, while fluid overload from failing kidneys back-strains the heart."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Failing kidneys stop making the red-cell hormone: the kidney produces erythropoietin, so as renal function declines, EPO falls and a characteristic renal anemia develops, often needing replacement to correct."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The kidney governs bone mineral balance: as renal function fails, impaired vitamin D activation and phosphate handling disturb calcium balance, producing the renal osteodystrophy and bone fragility of CKD-mineral bone disorder."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Kidney failure and dialysis weigh on mood: the fatigue, dietary and fluid restrictions and time burden of dialysis give advanced kidney disease one of the highest rates of depression among chronic illnesses."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "They share the genitourinary tract: the urinary and reproductive systems develop together and run side by side, so prostatic obstruction, pelvic surgery and pregnancy all directly affect the kidneys and bladder."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Lungs and kidneys jointly balance acid and can fail together: the kidney and lung co-regulate acid-base status, and pulmonary-renal syndromes like Goodpasture and ANCA vasculitis attack both at once."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Failing kidneys are written on the skin: uraemia causes intractable pruritus and a sallow complexion, and advanced renal failure can produce calciphylaxis and, with gadolinium, nephrogenic systemic fibrosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The kidney mineralises the skeleton: by regulating calcium, phosphate and active vitamin D, it keeps bone healthy, so renal failure causes renal osteodystrophy with weak, painful bones and fractures."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis can seed the urinary tract: genitourinary TB causes sterile pyuria, ureteric strictures and renal scarring, a quiet cause of declining kidney function in endemic regions."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Common painkillers can injure it: NSAIDs like ibuprofen reduce renal blood flow and can cause acute kidney injury, acute interstitial nephritis and, with chronic use, analgesic nephropathy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "A hidden network drains it: a rich renal lymphatic system clears interstitial fluid and protein from the kidney, and when overwhelmed it contributes to the oedema of nephrotic syndrome."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "A common diabetes drug it must clear: metformin is renally excreted and accumulates in kidney failure, risking lactic acidosis, so it is dose-reduced or stopped as eGFR falls."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: connects-to
    note: "A powerful antibiotic that can harm it: vancomycin is nephrotoxic and renally cleared, so it requires blood-level monitoring and dose adjustment to protect the kidney."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "A virus that scars the glomerulus: chronic hepatitis B causes membranous nephropathy and polyarteritis-nodosa renal disease through immune-complex deposition, one of several viral causes of kidney disease."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Infection inflames the kidney: Staphylococcus aureus causes infection-related glomerulonephritis and is a leading organism in dialysis-access infection and septic acute kidney injury."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "The gut talks to the kidney through diet: dietary fibre shifts the microbiome to produce fewer uraemic toxins like indoxyl sulfate, of interest in slowing chronic kidney disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Scarring is the common endpoint: whatever the initial insult — diabetes, hypertension, glomerulonephritis — progressive kidney disease converges on tubulointerstitial fibrosis, the strongest histological predictor of nephron loss and renal failure."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The kidney both clears and is harmed: it excretes many cytotoxic drugs so dosing tracks GFR, while cisplatin, methotrexate and tumour-lysis from chemotherapy are major causes of acute kidney injury."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "A renal-limited thrombotic microangiopathy: atypical haemolytic uraemic syndrome, from uncontrolled complement activation, attacks the glomerular and arteriolar endothelium to cause acute kidney injury, treated with the complement inhibitor eculizumab."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It governs blood pressure through the arteries: the kidney's renin-angiotensin system tunes arterial-wall tone and volume, while renal-artery atherosclerosis or stenosis drives secondary hypertension—a two-way axis between kidney and vessel."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A hereditary cause of kidney lesions: tuberous sclerosis studs the kidneys with angiomyolipomas (fat-and-vessel hamartomas that can haemorrhage) and cysts, a leading source of its morbidity treated with mTOR inhibitors."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Inherited renal cysts and cancer: von Hippel-Lindau disease fills the kidneys with cysts and multiple clear cell renal cell carcinomas, the leading cause of death in VHL and a model of hereditary kidney cancer."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Crescentic glomerulonephritis: ANCA-associated vasculitis is a leading cause of rapidly progressive glomerulonephritis, its pauci-immune necrotising injury destroying nephrons within weeks unless promptly treated."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Sickle nephropathy: sickle cell disease injures the kidney through medullary papillary necrosis, impaired urine concentration and a FSGS-like glomerulopathy, a common path to chronic kidney disease."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Acute kidney injury and collapsing GN: COVID-19 frequently causes acute kidney injury in severe disease and, in those with high-risk APOL1 variants, a collapsing glomerulopathy."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Cardiorenal calcification: chronic kidney disease accelerates atherosclerosis through uraemia, calcium-phosphate dysregulation and FGF23, making cardiovascular disease the leading cause of death in renal patients."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmune tubular disease: Sjögren's syndrome attacks the kidney as tubulointerstitial nephritis and distal renal tubular acidosis, a tubular pattern distinct from the glomerular injury of lupus nephritis."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Potassium and the heartbeat: the kidney's control of potassium ties it to the cardiac conduction system, where the hyperkalaemia of renal failure peaks the T wave and can stop the heart."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Renal blood flow: endothelial nitric oxide dilates the afferent arteriole and tunes glomerular pressure, and its loss in renal disease promotes hypertension and progressive injury."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoconstrictor counterweight: endothelin-1 constricts renal vessels and drives sodium retention and fibrosis, making endothelin antagonism a target in proteinuric kidney disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis master switch: TGF-β drives the tubulointerstitial fibrosis and glomerulosclerosis that are the common final pathway of chronic kidney disease progression."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Filtration-barrier maintenance: podocyte-derived VEGF sustains the fenestrated glomerular endothelium, which is why anti-VEGF cancer therapy causes proteinuria, hypertension and thrombotic microangiopathy."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Glomerular complement: C3 and the alternative pathway drive immune injury in glomerulonephritis and C3 glomerulopathy, a major mechanism of kidney damage targeted by emerging complement inhibitors."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Natriuretic counter-regulation: natriuretic peptides like BNP act on the kidney to promote sodium and water excretion, opposing the renin-angiotensin system in the cardiorenal control of volume."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Renal hemodynamics: prostaglandins (PGE2, prostacyclin) dilate the afferent arteriole and stimulate renin release to protect renal blood flow under stress, which is why NSAIDs that block them precipitate acute kidney injury."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Tubuloglomerular feedback: adenosine released at the macula densa in response to high tubular sodium constricts the afferent arteriole through A1 receptors, the feedback loop that stabilises single-nephron GFR."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kallikrein-kinin balance: the renal kallikrein-kinin system generates bradykinin that promotes vasodilation and natriuresis, a counter-regulatory arm to angiotensin II in the kidney's control of blood pressure and volume."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mineral homeostasis: the kidney is central to calcium balance, filtering it and reabsorbing it under PTH and vitamin-D control through channels like TRPV5 in the distal tubule, linking renal function to bone health and the disturbances of chronic kidney disease."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Intrarenal natriuresis: locally produced dopamine acts on proximal-tubule D1 receptors to inhibit sodium reabsorption and promote its excretion, an intrarenal natriuretic system that helps regulate blood pressure independent of the systemic circulation."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic renoprotection: GLP-1 receptor agonists exert direct renal effects that reduce albuminuria and slow the decline of kidney function in diabetic kidney disease, linking the incretin axis to renal outcomes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Oxygen sensing: the kidney is the body's oxygen sensor — peritubular cells stabilise HIF in hypoxia to produce the erythropoietin already mapped, the axis exploited by HIF-prolyl-hydroxylase inhibitors to treat renal anaemia."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Development and fibrosis: Wnt/β-catenin signalling patterns nephron development and, when pathologically reactivated, drives the tubulointerstitial fibrosis that is the final common pathway of chronic kidney disease."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Nephron patterning: NOTCH signalling directs nephron-progenitor differentiation and podocyte specification during kidney development, and its reactivation contributes to glomerular disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Fibrosis effector: TGF-β signalling through SMAD4 (TGF-β mapped) activates myofibroblasts to lay down the tubulointerstitial fibrosis that is the final common pathway of chronic kidney disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Tubular growth and cysts: mTOR governs tubular-cell and podocyte size, and its dysregulation drives the cyst growth of polycystic kidney disease and the hypertrophy of diabetic nephropathy."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Antioxidant defence: NRF2 protects the kidney against oxidative injury, and pharmacological NRF2 activation (bardoxolone) raises filtration rate in chronic kidney disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling maintains podocyte and tubular-cell survival and mediates the hypertrophic responses central to renal physiology and disease."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The NLRP3 inflammasome links metabolic and crystalline injury to the tubulointerstitial inflammation and fibrosis of chronic kidney disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 drives renal interstitial fibrosis and is a biomarker of progressive kidney disease, complementing the TGF-β/SMAD4 fibrotic axis already mapped."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling drives tubulointerstitial inflammation and the fibrotic progression shared across chronic kidney diseases of the renal system."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links tubular cell injury to the sterile inflammation of acute kidney injury and progressive renal disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF signalling drives mesangial and interstitial fibroblast proliferation, a core mechanism of the glomerulosclerosis and fibrosis of the renal system."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate podocyte and tubular-cell oxidative-stress defense and metabolic homeostasis across the renal system."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the immune-mediated glomerular and tubulointerstitial inflammation of renal disorders."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of growth factors and angiotensin II (PDGF and angiotensin-II already mapped) drives mesangial and tubular proliferation and fibrosis in the renal system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt/β-catenin signaling that governs nephron development and repair (Wnt already mapped), regulates the tubular and podocyte homeostasis of the renal system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the growth, survival, and metabolic homeostasis of the renal tubular epithelium."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins participate in the inflammatory signaling of tubulointerstitial injury in the renal system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK integrates the high energy demand of tubular transport, coupling the metabolism of the renal system to its reabsorptive function."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB inflammatory signaling participates in the tubulointerstitial inflammation and injury responses of the renal system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the podocyte and tubular-cell homeostasis and stress resilience of the renal system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the podocyte, tubular-epithelial, and growth-factor responses of the renal system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the nephron development and tubular gene expression of the renal system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the renal immune surveillance and inflammatory responses of the renal system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the renal development and immune-cell trafficking of the renal system."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 signaling participates in the renal inflammatory responses of the renal system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the renal inflammatory responses of the renal system."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Acid-base balance: the kidney maintains systemic pH by secreting protons and regenerating bicarbonate in the tubules, and its failure to excrete fixed acid produces the metabolic acidosis characteristic of renal disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic role: the kidney clears insulin and contributes to gluconeogenesis, so renal failure both prolongs insulin action, risking hypoglycaemia, and induces the insulin resistance that accompanies chronic kidney disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Renal anaemia: the kidney produces erythropoietin (already mapped) and its disease raises hepcidin through inflammation and reduced clearance, restricting iron availability and driving the anaemia of chronic kidney disease."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular tone control: smooth muscle in the afferent and efferent arterioles and the mesangium sets glomerular filtration pressure under RAAS and sympathetic control (angiotensin II already mapped), the microvascular regulation central to renal function."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Interstitial inflammation: infiltrating macrophages drive the tubulointerstitial inflammation and fibrosis (TGF-beta already mapped) that determine progression of chronic kidney disease, a key immune contributor to renal scarring."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Renal anaemia: falling erythropoietin (already mapped) production by the diseased kidney lowers haemoglobin, the renal anaemia treated with erythropoiesis-stimulating agents and, more recently, HIF stabilisers."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Urate handling: the kidney excretes most of the body's uric acid produced by xanthine oxidase, and impaired renal excretion causes hyperuricaemia and gout, while urate crystals and stones in turn injure the kidney."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron balance and anaemia: the kidney's failing erythropoietin (already mapped) and the raised hepcidin (already mapped) of chronic kidney disease disturb iron availability, producing an iron-restricted renal anaemia managed with iron and erythropoiesis-stimulating agents."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Renal inflammation: TNF and the inflammatory cytokines (IL-6 and IL-1 already mapped) drive the interstitial inflammation and fibrosis (TGF-beta already mapped) of progressive kidney disease, a target of anti-inflammatory approaches to slow renal decline."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Chloride transport: chloride is co-transported with sodium (already mapped) by the NKCC2 and NCC transporters that loop and thiazide diuretics block, and its handling underlies the kidney's control of volume and acid-base balance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium handling: the kidney is the principal regulator of magnesium, reabsorbing it in the loop and distal tubule, and renal wasting (as with loop diuretics or Gitelman syndrome) causes the hypomagnesaemia of renal disease."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal-renal axis: the adrenal gland's aldosterone (already mapped) acts on the distal nephron to reabsorb sodium and excrete potassium (already mapped), closing the renin-angiotensin-aldosterone loop that the kidney initiates."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 repair and fibrosis: IL-4 drives the M2 macrophages (already mapped) and the type-2 immunity involved in the renal repair and, when dysregulated, the interstitial fibrosis (TGF-β already mapped) of chronic kidney disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Profibrotic type-2 cytokine: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that contributes to the renal interstitial fibrosis (TGF-β already mapped) driving the progression of chronic kidney disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Renal adipokine clearance: leptin is cleared by the renal system and accumulates in renal failure, contributing to the cachexia, sympathetic activation and cardiovascular risk of chronic kidney disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Uraemic adipokine: adiponectin, with leptin (already mapped), is cleared by and accumulates in the renal failure, part of the uraemic metabolic-cardiovascular milieu of the renal system."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Uraemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), accumulates in the renal failure and contributes to the uraemic inflammatory-metabolic milieu of the renal system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Immune nephritis: the CD4 T-helper cells drive the immune glomerular and tubulointerstitial nephritis of the renal system, mediating the immune kidney injury."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Humoral nephritis: the B cells, with the T-helper cells (already mapped), drive the autoantibody and immune-complex glomerulonephritis of the renal system, the rituximab (anti-CD20) target."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Autoantibody plasma cells: the plasma cells secrete the autoantibodies (anti-GBM, immune-complex) that deposit in the glomerulus and drive the immune kidney injury of the renal system."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Renal tolerance: the regulatory T cells restrain the immune nephritis (T-helper cells already mapped) and maintain the tolerance of the renal system."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 nephritis: the IFN-γ of the infiltrating T cells is the type-II interferon arm driving the crescentic and lupus nephritides of the renal system."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune nephritis of the renal system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 nephritis: IL-17A drives the Th17 arm of the ANCA-associated and crescentic glomerulonephritides of the renal system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the crescentic and ANCA-associated glomerulonephritides of the renal system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Epithelial alarmin: IL-33, released by the injured tubular and endothelial cells, activates the ILC2s and shapes the type-2 (IL-4 and IL-13 already mapped) response and the fibrosis of the renal system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension (the allergic interstitial nephritis and minimal-change disease) of the renal system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the membrane-attack complex central to the membranous nephropathy and the complement-mediated glomerular injury of the renal system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment of the glomerulonephritis and the ANCA vasculitis of the renal system."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation causes the C3 glomerulopathy and atypical HUS of the renal system."
taxonomy:
  uberon: "UBERON:0001008"
---

# Renal System

## Overview

The renal system — also called the urinary system — is the body's master regulator of plasma composition, fluid volume, and chemical waste elimination. It comprises two **kidneys**, two **ureters**, the **urinary bladder**, and the **urethra** [^openstax-anatomy-ch25].

While its anatomical simplicity belies its functional complexity, the renal system executes one of the most demanding tasks in human physiology: continuously sampling and adjusting the chemical composition of every milliliter of plasma, 24 hours a day, filtering 180 liters of plasma per day while returning 99% of the filtrate to the circulation with exquisite selectivity. The kidneys maintain plasma Na⁺ within ±5 mEq/L, pH within ±0.05 units, and plasma osmolality within ±5 mOsm/kg — tolerances that no other organ system can achieve.

Beyond excretion, the renal system is an endocrine hub: the kidneys secrete **erythropoietin** (EPO, regulating red blood cell production), **renin** (initiating the RAAS cascade to control blood pressure), and produce **calcitriol** (1,25-dihydroxyvitamin D₃, regulating calcium-phosphate metabolism). This makes CKD a multisystem disease — its complications span anemia (low EPO), hypertension (high renin), and bone disease (low calcitriol) [^hall-guyton-14].

The renal and cardiovascular systems are deeply interdependent: renal perfusion depends on cardiac output; renal RAAS controls vascular resistance and cardiac preload; impaired kidney function is the dominant non-cardiac predictor of cardiovascular mortality.

## Structure

### Organs and Anatomical Relationships

**Kidneys** — paired, retroperitoneal, at T12–L3. Right kidney displaced inferior by liver. Each ~150 g, ~11 × 6 × 3 cm. Surrounded by renal capsule, perirenal fat, renal fascia (Gerota's). Composed of cortex (glomeruli, proximal/distal tubules), medulla (loops of Henle, collecting ducts, pyramids), and pelvis (drainage).

**Ureters** — fibromuscular tubes (~25–30 cm) connecting renal pelvis to bladder. Peristaltic waves propel urine. Three anatomical narrowings (sites of stone impaction): ureteropelvic junction, pelvic brim crossing, ureterovesical junction.

**Urinary Bladder** — muscular reservoir (capacity 400–600 mL comfortable, ~1000 mL maximum). Wall: urothelium (transitional epithelium) → lamina propria → detrusor muscle (smooth muscle). Trigone (base): orifices of two ureters + internal urethral orifice.

**Urethra** — female (~4 cm) or male (~20 cm, incorporating prostatic, membranous, and spongy/penile segments). External urethral sphincter (voluntary, skeletal muscle) allows conscious voiding control.

### Innervation and Voiding Reflex

Micturition is controlled by overlapping autonomic and somatic systems:
- **Parasympathetic (S2–S4, pelvic nerves)** — detrusor contraction (M3 receptors); internal sphincter relaxation
- **Sympathetic (T10–L2, hypogastric nerves)** — detrusor relaxation (β3 receptors); internal sphincter contraction (α1 receptors) — stores urine
- **Somatic (S2–S4, pudendal nerve)** — external sphincter voluntary control
- **Pontine micturition center** — coordinates parasympathetic activation + sphincter relaxation; overridden by cortical inhibition during continent storage

### Nephron Structure

~1–2 million nephrons per kidney (combined total ~2 million). Each nephron = renal corpuscle + proximal tubule + loop of Henle + distal tubule + collecting duct. See [Kidney](../../06-organ/kidney/README.md) for detailed nephron anatomy.

### Vascular Supply

Renal arteries arise directly from the aorta at L1–L2 and deliver 20–25% of cardiac output to the kidneys (~1.1 L/min combined). The high flow relative to kidney mass (5× body average) reflects the filtration function, not metabolic demand. Renal veins drain to the inferior vena cava.

### Lymphatics

Renal lymphatics drain to para-aortic lymph nodes. Obstruction (lymphoma, retroperitoneal fibrosis) can cause chyluria.

## Function

### Plasma Ultrafiltration and Selective Reabsorption

At the [glomerulus](../../05-tissue/glomerulus/README.md), hydrostatic pressure forces a protein-free filtrate into Bowman's space. Tubular epithelial cells then selectively reabsorb 99%+ of the filtrate through a coordinated array of transporters and channels:

- **PCT:** 65–70% NaCl and water; 100% glucose, amino acids, phosphate; 85% HCO₃⁻
- **Loop of Henle:** ~25% NaCl (ascending limb); ~15% water (descending limb); creates medullary gradient
- **DCT:** ~5% NaCl; regulated Ca²⁺ and Mg²⁺
- **Collecting duct:** aldosterone-regulated Na⁺; ADH-regulated water

### Electrolyte and Volume Homeostasis

The kidney is the dominant regulator of:

| Parameter | Mechanism |
|:---|:---|
| **Na⁺** | PCT (NHE3, Na⁺-K⁺-ATPase), TAL (NKCC2), DCT (NCC), CCD (ENaC/aldosterone) |
| **K⁺** | CCD principal cells: aldosterone ↑ K⁺ secretion via ROMK; intercalated cells reabsorb K⁺ |
| **Ca²⁺** | PCT (passive, 60%), TAL (passive, CLDN16/19), DCT (active, TRPV5/calbidin/NCX1) — PTH and calcitriol regulate |
| **Phosphate** | PCT (NaPi-IIa/IIc) — PTH inhibits; FGF-23 inhibits |
| **Magnesium** | TAL (CLDN16 paracellular), DCT (TRPM6 active) |
| **H⁺/HCO₃⁻** | PCT (HCO₃⁻ reclamation), α-IC cells (H⁺ secretion/net acid excretion) |

### Nitrogen Waste Excretion

The kidneys are the primary route for excreting nitrogenous waste:
- **Urea** — product of hepatic urea cycle (from ammonia of amino acid catabolism); filtered + partially reabsorbed + recycled in medullary concentration mechanism; serum BUN reflects balance between generation and excretion
- **Creatinine** — nonenzymatic breakdown product of creatine phosphate in muscle; near-freely filtered, minimally secreted; serum creatinine inversely reflects GFR (the basis of CKD staging)
- **Uric acid** — purine catabolism end-product; filtered, largely reabsorbed, secreted by PCT OAT4/URAT1 transporters; hyperuricemia causes gout, and high urate predicts CKD progression

### Acid-Base Homeostasis

Normal plasma pH = 7.35–7.45. The kidney handles long-term acid-base balance:
1. **HCO₃⁻ reclamation** in PCT — 85% of filtered bicarbonate recovered
2. **New HCO₃⁻ generation** in collecting duct α-intercalated cells via H⁺-ATPase — each H⁺ secreted = one new HCO₃⁻ returned to blood
3. **Ammonium (NH₄⁺) excretion** — PCT glutamine catabolism generates NH₃ → combines with H⁺ → NH₄⁺ in tubular lumen → excreted in urine; most important buffer for chronic acid loads
4. **Titratable acid excretion** — H⁺ buffered by HPO₄²⁻ → H₂PO₄⁻; excreted

### RAAS and Blood Pressure

RAAS is the dominant hormonal control loop for long-term blood pressure (see [Kidney](../../06-organ/kidney/README.md)):
- Renin from JG cells → Ang I → Ang II → vasoconstriction + aldosterone → Na⁺/water retention → blood pressure restoration
- ACE inhibitors block this cascade — antihypertensive + renoprotective

Natriuretic counterpoint:
- **ANP/BNP** (from atria/ventricles when stretched) → increase GFR, inhibit ENaC, suppress aldosterone and renin → natriuresis + diuresis → volume reduction

### Endocrine Functions

- **Erythropoietin (EPO):** Cortical peritubular fibroblasts; secreted in response to HIF-2α activation under hypoxia; drives RBC production in bone marrow. CKD → EPO deficiency → normocytic normochromic anemia of CKD; treated with recombinant EPO (epoetin) or HIF-prolyl hydroxylase inhibitors.
- **Renin:** JG cells; cleaves angiotensinogen; RAAS initiator.
- **Calcitriol (1,25(OH)₂D₃):** CYP27B1 (1α-hydroxylase) in PCT converts 25(OH)D → calcitriol; regulated by PTH, FGF-23, Ca²⁺, phosphate; stimulates intestinal Ca²⁺/PO₄ absorption; suppresses PTH; CKD → loss of 1α-hydroxylase → low calcitriol → secondary hyperparathyroidism → renal osteodystrophy.

## Connections

- **Part of:** [Human Body](../../08-whole-body/human-body/README.md) — one of the major organ systems.
- **Contains:** [Kidney](../../06-organ/kidney/README.md) — the primary functional organ.
- **Contains:** [Glomerulus](../../05-tissue/glomerulus/README.md) — the tissue-level filtration unit.
- **Contains:** [Podocyte](../../04-cellular/podocyte/README.md) — the key glomerular cell.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — RAAS, natriuretic peptides, and volume/pressure interdependence.
- **Connects to:** [Digestive System](../digestive-system/README.md) — water and electrolyte reabsorption in the gut is complementary and overlapping with renal control.
- **Connects to:** [Chronic Kidney Disease](../ckd/README.md) — the renal system's common end state: progressive nephron loss reduces GFR until fluid, electrolyte, acid-base, waste, and endocrine roles all fail, ending in dialysis or transplant.
- **Connects to:** [Endocrine System](../endocrine-system/README.md) — the kidney is itself endocrine, secreting erythropoietin and renin and activating vitamin D while responding to aldosterone, ADH, and PTH.
- **Connects to:** [IgA Nephropathy](../iga-nephropathy/README.md) — the world's commonest primary glomerulonephritis: mesangial galactose-deficient IgA1 deposits cause hematuria and can progress to chronic kidney disease.
- **Connects to:** [Erythropoietin](../../03-molecular/erythropoietin/README.md) — the renal system is an endocrine organ: peritubular cells sense low oxygen and secrete EPO to drive red-cell production, so kidney disease causes anemia while EPO excess causes polycythemia.
- **Connects to:** [Potassium](../../02-atomic/potassium/README.md) — potassium balance is a core renal job: the kidney tunes K+ excretion under aldosterone, so renal failure causes hyperkalemia while diuretics cause hypokalemia—shifts that can stop the heart.
- **Connects to:** [Renal Cell Carcinoma](../renal-cell-carcinoma/README.md) — the principal cancer of the renal system: arising from tubular epithelium, it can secrete erythropoietin or renin (paraneoplastic) and presents late with hematuria or a mass.
- **Connects to:** [Podocyte](../../04-cellular/podocyte/README.md) — podocytes are the renal system's filtration gatekeepers: their foot processes form the slit diaphragm that holds protein back, so podocyte injury causes proteinuria and nephrotic syndrome, a frequent first step toward CKD.
- **Connects to:** [Renin](../../03-molecular/renin/README.md) — renin launches the renal system's blood-pressure axis: juxtaglomerular cells release it when perfusion or sodium falls, triggering angiotensin and aldosterone to retain salt and water—making the kidney the master regulator of volume and pressure.
- **Connects to:** [Sodium](../../02-atomic/sodium/README.md) — sodium handling is the renal system's central task: the nephron filters and reabsorbs sodium to set extracellular volume and blood pressure, so disordered renal sodium balance drives hypertension and edema and is the target of most diuretics.
- **Connects to:** [Aldosterone](../../03-molecular/aldosterone/README.md) — Aldosterone is the kidney's salt-retaining hormone: released via the renin axis, it makes the distal nephron reabsorb sodium and excrete potassium, so it sets blood volume and pressure—and blocking it (spironolactone) treats resistant hypertension and heart failure.
- **Connects to:** [Calcium](../../02-atomic/calcium/README.md) — The kidney is central to calcium balance: it activates vitamin D to absorb calcium, fine-tunes calcium excretion under PTH, and when it fails, disturbed calcium-phosphate handling drives the bone disease and stones of kidney disease.
- **Connects to:** [Hypertension](../hypertension/README.md) — Kidney and blood pressure are locked in a two-way grip: the kidney sets long-term pressure through salt and the renin system, yet high pressure also damages its vessels—so hypertension is both a leading cause and a consequence of kidney disease.
- **Connects to:** [Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md) — The kidney is where vitamin D becomes active: it performs the final 1-alpha-hydroxylation to calcitriol, so kidney failure causes vitamin D deficiency and the bone disease of CKD—one of the organ's vital endocrine, non-excretory jobs.
- **Connects to:** [Phosphorus](../../02-atomic/phosphorus/README.md) — The renal system is the body's phosphate gatekeeper: kidneys excrete phosphate under FGF23 and PTH control, so failing kidneys retain it, driving the calcium-phosphate imbalance and vascular calcification of CKD-mineral bone disorder.
- **Connects to:** [PTH](../../03-molecular/pth/README.md) — The kidney and PTH run the calcium-phosphate axis together: failing kidneys retain phosphate and underproduce active vitamin D, driving secondary hyperparathyroidism in which PTH soars to defend calcium—at the cost of the bones.
- **Connects to:** [Hydrogen](../../02-atomic/hydrogen/README.md) — the kidney is the body's slow acid-base regulator through hydrogen: it excretes hydrogen ions and regenerates bicarbonate to hold blood pH steady, so kidney failure or tubular defects cause the metabolic acidosis (renal tubular acidosis) of renal disease.
- **Connects to:** [Albumin](../../03-molecular/albumin/README.md) — the kidney's filter is judged by albumin: a healthy glomerulus keeps this protein in the blood, so albumin leaking into urine (albuminuria) is the earliest, most sensitive sign of kidney damage and a marker that guides treatment.
- **Connects to:** [Angiotensin II](../../03-molecular/angiotensin-ii/README.md) — the renal system controls blood pressure through angiotensin II: the kidney's renin launches the cascade that makes angiotensin II to constrict vessels and tune filtration, the loop that ACE inhibitors and ARBs block to protect the kidney.
- **Connects to:** [Endothelial Cell](../../04-cellular/endothelial-cell/README.md) — the filtration barrier is built on endothelial cells: the glomerulus's fenestrated endothelium, with podocytes and the basement membrane, sieves the blood, so endothelial injury (as in preeclampsia or microangiopathy) leaks protein and crashes filtration.
- **Connects to:** [Oxygen](../../02-atomic/oxygen/README.md) — the kidney is the body's oxygen gauge: cells sensing low oxygen release erythropoietin to make red cells, while the medulla works on the edge of hypoxia, which is why poor perfusion so readily causes acute tubular injury.
- **Connects to:** [Heart](../../06-organ/heart/README.md) — the heart and kidney rise or fall together: in cardiorenal syndrome a failing heart starves and congests the kidney while fluid overload and neurohormones strain the heart, a vicious loop central to managing heart failure.
- **Connects to:** [Photon](../../01-subatomic/photon/README.md) — the kidney is read by imaging: ultrasound and CT photons reveal stones, obstruction and cysts, while nuclear renography traces how well each kidney filters and drains.
- **Connects to:** [Bone Marrow](../../05-tissue/bone-marrow/README.md) — the kidney commands the bone marrow: its erythropoietin tells the marrow how many red cells to make, so kidney failure causes the anemia of chronic kidney disease.
- **Connects to:** [Brain](../../06-organ/brain/README.md) — kidney and brain share fate: uremic toxins cloud the mind, the kidney's blood-pressure control guards against stroke, and rapid dialysis can swell the brain in disequilibrium syndrome.
- **Connects to:** [Electron](../../01-subatomic/electron/README.md) — electron microscopy reveals the kidney's exquisite filter: podocyte foot processes interdigitate over the slit diaphragm above a basement membrane and fenestrated endothelium — the three-layer barrier holding back protein while passing water and salts.
- **Connects to:** [Magnesium](../../02-atomic/magnesium/README.md) — the kidney is the body's magnesium thermostat: it finely tunes how much is reabsorbed or spilled into urine, so renal and tubular disorders are a leading cause of both magnesium deficiency and excess.
- **Connects to:** [Lung](../../06-organ/lung/README.md) — kidney and lung jointly hold the body's pH steady: the lungs blow off carbon dioxide while the kidney adjusts bicarbonate and acid, and when the kidney fails to clear fluid, the backed-up water floods the lungs as pulmonary edema.
- **Connects to:** [Liver](../../06-organ/liver/README.md) — liver and kidney share the work of detox: the liver turns ammonia into urea that the kidney then excretes, the two clear many drugs in tandem, and a failing liver can drag the kidney down with it in the hepatorenal syndrome.
- **Connects to:** [Nervous System](../nervous-system/README.md) — the nervous system tunes the kidney minute to minute: sympathetic nerves and baroreceptors adjust renal blood flow and renin release to defend blood pressure, while the buildup of wastes in kidney failure clouds the brain into uremic encephalopathy.
- **Connects to:** [Immune System](../immune-system/README.md) — the kidney is a frequent immune battleground: circulating immune complexes and complement lodge in the glomerulus to cause the many glomerulonephritides, making renal biopsy a window onto systemic autoimmune disease like lupus.
- **Connects to:** [Antibody](../../03-molecular/antibody/README.md) — specific autoantibodies name the kidney's diseases: anti-GBM antibodies attack the glomerular basement membrane in Goodpasture, ANCA drives the small-vessel vasculitides, and these blood tests pinpoint which glomerulonephritis is at work.
- **Connects to:** [Gout](../gout/README.md) — the kidney sets the body's urate: it excretes most uric acid, so impaired renal handling raises blood urate into gout and urate stones, while gout's crystals and its drugs in turn injure the kidney — a two-way burden.
- **Connects to:** [Skin](../../06-organ/skin/README.md) — failing kidneys show on the skin: uremia brings relentless itch and a sallow hue, disturbed calcium-phosphate balance calcifies skin vessels into deadly calciphylaxis, and the skin's vitamin D awaits the kidney's final activating step.
- **Connects to:** [Adrenal Gland](../../06-organ/adrenal-gland/README.md) — the kidney and adrenal run the salt axis together: the kidney's renin triggers the adrenal cortex to release aldosterone, which acts back on the nephron to retain sodium and excrete potassium, closing the loop that sets blood volume and pressure.
- **Connects to:** [Type 2 Diabetes](../type-2-diabetes/README.md) — diabetes is the leading destroyer of the renal system: chronic high glucose thickens and scars the glomerulus into diabetic nephropathy, the single biggest cause of kidney failure and dialysis worldwide.
- **Connects to:** [FGF23](../../03-molecular/fgf23/README.md) — bone signals the kidney about phosphate: FGF23 from bone tells the nephron to dump phosphate and curb active vitamin D, and as kidneys fail FGF23 climbs early, an opening move in the mineral-bone disorder of CKD.
- **Connects to:** [SGLT2](../../03-molecular/sglt2/README.md) — the proximal tubule reclaims the body's sugar: SGLT2 there reabsorbs nearly all filtered glucose, and blocking it spills glucose into the urine — drugs that lower sugar while unexpectedly protecting the kidney and heart.
- **Connects to:** [Fibroblast](../../04-cellular/fibroblast/README.md) — one kidney cell wears two hats: peritubular fibroblasts make the erythropoietin that drives red-cell production, yet when injured they transform into myofibroblasts that lay down the scar of chronic kidney disease.
- **Connects to:** [Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md) — autoimmunity often lands on the kidney: lupus nephritis, where immune complexes inflame the glomeruli, is among the most serious manifestations of SLE and a leading reason the disease becomes life-threatening.
- **Connects to:** [Wilms Tumor](../wilms-tumor/README.md) — the developing kidney can spawn a cancer: Wilms tumor (nephroblastoma) arises from embryonic renal precursor cells, the most common kidney cancer of childhood and the pediatric counterpart to adult renal cell carcinoma.
- **Connects to:** [Sepsis](../sepsis/README.md) — the kidney is both a source and a casualty of sepsis: urinary infection ascending to pyelonephritis can seed urosepsis, while severe sepsis in turn starves the kidneys into acute kidney injury.
- **Connects to:** [Venous Thromboembolism](../venous-thromboembolism/README.md) — leaky kidneys clot the blood: nephrotic syndrome spills anticoagulant proteins into the urine, leaving a hypercoagulable state prone to renal vein thrombosis and pulmonary embolism.
- **Connects to:** [Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md) — its commonest infection ascends from below: uropathogenic E. coli climbs the urinary tract to cause cystitis and pyelonephritis, the renal system's most frequent infection and a leading cause of urosepsis.
- **Connects to:** [Multiple Myeloma](../multiple-myeloma/README.md) — a blood cancer can clog the nephrons: multiple myeloma floods the filtrate with light chains that precipitate into casts, causing myeloma cast nephropathy — a classic route to kidney failure.
- **Connects to:** [Heart Failure](../heart-failure/README.md) — heart and kidney rise and fall together: in cardiorenal syndrome, a failing heart's low output and venous congestion impair renal perfusion, while fluid overload from failing kidneys back-strains the heart.
- **Connects to:** [Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md) — failing kidneys stop making the red-cell hormone: the kidney produces erythropoietin, so as renal function declines, EPO falls and a characteristic renal anemia develops, often needing replacement to correct.
- **Connects to:** [Osteoporosis](../osteoporosis/README.md) — the kidney governs bone mineral balance: as renal function fails, impaired vitamin D activation and phosphate handling disturb calcium balance, producing the renal osteodystrophy and bone fragility of CKD-mineral bone disorder.
- **Connects to:** [Major Depressive Disorder](../major-depressive-disorder/README.md) — kidney failure and dialysis weigh on mood: the fatigue, dietary and fluid restrictions and time burden of dialysis give advanced kidney disease one of the highest rates of depression among chronic illnesses.
- **Connects to:** [Reproductive System](../reproductive-system/README.md) — they share the genitourinary tract: the urinary and reproductive systems develop together and run side by side, so prostatic obstruction, pelvic surgery and pregnancy all directly affect the kidneys and bladder.
- **Connects to:** [Respiratory System](../respiratory-system/README.md) — lungs and kidneys jointly balance acid and can fail together: the kidney and lung co-regulate acid-base status, and pulmonary-renal syndromes like Goodpasture and ANCA vasculitis attack both at once.
- **Connects to:** [Integumentary System](../integumentary-system/README.md) — failing kidneys are written on the skin: uraemia causes intractable pruritus and a sallow complexion, and advanced renal failure can produce calciphylaxis and, with gadolinium, nephrogenic systemic fibrosis.
- **Connects to:** [Musculoskeletal System](../musculoskeletal-system/README.md) — the kidney mineralises the skeleton: by regulating calcium, phosphate and active vitamin D, it keeps bone healthy, so renal failure causes renal osteodystrophy with weak, painful bones and fractures.
- **Connects to:** [Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md) — tuberculosis can seed the urinary tract: genitourinary TB causes sterile pyuria, ureteric strictures and renal scarring, a quiet cause of declining kidney function in endemic regions.
- **Connects to:** [Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md) — common painkillers can injure it: NSAIDs like ibuprofen reduce renal blood flow and can cause acute kidney injury, acute interstitial nephritis and, with chronic use, analgesic nephropathy.
- **Connects to:** [Lymphatic System](../lymphatic-system/README.md) — a hidden network drains it: a rich renal lymphatic system clears interstitial fluid and protein from the kidney, and when overwhelmed it contributes to the oedema of nephrotic syndrome.
- **Connects to:** [Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md) — a common diabetes drug it must clear: metformin is renally excreted and accumulates in kidney failure, risking lactic acidosis, so it is dose-reduced or stopped as eGFR falls.
- **Connects to:** [Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md) — a powerful antibiotic that can harm it: vancomycin is nephrotoxic and renally cleared, so it requires blood-level monitoring and dose adjustment to protect the kidney.
- **Connects to:** [Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md) — a virus that scars the glomerulus: chronic hepatitis B causes membranous nephropathy and polyarteritis-nodosa renal disease through immune-complex deposition, one of several viral causes of kidney disease.
- **Connects to:** [Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md) — infection inflames the kidney: Staphylococcus aureus causes infection-related glomerulonephritis and is a leading organism in dialysis-access infection and septic acute kidney injury.
- **Connects to:** [Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md) — the gut talks to the kidney through diet: dietary fibre shifts the microbiome to produce fewer uraemic toxins like indoxyl sulfate, of interest in slowing chronic kidney disease.
- **Connects to:** [Fibrosis](../../05-tissue/fibrosis/README.md) — scarring is the common endpoint: whatever the initial insult — diabetes, hypertension, glomerulonephritis — progressive kidney disease converges on tubulointerstitial fibrosis, the strongest histological predictor of nephron loss and renal failure.
- **Connects to:** [Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md) — the kidney both clears and is harmed: it excretes many cytotoxic drugs so dosing tracks GFR, while cisplatin, methotrexate and tumour-lysis from chemotherapy are major causes of acute kidney injury.
- **Connects to:** [aHUS](../ahus/README.md) — a renal-limited thrombotic microangiopathy: atypical haemolytic uraemic syndrome, from uncontrolled complement activation, attacks the glomerular and arteriolar endothelium to cause acute kidney injury, treated with the complement inhibitor eculizumab.
- **Connects to:** [Arterial Wall](../../05-tissue/arterial-wall/README.md) — it governs blood pressure through the arteries: the kidney's renin-angiotensin system tunes arterial-wall tone and volume, while renal-artery atherosclerosis or stenosis drives secondary hypertension—a two-way axis between kidney and vessel.
- **Connects to:** [Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md) — a hereditary cause of kidney lesions: tuberous sclerosis studs the kidneys with angiomyolipomas (fat-and-vessel hamartomas that can haemorrhage) and cysts, a leading source of its morbidity treated with mTOR inhibitors.
- **Connects to:** [VHL Disease](../vhl-disease/README.md) — inherited renal cysts and cancer: von Hippel-Lindau disease fills the kidneys with cysts and multiple clear cell renal cell carcinomas, the leading cause of death in VHL and a model of hereditary kidney cancer.
- **Connects to:** [ANCA Vasculitis](../anca-vasculitis/README.md) — crescentic glomerulonephritis: ANCA-associated vasculitis is a leading cause of rapidly progressive glomerulonephritis, its pauci-immune necrotising injury destroying nephrons within weeks unless promptly treated.
- **Connects to:** [Sickle Cell Disease](../sickle-cell-disease/README.md) — sickle nephropathy: sickle cell disease injures the kidney through medullary papillary necrosis, impaired urine concentration and a FSGS-like glomerulopathy, a common path to chronic kidney disease.
- **Connects to:** [COVID-19](../covid-19-disease/README.md) — acute kidney injury and collapsing GN: COVID-19 frequently causes acute kidney injury in severe disease and, in those with high-risk APOL1 variants, a collapsing glomerulopathy.
- **Connects to:** [Atherosclerosis](../atherosclerosis/README.md) — cardiorenal calcification: chronic kidney disease accelerates atherosclerosis through uraemia, calcium-phosphate dysregulation and FGF23, making cardiovascular disease the leading cause of death in renal patients.
- **Connects to:** [Sjögren's Syndrome](../sjogrens-syndrome/README.md) — autoimmune tubular disease: Sjögren's syndrome attacks the kidney as tubulointerstitial nephritis and distal renal tubular acidosis, a tubular pattern distinct from the glomerular injury of lupus nephritis.
- **Connects to:** [Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md) — potassium and the heartbeat: the kidney's control of potassium ties it to the cardiac conduction system, where the hyperkalaemia of renal failure peaks the T wave and can stop the heart.
- **Connects to:** [Nitric Oxide](../../03-molecular/nitric-oxide/README.md) — renal blood flow: endothelial nitric oxide dilates the afferent arteriole and tunes glomerular pressure, and its loss in renal disease promotes hypertension and progressive injury.
- **Connects to:** [Endothelin-1](../../03-molecular/endothelin-1/README.md) — vasoconstrictor counterweight: endothelin-1 constricts renal vessels and drives sodium retention and fibrosis, making endothelin antagonism a target in proteinuric kidney disease.
- **Connects to:** [TGF-β](../../03-molecular/tgf-beta/README.md) — fibrosis master switch: TGF-β drives the tubulointerstitial fibrosis and glomerulosclerosis that are the common final pathway of chronic kidney disease progression.
- **Connects to:** [VEGF](../../03-molecular/vegf/README.md) — filtration-barrier maintenance: podocyte-derived VEGF sustains the fenestrated glomerular endothelium, which is why anti-VEGF cancer therapy causes proteinuria, hypertension and thrombotic microangiopathy.
- **Connects to:** [Complement C3](../../03-molecular/complement-c3/README.md) — glomerular complement: C3 and the alternative pathway drive immune injury in glomerulonephritis and C3 glomerulopathy, a major mechanism of kidney damage targeted by emerging complement inhibitors.
- **Connects to:** [BNP](../../03-molecular/bnp/README.md) — natriuretic counter-regulation: natriuretic peptides like BNP act on the kidney to promote sodium and water excretion, opposing the renin-angiotensin system in the cardiorenal control of volume.
- **Connects to:** [Prostaglandins](../../03-molecular/prostaglandins/README.md) — renal hemodynamics: prostaglandins (PGE2, prostacyclin) dilate the afferent arteriole and stimulate renin release to protect renal blood flow under stress, which is why NSAIDs that block them precipitate acute kidney injury.
- **Connects to:** [Adenosine](../../03-molecular/adenosine/README.md) — tubuloglomerular feedback: adenosine released at the macula densa in response to high tubular sodium constricts the afferent arteriole through A1 receptors, the feedback loop that stabilises single-nephron GFR.
- **Connects to:** [Bradykinin](../../03-molecular/bradykinin/README.md) — kallikrein-kinin balance: the renal kallikrein-kinin system generates bradykinin that promotes vasodilation and natriuresis, a counter-regulatory arm to angiotensin II in the kidney's control of blood pressure and volume.
- **Connects to:** [Calcium](../../02-atomic/calcium/README.md) — mineral homeostasis: the kidney is central to calcium balance, filtering it and reabsorbing it under PTH and vitamin-D control through channels like TRPV5 in the distal tubule, linking renal function to bone health and the disturbances of chronic kidney disease.
- **Connects to:** [Dopamine](../../03-molecular/dopamine/README.md) — intrarenal natriuresis: locally produced dopamine acts on proximal-tubule D1 receptors to inhibit sodium reabsorption and promote its excretion, an intrarenal natriuretic system that helps regulate blood pressure independent of the systemic circulation.
- **Connects to:** [GLP-1](../../03-molecular/glp-1/README.md) — metabolic renoprotection: GLP-1 receptor agonists exert direct renal effects that reduce albuminuria and slow the decline of kidney function in diabetic kidney disease, linking the incretin axis to renal outcomes.
- **Connects to:** [HIF-1alpha](../../03-molecular/hif-1alpha/README.md) — oxygen sensing: the kidney is the body's oxygen sensor, where peritubular cells stabilize HIF in hypoxia to produce the erythropoietin already mapped, the axis exploited by HIF-prolyl-hydroxylase inhibitors to treat renal anemia.
- **Connects to:** [Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md) — development and fibrosis: Wnt/β-catenin signaling patterns nephron development and, when pathologically reactivated, drives the tubulointerstitial fibrosis that is the final common pathway of chronic kidney disease.
- **Connects to:** [NOTCH](../../03-molecular/notch/README.md) — nephron patterning: NOTCH signaling directs nephron-progenitor differentiation and podocyte specification during kidney development, and its reactivation contributes to glomerular disease.
- **Connects to:** [SMAD4](../../03-molecular/smad4/README.md) — fibrosis effector: TGF-β signaling through SMAD4 (TGF-β mapped) activates myofibroblasts to lay down the tubulointerstitial fibrosis that is the final common pathway of chronic kidney disease.
- **Connects to:** [mTOR](../../03-molecular/mtor/README.md) — tubular growth and cysts: mTOR governs tubular-cell and podocyte size, and its dysregulation drives the cyst growth of polycystic kidney disease and the hypertrophy of diabetic nephropathy.
- **Connects to:** [NRF2](../../03-molecular/nfe2l2/README.md) — antioxidant defense: NRF2 protects the kidney against oxidative injury, and pharmacological NRF2 activation (bardoxolone) raises filtration rate in chronic kidney disease.
- **Connects to:** [AKT](../../03-molecular/akt/README.md) — cell survival and growth: PI3K-AKT signaling maintains podocyte and tubular-cell survival and mediates the hypertrophic responses central to renal physiology and disease.
- **Connects to:** [NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md) — sterile inflammation: the NLRP3 inflammasome links metabolic and crystalline injury to the tubulointerstitial inflammation and fibrosis of chronic kidney disease.
- **Connects to:** [Galectin-3](../../03-molecular/galectin-3/README.md) — fibrosis biomarker: galectin-3 drives renal interstitial fibrosis and marks progressive kidney disease, complementing the TGF-β/SMAD4 fibrotic axis already mapped.
- **Connects to:** [STAT3](../../03-molecular/stat3/README.md) — inflammatory fibrosis: IL-6-STAT3 signaling drives tubulointerstitial inflammation and the fibrotic progression shared across chronic kidney diseases.
- **Connects to:** [cGAS-STING](../../03-molecular/cgas-sting/README.md) — tubular DNA sensing: cytosolic DNA sensing through cGAS-STING links tubular cell injury to the sterile inflammation of acute kidney injury and progressive renal disease.
- **Connects to:** [PDGF](../../03-molecular/pdgf/README.md) — mesangial proliferation: PDGF signaling drives mesangial and interstitial fibroblast proliferation, a core mechanism of glomerulosclerosis and renal fibrosis.
- **Connects to:** [FOXO](../../03-molecular/foxo/README.md) — podocyte stress defense: FOXO transcription factors regulate podocyte and tubular-cell oxidative-stress defense and metabolic homeostasis across the renal system.
- **Connects to:** [STAT1](../../03-molecular/stat1/README.md) — immune renal inflammation: IFN-STAT1 signaling shapes the immune-mediated glomerular and tubulointerstitial inflammation of renal disorders.
- **Connects to:** [ERK1/2](../../03-molecular/erk1-2/README.md) — proliferation and fibrosis: ERK-MAPK signaling downstream of growth factors and angiotensin II (PDGF and angiotensin-II already mapped) drives mesangial and tubular proliferation and fibrosis in the renal system.
- **Connects to:** [GSK-3β](../../03-molecular/gsk-3b/README.md) — nephron homeostasis: GSK-3β, within the Wnt/β-catenin signaling that governs nephron development and repair (Wnt already mapped), regulates the tubular and podocyte homeostasis of the renal system.
- **Connects to:** [PIK3CA](../../03-molecular/pik3ca/README.md) — tubular growth and survival: PI3K (PIK3CA)-AKT signaling (AKT already mapped) governs the growth, survival, and metabolic homeostasis of the renal tubular epithelium.
- **Connects to:** [S100A8/A9](../../03-molecular/s100a8-a9/README.md) — tubulointerstitial inflammation: S100A8/A9 alarmins participate in the inflammatory signaling of tubulointerstitial injury in the renal system.
- **Connects to:** [AMPK](../../03-molecular/ampk/README.md) — tubular energy sensing: AMPK integrates the high energy demand of tubular transport, coupling the metabolism of the renal system to its reabsorptive function.
- **Connects to:** [NF-κB](../../03-molecular/nf-kb/README.md) — tubulointerstitial inflammation: NF-κB inflammatory signaling participates in the tubulointerstitial inflammation and injury responses of the renal system.
- **Connects to:** [Autophagy](../../03-molecular/autophagy/README.md) — podocyte homeostasis: Autophagy maintains the podocyte and tubular-cell homeostasis and stress resilience of the renal system.
- **Connects to:** [SRC Kinase](../../03-molecular/src-kinase/README.md) — podocyte and tubular signaling: SRC-family kinase signaling participates in the podocyte, tubular-epithelial, and growth-factor responses of the renal system.
- **Connects to:** [DNMT3A](../../03-molecular/dnmt3a/README.md) — epigenetic regulation: DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the nephron development and tubular gene expression of the renal system.
- **Connects to:** [CCR5](../../03-molecular/ccr5/README.md) — renal immune recruitment: CCR5-driven leukocyte recruitment participates in the renal immune surveillance and inflammatory responses of the renal system.
- **Connects to:** [CXCL12](../../03-molecular/cxcl12/README.md) — renal development: CXCL12-CXCR4 signaling participates in the renal development and immune-cell trafficking of the renal system.
- **Connects to:** [Interleukin-6](../../03-molecular/il-6/README.md) — renal inflammation: IL-6 signaling participates in the renal inflammatory responses of the renal system.
- **Connects to:** [IL-1β](../../03-molecular/il-1b/README.md) — inflammasome injury: IL-1β-driven inflammation participates in the renal inflammatory responses of the renal system.
- **Connects to:** [Proton](../../01-subatomic/proton/README.md) — acid-base balance: the kidney maintains systemic pH by secreting protons and regenerating bicarbonate in the tubules, and its failure to excrete fixed acid produces the metabolic acidosis characteristic of renal disease.
- **Connects to:** [Insulin](../../03-molecular/insulin/README.md) — metabolic role: the kidney clears insulin and contributes to gluconeogenesis, so renal failure both prolongs insulin action, risking hypoglycaemia, and induces the insulin resistance that accompanies chronic kidney disease.
- **Connects to:** [Hepcidin](../../03-molecular/hepcidin/README.md) — renal anaemia: the kidney produces erythropoietin (already mapped) and its disease raises hepcidin through inflammation and reduced clearance, restricting iron availability and driving the anaemia of chronic kidney disease.
- **Connects to:** [Smooth muscle cell](../../04-cellular/smooth-muscle-cell/README.md) — vascular tone control: smooth muscle in the afferent and efferent arterioles and the mesangium sets glomerular filtration pressure under RAAS and sympathetic control (angiotensin II already mapped), the microvascular regulation central to renal function.
- **Connects to:** [Macrophage](../../04-cellular/macrophage/README.md) — interstitial inflammation: infiltrating macrophages drive the tubulointerstitial inflammation and fibrosis (TGF-beta already mapped) that determine progression of chronic kidney disease, a key immune contributor to renal scarring.
- **Connects to:** [Hemoglobin](../../03-molecular/hemoglobin/README.md) — renal anaemia: falling erythropoietin (already mapped) production by the diseased kidney lowers haemoglobin, the renal anaemia treated with erythropoiesis-stimulating agents and, more recently, HIF stabilisers.
- **Connects to:** [Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md) — urate handling: the kidney excretes most of the body's uric acid produced by xanthine oxidase, and impaired renal excretion causes hyperuricaemia and gout, while urate crystals and stones in turn injure the kidney.
- **Connects to:** [Iron](../../02-atomic/iron/README.md) — iron balance and anaemia: the kidney's failing erythropoietin (already mapped) and the raised hepcidin (already mapped) of chronic kidney disease disturb iron availability, producing an iron-restricted renal anaemia managed with iron and erythropoiesis-stimulating agents.
- **Connects to:** [TNF-alpha](../../03-molecular/tnf-alpha/README.md) — renal inflammation: TNF and the inflammatory cytokines (IL-6 and IL-1 already mapped) drive the interstitial inflammation and fibrosis (TGF-beta already mapped) of progressive kidney disease, a target of anti-inflammatory approaches to slow renal decline.
- **Connects to:** [Chloride](../../02-atomic/chloride/README.md) — chloride transport: chloride is co-transported with sodium (already mapped) by the NKCC2 and NCC transporters that loop and thiazide diuretics block, and its handling underlies the kidney's control of volume and acid-base balance.
- **Connects to:** [Magnesium](../../02-atomic/magnesium/README.md) — magnesium handling: the kidney is the principal regulator of magnesium, reabsorbing it in the loop and distal tubule, and renal wasting (as with loop diuretics or Gitelman syndrome) causes the hypomagnesaemia of renal disease.
- **Connects to:** [Adrenal gland](../adrenal-gland/README.md) — the adrenal-renal axis: the adrenal gland's aldosterone (already mapped) acts on the distal nephron to reabsorb sodium and excrete potassium (already mapped), closing the renin-angiotensin-aldosterone loop that the kidney initiates.
- **Connects to:** [IL-4](../../03-molecular/il-4/README.md) — type-2 repair and fibrosis: IL-4 drives the M2 macrophages (already mapped) and the type-2 immunity involved in the renal repair and, when dysregulated, the interstitial fibrosis (TGF-β already mapped) of chronic kidney disease.
- **Connects to:** [IL-13](../../03-molecular/il-13/README.md) — profibrotic type-2 cytokine: IL-13, with IL-4 (already mapped), is a profibrotic type-2 cytokine that contributes to the renal interstitial fibrosis (TGF-β already mapped) driving the progression of chronic kidney disease.
- **Connects to:** [Leptin](../../03-molecular/leptin/README.md) — renal adipokine clearance: leptin is cleared by the renal system and accumulates in renal failure, contributing to the cachexia, sympathetic activation and cardiovascular risk of chronic kidney disease.
- **Connects to:** [Adiponectin](../../03-molecular/adiponectin/README.md) — uraemic adipokine: adiponectin, with leptin (already mapped), is cleared by and accumulates in the renal failure, part of the uraemic metabolic-cardiovascular milieu of the renal system.
- **Connects to:** [Resistin](../../03-molecular/resistin/README.md) — uraemic inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), accumulates in the renal failure and contributes to the uraemic inflammatory-metabolic milieu of the renal system.
- **Connects to:** [T-helper cell](../../04-cellular/t-helper-cell/README.md) — immune nephritis: the CD4 T-helper cells drive the immune glomerular and tubulointerstitial nephritis of the renal system, mediating the immune kidney injury.
- **Connects to:** [B cell](../../04-cellular/b-cell/README.md) — humoral nephritis: the B cells, with the T-helper cells (already mapped), drive the autoantibody and immune-complex glomerulonephritis of the renal system, the rituximab (anti-CD20) target.
- **Connects to:** [Plasma cell](../../04-cellular/plasma-cell/README.md) — autoantibody plasma cells: the plasma cells secrete the autoantibodies (anti-GBM, immune-complex) that deposit in the glomerulus and drive the immune kidney injury of the renal system.
- **Connects to:** [Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md) — renal tolerance: the regulatory T cells restrain the immune nephritis (T-helper cells already mapped) and maintain the tolerance of the renal system.
- **Connects to:** [IFN-gamma](../../03-molecular/ifn-gamma/README.md) — Th1 nephritis: the IFN-γ of the infiltrating T cells is the type-II interferon arm driving the crescentic and lupus nephritides of the renal system.
- **Connects to:** [IL-12](../../03-molecular/il-12/README.md) — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune nephritis of the renal system.
- **Connects to:** [IL-17A](../../03-molecular/il-17a/README.md) — Th17 nephritis: IL-17A drives the Th17 arm of the ANCA-associated and crescentic glomerulonephritides of the renal system.
- **Connects to:** [IL-23](../../03-molecular/il-23/README.md) — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the crescentic and ANCA-associated glomerulonephritides of the renal system.
- **Connects to:** [IL-33](../../03-molecular/il-33/README.md) — epithelial alarmin: IL-33, released by the injured tubular and endothelial cells, activates the ILC2s and shapes the type-2 (IL-4 and IL-13 already mapped) response and the fibrosis of the renal system.
- **Connects to:** [IgE](../../03-molecular/ige/README.md) — type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension (the allergic interstitial nephritis and minimal-change disease) of the renal system.
- **Connects to:** [Complement C5](../../03-molecular/complement-c5/README.md) — terminal complement: the complement C5 and its C5a (with C3 already mapped) generate the membrane-attack complex central to the membranous nephropathy and the complement-mediated glomerular injury of the renal system.
- **Connects to:** [C5aR1](../../03-molecular/c5ar1/README.md) — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid recruitment of the glomerulonephritis and the ANCA vasculitis of the renal system.
- **Connects to:** [Factor H](../../03-molecular/factor-h/README.md) — complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation causes the C3 glomerulopathy and atypical HUS of the renal system.
- **Treated by:** ACE inhibitors — renoprotection in CKD.
- **Treated by:** Loop diuretics — fluid management.

## Pathology

### Chronic Kidney Disease (CKD)

CKD affects ~850 million people worldwide — about 10% of the global adult population [^vanholder-2017-ckd-costs]. It is defined by GFR <60 mL/min/1.73 m² or markers of kidney damage for ≥3 months [^kdigo-2012-ckd].

**Systemic complications of advanced CKD (GFR <30 mL/min):**
- **Anemia** (EPO deficiency) → fatigue, dyspnea on exertion
- **Hypertension** (renin excess, volume overload) → cardiovascular risk
- **Metabolic acidosis** (reduced acid excretion capacity) → muscle wasting, bone disease
- **Hyperkalemia** (impaired K⁺ excretion) → arrhythmia risk
- **Renal osteodystrophy** (low calcitriol → secondary HPT → high PTH → bone turnover)
- **Uremia** (retention of urea, uremic toxins) → pericarditis, encephalopathy, platelet dysfunction
- **ESRD (GFR <15 mL/min)** → renal replacement therapy: hemodialysis, peritoneal dialysis, or transplant

### Acute Kidney Injury (AKI)

Sudden-onset rise in creatinine (≥0.3 mg/dL in 48h or ≥1.5× baseline in 7 days) or oliguria. Major causes: prerenal (60-70%), intrinsic (25-40%), postrenal (5-10%). COVID-19 AKI up to 30% of ICU patients.

### Urinary Tract Infections (UTI) and Pyelonephritis

Ascending bacterial infection (>80% *E. coli*): cystitis (bladder), pyelonephritis (kidney parenchyma). Predisposing factors: female anatomy, urinary obstruction, vesicoureteral reflux, immunosuppression, diabetes, catheterization.

### Nephrolithiasis

Most common urological condition in adults (~10% lifetime prevalence). Calcium oxalate (75%), uric acid (10%), struvite (5-10%), cystine (1%). Predisposing: dehydration, hypercalciuria, hyperoxaluria, low urine volume, anatomical abnormalities.

### Bladder Cancer

Predominantly urothelial (transitional cell) carcinoma. Most common risk factor: cigarette smoking. Other: occupational aromatic amine exposure, cyclophosphamide, chronic UTI (squamous cell), schistosomiasis.

### Polycystic Kidney Disease

ADPKD (PKD1/PKD2): autosomal dominant, progressive cyst growth in both kidneys → progressive renal failure by median age 55-70 depending on gene. Complication: hypertension (RAAS activation), intracranial aneurysms, liver cysts.

[^hall-guyton-14]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 26-32.
[^vanholder-2017-ckd-costs]: Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care. *Nat Rev Nephrol.* 2017;13(7):393-409. [doi:10.1038/nrneph.2017.63](https://doi.org/10.1038/nrneph.2017.63) · [PubMed 28479604](https://pubmed.ncbi.nlm.nih.gov/28479604/)
[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for CKD. *Kidney Int Suppl.* 2013;3(1):1-150. [kdigo.org](https://kdigo.org/guidelines/ckd-evaluation-and-management/)
[^openstax-anatomy-ch25]: OpenStax. *Anatomy & Physiology 2e*, Ch. 25: The Urinary System. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/25-introduction)
