# 🦥 Unsloth — Complete In-Depth Notes & Architectural Reference Guide
### Source: Unsloth Practical Lab & Handwritten Lecture Slides (SLM Experiment 07)

---

# TABLE OF CONTENTS

1. [What is Unsloth? — Philosophy & Core Mission](#1-what-is-unsloth)
2. [The Core Problem in Standard LLM Training](#2-the-core-problem-in-standard-llm-training)
   - 2.1 The Memory Wall & Bandwidth Bottleneck
   - 2.2 PyTorch Autograd Overhead & Activation Bloat
   - 2.3 The Inefficiency of Generic Kernel Launches
3. [Unsloth Architecture & The "Secret Sauce"](#3-unsloth-architecture--the-secret-sauce)
   - 3.1 Custom CUDA & OpenAI Triton Kernels
   - 3.2 Operator Fusion (RMSNorm, RoPE, MLP, Attention)
   - 3.3 Manual Backpropagation (Deriving Analytical Gradients)
   - 3.4 In-Kernel Cross-Entropy Loss (Bypassing Vocabulary Logit Materialization)
   - 3.5 Smart Gradient Checkpointing (Selective Recomputation)
   - 3.6 Native Sequence Packing (Neat Packing with Boundary Isolation)
   - 3.7 Exact Mathematics — Zero Accuracy Degradation Guarantee
4. [Mathematical Deep Dive: Derivations of Fused Operators](#4-mathematical-deep-dive-derivations-of-fused-operators)
   - 4.1 RMSNorm Forward & Backward Pass
   - 4.2 Rotary Positional Embeddings (RoPE) In-Place Rotation
   - 4.3 SwiGLU / GeLU Activation Fusion
   - 4.4 Low-Rank Adaptation (LoRA) Matrix Forward & Backward Pass
   - 4.5 Memory-Efficient Fused Cross-Entropy Math
5. [Software Stack & Architectural Hierarchy](#5-software-stack--architectural-hierarchy)
   - 5.1 Where Unsloth Fits Between PyTorch, Hugging Face, and TRL
   - 5.2 FastLanguageModel vs AutoModelForCausalLM
6. [The End-to-End 7-Stage Pipeline](#6-the-end-to-end-7-stage-pipeline)
   - 6.1 Stage 1: Load Base Model
   - 6.2 Stage 2: Quantization (4-bit, 8-bit, 16-bit)
   - 6.3 Stage 3: LoRA / PEFT Parameter Injection
   - 6.4 Stage 4: SFT / RL Training Execution
   - 6.5 Stage 5: Ultra-Fast Inference Acceleration
   - 6.6 Stage 6: Benchmarking & Evaluation
   - 6.7 Stage 7: Model Export & Deployment Freedom
7. [Supported Models, Architectures & Modalities](#7-supported-models-architectures--modalities)
   - 7.1 Text-to-Text Language Models (LLaMA, Qwen, Mistral, Gemma, Phi, DeepSeek)
   - 7.2 Multimodal Vision-Language Models (Qwen2-VL, LLaMA-Vision, Pixtral)
   - 7.3 Speech & Audio Models (Whisper, Orpheus)
   - 7.4 Classical Encoders (BERT, RoBERTa)
8. [Supported Fine-Tuning Paradigms](#8-supported-fine-tuning-paradigms)
   - 8.1 4-bit QLoRA (NF4 & INT8)
   - 8.2 16-bit LoRA & Full Fine-Tuning
   - 8.3 Native FP8 Training (Ada Lovelace & Hopper)
   - 8.4 Reinforcement Learning (RL) Superpowers: GRPO, DPO, PPO, KTO, ORPO
9. [Deep Dive into GRPO: DeepSeek-R1 Style Reasoning on a Single GPU](#9-deep-dive-into-grpo-deepseek-r1-style-reasoning-on-a-single-gpu)
   - 9.1 Why Traditional PPO Fails on Consumer Hardware
   - 9.2 The Mathematical Mechanics of GRPO
   - 9.3 Group Relative Advantage Estimation Without a Critic Model
   - 9.4 How Unsloth Slashes GRPO VRAM by 80%
10. [The Shock Factor: Extreme Long-Context Training](#10-the-shock-factor-extreme-long-context-training)
    - 10.1 Hardware VRAM vs Maximum Sequence Length Scaling Matrix
    - 10.2 Why Standard Hugging Face Crashes (OOM) at >4K Tokens
    - 10.3 Dynamic RoPE Scaling & Memory Compaction in Unsloth
11. [Memory Economics & Rigorous VRAM Calculation Guide](#11-memory-economics--rigorous-vram-calculation-guide)
    - 11.1 The 4 Components of GPU Memory
    - 11.2 Model Weight Memory Formulas
    - 11.3 Optimizer State Memory: FP32 vs 8-bit AdamW
    - 11.4 Activation Memory: Standard PyTorch vs Unsloth Triton Kernels
12. [Step-by-Step Code Implementation & Best Practices](#12-step-by-step-code-implementation--best-practices)
    - 12.1 Environment Setup & Diagnostics
    - 12.2 Model Initialization (`FastLanguageModel.from_pretrained`)
    - 12.3 LoRA Adapter Injection (`FastLanguageModel.get_peft_model`)
    - 12.4 Data Formatting & The Mandatory EOS Token Rule
    - 12.5 TRL `SFTTrainer` & `SFTConfig` Configuration
    - 12.6 Latency & Memory Profiling Execution
    - 12.7 Accelerated Inference (`FastLanguageModel.for_inference`)
13. [Model Export & Deployment Freedom](#13-model-export--deployment-freedom)
    - 13.1 Saving Standalone LoRA Adapters
    - 13.2 Merging into 16-bit Standalone Models (vLLM / SGLang)
    - 13.3 Native GGUF Quantization (Ollama / llama.cpp)
    - 13.4 Creating Ollama Modelfiles & Local Serving
14. [Comprehensive Benchmarks: Unsloth vs Stock Hugging Face](#14-comprehensive-benchmarks-unsloth-vs-stock-hugging-face)
15. [When to Use Unsloth vs When NOT to Use Unsloth (Decision Matrix)](#15-when-to-use-unsloth-vs-when-not-to-use-unsloth-decision-matrix)
16. [Hyperparameter Reference Dictionary (`SFTConfig`)](#16-hyperparameter-reference-dictionary-sftconfig)
17. [Common Errors, Debugging Checklist & Solutions](#17-common-errors-debugging-checklist--solutions)
18. [Quick Revision Cheat Sheet](#18-quick-revision-cheat-sheet)

---

# 1. What is Unsloth? — Philosophy & Core Mission

### The Core Vision
In the artificial intelligence ecosystem, fine-tuning large language models has traditionally been reserved for organizations with access to massive GPU clusters (e.g., 8× A100 or 8× H100 nodes). When individual developers, academic researchers, or startups attempt to fine-tune an 8B parameter model using standard open-source tools on a single consumer GPU (such as an NVIDIA RTX 3060, RTX 4090, or a free Google Colab T4 instance), they inevitably hit the **CUDA Out of Memory (OOM)** wall.

**Unsloth** was created by brothers Daniel and Michael Han to dismantle this barrier. 

> **Core Definition:**
> **Unsloth** is an ultra-optimized, open-source library that rewrites the lowest-level execution graph of Transformer models using custom **OpenAI Triton** and **CUDA** kernels. It delivers:
> - **2× to 5× faster training throughput**
> - **50% to 80% reduction in GPU VRAM consumption**
> - **Zero mathematical approximation or accuracy loss**
> - **Native export freedom** to Ollama, llama.cpp (GGUF), vLLM, and Hugging Face Hub.

Unsloth is **not** a high-level training abstraction like LLaMA Factory or Hugging Face Trainer. Instead, it is an **under-the-hood optimization engine**. It accelerates Hugging Face `transformers` and TRL (`Transformer Reinforcement Learning`) from the bottom up, making modern LLM fine-tuning accessible to anyone with a single NVIDIA GPU.

---

# 2. The Core Problem in Standard LLM Training

To appreciate why Unsloth is revolutionary, one must examine the computational inefficiencies embedded in the standard PyTorch + Hugging Face ecosystem.

```
Standard PyTorch Fine-Tuning Bottlenecks:
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Kernel Launch Latency: Hundreds of separate GPU kernels per layer   │
│ 2. Autograd Graph Bloat: Millions of intermediate activation tensors   │
│ 3. Naive Sequence Padding: Massive computation wasted on zeros (<pad>) │
│ 4. Slow Cross-Entropy: Materializes gigantic [B, S, V] logits in VRAM   │
│ 5. Memory Bandwidth Stalling: Constant round-trips to slow HBM VRAM     │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 The Memory Wall & Bandwidth Bottleneck
Modern GPUs (such as the NVIDIA A100 or RTX 4090) have enormous compute capacity (FLOPs), but their computational units are severely constrained by **memory bandwidth**. 
- GPU **SRAM (Static RAM / Shared Memory)** sits directly on the streaming multiprocessor (SM) and operates at tens of terabytes per second.
- GPU **HBM / GDDR VRAM** is relatively far away and orders of magnitude slower.

In stock PyTorch, a single Transformer decoder layer executes as dozens of independent function calls:
$$\text{RMSNorm} \longrightarrow \text{RoPE} \longrightarrow QKV \text{ Projections} \longrightarrow \text{Softmax} \longrightarrow \text{Attention Dropout} \longrightarrow \text{MLP Gate} \longrightarrow \text{SwiGLU} \longrightarrow \text{Down Proj}$$

Every single operation reads from global VRAM, executes a tiny calculation, and writes the intermediate result back to global VRAM. The GPU spends **80% of its time waiting for memory transfers** rather than computing!

### 2.2 PyTorch Autograd Overhead & Activation Bloat
PyTorch's automatic differentiation engine (`torch.autograd`) is designed for general-purpose deep learning. It functions by recording a dynamic directed acyclic graph (DAG) during the forward pass. To compute gradients via the chain rule during `.backward()`, PyTorch caches almost all intermediate tensor states.

For an 8B parameter model with a sequence length of 4,096 tokens, these cached forward activations consume **over 25 GB of VRAM alone** — far surpassing the memory required to hold the model weights themselves!

### 2.3 The Real-World Consequence
- Fine-tuning LLaMA-3.1 (8B) with stock Hugging Face + PEFT requires **at least 24 GB to 32 GB VRAM**.
- On consumer hardware (12GB or 16GB GPUs), training crashes immediately with:
  ```text
  torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.40 GiB...
  ```
- Long-context fine-tuning (>8,192 tokens) is virtually impossible without 80GB enterprise GPUs.

---

# 3. Unsloth Architecture & The "Secret Sauce"

Unsloth completely rewrites the Transformer forward and backward execution pipeline. It does this through six primary architectural pillars:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        UNSLOTH ACCELERATION ENGINE                           │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. Hand-Written OpenAI Triton Kernels (Replaces PyTorch generic CUDA)        │
│ 2. Operator Fusion: RMSNorm + RoPE + QKV Projections fused into 1 pass       │
│ 3. Manual Backpropagation Engine (Bypasses PyTorch Dynamic Autograd Graph)   │
│ 4. Custom Cross-Entropy Loss with In-Kernel Softmax Normalization            │
│ 5. Smart Sequence Packing: Merges short sequences without cross-attention    │
│ 6. Zero-Overhead Memory Caching: Allocates exact tensor footprints           │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Custom CUDA & OpenAI Triton Kernels
Instead of relying on PyTorch's generic CUDA dispatch, Unsloth is written in **OpenAI Triton**. Triton is a Python-based language and compiler that allows developers to write hardware-level GPU code with block-level memory management.
- Unsloth's Triton kernels explicitly control GPU thread blocks, shared memory allocation, and register reuse.
- Intermediate results stay pinned inside the GPU's high-speed L1/Shared Memory cache.

### 3.2 Operator Fusion
Unsloth fuses chains of operations into unified single-pass kernels:
- **Fused RoPE:** Rotary position embeddings are computed and applied to Query and Key tensors simultaneously in-place.
- **Fused RMSNorm:** Normalization factors and scaling parameters are calculated in a single memory read.
- **Fused SwiGLU / GeLU:** The gate projection, non-linear activation, and up projection are executed within the same GPU thread block.

### 3.3 Manual Backpropagation (Replacing PyTorch Autograd)
This is Unsloth's most radical innovation. **Unsloth discards PyTorch autograd for the core Transformer blocks.**
- The developers derived the exact analytical gradients for RMSNorm, RoPE, Attention, MLP projections, and Cross-Entropy on paper.
- They wrote custom `.backward()` kernels in Triton for each block.
- **Why this matters:** Because the backward math is computed directly from output gradients and input states, **intermediate activation tensors do not need to be saved in VRAM**. VRAM consumption drops by **50% to 80% instantly**.

### 3.4 In-Kernel Cross-Entropy Loss
In standard language modeling, computing loss requires projecting the final hidden dimension ($d_{model} = 4096$) to the full vocabulary dimension ($V = 128,256$ in LLaMA-3).
- In standard PyTorch, this produces an enormous tensor of logits:
  $$\text{Shape: } [Batch, Seq\_Len, Vocab\_Size] = [2, 2048, 128256] \approx 1.05 \text{ billion floats} \approx 4.2 \text{ GB VRAM}$$
- Just calculating Cross-Entropy causes an OOM spike!
- **Unsloth's Solution:** Unsloth computes the log-softmax, normalization constant, and negative log-likelihood **chunk by chunk inside a fused Triton kernel**. It never allocates the full $[B, S, V]$ tensor in global VRAM.

### 3.5 Smart Gradient Checkpointing
Standard PyTorch gradient checkpointing discards forward activations and recomputes the entire forward pass during the backward pass. This reduces memory by ~35% but incurs a **30% execution slowdown**.
- Unsloth implements **selective smart checkpointing**.
- It only checkpoints memory-intensive attention matrices, while caching lightweight normalized representations.
- Recomputation uses Unsloth's ultra-fast fused kernels, reducing the recomputation time penalty from 30% down to **<2%**.

### 3.6 Native Sequence Packing (Neat Packing)
Standard batching pads short examples with `<pad>` tokens to reach `max_seq_length`. If sample 1 has 100 tokens and sample 2 has 2,048 tokens, the GPU spends over 90% of its cycles multiplying zeros for sample 1.
- Unsloth concatenates multiple short conversations into a single contiguous block:
  $$[D_1, <eos>, D_2, <eos>, D_3, <eos>]$$
- It injects **custom attention boundary masks**, ensuring that tokens in $D_2$ can never attend to tokens in $D_1$.
- GPU compute efficiency reaches **95%+**.

### 3.7 Exact Mathematics — Zero Accuracy Degradation Guarantee
Unsloth does not use lossy approximations, low-bit activation pruning, or stochastic skipping.
- The forward calculations compute the exact mathematical formula of the Transformer paper.
- The backward calculations compute the exact analytical gradient of the loss function.
- The resulting model weights and loss curves are **bit-for-bit identical** to standard 16-bit PyTorch training.

---

# 4. Mathematical Deep Dive: Derivations of Fused Operators

To understand why Unsloth is mathematically exact, let us review the mathematical formulation of its fused kernels.

### 4.1 RMSNorm Forward & Backward Pass
Root Mean Square Normalization replaces standard LayerNorm by removing the mean-centering step:

$$\text{Forward: } y_i = \frac{x_i}{\text{RMS}(x)} \cdot \gamma_i, \quad \text{where } \text{RMS}(x) = \sqrt{\frac{1}{d} \sum_{j=1}^d x_j^2 + \epsilon}$$

Here, $x \in \mathbb{R}^d$ is the hidden state vector, $\gamma \in \mathbb{R}^d$ is the learnable gain parameter, and $\epsilon$ is a small stability constant.

**Analytical Backward Pass:**
Given the incoming gradient from the next layer $\frac{\partial L}{\partial y}$, standard autograd stores intermediate tensor $\text{RMS}(x)$ and all normalized states. Unsloth derives the exact gradient with respect to input $x_i$ directly:

$$\frac{\partial L}{\partial x_i} = \frac{\gamma_i}{\text{RMS}(x)} \frac{\partial L}{\partial y_i} - \frac{x_i}{d \cdot \text{RMS}(x)^3} \sum_{j=1}^d \left( \frac{\partial L}{\partial y_j} \cdot \gamma_j \cdot x_j \right)$$

$$\frac{\partial L}{\partial \gamma_i} = \frac{\partial L}{\partial y_i} \cdot \frac{x_i}{\text{RMS}(x)}$$

By fusing this summation into a single Triton parallel reduction across thread registers, Unsloth computes $\frac{\partial L}{\partial x}$ in a single pass without allocating intermediate memory buffers.

### 4.2 Rotary Positional Embeddings (RoPE) In-Place Rotation
RoPE encodes token position $m$ by rotating pairs of adjacent features in Query and Key vectors:

$$R_{\Theta, m}^d = \begin{pmatrix} \cos m\theta_1 & -\sin m\theta_1 & 0 & 0 & \dots \\ \sin m\theta_1 & \cos m\theta_1 & 0 & 0 & \dots \\ 0 & 0 & \cos m\theta_2 & -\sin m\theta_2 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

For a 2D feature pair $(x_1, x_2)$:
$$\begin{pmatrix} x_1' \\ x_2' \end{pmatrix} = \begin{pmatrix} x_1 \cos(m\theta) - x_2 \sin(m\theta) \\ x_1 \sin(m\theta) + x_2 \cos(m\theta) \end{pmatrix}$$

Standard PyTorch implements this by concatenating split tensors: `torch.cat((-x[..., 1::2], x[..., ::2]), dim=-1)`. This triggers tensor allocations and memory copies.
**Unsloth's Triton Kernel:** Computes the sine and cosine frequencies directly in GPU registers and performs the rotation in-place in SRAM.

### 4.3 Low-Rank Adaptation (LoRA) Matrix Math
For a frozen linear weight matrix $W_0 \in \mathbb{R}^{d \times k}$, LoRA decomposes the weight update $\Delta W$ into two low-rank matrices $A \in \mathbb{R}^{r \times k}$ and $B \in \mathbb{R}^{d \times r}$ with rank $r \ll \min(d, k)$:

$$\text{Forward: } h = W_0 x + \frac{\alpha}{r} (B \cdot A) x$$

During training:
- Base weights $W_0$ remain completely frozen in 4-bit (NF4) precision.
- Gradients are only computed for $A$ and $B$:
  $$\frac{\partial L}{\partial B} = \frac{\alpha}{r} \left( \frac{\partial L}{\partial h} \right)^T (A x), \quad \frac{\partial L}{\partial A} = \frac{\alpha}{r} \left( B^T \frac{\partial L}{\partial h} \right) x^T$$
Unsloth combines the dequantization of $W_0$, the low-rank projection $(BA)x$, and the gradient accumulation into fused matrix multiplication kernels.

---

# 5. Software Stack & Architectural Hierarchy

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DEEP LEARNING PLATFORMS                         │
│                  PyTorch  /  CUDA  /  Triton  /  ROCm                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                       HIGH-LEVEL ECOSYSTEM                             │
│       Hugging Face Transformers  │  PEFT  │  TRL (SFT / DPO / PPO)     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   UNSLOTH OPTIMIZATION ENGINE                          │
│  FastLanguageModel  │  Custom Triton Kernels  │  Manual Backprop       │
│  Fused RMSNorm/RoPE │  Cross-Entropy Engine   │  Neat Sequence Packing │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                        HARDWARE ACCELERATION                           │
│     NVIDIA GPUs (T4, V100, RTX 3090/4090, A100, H100, B200)            │
└────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Where Unsloth Fits Between PyTorch, Hugging Face, and TRL
- **PyTorch:** Provides the low-level tensor runtime, CUDA driver bindings, and memory allocator.
- **Hugging Face Transformers:** Defines model architectures, configuration classes, and tokenizers.
- **PEFT:** Provides the high-level LoRA configuration interface (`LoraConfig`).
- **TRL:** Provides the dataset loaders, loss abstractions, and training engines (`SFTTrainer`, `DPOTrainer`, `GRPOTrainer`).
- **Unsloth:** Sits directly underneath `transformers` and `peft`. It intercepts the model definition and replaces the standard forward/backward functions with its custom Triton kernels.

### 5.2 `FastLanguageModel` vs `AutoModelForCausalLM`
`FastLanguageModel` is Unsloth's drop-in replacement for Hugging Face's `AutoModelForCausalLM`. When called:
1. It downloads or loads the model weights.
2. It detects the GPU architecture (Ampere, Hopper, Turing).
3. It patches the model layers with Unsloth's fused attention, RoPE, RMSNorm, and MLP blocks.
4. It sets up memory mapping to prevent redundant host-to-device RAM copies.

---

# 6. The End-to-End 7-Stage Pipeline

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    THE 7-STAGE UNSLOTH WORKFLOW PIPELINE                     │
├─────────────────┬────────────────────────────────────────────────────────────┤
│ 1. Load         │ FastLanguageModel.from_pretrained(model_name, max_seq_len) │
│ 2. Quantize     │ load_in_4bit=True (Instant pre-quantized weights)          │
│ 3. Inject LoRA  │ FastLanguageModel.get_peft_model(model, r=16, alpha=32)    │
│ 4. Train        │ SFTTrainer / GRPOTrainer (TRL integration + neat packing)  │
│ 5. Inference    │ FastLanguageModel.for_inference(model) (2× speedup)        │
│ 6. Evaluate     │ Evaluate loss, benchmark generation latency                │
│ 7. Export       │ model.save_pretrained_merged(..., tokenizer, "gguf")       │
└─────────────────┴────────────────────────────────────────────────────────────┘
```

---

# 7. Supported Models, Architectures & Modalities

Unsloth maintains an extensive catalog of pre-quantized, verified base models under the `unsloth` Hugging Face organization.

### 7.1 Text-to-Text Language Models
| Model Family | Key Variants | Supported Context Length |
|---|---|---|
| **LLaMA 3.1 / 3.2** | 1B, 3B, 8B, 70B | Up to 128,000 tokens (Native RoPE) |
| **Qwen 2.5 / Coder** | 0.5B, 1.5B, 3B, 7B, 14B, 32B, 72B | Up to 128,000 tokens |
| **Mistral / NeMo** | 7B, 12B, Mixtral 8x7B, 8x22B | Up to 32,000–128,000 tokens |
| **Gemma 2** | 2B, 9B, 27B | Up to 8,192 tokens |
| **Phi-3 / Phi-4** | Mini (3.8B), Small (7B), Medium (14B) | Up to 128,000 tokens |
| **DeepSeek** | DeepSeek-V2.5, DeepSeek-V3, DeepSeek-R1-Distill | Extended context windows |
| **TinyLlama** | 1.1B Intermediate & Chat | Up to 2,048 tokens |

### 7.2 Multimodal Vision-Language Models
Unsloth provides accelerated fine-tuning for multimodal vision models:
- **Qwen2-VL** (2B, 7B, 72B)
- **Llama-3.2-Vision** (11B, 90B)
- **Pixtral-12B**
By fusing the vision encoder's patch projection and multi-head attention kernels, Unsloth cuts visual fine-tuning memory by **up to 60%**.

### 7.3 Speech & Audio Models
- **OpenAI Whisper (Tiny to Large-v3):** High-speed fine-tuning for automated speech recognition (ASR) and translation.
- **Orpheus TTS:** Text-to-speech parameter adaptation.

### 7.4 Classical Encoders
- **BERT, RoBERTa, DeBERTa:** Sequence classification, token extraction, and embedding fine-tuning.

---

# 8. Supported Fine-Tuning Paradigms

### 8.1 4-bit QLoRA (NF4 & INT8)
- Base weights loaded in 4-bit NormalFloat (`load_in_4bit=True`).
- Adapter matrices trained in 16-bit (BF16/FP16).
- Unsloth's Triton dequantization kernel outperforms standard bitsandbytes by **~4× in throughput**.

### 8.2 16-bit LoRA & Full Fine-Tuning
- Base weights loaded in Float16 or Bfloat16.
- Ideal when maximum precision is required or when fine-tuning on enterprise GPUs (A100/H100).

### 8.3 Native FP8 Training
- Supported on modern NVIDIA architectures (Ada Lovelace RTX 4090, Hopper H100).
- Halves memory footprint while preserving numerical stability over standard INT8.

### 8.4 Reinforcement Learning (RL) Superpowers
Unsloth has established itself as the leading platform for RL alignment:
- **GRPO (Group Relative Policy Optimization):** DeepSeek-R1 reasoning alignment.
- **DPO (Direct Preference Optimization):** Reference model caching with 60% memory savings.
- **PPO (Proximal Policy Optimization):** Full policy, value, and reward modeling.
- **KTO (Kahneman-Tversky Optimization):** Preference alignment from un-paired thumbs up/down data.
- **ORPO (Odds Ratio Preference Optimization):** Single-step combined SFT + preference loss.

---

# 9. Deep Dive into GRPO: DeepSeek-R1 Style Reasoning on a Single GPU

One of the most consequential recent updates to Unsloth is its native acceleration of **Group Relative Policy Optimization (GRPO)**.

### 9.1 Why Traditional PPO Fails on Consumer Hardware
In classical Reinforcement Learning from Human Feedback (PPO):
1. The **Policy Model** generates candidate completions.
2. A separate **Value / Critic Model** predicts expected future rewards for every token.
3. A **Reward Model** evaluates completions.
4. A **Reference Model** prevents policy drift via KL divergence.

Maintaining 4 separate copies of an 8B model in GPU memory requires **over 80 GB of VRAM**. PPO is impossible on a single consumer GPU.

### 9.2 The Mathematical Mechanics of GRPO
Introduced by DeepSeek in the R1 reasoning paper, GRPO **completely eliminates the Value/Critic model**:

```
                       GRPO REASONING ARCHITECTURE
                       
              ┌────────────────────────────────────────┐
              │           Input Prompt (Query)         │
              └───────────────────┬────────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Candidate Gen 1  │    │ Candidate Gen 2  │    │ Candidate Gen G  │
│      (o₁)        │    │      (o₂)        │    │      (o_G)       │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Reward Score r₁  │    │ Reward Score r₂  │    │ Reward Score r_G │
│ (Math / Format)  │    │ (Math / Format)  │    │ (Math / Format)  │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                 ┌───────────────▼───────────────┐
                 │  Group Normalization:         │
                 │  A_i = (r_i - Mean) / StdDev  │
                 └───────────────┬───────────────┘
                                 │
                 ┌───────────────▼───────────────┐
                 │  Policy Update (PPO-Clip)     │
                 └───────────────────────────────┘
```

Instead of predicting token values with a critic network:
1. For each prompt $q$, the policy model samples a **group of $G$ candidate outputs**: $\{o_1, o_2, \dots, o_G\}$.
2. Each completion is scored by verifiable reward functions (e.g., did the math output match the answer? did it follow XML formatting?).
3. The **Advantage** $\hat{A}_i$ is computed relative to the group:
   $$\hat{A}_i = \frac{r_i - \text{mean}(\{r_1, \dots, r_G\})}{\text{std}(\{r_1, \dots, r_G\}) + \epsilon}$$
4. The policy objective maximizes:
   $$L_{GRPO}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^G \left( \min\left( \frac{\pi_\theta(o_i|q)}{\pi_{old}(o_i|q)} \hat{A}_i, \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{old}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) \hat{A}_i \right) - \beta D_{KL}(\pi_\theta || \pi_{ref}) \right) \right]$$

### 9.3 How Unsloth Slashes GRPO VRAM by 80%
- Because GRPO generates $G$ completions per prompt (typically $G = 4$ or $8$), activation memory explodes during generation and backprop.
- Unsloth streams group generation through its fused Triton kernels, sharing base weights and reference states.
- **Result:** You can fine-tune reasoning models using GRPO on a **single 16GB or 24GB GPU** instead of an 8× A100 cluster!

---

# 10. The Shock Factor: Extreme Long-Context Training

Unsloth's most famous technical achievement is enabling **long context training on single consumer GPUs**.

### 10.1 Hardware VRAM vs Maximum Sequence Length Scaling Matrix

Using **LLaMA-3.1 (8B)** as the benchmark:

| GPU Memory | Standard Hugging Face Limit | Unsloth Max Context Length |
|---|---|---|
| **8 GB VRAM** (RTX 3070, RTX 4060) | ❌ **OOM Crash** | **~3,000 tokens** |
| **12 GB VRAM** (RTX 3060, RTX 4070) | ❌ **OOM Crash** | **~21,000 tokens** |
| **16 GB VRAM** (Colab T4, RTX 4080) | ~2,048 tokens max | **~40,000 tokens** |
| **24 GB VRAM** (RTX 3090, RTX 4090) | ~4,096–8,192 tokens max | **~78,000 tokens** |
| **80 GB VRAM** (NVIDIA A100 / H100) | ~28,000 tokens max | **Up to ~340,000 tokens!** |

### 10.2 Why Standard Hugging Face Crashes at Long Contexts
Memory consumption in Transformers consists of:
$$\text{Total VRAM} = \text{Model Weights} + \text{Optimizer States} + \text{Gradients} + \text{Activations}$$
While model weights and optimizer states are fixed with respect to sequence length, **activation memory scales linearly or quadratically with sequence length $N$**:
$$\text{Activation Memory} \propto N \times d_{model} \times N_{layers} \times N_{heads}$$
At $N = 32,768$, PyTorch's autograd graph allocates **over 45 GB of VRAM solely for activation tensors**!

### 10.3 How Unsloth Solves the Long-Context Problem
1. **Dynamic Chunked RoPE:** Position embeddings are evaluated block-by-block without creating full positional grids.
2. **FlashAttention-2 & Xformers Backend:** Tiled matrix multiplication avoids materializing $N \times N$ attention probability matrices.
3. **Activation Recomputation via Triton:** Discards forward intermediate states and recalculates them on-the-fly during the backward pass in microseconds.

---

# 11. Memory Economics & Rigorous VRAM Calculation Guide

To accurately estimate your hardware requirements before launching training, use the following formulas:

### 11.1 The 4 Components of GPU Memory
$$\text{VRAM}_{\text{Total}} = \text{VRAM}_{\text{Model}} + \text{VRAM}_{\text{LoRA}} + \text{VRAM}_{\text{Optimizer}} + \text{VRAM}_{\text{Activations}}$$

### 11.2 Model Weight Memory Formulas
$$\text{Memory (16-bit FP16/BF16)} = \text{Parameters (in Billions)} \times 2 \text{ GB}$$
$$\text{Memory (8-bit INT8)} = \text{Parameters (in Billions)} \times 1 \text{ GB}$$
$$\text{Memory (4-bit QLoRA)} = \text{Parameters (in Billions)} \times 0.5 \text{ GB}$$

*Examples:*
- LLaMA-3.1 (8B) in FP16: $8 \times 2 = 16 \text{ GB}$
- LLaMA-3.1 (8B) in 4-bit: $8 \times 0.5 = 4 \text{ GB}$ (Unsloth pre-quantized footprint)

### 11.3 Optimizer State Memory
Standard AdamW maintains two state tracking variables (momentum $\beta_1$ and variance $\beta_2$) in FP32 for every trainable parameter:
$$\text{AdamW Memory (Standard FP32)} = \text{Trainable Params} \times 8 \text{ bytes}$$
$$\text{AdamW Memory (8-bit quantized)} = \text{Trainable Params} \times 2 \text{ bytes}$$

Using `optim="adamw_8bit"` in Unsloth reduces optimizer memory overhead by **75%**.

---

# 12. Step-by-Step Code Implementation & Best Practices

Below is the production-tested code implementation.

### 12.1 Environment Setup & Diagnostics
```python
import torch
import random
import numpy as np

SEED = 3407
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

assert torch.cuda.is_available(), "CUDA GPU is required!"
print(f"GPU: {torch.cuda.get_device_name(0)}")
```

### 12.2 Model Initialization (`FastLanguageModel.from_pretrained`)
```python
from unsloth import FastLanguageModel

max_seq_length = 2048  # Supports 4096, 8192, up to 128K
dtype = None           # None = auto-detect (BF16 on Ampere/Hopper)
load_in_4bit = True    # 4-bit QLoRA

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/tinyllama-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)
```

### 12.3 LoRA Adapter Injection (`FastLanguageModel.get_peft_model`)
```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
    lora_alpha=32,
    lora_dropout=0.0,                        # 0.0 is required for Triton operator fusion!
    bias="none",
    use_gradient_checkpointing="unsloth",    # Unsloth ultra-fast checkpointing
    random_state=SEED,
)

model.print_trainable_parameters()
```

### 12.4 Data Formatting & The Mandatory EOS Token Rule
```python
alpaca_prompt = \"\"\"Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}\"\"\"

EOS_TOKEN = tokenizer.eos_token  # CRITICAL: Ensures model knows when to terminate

def formatting_prompts_func(examples):
    instructions = examples["instruction"]
    inputs       = examples["input"]
    outputs      = examples["output"]
    texts = []
    for instruction, input_text, output in zip(instructions, inputs, outputs):
        text = alpaca_prompt.format(instruction, input_text, output) + EOS_TOKEN
        texts.append(text)
    return {"text": texts}

dataset = dataset.map(formatting_prompts_func, batched=True)
```

### 12.5 TRL `SFTTrainer` & `SFTConfig` Configuration
```python
from trl import SFTTrainer, SFTConfig

training_args = SFTConfig(
    output_dir="./outputs",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,      # Effective batch size = 2 * 4 = 8
    warmup_steps=10,
    max_steps=60,                       # Or num_train_epochs=3
    learning_rate=2e-4,                 # 2e-4 standard for LoRA
    fp16=not torch.cuda.is_bf16_supported(),
    bf16=torch.cuda.is_bf16_supported(),
    logging_steps=10,
    optim="adamw_8bit",                 # 8-bit AdamW optimizer
    weight_decay=0.01,
    lr_scheduler_type="cosine",
    seed=SEED,
    report_to="none",
)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    packing=False,                      # Set True to enable Unsloth Neat Packing
    args=training_args,
)

trainer.train()
```

### 12.6 Accelerated Inference (`FastLanguageModel.for_inference`)
```python
FastLanguageModel.for_inference(model)

prompt = alpaca_prompt.format("Explain what a Linux pipe (|) does.", "", "")
inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        use_cache=True,
        temperature=0.7,
        top_p=0.9,
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

# 13. Model Export & Deployment Freedom

Unsloth provides native export pathways so you can deploy your fine-tuned model anywhere.

```
                     ┌──────────────────────────────────────────────┐
                     │          TRAINED UNSLOTH MODEL               │
                     └──────────────────────┬───────────────────────┘
                                            │
         ┌───────────────────┬──────────────┴───────┬───────────────────┐
         ▼                   ▼                      ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  LoRA Adapters  │ │ Merged 16-bit   │ │ Merged 4-bit    │ │  GGUF Format    │
│  save_pretrained│ │ (vLLM / SGLang) │ │ (Hugging Face)  │ │ (Ollama/llama.cpp│
│  Size: ~50MB    │ │ Size: ~16GB     │ │ Size: ~5.5GB    │ │ Size: ~4.5GB    │
└─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘
```

### 13.1 Saving Standalone LoRA Adapters
Saves only the lightweight adapter weights ($A$ and $B$ matrices):
```python
model.save_pretrained("lora_model")
tokenizer.save_pretrained("lora_model")
```

### 13.2 Merging into 16-bit Standalone Models
Fuses LoRA weights into the base weights ($W = W_0 + \frac{\alpha}{r}BA$) for deployment on **vLLM**, **TGI**, or **SGLang**:
```python
model.save_pretrained_merged("merged_16bit_model", tokenizer, save_method="merged_16bit")
```

### 13.3 Native GGUF Quantization
Exports directly to quantized GGUF format for **llama.cpp** or **Ollama**:
```python
model.save_pretrained_gguf("model_gguf", tokenizer, quantization_method="q4_k_m")
```

### 13.4 Creating Ollama Modelfiles & Local Serving
To deploy in Ollama:
```dockerfile
# Modelfile
FROM ./model_gguf/unsloth.Q4_K_M.gguf
TEMPLATE """{{ .Prompt }}"""
```
Run in terminal:
```bash
ollama create my-custom-model -f Modelfile
ollama run my-custom-model
```

---

# 14. Comprehensive Benchmarks: Unsloth vs Stock Hugging Face

| Feature / Metric | Standard Hugging Face (PyTorch + PEFT) | Unsloth Accelerated Engine |
|---|---|---|
| **Training Speed** | Baseline (1.0×) | **2.0× to 5.0× faster** |
| **VRAM Consumption** | High (Full autograd DAG) | **50% to 80% lower** |
| **Max Context on 16GB GPU** | ~2,048 tokens | **Up to 40,000+ tokens** |
| **Kernels Used** | Generic PyTorch CUDA kernels | **Custom OpenAI Triton fused kernels** |
| **Backpropagation** | Dynamic Autograd recording | **Hand-derived analytical gradients** |
| **Sequence Packing** | Manual (padding overhead) | **Native Neat Packing with boundary masking** |
| **Inference Mode** | Standard PyTorch forward | **2× faster native inference** |
| **GGUF Export** | Multi-step external C++ scripts | **One-line native export (`save_pretrained_gguf`)** |
| **RL Support** | Heavy multi-GPU setups required | **Single GPU GRPO / DPO enabled** |
| **Accuracy Loss** | 0% (Reference) | **0% (Exact mathematics guarantee)** |

---

# 15. When to Use Unsloth vs When NOT to Use Unsloth (Decision Matrix)

```
                              ┌────────────────────────────────────────┐
                              │    Do you want to fine-tune an LLM?    │
                              └───────────────────┬────────────────────┘
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         ▼                                                 ▼
             ┌───────────────────────┐                         ┌───────────────────────┐
             │ Single GPU / Desktop  │                         │ Multi-Node Cluster    │
             │ or Cloud Colab/RunPod │                         │ (100+ H100 Nodes)     │
             └───────────┬───────────┘                         └───────────┬───────────┘
                         │                                                 │
                         ▼                                                 ▼
             ┌───────────────────────┐                         ┌───────────────────────┐
             │   USE UNSLOTH!        │                         │ Megatron-LM /         │
             │ (2-5x faster, 80% VRAM│                         │ DeepSpeed ZeRO-3      │
             │ savings, instant GGUF)│                         └───────────────────────┘
             └───────────────────────┘
```

### ✅ When to Use Unsloth
1. **Constrained GPU Hardware:** You are training on a single GPU (Google Colab T4, RTX 3060, RTX 4090, A100).
2. **Long-Context Tasks:** Fine-tuning on books, legal contracts, or large codebases (8K to 64K+ tokens).
3. **Reasoning RL (GRPO):** Training DeepSeek-R1 style reasoning models without multi-GPU infrastructure.
4. **Fast Prototyping:** Iterating quickly where a 4-hour job finishes in 1 hour.
5. **Local Deployment:** You intend to serve via Ollama, vLLM, or llama.cpp.

### ❌ When NOT to Use Unsloth
1. **Multi-Node Distributed Training:** Unsloth is optimized for single-GPU and single-node multi-GPU workloads. For 100+ GPU supercomputers, Megatron-LM is the industry standard.
2. **Non-Transformer Architectures:** CNNs, RNNs, and Mamba/SSM architectures are not supported.
3. **Non-NVIDIA Hardware:** AMD ROCm and Apple Silicon (MPS) are currently experimental; NVIDIA CUDA is required.
4. **Strict No-Code GUI Requirement:** If you require a browser GUI without writing Python scripts, **LLaMA Factory (LlamaBoard)** is better suited.

---

# 16. Hyperparameter Reference Dictionary (`SFTConfig`)

| Hyperparameter | Typical Value | Purpose | Impact on Training |
|---|---|---|---|
| `per_device_train_batch_size` | `1` or `2` | Batch size per GPU step | Lower values save VRAM. Keep at 1–2 for low memory. |
| `gradient_accumulation_steps` | `4` or `8` | Number of steps before updating weights | Simulates effective batch size ($BS_{eff} = Batch \times Grad\_Accum$). |
| `learning_rate` | `2e-4` | Step size for optimizer | Standard for LoRA. Full FT typically uses `2e-5`. |
| `lr_scheduler_type` | `"cosine"` | Learning rate decay curve | Smooth cosine decay prevents sudden divergence. |
| `warmup_ratio` / `warmup_steps` | `0.03` / `10` | Initial LR warm-up phase | Prevents catastrophic forgetting in initial steps. |
| `optim` | `"adamw_8bit"` | Optimizer algorithm | 8-bit AdamW cuts optimizer VRAM by 75%. |
| `weight_decay` | `0.01` | L2 regularization penalty | Prevents LoRA weights from overfitting on small datasets. |
| `max_seq_length` | `2048` | Sequence token cutoff | Longer context requires more activation memory. |
| `packing` | `True` / `False` | Unsloth Neat Sequence Packing | Combines short samples; eliminates padding overhead. |
| `fp16` / `bf16` | Auto-detected | Mixed precision training | BF16 has higher dynamic range; preferred on Ampere+. |
| `seed` | `3407` | Random initialization seed | Guarantees identical shuffles and reproducible runs. |

---

# 17. Common Errors, Debugging Checklist & Solutions

### 1. `ImportError: cannot import name 'FastLanguageModel'`
- **Cause:** Incompatible transformers version or corrupted unsloth install.
- **Fix:** Install unsloth without dependencies overriding transformers:
  ```bash
  pip install --no-deps "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
  ```

### 2. Model Rambles Infinitely or Fails to Stop
- **Cause:** Forgetting to append `<eos>` token during dataset formatting.
- **Fix:** Ensure prompt formatter appends `+ tokenizer.eos_token`:
  ```python
  text = alpaca_prompt.format(instruction, input_text, output) + tokenizer.eos_token
  ```

### 3. `CUDA out of memory` during Long Context Training
- **Cause:** Sequence length combined with batch size exceeds available VRAM.
- **Fix:**
  - Set `per_device_train_batch_size = 1`.
  - Increase `gradient_accumulation_steps = 8`.
  - Verify `load_in_4bit = True`.
  - Enable `use_gradient_checkpointing = "unsloth"`.

### 4. Loss is `NaN`
- **Cause:** Numerical overflow in FP16 or learning rate too high.
- **Fix:** Switch to `bf16=True` (if supported) or lower learning rate to `1e-4` or `5e-5`.

---

# 18. Quick Revision Cheat Sheet

```python
# 1. Imports
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig

# 2. Load Model & Tokenizer (4-bit QLoRA)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/tinyllama-bnb-4bit",
    max_seq_length=2048,
    load_in_4bit=True,
)

# 3. Add Optimized LoRA
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.0,
    bias="none",
)

# 4. Train with SFTTrainer
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=SFTConfig(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        max_steps=60,
        learning_rate=2e-4,
        optim="adamw_8bit",
        output_dir="outputs",
    ),
)
trainer.train()

# 5. Fast Native Inference
FastLanguageModel.for_inference(model)
inputs = tokenizer(["Instruction: What is AI?\nResponse:"], return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=64)

# 6. Multi-Format Export Freedom
model.save_pretrained("lora_model")                                      # Save LoRA adapter (~50MB)
model.save_pretrained_merged("merged_model", tokenizer, "merged_16bit")  # Save 16-bit standalone
model.save_pretrained_gguf("gguf_model", tokenizer, "q4_k_m")             # Export to GGUF for Ollama
```

---

*Document: `SLM_Experiment/07_unsloth/UNSLOTH_NOTES.md`*
