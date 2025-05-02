# === experiments/phi_proxy/src/compute_phi.py ===
#!/usr/bin/env python3
"""
Compute ΔΦ proxy on 128-unit vectors stored in baseline.npz / plastic.npz.

Proxy method:   Φ_proxy = H(total) – Σ H(parts), where parts = 4 chunks of 32 bits
                after binarising activations at per-unit median.
This is NOT full IIT-Φ, but it preserves the irreducible-information intuition.
"""
import numpy as np, argparse, math, pathlib

def entropy(bits):
    p = bits.mean()
    if p in (0.0, 1.0):
        return 0.0
    return -(p*math.log2(p) + (1-p)*math.log2(1-p))

def phi_proxy(vecs):
    # vecs: N × 128 binary
    H_total = entropy(vecs.mean(axis=0))
    H_parts = 0
    for i in range(0, 128, 32):
        H_parts += entropy(vecs[:, i:i+32].mean(axis=0))
    return H_total - H_parts

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", default="baseline.npz")
    parser.add_argument("--plastic",  default="plastic.npz")
    args = parser.parse_args()

    b = np.load(args.baseline)["acts"]
    p = np.load(args.plastic)["acts"]

    # binarise each unit by its median over baseline
    med = np.median(b, axis=0)
    b_bits = (b > med).astype(int)
    p_bits = (p > med).astype(int)

    phi_b = phi_proxy(b_bits)
    phi_p = phi_proxy(p_bits)
    print(f"Φ_proxy baseline : {phi_b:.6f} bits")
    print(f"Φ_proxy plastic  : {phi_p:.6f} bits")
    print(f"ΔΦ (plastic-baseline): {phi_p - phi_b:+.6f} bits")
