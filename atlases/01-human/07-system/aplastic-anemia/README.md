---
schema: human-scale-entry/v1
id: aplastic-anemia
name: Aplastic Anemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Aplastic anemia (AA) is a bone marrow failure syndrome; autoreactive CD8+ T cells destroy HSCs via perforin/granzyme → pancytopenia. SAA: ANC <500/µL, plt <20,000/µL, reticulocytes <20,000/µL. Treatment: HSCT (young, matched donor) or ATG + cyclosporine + eltrombopag."
aliases: ["AA", "aplastic anaemia", "severe aplastic anemia", "SAA", "very severe aplastic anemia", "VSAA", "bone marrow failure"]
sources:
  - id: young-2018-aplastic-anemia-review
    type: peer-reviewed
    cite: "Young NS. Aplastic Anemia. N Engl J Med. 2018;379(17):1643-1656."
    doi: "10.1056/NEJMra1413485"
    pmid: "30354959"
    url: "https://doi.org/10.1056/NEJMra1413485"
  - id: townsley-2017-eltrombopag-aa
    type: peer-reviewed
    cite: "Townsley DM, Scheinberg P, Winkler T, et al. Eltrombopag Added to Standard Immunosuppression for Aplastic Anemia. N Engl J Med. 2017;376(16):1540-1550."
    doi: "10.1056/NEJMoa1613878"
    pmid: "28423296"
    url: "https://doi.org/10.1056/NEJMoa1613878"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: targets
    note: "AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "In aplastic anemia, autoreactive CTL target HSCs via perforin/granzyme-mediated cytotoxicity; elevated perforin+ CD8+ T cells in AA bone marrow predict treatment response; cyclosporine + anti-thymocyte globulin (ATG) reduce autoreactive CTL activity and restore hematopoiesis."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "In severe AA, HSC destruction → thrombocytopenia; elevated TPO cannot drive production from depleted marrow; eltrombopag added to hATG+CsA (triple IST) improves overall response and may expand HSCs via c-Mpl beyond megakaryopoiesis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Autoreactive CD8+ CTL are the primary effectors in AA; oligoclonally expanded T cells infiltrate the marrow and kill HSCs via perforin/granzyme B → caspase-3 → apoptosis; Vβ TCR skewing documented; hATG + cyclosporine suppresses autoreactive CTL and restores hematopoiesis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Activated T cells secrete IFN-γ in the AA marrow → STAT1 → ↑p21/WAF1 → HSC cell cycle arrest; IFN-γ also upregulates FasL on HSCs → autocrine apoptosis; IFN-γ levels correlate with AA severity and response to IST; ruxolitinib (JAK1/2) targets IFN-γ signaling in refractory AA."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "AA patients have 10-15% risk of clonal evolution to MDS or AML; monosomy 7 is the most common cytogenetic abnormality (→ high MDS/AML risk); eltrombopag requires karyotype monitoring every 3 months; prior IST may select DNMT3A/ASXL1-mutant clones."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Aplastic anemia and ALL both present with pancytopenia but are mirror images: AA a hypocellular marrow emptied by autoreactive T cells, ALL a hypercellular marrow packed with lymphoblasts — the marrow biopsy distinguishes empty from blast-replaced, a critical fork in management."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutropenia is the most dangerous cytopenia in aplastic anemia: with the marrow unable to produce granulocytes, severe AA (ANC <500) leaves patients defenseless against bacterial and fungal infection, the leading cause of death; G-CSF gives little response in a depleted marrow."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia in aplastic anemia reflects failed megakaryopoiesis despite high thrombopoietin; severe AA (platelets <20,000) risks spontaneous hemorrhage including intracranial bleeding, and the TPO-mimetic eltrombopag was developed to stimulate residual stem cells via c-Mpl."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Aplastic anemia is failure of all three blood lineages: as hematopoietic stem cells are destroyed, red-cell production collapses alongside neutrophils and platelets, giving the reticulocytopenic anemia of pancytopenia—so transfusions bridge to immunosuppression or transplant."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hepatitis-associated aplastic anemia is a striking syndrome: weeks to months after an acute (often seronegative, non-A-E) hepatitis, fulminant marrow failure appears—an immune attack on stem cells triggered by the hepatitis; severe but responsive to immunosuppression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Most acquired aplastic anemia is immune-mediated marrow failure: oligoclonal cytotoxic T cells and interferon-γ/TNF destroy hematopoietic stem cells, which is why immunosuppression (ATG plus ciclosporin) restores counts—the immune system, not a stem-cell defect, drives it."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Aplastic anemia can evolve into clonal marrow disease: immune-mediated stem-cell failure pressures surviving clones, so some patients progress to MDS or AML (often with monosomy 7)—aplastic anemia needs long-term monitoring for clonal evolution, not just count recovery."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Allogeneic stem-cell transplant is curative for severe aplastic anemia but brings graft-versus-host disease: donor immune cells can attack the recipient even as they restore hematopoiesis, so GVHD prophylaxis and matched donors are central to transplant in young patients."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Failure of regulatory T cells underlies acquired aplastic anemia: when Tregs cannot restrain autoreactive cytotoxic T cells, those T cells destroy hematopoietic stem cells via IFN-γ and perforin—so immunosuppression restoring tolerance can rescue the marrow."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells orchestrate the autoimmune attack in aplastic anemia: activated Th1 cells secrete interferon-gamma and TNF that, with cytotoxic T cells, destroy hematopoietic stem cells—which is why immunosuppression with ATG and cyclosporine can restore blood counts."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietin is high but futile in aplastic anemia: the anemia drives appropriate EPO release, yet the empty marrow has no stem cells to respond—unlike kidney-disease anemia where EPO itself is deficient, so EPO therapy alone cannot fix aplastic anemia."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Aplastic anemia overlaps with lupus: SLE can cause immune-mediated cytopenias and rarely marrow aplasia, and both are autoimmune disorders treated with immunosuppression—so a new pancytopenia prompts an autoimmune workup alongside marrow examination."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Aplastic anemia links to the thymus through autoimmunity: thymoma is an established cause of acquired marrow failure (and pure red cell aplasia), reflecting how disordered thymic T-cell selection can unleash the autoreactive T cells that attack stem cells."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Aplastic anemia is marrow failure by cytokine attack: autoreactive cytotoxic T cells flood the marrow with IFN-gamma and TNF that kill hematopoietic stem cells, so it is essentially a localized cytokine storm—why immunosuppression restores blood counts."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Antithymocyte globulin is a cornerstone of aplastic anemia therapy: these IgG antibodies raised against human T cells deplete the autoreactive lymphocytes destroying the marrow, so immunosuppression with ATG plus cyclosporine rescues many patients without a transplant."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Some aplastic anemia is a telomere disease: germline TERT and telomerase mutations (telomeropathies like dyskeratosis congenita) prematurely exhaust blood stem cells, so unexplained marrow failure with short telomeres warrants genetic testing before transplant."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation is a classic cause of aplastic anemia: X-ray and gamma photons damage dividing marrow stem cells, so high-dose exposure wipes out blood production—the same mechanism deliberately used in total-body irradiation before stem-cell transplant."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Aplastic anemia can follow hepatitis: a seronegative viral hepatitis sometimes precedes severe marrow failure (hepatitis-associated aplastic anemia), an immune-mediated link in which liver inflammation heralds the destruction of blood stem cells."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion-dependent aplastic anemia accumulates iron: regular red-cell transfusions for the pancytopenia deposit iron in the heart and liver, so iron chelation is needed in patients who depend on transfusions long-term."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Aplastic anemia is treated by calming T cells via calcineurin: cyclosporine, a calcineurin inhibitor, with anti-thymocyte globulin suppresses the T-cell attack on marrow stem cells—the immunosuppressive therapy that restores blood counts when transplant isn't an option."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Aplastic anemia typically spares the spleen: unlike many causes of low blood counts, it produces pancytopenia without splenomegaly, so an enlarged spleen argues against aplastic anemia and points to infiltration or hypersplenism instead."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha joins interferon-gamma in suppressing the marrow in aplastic anemia: these Th1 cytokines from autoreactive T cells poison blood-forming stem cells, which is why immunosuppression—not just transfusion—is central to treating the disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells are part of aplastic anemia's misdirected attack: alongside cytotoxic T cells, dysregulated innate lymphocytes help destroy the marrow's stem cells, deepening the pancytopenia that defines the disease."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Aplastic anemia starves tissues of oxygen: with red cell production shut down, hemoglobin falls and the blood carries less oxygen, causing the fatigue and breathlessness that, with bleeding and infection, mark the failing marrow."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Aplastic anemia overworks and overloads the heart: chronic anemia forces high-output pumping, and the iron from repeated transfusions deposits in the muscle, together threatening heart failure over years of treatment."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help ignite aplastic anemia: by presenting stem-cell antigens to T cells, they prime the autoimmune attack that cytotoxic T cells then carry out against the marrow—why immunosuppression can restore blood counts."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-based solvents can wipe out the marrow: benzene exposure is a classic environmental cause of aplastic anemia, its toxic metabolites poisoning the blood-forming stem cells into failure."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Aplastic anemia shows on the skin: the plummeting platelets cause petechiae and easy bruising, often the first visible sign that the marrow has stopped making blood cells."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "The marrow niche fails too in aplastic anemia: osteoblasts help build the stem-cell niche, so damage to this supportive scaffold compounds the loss of blood-forming stem cells."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12 anchors stem cells in the marrow niche: this chemokine retains and supports blood-forming stem cells, so a disrupted CXCL12 niche contributes to their loss in aplastic anemia."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the emptied marrow: where blood-forming cells should crowd, aplastic anemia leaves a near-deserted space filled with fat, the hypocellular wasteland that starves the blood of every cell line."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Losing neutrophils endangers the gut: with no white cells to defend it, the bowel wall can be invaded in neutropenic enterocolitis (typhlitis), while low platelets make gastrointestinal bleeding a constant threat."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The defenseless lung is a frequent battleground: profound neutropenia opens the airways to bacterial and fungal pneumonia, the kind of infection that is a leading cause of death in severe aplastic anemia."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody preparation is a cornerstone cure: antithymocyte globulin — antibodies raised against human T cells — wipes out the autoreactive T cells attacking the marrow, the immunosuppression that revives blood production in those who cannot transplant."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Androgens can coax the failing marrow: synthetic male hormones like danazol and oxymetholone stimulate blood-cell production and are still used, especially in inherited telomere-related aplastic anemia."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The gravest risk is bleeding into the brain: with platelets crashed, a spontaneous intracranial hemorrhage is a feared and often fatal complication, which is why platelet transfusions are given to hold the count above danger."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Hepatitis can be followed by marrow collapse: a severe hepatitis-associated aplastic anemia strikes weeks to months after acute hepatitis, usually in young men, an immune-mediated wipeout of the marrow triggered by the liver infection."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Inherited marrow failure shows in the skeleton: Fanconi anemia, a constitutional cause, comes with radial-ray and thumb anomalies and short stature, the bony clues that point to a genetic syndrome behind a child's aplasia."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The immunosuppression taxes the kidney: ciclosporin, a mainstay of treatment, is nephrotoxic and raises blood pressure, so renal function and drug levels are watched throughout the long course of therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Devouring macrophages can mimic marrow failure: in hemophagocytic syndromes overactive macrophages engulf blood cells, causing a pancytopenia that must be told apart from true aplastic anemia on the marrow biopsy."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "A tropical infection can empty the blood counts: visceral leishmaniasis fills the marrow with parasitized macrophages and enlarges the spleen, producing a pancytopenia that mimics aplastic anemia in endemic regions."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Both can give a 'dry tap,' but for opposite reasons: aplastic anemia empties the marrow while myelofibrosis scars it solid, so the marrow biopsy — hypocellular versus fibrotic — separates these two causes of marrow failure."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "A common virus can crash the marrow: Epstein-Barr and other viruses are recognized triggers of acquired aplastic anemia, setting off the autoreactive T-cell attack on hematopoietic stem cells in susceptible people."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Empty marrow leaves no defense: the profound neutropenia of severe aplastic anemia makes overwhelming bacterial and fungal sepsis the leading cause of death, which is why neutropenic fever is a medical emergency."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Autoreactive T cells run on IL-2: the cytokine expands the cytotoxic T-cell clones that destroy stem cells in aplastic anemia, and modulating IL-2 (low-dose, to favor regulatory T cells) is explored to restore tolerance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-mutant T-cell clones drive the attack: clonal large granular lymphocytes carrying STAT3 mutations are found in immune aplastic anemia, marking the autoreactive cytotoxic cells that destroy the marrow stem-cell pool."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammatory signaling fuels the assault: NF-κB activation in the autoreactive T cells and the marrow microenvironment supports the cytokine output that suppresses and kills hematopoietic stem cells in aplastic anemia."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An emerging PNH clone tips toward clotting: aplastic anemia frequently harbors a paroxysmal nocturnal hemoglobinuria clone whose complement-driven hemolysis creates a prothrombotic state and venous thromboembolism risk."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Empty marrow leaves the lung defenseless: the profound, prolonged neutropenia of severe aplastic anemia lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a leading infectious cause of death."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Lost neutrophils let the yeast bloodstream: severe neutropenia in aplastic anemia, compounded by immunosuppressive therapy, allows Candida to invade from the gut into the blood as invasive candidiasis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Transfusions and chronic anemia burden the heart: the repeated red-cell transfusions for aplastic anemia deposit iron in the myocardium while the sustained anemia adds high-output strain, together risking heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its immunosuppressive mainstay scars the kidney: ciclosporin, a calcineurin inhibitor central to treating aplastic anemia, is nephrotoxic, and prolonged use can leave chronic kidney impairment."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Deep immunosuppression reawakens zoster: the profound T-cell suppression from antithymocyte globulin and ciclosporin in aplastic anemia readily reactivates latent varicella-zoster as shingles."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A sudden life-threatening marrow failure weighs on mood: the abrupt diagnosis, transfusion dependence and risk of fatal infection or bleeding in aplastic anemia carry a heavy psychological burden."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Failing platelets bleed into the skin: the severe thrombocytopenia of aplastic anemia causes petechiae, purpura and mucosal bleeding, often the first visible sign of the marrow failure."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Transfusion iron overload poisons the glands: the chronic red-cell transfusions that support aplastic anemia deposit iron in the pancreas, pituitary and thyroid, causing diabetes and other endocrinopathies."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A precarious marrow failure breeds worry: the constant threat of bleeding and infection, transfusion dependence and uncertain prognosis of aplastic anemia foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its lowest platelets threaten the brain: severe thrombocytopenia in aplastic anemia risks intracranial haemorrhage, a leading cause of death, on top of the fatigue of profound anaemia."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Empty marrow leaves the lungs undefended: neutropenia invites bacterial and invasive fungal pneumonia, while thrombocytopenia can cause alveolar haemorrhage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It bleeds into and loads the gut: thrombocytopenia causes gastrointestinal bleeding, and years of red-cell transfusion deposit iron in the liver, causing iron-overload injury."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Profound anaemia strains the heart: chronic pancytopenia forces a high-output state, and transfusional iron overload can damage the myocardium over years of transfusion support."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "An autoimmune attack from the lymphoid system: in most cases cytotoxic T cells destroy haematopoietic stem cells, and a thymoma can drive the related pure red cell aplasia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment and overlap reach the kidney: the ciclosporin used to suppress the immune attack is nephrotoxic, and aplastic anaemia overlaps PNH, whose haemolysis injures the kidney."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The commonest cause of marrow aplasia: cytotoxic chemotherapy predictably suppresses the bone marrow, the dose-dependent and usually reversible counterpart of idiopathic aplastic anaemia."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Drugs can switch off the marrow: NSAIDs such as ibuprofen are among the many agents that rarely trigger idiosyncratic aplastic anaemia, alongside chloramphenicol and antithyroid drugs."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A virus that empties the marrow: untreated HIV suppresses haematopoiesis and causes pancytopenia and marrow failure that can resemble aplastic anaemia."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Eltrombopag revived its treatment: the thrombopoietin-receptor agonist eltrombopag restores trilineage haematopoiesis in aplastic anaemia, added to the antithymocyte globulin and ciclosporin immunosuppression that targets the marrow-destroying T cells."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Two routes to transfusion dependence: aplastic anaemia is an empty, failed marrow, whereas thalassaemia is a genetic globin defect with a hyperactive but ineffective marrow — opposite marrow states converging on lifelong transfusion."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatitis can precede it: a seronegative hepatitis that injures the liver lobule is a recognised trigger of post-hepatitic aplastic anaemia, where an immune attack on the marrow follows the liver inflammation weeks later."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Opposite anaemias: aplastic anaemia fails to make blood cells (pancytopenia) while iron-deficiency anaemia lacks the iron to build haemoglobin—and repeated transfusions for aplastic anaemia ironically cause iron overload."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Neutropenic gut infection: profound neutropenia in aplastic anaemia lets gut bacteria invade the bowel wall, causing typhlitis and a major route of life-threatening sepsis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Parvovirus aplastic crisis: parvovirus B19 transiently shuts down red-cell production, causing a sudden severe anaemia in sickle cell disease—a focused red-cell aplasia distinct from the global marrow failure of aplastic anaemia."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "Viral marrow suppression: HIV directly and indirectly suppresses the bone marrow, causing pancytopenia and occasionally an aplastic-anaemia-like picture in advanced infection."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Drug-induced marrow failure: anticonvulsants such as carbamazepine and felbamate are among the drugs that can trigger idiosyncratic aplastic anaemia, linking epilepsy treatment to marrow failure."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "An empty marrow cavity: aplastic anaemia leaves the cortical-bone-encased marrow hypocellular and fatty, the hallmark biopsy finding that distinguishes it from infiltrative marrow failure."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: connects-to
    note: "Viral marrow suppression: dengue transiently suppresses the bone marrow, producing the profound thrombocytopenia and pancytopenia that can mimic or unmask aplastic anaemia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen therapy: synthetic androgens such as danazol and oxymetholone stimulate residual haematopoiesis and lengthen telomeres, an older but still-used treatment for aplastic anaemia, especially telomere-related disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy-associated aplasia: pregnancy can trigger or worsen aplastic anaemia, often remitting after delivery, implicating the hormonal and immune shifts of the placental state."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 marrow attack: IL-17-producing T-helper cells contribute to the autoimmune destruction of haematopoietic stem cells in aplastic anaemia, alongside the dominant Th1 response."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory milieu: IL-6 is elevated in aplastic anaemia, part of the cytokine environment that suppresses haematopoiesis and supports the autoreactive immune response."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "Marrow-failure signal: FLT3 ligand rises markedly in aplastic anaemia as the body tries to stimulate the failing stem-cell pool, a useful marker of the depth of marrow failure."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Stem-cell survival: KIT and its ligand stem-cell factor sustain haematopoietic stem cells, the very cells the autoreactive T-cell attack of aplastic anaemia destroys, collapsing trilineage production."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic destruction: autoreactive T cells kill stem and progenitor cells through Fas and IFN-γ that converge on caspase-3-mediated apoptosis, the executioner step of immune marrow failure."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Innate inflammation: NLRP3-inflammasome activation contributes to the inflammatory bone-marrow microenvironment that accompanies the immune-mediated stem-cell destruction of aplastic anaemia."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "TPO-receptor rescue: eltrombopag stimulates the thrombopoietin receptor MPL on surviving haematopoietic stem cells to restore trilineage production in aplastic anaemia, a therapy that works even though the defect is immune."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ signalling: the IFN-γ that drives immune marrow failure in aplastic anaemia signals through STAT1 to suppress and kill haematopoietic stem cells, the intracellular transducer of the T-cell attack."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Progenitor suppression: TGF-β is among the inhibitory cytokines that suppress haematopoietic progenitor proliferation in the aplastic marrow, adding to the IFN-γ- and TNF-driven destruction of stem cells."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune predisposition: HLA-DR15 is over-represented in acquired aplastic anaemia, where MHC-class-II presentation of stem-cell antigens primes the autoreactive T cells that attack the marrow — explaining its response to immunosuppression."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Immunosuppressive therapy: corticosteroids acting through the glucocorticoid receptor accompany antithymocyte globulin and ciclosporin in the immunosuppression that rescues the marrow from the autoreactive T-cell attack of aplastic anaemia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Clonal evolution: surviving stem cells in aplastic anaemia can acquire mutations such as DNMT3A, and a subset of patients progress to myelodysplastic syndrome or acute leukaemia, the late clonal transformation that shadows the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "HSC apoptosis: Fas- and perforin-driven T-cell attack on haematopoietic stem cells (perforin already mapped) tips the BCL-2 anti-apoptotic balance toward the HSC apoptosis (caspase-3 already mapped) that empties the marrow in aplastic anaemia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "TPO-survival axis: thrombopoietin signalling through its receptor activates PI3K-AKT to support haematopoietic stem-cell survival, the axis eltrombopag exploits to restore haematopoiesis in aplastic anaemia."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune dysregulation: deficient regulatory IL-10 and regulatory T cells (already mapped) fail to restrain the autoreactive T-cell attack on the marrow in aplastic anaemia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Dual JAK-STAT axis: IFN-γ and the thrombopoietin receptor MPL both signal through JAK-STAT (STAT1, STAT3 and MPL already mapped) — the axis driving both the immune stem-cell destruction and the eltrombopag-stimulated marrow recovery of aplastic anaemia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1/IFN-γ response (already mapped) that mediates the cytotoxic T-cell attack on haematopoietic stem cells in aplastic anaemia."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "Clonal evolution: acquired clonal-haematopoiesis mutations (DNMT3A already mapped) including RUNX1 mark the evolution of aplastic anaemia toward myelodysplastic syndrome and acute leukaemia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-regulated metabolism drives both the autoreactive T-cell attack and the survival signalling of residual haematopoietic progenitors in aplastic anaemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling downstream of haematopoietic growth-factor and TPO receptors (MPL mapped) supports the progenitor responses compromised in aplastic anaemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the type-I-interferon and inflammatory milieu implicated in immune-mediated marrow failure."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the immune-cell activation that drives the T-cell-mediated destruction of haematopoietic stem cells in aplastic anemia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the suppression of haematopoietic stem cells and the immune dysregulation of aplastic anemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors govern the oxidative-stress resistance and quiescence of haematopoietic stem cells, whose failure contributes to the marrow exhaustion of aplastic anemia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α shapes the hypoxic bone-marrow niche and the stem-cell stress responses relevant to the marrow failure of aplastic anemia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory immune activation that accompanies the T-cell-mediated marrow destruction of aplastic anemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the hematopoietic stem-cell survival and self-renewal signaling whose disruption contributes to aplastic anemia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the autoreactive T cells that attack the hematopoietic stem cells of aplastic anemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the cytotoxic T-cell activation that destroys the marrow in aplastic anemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the residual hematopoietic stem cells under the immune and oxidative stress of aplastic anemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism driving the marrow failure of aplastic anemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven T-cell recruitment into the bone marrow contributes to the immune destruction of hematopoietic stem cells in aplastic anemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling participates in the apoptotic destruction of hematopoietic stem and progenitor cells in aplastic anemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the inflammatory bone-marrow microenvironment of aplastic anemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune dysregulation and marrow microenvironment of aplastic anemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement activation participates in the immune-mediated marrow injury (including PNH-overlap clones) of aplastic anemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hematopoietic and immune gene programs relevant to aplastic anemia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation of the T-cell-mediated marrow failure of aplastic anemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the T-cell activation and hematopoietic-stem-cell-niche interactions of aplastic anemia."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Pancytopenic anaemia: destruction of haematopoietic stem cells collapses red-cell production, and the falling haemoglobin, alongside neutropenia and thrombocytopenia, is a defining and transfusion-dependent feature of aplastic anaemia."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Transfusional iron overload: chronic transfusion for aplastic anaemia deposits iron in the heart and liver, and the disordered hepcidin-driven iron handling contributes to the overload that requires chelation therapy."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "T-cell checkpoint: the autoreactive T cells that destroy the marrow in aplastic anaemia are normally restrained by CTLA-4, and immunosuppressive therapy works by damping this T-cell attack to allow haematopoietic recovery."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th1/Th2 imbalance: aplastic anaemia is driven by a Th1, interferon-gamma-dominated (already mapped) attack on the marrow, and the deficient IL-4-driven type-2 counterbalance is part of the immune dysregulation that immunosuppression corrects."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative marrow stress: transfusional iron overload (hepcidin already mapped) and inflammation generate reactive oxygen species, to which xanthine oxidase contributes, adding oxidative injury to the already failing marrow of aplastic anaemia."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Iron cardiomyopathy: chronic transfusion deposits iron in the heart, and the resulting iron-overload cardiomyopathy, marked by troponin release, is a major cause of death in transfusion-dependent aplastic anaemia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 cytokine dysregulation: IL-13, with IL-4 (already mapped), reflects the broader cytokine dysregulation of aplastic anaemia beyond the dominant Th1/interferon-gamma (already mapped) attack on the marrow."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow vascular niche: VEGF supports the bone-marrow (already mapped) vascular niche of haematopoiesis, and the disturbed niche of the immune-attacked marrow contributes to the failure of blood-cell production in aplastic anaemia."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the inflammatory infiltrate (IL-6, TNF and IL-1 already mapped) of the immune attack on the marrow contribute to the suppression of haematopoiesis in aplastic anaemia."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper-deficiency mimic: copper is required for haematopoiesis, and its deficiency causes a marrow failure with cytopenias and vacuolated precursors that mimics aplastic anaemia and myelodysplasia (MDS already mapped)."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and haematopoiesis: zinc supports immune function and haematopoiesis, and excess zinc (or its supplementation) can induce a copper deficiency (already mapped) that causes cytopenias, part of the trace-metal balance relevant to aplastic anaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fatty marrow replacement: the hypocellular marrow (already mapped) of aplastic anaemia is replaced by fat, and the marrow adipocytes and their adipokine leptin signal to the residual haematopoietic cells of the failing marrow."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Immune-attack interferon: the type-I interferon, with the IFN-γ (already mapped) of the autoreactive T cells, is part of the interferon-driven immune attack on the haematopoietic stem cells in aplastic anaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), is secreted by the marrow adipocytes of the fatty marrow that replaces the failing haematopoiesis of aplastic anaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the fat-replaced marrow microenvironment of aplastic anaemia."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "MDS overlap: the aplastic anaemia can evolve to (or overlap with) the myelodysplastic syndrome (the clonal evolution, the monosomy-7), a feared late complication."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th1 driver: the CD4 Th1 cells (IFN-γ and IL-2 already mapped) orchestrate the immune attack on the haematopoietic stem cells of the marrow in aplastic anaemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusion iron: the transfusion-dependent (haemoglobin already mapped) aplastic anaemia accumulates the iron overload (hepcidin already mapped), needing the chelation."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1 (IFN-γ and IL-12 already mapped) attack of aplastic anaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune attack on the haematopoietic stem cells in aplastic anaemia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune dysregulation of aplastic anaemia."
---

# Aplastic Anemia

## Overview

**Aplastic anemia (AA)** is a potentially life-threatening **bone marrow failure syndrome** characterized by **hypocellular bone marrow** and **peripheral blood pancytopenia** (anemia, neutropenia, thrombocytopenia), resulting from destruction or failure of hematopoietic stem cells (HSCs) [^young-2018-aplastic-anemia-review].

In >80% of acquired AA cases, the disease is **immune-mediated**: autoreactive **CD8+ cytotoxic T lymphocytes** (CTL), oligoclonally expanded against unknown HSC antigens, destroy HSCs via **perforin/granzyme-B-mediated cytotoxicity** and Fas-FasL interactions. IFN-γ from activated T cells further suppresses HSC proliferation via STAT1 → ↑FasL expression on HSCs → HSC apoptosis. Tregs are quantitatively and functionally deficient in AA — implicating a breakdown in immune self-tolerance.

**Incidence:** 2-3 cases/100,000/year in Western countries; 5-7/100,000 in East Asia (higher in Asia for unknown reasons — possibly environmental/viral triggers); peak ages: 10-25 years and >60 years (bimodal distribution); equal sex distribution.

**Causes:**
- **Acquired idiopathic (most common, ~80%):** Immune-mediated; preceding viral infection (EBV, parvovirus B19, hepatitis-associated AA after NANB hepatitis), drugs, or no identifiable trigger
- **Drug-induced:** Chloramphenicol (classic), carbamazepine, methimazole, gold, NSAIDs — idiosyncratic reactions; not dose-dependent
- **Inherited bone marrow failure syndromes:** Fanconi anemia (FANC gene family, chromosomal fragility; risk of MDS/AML), dyskeratosis congenita (telomere biology genes: TERT, TERC, DKC1; mucocutaneous triad), Diamond-Blackfan anemia (RPS/RPL ribosomal protein mutations), Shwachman-Diamond syndrome (SBDS)
- **PNH clone expansion:** 25-40% of AA patients have GPI-deficient (PIGA-mutant) clones on FLAER flow; AA and PNH share immune-mediated pathophysiology

## Structure

### Diagnostic criteria and severity classification

**Diagnosis:**
- **Bone marrow biopsy:** Hypocellular marrow (<25-30% cellularity); fat-replaced with few residual hematopoietic cells; empty sinusoids; no evidence of malignant infiltration (rules out hypoplastic MDS, aleukemic leukemia)
- **Peripheral blood:** Pancytopenia — reticulocytopenia (reticulocyte count <20,000/µL or <1%); no or few blasts; target cells from iron deficiency
- **Cytogenetics:** Normal karyotype (vs. hypoplastic MDS which often has cytogenetic abnormalities — monosomy 7 most common)
- **Telomere length:** Short telomeres suggest constitutional telomere disorders (dyskeratosis congenita); tested by flow-FISH or qPCR; actionable as it contraindicates standard ATG (poor response; prefer androgens/danazol + HSCT from matched sibling)

**Severity classification (Camitta criteria, modified):**

| Category | ANC | Platelets | Reticulocytes | Marrow |
|:---|:---|:---|:---|:---|
| **Severe AA (SAA)** | <500/µL | <20,000/µL | <20,000/µL | <25% cellularity |
| **Very Severe AA (VSAA)** | <200/µL | <20,000/µL | <20,000/µL | <25% cellularity |
| **Moderate AA** | 500-2000/µL | 20,000-100,000/µL | — | >25% cellularity |

**VSAA** = SAA criteria + ANC <200/µL; higher risk of early mortality from infections

### Molecular mechanism

**T cell-mediated HSC destruction:**
1. Unknown antigen (possibly cryptic HSC antigen revealed by viral infection or drug metabolite) → Th1-skewed oligoclonal T cell expansion; T cell receptor (TCR) Vβ skewing (increased frequency of specific Vβ chains) documented in AA
2. Autoreactive CD8+ CTL overexpressing IFN-γ, TNF-α, and **perforin** infiltrate the bone marrow
3. **Perforin/granzyme pathway:** CTL form immunological synapse with HSC → perforin pores → granzyme B → Bid cleavage → MOMP → caspase-9/3 → HSC apoptosis
4. **Fas-FasL pathway:** IFN-γ → ↑FasL on T cells → HSC Fas → caspase-8/3 cascade
5. **IFN-γ direct suppression:** STAT1 → ↑p21/WAF1 (CDK inhibitor) → HSC cell cycle arrest; ↑Fas on HSCs → increased susceptibility to FasL-mediated killing
6. **Treg deficiency:** Quantitatively reduced Foxp3+ CD4+CD25+ Tregs in AA; impaired IL-10/TGF-β suppression of autoreactive CTL → unchecked T cell attack

**PNH clone selection mechanism:**
- In AA, immune destruction selectively kills GPI-anchor expressing HSCs (normal HSCs) because GPI-anchored proteins include immune escape signals; PIGA-null (GPI-deficient) HSCs escape immune attack → selective expansion → PNH clone
- Explains the frequent co-occurrence of AA + PNH clones and the progression from AA to PNH in some patients

## Function

### Treatment

**First-line — Allogeneic HSCT (preferred for young patients with matched sibling donor):**
- Age ≤40 years + SAA/VSAA + matched sibling donor (MSD) → HSCT is first-line therapy
- Conditioning: Cyclophosphamide (Cy) + ATG (or fludarabine-based reduced-intensity for older patients); prevents rejection of donor graft
- **5-year OS: >80-85%** with MSD HSCT in young patients (National Registry data)
- Graft failure (primary or secondary): 5-15% with sibling donors; treat with second HSCT or immunosuppression
- MUD (matched unrelated donor) HSCT: Acceptable second-line if ATG fails; 5-year OS ~70-75% in young patients; GvHD risk higher than MSD

**First-line for older patients or no MSD — Immunosuppressive therapy (IST):**

**ATG (anti-thymocyte globulin) + cyclosporine ± eltrombopag:**
- **Horse ATG (hATG; ATGAM; Pfizer):** 40 mg/kg/day × 4 days IV; polyclonal antibody depletes T cells; hATG superior to rabbit ATG (rATG) for AA in a NEJM-published head-to-head trial (response rate 68% vs. 37% at 6 months)
- **Cyclosporine A (CsA):** 10-12 mg/kg/day divided BID; calcineurin inhibitor → ↓IL-2 → blocks T cell activation; maintained for 12-24 months to prevent relapse; monitor trough levels (target 150-250 ng/mL)
- **Eltrombopag (EPAG; thrombopoietin receptor agonist):** Added to hATG + CsA → triple IST [^townsley-2017-eltrombopag-aa]

**EPAG-ATG-CsA triple IST (NIH trial) [^townsley-2017-eltrombopag-aa]:**
- EPAG 150 mg QD (titrated to 300 mg if no response by day 14) started on day 14 of ATG
- **Complete response rate at 6 months: 33% (triple IST) vs. 10% (ATG + CsA alone)**; overall response 80% vs. 51%
- **FDA approval: 2018** for refractory/relapsed SAA; 2022 for first-line SAA in combination with ATG
- Mechanism of EPAG in AA: TPO-R agonism → HSC expansion (c-Mpl on HSCs) + direct stimulation of multilineage hematopoietic progenitor proliferation; also proposed immune modulatory effects
- EPAG adverse effects: LFT elevation (monitor); thrombosis rare in AA (thrombocytopenic patients); cytogenetic abnormalities (chromosome 7 abnormalities): 7-8% at 24 months — monitor karyotype every 3 months

**Relapsed/refractory AA:**
- **Ruxolitinib + eltrombopag:** JAK1/2 inhibition + TPO-R; investigational in refractory AA; ORR ~60%
- **Avacopan (C5aR inhibitor) + eltrombopag:** Phase 2 (complement activation in AA refractory to ATG)
- **HSCT from matched unrelated donor (MUD):** After ≥1 ATG failure; 10/10 MUD or haploidentical + PT-Cy
- **Androgens (danazol):** Second-line; ↑telomerase (TERT) → HSC survival; useful in telomeropathies; hepatotoxic

### Differential diagnosis (critical distinctions)

| Condition | Key differentiator |
|:---|:---|
| **Hypoplastic MDS** | Cytogenetic abnormalities (monosomy 7, del5q); dysplasia on marrow biopsy; older patients |
| **PNH** | FLAER+ GPI-deficient clone >10%; hemolysis (high LDH, low haptoglobin) |
| **Acute leukemia (hypocellular)** | Blasts >5% on marrow biopsy; lymphoblasts in ALL |
| **Fanconi anemia** | Chromosomal fragility (MMC/DEB test); FANC gene panel; congenital anomalies |
| **Dyskeratosis congenita** | Mucocutaneous triad (nail dystrophy, leukoplakia, reticulate pigmentation); short telomeres |

## Pathology

**Clonal evolution:**
- 10-15% of AA patients develop clonal complications: MDS (most common), AML, or PNH evolution
- Risk factors: prior IST (ATG-selected clonal advantage); cytogenetic abnormalities at diagnosis (chromosome 7 monosomy → high MDS/AML risk); very long disease duration
- Monitor: karyotype and FLAER flow every 6-12 months

**Infections:**
- Severe neutropenia → risk of invasive fungal infections (Aspergillus, Candida) and gram-negative bacteremia; prophylaxis: fluconazole/posaconazole; antimicrobials at first fever
- Empiric antifungal coverage during ATG treatment (immunosuppression + neutropenia)
- CMV reactivation in IST: monitor weekly PCR; treat with valganciclovir

**Graft failure after HSCT:**
- Primary graft failure (no engraftment): 5-15% with sibling donor; higher with MUD; treat with second HSCT
- Secondary graft failure (initial engraftment then decline): Rejection by host T cells; reduced-intensity re-conditioning + second graft

**Transfusion iron overload:**
- Chronically transfused AA patients accumulate iron (no physiological iron excretion); ferritin >2,500 ng/mL → iron chelation (deferasirox); oral chelation preferred over deferoxamine

## Connections

- `targets` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — AA results from T cell-mediated HSC destruction → hypocellular marrow (<25% cellularity) replaced by fat; 25-40% of AA patients have PNH clones (AA-PNH overlap continuum); marrow biopsy showing fat-replaced hypocellular marrow is the diagnostic hallmark.
- `connects-to` → **[PNH](../pnh/README.md)** — AA and PNH are closely related: immune destruction of normal HSCs in AA allows PIGA-mutant GPI-deficient clone to expand; 25-40% of AA patients have PNH clones at diagnosis; some AA patients evolve to overt PNH; both conditions are treated at specialized hemato-oncology centers.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — In aplastic anemia, autoreactive CTL target HSCs via perforin/granzyme-mediated cytotoxicity; elevated perforin+ CD8+ T cells in AA bone marrow predict treatment response; cyclosporine + anti-thymocyte globulin (ATG) reduce autoreactive CTL activity and restore hematopoiesis.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — In severe AA, HSC destruction → thrombocytopenia; elevated TPO cannot drive production from depleted marrow; eltrombopag added to hATG+CsA (triple IST) improves overall response and may expand HSCs via c-Mpl beyond megakaryopoiesis.
- `connects-to` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — autoreactive CD8+ CTL are the primary effectors in AA; oligoclonally expanded T cells infiltrate the marrow and kill HSCs via perforin/granzyme B → caspase-3 → apoptosis; Vβ TCR skewing documented; hATG + cyclosporine suppresses autoreactive CTL and restores hematopoiesis.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — activated T cells secrete IFN-γ in the AA marrow → STAT1 → ↑p21/WAF1 → HSC cell cycle arrest; IFN-γ also upregulates FasL on HSCs → autocrine apoptosis; IFN-γ levels correlate with AA severity and response to IST; ruxolitinib targets IFN-γ signaling in refractory AA.
- `connects-to` → **[MDS](../mds/README.md)** — AA patients have 10-15% risk of clonal evolution to MDS or AML; monosomy 7 is the most common cytogenetic abnormality (→ high MDS/AML risk); eltrombopag requires karyotype monitoring every 3 months; prior IST may select DNMT3A/ASXL1-mutant clones.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Aplastic anemia and ALL both present with pancytopenia but are mirror images: AA a hypocellular marrow emptied by autoreactive T cells, ALL a hypercellular marrow packed with lymphoblasts — the marrow biopsy distinguishes empty from blast-replaced, a critical fork in management.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutropenia is the most dangerous cytopenia in aplastic anemia: with the marrow unable to produce granulocytes, severe AA (ANC <500) leaves patients defenseless against bacterial and fungal infection, the leading cause of death; G-CSF gives little response in a depleted marrow.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia in aplastic anemia reflects failed megakaryopoiesis despite high thrombopoietin; severe AA (platelets <20,000) risks spontaneous hemorrhage including intracranial bleeding, and the TPO-mimetic eltrombopag was developed to stimulate residual stem cells via c-Mpl.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Aplastic anemia is failure of all three blood lineages: as hematopoietic stem cells are destroyed, red-cell production collapses alongside neutrophils and platelets, giving the reticulocytopenic anemia of pancytopenia—so transfusions bridge to immunosuppression or transplant.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hepatitis-associated aplastic anemia is a striking syndrome: weeks to months after an acute (often seronegative, non-A-E) hepatitis, fulminant marrow failure appears—an immune attack on stem cells triggered by the hepatitis; severe but responsive to immunosuppression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Most acquired aplastic anemia is immune-mediated marrow failure: oligoclonal cytotoxic T cells and interferon-γ/TNF destroy hematopoietic stem cells, which is why immunosuppression (ATG plus ciclosporin) restores counts—the immune system, not a stem-cell defect, drives it.
- `connects-to` → **[AML](../aml/README.md)** — Aplastic anemia can evolve into clonal marrow disease: immune-mediated stem-cell failure pressures surviving clones, so some patients progress to MDS or AML (often with monosomy 7)—aplastic anemia needs long-term monitoring for clonal evolution, not just count recovery.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Allogeneic stem-cell transplant is curative for severe aplastic anemia but brings graft-versus-host disease: donor immune cells can attack the recipient even as they restore hematopoiesis, so GVHD prophylaxis and matched donors are central to transplant in young patients.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Failure of regulatory T cells underlies acquired aplastic anemia: when Tregs cannot restrain autoreactive cytotoxic T cells, those T cells destroy hematopoietic stem cells via IFN-γ and perforin—so immunosuppression restoring tolerance can rescue the marrow.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells orchestrate the autoimmune attack in aplastic anemia: activated Th1 cells secrete interferon-gamma and TNF that, with cytotoxic T cells, destroy hematopoietic stem cells—which is why immunosuppression with ATG and cyclosporine can restore blood counts.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietin is high but futile in aplastic anemia: the anemia drives appropriate EPO release, yet the empty marrow has no stem cells to respond—unlike kidney-disease anemia where EPO itself is deficient, so EPO therapy alone cannot fix aplastic anemia.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Aplastic anemia overlaps with lupus: SLE can cause immune-mediated cytopenias and rarely marrow aplasia, and both are autoimmune disorders treated with immunosuppression—so a new pancytopenia prompts an autoimmune workup alongside marrow examination.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Aplastic anemia links to the thymus through autoimmunity: thymoma is an established cause of acquired marrow failure (and pure red cell aplasia), reflecting how disordered thymic T-cell selection can unleash the autoreactive T cells that attack stem cells.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Aplastic anemia is marrow failure by cytokine attack: autoreactive cytotoxic T cells flood the marrow with IFN-gamma and TNF that kill hematopoietic stem cells, so it is essentially a localized cytokine storm—why immunosuppression restores blood counts.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Antithymocyte globulin is a cornerstone of aplastic anemia therapy: these IgG antibodies raised against human T cells deplete the autoreactive lymphocytes destroying the marrow, so immunosuppression with ATG plus cyclosporine rescues many patients without a transplant.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Some aplastic anemia is a telomere disease: germline TERT and telomerase mutations (telomeropathies like dyskeratosis congenita) prematurely exhaust blood stem cells, so unexplained marrow failure with short telomeres warrants genetic testing before transplant.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation is a classic cause of aplastic anemia: X-ray and gamma photons damage dividing marrow stem cells, so high-dose exposure wipes out blood production—the same mechanism deliberately used in total-body irradiation before stem-cell transplant.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Aplastic anemia can follow hepatitis: a seronegative viral hepatitis sometimes precedes severe marrow failure (hepatitis-associated aplastic anemia), an immune-mediated link in which liver inflammation heralds the destruction of blood stem cells.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion-dependent aplastic anemia accumulates iron: regular red-cell transfusions for the pancytopenia deposit iron in the heart and liver, so iron chelation is needed in patients who depend on transfusions long-term.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Aplastic anemia is treated by calming T cells via calcineurin: cyclosporine, a calcineurin inhibitor, with anti-thymocyte globulin suppresses the T-cell attack on marrow stem cells—the immunosuppressive therapy that restores blood counts when transplant isn't an option.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Aplastic anemia typically spares the spleen: unlike many causes of low blood counts, it produces pancytopenia without splenomegaly, so an enlarged spleen argues against aplastic anemia and points to infiltration or hypersplenism instead.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha joins interferon-gamma in suppressing the marrow in aplastic anemia: these Th1 cytokines from autoreactive T cells poison blood-forming stem cells, which is why immunosuppression—not just transfusion—is central to treating the disease.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells are part of aplastic anemia's misdirected attack: alongside cytotoxic T cells, dysregulated innate lymphocytes help destroy the marrow's stem cells, deepening the pancytopenia that defines the disease.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Aplastic anemia starves tissues of oxygen: with red cell production shut down, hemoglobin falls and the blood carries less oxygen, causing the fatigue and breathlessness that, with bleeding and infection, mark the failing marrow.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Aplastic anemia overworks and overloads the heart: chronic anemia forces high-output pumping, and the iron from repeated transfusions deposits in the muscle, together threatening heart failure over years of treatment.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help ignite aplastic anemia: by presenting stem-cell antigens to T cells, they prime the autoimmune attack that cytotoxic T cells then carry out against the marrow—why immunosuppression can restore blood counts.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-based solvents can wipe out the marrow: benzene exposure is a classic environmental cause of aplastic anemia, its toxic metabolites poisoning the blood-forming stem cells into failure.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Aplastic anemia shows on the skin: the plummeting platelets cause petechiae and easy bruising, often the first visible sign that the marrow has stopped making blood cells.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — The marrow niche fails too in aplastic anemia: osteoblasts help build the stem-cell niche, so damage to this supportive scaffold compounds the loss of blood-forming stem cells.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 anchors stem cells in the marrow niche: this chemokine retains and supports blood-forming stem cells, so a disrupted CXCL12 niche contributes to their loss in aplastic anemia.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the emptied marrow: where blood-forming cells should crowd, aplastic anemia leaves a near-deserted space filled with fat, the hypocellular wasteland that starves the blood of every cell line.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Losing neutrophils endangers the gut: with no white cells to defend it, the bowel wall can be invaded in neutropenic enterocolitis (typhlitis), while low platelets make gastrointestinal bleeding a constant threat.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The defenseless lung is a frequent battleground: profound neutropenia opens the airways to bacterial and fungal pneumonia, the kind of infection that is a leading cause of death in severe aplastic anemia.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody preparation is a cornerstone cure: antithymocyte globulin — antibodies raised against human T cells — wipes out the autoreactive T cells attacking the marrow, the immunosuppression that revives blood production in those who cannot transplant.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Androgens can coax the failing marrow: synthetic male hormones like danazol and oxymetholone stimulate blood-cell production and are still used, especially in inherited telomere-related aplastic anemia.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The gravest risk is bleeding into the brain: with platelets crashed, a spontaneous intracranial hemorrhage is a feared and often fatal complication, which is why platelet transfusions are given to hold the count above danger.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Hepatitis can be followed by marrow collapse: a severe hepatitis-associated aplastic anemia strikes weeks to months after acute hepatitis, usually in young men, an immune-mediated wipeout of the marrow triggered by the liver infection.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Inherited marrow failure shows in the skeleton: Fanconi anemia, a constitutional cause, comes with radial-ray and thumb anomalies and short stature, the bony clues that point to a genetic syndrome behind a child's aplasia.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The immunosuppression taxes the kidney: ciclosporin, a mainstay of treatment, is nephrotoxic and raises blood pressure, so renal function and drug levels are watched throughout the long course of therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Devouring macrophages can mimic marrow failure: in hemophagocytic syndromes overactive macrophages engulf blood cells, causing a pancytopenia that must be told apart from true aplastic anemia on the marrow biopsy.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — A tropical infection can empty the blood counts: visceral leishmaniasis fills the marrow with parasitized macrophages and enlarges the spleen, producing a pancytopenia that mimics aplastic anemia in endemic regions.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Both can give a 'dry tap,' but for opposite reasons: aplastic anemia empties the marrow while myelofibrosis scars it solid, so the marrow biopsy — hypocellular versus fibrotic — separates these two causes of marrow failure.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — A common virus can crash the marrow: Epstein-Barr and other viruses are recognized triggers of acquired aplastic anemia, setting off the autoreactive T-cell attack on hematopoietic stem cells in susceptible people.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Empty marrow leaves no defense: the profound neutropenia of severe aplastic anemia makes overwhelming bacterial and fungal sepsis the leading cause of death, which is why neutropenic fever is a medical emergency.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Autoreactive T cells run on IL-2: the cytokine expands the cytotoxic T-cell clones that destroy stem cells in aplastic anemia, and modulating IL-2 (low-dose, to favor regulatory T cells) is explored to restore tolerance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-mutant T-cell clones drive the attack: clonal large granular lymphocytes carrying STAT3 mutations are found in immune aplastic anemia, marking the autoreactive cytotoxic cells that destroy the marrow stem-cell pool.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammatory signaling fuels the assault: NF-κB activation in the autoreactive T cells and the marrow microenvironment supports the cytokine output that suppresses and kills hematopoietic stem cells in aplastic anemia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An emerging PNH clone tips toward clotting: aplastic anemia frequently harbors a paroxysmal nocturnal hemoglobinuria clone whose complement-driven hemolysis creates a prothrombotic state and venous thromboembolism risk.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Empty marrow leaves the lung defenseless: the profound, prolonged neutropenia of severe aplastic anemia lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a leading infectious cause of death.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Lost neutrophils let the yeast bloodstream: severe neutropenia in aplastic anemia, compounded by immunosuppressive therapy, allows Candida to invade from the gut into the blood as invasive candidiasis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Transfusions and chronic anemia burden the heart: the repeated red-cell transfusions for aplastic anemia deposit iron in the myocardium while the sustained anemia adds high-output strain, together risking heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its immunosuppressive mainstay scars the kidney: ciclosporin, a calcineurin inhibitor central to treating aplastic anemia, is nephrotoxic, and prolonged use can leave chronic kidney impairment.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Deep immunosuppression reawakens zoster: the profound T-cell suppression from antithymocyte globulin and ciclosporin in aplastic anemia readily reactivates latent varicella-zoster as shingles.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A sudden life-threatening marrow failure weighs on mood: the abrupt diagnosis, transfusion dependence and risk of fatal infection or bleeding in aplastic anemia carry a heavy psychological burden.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Failing platelets bleed into the skin: the severe thrombocytopenia of aplastic anemia causes petechiae, purpura and mucosal bleeding, often the first visible sign of the marrow failure.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Transfusion iron overload poisons the glands: the chronic red-cell transfusions that support aplastic anemia deposit iron in the pancreas, pituitary and thyroid, causing diabetes and other endocrinopathies.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A precarious marrow failure breeds worry: the constant threat of bleeding and infection, transfusion dependence and uncertain prognosis of aplastic anemia foster chronic health anxiety alongside depression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its lowest platelets threaten the brain: severe thrombocytopenia in aplastic anemia risks intracranial haemorrhage, a leading cause of death, on top of the fatigue of profound anaemia.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Empty marrow leaves the lungs undefended: neutropenia invites bacterial and invasive fungal pneumonia, while thrombocytopenia can cause alveolar haemorrhage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It bleeds into and loads the gut: thrombocytopenia causes gastrointestinal bleeding, and years of red-cell transfusion deposit iron in the liver, causing iron-overload injury.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Profound anaemia strains the heart: chronic pancytopenia forces a high-output state, and transfusional iron overload can damage the myocardium over years of transfusion support.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — An autoimmune attack from the lymphoid system: in most cases cytotoxic T cells destroy haematopoietic stem cells, and a thymoma can drive the related pure red cell aplasia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment and overlap reach the kidney: the ciclosporin used to suppress the immune attack is nephrotoxic, and aplastic anaemia overlaps PNH, whose haemolysis injures the kidney.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — The commonest cause of marrow aplasia: cytotoxic chemotherapy predictably suppresses the bone marrow, the dose-dependent and usually reversible counterpart of idiopathic aplastic anaemia.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — Drugs can switch off the marrow: NSAIDs such as ibuprofen are among the many agents that rarely trigger idiosyncratic aplastic anaemia, alongside chloramphenicol and antithyroid drugs.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A virus that empties the marrow: untreated HIV suppresses haematopoiesis and causes pancytopenia and marrow failure that can resemble aplastic anaemia.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Eltrombopag revived its treatment: the thrombopoietin-receptor agonist eltrombopag restores trilineage haematopoiesis in aplastic anaemia, added to the antithymocyte globulin and ciclosporin immunosuppression that targets the marrow-destroying T cells.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Two routes to transfusion dependence: aplastic anaemia is an empty, failed marrow, whereas thalassaemia is a genetic globin defect with a hyperactive but ineffective marrow — opposite marrow states converging on lifelong transfusion.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatitis can precede it: a seronegative hepatitis that injures the liver lobule is a recognised trigger of post-hepatitic aplastic anaemia, where an immune attack on the marrow follows the liver inflammation weeks later.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Opposite anaemias: aplastic anaemia fails to make blood cells (pancytopenia) while iron-deficiency anaemia lacks the iron to build haemoglobin—and repeated transfusions for aplastic anaemia ironically cause iron overload.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Neutropenic gut infection: profound neutropenia in aplastic anaemia lets gut bacteria invade the bowel wall, causing typhlitis and a major route of life-threatening sepsis.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Parvovirus aplastic crisis: parvovirus B19 transiently shuts down red-cell production, causing a sudden severe anaemia in sickle cell disease—a focused red-cell aplasia distinct from the global marrow failure of aplastic anaemia.
- `connects-to` → **[HIV](../hiv/README.md)** — Viral marrow suppression: HIV directly and indirectly suppresses the bone marrow, causing pancytopenia and occasionally an aplastic-anaemia-like picture in advanced infection.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Drug-induced marrow failure: anticonvulsants such as carbamazepine and felbamate are among the drugs that can trigger idiosyncratic aplastic anaemia, linking epilepsy treatment to marrow failure.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — An empty marrow cavity: aplastic anaemia leaves the cortical-bone-encased marrow hypocellular and fatty, the hallmark biopsy finding that distinguishes it from infiltrative marrow failure.
- `connects-to` → **[Dengue Virus](../../../02-pathogen/01-viruses/dengue-virus/README.md)** — Viral marrow suppression: dengue transiently suppresses the bone marrow, producing the profound thrombocytopenia and pancytopenia that can mimic or unmask aplastic anaemia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen therapy: synthetic androgens such as danazol and oxymetholone stimulate residual haematopoiesis and lengthen telomeres, an older but still-used treatment for aplastic anaemia, especially telomere-related disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy-associated aplasia: pregnancy can trigger or worsen aplastic anaemia, often remitting after delivery, implicating the hormonal and immune shifts of the placental state.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 marrow attack: IL-17-producing T-helper cells contribute to the autoimmune destruction of haematopoietic stem cells in aplastic anaemia, alongside the dominant Th1 response.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory milieu: IL-6 is elevated in aplastic anaemia, part of the cytokine environment that suppresses haematopoiesis and supports the autoreactive immune response.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — Marrow-failure signal: FLT3 ligand rises markedly in aplastic anaemia as the body tries to stimulate the failing stem-cell pool, a useful marker of the depth of marrow failure.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Stem-cell survival: KIT and its ligand stem-cell factor sustain haematopoietic stem cells, the very cells the autoreactive T-cell attack of aplastic anaemia destroys, collapsing trilineage production.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Apoptotic destruction: autoreactive T cells kill stem and progenitor cells through Fas and IFN-γ that converge on caspase-3-mediated apoptosis, the executioner step of immune marrow failure.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Innate inflammation: NLRP3-inflammasome activation contributes to the inflammatory bone-marrow microenvironment that accompanies the immune-mediated stem-cell destruction of aplastic anaemia.
- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — Eltrombopag stimulates the thrombopoietin receptor MPL on surviving haematopoietic stem cells to restore trilineage production in aplastic anaemia—a therapy that works even though the underlying defect is immune-mediated destruction.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The IFN-γ that drives immune marrow failure in aplastic anaemia signals through STAT1 to suppress and kill haematopoietic stem cells, the intracellular transducer through which the autoreactive T-cell attack collapses haematopoiesis.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β is among the inhibitory cytokines that suppress haematopoietic progenitor proliferation in the aplastic marrow, adding to the IFN-γ- and TNF-driven destruction that empties the bone marrow.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HLA-DR15 is over-represented in acquired aplastic anemia, where MHC-class-II presentation of stem-cell antigens primes the autoreactive T cells that attack the marrow—explaining its response to immunosuppression.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor accompany antithymocyte globulin and ciclosporin in the immunosuppression that rescues the marrow from the autoreactive T-cell attack of aplastic anemia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Surviving stem cells in aplastic anemia can acquire mutations such as DNMT3A, and a subset of patients progress to myelodysplastic syndrome or acute leukemia, the late clonal transformation that shadows the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Fas- and perforin-driven T-cell attack on hematopoietic stem cells (perforin already mapped) tips the BCL-2 anti-apoptotic balance toward the HSC apoptosis (caspase-3 already mapped) that empties the marrow in aplastic anemia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Thrombopoietin signaling through its receptor activates PI3K-AKT to support hematopoietic stem-cell survival, the axis eltrombopag exploits to restore hematopoiesis in aplastic anemia.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Deficient regulatory IL-10 and regulatory T cells (already mapped) fail to restrain the autoreactive T-cell attack on the marrow in aplastic anemia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IFN-γ and the thrombopoietin receptor MPL both signal through JAK-STAT (STAT1, STAT3 and MPL already mapped) — the axis driving both the immune stem-cell destruction and the eltrombopag-stimulated marrow recovery of aplastic anemia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 polarizes the Th1/IFN-γ response (already mapped) that mediates the cytotoxic T-cell attack on hematopoietic stem cells in aplastic anemia.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — Acquired clonal-hematopoiesis mutations (DNMT3A already mapped) including RUNX1 mark the evolution of aplastic anemia toward myelodysplastic syndrome and acute leukemia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated metabolism drives both the autoreactive T-cell attack and the survival signaling of residual hematopoietic progenitors in aplastic anemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of hematopoietic growth-factor and TPO receptors (MPL mapped) supports the progenitor responses compromised in aplastic anemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the type-I-interferon and inflammatory milieu implicated in immune-mediated marrow failure.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the immune-cell activation that drives the T-cell-mediated destruction of hematopoietic stem cells in aplastic anemia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the suppression of hematopoietic stem cells and the immune dysregulation of aplastic anemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors govern the oxidative-stress resistance and quiescence of hematopoietic stem cells, whose failure contributes to the marrow exhaustion of aplastic anemia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α shapes the hypoxic bone-marrow niche and the stem-cell stress responses relevant to the marrow failure of aplastic anemia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory immune activation that accompanies the T-cell-mediated marrow destruction of aplastic anemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the hematopoietic stem-cell survival and self-renewal signaling whose disruption contributes to aplastic anemia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the autoreactive T cells that attack the hematopoietic stem cells of aplastic anemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the cytotoxic T-cell activation that destroys the marrow in aplastic anemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the residual hematopoietic stem cells under the immune and oxidative stress of aplastic anemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism driving the marrow failure of aplastic anemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven T-cell recruitment into the bone marrow contributes to the immune destruction of hematopoietic stem cells in aplastic anemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling participates in the apoptotic destruction of hematopoietic stem and progenitor cells in aplastic anemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the inflammatory bone-marrow microenvironment of aplastic anemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune dysregulation and marrow microenvironment of aplastic anemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation participates in the immune-mediated marrow injury (including PNH-overlap clones) of aplastic anemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the hematopoietic and immune gene programs relevant to aplastic anemia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation of the T-cell-mediated marrow failure of aplastic anemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the T-cell activation and hematopoietic-stem-cell-niche interactions of aplastic anemia.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Pancytopenic anaemia: destruction of haematopoietic stem cells collapses red-cell production, and the falling haemoglobin, alongside neutropenia and thrombocytopenia, is a defining and transfusion-dependent feature of aplastic anaemia.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Transfusional iron overload: chronic transfusion for aplastic anaemia deposits iron in the heart and liver, and the disordered hepcidin-driven iron handling contributes to the overload that requires chelation therapy.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — T-cell checkpoint: the autoreactive T cells that destroy the marrow in aplastic anaemia are normally restrained by CTLA-4, and immunosuppressive therapy works by damping this T-cell attack to allow haematopoietic recovery.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th1/Th2 imbalance: aplastic anaemia is driven by a Th1, interferon-gamma-dominated (already mapped) attack on the marrow, and the deficient IL-4-driven type-2 counterbalance is part of the immune dysregulation that immunosuppression corrects.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative marrow stress: transfusional iron overload (hepcidin already mapped) and inflammation generate reactive oxygen species, to which xanthine oxidase contributes, adding oxidative injury to the already failing marrow of aplastic anaemia.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Iron cardiomyopathy: chronic transfusion deposits iron in the heart, and the resulting iron-overload cardiomyopathy, marked by troponin release, is a major cause of death in transfusion-dependent aplastic anaemia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 cytokine dysregulation: IL-13, with IL-4 (already mapped), reflects the broader cytokine dysregulation of aplastic anaemia beyond the dominant Th1/interferon-gamma (already mapped) attack on the marrow.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow vascular niche: VEGF supports the bone-marrow (already mapped) vascular niche of haematopoiesis, and the disturbed niche of the immune-attacked marrow contributes to the failure of blood-cell production in aplastic anaemia.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the inflammatory infiltrate (IL-6, TNF and IL-1 already mapped) of the immune attack on the marrow contribute to the suppression of haematopoiesis in aplastic anaemia.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper-deficiency mimic: copper is required for haematopoiesis, and its deficiency causes a marrow failure with cytopenias and vacuolated precursors that mimics aplastic anaemia and myelodysplasia (MDS already mapped).
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and haematopoiesis: zinc supports immune function and haematopoiesis, and excess zinc (or its supplementation) can induce a copper deficiency (already mapped) that causes cytopenias, part of the trace-metal balance relevant to aplastic anaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fatty marrow replacement: the hypocellular marrow (already mapped) of aplastic anaemia is replaced by fat, and the marrow adipocytes and their adipokine leptin signal to the residual haematopoietic cells of the failing marrow.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Immune-attack interferon: the type-I interferon, with the IFN-γ (already mapped) of the autoreactive T cells, is part of the interferon-driven immune attack on the haematopoietic stem cells in aplastic anaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte adipokine: adiponectin, with leptin (already mapped), is secreted by the marrow adipocytes of the fatty marrow that replaces the failing haematopoiesis of aplastic anaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the fat-replaced marrow microenvironment of aplastic anaemia.
- `connects-to` → **[MDS](../mds/README.md)** — MDS overlap: the aplastic anaemia can evolve to (or overlap with) the myelodysplastic syndrome (the clonal evolution, the monosomy-7), a feared late complication.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Th1 driver: the CD4 Th1 cells (IFN-γ and IL-2 already mapped) orchestrate the immune attack on the haematopoietic stem cells of the marrow in aplastic anaemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusion iron: the transfusion-dependent (haemoglobin already mapped) aplastic anaemia accumulates the iron overload (hepcidin already mapped), needing the chelation.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1 (IFN-γ and IL-12 already mapped) attack of aplastic anaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune attack on the haematopoietic stem cells in aplastic anaemia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune dysregulation of aplastic anaemia.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^young-2018-aplastic-anemia-review]: Young NS. Aplastic Anemia. *N Engl J Med.* 2018;379(17):1643-1656. [doi:10.1056/NEJMra1413485](https://doi.org/10.1056/NEJMra1413485) · [PubMed 30354959](https://pubmed.ncbi.nlm.nih.gov/30354959/)
[^townsley-2017-eltrombopag-aa]: Townsley DM, Scheinberg P, Winkler T, et al. Eltrombopag Added to Standard Immunosuppression for Aplastic Anemia. *N Engl J Med.* 2017;376(16):1540-1550. [doi:10.1056/NEJMoa1613878](https://doi.org/10.1056/NEJMoa1613878) · [PubMed 28423296](https://pubmed.ncbi.nlm.nih.gov/28423296/)
