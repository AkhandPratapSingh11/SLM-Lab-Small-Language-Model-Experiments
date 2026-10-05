# 🧠 SLM-Lab — Small Language Model Experiments

> **A structured, hands-on lab notebook series** for learning and experimenting with Small Language Models (SLMs) and Large Language Models (LLMs) — covering the full pipeline from model loading to fine-tuning, distillation, quantization, alignment, and no-code/CLI fine-tuning frameworks.

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
├── 05_funetuing/            ← Domain-specific LLM Fine-Tuning (alias: 05_finetune)
│   ├── finetune.ipynb               ← Master notebook (end-to-end)
│   ├── FINETUNING_NOTES.md          ← 2,000+ line reference notes
│   ├── Instruction_finetuning_on_domain_specific_dataset.ipynb
│   ├── non_Instruction_pretrain_llm_finetuning_on_domain_specific_data.ipynb
│   └── content/                     ← Domain datasets (Metformin.pdf)
│
└── 06_lammafactory/         ← LLaMA Factory (WebUI + CLI + YAML Engine)
    ├── llamafactory.ipynb           ← Master notebook (WebUI, CLI, QLoRA, Export)
    ├── LLAMA_FACTORY_NOTES.md       ← 2,300+ line comprehensive reference notes
    └── *.pdf                        ← Visual lecture notes & parameter cheatsheets
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

```
┌────────────────────────────────────────────────────────────────────────┐
│                        LLAMA FACTORY PLATFORM                          │
├────────────────────┬───────────────────────────────────────────────────┤
│  LlamaBoard WebUI  │  CLI Engine (YAML-Driven Automation)              │
│  - Browser GUI     │  - llamafactory-cli train / chat / eval / export  │
│  - Zero code       │  - OpenAI-compatible REST API server              │
└────────────────────┴───────────────────────────────────────────────────┘
```

**Key capabilities covered:**
- **Supported Formats:** Alpaca (Instruction), ShareGPT (Chat), DPO (Preference), KTO
- **Training Stages:** Pretraining, SFT, Reward Modeling, PPO (RLHF), DPO, KTO
- **PEFT Methods:** LoRA, QLoRA (4-bit BitsAndBytes / HQQ), Freeze Tuning, Full FT
- **Accelerators:** Unsloth kernels (2x faster, 50% less VRAM), GaLore (gradient projection), FlashAttention-2
- **Model Export & Serving:** LoRA weights merge (`merge_and_unload`), GGUF conversion, and OpenAI-compatible API serving
- Accompanied by **`LLAMA_FACTORY_NOTES.md`** (2,300+ lines complete guide covering all parameters, hyperparameters, and troubleshooting)

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
| `trl` | latest | DPO, PPO, SFT trainers |
| `PyMuPDF` (fitz) | latest | PDF text extraction |
| `llamafactory` | latest | Unified WebUI & CLI fine-tuning framework |
| `gradio` | latest | Web UI for model interaction & LlamaBoard |

**Hardware Tested:** NVIDIA H100 80GB HBM3 (all notebooks configured to easily scale down to consumer GPUs like RTX 3060 / 3090 / 4090 / T4)

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

# (Optional) For LLaMA Factory module:
git clone https://github.com/hiyouga/LLaMA-Factory.git
pip install -e ./LLaMA-Factory
```

---

## 📖 Recommended Learning Path

```
Level 1 (Beginner)     →  01_huggingface   (Hub, pipelines, AutoClasses)
Level 2 (Intermediate) →  02_bert_tasks    (Encoder fine-tuning, 4 NLP tasks)
Level 3 (Advanced)     →  03_distillation  (Teacher-student, dark knowledge)
Level 4 (Advanced)     →  04_quantization  (INT8/INT4, GPTQ, AWQ, GGUF)
Level 5 (Expert)       →  05_funetuing     (LoRA, SFT, Response Masking, DPO)
Level 6 (Production)   →  06_lammafactory  (WebUI, CLI configs, Unsloth, GaLore, API)
```

---

## 📝 Notes Style

Each module ships with exhaustive Markdown notes (`*_NOTES.md`) covering:
- Intuitions & analogies for complex deep learning concepts
- Rigorous mathematical formulations (derivations of Loss functions, LoRA decomposition, DPO objective)
- Real-world production code snippets with detailed comments
- Decision matrices & hardware trade-off tables
- Common error diagnoses and debugging checklists (NCCL errors, OOMs, label masking)

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co) — transformers, datasets, peft, trl
- [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) — unified fine-tuning engine by hiyouga
- [TinyLlama](https://github.com/jzhang38/TinyLlama) — compact 1.1B foundation LLM
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) — instruction tuning format
- [LoRA paper](https://arxiv.org/abs/2106.09685) — Hu et al. 2021
- [QLoRA paper](https://arxiv.org/abs/2305.14314) — Dettmers et al. 2023
- [DPO paper](https://arxiv.org/abs/2305.18290) — Rafailov et al. 2023
