---
schema: human-scale-entry/v1
id: platelet
name: Platelet
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Anucleate haematopoietic cell fragments (~2–3 µm) shed from megakaryocytes; circulate at 150–400×10⁹/L for 8–10 days. Form primary haemostatic plugs via GPIb/vWF adhesion and GPIIb/IIIa-fibrinogen aggregation; amplify coagulation via phosphatidylserine surface exposure."
aliases: ["thrombocyte", "PLT", "platelet fragment", "blood platelet"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    note: "Platelets are shed from megakaryocytes in bone marrow sinusoids and in the lung pulmonary capillary bed; TPO→Mpl pathway drives megakaryopoiesis; G-CSF/M-CSF do not promote thrombopoiesis."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Platelets form the primary haemostatic plug at vascular injury sites; GPIIb/IIIa-fibrinogen crosslinks bridge aggregates; platelet activation in atherosclerotic plaque rupture initiates arterial thrombosis/MI/stroke."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: modulated-by
    note: "Aspirin irreversibly acetylates COX-1 Ser529 in platelets, blocking TXA₂ synthesis; platelets cannot synthesise new COX-1 (anucleate), so aspirin effect lasts platelet lifespan (~8–10 days)."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Activated platelets release PDGF, TGF-β, PF4 that recruit and polarise macrophages; platelet–macrophage interactions amplify inflammation in atherosclerosis and thromboinflammation."
  - target: 01-human/03-molecular/fibrinogen
    relation: modulated-by
    note: "Modulated by Fibrinogen."
  - target: 03-medicine/02-traditional/ginkgo-biloba
    relation: modulated-by
    note: "Modulated by Ginkgo biloba (EGb 761)."
  - target: 01-human/03-molecular/thrombopoietin
    relation: modulated-by
    note: "TPO (THPO, chr3q27.3) binds c-Mpl → JAK2/STAT5 → megakaryocyte proliferation and platelet shedding; platelet count inversely regulates free TPO via Mpl-mediated absorption; romiplostim and eltrombopag (TPO-RAs) stimulate megakaryopoiesis in ITP and aplastic anemia."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for FcγR-mediated splenic destruction in ITP; CD8+ T cells also directly lyse platelets; romiplostim, eltrombopag (FDA 2008), fostamatinib (SYK inhibitor; FDA 2018), and efgartigimod (FcRn inhibitor; FDA 2023) are approved."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "PF4 (CXCL4) is the major CXC chemokine stored in platelet alpha-granules; released on platelet activation → neutralizes heparin locally + recruits neutrophils; in HIT, PF4-heparin complex forms the immunogenic neo-antigen that triggers anti-PF4 IgG → paradoxical thrombosis."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → platelet activation → dense granule release + TXA2 → procoagulant microparticles → paradoxical thrombosis in HIT; activated platelets consumed → thrombocytopenia; platelet transfusion is contraindicated in HIT."
---

# Platelet

## Overview

Platelets (thrombocytes) are the smallest formed elements of blood: anucleate discoid cell fragments 2–3 µm in diameter, circulating at 150–400×10⁹/L in healthy adults. They are shed from large polyploid megakaryocytes in the bone marrow sinusoids and pulmonary capillary bed, and circulate for 8–10 days before being cleared by hepatic and splenic macrophages.[^alberts-mol-cell-biology] Despite lacking a nucleus, platelets are metabolically active cells containing a rich array of surface receptors, intracellular granules, and signalling machinery.

Platelets perform two fundamental physiological roles: (1) primary haemostasis — forming an initial mechanical plug at sites of vascular injury within seconds; and (2) amplification of secondary haemostasis — providing the negatively charged phospholipid surface (phosphatidylserine, PS) on which the tenase and prothrombinase complexes assemble, dramatically accelerating thrombin generation and fibrin clot formation.[^janeway-immunobiology] Dysregulation leads to thrombotic disease (arterial thrombosis, myocardial infarction, stroke) or haemorrhagic disorders (thrombocytopenia, Glanzmann thrombasthenia, Bernard-Soulier syndrome).[^alberts-mol-cell-biology]

## Structure

**Morphology.** Resting platelets are biconvex discs 2–3 µm in diameter and 0.5 µm thick. Upon activation they undergo dramatic shape change — extending filopodia and lamellipodia — driven by Gα13/RhoA/ROCK-mediated myosin II contraction and Cdc42/Arp2/3-driven actin polymerisation. A marginal band of microtubules (8–24 tubulin coils) maintains the discoid shape at rest.[^alberts-mol-cell-biology]

**Surface receptors.** Key glycoprotein complexes:
- **GPIb-IX-V complex** (CD42b-CD42a-CD42d-CD42c): vWF receptor; mediates platelet adhesion at high shear stress; GPIb also binds thrombin and P-selectin; linked to filamin A cytoskeletal scaffold.
- **GPIIb/IIIa** (αIIbβ3 integrin): most abundant platelet surface protein; binds fibrinogen, vWF, fibronectin, and vitronectin after activation; 40,000–80,000 copies per platelet.
- **GPVI**: collagen receptor; signals via FcR γ-chain ITAM → Syk → LAT/SLP-76 → PLCγ2 → Ca²⁺/DAG.
- **α2β1** (VLA-2): secondary collagen receptor; stable adhesion under low-shear conditions.[^janeway-immunobiology]

**Granules.**
- **α-granules** (~50–80 per platelet): fibrinogen, vWF multimers, factor V, factor XI, P-selectin (CD62P, on granule membrane → surface upon activation), PDGF, TGF-β, PF4 (CXCL4), β-thromboglobulin, PAI-1, fibronectin; detected by CD62P surface expression as activation marker.
- **Dense (δ) granules** (~4–8 per platelet): ADP, ATP, serotonin (5-HT), Ca²⁺, polyphosphate; detected by mepacrine fluorescence or whole-mount EM.
- **Lysosomes (λ-granules)**: acid hydrolases (cathepsins B/D, β-hexosaminidase); released more slowly; important for clot degradation.

**Internal membrane systems.**
- **Open canalicular system (OCS)**: labyrinthine plasma membrane invaginations that increase surface area and serve as conduits for rapid granule secretion.
- **Dense tubular system (DTS)**: smooth ER-like membrane; Ca²⁺ store (SERCA pumps); site of thromboxane A₂ (TXA₂) and prostaglandin synthesis (COX-1 is expressed here).[^alberts-mol-cell-biology]

## Function

**Activation pathways.**

*Collagen pathway (primary trigger):* Subendothelial collagen exposed at vessel injury binds GPVI → FcR γ-chain ITAM phosphorylation (Fyn/Lyn) → Syk → LAT/SLP-76 scaffold → PLCγ2 → IP₃ (Ca²⁺ from DTS) + DAG (PKC activation) → α-granule and dense granule secretion; α2β1 provides stable adhesion under lower shear.[^janeway-immunobiology]

*vWF/GPIb pathway (high-shear trigger):* At high shear (stenosed arteries), elongated plasma vWF multimers bind GPIbα on flowing platelets → GPIb intracellular signalling (PI3K/Akt, 14-3-3ζ) → integrin activation, shape change, and TXA₂ synthesis; critical in arterial thrombosis.[^alberts-mol-cell-biology]

*ADP (P2Y receptor) pathway:* Dense-granule ADP released by activated platelets binds two GPCRs: P2Y1 (Gq → IP₃→Ca²⁺ → shape change and initial aggregation) and P2Y12 (Gi → ↓cAMP → sustained GPIIb/IIIa activation and aggregation). P2Y12 is the target of thienopyridine prodrugs clopidogrel and prasugrel (bioactivated to irreversible inhibitors by hepatic CYPs) and of direct-acting ticagrelor.[^janeway-immunobiology]

*TXA₂ pathway:* COX-1 in platelet DTS converts arachidonic acid → PGG₂/PGH₂ → TXA₂ synthase → TXA₂ (t½ ~30 s); binds TP receptor (Gq/G12/13) on nearby platelets → amplification loop. Aspirin irreversibly acetylates COX-1 Ser529, blocking TXA₂ for the platelet lifespan.[^alberts-mol-cell-biology]

*Thrombin (PAR) pathway:* Thrombin cleaves PAR1 (high affinity, Gq/G12/13/Gi) and PAR4 (lower affinity) → powerful activation; integrates coagulation and platelet biology. Vorapaxar (Zontivity) selectively blocks PAR1.[^janeway-immunobiology]

**GPIIb/IIIa-mediated aggregation.** Inside-out signalling (CalDAG-GEFI → Rap1b activation → talin-1 and kindlin-3 binding to β3 cytoplasmic tail → integrin extension to open conformation) enables GPIIb/IIIa to bind fibrinogen, bridging adjacent platelets. Outside-in signalling (Src/Syk/FAK) drives spreading, secondary granule secretion, and clot retraction. This is the final common pathway of platelet aggregation; blocked by abciximab (anti-αIIbβ3 Fab), eptifibatide (cyclic peptide), and tirofiban (small molecule).[^alberts-mol-cell-biology]

**Procoagulant platelet activity.** Maximally activated platelets (thrombin + collagen) undergo a specialised response: TMEM16F (ANO6) scramblase translocates PS from inner to outer leaflet; mitochondrial permeability transition pore (mPTP) opens → Ca²⁺ overload → "balloon" morphology; PS surface supports tenase (FXa/FVa) and prothrombinase (FIXa/FVIIIa) complexes, accelerating thrombin generation by ~10⁵-fold.[^janeway-immunobiology]

## Lifecycle

**Megakaryopoiesis.** In bone marrow, HSCs → MEP (megakaryocyte-erythroid progenitor) → BFU-Mk → CFU-Mk → megakaryoblast → promegakaryocyte → megakaryocyte (MK). MKs undergo endomitosis (DNA replication without cell division) reaching ploidy of 8N–128N and diameters of up to 150 µm. The primary driver is thrombopoietin (TPO), produced constitutively by hepatocytes and kidney, which binds the Mpl receptor (c-MPL) → JAK2/STAT5, PI3K/Akt, MAPK pathways. NF-E2 (p45/p18 heterodimer) is the critical transcription factor for proplatelet formation.[^alberts-mol-cell-biology]

**Proplatelet formation and shedding.** Mature MKs extend long proplatelet processes (driven by marginal-band microtubule sliding, powered by dynein) into bone marrow sinusoids and pulmonary capillaries. Platelet-sized buds pinch off the proplatelet tips into the blood stream. Each MK produces 2,000–5,000 platelets over its ~5-day lifespan; ~25–35% of platelet production occurs in the pulmonary vasculature.[^janeway-immunobiology]

**Platelet lifespan and clearance.** Circulating platelets survive 8–10 days. Ageing platelets progressively desialylate their surface glycoproteins (GPIbα, GPIIb/IIIa), and the exposed Galβ1-4GlcNAc residues are recognised by the Ashwell-Morell receptor (ASGR1/2) on hepatocytes, triggering platelet removal from circulation. Splenic red pulp macrophages also clear platelets via PS-dependent mechanisms. TPO levels are regulated by this platelet mass-sensing mechanism: fewer platelets → less TPO consumption → higher TPO → increased megakaryopoiesis.[^alberts-mol-cell-biology]

## Connections

- **Part of Bone Marrow** (`../../05-tissue/bone-marrow/README.md`): Platelets are shed from megakaryocytes in bone marrow sinusoids and in the lung pulmonary capillary bed; TPO→Mpl pathway drives megakaryopoiesis; G-CSF/M-CSF do not promote thrombopoiesis.[^alberts-mol-cell-biology]
- **Modulates Cardiovascular System** (`../../07-system/cardiovascular-system/README.md`): Platelets form the primary haemostatic plug at vascular injury sites; GPIIb/IIIa-fibrinogen crosslinks bridge aggregates; platelet activation in atherosclerotic plaque rupture initiates arterial thrombosis/MI/stroke.[^janeway-immunobiology]
- **Modulated by Aspirin** (`../../../03-medicine/01-modern/04-cardio/aspirin/README.md`): Aspirin irreversibly acetylates COX-1 Ser529 in platelets, blocking TXA₂ synthesis; platelets cannot synthesise new COX-1 (anucleate), so aspirin effect lasts platelet lifespan (~8–10 days).[^alberts-mol-cell-biology]
- **Modulates Macrophage** (`../macrophage/README.md`): Activated platelets release PDGF, TGF-β, PF4 that recruit and polarise macrophages; platelet–macrophage interactions amplify inflammation in atherosclerosis and thromboinflammation.[^janeway-immunobiology]
- `modulated-by` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — TPO (THPO, chr3q27.3) binds c-Mpl → JAK2/STAT5 → megakaryocyte proliferation and platelet shedding; platelet count inversely controls free TPO via Mpl-mediated absorption; romiplostim and eltrombopag stimulate megakaryopoiesis in ITP and aplastic anemia.
- `connects-to` → **[Immune Thrombocytopenia](../../07-system/immune-thrombocytopenia/README.md)** — Anti-GPIIb/IIIa and anti-GPIb/IX IgG opsonize platelets for FcγR-mediated splenic destruction; CD8+ T cells directly lyse platelets; romiplostim, eltrombopag (FDA 2008), fostamatinib (SYK inhibitor; FDA 2018), and efgartigimod (FcRn inhibitor; FDA 2023) are approved therapies.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — PF4 (CXCL4) is the major CXC chemokine stored in platelet alpha-granules; released on platelet activation → neutralizes heparin locally + recruits neutrophils; in HIT, PF4-heparin complex forms the immunogenic neo-antigen that triggers anti-PF4 IgG → paradoxical thrombosis.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../../07-system/heparin-induced-thrombocytopenia/README.md)** — Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → platelet activation → dense granule release + TXA2 → procoagulant microparticles → paradoxical thrombosis in HIT; activated platelets consumed → thrombocytopenia; platelet transfusion is contraindicated in HIT.

## Pathology

**Immune thrombocytopenic purpura (ITP).** Autoantibodies (anti-GPIb or anti-GPIIb/IIIa) coat platelets → accelerated splenic destruction via FcγR on macrophages; megakaryocyte suppression by anti-GPIb antibodies also contributes. Treat: corticosteroids, IVIG, anti-CD20 (rituximab), TPO-RAs (eltrombopag, romiplostim), splenectomy.[^janeway-immunobiology]

**Heparin-induced thrombocytopenia (HIT).** Heparin forms complexes with platelet factor 4 (PF4/CXCL4); anti-heparin-PF4 IgG antibodies (particularly IgG4) bind FcγRIIA on platelets → paradoxical platelet activation and thrombosis (HITT); treat with non-heparin anticoagulants (argatroban, fondaparinux, bivalirudin); diagnose with ELISA + functional 14C-serotonin release assay (SRA).[^alberts-mol-cell-biology]

**Glanzmann thrombasthenia.** Autosomal recessive mutations in ITGA2B or ITGB3 (GPIIb/IIIa) → absent aggregation despite normal platelet count and morphology; mucocutaneous bleeding; platelet transfusion or recombinant FVIIa.[^janeway-immunobiology]

**Bernard-Soulier syndrome.** Autosomal recessive mutations in GP1BA, GP1BB, or GP9 (GPIb-IX-V) → failure of platelet adhesion to vWF at high shear; giant platelets on blood smear; normal aggregation with ADP/collagen.[^alberts-mol-cell-biology]

**Essential thrombocythaemia (ET).** Clonal myeloproliferative neoplasm; JAK2 V617F (~60%), CALR exon 9 (~30%), or MPL mutations → constitutive TPO-receptor signalling → megakaryocyte hyperplasia and thrombocytosis (>450×10⁹/L); risk of arterial/venous thrombosis and haemorrhage; treat with aspirin, cytoreduction (hydroxyurea, anagrelide), ruxolitinib (JAK1/2 inhibitor).[^janeway-immunobiology]

**Arterial thrombosis in atherosclerosis.** Plaque rupture exposes collagen and vWF → platelet adhesion → ADP/TXA₂ amplification → thrombus occlusion → STEMI/stroke. Dual antiplatelet therapy (aspirin + P2Y12 inhibitor) is standard post-ACS management.[^alberts-mol-cell-biology]

## See Also

- [`../../05-tissue/bone-marrow/README.md`](../../05-tissue/bone-marrow/README.md) — site of megakaryopoiesis and platelet production
- [`../../07-system/cardiovascular-system/README.md`](../../07-system/cardiovascular-system/README.md) — haemostasis and thrombosis context
- [`../../../03-medicine/01-modern/04-cardio/aspirin/README.md`](../../../03-medicine/01-modern/04-cardio/aspirin/README.md) — COX-1 inhibitor; antiplatelet mechanism
- [`../macrophage/README.md`](../macrophage/README.md) — platelet clearance and inflammatory crosstalk
- [`../neutrophil/README.md`](../neutrophil/README.md) — platelet–neutrophil interactions in thromboinflammation and NETosis
- [`../../03-molecular/immunoglobulin-g/README.md`](../../03-molecular/immunoglobulin-g/README.md) — IgG autoantibodies in ITP and HIT
