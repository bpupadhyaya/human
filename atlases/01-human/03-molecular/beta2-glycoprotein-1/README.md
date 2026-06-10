---
schema: human-scale-entry/v1
id: beta2-glycoprotein-1
name: Beta-2 Glycoprotein I
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Beta-2 glycoprotein I (B2GPI; APOH; chr17q24.2) is a plasma phospholipid-binding glycoprotein; domain I contains the dominant anti-B2GPI IgG epitope in APS; anti-B2GPI IgG activates endothelium, platelets, and complement → thrombosis and pregnancy loss."
aliases: ["B2GPI", "beta-2 glycoprotein I", "APOH", "apolipoprotein H", "anti-B2GPI", "antiphospholipid antigen", "beta2-glycoprotein 1"]
sources:
  - id: miyakis-2006-aps-criteria
    type: peer-reviewed
    cite: "Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). J Thromb Haemost. 2006;4(2):295-306."
    doi: "10.1111/j.1538-7836.2006.01753.x"
    pmid: "16420554"
    url: "https://doi.org/10.1111/j.1538-7836.2006.01753.x"
  - id: de-groot-2004-b2gpi-domain1
    type: peer-reviewed
    cite: "de Groot PG, Derksen RH. The antiphospholipid syndrome: clinical characteristics and pathophysiology. Semin Thromb Hemost. 2004;30(6):597-606."
    doi: "10.1055/s-2004-861504"
    pmid: "15630643"
    url: "https://doi.org/10.1055/s-2004-861504"
  - id: rand-2019-aps-lancet
    type: peer-reviewed
    cite: "Rand JH, Wolgast LR. Dos and don'ts in diagnosing antiphospholipid syndrome. Hematology Am Soc Hematol Educ Program. 2012;2012:455-459."
    doi: "10.1182/asheducation-2012.1.455"
    pmid: "23233624"
    url: "https://doi.org/10.1182/asheducation-2012.1.455"
cross_links:
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the primary pathogenic autoantibodies in APS; activate endothelium (TLR4→NF-κB→TF), platelets (GPIbα), and complement → thrombosis and pregnancy loss; triple-positive aPL (LA + aCL + anti-B2GPI) confers highest risk."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-B2GPI autoantibodies are predominantly IgG (IgG1 > IgG4); domain I-specific IgG are most pathogenic in APS; IgG-B2GPI complexes bind phospholipid surfaces on endothelium and platelets → prothrombotic signaling; B2GPI-specific IgG titer correlates with thrombotic risk."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Anti-B2GPI → complement activation (C3b deposition → C5a → neutrophil/platelet activation → thrombus amplification); eculizumab (anti-C5; FDA-approved for other indications) is used off-label for catastrophic APS (CAPS) refractory to anticoagulation and plasma exchange."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "~50% of SLE patients have aPL antibodies (anti-B2GPI, aCL, LA); 30% of aPL-positive SLE patients develop APS; anti-B2GPI IgG may drive SLE nephritis through complement and endothelial activation; hydroxychloroquine reduces aPL titers and thrombotic risk in SLE."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Anti-B2GPI IgG + B2GPI on activated platelet PS → GPIbα interaction → P-selectin expression → platelet aggregation; Fc-dependent FcγRIIA → PI3K → further activation; aspirin is the cornerstone of thrombotic APS secondary prevention for arterial thrombosis."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Anti-B2GPI IgG inhibits Protein C activation and Protein S → impaired APC anticoagulant pathway → thrombin amplification; EPCR expression reduced on anti-B2GPI-activated endothelium → less APC; the resultant Protein C/S-deficient state underlies microvascular APS thrombosis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Anti-B2GPI IgG-B2GPI complexes on endothelial surface engage TLR4 → MyD88 → NF-κB → tissue factor + VCAM-1 + ICAM-1 → prothrombotic endothelial phenotype; B2GPI binds PS exposed by activated endothelium → the primary site of APS-associated arterial and venous thrombosis."
---

# Beta-2 Glycoprotein I

## Overview

**Beta-2 glycoprotein I (B2GPI; gene *APOH*, chromosome 17q24.2)** is a **plasma phospholipid-binding glycoprotein** and natural anticoagulant that functions as the principal autoantigen in **antiphospholipid syndrome (APS)** [^miyakis-2006-aps-criteria]. Originally described as "apolipoprotein H," B2GPI is now recognized as a cofactor that bridges antiphospholipid antibody binding to anionic phospholipid surfaces — explaining why "anti-cardiolipin antibodies" in fact predominantly target B2GPI rather than cardiolipin itself.

B2GPI circulates in plasma at ~200 µg/mL (normal). In its **resting (circular) conformation**, domain V shields domain I (the antibody epitope), limiting pathogenic antibody access. Upon **phospholipid binding**, B2GPI adopts an **extended (J-shaped) conformation** that exposes domain I — the epitope for the most clinically dangerous anti-B2GPI IgG antibodies. This conformational switch is a critical molecular gate in APS pathogenesis.

**Clinical significance:**
- Anti-B2GPI IgG (especially domain I-specific, R39-R43 epitope) = highest thrombotic risk aPL antibody
- Cofactor for anti-cardiolipin antibody binding (aCL antibodies bind cardiolipin only when B2GPI is present)
- Triple aPL positivity (lupus anticoagulant + aCL + anti-B2GPI): >10% annual thrombotic risk
- Obstetric APS: anti-B2GPI activates decidual endothelium and trophoblast → placental failure

## Structure

### Protein architecture

| Feature | Detail |
|:--------|:-------|
| Gene | *APOH*, chromosome 17q24.2 |
| Protein | 326 aa; 38-43 kDa mature glycoprotein (heavily N-glycosylated) |
| Structure | 5 complement control protein (CCP/Short Consensus Repeat) domains (CCP1-CCP5) |
| CCP1 (domain I) | Contains R39-R43-C40 epitope cluster — primary anti-B2GPI IgG target |
| CCP5 (domain V) | Membrane-binding domain; polybasic sequence (CKNKEKKC lysine cluster) binds anionic phospholipids (PS, cardiolipin, phosphatidylinositol) |
| Glycosylation | 4 N-linked oligosaccharides contribute ~35% of molecular weight; protects from proteolytic cleavage |

### Conformational states

**Circular conformation (resting; ~80% in plasma):**
- Domain I and domain V interact → "closed ring" structure
- Domain I epitope (R39-R43) sterically shielded → anti-B2GPI IgG cannot bind efficiently
- No phospholipid binding

**Extended/J-shaped conformation (activated; ~20% in plasma; predominant on phospholipid surfaces):**
- Domain I–domain V interaction broken
- Domain V anchors to anionic phospholipid membranes (apoptotic cells, activated platelets, endothelium)
- Domain I epitope fully exposed → anti-B2GPI IgG binds with high affinity → pathogenic activation

### Normal anticoagulant functions

In its physiological role, B2GPI is an **anticoagulant**:
1. **Inhibits factor Xa** (via domain I) and the **tenase complex** (factor IXa/VIIIa) → reduces thrombin generation
2. **Competes with prothrombin** for phospholipid binding → blocks prothrombinase efficiency
3. **Inhibits ADP-induced platelet aggregation** → antithrombotic
4. **Promotes clearance of apoptotic cells** via domain V phosphatidylserine binding → anti-inflammatory

**In APS:** Anti-B2GPI IgG bound to B2GPI on phospholipid surfaces paradoxically **converts B2GPI from anticoagulant to procoagulant** — blocking its normal functions while activating endothelium and platelets via Fc receptor-independent and Fc receptor-dependent mechanisms.

## Function

### Phospholipid binding and cofactor activity

B2GPI's physiological binding to anionic phospholipids (phosphatidylserine [PS] exposed on the outer leaflet of activated/apoptotic cells) is what positions it as the primary bridging molecule in APS pathogenesis:

- **On activated platelets:** PS flips to outer leaflet → B2GPI binds → anti-B2GPI IgG bridges B2GPI to platelet GPIbα (additional interaction) → further platelet activation
- **On apoptotic/necrotic cells:** B2GPI opsonizes apoptotic cells → recognition by macrophages → clearance; impaired clearance in APS may contribute to autoimmune amplification
- **On endothelial cells:** Inflammatory cytokines (TNF-α, IL-1β) increase surface expression of anionic phospholipid → B2GPI binding → anti-B2GPI IgG engages endothelial TLR4 → NF-κB → TF, ICAM-1, VCAM-1 → prothrombotic endothelial phenotype

## Mechanism

### Pathogenic mechanisms of anti-B2GPI IgG

**1. Endothelial cell activation (dominant mechanism):**
- Anti-B2GPI IgG (complexed with B2GPI on endothelial surface) → engagement of **TLR4** and **annexin A2** receptors → MyD88 → NF-κB → **tissue factor (TF)** upregulation + E-selectin + VCAM-1 + ICAM-1 → prothrombotic endothelial phenotype
- Endothelial TF → extrinsic coagulation cascade → thrombin → fibrin clot

**2. Platelet activation:**
- B2GPI on activated platelet surface + anti-B2GPI IgG → Fc-independent: direct B2GPI/GPIbα interaction → P-selectin expression → platelet aggregation
- Fc-dependent: anti-B2GPI IgG Fc → FcγRIIA on platelets → PI3K/PLCγ → platelet activation

**3. Complement activation:**
- Anti-B2GPI IgG-B2GPI immune complexes on cell surfaces → classical pathway C1q → C3 → C5 → C5a → neutrophil/platelet priming → amplification of thrombotic cascade
- **Pregnane loss model:** In obstetric APS, C5a on trophoblast → decidual NK and neutrophil activation → placental failure independent of thrombosis

**4. Protein C/S pathway inhibition:**
- Anti-B2GPI IgG inhibits protein C activation and protein S function → impaired anticoagulant pathway → thrombin amplification
- EPCR (endothelial protein C receptor) expression reduced by anti-B2GPI → less APC generated

**5. Lupus anticoagulant paradox:**
- Anti-B2GPI IgG inhibits phospholipid-dependent clotting reactions *in vitro* (prolonging APTT/dRVVT = lupus anticoagulant) — paradoxically indicating a THROMBOTIC state in vivo (anti-phospholipid antibodies compete with coagulation factors for phospholipid surfaces in the test, prolonging clotting time, but promote thrombosis in vivo by activating endothelium and platelets)

## Connections

- `connects-to` → **[Antiphospholipid Syndrome](../../07-system/antiphospholipid-syndrome/README.md)** — Anti-B2GPI IgG (domain I-specific; R39-R43 epitope) are the primary pathogenic autoantibodies in APS; activate endothelium (TLR4→NF-κB→TF), platelets (GPIbα), and complement → thrombosis and pregnancy loss; triple-positive aPL (LA + aCL + anti-B2GPI) confers highest risk.
- `connects-to` → **[Immunoglobulin G](../immunoglobulin-g/README.md)** — Anti-B2GPI autoantibodies are predominantly IgG (IgG1 > IgG4); domain I-specific IgG are most pathogenic in APS; IgG-B2GPI complexes bind phospholipid surfaces on endothelium and platelets → prothrombotic signaling; B2GPI-specific IgG titer correlates with thrombotic risk.
- `connects-to` → **[Complement C5](../complement-c5/README.md)** — Anti-B2GPI → complement activation (C3b deposition → C5a → neutrophil/platelet activation → thrombus amplification); eculizumab (anti-C5; FDA-approved for other indications) is used off-label for catastrophic APS (CAPS) refractory to anticoagulation and plasma exchange.
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — ~50% of SLE patients have aPL antibodies (anti-B2GPI, aCL, LA); 30% of aPL-positive SLE patients develop APS; anti-B2GPI IgG may drive SLE nephritis through complement and endothelial activation; hydroxychloroquine reduces aPL titers and thrombotic risk in SLE.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Anti-B2GPI IgG + B2GPI on activated platelet PS → GPIbα interaction → P-selectin expression → platelet aggregation; Fc-dependent FcγRIIA → PI3K → further activation; aspirin is the cornerstone of thrombotic APS secondary prevention for arterial thrombosis.
- `connects-to` → **[Protein C](../protein-c/README.md)** — Anti-B2GPI IgG inhibits Protein C activation and Protein S → impaired APC anticoagulant pathway → thrombin amplification; EPCR expression reduced on anti-B2GPI-activated endothelium → less APC generated; the resultant Protein C/S-deficient state underlies microvascular APS thrombosis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Anti-B2GPI IgG-B2GPI complexes on endothelial surface engage TLR4 → MyD88 → NF-κB → tissue factor + VCAM-1 + ICAM-1 → prothrombotic endothelial phenotype; B2GPI binds PS exposed by activated endothelium → the primary APS thrombosis initiation site.

[^miyakis-2006-aps-criteria]: Miyakis S, Lockshin MD, Atsumi T, et al. International consensus statement on an update of the classification criteria for definite antiphospholipid syndrome (APS). *J Thromb Haemost.* 2006;4(2):295-306. [doi:10.1111/j.1538-7836.2006.01753.x](https://doi.org/10.1111/j.1538-7836.2006.01753.x) · [PubMed 16420554](https://pubmed.ncbi.nlm.nih.gov/16420554/)
[^de-groot-2004-b2gpi-domain1]: de Groot PG, Derksen RH. The antiphospholipid syndrome: clinical characteristics and pathophysiology. *Semin Thromb Hemost.* 2004;30(6):597-606. [doi:10.1055/s-2004-861504](https://doi.org/10.1055/s-2004-861504) · [PubMed 15630643](https://pubmed.ncbi.nlm.nih.gov/15630643/)
[^rand-2019-aps-lancet]: Rand JH, Wolgast LR. Dos and don'ts in diagnosing antiphospholipid syndrome. *Hematology Am Soc Hematol Educ Program.* 2012;2012:455-459. [doi:10.1182/asheducation-2012.1.455](https://doi.org/10.1182/asheducation-2012.1.455) · [PubMed 23233624](https://pubmed.ncbi.nlm.nih.gov/23233624/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
