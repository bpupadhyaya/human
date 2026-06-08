---
schema: human-scale-entry/v1
id: adamts13
name: ADAMTS13
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "ADAMTS13 (ADAMTS13; chr9q34.2) is a plasma metalloprotease that cleaves ultra-large von Willebrand factor (ULVWF); ADAMTS13 deficiency (<10% activity) → ULVWF accumulation → platelet microthrombi → TTP. Caplacizumab (anti-VWF nanobody; FDA 2019) is first-line for iTTP."
aliases: ["ADAMTS13", "ADAMTS-13", "VWF-cleaving protease", "VWFCP", "a disintegrin and metalloproteinase with thrombospondin type 1 motifs 13"]
sources:
  - id: zheng-2001-adamts13-discovery
    type: peer-reviewed
    cite: "Zheng X, Chung D, Takayama TK, et al. Structure of von Willebrand factor-cleaving protease (ADAMTS13), a metalloprotease involved in thrombotic thrombocytopenic purpura. J Biol Chem. 2001;276(44):41059-41063."
    doi: "10.1074/jbc.C100515200"
    pmid: "11557775"
    url: "https://doi.org/10.1074/jbc.C100515200"
  - id: scully-2019-caplacizumab-hercules
    type: peer-reviewed
    cite: "Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. N Engl J Med. 2019;380(4):335-346."
    doi: "10.1056/NEJMoa1806311"
    pmid: "30625070"
    url: "https://doi.org/10.1056/NEJMoa1806311"
  - id: peyvandi-2016-adamts13-review
    type: peer-reviewed
    cite: "Peyvandi F, Scully M, Kremer Hovinga JA, et al. Caplacizumab for acquired thrombotic thrombocytopenic purpura. N Engl J Med. 2016;374(6):511-522."
    doi: "10.1056/NEJMoa1505533"
    pmid: "26863353"
    url: "https://doi.org/10.1056/NEJMoa1505533"
cross_links:
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP: anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome: ADAMTS13 biallelic mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Acquired iTTP is caused by IgG autoantibodies against ADAMTS13 (predominantly IgG4, inhibiting; also IgG1 non-inhibiting); anti-ADAMTS13 IgG titer tracks disease; rituximab (anti-CD20) depletes ADAMTS13-antibody-producing B cells → durable remission in iTTP."
---

# ADAMTS13

## Overview

**ADAMTS13** (A Disintegrin and Metalloproteinase with ThromboSpondin type 1 motifs, member 13; gene *ADAMTS13*, chromosome 9q34.2) is a **plasma metalloprotease** and the principal physiological regulator of von Willebrand factor (VWF) multimer size. ADAMTS13 cleaves ultra-large VWF (ULVWF) multimers — the most thrombogenic forms — preventing spontaneous platelet aggregation in the microcirculation [^zheng-2001-adamts13-discovery].

**Severe ADAMTS13 deficiency (<10% of normal activity)** is the defining pathophysiology of **thrombotic thrombocytopenic purpura (TTP)**: ULVWF accumulates on endothelial surfaces → platelet binding via VWF A1 domain / platelet GPIb → microthrombi in arterioles and capillaries → thrombotic microangiopathy (TMA) → consumptive thrombocytopenia + microangiopathic hemolytic anemia (MAHA) + end-organ ischemia (brain, kidney, heart).

Two forms of ADAMTS13 deficiency:
- **Acquired iTTP (immune-mediated TTP; ~95% of cases):** Anti-ADAMTS13 IgG autoantibodies (inhibiting or accelerating clearance) → activity <10%; median age 40-50 years; F>M; associated with HIV, pregnancy, medications (e.g., ticlopidine)
- **Congenital TTP (Upshaw-Schulman syndrome; ~5%):** Biallelic *ADAMTS13* mutations → absent/severely reduced constitutive activity; presents in childhood or pregnancy (ULVWF release); treated with FFP infusion (ADAMTS13 replacement)

**Clinical significance:**
- ADAMTS13 activity <10% + TMA = TTP (>90% specificity; sensitivity ~95% for acquired iTTP)
- Mortality of untreated TTP: ~90%; with plasma exchange (PEX) alone: ~20%; with caplacizumab added: ~6% (HERCULES trial)
- Caplacizumab (anti-VWF A1 domain nanobody; Cablivi; FDA Feb 2019) is now first-line alongside PEX + immunosuppression

## Structure

### Protein architecture

| Feature | Detail |
|:--------|:-------|
| Gene | *ADAMTS13*, chromosome 9q34.2 |
| Protein | 1427 aa; ~190 kDa (glycosylated); predominantly hepatic synthesis; also endothelium, platelets, glial cells |
| Domain structure | Signal peptide → propeptide → metalloprotease (M) → disintegrin-like (Dis) → thrombospondin-1 (TSP1) → Cys-rich (Cys) → spacer (Sp) → TSP2-8 → CUB1-2 (C-terminal) |
| Active site | HEXXHXXGXXH zinc-binding motif in metalloprotease domain; Zn²⁺ coordinated by three histidines; E228 is catalytic glutamate |
| Cleavage site | VWF Tyr1605↓Met1606 in the A2 domain (exposed by hydrodynamic shear force or allosteric unfolding) |

### Exosite interactions with VWF

ADAMTS13 engages VWF through multiple exosite interactions spanning its entire length:
1. **Metalloprotease domain (exosite 1):** Contacts VWF A2 domain near cleavage site
2. **Disintegrin + Cys-rich + spacer domains (exosite 2):** Bind VWF D4/C1-C2 domains; spacer domain critical for substrate recognition
3. **TSP2-8 + CUB domains (distal exosites):** Bind unfolded VWF A2 and other regions; TSP8 binds VWF A3 domain; CUB domains mediate A2 allosteric interactions
4. **Shear-dependent activation:** Under physiological shear (>20 dyne/cm²) or on activated endothelium, VWF A2 domain mechanically unfolds → exposes Tyr1605-Met1606 cleavage site for ADAMTS13; static conditions: VWF A2 folded → inaccessible

### Autoantibody epitopes in iTTP

Anti-ADAMTS13 autoantibodies (IgG4 predominant) target multiple domains:
- **Spacer domain:** Most common target (>85% of patients); anti-spacer antibodies sterically block VWF A2 domain access → most strongly inhibiting
- **CUB domains:** Non-inhibiting antibodies that accelerate ADAMTS13 clearance without directly blocking activity
- **TSP8 domain:** Additional target; may combine with spacer antibodies for full inhibition
- **Epitope mapping guides therapy:** Patients with high-titer anti-spacer IgG4 have the most refractory disease; respond best to rituximab

## Function

### Normal VWF processing

ADAMTS13 performs ongoing surveillance and size regulation of VWF:
1. **Release:** Endothelial Weibel-Palade bodies release ULVWF (>10 million Da multimers) on stimulation (thrombin, histamine, DDAVP, inflammation)
2. **Tethering:** ULVWF strings remain anchored to endothelial surface via P-selectin/VWF A1 domain interaction → present platelet-binding A1 domain
3. **ADAMTS13 cleavage:** Circulating ADAMTS13 cleaves the tethered ULVWF at Tyr1605-Met1606 under shear → generates smaller VWF multimers → released into plasma
4. **Result:** Normal plasma VWF has a regulated multimer distribution; largest multimers (which have highest platelet binding affinity due to more GPIb-binding sites) are continuously cleared

**Without ADAMTS13:** ULVWF strings persist → GPIb/IX/V-mediated platelet aggregation → platelet-rich microthrombi in arterioles → TTP

## Mechanism

### Pathogenesis of acquired iTTP

**Triggering events:** Endothelial activation (infection, surgery, pregnancy, autoimmune flare) → ULVWF release from Weibel-Palade bodies → normally cleaved immediately

**Anti-ADAMTS13 IgG (iTTP mechanism):**
1. Anti-spacer domain IgG4 → steric blockade of ADAMTS13 active site access to VWF A2 → ADAMTS13 function inhibited (inhibiting antibodies)
2. Anti-CUB domain IgG → immune complex formation → FcRn-mediated clearance → ADAMTS13 plasma level falls (non-inhibiting clearance antibodies)
3. Combined effect: ADAMTS13 activity <10% → ULVWF accumulates on activated endothelium → platelet aggregation → microthrombi → TMA pentad

**Microthrombus formation:**
- Platelet GPIbα binds ULVWF A1 domain → platelet tethering and activation → P-selectin expression → secondary ADP, thromboxane, thrombin release → platelet plug
- RBC passage through narrowed microvessels → mechanical fragmentation → schistocytes (hallmark of MAHA on peripheral blood smear)
- Platelet consumption → thrombocytopenia (typically <30,000/μL in TTP)
- Microthrombi in cerebral arterioles → neurological symptoms; in renal → AKI (mild cf. HUS); in coronary → MI; in gut → abdominal pain

### Caplacizumab mechanism of action

**Caplacizumab (Cablivi; Sanofi):** Bivalent anti-VWF nanobody (two VHH single-domain antibodies linked in tandem) that binds VWF A1 domain → blocks VWF-GPIbα interaction → prevents platelet tethering to ULVWF strings → rapidly reverses acute platelet microthrombus formation [^scully-2019-caplacizumab-hercules].

**Key pharmacology:**
- Mechanism: Does NOT restore ADAMTS13 activity; does NOT cleave ULVWF → VWF activity blocked acutely while PEX removes antibodies and restores ADAMTS13
- Nanobody (VHH) half-life: ~4 hours free; bivalent design increases avidity; SC injection OD after IV loading
- Onset: Platelet count rise within 1-2 days (vs. 4-5 days with PEX alone in HERCULES)
- **HERCULES trial (N Engl J Med 2019):** PEX + caplacizumab vs. PEX + placebo in iTTP: time to platelet count normalization 2.69 vs. 2.88 days (p=0.01); TTP-related deaths, recurrence, or major thromboembolic events: 12% vs. 38% (p<0.001); 12% early relapse rate with caplacizumab (after stopping) in ADAMTS13-unreplenished patients → indicates need for concomitant immunosuppression to deplete autoantibodies

### ADAMTS13 activity testing

**Key assays:**
- **FRETS-VWF73 (fluorescent substrate):** Fluorogenic VWF73 peptide containing Tyr1605-Met1606; most widely used; results in minutes; <10% activity = TTP threshold
- **CBA (collagen-binding assay):** Measures VWF multimer degradation indirectly
- **Anti-ADAMTS13 IgG ELISA:** Titer correlates with severity; important for identifying inhibiting vs. non-inhibiting antibodies
- **Inhibitor assay (mixing study):** Mixes patient plasma with normal plasma → confirms inhibiting antibody (activity remains <50% with equal mixing)

## Connections

- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../../07-system/thrombotic-thrombocytopenic-purpura/README.md)** — ADAMTS13 deficiency (<10% activity) is the defining pathophysiology of TTP; acquired iTTP is driven by anti-ADAMTS13 IgG4 antibodies; hereditary Upshaw-Schulman syndrome involves biallelic ADAMTS13 mutations; caplacizumab blocks VWF A1 domain → prevents ULVWF-platelet binding.
- `connects-to` → **[Immunoglobulin G](../immunoglobulin-g/README.md)** — Acquired iTTP is caused by IgG autoantibodies against ADAMTS13 (predominantly IgG4 inhibiting; also IgG1 non-inhibiting); anti-ADAMTS13 IgG titer tracks disease; rituximab (anti-CD20) depletes ADAMTS13-antibody-producing B cells → durable remission in iTTP.

[^zheng-2001-adamts13-discovery]: Zheng X, Chung D, Takayama TK, et al. Structure of von Willebrand factor-cleaving protease (ADAMTS13), a metalloprotease involved in thrombotic thrombocytopenic purpura. *J Biol Chem.* 2001;276(44):41059-41063. [doi:10.1074/jbc.C100515200](https://doi.org/10.1074/jbc.C100515200) · [PubMed 11557775](https://pubmed.ncbi.nlm.nih.gov/11557775/)
[^scully-2019-caplacizumab-hercules]: Scully M, Cataland SR, Peyvandi F, et al. Caplacizumab treatment for acquired thrombotic thrombocytopenic purpura. *N Engl J Med.* 2019;380(4):335-346. [doi:10.1056/NEJMoa1806311](https://doi.org/10.1056/NEJMoa1806311) · [PubMed 30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/)
[^peyvandi-2016-adamts13-review]: Peyvandi F, Scully M, Kremer Hovinga JA, et al. Caplacizumab for acquired thrombotic thrombocytopenic purpura. *N Engl J Med.* 2016;374(6):511-522. [doi:10.1056/NEJMoa1505533](https://doi.org/10.1056/NEJMoa1505533) · [PubMed 26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
