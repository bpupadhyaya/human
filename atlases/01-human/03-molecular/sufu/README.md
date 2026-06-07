---
schema: human-scale-entry/v1
id: sufu
name: SUFU
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "SUFU (Suppressor of Fused) sequesters GLI1/GLI2/GLI3 in the cytoplasm to block Hedgehog target genes; SMO activation dissociates SUFU-GLI → GLI nuclear → BCC/medulloblastoma program; LOF → constitutive HH signaling; germline SUFU = elevated desmoplastic medulloblastoma risk."
aliases: ["SUFU", "Suppressor of Fused", "SUFU GLI", "SUFU Hedgehog", "SUFU medulloblastoma", "SUFU tumor suppressor", "SUFU SMO pathway", "SUFU BCC", "SUFU Gorlin"]
sources:
  - id: taylor-2002-sufu-medulloblastoma
    type: peer-reviewed
    cite: "Taylor MD, Liu L, Raffel C, et al. Mutations in SUFU predispose to medulloblastoma. Nat Genet. 2002;31(3):306-310."
    doi: "10.1038/ng916"
    pmid: "12068298"
    url: "https://doi.org/10.1038/ng916"
  - id: brugiere-2010-sufu-gorlin
    type: peer-reviewed
    cite: "Brugières L, Pierron G, Chompret A, et al. Incomplete penetrance of the predisposition to medulloblastoma associated with germ-line SUFU mutations. J Med Genet. 2010;47(2):142-144."
    doi: "10.1136/jmg.2009.067504"
    pmid: "19903819"
    url: "https://doi.org/10.1136/jmg.2009.067504"
cross_links:
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "SUFU acts downstream of SMO in the Hedgehog pathway; SMO activation (by SHH or mutation) promotes SUFU-GLI dissociation → GLI nuclear; vismodegib/sonidegib target SMO in BCC and medulloblastoma; SUFU LOF mimics constitutive SMO activation by releasing GLI constitutively."
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "PTCH1 normally inhibits SMO; SHH binding to PTCH1 relieves SMO inhibition → SMO activates SUFU release of GLI; germline PTCH1 = Gorlin syndrome (more BCCs, OKC, and less medulloblastoma than SUFU-associated Gorlin); somatic PTCH1 loss is the most common BCC driver."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "SUFU-GLI axis drives BCC: SUFU LOF → constitutive GLI1/2 nuclear → PTCH1/CCND1/HHIP upregulation → BCC; vismodegib/sonidegib target SMO upstream of SUFU; SUFU germline has lower BCC risk than PTCH1 but higher desmoplastic medulloblastoma risk."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Germline SUFU causes Gorlin-like syndrome: desmoplastic/nodular medulloblastoma risk (SHH subgroup, age <5) is higher than PTCH1-Gorlin; BCC and OKC are less penetrant; radiation avoidance is critical; SUFU loss releases GLI constitutively in cerebellar granule progenitors."
---

# SUFU

## Overview

**SUFU** (Suppressor of Fused; also SUFUH) encodes a 484 amino acid (60 kDa) cytoplasmic protein that functions as the **primary negative regulator of GLI transcription factors** within the **Hedgehog (HH) signaling pathway**. SUFU was originally identified genetically in *Drosophila* as a suppressor of the segment polarity gene *fused* (a casein kinase that promotes HH signaling). In vertebrates, SUFU is the central brake on the HH cascade: it binds and sequesters GLI1, GLI2, and GLI3 transcription factors in the cytoplasm, preventing their nuclear translocation and target gene activation in the absence of HH ligand. Germline SUFU pathogenic variants were linked to medulloblastoma predisposition by Taylor et al. in 2002 [^taylor-2002-sufu-medulloblastoma] [^brugiere-2010-sufu-gorlin].

**Hedgehog pathway overview — canonical vertebrate model:**

```
No HH ligand (OFF state):              HH ligand present (ON state):
PTCH1 inhibits SMO                     SHH/DHH/IHH binds PTCH1
    ↓                                       ↓ PTCH1 inhibition relieved
SUFU binds GLI2/GLI3 in cytoplasm          SMO moves to primary cilium → active
    ↓                                       ↓
CK1/GSK3/CSNK→ GLI phosphorylation         KIF7 + SUFU-GLI dissociation
    ↓                                       ↓
Partial proteolysis: GLI3R repressor    GLI2/GLI3FL nuclear
    ↓                                       ↓
Target gene repression                  PTCH1, CCND1, MYC, BCL2, GLI1 activated
```

In the ON state: SUFU is the key switch allowing GLI-FL (full-length) to escape from the cytoplasm. SUFU phosphorylation by SMO-activated kinases (PKA, CK1, GSK3) is relieved → SUFU-GLI interaction weakened → GLI-FL released → nuclear import.

## Structure

### SUFU protein domains

**N-terminal domain (aa 1-268):**
- Contains a highly conserved SUFU domain (Pfam: PF05010); forms a saddle-shaped structure with two lobes (N-lobe and C-lobe connected by a linker)
- N-lobe engages the **SYGH motif** in GLI transcription factors — conserved tetrapeptide in all three GLI family members (GLI1: Ser202-Tyr203-Gly204-His205; GLI2 and GLI3: similar)
- Specific contacts: SUFU Asn342, Arg344 contact the GLI backbone; SUFU Asp352 contacts GLI Ser residue; structural studies (X-ray 2.3 Å, Furtado 2014) show GLI SYGH motif buried in SUFU hydrophobic groove

**C-terminal domain (aa 269-484):**
- Provides additional GLI contacts beyond the SYGH motif; C-terminal domain contacts GLI zinc fingers (ZF)
- Also contains interaction surface for **SPOP** (Speckle-type POZ protein): SPOP recruits CULLIN3 E3 ubiquitin ligase → ubiquitinates SUFU-bound GLI for partial proteolysis; generates GLI repressors
- Nuclear export signal (NES) within C-terminal: SUFU itself can enter nucleus; nuclear SUFU may directly repress GLI at target promoters (HDAC-dependent) — nuclear role adds to cytoplasmic sequestration

**Germline pathogenic variants:**
- Truncating (frameshift, nonsense, splice): ~60% of SUFU germline pathogenic variants; complete protein loss
- Missense in N-domain (contacts GLI): Gly75Val, Trp234Arg; disrupt GLI binding
- Large deletions: detected by MLPA; rare
- Functional test: SUFU wild-type suppresses HH-induced GLI-luc reporter ~10-fold; SUFU mutants with pathogenic missense fail to suppress → validates GLI interaction

## Function

### SUFU in vertebrate Hedgehog signaling

**Primary cilium dependency:**
Vertebrate HH signaling (unlike *Drosophila*) is tightly coupled to the **primary cilium**:
- In OFF state: PTCH1 localizes to cilium tip → excludes SMO from cilium → SUFU-GLI complex at cilium → partial proteolysis generates GLI repressors (GLI3R primarily)
- In ON state: HH ligand → PTCH1 exits cilium → SMO enters cilium → SMO signals via GPR161 suppression and PKA inhibition → SUFU-GLI traffics to cilium tip → SUFU-GLI dissociation at cilium tip → GLI2FL/GLI1 released → cytoplasm → nucleus

**GLI family members and SUFU interactions:**
| GLI protein | SUFU interaction | Primary function | Cancer role |
|---|---|---|---|
| GLI1 | Binds SUFU; no repressor form | Transcriptional activator | BCC oncogene, target of pathway activation |
| GLI2 | Binds SUFU; partial GLI2R | Activator + minor repressor | Medulloblastoma, BCC; primary HH effector |
| GLI3 | Binds SUFU; strong GLI3R | Repressor predominates | Limb patterning; partial activator in HH-on |

**SUFU as tumor suppressor:**
In HH-driven tumors, SUFU loss → GLI1/GLI2 constitutively nuclear → PTCH1, CCND1, BCL2, MYC, MYCN, HHIP, GLI1 target genes activated → proliferation. SUFU-null cells have very high GLI1 levels and are refractory to upstream HH inhibition (SMO inhibitors are ineffective because SUFU is already absent — GLI is downstream of SUFU).

### SUFU in tumor types

**Sporadic medulloblastoma (SHH subgroup):**
- SHH-driven medulloblastoma: ~30% of all medulloblastoma; defined by HH pathway activation
- SUFU somatic LOF: ~10-15% of SHH-MB in adults; more common in infants (where SUFU germline is also prevalent)
- Other SHH-MB drivers: PTCH1 LOF (~40%), SMO activating mutations (~10%), GLI2 amplification (~7%), MYCN amplification
- SUFU-mutant and PTCH1-mutant SHH-MB: similar prognosis; GLI2-amplified SHH-MB has worse prognosis

**Basal cell carcinoma (BCC):**
- SUFU somatic LOF: ~5-8% of BCC; less common than PTCH1 (~85%) and SMO (~15-20%)
- SUFU loss in BCC: often large chromosomal deletion at 10q24-25 (SUFU locus); occurs in locally advanced/aggressive BCC
- SMO inhibitors (vismodegib/sonidegib): NOT effective in SUFU-mutant BCC (SUFU is downstream of SMO); need GLI-directed therapies (arsenic trioxide — direct GLI1 inhibitor; GANT61; not FDA-approved for BCC)

## Mechanism

### Germline SUFU and cancer predisposition

Germline SUFU pathogenic variants cause a phenotype that overlaps but differs from Gorlin syndrome (PTCH1 germline):

**SUFU germline features:**
- **Desmoplastic/nodular medulloblastoma**: the most penetrant feature; SHH subgroup; infancy and early childhood (<5 years); ~30-40% penetrance (Brugières 2010: incomplete penetrance); desmoplastic/nodular histology (large cell nodules with pale cytoplasm surrounded by desmoplastic stroma = "pale islands")
- **BCC**: present but less frequent and later onset than PTCH1-Gorlin
- **Odontogenic keratocysts (OKC)**: less penetrant than PTCH1-Gorlin
- **Calcified falx cerebri**: uncommon
- **Other HH-driven tumors**: meningioma (slight elevation), rhabdomyoma (cardiac)

**SUFU vs PTCH1 comparison:**

| Feature | PTCH1-Gorlin | SUFU germline |
|---|---|---|
| BCCs | Hundreds from teens-30s | Fewer; later onset |
| Medulloblastoma | ~5% lifetime (SHH group) | ~30-40% in children |
| MB histology | Classic or SHH subgroup | Desmoplastic/nodular exclusively |
| MB age at onset | Any childhood | Primarily <5 years |
| OKC | ~70% | ~30% |
| Calcified falx | ~80% | Less common |
| Surveillance priority | BCC surveillance + annual brain MRI | Brain MRI intensive in children |

**SMO inhibitor relevance:**
SUFU germline tumors are resistant to SMO inhibitors (SUFU is downstream of SMO). This makes SUFU-mutant medulloblastoma different from PTCH1/SMO-mutant SHH-MB in terms of therapeutic targeting: vismodegib/sonidegib not applicable in SUFU-null tumors; GLI-targeting strategies needed.

## Connections

- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — SUFU acts downstream of SMO in the Hedgehog pathway; SMO activation (by SHH or mutation) promotes SUFU-GLI dissociation → GLI nuclear; vismodegib/sonidegib target SMO in BCC and medulloblastoma; SUFU LOF mimics constitutive SMO activation by releasing GLI constitutively.
- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — PTCH1 normally inhibits SMO; SHH binding to PTCH1 relieves SMO inhibition → SMO activates SUFU release of GLI; germline PTCH1 = Gorlin syndrome (more BCCs, OKC, and less medulloblastoma than SUFU-associated Gorlin); somatic PTCH1 loss is the most common BCC driver.
- `connects-to` → **[Basal Cell Carcinoma](../../07-system/basal-cell-carcinoma/README.md)** — SUFU-GLI axis drives BCC: SUFU LOF → constitutive GLI1/2 nuclear → PTCH1/CCND1/HHIP upregulation → BCC; vismodegib/sonidegib target SMO upstream of SUFU; SUFU germline has lower BCC risk than PTCH1 but higher desmoplastic medulloblastoma risk.
- `connects-to` → **[Gorlin Syndrome](../../07-system/gorlin-syndrome/README.md)** — Germline SUFU causes Gorlin-like syndrome: desmoplastic/nodular medulloblastoma risk (SHH subgroup, age <5) is higher than PTCH1-Gorlin; BCC and OKC are less penetrant; radiation avoidance is critical; SUFU loss releases GLI constitutively in cerebellar granule progenitors.

[^taylor-2002-sufu-medulloblastoma]: Taylor MD, Liu L, Raffel C, et al. Mutations in SUFU predispose to medulloblastoma. *Nat Genet.* 2002;31(3):306-310. [doi:10.1038/ng916](https://doi.org/10.1038/ng916) · [PubMed 12068298](https://pubmed.ncbi.nlm.nih.gov/12068298/)
[^brugiere-2010-sufu-gorlin]: Brugières L, Pierron G, Chompret A, et al. Incomplete penetrance of the predisposition to medulloblastoma associated with germ-line SUFU mutations. *J Med Genet.* 2010;47(2):142-144. [doi:10.1136/jmg.2009.067504](https://doi.org/10.1136/jmg.2009.067504) · [PubMed 19903819](https://pubmed.ncbi.nlm.nih.gov/19903819/)
