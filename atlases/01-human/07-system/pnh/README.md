---
schema: human-scale-entry/v1
id: pnh
name: Paroxysmal Nocturnal Hemoglobinuria
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "PNH is a clonal PIGA disorder of GPI-anchor synthesis; GPI-deficient RBCs lack CD55/CD59 → complement MAC lysis + C5a-driven thrombosis; eculizumab and ravulizumab (anti-C5 mAbs) normalize hemolysis and reduce thrombosis 90%; iptacopan (oral factor B inhibitor) also approved."
aliases: ["PNH", "paroxysmal nocturnal hemoglobinuria", "PIGA mutation", "GPI-anchor deficiency", "CD55/CD59 deficiency", "Marchiafava-Micheli disease"]
sources:
  - id: hillmen-2004-eculizumab-pnh
    type: peer-reviewed
    cite: "Hillmen P, Hall C, Marsh JC, et al. Effect of eculizumab on hemolysis and transfusion requirements in patients with paroxysmal nocturnal hemoglobinuria. N Engl J Med. 2004;350(6):552-559."
    doi: "10.1056/NEJMoa031688"
    pmid: "14762182"
    url: "https://doi.org/10.1056/NEJMoa031688"
  - id: brodsky-2008-eculizumab-triumph
    type: peer-reviewed
    cite: "Brodsky RA, Young NS, Antonioli E, et al. Multicenter phase 3 study of the complement inhibitor eculizumab for the treatment of patients with paroxysmal nocturnal hemoglobinuria. Blood. 2008;111(4):1840-1847."
    doi: "10.1182/blood-2007-06-094136"
    pmid: "18055865"
    url: "https://doi.org/10.1182/blood-2007-06-094136"
cross_links:
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "PIGA-mutant PNH clones lack GPI-anchored CD55/CD59 → terminal complement runs unchecked: C5 convertase → C5a (thrombosis/neutrophil activation) + C5b-9 MAC (hemolysis); eculizumab and ravulizumab (anti-C5) normalize LDH and reduce thrombotic events 90%."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "PNH arises from a single PIGA-mutant HSC in bone marrow; immune-mediated destruction of normal HSCs (aplastic anemia context) allows clonal expansion of GPI-deficient clone; 25-40% of aplastic anemia patients have PNH clones; PNH and AA overlap on a continuum."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "In PNH, uncontrolled terminal complement generates C5a alongside C5b-9 (MAC); C5a engages C5aR1 on GPI-deficient neutrophils → thrombosis; eculizumab blocks C5 → prevents both MAC-mediated hemolysis and C5a–C5aR1 signaling; avacopan (C5aR1 blockade) under investigation in PNH."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Both PNH and aHUS involve alternative complement pathway dysregulation; PNH erythrocytes lack GPI-anchored CD55/CD59 → complement-mediated hemolysis; CFH deficiency drives aHUS endotheliopathy; eculizumab and ravulizumab treat both; iptacopan (Factor B inhibitor) for PNH."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "PNH red cells, made by a PIGA-mutant clone, lack the GPI-anchored complement brakes CD55 and CD59, so the membrane attack complex lyses them → chronic intravascular hemolysis; anti-C5 drugs stop the lysis but C3-opsonized cells may still be cleared extravascularly."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "PNH is among the most thrombophilic diseases — 40-50% of untreated patients clot, classically in the hepatic veins; free hemoglobin scavenges nitric oxide while C5a and the MAC activate platelets, and complement inhibition (not anticoagulation alone) cuts thrombotic events ~90%."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The hepatic and portal veins are the signature thrombosis sites in PNH: Budd-Chiari syndrome presents with abdominal pain, hepatomegaly, and ascites; extravascular clearance of C3-opsonized cells also occurs in the liver."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "PNH and HIT are acquired prothrombotic states driven by cellular activation rather than clotting-factor excess: PNH via complement (C5a, MAC) and nitric-oxide-scavenging free hemoglobin, HIT via anti-PF4 IgG; both clot in unusual sites and resist plain anticoagulation."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "PNH clones frequently arise within bone-marrow-failure syndromes: small GPI-deficient clones occur in many aplastic anemia and hypoplastic MDS patients, where immune attack selects complement-resistant PNH cells; flow cytometry for GPI-anchored proteins is part of the MDS workup."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Complement drives thrombosis in PNH at the platelet surface: lacking GPI-anchored CD55/CD59, platelets are hit by C5a and the membrane-attack complex → activation and aggregation; this, plus nitric-oxide depletion from hemolysis, explains PNH's extreme thrombotic risk."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "PNH and atypical HUS are both complement-driven diseases treated by C5 blockade: PNH loses GPI-anchored regulators (CD55/CD59) on blood cells, while aHUS has dysregulated complement on endothelium—different lesions, both responsive to eculizumab."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "PNH is a key acquired thrombophilia to weigh alongside inherited ones: unlike factor V Leiden or prothrombin mutations, PNH thrombosis is complement- and platelet-driven and strikes unusual sites (hepatic, cerebral veins), so thrombosis with hemolysis warrants PNH testing."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "PNH hemolysis has an extravascular component handled by macrophages: C5 inhibitors stop intravascular lysis but leave C3 fragments coating red cells, which splenic and hepatic macrophages clear, so some patients stay anemic—addressed by newer C3 inhibitors."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "PNH is a disease of unchecked complement: loss of GPI-anchored regulators leaves red cells defenseless against the alternative complement pathway, so C3 and the terminal cascade lyse them—and C5/C3 inhibitors (eculizumab, pegcetacoplan) are the targeted treatment."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "PNH belongs to the bone-marrow-failure spectrum and can evolve clonally: it often arises with aplastic anemia, and the abnormal stem-cell clone can progress to MDS or acute myeloid leukemia—so PNH is monitored as a clonal disorder, not only hemolytic."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "PNH and DIC both cause thrombosis with hemolysis but oppositely: PNH's complement-driven intravascular hemolysis causes unusual-site venous thrombosis with normal clotting times, while DIC consumes clotting factors—distinguishing them guides treatment."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "PNH's intravascular hemolysis releases free hemoglobin that scavenges nitric oxide: the resulting NO depletion causes the disease's smooth-muscle symptoms—dystonia, abdominal pain, esophageal spasm and erectile dysfunction—and adds to its thrombotic risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "PNH damages the kidney over time: chronic intravascular hemolysis spills free hemoglobin into urine, and repeated hemoglobinuria with iron deposition and microthrombi causes progressive chronic kidney disease in a substantial fraction of patients."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "PNH arises where immune attack meets clonal escape: autoimmune marrow failure (as in aplastic anemia) selects for PIGA-mutant stem cells that lack GPI-anchored complement regulators, so the surviving clone is paradoxically vulnerable to complement attack."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "PNH unleashes free hemoglobin: complement rips open red cells, spilling hemoglobin into plasma where it stains the urine dark (hemoglobinuria) and mops up nitric oxide—so the classic morning-dark-urine and the NO-driven symptoms both flow from intravascular hemolysis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "PNH is diagnosed through the neutrophil: the PIGA mutation strips GPI-anchored proteins from all blood cells, so flow cytometry (FLAER) detecting GPI-deficient neutrophils and monocytes—not just red cells—confirms the clone and gauges its size."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Chronic hemolysis in PNH can raise pulmonary pressure: free hemoglobin scavenges nitric oxide, constricting pulmonary vessels, so persistent NO depletion contributes to pulmonary hypertension and the breathlessness of long-standing disease."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "PNH's free hemoglobin strangles smooth muscle: intravascular hemolysis releases hemoglobin that scavenges nitric oxide, so smooth muscle stays contracted—causing the dysphagia, abdominal pain, pulmonary hypertension and erectile dysfunction of the disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "PNH paradoxically causes iron deficiency despite hemolysis: hemoglobin and hemosiderin spill into the urine continuously, draining iron from the body—so a hemolytic anemia ends up needing iron replacement, unlike most where iron is recycled."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The PNH clone thrives by escaping cytotoxic T cells: in aplastic anemia, autoreactive T cells attack GPI-anchored marrow cells, but the GPI-negative PNH clone is invisible to them—so immune attack selects the clone that then expands."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PNH's intravascular hemolysis spills potassium: complement punches holes in unprotected red cells, releasing hemoglobin and potassium into blood and urine—dark morning urine (hemoglobinuria) and electrolyte shifts marking the destruction."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "PNH's leading killer is thrombosis driven by thrombin: complement-activated platelets and free hemoglobin tip the balance toward clotting, generating thrombin that clots odd sites like the hepatic veins (Budd-Chiari)—curbed by complement blockade."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "PNH's clone escapes NK cells too: losing the GPI anchor also strips the stress ligands NK cells use to spot abnormal cells, so the clone is invisible to NK as well as to T cells—reinforcing its survival edge in an attacked marrow."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "PNH also destroys blood in the spleen: once C5 blockers stop the intravascular lysis, red cells coated with complement C3 are instead cleared by spleen and liver macrophages, leaving a residual extravascular anemia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PNH's name points to hydrogen ions: the classic dawn hemoglobinuria was long blamed on the mild acidosis of sleep, the drop in blood pH thought to tip complement into attacking the unprotected red cells overnight."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "PNH clots by inflaming the endothelium: uncontrolled complement and free hemoglobin activate the vessel-lining cells and platelets, driving the unusual-site thromboses—like hepatic-vein Budd-Chiari—that are the disease's chief killer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "PNH is diagnosed by flow cytometry: laser light excites fluorescent tags on blood cells, exposing the clone that has lost its CD55 and CD59 surface shields, the test that confirms the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "PNH clots in dangerous places, including the brain: cerebral venous sinus thrombosis is a feared event of its complement-driven hypercoagulability, sometimes the first sign of the disease."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Free hemoglobin in PNH drives clotting through von Willebrand factor: complement-injured endothelium releases ultralarge multimers that snag platelets, compounding the thrombosis that menaces these patients."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "PNH's flaw is at the membrane's molecular anchor: a faulty PIG-A gene leaves blood cells unable to build the GPI tail that pins CD55 and CD59 to their surface, so without those complement brakes the red cells are torn apart."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "PNH cramps the gut from two directions: free hemoglobin soaks up nitric oxide, throwing intestinal smooth muscle into painful spasm, while clots in the mesenteric and portal veins can starve the bowel of blood."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Scavenged nitric oxide strains the circulation: with free hemoglobin mopping up the gas that relaxes vessels, pulmonary pressures climb and the heart labors, adding cardiovascular risk to PNH's thrombotic burden."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "PNH clots in dangerous places: it is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, making an unexplained CVST a reason to test for the disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Free hemoglobin steals the molecule of erection: by scavenging nitric oxide, PNH's intravascular hemolysis robs the penile vasculature of the relaxant it needs, so erectile dysfunction is a common and telling symptom."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The same nitric-oxide depletion cramps the gut: smooth-muscle dystonia of the esophagus and stomach causes the painful swallowing, abdominal pain, and spasm that flare with each bout of hemolysis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody transformed PNH: eculizumab and ravulizumab, monoclonal antibodies against complement C5, halt the intravascular hemolysis and thrombosis, while flow cytometry using antibodies to the missing GPI-anchored proteins (CD55, CD59) makes the diagnosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "PNH is a top cause of Budd-Chiari: its prothrombotic blood clots the hepatic veins, backing blood up into the liver and congesting and killing hepatocytes, so an unexplained hepatic-vein thrombosis should prompt a PNH test."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Clots can surface in the skin: PNH's thrombophilia reaches unusual sites including the dermal and cerebral veins, and painful skin lesions or necrosis from cutaneous vein thrombosis can be an early, visible warning of the disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic hemolysis wears down the kidneys: years of hemoglobin spilling into the urine deposit iron in the tubules and microthrombi in the vessels, so PNH slowly scars the kidney into chronic kidney disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "PNH bleeds iron into the urine: unlike most hemolysis, which recycles iron, the intravascular destruction sends free hemoglobin out through the kidney, and the steady urinary iron loss can leave the patient paradoxically iron-deficient."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The marrow's drive to replace lost cells: brisk hemolysis and any underlying marrow failure raise erythropoietin demand, and supplementing it can support red-cell production while complement blockade curbs the destruction."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its clots can strike the brain: PNH's hallmark thrombosis favors unusual sites including the cerebral venous sinuses, so stroke from venous or arterial clotting is among the gravest, sometimes presenting, complications."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "It bleeds iron into the urine: chronic intravascular hemolysis spills hemoglobin and hemosiderin into the urine, and the brisk erythropoiesis suppresses hepcidin, yet ongoing urinary iron loss can still drive iron deficiency."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The clone may escape an immune attack: PNH often grows out of immune-mediated marrow failure, where a faltering of regulatory T-cell restraint lets cytotoxic cells destroy normal stem cells while the GPI-deficient clone is spared."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Unchecked complement inflames as it clots: C5a generated by the runaway complement in PNH activates NF-κB in leukocytes and endothelium, amplifying the inflammatory, prothrombotic state behind its dreaded clotting."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Blocking complement opens an infection gap: the anti-C5 drugs eculizumab and ravulizumab that control PNH disable the membrane attack complex, sharply raising the risk of meningococcal infection and sepsis, so vaccination is mandatory."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Its clots favor the liver's veins: PNH is a classic cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver toward cirrhosis and, over years, can give rise to hepatocellular carcinoma."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Free hemoglobin and clots strain the heart: chronic intravascular hemolysis scavenges nitric oxide and, with pulmonary thrombosis, drives pulmonary hypertension and right-heart strain, while severe anemia adds high-output load toward heart failure."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow failure compounds the hemolysis: PNH frequently overlaps with aplastic anemia and bone-marrow failure, so impaired production layers an anemia-of-chronic-disease-like component onto the hemolytic anemia."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relentless fatigue and a chronic threat weigh on mood: the disabling hemolytic fatigue, the looming risk of catastrophic thrombosis and lifelong infusions give PNH a substantial psychological burden and depression."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Its complement-blocking therapy invites meningococcus: eculizumab and ravulizumab cut off the terminal complement needed to kill Neisseria, so meningococcal vaccination and prophylaxis are mandatory before treating PNH."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Complement inhibition lowers defense against encapsulated bacteria: the same terminal-complement blockade that treats PNH also blunts protection against pneumococcus, so vaccination against it precedes therapy."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Its only cure brings transplant risk: allogeneic hematopoietic stem-cell transplantation is the sole curative option for PNH, carrying the hazard of graft-versus-host disease against the recipient's tissues."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clots the gut's veins and cramps its muscle: PNH causes hepatic and mesenteric vein thrombosis (Budd-Chiari) and, from nitric-oxide depletion by free haemoglobin, oesophageal spasm and severe abdominal pain."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can clot the brain's veins: PNH's intense prothrombotic state predisposes to cerebral venous sinus thrombosis, and free-haemoglobin nitric-oxide scavenging drives the disabling headaches it causes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An unpredictable haemolytic, clotting disease breeds worry: the paroxysmal haemolysis, lifelong thrombosis risk and indefinite infusional therapy of PNH foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is visible at the skin and bedside: haemolysis causes jaundice and pallor with dark cola-coloured morning urine, while dermal thrombosis can produce painful purpuric skin lesions and necrosis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its clots can lodge in the lungs: beyond NO-driven pulmonary hypertension, the thrombotic tendency of PNH causes pulmonary embolism with acute breathlessness and chest pain."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It clots arteries as well as veins: although venous thrombosis dominates, PNH also causes arterial events including myocardial infarction and peripheral arterial occlusion."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It is born in the marrow: PNH arises from a clonal PIGA-mutant stem cell in the bone marrow and frequently overlaps marrow failure, while severe haemolytic crises cause bone and abdominal pain."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Free haemoglobin floods the tubules: acute haemolytic crises release haemoglobin that causes acute kidney injury, distinct from the slow haemosiderin scarring of chronic disease."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Its complement-blocking drug invites meningococcus: eculizumab, the mainstay treatment, blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before therapy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Complement inhibitors transformed it: anti-C5 antibodies (eculizumab, ravulizumab) and the anti-C3 agent pegcetacoplan block the complement-mediated haemolysis and thrombosis of PNH."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It springs from failing marrow under immune attack: PNH clones expand from GPI-deficient stem cells that escape the T-cell-mediated marrow destruction of aplastic anaemia, a lymphoid-immune origin."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "Anticoagulation guards against its clots: before complement inhibitors, anticoagulation including warfarin was central to managing the life-threatening venous thrombosis of PNH, still used adjunctively."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Marrow failure links it to cytotoxics: PNH arises against aplastic anaemia and MDS, whose immunosuppressive and chemotherapy regimens — and conditioning for the curative bone-marrow transplant — intersect with its course."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Both unleash free haemoglobin: PNH and sickle cell disease share intravascular haemolysis that releases cell-free haemoglobin, scavenging nitric oxide to cause smooth-muscle dystonia, pulmonary hypertension and thrombosis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It clots the hepatic veins: PNH characteristically causes Budd-Chiari syndrome, where hepatic-vein thrombosis congests the centrilobular zones of the liver lobule, a leading cause of its mortality."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Free haemoglobin scars the kidney: chronic intravascular haemolysis in PNH spills haemoglobin that causes pigment nephropathy and tubular haemosiderosis, driving the chronic kidney disease that shortens survival."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It strips the blood of nitric oxide: free haemoglobin from PNH haemolysis scavenges nitric oxide, causing smooth-muscle dystonia, pulmonary hypertension and the prothrombotic vascular dysfunction central to the disease."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "A differential of haemolytic anaemia: PNH and thrombotic thrombocytopenic purpura both cause intravascular haemolysis—PNH by complement lysis, TTP by microangiopathic shearing—distinguished by flow cytometry, the blood film and ADAMTS13."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "A complement-therapy bridge: the anti-C5 drugs (eculizumab, ravulizumab) that transformed PNH also treat complement-mediated diseases like myasthenia gravis, showing how one pathway links unrelated disorders."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Shared complement blockade: as in PNH, terminal-complement inhibition with eculizumab controls aquaporin-4 neuromyelitis optica, uniting a haemolytic and a neurological disease through the same C5 target."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "A dangerous mix with pregnancy: PNH sharply raises the already high thrombosis risk of pregnancy, threatening placental and maternal veins, so anticoagulation and complement inhibition are intensified throughout."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Acquired thrombophilia differential: like antiphospholipid syndrome, PNH causes thrombosis at unusual sites, so both are screened in unexplained clots—PNH distinguished by the haemolysis driving its hypercoagulability."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "Splanchnic-thrombosis workup: PNH and JAK2-mutant myeloproliferative neoplasms such as essential thrombocythaemia are both routinely sought in Budd-Chiari and portal-vein thrombosis, two clonal causes of unusual-site clots."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Complement and clots collide: COVID-19 activates complement and is prothrombotic, compounding PNH, while patients on the complement inhibitor eculizumab need meningococcal protection against breakthrough infection."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Thrombotic engine: complement activation, NO depletion and platelet activation in PNH create a prothrombotic, fibrinogen-rich state, and thrombosis is the leading cause of death in the disease."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Clonal marrow spectrum: PNH and JAK2-mutant myelofibrosis both arise from clonal haematopoiesis and are sought together in unusual-site thrombosis and marrow-failure workups."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Unusual-site clots: like polycythaemia vera, PNH is a clonal blood disorder routinely screened for in Budd-Chiari and splanchnic-vein thrombosis presentations."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Complement-driven thrombosis: complement attack on GPI-deficient platelets activates them to release PF4 and procoagulant microparticles, a key driver of the thrombosis that is PNH's leading cause of death."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Urinary iron loss: chronic intravascular haemolysis spills haemoglobin into the urine, and the resulting hemosiderinuria depletes body iron despite the haemolysis, often causing iron deficiency in PNH."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Heme as a danger signal: free heme released by intravascular haemolysis acts as a TLR4 agonist, driving sterile inflammation and endothelial activation that compound the thrombo-inflammation of PNH."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immune-escape origin: PNH clones expand under the IFN-γ-driven autoimmune marrow attack of aplastic anaemia, where the GPI-anchor-deficient clone evades a T-cell assault that targets GPI-positive progenitors."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clonal selection: perforin-mediated CD8 T-cell killing of GPI-positive haematopoietic progenitors in the failing marrow gives the GPI-negative PNH clone its survival advantage, linking PNH to aplastic anaemia."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Hypercoagulable state: complement-driven platelet activation and impaired fibrinolysis create the PNH prothrombotic state, against which the anticoagulant protein C pathway is overwhelmed — the basis for thrombosis prophylaxis."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Marrow-failure overlap: PNH arises from a PIGA-mutant clone expanding on a background of bone-marrow failure, and thrombopoietin-receptor agonists like eltrombopag can stimulate trilineage recovery in the aplastic-anaemia/PNH overlap syndromes."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "NET thrombosis: complement-activated neutrophils releasing S100A8/A9 and extracellular traps contribute to the venous thrombosis — often at unusual sites like the hepatic veins — that is the leading cause of death in PNH."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Free-heme inflammation: chronic intravascular haemolysis releases free haem that, as a DAMP signalling through RAGE, sustains a pro-inflammatory, pro-thrombotic vascular state beyond the nitric-oxide scavenging that drives the dystonic symptoms."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Marrow-failure immunity: the bone-marrow failure of PNH, overlapping with aplastic anaemia, involves T-cell and TNF-α-mediated immune attack on haematopoietic stem cells, the autoimmune pressure that selects the GPI-negative clone."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Complement-inflammasome crosstalk: complement C5a (already mapped) and free haem from intravascular haemolysis prime the NLRP3 inflammasome, adding an inflammatory dimension to the thrombosis and tissue injury of PNH."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Haemolytic hypoxia: chronic intravascular haemolysis and anaemia in PNH produce tissue hypoxia that drives HIF-mediated erythropoietin and adaptive responses, part of the systemic burden of the disease."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "NO-depletion dystonia: free haemoglobin from intravascular haemolysis scavenges nitric oxide (mapped), unleashing endothelin-1-driven vasoconstriction that causes the abdominal pain, dysphagia and pulmonary hypertension of PNH."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial thrombosis: complement-mediated endothelial activation releases Ang-2, contributing to the endothelial dysfunction and thrombosis that is the leading cause of death in PNH."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Clonal evolution: PNH arises within a failing, clonal marrow and can progress to myelodysplasia or acute leukaemia, transitions marked by lesions in genes such as RUNX1."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Erythropoietin and thrombopoietin signal through JAK2 (EPO and TPO mapped), the cytokine axis driving erythroid compensation against haemolysis and relevant to the marrow-failure background of PNH."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Sublytic complement attack on PNH cells triggers PI3K-AKT survival and activation signalling in platelets and endothelium, contributing to the prothrombotic state of the disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "C5a acting on C5aR (C5aR1 mapped) engages ERK-MAPK in neutrophils and platelets, amplifying the cellular activation that drives PNH thrombosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the prothrombotic state of paroxysmal nocturnal haemoglobinuria."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within complement-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the thrombosis of PNH."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that accompanies the chronic complement-mediated haemolysis of PNH."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the hematopoietic stem-cell survival that underlies the clonal expansion of the PIGA-mutant clone in PNH."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the immune bone-marrow microenvironment that favors escape of the PNH clone, often on an aplastic-anemia background."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling contributes to the immune marrow-failure background on which the PNH clone preferentially expands."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the platelet-activation and survival signaling relevant to the thrombotic complications of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling supports the clonal expansion of the PIGA-mutant hematopoietic stem cells of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and clonal advantage of the GPI-anchor-deficient clone of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and thrombosis of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the clonal hematopoietic-stem-cell adaptation of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the PIGA-mutant clonal hematopoietic cells of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the thrombo-inflammatory milieu of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation, as part of the clonal hematopoiesis underlying the disorder, participates in the aberrant marrow biology of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the hematopoietic-stem-cell niche interactions relevant to the clonal expansion of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the thromboinflammation of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial and immune activation relevant to paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the immune dysregulation relevant to the associated marrow failure of paroxysmal nocturnal hemoglobinuria."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Clonal immune escape: the leading model of PNH holds that an autoimmune T-cell attack targets GPI-anchored antigens presented on normal stem cells, so the GPI-negative PNH clone escapes MHC-restricted recognition and expands on a marrow-failure background."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell marrow attack: IL-2-driven expansion of the cytotoxic T cells that suppress haematopoiesis in the associated aplastic anaemia (interferon-gamma already mapped) creates the selective pressure under which the GPI-negative PNH clone is favoured."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Thrombosis mechanism: sublytic complement C5b-9 attack on platelets triggers calcium influx that activates them and releases procoagulant microparticles, a calcium-dependent step in the thrombosis that is the leading cause of death in PNH."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Smooth-muscle dystonia: scavenging of nitric oxide (already mapped) by free haemoglobin causes the oesophageal spasm, abdominal pain and dystonia of PNH, symptoms often severe enough to require opioids acting on the mu-opioid receptor."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative haemolysis: chronic intravascular haemolysis releases haem and purines, and xanthine-oxidase-derived reactive oxygen species and uric acid add oxidative stress and hyperuricaemia to the burden of PNH."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory amplification: complement activation in PNH drives IL-6 and other cytokines (TNF already mapped) that sustain an inflammatory, prothrombotic milieu compounding the haemolytic and thrombotic disease."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Thrombosis differential: the thrombosis of PNH occurs with normal ADAMTS13 (von Willebrand factor already mapped), distinguishing its complement-driven mechanism from the thrombotic microangiopathy of thrombotic thrombocytopenic purpura."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Pulmonary hypertension and cardiac strain: the nitric-oxide scavenging (already mapped) of chronic haemolysis and the thromboembolism of PNH raise pulmonary pressures and strain the right heart, and troponin elevation marks the myocardial injury."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 opposes the inflammatory cytokines (IL-6 and TNF already mapped) that the complement activation of PNH drives, part of the immune balance in the inflammatory, prothrombotic milieu of the disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and platelets: the complement-activated platelets (PF4 already mapped) of PNH generate thromboxane to amplify aggregation, part of the eicosanoid contribution to the thrombosis that is the leading cause of death in the disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Immune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6 and TNF already mapped) that the complement activation of PNH drives in its inflammatory milieu."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Platelet zinc and coagulation: zinc released from the complement-activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of PNH."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune balance: IL-13, with IL-4 (already mapped), is part of the anti-inflammatory arm balancing the complement-driven (already mapped) inflammatory milieu of paroxysmal nocturnal haemoglobinuria."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Marrow-failure immunity: the type-I interferon and the T-cell (IFN-γ already mapped) immune attack of the aplastic-anaemia (already mapped) marrow, from which the GPI-deficient PNH clone escapes, drive the clonal expansion of PNH."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Haemolytic hyperkalaemia: the massive intravascular haemolysis (haemoglobin already mapped) of a PNH crisis releases potassium, the hyperkalaemia adding to the metabolic derangement of severe haemolysis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipose adipokine: leptin from the marrow adipose tissue signals within the immune-metabolic milieu of the marrow-failure (aplastic anaemia already mapped) context of PNH."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the PNH marrow microenvironment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu (IL-6 already mapped) of PNH."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune dysregulation of the associated bone-marrow failure of PNH."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of PNH."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune-metabolic milieu of PNH."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 marrow autoimmunity: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated marrow attack (aplastic anaemia already mapped) from which the GPI-negative PNH clone escapes."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) in the autoimmune marrow-failure context from which the PNH clone arises."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Humoral arm: the B cells contribute the antibody (already mapped) and autoimmune dimension of the marrow-failure context (aplastic anaemia already mapped) underlying PNH."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Marrow-failure T cells: the CD4 T-helper cells, alongside the cytotoxic T cells (already mapped), drive the autoimmune attack on the bone marrow (already mapped) that provides the selective advantage for the PNH clone."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral effector: the plasma cells secrete the antibodies (already mapped) of the autoimmune marrow-failure context underlying PNH."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron loss: transferrin, the iron carrier, reflects the disordered iron handling of the chronic intravascular haemolysis and the haemoglobinuria (haemoglobin and hepcidin already mapped) that deplete the body iron in PNH."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems relevant to the complement amplification and thrombosis of PNH."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator of the thromboinflammatory dimension of the intravascular haemolysis and thrombosis of PNH."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Vascular mast cells: the mast cells contribute to the vascular tone and permeability that, with the nitric-oxide (already mapped) depletion of haemolysis, shape the vasculopathy of PNH."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-mast axis: TSLP, released from vascular and mucosal barriers under the haemolytic and complement (C3, C5, C5aR1 already mapped) stress of PNH, activates mast cells (already mapped) and dendritic cells, amplifying the systemic inflammatory response."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-coagulation axis: bradykinin, generated by the contact system activated by complement (C1-esterase inhibitor, C3, C5, C5aR1 and factor H already mapped) in PNH, augments vascular permeability and amplifies the thromboinflammatory vasculopathy of PNH."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell vasodilator: histamine, released from activated mast cells (already mapped) during the complement-driven haemolytic episodes of PNH, further impairs vascular tone alongside nitric-oxide (already mapped) depletion in the vasculopathy of PNH."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow ECM scaffold: periostin, expressed in the bone marrow stroma (already mapped) supporting the expanded PNH clone, modulates the extracellular matrix niche and fibrotic remodelling in the haematopoietic failure of PNH."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian haemolysis modulation: melatonin, via MT1/MT2 receptors on erythrocytes (already mapped) and complement-regulatory cells, influences the nocturnal complement activation surge (C5 and eculizumab target already mapped) that drives the episodic haemolysis of PNH."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine haematopoietic axis: prolactin, acting via PRLR on haematopoietic progenitors (already mapped) and T-helper cells (already mapped), modulates the immune-mediated selection of the GPI-deficient PNH clone in the marrow failure of PNH."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PNH testosterone: testosterone, via androgen receptors on erythrocytes (already mapped), suppresses complement-C5 (already mapped) activation; androgens (danazol) reduce the haemolytic burden by promoting erythropoiesis (erythropoietin already mapped) in PNH."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PNH serotonin: platelet (already mapped) serotonin amplifies the thrombotic risk and vascular inflammation of PNH; 5-HT2 signalling on endothelial cells (already mapped) promotes nitric-oxide (already mapped) scavenging and the haemolytic vascular injury of PNH."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PNH oxytocin: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells, attenuates macrophage (already mapped) NF-κB (already mapped) activation; oxytocin also modulates regulatory T cells (already mapped) to suppress erythrocyte (already mapped) destruction in PNH."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PNH vasopressin: vasopressin, via V2 receptors on endothelial cells (already mapped) and platelets (already mapped), amplifies the thrombotic risk of PNH; vasopressin activates the NF-κB (already mapped) vascular cascade and the complement-C5 (already mapped) haemolytic axis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PNH selenium: selenoprotein P reduces the complement-C5 (already mapped) and NF-κB (already mapped) driven oxidative injury to erythrocytes (already mapped) in PNH; selenium deficiency impairs erythropoiesis (erythropoietin already mapped) and amplifies anaemia severity."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PNH iodine: iodine-dependent thyroid hormones regulate bone-marrow (already mapped) erythropoiesis and erythrocyte (already mapped) mitochondrial function; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and worsens haemolytic anaemia in PNH."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PNH sodium: excess sodium promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the complement-C5 (already mapped) haemolytic cascade of PNH."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PNH magnesium: magnesium, as ATP-synthesis cofactor in erythrocytes (already mapped) and platelets (already mapped), maintains haematopoietic homeostasis; magnesium deficiency amplifies NF-κB (already mapped) and complement-C5 (already mapped) haemolysis in PNH."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PNH copper: copper, as ceruloplasmin cofactor in macrophages (already mapped) and hepatocytes (already mapped), supports iron (already mapped) recycling from haemolysed erythrocytes (already mapped); copper deficiency amplifies the IL-6 (already mapped) cascade of PNH."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PNH phosphorus: phosphorus-dependent ATP in erythrocytes (already mapped) and platelets (already mapped) sustains membrane integrity against complement-C5 (already mapped) haemolysis; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PNH."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PNH chloride: chloride via anion exchangers in erythrocytes (already mapped) maintains osmotic haemoglobin integrity; chloride dysregulation amplifies the complement-C5 (already mapped) haemolysis and NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of PNH."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PNH carbon: carbon as backbone of GPI-anchor proteins and NF-κB (already mapped) in erythrocytes (already mapped) and platelets (already mapped) sustains membrane protection; carbon depletion amplifies complement-C5 (already mapped) and IL-6 (already mapped) cascade of PNH."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PNH nitrogen: nitrogen in amino-acid scaffold of GPI-anchor proteins and complement regulators in erythrocytes (already mapped) sustains membrane protection; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "PNH oxygen: reactive oxygen species from complement-C5 (already mapped) activation in erythrocytes (already mapped) amplify haemolysis; oxygen dysregulation worsens NF-κB (already mapped) and IL-6 (already mapped) inflammatory and thrombotic cascade of PNH."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "PNH sulfur: sulfur in cysteine residues of complement regulators CD55 and CD59 in erythrocytes (already mapped) sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PNH PD-1: PD-1 on T-cells (already mapped) in bone marrow (already mapped) modulates immune-mediated haematopoietic stem-cell suppression; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "PNH GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates thromboinflammatory tone; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) thrombotic cascade of PNH."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "PNH angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives PNH thrombotic tone; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PNH wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates PNH vascular tone; wnt-beta-catenin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "PNH rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes PNH immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "PNH vegf: VEGF from macrophages (already mapped) and endothelial cells (already mapped) drives complement-mediated vascular injury; vegf dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "PNH fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes vascular ECM remodelling in PNH; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "PNH notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates haematopoietic cell fate in PNH; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH."
---

# Paroxysmal Nocturnal Hemoglobinuria

## Overview

**Paroxysmal nocturnal hemoglobinuria (PNH)** is a rare, acquired, clonal disorder of hematopoietic stem cells (HSCs) characterized by chronic intravascular and extravascular hemolysis, life-threatening thromboembolism, and bone marrow failure, all arising from a somatic mutation in the **PIGA (phosphatidylinositol glycan anchor class A)** gene [^hillmen-2004-eculizumab-pnh].

**PIGA** encodes the first enzyme in the **GPI-anchor (glycosylphosphatidylinositol)** biosynthetic pathway. GPI anchors are glycolipid structures embedded in the outer leaflet of the plasma membrane that tether a subset of surface proteins. The two most critical GPI-anchored complement regulators are:
- **CD55 (DAF, decay-accelerating factor):** Accelerates decay of C3/C5 convertases → prevents amplification of C3b deposition and C5 cleavage on host cells
- **CD59 (protectin/MIRL):** Inhibits C9 polymerization → blocks MAC (C5b-9) formation

When PIGA is mutated in an HSC → all progeny cells (RBCs, WBCs, platelets) of that clone lack GPI anchors → no CD55/CD59 → exposed to unregulated terminal complement activation on their surfaces → **intravascular hemolysis** (MAC on RBCs → osmotic lysis) and **thrombosis** (C5a → neutrophil/platelet activation → hypercoagulable state).

**Epidemiology:**
- Prevalence: ~10-16 per million; incidence ~1-2 per million per year; no ethnic or gender predisposition; peak onset 30-40 years
- Median survival was ~10 years pre-eculizumab (thrombosis was the leading cause of death); with complement inhibition, life expectancy approaches that of the general population
- **PNH-AA overlap:** 25-40% of aplastic anemia (AA) patients have detectable PNH clones; immune-mediated destruction of normal HSCs in AA → clonal selection of GPI-deficient cells (which escape T-cell-mediated immune attack via unknown mechanism — possibly reduced CD8⁺ T cell recognition)

## Structure

**GPI anchor biology:**
- GPI anchors are built on phosphatidylinositol on the ER membrane in a sequential 11-step pathway; PIGA catalyzes the first step (N-acetylglucosamine transfer to phosphatidylinositol) → PIGA loss → complete block in GPI synthesis → all downstream GPI-anchored proteins absent from cell surface
- PIGA is X-linked → a single somatic mutation in the single active PIGA allele (males) or the active X allele (females) is sufficient for clone formation
- PNH clone coexists with residual normal (PIGA-wildtype) HSC progeny; clone size (% GPI-negative cells by flow cytometry) varies from <1% (subclinical) to >95% (massive)
- **PNH phenotype by clone size:** Small clones (<10%) usually subclinical; intermediate (10-50%) → hemolysis and thrombosis risk; large (>50%) → overt PNH with high hemolytic rate and thrombosis

**Complement activation in PNH:**
- Alternative pathway (tick-over): Constant low-level spontaneous C3 hydrolysis → C3(H₂O) → factor B binding → factor D cleavage → C3(H₂O)Bb (fluid-phase C3 convertase) → C3b deposition on cell surfaces → amplification by properdin (C3bBb stabilization) → C3bBb (amplification C3 convertase) → more C3b → C5 convertase (C3bBbC3b) → **C5 cleavage**
- On normal cells: CD55 decays C3bBb before significant amplification; CD59 blocks MAC
- On PNH-RBCs: No CD55 → unchecked C3b amplification; no CD59 → MAC pore formation → rapid intravascular lysis
- **Extravascular hemolysis component:** C3b opsonization of PNH-RBCs (not blocked by anti-C5 agents) → macrophage CR1/CR3 recognition in liver/spleen → extravascular hemolysis; explains why ~25-35% of PNH patients have residual anemia even on anti-C5 therapy
- **Paroxysmal nature:** Historically named for episodes of dark morning urine (hemoglobin in urine after nocturnal complement activation → respiratory acidosis → enhanced complement activation); in practice, hemolysis is continuous rather than strictly paroxysmal in most patients

**Thrombosis in PNH:**
- PNH is one of the most thrombophilic disorders known; 40-50% of pre-eculizumab patients experienced thrombotic events; Budd-Chiari syndrome (hepatic vein thrombosis) is a defining manifestation
- Mechanisms: C5a → platelet activation (P-selectin expression) + neutrophil-platelet aggregates; MAC → platelet microvesiculation + procoagulant phosphatidylserine exposure; NO scavenging by free hemoglobin (hemolysis → hemoglobin → plasma → NO consumption → vasoconstriction + platelet aggregation); D-dimer and thrombin-antithrombin complex elevated even in non-thrombotic PNH

## Function

**Clinical manifestations:**

**Anemia and hemolysis:**
- LDH (intravascular hemolysis marker): Elevated 5-20× ULN in untreated PNH; correlates with hemolytic activity; used as primary treatment monitoring biomarker
- Reticulocytosis, ↓haptoglobin, ↑indirect bilirubin, ↑plasma free hemoglobin → dark urine (hemoglobinuria/hemosiderinuria); iron loss in urine → iron deficiency superimposed on hemolytic anemia → compounded anemia
- Ham test (acid hemolysis test) and sucrose lysis test: Historical diagnostic tests; replaced by flow cytometry

**Thrombosis (the dominant cause of morbidity and mortality):**
- Venous: Hepatic vein (Budd-Chiari syndrome, ~10-15%), mesenteric vein, portal vein, cerebral sinuses; Budd-Chiari presents with acute abdominal pain, hepatomegaly, ascites, liver failure
- Arterial: Stroke, MI, peripheral arterial occlusion (~5%)
- Thrombosis can occur despite anticoagulation → eculizumab/ravulizumab is anti-thrombotic (90% reduction in events vs. historical controls)

**Bone marrow failure:**
- 30-40% of PNH patients have features of aplastic anemia (hypocellular marrow, cytopenias); immune suppression treatment of AA (ATG + cyclosporine) can expand PNH clone; allogeneic HSCT is the only curative option for both conditions

**Diagnosis:**
- **High-sensitivity flow cytometry (FLAER assay):** FLAER (fluorescent aerolysin) binds GPI anchors → detects GPI-deficient WBCs (granulocytes, monocytes) ± RBCs; sensitivity: detects clones >0.01%; diagnostic standard (International PNH Interest Group criteria)
- **PNH clone size:** % GPI-deficient granulocytes (more reliable than RBCs due to variable RBC survival) by FLAER; granulocytes ≥10% = clinically significant PNH; granulocytes ≥50% = high hemolytic risk

## Pathology

**Treatment:**

*Complement inhibitors:*

**Eculizumab (Soliris; anti-C5 IgG4; Alexion/AstraZeneca) [^brodsky-2008-eculizumab-triumph]:**
- FDA approved 2007 — first ever PNH therapy; landmark approval based on TRIUMPH trial (N=87) + SHEPHERD extension
- TRIUMPH: LDH normalization 49% vs. 0% placebo; transfusion independence 49% vs. 0%; QoL normalization; 87% reduction in LDH area-under-curve
- Dosing: 600 mg IV Q1W × 4 (loading) → 900 mg Q2W maintenance; requires IV access every 2 weeks
- **Meningococcal vaccination mandatory ≥2 weeks before first dose** (or prophylactic penicillin until 2 weeks post-vaccination); MenACWY + MenB vaccines required; 1000-2000× increased meningococcal risk

**Ravulizumab (Ultomiris; anti-C5 IgG; engineered eculizumab derivative):**
- FDA approved 2018; non-inferior to eculizumab in ALXN1210-PNH-301; Q8W dosing (vs. Q2W eculizumab); preferred for treatment-naive patients
- No breakthrough hemolysis at end of dosing cycle (steady-state C5 suppression); higher trough C5 inhibition vs. eculizumab

**Iptacopan (Fabhalta; oral factor B inhibitor; Novartis):**
- FDA approved December 2023 for PNH (first oral complement inhibitor); targets alternative pathway factor B → blocks C3 convertase → prevents both C5 cleavage (intravascular hemolysis) and C3b opsonization (extravascular hemolysis)
- APPLY-PNH: 82% transfusion independence vs. 2% placebo; hemoglobin rise +2.4 g/dL vs. +0.4; oral QD → no infusion required; preferred for patients unable to access IV therapy

**Crovalimab (Piasky; subcutaneous anti-C5; Roche):**
- FDA approved 2023; 700 mg SC Q4W after loading; self-injection possible; addresses infusion access issues
- COMMODORE 1 and 2: non-inferior to eculizumab for LDH, transfusion independence

*Non-complement therapies:*
- **Anticoagulation:** Warfarin or LMWH for thrombotic events in PNH pre-complement inhibitor era; NOT protective enough alone — complement inhibitor is the mainstay anti-thrombotic
- **Iron supplementation:** Replaces urinary iron loss in hemolytic PNH
- **Folic acid:** Supports erythropoiesis under high hemolytic drive
- **Erythropoiesis-stimulating agents (ESA):** Adjunct in selected patients with anemia
- **Allogeneic HSCT:** Curative for PNH + aplastic anemia; not needed for isolated PNH well-controlled on complement inhibitor (risk/benefit not favored without aplastic anemia)
- **Danicopan (add-on factor D inhibitor):** For extravascular hemolysis breakthrough on anti-C5 agents; oral; FDA approved 2023

## Connections

- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — PIGA-mutant PNH clones lack GPI-anchored CD55/CD59 → terminal complement runs unchecked: C5 convertase → C5a (thrombosis/neutrophil activation) + C5b-9 MAC (hemolysis); eculizumab and ravulizumab (anti-C5) normalize LDH and reduce thrombotic events 90%.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — PNH originates from a single PIGA-mutant hematopoietic stem cell in bone marrow; immune-mediated destruction of normal HSCs (aplastic anemia context) allows clonal expansion of GPI-deficient clone; 25-40% of aplastic anemia patients have PNH clones; PNH and AA overlap on a continuum.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — In PNH, uncontrolled terminal complement generates C5a alongside C5b-9 (MAC); C5a engages C5aR1 on GPI-deficient neutrophils → thrombosis; eculizumab blocks C5 → prevents both MAC-mediated hemolysis and C5a–C5aR1 signaling; avacopan (C5aR1 blockade) under investigation in PNH.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Both PNH and aHUS involve alternative complement pathway dysregulation; PNH erythrocytes lack GPI-anchored CD55/CD59 → complement-mediated hemolysis; CFH deficiency drives aHUS endotheliopathy; eculizumab and ravulizumab treat both; iptacopan (Factor B inhibitor) for PNH.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — PNH red cells, made by a PIGA-mutant clone, lack the GPI-anchored complement brakes CD55 and CD59, so the membrane attack complex lyses them → chronic intravascular hemolysis; anti-C5 drugs stop the lysis but C3-opsonized cells may still be cleared extravascularly.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — PNH is among the most thrombophilic diseases — 40-50% of untreated patients clot, classically in the hepatic veins; free hemoglobin scavenges nitric oxide while C5a and the MAC activate platelets, and complement inhibition (not anticoagulation alone) cuts thrombotic events ~90%.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The hepatic and portal veins are the signature thrombosis sites in PNH: Budd-Chiari syndrome presents with abdominal pain, hepatomegaly, and ascites; extravascular clearance of C3-opsonized cells also occurs in the liver.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — PNH and HIT are acquired prothrombotic states driven by cellular activation rather than clotting-factor excess: PNH via complement (C5a, MAC) and nitric-oxide-scavenging free hemoglobin, HIT via anti-PF4 IgG; both clot in unusual sites and resist plain anticoagulation.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — PNH clones frequently arise within bone-marrow-failure syndromes: small GPI-deficient clones occur in many aplastic anemia and hypoplastic MDS patients, where immune attack selects complement-resistant PNH cells; flow cytometry for GPI-anchored proteins is part of the MDS workup.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Complement drives thrombosis in PNH at the platelet surface: lacking GPI-anchored CD55/CD59, platelets are hit by C5a and the membrane-attack complex → activation and aggregation; this, plus nitric-oxide depletion from hemolysis, explains PNH's extreme thrombotic risk.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — PNH and atypical HUS are both complement-driven diseases treated by C5 blockade: PNH loses GPI-anchored regulators (CD55/CD59) on blood cells, while aHUS has dysregulated complement on endothelium—different lesions, both responsive to eculizumab.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — PNH is a key acquired thrombophilia to weigh alongside inherited ones: unlike factor V Leiden or prothrombin mutations, PNH thrombosis is complement- and platelet-driven and strikes unusual sites (hepatic, cerebral veins), so thrombosis with hemolysis warrants PNH testing.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — PNH hemolysis has an extravascular component handled by macrophages: C5 inhibitors stop intravascular lysis but leave C3 fragments coating red cells, which splenic and hepatic macrophages clear, so some patients stay anemic—addressed by newer C3 inhibitors.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — PNH is a disease of unchecked complement: loss of GPI-anchored regulators leaves red cells defenseless against the alternative complement pathway, so C3 and the terminal cascade lyse them—and C5/C3 inhibitors (eculizumab, pegcetacoplan) are the targeted treatment.
- `connects-to` → **[AML](../aml/README.md)** — PNH belongs to the bone-marrow-failure spectrum and can evolve clonally: it often arises with aplastic anemia, and the abnormal stem-cell clone can progress to MDS or acute myeloid leukemia—so PNH is monitored as a clonal disorder, not only hemolytic.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — PNH and DIC both cause thrombosis with hemolysis but oppositely: PNH's complement-driven intravascular hemolysis causes unusual-site venous thrombosis with normal clotting times, while DIC consumes clotting factors—distinguishing them guides treatment.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — PNH's intravascular hemolysis releases free hemoglobin that scavenges nitric oxide: the resulting NO depletion causes the disease's smooth-muscle symptoms—dystonia, abdominal pain, esophageal spasm and erectile dysfunction—and adds to its thrombotic risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — PNH damages the kidney over time: chronic intravascular hemolysis spills free hemoglobin into urine, and repeated hemoglobinuria with iron deposition and microthrombi causes progressive chronic kidney disease in a substantial fraction of patients.
- `connects-to` → **[Immune System](../immune-system/README.md)** — PNH arises where immune attack meets clonal escape: autoimmune marrow failure (as in aplastic anemia) selects for PIGA-mutant stem cells that lack GPI-anchored complement regulators, so the surviving clone is paradoxically vulnerable to complement attack.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — PNH unleashes free hemoglobin: complement rips open red cells, spilling hemoglobin into plasma where it stains the urine dark (hemoglobinuria) and mops up nitric oxide—so the classic morning-dark-urine and the NO-driven symptoms both flow from intravascular hemolysis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — PNH is diagnosed through the neutrophil: the PIGA mutation strips GPI-anchored proteins from all blood cells, so flow cytometry (FLAER) detecting GPI-deficient neutrophils and monocytes—not just red cells—confirms the clone and gauges its size.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Chronic hemolysis in PNH can raise pulmonary pressure: free hemoglobin scavenges nitric oxide, constricting pulmonary vessels, so persistent NO depletion contributes to pulmonary hypertension and the breathlessness of long-standing disease.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — PNH's free hemoglobin strangles smooth muscle: intravascular hemolysis releases hemoglobin that scavenges nitric oxide, so smooth muscle stays contracted—causing the dysphagia, abdominal pain, pulmonary hypertension and erectile dysfunction of the disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — PNH paradoxically causes iron deficiency despite hemolysis: hemoglobin and hemosiderin spill into the urine continuously, draining iron from the body—so a hemolytic anemia ends up needing iron replacement, unlike most where iron is recycled.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The PNH clone thrives by escaping cytotoxic T cells: in aplastic anemia, autoreactive T cells attack GPI-anchored marrow cells, but the GPI-negative PNH clone is invisible to them—so immune attack selects the clone that then expands.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PNH's intravascular hemolysis spills potassium: complement punches holes in unprotected red cells, releasing hemoglobin and potassium into blood and urine—dark morning urine (hemoglobinuria) and electrolyte shifts marking the destruction.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — PNH's leading killer is thrombosis driven by thrombin: complement-activated platelets and free hemoglobin tip the balance toward clotting, generating thrombin that clots odd sites like the hepatic veins (Budd-Chiari)—curbed by complement blockade.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — PNH's clone escapes NK cells too: losing the GPI anchor also strips the stress ligands NK cells use to spot abnormal cells, so the clone is invisible to NK as well as to T cells—reinforcing its survival edge in an attacked marrow.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — PNH also destroys blood in the spleen: once C5 blockers stop the intravascular lysis, red cells coated with complement C3 are instead cleared by spleen and liver macrophages, leaving a residual extravascular anemia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PNH's name points to hydrogen ions: the classic dawn hemoglobinuria was long blamed on the mild acidosis of sleep, the drop in blood pH thought to tip complement into attacking the unprotected red cells overnight.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — PNH clots by inflaming the endothelium: uncontrolled complement and free hemoglobin activate the vessel-lining cells and platelets, driving the unusual-site thromboses—like hepatic-vein Budd-Chiari—that are the disease's chief killer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — PNH is diagnosed by flow cytometry: laser light excites fluorescent tags on blood cells, exposing the clone that has lost its CD55 and CD59 surface shields, the test that confirms the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — PNH clots in dangerous places, including the brain: cerebral venous sinus thrombosis is a feared event of its complement-driven hypercoagulability, sometimes the first sign of the disease.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Free hemoglobin in PNH drives clotting through von Willebrand factor: complement-injured endothelium releases ultralarge multimers that snag platelets, compounding the thrombosis that menaces these patients.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — PNH's flaw is at the membrane's molecular anchor: a faulty PIG-A gene leaves blood cells unable to build the GPI tail that pins CD55 and CD59 to their surface, so without those complement brakes the red cells are torn apart.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — PNH cramps the gut from two directions: free hemoglobin soaks up nitric oxide, throwing intestinal smooth muscle into painful spasm, while clots in the mesenteric and portal veins can starve the bowel of blood.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Scavenged nitric oxide strains the circulation: with free hemoglobin mopping up the gas that relaxes vessels, pulmonary pressures climb and the heart labors, adding cardiovascular risk to PNH's thrombotic burden.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — PNH clots in dangerous places: it is a leading cause of cerebral venous sinus thrombosis, where backed-up pressure and infarction injure neurons, making an unexplained CVST a reason to test for the disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Free hemoglobin steals the molecule of erection: by scavenging nitric oxide, PNH's intravascular hemolysis robs the penile vasculature of the relaxant it needs, so erectile dysfunction is a common and telling symptom.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The same nitric-oxide depletion cramps the gut: smooth-muscle dystonia of the esophagus and stomach causes the painful swallowing, abdominal pain, and spasm that flare with each bout of hemolysis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody transformed PNH: eculizumab and ravulizumab, monoclonal antibodies against complement C5, halt the intravascular hemolysis and thrombosis, while flow cytometry using antibodies to the missing GPI-anchored proteins (CD55, CD59) makes the diagnosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — PNH is a top cause of Budd-Chiari: its prothrombotic blood clots the hepatic veins, backing blood up into the liver and congesting and killing hepatocytes, so an unexplained hepatic-vein thrombosis should prompt a PNH test.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Clots can surface in the skin: PNH's thrombophilia reaches unusual sites including the dermal and cerebral veins, and painful skin lesions or necrosis from cutaneous vein thrombosis can be an early, visible warning of the disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Chronic hemolysis wears down the kidneys: years of hemoglobin spilling into the urine deposit iron in the tubules and microthrombi in the vessels, so PNH slowly scars the kidney into chronic kidney disease.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — PNH bleeds iron into the urine: unlike most hemolysis, which recycles iron, the intravascular destruction sends free hemoglobin out through the kidney, and the steady urinary iron loss can leave the patient paradoxically iron-deficient.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — The marrow's drive to replace lost cells: brisk hemolysis and any underlying marrow failure raise erythropoietin demand, and supplementing it can support red-cell production while complement blockade curbs the destruction.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its clots can strike the brain: PNH's hallmark thrombosis favors unusual sites including the cerebral venous sinuses, so stroke from venous or arterial clotting is among the gravest, sometimes presenting, complications.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — It bleeds iron into the urine: chronic intravascular hemolysis spills hemoglobin and hemosiderin into the urine, and the brisk erythropoiesis suppresses hepcidin, yet ongoing urinary iron loss can still drive iron deficiency.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The clone may escape an immune attack: PNH often grows out of immune-mediated marrow failure, where a faltering of regulatory T-cell restraint lets cytotoxic cells destroy normal stem cells while the GPI-deficient clone is spared.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Unchecked complement inflames as it clots: C5a generated by the runaway complement in PNH activates NF-κB in leukocytes and endothelium, amplifying the inflammatory, prothrombotic state behind its dreaded clotting.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Blocking complement opens an infection gap: the anti-C5 drugs eculizumab and ravulizumab that control PNH disable the membrane attack complex, sharply raising the risk of meningococcal infection and sepsis, so vaccination is mandatory.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Its clots favor the liver's veins: PNH is a classic cause of Budd-Chiari syndrome, hepatic vein thrombosis that congests the liver toward cirrhosis and, over years, can give rise to hepatocellular carcinoma.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Free hemoglobin and clots strain the heart: chronic intravascular hemolysis scavenges nitric oxide and, with pulmonary thrombosis, drives pulmonary hypertension and right-heart strain, while severe anemia adds high-output load toward heart failure.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow failure compounds the hemolysis: PNH frequently overlaps with aplastic anemia and bone-marrow failure, so impaired production layers an anemia-of-chronic-disease-like component onto the hemolytic anemia.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relentless fatigue and a chronic threat weigh on mood: the disabling hemolytic fatigue, the looming risk of catastrophic thrombosis and lifelong infusions give PNH a substantial psychological burden and depression.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Its complement-blocking therapy invites meningococcus: eculizumab and ravulizumab cut off the terminal complement needed to kill Neisseria, so meningococcal vaccination and prophylaxis are mandatory before treating PNH.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Complement inhibition lowers defense against encapsulated bacteria: the same terminal-complement blockade that treats PNH also blunts protection against pneumococcus, so vaccination against it precedes therapy.
- `connects-to` → **[Graft-versus-Host Disease](../gvhd/README.md)** — Its only cure brings transplant risk: allogeneic hematopoietic stem-cell transplantation is the sole curative option for PNH, carrying the hazard of graft-versus-host disease against the recipient's tissues.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clots the gut's veins and cramps its muscle: PNH causes hepatic and mesenteric vein thrombosis (Budd-Chiari) and, from nitric-oxide depletion by free haemoglobin, oesophageal spasm and severe abdominal pain.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can clot the brain's veins: PNH's intense prothrombotic state predisposes to cerebral venous sinus thrombosis, and free-haemoglobin nitric-oxide scavenging drives the disabling headaches it causes.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An unpredictable haemolytic, clotting disease breeds worry: the paroxysmal haemolysis, lifelong thrombosis risk and indefinite infusional therapy of PNH foster chronic health anxiety alongside depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is visible at the skin and bedside: haemolysis causes jaundice and pallor with dark cola-coloured morning urine, while dermal thrombosis can produce painful purpuric skin lesions and necrosis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its clots can lodge in the lungs: beyond NO-driven pulmonary hypertension, the thrombotic tendency of PNH causes pulmonary embolism with acute breathlessness and chest pain.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It clots arteries as well as veins: although venous thrombosis dominates, PNH also causes arterial events including myocardial infarction and peripheral arterial occlusion.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It is born in the marrow: PNH arises from a clonal PIGA-mutant stem cell in the bone marrow and frequently overlaps marrow failure, while severe haemolytic crises cause bone and abdominal pain.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Free haemoglobin floods the tubules: acute haemolytic crises release haemoglobin that causes acute kidney injury, distinct from the slow haemosiderin scarring of chronic disease.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Its complement-blocking drug invites meningococcus: eculizumab, the mainstay treatment, blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before therapy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Complement inhibitors transformed it: anti-C5 antibodies (eculizumab, ravulizumab) and the anti-C3 agent pegcetacoplan block the complement-mediated haemolysis and thrombosis of PNH.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It springs from failing marrow under immune attack: PNH clones expand from GPI-deficient stem cells that escape the T-cell-mediated marrow destruction of aplastic anaemia, a lymphoid-immune origin.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Anticoagulation guards against its clots: before complement inhibitors, anticoagulation including warfarin was central to managing the life-threatening venous thrombosis of PNH, still used adjunctively.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Marrow failure links it to cytotoxics: PNH arises against aplastic anaemia and MDS, whose immunosuppressive and chemotherapy regimens — and conditioning for the curative bone-marrow transplant — intersect with its course.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Both unleash free haemoglobin: PNH and sickle cell disease share intravascular haemolysis that releases cell-free haemoglobin, scavenging nitric oxide to cause smooth-muscle dystonia, pulmonary hypertension and thrombosis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It clots the hepatic veins: PNH characteristically causes Budd-Chiari syndrome, where hepatic-vein thrombosis congests the centrilobular zones of the liver lobule, a leading cause of its mortality.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Free haemoglobin scars the kidney: chronic intravascular haemolysis in PNH spills haemoglobin that causes pigment nephropathy and tubular haemosiderosis, driving the chronic kidney disease that shortens survival.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It strips the blood of nitric oxide: free haemoglobin from PNH haemolysis scavenges nitric oxide, causing smooth-muscle dystonia, pulmonary hypertension and the prothrombotic vascular dysfunction central to the disease.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — A differential of haemolytic anaemia: PNH and thrombotic thrombocytopenic purpura both cause intravascular haemolysis—PNH by complement lysis, TTP by microangiopathic shearing—distinguished by flow cytometry, the blood film and ADAMTS13.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — A complement-therapy bridge: the anti-C5 drugs (eculizumab, ravulizumab) that transformed PNH also treat complement-mediated diseases like myasthenia gravis, showing how one pathway links unrelated disorders.
- `connects-to` → **[NMO](../nmo/README.md)** — Shared complement blockade: as in PNH, terminal-complement inhibition with eculizumab controls aquaporin-4 neuromyelitis optica, uniting a haemolytic and a neurological disease through the same C5 target.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — A dangerous mix with pregnancy: PNH sharply raises the already high thrombosis risk of pregnancy, threatening placental and maternal veins, so anticoagulation and complement inhibition are intensified throughout.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Acquired thrombophilia differential: like antiphospholipid syndrome, PNH causes thrombosis at unusual sites, so both are screened in unexplained clots—PNH distinguished by the haemolysis driving its hypercoagulability.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — Splanchnic-thrombosis workup: PNH and JAK2-mutant myeloproliferative neoplasms such as essential thrombocythaemia are both routinely sought in Budd-Chiari and portal-vein thrombosis, two clonal causes of unusual-site clots.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Complement and clots collide: COVID-19 activates complement and is prothrombotic, compounding PNH, while patients on the complement inhibitor eculizumab need meningococcal protection against breakthrough infection.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Thrombotic engine: complement activation, NO depletion and platelet activation in PNH create a prothrombotic, fibrinogen-rich state, and thrombosis is the leading cause of death in the disease.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Clonal marrow spectrum: PNH and JAK2-mutant myelofibrosis both arise from clonal haematopoiesis and are sought together in unusual-site thrombosis and marrow-failure workups.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Unusual-site clots: like polycythaemia vera, PNH is a clonal blood disorder routinely screened for in Budd-Chiari and splanchnic-vein thrombosis presentations.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Complement-driven thrombosis: complement attack on GPI-deficient platelets activates them to release PF4 and procoagulant microparticles, a key driver of the thrombosis that is PNH's leading cause of death.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Urinary iron loss: chronic intravascular haemolysis spills haemoglobin into the urine, and the resulting hemosiderinuria depletes body iron despite the haemolysis, often causing iron deficiency in PNH.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Heme as a danger signal: free heme released by intravascular haemolysis acts as a TLR4 agonist, driving sterile inflammation and endothelial activation that compound the thrombo-inflammation of PNH.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — PNH clones expand under the IFN-γ-driven autoimmune marrow attack of aplastic anemia, where the GPI-anchor-deficient clone evades a T-cell assault directed at GPI-positive progenitors—the immune-escape model explaining why PNH and aplastic anemia overlap.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 T-cell killing of GPI-positive hematopoietic progenitors in the failing marrow gives the GPI-negative PNH clone its survival advantage, the cytotoxic mechanism behind the clonal selection that produces PNH.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Complement-driven platelet activation and impaired fibrinolysis create the PNH prothrombotic state against which the anticoagulant protein C pathway is overwhelmed—the rationale for anticoagulation and complement blockade to prevent the thrombosis that kills.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — PNH arises from a PIGA-mutant clone expanding on a background of bone-marrow failure, and thrombopoietin-receptor agonists like eltrombopag can stimulate trilineage recovery in the aplastic-anemia/PNH overlap syndromes.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Complement-activated neutrophils releasing S100A8/A9 and extracellular traps contribute to the venous thrombosis—often at unusual sites like the hepatic veins—that is the leading cause of death in PNH.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Chronic intravascular hemolysis releases free heme that, as a DAMP signaling through RAGE, sustains a pro-inflammatory, pro-thrombotic vascular state beyond the nitric-oxide scavenging that drives the dystonic symptoms.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — The bone-marrow failure of PNH, overlapping with aplastic anemia, involves T-cell and TNF-α-mediated immune attack on hematopoietic stem cells, the autoimmune pressure that selects the GPI-negative clone.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Complement C5a (already mapped) and free heme from intravascular hemolysis prime the NLRP3 inflammasome, adding an inflammatory dimension to the thrombosis and tissue injury of PNH.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Chronic intravascular hemolysis and anemia in PNH produce tissue hypoxia that drives HIF-mediated erythropoietin and adaptive responses, part of the systemic burden of the disease.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Free hemoglobin from intravascular hemolysis scavenges nitric oxide (mapped), unleashing endothelin-1-driven vasoconstriction that causes the abdominal pain, dysphagia and pulmonary hypertension of PNH.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Complement-mediated endothelial activation releases Ang-2, contributing to the endothelial dysfunction and thrombosis that is the leading cause of death in PNH.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — PNH arises within a failing, clonal marrow and can progress to myelodysplasia or acute leukemia, transitions marked by lesions in genes such as RUNX1.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Erythropoietin and thrombopoietin signal through JAK2 (EPO and TPO mapped), the cytokine axis driving erythroid compensation against hemolysis and relevant to the marrow-failure background of PNH.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Sublytic complement attack on PNH cells triggers PI3K-AKT survival and activation signaling in platelets and endothelium, contributing to the prothrombotic state of the disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — C5a acting on C5aR (C5aR1 mapped) engages ERK-MAPK in neutrophils and platelets, amplifying the cellular activation that drives PNH thrombosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the neutrophil-extracellular-trap-driven thromboinflammation that amplifies the prothrombotic state of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within complement-triggered neutrophil extracellular traps engages cGAS-STING, linking NET-driven inflammation to the thrombosis of PNH.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that accompanies the chronic complement-mediated hemolysis of PNH.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates the hematopoietic stem-cell survival that underlies the clonal expansion of the PIGA-mutant clone in PNH.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune bone-marrow microenvironment that favors escape of the PNH clone, often on an aplastic-anemia background.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling contributes to the immune marrow-failure background on which the PNH clone preferentially expands.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the platelet-activation and survival signaling relevant to the thrombotic complications of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling supports the clonal expansion of the PIGA-mutant hematopoietic stem cells of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and clonal advantage of the GPI-anchor-deficient clone of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of platelet and endothelial receptors participates in the platelet activation and thrombosis of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the clonal hematopoietic-stem-cell adaptation of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the PIGA-mutant clonal hematopoietic cells of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the thrombo-inflammatory milieu of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation, as part of the clonal hematopoiesis underlying the disorder, participates in the aberrant marrow biology of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the hematopoietic-stem-cell niche interactions relevant to the clonal expansion of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the thromboinflammation of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial and immune activation relevant to paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the immune dysregulation relevant to the associated marrow failure of paroxysmal nocturnal hemoglobinuria.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Clonal immune escape: the leading model of PNH holds that an autoimmune T-cell attack targets GPI-anchored antigens presented on normal stem cells, so the GPI-negative PNH clone escapes MHC-restricted recognition and expands on a marrow-failure background.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell marrow attack: IL-2-driven expansion of the cytotoxic T cells that suppress haematopoiesis in the associated aplastic anaemia (interferon-gamma already mapped) creates the selective pressure under which the GPI-negative PNH clone is favoured.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Thrombosis mechanism: sublytic complement C5b-9 attack on platelets triggers calcium influx that activates them and releases procoagulant microparticles, a calcium-dependent step in the thrombosis that is the leading cause of death in PNH.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Smooth-muscle dystonia: scavenging of nitric oxide (already mapped) by free haemoglobin causes the oesophageal spasm, abdominal pain and dystonia of PNH, symptoms often severe enough to require opioids acting on the mu-opioid receptor.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative haemolysis: chronic intravascular haemolysis releases haem and purines, and xanthine-oxidase-derived reactive oxygen species and uric acid add oxidative stress and hyperuricaemia to the burden of PNH.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory amplification: complement activation in PNH drives IL-6 and other cytokines (TNF already mapped) that sustain an inflammatory, prothrombotic milieu compounding the haemolytic and thrombotic disease.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Thrombosis differential: the thrombosis of PNH occurs with normal ADAMTS13 (von Willebrand factor already mapped), distinguishing its complement-driven mechanism from the thrombotic microangiopathy of thrombotic thrombocytopenic purpura.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Pulmonary hypertension and cardiac strain: the nitric-oxide scavenging (already mapped) of chronic haemolysis and the thromboembolism of PNH raise pulmonary pressures and strain the right heart, and troponin elevation marks the myocardial injury.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 opposes the inflammatory cytokines (IL-6 and TNF already mapped) that the complement activation of PNH drives, part of the immune balance in the inflammatory, prothrombotic milieu of the disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and platelets: the complement-activated platelets (PF4 already mapped) of PNH generate thromboxane to amplify aggregation, part of the eicosanoid contribution to the thrombosis that is the leading cause of death in the disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Immune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6 and TNF already mapped) that the complement activation of PNH drives in its inflammatory milieu.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Platelet zinc and coagulation: zinc released from the complement-activated platelets (already mapped) promotes the contact pathway and fibrin formation (fibrinogen and thrombin already mapped), adding to the prothrombotic state of PNH.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune balance: IL-13, with IL-4 (already mapped), is part of the anti-inflammatory arm balancing the complement-driven (already mapped) inflammatory milieu of paroxysmal nocturnal haemoglobinuria.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Marrow-failure immunity: the type-I interferon and the T-cell (IFN-γ already mapped) immune attack of the aplastic-anaemia (already mapped) marrow, from which the GPI-deficient PNH clone escapes, drive the clonal expansion of PNH.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Haemolytic hyperkalaemia: the massive intravascular haemolysis (haemoglobin already mapped) of a PNH crisis releases potassium, the hyperkalaemia adding to the metabolic derangement of severe haemolysis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipose adipokine: leptin from the marrow adipose tissue signals within the immune-metabolic milieu of the marrow-failure (aplastic anaemia already mapped) context of PNH.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the PNH marrow microenvironment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu (IL-6 already mapped) of PNH.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune dysregulation of the associated bone-marrow failure of PNH.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of PNH.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune-metabolic milieu of PNH.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 marrow autoimmunity: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-mediated marrow attack (aplastic anaemia already mapped) from which the GPI-negative PNH clone escapes.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) in the autoimmune marrow-failure context from which the PNH clone arises.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Humoral arm: the B cells contribute the antibody (already mapped) and autoimmune dimension of the marrow-failure context (aplastic anaemia already mapped) underlying PNH.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Marrow-failure T cells: the CD4 T-helper cells, alongside the cytotoxic T cells (already mapped), drive the autoimmune attack on the bone marrow (already mapped) that provides the selective advantage for the PNH clone.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral effector: the plasma cells secrete the antibodies (already mapped) of the autoimmune marrow-failure context underlying PNH.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron loss: transferrin, the iron carrier, reflects the disordered iron handling of the chronic intravascular haemolysis and the haemoglobinuria (haemoglobin and hepcidin already mapped) that deplete the body iron in PNH.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement (C3, C5, C5aR1 and factor H already mapped) and the contact-coagulation systems relevant to the complement amplification and thrombosis of PNH.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Thromboinflammation: osteopontin, released by the activated platelets (already mapped), is a matricellular mediator of the thromboinflammatory dimension of the intravascular haemolysis and thrombosis of PNH.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Vascular mast cells: the mast cells contribute to the vascular tone and permeability that, with the nitric-oxide (already mapped) depletion of haemolysis, shape the vasculopathy of PNH.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-mast axis: TSLP, released from vascular and mucosal barriers under the haemolytic and complement (C3, C5, C5aR1 already mapped) stress of PNH, activates mast cells (already mapped) and dendritic cells, amplifying the systemic inflammatory response.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-coagulation axis: bradykinin, generated by the contact system activated by complement (C1-esterase inhibitor, C3, C5, C5aR1 and factor H already mapped) in PNH, augments vascular permeability and amplifies the thromboinflammatory vasculopathy of PNH.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell vasodilator: histamine, released from activated mast cells (already mapped) during the complement-driven haemolytic episodes of PNH, further impairs vascular tone alongside nitric-oxide (already mapped) depletion in the vasculopathy of PNH.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow ECM scaffold: periostin, expressed in the bone marrow stroma (already mapped) supporting the expanded PNH clone, modulates the extracellular matrix niche and fibrotic remodelling in the haematopoietic failure of PNH.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian haemolysis modulation: melatonin, via MT1/MT2 receptors on erythrocytes (already mapped) and complement-regulatory cells, influences the nocturnal complement activation surge (C5 and eculizumab target already mapped) that drives the episodic haemolysis of PNH.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine haematopoietic axis: prolactin, acting via PRLR on haematopoietic progenitors (already mapped) and T-helper cells (already mapped), modulates the immune-mediated selection of the GPI-deficient PNH clone in the marrow failure of PNH.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PNH testosterone: testosterone, via androgen receptors on erythrocytes (already mapped), suppresses complement-C5 (already mapped) activation; androgens (danazol) reduce the haemolytic burden by promoting erythropoiesis (erythropoietin already mapped) in PNH.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PNH serotonin: platelet (already mapped) serotonin amplifies the thrombotic risk and vascular inflammation of PNH; 5-HT2 signalling on endothelial cells (already mapped) promotes nitric-oxide (already mapped) scavenging and the haemolytic vascular injury of PNH.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PNH oxytocin: oxytocin, via OXTR on bone-marrow (already mapped) stromal cells, attenuates macrophage (already mapped) NF-κB (already mapped) activation; oxytocin also modulates regulatory T cells (already mapped) to suppress erythrocyte (already mapped) destruction in PNH.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PNH vasopressin: vasopressin, via V2 receptors on endothelial cells (already mapped) and platelets (already mapped), amplifies the thrombotic risk of PNH; vasopressin activates the NF-κB (already mapped) vascular cascade and the complement-C5 (already mapped) haemolytic axis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PNH selenium: selenoprotein P reduces the complement-C5 (already mapped) and NF-κB (already mapped) driven oxidative injury to erythrocytes (already mapped) in PNH; selenium deficiency impairs erythropoiesis (erythropoietin already mapped) and amplifies anaemia severity.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PNH iodine: iodine-dependent thyroid hormones regulate bone-marrow (already mapped) erythropoiesis and erythrocyte (already mapped) mitochondrial function; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and worsens haemolytic anaemia in PNH.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PNH sodium: excess sodium promotes macrophage (already mapped) and neutrophil (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the complement-C5 (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PNH magnesium: magnesium, as ATP-synthesis cofactor in erythrocytes (already mapped) and platelets (already mapped), maintains haematopoietic homeostasis; magnesium deficiency amplifies NF-κB (already mapped) and complement-C5 (already mapped) haemolysis in PNH.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PNH copper: copper, as ceruloplasmin cofactor in macrophages (already mapped) and hepatocytes (already mapped), supports iron (already mapped) recycling from haemolysed erythrocytes (already mapped); copper deficiency amplifies the IL-6 (already mapped) cascade of PNH.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PNH phosphorus: phosphorus-dependent ATP in erythrocytes (already mapped) and platelets (already mapped) sustains membrane integrity against complement-C5 (already mapped) haemolysis; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PNH.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PNH chloride: chloride via anion exchangers in erythrocytes (already mapped) maintains osmotic haemoglobin integrity; chloride dysregulation amplifies the complement-C5 (already mapped) haemolysis and NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of PNH.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PNH carbon: carbon as backbone of GPI-anchor proteins and NF-κB (already mapped) in erythrocytes (already mapped) and platelets (already mapped) sustains membrane protection; carbon depletion amplifies complement-C5 (already mapped) and IL-6 (already mapped) cascade of PNH.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PNH nitrogen: nitrogen in amino-acid scaffold of GPI-anchor proteins and complement regulators in erythrocytes (already mapped) sustains membrane protection; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — PNH oxygen: reactive oxygen species from complement-C5 (already mapped) activation in erythrocytes (already mapped) amplify haemolysis; oxygen dysregulation worsens NF-κB (already mapped) and IL-6 (already mapped) inflammatory and thrombotic cascade of PNH.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — PNH sulfur: sulfur in cysteine residues of complement regulators CD55 and CD59 in erythrocytes (already mapped) sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PNH PD-1: PD-1 on T-cells (already mapped) in bone marrow (already mapped) modulates immune-mediated haematopoietic stem-cell suppression; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — PNH GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates thromboinflammatory tone; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) thrombotic cascade of PNH.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — PNH angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives PNH thrombotic tone; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PNH wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates PNH vascular tone; wnt-beta-catenin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — PNH rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes PNH immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) thrombotic cascade of PNH.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — PNH vegf: VEGF from macrophages (already mapped) and endothelial cells (already mapped) drives complement-mediated vascular injury; vegf dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — PNH fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes vascular ECM remodelling in PNH; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — PNH notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates haematopoietic cell fate in PNH; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) haemolytic cascade of PNH.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hillmen-2004-eculizumab-pnh]: Hillmen P, Hall C, Marsh JC, et al. Effect of eculizumab on hemolysis and transfusion requirements in patients with paroxysmal nocturnal hemoglobinuria. *N Engl J Med.* 2004;350(6):552-559. [doi:10.1056/NEJMoa031688](https://doi.org/10.1056/NEJMoa031688) · [PubMed 14762182](https://pubmed.ncbi.nlm.nih.gov/14762182/)
[^brodsky-2008-eculizumab-triumph]: Brodsky RA, Young NS, Antonioli E, et al. Multicenter phase 3 study of the complement inhibitor eculizumab for the treatment of patients with paroxysmal nocturnal hemoglobinuria. *Blood.* 2008;111(4):1840-1847. [doi:10.1182/blood-2007-06-094136](https://doi.org/10.1182/blood-2007-06-094136) · [PubMed 18055865](https://pubmed.ncbi.nlm.nih.gov/18055865/)
