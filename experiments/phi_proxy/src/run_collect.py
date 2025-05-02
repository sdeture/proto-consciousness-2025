# === experiments/phi_proxy/src/run_collect.py ===
#!/usr/bin/env python3
import torch, transformers, argparse, numpy as np
from tsquared import enable_plasticity, disable_plasticity

def collect(model, tok, texts, plastic):
    (enable_plasticity if plastic else disable_plasticity)(model)
    acts = []
    with torch.no_grad():
        for txt in texts:
            ids = tok(txt, return_tensors='pt').to(model.device)
            out = model(**ids, output_hidden_states=True)
            acts.append(out.hidden_states[-1][:, -1, :128].cpu())  # 128-dim slice
    return torch.cat(acts)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--texts", default="sentences.txt")
    args = p.parse_args()

    tok = transformers.AutoTokenizer.from_pretrained("meta-llama/Llama-3-8b")
    mdl = transformers.AutoModelForCausalLM.from_pretrained(
        "meta-llama/Llama-3-8b"
    ).half().cuda()

    sentences = [l.strip() for l in open(args.texts)]
    np.savez("baseline.npz", acts=collect(mdl, tok, sentences, False).numpy())
    np.savez("plastic.npz",  acts=collect(mdl, tok, sentences, True ).numpy())
