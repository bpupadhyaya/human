---
schema: human-scale-entry/v1
id: cystic-fibrosis
name: Cystic Fibrosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Cystic fibrosis is caused by biallelic CFTR mutations; defective chloride and bicarbonate transport → viscous mucus → progressive bronchiectasis, chronic Pseudomonas infection, and exocrine pancreatic insufficiency; median survival >40 years with CFTR modulator therapy."
aliases: ["cystic fibrosis", "CF", "CFTR disease", "CF lung disease", "CF bronchiectasis", "CF pancreatic insufficiency", "CF-related diabetes", "CFTR mutation disease", "mucoviscidosis", "cystic fibrosis Trikafta"]
sources:
  - id: riordan-1989-cftr-cloning
    type: peer-reviewed
    cite: "Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. Science. 1989;245(4922):1066-1073."
    doi: "10.1126/science.2475911"
    pmid: "2475911"
    url: "https://doi.org/10.1126/science.2475911"
  - id: heijerman-2019-etd-cf
    type: peer-reviewed
    cite: "Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation. Lancet. 2019;394(10212):1940-1948."
    doi: "10.1016/S0140-6736(19)32597-8"
    pmid: "31679946"
    url: "https://doi.org/10.1016/S0140-6736(19)32597-8"
cross_links:
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients."
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CF airway dominated by massive neutrophil recruitment (IL-8-driven); neutrophil elastase → proteolysis → bronchiectasis; NETs provide extracellular DNA that increases sputum viscoelasticity; dornase alfa (DNase I) cleaves NET-derived DNA → improved mucus clearance."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "NLRP3 inflammasome activation in CF airway → IL-1β/IL-18 release → amplifies airway inflammation; CFTR LOF → oxidative stress → NLRP3 priming; IL-1β drives CXCL8 production by airway epithelium → neutrophil recruitment loop; canakinumab (anti-IL-1β) explored as CF lung adjunct."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "CFTR mutations (5T, R117H) are second-hit modifiers in hereditary pancreatitis (PRSS1/SPINK1 mutations); compound heterozygosity → idiopathic chronic pancreatitis; CFTR LOF → reduced pancreatic duct bicarbonate → trypsinogen aggregation and premature activation → acinar injury."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Cystic fibrosis is at root a chloride-transport disease: CFTR is an apical chloride channel, so its loss leaves epithelia unable to move chloride and water, dehydrating secretions into thick mucus — and the same defect raises sweat chloride above 60 mmol/L, the diagnostic test."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung carries most of cystic fibrosis's morbidity: dehydrated mucus cripples mucociliary clearance, inviting chronic Pseudomonas and Staph infection and neutrophilic inflammation that scars airways into bronchiectasis — historically the leading cause of CF death."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Staphylococcus aureus is typically the first chronic airway colonizer in cystic fibrosis, dominating childhood before Pseudomonas takes over in adolescence; persistent S. aureus feeds the neutrophilic inflammation that drives early bronchiectasis."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is a major target of cystic fibrosis: thick CFTR-deficient secretions plug pancreatic ducts → autodigestion and fibrosis → exocrine insufficiency (malabsorption, steatorrhea needing enzyme replacement) and, as islets are destroyed, CF-related diabetes."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Cystic fibrosis and COPD are both chronic obstructive, neutrophil-driven airway diseases with mucus plugging and infective exacerbations, but differ in cause: CF is a monogenic CFTR channel defect from birth, COPD an acquired (usually smoking-driven) disease of later life."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Cystic fibrosis-related diabetes is the commonest CF comorbidity in adults: progressive destruction of pancreatic islets by the same ductal disease that causes exocrine failure produces an insulin-deficient diabetes distinct from type 1 and type 2, worsening lung function."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The respiratory system bears the lethal burden of cystic fibrosis: defective CFTR chloride transport thickens airway mucus, causing impaired clearance, chronic infection, bronchiectasis, and respiratory failure—the leading cause of death, now eased by CFTR modulators."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Cystic fibrosis disrupts the entire digestive system: thick secretions block pancreatic ducts causing exocrine insufficiency and malabsorption, plug the bowel as meconium ileus in newborns, and thicken bile—so enzyme replacement and nutrition are central to CF care."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cystic fibrosis usually causes male infertility: nearly all men with CF have congenital bilateral absence of the vas deferens from CFTR dysfunction, so they are azoospermic despite normal sperm production—and isolated CBAVD can be the only sign of mild CFTR mutations."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium transport is deranged in cystic fibrosis: defective CFTR not only blocks chloride exit but unleashes excess sodium and water absorption, dehydrating airway mucus—and the resulting high sweat sodium chloride is the basis of the diagnostic sweat test."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Aspergillus colonizes the cystic fibrosis airway: the thick mucus lets Aspergillus fumigatus grow, and the hypersensitivity response (ABPA) causes wheezing, mucus plugging and lung decline—so CF care monitors for and treats this fungal complication."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a CF target organ: thick bile from defective CFTR blocks small bile ducts, causing focal biliary cirrhosis and, in some, progressive CF liver disease with portal hypertension—a leading non-pulmonary cause of death in cystic fibrosis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Cystic fibrosis obstructs the small intestine with thick secretions: newborns can present with meconium ileus, and older patients suffer distal intestinal obstruction syndrome, while impaired pancreatic enzyme flow causes the fat malabsorption central to CF."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "CF-related diabetes is a common endocrine complication: thick secretions scar the pancreas and destroy insulin-producing islets, so a distinct form of diabetes emerges with age—now a leading comorbidity as CF patients live longer."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Cystic fibrosis weakens bone: malabsorption of vitamin D and calcium, chronic inflammation, steroids and delayed puberty cause CF-related low bone density, so fractures and osteoporosis are an increasingly important problem in the aging CF population."
---

# Cystic Fibrosis

## Overview

**Cystic fibrosis (CF)** is the most common life-shortening **autosomal recessive genetic disease** in European ancestry populations, affecting approximately 1 in 2,500 live births in Northern Europe and ~1 in 3,500 in the United States (~40,000 Americans, ~100,000 worldwide). CF is caused by biallelic loss-of-function mutations in **CFTR** (cystic fibrosis transmembrane conductance regulator; chromosome 7q31.2), an ATP-gated apical chloride and bicarbonate channel expressed in epithelial cells of the airways, pancreatic and biliary ducts, intestine, sweat glands, and reproductive tract. CFTR dysfunction impairs ion and fluid transport across these epithelia → thick, dehydrated, viscous secretions → luminal obstruction, chronic infection, and progressive organ destruction. CF was first described as a distinct clinical entity by Dorothy Andersen in 1938; CFTR was identified by positional cloning in 1989 [^riordan-1989-cftr-cloning].

CF is a **multi-system disease** dominated by lung pathology: mucociliary clearance failure → chronic bacterial infection (Pseudomonas aeruginosa, Staphylococcus aureus, Haemophilus influenzae) → neutrophilic airway inflammation → progressive bronchiectasis → respiratory failure. The exocrine pancreas is destroyed in ~85% of CF patients (pancreatic insufficiency → malabsorption, fat-soluble vitamin deficiency, growth failure), and ~40-50% of adults develop **CF-related diabetes (CFRD)** — a unique form of insulin deficiency from progressive β-cell loss. The **F508del** mutation (Phe508 deletion in CFTR NBD1) accounts for ~70% of CF alleles worldwide and causes protein misfolding with ER retention. The approval of **elexacaftor/tezacaftor/ivacaftor (Trikafta)** in 2019 — a triple combination that corrects F508del misfolding and potentiates channel gating — has transformed CF: ppFEV1 improved ~14 percentage points, exacerbation rates fell ~63%, and projected median survival has increased from ~40 years to potentially >50 years [^heijerman-2019-etd-cf].

**CF epidemiology by ancestry:**

| Ancestry | Carrier frequency | Disease incidence |
|---|---|---|
| Northern European | ~1/25 | ~1/2,500 |
| Ashkenazi Jewish | ~1/25-29 | ~1/3,200 |
| Hispanic | ~1/46 | ~1/8,500 |
| African-American | ~1/65 | ~1/17,000 |
| Asian | ~1/90+ | ~1/32,000+ |

## Structure

### Genetic basis of cystic fibrosis

**CFTR mutation spectrum:**
- Over 2,000 CFTR variants identified; ClinVar and CFTR2 database classify for clinical significance
- **F508del** (c.1521_1523delCTT; p.Phe508del): ~70% of all CF alleles worldwide; causes Class II defect (protein misfolded → ER retained → degraded before surface); most severe lung phenotype class
- **G551D**: ~3-5% of CF alleles; Class III gating mutation (protein reaches surface but channel gate stuck shut); responsive to ivacaftor monotherapy; historically worst FEV1 outcomes
- **W1282X**, **G542X**: common truncating (nonsense) mutations; Class I (no protein produced); not responsive to current modulators; ataluren/ELX-02 targeting these
- **R117H**: Class IV (reduced conductance); phenotype varies widely from male infertility/CBAVD only to mild CF; R117H with 5T poly-T tract → classic CF; with 7T → CBAVD only; with 9T → carrier without disease
- **2789+5G→A**, **3849+10kbC→T**: Class V splice mutations; reduced but present CFTR function; generally milder CF
- **Genotype-phenotype correlation**:
  - Pancreatic insufficiency/sufficiency: strongly correlated (Class I/II → PI; Class IV/V/R117H → PS)
  - Lung function: poorly correlated with genotype — predominantly determined by modifier genes, infection history, adherence, and environmental factors
  - CFRD: risk ~40-50% regardless of CFTR genotype class

**CFTR2 database and modifier genetics:**
- CFTR2 database (cftr2.org): clinical outcome data for >40,000 CF patients linked to CFTR variants; used for pathogenicity classification
- **Modifier genes** significantly influence CF lung disease severity:
  - TGF-β1 promoter (high-expression genotypes → worse lung disease; lower response to modulators)
  - MBL2 (mannose-binding lectin): low-MBL genotypes → worse P. aeruginosa outcomes
  - IFRD1, SLC26A9: associated with lung function variation
  - CXCR1/2: IL-8 receptor polymorphisms → differential neutrophil trafficking in CF airways

**Carrier screening:**
- ACMG/ACOG recommend universal carrier screening for CF in all pregnancies
- 23-mutation ACMG panel detects ~90% of CF alleles in Northern European ancestry; expanded panels (80-320 mutations) increase sensitivity to >99%
- Carrier couples (both partners positive): 25% chance of affected offspring; prenatal diagnosis by CVS or amniocentesis; PGT available

**Neonatal screening:**
- Most US states and many countries: immunoreactive trypsinogen (IRT, elevated in CF newborns) → if elevated → CFTR mutation panel; 2-tiered IRT/DNA protocol identifies >95% of CF newborns
- Early diagnosis → early pancreatic enzyme replacement → nutritional outcomes markedly improved; early modulator therapy → preserved lung function

## Function

### Clinical features of cystic fibrosis

**Pulmonary disease (dominant cause of morbidity and mortality):**
- **Airway infection**: earliest detectable pathology; S. aureus (MSSA/MRSA) common in childhood; P. aeruginosa (mucoid biofilm phenotype) colonizes in adolescence/adulthood (~40-60% of adults, declining with Trikafta era); Burkholderia cepacia complex (worst prognosis, lung transplant contraindication in some centers); Achromobacter xylosoxidans; NTM (nontuberculous mycobacteria, ~10-15% prevalence)
- **Chronic neutrophilic inflammation**: IL-8-driven massive neutrophil recruitment to airway; neutrophil elastase released → proteolytic damage to airways and epithelia → airway wall destruction; IL-6, IL-1β elevated
- **Bronchiectasis**: progressive permanent dilation and distortion of bronchi; visible on CT from early childhood; leads to air trapping, hyperinflation, reduced FEV1
- Respiratory failure: progressive FEV1 decline; severe CF: FEV1 <30% predicted; respiratory failure from hypercarbia/hypoxemia → lung transplant consideration
- **CF pulmonary exacerbations**: acute worsening of respiratory symptoms (increased cough, sputum, dyspnea, decreased FEV1); treated with IV antibiotics (usually 2-3 week courses) + intensified airway clearance; hospitalized exacerbations → faster FEV1 decline

**Pulmonary management:**
- **CFTR modulators**: F508del homozygotes + eligible heterozygotes → ETD (Trikafta) daily; reduces exacerbations ~63%, improves ppFEV1 ~14 pp, sweat Cl⁻ ↓ ~41 mmol/L; most transformative intervention in CF history
- **Airway clearance therapy (ACT)**: chest physiotherapy, high-frequency chest wall oscillation (ThAIRapy vest), oscillating positive expiratory pressure (Flutter, Aerobika); daily 20-30 min sessions
- **Dornase alfa (Pulmozyme)**: recombinant human DNase I; cleaves extracellular DNA (from neutrophil NETs) in CF sputum → reduces viscoelasticity → easier clearance; ppFEV1 ↑ ~5 pp
- **Hypertonic saline (7%)**: inhaled osmotic agent → draws water onto airway surface → thins mucus; reduces exacerbations ~56%
- **Azithromycin**: 3×/week long-term macrolide → anti-inflammatory + anti-Pseudomonas biofilm effects; reduces exacerbations ~35%; standard therapy for P. aeruginosa-colonized CF
- **Inhaled antibiotics**: tobramycin (TOBI, nebulized or inhaler), aztreonam (Cayston), colistin (inhaled); alternating monthly regimens for chronic P. aeruginosa suppression
- **Lung transplantation**: bilateral lung transplant when FEV1 <30-40% predicted + rapid decline; 5-year survival post-CF lung transplant ~50-55%; CF lower airway disease eliminated but chronic lung allograft dysfunction risk persists

**Gastrointestinal and nutritional disease:**
- **Exocrine pancreatic insufficiency (EPI, ~85%)**: absent lipase/protease/amylase in duodenum → fat malabsorption → steatorrhea, fat-soluble vitamin (A, D, E, K) deficiency, essential fatty acid deficiency → growth failure
- **Pancreatic enzyme replacement therapy (PERT)**: Creon/Zenpep/Pancreaze with all fat-containing meals; dose 1,000-2,500 IU lipase/kg/meal; dramatically improves nutritional outcomes
- **CF-related diabetes (CFRD)**: affects ~40-50% of CF adults; caused by progressive β-cell loss (pancreatic fibrosis, islet disruption) + peripheral insulin resistance; not classic T1DM (autoimmune) or T2DM (primarily insulin resistance); insulin therapy required (not oral hypoglycemics); Hb A1c may underestimate glycemia in CF (increased RBC turnover); CFRD → worsened FEV1 and nutritional status → treat aggressively
- **CF liver disease (CFLD, ~15-20%)**: biliary CFTR LOF → inspissated bile → focal biliary cirrhosis → multilobular cirrhosis in ~5%; portal hypertension, esophageal varices; ursodeoxycholic acid (UDCA) may slow progression; liver transplant in severe CFLD
- **Distal intestinal obstruction syndrome (DIOS)**: impacted fecal material in distal ileum/cecum → acute abdominal pain, vomiting; treated with polyethylene glycol lavage, Gastrografin enema; prevented by adequate hydration and PERT dosing
- **GERD**: highly prevalent in CF; acid aspiration worsens lung disease; treat with PPI + promotility agents

**CF reproductive and musculoskeletal features:**
- Male infertility: CBAVD (congenital bilateral absence of vas deferens) in ~98% of CF males; TESE + ICSI available
- Female fertility: reduced but possible; cervical mucus thicker → reduced sperm penetration; uterus and ovaries normal; pregnancy possible in CF with modulator therapy; Trikafta safe in pregnancy (growing evidence)
- CF-related bone disease (CFBD): osteopenia/osteoporosis from malabsorption (Ca, Vit D), chronic inflammation, GC use, hypogonadism; annual DEXA from age 18; bisphosphonates for established osteoporosis
- CF arthropathy: episodic periarthritis, symmetric non-erosive joint inflammation; HLA-linked predisposition; responds to NSAIDs; not responsive to CF antibiotics
- **Digital clubbing**: present in ~50-70% of CF patients with significant lung disease; correlates with FEV1

### The CFTR modulator era

**Transformative impact of ETD (Trikafta):**
- FDA-approved October 2019 for ages 12+ with ≥1 F508del allele; expanded to ages 2+ (2021)
- Clinical outcomes (Heijerman 2019 Phase 3, F508del homozygotes): ppFEV1 ↑ 14.3 pp (placebo-adjusted); sweat Cl⁻ ↓ 41.8 mmol/L; pulmonary exacerbations ↓ 63%; BMI ↑ 1.04 kg/m²
- Long-term data: continued ppFEV1 improvement at 3-5 years; hospitalization rates ↓ 65%; lung transplant referrals dramatically reduced; fertility improved (female CF patients increasingly conceiving)
- Mutation eligibility: ~90% of CF patients (all F508del homozygotes + heterozygotes with responsive second allele); ~10% not eligible (Class I premature stop mutations, rare class II mutations not responsive to elexacaftor)
- Future pipeline: CFTR mRNA therapy (Translate Bio + Sanofi); gene editing (ex vivo airway stem cell CRISPR; in vivo lipid nanoparticle delivery); next-generation correctors with improved thermostability

## Pathology

### Diagnosis

**Diagnostic criteria (CF Foundation, 2017):**
1. ≥1 characteristic phenotypic feature (chronic sinopulmonary disease, GI/nutritional abnormalities, CBAVD, or elevated sweat electrolytes) OR positive NBS (newborn screen)
AND
2. Evidence of CFTR dysfunction: sweat Cl⁻ ≥60 mmol/L (on 2 separate occasions) OR 2 CF-causing CFTR pathogenic variants in trans OR CFTR transepithelial nasal potential difference (NPD) consistent with CF

**Sweat chloride test:**
- Gibson-Cooke pilocarpine iontophoresis; sweat Cl⁻ ≥60 mmol/L = CF; 30-59 = intermediate (CF possible); <30 = normal
- Most sensitive and specific diagnostic test; must be performed at CF-certified laboratory; minimum sweat volume required (>75 mg)

**Differential diagnosis:**
- Primary ciliary dyskinesia (PCD): recurrent sinopulmonary infections, bronchiectasis, situs inversus; normal sweat Cl⁻; nasal nitric oxide low; electron microscopy of cilia
- Allergic bronchopulmonary aspergillosis (ABPA): CF complication or separate; elevated IgE, Aspergillus-specific IgE, eosinophilia; responds to antifungals + steroids
- Severe combined immunodeficiency (SCID): neonatal; no CF mutations; lymphocyte subset deficiency
- Shwachman-Diamond syndrome (SBDS gene): pancreatic insufficiency + bone marrow failure; normal sweat Cl⁻; neutropenia; SBDS sequencing
- Hirschsprung disease: neonatal bowel obstruction; normal sweat Cl⁻; absent ganglia on biopsy

**Multidisciplinary CF center care:**
- Pulmonology: airway clearance therapy, modulator prescribing, exacerbation management
- Gastroenterology/nutrition: PERT dosing, nutritional optimization, liver disease monitoring, CFRD management
- Endocrinology: CFRD (insulin management), bone disease (DEXA, bisphosphonates)
- Reproductive health: fertility counseling, pregnancy management
- Psychology/social work: CF is a lifelong demanding disease; mental health support integral (depression/anxiety prevalence ~3x general population in CF)
- CF microbiology: specialized sputum culture protocols for CF pathogens (Burkholderia, Pseudomonas susceptibility testing)
- Physiotherapy: ACT technique training and prescription
- Annual assessments: spirometry, CT chest (alternate years), glucose tolerance test, DEXA scan, sputum culture, liver ultrasound, comprehensive labs (vitamins, HbA1c, renal function)

## Connections

- `connects-to` → **[CFTR](../../03-molecular/cftr/README.md)** — Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients.
- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CF airway dominated by massive neutrophil recruitment (IL-8-driven); neutrophil elastase → proteolysis → bronchiectasis; NETs provide extracellular DNA that increases sputum viscoelasticity; dornase alfa (DNase I) cleaves NET-derived DNA → improved mucus clearance.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — NLRP3 inflammasome activation in CF airway → IL-1β/IL-18 release → amplifies airway inflammation; CFTR LOF → oxidative stress → NLRP3 priming; IL-1β drives CXCL8 production by airway epithelium → neutrophil recruitment loop; canakinumab (anti-IL-1β) explored as CF lung adjunct.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — CFTR mutations (5T, R117H) are second-hit modifiers in hereditary pancreatitis (PRSS1/SPINK1 mutations); compound heterozygosity → idiopathic chronic pancreatitis; CFTR LOF → reduced pancreatic duct bicarbonate → trypsinogen aggregation and premature activation → acinar injury.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Cystic fibrosis is at root a chloride-transport disease: CFTR is an apical chloride channel, so its loss leaves epithelia unable to move chloride and water, dehydrating secretions into thick mucus — and the same defect raises sweat chloride above 60 mmol/L, the diagnostic test.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung carries most of cystic fibrosis's morbidity: dehydrated mucus cripples mucociliary clearance, inviting chronic Pseudomonas and Staph infection and neutrophilic inflammation that scars airways into bronchiectasis — historically the leading cause of CF death.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Staphylococcus aureus is typically the first chronic airway colonizer in cystic fibrosis, dominating childhood before Pseudomonas takes over in adolescence; persistent S. aureus feeds the neutrophilic inflammation that drives early bronchiectasis.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is a major target of cystic fibrosis: thick CFTR-deficient secretions plug pancreatic ducts → autodigestion and fibrosis → exocrine insufficiency (malabsorption, steatorrhea needing enzyme replacement) and, as islets are destroyed, CF-related diabetes.
- `connects-to` → **[COPD](../copd/README.md)** — Cystic fibrosis and COPD are both chronic obstructive, neutrophil-driven airway diseases with mucus plugging and infective exacerbations, but differ in cause: CF is a monogenic CFTR channel defect from birth, COPD an acquired (usually smoking-driven) disease of later life.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Cystic fibrosis-related diabetes is the commonest CF comorbidity in adults: progressive destruction of pancreatic islets by the same ductal disease that causes exocrine failure produces an insulin-deficient diabetes distinct from type 1 and type 2, worsening lung function.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — The respiratory system bears the lethal burden of cystic fibrosis: defective CFTR chloride transport thickens airway mucus, causing impaired clearance, chronic infection, bronchiectasis, and respiratory failure—the leading cause of death, now eased by CFTR modulators.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Cystic fibrosis disrupts the entire digestive system: thick secretions block pancreatic ducts causing exocrine insufficiency and malabsorption, plug the bowel as meconium ileus in newborns, and thicken bile—so enzyme replacement and nutrition are central to CF care.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cystic fibrosis usually causes male infertility: nearly all men with CF have congenital bilateral absence of the vas deferens from CFTR dysfunction, so they are azoospermic despite normal sperm production—and isolated CBAVD can be the only sign of mild CFTR mutations.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium transport is deranged in cystic fibrosis: defective CFTR not only blocks chloride exit but unleashes excess sodium and water absorption, dehydrating airway mucus—and the resulting high sweat sodium chloride is the basis of the diagnostic sweat test.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Aspergillus colonizes the cystic fibrosis airway: the thick mucus lets Aspergillus fumigatus grow, and the hypersensitivity response (ABPA) causes wheezing, mucus plugging and lung decline—so CF care monitors for and treats this fungal complication.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a CF target organ: thick bile from defective CFTR blocks small bile ducts, causing focal biliary cirrhosis and, in some, progressive CF liver disease with portal hypertension—a leading non-pulmonary cause of death in cystic fibrosis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Cystic fibrosis obstructs the small intestine with thick secretions: newborns can present with meconium ileus, and older patients suffer distal intestinal obstruction syndrome, while impaired pancreatic enzyme flow causes the fat malabsorption central to CF.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — CF-related diabetes is a common endocrine complication: thick secretions scar the pancreas and destroy insulin-producing islets, so a distinct form of diabetes emerges with age—now a leading comorbidity as CF patients live longer.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Cystic fibrosis weakens bone: malabsorption of vitamin D and calcium, chronic inflammation, steroids and delayed puberty cause CF-related low bone density, so fractures and osteoporosis are an increasingly important problem in the aging CF population.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^riordan-1989-cftr-cloning]: Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. *Science.* 1989;245(4922):1066-1073. [doi:10.1126/science.2475911](https://doi.org/10.1126/science.2475911) · [PubMed 2475911](https://pubmed.ncbi.nlm.nih.gov/2475911/)
[^heijerman-2019-etd-cf]: Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation. *Lancet.* 2019;394(10212):1940-1948. [doi:10.1016/S0140-6736(19)32597-8](https://doi.org/10.1016/S0140-6736(19)32597-8) · [PubMed 31679946](https://pubmed.ncbi.nlm.nih.gov/31679946/)
