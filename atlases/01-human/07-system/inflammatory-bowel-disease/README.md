---
schema: human-scale-entry/v1
id: inflammatory-bowel-disease
name: Inflammatory Bowel Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic intestinal inflammation: Crohn's disease (transmural, any GI) and ulcerative colitis (mucosal, colon only). TNF-alpha, IL-12/23, and JAK-STAT drive inflammation. Anti-TNF (infliximab), anti-IL-23 (risankizumab), and anti-integrin (vedolizumab) are mainstay biologics."
aliases: ["IBD", "Crohn's disease", "ulcerative colitis", "UC", "CD", "inflammatory bowel disease"]
sources:
  - id: ng-2017-ibd-epidemiology
    type: peer-reviewed
    cite: "Ng SC, Shi HY, Hamidi N, et al. Worldwide incidence and prevalence of inflammatory bowel disease in the 21st century: a systematic review of population-based studies. Lancet. 2018;390(10114):2769-2778."
    doi: "10.1016/S0140-6736(17)32448-0"
    pmid: "29050646"
    url: "https://doi.org/10.1016/S0140-6736(17)32448-0"
  - id: sandborn-2012-vedolizumab
    type: peer-reviewed
    cite: "Feagan BG, Rutgeerts P, Sands BE, et al. Vedolizumab as induction and maintenance therapy for ulcerative colitis. N Engl J Med. 2013;369(8):699-710."
    doi: "10.1056/NEJMoa1215734"
    pmid: "23964932"
    url: "https://doi.org/10.1056/NEJMoa1215734"
  - id: sands-2019-ustekinumab-uc
    type: peer-reviewed
    cite: "Sands BE, Sandborn WJ, Panaccione R, et al. Ustekinumab as Induction and Maintenance Therapy for Ulcerative Colitis. N Engl J Med. 2019;381(13):1201-1214."
    doi: "10.1056/NEJMoa1900750"
    pmid: "31553834"
    url: "https://doi.org/10.1056/NEJMoa1915765"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha is the primary IBD effector cytokine; macrophage TNF drives NF-kB-mediated epithelial apoptosis and barrier disruption; infliximab, adalimumab, certolizumab, and golimumab provide remission in moderate-severe CD and UC refractory to corticosteroids."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "IBD is defined by dysregulated immune response to commensal bacteria; dysbiosis (reduced Bacteroidetes, Faecalibacterium prausnitzii; increased Proteobacteria) is universal; gut microbiome composition predicts treatment response; FMT induces remission in UC in ~30-50% in trials."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "TNF-alpha and IL-13 in IBD disrupt intestinal epithelial tight junctions → increased permeability → bacterial translocation → amplified immune response; mucosal healing (endoscopic) is now the primary therapeutic target — correlates with reduced hospitalization and surgery."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are dominant IBD innate effectors; colonic macrophages normally tolerogenic (CD33+, anti-inflammatory) become pro-inflammatory (TNF-alpha, IL-1beta, IL-23) in IBD under dysbiosis; macrophage polarization is the target of JAK inhibitors and IL-12/23 blockade."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "H4R on mucosal mast cells and Tregs modulates gut inflammation; enterochromaffin-like cells secrete histamine → parietal HCl; H1R/H4R amplify epithelial cytokine release; H4R blockade reduces experimental colitis; histamine levels correlate with IBD disease activity."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "IL-10 is the primary mucosal immunoregulatory cytokine; IL-10R mutations cause VEO-IBD (infantile perianal fistulizing Crohn's) curable by HSCT; IL-10 KO mice develop spontaneous microbiota-driven colitis; anti-TNF and JAK inhibitors partially restore IL-10 signaling in IBD."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: treated-by
    note: "Adalimumab achieves 52-week remission in 36% of Crohn's (CHARM trial) and 16.5% in UC (ULTRA-2); blocks mucosal macrophage TNFα → reduces NF-κB-driven epithelial apoptosis; both induction and maintenance approved; perianal fistula closure benefit confirmed."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is elevated in IBD mucosa but anti-IL-17A therapy (secukinumab) paradoxically worsens IBD in AS/PsA patients; gut epithelial IL-17A may protect barrier integrity; this dual role distinguishes mucosal IL-17A function from systemic Th17 pathogenicity."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is the core target in inflammatory bowel disease: ulcerative colitis causes continuous mucosal inflammation from the rectum proximally while Crohn's can produce patchy transmural colitis; this drives bloody diarrhea, urgency and colorectal-cancer risk."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Long-standing colonic IBD is a major risk factor for colorectal cancer: chronic inflammation drives a dysplasia-carcinoma sequence distinct from sporadic CRC, so patients with extensive UC or Crohn's colitis need surveillance colonoscopy with biopsies after ~8-10 years."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "IBD and ankylosing spondylitis overlap on the spondyloarthritis spectrum: they share IL-23/Th17 biology and HLA-B27 background, axial arthritis is a common extraintestinal feature of IBD, and TNF and IL-23 blockers treat both—though IL-17 inhibitors can paradoxically flare IBD."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "IBD and psoriasis are both IL-23/Th17-driven immune diseases that often co-occur and share biologics: ustekinumab (anti-IL-12/23) treats both—yet anti-TNF agents for IBD can paradoxically trigger psoriasis, revealing how intertwined these cytokine circuits are."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "IBD and rheumatoid arthritis are distinct immune-mediated diseases united by anti-TNF therapy: TNF blockers transformed both, yet RA is an autoantibody-driven symmetric synovitis while IBD is barrier-driven gut inflammation—one cytokine, very different target tissues."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "IBD reflects a breakdown of intestinal tolerance maintained by regulatory T cells: Tregs and their IL-10 restrain responses to gut microbes, and losing this brake (as with IL-10-receptor mutations) unleashes chronic inflammation—restoring Treg function is a goal."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells drive the inflammation of IBD: Th1/Th17 responses dominate Crohn's while a modified Th2 response marks ulcerative colitis, and these effector T cells attacking the gut wall are why immunosuppressants and biologics blocking their cytokines work."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Crohn's disease commonly strikes the small intestine: transmural inflammation of the terminal ileum causes strictures, fistulas and B12/bile-acid malabsorption—distinguishing Crohn's from ulcerative colitis, which is limited to the colon's mucosa."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 helps drive Crohn's disease: this cytokine, sharing a subunit with IL-23, pushes the Th1 response that inflames the gut wall, which is why ustekinumab—blocking the shared p40 subunit of IL-12 and IL-23—is an effective IBD therapy."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibitors are an oral option in IBD: several cytokines driving gut inflammation signal through the JAK-STAT pathway, so tofacitinib and upadacitinib treat ulcerative colitis when antibody biologics fail—a small-molecule alternative to anti-TNF."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "IBD is the prototypical chronic inflammatory disease of the digestive system: Crohn's can inflame anywhere from mouth to anus while ulcerative colitis is confined to the colon, so it reshapes gut structure and function and predisposes to bowel cancer."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "IBD reaches beyond the gut to the skin: erythema nodosum and pyoderma gangrenosum are classic cutaneous manifestations that track (or sometimes precede) bowel activity, so the integumentary system is a window onto this systemic immune disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils drive tissue damage in active IBD: recruited into the mucosa, they form the crypt abscesses that histologically define a flare and release proteases and oxidants that ulcerate the gut wall—so blunting neutrophil influx is part of controlling disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and IBD interact both ways: deficiency is common with intestinal inflammation and malabsorption, and low vitamin D—an immune modulator supporting gut-barrier and regulatory T-cell function—is linked to more active disease, so levels are checked and repleted."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "IBD's most important liver tie is primary sclerosing cholangitis: this progressive bile-duct scarring occurs mostly with ulcerative colitis, raises the risk of cholangiocarcinoma and colorectal cancer, and runs an independent course unaffected by bowel treatment."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "IBD, especially Crohn's, traces to faulty autophagy: risk genes like ATG16L1 cripple the cellular self-cleaning that clears gut bacteria and keeps Paneth cells working, so impaired autophagy lets the microbiome provoke chronic intestinal inflammation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells set the thermostat of IBD: by sampling gut microbes and deciding whether to trigger tolerance or attack, these cells tip the Th17-versus-regulatory-T-cell balance that determines whether the intestine stays calm or inflames."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B-cell antibodies help classify IBD: serologic markers—ASCA antibodies leaning toward Crohn's and pANCA toward ulcerative colitis—reflect the B-cell response to gut antigens and help distinguish the two forms when biopsies are ambiguous."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "IBD is a leading cause of iron-deficiency anemia: chronic gut bleeding and inflammation that blocks iron absorption leave many patients anemic, so iron status is monitored and often repleted intravenously when the gut can't take it up."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "IBD spills out onto the skin: erythema nodosum and pyoderma gangrenosum are extraintestinal manifestations that can flare with bowel activity, so skin lesions are a window onto the systemic reach of the gut disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the IBD gut: their numbers rise in the diseased mucosa, where their histamine and mediators drive the pain, diarrhea and barrier breakdown, linking the gut's immune-nerve crosstalk to symptoms."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "IBD inflames the eyes: uveitis and episcleritis are extraintestinal manifestations that can flare with bowel activity, so red, painful eyes in an IBD patient signal active systemic disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Crohn's disease scars the bowel into strictures: chronic transmural inflammation drives fibrosis of the gut wall, narrowing it until food can't pass—the fibrostenotic complication that often needs surgery."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Severe colitis bleeds away potassium: heavy diarrhea flushes potassium from the body, and the resulting hypokalemia can worsen gut paralysis and precipitate toxic megacolon in acute attacks."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "IBD is mapped by light and imaging: colonoscopy inspects the mucosa directly, while CT and MR enterography photons reveal small-bowel inflammation, strictures and abscesses beyond the scope's reach."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "IBD depletes zinc: chronic diarrhea and malabsorption lower it, contributing to the poor healing, skin rashes and impaired immunity that complicate the disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "IBD and its drugs strain the marrow: chronic inflammation and the thiopurines used to treat it can suppress blood-cell production, so counts are watched throughout therapy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy distinguishes IBD's two forms: Crohn's burrows transmurally with granulomas and fissures, while ulcerative colitis stays mucosal with crypt abscesses — and both show the disturbed Paneth cells and autophagy behind the barrier failure."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "IBD reaches the kidney by several routes: fat malabsorption drives calcium-oxalate stones, chronic inflammation can deposit AA amyloid, and the drugs used to treat it add their own nephrotoxic risk."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Chronic diarrhea flushes out magnesium: ongoing intestinal losses in active IBD deplete the mineral along with potassium and zinc, a deficiency that adds to the fatigue and cramping of a flare."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "The colon's fuel comes from fermented fiber: gut bacteria turn dietary fiber into butyrate that nourishes colonocytes and calms inflammation, so a depleted fiber-butyrate axis is implicated in IBD and exclusive enteral nutrition can induce remission."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia is IBD's most common complication: chronic gut bleeding plus inflammation that blocks iron use leaves erythrocytes small and scarce, a mixed iron-deficiency and anemia-of-chronic-disease that drives much of the fatigue patients feel."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "The pancreas is caught both ways: IBD itself raises the risk of acute and autoimmune pancreatitis, and the thiopurine drugs used to treat it are a classic cause of drug-induced pancreatitis that forces a change of therapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Active IBD thickens the blood: the systemic inflammation of a flare drives a hypercoagulable state, so deep-vein thrombosis and pulmonary embolism are markedly more common — which is why hospitalized patients get clot prophylaxis even amid bloody diarrhea."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "IBD erodes the skeleton: chronic inflammation, malabsorption of calcium and vitamin D, and repeated steroid courses thin the bones, making osteoporosis and fragility fractures a common long-term complication needing bone monitoring."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "In Crohn's the wall scars shut: chronic transmural inflammation activates fibroblasts to lay down collagen, and the resulting fibrosis stiffens the bowel into the strictures and obstruction that often demand surgery."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "A specific microbe is implicated: adherent-invasive E. coli colonize the Crohn's mucosa, invade epithelium, and survive inside macrophages, one of the clearest examples of a gut bacterium tipping a susceptible host into chronic intestinal inflammation."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the master switch behind the flare: this transcription factor, fired by microbial and cytokine signals in the gut wall, turns on the TNF, IL-6 and chemokine genes that sustain IBD inflammation — the hub many therapies act upstream of."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "The inflamed mucosa fills with antibody factories: expanded plasma cells secrete IgG and IgA into the bowel wall, and in ulcerative colitis autoantibodies and this B-lineage response form part of the tissue damage alongside the T-cell-driven inflammation."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: connects-to
    note: "C. difficile both complicates and mimics IBD: the disrupted microbiome and immunosuppression of IBD raise C. diff risk, and superimposed infection drives flares and toxic megacolon — so stool toxin testing is routine when a patient worsens."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Anemia is IBD's commonest extraintestinal complication: chronic gut blood loss plus the iron-sequestering anemia of inflammation drains hemoglobin, so iron status is tracked and intravenous iron often needed."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The inflammasome stokes the gut wall: microbial breach of the epithelium activates NLRP3 in mucosal macrophages, releasing IL-1β that amplifies the inflammation — a node studied to dampen IBD beyond TNF blockade."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 and IL-23 drive the gut through STAT3: STAT3 signaling sustains the pathogenic Th17 response and epithelial changes of IBD, the JAK-STAT axis that tofacitinib and other JAK inhibitors interrupt."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe colitis and immunosuppression invite sepsis: toxic megacolon and bowel perforation breach the gut barrier, and the biologics and steroids used to control IBD raise the risk of serious infection and sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Inflammation blunts the marrow beyond blood loss: the chronic cytokines of IBD raise hepcidin and suppress erythropoiesis, an anemia of chronic disease that compounds the iron deficiency from gut bleeding."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Its TNF blockers can wake latent TB: the anti-TNF biologics central to IBD treatment disable the granuloma containing Mycobacterium tuberculosis, so latent-TB screening and treatment precede therapy to prevent reactivation."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Combination immunosuppression opens the lung: thiopurines, steroids and biologics together in IBD can deplete T-cell defenses enough to risk Pneumocystis pneumonia, weighed in high-intensity regimens."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Through PSC it threatens the bile ducts: IBD — especially ulcerative colitis — is tightly linked to primary sclerosing cholangitis, whose chronic biliary inflammation carries a markedly raised risk of cholangiocarcinoma."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Its biologics can reactivate hepatitis B: the anti-TNF and other immunosuppressive therapies for IBD can reawaken a dormant hepatitis B virus, so screening and antiviral prophylaxis precede treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Combined immunosuppression opens the lung to mold: corticosteroids stacked on biologics or JAK inhibitors for IBD deeply blunt immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Gut inflammation and chronic disease weigh on mood: the relapsing course, urgency and gut-brain inflammatory signaling of IBD give it markedly elevated rates of depression."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunosuppression reawakens shingles: the thiopurines, anti-TNF and especially JAK inhibitors used for IBD blunt antiviral immunity and notably raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Crohn's reaches the urinary tract: fat malabsorption causes enteric hyperoxaluria with oxalate kidney stones, and bowel inflammation can form enterovesical fistulas and rarely renal amyloidosis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An unpredictable, urgent disease breeds worry: the relapsing flares, faecal urgency and gut-brain signalling of IBD foster chronic health anxiety alongside its well-documented depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is an immune-mediated disease at its core: dysregulated mucosal immunity with the IL-23/Th17 axis and innate immune defects drives the gut inflammation that biologic therapies target."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It inflames joints beyond the gut: enteropathic peripheral arthritis and sacroiliitis are common extraintestinal manifestations, alongside the steroid- and inflammation-driven bone loss of IBD."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can reach the nerves: terminal-ileal Crohn's causes vitamin B12 deficiency with neuropathy, and IBD raises the risk of cerebral venous thrombosis and peripheral neuropathy."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic gut inflammation reaches the vessels: IBD raises the risk of venous thromboembolism and, through systemic inflammation, of cardiovascular disease and rare pericarditis."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It touches fertility and pregnancy: active IBD and pelvic surgery can impair fertility, sulfasalazine causes reversible male infertility, and flares complicate pregnancy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its drugs raise lymphoma risk: thiopurines and anti-TNF therapy for IBD slightly increase the risk of lymphoma, including the rare hepatosplenic T-cell lymphoma in young men."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids tame the flare: corticosteroids induce remission in acute inflammatory bowel disease flares, but their toxicity makes them unsuitable for maintenance, driving the use of steroid-sparing biologics."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Shared immune dysregulation: inflammatory bowel disease and atopic dermatitis co-occur more than expected and share cytokine pathways, with JAK inhibitors now treating both."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: connects-to
    note: "TB shadows its treatment and mimics it: latent tuberculosis must be excluded before anti-TNF therapy, which can reactivate it, and intestinal TB closely mimics Crohn's disease."
  - target: 01-human/05-tissue/peyers-patches
    relation: connects-to
    note: "Crohn's begins over the gut's lymphoid follicles: its earliest lesions are aphthous ulcers of the epithelium covering Peyer's patches, where defective handling of bacteria by M cells and macrophages ignites the transmural inflammation of Crohn's disease."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "The gut-kidney axis of mucosal IgA: inflammatory bowel disease disturbs intestinal IgA production and barrier integrity, and IgA nephropathy is the commonest glomerulonephritis complicating IBD—mucosal immune dysregulation surfacing in the kidney."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A cautionary overlap of autoimmunity: TNF inhibitors that treat inflammatory bowel disease can unmask or worsen demyelinating disease, so multiple sclerosis is a contraindication—evidence that blocking one cytokine helps the gut yet harms the central nervous system."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Primary sclerosing cholangitis: IBD—especially ulcerative colitis—associates with PSC, where bile-duct inflammation and fibrosis injure the hepatic lobule, progressing to cirrhosis and raising cholangiocarcinoma risk."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Enteropathic spondyloarthritis: IBD shares the IL-23/Th17 axis with psoriatic arthritis and ankylosing spondylitis, the seronegative spondyloarthropathies that frequently co-occur with bowel inflammation."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A prothrombotic, atherogenic state: active IBD inflammation raises the risk of venous and arterial thrombosis and accelerates atherosclerosis of the arterial wall, a cardiovascular hazard beyond the gut."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Autoimmune clustering: inflammatory bowel disease and type 1 diabetes co-occur more than chance through shared HLA and immune-susceptibility loci, part of the broader tendency of organ-specific autoimmune diseases to aggregate."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "The liver comorbidity: non-alcoholic steatohepatitis is the commonest liver disease in IBD, driven by chronic inflammation, corticosteroids and metabolic disturbance rather than the bile-duct disease of associated cholangitis."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Aberrant mucosal antibody factories: chronic IBD spawns ectopic lymphoid follicles with active germinal centres in the inflamed gut wall, fuelling the local plasma-cell and autoantibody responses that sustain the disease."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 inflammation: IL-6 signalling through STAT3 sustains mucosal inflammation in IBD and renders lamina propria T cells resistant to apoptosis, perpetuating the disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis and stricturing: TGF-β drives the intestinal fibrosis behind the strictures of Crohn's disease, with the SMAD7 antagonist concept aimed at restoring its anti-inflammatory signalling."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Creeping fat: hypertrophied mesenteric adipose ('creeping fat') wrapping inflamed Crohn's bowel secretes leptin and other adipokines that modulate local gut inflammation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 transmural inflammation: IFN-γ from Th1 cells drives the transmural, granulomatous inflammation characteristic of Crohn's disease, damaging the intestinal wall."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome injury: IL-1β from inflammasome-activated macrophages amplifies the mucosal inflammation of IBD, with the IL-1/IL-1β axis an emerging therapeutic target."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the inflamed gut wall in IBD, replenishing the macrophages that sustain chronic intestinal inflammation."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA genetic risk: MHC class II HLA loci are major genetic associations of IBD, presenting gut microbial and self antigens to the CD4 T cells that drive the chronic mucosal immune response."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stricturing fibrosis: PDGF drives the intestinal fibroblast and myofibroblast proliferation behind the fibrotic strictures that complicate Crohn's disease and require surgery."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal antibody barrier: dysregulated secretory IgA at the gut surface alters the microbiota and barrier homeostasis whose breakdown underlies the aberrant immune response of IBD."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microbial sensing: TLR4 and related innate receptors sensing a dysbiotic microbiota across a breached epithelial barrier drive the loss of tolerance central to the gene-environment-microbiome model of IBD."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Ulcerative colitis Th2 arm: IL-13 from natural killer T and innate lymphoid cells damages the epithelial barrier and impairs tight junctions in ulcerative colitis, the type-2-skewed cytokine distinguishing it from Crohn's."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Innate DNA sensing: cytosolic and microbial DNA activating cGAS-STING in gut epithelium and myeloid cells amplifies intestinal inflammation, and STING gain-of-function causes an autoinflammatory enteropathy overlapping IBD."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Flare therapy: corticosteroids acting through the glucocorticoid receptor — systemic prednisone or gut-targeted budesonide — induce remission of IBD flares, though their toxicity and the failure to heal mucosa long-term make them bridging rather than maintenance therapy."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Fibrostenotic strictures: chronic transmural inflammation in Crohn's disease drives myofibroblast collagen deposition that forms the fibrotic strictures causing bowel obstruction, a fibrotic complication that immunosuppression does not reverse and that often needs surgery."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Epithelial alarmin: IL-33 released from damaged intestinal epithelium acts as an alarmin on innate lymphoid cells and mast cells, an upstream amplifier of the mucosal inflammation that has both pro-inflammatory and reparative roles in IBD."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbial sensing: TLR (TLR4 mapped) and IL-1-receptor signalling through MyD88 to NF-κB (mapped) transduces the dysregulated response to gut microbiota that drives the mucosal inflammation of IBD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Regulatory T cells: IL-2 sustains the regulatory T cells that maintain mucosal tolerance, and defective IL-2/Treg signalling contributes to the loss of tolerance to gut antigens in IBD."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Barrier integrity: E-cadherin junctions seal the intestinal epithelium, and the barrier breakdown that lets luminal microbes contact the mucosa is a central permissive step in IBD pathogenesis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Paneth-cell autophagy: mTOR signalling regulates Paneth-cell function and the autophagy (already mapped) that clears intracellular bacteria, a pathway whose Crohn's-associated defects impair mucosal antimicrobial defence."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Mucosal oxidative defence: NRF2 antioxidant defence protects the intestinal epithelium from the oxidative stress of chronic mucosal inflammation in inflammatory bowel disease."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Epithelial apoptosis: caspase-3-mediated apoptosis of intestinal epithelial cells contributes to the barrier breakdown that perpetuates the inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) regulates intestinal-epithelial survival and restitution, processes disrupted in the barrier failure of inflammatory bowel disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the mucosal macrophage and epithelial inflammatory responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives both regulatory-T-cell tolerance and the intestinal fibrosis (strictures) of inflammatory bowel disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling drives the Th1 epithelial injury characteristic of the mucosal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling in intestinal epithelium and immune cells transduces the cytokine stimuli that sustain the inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) shapes the immune-cell activation and epithelial responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the intestinal epithelial oxidative-stress defense and the T-cell programs implicated in inflammatory bowel disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic inflamed mucosa shapes the barrier and inflammatory responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven mucosal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the intestinal-epithelial and immune-cell responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic T-cell activity contributes to the epithelial injury of inflammatory bowel disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the immune-cell activation and epithelial-barrier signaling of inflammatory bowel disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the gut mucosa contributes to the intestinal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the mucosal immune responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of ciclosporin and tacrolimus, participates in the T-cell activation of inflammatory bowel disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed intestinal mucosa of inflammatory bowel disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the mucosal innate immune responses of inflammatory bowel disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling provides immunoregulatory modulation of the mucosal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the intestinal-epithelial and immune gene programs of inflammatory bowel disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage-driven mucosal inflammation and fibrosis of inflammatory bowel disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the mucosal immune dysregulation of inflammatory bowel disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: anaemia is the commonest systemic complication of inflammatory bowel disease, from chronic gut blood loss (iron already mapped) and inflammation-driven suppression of erythropoiesis, lowering haemoglobin and worsening fatigue."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 mucosal inflammation: IL-4 and the Th2 axis contribute to the mucosal immune response of ulcerative colitis, complementing the Th17/IL-23 and Th1 pathways (already mapped) that dominate Crohn's disease."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Dietary modulation: omega-3 fatty acids give rise to pro-resolving and anti-inflammatory mediators, and dietary fat composition influences the mucosal inflammation of inflammatory bowel disease, one of the diet-related factors shaping disease activity."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Mucosal eicosanoids: prostaglandins both protect and inflame the gut mucosa, so NSAIDs that block their synthesis can precipitate inflammatory bowel disease flares, while their modulation is part of the mucosal inflammatory response."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Gut motility and secretion: enterochromaffin-cell serotonin, elevated in the inflamed mucosa, drives the diarrhoea, altered motility and visceral hypersensitivity that contribute to the symptoms of inflammatory bowel disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative mucosal injury: reactive oxygen species from the infiltrating neutrophils (already mapped) and xanthine oxidase damage the epithelial barrier in inflammatory bowel disease, and this oxidative stress (NRF2 already mapped) perpetuates the inflammation."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Mucosal iNOS: inducible nitric oxide synthase is upregulated in the inflamed gut of inflammatory bowel disease, and the resulting nitric oxide, with the oxidative stress (already mapped), contributes to the epithelial injury and altered blood flow."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile-acid malabsorption: ileal Crohn's disease and resection disrupt the enterohepatic circulation of the bile acids derived from cholesterol, causing bile-acid diarrhoea and disturbed lipid handling, part of the malabsorption of inflammatory bowel disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Metabolic bone disease: the malabsorption, chronic inflammation and steroid therapy of inflammatory bowel disease deplete calcium and vitamin D, causing the osteoporosis and metabolic bone disease that complicate the illness."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the IL-6-driven (already mapped) hepcidin sequesters iron and, with the iron-deficiency (already mapped) from blood loss, causes the mixed anaemia that is the commonest systemic complication of inflammatory bowel disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Mucosal angiogenesis: VEGF drives the increased microvascular density and angiogenesis of the inflamed gut mucosa, part of the vascular component of the chronic inflammation of inflammatory bowel disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Diarrhoeal losses: the profuse diarrhoea of active inflammatory bowel disease depletes sodium and water, causing the volume depletion and electrolyte disturbance (calcium already mapped) that complicate flares."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Creeping-fat adipokine: adiponectin, with leptin (already mapped), is an adipokine of the 'creeping fat' — the mesenteric adipose that wraps the inflamed Crohn's bowel — a distinctive feature of inflammatory bowel disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory creeping-fat adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the creeping fat and the systemic inflammation (IL-6 already mapped) of inflammatory bowel disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Diarrhoeal magnesium loss: the profuse diarrhoea of active inflammatory bowel disease depletes magnesium (with sodium already mapped), contributing to the electrolyte disturbance of flares."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils prominent in the ulcerative-colitis mucosa of inflammatory bowel disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "IBD bone loss: the chronic inflammation, the malabsorption and the corticosteroid (glucocorticoid-receptor already mapped) use cause the osteoporosis and the low bone density of the cortical bone in inflammatory bowel disease."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Gut-GVHD parallel: the gastrointestinal graft-versus-host disease resembles inflammatory bowel disease histologically and mechanistically, both driven by the microbiome (TLR4 already mapped)-immune dysregulation of the gut."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Enteric neuroimmune: substance P of the enteric nervous system drives the neurogenic inflammation and the visceral hypersensitivity/pain of inflammatory bowel disease."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium status: the selenium selenoprotein antioxidant defence modulates the gut inflammation, and its deficiency (the malabsorption) is common and immunomodulatory in inflammatory bowel disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension present in the UC-leaning end of inflammatory bowel disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Epithelial cytotoxicity: the cytotoxic T cells (perforin already mapped), including the tissue-resident memory subset, contribute to the epithelial injury of inflammatory bowel disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the dysregulated mucosal innate immunity of inflammatory bowel disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in mucosa: the complement C5 and its C5a (with C3 already mapped) contribute to the neutrophil (already mapped) recruitment and the mucosal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the inflamed mucosa of inflammatory bowel disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped), and its dysregulation on the injured epithelium amplifies the mucosal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "IBD iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron-deficiency anaemia that is the commonest systemic complication of inflammatory bowel disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP released by the inflamed intestinal epithelium (already mapped) drives dendritic-cell (already mapped) and mast-cell (already mapped) priming that sustains the Th2 (IL-4, IL-5, IL-13 already mapped) and Th9 arms of mucosal immunity in IBD."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin gut pain and permeability: bradykinin, via B1/B2 receptors on intestinal epithelial cells (already mapped) and mast cells (already mapped), amplifies gut pain, mucosal permeability and the NF-kB (already mapped) inflammatory cascade of IBD."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement and kinin regulation: C1-INH controls the classical complement pathway (C3, C5 and C5aR1 already mapped) and the bradykinin (already mapped) kinin-kallikrein axis; deficiency worsens mucosal oedema and complement-mediated epithelial (already mapped) injury in IBD."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia-of-IBD therapy: erythropoietin, responding to the anaemia of chronic disease (already mapped) and iron-deficiency anaemia (already mapped) complicating IBD, stimulates erythrocyte (already mapped) production and can suppress mucosal NF-kB (already mapped) inflammation."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Intestinal fibrosis mediator: periostin, from intestinal fibroblasts (fibrosis already mapped) under TGF-β (already mapped) and IL-13 (already mapped) stimulation, promotes subepithelial collagen (already mapped) deposition and the stricturing phenotype of Crohn's disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Enteric melatonin: melatonin produced by enterochromaffin cells of the gut epithelium (already mapped) activates MT1/MT2 receptors on mast cells (already mapped) and immune cells, attenuating the NF-κB (already mapped) and NLRP3 (already mapped) mucosal inflammation of IBD."
---

# Inflammatory Bowel Disease

## Overview

**Inflammatory bowel disease (IBD)** encompasses two major chronic, relapsing-remitting intestinal inflammatory conditions — **Crohn's disease (CD)** and **ulcerative colitis (UC)** — characterized by dysregulated mucosal immunity against the intestinal microbiome in genetically susceptible individuals. IBD affects approximately **6.8 million people worldwide** (prevalence highest in North America and Europe, rapidly increasing in Asia, Africa, and South America) [^ng-2017-ibd-epidemiology].

IBD is distinct from infectious colitis, ischemic colitis, and irritable bowel syndrome (IBS, functional — no inflammation). The chronic nature, unpredictable relapse, colorectal cancer risk, and systemic manifestations make IBD a major cause of disability in young adults.

**Crohn's disease vs. ulcerative colitis:**

| Feature | Crohn's Disease (CD) | Ulcerative Colitis (UC) |
|:---|:---|:---|
| Location | Any GI segment (mouth to anus); ileum + right colon most common | Colon only; rectum always involved; continuous proximal extension |
| Depth | Transmural inflammation | Mucosal/submucosal only |
| Distribution | Skip lesions (patchy) | Continuous |
| Complications | Fistulae, abscesses, strictures, bowel obstruction | Toxic megacolon, massive hemorrhage |
| Cancer risk | Slightly elevated (small bowel CD) | Increased with extent and duration (surveillance colonoscopy) |
| Surgery | Resection (not curative — recurrence at anastomosis) | Colectomy is curative |
| Serology | ASCA+ (Saccharomyces cerevisiae antibodies) ~50% | pANCA+ ~65% |

**Classification (UC extent — Montreal Classification):**
- E1 (proctitis): Disease limited to rectum; managed with topical 5-ASA
- E2 (left-sided): Extends to splenic flexure; systemic therapy often needed
- E3 (extensive/pancolitis): Proximal to splenic flexure; highest cancer and complication risk

**CD classification (Montreal — location, behavior, perianal):**
- L1 (ileal), L2 (colonic), L3 (ileocolonic), L4 (upper GI)
- B1 (non-stricturing, non-penetrating), B2 (stricturing), B3 (penetrating/fistulizing)
- Perianal disease: p (+perianal) modifier

## Structure

### Genetic architecture of IBD

IBD is a complex polygenic disease with >240 susceptibility loci (GWAS):
- **NOD2 (CARD15):** First IBD gene (Hugot and Ogura 2001); variants (Arg702Trp, Gly908Arg, Leu1007fsX; 3 major; allele frequency 8-15% Caucasian) → impaired bacterial peptidoglycan sensing → defective mucosal immunity → ileal Crohn's; homozygous NOD2 variants → 40× increased CD risk
- **ATG16L1 T300A:** Autophagy pathway → impaired bacterial clearance and Paneth cell function → CD susceptibility
- **IL23R R381Q:** Protective loss-of-function variant; IL-23R signaling required for Th17 differentiation → IL-23 pathway variants among strongest IBD loci; basis for ustekinumab (anti-IL-12/23) and mirikizumab (anti-IL-23p19) therapy
- **HLA region:** Complex IBD associations; HLA-DRB1*01:03 strongly associated with extensive UC
- **CARD9, JAK2, STAT3:** Multiple inflammatory pathway variants in IBD GWAS

### Mucosal immune dysregulation

**Normal gut immunity:** Lamina propria macrophages (tolerogenic CD33+, IL-10-producing) and Tregs maintain homeostasis to commensal bacteria; IgA secretion (plasma cells → secretory IgA → bacterial coating → immune exclusion); epithelial barrier (tight junctions: claudins, occludin, ZO-1) + mucus layer → physical separation

**IBD pathogenesis:**
1. **Epithelial barrier disruption:** Genetic (NOD2, ATG16L1) or environmental (antibiotics, NSAIDs, Western diet → reduced Bacteroidetes) → altered microbiome → intestinal permeability → bacterial/LPS translocation into lamina propria
2. **Innate immune activation:** Pattern recognition receptors (TLR4, NOD2) on macrophages and dendritic cells → NF-kB → TNF-alpha, IL-1beta, IL-6, IL-12, IL-23
3. **Adaptive immune dysregulation:**
   - **Crohn's:** Th1 (IFN-gamma, IL-2) and Th17 (IL-17A/F, IL-22) dominant; driven by IL-12 (Th1) and IL-23 (Th17/Th1) from DCs
   - **UC:** Th2 (IL-5, IL-13) pattern in some patients; atypical Th2 (non-classical NKT cells → IL-13); IL-13 → epithelial apoptosis and barrier dysfunction; eosinophilic infiltration
4. **Treg deficiency:** Reduced FoxP3+ Tregs in IBD mucosa → insufficient immunosuppression; impaired IL-10 signaling (IL-10 knockout → colitis in mice; IL-10R mutations → neonatal IBD)
5. **Microbiome dysbiosis:** Reduced diversity, reduced short-chain fatty acid (SCFA) producers (Faecalibacterium prausnitzii, Roseburia), increased mucosa-adherent bacteria (adherent-invasive E. coli, AIEC) → epithelial invasion and inflammatory amplification

## Function

### Clinical presentation

**Ulcerative colitis symptoms:**
- **Bloody diarrhea** (cardinal symptom): Mucopurulent bloody stool, ≥6 stools/day in severe disease
- Urgency, tenesmus (rectal inflammation), nocturnal diarrhea
- Cramps, lower abdominal pain
- **Acute severe UC (Truelove-Witts criteria):** ≥6 bloody stools/day + at least one systemic feature (HR >90, fever >37.8°C, Hb <10.5 g/dL, ESR >30) → inpatient IV corticosteroids; if no response in 72h → infliximab or colectomy

**Crohn's disease symptoms:**
- Right lower quadrant pain (ileitis → terminal ileum), diarrhea (often non-bloody), weight loss
- **Strictures:** Colicky obstructive pain (post-prandial), early satiety
- **Fistulae:** Entero-enteric (asymptomatic), entero-vesicular (pneumaturia, fecaluria), entero-vaginal (fecal vaginal discharge), perianal (complex anal fistulae with abscesses → significant morbidity)
- **Abscesses:** Psoas abscess, intra-abdominal → fever, mass; drain + antibiotics

**Extra-intestinal manifestations (EIMs, 25-40% of IBD):**
- **Joints:** Peripheral arthritis (pauciarticular — correlates with gut disease activity; polyarticular — independent); axial arthropathy (sacroiliitis, IBD-associated AS — independent of gut activity)
- **Skin:** Erythema nodosum (correlates with activity), pyoderma gangrenosum (independent, treat with biologics)
- **Eyes:** Episcleritis (activity-correlated), uveitis (independent — requires ophthalmology)
- **Liver/biliary:** Primary sclerosing cholangitis (PSC) — almost exclusively UC (~5%); increased cholangiocarcinoma risk; no effective medical therapy; liver transplant if end-stage; increased colorectal cancer risk in PSC-UC (annual surveillance colonoscopy regardless of UC extent)

### Biomarkers

- **Fecal calprotectin:** Neutrophil cytosolic protein; correlates with endoscopic inflammation; ≥150 μg/g = active mucosal disease; used to monitor therapy response and guide endoscopy scheduling
- **CRP:** Non-specific but elevated in CD (especially ileal disease); may be normal in UC with mild activity
- **Serology:** ASCA (Crohn's) and pANCA (UC) — distinguish CD from UC in indeterminate colitis (~70% sensitivity, >90% specificity)
- **Endoscopy:** Gold standard; direct visualization + biopsy; mucosal healing (Mayo score 0-1 in UC, SES-CD in CD) is the therapeutic target

## Pathology

### Treatment [^sandborn-2012-vedolizumab] [^sands-2019-ustekinumab-uc]

**Step-up vs. early aggressive (top-down) strategy:**
- **Step-up (conventional):** 5-ASA → corticosteroids → thiopurines → anti-TNF → combination
- **Top-down (early biologic):** Anti-TNF ± thiopurine from diagnosis in high-risk patients (deep ulcers, fistulizing, steroid-dependent, high CRP, extensive disease) → superior mucosal healing and steroid-free remission (SONIC trial: infliximab + azathioprine superior to monotherapy in CD)

**Aminosalicylates (5-ASA):**
- Mesalamine (UC first-line, mild-moderate): Mucosal anti-inflammatory (NF-kB inhibition, prostaglandin modulation); oral + rectal formulations for UC; proctitis treated with suppository only; NOT effective in CD (Cochrane review: no benefit over placebo)
- Sulfasalazine: 5-ASA prodrug; folate supplementation required

**Corticosteroids:**
- Prednisone/methylprednisolone: Rapid induction (40-60 mg/day PO or IV) for moderate-severe flares; NOT maintenance therapy (bone loss, HPA suppression, complications)
- **Budesonide (oral controlled-ileal release, Entocort):** Ileal/right colonic CD induction; 90% first-pass hepatic metabolism → limited systemic effects; 9 mg daily; gentler than prednisone but not for severe disease

**Immunomodulators:**
- **Azathioprine/6-mercaptopurine (6-MP):** Purine antimetabolite → lymphocyte antiproliferation; TPMT/NUDT15 genotyping before initiation (rapid metabolizers → myelosuppression); used as maintenance alone or in combination with anti-TNF (reduces antibody formation to biologic); 3-6 months to full effect
- **Methotrexate (IM/SC, Crohn's only):** Anti-inflammatory + immunomodulatory; second-line immunomodulator if azathioprine intolerant; not used in UC (less evidence)

**Anti-TNF biologics (first-line biologic for moderate-severe IBD):**
- **Infliximab (Remicade, chimeric anti-TNF):** IV infusion; highly effective in CD and UC; mucosal healing ~40% in CD; first biologic approved for fistulizing CD; SONIC trial: infliximab + azathioprine → 57% clinical remission in CD vs. 30% azathioprine alone; scheduled maintenance superior to episodic
- **Adalimumab (Humira, human anti-TNF):** SC biweekly; CLASSIC-I/II in CD; ULTRA in UC; preferred for patients with injection-site preference or infusion reaction to infliximab
- **Certolizumab pegol (Cimzia, PEGylated anti-TNF Fab):** SC; CD (not UC); no Fc → no complement, minimal placental transfer → safe in pregnancy
- **Golimumab (Simponi):** SC monthly; UC only (PURSUIT trial)
- **Anti-TNF monitoring:** Therapeutic drug monitoring (TDM) — trough levels (infliximab ≥5 μg/mL, adalimumab ≥7.5 μg/mL); anti-drug antibodies (ADA) → loss of response; dose optimization or switch based on TDM

**Anti-integrin biologics (gut-selective):**
- **Vedolizumab (Entyvio, anti-alpha-4-beta-7 integrin):** Prevents lymphocyte trafficking to the gut (MAdCAM-1 binding on gut endothelium); approved UC and CD; GEMINI I (UC) and II (CD); gut-selective → fewer systemic infections than anti-TNF; PML not reported (vs. natalizumab, which blocks alpha-4 globally) [^sandborn-2012-vedolizumab]; preferred in elderly, immunocompromised, or post-transplant IBD
- **Ozanimod (sphingosine-1-phosphate modulator):** Retains lymphocytes in lymph nodes → prevents gut trafficking; oral; approved UC; mild side effects (bradycardia at initiation, ophthalmic assessment)

**Anti-IL-12/23 and anti-IL-23:**
- **Ustekinumab (Stelara, anti-IL-12/23 p40 subunit):** IV induction, SC maintenance; approved CD (UNIFI Phase III) and UC (STELARA-UC) [^sands-2019-ustekinumab-uc]; excellent safety; preferred in patients with psoriasis comorbidity (dual indication); ORR ~60% induction
- **Risankizumab (Skyrizi, anti-IL-23 p19):** Selective IL-23 blockade (spares IL-12 → preserves IFN-gamma-mediated immunity); approved CD 2022 and UC 2024; ADVANCE/MOTIVATE (CD), INSPIRE (UC): superior remission rates vs. placebo; also approved for psoriasis and PsA
- **Mirikizumab (Omvoh, anti-IL-23 p19):** Approved UC 2023 (LUCENT-1/2); Crohn's filed

**JAK inhibitors (IBD):**
- **Tofacitinib (Xeljanz, JAK1/3):** Approved UC (OCTAVE I/II); 18.5% remission vs. 8.2% placebo at week 8; effective in anti-TNF-refractory UC; VTE boxed warning limits use in older/high-CV-risk patients
- **Upadacitinib (Rinvoq, JAK1):** Approved UC (2022) and CD (2023); ULTA II (CD): 45.5% remission vs 13.1% placebo at week 12; SELECT UC I/II; superior to adalimumab in UC head-to-head; JAK1 selectivity reduces anemia/cytopenias vs. tofacitinib
- **Filgotinib (Jyseleca, JAK1, EU only):** Approved UC in EU; SELECTION trial

**Surgery:**
- **UC:** Proctocolectomy (total colectomy + rectal excision); curative; options: permanent end ileostomy or J-pouch ileal-anal anastomosis (IPAA, restorative — preferred when feasible); pouchitis (antibiotic/probiotic/biologic)
- **CD:** Resection for obstruction, perforation, fistula, or medically refractory disease; does NOT cure — disease recurs at anastomosis (~50% endoscopic recurrence at 1 year post-resection); post-operative prophylaxis with anti-TNF or immunomodulator recommended

## Connections

- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha is the primary effector cytokine in IBD; mucosal macrophages produce TNF → NF-kB-mediated epithelial apoptosis and barrier disruption; anti-TNF biologics (infliximab, adalimumab) are the backbone of moderate-severe IBD therapy and achieve mucosal healing in ~40% of CD and UC.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — IBD is fundamentally a dysregulated immune response to commensal bacteria in susceptible hosts; dysbiosis (loss of Faecalibacterium prausnitzii and Bacteroidetes) is universal; gut microbiome composition predicts treatment response; FMT induces UC remission in ~30-50% of patients in clinical trials.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — TNF-alpha and IL-13 in IBD disrupt tight junction proteins → increased permeability → bacterial translocation; mucosal healing (endoscopic Mayo 0-1 in UC) is now the primary therapeutic target — associated with sustained remission and reduced surgical risk.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — colonic macrophages shift from tolerogenic (CD33+, IL-10-producing) to pro-inflammatory (TNF-alpha, IL-1beta, IL-23) in IBD; macrophage IL-23 production drives Th17 differentiation; anti-IL-12/23 (ustekinumab, risankizumab) and JAK inhibitors target macrophage-driven intestinal inflammation.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — mucosal neutrophil infiltration in IBD releases calprotectin into the gut lumen; fecal calprotectin >150 μg/g distinguishes IBD from IBS (sensitivity >80%); FC >250 correlates with active endoscopy; serial FC monitors biologic response and predicts relapse.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — H4R on mucosal mast cells and Tregs modulates gut inflammation; enterochromaffin-like cells secrete histamine → parietal HCl; H1R/H4R amplify epithelial cytokine release; H4R blockade reduces experimental colitis; histamine levels correlate with IBD disease activity.
- `treated-by` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — approved for Crohn's disease (CHARM trial: 36% vs 12% 52-week remission) and ulcerative colitis (ULTRA-2: 16.5% vs 9.3%); blocks mucosal macrophage TNFα → reduces epithelial apoptosis; perianal fistula closure benefit; induction and maintenance approved.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is elevated in IBD mucosa but anti-IL-17A therapy (secukinumab) paradoxically worsens IBD in AS/PsA patients; gut epithelial IL-17A may protect barrier integrity; this dual role distinguishes mucosal IL-17A function from systemic Th17 pathogenicity.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is the core target in inflammatory bowel disease: ulcerative colitis causes continuous mucosal inflammation from the rectum proximally while Crohn's can produce patchy transmural colitis; this drives bloody diarrhea, urgency and colorectal-cancer risk.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Long-standing colonic IBD is a major risk factor for colorectal cancer: chronic inflammation drives a dysplasia-carcinoma sequence distinct from sporadic CRC, so patients with extensive UC or Crohn's colitis need surveillance colonoscopy with biopsies after ~8-10 years.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — IBD and ankylosing spondylitis overlap on the spondyloarthritis spectrum: they share IL-23/Th17 biology and HLA-B27 background, axial arthritis is a common extraintestinal feature of IBD, and TNF and IL-23 blockers treat both—though IL-17 inhibitors can paradoxically flare IBD.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — IBD and psoriasis are both IL-23/Th17-driven immune diseases that often co-occur and share biologics: ustekinumab (anti-IL-12/23) treats both—yet anti-TNF agents for IBD can paradoxically trigger psoriasis, revealing how intertwined these cytokine circuits are.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — IBD and rheumatoid arthritis are distinct immune-mediated diseases united by anti-TNF therapy: TNF blockers transformed both, yet RA is an autoantibody-driven symmetric synovitis while IBD is barrier-driven gut inflammation—one cytokine, very different target tissues.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — IBD reflects a breakdown of intestinal tolerance maintained by regulatory T cells: Tregs and their IL-10 restrain responses to gut microbes, and losing this brake (as with IL-10-receptor mutations) unleashes chronic inflammation—restoring Treg function is a goal.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells drive the inflammation of IBD: Th1/Th17 responses dominate Crohn's while a modified Th2 response marks ulcerative colitis, and these effector T cells attacking the gut wall are why immunosuppressants and biologics blocking their cytokines work.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Crohn's disease commonly strikes the small intestine: transmural inflammation of the terminal ileum causes strictures, fistulas and B12/bile-acid malabsorption—distinguishing Crohn's from ulcerative colitis, which is limited to the colon's mucosa.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 helps drive Crohn's disease: this cytokine, sharing a subunit with IL-23, pushes the Th1 response that inflames the gut wall, which is why ustekinumab—blocking the shared p40 subunit of IL-12 and IL-23—is an effective IBD therapy.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibitors are an oral option in IBD: several cytokines driving gut inflammation signal through the JAK-STAT pathway, so tofacitinib and upadacitinib treat ulcerative colitis when antibody biologics fail—a small-molecule alternative to anti-TNF.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — IBD is the prototypical chronic inflammatory disease of the digestive system: Crohn's can inflame anywhere from mouth to anus while ulcerative colitis is confined to the colon, so it reshapes gut structure and function and predisposes to bowel cancer.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — IBD reaches beyond the gut to the skin: erythema nodosum and pyoderma gangrenosum are classic cutaneous manifestations that track (or sometimes precede) bowel activity, so the integumentary system is a window onto this systemic immune disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils drive tissue damage in active IBD: recruited into the mucosa, they form the crypt abscesses that histologically define a flare and release proteases and oxidants that ulcerate the gut wall—so blunting neutrophil influx is part of controlling disease.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and IBD interact both ways: deficiency is common with intestinal inflammation and malabsorption, and low vitamin D—an immune modulator supporting gut-barrier and regulatory T-cell function—is linked to more active disease, so levels are checked and repleted.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — IBD's most important liver tie is primary sclerosing cholangitis: this progressive bile-duct scarring occurs mostly with ulcerative colitis, raises the risk of cholangiocarcinoma and colorectal cancer, and runs an independent course unaffected by bowel treatment.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — IBD, especially Crohn's, traces to faulty autophagy: risk genes like ATG16L1 cripple the cellular self-cleaning that clears gut bacteria and keeps Paneth cells working, so impaired autophagy lets the microbiome provoke chronic intestinal inflammation.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells set the thermostat of IBD: by sampling gut microbes and deciding whether to trigger tolerance or attack, these cells tip the Th17-versus-regulatory-T-cell balance that determines whether the intestine stays calm or inflames.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B-cell antibodies help classify IBD: serologic markers—ASCA antibodies leaning toward Crohn's and pANCA toward ulcerative colitis—reflect the B-cell response to gut antigens and help distinguish the two forms when biopsies are ambiguous.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — IBD is a leading cause of iron-deficiency anemia: chronic gut bleeding and inflammation that blocks iron absorption leave many patients anemic, so iron status is monitored and often repleted intravenously when the gut can't take it up.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — IBD spills out onto the skin: erythema nodosum and pyoderma gangrenosum are extraintestinal manifestations that can flare with bowel activity, so skin lesions are a window onto the systemic reach of the gut disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the IBD gut: their numbers rise in the diseased mucosa, where their histamine and mediators drive the pain, diarrhea and barrier breakdown, linking the gut's immune-nerve crosstalk to symptoms.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — IBD inflames the eyes: uveitis and episcleritis are extraintestinal manifestations that can flare with bowel activity, so red, painful eyes in an IBD patient signal active systemic disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Crohn's disease scars the bowel into strictures: chronic transmural inflammation drives fibrosis of the gut wall, narrowing it until food can't pass—the fibrostenotic complication that often needs surgery.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Severe colitis bleeds away potassium: heavy diarrhea flushes potassium from the body, and the resulting hypokalemia can worsen gut paralysis and precipitate toxic megacolon in acute attacks.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — IBD is mapped by light and imaging: colonoscopy inspects the mucosa directly, while CT and MR enterography photons reveal small-bowel inflammation, strictures and abscesses beyond the scope's reach.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — IBD depletes zinc: chronic diarrhea and malabsorption lower it, contributing to the poor healing, skin rashes and impaired immunity that complicate the disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — IBD and its drugs strain the marrow: chronic inflammation and the thiopurines used to treat it can suppress blood-cell production, so counts are watched throughout therapy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy distinguishes IBD's two forms: Crohn's burrows transmurally with granulomas and fissures, while ulcerative colitis stays mucosal with crypt abscesses — and both show the disturbed Paneth cells and autophagy behind the barrier failure.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — IBD reaches the kidney by several routes: fat malabsorption drives calcium-oxalate stones, chronic inflammation can deposit AA amyloid, and the drugs used to treat it add their own nephrotoxic risk.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Chronic diarrhea flushes out magnesium: ongoing intestinal losses in active IBD deplete the mineral along with potassium and zinc, a deficiency that adds to the fatigue and cramping of a flare.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — The colon's fuel comes from fermented fiber: gut bacteria turn dietary fiber into butyrate that nourishes colonocytes and calms inflammation, so a depleted fiber-butyrate axis is implicated in IBD and exclusive enteral nutrition can induce remission.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia is IBD's most common complication: chronic gut bleeding plus inflammation that blocks iron use leaves erythrocytes small and scarce, a mixed iron-deficiency and anemia-of-chronic-disease that drives much of the fatigue patients feel.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — The pancreas is caught both ways: IBD itself raises the risk of acute and autoimmune pancreatitis, and the thiopurine drugs used to treat it are a classic cause of drug-induced pancreatitis that forces a change of therapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Active IBD thickens the blood: the systemic inflammation of a flare drives a hypercoagulable state, so deep-vein thrombosis and pulmonary embolism are markedly more common — which is why hospitalized patients get clot prophylaxis even amid bloody diarrhea.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — IBD erodes the skeleton: chronic inflammation, malabsorption of calcium and vitamin D, and repeated steroid courses thin the bones, making osteoporosis and fragility fractures a common long-term complication needing bone monitoring.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — In Crohn's the wall scars shut: chronic transmural inflammation activates fibroblasts to lay down collagen, and the resulting fibrosis stiffens the bowel into the strictures and obstruction that often demand surgery.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — A specific microbe is implicated: adherent-invasive E. coli colonize the Crohn's mucosa, invade epithelium, and survive inside macrophages, one of the clearest examples of a gut bacterium tipping a susceptible host into chronic intestinal inflammation.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the master switch behind the flare: this transcription factor, fired by microbial and cytokine signals in the gut wall, turns on the TNF, IL-6 and chemokine genes that sustain IBD inflammation — the hub many therapies act upstream of.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — The inflamed mucosa fills with antibody factories: expanded plasma cells secrete IgG and IgA into the bowel wall, and in ulcerative colitis autoantibodies and this B-lineage response form part of the tissue damage alongside the T-cell-driven inflammation.
- `connects-to` → **[Clostridioides difficile](../../../02-pathogen/02-bacteria/clostridioides-difficile/README.md)** — C. difficile both complicates and mimics IBD: the disrupted microbiome and immunosuppression of IBD raise C. diff risk, and superimposed infection drives flares and toxic megacolon — so stool toxin testing is routine when a patient worsens.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Anemia is IBD's commonest extraintestinal complication: chronic gut blood loss plus the iron-sequestering anemia of inflammation drains hemoglobin, so iron status is tracked and intravenous iron often needed.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The inflammasome stokes the gut wall: microbial breach of the epithelium activates NLRP3 in mucosal macrophages, releasing IL-1β that amplifies the inflammation — a node studied to dampen IBD beyond TNF blockade.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 and IL-23 drive the gut through STAT3: STAT3 signaling sustains the pathogenic Th17 response and epithelial changes of IBD, the JAK-STAT axis that tofacitinib and other JAK inhibitors interrupt.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe colitis and immunosuppression invite sepsis: toxic megacolon and bowel perforation breach the gut barrier, and the biologics and steroids used to control IBD raise the risk of serious infection and sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Inflammation blunts the marrow beyond blood loss: the chronic cytokines of IBD raise hepcidin and suppress erythropoiesis, an anemia of chronic disease that compounds the iron deficiency from gut bleeding.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Its TNF blockers can wake latent TB: the anti-TNF biologics central to IBD treatment disable the granuloma containing Mycobacterium tuberculosis, so latent-TB screening and treatment precede therapy to prevent reactivation.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Combination immunosuppression opens the lung: thiopurines, steroids and biologics together in IBD can deplete T-cell defenses enough to risk Pneumocystis pneumonia, weighed in high-intensity regimens.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Through PSC it threatens the bile ducts: IBD — especially ulcerative colitis — is tightly linked to primary sclerosing cholangitis, whose chronic biliary inflammation carries a markedly raised risk of cholangiocarcinoma.
- `connects-to` → **[Hepatitis B virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Its biologics can reactivate hepatitis B: the anti-TNF and other immunosuppressive therapies for IBD can reawaken a dormant hepatitis B virus, so screening and antiviral prophylaxis precede treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Combined immunosuppression opens the lung to mold: corticosteroids stacked on biologics or JAK inhibitors for IBD deeply blunt immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Gut inflammation and chronic disease weigh on mood: the relapsing course, urgency and gut-brain inflammatory signaling of IBD give it markedly elevated rates of depression.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunosuppression reawakens shingles: the thiopurines, anti-TNF and especially JAK inhibitors used for IBD blunt antiviral immunity and notably raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Crohn's reaches the urinary tract: fat malabsorption causes enteric hyperoxaluria with oxalate kidney stones, and bowel inflammation can form enterovesical fistulas and rarely renal amyloidosis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An unpredictable, urgent disease breeds worry: the relapsing flares, faecal urgency and gut-brain signalling of IBD foster chronic health anxiety alongside its well-documented depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is an immune-mediated disease at its core: dysregulated mucosal immunity with the IL-23/Th17 axis and innate immune defects drives the gut inflammation that biologic therapies target.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It inflames joints beyond the gut: enteropathic peripheral arthritis and sacroiliitis are common extraintestinal manifestations, alongside the steroid- and inflammation-driven bone loss of IBD.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can reach the nerves: terminal-ileal Crohn's causes vitamin B12 deficiency with neuropathy, and IBD raises the risk of cerebral venous thrombosis and peripheral neuropathy.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic gut inflammation reaches the vessels: IBD raises the risk of venous thromboembolism and, through systemic inflammation, of cardiovascular disease and rare pericarditis.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It touches fertility and pregnancy: active IBD and pelvic surgery can impair fertility, sulfasalazine causes reversible male infertility, and flares complicate pregnancy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its drugs raise lymphoma risk: thiopurines and anti-TNF therapy for IBD slightly increase the risk of lymphoma, including the rare hepatosplenic T-cell lymphoma in young men.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids tame the flare: corticosteroids induce remission in acute inflammatory bowel disease flares, but their toxicity makes them unsuitable for maintenance, driving the use of steroid-sparing biologics.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Shared immune dysregulation: inflammatory bowel disease and atopic dermatitis co-occur more than expected and share cytokine pathways, with JAK inhibitors now treating both.
- `connects-to` → **[Mycobacterium tuberculosis](../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)** — TB shadows its treatment and mimics it: latent tuberculosis must be excluded before anti-TNF therapy, which can reactivate it, and intestinal TB closely mimics Crohn's disease.
- `connects-to` → **[Peyer's Patches](../../05-tissue/peyers-patches/README.md)** — Crohn's begins over the gut's lymphoid follicles: its earliest lesions are aphthous ulcers of the epithelium covering Peyer's patches, where defective handling of bacteria by M cells and macrophages ignites the transmural inflammation of Crohn's disease.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — The gut-kidney axis of mucosal IgA: inflammatory bowel disease disturbs intestinal IgA production and barrier integrity, and IgA nephropathy is the commonest glomerulonephritis complicating IBD—mucosal immune dysregulation surfacing in the kidney.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A cautionary overlap of autoimmunity: TNF inhibitors that treat inflammatory bowel disease can unmask or worsen demyelinating disease, so multiple sclerosis is a contraindication—evidence that blocking one cytokine helps the gut yet harms the central nervous system.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Primary sclerosing cholangitis: IBD—especially ulcerative colitis—associates with PSC, where bile-duct inflammation and fibrosis injure the hepatic lobule, progressing to cirrhosis and raising cholangiocarcinoma risk.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Enteropathic spondyloarthritis: IBD shares the IL-23/Th17 axis with psoriatic arthritis and ankylosing spondylitis, the seronegative spondyloarthropathies that frequently co-occur with bowel inflammation.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A prothrombotic, atherogenic state: active IBD inflammation raises the risk of venous and arterial thrombosis and accelerates atherosclerosis of the arterial wall, a cardiovascular hazard beyond the gut.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Autoimmune clustering: inflammatory bowel disease and type 1 diabetes co-occur more than chance through shared HLA and immune-susceptibility loci, part of the broader tendency of organ-specific autoimmune diseases to aggregate.
- `connects-to` → **[NASH](../nash/README.md)** — The liver comorbidity: non-alcoholic steatohepatitis is the commonest liver disease in IBD, driven by chronic inflammation, corticosteroids and metabolic disturbance rather than the bile-duct disease of associated cholangitis.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Aberrant mucosal antibody factories: chronic IBD spawns ectopic lymphoid follicles with active germinal centres in the inflamed gut wall, fuelling the local plasma-cell and autoantibody responses that sustain the disease.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 inflammation: IL-6 signalling through STAT3 sustains mucosal inflammation in IBD and renders lamina propria T cells resistant to apoptosis, perpetuating the disease.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Fibrosis and stricturing: TGF-β drives the intestinal fibrosis behind the strictures of Crohn's disease, with the SMAD7 antagonist concept aimed at restoring its anti-inflammatory signalling.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Creeping fat: hypertrophied mesenteric adipose ('creeping fat') wrapping inflamed Crohn's bowel secretes leptin and other adipokines that modulate local gut inflammation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 transmural inflammation: IFN-γ from Th1 cells drives the transmural, granulomatous inflammation characteristic of Crohn's disease, damaging the intestinal wall.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome injury: IL-1β from inflammasome-activated macrophages amplifies the mucosal inflammation of IBD, with the IL-1/IL-1β axis an emerging therapeutic target.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into the inflamed gut wall in IBD, replenishing the macrophages that sustain chronic intestinal inflammation.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — HLA genetic risk: MHC class II HLA loci are major genetic associations of IBD, presenting gut microbial and self antigens to the CD4 T cells that drive the chronic mucosal immune response.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Stricturing fibrosis: PDGF drives the intestinal fibroblast and myofibroblast proliferation behind the fibrotic strictures that complicate Crohn's disease and require surgery.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal antibody barrier: dysregulated secretory IgA at the gut surface alters the microbiota and barrier homeostasis whose breakdown underlies the aberrant immune response of IBD.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 and related innate receptors sensing a dysbiotic microbiota across a breached epithelial barrier drive the loss of immune tolerance central to the gene-environment-microbiome model of inflammatory bowel disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — IL-13 from natural killer T and innate lymphoid cells damages the epithelial barrier and impairs tight junctions in ulcerative colitis, the type-2-skewed cytokine arm that distinguishes UC from the Th1/Th17-driven Crohn's disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic and microbial DNA activating cGAS-STING in gut epithelium and myeloid cells amplifies intestinal inflammation, and STING gain-of-function causes an autoinflammatory enteropathy that overlaps with IBD.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor—systemic prednisone or gut-targeted budesonide—induce remission of IBD flares, though their toxicity and failure to heal mucosa long-term make them bridging rather than maintenance therapy.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Chronic transmural inflammation in Crohn's disease drives myofibroblast collagen deposition that forms the fibrotic strictures causing bowel obstruction, a complication that immunosuppression does not reverse and that often needs surgery.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from damaged intestinal epithelium acts as an alarmin on innate lymphoid cells and mast cells, an upstream amplifier of the mucosal inflammation that has both pro-inflammatory and reparative roles in IBD.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR (TLR4 mapped) and IL-1-receptor signaling through MyD88 to NF-κB (mapped) transduces the dysregulated response to gut microbiota that drives the mucosal inflammation of IBD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — IL-2 sustains the regulatory T cells that maintain mucosal tolerance, and defective IL-2/Treg signaling contributes to the loss of tolerance to gut antigens in IBD.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — E-cadherin junctions seal the intestinal epithelium, and the barrier breakdown that lets luminal microbes contact the mucosa is a central permissive step in IBD pathogenesis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling regulates Paneth-cell function and the autophagy (already mapped) that clears intracellular bacteria, a pathway whose Crohn's-associated defects impair mucosal antimicrobial defense.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense protects the intestinal epithelium from the oxidative stress of chronic mucosal inflammation in inflammatory bowel disease.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of intestinal epithelial cells contributes to the barrier breakdown that perpetuates the inflammation of inflammatory bowel disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) regulates intestinal-epithelial survival and restitution, processes disrupted in the barrier failure of inflammatory bowel disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the mucosal macrophage and epithelial inflammatory responses of inflammatory bowel disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives both regulatory-T-cell tolerance and the intestinal fibrosis (strictures) of inflammatory bowel disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling drives the Th1 epithelial injury characteristic of the mucosal inflammation of inflammatory bowel disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling in intestinal epithelium and immune cells transduces the cytokine stimuli that sustain the inflammation of inflammatory bowel disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) shapes the immune-cell activation and epithelial responses of inflammatory bowel disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the intestinal epithelial oxidative-stress defense and the T-cell programs implicated in inflammatory bowel disease.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic inflamed mucosa shapes the barrier and inflammatory responses of inflammatory bowel disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven mucosal inflammation of inflammatory bowel disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the intestinal-epithelial and immune-cell responses of inflammatory bowel disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic T-cell activity contributes to the epithelial injury of inflammatory bowel disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the immune-cell activation and epithelial-barrier signaling of inflammatory bowel disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the gut mucosa contributes to the intestinal inflammation of inflammatory bowel disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the mucosal immune responses of inflammatory bowel disease.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of ciclosporin and tacrolimus, participates in the T-cell activation of inflammatory bowel disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking into the inflamed intestinal mucosa of inflammatory bowel disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the mucosal innate immune responses of inflammatory bowel disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling provides immunoregulatory modulation of the mucosal inflammation of inflammatory bowel disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the intestinal-epithelial and immune gene programs of inflammatory bowel disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage-driven mucosal inflammation and fibrosis of inflammatory bowel disease.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the mucosal immune dysregulation of inflammatory bowel disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: anaemia is the commonest systemic complication of inflammatory bowel disease, from chronic gut blood loss (iron already mapped) and inflammation-driven suppression of erythropoiesis, lowering haemoglobin and worsening fatigue.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 mucosal inflammation: IL-4 and the Th2 axis contribute to the mucosal immune response of ulcerative colitis, complementing the Th17/IL-23 and Th1 pathways (already mapped) that dominate Crohn's disease.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Dietary modulation: omega-3 fatty acids give rise to pro-resolving and anti-inflammatory mediators, and dietary fat composition influences the mucosal inflammation of inflammatory bowel disease, one of the diet-related factors shaping disease activity.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Mucosal eicosanoids: prostaglandins both protect and inflame the gut mucosa, so NSAIDs that block their synthesis can precipitate inflammatory bowel disease flares, while their modulation is part of the mucosal inflammatory response.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Gut motility and secretion: enterochromaffin-cell serotonin, elevated in the inflamed mucosa, drives the diarrhoea, altered motility and visceral hypersensitivity that contribute to the symptoms of inflammatory bowel disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative mucosal injury: reactive oxygen species from the infiltrating neutrophils (already mapped) and xanthine oxidase damage the epithelial barrier in inflammatory bowel disease, and this oxidative stress (NRF2 already mapped) perpetuates the inflammation.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Mucosal iNOS: inducible nitric oxide synthase is upregulated in the inflamed gut of inflammatory bowel disease, and the resulting nitric oxide, with the oxidative stress (already mapped), contributes to the epithelial injury and altered blood flow.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile-acid malabsorption: ileal Crohn's disease and resection disrupt the enterohepatic circulation of the bile acids derived from cholesterol, causing bile-acid diarrhoea and disturbed lipid handling, part of the malabsorption of inflammatory bowel disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Metabolic bone disease: the malabsorption, chronic inflammation and steroid therapy of inflammatory bowel disease deplete calcium and vitamin D, causing the osteoporosis and metabolic bone disease that complicate the illness.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the IL-6-driven (already mapped) hepcidin sequesters iron and, with the iron-deficiency (already mapped) from blood loss, causes the mixed anaemia that is the commonest systemic complication of inflammatory bowel disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Mucosal angiogenesis: VEGF drives the increased microvascular density and angiogenesis of the inflamed gut mucosa, part of the vascular component of the chronic inflammation of inflammatory bowel disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Diarrhoeal losses: the profuse diarrhoea of active inflammatory bowel disease depletes sodium and water, causing the volume depletion and electrolyte disturbance (calcium already mapped) that complicate flares.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Creeping-fat adipokine: adiponectin, with leptin (already mapped), is an adipokine of the 'creeping fat' — the mesenteric adipose that wraps the inflamed Crohn's bowel — a distinctive feature of inflammatory bowel disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory creeping-fat adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the creeping fat and the systemic inflammation (IL-6 already mapped) of inflammatory bowel disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Diarrhoeal magnesium loss: the profuse diarrhoea of active inflammatory bowel disease depletes magnesium (with sodium already mapped), contributing to the electrolyte disturbance of flares.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the eosinophils prominent in the ulcerative-colitis mucosa of inflammatory bowel disease.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — IBD bone loss: the chronic inflammation, the malabsorption and the corticosteroid (glucocorticoid-receptor already mapped) use cause the osteoporosis and the low bone density of the cortical bone in inflammatory bowel disease.
- `connects-to` → **[GVHD](../gvhd/README.md)** — Gut-GVHD parallel: the gastrointestinal graft-versus-host disease resembles inflammatory bowel disease histologically and mechanistically, both driven by the microbiome (TLR4 already mapped)-immune dysregulation of the gut.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Enteric neuroimmune: substance P of the enteric nervous system drives the neurogenic inflammation and the visceral hypersensitivity/pain of inflammatory bowel disease.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium status: the selenium selenoprotein antioxidant defence modulates the gut inflammation, and its deficiency (the malabsorption) is common and immunomodulatory in inflammatory bowel disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension present in the UC-leaning end of inflammatory bowel disease.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Epithelial cytotoxicity: the cytotoxic T cells (perforin already mapped), including the tissue-resident memory subset, contribute to the epithelial injury of inflammatory bowel disease.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate lymphoid arm: the NK cells and the innate lymphoid cells (perforin already mapped) are part of the dysregulated mucosal innate immunity of inflammatory bowel disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in mucosa: the complement C5 and its C5a (with C3 already mapped) contribute to the neutrophil (already mapped) recruitment and the mucosal inflammation of inflammatory bowel disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the inflamed mucosa of inflammatory bowel disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped), and its dysregulation on the injured epithelium amplifies the mucosal inflammation of inflammatory bowel disease.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — IBD iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the iron-deficiency anaemia that is the commonest systemic complication of inflammatory bowel disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial alarmin: TSLP released by the inflamed intestinal epithelium (already mapped) drives dendritic-cell (already mapped) and mast-cell (already mapped) priming that sustains the Th2 (IL-4, IL-5, IL-13 already mapped) and Th9 arms of mucosal immunity in IBD.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin gut pain and permeability: bradykinin, via B1/B2 receptors on intestinal epithelial cells (already mapped) and mast cells (already mapped), amplifies gut pain, mucosal permeability and the NF-kB (already mapped) inflammatory cascade of IBD.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement and kinin regulation: C1-INH controls the classical complement pathway (C3, C5 and C5aR1 already mapped) and the bradykinin (already mapped) kinin-kallikrein axis; deficiency worsens mucosal oedema and complement-mediated epithelial (already mapped) injury in IBD.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia-of-IBD therapy: erythropoietin, responding to the anaemia of chronic disease (already mapped) and iron-deficiency anaemia (already mapped) complicating IBD, stimulates erythrocyte (already mapped) production and can suppress mucosal NF-κB (already mapped) inflammation.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Intestinal fibrosis mediator: periostin, from intestinal fibroblasts (fibrosis already mapped) under TGF-β (already mapped) and IL-13 (already mapped) stimulation, promotes subepithelial collagen (already mapped) deposition and the stricturing phenotype of Crohn's disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Enteric melatonin: melatonin produced by enterochromaffin cells of the gut epithelium (already mapped) activates MT1/MT2 receptors on mast cells (already mapped) and immune cells, attenuating the NF-κB (already mapped) and NLRP3 (already mapped) mucosal inflammation of IBD.

[^ng-2017-ibd-epidemiology]: Ng SC, Shi HY, Hamidi N, et al. Worldwide incidence and prevalence of inflammatory bowel disease in the 21st century: a systematic review of population-based studies. *Lancet.* 2018;390(10114):2769-2778. [doi:10.1016/S0140-6736(17)32448-0](https://doi.org/10.1016/S0140-6736(17)32448-0) · [PubMed 29050646](https://pubmed.ncbi.nlm.nih.gov/29050646/)
[^sandborn-2012-vedolizumab]: Feagan BG, Rutgeerts P, Sands BE, et al. Vedolizumab as induction and maintenance therapy for ulcerative colitis. *N Engl J Med.* 2013;369(8):699-710. [doi:10.1056/NEJMoa1215734](https://doi.org/10.1056/NEJMoa1215734) · [PubMed 23964932](https://pubmed.ncbi.nlm.nih.gov/23964932/)
[^sands-2019-ustekinumab-uc]: Sands BE, Sandborn WJ, Panaccione R, et al. Ustekinumab as Induction and Maintenance Therapy for Ulcerative Colitis. *N Engl J Med.* 2019;381(13):1201-1214. [doi:10.1056/NEJMoa1900750](https://doi.org/10.1056/NEJMoa1900750) · [PubMed 31553834](https://pubmed.ncbi.nlm.nih.gov/31553834/)
