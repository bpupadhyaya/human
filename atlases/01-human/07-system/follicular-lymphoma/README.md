---
schema: human-scale-entry/v1
id: follicular-lymphoma
name: Follicular Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Follicular lymphoma is the most common indolent B-cell lymphoma; t(14;18) BCL-2-IGH in ~85% drives apoptosis resistance; EZH2 Y641 in ~25% silences tumor suppressors. Rituximab+bendamustine or R-CHOP are standard; tazemetostat is approved for EZH2-mutant relapsed/refractory FL."
aliases: ["follicular lymphoma", "FL", "indolent NHL", "t(14;18) lymphoma", "BCL-2-IGH", "follicle center lymphoma", "grade 1-2 follicular lymphoma"]
sources:
  - id: marcus-2017-gallium
    type: peer-reviewed
    cite: "Marcus R, Davies A, Ando K, et al. Obinutuzumab for the first-line treatment of follicular lymphoma. N Engl J Med. 2017;377(14):1331-1344."
    doi: "10.1056/NEJMoa1614598"
    pmid: "28976863"
    url: "https://doi.org/10.1056/NEJMoa1614598"
  - id: morschhauser-2020-tazemetostat
    type: peer-reviewed
    cite: "Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003): a multicentre, open-label, single-arm, phase 2 trial. Lancet Oncol. 2020;21(11):1433-1442."
    doi: "10.1016/S1470-2045(20)30441-1"
    pmid: "33035457"
    url: "https://doi.org/10.1016/S1470-2045(20)30441-1"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "t(14;18) BCL-2-IGH translocation in ~85-90% of FL → BCL-2 overexpression in GC B-cells → apoptosis resistance; BCL-2 is the defining molecular feature of FL; venetoclax (BCL-2 inhibitor) active in relapsed FL; BCL-2 overexpression does not predict venetoclax response in FL."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20 mAb) is the backbone of FL therapy; R-CHOP and R-bendamustine are first-line options; obinutuzumab (glycoengineered anti-CD20) + chemotherapy (GALLIUM trial) improved PFS vs. rituximab; anti-CD20 maintenance improves PFS after induction."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Histologic transformation of FL to DLBCL occurs in ~30% at 10 years; POD24 (progression within 24 months) is associated with MYC acquisition and poor prognosis; double-hit lymphoma (MYC+BCL-2 rearrangement) arising from FL is treated as aggressive lymphoma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "CREBBP mutations in ~60% and EP300 mutations in ~15% of FL → loss of HAT activity → decreased H3K18/K27 acetylation; CREBBP/EZH2 co-mutations in ~30% of FL → dual epigenetic reprogramming; EZH2 silences TNFAIP3/A20 (NF-κB inhibitor) → enhanced NF-κB in FL cells."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2 Y641F/N gain-of-function in ~25% of FL → H3K27me3 → silences tumor suppressor and differentiation genes; tazemetostat (EZH2i) approved for R/R EZH2-mutant FL (ORR 69%) and EZH2-WT FL (ORR 35%); CREBBP co-mutation in ~30% creates dual epigenetic dysregulation."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Histologic transformation from FL to DLBCL occurs in ~30% at 10 years; requires MYC rearrangement, TP53 mutation, or CDKN2A loss on top of BCL-2-IGH; transformed FL is treated as de novo DLBCL; CAR-T (axi-cel) or auto-SCT preferred after induction."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "FL tumor microenvironment is immune-rich (Tfh, Tregs, FDC); mosunetuzumab (CD20×CD3 bispecific, approved R/R FL) redirects T-cells to kill FL B-cells; PD-1 blockade + rituximab has modest single-agent activity; lenalidomide → NK-cell ADCC and immune reprogramming in R/R FL."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Follicular and mantle cell lymphoma are both translocation-defined B-cell NHLs but opposites: FL (t(14;18), BCL-2) is indolent and apoptosis-resistant, MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive — the two classic overexpression translocation lymphomas."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Follicular lymphoma arises from germinal-center B cells frozen mid-maturation: t(14;18) places BCL-2 under the immunoglobulin enhancer, so cells that should die during affinity maturation survive, accumulating as CD10+/BCL6+ clonal follicles that mimic the germinal center."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Follicular lymphoma is a disseminated nodal disease that often involves the spleen and bone marrow at diagnosis (stage III-IV in ~80%); splenic and marrow involvement rarely changes the indolent watch-and-wait or rituximab-based management, since FL is treatable but not curable."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Follicular lymphoma and CLL/SLL are the commonest indolent B-cell lymphomas: both slow-growing, manageable-but-incurable, and prone to transformation into aggressive DLBCL (Richter for CLL); they differ in origin—germinal-center FL with t(14;18)/BCL2 vs CD5+ post-GC CLL."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Follicular lymphoma is a disease of the lymphatic system: malignant germinal-center B cells expand lymph-node follicles, producing the waxing-and-waning painless lymphadenopathy that is its hallmark, with spread to spleen and marrow; many cases are watched while asymptomatic."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Follicular lymphoma arises directly from the germinal center: a malignancy of follicle-center B cells frozen mid-reaction that recapitulates follicular architecture, and its founding t(14;18) drives constitutive BCL2 to block the apoptosis that normally prunes these cells."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Follicular and Hodgkin lymphomas both arise from germinal-center B cells but behave oppositely: follicular is indolent, BCL2-driven and incurable, smoldering for years, while Hodgkin's Reed-Sternberg tumor is aggressive yet highly curable—indolence versus curability."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Follicular and Burkitt lymphomas are germinal-center B-cell tumors at opposite tempos: follicular is slow, BCL2 [t(14;18)]-driven and incurable, while Burkitt is the fastest-growing human tumor, MYC [t(8;14)]-driven yet curable—each named by its translocation."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Follicular lymphoma and multiple myeloma are both incurable B-lineage malignancies at different maturation stages: FL is a CD20+ germinal-center B-cell tumor, myeloma a marrow plasma-cell cancer secreting monoclonal protein—both relapse and remit over years."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Follicular lymphoma depends on follicular helper T cells in its microenvironment: the malignant B cells need Tfh signals and a supportive niche to survive, so FL is as much a disease of the microenvironment as of the B cell—explaining its indolent, relapsing course."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Follicular lymphoma is a germinal-center B cell blocked from becoming a plasma cell: the t(14;18) BCL2 translocation lets it resist apoptosis and accumulate instead of maturing into antibody-secreting cells—an indolent buildup unlike high-grade lymphomas."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Follicular lymphoma's behavior is shaped by immune surveillance: the microenvironment can restrain or enable the tumor, and FL can spontaneously regress or transform—so immune-modulating therapies (rituximab, lenalidomide) are central to its largely incurable course."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Follicular lymphoma usually involves the bone marrow at diagnosis: the indolent clone seeds marrow in a paratrabecular pattern, so it is typically advanced-stage yet slow-growing—curative local therapy is rarely possible, but it can be watched or controlled for years."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy can cure the rare localized follicular lymphoma: low-dose photon radiation to a single involved site is potentially curative in stage I disease, a notable exception in a lymphoma that is otherwise incurable but indolent and managed over many years."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Follicular lymphoma can transform and reach the nervous system: histologic transformation to aggressive DLBCL—and rarely CNS involvement—marks a turn for the worse in this usually indolent disease, shifting management from watchful waiting to intensive therapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Follicular lymphoma is built on follicular dendritic cells: these stromal cells form the germinal-center meshwork the malignant B cells depend on for survival signals, so the tumor recreates a follicle—its microenvironment shaping when indolent disease turns aggressive."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Follicular lymphoma now yields to T-cell therapies: CD19 CAR-T cells and CD20×CD3 bispecifics (mosunetuzumab) redirect cytotoxic T cells against the B-cell clone, giving durable remissions in this otherwise relapsing, incurable indolent lymphoma."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Follicular lymphoma is usually widespread at diagnosis, infiltrating the liver: indolent but disseminated, it commonly involves liver, spleen, and marrow by the time it is found—so it is staged as advanced yet often watched rather than treated."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Follicular lymphoma can be hit through the PI3K-mTOR pathway: this survival signaling is active in the lymphoma, so PI3K inhibitors (idelalisib, copanlisib) that feed into mTOR are approved options for relapsed disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Follicular lymphoma lives or dies by its microenvironment, especially regulatory T cells: the mix of Tregs and other immune cells around the tumor follicles predicts how indolent or aggressive the lymphoma will be, more than the tumor cells alone."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Rituximab clears follicular lymphoma largely through NK cells: the anti-CD20 antibody coats the B cells and natural killer cells destroy them by antibody-dependent killing, so NK function shapes how well this mainstay therapy works."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages predict outcome in follicular lymphoma: the number of lymphoma-associated macrophages in the tumor tracks with prognosis, and these cells both support the malignant B cells and mediate the killing when rituximab is given."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Follicular lymphoma leans on its vascular niche via VEGF: the indolent tumor recruits new vessels and a supportive microenvironment in the lymph node, with VEGF-driven angiogenesis sustaining the slow-growing B-cell clone."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "B-cell receptor signaling keeps follicular lymphoma alive through calcium: tonic receptor firing drives a calcium flux that promotes survival, which is why BTK and PI3K inhibitors that interrupt this pathway have a role in treatment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Follicular lymphoma quietly drains iron: marrow infiltration and chronic disease suppress red-cell production and sequester iron, so anemia often accompanies this slow-growing lymphoma."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Follicular lymphoma has a gut form: duodenal-type follicular lymphoma arises in the small intestine as an indolent, often localized disease found incidentally on endoscopy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Follicular lymphoma depends on endothelial cells: VEGF from the tumor and its niche recruits these vessel-lining cells to build the vasculature that sustains the slow-growing clone in the lymph node."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "When follicular lymphoma transforms to aggressive DLBCL and is treated, rapid cell death can trigger tumor lysis, spilling phosphate and potassium into the blood as a metabolic emergency."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Follicular lymphoma has a skin form: primary cutaneous follicle-center lymphoma appears as slow-growing nodules on the head and trunk, an indolent cousin of the nodal disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Follicular lymphoma leans on its niche: T-follicular-helper cells feed the malignant B cells signals like IL-4 and CD40L, so the tumor depends on a supportive microenvironment, not its mutations alone."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows follicular lymphoma's small cleaved cell: the centrocyte, with its notched, angular nucleus, recapitulates the germinal-center cell it came from, packed into nodular follicles by the BCL2 that blocks its death."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Follicular lymphoma can settle in the eye's surroundings: ocular adnexal lymphoma in the orbit, conjunctiva, and lacrimal gland is an indolent extranodal site, presenting as a painless salmon-pink mass."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut hosts a distinct follicular lymphoma: the duodenal-type and other GI involvement stud the bowel, an indolent presentation often found incidentally on endoscopy of the small and large intestine."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Follicular lymphoma is exquisitely antibody-sensitive: anti-CD20 antibodies (rituximab, obinutuzumab) anchor its treatment, and bispecific antibodies like mosunetuzumab now bring durable responses to relapsed disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Treatment, more than the tumor, reaches the nerves: the vincristine in regimens like R-CVP and R-CHOP injures peripheral neurons into a dose-limiting neuropathy, the indolent lymphoma itself rarely touching the nervous system."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "When follicular lymphoma transforms, the cure can wound the heart: aggressive transformation to diffuse large B-cell lymphoma calls for anthracycline-based R-CHOP, whose doxorubicin carries cumulative cardiotoxicity."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Anti-CD20 therapy can reawaken hepatitis B: rituximab and obinutuzumab deplete the B cells that help hold the virus in check, so patients are screened and given antiviral prophylaxis before treatment to prevent a dangerous reactivation."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Relapsed follicular lymphoma leans on PI3K-AKT: chronic B-cell-receptor signaling through this pathway sustains the indolent tumor, the target of the PI3K-delta inhibitors (idelalisib, copanlisib) developed for repeatedly relapsing disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Its therapies leave patients open to infection: rituximab can cause a late-onset neutropenia and bendamustine deeply suppresses immunity, so falling neutrophil counts and opportunistic infections are watched for through the long course of treatment."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF nurtures the follicular clone: the survival cytokine, supplied by the follicle's accessory cells, helps keep the BCL-2-protected lymphoma cells alive — one of the microenvironmental dependencies of this indolent disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells in the node carry prognostic weight: their density in the follicular lymphoma microenvironment correlates with outcome, part of the tumor-supporting stroma that shapes how the indolent disease behaves."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "The newest immunotherapies can spark a storm: CD20xCD3 bispecific antibodies and CAR-T for relapsed follicular lymphoma set off cytokine release syndrome as the T cells engage, managed with tocilizumab."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12 keeps the clone in its follicle: stromal cells secrete this chemokine to retain follicular lymphoma cells via CXCR4 in the protective germinal-center niche, where survival signals shield them from therapy."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV can ride along with the lymphoma: the virus is found in a subset of follicular lymphomas and, with the immunosuppression of treatment, can drive EBV-positive transformation and lymphoproliferation."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Repeated immunosuppression invites infection: the B-cell depletion and chemotherapy used over the long course of relapsing follicular lymphoma leave patients hypogammaglobulinemic and prone to sepsis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The supportive niche signals through STAT3: follicular lymphoma depends heavily on its microenvironment, where cytokines like IL-4 drive STAT signaling that sustains the slow-growing, niche-addicted B-cell clone."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An indolent lymphoma that still clots: like other lymphomas, follicular lymphoma raises venous thromboembolism risk through tumor-driven hypercoagulability and the catheters and immobility of treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow infiltration and inflammation lower the count: follicular lymphoma commonly involves the bone marrow and raises inflammatory cytokines, producing an anemia of chronic disease alongside any marrow crowding."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Anti-CD20 therapy can reactivate it: the rituximab and obinutuzumab central to follicular lymphoma treatment deplete B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede therapy."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Bendamustine-rituximab deeply depletes T cells: this common follicular lymphoma regimen causes prolonged lymphopenia, raising Pneumocystis pneumonia risk enough that prophylaxis is recommended during and after treatment."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Anthracyclines for transformation scar the heart: when follicular lymphoma transforms and is treated with R-CHOP, the doxorubicin is dose-dependently cardiotoxic, risking a later cardiomyopathy and heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemotherapy injures the nerves: the vincristine in R-CHOP and the bendamustine used for follicular lymphoma cause peripheral neuropathy with numbness and neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "B-cell-depleting therapy opens the lung to mold: rituximab and bendamustine for follicular lymphoma cause prolonged immunosuppression that can permit invasive aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, relapsing, incurable cancer weighs on mood: the indolent but recurring course and lifelong watchful management of follicular lymphoma contribute to a substantial burden of depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It has a home in the gut: duodenal-type follicular lymphoma is a recognised indolent GI presentation, and nodal disease enlarges the spleen and can involve the bowel."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its B-cell-depleting therapy reawakens shingles: rituximab and bendamustine for follicular lymphoma cause deep, lasting immunosuppression that allows latent varicella-zoster to reactivate."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Watchful waiting with an incurable cancer breeds worry: the indolent but relapsing course and constant surveillance of follicular lymphoma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Bulky retroperitoneal nodes block the ureters: large abdominal lymph-node masses in follicular lymphoma can obstruct the ureters, causing hydronephrosis and post-renal failure."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Chest nodes crowd the lungs: mediastinal and hilar disease can cause pleural effusions and airway compression, and transformation to aggressive lymphoma can infiltrate the lung."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It has a skin-only form: primary cutaneous follicle-centre lymphoma is an indolent variant presenting as nodules and plaques on the scalp and trunk with an excellent prognosis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It hides in the marrow: follicular lymphoma frequently infiltrates the bone marrow, causing cytopenias, and bony involvement can occur in advanced disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment can reach the heart: when follicular lymphoma transforms and needs anthracycline chemotherapy, dose-dependent cardiotoxicity follows, on top of anaemia's strain on the heart."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Therapy threatens fertility: chemotherapy for follicular lymphoma can impair fertility, prompting preservation counselling, and rare gonadal involvement occurs."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemoimmunotherapy controls it: bendamustine or CHOP with an anti-CD20 antibody is standard first-line treatment for symptomatic follicular lymphoma, though it is rarely cured."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Targeted drugs for an indolent cancer: the EZH2 inhibitor tazemetostat for EZH2-mutant disease, lenalidomide and BCL-2 inhibitors extend the options in follicular lymphoma."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Cell therapy for relapse: CD19 CAR-T cells and bispecific antibodies such as mosunetuzumab achieve high response rates in relapsed or refractory follicular lymphoma."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A microenvironment-dependent tumour: follicular lymphoma leans heavily on its immunosuppressive niche of regulatory and exhausted T cells, so checkpoint blockade and immunomodulators like lenalidomide act through that microenvironment rather than the tumour cell alone."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "It has an indolent gut form: primary duodenal-type follicular lymphoma grows in the small-bowel mucosa as a remarkably indolent, often localized disease, contrasting with nodal follicular lymphoma."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Two indolent B-cell neoplasms: follicular lymphoma and Waldenström macroglobulinaemia are both slow-growing mature B-cell cancers managed by watchful waiting and rituximab-based therapy, contrasting with the aggressive lymphomas."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "The mark of transformation: acquiring a TP53 mutation drives indolent follicular lymphoma to transform into aggressive diffuse large B-cell lymphoma, the event that worsens prognosis."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Immunosuppression-associated lymphoma: chronic immune stimulation and methotrexate or biologic therapy in rheumatoid arthritis raise the risk of non-Hodgkin lymphomas including follicular lymphoma."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Anthracycline cardiotoxicity: when follicular lymphoma transforms or needs R-CHOP, the doxorubicin component causes dose-dependent cardiomyopathy, monitored during treatment."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "An infectious driver: chronic hepatitis C drives the B-cell stimulation behind some indolent B-cell lymphomas including follicular lymphoma, which can respond to antiviral therapy."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmune lymphoma risk: chronic autoimmune B-cell stimulation in Sjögren's syndrome and rheumatoid arthritis raises the risk of follicular and other B-cell lymphomas."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal complications: follicular lymphoma can cause renal injury through tumour-lysis at treatment, ureteric obstruction by bulky nodes, or rarely a paraneoplastic glomerulonephritis."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "Chronic antigen drive: chronic hepatitis C is associated with follicular and marginal-zone lymphomas through sustained B-cell stimulation, and antiviral therapy can induce remission."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Recurrent mutation: FOXO1 mutations recur in follicular lymphoma, dysregulating this transcription factor in germinal-centre B cells and contributing to transformation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-delta dependence: PI3K signalling sustains follicular lymphoma survival, and PI3K-delta inhibitors such as idelalisib and copanlisib are approved for relapsed disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels follicular lymphoma B cells through the G1 checkpoint, the proliferative engine that accelerates as the indolent disease transforms."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Supportive niche: IL-6 from the follicular dendritic cells and T-helper cells of the germinal-centre microenvironment sustains follicular lymphoma cell survival."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Germinal-centre hypoxia: the physiologically hypoxic germinal centre stabilises HIF-1α, shaping the metabolism and survival of the follicular lymphoma cells that arise there."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Prognostic macrophages: CCL2 recruits tumour-associated macrophages into follicular lymphoma, whose abundance in the microenvironment carries prognostic weight—this lymphoma's biology is unusually microenvironment-dependent."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppressive niche: TGF-beta from the Treg-rich follicular lymphoma microenvironment dampens anti-tumour immunity, helping the malignant B cells evade the immune system."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Transformation to DLBCL: TERT activation and telomere maintenance accompany the histological transformation of indolent follicular lymphoma into aggressive diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis blockade: the defining t(14;18) translocation overexpresses BCL-2, which blocks caspase-3-mediated apoptosis and lets germinal-centre B cells survive that should have died — the founding lesion of follicular lymphoma."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BCR survival signalling: B-cell-receptor signalling through BTK supports the survival of follicular lymphoma cells, a therapeutic node targeted by BTK inhibitors in relapsed disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Microenvironment cytokines: IL-4 and IL-21 from the supportive follicular-helper-T-cell niche signal through JAK-STAT to nurture follicular lymphoma cells, reflecting the disease's unusual dependence on its microenvironment."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cellular immunotherapy: CD20-CD3 bispecific antibodies (mosunetuzumab) and CD19 CAR-T cells redirect cytotoxic T cells to kill follicular-lymphoma cells through perforin and granzyme, highly active options in relapsed disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-dependent killing: anti-CD20 antibodies (rituximab, obinutuzumab), the backbone of follicular-lymphoma therapy, kill cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex on the malignant B cells."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic dysregulation: follicular lymphoma is driven heavily by mutations in chromatin modifiers (CREBBP, KMT2D, EZH2) that, with altered DNA methylation, lock the cell in a germinal-centre programme — the epigenetic basis for EZH2-inhibitor therapy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K target: PTEN loss and PI3K-AKT activation (PIK3CA, AKT and mTOR already mapped) support follicular-lymphoma survival, the pathway the PI3K inhibitors copanlisib and idelalisib block in relapsed disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: the cyclin-D-CDK4/6 axis (CDK4/6 already mapped) releases E2F1 to drive cell-cycle entry, an increasingly active programme as follicular lymphoma acquires higher grade."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Histologic transformation: CDKN2A loss is a recurrent driver of the transformation of indolent follicular lymphoma into aggressive diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive niche: an IL-10-rich, regulatory-T-cell-laden microenvironment supports immune evasion and the survival of follicular-lymphoma B cells in their germinal-centre-like niche."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Transformation checkpoint: deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) accompanies the histologic transformation of indolent follicular lymphoma to aggressive disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "BCR-MAPK input: tonic B-cell-receptor and RAS signalling through ERK1/2 MAPK provides a proliferative input in follicular lymphoma, particularly upon transformation."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 in the follicular-lymphoma microenvironment modulates the T-follicular-helper interactions and immune evasion on which the tumour depends."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) shapes the immunosuppressive microenvironment that sustains follicular lymphoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the immune microenvironment and immunotherapy responsiveness of follicular lymphoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response within the T-cell-rich microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by PI3K-AKT signalling, modulate the survival and quiescence of the BCL2-translocated cells of follicular lymphoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS-ERK signalling (KRAS upstream of the mapped ERK1/2) provides a proliferative input cooperating with the BCL2 translocation in follicular lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt signaling of the follicular lymphoma clone."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the follicular-lymphoma tumor microenvironment, a key determinant of prognosis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis, complementing the anti-apoptotic BCL2 translocation in follicular lymphoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the B-cell receptor supports the survival of follicular lymphoma cells."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of the indolent follicular lymphoma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A and the CREBBP/EZH2-linked chromatin machinery (EZH2 already mapped) are recurrently altered in follicular lymphoma, dysregulating its transcriptional program."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of follicular lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the germinal-center homing and microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the germinal-center B-cell biology and microenvironment interactions of follicular lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of follicular lymphoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microenvironment and stromal interactions of follicular lymphoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Microenvironment dependence: follicular lymphoma relies on its germinal-centre-like niche, and MHC class II antigen presentation to follicular helper T cells sustains it, while MHC loss accompanies transformation and immune escape."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell therapies: IL-2-driven T-cell expansion powers the CD19 CAR-T and CD20xCD3 bispecific therapies (perforin already mapped) increasingly used for relapsed follicular lymphoma."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Immune checkpoint: CTLA-4 on the regulatory T cells enriched in the follicular lymphoma microenvironment helps the tumour evade immunity, part of the immunosuppressive niche that distinguishes this microenvironment-dependent lymphoma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow involvement: paratrabecular bone-marrow infiltration by follicular lymphoma and its immunochemotherapy lower haemoglobin, the anaemia with other cytopenias marking advanced disease and treatment toxicity."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin in R-CHOP regimens for follicular lymphoma is cardiotoxic, and troponin elevation helps detect the myocardial injury that constrains anthracycline use in this often long-lived indolent lymphoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis on transformation: when follicular lymphoma transforms to aggressive disease (DLBCL already mapped) and is treated, the rapid cell lysis releases purines that xanthine oxidase converts to uric acid, risking tumour-lysis syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 microenvironment: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine milieu of the follicular helper T cells (already mapped) that support the follicular lymphoma clone in its germinal-centre-like niche."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the follicular lymphoma microenvironment, part of the supportive stroma of this indolent lymphoma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Immunosuppressive eicosanoids: prostaglandin E2 in the follicular lymphoma microenvironment (IL-10 already mapped) dampens the anti-tumour immune response, part of the immune tolerance that sustains the indolent clone."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the lymphoma cells, part of the bone-marrow (already mapped) microenvironment that supports the indolent follicular lymphoma clone."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the lymphoma cells, part of the metabolic microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and contributes, with the marrow involvement, to the anaemia (haemoglobin already mapped) of follicular lymphoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon immunity: type-I interferon shapes the innate-immune tumour microenvironment and underlay the historical interferon therapy of follicular lymphoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and lymphocyte immunity: zinc is essential for the lymphocyte biology and immune function, and disturbed zinc status accompanies the immune dysfunction of follicular lymphoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-lymphoma immunity of follicular lymphoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the follicular-lymphoma microenvironment, opposing the immunosuppressive (IL-10 already mapped) milieu."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium immune status: the selenium selenoprotein antioxidant defence supports the lymphocyte (zinc already mapped) immune function disturbed in follicular lymphoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the follicular-lymphoma microenvironment."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the reactive T-cell microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the follicular-lymphoma microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Anti-CD20 CDC: the complement C5 and the terminal MAC (with C3 already mapped) mediate the complement-dependent cytotoxicity of the anti-CD20 (rituximab/obinutuzumab; CD20 already mapped) therapy of follicular lymphoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling shapes the myeloid and macrophage response within the immune microenvironment of follicular lymphoma."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Prognostic vitamin: the low vitamin D status is associated with a worse outcome in follicular lymphoma and modulates the immune microenvironment and the response to the immunochemotherapy."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the follicular-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 (already mapped) complement-dependent killing by obinutuzumab and rituximab."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway that mediates the anti-CD20 (already mapped) complement-dependent cytotoxicity of follicular lymphoma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow-involved follicular lymphoma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Stromal matricellular: periostin, a matricellular mediator, is part of the stromal remodelling of the follicular-lymphoma nodal microenvironment on which the tumour depends."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Nodal architecture: collagen, the extracellular-matrix scaffold, supports the follicular dendritic-cell network and the nodal architecture of the follicular-lymphoma microenvironment."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "FDC-network matrix: fibronectin, an extracellular-matrix glycoprotein, is part of the provisional matrix of the follicular dendritic-cell network that nurtures the follicular-lymphoma cells."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-FL axis: TSLP, from the follicular-lymphoma stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive tumour microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-FL axis: bradykinin, via B1/B2 receptors on follicular-lymphoma tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability, tumour oedema, and the inflammatory milieu of the follicular-lymphoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-FL axis: erythropoietin, via the EPOR on follicular-lymphoma B cells (already mapped), activates the PI3K/AKT (already mapped) survival axis and modulates macrophage (already mapped) polarisation in the anaemia of follicular lymphoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-FL axis: histamine, from mast cells in the follicular-lymphoma microenvironment, signals via H1/H2 receptors on malignant B cells (already mapped) and tumour endothelium, modulating BCL2-driven (already mapped) survival and the immunosuppressive FL milieu."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-FL axis: melatonin, via MT1/MT2 receptors on follicular-lymphoma B cells, modulates circadian immune rhythms, suppresses BCL2-driven (already mapped) anti-apoptotic signalling, and enhances the sensitivity to anti-CD20 (rituximab) chemoimmunotherapy."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-FL axis: testosterone, via androgen receptor signalling on follicular-lymphoma B cells and stromal cells, modulates BCL2-driven (already mapped) lymphoma-cell survival and the sex-biased immune microenvironment of follicular lymphoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "FL prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) survival cascade of follicular lymphoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "FL oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) cascade of follicular lymphoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "FL vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) proliferation cascade of FL."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "FL serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "FL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and B-cell (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "FL sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the B-cell (already mapped) survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "FL magnesium: magnesium cofactors kinase signalling in B-cells (already mapped) and macrophages (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "FL copper: copper, via ceruloplasmin in macrophages (already mapped) and B-cells (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "FL potassium: potassium regulates macrophage (already mapped) and B-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "FL chloride: chloride channels on B-cells (already mapped) and macrophages (already mapped) regulate apoptotic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "FL sulfur: glutathione from sulfur amino acids in macrophages (already mapped) and B-cells (already mapped) counters ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "FL nitrogen: nitric oxide from iNOS in macrophages (already mapped) modulates anti-tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell (already mapped) cascade of follicular lymphoma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "FL carbon: carbon in nucleotides of B-cells (already mapped) and macrophages (already mapped) fuels malignant proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "FL hydrogen: hydrogen via ROS from macrophages (already mapped) and B-cells (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "FL oxygen: oxygen drives B-cell (already mapped) and macrophage (already mapped) mitochondrial metabolism, supporting tumour growth; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of follicular lymphoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "follicular-lymphoma glp-1: GLP-1 from macrophages (already mapped) and B-cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) lymphoma cascade in follicular lymphoma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "follicular-lymphoma angiotensin-ii: angiotensin II on B-cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "follicular-lymphoma wnt-beta-catenin: WNT/β-catenin on B-cells (already mapped) and macrophages (already mapped) promotes growth; wnt-beta-catenin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "follicular-lymphoma rankl: RANKL from macrophages (already mapped) and B-cells (already mapped) promotes osteoclast activation; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "follicular-lymphoma igf-1: IGF-1 from macrophages (already mapped) and B-cells (already mapped) promotes lymphoma survival; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "follicular-lymphoma activin-a: activin-A from macrophages (already mapped) and B-cells (already mapped) promotes lymphoma-stromal invasion; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "follicular-lymphoma cgrp: CGRP from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "follicular-lymphoma calcitonin: calcitonin from macrophages (already mapped) and B-cells (already mapped) modulates calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "follicular-lymphoma substance-p: substance-P from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "follicular-lymphoma insulin-receptor: insulin receptor on macrophages (already mapped) and B-cells (already mapped) modulates lymphoma metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "follicular-lymphoma aldosterone: aldosterone from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "follicular-lymphoma androgen-receptor: androgen receptor on macrophages (already mapped) and B-cells (already mapped) modulates lymphoma androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL."
---

# Follicular Lymphoma

## Overview

**Follicular lymphoma (FL)** is the most common indolent non-Hodgkin B-cell lymphoma in western countries, comprising ~20-25% of all NHL (~15,000 new cases/year in the US). FL arises from germinal center (GC) B-cells, characterized by follicular (nodular) growth pattern recapitulating normal GC architecture, with CD10+/BCL-6+/BCL-2+ B-cells filling and expanding secondary lymphoid follicles. The pathognomonic molecular event is **t(14;18)(q32;q21)** — BCL-2-IGH translocation in ~85-90% of cases — juxtaposing BCL-2 under the IGH enhancer to drive constitutive BCL-2 overexpression in GC B-cells that normally downregulate BCL-2 during affinity maturation. FL is an incurable disease in most patients with current therapy, yet it follows a characteristically indolent natural history with median OS >15 years in early stages; the GALLIUM trial demonstrated obinutuzumab-based regimens improve progression-free survival over rituximab in frontline treatment [^marcus-2017-gallium]. **Histologic transformation** to aggressive DLBCL is the most serious complication (~30% at 10 years) and is the most common cause of FL-related death.

**Epidemiology:**
- ~15,000 new cases/year in the US; median age at diagnosis ~60 years; M:F equal
- Incidence rising in western countries; higher in North America and Europe than Asia
- 5-year survival: ~90% for grades 1-2; ~70-80% for grade 3B; transformed FL treated like de novo DLBCL
- Median OS: >15 years for grade 1-2 FL; ~50% of patients alive at 20 years; 5-year OS ~88%

**Prognostic risk stratification:**
- **FLIPI (Follicular Lymphoma International Prognostic Index):** 5 adverse factors: age >60, Ann Arbor stage III-IV, Hgb <12 g/dL, LDH > ULN, ≥5 nodal areas
  - Low risk (0-1): 5-year OS ~91%; Intermediate (2): ~78%; High (≥3): ~53%
- **FLIPI-2:** Bone marrow involvement, longest diameter >6 cm, β2M > ULN, Hgb < LLN, age >60
- **POD24 (progression of disease within 24 months):** Strong adverse prognostic marker; ~20% of patients; OS only ~50% at 5 years from POD24; associated with histologic transformation risk

## Structure

### Molecular landscape

**Founding event — t(14;18) BCL-2-IGH:**
t(14;18)(q32;q21) translocation → BCL-2 gene (18q21) fused to IgH locus (14q32) → constitutive BCL-2 overexpression in GC B-cells (which normally downregulate BCL-2 during affinity maturation to allow negative selection). BCL-2 overexpression blocks GC B-cell apoptosis → prolonged GC residence → accumulation of additional mutations → FL development. t(14;18) is detectable in ~50% of normal healthy adults (clonal hematopoiesis-like phenomenon) — requiring additional "hits" for malignant transformation.

**Epigenetic mutations (co-drivers):**
- **CREBBP:** Mutations in ~60% of FL; HAT (histone acetyltransferase) domain mutations → loss of H3K18/K27 acetylation at BCL-6-target loci → impaired activation-induced deaminase (AID) regulation; cooperates with EZH2
- **EP300:** Mutations in ~15% (non-overlapping with CREBBP); similar HAT function
- **KMT2D (MLL4):** ~80% of FL; histone H3K4 methyltransferase; loss → decreased H3K4me3 at promoters → gene silencing (including CDKN2A-independent tumor suppressors)
- **EZH2 Y641/A677/A687:** ~25% gain-of-function mutations → H3K27me3 accumulation → silences tumor suppressors and differentiation regulators; cooperates with CREBBP/KMT2D loss
- **TNFRSF14 (HVEM):** ~40% mutations → loss of BTLA-HVEM checkpoint → tumor-microenvironment immune evasion
- **RRAGC:** ~17% mutations → mTORC1 amino acid sensing dysregulation (rare among lymphomas)

**FL histological grading:**
- Grade 1: 0-5 centroblasts per high power field (HPF)
- Grade 2: 6-15 centroblasts/HPF
- Grade 3A: >15 centroblasts/HPF; centrocytes still present
- Grade 3B: >15 centroblasts/HPF; solid sheets of centroblasts; no centrocytes → treated as aggressive DLBCL
- **Diffuse large B-cell lymphoma (DLBCL) transformation:** Loss of follicular architecture; MYC rearrangement (de novo or secondary); TP53 mutation → aggressive lymphoma with poor prognosis

**Immunophenotype:**
CD19+, CD20+, CD10+ (GC marker), BCL-6+, BCL-2+ (overexpressed via t(14;18)), surface IgM or IgG, FMC7+; CD5 negative, CD23 negative (distinguishes FL from mantle cell lymphoma, CLL).

## Function

### Germinal center biology and FL pathogenesis

**Normal GC B-cell biology:**
GC formation → B-cells undergo somatic hypermutation (SHM) of Ig variable regions → selection for high-affinity antibody clones → antigen-selected B-cells differentiate into plasma cells (BCL-2-low; BLIMP1+) or memory B-cells (BCL-2 restored). BCL-2 is transiently downregulated during GC to allow negative selection of low-affinity clones. EZH2 is highly expressed in GC B-cells to maintain GC identity and suppress PRDM1 (BLIMP1) — preventing premature plasma cell differentiation.

**FL oncogenesis:**
t(14;18) translocation (during V(D)J recombination or SHM) → BCL-2 constitutively expressed in GC B-cells → apoptosis resistance → prolonged GC residence → accumulation of KMT2D, CREBBP, EZH2, TNFRSF14 mutations → FL initiation. The BCL-2-overexpressing, GC-arrested B-cells accumulate in lymph nodes → follicular (nodular) architecture → tumor mass formation without significant constitutional symptoms initially.

**Immunologic microenvironment:**
FL is characteristically "immune-rich" — abundant T follicular helper cells (Tfh), T regulatory cells (Tregs), and follicular dendritic cells (FDC) in the tumor microenvironment. The immune microenvironment influences FL prognosis (high Tfh → better prognosis; high Tregs → worse). TNFRSF14 mutations → loss of HVEM → loss of BTLA/CD160 inhibitory signaling → modified tumor-T cell crosstalk. Mosunetuzumab and bispecific antibodies redirect endogenous T-cells to kill FL B-cells.

### Histologic transformation to DLBCL

**Mechanisms:**
- MYC rearrangement acquisition (in addition to BCL-2-IGH) → double-hit lymphoma; often q8p24 → MYC-IG translocation
- TP53 mutation/deletion → p53 dysfunction → rapid proliferation
- CDKN2A loss → CDK4/6 unrestrained → cell cycle bypass
- BCL-2-IGH + BCL-6 rearrangement → MYC-independent transformation route

**Clinical significance:**
- Transformation rate: ~2-3%/year in first 5 years; lower thereafter
- Histologic biopsy required to confirm transformation (PET can identify biopsy target: FDG avid site)
- Transformed FL: Treat as de novo DLBCL; CAR-T or consolidative auto-SCT in second remission

## Pathology

### Staging and workup

**Ann Arbor staging (Lugano classification 2014):**
- Stage I: Single node region or single extranodal site
- Stage II: ≥2 node regions, same side of diaphragm
- Stage III: Node regions on both sides of diaphragm
- Stage IV: Disseminated extralymphatic involvement
- Most FL presents at Stage III-IV (~80%) — but this does not mandate immediate treatment

**Staging workup:**
- CT chest/abdomen/pelvis with contrast: Baseline nodal and extranodal assessment
- PET-CT: Standard per Lugano guidelines for staging and treatment response (Deauville score); essential for identifying histologic transformation (avid site for biopsy)
- Bone marrow biopsy: For staging in low-risk or limited staging CT; often involved in FL (BM involvement = stage IV → does not change management in asymptomatic FL)
- CBC, CMP, LDH, β2M, uric acid, hepatitis B/C (rituximab reactivation risk)
- t(14;18) FISH or PCR: Confirmatory in atypical cases
- EZH2 mutation testing: If considering tazemetostat for R/R FL
- Molecular profile (NGS panel): CREBBP, KMT2D, EZH2, TNFRSF14 for prognosis/clinical trials

### Treatment

**Watch and wait (asymptomatic, low tumor burden):**
Standard approach for asymptomatic Grade 1-2 FL without GELF criteria (Groupe d'Etude des Lymphomes Folliculaires): No "B symptoms," no bulky disease >7 cm, no organ compromise, no rapid progression, adequate blood counts. Observation with CT q3-6 months; treatment initiation at symptom onset or disease progression.

**First-line (symptomatic or high tumor burden):**
- **R-bendamustine (BR):** Rituximab 375 mg/m² D1 + Bendamustine 90 mg/m² D1-2 q28d × 6 cycles; preferred over R-CHOP for Grade 1-2 FL (BRIGHT trial: superior PFS; less alopecia/neurotoxicity)
- **R-CHOP:** Rituximab + cyclophosphamide + doxorubicin + vincristine + prednisone; q21d × 6-8 cycles; alternative for Grade 3A or bulky disease
- **Obinutuzumab + chemotherapy (G-CHOP or G-bendamustine, GALLIUM trial):** [^marcus-2017-gallium] 3-year PFS 80.0% vs. 73.3% (rituximab+chemo); FDA approved 2016; obinutuzumab maintenance × 2 years post-induction; preferred for high-FLIPI or high tumor burden
- **Rituximab monotherapy:** For elderly/frail patients with limited tumor burden; ORR ~60-70%; maintenance rituximab q8 weeks × 2 years improves PFS

**Rituximab/obinutuzumab maintenance (post-induction):**
- Rituximab 375 mg/m² q8w × 2 years (PRIMA trial): Improves PFS vs. observation; OS benefit not shown
- Obinutuzumab 1000 mg q8w × 2 years: After G-chemotherapy induction (GALLIUM)

**Relapsed/refractory FL:**
- **Tazemetostat 800 mg BID (EZH2-mutant FL):** [^morschhauser-2020-tazemetostat] ORR 69%; FDA approved 2020 for ≥2 prior lines
- **Tazemetostat 800 mg BID (EZH2 WT FL, no satisfactory alternatives):** ORR 35%; FDA approved
- **Lenalidomide + rituximab (R-squared, AUGMENT trial):** ORR 78%; PFS 39.4 vs. 14.1 months vs. rituximab+placebo; FDA approved 2019 for R/R FL
- **Mosunetuzumab (CD20×CD3 bispecific, CELESTIMO trial):** FDA approved 2022 for R/R FL ≥2 prior lines; ORR 80% (CR 60%); step-up dosing cycle 1 (to mitigate CRS)
- **Epcoritamab, glofitamab:** CD20×CD3 bispecifics under evaluation for R/R FL
- **Axicabtagene ciloleucel (CAR-T, ZUMA-5):** ORR 94% in R/R FL ≥2 prior lines; CR 79%; FDA approved 2021; durable responses (18-month DOR ~76%); toxicities: CRS, ICANS

**Consolidation (selected patients):**
- Auto-SCT: PR/CR after ≥2 prior lines; improves PFS; OS benefit not demonstrated in biologic therapy era
- Allo-SCT: For chemotherapy-sensitive disease in poor-risk patients or transformed FL; curative potential at cost of transplant morbidity/mortality

**Radiation:**
- Involved-field RT (24-30 Gy): Stage I/II FL → 10-year PFS ~50%; potentially curative in 40% of stage I
- Palliative RT (2×2 Gy): Very effective for local symptoms (response rate >90%)

**POD24 management:**
High-risk subset (progression within 24 months of first chemoimmunotherapy): Consider CAR-T, clinical trial, or allo-SCT; immune-mediated agents preferred over chemoimmunotherapy rechallenge.

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — t(14;18) BCL-2-IGH translocation in ~85-90% of FL → BCL-2 overexpression in GC B-cells → apoptosis resistance; BCL-2 is the defining molecular feature of FL; venetoclax (BCL-2 inhibitor) active in relapsed FL; BCL-2 overexpression does not predict venetoclax response in FL.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20 mAb) is the backbone of FL therapy; R-CHOP and R-bendamustine are first-line options; obinutuzumab (glycoengineered anti-CD20) + chemotherapy (GALLIUM trial) improved PFS vs. rituximab; anti-CD20 maintenance improves PFS after induction.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Histologic transformation of FL to DLBCL occurs in ~30% at 10 years; POD24 (progression within 24 months) is associated with MYC acquisition and poor prognosis; double-hit lymphoma (MYC+BCL-2 rearrangement) arising from FL is treated as aggressive lymphoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — CREBBP mutations in ~60% and EP300 mutations in ~15% of FL → loss of HAT activity → decreased H3K18/K27 acetylation; CREBBP/EZH2 co-mutations in ~30% of FL → dual epigenetic reprogramming; EZH2 silences TNFAIP3/A20 (NF-κB inhibitor) → enhanced NF-κB in FL cells.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 Y641F/N gain-of-function in ~25% of FL → H3K27me3 → silences tumor suppressor and differentiation genes; tazemetostat (EZH2i) approved for R/R EZH2-mutant FL (ORR 69%) and EZH2-WT FL (ORR 35%); CREBBP co-mutation in ~30% creates dual epigenetic dysregulation.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Histologic transformation from FL to DLBCL occurs in ~30% at 10 years; requires MYC rearrangement, TP53 mutation, or CDKN2A loss on top of BCL-2-IGH; transformed FL is treated as de novo DLBCL; CAR-T (axi-cel) or auto-SCT preferred after induction.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — FL tumor microenvironment is immune-rich (Tfh, Tregs, FDC); mosunetuzumab (CD20×CD3 bispecific, approved R/R FL) redirects T-cells to kill FL B-cells; PD-1 blockade + rituximab has modest single-agent activity; lenalidomide → NK-cell ADCC and immune reprogramming in R/R FL.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Follicular and mantle cell lymphoma are both translocation-defined B-cell NHLs but opposites: FL (t(14;18), BCL-2) is indolent and apoptosis-resistant, MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive — the two classic overexpression translocation lymphomas.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Follicular lymphoma arises from germinal-center B cells frozen mid-maturation: t(14;18) places BCL-2 under the immunoglobulin enhancer, so cells that should die during affinity maturation survive, accumulating as CD10+/BCL6+ clonal follicles that mimic the germinal center.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Follicular lymphoma is a disseminated nodal disease that often involves the spleen and bone marrow at diagnosis (stage III-IV in ~80%); splenic and marrow involvement rarely changes the indolent watch-and-wait or rituximab-based management, since FL is treatable but not curable.
- `connects-to` → **[CLL](../cll/README.md)** — Follicular lymphoma and CLL/SLL are the commonest indolent B-cell lymphomas: both slow-growing, manageable-but-incurable, and prone to transformation into aggressive DLBCL (Richter for CLL); they differ in origin—germinal-center FL with t(14;18)/BCL2 vs CD5+ post-GC CLL.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Follicular lymphoma is a disease of the lymphatic system: malignant germinal-center B cells expand lymph-node follicles, producing the waxing-and-waning painless lymphadenopathy that is its hallmark, with spread to spleen and marrow; many cases are watched while asymptomatic.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Follicular lymphoma arises directly from the germinal center: a malignancy of follicle-center B cells frozen mid-reaction that recapitulates follicular architecture, and its founding t(14;18) drives constitutive BCL2 to block the apoptosis that normally prunes these cells.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Follicular and Hodgkin lymphomas both arise from germinal-center B cells but behave oppositely: follicular is indolent, BCL2-driven and incurable, smoldering for years, while Hodgkin's Reed-Sternberg tumor is aggressive yet highly curable—indolence versus curability.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Follicular and Burkitt lymphomas are germinal-center B-cell tumors at opposite tempos: follicular is slow, BCL2 [t(14;18)]-driven and incurable, while Burkitt is the fastest-growing human tumor, MYC [t(8;14)]-driven yet curable—each named by its translocation.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Follicular lymphoma and multiple myeloma are both incurable B-lineage malignancies at different maturation stages: FL is a CD20+ germinal-center B-cell tumor, myeloma a marrow plasma-cell cancer secreting monoclonal protein—both relapse and remit over years.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Follicular lymphoma depends on follicular helper T cells in its microenvironment: the malignant B cells need Tfh signals and a supportive niche to survive, so FL is as much a disease of the microenvironment as of the B cell—explaining its indolent, relapsing course.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Follicular lymphoma is a germinal-center B cell blocked from becoming a plasma cell: the t(14;18) BCL2 translocation lets it resist apoptosis and accumulate instead of maturing into antibody-secreting cells—an indolent buildup unlike high-grade lymphomas.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Follicular lymphoma's behavior is shaped by immune surveillance: the microenvironment can restrain or enable the tumor, and FL can spontaneously regress or transform—so immune-modulating therapies (rituximab, lenalidomide) are central to its largely incurable course.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Follicular lymphoma usually involves the bone marrow at diagnosis: the indolent clone seeds marrow in a paratrabecular pattern, so it is typically advanced-stage yet slow-growing—curative local therapy is rarely possible, but it can be watched or controlled for years.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy can cure the rare localized follicular lymphoma: low-dose photon radiation to a single involved site is potentially curative in stage I disease, a notable exception in a lymphoma that is otherwise incurable but indolent and managed over many years.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Follicular lymphoma can transform and reach the nervous system: histologic transformation to aggressive DLBCL—and rarely CNS involvement—marks a turn for the worse in this usually indolent disease, shifting management from watchful waiting to intensive therapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Follicular lymphoma is built on follicular dendritic cells: these stromal cells form the germinal-center meshwork the malignant B cells depend on for survival signals, so the tumor recreates a follicle—its microenvironment shaping when indolent disease turns aggressive.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Follicular lymphoma now yields to T-cell therapies: CD19 CAR-T cells and CD20×CD3 bispecifics (mosunetuzumab) redirect cytotoxic T cells against the B-cell clone, giving durable remissions in this otherwise relapsing, incurable indolent lymphoma.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Follicular lymphoma is usually widespread at diagnosis, infiltrating the liver: indolent but disseminated, it commonly involves liver, spleen, and marrow by the time it is found—so it is staged as advanced yet often watched rather than treated.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Follicular lymphoma can be hit through the PI3K-mTOR pathway: this survival signaling is active in the lymphoma, so PI3K inhibitors (idelalisib, copanlisib) that feed into mTOR are approved options for relapsed disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Follicular lymphoma lives or dies by its microenvironment, especially regulatory T cells: the mix of Tregs and other immune cells around the tumor follicles predicts how indolent or aggressive the lymphoma will be, more than the tumor cells alone.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Rituximab clears follicular lymphoma largely through NK cells: the anti-CD20 antibody coats the B cells and natural killer cells destroy them by antibody-dependent killing, so NK function shapes how well this mainstay therapy works.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages predict outcome in follicular lymphoma: the number of lymphoma-associated macrophages in the tumor tracks with prognosis, and these cells both support the malignant B cells and mediate the killing when rituximab is given.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Follicular lymphoma leans on its vascular niche via VEGF: the indolent tumor recruits new vessels and a supportive microenvironment in the lymph node, with VEGF-driven angiogenesis sustaining the slow-growing B-cell clone.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — B-cell receptor signaling keeps follicular lymphoma alive through calcium: tonic receptor firing drives a calcium flux that promotes survival, which is why BTK and PI3K inhibitors that interrupt this pathway have a role in treatment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Follicular lymphoma quietly drains iron: marrow infiltration and chronic disease suppress red-cell production and sequester iron, so anemia often accompanies this slow-growing lymphoma.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Follicular lymphoma has a gut form: duodenal-type follicular lymphoma arises in the small intestine as an indolent, often localized disease found incidentally on endoscopy.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Follicular lymphoma depends on endothelial cells: VEGF from the tumor and its niche recruits these vessel-lining cells to build the vasculature that sustains the slow-growing clone in the lymph node.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — When follicular lymphoma transforms to aggressive DLBCL and is treated, rapid cell death can trigger tumor lysis, spilling phosphate and potassium into the blood as a metabolic emergency.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Follicular lymphoma has a skin form: primary cutaneous follicle-center lymphoma appears as slow-growing nodules on the head and trunk, an indolent cousin of the nodal disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Follicular lymphoma leans on its niche: T-follicular-helper cells feed the malignant B cells signals like IL-4 and CD40L, so the tumor depends on a supportive microenvironment, not its mutations alone.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows follicular lymphoma's small cleaved cell: the centrocyte, with its notched, angular nucleus, recapitulates the germinal-center cell it came from, packed into nodular follicles by the BCL2 that blocks its death.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Follicular lymphoma can settle in the eye's surroundings: ocular adnexal lymphoma in the orbit, conjunctiva, and lacrimal gland is an indolent extranodal site, presenting as a painless salmon-pink mass.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut hosts a distinct follicular lymphoma: the duodenal-type and other GI involvement stud the bowel, an indolent presentation often found incidentally on endoscopy of the small and large intestine.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Follicular lymphoma is exquisitely antibody-sensitive: anti-CD20 antibodies (rituximab, obinutuzumab) anchor its treatment, and bispecific antibodies like mosunetuzumab now bring durable responses to relapsed disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Treatment, more than the tumor, reaches the nerves: the vincristine in regimens like R-CVP and R-CHOP injures peripheral neurons into a dose-limiting neuropathy, the indolent lymphoma itself rarely touching the nervous system.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — When follicular lymphoma transforms, the cure can wound the heart: aggressive transformation to diffuse large B-cell lymphoma calls for anthracycline-based R-CHOP, whose doxorubicin carries cumulative cardiotoxicity.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Anti-CD20 therapy can reawaken hepatitis B: rituximab and obinutuzumab deplete the B cells that help hold the virus in check, so patients are screened and given antiviral prophylaxis before treatment to prevent a dangerous reactivation.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Relapsed follicular lymphoma leans on PI3K-AKT: chronic B-cell-receptor signaling through this pathway sustains the indolent tumor, the target of the PI3K-delta inhibitors (idelalisib, copanlisib) developed for repeatedly relapsing disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Its therapies leave patients open to infection: rituximab can cause a late-onset neutropenia and bendamustine deeply suppresses immunity, so falling neutrophil counts and opportunistic infections are watched for through the long course of treatment.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF nurtures the follicular clone: the survival cytokine, supplied by the follicle's accessory cells, helps keep the BCL-2-protected lymphoma cells alive — one of the microenvironmental dependencies of this indolent disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells in the node carry prognostic weight: their density in the follicular lymphoma microenvironment correlates with outcome, part of the tumor-supporting stroma that shapes how the indolent disease behaves.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — The newest immunotherapies can spark a storm: CD20xCD3 bispecific antibodies and CAR-T for relapsed follicular lymphoma set off cytokine release syndrome as the T cells engage, managed with tocilizumab.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 keeps the clone in its follicle: stromal cells secrete this chemokine to retain follicular lymphoma cells via CXCR4 in the protective germinal-center niche, where survival signals shield them from therapy.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV can ride along with the lymphoma: the virus is found in a subset of follicular lymphomas and, with the immunosuppression of treatment, can drive EBV-positive transformation and lymphoproliferation.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Repeated immunosuppression invites infection: the B-cell depletion and chemotherapy used over the long course of relapsing follicular lymphoma leave patients hypogammaglobulinemic and prone to sepsis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The supportive niche signals through STAT3: follicular lymphoma depends heavily on its microenvironment, where cytokines like IL-4 drive STAT signaling that sustains the slow-growing, niche-addicted B-cell clone.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An indolent lymphoma that still clots: like other lymphomas, follicular lymphoma raises venous thromboembolism risk through tumor-driven hypercoagulability and the catheters and immobility of treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow infiltration and inflammation lower the count: follicular lymphoma commonly involves the bone marrow and raises inflammatory cytokines, producing an anemia of chronic disease alongside any marrow crowding.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Anti-CD20 therapy can reactivate it: the rituximab and obinutuzumab central to follicular lymphoma treatment deplete B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede therapy.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Bendamustine-rituximab deeply depletes T cells: this common follicular lymphoma regimen causes prolonged lymphopenia, raising Pneumocystis pneumonia risk enough that prophylaxis is recommended during and after treatment.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Anthracyclines for transformation scar the heart: when follicular lymphoma transforms and is treated with R-CHOP, the doxorubicin is dose-dependently cardiotoxic, risking a later cardiomyopathy and heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemotherapy injures the nerves: the vincristine in R-CHOP and the bendamustine used for follicular lymphoma cause peripheral neuropathy with numbness and neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — B-cell-depleting therapy opens the lung to mold: rituximab and bendamustine for follicular lymphoma cause prolonged immunosuppression that can permit invasive aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, relapsing, incurable cancer weighs on mood: the indolent but recurring course and lifelong watchful management of follicular lymphoma contribute to a substantial burden of depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It has a home in the gut: duodenal-type follicular lymphoma is a recognised indolent GI presentation, and nodal disease enlarges the spleen and can involve the bowel.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its B-cell-depleting therapy reawakens shingles: rituximab and bendamustine for follicular lymphoma cause deep, lasting immunosuppression that allows latent varicella-zoster to reactivate.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Watchful waiting with an incurable cancer breeds worry: the indolent but relapsing course and constant surveillance of follicular lymphoma foster chronic health anxiety alongside depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Bulky retroperitoneal nodes block the ureters: large abdominal lymph-node masses in follicular lymphoma can obstruct the ureters, causing hydronephrosis and post-renal failure.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Chest nodes crowd the lungs: mediastinal and hilar disease can cause pleural effusions and airway compression, and transformation to aggressive lymphoma can infiltrate the lung.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It has a skin-only form: primary cutaneous follicle-centre lymphoma is an indolent variant presenting as nodules and plaques on the scalp and trunk with an excellent prognosis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It hides in the marrow: follicular lymphoma frequently infiltrates the bone marrow, causing cytopenias, and bony involvement can occur in advanced disease.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment can reach the heart: when follicular lymphoma transforms and needs anthracycline chemotherapy, dose-dependent cardiotoxicity follows, on top of anaemia's strain on the heart.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Therapy threatens fertility: chemotherapy for follicular lymphoma can impair fertility, prompting preservation counselling, and rare gonadal involvement occurs.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemoimmunotherapy controls it: bendamustine or CHOP with an anti-CD20 antibody is standard first-line treatment for symptomatic follicular lymphoma, though it is rarely cured.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Targeted drugs for an indolent cancer: the EZH2 inhibitor tazemetostat for EZH2-mutant disease, lenalidomide and BCL-2 inhibitors extend the options in follicular lymphoma.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Cell therapy for relapse: CD19 CAR-T cells and bispecific antibodies such as mosunetuzumab achieve high response rates in relapsed or refractory follicular lymphoma.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A microenvironment-dependent tumour: follicular lymphoma leans heavily on its immunosuppressive niche of regulatory and exhausted T cells, so checkpoint blockade and immunomodulators like lenalidomide act through that microenvironment rather than the tumour cell alone.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — It has an indolent gut form: primary duodenal-type follicular lymphoma grows in the small-bowel mucosa as a remarkably indolent, often localized disease, contrasting with nodal follicular lymphoma.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Two indolent B-cell neoplasms: follicular lymphoma and Waldenström macroglobulinaemia are both slow-growing mature B-cell cancers managed by watchful waiting and rituximab-based therapy, contrasting with the aggressive lymphomas.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — The mark of transformation: acquiring a TP53 mutation drives indolent follicular lymphoma to transform into aggressive diffuse large B-cell lymphoma, the event that worsens prognosis.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Immunosuppression-associated lymphoma: chronic immune stimulation and methotrexate or biologic therapy in rheumatoid arthritis raise the risk of non-Hodgkin lymphomas including follicular lymphoma.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Anthracycline cardiotoxicity: when follicular lymphoma transforms or needs R-CHOP, the doxorubicin component causes dose-dependent cardiomyopathy, monitored during treatment.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — An infectious driver: chronic hepatitis C drives the B-cell stimulation behind some indolent B-cell lymphomas including follicular lymphoma, which can respond to antiviral therapy.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmune lymphoma risk: chronic autoimmune B-cell stimulation in Sjögren's syndrome and rheumatoid arthritis raises the risk of follicular and other B-cell lymphomas.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal complications: follicular lymphoma can cause renal injury through tumour-lysis at treatment, ureteric obstruction by bulky nodes, or rarely a paraneoplastic glomerulonephritis.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — Chronic antigen drive: chronic hepatitis C is associated with follicular and marginal-zone lymphomas through sustained B-cell stimulation, and antiviral therapy can induce remission.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — Recurrent mutation: FOXO1 mutations recur in follicular lymphoma, dysregulating this transcription factor in germinal-centre B cells and contributing to transformation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-delta dependence: PI3K signalling sustains follicular lymphoma survival, and PI3K-delta inhibitors such as idelalisib and copanlisib are approved for relapsed disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels follicular lymphoma B cells through the G1 checkpoint, the proliferative engine that accelerates as the indolent disease transforms.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Supportive niche: IL-6 from the follicular dendritic cells and T-helper cells of the germinal-centre microenvironment sustains follicular lymphoma cell survival.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Germinal-centre hypoxia: the physiologically hypoxic germinal centre stabilises HIF-1α, shaping the metabolism and survival of the follicular lymphoma cells that arise there.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Prognostic macrophages: CCL2 recruits tumour-associated macrophages into follicular lymphoma, whose abundance in the microenvironment carries prognostic weight—this lymphoma's biology is unusually microenvironment-dependent.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immunosuppressive niche: TGF-beta from the Treg-rich follicular lymphoma microenvironment dampens anti-tumour immunity, helping the malignant B cells evade the immune system.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Transformation to DLBCL: TERT activation and telomere maintenance accompany the histological transformation of indolent follicular lymphoma into aggressive diffuse large B-cell lymphoma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The defining t(14;18) translocation overexpresses BCL-2, which blocks caspase-3-mediated apoptosis and lets germinal-center B cells survive that should have died—the founding molecular lesion of follicular lymphoma.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — B-cell-receptor signaling through BTK supports the survival of follicular lymphoma cells, a therapeutic node targeted by BTK inhibitors in relapsed disease alongside the PI3K and BCL-2 pathways.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-4 and IL-21 from the supportive follicular-helper-T-cell niche signal through JAK-STAT to nurture follicular lymphoma cells, reflecting the disease's unusual dependence on its surrounding microenvironment.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD20-CD3 bispecific antibodies (mosunetuzumab) and CD19 CAR-T cells redirect cytotoxic T cells to kill follicular-lymphoma cells through perforin and granzyme, highly active options in relapsed disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Anti-CD20 antibodies (rituximab, obinutuzumab), the backbone of follicular-lymphoma therapy, kill cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex on the malignant B cells.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Follicular lymphoma is driven heavily by mutations in chromatin modifiers (CREBBP, KMT2D, EZH2) that, with altered DNA methylation, lock the cell in a germinal-center program—the epigenetic basis for EZH2-inhibitor therapy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss and PI3K-AKT activation (PIK3CA, AKT and mTOR already mapped) support follicular-lymphoma survival, the pathway the PI3K inhibitors copanlisib and idelalisib block in relapsed disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (CDK4/6 already mapped) releases E2F1 to drive cell-cycle entry, an increasingly active program as follicular lymphoma acquires higher grade.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss is a recurrent driver of the transformation of indolent follicular lymphoma into aggressive diffuse large B-cell lymphoma.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — An IL-10-rich, regulatory-T-cell-laden microenvironment supports immune evasion and the survival of follicular-lymphoma B cells in their germinal-center-like niche.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) accompanies the histologic transformation of indolent follicular lymphoma to aggressive disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Tonic B-cell-receptor and RAS signaling through ERK1/2 MAPK provides a proliferative input in follicular lymphoma, particularly upon transformation.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 in the follicular-lymphoma microenvironment modulates the T-follicular-helper interactions and immune evasion on which the tumor depends.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) shapes the immunosuppressive microenvironment that sustains follicular lymphoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the immune microenvironment and immunotherapy responsiveness of follicular lymphoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response within the T-cell-rich microenvironment of follicular lymphoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by PI3K-AKT signaling, modulate the survival and quiescence of the BCL2-translocated cells of follicular lymphoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (KRAS upstream of the mapped ERK1/2) provides a proliferative input cooperating with the BCL2 translocation in follicular lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt signaling of the follicular lymphoma clone.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the follicular-lymphoma tumor microenvironment, a key determinant of prognosis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis, complementing the anti-apoptotic BCL2 translocation in follicular lymphoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the B-cell receptor supports the survival of follicular lymphoma cells.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of the indolent follicular lymphoma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the CREBBP/EZH2-linked chromatin machinery (EZH2 already mapped) are recurrently altered in follicular lymphoma, dysregulating its transcriptional program.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of follicular lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the germinal-center homing and microenvironment of follicular lymphoma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the germinal-center B-cell biology and microenvironment interactions of follicular lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of follicular lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of follicular lymphoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory microenvironment of follicular lymphoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of follicular lymphoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of follicular lymphoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microenvironment and stromal interactions of follicular lymphoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Microenvironment dependence: follicular lymphoma relies on its germinal-centre-like niche, and MHC class II antigen presentation to follicular helper T cells sustains it, while MHC loss accompanies transformation and immune escape.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell therapies: IL-2-driven T-cell expansion powers the CD19 CAR-T and CD20xCD3 bispecific therapies (perforin already mapped) increasingly used for relapsed follicular lymphoma.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Immune checkpoint: CTLA-4 on the regulatory T cells enriched in the follicular lymphoma microenvironment helps the tumour evade immunity, part of the immunosuppressive niche that distinguishes this microenvironment-dependent lymphoma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow involvement: paratrabecular bone-marrow infiltration by follicular lymphoma and its immunochemotherapy lower haemoglobin, the anaemia with other cytopenias marking advanced disease and treatment toxicity.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin in R-CHOP regimens for follicular lymphoma is cardiotoxic, and troponin elevation helps detect the myocardial injury that constrains anthracycline use in this often long-lived indolent lymphoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis on transformation: when follicular lymphoma transforms to aggressive disease (DLBCL already mapped) and is treated, the rapid cell lysis releases purines that xanthine oxidase converts to uric acid, risking tumour-lysis syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 microenvironment: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine milieu of the follicular helper T cells (already mapped) that support the follicular lymphoma clone in its germinal-centre-like niche.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the follicular lymphoma microenvironment, part of the supportive stroma of this indolent lymphoma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Immunosuppressive eicosanoids: prostaglandin E2 in the follicular lymphoma microenvironment (IL-10 already mapped) dampens the anti-tumour immune response, part of the immune tolerance that sustains the indolent clone.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the lymphoma cells, part of the bone-marrow (already mapped) microenvironment that supports the indolent follicular lymphoma clone.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the lymphoma cells, part of the metabolic microenvironment of follicular lymphoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and contributes, with the marrow involvement, to the anaemia (haemoglobin already mapped) of follicular lymphoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of follicular lymphoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon immunity: type-I interferon shapes the innate-immune tumour microenvironment and underlay the historical interferon therapy of follicular lymphoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and lymphocyte immunity: zinc is essential for the lymphocyte biology and immune function, and disturbed zinc status accompanies the immune dysfunction of follicular lymphoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm of the anti-lymphoma immunity of follicular lymphoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the follicular-lymphoma microenvironment, opposing the immunosuppressive (IL-10 already mapped) milieu.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium immune status: the selenium selenoprotein antioxidant defence supports the lymphocyte (zinc already mapped) immune function disturbed in follicular lymphoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the follicular-lymphoma microenvironment.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the reactive T-cell microenvironment of follicular lymphoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the follicular-lymphoma microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Anti-CD20 CDC: the complement C5 and the terminal MAC (with C3 already mapped) mediate the complement-dependent cytotoxicity of the anti-CD20 (rituximab/obinutuzumab; CD20 already mapped) therapy of follicular lymphoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling shapes the myeloid and macrophage response within the immune microenvironment of follicular lymphoma.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Prognostic vitamin: the low vitamin D status is associated with a worse outcome in follicular lymphoma and modulates the immune microenvironment and the response to the immunochemotherapy.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the follicular-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 (already mapped) complement-dependent killing by obinutuzumab and rituximab.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway that mediates the anti-CD20 (already mapped) complement-dependent cytotoxicity of follicular lymphoma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the marrow-involved follicular lymphoma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Stromal matricellular: periostin, a matricellular mediator, is part of the stromal remodelling of the follicular-lymphoma nodal microenvironment on which the tumour depends.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Nodal architecture: collagen, the extracellular-matrix scaffold, supports the follicular dendritic-cell network and the nodal architecture of the follicular-lymphoma microenvironment.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — FDC-network matrix: fibronectin, an extracellular-matrix glycoprotein, is part of the provisional matrix of the follicular dendritic-cell network that nurtures the follicular-lymphoma cells.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-FL axis: TSLP, from the follicular-lymphoma stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive tumour microenvironment of follicular lymphoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-FL axis: bradykinin, via B1/B2 receptors on follicular-lymphoma tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability, tumour oedema, and the inflammatory milieu of the follicular-lymphoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-FL axis: erythropoietin, via the EPOR on follicular-lymphoma B cells (already mapped), activates the PI3K/AKT (already mapped) survival axis and modulates macrophage (already mapped) polarisation in the anaemia of follicular lymphoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-FL axis: histamine, from mast cells in the follicular-lymphoma microenvironment, signals via H1/H2 receptors on malignant B cells (already mapped) and tumour endothelium, modulating BCL2-driven (already mapped) survival and the immunosuppressive FL milieu.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-FL axis: melatonin, via MT1/MT2 receptors on follicular-lymphoma B cells, modulates circadian immune rhythms, suppresses BCL2-driven (already mapped) anti-apoptotic signalling, and enhances the sensitivity to anti-CD20 (rituximab) chemoimmunotherapy.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-FL axis: testosterone, via androgen receptor signalling on follicular-lymphoma B cells and stromal cells, modulates BCL2-driven (already mapped) lymphoma-cell survival and the sex-biased immune microenvironment of follicular lymphoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — FL prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) survival cascade of follicular lymphoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — FL oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) cascade of follicular lymphoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — FL vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) proliferation cascade of FL.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — FL serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) B-cell (already mapped) survival cascade of follicular lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — FL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and B-cell (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) survival cascade of follicular lymphoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — FL sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the B-cell (already mapped) survival cascade of follicular lymphoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — FL magnesium: magnesium cofactors kinase signalling in B-cells (already mapped) and macrophages (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — FL copper: copper, via ceruloplasmin in macrophages (already mapped) and B-cells (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — FL potassium: potassium regulates macrophage (already mapped) and B-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — FL chloride: chloride channels on B-cells (already mapped) and macrophages (already mapped) regulate apoptotic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — FL sulfur: glutathione from sulfur amino acids in macrophages (already mapped) and B-cells (already mapped) counters ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell survival cascade of follicular lymphoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — FL nitrogen: nitric oxide from iNOS in macrophages (already mapped) modulates anti-tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell (already mapped) cascade of follicular lymphoma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — FL carbon: carbon in nucleotides of B-cells (already mapped) and macrophages (already mapped) fuels malignant proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — FL hydrogen: hydrogen via ROS from macrophages (already mapped) and B-cells (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) B-cell cascade of follicular lymphoma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — FL oxygen: oxygen drives B-cell (already mapped) and macrophage (already mapped) mitochondrial metabolism, supporting tumour growth; oxygen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) cascade of follicular lymphoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — follicular-lymphoma glp-1: GLP-1 from macrophages (already mapped) and B-cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) lymphoma cascade in follicular lymphoma.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — follicular-lymphoma angiotensin-ii: angiotensin II on B-cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — follicular-lymphoma wnt-beta-catenin: WNT/β-catenin on B-cells (already mapped) and macrophages (already mapped) promotes growth; wnt-beta-catenin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — follicular-lymphoma rankl: RANKL from macrophages (already mapped) and B-cells (already mapped) promotes osteoclast activation; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — follicular-lymphoma igf-1: IGF-1 from macrophages (already mapped) and B-cells (already mapped) promotes lymphoma survival; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — follicular-lymphoma activin-a: activin-A from macrophages (already mapped) and B-cells (already mapped) promotes lymphoma-stromal invasion; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — follicular-lymphoma cgrp: CGRP from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — follicular-lymphoma calcitonin: calcitonin from macrophages (already mapped) and B-cells (already mapped) modulates calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — follicular-lymphoma substance-p: substance-P from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in follicular lymphoma.
- `connects-to` → **[Insulin-Receptor](../../03-molecular/insulin-receptor/README.md)** — follicular-lymphoma insulin-receptor: insulin receptor on macrophages (already mapped) and B-cells (already mapped) modulates lymphoma metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — follicular-lymphoma aldosterone: aldosterone from macrophages (already mapped) and B-cells (already mapped) modulates lymphoma fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — follicular-lymphoma androgen-receptor: androgen receptor on macrophages (already mapped) and B-cells (already mapped) modulates lymphoma androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and BCL-2 (already mapped) cascade in FL.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^marcus-2017-gallium]: Marcus R, Davies A, Ando K, et al. Obinutuzumab for the first-line treatment of follicular lymphoma. *N Engl J Med.* 2017;377(14):1331-1344. [doi:10.1056/NEJMoa1614598](https://doi.org/10.1056/NEJMoa1614598) · [PubMed 28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/)
[^morschhauser-2020-tazemetostat]: Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003). *Lancet Oncol.* 2020;21(11):1433-1442. [doi:10.1016/S1470-2045(20)30441-1](https://doi.org/10.1016/S1470-2045(20)30441-1) · [PubMed 33035457](https://pubmed.ncbi.nlm.nih.gov/33035457/)
