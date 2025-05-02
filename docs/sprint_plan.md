# 4‑Week Sprint Plan – Proto‑Consciousness Agenda

| Week | Objectives (O) | Key Results (KR) | Leads / Help‑Wanted Labels |
|------|----------------|------------------|---------------------------|
| **1 – Bootstrap** | **O1.1** Land working Φ‑proxy pipeline on laptop‑class GPU.<br>**O1.2** Publish onboarding docs & starter issues. | • `run_collect.py` + `compute_phi.py` run on Mistral‑7B‑4bit.<br>• `CODING_GUIDE_WINDSURF.md` merged & CI badge green.<br>• 5 issues tagged `good first issue`. | Skylar (PO) — help: `documentation`, `setup` |
| **2 – Model Sweep** | **O2.1** Measure ΔΦ for Mistral‑7B, Phi‑2, Llama‑3‑8B‑4bit.<br>**O2.2** Stand up MeCo baseline on GPT‑4. | • Table in `README_phi.md` with ΔΦ ±95 % CI.<br>• `meco_runner.py` logs self‑prediction accuracy. | Lead: volunteer `phi-sweep` — help: `hf-loading` |
| **3 – Self‑Prediction Study** | **O3.1** Integrate MeCo tool‑gating; rerun SAD benchmark.<br>**O3.2** Draft 400‑word methods section. | • CSV with +4 pp accuracy over baseline.<br>• `README_meco.md` + diagram merged. | Lead: volunteer `meco-lead` — help: `analysis` |
| **4 – Embodiment Loop** | **O4.1** Create MuJoCo wrapper; run closed loop.<br>**O4.2** Compute Φ in embodied run.<br>**O4.3** Publish Substack write‑up & GitHub release v0.1. | • `embodiment_runner.py` demo GIF.<br>• Φ result appended to summary table.<br>• Substack post scheduled; release notes drafted. | Skylar + Manus — help: `mujoco`, `video` |

**Definition of Done:** green CI, README tables populated, Substack post summarising ΔΦ across all conditions.
