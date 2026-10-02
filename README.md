# 🧠 SLM-Lab — Small Language Model Experiments

> **A structured, hands-on lab notebook series** for learning and experimenting with Small Language Models (SLMs) and Large Language Models (LLMs) — covering the full pipeline from model loading to fine-tuning, distillation, quantization, and alignment.

---

## 📌 Repo Name Suggestion

```
SLM-Lab
```
or
```
slm-experiments
```

> **About (GitHub description):**
> *"End-to-end experiments with Small & Large Language Models — Hugging Face ecosystem, BERT fine-tuning, knowledge distillation, quantization (INT8/INT4), and domain-specific LLM fine-tuning with LoRA, SFT & DPO. Includes detailed notes in every module."*

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
└── 05_funetuing/            ← Domain-specific LLM Fine-Tuning
    ├── finetune.ipynb               ← Master notebook (end-to-end)
    ├── FINETUNING_NOTES.md          ← 2000+ line reference notes
    ├── Instruction_finetuning_on_domain_specific_dataset.ipynb
    └── non_Instruction_pretrain_llm_finetuning_on_domain_specific_data.ipynb
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

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `torch` | 2.8.0+cu128 | Core deep learning framework |
| `transformers` | 5.17.0 | Model architectures & Trainer API |
| `datasets` | 5.0.1 | Data loading & preprocessing |
| `peft` | latest | LoRA, QLoRA — parameter-efficient fine-tuning |
| `bitsandbytes` | 0.50.2 | INT8/INT4 quantization kernels |
| `accelerate` | 1.15.0 | Multi-GPU & mixed precision management |
| `trl` | latest | DPO, PPO, SFT trainers |
| `PyMuPDF` (fitz) | latest | PDF text extraction |

**GPU:** NVIDIA H100 80GB HBM3 (experiments designed to scale down to RTX 3090/4090)

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/<your-username>/SLM-Lab.git
cd SLM-Lab

# Create virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -U transformers datasets peft bitsandbytes accelerate trl PyMuPDF

# Start with Module 01
jupyter notebook SLM_Experiment/01_huggingface/huggingface.ipynb
```

---

## 📖 Learning Path

```
Beginner    →  01_huggingface   (Hub, pipelines, AutoClasses)
Intermediate→  02_bert_tasks    (encoder fine-tuning, 4 NLP tasks)
Advanced    →  03_distillation  (teacher-student, soft labels)
Advanced    →  04_quantization  (INT8/INT4, GPTQ, GGUF)
Expert      →  05_funetuing     (LoRA, SFT, Response Masking, DPO)
```

---

## 📝 Notes Style

Each module ships with detailed Markdown notes (`*_NOTES.md`) covering:
- Concepts explained with analogies and intuitions
- Mathematical derivations (where applicable)
- Code snippets with line-by-line comments
- Decision tables (when to use what)
- Common pitfalls and fixes

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co) — transformers, datasets, peft, trl
- [TinyLlama](https://github.com/jzhang38/TinyLlama) — compact 1.1B LLM used throughout Module 05
- [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) — instruction dataset format
- [LoRA paper](https://arxiv.org/abs/2106.09685) — Hu et al. 2021
- [DPO paper](https://arxiv.org/abs/2305.18290) — Rafailov et al. 2023
