# Contributing to **proto-consciousness-2025**

Thank you for considering a contribution! This project explores whether inference‑time plasticity bumps Φ in LLMs. We value **clear code, reproducible results, and a welcoming culture**.

---

## ✨ Quick start checklist

1. **Fork** the repo & clone your fork.  
2. `python -m venv .venv && source .venv/bin/activate`  
3. `pip install -r requirements.txt` (GPU ≥ 8 GB; see guide).  
4. Pick a **good‑first‑issue** or open a discussion before big changes.  
5. Create a feature branch, commit small & descriptive, open a PR.

---

## 🗂️ Repository structure

| Path | Purpose |
|------|---------|
| `experiments/phi_proxy/` | ΔΦ pipeline (code, data, README). |
| `experiments/self_prediction/` | MeCo tool‑gating study (TBD). |
| `experiments/embodiment/` | MuJoCo closed‑loop test (TBD). |
| `docs/` | Diagrams, papers, blog drafts. |

---

## 🛠️ Setup details

| Requirement | Version / Notes |
|-------------|-----------------|
| **Python** | 3.10 |
| **PyTorch** | 2.2.2 + CUDA 11.8 |
| **Transformers** | ≥ 4.40 |
| **Windsurf** (optional) | see tutorial link in guide |
| **GPU VRAM** | ≥ 8 GB (Mistral‑7B‑4bit fits) |

---

## 🤝 Etiquette & review style

* Open an issue first for core‑logic changes.  
* PRs ≤ 400 LOC.  
* Commit messages in present‑tense imperative.  
* Be kind; mark nit‑picks with ✨`nit`.  

---

## 🏷️ Good first issues workflow

1. Comment **/claim**.  
2. Outline plan in issue.  
3. PR within 7 days.

Labels: `good first issue`, `documentation`, `phi-sweep`.

---

## 🌀 Windsurf tips

* Pin `README_phi.md` for context.  
* Use Cascade: collect → compute → summarise.  
* Store repo path as Memory.

---

## 📜 Code style

* `ruff check .` for lint.  
* `black .` for formatting.  
* Google‑style docstrings.

---

## 🔒 License & conduct

Apache‑2.0; see `CODE_OF_CONDUCT.md`.

---

## 🏆 Recognition

Meaningful PR = co‑author on the pre‑print. Minor fixes get shout‑outs.

Happy hacking!
