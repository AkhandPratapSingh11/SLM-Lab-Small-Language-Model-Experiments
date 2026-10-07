# 🔬 Module 12 — LoRA & QLoRA Deep Dive Masterclass

> **Parameter-Efficient Fine-Tuning (PEFT) Under the Microscope** — mathematical derivations, matrix rank dynamics, and state-of-the-art adaptation variants (LoRA, QLoRA, DoRA, rsLoRA, PiSSA).

---

## 🎯 Objectives & Scope
- **Mathematical Foundations:**
  - Low-rank decomposition math: $W = W_0 + \frac{\alpha}{r} (B \cdot A)$.
  - Rank ($r$), Alpha ($\alpha$), scaling factor, and target module selection.
- **Advanced LoRA Variants:**
  - **QLoRA:** 4-bit NormalFloat (NF4) quantization + double quantization + paged optimizers.
  - **DoRA (Weight-Decomposed LoRA):** Decoupling magnitude and directional updates for full-FT parity.
  - **rsLoRA (Rank-Stabilized LoRA):** Scaling factor $\frac{\alpha}{\sqrt{r}}$ for high-rank stability.
  - **PiSSA (Principal Singular values and Singular vectors Adaptation):** SVD-based parameter initialization.
  - **LongLoRA:** Shifted sparse attention for context extension.

