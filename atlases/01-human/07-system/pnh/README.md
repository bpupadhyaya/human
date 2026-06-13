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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hillmen-2004-eculizumab-pnh]: Hillmen P, Hall C, Marsh JC, et al. Effect of eculizumab on hemolysis and transfusion requirements in patients with paroxysmal nocturnal hemoglobinuria. *N Engl J Med.* 2004;350(6):552-559. [doi:10.1056/NEJMoa031688](https://doi.org/10.1056/NEJMoa031688) · [PubMed 14762182](https://pubmed.ncbi.nlm.nih.gov/14762182/)
[^brodsky-2008-eculizumab-triumph]: Brodsky RA, Young NS, Antonioli E, et al. Multicenter phase 3 study of the complement inhibitor eculizumab for the treatment of patients with paroxysmal nocturnal hemoglobinuria. *Blood.* 2008;111(4):1840-1847. [doi:10.1182/blood-2007-06-094136](https://doi.org/10.1182/blood-2007-06-094136) · [PubMed 18055865](https://pubmed.ncbi.nlm.nih.gov/18055865/)
