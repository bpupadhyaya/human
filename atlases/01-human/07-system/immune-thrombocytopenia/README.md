---
schema: human-scale-entry/v1
id: immune-thrombocytopenia
name: Immune Thrombocytopenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Immune thrombocytopenia (ITP): anti-platelet IgG (anti-GPIIb/IIIa) → FcγR-mediated splenic destruction + CD8+ T-cell lysis; platelet <100×10⁹/L. Corticosteroids/IVIG first-line; romiplostim, eltrombopag (TPO-RAs); efgartigimod (FcRn inhibitor; FDA Jun 2023)."
aliases: ["ITP", "immune thrombocytopenic purpura", "idiopathic thrombocytopenic purpura", "primary ITP", "anti-platelet antibody"]
sources:
  - id: cines-2002-itp-review
    type: peer-reviewed
    cite: "Cines DB, Blanchette VS. Immune thrombocytopenic purpura. N Engl J Med. 2002;346(13):995-1008."
    doi: "10.1056/NEJMra010532"
    pmid: "11919310"
  - id: neunert-2019-ash-itp-guidelines
    type: peer-reviewed
    cite: "Neunert C, Terrell DR, Arnold DM, et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. Blood Adv. 2019;3(23):3829-3866."
    doi: "10.1182/bloodadvances.2019000966"
    pmid: "31794604"
  - id: bussel-2006-romiplostim-itp
    type: peer-reviewed
    cite: "Bussel JB, Kuter DJ, George JN, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. N Engl J Med. 2006;355(16):1672-1681."
    doi: "10.1056/NEJMoa054626"
    pmid: "17050891"
  - id: cheng-2011-eltrombopag-raise
    type: peer-reviewed
    cite: "Cheng G, Saleh MN, Marcher C, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE). Lancet. 2011;377(9763):393-402."
    doi: "10.1016/S0140-6736(10)60959-2"
    pmid: "21237459"
cross_links:
  - target: 01-human/03-molecular/thrombopoietin
    relation: modulated-by
    note: "Anti-platelet IgG destroys platelets faster than compensatory TPO can restore them; romiplostim (FDA Aug 2008) and eltrombopag RAISE (FDA Nov 2008) bypass antibody-mediated destruction by stimulating c-Mpl on megakaryocyte progenitors; avatrombopag is also approved."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn recycles anti-GPIIb/IIIa IgG, sustaining pathogenic platelet antibody titers; efgartigimod (ADVANCE-SC: sustained platelet response ~22% vs ~5%; FDA Jun 2023) accelerates IgG catabolism → lower anti-platelet antibody levels; rozanolixizumab under investigation in ITP."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "Pathogenic anti-GPIIb/IIIa IgG (and anti-GPIb/IX IgG) opsonizes platelets for FcγRIII-mediated splenic macrophage phagocytosis; IVIG (2 g/kg) blocks Fc receptors and provides anti-idiotypic antibodies; rituximab (anti-CD20) depletes anti-platelet IgG-secreting B cells."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for FcγR-mediated splenic destruction and CD8+ T-cell lysis; resulting thrombocytopenia causes mucocutaneous bleeding; ITP management targets platelet count >50×10⁹/L (safe for most activities) or >100×10⁹/L (surgery)."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is the engine of ITP: red-pulp macrophages phagocytose IgG-opsonized platelets via FcγRIII, and splenic autoreactive B cells are a primary antibody source; splenectomy removes both and gives durable remission in ~60-70%, though now used later given effective TPO-RAs."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Splenic macrophages drive platelet destruction in ITP — FcγRIII (CD16) on red-pulp macrophages binds IgG-opsonized platelets → phagocytosis; IVIG works by Fc-receptor blockade and fostamatinib by inhibiting macrophage SYK signaling downstream of FcγR, both sparing platelets."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "H. pylori is a cause of secondary ITP (~40-60% seropositive in endemic regions); eradication normalizes platelets in ~half of seropositive patients, likely by removing molecular-mimicry antigens and polyclonal B-cell stimulation, so ASH advises testing all ITP patients."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Immune thrombocytopenia and IgA nephropathy are both antibody-mediated autoimmune diseases: ITP from anti-platelet IgG driving splenic destruction, IgAN from galactose-deficient IgA1 immune complexes in the kidney — distinct antigens, but both respond to B-cell-directed therapy."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Autoreactive B cells are the source of ITP's anti-platelet antibodies, so B-cell depletion with rituximab (anti-CD20) raises platelet counts in ~60% of patients; splenic B cells are a major antibody factory, part of why splenectomy works — both attack the antibody supply."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "ITP is often secondary to systemic lupus erythematosus: thrombocytopenia is a diagnostic criterion for SLE and can be its presenting feature; ITP plus autoimmune hemolytic anemia is termed Evans syndrome, so new-onset ITP warrants screening for connective-tissue disease."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hepatitis C is a leading cause of secondary immune thrombocytopenia: the virus drives anti-platelet antibodies and immune-complex clearance (with hypersplenism and low thrombopoietin), so HCV testing is routine in new ITP and antiviral cure often raises the platelet count."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Immune thrombocytopenia is a classic autoimmune complication of CLL: the dysregulated malignant B cells break tolerance and drive anti-platelet antibodies, producing thrombocytopenia out of proportion to marrow infiltration; it responds to steroids, rituximab or treating the CLL."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "ITP is not just platelet destruction but impaired production: anti-platelet antibodies also damage bone-marrow megakaryocytes and blunt output, and thrombopoietin is inappropriately low—why TPO-receptor agonists (eltrombopag, romiplostim) that stimulate megakaryocytes work."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "ITP and TTP both cause thrombocytopenia but are opposite emergencies: ITP is antibody-mediated platelet destruction, while TTP is ADAMTS13 deficiency forming microthrombi that consume platelets—TTP adds hemolysis and needs urgent plasma exchange."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "ITP and DIC are both thrombocytopenias distinguished by coagulation testing: ITP is immune platelet destruction with normal clotting times, while DIC consumes platelets and clotting factors, prolonging PT/PTT with high D-dimer—the coagulation panel separates them."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "ITP and antiphospholipid syndrome overlap: many ITP patients carry antiphospholipid antibodies, and APS itself can cause moderate thrombocytopenia, yet APS's danger is clotting, not bleeding—so a thrombocytopenic patient who also clots should be tested for them."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells fuel ITP by making anti-platelet antibodies: long-lived autoantibody-secreting plasma cells (some splenic) coat platelets for destruction, and because they resist rituximab, plasma-cell-directed or splenectomy approaches address refractory ITP."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a classic secondary cause of immune thrombocytopenia: the virus drives anti-platelet antibodies and impairs production, so new thrombocytopenia warrants HIV testing—and antiretroviral therapy often restores the platelet count better than immunosuppression."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells license the autoimmunity of ITP: loss of tolerance lets Th cells help B cells make anti-platelet antibodies and skews regulatory balance, so therapies restoring immune regulation, not just removing antibody, are increasingly used in ITP."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immune thrombocytopenia is an autoimmune disease of platelet destruction: autoantibodies and T cells target platelet glycoproteins, clearing them in the spleen while also impairing production—so it joins the antibody-mediated cytopenias treated by immunosuppression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The feared complication of immune thrombocytopenia is bleeding into the nervous system: although rare, intracranial hemorrhage from very low platelets is the main life-threatening risk, so severe thrombocytopenia with neurological signs is a medical emergency."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Viral infection commonly triggers immune thrombocytopenia: especially in children, EBV and other viruses provoke cross-reactive antiplatelet antibodies, causing an acute, often self-limited ITP—molecular mimicry turning antiviral immunity against platelets."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "ITP is not only antibody-driven: cytotoxic CD8 T cells can directly lyse platelets and attack marrow megakaryocytes, explaining cases with low platelet antibodies and the variable response to therapies aimed only at antibody production."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "Childhood ITP often follows infection or vaccination: measles and other viruses (and the MMR vaccine) can trigger transient antiplatelet antibodies, causing self-limited thrombocytopenia weeks later—usually resolving without treatment, unlike chronic adult ITP."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "ITP crosses the placenta: maternal anti-platelet IgG passes to the fetus and can lower the newborn's platelets, so pregnant patients need monitoring—distinct from neonatal alloimmune thrombocytopenia, where the mother targets paternal platelet antigens."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Immune thrombocytopenia is first treated with cortisol's kin: corticosteroids dampen the antibody response and the macrophage clearance of platelets, raising counts as the standard first-line therapy for symptomatic ITP."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "ITP stems from failed tolerance by regulatory T cells: deficient or dysfunctional Tregs let the immune system make antibodies against the body's own platelets, so restoring regulatory T-cell control is an emerging therapeutic goal."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver quietly governs platelet counts in ITP: it makes most of the body's thrombopoietin and helps clear antibody-coated platelets, so liver function shapes both platelet production and destruction in the disease."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab treats ITP by deleting B cells via CD20: stripping the antibody-producing B cells lowers the anti-platelet autoantibodies, a second-line option that can give durable remissions in immune thrombocytopenia."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ITP's most feared danger is bleeding into the brain: though rare, intracranial hemorrhage from the very low platelet count is the leading cause of death, which is why severe thrombocytopenia is treated urgently."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help break self-tolerance in ITP: by presenting platelet antigens to T cells they license the autoimmune response that drives B cells to make anti-platelet antibodies, a step upstream of the destruction."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chronic ITP can drain iron: ongoing mucosal and menstrual bleeding from the very low platelet count slowly depletes the body's iron, adding deficiency anemia to the thrombocytopenia."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "ITP shows first on the skin: pinpoint petechiae and bruising purpura, the bleeding into skin from too few platelets, are the cardinal visible sign that brings patients in."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "ITP destroys platelets partly through complement: antibody-coated platelets can fix complement C3, marking them for a second route of clearance beyond the spleen's macrophages."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "When ITP is unclear the marrow is checked under the microscope: it shows plentiful megakaryocytes, confirming platelets are being destroyed in the periphery rather than underproduced."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "ITP can bleed into the gut: severe thrombocytopenia causes gastrointestinal hemorrhage, one of the dangerous internal bleeds beyond the visible skin purpura."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "ITP's autoantibodies are made in germinal centers: spleen B cells there produce the anti-platelet antibodies, which is why splenectomy and B-cell-depleting rituximab can control it."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows ITP's two-front problem: spleen macrophages devour antibody-coated platelets, while the marrow's megakaryocytes — normal or increased in number — are themselves hampered from releasing new ones."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Very low platelets can bleed into the eye: retinal and conjunctival hemorrhages appear in severe ITP, a visible warning of the bleeding risk that, at its worst, threatens intracranial hemorrhage."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "ITP can show up as blood in the urine: profound thrombocytopenia causes mucosal and urinary-tract bleeding, hematuria being one of the wet-purpura signs that signals a dangerously low count."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "ITP is an autoantibody disease: IgG antibodies against platelet glycoproteins GPIIb/IIIa and GPIb tag platelets for splenic destruction and also stunt megakaryocytes, which is why anti-CD20 and IVIG therapies work by removing or blockading that antibody."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "When the same autoimmunity also targets red cells, ITP becomes Evans syndrome: simultaneous immune destruction of platelets and erythrocytes (autoimmune hemolytic anemia), a more refractory combined cytopenia hinting at an underlying lymphoma or lupus."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Low vitamin D tracks with autoimmunity: deficiency is common in chronic ITP and, by tilting regulatory-T-cell balance, is studied as a modifier of the immune dysregulation that lets antibodies turn against the body's own platelets."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "ITP complicates pregnancy two ways: it must be told apart from benign gestational thrombocytopenia, and the platelet-targeting IgG crosses the placenta to lower the baby's count, so mother and newborn are both watched around delivery."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "Blocking BTK hits ITP from both sides: the kinase drives B-cell antibody production and the macrophage Fc-receptor signaling that destroys platelets, so BTK inhibitors like rilzabrutinib are an emerging targeted treatment."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Childhood ITP often follows a virus: acute self-limited ITP classically appears a week or two after infections such as varicella, when antibodies raised against the virus cross-react with platelets before fading as the child recovers."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Two ways to run out of platelets: ITP destroys them in the periphery while the marrow works overtime, whereas aplastic anemia fails to make them at all — the contrast drives the bone-marrow exam that distinguishes peripheral destruction from production failure."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Destruction is not antibody alone: natural killer and cytotoxic cells contribute to platelet clearance and to the dysregulated immunity of ITP, part of why some cases resist antibody-focused treatments and need broader immune suppression."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Bleeding turns on what platelets grip: von Willebrand factor is the glue platelets use to plug vessels, so when ITP drops the platelet count the vWF-platelet plug fails, producing the bruising and mucosal bleeding that define the disease's danger."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement helps clear the platelets: antiplatelet antibodies fix complement to opsonize and lyse platelets in ITP, a pathway that complement inhibitors (e.g. sutimlimab) are explored to interrupt."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A bleeding disorder that paradoxically clots: ITP carries a raised thrombosis risk, amplified by thrombopoietin-receptor agonists and splenectomy, so venous thromboembolism is a real hazard even amid low platelets."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection and its vaccines can trigger it: COVID-19, like other viral illnesses, precipitates secondary immune thrombocytopenia, and rare post-vaccination ITP is recognized — examples of infection-driven autoimmunity against platelets."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Dysregulated T-cell signaling underlies the autoimmunity: STAT3 activation in the T and B cells of ITP supports the autoreactive response that makes anti-platelet antibodies, part of the immune imbalance behind the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Immune activation runs through NF-κB: B-cell and macrophage NF-κB signaling sustains the autoantibody production and Fc-receptor-mediated platelet destruction that define immune thrombocytopenia."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Removing the spleen and suppressing immunity raise infection risk: splenectomy for refractory ITP leaves patients prone to overwhelming post-splenectomy infection, and rituximab and steroids add further sepsis risk."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "It can be the first sign of HIV: HIV is a classic cause of secondary immune thrombocytopenia, sometimes the presenting feature, so HIV testing is part of the standard ITP workup."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its B-cell-directed therapy opens the lung: the rituximab and prolonged steroids used in refractory ITP deplete immune defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A relapsing disease and its steroids weigh on mood: the unpredictable bleeding risk, activity restrictions and mood effects of chronic corticosteroids in ITP contribute to depression and reduced quality of life."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It threatens the brain from both directions: severe thrombocytopenia risks intracranial hemorrhage, while the TPO-receptor agonists used to raise platelets and post-splenectomy state carry a thrombotic stroke risk."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its immunosuppression opens the lung to mold: the high-dose corticosteroids and rituximab used to treat ITP blunt immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Prolonged steroids thin the bones: the repeated and long courses of corticosteroids used to control ITP accelerate bone loss and raise fracture risk."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Low platelets bleed into the skin: ITP causes petechiae, purpura and easy bruising, and the wet purpura of mucosal and oral bleeding signals a dangerously low platelet count."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It bleeds the gut and ties to H. pylori: severe thrombocytopenia in ITP risks gastrointestinal haemorrhage, and eradicating Helicobacter pylori can raise the platelet count in many patients."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Living with a bleeding risk breeds worry: the unpredictable platelet counts, fear of haemorrhage and relapsing course of ITP foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The spleen is its engine: the spleen is the principal site where antibody-coated platelets are destroyed and where the autoantibodies are made, which is why splenectomy is a long-standing treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with autoimmune glands: ITP commonly coexists with autoimmune thyroid disease and other autoimmunity, reflecting a broader autoimmune predisposition."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its platelet-boosting drugs can scar the marrow: the thrombopoietin-receptor agonists eltrombopag and romiplostim can cause bone-marrow reticulin fibrosis with long-term use."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "First-line lifts the platelets: corticosteroids are the initial treatment for immune thrombocytopenia, dampening the autoimmune platelet destruction, with IVIG added for urgent rises."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment can swing toward clotting: the thrombopoietin-receptor agonists used in chronic ITP raise platelet counts but carry a thrombotic and cardiovascular risk."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Bleeding and overlap reach the kidney: ITP can cause haematuria, and when it accompanies lupus or Evans syndrome a coexisting glomerulonephritis may be present."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "A virus that lowers the platelets: chronic hepatitis C is a recognised secondary cause of immune thrombocytopenia, and treating the infection often raises the platelet count."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "A thrombocytopenia that clots instead of bleeds: unlike immune thrombocytopenia, heparin-induced thrombocytopenia causes thrombosis, a key contrast in the workup of a falling platelet count."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cytotoxic immunosuppression for refractory disease: vincristine, cyclophosphamide and azathioprine are used in immune thrombocytopenia that resists steroids and first-line agents."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: connects-to
    note: "Pulsed steroids to reset immunity: high-dose dexamethasone given in short 4-day pulses is a standard first-line treatment for immune thrombocytopenia, raising platelet counts faster and with fewer long-term effects than prolonged daily prednisone."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Low platelets as a paraneoplastic clue: immune thrombocytopenia can arise secondary to lymphoproliferative disease, including Hodgkin lymphoma, where disordered immunity generates anti-platelet antibodies—so refractory ITP warrants a search for hidden lymphoma."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Autoimmunity that also attacks platelets: like SLE, rheumatoid arthritis can drive secondary immune thrombocytopenia, and in Felty syndrome RA combines with splenomegaly and cytopenias—the same spleen that destroys antibody-coated platelets in ITP."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "A mimic to exclude: isolated thrombocytopenia in myelodysplastic syndrome can mimic ITP, and the two are distinguished by marrow examination—essential before immunosuppressing a presumed ITP."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Secondary ITP: indolent B-cell lymphomas like follicular lymphoma (and CLL) can trigger secondary immune thrombocytopenia through dysregulated antibody-producing B cells."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Where thrombopoietin is made: TPO, the platelet growth factor that is inappropriately low relative to need in ITP, is produced constitutively by the hepatic lobule, so liver disease lowers platelet counts."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Central versus peripheral: myelofibrosis crowds out megakaryocytes for a production-failure low platelet count, the marrow-failure differential to distinguish from the peripheral antibody-mediated platelet destruction of ITP."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Infection-driven thrombocytopenia: dengue causes profound platelet falls through immune-mediated destruction and marrow suppression, a leading infectious mimic of ITP in endemic regions."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Secondary ITP from lymphoma: low-grade B-cell malignancies like Waldenstrom macroglobulinaemia can drive autoimmune platelet destruction, so a new ITP in an older adult warrants screening for an underlying lymphoproliferative disorder."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "HIV-associated ITP: HIV is a recognised cause of secondary immune thrombocytopenia, sometimes its presenting feature, and the platelet count often improves with antiretroviral therapy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1-skewed autoimmunity: an IFN-γ-dominated cytokine profile drives the autoreactive T-cell help and macrophage activation that destroy antibody-coated platelets in ITP."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival factor: BAFF sustains the autoreactive B cells producing anti-platelet antibodies in ITP, part of the rationale for B-cell-directed therapy."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic platelet lysis: beyond antibody-mediated clearance, CD8 cytotoxic T cells use perforin to directly lyse platelets and megakaryocytes in ITP."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory dysregulation: IL-6 contributes to the loss of immune tolerance in ITP, supporting the autoreactive T- and B-cell responses against platelets."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Immune activation: elevated TNF-α reflects the inflammatory immune dysregulation of ITP, promoting macrophage-mediated platelet destruction."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet activation and antigen: PF4 from activated platelets marks the platelet activation in ITP and anchors the antigenic overlap with PF4-driven HIT and VITT that the disorder is distinguished from."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Regulatory T-cell deficit: defective IL-2-dependent regulatory T cells permit the antiplatelet autoimmunity of ITP, and low-dose IL-2 to expand Tregs is under investigation as therapy."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Autoantigen presentation: MHC class II presentation of platelet-glycoprotein peptides to CD4 T cells licenses the B cells that make the anti-GPIIb/IIIa autoantibodies of ITP."
  - target: 01-human/03-molecular/mpl
    relation: connects-to
    note: "Production boost: thrombopoietin-receptor agonists (eltrombopag, romiplostim) stimulate MPL on megakaryocytes to raise platelet production in ITP, a paradigm shift from suppressing destruction to driving production."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Impaired production and apoptosis: antiplatelet antibodies also impair megakaryocyte platelet release and trigger caspase-3-mediated platelet apoptosis, so ITP thrombocytopenia reflects underproduction as well as destruction."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Splenic clearance: CCL2 helps recruit the splenic macrophages that phagocytose antibody-opsonised platelets through their Fcγ receptors, the principal site of the accelerated platelet destruction in ITP."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "First-line therapy: corticosteroids acting through the glucocorticoid receptor are first-line for immune thrombocytopenia, dampening autoantibody production and macrophage Fcγ-receptor-mediated platelet phagocytosis to raise the platelet count."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Plasma-cell persistence: long-lived anti-platelet plasma cells survive on BCL-2 and lack CD20, so they escape rituximab — the basis for relapses after B-cell depletion in ITP and the rationale for plasma-cell-directed approaches."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "FcγR signalling: macrophage Fcγ-receptor engagement by antibody-coated platelets signals through Src-family and Syk kinases to trigger phagocytosis, the pathway the Syk inhibitor fostamatinib blocks to reduce platelet destruction in ITP."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Failed regulation: regulatory T cells and their IL-10 are deficient in immune thrombocytopenia, removing a brake that normally restrains the autoreactive anti-platelet response."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Tolerance checkpoint: impaired CTLA-4-dependent regulatory T-cell control contributes to the breakdown of self-tolerance that allows anti-platelet autoantibodies to arise in ITP."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 skew: an IL-17-producing Th17 skew accompanies the Th1-dominated immune dysregulation of ITP, adding to the inflammatory imbalance behind platelet autoimmunity."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Thrombopoietin signalling: thrombopoietin acting through the MPL receptor and JAK-STAT (MPL and STAT3 already mapped) drives megakaryopoiesis, the pathway harnessed by TPO-receptor agonists to raise platelet counts in ITP."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12-driven Th1 polarisation (IFN-γ already mapped) skews the autoimmune response that targets platelets for destruction in immune thrombocytopenia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint tolerance: impaired PD-1 and other inhibitory-checkpoint control of autoreactive T and B cells contributes to the loss of self-tolerance underlying immune thrombocytopenia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling downstream of BAFF and the TPO receptor MPL (both mapped) participates in both the autoimmunity and the megakaryocyte responses of immune thrombocytopenia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR-regulated T-cell metabolism shapes the regulatory-T-cell deficiency of ITP, and mTOR inhibition (sirolimus) restores tolerance in refractory disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the macrophage-mediated platelet clearance and immune dysregulation of immune thrombocytopenia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the dysregulated T-cell and interferon response that drives the anti-platelet autoimmunity of immune thrombocytopenia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the loss of tolerance and inflammatory tone of immune thrombocytopenia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) supports the survival of the autoreactive B and T cells driving immune thrombocytopenia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the autoreactive lymphocyte tolerance and survival balance relevant to the anti-platelet antibody production of immune thrombocytopenia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling shapes the regulatory-T-cell control whose deficiency permits the autoimmunity of immune thrombocytopenia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the innate inflammatory activation accompanying immune thrombocytopenia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the T-cell and B-cell inflammatory signaling that drives the autoantibody response of immune thrombocytopenia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of the B-cell and Fc receptors participates in the immune activation of immune thrombocytopenia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates megakaryocyte and immune-cell survival relevant to the impaired platelet production of immune thrombocytopenia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism of immune thrombocytopenia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte trafficking participates in the immune dysregulation of immune thrombocytopenia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the autoreactive immune response in immune thrombocytopenia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the megakaryocyte and bone-marrow-niche interactions relevant to immune thrombocytopenia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune dysregulation of immune thrombocytopenia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the inflammatory milieu of immune thrombocytopenia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses of immune thrombocytopenia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of immune thrombocytopenia, and calcineurin inhibitors are used in refractory disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation of immune thrombocytopenia."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Evans syndrome: when immune thrombocytopenia occurs together with autoimmune haemolytic anaemia (Evans syndrome), haemoglobin falls alongside the platelets, reflecting a broader breakdown of tolerance to blood-cell antigens."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Autoantibody help: Th2 cytokines including IL-4 support the B cells that produce the anti-platelet (anti-GPIIb/IIIa) autoantibodies (IgG already mapped) central to the platelet destruction of immune thrombocytopenia."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Female predominance: immune thrombocytopenia, like many autoimmune diseases, is more common in young women, and estrogen's enhancement of antibody responses is thought to contribute to this sex difference in susceptibility."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "TTP differential: a normal ADAMTS13 distinguishes immune thrombocytopenia from thrombotic thrombocytopenic purpura, where its severe deficiency lets von Willebrand factor (already mapped) multimers consume platelets, the key differential of an isolated low count."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet granule store: platelets are the body's main reservoir of serotonin in their dense granules, so the platelet destruction of immune thrombocytopenia depletes this store, one facet of the loss of platelet function beyond the low count."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 autoantibody help: IL-13, with the IL-4 (already mapped) type-2 response, supports the B cells producing the anti-platelet autoantibodies that drive the platelet destruction of immune thrombocytopenia."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "GPIIb/IIIa target: fibrinogen bridges platelets by binding the GPIIb/IIIa integrin that is itself the main antigen of the anti-platelet autoantibodies, so the destruction and dysfunction of platelets in immune thrombocytopenia impairs this aggregation."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Thromboxane and platelet function: activated platelets generate thromboxane A2 to amplify aggregation, and the loss of platelet numbers and function in immune thrombocytopenia diminishes this eicosanoid arm of haemostasis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial platelet control: endothelial nitric oxide normally inhibits platelet activation, part of the vascular regulation of the platelets whose autoimmune destruction defines immune thrombocytopenia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Regulatory tolerance: TGF-β, with IL-10 (already mapped), enforces the regulatory-T-cell tolerance whose failure permits the anti-platelet autoimmunity of immune thrombocytopenia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Megakaryocyte niche: VEGF supports the marrow vascular niche of the megakaryocytes, and the impaired platelet production (thrombopoietin already mapped) of immune thrombocytopenia involves this microenvironment as well as the autoantibody attack."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon dysregulation: type-I interferon signalling is implicated in the loss of tolerance of immune thrombocytopenia, and interferon therapy can itself precipitate the autoimmune platelet destruction."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin modulates the autoreactive T-cell (already mapped) response implicated in immune thrombocytopenia, part of the metabolic-immune axis of the autoimmune disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the autoimmune immune thrombocytopenia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) accompanying immune thrombocytopenia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the T-helper imbalance (with the Th1 IFN-γ already mapped) that skews the autoimmune response of immune thrombocytopenia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Th2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the T-helper cytokine balance dysregulated in immune thrombocytopenia."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Inflammatory iron: the IL-6-driven (already mapped) hepcidin of the systemic inflammation accompanying immune thrombocytopenia contributes to any concurrent anaemia of chronic disease."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Thrombopoietin source: the hepatocytes are the main source of the thrombopoietin (already mapped), the MPL (already mapped) ligand whose relatively low level (the failure to compensate) contributes to the impaired platelet production of immune thrombocytopenia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 dimension of the T-helper cytokine dysregulation of immune thrombocytopenia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell/allergic arm: histamine, released by the mast cells and basophils, is part of the type-2/allergic component contributing to some (e.g. drug-induced) forms of immune thrombocytopenia."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Innate/FcγR arm: the neutrophils, via their Fcγ receptors, participate in the innate immune dysregulation and the drug-induced forms of immune thrombocytopenia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated platelet destruction of immune thrombocytopenia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the micronutrient dimension of the immune dysregulation of immune thrombocytopenia."
---

# Immune Thrombocytopenia

## Overview

Immune thrombocytopenia (ITP) is an autoimmune disorder characterized by isolated thrombocytopenia (platelet count <100 × 10⁹/L) caused by autoantibody-mediated platelet destruction and impaired platelet production. It is the most common acquired thrombocytopenic disorder, with a prevalence of approximately 5–10 per 100,000 adults and 3–5 per 100,000 children [^cines-2002-itp-review]. ITP is clinically heterogeneous, ranging from an incidental laboratory finding in asymptomatic patients to life-threatening intracranial hemorrhage.

ITP is classified as:
- **Primary ITP**: No identifiable underlying cause (~80%)
- **Secondary ITP**: Associated with systemic lupus erythematosus (SLE), antiphospholipid syndrome, CLL, HIV, HCV, Helicobacter pylori infection, or drug exposure

By chronicity:
- **Newly diagnosed**: <3 months
- **Persistent**: 3–12 months (not spontaneously remitting)
- **Chronic**: >12 months

The discovery that **FcRn inhibition** (efgartigimod alfa, rozanolixizumab) accelerates catabolism of pathogenic anti-platelet IgG has established ITP as a flagship indication for the growing class of FcRn inhibitors, alongside myasthenia gravis, CIDP, and pemphigus [^neunert-2019-ash-itp-guidelines].

## Structure

### Pathogenic Mechanism — Three Pillars

ITP pathogenesis involves three interconnected immune abnormalities [^cines-2002-itp-review]:

**Pillar 1 — Anti-platelet antibodies:**
- **Anti-GPIIb/IIIa** (integrin αIIbβ3): Most common; present in ~60–70% of ITP patients
- **Anti-GPIb/IX**: ~20–40%; particularly important in MuSK-analogous IgG4-mediated functional blockade
- IgG1 and IgG3 (complement-activating subclasses) are the dominant pathogenic antibodies
- These antibodies are produced by autoreactive B cells in the spleen (primary site) and bone marrow
- Anti-GPIIb/IIIa IgG can also directly inhibit platelet aggregation → functional platelet impairment beyond reduced count

**Pillar 2 — FcγR-mediated platelet destruction:**
- IgG-opsonized platelets → **FcγRIII (CD16)** on splenic red pulp macrophages → phagocytosis; splenic FcγRIIa (CD32) also contributes
- **FcRn recycling** of anti-platelet IgG maintains chronic pathogenic antibody levels — the pharmacological basis for FcRn inhibitor therapy
- IVIG (2 g/kg IV over 2 days) acutely raises platelet count by: FcγR blockade on macrophages, anti-idiotypic antibodies, and possibly inhibiting FcRn recycling temporarily

**Pillar 3 — T-cell-mediated platelet destruction:**
- CD8+ cytotoxic T cells directly lyse platelets independent of IgG (important in seronegative ITP ~30%)
- Treg dysfunction: reduced Foxp3+ Treg numbers and suppressive function → failure to restrain autoreactive B and T cells
- CD4+ Th1 skewing: elevated IFN-γ, TNF-α → further macrophage activation

### Why Megakaryopoiesis is Impaired

Despite thrombocytopenia and elevated (or inappropriately normal) TPO, platelet production is suboptimal because:
1. Anti-GPIIb/IIIa antibodies bind megakaryocyte surface GPIIb/IIIa → impair proplatelet formation
2. CD8+ T cells infiltrate bone marrow → direct megakaryocyte destruction
3. Elevated megakaryocyte c-Mpl absorbs circulating TPO → blunts the expected TPO rise

This explains the apparent paradox that TPO-RAs can still further stimulate platelet production despite "normal" or modestly elevated endogenous TPO.

## Function

ITP disrupts normal haemostasis through quantitative (low count) and qualitative (antibody-coated, dysfunctional) platelet defects:

- **Mucocutaneous bleeding** — the hallmark: petechiae, purpura, ecchymoses, gingival bleeding, epistaxis, menorrhagia
- **Visceral bleeding** — GI hemorrhage, hematuria (less common)
- **Intracranial hemorrhage (ICH)** — rare (<1–2% of ITP), life-threatening; risk correlates with platelet count <10×10⁹/L and older age; the primary indication for emergency therapy
- **Fatigue and quality of life** — prevalent even without bleeding; correlates with disease activity and anti-platelet antibody levels, not just platelet count

Platelet count thresholds guide management:
- **>100 × 10⁹/L**: Normal; no ITP by definition
- **50–100 × 10⁹/L**: Low but safe for most activities; no routine treatment needed unless symptomatic
- **20–50 × 10⁹/L**: Increased mucocutaneous bleeding risk; treatment often initiated
- **<20 × 10⁹/L**: High risk; treatment recommended
- **<10 × 10⁹/L**: Emergency treatment threshold; highest ICH risk

## Pathology

### Diagnosis — Exclusion Process

ITP is a **diagnosis of exclusion** — no single definitive test exists:

1. **Complete blood count + peripheral smear**: Isolated thrombocytopenia (no anemia, no leukopenia unless drug-induced); large platelets on smear (young platelets); normal or increased megakaryocytes on bone marrow biopsy
2. **Screening for secondary causes**: ANA (SLE), antiphospholipid antibodies, HIV, HCV, HBV, *H. pylori* antigen/antibody
3. **Bone marrow biopsy**: Not routinely required in young patients with typical ITP; indicated in patients >60 years, atypical findings, or non-response to first-line therapy to exclude MDS or lymphoma
4. **Anti-platelet antibodies**: Low sensitivity (~50–70%); positive result supports diagnosis but negative does not exclude; not routinely used in guidelines
5. **Drug history review**: Quinine, heparin (HIT), valproate, trimethoprim-sulfamethoxazole among many causes of drug-induced thrombocytopenia

### H. pylori and Secondary ITP

*H. pylori* infection is found in ~40–60% of ITP patients (in endemic populations); eradication with triple therapy achieves platelet normalization in ~50% of seropositive patients, presumably by eliminating molecular mimicry antigens and reducing polyclonal B cell stimulation. ASH 2019 guidelines recommend *H. pylori* testing and treatment in all ITP patients.

## Treatment

### First-line (Newly Diagnosed ITP)

**Corticosteroids:**
- **Dexamethasone** 40 mg/day × 4 days: rapid platelet response (>50 × 10⁹/L) in 70–80%; preferred for faster kinetics over prednisone
- **Prednisone** 1 mg/kg/day × 2–4 weeks then taper: traditional standard; higher cumulative steroid exposure
- Complete remission (platelet >100 × 10⁹/L at 6 months off therapy): ~15–25% with either regimen

**IVIG:**
- 1–2 g/kg over 1–2 days for acute severe ITP or steroid contraindications
- Rapid platelet rise (often within 24–72 h) via FcγR blockade; effect transient (2–4 weeks)
- Anti-D (WinRho): 50–75 µg/kg in Rh+ non-splenectomized patients; activates FcγR blockade via IgG-coated RBCs

### Second-line

**Splenectomy:**
- Removes primary site of anti-platelet IgG production and platelet destruction
- Complete response (no therapy, platelet >100 × 10⁹/L) in ~60–70%; durable at 5 years in ~50%
- Delayed with laparoscopic technique; preceded by pneumococcal, meningococcal, Hib vaccination

**Rituximab (anti-CD20):**
- 375 mg/m² weekly × 4 doses (lymphoma schedule) or 1000 mg × 2 doses (RA schedule)
- Initial platelet response ~60%; sustained (>1 year) response ~20–25%
- Depletes CD20+ B cells → reduces anti-platelet IgG-secreting plasma cell precursors

**TPO-receptor agonists:**
- **Romiplostim** (Nplate): SC injection weekly; platelet response 88% vs 14% in pivotal trial [^bussel-2006-romiplostim-itp]; FDA August 2008
- **Eltrombopag** (Promacta): oral daily; RAISE trial (59% vs 16% platelet response at 6 months; FDA November 2008) [^cheng-2011-eltrombopag-raise]; also useful in aplastic anemia (with horse-ATG + cyclosporine)
- **Avatrombopag** (Doptelet): oral daily; non-inferior to eltrombopag; also approved for CLD-associated thrombocytopenia pre-procedure

**Fostamatinib (Tavalisse):**
- Oral SYK (spleen tyrosine kinase) inhibitor → blocks FcγR signaling in macrophages → reduces phagocytosis of IgG-opsonized platelets
- FIT trials: 18% vs 2% complete response; FDA April 2018 for adults with chronic ITP who have failed ≥1 previous treatment

### Third-line / Novel Agents

**FcRn inhibitors:**
- **Efgartigimod alfa SC** (Vyvgart Hytrulo): ADVANCE-SC+ trial: sustained platelet response (≥2 consecutive counts ≥50×10⁹/L) ~22% vs ~5% placebo; FDA June 2023 for adults with primary ITP
- **Rozanolixizumab** (Rystiggo): MYRIAD Phase 3 ongoing for ITP; already FDA-approved for generalized MG
- Mechanism: compete with IgG for FcRn binding → IgG (including anti-platelet IgG) routed to lysosomal degradation → reduced pathogenic antibody titers

**Anti-CD38:**
- **Mezagitamab**: MAYA-2 Phase 2 trial in ITP; anti-CD38 depletes plasma cells that secrete anti-platelet IgG (analogous to daratumumab in myeloma)
- **Daratumumab**: Case reports/series in refractory ITP

### Pregnancy-Associated ITP

ITP in pregnancy carries risk of neonatal thrombocytopenia (maternal IgG crosses placenta via FcRn on syncytiotrophoblasts → anti-platelet IgG opsonizes fetal platelets). Maternal platelet count does not predict neonatal platelet count well. Management:
- Platelet >30 × 10⁹/L in first/second trimester: observe
- Target >50 × 10⁹/L for vaginal delivery; >80 × 10⁹/L for cesarean
- IVIG ± corticosteroids are preferred (avoid TPO-RAs in pregnancy; safety data lacking)
- FcRn inhibitors under investigation for prevention of neonatal ITP

## Connections

- **Modulated by** → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Anti-platelet IgG destroys platelets faster than compensatory TPO can restore them; romiplostim and eltrombopag (RAISE) bypass antibody-mediated destruction by stimulating c-Mpl on megakaryocyte progenitors; avatrombopag also approved.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn recycles anti-GPIIb/IIIa IgG sustaining pathogenic titers; efgartigimod (ADVANCE-SC: ~22% vs ~5% sustained platelet response; FDA Jun 2023) accelerates IgG catabolism → lower anti-platelet antibody levels; rozanolixizumab under investigation.
- **Modulated by** → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Pathogenic anti-GPIIb/IIIa IgG1/IgG3 opsonizes platelets for FcγRIII-mediated splenic phagocytosis; IVIG blocks Fc receptors; rituximab depletes anti-platelet IgG-secreting B cells.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for destruction; CD8+ T cells directly lyse platelets; thrombocytopenia causes mucocutaneous bleeding; ITP treatment targets platelet count >50–100×10⁹/L.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is the engine of ITP: red-pulp macrophages phagocytose IgG-opsonized platelets via FcγRIII, and splenic autoreactive B cells are a primary antibody source; splenectomy removes both and gives durable remission in ~60-70%, though now used later given effective TPO-RAs.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Splenic macrophages drive platelet destruction in ITP — FcγRIII (CD16) on red-pulp macrophages binds IgG-opsonized platelets → phagocytosis; IVIG works by Fc-receptor blockade and fostamatinib by inhibiting macrophage SYK signaling downstream of FcγR, both sparing platelets.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — H. pylori is a cause of secondary ITP (~40-60% seropositive in endemic regions); eradication normalizes platelets in ~half of seropositive patients, likely by removing molecular-mimicry antigens and polyclonal B-cell stimulation, so ASH advises testing all ITP patients.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — Immune thrombocytopenia and IgA nephropathy are both antibody-mediated autoimmune diseases: ITP from anti-platelet IgG driving splenic destruction, IgAN from galactose-deficient IgA1 immune complexes in the kidney — distinct antigens, but both respond to B-cell-directed therapy.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Autoreactive B cells are the source of ITP's anti-platelet antibodies, so B-cell depletion with rituximab (anti-CD20) raises platelet counts in ~60% of patients; splenic B cells are a major antibody factory, part of why splenectomy works — both attack the antibody supply.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — ITP is often secondary to systemic lupus erythematosus: thrombocytopenia is a diagnostic criterion for SLE and can be its presenting feature; ITP plus autoimmune hemolytic anemia is termed Evans syndrome, so new-onset ITP warrants screening for connective-tissue disease.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hepatitis C is a leading cause of secondary immune thrombocytopenia: the virus drives anti-platelet antibodies and immune-complex clearance (with hypersplenism and low thrombopoietin), so HCV testing is routine in new ITP and antiviral cure often raises the platelet count.
- `connects-to` → **[CLL](../cll/README.md)** — Immune thrombocytopenia is a classic autoimmune complication of CLL: the dysregulated malignant B cells break tolerance and drive anti-platelet antibodies, producing thrombocytopenia out of proportion to marrow infiltration; it responds to steroids, rituximab or treating the CLL.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — ITP is not just platelet destruction but impaired production: anti-platelet antibodies also damage bone-marrow megakaryocytes and blunt output, and thrombopoietin is inappropriately low—why TPO-receptor agonists (eltrombopag, romiplostim) that stimulate megakaryocytes work.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — ITP and TTP both cause thrombocytopenia but are opposite emergencies: ITP is antibody-mediated platelet destruction, while TTP is ADAMTS13 deficiency forming microthrombi that consume platelets—TTP adds hemolysis and needs urgent plasma exchange.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — ITP and DIC are both thrombocytopenias distinguished by coagulation testing: ITP is immune platelet destruction with normal clotting times, while DIC consumes platelets and clotting factors, prolonging PT/PTT with high D-dimer—the coagulation panel separates them.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — ITP and antiphospholipid syndrome overlap: many ITP patients carry antiphospholipid antibodies, and APS itself can cause moderate thrombocytopenia, yet APS's danger is clotting, not bleeding—so a thrombocytopenic patient who also clots should be tested for them.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells fuel ITP by making anti-platelet antibodies: long-lived autoantibody-secreting plasma cells (some splenic) coat platelets for destruction, and because they resist rituximab, plasma-cell-directed or splenectomy approaches address refractory ITP.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a classic secondary cause of immune thrombocytopenia: the virus drives anti-platelet antibodies and impairs production, so new thrombocytopenia warrants HIV testing—and antiretroviral therapy often restores the platelet count better than immunosuppression.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells license the autoimmunity of ITP: loss of tolerance lets Th cells help B cells make anti-platelet antibodies and skews regulatory balance, so therapies restoring immune regulation, not just removing antibody, are increasingly used in ITP.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immune thrombocytopenia is an autoimmune disease of platelet destruction: autoantibodies and T cells target platelet glycoproteins, clearing them in the spleen while also impairing production—so it joins the antibody-mediated cytopenias treated by immunosuppression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The feared complication of immune thrombocytopenia is bleeding into the nervous system: although rare, intracranial hemorrhage from very low platelets is the main life-threatening risk, so severe thrombocytopenia with neurological signs is a medical emergency.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Viral infection commonly triggers immune thrombocytopenia: especially in children, EBV and other viruses provoke cross-reactive antiplatelet antibodies, causing an acute, often self-limited ITP—molecular mimicry turning antiviral immunity against platelets.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — ITP is not only antibody-driven: cytotoxic CD8 T cells can directly lyse platelets and attack marrow megakaryocytes, explaining cases with low platelet antibodies and the variable response to therapies aimed only at antibody production.
- `connects-to` → **[Measles](../measles/README.md)** — Childhood ITP often follows infection or vaccination: measles and other viruses (and the MMR vaccine) can trigger transient antiplatelet antibodies, causing self-limited thrombocytopenia weeks later—usually resolving without treatment, unlike chronic adult ITP.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — ITP crosses the placenta: maternal anti-platelet IgG passes to the fetus and can lower the newborn's platelets, so pregnant patients need monitoring—distinct from neonatal alloimmune thrombocytopenia, where the mother targets paternal platelet antigens.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Immune thrombocytopenia is first treated with cortisol's kin: corticosteroids dampen the antibody response and the macrophage clearance of platelets, raising counts as the standard first-line therapy for symptomatic ITP.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — ITP stems from failed tolerance by regulatory T cells: deficient or dysfunctional Tregs let the immune system make antibodies against the body's own platelets, so restoring regulatory T-cell control is an emerging therapeutic goal.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver quietly governs platelet counts in ITP: it makes most of the body's thrombopoietin and helps clear antibody-coated platelets, so liver function shapes both platelet production and destruction in the disease.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab treats ITP by deleting B cells via CD20: stripping the antibody-producing B cells lowers the anti-platelet autoantibodies, a second-line option that can give durable remissions in immune thrombocytopenia.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ITP's most feared danger is bleeding into the brain: though rare, intracranial hemorrhage from the very low platelet count is the leading cause of death, which is why severe thrombocytopenia is treated urgently.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help break self-tolerance in ITP: by presenting platelet antigens to T cells they license the autoimmune response that drives B cells to make anti-platelet antibodies, a step upstream of the destruction.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chronic ITP can drain iron: ongoing mucosal and menstrual bleeding from the very low platelet count slowly depletes the body's iron, adding deficiency anemia to the thrombocytopenia.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — ITP shows first on the skin: pinpoint petechiae and bruising purpura, the bleeding into skin from too few platelets, are the cardinal visible sign that brings patients in.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — ITP destroys platelets partly through complement: antibody-coated platelets can fix complement C3, marking them for a second route of clearance beyond the spleen's macrophages.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — When ITP is unclear the marrow is checked under the microscope: it shows plentiful megakaryocytes, confirming platelets are being destroyed in the periphery rather than underproduced.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — ITP can bleed into the gut: severe thrombocytopenia causes gastrointestinal hemorrhage, one of the dangerous internal bleeds beyond the visible skin purpura.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — ITP's autoantibodies are made in germinal centers: spleen B cells there produce the anti-platelet antibodies, which is why splenectomy and B-cell-depleting rituximab can control it.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows ITP's two-front problem: spleen macrophages devour antibody-coated platelets, while the marrow's megakaryocytes — normal or increased in number — are themselves hampered from releasing new ones.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Very low platelets can bleed into the eye: retinal and conjunctival hemorrhages appear in severe ITP, a visible warning of the bleeding risk that, at its worst, threatens intracranial hemorrhage.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — ITP can show up as blood in the urine: profound thrombocytopenia causes mucosal and urinary-tract bleeding, hematuria being one of the wet-purpura signs that signals a dangerously low count.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — ITP is an autoantibody disease: IgG antibodies against platelet glycoproteins GPIIb/IIIa and GPIb tag platelets for splenic destruction and also stunt megakaryocytes, which is why anti-CD20 and IVIG therapies work by removing or blockading that antibody.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — When the same autoimmunity also targets red cells, ITP becomes Evans syndrome: simultaneous immune destruction of platelets and erythrocytes (autoimmune hemolytic anemia), a more refractory combined cytopenia hinting at an underlying lymphoma or lupus.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Low vitamin D tracks with autoimmunity: deficiency is common in chronic ITP and, by tilting regulatory-T-cell balance, is studied as a modifier of the immune dysregulation that lets antibodies turn against the body's own platelets.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — ITP complicates pregnancy two ways: it must be told apart from benign gestational thrombocytopenia, and the platelet-targeting IgG crosses the placenta to lower the baby's count, so mother and newborn are both watched around delivery.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — Blocking BTK hits ITP from both sides: the kinase drives B-cell antibody production and the macrophage Fc-receptor signaling that destroys platelets, so BTK inhibitors like rilzabrutinib are an emerging targeted treatment.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Childhood ITP often follows a virus: acute self-limited ITP classically appears a week or two after infections such as varicella, when antibodies raised against the virus cross-react with platelets before fading as the child recovers.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Two ways to run out of platelets: ITP destroys them in the periphery while the marrow works overtime, whereas aplastic anemia fails to make them at all — the contrast drives the bone-marrow exam that distinguishes peripheral destruction from production failure.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Destruction is not antibody alone: natural killer and cytotoxic cells contribute to platelet clearance and to the dysregulated immunity of ITP, part of why some cases resist antibody-focused treatments and need broader immune suppression.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Bleeding turns on what platelets grip: von Willebrand factor is the glue platelets use to plug vessels, so when ITP drops the platelet count the vWF-platelet plug fails, producing the bruising and mucosal bleeding that define the disease's danger.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement helps clear the platelets: antiplatelet antibodies fix complement to opsonize and lyse platelets in ITP, a pathway that complement inhibitors (e.g. sutimlimab) are explored to interrupt.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A bleeding disorder that paradoxically clots: ITP carries a raised thrombosis risk, amplified by thrombopoietin-receptor agonists and splenectomy, so venous thromboembolism is a real hazard even amid low platelets.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection and its vaccines can trigger it: COVID-19, like other viral illnesses, precipitates secondary immune thrombocytopenia, and rare post-vaccination ITP is recognized — examples of infection-driven autoimmunity against platelets.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Dysregulated T-cell signaling underlies the autoimmunity: STAT3 activation in the T and B cells of ITP supports the autoreactive response that makes anti-platelet antibodies, part of the immune imbalance behind the disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Immune activation runs through NF-κB: B-cell and macrophage NF-κB signaling sustains the autoantibody production and Fc-receptor-mediated platelet destruction that define immune thrombocytopenia.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Removing the spleen and suppressing immunity raise infection risk: splenectomy for refractory ITP leaves patients prone to overwhelming post-splenectomy infection, and rituximab and steroids add further sepsis risk.
- `connects-to` → **[HIV](../hiv/README.md)** — It can be the first sign of HIV: HIV is a classic cause of secondary immune thrombocytopenia, sometimes the presenting feature, so HIV testing is part of the standard ITP workup.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its B-cell-directed therapy opens the lung: the rituximab and prolonged steroids used in refractory ITP deplete immune defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A relapsing disease and its steroids weigh on mood: the unpredictable bleeding risk, activity restrictions and mood effects of chronic corticosteroids in ITP contribute to depression and reduced quality of life.
- `connects-to` → **[Stroke](../stroke/README.md)** — It threatens the brain from both directions: severe thrombocytopenia risks intracranial hemorrhage, while the TPO-receptor agonists used to raise platelets and post-splenectomy state carry a thrombotic stroke risk.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its immunosuppression opens the lung to mold: the high-dose corticosteroids and rituximab used to treat ITP blunt immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Prolonged steroids thin the bones: the repeated and long courses of corticosteroids used to control ITP accelerate bone loss and raise fracture risk.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Low platelets bleed into the skin: ITP causes petechiae, purpura and easy bruising, and the wet purpura of mucosal and oral bleeding signals a dangerously low platelet count.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It bleeds the gut and ties to H. pylori: severe thrombocytopenia in ITP risks gastrointestinal haemorrhage, and eradicating Helicobacter pylori can raise the platelet count in many patients.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Living with a bleeding risk breeds worry: the unpredictable platelet counts, fear of haemorrhage and relapsing course of ITP foster chronic health anxiety alongside depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The spleen is its engine: the spleen is the principal site where antibody-coated platelets are destroyed and where the autoantibodies are made, which is why splenectomy is a long-standing treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with autoimmune glands: ITP commonly coexists with autoimmune thyroid disease and other autoimmunity, reflecting a broader autoimmune predisposition.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its platelet-boosting drugs can scar the marrow: the thrombopoietin-receptor agonists eltrombopag and romiplostim can cause bone-marrow reticulin fibrosis with long-term use.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — First-line lifts the platelets: corticosteroids are the initial treatment for immune thrombocytopenia, dampening the autoimmune platelet destruction, with IVIG added for urgent rises.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment can swing toward clotting: the thrombopoietin-receptor agonists used in chronic ITP raise platelet counts but carry a thrombotic and cardiovascular risk.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Bleeding and overlap reach the kidney: ITP can cause haematuria, and when it accompanies lupus or Evans syndrome a coexisting glomerulonephritis may be present.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — A virus that lowers the platelets: chronic hepatitis C is a recognised secondary cause of immune thrombocytopenia, and treating the infection often raises the platelet count.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../heparin-induced-thrombocytopenia/README.md)** — A thrombocytopenia that clots instead of bleeds: unlike immune thrombocytopenia, heparin-induced thrombocytopenia causes thrombosis, a key contrast in the workup of a falling platelet count.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cytotoxic immunosuppression for refractory disease: vincristine, cyclophosphamide and azathioprine are used in immune thrombocytopenia that resists steroids and first-line agents.
- `connects-to` → **[Dexamethasone](../../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — Pulsed steroids to reset immunity: high-dose dexamethasone given in short 4-day pulses is a standard first-line treatment for immune thrombocytopenia, raising platelet counts faster and with fewer long-term effects than prolonged daily prednisone.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Low platelets as a paraneoplastic clue: immune thrombocytopenia can arise secondary to lymphoproliferative disease, including Hodgkin lymphoma, where disordered immunity generates anti-platelet antibodies—so refractory ITP warrants a search for hidden lymphoma.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Autoimmunity that also attacks platelets: like SLE, rheumatoid arthritis can drive secondary immune thrombocytopenia, and in Felty syndrome RA combines with splenomegaly and cytopenias—the same spleen that destroys antibody-coated platelets in ITP.
- `connects-to` → **[MDS](../mds/README.md)** — A mimic to exclude: isolated thrombocytopenia in myelodysplastic syndrome can mimic ITP, and the two are distinguished by marrow examination—essential before immunosuppressing a presumed ITP.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Secondary ITP: indolent B-cell lymphomas like follicular lymphoma (and CLL) can trigger secondary immune thrombocytopenia through dysregulated antibody-producing B cells.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Where thrombopoietin is made: TPO, the platelet growth factor that is inappropriately low relative to need in ITP, is produced constitutively by the hepatic lobule, so liver disease lowers platelet counts.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Central versus peripheral: myelofibrosis crowds out megakaryocytes for a production-failure low platelet count, the marrow-failure differential to distinguish from the peripheral antibody-mediated platelet destruction of ITP.
- `connects-to` → **[Dengue Fever](../dengue-fever/README.md)** — Infection-driven thrombocytopenia: dengue causes profound platelet falls through immune-mediated destruction and marrow suppression, a leading infectious mimic of ITP in endemic regions.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Secondary ITP from lymphoma: low-grade B-cell malignancies like Waldenstrom macroglobulinaemia can drive autoimmune platelet destruction, so a new ITP in an older adult warrants screening for an underlying lymphoproliferative disorder.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — HIV-associated ITP: HIV is a recognised cause of secondary immune thrombocytopenia, sometimes its presenting feature, and the platelet count often improves with antiretroviral therapy.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1-skewed autoimmunity: an IFN-γ-dominated cytokine profile drives the autoreactive T-cell help and macrophage activation that destroy antibody-coated platelets in ITP.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell survival factor: BAFF sustains the autoreactive B cells producing anti-platelet antibodies in ITP, part of the rationale for B-cell-directed therapy.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic platelet lysis: beyond antibody-mediated clearance, CD8 cytotoxic T cells use perforin to directly lyse platelets and megakaryocytes in ITP.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory dysregulation: IL-6 contributes to the loss of immune tolerance in ITP, supporting the autoreactive T- and B-cell responses against platelets.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Immune activation: elevated TNF-α reflects the inflammatory immune dysregulation of ITP, promoting macrophage-mediated platelet destruction.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet activation and antigen: PF4 from activated platelets marks the platelet activation in ITP and anchors the antigenic overlap with PF4-driven HIT and VITT that the disorder is distinguished from.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Regulatory T-cell deficit: defective IL-2-dependent regulatory T cells permit the antiplatelet autoimmunity of ITP, and low-dose IL-2 to expand Tregs is under investigation as therapy.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Autoantigen presentation: MHC class II presentation of platelet-glycoprotein peptides to CD4 T cells licenses the B cells that make the anti-GPIIb/IIIa autoantibodies of ITP.
- `connects-to` → **[MPL](../../03-molecular/mpl/README.md)** — Thrombopoietin-receptor agonists (eltrombopag, romiplostim) stimulate MPL on megakaryocytes to raise platelet production in ITP—a paradigm shift from suppressing platelet destruction to driving production that transformed second-line therapy.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Antiplatelet antibodies also impair megakaryocyte platelet release and trigger caspase-3-mediated platelet apoptosis, so the thrombocytopenia of ITP reflects underproduction as well as accelerated destruction.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 helps recruit the splenic macrophages that phagocytose antibody-opsonized platelets through their Fcγ receptors, the principal site of the accelerated platelet destruction that splenectomy historically addressed.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor are first-line for immune thrombocytopenia, dampening autoantibody production and macrophage Fcγ-receptor-mediated platelet phagocytosis to raise the platelet count.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Long-lived anti-platelet plasma cells survive on BCL-2 and lack CD20, so they escape rituximab—the basis for relapses after B-cell depletion in ITP and the rationale for plasma-cell-directed approaches.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — Macrophage Fcγ-receptor engagement by antibody-coated platelets signals through Src-family and Syk kinases to trigger phagocytosis, the pathway the Syk inhibitor fostamatinib blocks to reduce platelet destruction in ITP.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Regulatory T cells and their IL-10 are deficient in immune thrombocytopenia, removing a brake that normally restrains the autoreactive anti-platelet response.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Impaired CTLA-4-dependent regulatory T-cell control contributes to the breakdown of self-tolerance that allows anti-platelet autoantibodies to arise in ITP.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — An IL-17-producing Th17 skew accompanies the Th1-dominated immune dysregulation of ITP, adding to the inflammatory imbalance behind platelet autoimmunity.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Thrombopoietin acting through the MPL receptor and JAK-STAT (MPL and STAT3 already mapped) drives megakaryopoiesis, the pathway harnessed by TPO-receptor agonists to raise platelet counts in ITP.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12-driven Th1 polarization (IFN-γ already mapped) skews the autoimmune response that targets platelets for destruction in immune thrombocytopenia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Impaired PD-1 and other inhibitory-checkpoint control of autoreactive T and B cells contributes to the loss of self-tolerance underlying immune thrombocytopenia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling downstream of BAFF and the TPO receptor MPL (both mapped) participates in both the autoimmunity and the megakaryocyte responses of immune thrombocytopenia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR-regulated T-cell metabolism shapes the regulatory-T-cell deficiency of ITP, and mTOR inhibition (sirolimus) restores tolerance in refractory disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the macrophage-mediated platelet clearance and immune dysregulation of immune thrombocytopenia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the dysregulated T-cell and interferon response that drives the anti-platelet autoimmunity of immune thrombocytopenia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the loss of tolerance and inflammatory tone of immune thrombocytopenia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) supports the survival of the autoreactive B and T cells driving immune thrombocytopenia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the autoreactive lymphocyte tolerance and survival balance relevant to the anti-platelet antibody production of immune thrombocytopenia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the regulatory-T-cell control whose deficiency permits the autoimmunity of immune thrombocytopenia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the innate inflammatory activation accompanying immune thrombocytopenia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the T-cell and B-cell inflammatory signaling that drives the autoantibody response of immune thrombocytopenia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of the B-cell and Fc receptors participates in the immune activation of immune thrombocytopenia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates megakaryocyte and immune-cell survival relevant to the impaired platelet production of immune thrombocytopenia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism of immune thrombocytopenia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte trafficking participates in the immune dysregulation of immune thrombocytopenia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the autoreactive immune response in immune thrombocytopenia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the megakaryocyte and bone-marrow-niche interactions relevant to immune thrombocytopenia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune dysregulation of immune thrombocytopenia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the inflammatory milieu of immune thrombocytopenia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the autoreactive immune responses of immune thrombocytopenia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of immune thrombocytopenia, and calcineurin inhibitors are used in refractory disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation of immune thrombocytopenia.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Evans syndrome: when immune thrombocytopenia occurs together with autoimmune haemolytic anaemia (Evans syndrome), haemoglobin falls alongside the platelets, reflecting a broader breakdown of tolerance to blood-cell antigens.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Autoantibody help: Th2 cytokines including IL-4 support the B cells that produce the anti-platelet (anti-GPIIb/IIIa) autoantibodies (IgG already mapped) central to the platelet destruction of immune thrombocytopenia.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Female predominance: immune thrombocytopenia, like many autoimmune diseases, is more common in young women, and estrogen's enhancement of antibody responses is thought to contribute to this sex difference in susceptibility.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — TTP differential: a normal ADAMTS13 distinguishes immune thrombocytopenia from thrombotic thrombocytopenic purpura, where its severe deficiency lets von Willebrand factor (already mapped) multimers consume platelets, the key differential of an isolated low count.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet granule store: platelets are the body's main reservoir of serotonin in their dense granules, so the platelet destruction of immune thrombocytopenia depletes this store, one facet of the loss of platelet function beyond the low count.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 autoantibody help: IL-13, with the IL-4 (already mapped) type-2 response, supports the B cells producing the anti-platelet autoantibodies that drive the platelet destruction of immune thrombocytopenia.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — GPIIb/IIIa target: fibrinogen bridges platelets by binding the GPIIb/IIIa integrin that is itself the main antigen of the anti-platelet autoantibodies, so the destruction and dysfunction of platelets in immune thrombocytopenia impairs this aggregation.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Thromboxane and platelet function: activated platelets generate thromboxane A2 to amplify aggregation, and the loss of platelet numbers and function in immune thrombocytopenia diminishes this eicosanoid arm of haemostasis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial platelet control: endothelial nitric oxide normally inhibits platelet activation, part of the vascular regulation of the platelets whose autoimmune destruction defines immune thrombocytopenia.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Regulatory tolerance: TGF-β, with IL-10 (already mapped), enforces the regulatory-T-cell tolerance whose failure permits the anti-platelet autoimmunity of immune thrombocytopenia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Megakaryocyte niche: VEGF supports the marrow vascular niche of the megakaryocytes, and the impaired platelet production (thrombopoietin already mapped) of immune thrombocytopenia involves this microenvironment as well as the autoantibody attack.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon dysregulation: type-I interferon signalling is implicated in the loss of tolerance of immune thrombocytopenia, and interferon therapy can itself precipitate the autoimmune platelet destruction.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin modulates the autoreactive T-cell (already mapped) response implicated in immune thrombocytopenia, part of the metabolic-immune axis of the autoimmune disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the autoimmune immune thrombocytopenia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) accompanying immune thrombocytopenia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the T-helper imbalance (with the Th1 IFN-γ already mapped) that skews the autoimmune response of immune thrombocytopenia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Th2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the T-helper cytokine balance dysregulated in immune thrombocytopenia.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Inflammatory iron: the IL-6-driven (already mapped) hepcidin of the systemic inflammation accompanying immune thrombocytopenia contributes to any concurrent anaemia of chronic disease.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Thrombopoietin source: the hepatocytes are the main source of the thrombopoietin (already mapped), the MPL (already mapped) ligand whose relatively low level (the failure to compensate) contributes to the impaired platelet production of immune thrombocytopenia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 dimension of the T-helper cytokine dysregulation of immune thrombocytopenia.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell/allergic arm: histamine, released by the mast cells and basophils, is part of the type-2/allergic component contributing to some (e.g. drug-induced) forms of immune thrombocytopenia.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Innate/FcγR arm: the neutrophils, via their Fcγ receptors, participate in the innate immune dysregulation and the drug-induced forms of immune thrombocytopenia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) contributes to the complement-mediated platelet destruction of immune thrombocytopenia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the micronutrient dimension of the immune dysregulation of immune thrombocytopenia.

[^cines-2002-itp-review]: Cines DB, Blanchette VS. Immune thrombocytopenic purpura. *N Engl J Med.* 2002;346(13):995-1008. [doi:10.1056/NEJMra010532](https://doi.org/10.1056/NEJMra010532) · [PubMed 11919310](https://pubmed.ncbi.nlm.nih.gov/11919310/)
[^neunert-2019-ash-itp-guidelines]: Neunert C, et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. *Blood Adv.* 2019;3(23):3829-3866. [doi:10.1182/bloodadvances.2019000966](https://doi.org/10.1182/bloodadvances.2019000966) · [PubMed 31794604](https://pubmed.ncbi.nlm.nih.gov/31794604/)
[^bussel-2006-romiplostim-itp]: Bussel JB, et al. AMG 531, a thrombopoiesis-stimulating protein, for chronic ITP. *N Engl J Med.* 2006;355(16):1672-1681. [doi:10.1056/NEJMoa054626](https://doi.org/10.1056/NEJMoa054626) · [PubMed 17050891](https://pubmed.ncbi.nlm.nih.gov/17050891/)
[^cheng-2011-eltrombopag-raise]: Cheng G, et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE). *Lancet.* 2011;377(9763):393-402. [doi:10.1016/S0140-6736(10)60959-2](https://doi.org/10.1016/S0140-6736(10)60959-2) · [PubMed 21237459](https://pubmed.ncbi.nlm.nih.gov/21237459/)
