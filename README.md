# 🧠 SLM-Lab — Small Language Model Experiments

> **A structured, hands-on lab notebook series** for learning and experimenting with Small Language Models (SLMs) and Large Language Models (LLMs) — covering the full pipeline from model loading to fine-tuning, distillation, quantization, alignment, LLaMA Factory, and ultra-fast Unsloth acceleration.

---

## 🗂️ Repository Structure

```
SLM_Experiment/
├── 01_huggingface/          ← Hugging Face ecosystem & Hub fundamentals
│   ├── huggingface.ipynb
│   └── HUGGINGFACE_NOTES.md
│
├── 02_bert_tasks/           ← BERT fine-tuning across 4 NLP tasks
│   ├── bert_finetuning.ipynb
│   ├── BERT_FINETUNING_NOTES.md
│   ├── multi_task_bert/     ← Modular multi-task BERT pipeline
│   └── checkpoints/
│
├── 03_distillation/         ← Knowledge Distillation (CNN + LLM)
│   ├── Knowledge_Distillation_CNN.ipynb
│   ├── Knowledge_Distillation_LLM.ipynb
│   └── structured_KD_notes.md
│
├── 04_quantization/         ← LLM Quantization (INT8 / INT4 / GPTQ / GGUF)
│   ├── LLM_Quantization.ipynb
│   ├── LLM_Quantization_Notes.md
│   └── structured_quantization_notes.md
│
├── 05_funetuing/            ← Domain-specific LLM Fine-Tuning
│   ├── finetune.ipynb               ← Master notebook (end-to-end)
│   ├── FINETUNING_NOTES.md          ← 2,000+ line reference notes
│   ├── Instruction_finetuning_on_domain_specific_dataset.ipynb
│   ├── non_Instruction_pretrain_llm_finetuning_on_domain_specific_data.ipynb
│   └── content/                     ← Domain datasets (Metformin.pdf)
│
├── 06_lammafactory/         ← LLaMA Factory Framework (WebUI + CLI Engine)
│   ├── llamafactory.ipynb           ← Master notebook (WebUI, YAML configs, QLoRA)
│   ├── LLAMA_FACTORY_NOTES.md       ← 2,300+ line comprehensive reference notes
│   └── *.pdf                        ← Visual lecture notes & parameter cheatsheets
│
└── 07_unsloth/              ← Unsloth Ultra-Fast & Memory-Efficient Fine-Tuning 🦥
    ├── unsloth_practical.ipynb      ← Master tutorial notebook (LoRA, SFT, Export)
    ├── UNSLOTH_NOTES.md             ← 800+ line comprehensive architectural guide
    └── *.pdf                        ← Lecture slides & handwritten notes
```

---

## 📚 Modules Overview

### `01` — Hugging Face Ecosystem
> Everything you need to start using Hugging Face in production.

- Hub authentication, model/dataset loading, `AutoClasses`, `pipeline` API
- Publishing models to the Hub (`push_to_hub`)
- Serverless Inference API & Spaces
- Detailed notes in Hinglish with step-by-step examples

---

### `02` — BERT Fine-Tuning (4 NLP Tasks)
> Multi-task fine-tuning of BERT from fundamentals to production-ready code.

| Task | Dataset | Output |
|---|---|---|
| Text Classification | IMDB Sentiment | Binary label (0/1) |
| Named Entity Recognition (NER) | CoNLL-2003 | Token-level labels |
| Extractive QA | SQuAD | Start/End token span |
| Natural Language Inference (NLI) | SNLI | Entailment / Contradiction / Neutral |

- Custom `TrainingArguments`, `Trainer` API, evaluation metrics
- Modular `multi_task_bert/` pipeline with shared `DataLoader`, model cards

---

### `03` — Knowledge Distillation
> Transfer intelligence from a large Teacher model to a compact Student model.

- **CNN Distillation**: ResNet teacher → small custom CNN student with soft-label loss
- **LLM Distillation**: Large language model → smaller language model using logit matching
- Covers temperature scaling, KL divergence, soft vs hard targets
- Detailed math: `L_KD = α × L_CE + (1-α) × T² × KL(σ(z_t/T) || σ(z_s/T))`

---

### `04` — LLM Quantization
> Compress large models for fast, memory-efficient inference.

- Symmetric & Asymmetric quantization math (INT8, INT4, NF4)
- PTQ (Post-Training Quantization) vs QAT (Quantization-Aware Training)
- GPTQ (Hessian-based layer-wise quantization)
- AWQ (Activation-aware Weight Quantization)
- GGML / GGUF formats and `llama.cpp` ecosystem

---

### `05` — Domain-Specific LLM Fine-Tuning ⭐
> The complete 4-stage pipeline to build a domain specialist assistant.

```
Base LLM (TinyLlama-1.1B)
    ↓
Stage 1: Non-Instruction Domain Adaptation  (raw PDF corpus, causal LM loss)
    ↓  merge_and_unload()
Stage 2: Supervised Instruction Fine-Tuning  (Alpaca format + response masking)
    ↓
Stage 3: Preference Alignment  (DPO / RLHF — theory + datasets)
    ↓
Domain Specialist Assistant  (Pharmacology: Metformin, Atorvastatin, mRNA)
```

**Key techniques covered:**
- LoRA & QLoRA with `peft` — `r`, `lora_alpha`, `target_modules` explained
- Full FT vs Selective Layer Freezing vs LoRA — VRAM comparison table
- **Response Masking** — `-100` label trick for SFT loss masking
- Two-stage LoRA pipeline (domain adapter → merge → instruction adapter)
- Text generation controls: `temperature`, `top_p`, `repetition_penalty`
- DPO mathematics from first principles
- Accompanied by **`FINETUNING_NOTES.md`** (2,000+ lines comprehensive reference)

---

### `06` — LLaMA Factory Framework (WebUI + CLI) 🚀
> Industrial-grade, all-in-one fine-tuning engine supporting 100+ open-source LLMs.

- **WebUI & CLI:** Train via browser GUI (LlamaBoard) or reproducible YAML configuration scripts
- **Supported Formats:** Alpaca (Instruction), ShareGPT (Chat), DPO (Preference), KTO
- **Training Stages:** Pretraining, SFT, Reward Modeling, PPO (RLHF), DPO, KTO
- **PEFT Methods:** LoRA, QLoRA (4-bit BitsAndBytes / HQQ), Freeze Tuning, Full FT
- **Accelerators:** Unsloth kernels, GaLore (gradient projection), FlashAttention-2
- **Model Export & Serving:** LoRA weights merge (`merge_and_unload`), GGUF conversion, and OpenAI-compatible REST API server
- Accompanied by **`LLAMA_FACTORY_NOTES.md`** (2,300+ lines complete guide covering all parameters and training stages)

---

### `07` — Unsloth Fine-Tuning & Inference Engine 🦥
> 2× to 5× faster training with 50% to 80% less VRAM on a single GPU.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        UNSLOTH ACCELERATION ENGINE                     │
├────────────────────┬───────────────────────────────────────────────────┤
│  Custom Kernels    │  Hand-written OpenAI Triton & CUDA kernels        │
│  Operator Fusion   │  RMSNorm, RoPE, and MLP fused in single GPU pass  │
│  Manual Backprop   │  Bypasses PyTorch autograd graph for zero bloat   │
│  Neat Packing      │  Packs sequences without cross-attention leakage  │
│  Extreme Context   │  Enables up to 300K+ token context windows        │
│  Reasoning RL      │  Cuts GRPO (DeepSeek-R1 style) VRAM by 80%        │
└────────────────────┴───────────────────────────────────────────────────┘
```

**Key capabilities covered:**
- **Exact Mathematics:** 0% accuracy degradation — identical loss curves to standard FP16/BF16
- **Context Scaling:** Train 40,000+ tokens on a 16GB GPU (vs 2,048 in standard PyTorch)
- **Fast Inference:** Built-in 2× inference speedup with `FastLanguageModel.for_inference()`
- **Deployment Freedom:** Direct export to GGUF (llama.cpp/Ollama), vLLM, and Hugging Face Hub
- Accompanied by **`UNSLOTH_NOTES.md`** (in-depth architectural guide, mathematical derivations, and memory economics)

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `torch` | 2.8.0+cu128 | Core deep learning framework |
| `transformers` | 5.18.0 | Model architectures & Trainer API |
| `datasets` | 5.0.1 | Data loading & preprocessing |
| `peft` | latest | LoRA, QLoRA — parameter-efficient fine-tuning |
| `bitsandbytes` | 0.50.2 | INT8/INT4 quantization kernels |
| `accelerate` | 1.15.0 | Multi-GPU & mixed precision management |
| `trl` | latest | DPO, PPO, SFT, and GRPO trainers |
| `unsloth` | latest | Triton/CUDA fused kernels & memory acceleration |
| `PyMuPDF` (fitz) | latest | PDF text extraction |
| `llamafactory` | latest | Unified WebUI & CLI fine-tuning framework |
| `gradio` | latest | Web UI for model interaction & LlamaBoard |

**Hardware Tested:** NVIDIA H100 80GB HBM3 (all notebooks configured to scale down to consumer GPUs like RTX 3060 / 3090 / 4090 / Colab T4)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/AkhandPratapSingh11/SLM-Lab-Small-Language-Model-Experiments.git
cd SLM-Lab-Small-Language-Model-Experiments

# Create and activate virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install core dependencies
pip install -U transformers datasets peft bitsandbytes accelerate trl PyMuPDF

# (Optional) For Unsloth module:
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

---

## 📖 Recommended Learning Path

```
Level 1 (Beginner)     →  01_huggingface   (Hub, pipelines, AutoClasses)
Level 2 (Intermediate) →  02_bert_tasks    (Encoder fine-tuning, 4 NLP tasks)
Level 3 (Advanced)     →  03_distillation  (Teacher-student, dark knowledge)
Level 4 (Advanced)     →  04_quantization  (INT8/INT4, GPTQ, AWQ, GGUF)
Level 5 (Expert)       →  05_funetuing     (LoRA, SFT, Response Masking, DPO)
Level 6 (Production)   →  06_lammafactory  (WebUI, CLI configs, YAML automation)
Level 7 (High-Perf)    →  07_unsloth       (Triton kernels, 80% VRAM savings, GRPO)
```

---

## 📝 Notes Style

Each module ships with exhaustive Markdown notes (`*_NOTES.md`) covering:
- Intuitions & analogies for complex deep learning concepts
- Rigorous mathematical formulations (derivations of loss functions, LoRA decomposition, DPO, GRPO)
- Real-world production code snippets with line-by-line commentary
- Decision matrices & hardware trade-off tables
- Common error diagnoses and debugging checklists (NCCL errors, OOMs, label masking)

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co) — transformers, datasets, peft, trl
- [Unsloth](https://github.com/unslothai/unsloth) — ultra-fast LLM fine-tuning by Daniel & Michael Han
- [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) — unified fine-tuning engine by hiyouga
- [TinyLlama](https://github.com/jzhang38/TinyLlama) — compact 1.1B foundation LLM
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) — instruction tuning format
- [LoRA paper](https://arxiv.org/abs/2106.09685) — Hu et al. 2021
- [DeepSeek-R1 / GRPO](https://arxiv.org/abs/2501.12948) — DeepSeek AI 2025

