# Φ-Proxy Experiment – WindSurf Coding Guide  
*(Measures ΔΦ in inference-time-plastic Transformers)*  

---

## 0 Why this matters (one-paragraph brief)
Inference-time plasticity (e.g., **Transformer-Squared**) rewrites a subset of weights during the forward pass, creating a causal feedback loop. Integrated-Information Theory (IIT) predicts this should raise irreducible information integration Φ. By comparing activations with plasticity **ON/OFF** we can record a proxy ΔΦ. Detecting even micro-bit gains would be the first empirical Φ>0 signal in an LLM, informing model-welfare debate.  

---

## 1 Prerequisites  

| Requirement | Details |
|-------------|---------|
| **GPU** | ≥ 8 GB VRAM. RTX‑3060‑laptop or equivalent. |
| **Python** | 3.10 recommended. |
| **Packages** | `pip install torch==2.2.2+cu118 transformers>=4.40 bitsandbytes pyphi-lite tsquared gh` |
| **Repo path** | `~/Documents/proto-consciousness-2025` (assumed below). |
| **Input text** | `experiments/phi_proxy/sentences.txt` – 64 wiki sentences (≤32 tokens each). |

---

## 2 Model options that fit 8 GB

| Model | VRAM (4‑bit) | Notes |
|-------|--------------|-------|
| **Mistral‑7B‑Instruct‑v0.2** | ~6.5 GB | Strong reasoning; 8 k ctx. |
| **Phi‑2 (2.7 B)** | ~3 GB | Good code/math accuracy for size. |
| **TinyLlama‑1.1B‑Chat** | ~2 GB | Very fast smoke‑tests. |

> **Loading 4‑bit example**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained(
        "mistralai/Mistral-7B-Instruct-v0.2",
        device_map="auto",
        load_in_4bit=True)
tok = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
```

---

## 3 Folder tree (already scaffolded)

```
experiments/phi_proxy/
  README_phi.md          # paste problem-framing & results
  sentences.txt          # 64 held‑out sentences
  data/                  # .npz tensors land here
  src/
    run_collect.py       # gather activations
    compute_phi.py       # Φ‑proxy calculation
```

---

## 4 WindSurf task chain

| Step | Mode | Command / Action |
|------|------|------------------|
| **collect_activations** | *Command* | ```cd ~/Documents/proto-consciousness-2025/experiments/phi_proxy/src && python run_collect.py --texts ../sentences.txt``` |
| **compute_phi** | *Command* | ```python compute_phi.py``` |
| **summarise** | *Supercomplete or Chat* | Append a **Results** section to `../README_phi.md` with baseline Φ, plastic Φ, ΔΦ and one-sentence interpretation. |

*Tips*: use Cascade to isolate steps; pin `README_phi.md` as context; store absolute repo path as a Memory to avoid “path not found”.

---

## 5 Troubleshooting quick hits

| Symptom | Fix |
|---------|-----|
| **CUDA OOM** | Add `load_in_4bit=True`, reduce batch size to 8 sentences. |
| **`Module tsquared not found`** | `pip install tsquared` (Sakana AI). |
| **Φ = NaN** | Ensure median binarisation uses **baseline** activations only. |
| **No GPU** | Run on RunPod A10 24 GB; PyTorch 2.1 + CUDA 11.8 image. |

---

## 6 RunPod (optional)

1. Spin up **Single GPU | A10 24 GB** (~$0.25/hr).  
2. `git clone` repo ➜ `pip install ...` (same requirements).  
3. Execute the task chain; outputs sync via Git.

---

> **Save this file** at the repo root as `CODING_GUIDE_WINDSURF.md`.  
> WindSurf can now read one document and execute the whole experiment end‑to‑end.
