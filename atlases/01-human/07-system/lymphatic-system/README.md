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
