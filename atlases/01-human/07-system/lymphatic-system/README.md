---
schema: human-scale-entry/v1
id: lymphatic-system
name: Lymphatic System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-05
summary: "Network of blind-ended capillaries, collecting vessels, 400–700 lymph nodes, spleen, thymus, and MALT returning 3–4 L/day interstitial fluid to circulation and routing immune surveillance of antigens."
aliases: ["lymphatics", "lymph system", "lymphoid system", "secondary lymphoid organs", "lymph vessels"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/spleen
    relation: contains
    note: "Spleen is the largest secondary lymphoid organ; red pulp macrophages clear senescent RBCs and recycle iron; white pulp PALS (T cells) and B-cell follicles with marginal zone B cells respond to polysaccharide antigens."
  - target: 01-human/06-organ/thymus
    relation: contains
    note: "Thymus is the primary lymphoid organ for T-cell development: V(D)J rearrangement, positive selection on cTEC MHC, and negative selection on mTEC AIRE-presented self antigens; thymic output declines with age."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Lymph nodes (400–700) are antigen-filtering and immune activation hubs; DCs arriving via afferent lymph activate naïve T/B cells; germinal centre reactions produce affinity-matured IgG plasma cells; HEV enable lymphocyte recirculation."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Thoracic duct returns 2–4 L lymph/day to the left subclavian vein, essential for plasma volume maintenance; lymphatic dysfunction → oedema and chylothorax; collecting vessels have intrinsic smooth muscle and valves for unidirectional flow."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "Lymph node GCs drive B cell affinity maturation: FDC antigen selection → SHM + class switch → plasma cells or memory B cells; Peyer's patch GCs → sIgA class switching; splenic MZ B cells mount T-independent IgM responses to polysaccharide antigens."
  - target: 01-human/04-cellular/t-helper-cell
    relation: contains
    note: "Naive T cells enter via HEV → cognate DC-T cell interaction in paracortex → Th1/Th2/Th17/Tfh differentiation; Tfh cells migrate to GC border → provide CD40L/IL-21 help to B cells → affinity maturation and CSR; the paracortex is the primary site of naive T cell activation."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow is the lymphopoiesis site: HSC → CLP → pro-B cells (VDJ → μ chain → pre-BCR → naive B cell export); NK cells, ILC progenitors, and DC precursors also originate in bone marrow; T cell progenitors exit bone marrow and migrate to thymus for positive/negative selection."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The lymphatic system drains and patrols the reproductive organs: pelvic and para-aortic nodes filter lymph from uterus, ovaries, prostate, and testes — so nodal status drives staging and spread of gynecologic and prostate cancers, and sentinel-node mapping guides their surgery."
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Dendritic cells are the lymphatic system's messengers: they capture antigen in tissues, then migrate through afferent lymphatics to the draining lymph node to present it to naive T cells — linking innate detection to adaptive immunity, and the basis of DC cancer vaccines."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Hodgkin lymphoma is the prototypical cancer of the lymphatic system: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), reflecting lymphatic drainage anatomy — unlike the scattered spread of non-Hodgkin lymphomas."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Diffuse large B-cell lymphoma is the commonest malignancy of the lymphatic system: it arises from germinal-center or activated B cells in lymph nodes (or extranodal lymphoid tissue), producing rapidly enlarging masses—the lymphatic system's own immune cells becoming cancer."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells are the antibody-secreting end-product of the lymphatic system: B cells activated in lymph-node germinal centers become plasma cells that home to bone marrow and mucosa to pump out immunoglobulin, the humoral output of lymphoid tissue—malignant as myeloma."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut houses the largest share of the lymphatic system: gut-associated lymphoid tissue (Peyer patches, mesenteric nodes) and lacteals that absorb dietary fat make the digestive tract a major immune and lymph-transport organ, tying mucosal immunity and fat transport together."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Follicular lymphoma is a cancer of the lymphatic system's architecture: it arises from germinal-center B cells in lymph node follicles and spreads through nodes, spleen and marrow—turning antibody-maturation machinery into an indolent malignancy."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "The lymphatic system governs how breast cancer is staged: tumor cells drain first to axillary lymph nodes, so sentinel-node biopsy guides treatment and node status drives prognosis—while removing nodes can cause arm lymphedema, the cost of disrupting drainage."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Melanoma exploits the lymphatic system to metastasize: it spreads early through dermal lymphatics to regional nodes, making sentinel lymph-node biopsy central to staging, and can even induce lymphangiogenesis—so lymphatic involvement strongly predicts outcome."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Mantle cell lymphoma illustrates the lymphatic system's vulnerability: arising from mantle-zone B cells of the lymph node, it spreads through the lymphatic network to nodes, marrow and gut—the system built to circulate lymphocytes also disseminates their cancers."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells patrol the lymphatic system: alongside B and T cells they traffic through lymph nodes screening for infected and tumor cells, and rare NK-cell lymphomas arise here—part of the immune surveillance the lymphatic network is built to support."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine feeds the lymphatic system dietary fat: specialized lacteals in each villus absorb fat as chyle and carry it through lymphatics to the bloodstream, so gut lymphatics handle nutrition as well as immunity—and blockage causes fat malabsorption."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages patrol the lymphatic system: positioned in lymph-node sinuses, they filter incoming lymph, capture pathogens and present antigen to lymphocytes, so the lymphatics are not just drainage but a surveillance network staffed by phagocytes."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "The lymphatic system is where antibodies are made: B cells in lymph-node germinal centers mature into plasma cells producing IgG, which drains into blood to neutralize pathogens—so the lymphatics turn captured antigen into circulating humoral immunity."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "The gut's lymphatic tissue produces secretory IgA: Peyer's patches and mesenteric nodes generate IgA-secreting plasma cells that protect mucosal surfaces, so the lymphatic system guards the body's largest interface with the outside world."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Lymphatic vessels grow under VEGF control: VEGF-C and VEGF-D acting on VEGFR-3 drive lymphangiogenesis, building and remodeling the lymphatic network—and tumors hijack this signal to sprout lymphatics that carry cancer cells to lymph nodes."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is the body's largest single source of lymph: high sinusoidal filtration produces protein-rich hepatic lymph that drains via the thoracic duct, so in cirrhosis overwhelmed lymphatics contribute to the ascites that fills the abdomen."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Lymph nodes are where cytotoxic T cells are armed: naive CD8 cells survey nodes until a dendritic cell presents antigen, then activate and exit through lymphatics into blood to hunt infected or tumor cells—so the lymphatic system stages antiviral and antitumor immunity."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "The lymphatic system rescues leaked albumin: capillaries constantly leak protein into tissues, and lymph vessels collect this albumin-rich fluid and return it to the blood—so blocked lymphatics cause the protein-rich swelling of lymphedema."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Lymphatic vessels are built from specialized endothelial cells: distinct from blood-vessel lining, these cells form one-way valves and loose junctions that soak up fluid, and VEGF-C drives them to sprout new lymphatics (lymphangiogenesis)."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Lymph nodes are where regulatory T cells learn tolerance: the lymphatic system funnels antigens and lymphocytes into nodes where Tregs are induced and licensed, making lymphoid tissue the training ground for immune self-restraint."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "The lymphatic system is the body's fat-transport highway: intestinal lacteals absorb dietary fats packaged as chylomicrons—rich in cholesterol and triglyceride—into lymph rather than blood, delivering them to the circulation downstream."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin depends on its lymphatics for drainage and defense: a fine network clears fluid and ferries antigen-loaded dendritic cells to nodes, so when it fails, fluid pools as lymphedema and immune surveillance of the skin suffers."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Skin lymphatics help regulate the body's sodium: salt stored in the skin is sensed by macrophages that trigger lymphatic growth to clear it, an unexpected role linking the lymphatic system to sodium balance and blood pressure."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lungs sit at the lymphatic system's outflow: the thoracic duct empties lymph near the heart, and injury to it leaks milky lymph into the chest as a chylothorax, a distinctive lymphatic emergency."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Lymph nodes do their work in germinal centers: within them B cells multiply, mutate, and are selected to make ever-better antibodies, the engine of the adaptive response the lymphatic system carries."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut holds the body's largest lymphatic tissue: the bowel wall, including the large intestine, is packed with lymphoid follicles (GALT) that sample microbes and mount the mucosal immunity the lymphatics coordinate."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The lymphatic system is mapped with radiotracers: lymphoscintigraphy follows injected photons to find the sentinel node in cancer staging and to chart blocked drainage in lymphedema."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Lymph is pumped, not just drained: smooth-muscle cells in the walls of collecting lymphatics contract rhythmically to push lymph against gravity toward the chest."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The lymphatic system returns its fluid to the blood at the heart: the thoracic duct empties into the great veins near it, closing the loop between lymph and circulation."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the lymphatic capillary's clever valve: its endothelial cells overlap as loose flaps tethered by anchoring filaments, opening one way to admit fluid and large molecules and closing to keep them from leaking back."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain was long thought to have no lymphatics — then they were found: meningeal lymphatic vessels and the glymphatic flow along blood vessels drain the brain's waste, a discovery reshaping how we think about Alzheimer's and brain fluid."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney has its own lymphatic drainage: renal lymphatics clear interstitial fluid and immune cells from the kidney, and their dysfunction contributes to the swelling and inflammation of kidney disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Lymph is the antibody's highway: afferent lymph carries antigen to the nodes where plasma cells make antibody, then efferent lymph and the thoracic duct pour that immunoglobulin into the bloodstream, so lymphatic blockage blunts the spread of the response."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Infection can race up the lymphatics: bacteria draining from a wound inflame the vessels into lymphangitis, the tender red streak tracking toward a swollen node as neutrophils pour in to fight the spreading microbes."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets keep blood and lymph apart: in development their CLEC-2 receptor binds podoplanin on budding lymphatic endothelium and plugs the junction so the new vessels stay blood-free — a separation whose failure leaves lymphatics blood-filled."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "Tuberculosis loves the lymph nodes: when M. tuberculosis seeds the cervical nodes it produces scrofula, a chronic swelling and breakdown of the lymphatic tissue that is one of TB's commonest sites outside the lung."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The lymphatics carry the fat from a meal: gut lacteals absorb dietary lipids as chylomicrons and ferry them through lymph into the blood, and leaky or damaged lymphatics promote local fat deposition — linking the system to adipose tissue."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Scarring chokes the lymph vessels: TGF-beta drives the fibrosis that stiffens lymphatic channels in chronic lymphedema, while also restraining the lymphangiogenesis needed to repair them — a target for keeping lymph flowing."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut feeds the lymph: specialized lacteals inside each intestinal villus collect the fat absorbed by the epithelium, packaging dietary lipids into milky chyle that drains through the lymphatics to the bloodstream — the lymphatic system's role in nutrition."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "When the heart backs up, the lymphatics flood: high venous pressure in heart failure outpaces lymphatic return of interstitial fluid, so the drainage system is overwhelmed and fluid pools as the edema and effusions that mark decompensation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "The vessels pump themselves with a gas signal: nitric oxide released by lymphatic endothelium tunes the rhythmic contractions of lymphatic muscle that propel lymph forward, so it helps set the pace of drainage against gravity."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Strep inflames the lymphatic channels: Streptococcus pyogenes causes lymphangitis — the red streak tracking up a limb toward the nodes — and recurrent attacks scar the vessels into chronic lymphedema."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess fat throttles the lymphatics: obesity impairs lymphatic pumping and damages the vessels, causing a distinct obesity-related lymphedema, while the lymphatic system in turn shapes fat deposition and inflammation."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A lymphoid leukemia fills the system: chronic lymphocytic leukemia accumulates malignant B lymphocytes that swell the lymph nodes and spleen, a tumor of the very cells the lymphatic system is built to circulate."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "The fastest cancer grows in its tissue: Burkitt lymphoma is an explosive germinal-center B-cell tumor of the lymphatic system, the most rapidly proliferating human cancer, often presenting as a bulky nodal or abdominal mass."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "A virus makes the lymphatic system its home: Epstein-Barr virus infects B lymphocytes, causing the lymphadenopathy of mononucleosis and driving several lymphomas that arise from the cells it transforms."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The lymphatics are a highway for infection: pathogens draining through lymph cause lymphangitis and lymphadenitis, and when the nodes are overwhelmed the infection can spill into the blood as sepsis."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "It is a disease of the lymphoid organs: HIV replicates in and progressively destroys the CD4 T cells and lymphoid tissue of the lymphatic system, with persistent lymphadenopathy and eventual collapse of nodal architecture."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "It classically inflames the nodes: Mycobacterium tuberculosis causes lymphadenitis — scrofula in the neck — a granulomatous infection of the lymphatic system that can persist or drain through the skin."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Its own T cells can turn malignant: peripheral T-cell lymphomas arise from the mature T lymphocytes that populate the lymph nodes, an aggressive cancer of the lymphatic system's cellular residents."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "When lymph drainage fails, the skin breaks down: lymphedema from damaged or removed lymphatics causes chronic swelling, fibrotic skin changes and ulcers that heal poorly without drainage."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Stagnant lymph invites recurrent infection: lymphedema impairs immune surveillance in the swollen limb, predisposing to repeated cellulitis and erysipelas, often from staphylococci and streptococci."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Chronic swelling and disfigurement weigh on mood: the disabling, visible and progressive nature of lymphedema, and the burden of lymphatic cancers, contribute to depression and reduced quality of life."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The skeleton houses its factory and its drainage burdens the limbs: bone marrow is the primary lymphoid organ that makes lymphocytes, and limb lymphatics, when they fail, swell the soft tissues with lymphedema."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The chest holds its great vessel: the thoracic duct returns lymph to the bloodstream in the chest, so its injury causes chylothorax, and pulmonary lymphatics clear the lung's interstitial fluid."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It drains the skin and shows there when it fails: dermal lymphatics clear fluid and immune cells from the skin, so lymphedema thickens and hardens it and breached skin lets lymphangitis track up the limb."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The brain has its own drainage: the glymphatic system and newly-discovered meningeal lymphatic vessels clear cerebrospinal fluid and waste to cervical lymph nodes, linking the lymphatic and nervous systems."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The thymus is a lymphoid and endocrine organ: this primary lymphoid organ where T cells mature also secretes thymic hormones, sitting at the crossroads of the lymphatic and endocrine systems."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A hidden network drains the kidney: a rich renal lymphatic system clears interstitial fluid and protein from the kidney, and when overwhelmed it contributes to the oedema of nephrotic syndrome."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A classic cause of swollen nodes: toxoplasmosis typically presents with painless cervical lymphadenopathy, a common reactive enlargement of the lymphatic system."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "The lymphatics absorb dietary fat: long-chain fats and fat-soluble vitamins enter specialised intestinal lacteals as chyle rather than the portal blood, carried by the lymphatic system to the circulation."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "A lymphoid malignancy of the system: Waldenström macroglobulinaemia is a lymphoplasmacytic lymphoma that infiltrates lymph nodes, spleen and marrow, secreting IgM that thickens the blood."
  - target: 01-human/05-tissue/peyers-patches
    relation: connects-to
    note: "Gut lymphoid tissue is part of it: Peyer's patches and other gut-associated lymphoid tissue are major secondary lymphoid organs of the lymphatic system, sampling intestinal antigens to launch mucosal immunity."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "A virus that lives in the lymph nodes: HIV replicates in and progressively destroys lymphoid tissue, causing the generalised lymphadenopathy and follicular collapse that mark advancing infection."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its cancers are chemo-treated: the lymphomas and leukaemias arising in lymphoid tissue are treated with combination chemotherapy, the mainstay of curing many of them."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Cancer of the lymphoid progenitor: acute lymphoblastic leukaemia is the malignant proliferation of immature B- or T-lymphocyte precursors, the founding cells of the lymphatic system, filling marrow and infiltrating lymph nodes, thymus and spleen."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "The plasma cell at its end stage turns malignant: multiple myeloma is a clonal cancer of antibody-secreting plasma cells—the terminal product of the lymphatic system's B-cell lineage—accumulating in bone marrow and flooding blood with monoclonal immunoglobulin."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Where anti-tumour immunity is orchestrated: checkpoint inhibitors work largely within the lymphatic system, freeing T cells primed by dendritic cells in the lymph nodes that drain a tumour, so intact lymphatic drainage shapes the response to immunotherapy."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Lymphoedema fibrosis: chronic lymph stasis—after node dissection, radiation or filariasis—drives tissue fibrosis and fat deposition, the irreversible limb swelling that defines lymphoedema."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Lymphoid proliferation and MALT lymphoma: Sjögren's chronic lymphocytic infiltration of glands forms ectopic lymphoid tissue and carries the highest lymphoma risk of the autoimmune diseases, a disorder of the lymphatic system itself."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Ectopic lymphoid tissue in the joint: rheumatoid arthritis builds germinal-centre-like follicles in inflamed synovium and causes lymphadenopathy, with a raised risk of lymphoma from chronic lymphatic activation."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Lymphatics clear the artery: adventitial lymphatic vessels drain cholesterol from the arterial wall in reverse cholesterol transport, and when they fail, lipid accumulates and atherosclerosis worsens—an unexpected role for the lymphatic system in heart disease."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Nodal spread defines prognosis: head and neck cancer metastasises first to the cervical lymph nodes, so the lymphatic system's drainage map dictates staging, neck dissection and the entire treatment plan."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The biggest lymph source: the liver generates a large share of the body's lymph from protein-rich fluid in the hepatic sinusoids, and when cirrhosis overwhelms this drainage the overflow becomes ascites."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Lymph-node homing: CXCL12 (with CXCR4) directs the trafficking and positioning of lymphocytes and dendritic cells within lymph nodes, organising the adaptive immune response."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and lymphedema: adipose-derived leptin links obesity to impaired lymphatic vessel function and lymphoedema, and it also modulates immune cells within lymph nodes."
  - target: 02-pathogen/04-parasites/trypanosoma-brucei
    relation: connects-to
    note: "Lymphatic-tropic infection: African trypanosomiasis spreads through and enlarges lymph nodes—the posterior cervical swelling of Winterbottom's sign—before invading the central nervous system."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Lymphoid organogenesis: TNF-family signalling builds and maintains the secondary lymphoid organs, and excess TNF-α drives the reactive lymph-node enlargement of infection and inflammation."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell follicles: BAFF sustains the B cells of lymph-node and splenic follicles, organising the germinal-centre reactions at the heart of the lymphatic system's adaptive immunity."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Germinal-centre signalling: IL-6 within lymph nodes supports T-follicular-helper and B-cell responses, and its excess drives lymphadenopathy in conditions like Castleman disease."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Lymphangiogenesis: the angiopoietin-Tie2 axis, with VEGF-C, builds and remodels lymphatic vessels, and its dysregulation underlies the failed vessel formation of primary lymphoedema."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Lymph-node immunity: complement C3 opsonises antigens trafficked to lymph nodes and is retained on follicular dendritic cells, focusing the humoral immune responses the lymphatic system orchestrates."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "Dietary-lipid transport: intestinal lacteals absorb dietary fat as ApoE-bearing chylomicrons into the lymph (chyle), the lymphatic system's distinctive role in carrying fat to the bloodstream."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Lymphatic development: adrenomedullin signalling through RAMP2 is essential for lymphatic vessel formation and maintaining the integrity of the lymphatic endothelium, so its loss causes severe lymphatic defects."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Lymphatic pumping: prostaglandins regulate the rhythmic intrinsic contractions of collecting lymphatics that actively propel lymph against gravity, the pumping mechanism that drains tissue fluid back to the circulation."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Inflammatory drainage: histamine and other inflammatory mediators increase lymphatic permeability and modulate lymphatic contractility, coupling local inflammation to the lymph drainage and immune-cell transport the system provides."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Lymphangion pumping: rhythmic calcium transients in lymphatic-vessel smooth muscle drive the spontaneous contractions of each lymphangion that actively pump lymph against gravity, the intrinsic pacemaker mechanism propelling lymph back to the bloodstream."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Sympathetic regulation: sympathetic norepinephrine acting on lymphatic-muscle adrenergic receptors modulates the frequency and force of lymphatic contractions, the neural control of lymph flow that adjusts drainage to the body's needs."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Lymph-node immunity: lymph carries antigen-presenting cells to the lymph nodes, where MHC-class-II presentation to T cells launches the adaptive immune response — the immune-surveillance function that is the lymphatic system's defining role."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Lymphatic tone: endothelin-1 modulates the contractility of lymphatic collecting vessels, working alongside the nitric oxide and norepinephrine already mapped to set the intrinsic pumping that propels lymph."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Node lymphocyte expansion: IL-2 drives the clonal proliferation of T cells within lymph nodes, the amplification step of the adaptive immune response that the lymphatic system organises."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Fluid filtration: bradykinin raises capillary permeability and interstitial fluid formation, increasing the filtered load that the lymphatics must return to the circulation to prevent oedema."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Leukocyte trafficking: CCL2 and related chemokines direct the trafficking of monocytes and dendritic cells into and through the lymphatic system, guiding antigen delivery to draining lymph nodes."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic effector: cytotoxic T cells primed in the lymph nodes deploy perforin to kill infected and malignant cells, an effector arm generated by the lymphatic system's adaptive response."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nodal tolerance: the PD-1 checkpoint operating within lymph nodes enforces peripheral tolerance, restraining the T-cell responses organised in lymphatic tissue."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling downstream of VEGFR3 (VEGF mapped) drives lymphatic-endothelial proliferation and lymphangiogenesis and supports lymphocyte survival in lymphoid organs."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR governs lymphatic-endothelial growth — its inhibition (sirolimus) treats lymphatic malformations — and shapes the metabolism of lymphocytes trafficking through the system."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT cytokine signalling coordinates the lymphocyte differentiation and effector responses orchestrated within the lymphatic organs."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 (JAK1/2 already mapped) programs the T-follicular-helper and Th17 differentiation and germinal-centre responses of the lymphatic organs."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon-programmed antiviral and antitumour lymphocyte responses coordinated within the lymphatic system."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates lymphocyte apoptosis, lymphangiogenesis and the immune regulation that occurs within the lymphatic organs."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate lymphocyte homeostasis and the lymphatic-endothelial stress responses across the lymphatic system."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling governs lymphatic-vessel development and remodeling and the regulatory immune tone of the lymphatic system."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α couples the metabolic and inflammatory status of lymphoid tissue to the lymphangiogenesis (VEGF already mapped) of the lymphatic system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), acting downstream of VEGFR-3 (VEGF already mapped), governs the lymphatic-endothelial growth and remodeling of the lymphatic system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of VEGFR-3 and other receptors drives the lymphangiogenesis and lymphatic-endothelial responses of the lymphatic system."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB inflammatory signaling regulates the lymphatic-endothelial and lymph-node immune responses of the lymphatic system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the lymphatic-endothelial and immune-cell metabolism of the lymphatic system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy participates in the lymphocyte homeostasis and lymphatic-endothelial maintenance of the lymphatic system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the trafficking of leukocytes through the lymphatic vessels and nodes of the lymphatic system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the lymphocyte and lymphatic-endothelial gene programs of the lymphatic system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the lymphatic-endothelial junction dynamics and immune-cell activation of the lymphatic system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the lymphatic-endothelial and immune responses of the lymphatic system."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β signaling participates in the inflammatory and immune-trafficking responses of the lymphatic system."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the lymphocyte-mediated immune responses of the lymphatic system."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of lymphocyte differentiation in the lymphatic system."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Peripheral tolerance: CTLA-4 restrains T-cell activation in lymph nodes and enforces self-tolerance (alongside PD-1 already mapped), a checkpoint that keeps the lymphatic system's constant immune surveillance from turning on the host."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 and humoral arm: IL-4 drives the Th2 response and B-cell antibody class-switching within lymphoid tissue, one of the polarised programmes (balanced against Th1) the lymphatic system uses to tailor immunity to different threats."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 differentiation: IL-12 from dendritic cells drives naive T cells toward the Th1 programme and activates NK cells, directing the cell-mediated immunity that the lymphatic system mounts against intracellular pathogens."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Cell-mediated effector: interferon-gamma from the Th1 cells and NK cells the lymphatic system marshals (IL-12 already mapped) activates macrophages and cytotoxic responses, the effector cytokine of the cell-mediated immunity against intracellular pathogens."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune regulation: IL-10 from regulatory lymphocytes in lymphoid tissue restrains the immune response, balancing the Th1 (IL-12 already mapped) and Th2 programmes to resolve inflammation and preserve tolerance within the lymphatic system."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Vessel structure and lymphoedema: collagen forms the framework of lymphatic vessels and lymph nodes, and when lymph drainage fails, the chronic protein-rich stasis drives the fibrosis and collagen deposition of lymphoedema."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Perilymphatic immunity: mast cells cluster around lymphatic vessels, releasing histamine (already mapped) and mediators that regulate lymphatic contractility and permeability, part of the immune surveillance woven through the lymphatic system."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic lymph: the liver produces a large fraction of the body's lymph from the sinusoidal fluid, and when hepatic lymph outstrips drainage in cirrhosis or heart failure it forms ascites, a major output of the lymphatic system."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary lymphatics and chyle: the lungs are drained by a rich lymphatic network, and disruption of the thoracic duct spills lymph as a chylothorax, illustrating the lymphatic transport of fat-laden chyle."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 lymphatic remodelling: IL-13, with IL-4 (already mapped), is the type-2 cytokine that, alongside the lymphangiogenic VEGF (already mapped), drives the lymphatic remodelling seen in filariasis and chronic inflammation of the lymphatic system."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Lympho-adipose crosstalk: adiponectin, with leptin (already mapped), mediates the crosstalk between the lymphatic vessels and the perinodal and subcutaneous adipose tissue that supports lymphatic function."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the fat surrounding the lymphatics and lymph nodes, linking metabolism to lymphatic and immune function."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Sinus macrophages: the subcapsular-sinus and medullary macrophages of the lymph nodes filter the lymph and present the captured antigens, the resident phagocytes of the lymphatic system."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK trafficking: the natural killer cells (perforin already mapped) traffic through the lymphatic system, providing the innate cytotoxic surveillance of the circulating lymph and nodes."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Interstitial sodium and lymphoedema: the lymphatic system clears the interstitial sodium and fluid, and its dysfunction produces the sodium-rich lymphoedema, linking the lymphatics to the body's sodium and volume balance."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil trafficking: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), expands and traffics the eosinophils through the lymphatic system in the allergic and anti-helminth responses."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 lymphoid axis: IL-23 sustains the Th17 (IL-17 already mapped) cells generated and trafficked through the lymph nodes of the lymphatic system for the mucosal defence."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "IgE class-switch: the IgE (with IL-4 and IL-13 already mapped) is class-switched in the germinal centres of the lymph nodes (immunoglobulin already mapped) of the lymphatic system, arming the allergic response."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement (C3 already mapped) pathway in the lymph and interstitial fluid, protecting the host tissue drained by the lymphatic system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Permeability control: the C1-esterase inhibitor regulates the complement and contact (bradykinin already mapped) systems; its deficiency causes the angioedema of the interstitial tissues drained by the lymphatic system."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Immune-complex ferrying: the erythrocytes bind the complement (C3 already mapped)-opsonised immune complexes via CR1 and deliver them to the splenic and hepatic phagocytes, complementing the lymphatic clearance of the lymphatic system."
---

# Lymphatic System

## Overview

The lymphatic system is the body's second vascular network, operating in parallel with and complementary to the cardiovascular system. Unlike the closed cardiovascular circuit, the lymphatics form a one-way drainage system beginning with blind-ended lymphatic capillaries in nearly every vascularised tissue, converging into progressively larger collecting vessels, passing through chains of lymph nodes, and ultimately emptying into the venous circulation at the thoracic duct (left subclavian vein) and right lymphatic duct (right subclavian vein) [^guyton-hall].

Three functions define the lymphatic system:
1. **Fluid homeostasis** — Starling forces net ~3 L/day of protein-rich plasma filtrate into the interstitium that cannot be fully reabsorbed by venous capillaries; lymphatics collect this fluid (now lymph) and return it to the blood. Failure → lymphoedema.
2. **Immune surveillance** — lymphatics are the highway for antigen-presenting cells (DCs, macrophages) carrying captured antigens from tissues to regional lymph nodes where adaptive immune responses are initiated.
3. **Lipid transport** — dietary fat (chylomicrons, >75 nm — too large for fenestrated capillaries) is absorbed into intestinal lacteals → mesenteric lymphatics → cisterna chyli → thoracic duct → blood.

## Structure

### Lymphatic Capillaries

Lymphatic capillaries are blind-ended, highly permeable endothelial tubes with a unique structure permitting efficient uptake of interstitial fluid, large macromolecules, lipid particles, and cells [^alberts-mol-cell-biology]:
- **Button junctions**: discontinuous, overlapping VE-cadherin contacts between lymphatic endothelial cells (LECs) create flap-like openings that act as one-way valves allowing fluid entry but preventing backflow
- **No basement membrane** (or extremely thin, discontinuous)
- **Anchoring filaments**: connect LECs to surrounding extracellular matrix; when tissue pressure rises (inflammation, oedema), filaments pull junctions open → ↑lymphatic uptake
- Extremely low intraluminal pressure (~0 mmHg at rest)
- Identifiable by LYVE-1 (lymphatic vessel endothelial hyaluronan receptor-1), podoplanin (PDPN/gp38), PROX1 (nuclear master TF of LEC identity), VEGFR3

### Collecting Lymphatics

Collecting lymphatics propel lymph from capillaries toward lymph nodes and the thoracic duct [^guyton-hall]:
- **Zipper junctions** (continuous VE-cadherin) — less permeable than capillaries
- **Lymphatic smooth muscle** (LSM) — intrinsic pacemaker-like contractions (~10 contractions/min); stretch-sensitive; driven by IP₃-mediated Ca²⁺ release and myosin light chain kinase (MLCK); extrinsically augmented by compression (arterial pulsatility, skeletal muscle pumping, respiration)
- **Bicuspid valves** every 1–2 cm — prevent lymph backflow; critical for unidirectional flow; valve-to-valve segments are called **lymphangions** (functional pump units)
- Innervated by sympathetic adrenergic fibres (vasoconstriction/tone modulation)

### Lymph Nodes

400–700 lymph nodes in the adult human body; clustered at anatomical junctions (cervical, axillary, inguinal, mesenteric/coeliac, iliac, para-aortic, mediastinal) [^guyton-hall].

**Detailed architecture**:
| Zone | Cell populations | Function |
|:---|:---|:---|
| Capsule + trabeculae | Fibroblastic reticular cells (FRCs) | Structural; conduit network for small antigens and cytokines |
| Subcapsular sinus (SCS) | SCS macrophages (CD169/Siglec-1⁺); DCs | First filter; trap large antigens and cell debris; relay to follicular DCs and B cells |
| Cortex (follicles) | Follicular DCs (FDCs); B cells; Tfh | Primary follicles (naïve B cells); secondary follicles with **germinal centres** (centroblasts → somatic hypermutation → centrocytes → affinity selection by FDC → affinity maturation → class switch → plasma cells or memory B cells) |
| Paracortex (T-cell zone) | DCs; naïve and memory T cells; HEV | DCs present antigen on MHC-I (CD8 CTL) and MHC-II (CD4 Th); HEV (high endothelial venules, PNAd+/ICAM-1+/VCAM-1+) are the portal for naïve lymphocyte entry from blood; CCL19/21 attract CCR7+ DCs and T cells |
| Medullary cords and sinuses | Plasma cells; macrophages | Antibody secretion; filtration of lymph before efferent exit |
| Efferent lymphatics | — | Lymph exits carrying antibodies, effector cells toward the next node or thoracic duct |

### Thoracic Duct and Cisterna Chyli

The thoracic duct (the largest lymphatic vessel; 38–45 cm long, 5 mm diameter at origin) collects lymph from the left upper body and all of the lower body (legs, pelvis, abdomen, left thorax, left arm, left head/neck), carrying 2–4 L/day, emptying into the left subclavian vein at the jugulo-subclavian junction. The **right lymphatic duct** drains the right upper body into the right subclavian vein [^guyton-hall].

The **cisterna chyli** (when present) is the dilated lymphatic reservoir at L1-L2, receiving intestinal lymphatics (lacteals) loaded with dietary chylomicrons (giving lymph/chyle a milky appearance postprandially) and lumbar lymphatics.

### Spleen

The spleen (~150 g, largest lymphoid organ) performs dual immune and haematological functions [^guyton-hall]:

**Red pulp** (80% of volume):
- **Splenic cords of Billroth** — loose reticular meshwork; red pulp macrophages (CD163+, CD68+) scrutinise passing RBCs; senescent/abnormal RBCs (↓deformability — cannot squeeze through 1–3 μm slit pores of venous sinuses) are trapped and phagocytosed (extravascular haemolysis)
- **Venous sinuses** — fenestrated endothelium (2–3 μm gaps) through which deformable RBCs must squeeze; the bottleneck that filters the blood (~350 L of blood filtered per day)
- **Functions**: RBC quality control; iron recycling (haemoglobin → haem oxygenase → biliverdin → bilirubin [exported] + iron [recycled via ferroportin → transferrin → bone marrow]); platelet reservoir (~30% of total platelets sequestered at rest); extramedullary haematopoiesis (foetal; pathological in myelofibrosis, haemolytic anaemias)

**White pulp** (immune function):
- **PALS (periarteriolar lymphatic sheath)** — T cell zone (CD4+ and CD8+ T cells, DCs) surrounding the central arteriole; site of T cell activation by blood-borne antigens
- **Primary/secondary follicles** — B cell zone; secondary follicles develop germinal centres upon antigen stimulation; produce IgM/IgG/IgA
- **Marginal zone (MZ)** — ring surrounding white pulp; MZ B cells (CD21hi, IgMhi, IgDlo) are pre-activated, mount rapid T-independent IgM responses to polysaccharide antigens (encapsulated bacteria) without the germinal centre delay; this is why splenectomy → ↑susceptibility to encapsulated organisms (S. pneumoniae, H. influenzae, N. meningitidis)

### Thymus

A bilobed primary lymphoid organ in the anterior superior mediastinum, maximal at puberty (~40 g), progressively replaced by adipose tissue (involutes) throughout adult life [^guyton-hall].

**Architecture**:
- **Cortex**: densely packed developing thymocytes (CD4-CD8- double negative → CD4+CD8+ double positive) among cortical thymic epithelial cells (cTECs); site of positive selection — DP thymocytes must recognise self-MHC + peptide with sufficient affinity to survive; ~95% fail and die by neglect
- **Medulla**: mature single-positive thymocytes (CD4+ or CD8+) among medullary thymic epithelial cells (mTECs) expressing self-antigens under **AIRE** (autoimmune regulator) transcriptional control; negative selection — T cells recognising self-antigens with high affinity undergo clonal deletion or Treg conversion; ~5% of DP thymocytes eventually exit as mature naive T cells
- **Hassall's corpuscles**: whorled keratin structures in medulla; secrete TSLP → tolerise DCs toward Treg induction

### MALT (Mucosa-Associated Lymphoid Tissue)

Lymphoid tissue embedded in mucosal surfaces without a capsule [^guyton-hall]:
- **Tonsils** (Waldeyer's ring): palatine + pharyngeal (adenoids) + lingual; first lymphoid encounter of ingested/inhaled antigens
- **Peyer's patches** (gut): 10–70 in ileum; M cells (microfold cells) transcytose luminal antigens from gut lumen → subepithelial dome (SED) DCs → Peyer's patch T and B zones → IgA production → secretory IgA (sIgA) into gut lumen (dimeric IgA + secretory component)
- **BALT** (bronchus-associated LT): induced in lung during infection/inflammation; not constitutive
- **GALT** (gut-associated LT): includes mesenteric lymph nodes as central processing hubs

## Function

### Fluid Homeostasis

At the capillary level, Starling forces dictate net fluid movement [^guyton-hall]:
- At the arterial end: hydrostatic pressure (~35 mmHg) exceeds oncotic pressure (~28 mmHg) → net filtration (~20 mL/min systemic)
- At the venous end: hydrostatic falls to ~15 mmHg; net reabsorption slightly less than filtration
- **Net filtration ≈ 3 L/day** that is not reabsorbed by venous capillaries → must be returned via lymphatics to prevent progressive oedema

Lymphatic capillaries generate their uptake force through tissue pressure rising above the slight negativity of lymph capillary pressure. The lymphangion pumping mechanism propels lymph against gravity (e.g., from feet to thoracic duct, >100 cm).

### Immune Surveillance and Adaptive Immunity

The lymph node functions as the critical encounter point between travelling antigen-bearing DCs (arriving via afferent lymph) and recirculating naïve lymphocytes (entering via HEV) [^alberts-mol-cell-biology]:

1. Tissue injury/infection → DC maturation → CCR7 upregulation → migration along CCL19/21 gradient into afferent lymphatics → subcapsular sinus → paracortex
2. Naïve T cells enter via HEV (L-selectin/PNAd tethering → LFA-1/ICAM-1 arrest → diapedesis → CCR7-guided paracortex migration)
3. DC–T cell cognate interaction (TCR-pMHC + CD28-B7 + cytokine signals) → T cell activation → clonal expansion
4. Tfh cells form in paracortex → migrate to follicle border → cognate B cell interaction → germinal centre reaction
5. Plasma cells and memory cells exit via efferent lymphatics → blood → effector tissues

### Dietary Lipid Transport

Enterocytes package dietary triglycerides + cholesterol + apoB-48 into chylomicrons (75–1,200 nm) — too large for the tight inter-endothelial junctions of blood capillaries. Chylomicrons enter intestinal lacteals via the permeable button junctions → mesenteric lymphatics → cisterna chyli → thoracic duct → left subclavian vein → bloodstream. This route explains why fat-soluble vitamins (A, D, E, K), lipophilic drugs, and fat-soluble toxins initially enter the circulation via the lymphatic (not portal) route, bypassing first-pass hepatic metabolism [^guyton-hall].

## Connections

- `contains` → **[Spleen](../../06-organ/spleen/README.md)** — largest secondary lymphoid organ; RBC quality control and adaptive immune responses to blood-borne antigens
- `contains` → **[Thymus](../../06-organ/thymus/README.md)** — primary lymphoid organ for T-cell education (positive and negative selection)
- `modulates` → **[Immune System](../immune-system/README.md)** — lymph nodes are the hubs of adaptive immune activation; HEV enable lymphocyte trafficking; germinal centres drive antibody affinity maturation
- `modulates` → **[Cardiovascular System](../cardiovascular-system/README.md)** — returns 2–4 L/day lymph to venous circulation; collecting lymphatics are active pumps essential for plasma volume homeostasis
- `contains` → **[B Cell](../../04-cellular/b-cell/README.md)** — Lymph node GCs drive B cell affinity maturation: FDC antigen selection → SHM + class switch → plasma cells or memory B cells; Peyer's patch GCs → sIgA class switching; splenic MZ B cells mount T-independent IgM responses to polysaccharide antigens.
- `contains` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Naive T cells enter via HEV → cognate DC-T cell interaction in paracortex → Th1/Th2/Th17/Tfh differentiation; Tfh cells migrate to GC border → provide CD40L/IL-21 help to B cells → affinity maturation and CSR; the paracortex is the primary site of naive T cell activation.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow is the lymphopoiesis site: HSC → CLP → pro-B cells (VDJ → μ chain → pre-BCR → naive B cell export); NK cells, ILC progenitors, and DC precursors also originate in bone marrow; T cell progenitors exit bone marrow and migrate to thymus for positive/negative selection.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The lymphatic system drains and patrols the reproductive organs: pelvic and para-aortic nodes filter lymph from uterus, ovaries, prostate, and testes — so nodal status drives staging and spread of gynecologic and prostate cancers, and sentinel-node mapping guides their surgery.
- `contains` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are the lymphatic system's messengers: they capture antigen in tissues, then migrate through afferent lymphatics to the draining lymph node to present it to naive T cells — linking innate detection to adaptive immunity, and the basis of DC cancer vaccines.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Hodgkin lymphoma is the prototypical cancer of the lymphatic system: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), reflecting lymphatic drainage anatomy — unlike the scattered spread of non-Hodgkin lymphomas.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Diffuse large B-cell lymphoma is the commonest malignancy of the lymphatic system: it arises from germinal-center or activated B cells in lymph nodes (or extranodal lymphoid tissue), producing rapidly enlarging masses—the lymphatic system's own immune cells becoming cancer.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells are the antibody-secreting end-product of the lymphatic system: B cells activated in lymph-node germinal centers become plasma cells that home to bone marrow and mucosa to pump out immunoglobulin, the humoral output of lymphoid tissue—malignant as myeloma.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut houses the largest share of the lymphatic system: gut-associated lymphoid tissue (Peyer patches, mesenteric nodes) and lacteals that absorb dietary fat make the digestive tract a major immune and lymph-transport organ, tying mucosal immunity and fat transport together.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Follicular lymphoma is a cancer of the lymphatic system's architecture: it arises from germinal-center B cells in lymph node follicles and spreads through nodes, spleen and marrow—turning antibody-maturation machinery into an indolent malignancy.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — The lymphatic system governs how breast cancer is staged: tumor cells drain first to axillary lymph nodes, so sentinel-node biopsy guides treatment and node status drives prognosis—while removing nodes can cause arm lymphedema, the cost of disrupting drainage.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Melanoma exploits the lymphatic system to metastasize: it spreads early through dermal lymphatics to regional nodes, making sentinel lymph-node biopsy central to staging, and can even induce lymphangiogenesis—so lymphatic involvement strongly predicts outcome.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Mantle cell lymphoma illustrates the lymphatic system's vulnerability: arising from mantle-zone B cells of the lymph node, it spreads through the lymphatic network to nodes, marrow and gut—the system built to circulate lymphocytes also disseminates their cancers.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells patrol the lymphatic system: alongside B and T cells they traffic through lymph nodes screening for infected and tumor cells, and rare NK-cell lymphomas arise here—part of the immune surveillance the lymphatic network is built to support.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine feeds the lymphatic system dietary fat: specialized lacteals in each villus absorb fat as chyle and carry it through lymphatics to the bloodstream, so gut lymphatics handle nutrition as well as immunity—and blockage causes fat malabsorption.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages patrol the lymphatic system: positioned in lymph-node sinuses, they filter incoming lymph, capture pathogens and present antigen to lymphocytes, so the lymphatics are not just drainage but a surveillance network staffed by phagocytes.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — The lymphatic system is where antibodies are made: B cells in lymph-node germinal centers mature into plasma cells producing IgG, which drains into blood to neutralize pathogens—so the lymphatics turn captured antigen into circulating humoral immunity.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — The gut's lymphatic tissue produces secretory IgA: Peyer's patches and mesenteric nodes generate IgA-secreting plasma cells that protect mucosal surfaces, so the lymphatic system guards the body's largest interface with the outside world.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Lymphatic vessels grow under VEGF control: VEGF-C and VEGF-D acting on VEGFR-3 drive lymphangiogenesis, building and remodeling the lymphatic network—and tumors hijack this signal to sprout lymphatics that carry cancer cells to lymph nodes.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is the body's largest single source of lymph: high sinusoidal filtration produces protein-rich hepatic lymph that drains via the thoracic duct, so in cirrhosis overwhelmed lymphatics contribute to the ascites that fills the abdomen.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Lymph nodes are where cytotoxic T cells are armed: naive CD8 cells survey nodes until a dendritic cell presents antigen, then activate and exit through lymphatics into blood to hunt infected or tumor cells—so the lymphatic system stages antiviral and antitumor immunity.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — The lymphatic system rescues leaked albumin: capillaries constantly leak protein into tissues, and lymph vessels collect this albumin-rich fluid and return it to the blood—so blocked lymphatics cause the protein-rich swelling of lymphedema.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Lymphatic vessels are built from specialized endothelial cells: distinct from blood-vessel lining, these cells form one-way valves and loose junctions that soak up fluid, and VEGF-C drives them to sprout new lymphatics (lymphangiogenesis).
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Lymph nodes are where regulatory T cells learn tolerance: the lymphatic system funnels antigens and lymphocytes into nodes where Tregs are induced and licensed, making lymphoid tissue the training ground for immune self-restraint.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — The lymphatic system is the body's fat-transport highway: intestinal lacteals absorb dietary fats packaged as chylomicrons—rich in cholesterol and triglyceride—into lymph rather than blood, delivering them to the circulation downstream.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin depends on its lymphatics for drainage and defense: a fine network clears fluid and ferries antigen-loaded dendritic cells to nodes, so when it fails, fluid pools as lymphedema and immune surveillance of the skin suffers.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Skin lymphatics help regulate the body's sodium: salt stored in the skin is sensed by macrophages that trigger lymphatic growth to clear it, an unexpected role linking the lymphatic system to sodium balance and blood pressure.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lungs sit at the lymphatic system's outflow: the thoracic duct empties lymph near the heart, and injury to it leaks milky lymph into the chest as a chylothorax, a distinctive lymphatic emergency.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Lymph nodes do their work in germinal centers: within them B cells multiply, mutate, and are selected to make ever-better antibodies, the engine of the adaptive response the lymphatic system carries.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut holds the body's largest lymphatic tissue: the bowel wall, including the large intestine, is packed with lymphoid follicles (GALT) that sample microbes and mount the mucosal immunity the lymphatics coordinate.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — The lymphatic system is mapped with radiotracers: lymphoscintigraphy follows injected photons to find the sentinel node in cancer staging and to chart blocked drainage in lymphedema.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Lymph is pumped, not just drained: smooth-muscle cells in the walls of collecting lymphatics contract rhythmically to push lymph against gravity toward the chest.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The lymphatic system returns its fluid to the blood at the heart: the thoracic duct empties into the great veins near it, closing the loop between lymph and circulation.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the lymphatic capillary's clever valve: its endothelial cells overlap as loose flaps tethered by anchoring filaments, opening one way to admit fluid and large molecules and closing to keep them from leaking back.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain was long thought to have no lymphatics — then they were found: meningeal lymphatic vessels and the glymphatic flow along blood vessels drain the brain's waste, a discovery reshaping how we think about Alzheimer's and brain fluid.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney has its own lymphatic drainage: renal lymphatics clear interstitial fluid and immune cells from the kidney, and their dysfunction contributes to the swelling and inflammation of kidney disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Lymph is the antibody's highway: afferent lymph carries antigen to the nodes where plasma cells make antibody, then efferent lymph and the thoracic duct pour that immunoglobulin into the bloodstream, so lymphatic blockage blunts the spread of the response.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Infection can race up the lymphatics: bacteria draining from a wound inflame the vessels into lymphangitis, the tender red streak tracking toward a swollen node as neutrophils pour in to fight the spreading microbes.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets keep blood and lymph apart: in development their CLEC-2 receptor binds podoplanin on budding lymphatic endothelium and plugs the junction so the new vessels stay blood-free — a separation whose failure leaves lymphatics blood-filled.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — Tuberculosis loves the lymph nodes: when M. tuberculosis seeds the cervical nodes it produces scrofula, a chronic swelling and breakdown of the lymphatic tissue that is one of TB's commonest sites outside the lung.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The lymphatics carry the fat from a meal: gut lacteals absorb dietary lipids as chylomicrons and ferry them through lymph into the blood, and leaky or damaged lymphatics promote local fat deposition — linking the system to adipose tissue.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Scarring chokes the lymph vessels: TGF-beta drives the fibrosis that stiffens lymphatic channels in chronic lymphedema, while also restraining the lymphangiogenesis needed to repair them — a target for keeping lymph flowing.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut feeds the lymph: specialized lacteals inside each intestinal villus collect the fat absorbed by the epithelium, packaging dietary lipids into milky chyle that drains through the lymphatics to the bloodstream — the lymphatic system's role in nutrition.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — When the heart backs up, the lymphatics flood: high venous pressure in heart failure outpaces lymphatic return of interstitial fluid, so the drainage system is overwhelmed and fluid pools as the edema and effusions that mark decompensation.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — The vessels pump themselves with a gas signal: nitric oxide released by lymphatic endothelium tunes the rhythmic contractions of lymphatic muscle that propel lymph forward, so it helps set the pace of drainage against gravity.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Strep inflames the lymphatic channels: Streptococcus pyogenes causes lymphangitis — the red streak tracking up a limb toward the nodes — and recurrent attacks scar the vessels into chronic lymphedema.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess fat throttles the lymphatics: obesity impairs lymphatic pumping and damages the vessels, causing a distinct obesity-related lymphedema, while the lymphatic system in turn shapes fat deposition and inflammation.
- `connects-to` → **[CLL](../cll/README.md)** — A lymphoid leukemia fills the system: chronic lymphocytic leukemia accumulates malignant B lymphocytes that swell the lymph nodes and spleen, a tumor of the very cells the lymphatic system is built to circulate.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — The fastest cancer grows in its tissue: Burkitt lymphoma is an explosive germinal-center B-cell tumor of the lymphatic system, the most rapidly proliferating human cancer, often presenting as a bulky nodal or abdominal mass.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — A virus makes the lymphatic system its home: Epstein-Barr virus infects B lymphocytes, causing the lymphadenopathy of mononucleosis and driving several lymphomas that arise from the cells it transforms.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The lymphatics are a highway for infection: pathogens draining through lymph cause lymphangitis and lymphadenitis, and when the nodes are overwhelmed the infection can spill into the blood as sepsis.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — It is a disease of the lymphoid organs: HIV replicates in and progressively destroys the CD4 T cells and lymphoid tissue of the lymphatic system, with persistent lymphadenopathy and eventual collapse of nodal architecture.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — It classically inflames the nodes: Mycobacterium tuberculosis causes lymphadenitis — scrofula in the neck — a granulomatous infection of the lymphatic system that can persist or drain through the skin.
- `connects-to` → **[Peripheral T-cell Lymphoma](../ptcl/README.md)** — Its own T cells can turn malignant: peripheral T-cell lymphomas arise from the mature T lymphocytes that populate the lymph nodes, an aggressive cancer of the lymphatic system's cellular residents.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — When lymph drainage fails, the skin breaks down: lymphedema from damaged or removed lymphatics causes chronic swelling, fibrotic skin changes and ulcers that heal poorly without drainage.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Stagnant lymph invites recurrent infection: lymphedema impairs immune surveillance in the swollen limb, predisposing to repeated cellulitis and erysipelas, often from staphylococci and streptococci.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Chronic swelling and disfigurement weigh on mood: the disabling, visible and progressive nature of lymphedema, and the burden of lymphatic cancers, contribute to depression and reduced quality of life.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The skeleton houses its factory and its drainage burdens the limbs: bone marrow is the primary lymphoid organ that makes lymphocytes, and limb lymphatics, when they fail, swell the soft tissues with lymphedema.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The chest holds its great vessel: the thoracic duct returns lymph to the bloodstream in the chest, so its injury causes chylothorax, and pulmonary lymphatics clear the lung's interstitial fluid.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It drains the skin and shows there when it fails: dermal lymphatics clear fluid and immune cells from the skin, so lymphedema thickens and hardens it and breached skin lets lymphangitis track up the limb.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The brain has its own drainage: the glymphatic system and newly-discovered meningeal lymphatic vessels clear cerebrospinal fluid and waste to cervical lymph nodes, linking the lymphatic and nervous systems.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The thymus is a lymphoid and endocrine organ: this primary lymphoid organ where T cells mature also secretes thymic hormones, sitting at the crossroads of the lymphatic and endocrine systems.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A hidden network drains the kidney: a rich renal lymphatic system clears interstitial fluid and protein from the kidney, and when overwhelmed it contributes to the oedema of nephrotic syndrome.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A classic cause of swollen nodes: toxoplasmosis typically presents with painless cervical lymphadenopathy, a common reactive enlargement of the lymphatic system.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — The lymphatics absorb dietary fat: long-chain fats and fat-soluble vitamins enter specialised intestinal lacteals as chyle rather than the portal blood, carried by the lymphatic system to the circulation.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — A lymphoid malignancy of the system: Waldenström macroglobulinaemia is a lymphoplasmacytic lymphoma that infiltrates lymph nodes, spleen and marrow, secreting IgM that thickens the blood.
- `connects-to` → **[Peyer's Patches](../../05-tissue/peyers-patches/README.md)** — Gut lymphoid tissue is part of it: Peyer's patches and other gut-associated lymphoid tissue are major secondary lymphoid organs of the lymphatic system, sampling intestinal antigens to launch mucosal immunity.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — A virus that lives in the lymph nodes: HIV replicates in and progressively destroys lymphoid tissue, causing the generalised lymphadenopathy and follicular collapse that mark advancing infection.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its cancers are chemo-treated: the lymphomas and leukaemias arising in lymphoid tissue are treated with combination chemotherapy, the mainstay of curing many of them.
- `connects-to` → **[ALL](../all/README.md)** — Cancer of the lymphoid progenitor: acute lymphoblastic leukaemia is the malignant proliferation of immature B- or T-lymphocyte precursors, the founding cells of the lymphatic system, filling marrow and infiltrating lymph nodes, thymus and spleen.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — The plasma cell at its end stage turns malignant: multiple myeloma is a clonal cancer of antibody-secreting plasma cells—the terminal product of the lymphatic system's B-cell lineage—accumulating in bone marrow and flooding blood with monoclonal immunoglobulin.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Where anti-tumour immunity is orchestrated: checkpoint inhibitors work largely within the lymphatic system, freeing T cells primed by dendritic cells in the lymph nodes that drain a tumour, so intact lymphatic drainage shapes the response to immunotherapy.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Lymphoedema fibrosis: chronic lymph stasis—after node dissection, radiation or filariasis—drives tissue fibrosis and fat deposition, the irreversible limb swelling that defines lymphoedema.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Lymphoid proliferation and MALT lymphoma: Sjögren's chronic lymphocytic infiltration of glands forms ectopic lymphoid tissue and carries the highest lymphoma risk of the autoimmune diseases, a disorder of the lymphatic system itself.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Ectopic lymphoid tissue in the joint: rheumatoid arthritis builds germinal-centre-like follicles in inflamed synovium and causes lymphadenopathy, with a raised risk of lymphoma from chronic lymphatic activation.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Lymphatics clear the artery: adventitial lymphatic vessels drain cholesterol from the arterial wall in reverse cholesterol transport, and when they fail, lipid accumulates and atherosclerosis worsens—an unexpected role for the lymphatic system in heart disease.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Nodal spread defines prognosis: head and neck cancer metastasises first to the cervical lymph nodes, so the lymphatic system's drainage map dictates staging, neck dissection and the entire treatment plan.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The biggest lymph source: the liver generates a large share of the body's lymph from protein-rich fluid in the hepatic sinusoids, and when cirrhosis overwhelms this drainage the overflow becomes ascites.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Lymph-node homing: CXCL12 (with CXCR4) directs the trafficking and positioning of lymphocytes and dendritic cells within lymph nodes, organising the adaptive immune response.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and lymphedema: adipose-derived leptin links obesity to impaired lymphatic vessel function and lymphoedema, and it also modulates immune cells within lymph nodes.
- `connects-to` → **[Trypanosoma brucei](../../../02-pathogen/04-parasites/trypanosoma-brucei/README.md)** — Lymphatic-tropic infection: African trypanosomiasis spreads through and enlarges lymph nodes—the posterior cervical swelling of Winterbottom's sign—before invading the central nervous system.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Lymphoid organogenesis: TNF-family signalling builds and maintains the secondary lymphoid organs, and excess TNF-α drives the reactive lymph-node enlargement of infection and inflammation.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell follicles: BAFF sustains the B cells of lymph-node and splenic follicles, organising the germinal-centre reactions at the heart of the lymphatic system's adaptive immunity.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Germinal-centre signalling: IL-6 within lymph nodes supports T-follicular-helper and B-cell responses, and its excess drives lymphadenopathy in conditions like Castleman disease.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Lymphangiogenesis: the angiopoietin-Tie2 axis, with VEGF-C, builds and remodels lymphatic vessels, and its dysregulation underlies the failed vessel formation of primary lymphoedema.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Lymph-node immunity: complement C3 opsonises antigens trafficked to lymph nodes and is retained on follicular dendritic cells, focusing the humoral immune responses the lymphatic system orchestrates.
- `connects-to` → **[ApoE](../../03-molecular/apoe/README.md)** — Dietary-lipid transport: intestinal lacteals absorb dietary fat as ApoE-bearing chylomicrons into the lymph (chyle), the lymphatic system's distinctive role in carrying fat to the bloodstream.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Adrenomedullin signaling through RAMP2 is essential for lymphatic vessel formation and for maintaining the integrity of the lymphatic endothelium, so its disruption causes severe developmental lymphatic defects and edema.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Prostaglandins regulate the rhythmic intrinsic contractions of collecting lymphatics that actively propel lymph against gravity, the pumping mechanism that returns interstitial fluid and protein to the bloodstream.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine and other inflammatory mediators increase lymphatic permeability and modulate lymphatic contractility, coupling local inflammation to the lymph drainage and immune-cell transport that the lymphatic system provides.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Rhythmic calcium transients in lymphatic-vessel smooth muscle drive the spontaneous contractions of each lymphangion that actively pump lymph against gravity, the intrinsic pacemaker mechanism propelling lymph back to the bloodstream.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Sympathetic norepinephrine acting on lymphatic-muscle adrenergic receptors modulates the frequency and force of lymphatic contractions, the neural control of lymph flow that adjusts drainage to the body's needs.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Lymph carries antigen-presenting cells to the lymph nodes, where MHC-class-II presentation to T cells launches the adaptive immune response—the immune-surveillance function that is the lymphatic system's defining role.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 modulates the contractility of lymphatic collecting vessels, working alongside the nitric oxide and norepinephrine already mapped to set the intrinsic pumping that propels lymph.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 drives the clonal proliferation of T cells within lymph nodes, the amplification step of the adaptive immune response that the lymphatic system organizes.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Bradykinin raises capillary permeability and interstitial fluid formation, increasing the filtered load that the lymphatics must return to the circulation to prevent edema.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 and related chemokines direct the trafficking of monocytes and dendritic cells into and through the lymphatic system, guiding antigen delivery to draining lymph nodes.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic T cells primed in the lymph nodes deploy perforin to kill infected and malignant cells, an effector arm generated by the lymphatic system's adaptive response.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — The PD-1 checkpoint operating within lymph nodes enforces peripheral tolerance, restraining the T-cell responses organized in lymphatic tissue.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling downstream of VEGFR3 (VEGF mapped) drives lymphatic-endothelial proliferation and lymphangiogenesis and supports lymphocyte survival in lymphoid organs.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR governs lymphatic-endothelial growth — its inhibition (sirolimus) treats lymphatic malformations — and shapes the metabolism of lymphocytes trafficking through the system.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT cytokine signaling coordinates the lymphocyte differentiation and effector responses orchestrated within the lymphatic organs.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 (JAK1/2 already mapped) programs the T-follicular-helper and Th17 differentiation and germinal-center responses of the lymphatic organs.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon-programmed antiviral and antitumor lymphocyte responses coordinated within the lymphatic system.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates lymphocyte apoptosis, lymphangiogenesis and the immune regulation that occurs within the lymphatic organs.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate lymphocyte homeostasis and the lymphatic-endothelial stress responses across the lymphatic system.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling governs lymphatic-vessel development and remodeling and the regulatory immune tone of the lymphatic system.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α couples the metabolic and inflammatory status of lymphoid tissue to the lymphangiogenesis (VEGF already mapped) of the lymphatic system.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), acting downstream of VEGFR-3 (VEGF already mapped), governs the lymphatic-endothelial growth and remodeling of the lymphatic system.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of VEGFR-3 and other receptors drives the lymphangiogenesis and lymphatic-endothelial responses of the lymphatic system.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB inflammatory signaling regulates the lymphatic-endothelial and lymph-node immune responses of the lymphatic system.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the lymphatic-endothelial and immune-cell metabolism of the lymphatic system.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy participates in the lymphocyte homeostasis and lymphatic-endothelial maintenance of the lymphatic system.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the trafficking of leukocytes through the lymphatic vessels and nodes of the lymphatic system.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the lymphocyte and lymphatic-endothelial gene programs of the lymphatic system.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the lymphatic-endothelial junction dynamics and immune-cell activation of the lymphatic system.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the lymphatic-endothelial and immune responses of the lymphatic system.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β signaling participates in the inflammatory and immune-trafficking responses of the lymphatic system.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the lymphocyte-mediated immune responses of the lymphatic system.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of lymphocyte differentiation in the lymphatic system.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Peripheral tolerance: CTLA-4 restrains T-cell activation in lymph nodes and enforces self-tolerance (alongside PD-1 already mapped), a checkpoint that keeps the lymphatic system's constant immune surveillance from turning on the host.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 and humoral arm: IL-4 drives the Th2 response and B-cell antibody class-switching within lymphoid tissue, one of the polarised programmes (balanced against Th1) the lymphatic system uses to tailor immunity to different threats.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 differentiation: IL-12 from dendritic cells drives naive T cells toward the Th1 programme and activates NK cells, directing the cell-mediated immunity that the lymphatic system mounts against intracellular pathogens.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Cell-mediated effector: interferon-gamma from the Th1 cells and NK cells the lymphatic system marshals (IL-12 already mapped) activates macrophages and cytotoxic responses, the effector cytokine of the cell-mediated immunity against intracellular pathogens.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune regulation: IL-10 from regulatory lymphocytes in lymphoid tissue restrains the immune response, balancing the Th1 (IL-12 already mapped) and Th2 programmes to resolve inflammation and preserve tolerance within the lymphatic system.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Vessel structure and lymphoedema: collagen forms the framework of lymphatic vessels and lymph nodes, and when lymph drainage fails, the chronic protein-rich stasis drives the fibrosis and collagen deposition of lymphoedema.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Perilymphatic immunity: mast cells cluster around lymphatic vessels, releasing histamine (already mapped) and mediators that regulate lymphatic contractility and permeability, part of the immune surveillance woven through the lymphatic system.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic lymph: the liver produces a large fraction of the body's lymph from the sinusoidal fluid, and when hepatic lymph outstrips drainage in cirrhosis or heart failure it forms ascites, a major output of the lymphatic system.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary lymphatics and chyle: the lungs are drained by a rich lymphatic network, and disruption of the thoracic duct spills lymph as a chylothorax, illustrating the lymphatic transport of fat-laden chyle.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 lymphatic remodelling: IL-13, with IL-4 (already mapped), is the type-2 cytokine that, alongside the lymphangiogenic VEGF (already mapped), drives the lymphatic remodelling seen in filariasis and chronic inflammation of the lymphatic system.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Lympho-adipose crosstalk: adiponectin, with leptin (already mapped), mediates the crosstalk between the lymphatic vessels and the perinodal and subcutaneous adipose tissue that supports lymphatic function.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu of the fat surrounding the lymphatics and lymph nodes, linking metabolism to lymphatic and immune function.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Sinus macrophages: the subcapsular-sinus and medullary macrophages of the lymph nodes filter the lymph and present the captured antigens, the resident phagocytes of the lymphatic system.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK trafficking: the natural killer cells (perforin already mapped) traffic through the lymphatic system, providing the innate cytotoxic surveillance of the circulating lymph and nodes.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Interstitial sodium and lymphoedema: the lymphatic system clears the interstitial sodium and fluid, and its dysfunction produces the sodium-rich lymphoedema, linking the lymphatics to the body's sodium and volume balance.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil trafficking: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), expands and traffics the eosinophils through the lymphatic system in the allergic and anti-helminth responses.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 lymphoid axis: IL-23 sustains the Th17 (IL-17 already mapped) cells generated and trafficked through the lymph nodes of the lymphatic system for the mucosal defence.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — IgE class-switch: the IgE (with IL-4 and IL-13 already mapped) is class-switched in the germinal centres of the lymph nodes (immunoglobulin already mapped) of the lymphatic system, arming the allergic response.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement (C3 already mapped) pathway in the lymph and interstitial fluid, protecting the host tissue drained by the lymphatic system.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Permeability control: the C1-esterase inhibitor regulates the complement and contact (bradykinin already mapped) systems; its deficiency causes the angioedema of the interstitial tissues drained by the lymphatic system.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Immune-complex ferrying: the erythrocytes bind the complement (C3 already mapped)-opsonised immune complexes via CR1 and deliver them to the splenic and hepatic phagocytes, complementing the lymphatic clearance of the lymphatic system.

## Pathology

### Lymphoedema

Failure of lymphatic drainage → progressive protein-rich fluid accumulation in the interstitium → tissue fibrosis and adipose deposition [^guyton-hall].

**Primary lymphoedema**: monogenic disorders of lymphatic development:
- Milroy disease (VEGFR3/FLT4 loss-of-function → absent/hypoplastic lymphatics, bilateral leg oedema from birth)
- Meige disease / lymphoedema praecox (FOXC2 mutations → lymphatic valve aplasia → pubertal onset)
- Lymphoedema-distichiasis (FOXC2 mutations → extra eyelash row + lymphoedema)
- Hennekam syndrome (CCBE1, ADAMTS3 mutations → generalised lymphangiectasia)

**Secondary lymphoedema** (far more common):
- **Filariasis** (W. bancrofti/B. malayi/B. timori — most common worldwide cause; mosquito-transmitted nematodes invade collecting lymphatics → inflammatory obstruction → chronic progressive elephantiasis)
- **Breast cancer surgery + radiotherapy** — sentinel node biopsy/axillary clearance + RT → 20–30% incidence of arm lymphoedema; similarly pelvic node dissection → leg lymphoedema
- **Infection** (recurrent cellulitis, lymphangitis)

**Treatment**: complex decongestive therapy (CDT) — manual lymphatic drainage + compression bandaging + skin care; pneumatic compression devices; vascularised lymph node transfer (surgical); lymphovenous anastomosis.

### Lymphoma

Malignancies of lymphoid cells; classified by cell of origin and molecular features [^alberts-mol-cell-biology]:

**Hodgkin Lymphoma (HL)**:
- Reed-Sternberg cells (RS cells: binucleate/multinucleate giant cells, CD30+, CD15+, PAX5 dim, CD45−) are the malignant cell, derived from germinal centre B cells that have lost BCR expression (normally lethal but RS cells escape via NF-κB and JAP/STAT signalling)
- Strong EBV association (~40% classic HL)
- Subtypes: nodular sclerosis (most common, young adults, mediastinal), mixed cellularity, lymphocyte-rich, lymphocyte-depleted; nodular lymphocyte predominant HL (LP cells, CD20+, CD45+)
- Treatment: ABVD (doxorubicin/bleomycin/vinblastine/dacarbazine) → >85% cure in early-stage; brentuximab vedotin (anti-CD30 ADC) + nivolumab for relapsed/refractory

**Non-Hodgkin Lymphoma (NHL)** (~60 distinct entities by WHO classification):
| Subtype | Key features | Genetics |
|:---|:---|:---|
| DLBCL (large B cell) | Most common NHL (~30%); aggressive; R-CHOP | BCL6, MYC, BCL2 — "double/triple hit" → poor prognosis |
| Follicular lymphoma (FL) | Indolent; GCB origin; follicular pattern | t(14;18) → BCL2 overexpression → ↓apoptosis; R-bendamustine |
| Burkitt lymphoma (BL) | Highly aggressive; jaw masses in endemic BL (children); abdominal in sporadic | t(8;14) → MYC overexpression; EBV (endemic); HIV-associated |
| CLL/SLL | Indolent; blood + marrow; CD5+, CD23+, surface IgM low | del(17p)/TP53 → ibrutinib/venetoclax; IGHV mutated → better prognosis |
| Mantle cell lymphoma (MCL) | Moderately aggressive; CD5+, CD23−; widespread | t(11;14) → cyclin D1 overexpression → ↑cell cycle entry |
| Marginal zone lymphoma | MALT-type (stomach, lung, salivary gland); splenic; nodal | Gastric MALT: H. pylori-driven; t(11;18)/t(14;18)/t(1;14) |
| Peripheral T-cell lymphoma | Heterogeneous; AITL (angioimmunoblastic, TFH-like), ALCL (CD30+) | Poor prognosis generally |

### Kaposi Sarcoma (KS)

HHV-8 (KSHV) infects lymphatic endothelial cells → reprogrammes them toward a hybrid LEC/BEC (blood EC) phenotype → spindle cell tumour secreting VEGF-C/D + VEGFR3 autocrine → highly vascular lesions. Clinical forms: classic (elderly Mediterranean men — indolent leg skin), endemic (sub-Saharan African children — aggressive nodal), AIDS-related (AIDS-defining illness; now rare with ART), iatrogenic (transplant-associated). Treatment: ART (for AIDS-KS — immune reconstitution clears lesions); liposomal doxorubicin (systemic); radiotherapy (local).

### Chylothorax

Thoracic duct injury (trauma, surgery — e.g., oesophagectomy, cardiac surgery; or malignant infiltration — lymphoma, lung cancer) → chyle leaks into pleural space → milky, triglyceride-rich (>110 mg/dL), lymphocyte-predominant pleural effusion. Treatment: nil by mouth → medium-chain triglycerides (MCT) diet → somatostatin analogues (octreotide) → pleurodesis → thoracic duct ligation or embolisation (interventional radiology).

### Overwhelming Post-Splenectomy Infection (OPSI)

Splenectomy removes the primary site of T-independent IgM responses to polysaccharide antigens (marginal zone B cells) and reduces opsonisation capacity for encapsulated organisms → ↑risk of fulminant sepsis by S. pneumoniae (commonest, ~50%), H. influenzae type b, N. meningitidis. OPSI risk: ~1–5% lifetime risk; mortality ~50%. Prevention: vaccination pre-splenectomy (pneumococcal [PCV13 + PPSV23], Hib, MenACWY, MenB); lifelong penicillin prophylaxis (especially children/first 2 years post-splenectomy); antibiotic standby prescription; medical alert card.

### Filariasis (Elephantiasis)

Wuchereria bancrofti (and Brugia malayi/timori) are filarial nematodes transmitted by Culex/Anopheles/Aedes mosquitoes → adults reside in lymphatic vessels → host inflammatory response to microfilariae and adult worm products → lymphangitis + progressive fibrosis → chronic lymphoedema → elephantiasis (grotesque limb/scrotal enlargement). ~120 million infected worldwide; 40 million with clinical lymphoedema. Treatment: diethylcarbamazine (DEC) + albendazole + ivermectin (triple therapy per WHO 2022) — kills microfilariae; adult worms persist; no curative antihelmintic; doxycycline (4–6 weeks) kills endosymbiotic Wolbachia → adult worm sterilisation/death. Lymphoedema management: CDT.

## See Also

- [spleen](../../06-organ/spleen/README.md) — largest lymphoid organ; immune and haematological functions
- [thymus](../../06-organ/thymus/README.md) — T-cell education primary organ
- [immune-system](../../07-system/immune-system/README.md) — lymphatics as the highway for adaptive immunity
- [cardiovascular-system](../../07-system/cardiovascular-system/README.md) — lymphatic return to venous circulation
- [bone-marrow](../../05-tissue/bone-marrow/README.md) — origin of all lymphoid and myeloid cells
- [b-cell](../../04-cellular/b-cell/README.md) — germinal centre reactions in lymph nodes and MALT
- [t-helper-cell](../../04-cellular/t-helper-cell/README.md) — T cell activation in lymph node paracortex

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
