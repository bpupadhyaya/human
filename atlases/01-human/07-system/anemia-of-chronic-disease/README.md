---
schema: human-scale-entry/v1
id: anemia-of-chronic-disease
name: Anemia of Chronic Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Anemia of chronic disease (ACD) is anemia from chronic inflammation (infection, autoimmune disease, malignancy, CKD); IL-6 → hepcidin → ferroportin degradation → iron sequestration → iron-restricted erythropoiesis. Treat underlying cause; IV iron and ESAs in CKD."
aliases: ["ACD", "anemia of chronic disease", "anemia of inflammation", "AI", "functional iron deficiency", "AOCD", "inflammatory anemia", "iron sequestration anemia"]
sources:
  - id: weiss-2005-acd-review
    type: peer-reviewed
    cite: "Weiss G, Goodnough LT. Anemia of chronic disease. N Engl J Med. 2005;352(10):1011-1023."
    doi: "10.1056/NEJMra041809"
    pmid: "15758012"
    url: "https://doi.org/10.1056/NEJMra041809"
  - id: nemeth-2004-il6-hepcidin
    type: peer-reviewed
    cite: "Nemeth E, Rivera S, Gabayan V, et al. IL-6 mediates hypoferremia of inflammation by inducing the synthesis of the iron regulatory hormone hepcidin. J Clin Invest. 2004;113(9):1271-1276."
    doi: "10.1172/JCI200420945"
    pmid: "15124018"
    url: "https://doi.org/10.1172/JCI200420945"
  - id: ganz-2019-acd-iron
    type: peer-reviewed
    cite: "Ganz T. Anemia of Inflammation. N Engl J Med. 2019;381(12):1148-1157."
    doi: "10.1056/NEJMra1916038"
    pmid: "31532961"
    url: "https://doi.org/10.1056/NEJMra1916038"
cross_links:
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin is the central molecular effector of ACD: IL-6 → STAT3 → hepcidin → ferroportin degradation → iron sequestration in macrophages/hepatocytes → hypoferremia → iron-restricted erythropoiesis; hepcidin pathway inhibitors (anti-HJV, ERFE mimetics) under development for ACD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the primary upstream driver of ACD: IL-6 from macrophages in infection/autoimmune disease/malignancy → STAT3 → hepcidin → ferroportin degradation → iron-restricted erythropoiesis; IL-6 also suppresses EPO production → blunted erythropoietic response."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO production is suppressed in ACD by TNF-α/IL-1β/IFN-γ and EPO-R signaling is blunted by inflammatory cytokines → EPO hyporesponsiveness; ESAs (epoetin, darbepoetin) are used in CKD-ACD with Hgb target 10-11.5 g/dL; HIF-PHIs restore EPO while suppressing hepcidin."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "CKD anemia combines EPO deficiency (from peritubular cell loss) with ACD-driven hepcidin elevation and functional iron deficiency; target Hgb 10-11.5 g/dL with ESA + IV iron; HIF-PHIs (roxadustat) treat CKD anemia by restoring EPO and suppressing hepcidin simultaneously."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin is the cellular target of hepcidin in ACD; IL-6 → hepcidin → FPN internalization → iron trapping in macrophages and enterocytes → hypoferremia → iron-restricted erythropoiesis; FPN is also the therapeutic target — anti-HJV antibodies and ERFE mimetics restore FPN."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 links chronic infection to ACD: IL-12 → IFN-γ + TNF-α → macrophage activation → IL-6 → hepcidin; IL-12-driven Th1 inflammation is characteristic of TB, HIV, and leishmaniasis; blocking IL-12 (ustekinumab) partially attenuates ACD but increases infection risk."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "TB is a major cause of ACD: MTB infection → sustained IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency; ACD severity tracks TB activity; successful TB treatment restores haemoglobin; IL-12/IFN-γ activation is the predominant immune driver."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a major driver of ACD in sub-Saharan Africa: chronic viral replication + immune activation → IL-6 + IFN-γ → hepcidin elevation → functional iron deficiency; AZT directly suppresses erythropoiesis; ACD severity tracks viral load and CD4 depletion."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "Visceral leishmaniasis causes severe ACD: chronic Leishmania infection drives IL-6 + IFN-γ + TNF-α → hepcidin → hypoferremia; BM infiltration, hypersplenism, and haemolysis compound VL anemia; successful L-AmB treatment eliminates inflammatory stimulus and resolves ACD."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Anemia of chronic disease and IDA are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but ACD has normal/high ferritin with hepcidin-trapped macrophage iron, while IDA has low ferritin from true depletion; combined ACD+IDA is common."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive anemia of chronic disease: inflammatory IL-6 raises hepcidin, which degrades macrophage ferroportin so recycled iron from senescent red cells stays locked inside (reticuloendothelial block); serum iron falls while macrophage and ferritin iron stores rise."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Rheumatoid arthritis is a prototypical cause of anemia of chronic disease: sustained IL-6 and inflammation raise hepcidin, sequestering iron and blunting erythropoiesis, so anemia tracks disease activity; effective immunosuppression (IL-6 blockade, DMARDs) often corrects it."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia of chronic disease blunts red-cell production several ways: inflammatory cytokines suppress erythropoietin and its marrow response, shorten erythrocyte survival, and via hepcidin lock iron from red cells—a typically normocytic anemia that resists oral iron."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Anemia is the commonest systemic complication of inflammatory bowel disease, usually mixed: gut inflammation raises hepcidin while bleeding and poor absorption add iron deficiency—so IBD anemia needs both inflammation control and iron repletion."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Lupus commonly causes anemia of chronic disease via systemic inflammation, but parse the cause: SLE also produces autoimmune hemolytic anemia, renal-failure anemia, and drug effects, so falling hemoglobin needs sorting inflammatory from hemolytic and renal mechanisms."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anemia of chronic disease is about iron sequestration: inflammation raises hepcidin, which traps iron inside macrophages and blocks gut absorption, so iron is abundant but unavailable—a 'functional iron deficiency' distinct from true iron-deficiency anemia."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Anemia of chronic disease and MDS both cause anemia but differ: ACD is inflammation-driven iron sequestration with adequate marrow, while MDS is clonal marrow failure with dysplasia—so anemia not explained by inflammation or iron warrants marrow examination for MDS."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Multiple myeloma commonly presents with anemia of chronic disease: the tumor's IL-6 drives hepcidin and inflammatory anemia, compounded by marrow replacement and renal failure, so unexplained anemia with high ESR and bone pain should prompt evaluation for myeloma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Anemia of chronic disease blunts the bone marrow: inflammatory cytokines suppress erythroid progenitors and dampen their response to erythropoietin, so the marrow underproduces red cells despite adequate stores—a hypoproliferative anemia driven from outside the marrow."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Transferrin distinguishes anemia of chronic disease from iron deficiency: inflammation lowers transferrin (low TIBC) while ferritin stays high, the mirror image of iron-deficiency anemia's high transferrin and low ferritin—so these proteins separate the two commonest anemias."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Anemia of chronic disease is anemia manufactured by the immune system: sustained inflammation raises hepcidin and cytokines that sequester iron and curb red-cell production, an evolutionary defense (starving microbes of iron) that becomes maladaptive in chronic illness."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver runs the anemia of chronic disease: it makes hepcidin, the master iron-regulating hormone, in response to inflammation, and this hepcidin surge locks iron away from red-cell production—so a healthy liver's signal becomes the cause of the anemia."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Anemia and heart failure feed each other: inflammation in heart failure raises hepcidin and blunts erythropoiesis, while the resulting anemia forces the failing heart to work harder—so this anemia worsens symptoms and prognosis in HF."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α helps drive the anemia of chronic disease: this inflammatory cytokine directly suppresses red-cell production in the marrow and blunts the response to erythropoietin, so anti-TNF therapy for inflammatory disease can also lift the accompanying anemia."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Anemia of inflammation is orchestrated by hepatocytes: in response to IL-6 they pump out hepcidin, the hormone that locks iron inside cells and starves red-cell production—so the liver's iron-master cell sits at the center of this anemia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Inflammation overrides the HIF oxygen-sensing that should fix anemia: low oxygen normally stabilizes HIF to boost erythropoietin and suppress hepcidin, but inflammatory signals blunt this response—so anemia of chronic disease persists despite the need for red cells."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen helps drive anemia of inflammation: its macrophages recycle iron from old red cells but, under inflammatory hepcidin, hoard it instead of returning it—while also clearing red cells faster, compounding the anemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Anemia of chronic disease starves tissues of oxygen: with fewer red cells the blood carries less oxygen, and the body senses the hypoxia and tries to compensate, though inflammation blunts the usual erythropoietin rise that would restore delivery."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney's anemia signal is blunted in chronic disease: kidneys make erythropoietin in response to low oxygen, but inflammatory cytokines dull both the hormone's output and the marrow's response, a key reason the anemia persists."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anemia of chronic disease lowers hemoglobin without true iron lack: locked-away iron starves developing red cells, so each carries less hemoglobin, giving the mild normocytic anemia that ferritin (high here) helps tell apart from iron deficiency."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Anemia of chronic disease starts at the gut: inflammation's hepcidin destroys ferroportin on the small intestine's iron-exporting cells, so dietary iron is absorbed but trapped in the lining, never reaching the blood—why oral iron often fails here."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Chronic anemia makes the heart work overtime: with less hemoglobin to carry oxygen, the heart pumps faster and harder, so in older or already-strained hearts this anemia can tip toward high-output failure and worsen heart disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Interferon-gamma helps lock iron away in chronic disease: this Th1 cytokine, high in chronic infections like TB, drives macrophages to hoard iron and blunts red-cell production, deepening the anemia of inflammation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The marrow tells the story under the microscope: a Prussian-blue stain shows iron trapped in macrophages but missing from developing red cells, the light-microscopy signature that separates anemia of inflammation from true iron deficiency."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper is needed to move iron: ceruloplasmin, a copper enzyme, oxidizes iron for loading onto transferrin, so copper deficiency causes an anemia that can be mistaken for the anemia of chronic disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 is the switch that locks iron away: IL-6 signals through it to switch on hepcidin in the liver, the molecular relay that turns inflammation into the iron-restricted anemia of chronic disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows where the iron is hidden: macrophages of the spleen and marrow swell with ferritin and hemosiderin granules, hoarding the iron that hepcidin won't let them release to the hungry red-cell precursors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D can ease the iron block: it suppresses hepcidin, so deficiency — common in the chronic inflammatory diseases that cause this anemia — tightens the iron restriction, and repletion modestly loosens it."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Inflammatory bowel disease is a classic cause: chronic gut inflammation drives the IL-6 and hepcidin that lock away iron, so the large intestine's disease shows up as the anemia in the blood."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The same inflammation that drops the red cells lifts the platelets: IL-6 drives both hepcidin and thrombopoiesis, so a reactive thrombocytosis often travels alongside the anemia of chronic disease."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Anemia keeps company with a falling albumin: both are negative acute-phase reactants, suppressed as the liver reprioritizes its output during chronic inflammation, so the two markers sink together as a measure of disease burden."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Helper T cells light the fuse: their interferon-gamma and the cytokines they orchestrate drive the hepcidin surge and blunt the marrow's response, the adaptive-immune arm of the anemia's inflammatory cause."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Blocking the cytokine can lift the anemia: antibodies against IL-6 (tocilizumab) cut the hepcidin surge and correct the anemia of inflammatory disease, and anti-hepcidin agents are in development to free the trapped iron."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Even fat can cause it: obesity is a chronic low-grade inflammatory state whose raised IL-6 and hepcidin lock iron away, giving many obese people a mild functional iron deficiency and blunted anemia of inflammation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "It shows, faintly, on the skin: the chronic, usually mild anemia produces the pallor of conjunctivae, palms, and nail beds that, with fatigue, is often the only outward clue to the iron locked away inside."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Repeated malaria grinds out anemia of inflammation: the parasite's chronic immune activation drives hepcidin up to lock away iron, compounding the hemolysis and marrow suppression that make malarial anemia a leading childhood killer."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help hide the iron: in chronic infection they release lactoferrin that scavenges iron away from microbes, and their inflammatory signals push hepcidin up, reinforcing the iron sequestration behind the anemia."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Cancer wears two anemia hats at once: a colorectal tumor both bleeds to cause iron deficiency and drives inflammatory hepcidin to lock away stores, so its anemia is often a mixed picture and a clue prompting the search for the tumor."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation runs through a master switch: NF-κB activated by inflammatory signals turns on the IL-6 that drives hepcidin, the upstream hub linking chronic disease to the iron-locking that starves red-cell production."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Acute inflammation drops iron within hours: sepsis triggers a hepcidin surge that pulls iron out of the blood, an evolved defense to starve microbes that simultaneously chokes erythropoiesis into the anemia of critical illness."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "T cells help suppress the marrow: interferon-gamma from cytotoxic and helper T cells directly inhibits erythroid progenitors, an immune brake on red-cell production layered on the hepcidin-driven iron restriction."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Smokers' lungs inflame the marrow too: the chronic systemic inflammation of COPD raises hepcidin and cytokines that blunt erythropoiesis, so a meaningful share of COPD patients carry an anemia of chronic disease that worsens their breathlessness."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "A chronic leukemia drives the same anemia: the inflammatory cytokine output of chronic myeloid leukemia and its crowding of the marrow produce an anemia of chronic disease on top of the malignancy's own marrow takeover."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Chronic inflammation layers onto the hemolysis: beyond the relentless red-cell destruction, the ongoing vaso-occlusive inflammation of sickle cell disease raises hepcidin and cytokines that add an anemia-of-chronic-disease component to the baseline anemia."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Another inflammatory arthritis drives it: the sustained IL-6 of active ankylosing spondylitis raises hepcidin and blunts erythropoiesis, producing an anemia of chronic disease that tracks with disease activity."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Chronic viral infection feeds it: persistent hepatitis C inflammation, compounded by a cirrhotic liver and hypersplenism, raises hepcidin and suppresses red-cell production into an anemia of chronic disease."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Cancer and hormone therapy both contribute: advanced prostate cancer's inflammation and marrow metastases, plus the androgen-deprivation therapy that withdraws erythropoietic drive, combine into an anemia of chronic disease."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Its joint inflammation drains the blood: the sustained IL-6 and inflammatory drive of active psoriatic arthritis raises hepcidin and blunts erythropoiesis, producing an anemia of chronic disease in poorly controlled patients."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Lymphoma stokes the inflammatory anemia: the cytokine output and marrow involvement of aggressive lymphomas like DLBCL raise hepcidin and suppress red-cell production, a frequent cause of anemia of chronic disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its fatigue compounds low mood: the persistent tiredness and reduced oxygen delivery of anemia of chronic disease worsen the fatigue and functional decline that feed depression in chronically ill patients."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The liver runs its central switch: hepatic hepcidin, raised by inflammation, locks iron away from red-cell production, and chronic gut inflammation and bleeding compound the anemia of chronic disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones tune red-cell output: erythropoietin is an endocrine signal, and hypothyroidism, hypogonadism and hypopituitarism each blunt erythropoiesis, overlapping with the picture of anemia of chronic disease."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "A chronic gastric infection saps the blood: persistent Helicobacter pylori gastritis drives both iron-deficiency and an inflammatory anemia, and its eradication can correct otherwise refractory anemia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Pallor is its visible sign: anemia of chronic disease shows as pallor of the skin, conjunctivae and nail beds, a bedside clue that prompts the search for an underlying chronic illness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Low oxygen delivery dulls the mind and stirs the legs: the anemia contributes to fatigue and impaired concentration, and the iron-restriction underlying it can exacerbate restless legs syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy compounds it: when chronic inflammatory disease coexists with the physiological dilutional anemia of pregnancy, the combined anemia can affect maternal wellbeing and fetal outcomes."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Low oxygen-carrying capacity raises the cardiac workload: chronic anemia drives compensatory tachycardia and a high-output state, aggravating ischaemia and, over time, straining the heart."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The reticuloendothelial system drives it: splenic and nodal macrophages trap recycled iron behind hepcidin, the core mechanism that starves the marrow of iron for erythropoiesis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Lung disease usually raises red cells via hypoxic erythropoietin, but in COPD the systemic inflammation blunts that response, so anemia of chronic disease can paradoxically appear instead."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It overlaps with the anaemia of kidney disease: chronic kidney disease causes a closely related anaemia through erythropoietin deficiency and inflammatory hepcidin excess, blurring the line with anaemia of chronic disease."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Chronic joint inflammation drives it: rheumatoid arthritis and other inflammatory arthritides raise IL-6 and hepcidin, making anaemia of chronic disease their commonest extra-articular feature."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "A chronic infection that causes it: tuberculosis sustains the inflammatory cytokines that block iron use, making anaemia of chronic disease a frequent finding in active TB."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver sets the iron trap: IL-6 from inflammation drives hepatocytes in the liver lobule to make hepcidin, the master regulator that locks iron inside macrophages and starves erythropoiesis — the core of anaemia of chronic disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cancer anaemia comes from both sides: malignancy itself drives anaemia of chronic disease through inflammation, while chemotherapy adds marrow suppression — managed with iron, erythropoiesis-stimulating agents or transfusion."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Two non-deficiency anaemias contrasted: anaemia of chronic disease comes from inflammatory iron sequestration with a working marrow, whereas aplastic anaemia is failure of the marrow itself — both with normal iron stores."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Chronic anaemia strains the heart: persistent low haemoglobin forces a higher cardiac output, and in heart failure or CKD the anaemia of chronic disease worsens myocardial workload and outcomes."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Anaemia of inflammation in infection: severe COVID-19 raises IL-6 and hepcidin, sequestering iron in macrophages and causing the anaemia of inflammation typical of chronic-disease anaemia."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Anaemia of a chronic marrow disease: myelofibrosis causes anaemia through marrow fibrosis and splenic sequestration compounded by an inflammatory, hepcidin-driven component, blending with the anaemia of chronic disease."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "A textbook inflammatory anaemia: giant-cell arteritis produces a marked anaemia of chronic disease with very high ESR/CRP and reactive thrombocytosis, the IL-6-driven hepcidin response a clue to the diagnosis."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Multifactorial anaemia of autoimmunity: systemic sclerosis causes anaemia through chronic inflammation (hepcidin) compounded by GI blood loss from gastric antral vascular ectasia and renal involvement."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Chronic viral inflammation lowers haemoglobin: persistent hepatitis B drives an inflammatory, hepcidin-mediated anaemia of chronic disease, compounded in cirrhosis by hypersplenism and bleeding."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Hepcidin gates the gut: inflammation-driven hepcidin blocks ferroportin on the duodenal enterocytes of the intestinal epithelium, trapping dietary iron and starving erythropoiesis even when body iron stores are adequate."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Cancer-related anaemia: solid tumours like ovarian cancer drive IL-6 and hepcidin to produce an anaemia of inflammation, compounded by chemotherapy myelosuppression and bleeding."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "An underrecognised anaemia: the chronic low-grade inflammation and kidney disease of type 2 diabetes contribute to an anaemia of inflammation, blunting erythropoietin and restricting iron through hepcidin."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Hepcidin inducer: IL-1β from activated macrophages stimulates hepcidin production and suppresses erythropoiesis, a key inflammatory driver of the iron-restricted anaemia of inflammation."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome source: NLRP3-inflammasome activation matures the IL-1β that, with IL-6, sustains the hepcidin-driven iron sequestration of anaemia of chronic disease."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Vasculitic anaemia: the systemic inflammation of ANCA-associated vasculitis drives an anaemia of chronic disease, often compounded by renal failure and alveolar haemorrhage."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Hepcidin and erythroid block: activin/BMP signalling induces hepcidin and impairs erythroid maturation, a pathway distinct from IL-6 that activin ligand-traps (luspatercept) target to relieve inflammatory anaemia."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microbial hepcidin induction: TLR4 sensing of bacterial products directly drives hepatocyte hepcidin in infection, locking away iron as part of the host iron-withholding defence that produces anaemia of inflammation."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Nutritional immunity: S100A8/A9 (calprotectin) sequesters iron and other metals from pathogens during inflammation, part of the same metal-withholding host response whose chronic activation causes anaemia of chronic disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Erythroid maturation block: TGF-β superfamily signalling (alongside activin) suppresses late-stage erythroid maturation in anaemia of chronic disease, contributing to the ineffective erythropoiesis that ligand traps like luspatercept relieve."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Eryptosis: inflammatory cytokines and oxidative stress in chronic disease trigger caspase-mediated eryptosis (red-cell suicidal death), shortening erythrocyte survival and compounding the anaemia beyond iron restriction."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon marrow suppression: in chronic viral and autoimmune disease, type I interferon directly suppresses erythroid progenitors, an interferon-driven arm of anaemia of chronic disease distinct from the hepcidin-iron axis."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "HIF-PHI therapy: prolyl-hydroxylase (EGLN/PHD) inhibitors like roxadustat stabilise HIF to raise endogenous erythropoietin and lower hepcidin, treating anaemia of chronic disease by targeting the oxygen-sensing pathway upstream of both."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Shortened red-cell lifespan: the oxidative stress of chronic inflammation, partly from xanthine-oxidase-derived reactive oxygen species, damages erythrocytes and hastens their removal by macrophages, a second mechanism of anaemia layered on iron sequestration."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "DAMP amplification: DAMPs signalling through RAGE sustain the NF-κB-driven cytokine output of chronic inflammation that keeps IL-6 and hepcidin elevated, feeding the iron-restriction that defines anaemia of chronic disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Hepcidin transcription: the BMP-SMAD pathway acting through SMAD4 is the principal transcriptional driver of hepcidin (already mapped), and inflammation amplifies it to lock iron away in the anaemia of chronic disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "EPO-resistant erythropoiesis: inflammatory cytokines and erythropoietin both signal through JAK kinases, and chronic JAK-STAT cytokine signalling blunts the erythropoietin response, contributing to the EPO-resistant anaemia of chronic disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Erythroid survival: erythropoietin signals through PI3K-AKT to support erythroid-progenitor survival, and the blunted EPO response of chronic inflammation weakens this pro-survival signal, deepening the anaemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory hepcidin induction: TLR (TLR4 mapped) and IL-1 signalling through MyD88 helps drive the hepcidin (mapped) induction that sequesters iron in anaemia of chronic disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Erythroid suppression: IFN-γ (mapped) signalling through STAT1 directly inhibits erythroid-progenitor proliferation, blunting the marrow response that would otherwise correct the anaemia."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Progenitor apoptosis: inflammatory cytokines tip the BCL-2 balance toward apoptosis of erythroid progenitors (caspase-3 mapped), reducing red-cell output in anaemia of inflammation."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EPO-driven ERK-MAPK signalling promotes erythroid progenitor proliferation (EPO mapped); the blunted EPO responsiveness of ACD impairs this proliferative drive."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-regulated translation and iron-sensing govern erythroid maturation, coupling the iron restriction of ACD to ineffective erythropoiesis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restrains the PI3K-AKT signalling downstream of the erythropoietin receptor that drives erythroid survival and expansion, a node in the impaired EPO response of ACD."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage inflammatory activation that drives the hepcidin-mediated iron sequestration of anemia of chronic disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the chronic inflammatory tone that sustains the hepcidin response and iron restriction of anemia of chronic disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2-driven monocyte recruitment sustains the inflammatory macrophage activity that underlies the iron sequestration of anemia of chronic disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the oxidative-stress and survival programs of erythroid progenitors that are suppressed in the inflammatory milieu of anemia of chronic disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA) signaling transduces the erythropoietin survival signal in erythroid progenitors that is blunted in anemia of chronic disease (AKT already mapped)."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cell-cycle progression of erythroid progenitors is restrained by the inflammatory cytokine milieu of anemia of chronic disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the inflammatory signaling that drives the hepcidin-mediated iron sequestration of anemia of chronic disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-bearing cytotoxic lymphocytes contribute to the immune-mediated suppression of erythropoiesis in anemia of chronic disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Macrophage autophagy participates in the iron-recycling and erythrophagocytosis dysregulated in anemia of chronic disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the erythroid and macrophage iron-metabolism adaptation of anemia of chronic disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of cytokine and EPO receptors participates in the suppressed erythropoiesis of anemia of chronic disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte and macrophage activation contributes to the inflammatory iron sequestration of anemia of chronic disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the inflammatory and erythroid gene programs of anemia of chronic disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the bone-marrow erythroid-niche interactions relevant to anemia of chronic disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory milieu driving the hepcidin response of anemia of chronic disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the chronic inflammation driving the anemia of chronic disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory milieu of the anemia of chronic disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the erythroid and inflammatory gene programs of the anemia of chronic disease."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen erythropoiesis: testosterone stimulates erythropoietin production and erythroid progenitors, so the hypogonadism common in chronic illness and aging deepens the anemia of chronic disease beyond the inflammatory iron restriction."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Erythroid support: IGF-1 promotes the proliferation and survival of erythroid progenitors, and its suppression in chronic illness and malnutrition contributes to the blunted erythropoiesis of the anemia of chronic disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative red-cell loss: the inflammatory oxidative milieu accelerates eryptosis and shortens red-cell survival, and the NRF2 antioxidant response modulates this stress, adding a haemolytic component to the anemia of chronic disease."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences in erythropoiesis: sex hormones modulate red-cell production, with testosterone (already mapped) stimulating and estrogen restraining erythropoiesis, contributing to the different baseline haemoglobin against which the anemia of chronic disease develops."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune-regulatory tuning: the anti-inflammatory cytokine IL-10 can paradoxically raise hepcidin (already mapped) and modulate macrophage iron handling, part of the complex cytokine balance that shapes the anemia of chronic disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Nutritional immunity: like iron (already mapped), zinc is redistributed away from the plasma during inflammation as part of nutritional immunity, and the resulting hypozincaemia can further impair the erythropoiesis blunted in chronic disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the underlying inflammatory disease contribute to the cytokine milieu (IL-6, TNF and IL-1 already mapped) that raises hepcidin (already mapped) and blunts erythropoiesis in the anemia of chronic disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Macrophage polarisation: IL-4 polarises macrophages (already mapped) toward an iron-recycling, anti-inflammatory phenotype opposing the iron-sequestering inflammatory state, so the M1/M2 balance shapes the iron handling of the anemia of chronic disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Erythropoietic suppression: nitric oxide generated in inflammation impairs erythroid progenitor proliferation and shortens red-cell survival, adding to the hepcidin-driven iron restriction (already mapped) in the anemia of chronic disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 iron-recycling macrophages: IL-13, with IL-4 (already mapped), polarises the macrophages (already mapped) toward the anti-inflammatory iron-recycling phenotype that opposes the iron-sequestering inflammatory state of the anemia of chronic disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Trace-metal redistribution: the inflammation of the anemia of chronic disease redistributes zinc as well as iron (already mapped), the hypozincaemia of inflammation accompanying the hypoferraemia in the acute-phase response."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "A common cause: inflammatory bowel disease is a frequent cause of the anemia of chronic disease (IL-6 and hepcidin already mapped), often combined with iron-deficiency anaemia from chronic gastrointestinal blood loss."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Malignancy cause: Hodgkin lymphoma and other cancers commonly cause the anemia of chronic disease through their cytokine (IL-6 already mapped) drive of hepcidin (already mapped) and the marrow involvement."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and hepcidin: leptin modulates the hepcidin (already mapped) and erythropoiesis, linking the obesity (already mapped)-related inflammation to the iron and red-cell dysregulation of the anemia of chronic disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine axis: adiponectin, with leptin (already mapped), is part of the adipokine axis of the obesity-related and inflammatory dysregulation of iron and erythropoiesis in the anemia of chronic disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity-related inflammation contributing to the hepcidin (already mapped) and iron dysregulation of the anemia of chronic disease."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "IBD anemia: the inflammatory bowel disease is a common cause of the anemia of chronic disease (the inflammation-hepcidin already mapped), compounded by the iron-deficiency blood loss."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepcidin-producing liver: the liver (the hepatocytes already mapped) produces the hepcidin (already mapped) under the IL-6 (already mapped) drive, the endocrine hub of the iron sequestration of the anemia of chronic disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate inflammatory NK: the NK cells (perforin already mapped), via their IFN-γ (already mapped), contribute to the inflammatory cytokine milieu that drives the hepcidin (already mapped) of the anemia of chronic disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu underlying the anemia of chronic disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation that drives the hepcidin (already mapped) iron sequestration of the anemia of chronic disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the diverse chronic inflammatory conditions underlying the anemia of chronic disease."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (already mapped) of the chronic infections, autoimmunity and myeloma (already mapped) that drive the inflammation of the anemia of chronic disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) and sustain the chronic inflammatory response (IL-6 and TNF already mapped) that drives the anemia of chronic disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Inflammatory mast cells: the mast cells contribute to the chronic inflammatory milieu (IL-6 and TNF already mapped) that drives the hepcidin (already mapped) induction of the anemia of chronic disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the chronic inflammatory response of the infections and autoimmunity that drive the anemia of chronic disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the myeloid activation that sustains the inflammatory cytokine (IL-6 already mapped) drive of the anemia of chronic disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the chronic inflammatory response driving the anemia of chronic disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the immune complexes of the autoimmune and infectious drivers of the anemia of chronic disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Inflammatory matricellular: osteopontin, a pro-inflammatory matricellular cytokine, is part of the chronic-inflammatory milieu (with IL-6 and TNF-α already mapped) that suppresses the erythropoiesis of the anemia of chronic disease."
---

# Anemia of Chronic Disease

## Overview

**Anemia of chronic disease (ACD)**, also known as **anemia of inflammation (AI)**, is the **second most common anemia worldwide** after iron deficiency anemia, affecting hundreds of millions of people — predominantly those with chronic infection, autoimmune disease, malignancy, and chronic kidney disease (CKD) [^weiss-2005-acd-review]. Unlike iron deficiency anemia (IDA), ACD occurs despite **adequate or elevated iron stores**: the iron is present but functionally unavailable — sequestered within macrophages and hepatocytes by hepcidin-mediated ferroportin degradation, unable to reach the bone marrow for erythropoiesis.

The central molecular mechanism is the **IL-6 → STAT3 → hepcidin → ferroportin axis** [^nemeth-2004-il6-hepcidin]:
1. Chronic inflammation → sustained IL-6 production from macrophages/monocytes
2. IL-6 → hepatocyte STAT3 → HAMP promoter → elevated hepcidin (3-10× normal)
3. High hepcidin → ferroportin internalization/lysosomal degradation → iron trapping in macrophages and hepatocytes
4. Bone marrow iron shortage → iron-restricted erythropoiesis → normocytic or microcytic anemia

ACD is compounded by additional inflammation-driven mechanisms: **EPO hyporesponsiveness** (IFN-γ, TNF-α blunt EPO signaling on erythroid progenitors), **shortened RBC lifespan** (increased macrophage erythrophagocytosis), and **suppressed EPO production** (TNF-α, IL-1β inhibit renal EPO synthesis). These combined effects make ACD resistant to iron supplementation alone and frequently require treatment of the underlying disease.

**Clinical features:**
- Usually **mild to moderate** anemia (Hgb 8–11 g/dL); rarely severe unless compounded by bleeding, hemolysis, or advanced CKD
- Typically **normocytic, normochromic** (MCV 80–100 fL); can become microcytic if iron stores become truly depleted (ACD+IDA overlap)
- Develops **gradually** over weeks to months of chronic inflammation
- Symptom burden correlates with Hgb level and the underlying condition (fatigue, dyspnea, reduced quality of life)

## Structure

### Pathophysiological framework

**Multi-pathway model of ACD:**

| Mechanism | Driver | Effect on Erythropoiesis |
|:----------|:-------|:------------------------|
| Iron sequestration (hepcidin-mediated) | IL-6 → STAT3 → hepcidin → ferroportin degradation | Functional iron deficiency — stores elevated but unavailable |
| EPO suppression | TNF-α, IL-1β, IFN-γ → ↓renal EPO synthesis; direct CKD effect | Insufficient EPO stimulus for erythroid expansion |
| EPO hyporesponsiveness | IFN-γ, TNF-α → blunted EPO-R signaling; iron shortage limits response | Erythroid progenitors fail to respond to available EPO |
| Shortened RBC lifespan | Macrophage activation → increased erythrophagocytosis; low-grade hemolysis | Reduced RBC survival (120 days → ~80 days in ACD) |
| Inhibited erythroid differentiation | IFN-γ → apoptosis of BFU-E/CFU-E in bone marrow | Reduced erythroid colony formation |

**Iron compartmentalization in ACD (vs. IDA):**

| Iron Parameter | ACD | IDA | ACD+IDA |
|:--------------|:----|:----|:--------|
| Serum iron | Low | Low | Low |
| TIBC/transferrin | Low or normal | High | Low or normal |
| Transferrin saturation | Low-normal | Very low | Low |
| Serum ferritin | Normal to high | <30 ng/mL | Low-normal (acute phase) |
| Soluble TfR (sTfR) | Low-normal | High | High |
| sTfR/log ferritin index | <1 | >2 | >2 |
| Hepcidin | High | Very low | Variable |
| Reticulocyte Hgb (CHr) | Low | Low | Low |
| Bone marrow iron | Normal to high | Absent | Low |

**Key diagnostic pearl:** Ferritin is an acute-phase reactant — it rises during inflammation even when iron stores are genuinely low, masking IDA in the ACD setting. The **sTfR/log ferritin index** (>2 indicates an IDA component) is less affected by inflammation and is the best single test to detect concurrent IDA in an inflamed patient.

## Function

### Nutritional immunity — the adaptive role of ACD

The hepcidin-driven iron sequestration of ACD is not purely pathological. **Nutritional immunity** is the evolutionary strategy of withholding iron from pathogens (bacteria, fungi, intracellular parasites require iron for growth) by reducing circulating transferrin-bound iron. In acute infection, ACD-like hypoferremia is a **deliberate innate immune mechanism**: iron restriction limits pathogen replication, while the bone marrow tolerates temporary anemia better than systemic bacteremia [^ganz-2019-acd-iron].

This adaptive rationale explains why **aggressive iron supplementation during active infection can be harmful** — parenteral iron in bacteremic patients increases free iron → pathogen growth → worsened outcomes (demonstrated in neonatal malaria trials and suggested in critical illness studies).

### Disease associations

**Infections:**
- Chronic bacterial infections (TB, osteomyelitis, endocarditis)
- HIV, hepatitis C, parasitic infections (malaria, visceral leishmaniasis)

**Autoimmune/inflammatory diseases:**
- **Rheumatoid arthritis** — most studied ACD association; Hgb inversely correlates with ESR/CRP; treat underlying disease (DMARDs); tocilizumab (anti-IL-6R) rapidly reverses ACD via hepcidin suppression
- **SLE** — multifactorial anemia (ACD + autoimmune hemolytic anemia + drug effects)
- **IBD (Crohn's/UC)** — ACD + true IDA (mucosal bleeding) coexist; ferritin unreliable; sTfR index + CRP-adjusted ferritin thresholds used; IV iron (ferric carboxymaltose) preferred
- **AOSD (adult-onset Still's disease)** — dramatic ACD with hyperferritinemia; macrophage activation also contributes
- **Vasculitis (GCA, AAV)** — IL-6-driven ACD; resolves with immunosuppression

**CKD/ESRD:**
- CKD-related anemia = ACD + EPO deficiency (uremic suppression of renal EPO synthesis) + shortened RBC lifespan
- Most common indication for ESA therapy (KDIGO target: Hgb 10-11.5 g/dL)

**Malignancy:**
- Cancer-related ACD affects ~40% of cancer patients
- Compounded by: bone marrow invasion, chemotherapy toxicity, gastrointestinal bleeding, hemolysis

## Pathology

### Diagnosis

**Diagnostic approach:**
1. Confirm anemia and assess severity/morphology (CBC, peripheral smear)
2. Establish underlying chronic disease context (clinical + CRP/ESR/ferritin)
3. Iron studies: serum iron + TIBC + transferrin saturation + serum ferritin
4. Distinguish ACD vs. IDA vs. ACD+IDA:
   - ACD: ferritin normal/high + low TSAT + normal sTfR + elevated CRP
   - IDA: ferritin <30 ng/mL + very low TSAT + high sTfR + normal CRP
   - ACD+IDA: "normal" ferritin may mask true IDA; sTfR/log ferritin index >2 indicates IDA
5. Additional: reticulocyte count, reticulocyte hemoglobin (CHr), soluble TfR
6. Bone marrow biopsy with Prussian blue stain: gold standard (stainable iron present in macrophages but absent from erythroid precursors = ACD)

### Treatment [^weiss-2005-acd-review]

**1. Treat the underlying cause — most effective strategy:**
- RA/autoimmune disease: DMARDs, IL-6R blockade (tocilizumab) → IL-6 falls → hepcidin falls → iron mobilizes → Hgb rises within 4-8 weeks
- Infection: Eradicate organism → hepcidin normalization → anemia resolves
- IBD: Induce remission with biologics/5-ASA
- Cancer: Chemotherapy/surgery targeting tumor → inflammation subsides

**2. Iron supplementation:**
- **Oral iron:** Minimally effective in pure ACD (hepcidin degrades intestinal ferroportin → absorbed iron cannot exit enterocyte); useful only if concurrent true IDA
- **IV iron (ferric carboxymaltose, iron sucrose, ferric gluconate):** Bypasses intestinal absorption; effective in CKD-related anemia and IBD-related anemia; less effective in pure ACD without true iron depletion
- KDIGO threshold for IV iron in CKD: ferritin <500 ng/mL + TSAT <30% in ESA-treated patients

**3. Erythropoiesis-stimulating agents (ESAs):**
- **Epoetin alfa, darbepoetin alfa** — stimulate erythroid progenitor proliferation via EPO receptor
- **Indications:** CKD-related anemia (Hgb <10 g/dL); chemotherapy-related anemia when cure is not expected
- **Target Hgb:** 10-11.5 g/dL; avoid >13 g/dL (↑VTE and CV events — FDA black box)
- **ESA hyporesponsiveness:** Functional iron deficiency (persistent high hepcidin) is the most common cause → co-administer IV iron
- **Not indicated:** Non-chemotherapy cancer anemia, surgical anemia, anemia of aging

**4. Transfusion:**
- For severe symptomatic anemia (Hgb <7-8 g/dL) or rapid-onset cardiovascular compromise
- Leukoreduced PRBCs; avoid overtransfusion; restrictive strategy (Hgb <7 g/dL trigger in stable patients)

**5. Emerging therapies:**
- **HIF prolyl hydroxylase inhibitors (HIF-PHIs):** Roxadustat, daprodustat, vadadustat — stabilize HIF-2α → EPO synthesis + hepcidin suppression; FDA-approved for dialysis CKD-anemia (roxadustat REMS program 2023); approved broadly in EU/China
- **Luspatercept (Reblozyl):** Activin receptor ligand trap → promotes late-stage erythroid maturation; FDA-approved for MDS-related anemia (2020) and beta-thalassemia; phase 2 studies in ACD/CKD
- **Hepcidin pathway antagonists (investigational):** Anti-HJV antibodies, ERFE mimetics, anti-TMPRSS6 siRNA; clinical trials ongoing for ACD

## Connections

- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepcidin is the central molecular effector of ACD: IL-6 → STAT3 → hepcidin → ferroportin degradation → iron sequestration in macrophages/hepatocytes → hypoferremia → iron-restricted erythropoiesis; hepcidin pathway inhibitors (anti-HJV, ERFE mimetics) under development for ACD.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the primary upstream driver of ACD: IL-6 from macrophages in infection/autoimmune disease/malignancy → STAT3 → hepcidin → ferroportin degradation → iron-restricted erythropoiesis; IL-6 also suppresses EPO production → blunted erythropoietic response.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO production is suppressed in ACD by TNF-α/IL-1β/IFN-γ and EPO-R signaling is blunted by inflammatory cytokines → EPO hyporesponsiveness; ESAs (epoetin, darbepoetin) are used in CKD-ACD with Hgb target 10-11.5 g/dL; HIF-PHIs restore EPO while suppressing hepcidin.
- `connects-to` → **[CKD](../ckd/README.md)** — CKD anemia combines EPO deficiency (from peritubular cell loss) with ACD-driven hepcidin elevation and functional iron deficiency; target Hgb 10-11.5 g/dL with ESA + IV iron; HIF-PHIs (roxadustat) treat CKD anemia by restoring EPO and suppressing hepcidin simultaneously.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin is the cellular target of hepcidin in ACD; IL-6 → hepcidin → FPN internalization → iron trapping in macrophages and enterocytes → hypoferremia → iron-restricted erythropoiesis; FPN is also the therapeutic target — anti-HJV antibodies and ERFE mimetics restore FPN.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 inflammation is the predominant immune mechanism linking chronic intracellular infection to ACD: IL-12 → IFN-γ + TNF-α → IL-6 → hepcidin; chronic IL-12/IFN-γ-driven diseases (TB, HIV, leishmaniasis) are classic ACD causes; IL-12-mediated nutritional immunity withholds iron from both pathogens and erythroid progenitors.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — TB is a leading global cause of ACD: MTB-driven IL-6 + TNF-α + IFN-γ → hepcidin elevation → functional iron deficiency and normochromic normocytic anemia; ACD severity tracks TB disease activity (smear positivity, cavitary disease); successful TB treatment typically resolves ACD within weeks to months.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a major ACD driver in sub-Saharan Africa: chronic viral replication + immune activation → elevated IL-6 + IFN-γ → hepcidin-mediated iron sequestration; AZT (zidovudine) directly suppresses erythropoiesis (bone marrow toxicity); anemia severity correlates with viral load and CD4 depletion and responds to ART.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — Visceral leishmaniasis causes severe ACD: chronic Leishmania infection drives IL-6 + IFN-γ + TNF-α → hepcidin → hypoferremia; BM infiltration, hypersplenism, and haemolysis compound VL anemia; successful L-AmB treatment eliminates inflammatory stimulus and resolves ACD.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Anemia of chronic disease and IDA are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but ACD has normal/high ferritin with hepcidin-trapped macrophage iron, while IDA has low ferritin from true depletion; combined ACD+IDA is common.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive anemia of chronic disease: inflammatory IL-6 raises hepcidin, which degrades macrophage ferroportin so recycled iron from senescent red cells stays locked inside (reticuloendothelial block); serum iron falls while macrophage and ferritin iron stores rise.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Rheumatoid arthritis is a prototypical cause of anemia of chronic disease: sustained IL-6 and inflammation raise hepcidin, sequestering iron and blunting erythropoiesis, so anemia tracks disease activity; effective immunosuppression (IL-6 blockade, DMARDs) often corrects it.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia of chronic disease blunts red-cell production several ways: inflammatory cytokines suppress erythropoietin and its marrow response, shorten erythrocyte survival, and via hepcidin lock iron from red cells—a typically normocytic anemia that resists oral iron.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Anemia is the commonest systemic complication of inflammatory bowel disease, usually mixed: gut inflammation raises hepcidin while bleeding and poor absorption add iron deficiency—so IBD anemia needs both inflammation control and iron repletion.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Lupus commonly causes anemia of chronic disease via systemic inflammation, but parse the cause: SLE also produces autoimmune hemolytic anemia, renal-failure anemia, and drug effects, so falling hemoglobin needs sorting inflammatory from hemolytic and renal mechanisms.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anemia of chronic disease is about iron sequestration: inflammation raises hepcidin, which traps iron inside macrophages and blocks gut absorption, so iron is abundant but unavailable—a 'functional iron deficiency' distinct from true iron-deficiency anemia.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Anemia of chronic disease and MDS both cause anemia but differ: ACD is inflammation-driven iron sequestration with adequate marrow, while MDS is clonal marrow failure with dysplasia—so anemia not explained by inflammation or iron warrants marrow examination for MDS.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Multiple myeloma commonly presents with anemia of chronic disease: the tumor's IL-6 drives hepcidin and inflammatory anemia, compounded by marrow replacement and renal failure, so unexplained anemia with high ESR and bone pain should prompt evaluation for myeloma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Anemia of chronic disease blunts the bone marrow: inflammatory cytokines suppress erythroid progenitors and dampen their response to erythropoietin, so the marrow underproduces red cells despite adequate stores—a hypoproliferative anemia driven from outside the marrow.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Transferrin distinguishes anemia of chronic disease from iron deficiency: inflammation lowers transferrin (low TIBC) while ferritin stays high, the mirror image of iron-deficiency anemia's high transferrin and low ferritin—so these proteins separate the two commonest anemias.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Anemia of chronic disease is anemia manufactured by the immune system: sustained inflammation raises hepcidin and cytokines that sequester iron and curb red-cell production, an evolutionary defense (starving microbes of iron) that becomes maladaptive in chronic illness.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver runs the anemia of chronic disease: it makes hepcidin, the master iron-regulating hormone, in response to inflammation, and this hepcidin surge locks iron away from red-cell production—so a healthy liver's signal becomes the cause of the anemia.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Anemia and heart failure feed each other: inflammation in heart failure raises hepcidin and blunts erythropoiesis, while the resulting anemia forces the failing heart to work harder—so this anemia worsens symptoms and prognosis in HF.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α helps drive the anemia of chronic disease: this inflammatory cytokine directly suppresses red-cell production in the marrow and blunts the response to erythropoietin, so anti-TNF therapy for inflammatory disease can also lift the accompanying anemia.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Anemia of inflammation is orchestrated by hepatocytes: in response to IL-6 they pump out hepcidin, the hormone that locks iron inside cells and starves red-cell production—so the liver's iron-master cell sits at the center of this anemia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Inflammation overrides the HIF oxygen-sensing that should fix anemia: low oxygen normally stabilizes HIF to boost erythropoietin and suppress hepcidin, but inflammatory signals blunt this response—so anemia of chronic disease persists despite the need for red cells.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen helps drive anemia of inflammation: its macrophages recycle iron from old red cells but, under inflammatory hepcidin, hoard it instead of returning it—while also clearing red cells faster, compounding the anemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Anemia of chronic disease starves tissues of oxygen: with fewer red cells the blood carries less oxygen, and the body senses the hypoxia and tries to compensate, though inflammation blunts the usual erythropoietin rise that would restore delivery.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney's anemia signal is blunted in chronic disease: kidneys make erythropoietin in response to low oxygen, but inflammatory cytokines dull both the hormone's output and the marrow's response, a key reason the anemia persists.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anemia of chronic disease lowers hemoglobin without true iron lack: locked-away iron starves developing red cells, so each carries less hemoglobin, giving the mild normocytic anemia that ferritin (high here) helps tell apart from iron deficiency.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Anemia of chronic disease starts at the gut: inflammation's hepcidin destroys ferroportin on the small intestine's iron-exporting cells, so dietary iron is absorbed but trapped in the lining, never reaching the blood—why oral iron often fails here.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Chronic anemia makes the heart work overtime: with less hemoglobin to carry oxygen, the heart pumps faster and harder, so in older or already-strained hearts this anemia can tip toward high-output failure and worsen heart disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Interferon-gamma helps lock iron away in chronic disease: this Th1 cytokine, high in chronic infections like TB, drives macrophages to hoard iron and blunts red-cell production, deepening the anemia of inflammation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — The marrow tells the story under the microscope: a Prussian-blue stain shows iron trapped in macrophages but missing from developing red cells, the light-microscopy signature that separates anemia of inflammation from true iron deficiency.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper is needed to move iron: ceruloplasmin, a copper enzyme, oxidizes iron for loading onto transferrin, so copper deficiency causes an anemia that can be mistaken for the anemia of chronic disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 is the switch that locks iron away: IL-6 signals through it to switch on hepcidin in the liver, the molecular relay that turns inflammation into the iron-restricted anemia of chronic disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows where the iron is hidden: macrophages of the spleen and marrow swell with ferritin and hemosiderin granules, hoarding the iron that hepcidin won't let them release to the hungry red-cell precursors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D can ease the iron block: it suppresses hepcidin, so deficiency — common in the chronic inflammatory diseases that cause this anemia — tightens the iron restriction, and repletion modestly loosens it.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Inflammatory bowel disease is a classic cause: chronic gut inflammation drives the IL-6 and hepcidin that lock away iron, so the large intestine's disease shows up as the anemia in the blood.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The same inflammation that drops the red cells lifts the platelets: IL-6 drives both hepcidin and thrombopoiesis, so a reactive thrombocytosis often travels alongside the anemia of chronic disease.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Anemia keeps company with a falling albumin: both are negative acute-phase reactants, suppressed as the liver reprioritizes its output during chronic inflammation, so the two markers sink together as a measure of disease burden.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Helper T cells light the fuse: their interferon-gamma and the cytokines they orchestrate drive the hepcidin surge and blunt the marrow's response, the adaptive-immune arm of the anemia's inflammatory cause.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Blocking the cytokine can lift the anemia: antibodies against IL-6 (tocilizumab) cut the hepcidin surge and correct the anemia of inflammatory disease, and anti-hepcidin agents are in development to free the trapped iron.
- `connects-to` → **[Obesity](../obesity/README.md)** — Even fat can cause it: obesity is a chronic low-grade inflammatory state whose raised IL-6 and hepcidin lock iron away, giving many obese people a mild functional iron deficiency and blunted anemia of inflammation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — It shows, faintly, on the skin: the chronic, usually mild anemia produces the pallor of conjunctivae, palms, and nail beds that, with fatigue, is often the only outward clue to the iron locked away inside.
- `connects-to` → **[Malaria](../malaria/README.md)** — Repeated malaria grinds out anemia of inflammation: the parasite's chronic immune activation drives hepcidin up to lock away iron, compounding the hemolysis and marrow suppression that make malarial anemia a leading childhood killer.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help hide the iron: in chronic infection they release lactoferrin that scavenges iron away from microbes, and their inflammatory signals push hepcidin up, reinforcing the iron sequestration behind the anemia.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Cancer wears two anemia hats at once: a colorectal tumor both bleeds to cause iron deficiency and drives inflammatory hepcidin to lock away stores, so its anemia is often a mixed picture and a clue prompting the search for the tumor.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation runs through a master switch: NF-κB activated by inflammatory signals turns on the IL-6 that drives hepcidin, the upstream hub linking chronic disease to the iron-locking that starves red-cell production.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Acute inflammation drops iron within hours: sepsis triggers a hepcidin surge that pulls iron out of the blood, an evolved defense to starve microbes that simultaneously chokes erythropoiesis into the anemia of critical illness.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — T cells help suppress the marrow: interferon-gamma from cytotoxic and helper T cells directly inhibits erythroid progenitors, an immune brake on red-cell production layered on the hepcidin-driven iron restriction.
- `connects-to` → **[COPD](../copd/README.md)** — Smokers' lungs inflame the marrow too: the chronic systemic inflammation of COPD raises hepcidin and cytokines that blunt erythropoiesis, so a meaningful share of COPD patients carry an anemia of chronic disease that worsens their breathlessness.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — A chronic leukemia drives the same anemia: the inflammatory cytokine output of chronic myeloid leukemia and its crowding of the marrow produce an anemia of chronic disease on top of the malignancy's own marrow takeover.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Chronic inflammation layers onto the hemolysis: beyond the relentless red-cell destruction, the ongoing vaso-occlusive inflammation of sickle cell disease raises hepcidin and cytokines that add an anemia-of-chronic-disease component to the baseline anemia.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Another inflammatory arthritis drives it: the sustained IL-6 of active ankylosing spondylitis raises hepcidin and blunts erythropoiesis, producing an anemia of chronic disease that tracks with disease activity.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Chronic viral infection feeds it: persistent hepatitis C inflammation, compounded by a cirrhotic liver and hypersplenism, raises hepcidin and suppresses red-cell production into an anemia of chronic disease.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Cancer and hormone therapy both contribute: advanced prostate cancer's inflammation and marrow metastases, plus the androgen-deprivation therapy that withdraws erythropoietic drive, combine into an anemia of chronic disease.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Its joint inflammation drains the blood: the sustained IL-6 and inflammatory drive of active psoriatic arthritis raises hepcidin and blunts erythropoiesis, producing an anemia of chronic disease in poorly controlled patients.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Lymphoma stokes the inflammatory anemia: the cytokine output and marrow involvement of aggressive lymphomas like DLBCL raise hepcidin and suppress red-cell production, a frequent cause of anemia of chronic disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its fatigue compounds low mood: the persistent tiredness and reduced oxygen delivery of anemia of chronic disease worsen the fatigue and functional decline that feed depression in chronically ill patients.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The liver runs its central switch: hepatic hepcidin, raised by inflammation, locks iron away from red-cell production, and chronic gut inflammation and bleeding compound the anemia of chronic disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones tune red-cell output: erythropoietin is an endocrine signal, and hypothyroidism, hypogonadism and hypopituitarism each blunt erythropoiesis, overlapping with the picture of anemia of chronic disease.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — A chronic gastric infection saps the blood: persistent Helicobacter pylori gastritis drives both iron-deficiency and an inflammatory anemia, and its eradication can correct otherwise refractory anemia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Pallor is its visible sign: anemia of chronic disease shows as pallor of the skin, conjunctivae and nail beds, a bedside clue that prompts the search for an underlying chronic illness.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Low oxygen delivery dulls the mind and stirs the legs: the anemia contributes to fatigue and impaired concentration, and the iron-restriction underlying it can exacerbate restless legs syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy compounds it: when chronic inflammatory disease coexists with the physiological dilutional anemia of pregnancy, the combined anemia can affect maternal wellbeing and fetal outcomes.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Low oxygen-carrying capacity raises the cardiac workload: chronic anemia drives compensatory tachycardia and a high-output state, aggravating ischaemia and, over time, straining the heart.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The reticuloendothelial system drives it: splenic and nodal macrophages trap recycled iron behind hepcidin, the core mechanism that starves the marrow of iron for erythropoiesis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Lung disease usually raises red cells via hypoxic erythropoietin, but in COPD the systemic inflammation blunts that response, so anemia of chronic disease can paradoxically appear instead.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It overlaps with the anaemia of kidney disease: chronic kidney disease causes a closely related anaemia through erythropoietin deficiency and inflammatory hepcidin excess, blurring the line with anaemia of chronic disease.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Chronic joint inflammation drives it: rheumatoid arthritis and other inflammatory arthritides raise IL-6 and hepcidin, making anaemia of chronic disease their commonest extra-articular feature.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — A chronic infection that causes it: tuberculosis sustains the inflammatory cytokines that block iron use, making anaemia of chronic disease a frequent finding in active TB.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The liver sets the iron trap: IL-6 from inflammation drives hepatocytes in the liver lobule to make hepcidin, the master regulator that locks iron inside macrophages and starves erythropoiesis — the core of anaemia of chronic disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cancer anaemia comes from both sides: malignancy itself drives anaemia of chronic disease through inflammation, while chemotherapy adds marrow suppression — managed with iron, erythropoiesis-stimulating agents or transfusion.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Two non-deficiency anaemias contrasted: anaemia of chronic disease comes from inflammatory iron sequestration with a working marrow, whereas aplastic anaemia is failure of the marrow itself — both with normal iron stores.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Chronic anaemia strains the heart: persistent low haemoglobin forces a higher cardiac output, and in heart failure or CKD the anaemia of chronic disease worsens myocardial workload and outcomes.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Anaemia of inflammation in infection: severe COVID-19 raises IL-6 and hepcidin, sequestering iron in macrophages and causing the anaemia of inflammation typical of chronic-disease anaemia.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Anaemia of a chronic marrow disease: myelofibrosis causes anaemia through marrow fibrosis and splenic sequestration compounded by an inflammatory, hepcidin-driven component, blending with the anaemia of chronic disease.
- `connects-to` → **[Giant Cell Arteritis](../giant-cell-arteritis/README.md)** — A textbook inflammatory anaemia: giant-cell arteritis produces a marked anaemia of chronic disease with very high ESR/CRP and reactive thrombocytosis, the IL-6-driven hepcidin response a clue to the diagnosis.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Multifactorial anaemia of autoimmunity: systemic sclerosis causes anaemia through chronic inflammation (hepcidin) compounded by GI blood loss from gastric antral vascular ectasia and renal involvement.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Chronic viral inflammation lowers haemoglobin: persistent hepatitis B drives an inflammatory, hepcidin-mediated anaemia of chronic disease, compounded in cirrhosis by hypersplenism and bleeding.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Hepcidin gates the gut: inflammation-driven hepcidin blocks ferroportin on the duodenal enterocytes of the intestinal epithelium, trapping dietary iron and starving erythropoiesis even when body iron stores are adequate.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Cancer-related anaemia: solid tumours like ovarian cancer drive IL-6 and hepcidin to produce an anaemia of inflammation, compounded by chemotherapy myelosuppression and bleeding.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — An underrecognised anaemia: the chronic low-grade inflammation and kidney disease of type 2 diabetes contribute to an anaemia of inflammation, blunting erythropoietin and restricting iron through hepcidin.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Hepcidin inducer: IL-1β from activated macrophages stimulates hepcidin production and suppresses erythropoiesis, a key inflammatory driver of the iron-restricted anaemia of inflammation.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome source: NLRP3-inflammasome activation matures the IL-1β that, with IL-6, sustains the hepcidin-driven iron sequestration of anaemia of chronic disease.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Vasculitic anaemia: the systemic inflammation of ANCA-associated vasculitis drives an anaemia of chronic disease, often compounded by renal failure and alveolar haemorrhage.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Hepcidin and erythroid block: activin/BMP signalling induces hepcidin and impairs erythroid maturation, a pathway distinct from IL-6 that activin ligand-traps (luspatercept) target to relieve inflammatory anaemia.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Microbial hepcidin induction: TLR4 sensing of bacterial products directly drives hepatocyte hepcidin in infection, locking away iron as part of the host iron-withholding defence that produces anaemia of inflammation.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Nutritional immunity: S100A8/A9 (calprotectin) sequesters iron and other metals from pathogens during inflammation, part of the same metal-withholding host response whose chronic activation causes anaemia of chronic disease.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β superfamily signaling (alongside activin) suppresses late-stage erythroid maturation in anemia of chronic disease, contributing to the ineffective erythropoiesis that ligand traps like luspatercept relieve.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Inflammatory cytokines and oxidative stress trigger caspase-mediated eryptosis (red-cell suicidal death), shortening erythrocyte survival and compounding anemia of chronic disease beyond the hepcidin-driven iron restriction.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — In chronic viral and autoimmune disease, type I interferon directly suppresses erythroid progenitors—an interferon-driven arm of anemia of chronic disease distinct from the dominant hepcidin-iron-sequestration axis.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — Prolyl-hydroxylase (EGLN/PHD) inhibitors like roxadustat stabilize HIF to raise endogenous erythropoietin and lower hepcidin, treating anemia of chronic disease by targeting the oxygen-sensing pathway upstream of both.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — The oxidative stress of chronic inflammation, partly from xanthine-oxidase-derived reactive oxygen species, damages erythrocytes and hastens their removal by macrophages, a second mechanism of anemia layered on iron sequestration.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — DAMPs signaling through RAGE sustain the NF-κB-driven cytokine output of chronic inflammation that keeps IL-6 and hepcidin elevated, feeding the iron-restriction that defines anemia of chronic disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — The BMP-SMAD pathway acting through SMAD4 is the principal transcriptional driver of hepcidin (already mapped), and inflammation amplifies it to lock iron away in the anemia of chronic disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Inflammatory cytokines and erythropoietin both signal through JAK kinases, and chronic JAK-STAT cytokine signaling blunts the erythropoietin response, contributing to the EPO-resistant anemia of chronic disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Erythropoietin signals through PI3K-AKT to support erythroid-progenitor survival, and the blunted EPO response of chronic inflammation weakens this pro-survival signal, deepening the anemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR (TLR4 mapped) and IL-1 signaling through MyD88 helps drive the hepcidin (mapped) induction that sequesters iron in anemia of chronic disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ (mapped) signaling through STAT1 directly inhibits erythroid-progenitor proliferation, blunting the marrow response that would otherwise correct the anemia.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Inflammatory cytokines tip the BCL-2 balance toward apoptosis of erythroid progenitors (caspase-3 mapped), reducing red-cell output in anemia of inflammation.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EPO-driven ERK-MAPK signaling promotes erythroid progenitor proliferation (EPO mapped); the blunted EPO responsiveness of ACD impairs this proliferative drive.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated translation and iron-sensing govern erythroid maturation, coupling the iron restriction of ACD to ineffective erythropoiesis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restrains the PI3K-AKT signaling downstream of the erythropoietin receptor that drives erythroid survival and expansion, a node in the impaired EPO response of ACD.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage inflammatory activation that drives the hepcidin-mediated iron sequestration of anemia of chronic disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the chronic inflammatory tone that sustains the hepcidin response and iron restriction of anemia of chronic disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2-driven monocyte recruitment sustains the inflammatory macrophage activity that underlies the iron sequestration of anemia of chronic disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the oxidative-stress and survival programs of erythroid progenitors that are suppressed in the inflammatory milieu of anemia of chronic disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA) signaling transduces the erythropoietin survival signal in erythroid progenitors that is blunted in anemia of chronic disease (AKT already mapped).
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cell-cycle progression of erythroid progenitors is restrained by the inflammatory cytokine milieu of anemia of chronic disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the inflammatory signaling that drives the hepcidin-mediated iron sequestration of anemia of chronic disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-bearing cytotoxic lymphocytes contribute to the immune-mediated suppression of erythropoiesis in anemia of chronic disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Macrophage autophagy participates in the iron-recycling and erythrophagocytosis dysregulated in anemia of chronic disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the erythroid and macrophage iron-metabolism adaptation of anemia of chronic disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of cytokine and EPO receptors participates in the suppressed erythropoiesis of anemia of chronic disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte and macrophage activation contributes to the inflammatory iron sequestration of anemia of chronic disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the inflammatory and erythroid gene programs of anemia of chronic disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the bone-marrow erythroid-niche interactions relevant to anemia of chronic disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory milieu driving the hepcidin response of anemia of chronic disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the chronic inflammation driving the anemia of chronic disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory milieu of the anemia of chronic disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the erythroid and inflammatory gene programs of the anemia of chronic disease.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen erythropoiesis: testosterone stimulates erythropoietin production and erythroid progenitors, so the hypogonadism common in chronic illness and aging deepens the anemia of chronic disease beyond the inflammatory iron restriction.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Erythroid support: IGF-1 promotes the proliferation and survival of erythroid progenitors, and its suppression in chronic illness and malnutrition contributes to the blunted erythropoiesis of the anemia of chronic disease.
- `connects-to` → **[NFE2L2](../../03-molecular/nfe2l2/README.md)** — Oxidative red-cell loss: the inflammatory oxidative milieu accelerates eryptosis and shortens red-cell survival, and the NRF2 antioxidant response modulates this stress, adding a haemolytic component to the anemia of chronic disease.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences in erythropoiesis: sex hormones modulate red-cell production, with testosterone (already mapped) stimulating and estrogen restraining erythropoiesis, contributing to the different baseline haemoglobin against which the anemia of chronic disease develops.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune-regulatory tuning: the anti-inflammatory cytokine IL-10 can paradoxically raise hepcidin (already mapped) and modulate macrophage iron handling, part of the complex cytokine balance that shapes the anemia of chronic disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Nutritional immunity: like iron (already mapped), zinc is redistributed away from the plasma during inflammation as part of nutritional immunity, and the resulting hypozincaemia can further impair the erythropoiesis blunted in chronic disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the underlying inflammatory disease contribute to the cytokine milieu (IL-6, TNF and IL-1 already mapped) that raises hepcidin (already mapped) and blunts erythropoiesis in the anemia of chronic disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Macrophage polarisation: IL-4 polarises macrophages (already mapped) toward an iron-recycling, anti-inflammatory phenotype opposing the iron-sequestering inflammatory state, so the M1/M2 balance shapes the iron handling of the anemia of chronic disease.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Erythropoietic suppression: nitric oxide generated in inflammation impairs erythroid progenitor proliferation and shortens red-cell survival, adding to the hepcidin-driven iron restriction (already mapped) in the anemia of chronic disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 iron-recycling macrophages: IL-13, with IL-4 (already mapped), polarises the macrophages (already mapped) toward the anti-inflammatory iron-recycling phenotype that opposes the iron-sequestering inflammatory state of the anemia of chronic disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Trace-metal redistribution: the inflammation of the anemia of chronic disease redistributes zinc as well as iron (already mapped), the hypozincaemia of inflammation accompanying the hypoferraemia in the acute-phase response.
- `connects-to` → **[Inflammatory bowel disease](../inflammatory-bowel-disease/README.md)** — A common cause: inflammatory bowel disease is a frequent cause of the anemia of chronic disease (IL-6 and hepcidin already mapped), often combined with iron-deficiency anaemia from chronic gastrointestinal blood loss.
- `connects-to` → **[Hodgkin lymphoma](../hodgkin-lymphoma/README.md)** — Malignancy cause: Hodgkin lymphoma and other cancers commonly cause the anemia of chronic disease through their cytokine (IL-6 already mapped) drive of hepcidin (already mapped) and the marrow involvement.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and hepcidin: leptin modulates the hepcidin (already mapped) and erythropoiesis, linking the obesity (already mapped)-related inflammation to the iron and red-cell dysregulation of the anemia of chronic disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine axis: adiponectin, with leptin (already mapped), is part of the adipokine axis of the obesity-related and inflammatory dysregulation of iron and erythropoiesis in the anemia of chronic disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity-related inflammation contributing to the hepcidin (already mapped) and iron dysregulation of the anemia of chronic disease.
- `connects-to` → **[Inflammatory bowel disease](../inflammatory-bowel-disease/README.md)** — IBD anemia: the inflammatory bowel disease is a common cause of the anemia of chronic disease (the inflammation-hepcidin already mapped), compounded by the iron-deficiency blood loss.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepcidin-producing liver: the liver (the hepatocytes already mapped) produces the hepcidin (already mapped) under the IL-6 (already mapped) drive, the endocrine hub of the iron sequestration of the anemia of chronic disease.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate inflammatory NK: the NK cells (perforin already mapped), via their IFN-γ (already mapped), contribute to the inflammatory cytokine milieu that drives the hepcidin (already mapped) of the anemia of chronic disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu underlying the anemia of chronic disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic inflammation that drives the hepcidin (already mapped) iron sequestration of the anemia of chronic disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the diverse chronic inflammatory conditions underlying the anemia of chronic disease.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (already mapped) of the chronic infections, autoimmunity and myeloma (already mapped) that drive the inflammation of the anemia of chronic disease.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) and sustain the chronic inflammatory response (IL-6 and TNF already mapped) that drives the anemia of chronic disease.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Inflammatory mast cells: the mast cells contribute to the chronic inflammatory milieu (IL-6 and TNF already mapped) that drives the hepcidin (already mapped) induction of the anemia of chronic disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the chronic inflammatory response of the infections and autoimmunity that drive the anemia of chronic disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the myeloid activation that sustains the inflammatory cytokine (IL-6 already mapped) drive of the anemia of chronic disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the chronic inflammatory response driving the anemia of chronic disease.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the immune complexes of the autoimmune and infectious drivers of the anemia of chronic disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Inflammatory matricellular: osteopontin, a pro-inflammatory matricellular cytokine, is part of the chronic-inflammatory milieu (with IL-6 and TNF-α already mapped) that suppresses the erythropoiesis of the anemia of chronic disease.

[^weiss-2005-acd-review]: Weiss G, Goodnough LT. Anemia of chronic disease. *N Engl J Med.* 2005;352(10):1011-1023. [doi:10.1056/NEJMra041809](https://doi.org/10.1056/NEJMra041809) · [PubMed 15758012](https://pubmed.ncbi.nlm.nih.gov/15758012/)
[^nemeth-2004-il6-hepcidin]: Nemeth E, Rivera S, Gabayan V, et al. IL-6 mediates hypoferremia of inflammation by inducing the synthesis of the iron regulatory hormone hepcidin. *J Clin Invest.* 2004;113(9):1271-1276. [doi:10.1172/JCI200420945](https://doi.org/10.1172/JCI200420945) · [PubMed 15124018](https://pubmed.ncbi.nlm.nih.gov/15124018/)
[^ganz-2019-acd-iron]: Ganz T. Anemia of Inflammation. *N Engl J Med.* 2019;381(12):1148-1157. [doi:10.1056/NEJMra1916038](https://doi.org/10.1056/NEJMra1916038) · [PubMed 31532961](https://pubmed.ncbi.nlm.nih.gov/31532961/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
