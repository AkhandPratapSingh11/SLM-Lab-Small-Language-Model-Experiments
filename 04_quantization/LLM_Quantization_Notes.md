# 📦 LLM Model Quantization — Complete Structured Notes
### Source: LLM Finetuning 09 + 12 (Model Quantization Course)

---

# TABLE OF CONTENTS

1. What is Quantization?
2. Why Do We Use Quantization?
3. RAM vs VRAM vs CPU vs GPU
4. Data Types & Memory Consumption
5. Precision in Deep Learning
6. Quantization Formula — Math
   - 6.1 Symmetric Quantization
   - 6.2 Asymmetric Quantization
   - 6.3 Per-Tensor Quantization
   - 6.4 Per-Channel Quantization
7. Quantization Error & Calibration
8. Types of Quantization
   - 8.1 PTQ — Post-Training Quantization
     - 8.1.1 Static PTQ
     - 8.1.2 Dynamic PTQ
   - 8.2 QAT — Quantization-Aware Training
9. Advanced LLM Quantization Ecosystem — Glossary
10. GPTQ — Gradient Post-Training Quantization
    - 10.1 GPTQ vs Standard PTQ
    - 10.2 GPTQ Mathematics (Hessian-based)
    - 10.3 GPTQ Tools
11. AWQ — Activation-aware Weight Quantization
    - 11.1 AWQ Mathematics
    - 11.2 GPTQ vs AWQ Comparison
12. QAT on LLMs (Advanced)
13. GGML — Georgi Gerganov's Machine Learning
14. GGUF — Gerganov's General Unified Format
15. Complete Quantization Workflow (End-to-End)
16. Tool Ecosystem Summary Table
17. Decision Guide — When to Use What

---

# 1. What is Quantization?

**Definition:**
> Quantization is the process of converting model weights and biases from **high-precision numbers** (like float32) to **lower-precision numbers** (like int8 or float16).

OR more simply:
> Quantization is the art of **shrinking models** by converting high-precision numbers (weights and biases) into smaller ones, while trying to **keep their intelligence intact**.

## What Do We Quantize?

| Model Type | Quantizable Weights |
|---|---|
| ANN | Weights between hidden layers |
| CNN | Convolution filters |
| RNN / LSTM | Recurrent weight matrices (hidden state transitions) |
| Transformer / LLM | Q, K, V matrices + Feed-Forward Network (FFN) weights |

**Additional Notes:**
- Biases can also be quantized (optional)
- Activations are also quantized during inference (for speed) or during training (in QAT)
- **Attention layers in LLMs are tricky** — especially softmax, which is precision-sensitive

## Simple Analogy

```
Storing prices of products:
  Full detail:    Rs.1299.956  →  float16 (high precision)
  After rounding: Rs.1300      →  int8 style (lower precision)
  Loss: 1300 - 1299.956 = 0.044  (tiny — core info preserved)
```

---

# 2. Why Do We Use Quantization?

| Goal | How Quantization Helps |
|---|---|
| Shrink Model Size | Convert GB models into MB |
| Save RAM/VRAM | Load large models on small GPUs |
| Faster Inference | Smaller integers → faster matrix ops |
| Edge Deployment | Enables mobile/IoT/edge inference |
| Lower Serving Cost | Less VRAM = cheaper GPU serving |

## Memory Savings — 100M Parameter Model

| Data Type | Memory Required |
|---|---|
| float32 | 100M × 4B = 400 MB |
| float16 | 100M × 2B = 200 MB |
| int8 | 100M × 1B = 100 MB |
| int4 | 100M × 0.5B = 50 MB |

```
A 1GB model in FP32 → becomes ~250MB in INT8
FP32 weights = 4 bytes/param → INT8 = 1 byte/param → 4x smaller
```

## Other Key Benefits
- **Load LLaMA 7B on 6GB GPU** — possible with quantization
- **Edge devices** (phones, IoT) — face detection, offline voice assistants
- **Accelerator optimization** — TPUs, NVIDIA Tensor Cores, Intel AVX512 are hardware-optimized for INT8/INT4
- **Reduce cloud costs** — smaller storage, bandwidth, compute

## Engineer's Rule of Thumb
```
FP32      → Full training (highest precision)
FP16/BF16 → Mixed precision training
INT8/INT4 → Inference (fastest, smallest)
```

---

# 3. RAM vs VRAM vs CPU vs GPU

| Component | Description |
|---|---|
| **RAM** | Main memory — stores OS, programs, CPU-based models |
| **CPU** | Brain of computer — general-purpose instruction execution |
| **VRAM** | GPU-dedicated memory — model weights, activations, gradients |
| **GPU** | Parallel processor — optimized for matrix/tensor operations |

## Comparison Table

| Feature | RAM | VRAM |
|---|---|---|
| Used by | CPU | GPU |
| Speed | Slower | Extremely fast (tensor-optimized) |
| Application | Web, apps, CPU training | Deep learning inference/training |
| Capacity | 8–64 GB typical | 2–48 GB (depends on GPU) |
| Model hosted? | On CPU | On GPU |
| Quantization helps? | Yes (smaller RAM needed) | Yes (smaller VRAM needed) |

**Key Rules:**
- Model on CPU → RAM used
- Model on GPU (LLaMA etc.) → VRAM used
- VRAM full → model crashes (OOM = Out of Memory)

---

# 4. Data Types & Memory Consumption

```
8 bits = 1 byte
float32 = 32 bits = 4 bytes per number
```

## Complete Data Types Reference

| Data Type | Meaning | Size | Precision | Example Value | Usage in DL |
|---|---|---|---|---|---|
| **float64** | 64-bit float | 8 bytes | Very High | 3.14159265358979 (~15-16 digits) | Scientific computing |
| **float32** | 32-bit float | 4 bytes | High | 3.14159265 (~7 digits) | Training & baseline |
| **float16** | 16-bit float | 2 bytes | Medium | 3.14 (~3-4 digits) | Mixed precision (AMP) |
| **bfloat16** | Brain float 16 | 2 bytes | Medium | 3.14 (less mantissa) | Training on TPUs |
| **fp8** | 8-bit float (E4M3/E5M2) | 1 byte | Low-Medium | ~2.75 (~2-3 digits) | NVIDIA Hopper GPUs |
| **nf4** | NormalFloat 4 (log-based) | 0.5 bytes | Very Low | 0.5, 1.0, 2.0 (coarse) | bitsandbytes, GPTQ/AWQ |
| **int8** | 8-bit integer | 1 byte | Low | -128 to +127 (no decimal) | Quantized inference |
| **int4** | 4-bit integer | 0.5 bytes | Very Low | -8 to +7 (coarse) | GPTQ, AWQ, extreme quant |
| **int32** | 32-bit integer | 4 bytes | Exact | 123456 | Indexing, padding, ops |
| **bool** | Boolean | 1 bit | None | True/False | Attention masks |

**FP8 Variants:**
- E4M3 → 4-bit exponent, 3-bit mantissa (NVIDIA Hopper)
- E5M2 → 5-bit exponent, 2-bit mantissa

---

# 5. Precision in Deep Learning

**Definition:**
> "How exact, detailed, and accurate a number can be stored"

```
Value          Precision Level
3.14159265     High precision (float32)
3.14           Low precision (float16)
3              Lowest precision (INT8)

Rs.87.5793     High precision (float32-like)
Rs.87.57       Medium precision (float16-like)
Rs.87          Low precision (int8/int4-like)
```

## CRITICAL: Precision ≠ Accuracy

| Term | Meaning | Related to |
|---|---|---|
| **Precision** | How finely a number is stored | Data format (float32, int8) |
| **Accuracy** | How close prediction is to true value | Model performance |

**Dart Board Analogy:**
```
Precision = How tight your dart group is (clustered close together)
Accuracy  = How close they are to the bullseye

High precision, low accuracy  = all darts tightly grouped but FAR from target
Low precision, high accuracy  = darts scattered but AVERAGE hits center
```

**KEY POINT:**
> A model CAN be low precision but still HIGH accuracy!
> - Quantize float32 → int8 (precision drops)
> - But model still gives correct output (accuracy maintained)
> - Low precision ≠ Low accuracy

## Precision Comparison

| Format | Bit Width | Precision Level | Memory | Speed | Numerical Accuracy |
|---|---|---|---|---|---|
| FP32 | 32-bit | High (~7 decimal digits) | High | Slow | Best |
| FP16 | 16-bit | Medium (~3-4 decimal digits) | Medium | Faster | Slight drop |
| INT8 | 8-bit | Low (no decimals, -128 to +127) | Low | Fastest | Small loss |
| INT4/NF4 | 4-bit | Very Low (coarse) | Very Low | Ultra-Fast | Moderate loss |
| FP8 | 8-bit | Low-Medium (~2-3 digits) | Low | Fast | Slight drop |

---

# 6. Quantization Formula — Math

**Goal:** Store float32 numbers (-128 to +127 or 0 to 255) using small integers with minimal information loss.

**Three math components:**
1. Scale & Zero-point
2. Clipping and rounding
3. Range mapping

## 6.1 Symmetric Quantization

**Definition:**
- `zero_point = 0`
- Data centered around 0
- Assumes range like [-X, +X]
- Quantization range: **[-128, +127]** (INT8)

**When to use:** Weights between [-2.0, +2.0] — equal spread of positive and negative.

### Step-by-Step Worked Example (Symmetric INT8)

```
Given:
  Float value x = 1.23
  Quant range   = INT8 = [-128, +127]
  Tensor Min/Max = [-2.0, +2.0]

Step 1: Calculate scale
  scale = (rmax - rmin) / (qmax - qmin)
  scale = (2.0 - (-2.0)) / (127 - (-128))
  scale = 4.0 / 255
  scale ≈ 0.01569

Step 2: Zero point
  zero_point = 0  (symmetric → no shift needed)

Step 3: Quantize
  q = round(x / scale) + zero_point
  q = round(1.23 / 0.01569) + 0
  q = round(78.4) = 78
  ✅ 78 = quantized integer representation of 1.23

Step 4: Dequantize
  x' = (q - zero_point) × scale
  x' = (78 - 0) × 0.01569
  x' ≈ 1.229  ← very close to original 1.23
```

## 6.2 Asymmetric Quantization

**Definition:**
- `zero_point ≠ 0` (non-zero shift)
- Used when data NOT centered around 0 (e.g., only positive: [0.5, 2.5])
- Quantization range: **[0, 255]** (uint8)

**When to use:** Weights only positive (ReLU outputs, embeddings with non-zero bias).

### Tensor Range Decision Table

| Tensor Range | Quant Range | Quant Type | Zero Point |
|---|---|---|---|
| [-2.0, +2.0] | [-128, 127] | Symmetric | 0 |
| [0.5, 2.5] | [0, 255] | Asymmetric | Non-zero |
| [-3.5, 8.2] | [0, 255] | Asymmetric | Non-zero |

### Step-by-Step Worked Example (Asymmetric)

```
Given:
  Float value x = 1.23
  Quant range   = uint8 = [0, 255]
  Tensor Min/Max = [0.5, 2.5]

Step 1: Calculate scale
  scale = (rmax - rmin) / (qmax - qmin)
  scale = (2.5 - 0.5) / (255 - 0)
  scale = 2.0 / 255 ≈ 0.00784

Step 2: Calculate zero_point
  zero_point = round(-rmin / scale + qmin)
  zero_point = round(-0.5 / 0.00784 + 0)
  zero_point = round(-63.7) → clip to 0 (uint8 min is 0)

Step 3: Quantize x = 1.23
  q = round(x / scale) + zero_point
  q = round(1.23 / 0.00784) + 0 = 157

Step 4: Dequantize
  x' = (q - zero_point) × scale
  x' = (157 - 0) × 0.00784 ≈ 1.23 ✅
```

## Why INT8 (Not UINT8) in Practice?

Despite asymmetric concept, most use **signed INT8** because:
1. **Hardware support:** Intel AVX2/AVX-512, NVIDIA TensorRT, ARM/Qualcomm — all optimized for signed INT8
2. **Framework defaults:** `torch.quantization`, `onnxruntime`, `transformers` — all default to symmetric INT8
3. **Model weights reality:** Q/K/V and FFN weights mostly centered around 0 → symmetric INT8 works great
4. Even in asymmetric mode, frameworks use INT8 with non-zero zero_point (not uint8)

## 6.3 Per-Tensor Quantization

**Definition:** Entire tensor (full weight matrix) shares **a single scale and zero-point**.

```python
W = [
    [0.1, 0.2, 0.3],    # Channel 1 — small range
    [1.5, 2.0, 1.8],    # Channel 2 — medium range
    [0.05, 0.07, 0.08], # Channel 3 — tiny range
    [3.0, 2.5, 3.2]     # Channel 4 — large range
]
# Per-tensor: 1 scale + 1 zero-point for ALL values
# Same formula applies to every element regardless of channel
```

**Use case:** Activations. Simpler, faster. Less accurate if channels have very different ranges.

## 6.4 Per-Channel Quantization

**Definition:** Each channel (row) gets its **own scale and zero-point**.

```python
W = [
    [0.1, 0.2, 0.3],     # Channel 1 → small range → scale1, zp1
    [1.5, 2.0, 1.8],     # Channel 2 → medium range → scale2, zp2
    [0.05, 0.07, 0.08],  # Channel 3 → tiny range → scale3, zp3
    [3.0, 2.5, 3.2]      # Channel 4 → large range → scale4, zp4
]
# Per-channel: 4 scales + 4 zero-points (one per row)
# Fine-tuned → less accuracy loss
```

## Per-Tensor vs Per-Channel Comparison

| Feature | Per-Tensor | Per-Channel |
|---|---|---|
| Granularity | Single scale/zero-point | One per channel |
| Speed | Faster (simpler) | Slightly slower |
| Accuracy | Lower | Higher |
| Use Case | Activations | Weights in LLMs/CNNs |
| Preferred for | Small models, quick inference | High accuracy, transformers |

## In Practice

```
LLMs:
  → Symmetric + Per-Channel for weights (efficient & accurate)

CNNs / activations:
  → Asymmetric + Per-Tensor for dynamic range handling

Transformers (LLaMA, BERT):
  → Q/K/V and FFN weights: symmetric + per-channel (row-wise)
```

---

# 7. Quantization Error & Calibration

## Quantization Error

**Definition:**
> The small difference between the original float value and the value after quantize → dequantize.

**Why it happens:** High-precision float (e.g., 3.14159265) → low-precision integer (INT8 has only 256 possible values).

```
Original:                  x  = 1.23
After quantize+dequantize: x' = 1.21
Quantization Error = |x - x'| = 0.02
```

**Implication:**
- Too much error → model accuracy drops
- LLMs especially sensitive → must quantize carefully

## Calibration

**Definition:**
> The process of analyzing real data to find accurate min/max values of tensors for quantization.

**Used in:** Post-Training Quantization (PTQ).

**Process:**
1. Pass a few batches of real data (forward pass only — no training)
2. Collect activation ranges (min/max) per layer
3. Use these to compute accurate scale & zero-point

**Why it matters:**
- Without calibration → wrong min/max → overflow/clipping → garbage output!
- Typical size: **50–200 representative samples** is sufficient

```python
# PyTorch Calibration Example
model.eval()
model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
torch.quantization.prepare(model, inplace=True)

# Calibration step — just forward pass, no weight updates:
for batch in calibration_data:
    model(batch)

torch.quantization.convert(model, inplace=True)
```

---

# 8. Types of Quantization

```
Quantization
├── PTQ (Post-Training Quantization)     ← No retraining
│   ├── Static PTQ  (Activations + Weights — needs calibration)
│   └── Dynamic PTQ (Weights only, on-the-fly activation)
└── QAT (Quantization-Aware Training)   ← Retraining required
```

## Cricket Analogy

```
PTQ: "Train with perfect bat, play with cheap bat later"
  → Train in float32, switch to INT8 at inference
  → Model never practiced this!

QAT: "Train and play with the same cheap bat"
  → Model trains with INT8 simulation from day 1
  → Learns to handle its limitations
  → More consistent performance
```

## 8.1 PTQ — Post-Training Quantization

Model already trained in FP32. Apply quantization afterward. **No retraining.**

**What gets quantized:**
- Weights ✅
- Biases ✅ (usually)
- Activations → depends on Static vs Dynamic

### 8.1.1 Static PTQ

> Both **weights AND activations** are quantized using a calibration dataset.

**Process:**
1. Train model in float32
2. Provide calibration data (few batches)
3. Compute min/max of weights & activations
4. Quantize both statically (before inference)

**Analogy:** You test every camera setting before a shoot, lock all values — ready.

**Pros:** Very optimized (speed + memory). Works well on mobile (qnnpack) & edge (fbgemm).

**Cons:** Needs calibration data. Slight risk of poor accuracy if calibration is bad.

### 8.1.2 Dynamic PTQ

> **Only weights** quantized. Activations quantized **on-the-fly** at runtime.

**Process:**
- Weights stored as INT8 (pre-quantized)
- Activations remain FP32, converted dynamically during inference
- No calibration needed

**Analogy:** Camera in auto-mode. Adjusts lighting dynamically.

**Pros:** No calibration. Easy to apply to pre-trained models (especially LLMs).

**Cons:** Slightly less optimized. Works best for fully connected layers, not CNNs.

### Static vs Dynamic Summary

| Feature | Dynamic Quantization | Static Quantization |
|---|---|---|
| Weights | INT8 (pre-quantized) | INT8 (pre-quantized) |
| Activations | Quantized on-the-fly | Quantized beforehand (calibration) |
| Calibration | Not needed | Needed |
| Accuracy | Moderate | Better |
| Speed | Fast | Faster (usually) |

### What Gets Quantized — Complete Table

| Type | Weights | Bias | Activations | Calibration | Training |
|---|---|---|---|---|---|
| PTQ (Static) | Yes | Yes | Yes | Yes | No |
| PTQ (Dynamic) | Yes | Yes | At runtime | No | No |
| QAT | Yes | Yes | Yes | No | Yes (full) |

## 8.2 QAT — Quantization-Aware Training

> Model **trained with quantization simulation** so it learns to handle low-precision.

**Summary:**
```
Insert fake quant/dequant ops during training
→ Backprop uses float32 but forward uses simulated INT8
→ After training, convert to real INT8 model
```

### Inside QAT

**Forward Pass:**
- Quantization simulated (rounded to INT8)
- Model **learns to handle quantization error**

**Backward Pass:**
- Backpropagation on actual FP32 weights
- Gradient computed w.r.t. quantized values
- Technique called **Straight-Through Estimator (STE)**

**Analogy:** Train a cricketer with a plastic bat from Day 1 — masters it in real matches.

**Pros:** Best accuracy. Model learns to handle quantization errors.

**Cons:** Slower (requires retraining). More complex to set up.

### QAT Steps

```
1. Choose what to quantize (Linear layers in Attention + MLP)
2. Insert fake quantization (prepare_qat)
3. Train or fine-tune with representative data
4. Convert to real INT8 model (convert)
5. Evaluate, skip sensitive layers if needed
```

**Skip these (keep in FP32):**
- Embeddings (usually)
- LayerNorms
- Final `lm_head`

**Quantize these:**
- `q_proj, k_proj, v_proj, o_proj` (Attention)
- `up_proj, gate_proj, down_proj` (MLP)

## PTQ vs QAT Master Comparison

| Feature | PTQ | QAT |
|---|---|---|
| When applied | After training | During training |
| Model learning-aware? | No | Yes |
| Accuracy impact | Slight drop (1–5%) | Minimal or none |
| Use case | Fast compression | Production-grade (edge) |
| Training time | No retraining — very fast | Retraining required |
| Toolkits | torch.quantization, GPTQ, BnB | prepare_qat, AutoQAT, TensorRT-QAT |
| Complexity | Easy | More complex |
| Activation quant | Optional/estimated | Accurate (learned) |

## Decision Guide

| Scenario | Best Option |
|---|---|
| Compress model for faster inference | PTQ |
| Deploy on edge/mobile (high accuracy needed) | QAT |
| Need quick model size reduction | PTQ |
| Training from scratch or fine-tuning | QAT |
| LLM inference only | PTQ (GPTQ, AWQ) |

---

# 9. Advanced LLM Quantization Ecosystem — Glossary

| Term | Full Form | Meaning |
|---|---|---|
| **FP** | Floating Point | Generic float types |
| **INT** | Integer | INT8, INT4 used for quantization |
| **PTQ** | Post-Training Quantization | Quantize after training, no retraining |
| **QAT** | Quantization-Aware Training | Simulate quantization during training |
| **GPTQ** | Gradient Post-Training Quantization | Advanced PTQ for Transformers using Hessian |
| **AWQ** | Activation-aware Weight Quantization | PTQ that considers activation distribution |
| **GGML** | Georgi Gerganov's Machine Learning | C-based tensor library / inference runtime |
| **GGUF** | Gerganov's General Unified Format | Successor binary format to GGML for LLMs |
| **llama.cpp** | — | C++ project using GGML/GGUF for local LLM inference |
| **AutoGPTQ** | — | HuggingFace wrapper for GPTQ |
| **bitsandbytes** | — | HF-compatible library for INT8/4-bit loading |

> **Common Myths (Corrected):**
> - GPTQ ≠ "Generative Pretrained Transformer Quantization" → it's **Gradient PTQ**
> - GGUF ≠ "GPT-Generated Unified Format" → that's a backronym, unofficial
> - GGML ≠ "GPT-Generated Model Language" → it's Georgi Gerganov's library

## One-Line Summary

```
PTQ, QAT        = Quantization TECHNIQUES (how it's done)
GPTQ, AWQ       = Quantization ALGORITHMS (which method for LLMs)
GGUF            = Model FILE FORMAT (where quantized model is stored)
GGML / llama.cpp = INFERENCE RUNTIME (how to run quantized model)
```

---

# 10. GPTQ — Gradient Post-Training Quantization

**Definition:**
> GPTQ is an advanced PTQ method for LLMs (LLaMA, GPT, Mistral, Falcon).
> Quantizes weights to **INT4** after training, **without fine-tuning**, preserving accuracy.

## Key Characteristics

- Advanced PTQ using **second-order (Hessian) optimization**
- For **Transformer-based LLMs** specifically
- Targets **INT4/INT8** compression
- Does **NOT** require retraining

## Core Idea: Matrix Approximation

```
Replace original weight matrix W with quantized Ŵ (W-hat)

Objective: min ||WX - ŴX||²
           (minimize OUTPUT difference, not weight difference)

Where:
  W = Original weight matrix
  Ŵ = Quantized weight matrix
  X = Input activations
```

## GPTQ Behavior Summary

| Concept | GPTQ Behavior |
|---|---|
| Type | Post-Training Quantization — no retraining |
| Precision | Typically INT4 (also INT3, INT2 for extreme) |
| Target | Linear layers: Q/K/V, FFN |
| Core Idea | Layer-by-layer second-order optimization |
| Accuracy | High — close to original FP16 model |
| Speed | Much faster than QAT |
| Calibration | 50–200 representative text samples required |

## 10.1 GPTQ vs Standard PTQ

| Approach | Method | Focuses on |
|---|---|---|
| Standard PTQ | min/max scaling | Minimize weight difference |
| GPTQ | Hessian-based optimization | Minimize OUTPUT difference |

```
Standard PTQ analogy:
  Blindly shrink all clothes to medium size

GPTQ analogy:
  Check body shape, try each shirt, adjust next based on previous fit
  Smart and adaptive!
```

**GPTQ is smarter because it:**
1. Tracks error at output level, not just weight level
2. Uses second-order information (Hessian) to find weight sensitivity
3. Selectively quantizes to minimize final output error

## 10.2 GPTQ Mathematics (Hessian-based)

### Step 1: Layer Representation

```
Input: X [b × n]   →   Weight: W.T [n × d]   =   Output: Y [b × d]
(b = batch size, n = input features, d = output features)
```

### Step 2: Quantization Goal

```
min ||WX - ŴX||²
(minimize output error, not weight error)
```

### Step 3: Hessian Matrix

```
H = Xᵀ × X

This is a covariance matrix of inputs.
It tells us which directions in W are more sensitive to changes.

H[i,i] (diagonal) = sensitivity of output to weight i
  Large H[i,i] → weight is sensitive → quantize carefully
  Small H[i,i] → weight is less sensitive → can quantize aggressively
```

**Flow:**
```
Real Input (X) → Compute Hessian (XᵀX) → Sensitivity per Row → Safer Quantization
```

### Step 4: Blockwise Greedy Quantization

| Step | What GPTQ Does |
|---|---|
| 1 | Takes one row of weights |
| 2 | Computes output using real calibration input |
| 3 | Tries all possible 4-bit values for each weight |
| 4 | Measures which rounding causes least error |
| 5 | Picks smart quantized value |
| 6 | Compensates in next rows for any introduced error |

**Error impact formula:**
```
error_impact(w_i) = (w_i - ŵ_i)² × H[i,i]
→ Choose ŵ_i that minimizes this
```

### Step 5: Error Compensation

```
Similar to Low-Rank Approximation.
Later rows compensate for errors introduced by earlier ones.
```

### Worked Example

```
Suppose: d=2 features, n=1 output neuron, b=3 examples

Original weight W quantized to Ŵ
→ Error large when H[i,i] is large
→ GPTQ avoids that quantized value

So: GPTQ won't pick ŵ_i = -0.5 if H[i,i] is large
    (that weight is sensitive → big impact on output)
```

## GPTQ Output Formats

| Format | Description |
|---|---|
| `.safetensors` | HuggingFace ecosystem (AutoGPTQ) |
| `.gguf` | For llama.cpp (CPU/Mac inference) |
| `.pt` / custom | PyTorch checkpoint |

## 10.3 GPTQ Tools

| Tool | Description |
|---|---|
| **AutoGPTQ** | HF-compatible high-level wrapper — easy API |
| **GPTQ-for-LLaMA** | Original low-level repo by Yao Fu et al. |
| **ExLlama / ExLlamaV2** | Fast CUDA inference for GPTQ models |
| **llama.cpp** | GGUF/GPTQ on CPU and Mac (Metal backend) |
| **HF Transformers + bitsandbytes** | For QLoRA / 4-bit loading workflows |

---

# 11. AWQ — Activation-aware Weight Quantization

**Definition:**
> AWQ is a PTQ method like GPTQ, but improves accuracy by considering **activation distribution** during quantization.

## Core Intuition

Instead of blindly quantizing weights, AWQ:
1. Checks how each weight affects the output **after activation functions** (GELU, ReLU)
2. Prunes and rescales weights to cause **minimum distortion** — especially on important tokens

## 11.1 AWQ Mathematics — 4 Steps

### Step 1: Calibration
- Pass 50–200 real text prompts through model
- Collect activation values X from these prompts

### Step 2: Token Importance Estimation
- Calculate **per-token activation scores**
- Identify **"important tokens"** — whose quantization must be handled carefully

### Step 3: Weight Rescaling & Pruning
```
Weight matrix W adjusted based on token importance
Weights rescaled + non-important rows/columns pruned before quantization
Done blockwise (typically 128-row blocks)
```

### Step 4: INT4 Quantization
```
Once rescaled:
  scale = (max - min) / (qmax - qmin)
  q = round(x / scale) + zero_point
Standard INT4 formula applied to rescaled weights
```

## 11.2 GPTQ vs AWQ Comparison

| Feature | GPTQ | AWQ |
|---|---|---|
| Error Modeling | Weight-only error | Weight + Activation error |
| Uses Hessian | Yes | No (simpler & faster) |
| Calibration Needed | Yes (50–200 samples) | Yes (same) |
| Precision | INT4 (mainly) | INT4 (mainly) |
| Speed | Fast | Even faster (no second-order calc) |
| Accuracy | High | Very High (better in some LLMs) |
| Quant Target | Weights | Weights + Activation impact |
| Use Case | LLaMA, GPT | LLaMA, Mistral, ChatGLM, etc. |

**Analogy:**
```
GPTQ = Measures how much raw ingredients changed (before cooking)
AWQ  = Measures how the final dish TASTES after cooking (post-activation)
```

---

# 12. QAT on LLMs — Advanced Details

## Why QAT is Expensive for LLMs

### 1. Model Size
```
MLPs/CNNs → few million parameters
LLMs      → billions (7B, 13B, 70B)
Fake quantization + backprop on every param = HUGE compute + memory
```

### 2. Fake Quantization Overhead
- Every forward pass applies FakeQuantize (rounding + clamping)
- Large models + long sequences → cost multiplies enormously

### 3. Backpropagation Cost
- Even with fake quant, gradients computed in FP32
- No memory savings during training
- Full VRAM footprint of original model still needed

### 4. Retraining Requirement
- PTQ = no retraining (cheap)
- QAT = must fine-tune on representative data
- Fine-tuning a 7B model = multi-GPU cluster or TPU pod

### 5. Resource Requirements
```
QAT on LLaMA-7B  → at least 4–8 A100 80GB GPUs
QAT on LLaMA-65B → dozens of GPUs (industrial scale)
Only big labs (Meta, Microsoft, OpenAI) can afford this
```

## Practical Alternatives to Full QAT

| Alternative | Description |
|---|---|
| PTQ (GPTQ, AWQ) | Just calibration data + few forward passes — cheap |
| LoRA + QAT (Partial) | Apply QAT only on adapter layers, not whole model |
| Hybrid approach | Keep embeddings in FP32, quantize Linear/Attention layers |

## MLPs vs LLMs Comparison

| Aspect | MLPs | LLMs (GPT, LLaMA) |
|---|---|---|
| PTQ | Easy (torch.quantization) | Layer-wise, calibration needed, uses GPTQ/AWQ |
| QAT | Light training needed | Heavy retraining with STE, advanced toolkits |
| Activation Handling | Simple | Complex (softmax, attention — precision-sensitive) |
| Tools | Built-in torch | GPTQ, AWQ, bitsandbytes, torchao, TensorRT-LLM |
| Hardware Need | Single GPU | Multi-GPU/TPU for QAT |

## QAT Tools for LLMs

| Tool | Description |
|---|---|
| **torchao** | PyTorch QAT backend |
| **Intel Neural Compressor** | Full QAT pipeline |
| **NVIDIA TensorRT-LLM** | QAT for production |
| **OpenVINO** | QAT & PTQ optimizations |
| **HQQ** | High-Quality Quantization + QAT |
| **SmoothQuant** | Can be combined with QAT |

---

# 13. GGML — Georgi Gerganov's Machine Learning

## What is GGML?

- **C-based tensor library** optimized for inference of quantized models on CPU and Apple Silicon
- NOT designed for training or GPU inference (by default)
- NOT "GPT-Generated Model Language" (common myth)

## Key Highlights

| Feature | Description |
|---|---|
| Language | Pure C (highly portable) |
| Focus | Efficient inference with quantized weights |
| Quantization | INT8, INT4, Q4_0, Q4_K, Q5_0, Q8_0 |
| Model Types | Decoder-only LLMs (LLaMA, Falcon) |
| Hardware | CPU (x86, ARM), Apple Silicon (Metal backend) |

## What GGML is NOT For

| Not Meant For | Reason |
|---|---|
| GPU acceleration | No CUDA/ROCm in core |
| Model training | No backward pass / autograd |
| Fine-tuning | Only forward/inference supported |

## GGML Quantization Types

| Quantization | Bit Width | Use Case |
|---|---|---|
| Q4_0 | 4-bit | Basic compression, smallest size |
| Q4_K | 4-bit | Smarter quantization (like AWQ) |
| Q5_0 | 5-bit | Balanced speed & accuracy |
| Q8_0 | 8-bit | Near-FP16 quality |
| F16/F32 | 16/32-bit | Full precision |

## GGML File Format (`.bin`)

```
[Header]  → Magic bytes: GGML, Version info
[Model Info] → Dimensions, layers, vocab size
[Tensor Blobs] → Each tensor: name, shape, data type, quantized values
```

## GGML → GGUF Migration

```bash
# GGML format is deprecated for new projects
python3 convert-llama-ggml-to-gguf.py
```

GGUF adds: tokenizer support, format standardization, metadata, newer LLaMA compatibility.

---

# 14. GGUF — Gerganov's General Unified Format

## What is GGUF?

> Standardized **binary file format** for storing and deploying quantized LLMs, primarily for llama.cpp ecosystem.

- Successor to GGML format
- Self-describing (everything in one file)
- Supported by HuggingFace + llama.cpp

## Why GGUF was Created

| Problem in GGML | GGUF Solution |
|---|---|
| Separate tokenizer & metadata files | Single self-contained file |
| No versioning | Formal versioning + backward compatibility |
| Hard to inspect | Human-readable metadata (gguf-tool) |
| No standard tokenizer info | Tokenizer, vocab, pre-tokenizer embedded |
| Limited quantization types | Native: INT4, Q8_0, Q6_K, etc. |

## GGUF File Contents

| Component | Description |
|---|---|
| model parameters | Hidden size, head count, vocab size |
| tensor weights | Quantized Q/K/V, FFN tensors |
| tokenizer config | Pre-tokenizer, vocab, tokenizer type |
| metadata | Format version, model source, notes |
| quantization type | Q4_K, Q8_0, etc. |

## GGUF File Structure

```
[Header]
  Magic Number: GGUF
  Version: v1 or v2

[Metadata]
  Model name, tokenizer info, quantization method

[Tensors]
  All quantized model weights
  Each: name, shape, data type, actual data

[Tokenizer Info]
  Tokenizer type (BPE, SentencePiece)
  Special tokens, pre-tokenizer config
```

## GGUF Quantization Types

| Type | Bits | Notes |
|---|---|---|
| Q4_0 | 4-bit | Basic 4-bit weights |
| Q4_K | 4-bit | Activation-aware 4-bit (AWQ-style) |
| Q5_0 | 5-bit | Balanced accuracy/speed |
| Q8_0 | 8-bit | Near FP16 accuracy |
| F16 | 16-bit | Half-precision |
| F32 | 32-bit | Full precision |

## Supported Models

LLaMA 1/2/3, Falcon, Mistral, BLOOM/BLOOMZ, GPT-J, GPT-NeoX, Phi-2, StarCoder

## GGUF Tooling

| Tool | Purpose |
|---|---|
| **llama.cpp** | Main runtime for .gguf models |
| **convert.py** | Convert HuggingFace → GGUF |
| **gguf-tool** | Inspect, edit, compare GGUF files |
| **text-generation-webui** | UI-based serving |
| **KoboldCpp, llamafile** | Other GGUF-compatible backends |

## Real-World GGUF Workflow

```bash
# Step 1: Quantize using AutoGPTQ or AWQ
# Step 2: Export to GGUF
python3 convert.py --model hf_model_path --outfile model.gguf
# Step 3: Run on CPU/Mac
llama.cpp --model model.gguf --prompt "Explain black holes."
```

## Pros & Limitations

**Pros:**
- Compact single file
- Easy deployment across devices
- Standardized for llama.cpp ecosystem
- Compatible with many quant formats

**Limitations:**
- Optimized mainly for decoder-only (causal) transformers
- Not natively supported by HF libraries (conversion needed)

## GGML vs GGUF Summary

| Feature | GGML (Old) | GGUF (New) |
|---|---|---|
| File extension | .bin | .gguf |
| Tokenizer | Not inside | Embedded |
| Versioning | No | Versioned & standardized |
| Quant formats | Limited | Wide (Q2_K to Q8_0) |
| Status | Legacy | Recommended |

---

# 15. Complete Quantization Workflow (End-to-End)

```
STEP 1: Quantize the model
├── PTQ  → Post-Training Quantization (standard, no retraining)
├── QAT  → Quantization-Aware Training (retraining needed, best accuracy)
├── GPTQ → Gradient-based PTQ for Transformers (INT4, fast inference)
└── AWQ  → Activation-aware Weight Quantization (better accuracy)

STEP 2: Save in a format
├── .gguf         → llama.cpp ecosystem (CPU/Mac)
├── .safetensors  → HuggingFace Transformers
├── .onnx         → ONNX Runtime
└── .engine       → TensorRT (NVIDIA-optimized)

STEP 3: Run with inference engine
├── llama.cpp       → GGUF models (CPU/Mac)
├── GGML            → older .bin format
├── vLLM            → safetensors, high-throughput GPU
└── TensorRT-LLM    → INT4/INT8 NVIDIA GPUs

COMPLETE EXAMPLE:
  1. LLaMA-3 8B model in FP16
  2. Quantize using GPTQ (type of PTQ)
  3. Export to GGUF format
  4. Run using llama.cpp on CPU — no GPU required!

  Flow: FP16 → GPTQ → .gguf → llama.cpp
```

---

# 16. Tool Ecosystem Summary Table

| Tool / Format | Category | Description |
|---|---|---|
| **GPTQ** | Quantization Library | PTQ for LLMs. HF + AutoGPTQ. Fast 4-bit GPU inference. |
| **AWQ** | Quantization Library | Activation-aware. Better accuracy than GPTQ in some LLMs. |
| **bitsandbytes** | Quantization Library | HF-compatible. INT8 (LLM.int8()) + 4-bit (nf4). Easy. |
| **GGML** | Inference Runtime | C-based. CPU/Mac optimized. Backbone for llama.cpp. |
| **llama.cpp** | Inference Runtime | C++ wrapper for GGML/GGUF. CLI + Python API. |
| **GGUF** | Model File Format | Self-contained quantized model file. llama.cpp ecosystem. |
| **TensorRT-LLM** | GPU Deployment | NVIDIA production inference. FP16/INT8/INT4. |
| **vLLM** | GPU Deployment | High-throughput serving. Paged attention. Multi-GPU. |
| **ONNX Runtime** | Cross-platform | Inference for ONNX models. CPU, GPU, TensorRT. |

## Categorized

```
Quantization Libraries:
  GPTQ (AutoGPTQ) — Fastest 4-bit (HuggingFace compatible)
  AWQ             — 4-bit with activation-aware optimization
  bitsandbytes    — INT8/4-bit quick loading for HF models

Model File Format:
  GGUF            — Efficient format for llama.cpp ecosystem

Inference Runtimes:
  GGML            — C-based lightweight inference (CPU/Mac)
  llama.cpp       — CLI + API for GGML/GGUF models

GPU/Server Deployment:
  TensorRT-LLM    — NVIDIA production inference
  vLLM            — High-throughput batched serving
  ONNX Runtime    — Cross-platform inference
```

---

# 17. Decision Guide — When to Use What

## By Goal

| Scenario | Best Method |
|---|---|
| Quick compression, minimal effort | Dynamic PTQ |
| Maximum optimization, have calibration data | Static PTQ |
| Best accuracy, can afford retraining | QAT |
| LLM inference on consumer GPU | GPTQ or AWQ |
| LLM inference on CPU/Mac | GGUF + llama.cpp |
| HuggingFace ecosystem, quick load | bitsandbytes (INT8/4-bit) |
| High-throughput server inference | vLLM |
| NVIDIA production server | TensorRT-LLM |
| Edge/mobile deployment | QAT → ONNX |

## Memory & Quality Trade-offs

```
FP32  → Best quality, most memory  (4 bytes/param)
FP16  → Very good quality, 2x savings
INT8  → Good quality, 4x savings, fast
INT4  → Acceptable quality, 8x savings, very fast
INT2  → Poor quality, 16x savings, extreme compression
```

## LLM-Specific Decision Flow

```
Have a trained LLM?
├── YES → Use PTQ (no retraining needed)
│         ├── On GPU?      → GPTQ or AWQ
│         ├── On CPU/Mac?  → GGUF + llama.cpp
│         └── Quick load?  → bitsandbytes
│
└── YES + Accuracy critical + Resources available?
          └── Use QAT (retraining)
              → torchao / TensorRT-LLM QAT / HQQ
```

---

# Key Formulas Quick Reference

```
Quantization:
  q = round(x / scale) + zero_point

Scale:
  scale = (rmax - rmin) / (qmax - qmin)

Zero Point:
  zero_point = round(-rmin / scale + qmin)

Dequantization:
  x' = (q - zero_point) × scale

Quantization Error:
  error = |x - x'|

GPTQ Hessian:
  H = Xᵀ × X

GPTQ Error Impact per Weight:
  error_impact(w_i) = (w_i - ŵ_i)² × H[i,i]
  → Pick ŵ_i that minimizes this

GPTQ Objective:
  min ||WX - ŴX||² using Hessian guidance
```

---

# Summary Mental Model

```
START: Pretrained LLM in FP32 (huge, slow, accurate)
         |
         ↓
QUANTIZE using:
  GPTQ → if GPU, need fast 4-bit
  AWQ  → if GPU, need best accuracy
  BnB  → if HF, quick INT8/4-bit load
  PTQ  → if quick, no accuracy concern
         |
         ↓
SAVE in:
  .gguf        → CPU/Mac via llama.cpp
  .safetensors → HF + vLLM
  .onnx        → cross-platform
  .engine      → TensorRT
         |
         ↓
RUN with:
  llama.cpp    → CPU/Mac (GGUF)
  vLLM         → GPU server
  TensorRT-LLM → NVIDIA production
  ONNX Runtime → cross-platform
         |
         ↓
RESULT: Smaller model, faster inference, less memory!
```

---

*Source: LLM Finetuning 09 Model Quantization Course + LLM Finetuning 12 Model Quantization Course*
*Topics: Quantization fundamentals → Advanced GPTQ/AWQ → GGML/GGUF ecosystem*
