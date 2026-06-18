---
schema: human-scale-entry/v1
id: myasthenia-gravis
name: Myasthenia Gravis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Myasthenia gravis (MG) is an autoimmune NMJ disease; AChR antibodies (85%) activate complement → AChR destruction → fatigable weakness; MuSK antibodies (6%) cause IgG4-mediated dysfunction. Pyridostigmine, steroids, thymectomy, eculizumab, and efgartigimod are treatments."
aliases: ["MG", "myasthenia gravis", "generalised myasthenia gravis", "gMG", "AChR antibody", "MuSK antibody", "seronegative MG", "myasthenic crisis", "ocular MG", "neuromuscular junction disease", "fatigable weakness", "ptosis", "diplopia"]
sources:
  - id: gilhus-2016-mg-review
    type: peer-reviewed
    cite: "Gilhus NE. Myasthenia Gravis. N Engl J Med. 2016;375(26):2570-2581."
    doi: "10.1056/NEJMra1602678"
    pmid: "28029925"
    url: "https://doi.org/10.1056/NEJMra1602678"
  - id: howard-2021-efgartigimod-adapt
    type: peer-reviewed
    cite: "Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT). Lancet Neurol. 2021;20(7):526-536."
    doi: "10.1016/S1474-4422(21)00159-9"
    pmid: "34146511"
    url: "https://doi.org/10.1016/S1474-4422(21)00159-9"
  - id: howard-2017-eculizumab-regain
    type: peer-reviewed
    cite: "Howard JF Jr, Utsugisawa K, Benatar M, et al. Safety and efficacy of eculizumab in anti-acetylcholine receptor antibody-positive refractory generalised myasthenia gravis (REGAIN). Lancet Neurol. 2017;16(12):976-986."
    doi: "10.1016/S1474-4422(17)30369-1"
    pmid: "29066163"
    url: "https://doi.org/10.1016/S1474-4422(17)30369-1"
cross_links:
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Anti-AChR IgG1/IgG3 in MG activates classical complement → C3b opsonization + MAC-mediated AChR destruction at the NMJ; reduces AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) increases ACh dwell time at the NMJ."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement-mediated AChR destruction drives AChR+ MG; eculizumab (anti-C5; REGAIN trial) and zilucoplan (subcutaneous anti-C5 peptide; RAISE trial; FDA Oct 2023) block terminal complement → prevent MAC formation at NMJ → reduce AChR destruction and MG severity."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Efgartigimod (Vyvgart; ADAPT trial: 68% vs. 30% minimal symptom expression at week 12) and rozanolixizumab (Rystiggo) target FcRn → block IgG recycling → accelerate anti-AChR IgG catabolism; efgartigimod FDA Dec 2021, rozanolixizumab FDA Jun 2023 for generalized AChR+ MG."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Thymic hyperplasia (germinal centers with AChR-reactive Th cells) in ~70% of AChR+ MG; thymoma (10-15%) produces AChR-reactive T cells escaping tolerance; MGTX trial (NEJM 2016) showed thymectomy + prednisone reduces disability in non-thymomatous AChR+ gMG."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets."
  - target: 01-human/03-molecular/snare-complex
    relation: connects-to
    note: "The SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Myasthenia gravis and multiple sclerosis are both autoimmune neurological diseases on opposite sides of the synapse and the immune system: MG is an antibody-and-complement attack on the neuromuscular junction (peripheral), while MS is T-cell demyelination of central myelin."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Antibody subclass dictates myasthenia gravis: AChR+ MG runs on complement-fixing IgG1/IgG3 (so eculizumab works), whereas MuSK+ MG is driven by non-complement IgG4 that blocks MuSK signaling; FcRn inhibitors like efgartigimod treat both by speeding IgG breakdown."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Myasthenia gravis is a postsynaptic disease: the motor neuron terminal releases acetylcholine normally, but antibody-mediated loss of muscle AChRs blunts the endplate response — distinguishing it from Lambert-Eaton syndrome, where antibodies block presynaptic calcium channels."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Myasthenia gravis is the prototypical neuromuscular-junction disease: anti-AChR (or MuSK) autoantibodies plus complement destroy the folded postsynaptic endplate, so repeated firing fatigues transmission → fluctuating weakness; AChE inhibitors raise available ACh."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Myasthenia gravis is a T-cell-dependent autoimmune disease: CD4+ T helper cells, often primed in a hyperplastic or thymomatous thymus, drive B cells to make high-affinity anti-AChR IgG; this T-cell help is why thymectomy and broad immunosuppression are therapeutic."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Myasthenia gravis and CIDP are both antibody/complement-mediated, treatable autoimmune neuromuscular disorders at different sites: MG hits the postsynaptic junction (fatigable weakness, normal reflexes), CIDP attacks nerve myelin (areflexia, sensory loss); both improve with IVIG."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Myasthenia gravis and neuromyelitis optica are antibody-mediated diseases that co-occur more than chance: both are driven by pathogenic IgG (anti-AChR vs anti-AQP4) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Myasthenia gravis and pemphigus vulgaris are paradigm IgG autoantibody diseases against a cell-surface protein: anti-acetylcholine-receptor in MG versus anti-desmoglein in pemphigus, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells sustain myasthenia gravis by making anti-acetylcholine-receptor antibodies: they secrete the IgG that blocks and destroys neuromuscular AChRs, and because they resist rituximab, plasma-cell-directed and FcRn-blocking therapies are used in refractory disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages execute the antibody attack in myasthenia gravis: anti-AChR IgG fixes complement and recruits macrophages that phagocytose the postsynaptic membrane, so innate effectors translate the autoantibody into loss of acetylcholine receptors at the neuromuscular junction."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Myasthenia gravis and rheumatoid arthritis are both antibody-mediated autoimmune diseases, but MG targets a single neuromuscular receptor while RA attacks the synovium broadly—yet both respond to B-cell depletion, reflecting shared autoreactive antibody-producing cells."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye is where myasthenia gravis usually begins: ptosis and diplopia from fatigable extraocular and eyelid muscles are the presenting sign in most patients, and ocular MG may stay confined to the eye or generalize—making the eye both first clue and prognostic marker."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell-depleting therapy is increasingly used in myasthenia gravis: rituximab against CD20 is especially effective in MuSK-antibody MG, removing the B cells that mature into the plasma cells making pathogenic acetylcholine-receptor antibodies."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Myasthenia gravis is a classic antibody-mediated autoimmune disease: autoantibodies against the acetylcholine receptor (or MuSK) and complement attack the neuromuscular junction, so it overlaps with other autoimmunity and responds to immunosuppression and thymectomy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Myasthenia gravis sits at the nervous system's output: it spares nerve and muscle themselves but attacks the neuromuscular junction where they meet, so signals fail to reach muscle—causing the fatigable weakness, ptosis and diplopia that define it."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Myasthenia gravis can become a respiratory emergency: when weakness spreads to the diaphragm and breathing muscles, a myasthenic crisis causes respiratory failure needing ventilation—so falling breathing capacity, not limb weakness, is the feared complication."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Myasthenia gravis clusters with autoimmune thyroid disease: Graves' and Hashimoto's coexist in many patients, reflecting shared loss of self-tolerance, and thyroid dysfunction can itself worsen muscle weakness—so thyroid testing is routine in MG."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "MG begins with broken thymic tolerance: the thymus normally trains regulatory T cells to ignore self, but in MG (often with thymic hyperplasia or thymoma) this fails, letting B cells make anti-acetylcholine-receptor antibodies—why thymectomy can help."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Myasthenia gravis is HLA-associated: MHC class II molecules present acetylcholine-receptor peptides to helper T cells in the thymus, breaking tolerance—the genetic and immunologic root of the anti-AChR antibodies that block the neuromuscular junction."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium triggers the signal myasthenia blocks downstream: nerve-terminal calcium influx releases acetylcholine, but in MG antibodies destroy the receptors that catch it—unlike Lambert-Eaton, which attacks the calcium channels themselves."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Myasthenia can reach the heart muscle: thymoma-associated MG may carry anti-striational antibodies that cause myocarditis and arrhythmia, so cardiac symptoms in MG (especially with thymoma) prompt evaluation of the heart, not just skeletal muscle."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Myasthenia silences a sodium gate at the muscle: the acetylcholine receptor it attacks is a sodium-admitting channel, so when antibodies destroy these receptors, too little sodium flows in to fire the muscle, and the endplate fails to reach threshold."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 fuels the antibody factories of myasthenia: it drives the thymic germinal centers that churn out anti-receptor antibodies, which is why IL-6-pathway blockers are being trialed to dampen the autoimmune attack at its source."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help start myasthenia in the thymus: by presenting acetylcholine-receptor fragments to T cells in the abnormal thymus, they prime the immune response that licenses B cells to make the receptor-blocking antibodies."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "A myasthenic crisis can choke off oxygen: when weakness spreads to the breathing muscles, ventilation fails and blood oxygen falls, the emergency that lands patients on a ventilator and defines the disease's gravest turn."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Myasthenia from a thymoma can hit the bone marrow: the same tumor that drives the autoimmunity can trigger paraneoplastic pure red cell aplasia, shutting down marrow red-cell production alongside the muscle disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Myasthenia, especially with thymoma, can inflame the heart: autoimmune myocarditis and conduction problems occur, so cardiac symptoms in a myasthenic patient prompt a search for heart involvement beyond the muscles."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "MG's hidden thymoma is found by imaging: chest CT photons screen for the thymus tumor that drives many cases, prompting the thymectomy that can improve the disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium is dangerous in myasthenia: high levels block acetylcholine release at the junction, so intravenous magnesium—as given for eclampsia—can trigger a sudden myasthenic crisis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Myasthenia plays out where peripheral nerve meets muscle: the motor nerve terminal releases acetylcholine that antibody-blocked receptors can't fully receive, and in the related LEMS the nerve terminal itself is attacked."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the damaged endplate: where antibodies have attacked, the postsynaptic membrane's deep folds flatten and simplify and the synaptic cleft widens, so the acetylcholine that does arrive finds far fewer receptors to act on."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium swings unmask the weakness: because neuromuscular transmission is already marginal, disturbances in potassium and certain drugs that affect it can abruptly worsen myasthenic weakness, a hazard during illness and surgery."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Treatment leans on the adrenal hormone: long-term corticosteroids are a mainstay that suppress the autoimmune attack but also suppress the body's own adrenal output, so steroids must be tapered carefully to avoid a crisis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Myasthenia is named by its antibodies: most patients carry anti-acetylcholine-receptor antibodies, a minority anti-MuSK or anti-LRP4, and these autoantibodies both confirm the diagnosis and are the very cause of the weakness."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "The antibodies destroy the junction through complement: anti-AChR IgG fixes complement to riddle the postsynaptic membrane with membrane-attack complex, which is why complement-blocking drugs like eculizumab help refractory disease."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Myasthenia spares the involuntary muscles: it attacks only the nicotinic junctions of voluntary striated muscle, leaving the smooth muscle of gut and vessels — which runs on different receptors — untouched, so the weakness never reaches them."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Fatigable weakness is its signature: myasthenia tires the voluntary muscles with use — drooping eyelids, weak chewing, a failing grip by evening — and a myasthenic crisis of the breathing muscles is its life-threatening extreme."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Antibodies can cross to the baby: maternal anti-AChR IgG traverses the placenta to cause a transient neonatal myasthenia, and the disease's course and drugs must be managed carefully through pregnancy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The immunosuppression carries a cost: the steroids, azathioprine, and rituximab used to control myasthenia suppress the marrow and immunity, dropping neutrophils and raising the infection risk that monitoring guards against."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF keeps the autoantibody factories alive: the cytokine rescues the autoreactive B cells that make anti-AChR antibody, so it runs high in myasthenia and is a target of B-cell-directed therapy."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Myasthenia keeps autoimmune company: it co-occurs with lupus and other autoimmune diseases more often than chance, reflecting a shared genetic susceptibility to losing self-tolerance."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The antibody source hides in lymphoid tissue: long-lived plasma cells in the spleen and marrow keep secreting anti-AChR antibody, which is why B-cell depletion can fail to clear it and plasma exchange is used in crisis."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Myasthenia is a disease of one synapse: anti-AChR antibody, complement, and receptor internalization destroy the postsynaptic folds of the neuromuscular junction, so each nerve impulse fails to reach threshold and the muscle fatigues."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "The thymus grows the wrong germinal centers: thymic hyperplasia in myasthenia forms ectopic germinal centers that school autoreactive B cells against AChR, which is why thymectomy can improve the disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "A Th17 arm drives the autoimmunity: IL-17A from helper T cells promotes germinal-center responses and the anti-AChR antibody production in myasthenia, running higher in more active and refractory disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB sustains the autoreactive B cells: BAFF and inflammatory signals act through NF-κB in the ectopic thymic germinal centers to keep the anti-AChR antibody response alive, part of the B-cell biology rituximab targets."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A myasthenic crisis collides with infection: respiratory-muscle weakness causes aspiration and ventilator dependence while immunosuppressive therapy lowers defenses, so pneumonia and sepsis are major dangers — and infection itself often triggers the crisis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Crisis and its treatment raise clot risk: immobility during a myasthenic crisis plus the prothrombotic effect of intravenous immunoglobulin therapy increase the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Long-term steroids thin the bone: the prolonged corticosteroids that control myasthenia gravis, compounded by reduced mobility during weakness, accelerate bone loss and raise osteoporotic fracture risk."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its immunosuppression opens the lung: the steroids, azathioprine and rituximab used for myasthenia gravis can deplete T-cell defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmunity keeps company: myasthenia gravis frequently coexists with other autoimmune diseases including Sjögren's syndrome, reflecting a shared predisposition to loss of self-tolerance."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its immunosuppression opens the lung to mold: the corticosteroids, azathioprine and rituximab used to control myasthenia gravis blunt immunity, occasionally permitting invasive pulmonary aspergillosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its long steroid courses raise blood sugar: the prolonged high-dose corticosteroids used to suppress myasthenia gravis induce insulin resistance and frequently precipitate steroid-induced diabetes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Fluctuating weakness and steroids weigh on mood: the unpredictable muscle weakness, fear of crisis and corticosteroid mood effects of myasthenia gravis contribute to depression and impaired quality of life."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "A crisis can paralyse breathing: weakness of the diaphragm and bulbar muscles in a myasthenic crisis causes neuromuscular respiratory failure, the most dangerous manifestation, requiring ventilation."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Bulbar weakness disrupts swallowing: myasthenia gravis weakens the muscles of chewing and swallowing, causing dysphagia and aspiration, while pyridostigmine's cholinergic effect brings cramps and diarrhoea."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with autoimmune thyroid disease: myasthenia gravis frequently coexists with Graves' disease and Hashimoto's thyroiditis, and thyroid dysfunction can itself worsen the muscle weakness."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The thymus drives the disease: thymic hyperplasia and thymoma generate the autoreactive response against acetylcholine receptors, which is why thymectomy improves outcomes in myasthenia gravis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can inflame the heart: autoimmune myocarditis occurs especially with thymoma and anti-striational antibodies, causing arrhythmia and heart failure that complicate the disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its thymoma brings skin autoimmunity: thymoma-associated myasthenia can accompany paraneoplastic pemphigus and other cutaneous autoimmune disease, reflecting the syndrome's broad autoreactivity."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment, not the disease, reaches the kidney: long-term calcineurin-inhibitor immunosuppression for myasthenia is nephrotoxic, and a thymoma can rarely associate with membranous nephropathy."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "Some common drugs worsen it: beta-blockers, like aminoglycosides and intravenous magnesium, can impair neuromuscular transmission and unmask or aggravate myasthenia gravis."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Infection can tip it into crisis: a respiratory infection such as pneumococcal pneumonia is a frequent trigger of life-threatening myasthenic crisis, and vaccination is advised before immunosuppression."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "The mainstay of immunosuppression: corticosteroids are first-line for moderate-to-severe myasthenia gravis, though high starting doses can transiently worsen weakness before the disease improves."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Cancer immunotherapy can trigger it: PD-1 and CTLA-4 checkpoint inhibitors cause a severe immune-related myasthenia gravis, often overlapping with myositis and myocarditis, that can be life-threatening."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "It runs with other autoimmunity: myasthenia gravis clusters with autoimmune thyroid disease, type 1 diabetes and other organ-specific autoimmune conditions, reflecting a shared loss of self-tolerance."
---

# Myasthenia Gravis

## Overview

**Myasthenia gravis (MG)** is an autoimmune disease of the **neuromuscular junction (NMJ)** characterized by **fatigable muscle weakness** — weakness that worsens with repeated activity and improves with rest [^gilhus-2016-mg-review]. MG is the most common primary disorder of neuromuscular transmission and affects approximately 150-200 per 100,000 people globally (prevalence increasing with aging populations).

**The defining feature** is autoantibody-mediated impairment of acetylcholine receptor (AChR) function at the motor endplate, resulting in insufficient neuromuscular transmission. With each nerve impulse, acetylcholine (ACh) release is normal, but fewer AChRs are available to respond → reduced end-plate potential → failure to reach action potential threshold → impaired muscle contraction, especially with repetitive stimulation.

**Serological classification (critical for treatment decisions):**

| Antibody type | Prevalence | Target | Mechanism | Thymus |
|---|---|---|---|---|
| Anti-AChR (IgG1/IgG3) | ~85% | AChR α-subunit (main immunogenic region, MIR) | Complement activation → MAC → AChR destruction; receptor internalization; functional blockade | Thymic hyperplasia (70%); thymoma (10-15%) |
| Anti-MuSK (IgG4) | ~6% | Muscle-specific kinase (MuSK; agrin receptor) | IgG4 blocks MuSK-agrin signaling → AChR clustering failure; NO complement activation | Normal thymus usually |
| Anti-LRP4 (IgG1/2) | ~2-3% | LDL receptor-related protein 4 | Blocks LRP4-agrin-MuSK signaling → AChR clustering | Normal |
| Anti-agrin | ~2% | Agrin (muscle-specific) | Disrupts NMJ architecture | Normal |
| Seronegative | ~10% | Unknown (may have low-titer AChR or novel targets) | Unknown | Thymic hyperplasia may be present |

**Clinical subtypes:**
- **Ocular MG (OMG):** Restricted to levator palpebrae (ptosis) and extraocular muscles (diplopia); ~50% of patients at onset; 15% remain purely ocular after 2 years; high risk of progression to generalized
- **Generalized MG (gMG):** Limb, bulbar (dysphagia, dysarthria), axial, or respiratory muscle involvement; severity graded by MGFA classification (Class I ocular to Class V intubated)

## Structure

### NMJ anatomy and MG pathophysiology

**Normal NMJ:**
- Motor nerve terminal → releases ACh from synaptic vesicles (via SNARE complex: VAMP/synaptobrevin + SNAP-25 + syntaxin)
- ACh diffuses 50 nm across synaptic cleft → binds **AChR** (nicotinic α1β1γδ or α1β1εδ in adult) on muscle endplate → Na⁺ influx → depolarization → action potential → muscle contraction
- AChE (acetylcholinesterase) in basal lamina terminates ACh signal

**Pathogenesis in AChR+ MG:**

**Step 1 — Thymic sensitization:**
- Thymic myoid cells normally express AChR (function: clonal deletion of self-reactive T cells)
- In MG thymus (hyperplastic germinal centers): AChR-specific CD4+ T cells escaping deletion interact with thymic B cells → anti-AChR IgG production
- **Thymoma** (10-15% of MG): tumor produces AChR-reactive T cells that escape tolerance → systemic anti-AChR humoral immunity; thymoma patients often have more refractory disease

**Step 2 — Anti-AChR IgG effector mechanisms:**
1. **Complement-mediated destruction:** Anti-AChR IgG1/IgG3 → Fc-mediated C1q binding → classical complement cascade → C3b → C5 → MAC (C5b-9) → membrane attack on motor endplate → AChR degradation and structural endplate damage (simplified postsynaptic membrane)
2. **Receptor internalization (antigenic modulation):** Cross-linking of AChRs by bivalent IgG → accelerated receptor internalization and lysosomal degradation → loss of surface AChR
3. **Direct functional blockade:** Some anti-AChR antibodies bind at or near the ACh-binding site → competitive inhibition of ACh binding

**Step 3 — Impaired NMJ safety factor:**
- Normal NMJ: ACh release → EPP amplitude ~60-70 mV; action potential threshold ~-45 mV → large "safety factor"
- In MG: reduced AChR density → EPP amplitude reduced → may fall below action potential threshold with repetitive stimulation → fatigable weakness (classical electrophysiological correlate: ≥10% decrement on 3 Hz RNS)

**MuSK+ MG mechanism:**
- MuSK normally clusters AChRs at the endplate via the agrin-LRP4-MuSK signaling axis
- IgG4 anti-MuSK → blocks agrin binding to MuSK → disrupts AChR clustering → dispersed, fewer AChRs
- No complement activation (IgG4 does not activate C1q) → complement inhibitors (eculizumab) less effective
- Clinical phenotype: bulbar-predominant, facial/neck weakness, respiratory vulnerability; worse prognosis; not improved by thymectomy

## Function

### Diagnosis

**Antibody testing:**
- Anti-AChR (ELISA binding assay): sensitivity ~85% generalized, ~50-60% ocular MG
- Anti-MuSK (cell-based assay or ELISA): ordered if AChR-negative gMG
- Anti-LRP4, anti-agrin: specialized labs
- AChR blocking assay: ~20% additional positivity in AChR-binding–negative generalized MG

**Pharmacological testing:**
- **Edrophonium test (Tensilon test):** Ultra-short–acting reversible AChE inhibitor; transient dramatic improvement of ptosis/diplopia; sensitivity ~80-95% but false positives possible; rarely used now given ab testing

**Neurophysiology:**
- **Repetitive nerve stimulation (3 Hz RNS):** ≥10% decrement in compound muscle action potential amplitude is diagnostic; most sensitive in proximal/facial muscles
- **Single-fiber EMG (SFEMG):** Most sensitive test (~96-100%); measures jitter (variability of inter-potential interval); elevated jitter = impaired NMJ transmission; gold standard for seronegative MG

**Imaging:**
- **CT chest:** All MG patients screened for thymoma; MRI chest for equivocal CT
- **PET-CT:** Occasionally used for thymoma staging

**Clinical scores:**
- **QMG (Quantitative MG Score):** 13-item semi-quantitative scale; used as primary endpoint in MG trials; range 0-39
- **MGFA Classification (Class I-V):** Severity classification system
- **MG Activities of Daily Living (MG-ADL):** Patient-reported; 8 items; used in trials

## Pathology

### Therapies

**Symptomatic:**
- **Pyridostigmine (Mestinon):** Reversible AChE inhibitor (carbamate); increases ACh concentration at NMJ; 30-60 mg PO Q3-6H; rapid onset; does NOT modify disease course; avoidance in MuSK+ (may worsen bulbar symptoms)

**Immunosuppression (disease-modifying):**
- **Corticosteroids:** Prednisone 1 mg/kg/day; initial transient worsening in first 2-4 weeks (mechanism uncertain — may reduce ACh release); taper after remission; steroid-sparing agents needed for chronic therapy
- **Azathioprine (AZA):** 6-MP prodrug; purine synthesis inhibitor → lymphocyte suppression; steroid-sparing; onset 6-12 months (delayed efficacy); ~50% require combination; thiopurine methyltransferase (TPMT) genotyping before starting
- **Mycophenolate mofetil (MMF):** IMDPH inhibitor → lymphocyte suppression; onset 6-12 months; equivalent efficacy to AZA; preferred when TPMT-deficient
- **Rituximab (anti-CD20):** Effective particularly in **MuSK+ MG** (IgG4-mediated, B-cell dependent); 375 mg/m² × 4 weekly or 1g × 2; durable response in many patients; no RCT evidence in AChR+ MG but used

**Thymectomy:**
- **MGTX trial (Wolfe et al., NEJM 2016):** 126 patients, non-thymomatous AChR+ gMG age 18-65; thymectomy + prednisolone vs. prednisolone alone; 3-year minimal manifestation status: thymectomy 67% vs. 47%; lower steroid requirement; FDA guidance updated to recommend for non-thymomatous AChR+ MG
- **Thymoma:** All thymoma-associated MG requires thymectomy regardless of disease severity; thymoma resection does not reliably improve MG

**Acute/Crisis management:**
- **IVIG (2 g/kg over 2-5 days):** Rapid efficacy (days); non-specific immunomodulation; preferred in myasthenic crisis
- **Plasma exchange (PLEX):** Faster onset than IVIG; removes pathogenic anti-AChR IgG directly; 5-7 exchanges over 10-14 days; preferred if rapid intubation at risk
- **Myasthenic crisis triggers:** Infections (especially respiratory); surgery/anesthesia; aminoglycosides; fluoroquinolones; beta-blockers; magnesium; chloroquine/hydroxychloroquine; D-penicillamine

**Complement inhibitors:**
- **Eculizumab (Soliris; anti-C5 mAb; Alexion/AZ):** REGAIN trial (n=125; refractory AChR+ gMG): 26.3% vs. 13.5% QMG responders; Muppidi re-analysis: substantial functional improvement; FDA approved October 2017; IV Q2W; requires meningococcal vaccination [^howard-2017-eculizumab-regain]
- **Ravulizumab (Ultomiris; anti-C5; Alexion/AZ):** Extended half-life anti-C5 (Q8W IV); CHAMPION MG trial (n=175): 29.7% vs. 11.5% QMG response; FDA approved April 2022; superior convenience vs. eculizumab
- **Zilucoplan (Zilbrysq; anti-C5 peptidomimetic macrocycle; UCB):** Subcutaneous daily self-injection; RAISE trial (n=174): QMG -4.39 vs. -2.30 (p=0.0005); FDA approved October 2023; first SC complement inhibitor for MG

**FcRn inhibitors:**
- **Efgartigimod (Vyvgart; argenx):** Engineered Fc fragment competing with IgG for FcRn → ~75% IgG reduction → reduces anti-AChR titers; ADAPT trial (n=167, AChR+ subgroup): 68% vs. 30% minimal symptom expression (MG-ADL ≥4 improvement maintained); FDA approved December 2021 for AChR+ gMG; IV Q1W ×4 cycles [^howard-2021-efgartigimod-adapt]; SC formulation (Vyvgart Hytrulo) approved 2023
- **Rozanolixizumab (Rystiggo; UCB):** Humanized anti-FcRn mAb; ~70% IgG reduction; MG0002 Phase 3: primary endpoint met; FDA approved June 2023 for AChR+ or MuSK+ gMG

## Connections

- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Anti-AChR IgG1/IgG3 in MG activates classical complement → C3b opsonization + MAC-mediated AChR destruction at the NMJ; reduces AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) increases ACh dwell time at the NMJ.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement-mediated AChR destruction drives AChR+ MG; eculizumab (anti-C5; REGAIN trial) and zilucoplan (subcutaneous anti-C5 peptide; RAISE trial; FDA Oct 2023) block terminal complement → prevent MAC formation at NMJ → reduce AChR destruction and MG severity.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — Efgartigimod (Vyvgart; ADAPT trial: 68% vs. 30% minimal symptom expression at week 12) and rozanolixizumab (Rystiggo) target FcRn → block IgG recycling → accelerate anti-AChR IgG catabolism; efgartigimod FDA Dec 2021, rozanolixizumab FDA Jun 2023 for generalized AChR+ MG.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — thymic hyperplasia (germinal centers with AChR-reactive Th cells) in ~70% of AChR+ MG; thymoma (10-15%) produces AChR-reactive T cells escaping tolerance; MGTX trial (NEJM 2016) showed thymectomy + prednisone reduces disability in non-thymomatous AChR+ gMG.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets.
- `connects-to` → **[SNARE Complex](../../03-molecular/snare-complex/README.md)** — the SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Myasthenia gravis and multiple sclerosis are both autoimmune neurological diseases on opposite sides of the synapse and the immune system: MG is an antibody-and-complement attack on the neuromuscular junction (peripheral), while MS is T-cell demyelination of central myelin.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Antibody subclass dictates myasthenia gravis: AChR+ MG runs on complement-fixing IgG1/IgG3 (so eculizumab works), whereas MuSK+ MG is driven by non-complement IgG4 that blocks MuSK signaling; FcRn inhibitors like efgartigimod treat both by speeding IgG breakdown.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Myasthenia gravis is a postsynaptic disease: the motor neuron terminal releases acetylcholine normally, but antibody-mediated loss of muscle AChRs blunts the endplate response — distinguishing it from Lambert-Eaton syndrome, where antibodies block presynaptic calcium channels.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Myasthenia gravis is the prototypical neuromuscular-junction disease: anti-AChR (or MuSK) autoantibodies plus complement destroy the folded postsynaptic endplate, so repeated firing fatigues transmission → fluctuating weakness; AChE inhibitors raise available ACh.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Myasthenia gravis is a T-cell-dependent autoimmune disease: CD4+ T helper cells, often primed in a hyperplastic or thymomatous thymus, drive B cells to make high-affinity anti-AChR IgG; this T-cell help is why thymectomy and broad immunosuppression are therapeutic.
- `connects-to` → **[CIDP](../cidp/README.md)** — Myasthenia gravis and CIDP are both antibody/complement-mediated, treatable autoimmune neuromuscular disorders at different sites: MG hits the postsynaptic junction (fatigable weakness, normal reflexes), CIDP attacks nerve myelin (areflexia, sensory loss); both improve with IVIG.
- `connects-to` → **[NMOSD](../nmo/README.md)** — Myasthenia gravis and neuromyelitis optica are antibody-mediated diseases that co-occur more than chance: both are driven by pathogenic IgG (anti-AChR vs anti-AQP4) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Myasthenia gravis and pemphigus vulgaris are paradigm IgG autoantibody diseases against a cell-surface protein: anti-acetylcholine-receptor in MG versus anti-desmoglein in pemphigus, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells sustain myasthenia gravis by making anti-acetylcholine-receptor antibodies: they secrete the IgG that blocks and destroys neuromuscular AChRs, and because they resist rituximab, plasma-cell-directed and FcRn-blocking therapies are used in refractory disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages execute the antibody attack in myasthenia gravis: anti-AChR IgG fixes complement and recruits macrophages that phagocytose the postsynaptic membrane, so innate effectors translate the autoantibody into loss of acetylcholine receptors at the neuromuscular junction.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Myasthenia gravis and rheumatoid arthritis are both antibody-mediated autoimmune diseases, but MG targets a single neuromuscular receptor while RA attacks the synovium broadly—yet both respond to B-cell depletion, reflecting shared autoreactive antibody-producing cells.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye is where myasthenia gravis usually begins: ptosis and diplopia from fatigable extraocular and eyelid muscles are the presenting sign in most patients, and ocular MG may stay confined to the eye or generalize—making the eye both first clue and prognostic marker.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — B-cell-depleting therapy is increasingly used in myasthenia gravis: rituximab against CD20 is especially effective in MuSK-antibody MG, removing the B cells that mature into the plasma cells making pathogenic acetylcholine-receptor antibodies.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Myasthenia gravis is a classic antibody-mediated autoimmune disease: autoantibodies against the acetylcholine receptor (or MuSK) and complement attack the neuromuscular junction, so it overlaps with other autoimmunity and responds to immunosuppression and thymectomy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Myasthenia gravis sits at the nervous system's output: it spares nerve and muscle themselves but attacks the neuromuscular junction where they meet, so signals fail to reach muscle—causing the fatigable weakness, ptosis and diplopia that define it.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Myasthenia gravis can become a respiratory emergency: when weakness spreads to the diaphragm and breathing muscles, a myasthenic crisis causes respiratory failure needing ventilation—so falling breathing capacity, not limb weakness, is the feared complication.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Myasthenia gravis clusters with autoimmune thyroid disease: Graves' and Hashimoto's coexist in many patients, reflecting shared loss of self-tolerance, and thyroid dysfunction can itself worsen muscle weakness—so thyroid testing is routine in MG.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — MG begins with broken thymic tolerance: the thymus normally trains regulatory T cells to ignore self, but in MG (often with thymic hyperplasia or thymoma) this fails, letting B cells make anti-acetylcholine-receptor antibodies—why thymectomy can help.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Myasthenia gravis is HLA-associated: MHC class II molecules present acetylcholine-receptor peptides to helper T cells in the thymus, breaking tolerance—the genetic and immunologic root of the anti-AChR antibodies that block the neuromuscular junction.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium triggers the signal myasthenia blocks downstream: nerve-terminal calcium influx releases acetylcholine, but in MG antibodies destroy the receptors that catch it—unlike Lambert-Eaton, which attacks the calcium channels themselves.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Myasthenia can reach the heart muscle: thymoma-associated MG may carry anti-striational antibodies that cause myocarditis and arrhythmia, so cardiac symptoms in MG (especially with thymoma) prompt evaluation of the heart, not just skeletal muscle.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Myasthenia silences a sodium gate at the muscle: the acetylcholine receptor it attacks is a sodium-admitting channel, so when antibodies destroy these receptors, too little sodium flows in to fire the muscle, and the endplate fails to reach threshold.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 fuels the antibody factories of myasthenia: it drives the thymic germinal centers that churn out anti-receptor antibodies, which is why IL-6-pathway blockers are being trialed to dampen the autoimmune attack at its source.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help start myasthenia in the thymus: by presenting acetylcholine-receptor fragments to T cells in the abnormal thymus, they prime the immune response that licenses B cells to make the receptor-blocking antibodies.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — A myasthenic crisis can choke off oxygen: when weakness spreads to the breathing muscles, ventilation fails and blood oxygen falls, the emergency that lands patients on a ventilator and defines the disease's gravest turn.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Myasthenia from a thymoma can hit the bone marrow: the same tumor that drives the autoimmunity can trigger paraneoplastic pure red cell aplasia, shutting down marrow red-cell production alongside the muscle disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Myasthenia, especially with thymoma, can inflame the heart: autoimmune myocarditis and conduction problems occur, so cardiac symptoms in a myasthenic patient prompt a search for heart involvement beyond the muscles.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — MG's hidden thymoma is found by imaging: chest CT photons screen for the thymus tumor that drives many cases, prompting the thymectomy that can improve the disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium is dangerous in myasthenia: high levels block acetylcholine release at the junction, so intravenous magnesium—as given for eclampsia—can trigger a sudden myasthenic crisis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Myasthenia plays out where peripheral nerve meets muscle: the motor nerve terminal releases acetylcholine that antibody-blocked receptors can't fully receive, and in the related LEMS the nerve terminal itself is attacked.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the damaged endplate: where antibodies have attacked, the postsynaptic membrane's deep folds flatten and simplify and the synaptic cleft widens, so the acetylcholine that does arrive finds far fewer receptors to act on.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium swings unmask the weakness: because neuromuscular transmission is already marginal, disturbances in potassium and certain drugs that affect it can abruptly worsen myasthenic weakness, a hazard during illness and surgery.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Treatment leans on the adrenal hormone: long-term corticosteroids are a mainstay that suppress the autoimmune attack but also suppress the body's own adrenal output, so steroids must be tapered carefully to avoid a crisis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Myasthenia is named by its antibodies: most patients carry anti-acetylcholine-receptor antibodies, a minority anti-MuSK or anti-LRP4, and these autoantibodies both confirm the diagnosis and are the very cause of the weakness.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The antibodies destroy the junction through complement: anti-AChR IgG fixes complement to riddle the postsynaptic membrane with membrane-attack complex, which is why complement-blocking drugs like eculizumab help refractory disease.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Myasthenia spares the involuntary muscles: it attacks only the nicotinic junctions of voluntary striated muscle, leaving the smooth muscle of gut and vessels — which runs on different receptors — untouched, so the weakness never reaches them.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Fatigable weakness is its signature: myasthenia tires the voluntary muscles with use — drooping eyelids, weak chewing, a failing grip by evening — and a myasthenic crisis of the breathing muscles is its life-threatening extreme.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Antibodies can cross to the baby: maternal anti-AChR IgG traverses the placenta to cause a transient neonatal myasthenia, and the disease's course and drugs must be managed carefully through pregnancy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The immunosuppression carries a cost: the steroids, azathioprine, and rituximab used to control myasthenia suppress the marrow and immunity, dropping neutrophils and raising the infection risk that monitoring guards against.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF keeps the autoantibody factories alive: the cytokine rescues the autoreactive B cells that make anti-AChR antibody, so it runs high in myasthenia and is a target of B-cell-directed therapy.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Myasthenia keeps autoimmune company: it co-occurs with lupus and other autoimmune diseases more often than chance, reflecting a shared genetic susceptibility to losing self-tolerance.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The antibody source hides in lymphoid tissue: long-lived plasma cells in the spleen and marrow keep secreting anti-AChR antibody, which is why B-cell depletion can fail to clear it and plasma exchange is used in crisis.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Myasthenia is a disease of one synapse: anti-AChR antibody, complement, and receptor internalization destroy the postsynaptic folds of the neuromuscular junction, so each nerve impulse fails to reach threshold and the muscle fatigues.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — The thymus grows the wrong germinal centers: thymic hyperplasia in myasthenia forms ectopic germinal centers that school autoreactive B cells against AChR, which is why thymectomy can improve the disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17 arm drives the autoimmunity: IL-17A from helper T cells promotes germinal-center responses and the anti-AChR antibody production in myasthenia, running higher in more active and refractory disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB sustains the autoreactive B cells: BAFF and inflammatory signals act through NF-κB in the ectopic thymic germinal centers to keep the anti-AChR antibody response alive, part of the B-cell biology rituximab targets.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A myasthenic crisis collides with infection: respiratory-muscle weakness causes aspiration and ventilator dependence while immunosuppressive therapy lowers defenses, so pneumonia and sepsis are major dangers — and infection itself often triggers the crisis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Crisis and its treatment raise clot risk: immobility during a myasthenic crisis plus the prothrombotic effect of intravenous immunoglobulin therapy increase the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Long-term steroids thin the bone: the prolonged corticosteroids that control myasthenia gravis, compounded by reduced mobility during weakness, accelerate bone loss and raise osteoporotic fracture risk.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its immunosuppression opens the lung: the steroids, azathioprine and rituximab used for myasthenia gravis can deplete T-cell defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmunity keeps company: myasthenia gravis frequently coexists with other autoimmune diseases including Sjögren's syndrome, reflecting a shared predisposition to loss of self-tolerance.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its immunosuppression opens the lung to mold: the corticosteroids, azathioprine and rituximab used to control myasthenia gravis blunt immunity, occasionally permitting invasive pulmonary aspergillosis.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its long steroid courses raise blood sugar: the prolonged high-dose corticosteroids used to suppress myasthenia gravis induce insulin resistance and frequently precipitate steroid-induced diabetes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Fluctuating weakness and steroids weigh on mood: the unpredictable muscle weakness, fear of crisis and corticosteroid mood effects of myasthenia gravis contribute to depression and impaired quality of life.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — A crisis can paralyse breathing: weakness of the diaphragm and bulbar muscles in a myasthenic crisis causes neuromuscular respiratory failure, the most dangerous manifestation, requiring ventilation.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Bulbar weakness disrupts swallowing: myasthenia gravis weakens the muscles of chewing and swallowing, causing dysphagia and aspiration, while pyridostigmine's cholinergic effect brings cramps and diarrhoea.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with autoimmune thyroid disease: myasthenia gravis frequently coexists with Graves' disease and Hashimoto's thyroiditis, and thyroid dysfunction can itself worsen the muscle weakness.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The thymus drives the disease: thymic hyperplasia and thymoma generate the autoreactive response against acetylcholine receptors, which is why thymectomy improves outcomes in myasthenia gravis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can inflame the heart: autoimmune myocarditis occurs especially with thymoma and anti-striational antibodies, causing arrhythmia and heart failure that complicate the disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its thymoma brings skin autoimmunity: thymoma-associated myasthenia can accompany paraneoplastic pemphigus and other cutaneous autoimmune disease, reflecting the syndrome's broad autoreactivity.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment, not the disease, reaches the kidney: long-term calcineurin-inhibitor immunosuppression for myasthenia is nephrotoxic, and a thymoma can rarely associate with membranous nephropathy.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — Some common drugs worsen it: beta-blockers, like aminoglycosides and intravenous magnesium, can impair neuromuscular transmission and unmask or aggravate myasthenia gravis.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Infection can tip it into crisis: a respiratory infection such as pneumococcal pneumonia is a frequent trigger of life-threatening myasthenic crisis, and vaccination is advised before immunosuppression.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — The mainstay of immunosuppression: corticosteroids are first-line for moderate-to-severe myasthenia gravis, though high starting doses can transiently worsen weakness before the disease improves.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Cancer immunotherapy can trigger it: PD-1 and CTLA-4 checkpoint inhibitors cause a severe immune-related myasthenia gravis, often overlapping with myositis and myocarditis, that can be life-threatening.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — It runs with other autoimmunity: myasthenia gravis clusters with autoimmune thyroid disease, type 1 diabetes and other organ-specific autoimmune conditions, reflecting a shared loss of self-tolerance.

[^gilhus-2016-mg-review]: Gilhus NE. Myasthenia Gravis. *N Engl J Med.* 2016;375(26):2570-2581. [doi:10.1056/NEJMra1602678](https://doi.org/10.1056/NEJMra1602678) · [PubMed 28029925](https://pubmed.ncbi.nlm.nih.gov/28029925/)
[^howard-2021-efgartigimod-adapt]: Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT). *Lancet Neurol.* 2021;20(7):526-536. [doi:10.1016/S1474-4422(21)00159-9](https://doi.org/10.1016/S1474-4422(21)00159-9) · [PubMed 34146511](https://pubmed.ncbi.nlm.nih.gov/34146511/)
[^howard-2017-eculizumab-regain]: Howard JF Jr, Utsugisawa K, Benatar M, et al. Safety and efficacy of eculizumab in anti-acetylcholine receptor antibody-positive refractory generalised myasthenia gravis (REGAIN). *Lancet Neurol.* 2017;16(12):976-986. [doi:10.1016/S1474-4422(17)30369-1](https://doi.org/10.1016/S1474-4422(17)30369-1) · [PubMed 29066163](https://pubmed.ncbi.nlm.nih.gov/29066163/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
