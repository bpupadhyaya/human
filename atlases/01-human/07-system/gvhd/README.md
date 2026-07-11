---
schema: human-scale-entry/v1
id: gvhd
name: Graft-Versus-Host Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "GvHD occurs when donor T cells recognize host alloantigens after allogeneic HSCT; acute (skin, gut, liver, <100 days) vs. chronic (fibrotic, >100 days). IL-10/Treg axis is protective; ruxolitinib (JAK1/2) is the approved steroid-refractory treatment."
aliases: ["GvHD", "graft versus host disease", "GVHD", "acute GvHD", "chronic GvHD", "aGvHD", "cGvHD"]
sources:
  - id: ferrara-2009-gvhd-review
    type: peer-reviewed
    cite: "Ferrara JL, Levine JE, Reddy P, Holler E. Graft-versus-host disease. Lancet. 2009;373(9674):1550-1561."
    doi: "10.1016/S0140-6736(09)60237-3"
    pmid: "19380114"
    url: "https://doi.org/10.1016/S0140-6736(09)60237-3"
  - id: zeiser-2020-ruxolitinib-gvhd-reach
    type: peer-reviewed
    cite: "Zeiser R, von Bubnoff N, Butler J, et al. Ruxolitinib for Glucocorticoid-Refractory Acute Graft-versus-Host Disease. N Engl J Med. 2020;382(19):1800-1810."
    doi: "10.1056/NEJMoa1917635"
    pmid: "32374962"
    url: "https://doi.org/10.1056/NEJMoa1917635"
  - id: przepiorka-2020-ruxolitinib-cgvhd-reach3
    type: peer-reviewed
    cite: "Przepiorka D, Luo L, Subramaniam S, et al. FDA Approval Summary: Ruxolitinib for Treatment of Chronic Graft-versus-Host Disease. Oncologist. 2022;27(2):98-104."
    doi: "10.1093/oncolo/oyab055"
    pmid: "35641197"
    url: "https://doi.org/10.1093/oncolo/oyab055"
cross_links:
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor hematopoietic stem cell engraftment is required for GvHD to occur; the bone marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is a central amplifier of acute GvHD: conditioning regimen tissue damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization + survival signals; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis in clinical trials."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Alloreactive donor CD4+ Th1 cells are the central drivers of acute GvHD: IL-12+IFN-γ drives Th1 polarization; IL-6+TGF-β drives Th17; donor T helper cells recognize host alloantigens via direct (host MHC mismatch) and indirect (host peptides on donor APCs) pathways."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Donor CD8+ CTLs are the primary effectors of target organ damage in acute GvHD: recognize host MHC-I mismatch → perforin/granzyme-mediated killing of skin basal keratinocytes, GI crypt ISCs, and biliary epithelium → grade III/IV GvHD is the leading cause of non-relapse mortality."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Gut microbiome diversity at transplant predicts GvHD severity; Akkermansia muciniphila and Blautia spp. are protective — loss of butyrate-producing bacteria reduces Treg support; antibiotic dysbiosis → loss of SCFAs → increased GvHD risk; FMT is investigational for GvHD rescue."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Skin is the first and most common target of acute graft-versus-host disease: donor CD8 T cells kill basal keratinocytes, producing a maculopapular rash that can progress to bullae, while chronic GvHD turns the skin lichenoid and sclerodermatous."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Ruxolitinib, a JAK1/JAK2 inhibitor, is the approved treatment for steroid-refractory graft-versus-host disease, both acute and chronic: by blocking JAK-STAT signaling downstream of IL-6, IFN-γ, and IL-12 it suppresses Th1/Th17 effectors while sparing regulatory T cells."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Donor regulatory T cells are the protective counterweight in GvHD: through IL-10 and TGF-β they restrain alloreactive effector T cells, and the graft's Treg-to-conventional-T ratio predicts tolerance versus disease — the rationale behind post-transplant cyclophosphamide."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "Transplant-associated TMA is a serious allo-transplant complication overlapping with aHUS: conditioning, calcineurin inhibitors, infection and GVHD injure endothelium and activate complement → schistocytic hemolysis, thrombocytopenia and renal TMA; complement therapy can help."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "GVHD is the chief toxicity of the allogeneic stem-cell transplant used to cure AML and other leukemias: donor T cells attacking host tissue cause GVHD, but the same alloreactivity gives the curative graft-versus-leukemia effect—separating that benefit from GVHD harm is the art."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a major target organ of GVHD: donor T-cell attack on bile-duct epithelium causes a cholestatic hepatitis with rising bilirubin and alkaline phosphatase, part of the classic skin-gut-liver triad of acute GVHD; severe hepatic GVHD carries a poor prognosis."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Chronic GVHD can clinically mimic systemic sclerosis: donor T cells drive fibrosis of skin and organs resembling scleroderma, with TGF-β-mediated collagen deposition and tight, hidebound skin—so chronic GVHD is an alloimmune model of sclerodermatous fibrosis."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Chronic GVHD often produces a Sjögren's-like sicca syndrome: donor immune attack on lacrimal and salivary glands causes severe dry eyes and mouth, mirroring Sjögren's, so the same autoimmune-like glandular destruction arises here from alloreactivity after transplant."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Host dendritic cells ignite graft-versus-host disease: conditioning damage activates recipient antigen-presenting cells that display alloantigens to donor T cells, priming the attack on host tissues—so depleting these dendritic cells is a strategy to prevent GVHD."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Graft-versus-host disease is driven by a cytokine storm: donor T cells activated against host tissue release a flood of TNF, IL-6 and IFN-γ that amplifies organ damage—so cytokine-targeted drugs (ruxolitinib, anti-IL-6) treat steroid-refractory GVHD."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells distinguish graft-versus-host disease from graft-versus-leukemia: donor NK cells can attack residual leukemia while contributing less to GVHD than T cells—NK biology is exploited to separate the cure from the toxicity of transplant."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a major chronic GVHD target: donor immune attack on bronchioles causes bronchiolitis obliterans, an irreversible obstructive lung disease, so new airflow obstruction after transplant signals pulmonary GVHD—a feared, treatment-resistant complication."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is a major battleground in GVHD: donor T cells attack the gut epithelium, causing severe secretory diarrhea and mucosal sloughing, and gut GVHD severity—worsened by microbiome injury—is a leading determinant of transplant survival."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "GVHD prevention hinges on calcineurin inhibition: cyclosporine and tacrolimus block calcineurin to suppress the donor T-cell activation that drives the disease, forming the backbone of prophylaxis after allogeneic stem-cell transplant."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "GVHD is the dark side of transplant immunity: grafted donor immune cells recognize the recipient's tissues as foreign and attack them, the mirror image of rejection—yet the same alloreactivity also fights residual leukemia (graft-versus-leukemia)."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Chronic GVHD frequently strikes the eye: donor immune cells attack the lacrimal glands and ocular surface, causing severe dry eye and keratoconjunctivitis much like Sjögren's—so eye care is a routine part of managing transplant survivors."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "GVHD begins with MHC mismatch: donor T cells recognize the recipient's MHC (HLA) molecules as foreign, especially MHC class II on antigen-presenting cells, so the degree of HLA matching between donor and host predicts the risk and severity of GVHD."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells drive chronic GVHD: alloreactive B cells and autoantibodies fuel the fibrotic, scleroderma-like late disease, which is why B-cell-targeted therapy (the BTK inhibitor ibrutinib) became an approved treatment—shifting GVHD beyond a purely T-cell view."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut GVHD destroys the intestinal epithelium: donor T cells attack the crypts and their stem cells, stripping the gut lining to cause the severe diarrhea that marks acute GVHD—so protecting epithelial stem cells is a treatment goal."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "GVHD cripples the thymus and immune recovery: the donor attack damages thymic tissue needed to educate new T cells, so chronic GVHD leaves patients immunodeficient and prone to infection long after transplant."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Acute GVHD is driven by a TNF-alpha cytokine storm: conditioning and donor T cells trigger TNF-alpha and other cytokines that injure skin, gut and liver, so TNF blockade is among the targeted treatments for steroid-refractory disease."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Chronic GVHD turns on fibroblasts to scar tissue: persistent donor-immune attack and TGF-beta drive fibroblasts to lay down collagen, producing the skin tightening, joint stiffness and lung scarring that define the chronic, scleroderma-like disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Donor killer cells use perforin to attack the host: cytotoxic T and NK cells punch holes in host-cell membranes with perforin to deliver lethal granzymes, a core mechanism of the tissue destruction in acute GVHD."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "GVHD often begins with radiation's photons: total-body irradiation in transplant conditioning damages host tissues, releasing danger signals that activate donor T cells, so the conditioning that enables the graft also primes the graft-versus-host attack."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Gut GVHD can drain the body's potassium: severe inflammation of the bowel lining causes torrential, watery diarrhea—liters a day—that washes out potassium and fluid, a dangerous electrolyte loss needing close replacement."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic GVHD ends in fibrosis: the persistent immune attack lays down scar tissue, hardening the skin like scleroderma and choking the airways with bronchiolitis obliterans, the disabling late face of the disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive GVHD's tissue destruction: recruited by donor T cells, they flood target organs and pour out inflammatory mediators that amplify the damage, making them an effector behind the skin, gut, and liver injury."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "GVHD prophylaxis wastes magnesium: the calcineurin inhibitors cyclosporine and tacrolimus make the kidney spill it, so hypomagnesemia—and the seizures it can provoke—is a common side effect of preventing the disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "IL-2 sits at the center of GVHD control: calcineurin inhibitors block its production to stop donor T cells, while low-dose IL-2 is given to expand regulatory T cells and calm chronic disease."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Chronic GVHD can attack the nerves and muscle: polyneuropathy, myositis and a myasthenia-like syndrome are recognized neuromuscular complications of the prolonged autoimmune assault."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows GVHD killing cell by cell: donor T cells trigger apoptosis of individual keratinocytes in the skin and crypt cells in the gut, the scattered single-cell death — satellite cell necrosis — that is the disease's histologic signature."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "GVHD strikes the upper gut too: beyond the diarrhea of intestinal involvement, gastric GVHD brings nausea, vomiting, early satiety, and anorexia, diagnosed by biopsy of the stomach lining."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Chronic GVHD can reach the kidney: it is an unusual cause of membranous nephropathy and nephrotic syndrome, the misdirected immune attack depositing in the glomerulus long after the transplant."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Chronic GVHD recruits the donor's B cells: alloantibodies and autoantibodies contribute to its sclerosis, which is why the B-cell-depleting antibody rituximab — and antithymocyte globulin in prophylaxis — are part of its management."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Chronic GVHD stiffens the body's framework: a scleroderma-like fasciitis and joint contractures bind down the limbs, limiting movement as the donor immune cells lay down fibrosis in fascia and muscle."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Chronic GVHD scars the genital tract: vaginal and penile mucosal inflammation, dryness, and stenosis are underrecognized but common, the same lichenoid and sclerotic attack that hits skin and mouth."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Corticosteroids are the first line and a double edge: high-dose glucocorticoids suppress the donor T cells driving GVHD, but their infections, bone loss, and metabolic harm make steroid-sparing agents a constant goal."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatic GVHD strikes the liver cells and ducts: donor T cells attack the bile-duct epithelium and injure hepatocytes, producing a cholestatic hepatitis with rising bilirubin that is one of acute GVHD's three classic targets."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The transplanted immunity can turn on the thyroid: chronic GVHD and post-transplant immune dysregulation raise the rate of autoimmune thyroid disease, one of the late endocrine complications survivors are monitored for."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 cells drive part of the attack: IL-17A from donor T cells fuels the inflammation of skin, gut, and lung GVHD, making the IL-17 axis one of the pathways targeted to tame the disease."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small bowel is a primary GVHD target: donor T cells trigger crypt-cell apoptosis and a secretory diarrhea whose volume grades acute gut GVHD, the leak of the damaged mucosa amplifying the systemic inflammation."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "GVHD is the price of the cure for MDS: the allogeneic transplant given for myelodysplastic syndromes carries a graft-versus-tumor benefit, but the same donor cells that clear the marrow disease can turn on the host."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "A donor-T-cell cytokine drives the attack: IFN-γ pours from activated donor T cells to license macrophages and damage host epithelium, a central effector of acute GVHD's gut, skin and liver injury."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "The inflammatory signal travels through JAK-STAT: IFN and other cytokines act via STAT1 to amplify the alloimmune response, the pathway the JAK inhibitor ruxolitinib blocks to treat steroid-refractory GVHD."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "It rides in with the leukemia cure: allogeneic transplant for acute lymphoblastic leukemia delivers a graft-versus-leukemia effect, but the same donor immunity that hunts residual blasts can turn against the host as GVHD."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Tissue damage and alloantigen converge on NF-κB: conditioning injury and donor T-cell activation switch on NF-κB in host antigen-presenting cells and target tissues, amplifying the cytokine storm that drives acute GVHD."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 steers the pathogenic T cells: downstream of IL-6 and IL-21, STAT3 drives the Th17 and effector responses central to GVHD, part of the JAK-STAT signaling that ruxolitinib targets in steroid-refractory disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "It strips defenses and breaches the gut: the immunosuppression treating GVHD plus its destruction of the intestinal barrier let gut bacteria translocate, making infection and sepsis a leading cause of death."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Deep immunosuppression opens the lung to mold: the prolonged steroids and other immunosuppressants treating GVHD profoundly impair defenses, making invasive pulmonary aspergillosis a feared and frequent infection."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "T-cell suppression invites Pneumocystis: the immunosuppression controlling GVHD depletes the T-cell defenses against Pneumocystis, so PJP prophylaxis is standard for these transplant patients."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its drugs are hard on the kidney: the calcineurin inhibitors (ciclosporin, tacrolimus) central to GVHD prophylaxis and treatment are nephrotoxic, and chronic exposure can leave lasting chronic kidney disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Chronic GVHD scleroses and ulcerates the skin: its sclerodermatous skin changes, oral and genital erosions, on top of steroid immunosuppression, leave wounds that are slow and difficult to heal."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Prolonged steroids erode the skeleton: the months to years of high-dose corticosteroids used to control chronic GVHD cause bone loss and avascular necrosis, a major long-term complication."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A grueling chronic complication weighs on mood: the prolonged disability, disfigurement and treatment burden of chronic GVHD after a hoped-for cure contribute to substantial depression in survivors."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin is its commonest target: GVHD produces an acute maculopapular rash and, in chronic disease, lichenoid and sclerodermatous skin with fibrosis, dyspigmentation and nail and hair loss."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It attacks the gut and liver: GVHD causes profuse secretory diarrhoea, nausea and mucositis along the GI tract, and a cholestatic hepatitis when it strikes the liver."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Chronic disease scars the airways: lung GVHD presents as bronchiolitis obliterans, an obstructive, progressive and often irreversible narrowing of the small airways."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It and its drugs can harm the nerves: chronic GVHD causes immune-mediated peripheral neuropathy and myositis, while the calcineurin inhibitors used to treat it cause tremor, seizures and PRES."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Transplant and chronic GVHD derail hormones: thyroid dysfunction, gonadal failure and steroid-induced adrenal insufficiency are common endocrine complications after allogeneic transplant."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can attack the kidney: membranous nephropathy is a recognised renal manifestation of chronic GVHD, compounded by the nephrotoxicity of calcineurin-inhibitor immunosuppression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It is born of donor lymphocytes and cripples lymphoid recovery: donor T cells attack the host while thymic GVHD delays T-cell reconstitution, leaving prolonged immunodeficiency after transplant."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its treatment strains the circulation: long courses of corticosteroids and calcineurin inhibitors for GVHD drive hypertension and cardiovascular risk, and rare cardiac GVHD causes pericarditis."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Deep immunosuppression reawakens latent virus: the heavy immune suppression of GVHD lets varicella-zoster reactivate as shingles, sometimes disseminated."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "The first-line treatment: high-dose corticosteroids are the mainstay for acute and chronic graft-versus-host disease, though steroid-refractory disease carries a poor prognosis and drives the search for alternatives."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Cytomegalovirus reawakens under treatment: the heavy immunosuppression for GVHD allows CMV reactivation, causing pneumonitis, colitis and marrow suppression that are major causes of post-transplant death."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "The microbiome shapes its severity: loss of gut bacterial diversity worsens GVHD, while fibre-derived butyrate that nourishes the intestinal epithelium is protective, making diet and the microbiome therapeutic targets."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "JAK inhibition for refractory disease: ruxolitinib, a JAK1/2 inhibitor, is approved for steroid-refractory acute and chronic GVHD, with belumosudil (ROCK2) for chronic disease — targeted alternatives to broad immunosuppression."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo prevents and conditions: methotrexate is a classic GVHD prophylactic and post-transplant cyclophosphamide enables haploidentical grafts by deleting alloreactive T cells, while the conditioning chemo sets the stage for the donor immune attack."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Its treatment wrecks the skeleton: prolonged corticosteroids and calcineurin inhibitors for GVHD cause osteoporosis and avascular necrosis of bone, a major cause of disability in long-term transplant survivors."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "The cure that can turn hostile: allogeneic stem-cell transplant is curative for severe aplastic anaemia, and GVHD is its principal transplant-related danger—the same donor graft that rebuilds the marrow can attack the host."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Hepatic GVHD strikes the bile ducts: donor T cells attack the small bile ducts within the hepatic lobule, causing cholestatic jaundice and a rising bilirubin that grades liver involvement."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Chronic GVHD's autoimmune face: alloreactive germinal-centre reactions and B-cell help generate the autoantibodies and the sclerotic, Sjögren- and scleroderma-like features of chronic graft-versus-host disease."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung GVHD: chronic graft-versus-host disease attacks the small airways as bronchiolitis obliterans, scarring around the alveoli into an irreversible obstructive lung disease, a feared pulmonary complication."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Post-transplant lymphoma: the heavy immunosuppression needed for GVHD lets EBV-driven B cells proliferate unchecked as post-transplant lymphoproliferative disease, which can become a diffuse large B-cell lymphoma."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Transplant for a marrow disease: allogeneic stem-cell transplant is the only cure for myelofibrosis, but graft-versus-host disease is a major source of its transplant-related morbidity and mortality."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Defenceless after transplant: GVHD and its immunosuppression leave allograft recipients profoundly vulnerable to severe, prolonged COVID-19 with blunted vaccine responses."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "Transplant-associated TMA: calcineurin inhibitors and the endothelial injury of the transplant setting cause a thrombotic microangiopathy overlapping with TTP and aHUS, complicating GVHD management."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Autoimmune mimicry: chronic GVHD can produce myositis and fasciitis resembling dermatomyositis, one of several connective-tissue-disease pictures the alloimmune attack reproduces alongside its sclerodermatous and sicca forms."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrotic driver: TGF-β orchestrates the tissue fibrosis of chronic GVHD, scarring skin, lung and gut in the sclerodermatous and bronchiolitis-obliterans forms of the disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Conditioning damage: tissue injury from the conditioning regimen releases IL-1β, an innate alarm signal that primes donor T cells and amplifies the cytokine storm of acute GVHD."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Innate priming: damage-associated signals after transplant activate the NLRP3 inflammasome in host antigen-presenting cells, maturing IL-1β to intensify the alloreactive attack of GVHD."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Prophylaxis target: mTOR drives the metabolism and proliferation of alloreactive donor T cells, so mTOR inhibitors like sirolimus are used in GVHD prophylaxis while sparing regulatory T cells."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microbial trigger: conditioning damages the gut barrier, letting bacterial LPS engage TLR4 on host antigen-presenting cells, the innate signal that ignites the cytokine storm of acute gut GVHD."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Gut-GVHD biomarker: S100A8/A9 released by damaged intestinal epithelium and neutrophils amplifies GVHD inflammation, and faecal calprotectin tracks the activity of gastrointestinal GVHD."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "Chronic-GVHD therapy: BTK signalling in donor B and T cells drives the autoreactive, fibrotic chronic GVHD, the basis for ibrutinib being approved for steroid-refractory chronic graft-versus-host disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Target-organ recruitment: CCL2 draws donor monocytes and macrophages into the skin, gut and liver of acute GVHD, amplifying the inflammatory tissue destruction caused by the alloreactive T-cell attack."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic hallmark: donor cytotoxic T cells drive caspase-3-mediated apoptosis of host epithelial cells — the crypt-cell and keratinocyte apoptosis that is the defining histological lesion of acute GVHD."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Refractory biomarker: the IL-33/ST2 alarmin axis is activated by conditioning-induced tissue damage, and a high soluble ST2 level is a validated biomarker predicting steroid-refractory, lethal acute graft-versus-host disease."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell chronic GVHD: excess BAFF after transplant rescues alloreactive and autoreactive B cells, driving the antibody-mediated, sclerodermatous chronic graft-versus-host disease that B-cell-directed therapies like rituximab and ibrutinib target."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Fibrotic remodelling: periostin and other matricellular proteins drive the tissue fibrosis of chronic GVHD, the sclerodermatous skin, fasciitis and bronchiolitis-obliterans lung disease that make advanced chronic GVHD so disabling."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Alloreactive differentiation: NOTCH signalling in donor T cells drives their differentiation into the pathogenic alloreactive effectors of graft-versus-host disease, a targetable axis distinct from calcineurin and JAK inhibition."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "T-cell proliferation: the PI3K-AKT-mTOR pathway (mTOR already mapped, the target of sirolimus) drives the proliferation and metabolic activation of alloreactive donor T cells in GVHD."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 from activated host antigen-presenting cells polarises donor T cells toward the Th1/IFN-γ response (already mapped) that mediates acute graft-versus-host disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate DNA sensing: cGAS-STING detection of cytosolic DNA released by conditioning-regimen tissue damage drives type-I-interferon production that amplifies the inflammatory priming of acute graft-versus-host disease."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Alloreactive checkpoint: PD-1 engagement restrains alloreactive donor T cells, and checkpoint-inhibitor blockade of this brake can precipitate GVHD-like immunopathology — underscoring its role in tolerance after transplant."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibrotic chronicity: PDGF drives the fibroblast activation and tissue fibrosis of chronic sclerodermatous graft-versus-host disease, alongside the periostin and TGF-β pathways already mapped."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "TCR-driven ERK-MAPK signalling in donor alloreactive T cells contributes to their activation and expansion in the effector phase of graft-versus-host disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives the tissue fibrosis of chronic graft-versus-host disease, especially of skin and lung."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the fibro-inflammatory tissue injury characteristic of chronic graft-versus-host disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) drives the proliferation and effector differentiation of the alloreactive donor T cells that mediate graft-versus-host disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated epigenetic programming of alloreactive donor T cells shapes their pathogenicity in graft-versus-host disease, an emerging therapeutic target."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 chemokine signalling directs the trafficking of alloreactive donor T cells to the target organs of graft-versus-host disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the alloreactive T-cell survival and tissue oxidative-stress responses that shape graft-versus-host disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-driven metabolic reprogramming of alloreactive T cells and the hypoxic inflamed target tissues contributes to graft-versus-host disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cell-cycle activity fuels the clonal expansion of alloreactive donor T cells in graft-versus-host disease, an emerging therapeutic target."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the T-cell activation and inflammatory signaling that drive the alloreactivity of graft-versus-host disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the donor-T-cell activation central to graft-versus-host disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation shapes the effector differentiation of the donor T cells that mediate graft-versus-host disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the alloreactive T-cell metabolism of graft-versus-host disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the alloreactive T-cell and target-tissue responses of graft-versus-host disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven donor-T-cell trafficking into target organs drives the tissue injury of graft-versus-host disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 activation participates in the tissue injury of graft-versus-host disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (A2A-receptor) immunoregulatory signaling modulates the alloreactive T-cell responses of graft-versus-host disease."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20-expressing B cells contribute to the alloantibody and immune dysregulation of chronic graft-versus-host disease, a rationale for B-cell-depleting therapy."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the alloreactive immune responses of graft-versus-host disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the T-cell activation and target-organ inflammation of graft-versus-host disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the tissue-damage and immune activation of graft-versus-host disease."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Costimulation blockade: abatacept, a CTLA-4-Ig fusion protein, blocks the CD28 costimulation that donor T cells need to activate against host tissue, and it is approved to help prevent graft-versus-host disease after mismatched transplant."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal barrier: conditioning and gut graft-versus-host disease disrupt the secretory IgA that protects the intestinal mucosa, weakening the barrier that normally restrains the microbiota and amplifying the gut inflammation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis balance: anti-apoptotic BCL-2 family proteins set the survival threshold of alloreactive donor T cells and of the target-organ epithelium they attack, influencing both the graft-versus-host injury and the beneficial graft-versus-leukaemia effect."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Sclerodermatous fibrosis: chronic graft-versus-host disease drives fibroblast collagen deposition (TGF-beta and PDGF already mapped), producing the sclerodermatous skin thickening, joint contractures and fibrosis that define the chronic form."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 fibrosis: IL-13 and the type-2 cytokine response promote the macrophage and fibroblast activation that drives the fibrosis of chronic graft-versus-host disease, complementing the TGF-beta (already mapped) pathway."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Post-transplant cytopenias: marrow graft-versus-host effects, drug toxicity and infection lower haemoglobin after transplant, and the resulting anaemia adds to the morbidity of graft-versus-host disease and its treatment."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the inflamed gut and skin (IL-6, TNF and IL-1 already mapped) contribute to the tissue injury of acute graft-versus-host disease, part of the eicosanoid dimension of the alloreactive attack."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 fibrotic axis: IL-4, with IL-13 (already mapped), polarises macrophages and fibroblasts (already mapped) toward the type-2 fibrotic response that drives the sclerotic fibrosis of chronic graft-versus-host disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative tissue injury: the conditioning regimen and the alloreactive attack generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress amplifies the epithelial damage of graft-versus-host disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusional iron overload: the repeated transfusions before and after the transplant load the patient with iron (haemoglobin already mapped), and the resulting iron overload adds oxidative burden to the tissues attacked in graft-versus-host disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron-restricted anaemia: the inflammation (IL-6 already mapped) of graft-versus-host disease raises hepcidin, sequestering iron and contributing to the anaemia (haemoglobin already mapped) that complicates the post-transplant course."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial injury: nitric oxide is dysregulated in the endothelial damage of graft-versus-host disease, part of the vascular injury (with the epithelial attack) that underlies the transplant-associated microangiopathy and organ damage."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Vascular injury: VEGF and the dysregulated angiogenesis (nitric oxide already mapped) reflect the endothelial damage of the transplant-associated microangiopathy and the vascular component of graft-versus-host disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "TA-TMA complement: the complement C5 (C3 already mapped) drives the transplant-associated thrombotic microangiopathy that complicates graft-versus-host disease, the target of eculizumab."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic GVHD: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils whose presence is a marker of graft-versus-host disease, notably the chronic and gastrointestinal forms."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic GVHD: the liver GVHD (the cholestatic hepatitis, the bile-duct destruction) is a major acute-GVHD target organ (with the skin and gut already mapped)."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Donor CD4 cells: the donor CD4 T-helper cells (Th1 and Th17 — IFN-γ and IL-17 already mapped) orchestrate the alloreactive attack and, in the chronic form, the fibrosis of graft-versus-host disease."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Scleroderma-like chronic GVHD: the chronic GVHD (the fibrosis — collagen and TGF-β already mapped) resembles the systemic sclerosis (scleroderma), sharing the fibrotic mechanisms."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu of graft-versus-host disease, altered by the steroid therapy and the systemic inflammation (IL-6 already mapped)."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of graft-versus-host disease and its treatment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of graft-versus-host disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the donor-T-cell alloreactivity of graft-versus-host disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the chronic graft-versus-host disease."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "cGVHD humoral arm: the plasma cells (BAFF and CD20 already mapped) secrete the alloantibodies of the chronic, antibody-mediated graft-versus-host disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated tissue injury of the graft-versus-host disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Sclerodermatous cGVHD: the mast cells accumulate in the sclerodermatous skin and, via their profibrotic mediators, promote the fibrosis (TGF-β and PDGF already mapped) of the chronic graft-versus-host disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Acute tissue damage: the neutrophils, recruited by the microbiome-driven and complement (C5aR1 already mapped) signals, amplify the target-tissue injury of the acute graft-versus-host disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-amplified tissue injury of graft-versus-host disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact systems activated in the endothelial and target-tissue injury of graft-versus-host disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Post-transplant iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the transfusional iron overload and the anaemia complicating graft-versus-host disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-alloimmune axis: TSLP, from damaged intestinal (already mapped) and skin (already mapped) epithelium of the conditioning regimen, primes host dendritic cells (already mapped) toward alloreactive Th2 and Th17 (already mapped) responses in graft-versus-host disease."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-vascular axis: bradykinin, from the contact-pathway activation in the conditioned endothelium (already mapped), amplifies the vascular permeability and the tissue oedema contributing to the endothelial injury of graft-versus-host disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Engraftment anaemia: erythropoietin drives red-cell regeneration to correct the anaemia of the conditioning regimen, the myelosuppression (bone-marrow already mapped), and the haemolysis (already mapped) complicating graft-versus-host disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell target-organ effector: mast cells (already mapped) in the target organs of GVHD — gut, skin, liver — release histamine that amplifies the vascular permeability and the tissue oedema of acute graft-versus-host disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian transplant biology: circadian disruption is common in transplant patients; melatonin has immunomodulatory effects on T-cell (already mapped) differentiation and alloreactivity, a property studied in the alloimmune context of GVHD."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stress-immune axis: prolactin, elevated by transplant stress and the immunosuppressive (calcineurin, cortisol already mapped) regimen, modulates T-cell (already mapped) and natural-killer-cell (already mapped) activity in the allograft context."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "GVHD testosterone: testosterone, via androgen receptors on T-helper cells (already mapped) and regulatory T cells (already mapped), attenuates alloreactive T-cell expansion; androgen deficiency amplifies the IL-6 (already mapped)-driven donor T-cell severity of GVHD."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "GVHD serotonin: serotonin, via 5-HT receptors on T-helper cells (already mapped) and natural-killer cells (already mapped), modulates the cytokine-storm (already mapped) immune axis; serotonin dysregulation amplifies the gut-microbiome (already mapped) dysbiosis of mucosal GVHD."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "GVHD oxytocin: oxytocin, via OXTR on regulatory T cells (already mapped) and dendritic cells (already mapped), promotes immunological tolerance by enhancing T-regulatory (Treg) expansion; oxytocin attenuates the IL-6 (already mapped)-driven donor alloreactivity of GVHD."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "GVHD vasopressin: vasopressin, via V1aR on regulatory T cells (already mapped) and dendritic cells (already mapped), modulates alloreactive immune activation; vasopressin dysregulation amplifies the IL-6 (already mapped) and TNF-α (already mapped) cytokine-storm cascade of GVHD."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "GVHD selenium: selenium, as GPx in macrophages (already mapped) and intestinal-epithelium (already mapped), scavenges the cytokine-storm (already mapped)-driven ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) tissue-damage cascade of GVHD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GVHD iodine: iodine-dependent thyroid hormones modulate T-helper cell (already mapped) and regulatory T-cell (already mapped) differentiation; iodine deficiency amplifies the IL-6 (already mapped) and TNF-α (already mapped) alloreactive cytokine cascade of GVHD."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "GVHD zinc: zinc cofactors macrophage (already mapped) anti-inflammatory resolution and regulatory T-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive tissue damage in GVHD."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "GVHD sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) amplifies alloreactive T-cell tissue damage in GVHD."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "GVHD copper: copper cofactors macrophage (already mapped) and regulatory T-cell (already mapped) function; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive tissue damage in GVHD."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "GVHD calcium: calcium signals macrophage (already mapped) and regulatory T-cell (already mapped) activation; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive cascade of GVHD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "GVHD chloride: chloride channels regulate macrophage (already mapped) and regulatory T-cell (already mapped) volume during alloreactive responses; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of GVHD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "GVHD nitrogen: nitrogen, as protein backbone in cytokines (already mapped) and effector T-cells (already mapped), sustains alloreactive signalling; nitrogen-derived RNS amplifies NF-κB (already mapped) and TNF-α (already mapped) tissue inflammation of GVHD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "GVHD phosphorus: phosphorus as ATP in macrophages (already mapped) and effector T-cells (already mapped) fuels alloreactive kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of GVHD."
---

# Graft-Versus-Host Disease

## Overview

**Graft-versus-host disease (GvHD)** is the leading cause of non-relapse morbidity and mortality after **allogeneic hematopoietic stem cell transplantation (allo-HSCT)**, occurring when immunologically competent donor T cells recognize and attack the tissues of an immunologically distinct host [^ferrara-2009-gvhd-review].

GvHD occurs in two biologically distinct forms:
- **Acute GvHD (aGvHD):** Classically defined as occurring within **100 days** post-transplant (though now recognized by clinical syndrome rather than timing); targets skin, gastrointestinal tract, and liver; characterized by donor T cell cytotoxicity and pro-inflammatory cytokine storm
- **Chronic GvHD (cGvHD):** Occurring after day 100 (or earlier with overlap syndrome); resembles fibrotic autoimmune disorders (scleroderma, Sjögren's syndrome, primary biliary cirrhosis analogues); targets skin/fascia, mouth, eyes, lungs, joints, and liver; involves dysregulated B cell and Th2/Th17 responses

**Incidence and impact:**
- Allo-HSCT performed in ~30,000 patients/year in the US; GvHD incidence: ~30-50% acute (grade II-IV), ~40-70% chronic
- Grade III-IV acute GvHD: ~15-20%; associated with 80-90% 2-year mortality without effective treatment
- 5-year non-relapse mortality from chronic GvHD: ~20-30% in high-risk patients
- Annual US cost of GvHD management: >$500 million

**The GvL trade-off:** Donor T cells cause GvHD, but also mediate the **graft-versus-leukemia (GvL)** effect — direct allograft T cell cytotoxicity against residual leukemic/lymphoma cells. Strategies to prevent GvHD (T cell depletion, immunosuppression) inevitably reduce GvL, increasing relapse risk. This fundamental biological tension defines the central challenge of allogeneic transplantation.

## Structure

### Three-phase pathogenesis model (Ferrara model)

**Phase 1 — Tissue damage and APC activation (afferent phase):**
- Pre-transplant conditioning regimen (total body irradiation, high-dose chemotherapy) → GI mucosal damage → bacterial product translocation (LPS, flagellin, peptidoglycan) + host DAMP release (HMGB1, heat shock proteins, ATP)
- Host antigen-presenting cells (APCs: macrophages, DCs) activated via TLR4/TLR5/TLR2 → ↑IL-6, IL-1β, TNF-α, IL-12; ↑MHC class I/II expression; ↑CD80/86 costimulation
- **Host APC priming of donor T cells** is the critical initial event

**Phase 2 — T cell activation and expansion (central phase):**
- Donor naïve CD4+ and CD8+ T cells recognize **host alloantigens** (direct pathway: foreign donor MHC complexes; indirect pathway: host-derived peptides on donor APCs)
- IL-12 + IFN-γ → **Th1 differentiation**; IL-6 + TGF-β → **Th17 differentiation**
- CD8+ CTL → recognize host MHC class I mismatch → kill host epithelium via perforin/granzyme and Fas-FasL
- Cytokine amplification: **TNF-α** (from donor Th1 + host macrophages) → NF-κB → IL-6, IL-8, IL-1β; **IFN-γ** → CXCL9/CXCL10 → further CTL recruitment
- Protective countercurrent: donor-derived **Foxp3+ Tregs** secrete **IL-10** and **TGF-β** → suppress alloreactive T cells; Treg:Tconv ratio in graft is the key determinant of GvHD vs. tolerance

**Phase 3 — Target organ damage (efferent phase):**
- **Skin:** CD8+ T cell-mediated basal keratinocyte apoptosis → grade I (maculopapular rash) → grade IV (bullous dermatitis); satellitosis (single-cell lymphocytic apoptosis) on biopsy
- **GI tract:** Crypt apoptosis → loss of intestinal stem cells → diarrhea (secretary + bloody) → grade III/IV GvHD carries >80% mortality without salvage; gut is the primary determinant of aGvHD lethality
- **Liver:** Donor T cell injury to biliary epithelium → cholestatic hepatitis (↑bilirubin, alkaline phosphatase) → grade IV → hepatic failure

### Grading systems

**Acute GvHD — Overall grade (Glucksberg/Harris):**
- Grade I: Skin only (stage 1-2); no functional impairment
- Grade II: Skin stage 3, or liver bilirubin 2-3 mg/dL, or GI diarrhea 500-1000 mL/day; mild functional impairment
- Grade III: Skin/liver/GI involvement; marked functional impairment
- Grade IV: Generalized erythroderma ± bullae; bilirubin >15 mg/dL; diarrhea >1500 mL/day; severe functional impairment

**Chronic GvHD — NIH scoring:**
- NIH Consensus Criteria (2005, revised 2014): Organ-specific scoring (skin, mouth, eyes, GI, liver, lungs, joints/fascia, genitalia) → overall: mild/moderate/severe
- Key differentiating features from aGvHD: lichen planus-like changes, scleroderma, bronchiolitis obliterans (BO), dry eyes (keratoconjunctivitis sicca)

### Risk factors

- **HLA mismatch:** Fully matched 10/10 (HLA-A, B, C, DRB1, DQB1) vs. 9/10 or lower → progressively higher GvHD risk
- **Unrelated donor** vs. matched sibling: ×2-3 higher GvHD risk
- **Graft source:** Peripheral blood stem cells (PBSC) > bone marrow > cord blood for chronic GvHD risk
- **Conditioning intensity:** Myeloablative conditioning > reduced-intensity conditioning → more tissue damage → more phase 1 danger signals
- **CMV serostatus mismatch** and **older recipient age** → higher GvHD risk
- **Microbiome diversity:** High gut microbiome diversity at transplant → lower GvHD risk (clinical trial data; Akkermansia muciniphila, Blautia spp. protective)

## Function

### Prevention strategies

**Calcineurin inhibitor–based prophylaxis (standard of care):**
- **Tacrolimus** (FK506) + **methotrexate** (MTX): most widely used backbone; tacrolimus inhibits calcineurin → ↓NFAT → ↓IL-2 transcription → T cell activation blockade; MTX kills rapidly proliferating T cells
- **Cyclosporine + MTX:** Alternative; similar efficacy to tacrolimus + MTX in matched sibling transplants
- Post-transplant cyclophosphamide (**PT-Cy; BuCyPT**): High-dose Cy on days +3/+4 → kills proliferating alloreactive T cells while sparing slowly dividing Tregs → profoundly reduces GvHD; now standard for haploidentical (half-matched) transplants and increasingly used in MUD transplants

**PTCy mechanism:** Donor alloreactive T cells proliferate rapidly (day 3-4 after infusion) → high cyclophosphamide sensitivity via aldehyde dehydrogenase (ALDH) low expression; Tregs express high ALDH → PTCy preferentially kills alloreactive Teffs, spares Tregs → immune reconstitution weighted toward tolerance

### Treatment — Acute GvHD

**First-line: Corticosteroids:**
- Methylprednisolone 1-2 mg/kg/day; ~50% complete response rate; steroid-refractory (SR) in ~50% of patients (response day 5-7 defines SR)
- Mechanism: glucocorticoid receptor → ↓NF-κB + AP-1 → broad anti-inflammatory; apoptosis of activated T cells

**Second-line steroid-refractory aGvHD:**

**Ruxolitinib (Jakafi; JAK1/2 inhibitor; Incyte)** [^zeiser-2020-ruxolitinib-gvhd-reach]:
- **REACH2 trial** (Phase 3): Ruxolitinib 10 mg BID vs. investigator's choice (BAT; 7 options including MMF, infliximab, etanercept, tacrolimus) in SR aGvHD grade II-IV
- **Day 28 ORR: 62% vs. 39%** (OR 2.64, p<0.001); CR 34% vs. 19%; durable ORR at day 56: 40% vs. 22%
- Mechanism: JAK1/JAK2 inhibition → ↓STAT3/STAT5 → ↓IL-2, IL-6, IL-12, IFN-γ signaling → suppression of Th1/Th17 effector programs; also increases Treg proportion
- **FDA approval: May 2019** for SR acute GvHD ≥12 years old (first approved second-line agent)
- Adverse effects: anemia (Hgb ↓), thrombocytopenia, CMV reactivation (monitor PCR); secondary viral infections

**Ruxolitinib for chronic GvHD (REACH3):**
- SR chronic GvHD: Ruxolitinib 10 mg BID vs. BAT; ORR at week 24: **49.7% vs. 25.6%** (OR 2.99); failure-free survival superior
- **FDA approval: September 2021** for SR/RI chronic GvHD ≥12 years old [^przepiorka-2020-ruxolitinib-cgvhd-reach3]

**Ibrutinib (Imbruvica; BTK inhibitor; AbbVie/J&J) for chronic GvHD:**
- Ibrutinib inhibits BTK → ↓B cell activation → ↓donor B cell-mediated fibrogenesis + ↓Th2 cytokines (IL-4, IL-13) via ITK inhibition
- **FDA accelerated approval August 2017** for SR/RI cGvHD after ≥1 prior therapy; iNNOVATE trial (open-label): 67% ORR; 21% CR; 46% sustained response ≥20 weeks
- GI cGvHD and IBRUTINIB: less effective for GI manifestations vs. skin/mouth; replaced in many centers by ruxolitinib post-REACH3

**Belumosudil (Rezurock; ROCK2 inhibitor; Kadmon/Sanofi) for chronic GvHD:**
- ROCK2 (Rho-associated kinase 2): Belumosudil → ↓STAT3 phosphorylation (independently of JAK) → ↓Th17 polarization + ↑Treg differentiation; also inhibits fibroblast activation → anti-fibrotic in skin/lung cGvHD
- **KD025-213 Phase 2:** 200 mg QD: 74% ORR; 200 mg BID: 77% ORR; lung ORR 29% (rare responders in this manifestation)
- **FDA approval: August 2021** for SR/RI cGvHD ≥12 years after ≥2 prior therapies
- Distinct mechanism from ruxolitinib/ibrutinib; can be combined or used sequentially

**Axatilimab (anti-CSF-1R; Syndax) for cGvHD:**
- Targets colony-stimulating factor-1 receptor (CSF-1R) on macrophages → depletes fibrosis-driving macrophages (particularly in skin/fascia/GI fibrosis)
- **AGAVE-201 Phase 2:** 200 µg/kg Q2W: 74% ORR (best cohort); 100 µg/kg Q2W: 67% ORR; anti-fibrotic signal in skin and GI
- **FDA approval: August 2024** for SR/RI cGvHD after ≥2 prior therapies; newest approved mechanism

### IL-10 and Treg biology in GvHD

The protective Treg/IL-10 axis is the key biological counterbalance to alloreactive T cell pathogenicity:
- **Graft Treg content:** Peripheral blood grafts have ~5-10× fewer Tregs than bone marrow; Treg:Tconv ratio <1:20 in PBSC grafts predicts GvHD risk
- **Ex vivo Treg expansion:** ORCA-T (Orca Bio): selective Treg expansion from donor → 1-year GvHD-free survival 79% vs. 29% (matched external control); Phase 3 (PRECISION-T) ongoing
- **IL-10 serum kinetics:** Post-HSCT IL-10 peaks day +7 in non-GvHD patients; patients developing GvHD show paradoxically low IL-10 at day +7 (despite apparent inflammation) — reflecting insufficient Treg engagement
- **IL-10R mutations and VEO-IBD:** Biallelic loss-of-function mutations in *IL10RA* or *IL10RB* → infantile pancolitis; allo-HSCT from IL-10R-functional donor → curative, reinforcing the direct mechanistic role of the IL-10 axis in gut immune tolerance

## Pathology

**Refractory GvHD:**
- Grade III-IV SR aGvHD: 2-year OS <20%; multiple sequential salvage therapies further impair immune reconstitution; opportunistic infections (CMV, fungal, PJP) are major causes of death
- **Steroid refractory definition:** Progression after 3 days of methylprednisolone ≥2 mg/kg/day, or no improvement after 7 days, or inability to taper steroids

**Chronic GvHD — Bronchiolitis obliterans syndrome (BOS):**
- Lung manifestation of cGvHD; irreversible obstructive lung disease (FEV1/FVC <0.7); NIH lung score 2-3
- Pathology: concentric fibrotic obliteration of bronchioles; analogous to BOS in solid organ lung transplant
- Treatment: inhaled fluticasone + azithromycin + montelukast (FAM regimen); systemic immunosuppression; lung transplant in extreme cases
- Poor prognosis: FEV1 decline >10% in 2 years before diagnosis → 50% mortality within 2 years

**Infection and immune reconstitution:**
- GvHD and its treatment (immunosuppression) → profound secondary immunodeficiency
- CMV reactivation: monitored weekly by PCR; treated with valganciclovir (preemptive strategy)
- Invasive fungal infections (Aspergillus, Candida): prophylaxis with voriconazole or posaconazole for high-risk patients
- PJP prophylaxis: trimethoprim-sulfamethoxazole until CD4+ >200 cells/µL
- Hypogammaglobulinemia: monthly IVIG for IgG <400 mg/dL until immune reconstitution

**GvHD vs. relapse — the central tension:**
- Aggressive GvHD prophylaxis → reduced GvL → higher leukemia relapse rates (paradox: patients who develop mild cGvHD have lower relapse risk — GvL signal)
- **Donor lymphocyte infusion (DLI):** Infusion of additional donor T cells post-transplant to enhance GvL in patients with molecular relapse; deliberately induces mild GvHD to eliminate residual disease; used primarily in CML (90% CMR rates), AML, MDS

## Connections

- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — GvHD originates from allogeneic bone marrow or peripheral blood stem cell transplantation; donor hematopoietic stem cell engraftment is required for GvHD to occur; the bone marrow niche is reshaped by donor-derived immune reconstitution, influencing GvHD vs. GvL balance.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is a central amplifier of acute GvHD: conditioning regimen tissue damage releases DAMPs → IL-6 from host APCs → JAK1/STAT3 in donor T cells → Th17 polarization + survival signals; tocilizumab (anti-IL-6R) is studied as GvHD prophylaxis in clinical trials.
- `connects-to` → **[T-Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Alloreactive donor CD4+ Th1 cells are the central drivers of acute GvHD: IL-12+IFN-γ drives Th1 polarization; IL-6+TGF-β drives Th17; recognize host alloantigens via direct (host MHC mismatch) and indirect (host peptides on donor APCs) pathways.
- `connects-to` → **[T-Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Donor CD8+ CTLs are the primary effectors of target organ damage: recognize host MHC-I mismatch → perforin/granzyme-mediated killing of skin keratinocytes, GI crypt ISCs, and biliary epithelium → grade III/IV GvHD is the leading cause of non-relapse mortality.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Gut microbiome diversity at transplant predicts GvHD severity; Akkermansia muciniphila and Blautia spp. are protective — loss of butyrate-producing bacteria reduces Treg support; antibiotic dysbiosis → loss of SCFAs → increased GvHD risk; FMT is investigational for GvHD rescue.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Skin is the first and most common target of acute graft-versus-host disease: donor CD8 T cells kill basal keratinocytes, producing a maculopapular rash that can progress to bullae, while chronic GvHD turns the skin lichenoid and sclerodermatous.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Ruxolitinib, a JAK1/JAK2 inhibitor, is the approved treatment for steroid-refractory graft-versus-host disease, both acute and chronic: by blocking JAK-STAT signaling downstream of IL-6, IFN-γ, and IL-12 it suppresses Th1/Th17 effectors while sparing regulatory T cells.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Donor regulatory T cells are the protective counterweight in GvHD: through IL-10 and TGF-β they restrain alloreactive effector T cells, and the graft's Treg-to-conventional-T ratio predicts tolerance versus disease — the rationale behind post-transplant cyclophosphamide.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — Transplant-associated TMA is a serious allo-transplant complication overlapping with aHUS: conditioning, calcineurin inhibitors, infection and GVHD injure endothelium and activate complement → schistocytic hemolysis, thrombocytopenia and renal TMA; complement therapy can help.
- `connects-to` → **[AML](../aml/README.md)** — GVHD is the chief toxicity of the allogeneic stem-cell transplant used to cure AML and other leukemias: donor T cells attacking host tissue cause GVHD, but the same alloreactivity gives the curative graft-versus-leukemia effect—separating that benefit from GVHD harm is the art.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a major target organ of GVHD: donor T-cell attack on bile-duct epithelium causes a cholestatic hepatitis with rising bilirubin and alkaline phosphatase, part of the classic skin-gut-liver triad of acute GVHD; severe hepatic GVHD carries a poor prognosis.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Chronic GVHD can clinically mimic systemic sclerosis: donor T cells drive fibrosis of skin and organs resembling scleroderma, with TGF-β-mediated collagen deposition and tight, hidebound skin—so chronic GVHD is an alloimmune model of sclerodermatous fibrosis.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Chronic GVHD often produces a Sjögren's-like sicca syndrome: donor immune attack on lacrimal and salivary glands causes severe dry eyes and mouth, mirroring Sjögren's, so the same autoimmune-like glandular destruction arises here from alloreactivity after transplant.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Host dendritic cells ignite graft-versus-host disease: conditioning damage activates recipient antigen-presenting cells that display alloantigens to donor T cells, priming the attack on host tissues—so depleting these dendritic cells is a strategy to prevent GVHD.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Graft-versus-host disease is driven by a cytokine storm: donor T cells activated against host tissue release a flood of TNF, IL-6 and IFN-γ that amplifies organ damage—so cytokine-targeted drugs (ruxolitinib, anti-IL-6) treat steroid-refractory GVHD.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells distinguish graft-versus-host disease from graft-versus-leukemia: donor NK cells can attack residual leukemia while contributing less to GVHD than T cells—NK biology is exploited to separate the cure from the toxicity of transplant.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a major chronic GVHD target: donor immune attack on bronchioles causes bronchiolitis obliterans, an irreversible obstructive lung disease, so new airflow obstruction after transplant signals pulmonary GVHD—a feared, treatment-resistant complication.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is a major battleground in GVHD: donor T cells attack the gut epithelium, causing severe secretory diarrhea and mucosal sloughing, and gut GVHD severity—worsened by microbiome injury—is a leading determinant of transplant survival.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — GVHD prevention hinges on calcineurin inhibition: cyclosporine and tacrolimus block calcineurin to suppress the donor T-cell activation that drives the disease, forming the backbone of prophylaxis after allogeneic stem-cell transplant.
- `connects-to` → **[Immune System](../immune-system/README.md)** — GVHD is the dark side of transplant immunity: grafted donor immune cells recognize the recipient's tissues as foreign and attack them, the mirror image of rejection—yet the same alloreactivity also fights residual leukemia (graft-versus-leukemia).
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Chronic GVHD frequently strikes the eye: donor immune cells attack the lacrimal glands and ocular surface, causing severe dry eye and keratoconjunctivitis much like Sjögren's—so eye care is a routine part of managing transplant survivors.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — GVHD begins with MHC mismatch: donor T cells recognize the recipient's MHC (HLA) molecules as foreign, especially MHC class II on antigen-presenting cells, so the degree of HLA matching between donor and host predicts the risk and severity of GVHD.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells drive chronic GVHD: alloreactive B cells and autoantibodies fuel the fibrotic, scleroderma-like late disease, which is why B-cell-targeted therapy (the BTK inhibitor ibrutinib) became an approved treatment—shifting GVHD beyond a purely T-cell view.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut GVHD destroys the intestinal epithelium: donor T cells attack the crypts and their stem cells, stripping the gut lining to cause the severe diarrhea that marks acute GVHD—so protecting epithelial stem cells is a treatment goal.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — GVHD cripples the thymus and immune recovery: the donor attack damages thymic tissue needed to educate new T cells, so chronic GVHD leaves patients immunodeficient and prone to infection long after transplant.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Acute GVHD is driven by a TNF-alpha cytokine storm: conditioning and donor T cells trigger TNF-alpha and other cytokines that injure skin, gut and liver, so TNF blockade is among the targeted treatments for steroid-refractory disease.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Chronic GVHD turns on fibroblasts to scar tissue: persistent donor-immune attack and TGF-beta drive fibroblasts to lay down collagen, producing the skin tightening, joint stiffness and lung scarring that define the chronic, scleroderma-like disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Donor killer cells use perforin to attack the host: cytotoxic T and NK cells punch holes in host-cell membranes with perforin to deliver lethal granzymes, a core mechanism of the tissue destruction in acute GVHD.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — GVHD often begins with radiation's photons: total-body irradiation in transplant conditioning damages host tissues, releasing danger signals that activate donor T cells, so the conditioning that enables the graft also primes the graft-versus-host attack.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Gut GVHD can drain the body's potassium: severe inflammation of the bowel lining causes torrential, watery diarrhea—liters a day—that washes out potassium and fluid, a dangerous electrolyte loss needing close replacement.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic GVHD ends in fibrosis: the persistent immune attack lays down scar tissue, hardening the skin like scleroderma and choking the airways with bronchiolitis obliterans, the disabling late face of the disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive GVHD's tissue destruction: recruited by donor T cells, they flood target organs and pour out inflammatory mediators that amplify the damage, making them an effector behind the skin, gut, and liver injury.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — GVHD prophylaxis wastes magnesium: the calcineurin inhibitors cyclosporine and tacrolimus make the kidney spill it, so hypomagnesemia—and the seizures it can provoke—is a common side effect of preventing the disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 sits at the center of GVHD control: calcineurin inhibitors block its production to stop donor T cells, while low-dose IL-2 is given to expand regulatory T cells and calm chronic disease.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Chronic GVHD can attack the nerves and muscle: polyneuropathy, myositis and a myasthenia-like syndrome are recognized neuromuscular complications of the prolonged autoimmune assault.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows GVHD killing cell by cell: donor T cells trigger apoptosis of individual keratinocytes in the skin and crypt cells in the gut, the scattered single-cell death — satellite cell necrosis — that is the disease's histologic signature.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — GVHD strikes the upper gut too: beyond the diarrhea of intestinal involvement, gastric GVHD brings nausea, vomiting, early satiety, and anorexia, diagnosed by biopsy of the stomach lining.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Chronic GVHD can reach the kidney: it is an unusual cause of membranous nephropathy and nephrotic syndrome, the misdirected immune attack depositing in the glomerulus long after the transplant.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Chronic GVHD recruits the donor's B cells: alloantibodies and autoantibodies contribute to its sclerosis, which is why the B-cell-depleting antibody rituximab — and antithymocyte globulin in prophylaxis — are part of its management.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Chronic GVHD stiffens the body's framework: a scleroderma-like fasciitis and joint contractures bind down the limbs, limiting movement as the donor immune cells lay down fibrosis in fascia and muscle.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Chronic GVHD scars the genital tract: vaginal and penile mucosal inflammation, dryness, and stenosis are underrecognized but common, the same lichenoid and sclerotic attack that hits skin and mouth.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Corticosteroids are the first line and a double edge: high-dose glucocorticoids suppress the donor T cells driving GVHD, but their infections, bone loss, and metabolic harm make steroid-sparing agents a constant goal.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatic GVHD strikes the liver cells and ducts: donor T cells attack the bile-duct epithelium and injure hepatocytes, producing a cholestatic hepatitis with rising bilirubin that is one of acute GVHD's three classic targets.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The transplanted immunity can turn on the thyroid: chronic GVHD and post-transplant immune dysregulation raise the rate of autoimmune thyroid disease, one of the late endocrine complications survivors are monitored for.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 cells drive part of the attack: IL-17A from donor T cells fuels the inflammation of skin, gut, and lung GVHD, making the IL-17 axis one of the pathways targeted to tame the disease.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small bowel is a primary GVHD target: donor T cells trigger crypt-cell apoptosis and a secretory diarrhea whose volume grades acute gut GVHD, the leak of the damaged mucosa amplifying the systemic inflammation.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — GVHD is the price of the cure for MDS: the allogeneic transplant given for myelodysplastic syndromes carries a graft-versus-tumor benefit, but the same donor cells that clear the marrow disease can turn on the host.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — A donor-T-cell cytokine drives the attack: IFN-γ pours from activated donor T cells to license macrophages and damage host epithelium, a central effector of acute GVHD's gut, skin and liver injury.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The inflammatory signal travels through JAK-STAT: IFN and other cytokines act via STAT1 to amplify the alloimmune response, the pathway the JAK inhibitor ruxolitinib blocks to treat steroid-refractory GVHD.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — It rides in with the leukemia cure: allogeneic transplant for acute lymphoblastic leukemia delivers a graft-versus-leukemia effect, but the same donor immunity that hunts residual blasts can turn against the host as GVHD.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Tissue damage and alloantigen converge on NF-κB: conditioning injury and donor T-cell activation switch on NF-κB in host antigen-presenting cells and target tissues, amplifying the cytokine storm that drives acute GVHD.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 steers the pathogenic T cells: downstream of IL-6 and IL-21, STAT3 drives the Th17 and effector responses central to GVHD, part of the JAK-STAT signaling that ruxolitinib targets in steroid-refractory disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — It strips defenses and breaches the gut: the immunosuppression treating GVHD plus its destruction of the intestinal barrier let gut bacteria translocate, making infection and sepsis a leading cause of death.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Deep immunosuppression opens the lung to mold: the prolonged steroids and other immunosuppressants treating GVHD profoundly impair defenses, making invasive pulmonary aspergillosis a feared and frequent infection.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — T-cell suppression invites Pneumocystis: the immunosuppression controlling GVHD depletes the T-cell defenses against Pneumocystis, so PJP prophylaxis is standard for these transplant patients.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its drugs are hard on the kidney: the calcineurin inhibitors (ciclosporin, tacrolimus) central to GVHD prophylaxis and treatment are nephrotoxic, and chronic exposure can leave lasting chronic kidney disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Chronic GVHD scleroses and ulcerates the skin: its sclerodermatous skin changes, oral and genital erosions, on top of steroid immunosuppression, leave wounds that are slow and difficult to heal.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Prolonged steroids erode the skeleton: the months to years of high-dose corticosteroids used to control chronic GVHD cause bone loss and avascular necrosis, a major long-term complication.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A grueling chronic complication weighs on mood: the prolonged disability, disfigurement and treatment burden of chronic GVHD after a hoped-for cure contribute to substantial depression in survivors.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin is its commonest target: GVHD produces an acute maculopapular rash and, in chronic disease, lichenoid and sclerodermatous skin with fibrosis, dyspigmentation and nail and hair loss.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It attacks the gut and liver: GVHD causes profuse secretory diarrhoea, nausea and mucositis along the GI tract, and a cholestatic hepatitis when it strikes the liver.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Chronic disease scars the airways: lung GVHD presents as bronchiolitis obliterans, an obstructive, progressive and often irreversible narrowing of the small airways.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It and its drugs can harm the nerves: chronic GVHD causes immune-mediated peripheral neuropathy and myositis, while the calcineurin inhibitors used to treat it cause tremor, seizures and PRES.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Transplant and chronic GVHD derail hormones: thyroid dysfunction, gonadal failure and steroid-induced adrenal insufficiency are common endocrine complications after allogeneic transplant.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can attack the kidney: membranous nephropathy is a recognised renal manifestation of chronic GVHD, compounded by the nephrotoxicity of calcineurin-inhibitor immunosuppression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It is born of donor lymphocytes and cripples lymphoid recovery: donor T cells attack the host while thymic GVHD delays T-cell reconstitution, leaving prolonged immunodeficiency after transplant.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its treatment strains the circulation: long courses of corticosteroids and calcineurin inhibitors for GVHD drive hypertension and cardiovascular risk, and rare cardiac GVHD causes pericarditis.
- `connects-to` → **[Varicella-zoster virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Deep immunosuppression reawakens latent virus: the heavy immune suppression of GVHD lets varicella-zoster reactivate as shingles, sometimes disseminated.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — The first-line treatment: high-dose corticosteroids are the mainstay for acute and chronic graft-versus-host disease, though steroid-refractory disease carries a poor prognosis and drives the search for alternatives.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Cytomegalovirus reawakens under treatment: the heavy immunosuppression for GVHD allows CMV reactivation, causing pneumonitis, colitis and marrow suppression that are major causes of post-transplant death.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — The microbiome shapes its severity: loss of gut bacterial diversity worsens GVHD, while fibre-derived butyrate that nourishes the intestinal epithelium is protective, making diet and the microbiome therapeutic targets.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — JAK inhibition for refractory disease: ruxolitinib, a JAK1/2 inhibitor, is approved for steroid-refractory acute and chronic GVHD, with belumosudil (ROCK2) for chronic disease — targeted alternatives to broad immunosuppression.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo prevents and conditions: methotrexate is a classic GVHD prophylactic and post-transplant cyclophosphamide enables haploidentical grafts by deleting alloreactive T cells, while the conditioning chemo sets the stage for the donor immune attack.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Its treatment wrecks the skeleton: prolonged corticosteroids and calcineurin inhibitors for GVHD cause osteoporosis and avascular necrosis of bone, a major cause of disability in long-term transplant survivors.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — The cure that can turn hostile: allogeneic stem-cell transplant is curative for severe aplastic anaemia, and GVHD is its principal transplant-related danger—the same donor graft that rebuilds the marrow can attack the host.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Hepatic GVHD strikes the bile ducts: donor T cells attack the small bile ducts within the hepatic lobule, causing cholestatic jaundice and a rising bilirubin that grades liver involvement.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Chronic GVHD's autoimmune face: alloreactive germinal-centre reactions and B-cell help generate the autoantibodies and the sclerotic, Sjögren- and scleroderma-like features of chronic graft-versus-host disease.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung GVHD: chronic graft-versus-host disease attacks the small airways as bronchiolitis obliterans, scarring around the alveoli into an irreversible obstructive lung disease, a feared pulmonary complication.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Post-transplant lymphoma: the heavy immunosuppression needed for GVHD lets EBV-driven B cells proliferate unchecked as post-transplant lymphoproliferative disease, which can become a diffuse large B-cell lymphoma.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Transplant for a marrow disease: allogeneic stem-cell transplant is the only cure for myelofibrosis, but graft-versus-host disease is a major source of its transplant-related morbidity and mortality.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Defenceless after transplant: GVHD and its immunosuppression leave allograft recipients profoundly vulnerable to severe, prolonged COVID-19 with blunted vaccine responses.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — Transplant-associated TMA: calcineurin inhibitors and the endothelial injury of the transplant setting cause a thrombotic microangiopathy overlapping with TTP and aHUS, complicating GVHD management.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Autoimmune mimicry: chronic GVHD can produce myositis and fasciitis resembling dermatomyositis, one of several connective-tissue-disease pictures the alloimmune attack reproduces alongside its sclerodermatous and sicca forms.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Fibrotic driver: TGF-β orchestrates the tissue fibrosis of chronic GVHD, scarring skin, lung and gut in the sclerodermatous and bronchiolitis-obliterans forms of the disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Conditioning damage: tissue injury from the conditioning regimen releases IL-1β, an innate alarm signal that primes donor T cells and amplifies the cytokine storm of acute GVHD.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Innate priming: damage-associated signals after transplant activate the NLRP3 inflammasome in host antigen-presenting cells, maturing IL-1β to intensify the alloreactive attack of GVHD.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Prophylaxis target: mTOR drives the metabolism and proliferation of alloreactive donor T cells, so mTOR inhibitors like sirolimus are used in GVHD prophylaxis while sparing regulatory T cells.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Microbial trigger: conditioning damages the gut barrier, letting bacterial LPS engage TLR4 on host antigen-presenting cells, the innate signal that ignites the cytokine storm of acute gut GVHD.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Gut-GVHD biomarker: S100A8/A9 released by damaged intestinal epithelium and neutrophils amplifies GVHD inflammation, and faecal calprotectin tracks the activity of gastrointestinal GVHD.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK signaling in donor B and T cells drives the autoreactive, fibrotic chronic GVHD, the basis for ibrutinib being approved for steroid-refractory chronic graft-versus-host disease—a B-cell-directed strategy distinct from T-cell immunosuppression.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 draws donor monocytes and macrophages into the skin, gut, and liver of acute GVHD, amplifying the inflammatory tissue destruction that the alloreactive donor T-cell attack initiates in these target organs.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Donor cytotoxic T cells drive caspase-3-mediated apoptosis of host epithelial cells—the crypt-cell and keratinocyte apoptosis that is the defining histological lesion of acute GVHD on biopsy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — The IL-33/ST2 alarmin axis is activated by conditioning-induced tissue damage, and a high soluble ST2 level is a validated biomarker predicting steroid-refractory, lethal acute graft-versus-host disease.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Excess BAFF after transplant rescues alloreactive and autoreactive B cells, driving the antibody-mediated, sclerodermatous chronic graft-versus-host disease that B-cell-directed therapies like rituximab and ibrutinib target.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin and other matricellular proteins drive the tissue fibrosis of chronic GVHD, the sclerodermatous skin, fasciitis and bronchiolitis-obliterans lung disease that make advanced chronic GVHD so disabling.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling in donor T cells drives their differentiation into the pathogenic alloreactive effectors of graft-versus-host disease, a targetable axis distinct from calcineurin and JAK inhibition.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — The PI3K-AKT-mTOR pathway (mTOR already mapped, the target of sirolimus) drives the proliferation and metabolic activation of alloreactive donor T cells in GVHD.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 from activated host antigen-presenting cells polarizes donor T cells toward the Th1/IFN-γ response (already mapped) that mediates acute graft-versus-host disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING detection of cytosolic DNA released by conditioning-regimen tissue damage drives type-I-interferon production that amplifies the inflammatory priming of acute graft-versus-host disease.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 engagement restrains alloreactive donor T cells, and checkpoint-inhibitor blockade of this brake can precipitate GVHD-like immunopathology — underscoring its role in tolerance after transplant.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF drives the fibroblast activation and tissue fibrosis of chronic sclerodermatous graft-versus-host disease, alongside the periostin and TGF-β pathways already mapped.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — TCR-driven ERK-MAPK signaling in donor alloreactive T cells contributes to their activation and expansion in the effector phase of graft-versus-host disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives the tissue fibrosis of chronic graft-versus-host disease, especially of skin and lung.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the fibro-inflammatory tissue injury characteristic of chronic graft-versus-host disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) drives the proliferation and effector differentiation of the alloreactive donor T cells that mediate graft-versus-host disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated epigenetic programming of alloreactive donor T cells shapes their pathogenicity in graft-versus-host disease, an emerging therapeutic target.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 chemokine signaling directs the trafficking of alloreactive donor T cells to the target organs of graft-versus-host disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the alloreactive T-cell survival and tissue oxidative-stress responses that shape graft-versus-host disease.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-driven metabolic reprogramming of alloreactive T cells and the hypoxic inflamed target tissues contributes to graft-versus-host disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cell-cycle activity fuels the clonal expansion of alloreactive donor T cells in graft-versus-host disease, an emerging therapeutic target.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the T-cell activation and inflammatory signaling that drive the alloreactivity of graft-versus-host disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LCK) kinase signaling downstream of the T-cell receptor drives the donor-T-cell activation central to graft-versus-host disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation shapes the effector differentiation of the donor T cells that mediate graft-versus-host disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the alloreactive T-cell metabolism of graft-versus-host disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the alloreactive T-cell and target-tissue responses of graft-versus-host disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven donor-T-cell trafficking into target organs drives the tissue injury of graft-versus-host disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 activation participates in the tissue injury of graft-versus-host disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (A2A-receptor) immunoregulatory signaling modulates the alloreactive T-cell responses of graft-versus-host disease.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20-expressing B cells contribute to the alloantibody and immune dysregulation of chronic graft-versus-host disease, a rationale for B-cell-depleting therapy.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the alloreactive immune responses of graft-versus-host disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the T-cell activation and target-organ inflammation of graft-versus-host disease.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the tissue-damage and immune activation of graft-versus-host disease.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Costimulation blockade: abatacept, a CTLA-4-Ig fusion protein, blocks the CD28 costimulation that donor T cells need to activate against host tissue, and it is approved to help prevent graft-versus-host disease after mismatched transplant.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal barrier: conditioning and gut graft-versus-host disease disrupt the secretory IgA that protects the intestinal mucosa, weakening the barrier that normally restrains the microbiota and amplifying the gut inflammation.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Apoptosis balance: anti-apoptotic BCL-2 family proteins set the survival threshold of alloreactive donor T cells and of the target-organ epithelium they attack, influencing both the graft-versus-host injury and the beneficial graft-versus-leukaemia effect.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Sclerodermatous fibrosis: chronic graft-versus-host disease drives fibroblast collagen deposition (TGF-beta and PDGF already mapped), producing the sclerodermatous skin thickening, joint contractures and fibrosis that define the chronic form.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 fibrosis: IL-13 and the type-2 cytokine response promote the macrophage and fibroblast activation that drives the fibrosis of chronic graft-versus-host disease, complementing the TGF-beta (already mapped) pathway.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Post-transplant cytopenias: marrow graft-versus-host effects, drug toxicity and infection lower haemoglobin after transplant, and the resulting anaemia adds to the morbidity of graft-versus-host disease and its treatment.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the inflamed gut and skin (IL-6, TNF and IL-1 already mapped) contribute to the tissue injury of acute graft-versus-host disease, part of the eicosanoid dimension of the alloreactive attack.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 fibrotic axis: IL-4, with IL-13 (already mapped), polarises macrophages and fibroblasts (already mapped) toward the type-2 fibrotic response that drives the sclerotic fibrosis of chronic graft-versus-host disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative tissue injury: the conditioning regimen and the alloreactive attack generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress amplifies the epithelial damage of graft-versus-host disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusional iron overload: the repeated transfusions before and after the transplant load the patient with iron (haemoglobin already mapped), and the resulting iron overload adds oxidative burden to the tissues attacked in graft-versus-host disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Iron-restricted anaemia: the inflammation (IL-6 already mapped) of graft-versus-host disease raises hepcidin, sequestering iron and contributing to the anaemia (haemoglobin already mapped) that complicates the post-transplant course.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial injury: nitric oxide is dysregulated in the endothelial damage of graft-versus-host disease, part of the vascular injury (with the epithelial attack) that underlies the transplant-associated microangiopathy and organ damage.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Vascular injury: VEGF and the dysregulated angiogenesis (nitric oxide already mapped) reflect the endothelial damage of the transplant-associated microangiopathy and the vascular component of graft-versus-host disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — TA-TMA complement: the complement C5 (C3 already mapped) drives the transplant-associated thrombotic microangiopathy that complicates graft-versus-host disease, the target of eculizumab.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilic GVHD: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils whose presence is a marker of graft-versus-host disease, notably the chronic and gastrointestinal forms.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic GVHD: the liver GVHD (the cholestatic hepatitis, the bile-duct destruction) is a major acute-GVHD target organ (with the skin and gut already mapped).
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Donor CD4 cells: the donor CD4 T-helper cells (Th1 and Th17 — IFN-γ and IL-17 already mapped) orchestrate the alloreactive attack and, in the chronic form, the fibrosis of graft-versus-host disease.
- `connects-to` → **[Systemic sclerosis](../systemic-sclerosis/README.md)** — Scleroderma-like chronic GVHD: the chronic GVHD (the fibrosis — collagen and TGF-β already mapped) resembles the systemic sclerosis (scleroderma), sharing the fibrotic mechanisms.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu of graft-versus-host disease, altered by the steroid therapy and the systemic inflammation (IL-6 already mapped).
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of graft-versus-host disease and its treatment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the immune-metabolic milieu of graft-versus-host disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the donor-T-cell alloreactivity of graft-versus-host disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the chronic graft-versus-host disease.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — cGVHD humoral arm: the plasma cells (BAFF and CD20 already mapped) secrete the alloantibodies of the chronic, antibody-mediated graft-versus-host disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated tissue injury of the graft-versus-host disease.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Sclerodermatous cGVHD: the mast cells accumulate in the sclerodermatous skin and, via their profibrotic mediators, promote the fibrosis (TGF-β and PDGF already mapped) of the chronic graft-versus-host disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Acute tissue damage: the neutrophils, recruited by the microbiome-driven and complement (C5aR1 already mapped) signals, amplify the target-tissue injury of the acute graft-versus-host disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-amplified tissue injury of graft-versus-host disease.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact systems activated in the endothelial and target-tissue injury of graft-versus-host disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Post-transplant iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the transfusional iron overload and the anaemia complicating graft-versus-host disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-alloimmune axis: TSLP, from damaged intestinal (already mapped) and skin (already mapped) epithelium of the conditioning regimen, primes host dendritic cells (already mapped) toward alloreactive Th2 and Th17 (already mapped) responses in graft-versus-host disease.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-vascular axis: bradykinin, from the contact-pathway activation in the conditioned endothelium (already mapped), amplifies the vascular permeability and the tissue oedema contributing to the endothelial injury of graft-versus-host disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Engraftment anaemia: erythropoietin drives red-cell regeneration to correct the anaemia of the conditioning regimen, the myelosuppression (bone-marrow already mapped), and the haemolysis (already mapped) complicating graft-versus-host disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell target-organ effector: mast cells (already mapped) in the target organs of GVHD — gut, skin, liver — release histamine that amplifies the vascular permeability and the tissue oedema of acute graft-versus-host disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian transplant biology: circadian disruption is common in transplant patients; melatonin has immunomodulatory effects on T-cell (already mapped) differentiation and alloreactivity, a property studied in the alloimmune context of GVHD.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stress-immune axis: prolactin, elevated by transplant stress and the immunosuppressive (calcineurin, cortisol already mapped) regimen, modulates T-cell (already mapped) and natural-killer-cell (already mapped) activity in the allograft context.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen immunomodulation: testosterone, via androgen receptors on T-helper cells (already mapped) and regulatory T cells (already mapped), attenuates alloreactive T-cell expansion; androgen deficiency amplifies the IL-6 (already mapped)-driven donor T-cell severity of GVHD.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gut-immune serotonergic axis: serotonin, via 5-HT receptors on T-helper cells (already mapped) and natural-killer cells (already mapped), modulates the cytokine-storm (already mapped) immune axis; serotonin dysregulation amplifies the gut-microbiome (already mapped) dysbiosis of mucosal GVHD.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Tolerogenic neuropeptide: oxytocin, via OXTR on regulatory T cells (already mapped) and dendritic cells (already mapped), promotes immunological tolerance by enhancing T-regulatory (Treg) expansion; oxytocin attenuates the IL-6 (already mapped)-driven donor alloreactivity of GVHD.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Alloreactive modulator: vasopressin, via V1aR on regulatory T cells (already mapped) and dendritic cells (already mapped), modulates alloreactive immune activation; vasopressin dysregulation amplifies the IL-6 (already mapped) and TNF-α (already mapped) cytokine-storm cascade of GVHD.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Cytokine-storm ROS scavenger: selenium, as GPx in macrophages (already mapped) and intestinal-epithelium (already mapped), scavenges the cytokine-storm (already mapped)-driven ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) tissue-damage cascade of GVHD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-immune tolerance axis: iodine-dependent thyroid hormones modulate T-helper cell (already mapped) and regulatory T-cell (already mapped) differentiation; iodine deficiency amplifies the IL-6 (already mapped) and TNF-α (already mapped) alloreactive cytokine cascade of GVHD.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — GVHD zinc: zinc cofactors macrophage (already mapped) anti-inflammatory resolution and regulatory T-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive tissue damage in GVHD.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — GVHD sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) amplifies alloreactive T-cell tissue damage in GVHD.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — GVHD copper: copper cofactors macrophage (already mapped) and regulatory T-cell (already mapped) function; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive tissue damage in GVHD.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — GVHD calcium: calcium signals macrophage (already mapped) and regulatory T-cell (already mapped) activation; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) alloreactive cascade of GVHD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — GVHD chloride: chloride channels regulate macrophage (already mapped) and regulatory T-cell (already mapped) volume during alloreactive responses; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of GVHD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — GVHD nitrogen: nitrogen, as protein backbone in cytokines (already mapped) and effector T-cells (already mapped), sustains alloreactive signalling; nitrogen-derived RNS amplifies NF-κB (already mapped) and TNF-α (already mapped) tissue inflammation of GVHD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — GVHD phosphorus: phosphorus as ATP in macrophages (already mapped) and effector T-cells (already mapped) fuels alloreactive kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of GVHD.

[^ferrara-2009-gvhd-review]: Ferrara JL, Levine JE, Reddy P, Holler E. Graft-versus-host disease. *Lancet.* 2009;373(9674):1550-1561. [doi:10.1016/S0140-6736(09)60237-3](https://doi.org/10.1016/S0140-6736(09)60237-3) · [PubMed 19380114](https://pubmed.ncbi.nlm.nih.gov/19380114/)
[^zeiser-2020-ruxolitinib-gvhd-reach]: Zeiser R, von Bubnoff N, Butler J, et al. Ruxolitinib for Glucocorticoid-Refractory Acute Graft-versus-Host Disease. *N Engl J Med.* 2020;382(19):1800-1810. [doi:10.1056/NEJMoa1917635](https://doi.org/10.1056/NEJMoa1917635) · [PubMed 32374962](https://pubmed.ncbi.nlm.nih.gov/32374962/)
[^przepiorka-2020-ruxolitinib-cgvhd-reach3]: Przepiorka D, Luo L, Subramaniam S, et al. FDA Approval Summary: Ruxolitinib for Treatment of Chronic Graft-versus-Host Disease. *Oncologist.* 2022;27(2):98-104. [doi:10.1093/oncolo/oyab055](https://doi.org/10.1093/oncolo/oyab055) · [PubMed 35641197](https://pubmed.ncbi.nlm.nih.gov/35641197/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
