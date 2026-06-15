---
schema: human-scale-entry/v1
id: iron-deficiency-anemia
name: Iron Deficiency Anemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Iron deficiency anemia (IDA) is the world's most common nutritional disorder (~2B affected); chronic blood loss, inadequate intake, or malabsorption → depleted iron stores → microcytic hypochromic anemia; treat with ferrous sulfate orally or IV iron carboxymaltose."
aliases: ["IDA", "iron deficiency anemia", "iron deficiency anaemia", "iron-deficiency anemia", "microcytic anemia", "hypochromic anemia", "sideropenic anemia", "nutritional anemia"]
sources:
  - id: camaschella-2015-iron-deficiency
    type: peer-reviewed
    cite: "Camaschella C. Iron-deficiency anemia. N Engl J Med. 2015;372(19):1832-1843."
    doi: "10.1056/NEJMra1401038"
    pmid: "25946282"
    url: "https://doi.org/10.1056/NEJMra1401038"
  - id: who-ferritin-guideline-2020
    type: clinical-guideline
    cite: "World Health Organization. WHO guideline on use of ferritin concentrations to assess iron status in individuals and populations. WHO; 2020."
    url: "https://www.who.int/publications/i/item/9789240000124"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin (SLC40A1) is the basolateral iron exporter on duodenal enterocytes; in IDA, hepcidin falls to near zero → FPN expression maximized → increased duodenal iron absorption and macrophage iron release; FPN is the final gateway of iron delivery to plasma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "In IDA, serum iron falls → apotransferrin rises (TIBC elevated) → TSAT drops <20% → TFR1 upregulated on erythroid progenitors; reticulocyte Hgb (CHr) falls before morphological change; TSAT and ferritin together diagnose and stage iron deficiency."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "IDA suppresses hepcidin to near zero via ERFE from erythroid progenitors and hypoxia signaling; low hepcidin → FPN stabilization → maximal duodenal iron absorption; hepcidin measurement distinguishes IDA (very low) from ACD (elevated) in overlapping cases."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Iron deficiency limits erythropoiesis despite adequate EPO: iron-restricted erythroid progenitors cannot synthesize haem → EPO-resistant microcytic anemia; elevated EPO in IDA reflects compensatory drive; IV iron + ESA combined is more effective than either alone."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "IDA's defining feature is microcytic hypochromic anemia from insufficient haem synthesis; iron depletion → reduced haem → smaller, paler RBCs (↓MCV, ↓MCH); Hgb electrophoresis may show elevated HbA₂ if concurrent β-thalassaemia trait makes IDA appear milder."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency anaemia is, at root, a shortage of the element iron: each haemoglobin tetramer needs four iron atoms, so when absorbed iron (~1-2 mg/day) cannot keep up with loss or demand, stores empty (low ferritin) and haem synthesis stalls, yielding small, pale red cells."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "In a man or postmenopausal woman, unexplained iron deficiency anaemia is colorectal cancer until proven otherwise: a slow-bleeding right-sided tumour drips occult blood into the gut, so guidelines mandate colonoscopy to find the source before treating the anaemia."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "Helicobacter pylori is an under-recognised cause of refractory iron deficiency: chronic gastritis lowers the stomach acid needed to reduce Fe³⁺ for absorption and the bacterium competes for iron, so eradicating H. pylori can reverse a deficiency that resisted oral iron."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "IDA and anemia of chronic disease are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but IDA has low ferritin and high transferrin from true iron lack, while ACD has normal/high ferritin with hepcidin-locked iron; they often coexist."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Iron deficiency starves erythropoiesis of heme: developing red cells undergo extra divisions, producing small (microcytic), pale (hypochromic) erythrocytes with raised red-cell distribution width; the low hemoglobin defines the anemia, and iron repletion restores red-cell size."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Iron-deficiency anemia and thalassemia trait are the classic microcytic-anemia differentials: both lower MCV, but IDA shows low ferritin and high RDW while thalassemia has normal/high iron and raised HbA2—crucially, giving iron to thalassemia trait misdiagnosed as IDA is harmful."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Iron deficiency is the commonest systemic complication of inflammatory bowel disease: chronic gut bleeding plus impaired absorption and inflammation-raised hepcidin deplete iron, so IBD anemia is typically mixed iron-deficiency and chronic-disease anemia, often needing IV iron."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Iron deficiency anemia in an older adult is a red flag for GI malignancy including gastric cancer: chronic occult blood loss from an ulcerating tumor depletes iron, so unexplained iron-deficiency anemia mandates upper and lower endoscopy to exclude gastric or colorectal cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Heavy menstrual bleeding makes iron deficiency anemia the commonest anemia in women of reproductive age: monthly blood loss, plus the iron demands of pregnancy, outpaces dietary intake—so menorrhagia and pregnancy are leading causes of iron deficiency worldwide."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Iron-deficiency anemia and MDS are opposite causes of anemia: IDA is a microcytic anemia from depleted iron that corrects with replacement, while MDS is a clonal marrow-failure anemia with normal or high iron—so iron studies and marrow biopsy distinguish them."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Iron deficiency is common and treatable in chronic kidney disease: both absolute iron loss and functional deficiency from inflammation-driven hepcidin limit erythropoiesis, so IV iron plus erythropoietin-stimulating agents are mainstays of CKD anemia management."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Iron deficiency is a key treatable comorbidity in heart failure—even without anemia: low iron impairs muscle and cardiac energetics, worsening symptoms and outcomes, so intravenous iron improves exercise capacity in iron-deficient HFrEF patients."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Iron deficiency starves the bone marrow's red-cell factory: without iron, erythroblasts cannot make hemoglobin, so the marrow turns out small, pale (microcytic, hypochromic) red cells—the morphologic signature that distinguishes iron-deficiency anemia."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is a key clue in iron-deficiency anemia: in adults, occult bleeding from colonic lesions—especially colorectal cancer—is a leading cause, so unexplained iron deficiency in an older adult mandates colonoscopy to find the source."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Iron-deficiency anemia is often a window into the digestive system: iron is absorbed in the duodenum, so malabsorption (celiac disease, gastric surgery) or chronic GI blood loss commonly causes it—making the gut the first place to investigate."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy strains iron balance through the placenta: the growing fetus and placenta draw heavily on maternal iron, so iron-deficiency anemia is common in pregnancy and, untreated, raises risks of preterm birth and low birth weight—prompting routine supplementation."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Iron deficiency oddly raises the platelet count: lacking iron, the marrow over-produces platelets (reactive thrombocytosis), so an unexplained high platelet count with microcytic anemia points to iron deficiency—and corrects once iron is replaced."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Iron deficiency reaches the nervous system: iron is needed for myelin and neurotransmitter synthesis, so deficiency impairs attention and child development and causes restless legs syndrome—showing anemia harms neurons, not just red cells."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Most of the body's iron comes from macrophages recycling old red cells: they engulf senescent erythrocytes and return the iron via ferroportin, so this recycling—not diet—supplies most daily iron, and its disruption shapes both iron-deficiency and overload."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Iron needs copper to move: copper-dependent enzymes (ceruloplasmin, hephaestin) oxidize iron so transferrin can carry it, so copper deficiency causes an anemia that looks like iron deficiency but won't respond to iron alone."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach gatekeeps iron absorption: acid frees dietary iron for uptake downstream, so atrophic gastritis, H. pylori, acid-blocking drugs or gastric surgery cause iron-deficiency anemia by impairing this first step."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine is where iron deficiency is won or lost: the duodenum absorbs dietary iron, so celiac disease, bypass surgery or fast transit there cuts uptake and is a leading cause of iron-deficiency anemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Iron deficiency ultimately means too little oxygen delivered: without iron, hemoglobin falls and blood carries less oxygen, producing the fatigue, breathlessness and even the odd cravings (pica) that drive patients to seek care."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF senses the iron-oxygen shortfall and ramps up absorption: in the oxygen-starved gut lining, HIF-2alpha switches on the duodenal iron-uptake machinery, so this sensor links low iron and low oxygen to the body's effort to claw iron back."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe iron-deficiency anemia overworks the heart: with too little hemoglobin to carry oxygen, the heart races and pumps harder, so prolonged anemia can enlarge it and tip toward high-output heart failure."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Iron deficiency shows on the surface: pallor, brittle spoon-shaped nails (koilonychia), cracked mouth corners, and a smooth sore tongue are classic outward signs that point to the diagnosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Iron deficiency weakens the immune T cells: iron is needed for lymphocytes to proliferate and function, so deficiency blunts cell-mediated immunity and can leave a person more prone to infection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Unexplained iron deficiency sends doctors looking with light: endoscopy and colonoscopy hunt the gut for a bleeding source, and a marrow iron stain under the microscope confirms depleted stores."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and iron compete for absorption: high doses of one interfere with the other in the gut, so supplements must be balanced lest correcting one mineral deepen deficiency of the other."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Iron enters through the gut lining: the duodenal epithelium absorbs dietary iron, so celiac disease or any damage to this lining causes iron deficiency that no amount of dietary iron can fix."
---

# Iron Deficiency Anemia

## Overview

**Iron deficiency anemia (IDA)** is the most prevalent nutritional deficiency and most common cause of anemia worldwide. The WHO estimates that approximately **2 billion people** — one-quarter of the global population — are affected by anemia, with IDA responsible for ~50% of cases. Globally, IDA contributes substantially to maternal and childhood mortality, impaired cognitive development, reduced work capacity, and adverse pregnancy outcomes [^camaschella-2015-iron-deficiency].

Iron deficiency exists on a spectrum from **depleted stores** (no clinical anemia) to **iron-restricted erythropoiesis** (partial functional deficit) to **frank IDA** (anaemia with characteristic morphological and laboratory changes):

**Stage 1 — Iron depletion:** Bone marrow iron stores absent (Prussian blue stain); serum ferritin falls (<12 ng/mL is diagnostic threshold; <30 ng/mL = probable depletion in inflammatory states); haemoglobin, TSAT, and MCV still normal.

**Stage 2 — Iron-restricted erythropoiesis:** Reticulocyte haemoglobin content (CHr) falls; elevated soluble TFR1 (sTFR); hypochromic reticulocytes; hepcidin falls to near zero; TSAT <20%; haemoglobin begins to decline; MCV still normal or borderline.

**Stage 3 — Frank IDA:** Haemoglobin below reference range; MCV <80 fL (microcytosis); MCH <27 pg (hypochromia); target cells, pencil cells, and anisocytosis on blood smear; TSAT <15%; serum ferritin <12 ng/mL; sTFR high [^who-ferritin-guideline-2020].

**Global epidemiology:**
- Most prevalent in: South Asia, sub-Saharan Africa, parts of Southeast Asia
- Highest-risk groups: premenopausal women (menstrual blood loss), infants and young children (rapid growth + low dietary iron density), pregnant women (dramatically increased demand), adolescent girls
- Estimated 1.2 billion people have IDA specifically (vs. 2 billion with anaemia of any cause)
- Leading cause of years lived with disability (YLDs) among nutritional disorders

## Structure

### Causes and pathophysiology of iron depletion

Iron balance is maintained at ~1–2 mg/day (absorbed = lost). IDA develops when this equilibrium is chronically disrupted:

**A. Chronic blood loss (most common cause in adults):**
- **Gastrointestinal:** peptic ulcer disease, colorectal cancer, colonic polyps, angiodysplasia, NSAIDs/aspirin-induced gastritis, hookworm infection (Necator/Ancylostoma, endemic in tropics)
- **Menstrual:** normal menstruation ~15 mg Fe/cycle; heavy menstrual bleeding (HMB, >80 mL/cycle) → 30-45 mg/cycle → depletes stores within months without dietary compensation
- **Occult GI bleeding:** most important to exclude in men and postmenopausal women — colonoscopy/upper endoscopy mandatory; colorectal cancer and gastric cancer classically present with IDA

**B. Inadequate dietary intake:**
- Strict vegetarian/vegan diets: non-haem plant iron has 5-10% bioavailability vs. 20-30% for haem iron
- Food insecurity, poverty: cereal-dominant diets low in iron-rich foods (meat, fish, legumes)
- Infants: cow's milk formula (low iron) or late introduction of iron-rich foods; human breast milk has low iron content but high bioavailability (~50%); premature infants especially vulnerable (missed third-trimester iron transfer)

**C. Malabsorption:**
- **Coeliac disease:** commonest cause of malabsorption-related IDA in developed countries; villous atrophy in proximal duodenum (highest FPN expression site) → severe IDA often presenting feature of coeliac disease
- **Helicobacter pylori gastritis:** reduces gastric acid (needed to reduce Fe³⁺ → Fe²⁺ for DMT1) and competes for iron; H. pylori eradication can reverse refractory IDA
- **Bariatric surgery:** gastric bypass diverts food past the duodenum → dramatically reduces iron absorption; ~50% of bariatric patients develop IDA within 2 years; IV iron often required indefinitely
- **Inflammatory bowel disease (IBD):** duodenal/jejunal inflammation (Crohn's) reduces absorption; concurrent ACD (hepcidin elevation) compounds deficiency
- **Achlorhydria:** proton pump inhibitor (PPI) long-term use, autoimmune gastritis → reduced Fe³⁺ reduction → impaired absorption

**D. Increased demand:**
- **Pregnancy:** fetal-placental iron requirement ~700 mg per pregnancy; average dietary iron insufficient; all pregnant women require iron supplementation
- **Rapid growth:** infancy, adolescence; increased RBC mass demands outpace intake
- **Intense endurance exercise:** "foot strike" haemolysis; increased GI losses; elevated hepcidin post-exercise transiently reduces absorption
- **Erythropoiesis-stimulating agents (ESA):** rHuEPO dramatically increases erythroid iron demand → functional IDA (iron needs outpace supply even if stores present); requires concurrent IV iron

## Function

### Why iron deficiency causes disease beyond anaemia

Iron is essential for:
1. **Haemoglobin synthesis:** 4 haem groups per tetramer require 4 Fe²⁺; haem synthesis is rate-limited by iron availability → microcytic, hypochromic RBCs
2. **Mitochondrial respiration:** cytochromes (Complex I-IV), Fe-S cluster proteins in the electron transport chain; iron deficiency → mitochondrial dysfunction → fatigue out of proportion to anaemia
3. **Thyroid peroxidase:** TPO requires haem; iron deficiency → impaired T4 synthesis → hypothyroid features may co-exist
4. **Ribonucleotide reductase:** iron-dependent rate-limiting enzyme in DNA synthesis → IDA affects rapidly proliferating cells (gut epithelium, immune cells)
5. **Neurotransmitter synthesis:** monoamine oxidase and tyrosine hydroxylase are iron-dependent → dopamine and serotonin deficiency → cognitive impairment, restless legs syndrome (RLS), mood changes
6. **Phagocyte function:** NADPH oxidase (NOX2) requires iron; IDA → impaired neutrophil oxidative burst → ↑ infection susceptibility

**Non-anaemic symptoms of iron deficiency (Stage 1-2):** Fatigue, cold intolerance, pica (craving for ice/clay/starch — particularly pagophagia/ice craving), koilonychia (spoon nails), angular cheilitis, glossitis, Plummer-Vinson syndrome (oesophageal webs + dysphagia), restless legs syndrome, cognitive impairment, reduced exercise tolerance, hair loss.

## Pathology

### Diagnosis

**Step 1 — Confirm anaemia:** CBC (Hb below gender-specific reference), MCV <80 fL, MCH <27 pg, RDW elevated (anisocytosis). Blood smear: hypochromic microcytes, target cells, pencil cells.

**Step 2 — Iron studies:**

| Test | IDA | ACD | ACD + IDA |
|:-----|:----|:----|:----------|
| Serum ferritin | <12 ng/mL (diagnostic); <30 ng/mL (probable) | ↑ (acute-phase reactant) | Normal (may be falsely normal in inflammation) |
| TSAT | <15-20% | Low-normal | Low |
| TIBC (transferrin) | ↑ | ↓ or normal | Variable |
| Serum iron | ↓ | ↓ | ↓ |
| sTFR (soluble TFR1) | ↑ (>28.1 nmol/L) | Normal | ↑ |
| sTFR/log ferritin index | >2 (IDA likely) | <1 | >2 |
| Reticulocyte Hgb (CHr) | <28 pg | <28 pg | <28 pg |
| Hepcidin | Very low (<3 ng/mL) | Elevated | Intermediate |

**Key diagnostic challenge:** Ferritin is an acute-phase reactant — rises during infection, inflammation, or malignancy even when iron stores are depleted. **Threshold adjustments:** ferritin <30 ng/mL = probable IDA when CRP <5 mg/L; ferritin <70 ng/mL = probable IDA when CRP >5 mg/L (WHO 2020). sTFR/log ferritin ratio (>2 suggests IDA component) is least affected by inflammation.

**Step 3 — Identify the cause:** Occult GI blood loss is mandatory investigation in men and postmenopausal women. Coeliac serology (TTG-IgA, total IgA), H. pylori testing, dietary history, menstrual history. Colonoscopy + OGD for any adult with unexplained IDA — colorectal cancer must be excluded.

### Treatment [^camaschella-2015-iron-deficiency]

**1. Oral iron:**
- **Ferrous sulfate** (65 mg elemental Fe per 325 mg tablet): standard of care; 1-2 tablets daily fasting for maximal absorption; side effects: nausea, constipation, black stools
- **Ferrous fumarate, ferrous gluconate:** lower elemental iron but better tolerability
- **Dosing principle:** Once daily is as effective as twice daily and reduces side effects (hepcidin spike 6-8 h post-dose blunts afternoon dose absorption → alternate days is equally effective)
- **Duration:** 3-6 months after Hb normalizes to replete stores; confirm with repeat ferritin >30 ng/mL

**2. Intravenous iron:**
- **Indications:** Oral iron intolerance; malabsorption (coeliac, bariatric surgery, IBD); ongoing losses exceed oral absorption capacity; pre-operative anaemia optimization; CKD/ESA therapy; pregnancy (2nd/3rd trimester when oral fails)
- **Formulations:**
  - **Ferric carboxymaltose (Ferinject):** 500-1000 mg as single infusion (15 min); minimal anaphylaxis risk; can give 1000 mg dose → fewest infusions; FDA-approved
  - **Iron sucrose (Venofer):** 200 mg per infusion × 3-5 doses; well-tolerated; preferred in dialysis patients
  - **Low-molecular-weight iron dextran:** large doses possible (total dose infusion); higher anaphylaxis rate
  - **Ferric gluconate:** lower dose per infusion; safe; multiple infusions needed
- **Response:** Reticulocytosis within 3-5 days; Hb rise 1-2 g/dL per week; normalize stores within 2-3 months
- **Caution:** Hypophosphataemia after ferric carboxymaltose (FGFR-mediated FGF23 elevation → phosphaturia); monitor serum phosphate; rare anaphylaxis with dextran preparations

**3. Dietary counselling:**
- Increase haem iron: red meat, fish, poultry (20-30% bioavailability)
- Enhance non-haem iron absorption: concurrent vitamin C (ascorbate reduces Fe³⁺ → Fe²⁺)
- Avoid: tea, coffee, calcium supplements, phytates (whole grains, legumes) — all inhibit non-haem iron absorption

**4. Treat the underlying cause:** H. pylori eradication → ~90% Hb improvement in H. pylori-associated IDA; coeliac diet → normalizes duodenal absorption; NSAID/aspirin discontinuation or switch to PPI cover; colonoscopy for polyp/cancer removal.

**Special situations:**
- **Pregnancy:** IV iron ferric carboxymaltose after 12 weeks preferred over oral iron if Hb <9-10 g/dL or intolerance; targets Hb >11 g/dL for delivery
- **IBD:** IV iron preferred (oral worsens bowel disease); ferric carboxymaltose 500-1000 mg initial dose
- **Heart failure:** IV iron improves exercise capacity and quality of life even without anaemia in HF patients with ferritin <100 ng/mL or TSAT <20% (FAIR-HF, AFFIRM-AHF trials)
- **Pre-operative:** Oral or IV iron 4-6 weeks pre-op; IV iron 1-2 weeks pre-op for urgent surgery; targets Hb >13 g/dL males, >12 g/dL females before elective major surgery

## Connections

- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin (SLC40A1) is the basolateral iron exporter on duodenal enterocytes; in IDA, hepcidin falls to near zero → FPN expression maximized → increased duodenal iron absorption and macrophage iron release; FPN is the final gateway of iron delivery to plasma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — In IDA, serum iron falls → apotransferrin rises (TIBC elevated) → TSAT drops <20% → TFR1 upregulated on erythroid progenitors; reticulocyte Hgb (CHr) falls before morphological change; TSAT and ferritin together diagnose and stage iron deficiency.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — IDA suppresses hepcidin to near zero via ERFE from erythroid progenitors and hypoxia signaling; low hepcidin → FPN stabilization → maximal duodenal iron absorption; hepcidin measurement distinguishes IDA (very low) from ACD (elevated) in overlapping cases.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Iron deficiency limits erythropoiesis despite adequate EPO: iron-restricted erythroid progenitors cannot synthesize haem → EPO-resistant microcytic anemia; elevated EPO in IDA reflects compensatory drive; IV iron + ESA combined is more effective than either alone.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — IDA's defining feature is microcytic hypochromic anemia from insufficient haem synthesis; iron depletion → reduced haem → smaller, paler RBCs (↓MCV, ↓MCH); Hgb electrophoresis may show elevated HbA₂ if concurrent β-thalassaemia trait makes IDA appear milder.
- `connects-to` → **[Malaria](../malaria/README.md)** — Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency anaemia is, at root, a shortage of the element iron: each haemoglobin tetramer needs four iron atoms, so when absorbed iron (~1-2 mg/day) cannot keep up with loss or demand, stores empty (low ferritin) and haem synthesis stalls, yielding small, pale red cells.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — In a man or postmenopausal woman, unexplained iron deficiency anaemia is colorectal cancer until proven otherwise: a slow-bleeding right-sided tumour drips occult blood into the gut, so guidelines mandate colonoscopy to find the source before treating the anaemia.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — Helicobacter pylori is an under-recognised cause of refractory iron deficiency: chronic gastritis lowers the stomach acid needed to reduce Fe³⁺ for absorption and the bacterium competes for iron, so eradicating H. pylori can reverse a deficiency that resisted oral iron.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — IDA and anemia of chronic disease are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but IDA has low ferritin and high transferrin from true iron lack, while ACD has normal/high ferritin with hepcidin-locked iron; they often coexist.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Iron deficiency starves erythropoiesis of heme: developing red cells undergo extra divisions, producing small (microcytic), pale (hypochromic) erythrocytes with raised red-cell distribution width; the low hemoglobin defines the anemia, and iron repletion restores red-cell size.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Iron-deficiency anemia and thalassemia trait are the classic microcytic-anemia differentials: both lower MCV, but IDA shows low ferritin and high RDW while thalassemia has normal/high iron and raised HbA2—crucially, giving iron to thalassemia trait misdiagnosed as IDA is harmful.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Iron deficiency is the commonest systemic complication of inflammatory bowel disease: chronic gut bleeding plus impaired absorption and inflammation-raised hepcidin deplete iron, so IBD anemia is typically mixed iron-deficiency and chronic-disease anemia, often needing IV iron.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Iron deficiency anemia in an older adult is a red flag for GI malignancy including gastric cancer: chronic occult blood loss from an ulcerating tumor depletes iron, so unexplained iron-deficiency anemia mandates upper and lower endoscopy to exclude gastric or colorectal cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Heavy menstrual bleeding makes iron deficiency anemia the commonest anemia in women of reproductive age: monthly blood loss, plus the iron demands of pregnancy, outpaces dietary intake—so menorrhagia and pregnancy are leading causes of iron deficiency worldwide.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Iron-deficiency anemia and MDS are opposite causes of anemia: IDA is a microcytic anemia from depleted iron that corrects with replacement, while MDS is a clonal marrow-failure anemia with normal or high iron—so iron studies and marrow biopsy distinguish them.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Iron deficiency is common and treatable in chronic kidney disease: both absolute iron loss and functional deficiency from inflammation-driven hepcidin limit erythropoiesis, so IV iron plus erythropoietin-stimulating agents are mainstays of CKD anemia management.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Iron deficiency is a key treatable comorbidity in heart failure—even without anemia: low iron impairs muscle and cardiac energetics, worsening symptoms and outcomes, so intravenous iron improves exercise capacity in iron-deficient HFrEF patients.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Iron deficiency starves the bone marrow's red-cell factory: without iron, erythroblasts cannot make hemoglobin, so the marrow turns out small, pale (microcytic, hypochromic) red cells—the morphologic signature that distinguishes iron-deficiency anemia.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is a key clue in iron-deficiency anemia: in adults, occult bleeding from colonic lesions—especially colorectal cancer—is a leading cause, so unexplained iron deficiency in an older adult mandates colonoscopy to find the source.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Iron-deficiency anemia is often a window into the digestive system: iron is absorbed in the duodenum, so malabsorption (celiac disease, gastric surgery) or chronic GI blood loss commonly causes it—making the gut the first place to investigate.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy strains iron balance through the placenta: the growing fetus and placenta draw heavily on maternal iron, so iron-deficiency anemia is common in pregnancy and, untreated, raises risks of preterm birth and low birth weight—prompting routine supplementation.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Iron deficiency oddly raises the platelet count: lacking iron, the marrow over-produces platelets (reactive thrombocytosis), so an unexplained high platelet count with microcytic anemia points to iron deficiency—and corrects once iron is replaced.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Iron deficiency reaches the nervous system: iron is needed for myelin and neurotransmitter synthesis, so deficiency impairs attention and child development and causes restless legs syndrome—showing anemia harms neurons, not just red cells.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Most of the body's iron comes from macrophages recycling old red cells: they engulf senescent erythrocytes and return the iron via ferroportin, so this recycling—not diet—supplies most daily iron, and its disruption shapes both iron-deficiency and overload.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Iron needs copper to move: copper-dependent enzymes (ceruloplasmin, hephaestin) oxidize iron so transferrin can carry it, so copper deficiency causes an anemia that looks like iron deficiency but won't respond to iron alone.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach gatekeeps iron absorption: acid frees dietary iron for uptake downstream, so atrophic gastritis, H. pylori, acid-blocking drugs or gastric surgery cause iron-deficiency anemia by impairing this first step.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine is where iron deficiency is won or lost: the duodenum absorbs dietary iron, so celiac disease, bypass surgery or fast transit there cuts uptake and is a leading cause of iron-deficiency anemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Iron deficiency ultimately means too little oxygen delivered: without iron, hemoglobin falls and blood carries less oxygen, producing the fatigue, breathlessness and even the odd cravings (pica) that drive patients to seek care.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF senses the iron-oxygen shortfall and ramps up absorption: in the oxygen-starved gut lining, HIF-2alpha switches on the duodenal iron-uptake machinery, so this sensor links low iron and low oxygen to the body's effort to claw iron back.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe iron-deficiency anemia overworks the heart: with too little hemoglobin to carry oxygen, the heart races and pumps harder, so prolonged anemia can enlarge it and tip toward high-output heart failure.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Iron deficiency shows on the surface: pallor, brittle spoon-shaped nails (koilonychia), cracked mouth corners, and a smooth sore tongue are classic outward signs that point to the diagnosis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Iron deficiency weakens the immune T cells: iron is needed for lymphocytes to proliferate and function, so deficiency blunts cell-mediated immunity and can leave a person more prone to infection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Unexplained iron deficiency sends doctors looking with light: endoscopy and colonoscopy hunt the gut for a bleeding source, and a marrow iron stain under the microscope confirms depleted stores.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and iron compete for absorption: high doses of one interfere with the other in the gut, so supplements must be balanced lest correcting one mineral deepen deficiency of the other.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Iron enters through the gut lining: the duodenal epithelium absorbs dietary iron, so celiac disease or any damage to this lining causes iron deficiency that no amount of dietary iron can fix.

[^camaschella-2015-iron-deficiency]: Camaschella C. Iron-deficiency anemia. *N Engl J Med.* 2015;372(19):1832-1843. [doi:10.1056/NEJMra1401038](https://doi.org/10.1056/NEJMra1401038) · [PubMed 25946282](https://pubmed.ncbi.nlm.nih.gov/25946282/)
[^who-ferritin-guideline-2020]: World Health Organization. WHO guideline on use of ferritin concentrations to assess iron status in individuals and populations. WHO; 2020. [WHO publication](https://www.who.int/publications/i/item/9789240000124)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
