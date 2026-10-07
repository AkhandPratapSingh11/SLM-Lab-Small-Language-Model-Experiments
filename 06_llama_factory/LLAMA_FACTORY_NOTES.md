# 🦙 LLaMA Factory — Complete Structured Notes
### Source: LLM Finetuning with LLaMA Factory (WebUI + CLI + YAML Config)

---

# TABLE OF CONTENTS

1. What is LLaMA Factory?
2. Why Use LLaMA Factory?
3. Architecture — How LLaMA Factory Works Internally
4. Installation & Setup
5. Supported Models
6. Training Methods & Stages
   - 6.1 SFT — Supervised Fine-Tuning
   - 6.2 LoRA — Low-Rank Adaptation
   - 6.3 QLoRA — Quantized LoRA
   - 6.4 Full Fine-Tuning
   - 6.5 DPO — Direct Preference Optimization
   - 6.6 PPO — Proximal Policy Optimization (RLHF)
   - 6.7 Reward Modeling
   - 6.8 KTO — Kahneman-Tversky Optimization
   - 6.9 Pretraining
7. Dataset Formats
   - 7.1 Alpaca Format (Instruction Finetuning)
   - 7.2 ShareGPT Format (Chat Finetuning)
   - 7.3 DPO Format (Preference Training)
8. WebUI (LlamaBoard) — Step-by-Step Guide
9. CLI — Command Line Interface Reference
10. YAML Configuration — Complete Parameter Reference
    - 10.1 Hub & Model Parameters
    - 10.2 Finetuning Method
    - 10.3 Quantization Parameters
    - 10.4 RoPE Scaling (Context Extension)
    - 10.5 Speed Enhancers
    - 10.6 Training Stage
    - 10.7 Core Training Parameters
    - 10.8 Extra Configurations
    - 10.9 Freeze Tuning Parameters
    - 10.10 LoRA Configurations
    - 10.11 RLHF Configurations
    - 10.12 Multimodal Configurations
    - 10.13 GaLore (Gradient Memory Optimization)
    - 10.14 APOLLO Optimizer
    - 10.15 BAdam Optimizer
    - 10.16 SwanLab (Experiment Tracking)
    - 10.17 Output & Device Parameters
11. Epochs vs Logging Steps — Deep Explanation
12. Working Example — Gemma + Unix Commands Dataset
    - 12.1 Dataset Preparation
    - 12.2 WebUI Training Walkthrough
    - 12.3 CLI Training with YAML
    - 12.4 Inference with PeftModel
13. Decision Guide — Which Training Method to Use?
14. Common Errors & Fixes
15. Comparison Tables
16. Quick Reference Cheat Sheet

---

# 1. What is LLaMA Factory?

**Definition:**
> LLaMA Factory is an **all-in-one LLM fine-tuning framework** that lets you fine-tune large language models (LLMs) WITHOUT writing code — using either a WebUI or a command-line interface.

OR more simply:
> LLaMA Factory is the **"one-click fine-tuning platform"** for LLMs. Whether you want LoRA, QLoRA, Full Fine-Tuning, DPO, PPO, or Reward Models — everything is available from a single interface.

## What Makes It Special?

```
Traditional fine-tuning workflow:
  → Install HuggingFace Transformers
  → Install PEFT
  → Install BitsAndBytes
  → Install TRL
  → Write training scripts
  → Debug dataset loading
  → Debug YAML configs
  → Debug GPU memory errors
  Total: Hours or days of setup

LLaMA Factory workflow:
  → pip install llamafactory
  → llamafactory-cli webui
  → Select model, dataset, click Train!
  Total: Minutes
```

## Two Interfaces

| Interface | Type | Best For |
|---|---|---|
| **LlamaBoard / WebUI** | Browser-based GUI | Beginners, visual workflow, quick experiments |
| **CLI** | Terminal commands + YAML | Automation, scripting, production pipelines |

## Core Philosophy

LLaMA Factory follows the principle of **"wrapping complexity, exposing simplicity"**:
- Internally uses: **Transformers + PEFT + BitsAndBytes + TRL**
- Externally shows: Simple dropdowns, sliders, and config files

---

# 2. Why Use LLaMA Factory?

| Problem | LLaMA Factory Solution |
|---|---|
| Fine-tuning requires expert knowledge | WebUI makes it accessible to beginners |
| Too many libraries to install/configure | One install wraps everything |
| Different fine-tuning methods need different code | All methods in one platform |
| YAML config is complex | GUI generates config for you |
| RLHF pipeline is hard to set up | PPO + Reward Model in one place |
| Hard to track experiments | SwanLab / WandB integration built-in |
| Multi-GPU training setup is painful | DeepSpeed integrated directly |

## Engineer's Summary

```
If you want to fine-tune LLMs:
  → Research/Prototyping   → Use WebUI (fast iteration)
  → Production/Automation  → Use CLI + YAML config
  → Both paths go through LLaMA Factory internals (same engine)
```

## Supported Training Ecosystem

```
LLaMA Factory
├── Fine-Tuning Methods
│   ├── LoRA (Low-Rank Adapters)
│   ├── QLoRA (4-bit Quantized LoRA)
│   ├── Full Fine-Tuning
│   ├── Freeze Tuning
│   └── OFT (Orthogonal Fine-Tuning)
│
├── Training Stages
│   ├── SFT (Supervised Fine-Tuning)
│   ├── Reward Modeling (RLHF Step 1)
│   ├── PPO (RLHF Step 2)
│   ├── DPO (Direct Preference Optimization)
│   ├── KTO (Kahneman-Tversky Optimization)
│   └── Pretraining (Next-token prediction)
│
├── Features
│   ├── Flash Attention
│   ├── GaLore (Gradient compression)
│   ├── DeepSpeed (Multi-GPU)
│   ├── Unsloth (Ultra-fast training)
│   ├── SwanLab / WandB / TensorBoard
│   └── OpenAI-compatible API server
│
└── Export
    ├── Merge LoRA + Base Model
    ├── Export as .safetensors
    └── Quantize to 4-bit/8-bit for deployment
```

---

# 3. Architecture — How LLaMA Factory Works Internally

## Layered Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER LAYER                           │
│         WebUI (LlamaBoard) ←→ CLI (llamafactory-cli)   │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────┐
│                 LLAMA FACTORY CORE                       │
│   Config Parser → Trainer → Dataset Loader → Exporter  │
└───────┬───────────┬──────────┬───────────────┬──────────┘
        │           │          │               │
   ┌────▼────┐ ┌───▼────┐ ┌───▼────┐   ┌─────▼──────┐
   │Transfor-│ │  PEFT  │ │ Bits & │   │   TRL      │
   │ mers    │ │(LoRA,  │ │ Bytes  │   │(DPO, PPO,  │
   │(Model   │ │ DoRA,  │ │(4-bit, │   │ Reward     │
   │ loading)│ │ PiSSA) │ │ 8-bit) │   │ Model)     │
   └─────────┘ └────────┘ └────────┘   └────────────┘
                        │
              ┌─────────▼──────────┐
              │    GPU / CPU       │
              │  (CUDA / Metal /   │
              │   CPU inference)   │
              └────────────────────┘
```

## Data Flow During Training

```
1. User selects model → LF loads weights via Transformers
2. User selects method → LF applies PEFT / BnB wrapping
3. User loads dataset → LF processes into tokenized format
4. User clicks Train  → LF calls Trainer.train()
5. Training finishes  → Adapter weights saved to output_dir
6. Export button      → LF merges adapter + base → final model
```

---

# 4. Installation & Setup

## pip Installation

```bash
# Basic install
pip install llamafactory

# With all optional dependencies
pip install llamafactory[torch,metrics]

# For QLoRA support (BitsAndBytes)
pip install bitsandbytes

# For Flash Attention (faster training)
pip install flash-attn --no-build-isolation

# For Unsloth (ultra-fast)
pip install unsloth
```

## From Source (Recommended for development)

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

## Launch WebUI

```bash
llamafactory-cli webui
# → Opens in browser at http://localhost:7860
```

## Verify Installation

```bash
llamafactory-cli version
# → LLaMA Factory 0.x.x
```

---

# 5. Supported Models

LLaMA Factory supports a wide range of modern LLMs. Here is the complete family breakdown:

## Model Families

| Family | Developer | Examples |
|---|---|---|
| **LLaMA** | Meta | LLaMA, LLaMA-2, LLaMA-3 (7B, 8B, 13B, 70B) |
| **Mistral** | Mistral AI | Mistral-7B, Mixtral-8x7B (MoE) |
| **Qwen** | Alibaba | Qwen-1, Qwen-2, Qwen-VL, Qwen-Coder |
| **Gemma** | Google | Gemma-2B, Gemma-7B, Gemma-1.1-2b-it |
| **Yi** | 01.AI | Yi-6B, Yi-34B |
| **Phi** | Microsoft | Phi-2, Phi-3-mini, Phi-3-medium |
| **Baichuan** | Baichuan Inc | Baichuan-7B, Baichuan-13B |
| **ChatGLM** | Tsinghua/Zhipu AI | ChatGLM-2, ChatGLM-3, GLM-4 |
| **DeepSeek** | DeepSeek AI | DeepSeek-7B, DeepSeek-Coder |
| **OpenBuddy** | OpenBuddy Team | OpenBuddy-LLaMA variants |

## Template System

Each model family has a **chat template** that defines how prompts are formatted:

```
model: meta-llama/Meta-Llama-3-8B-Instruct → template: llama3
model: google/gemma-1.1-2b-it              → template: gemma
model: mistralai/Mistral-7B-Instruct-v0.2  → template: mistral
model: Qwen/Qwen2-7B-Instruct              → template: qwen
```

The template defines special tokens like `<|user|>`, `<|assistant|>`, `<s>`, `[INST]`, etc., which are critical for instruction fine-tuning.

---

# 6. Training Methods & Stages

## Overview Diagram

```
TRAINING METHODS (HOW weights are updated):
├── LoRA      → Train small adapter matrices only
├── QLoRA     → LoRA on 4-bit quantized base model
├── Full      → Train ALL weights
├── Freeze    → Freeze some layers, train the rest
└── OFT       → Orthogonal Fine-Tuning (LoRA alternative)

TRAINING STAGES (WHAT objective is optimized):
├── SFT              → Learn from instruction-output pairs
├── Pretraining      → Learn next-token prediction from raw text
├── Reward Modeling  → Learn to score good vs bad responses
├── PPO              → RLHF alignment using reward model
├── DPO              → Preference alignment (no reward model)
└── KTO              → Improved preference alignment
```

## 6.1 SFT — Supervised Fine-Tuning

**Definition:**
> Train the model to follow instructions by showing it instruction→output pairs.

**How it works:**
```
Input: [System prompt] + [User instruction] + [Input context]
Target: [Expected output / response]

Loss: Cross-entropy on output tokens ONLY
      (prompt tokens are masked by default in LLaMA Factory)
```

**Analogy:**
```
Teaching a student by giving them:
  → Question: "What is the capital of France?"
  → Answer:   "Paris"
  → The student memorizes correct question-answer patterns
  → SFT = showing the model thousands of such Q&A pairs
```

**When to use:**
- Teaching a base model to follow instructions
- Adapting a model to a new domain (medical, legal, coding)
- Most common and practical fine-tuning task

## 6.2 LoRA — Low-Rank Adaptation

**Definition:**
> Instead of updating ALL model weights (billions of parameters), LoRA adds small **adapter matrices** to specific layers. Only these adapters are trained.

**Mathematical Intuition:**
```
Original layer weight: W  (large matrix, e.g., 4096 × 4096)

LoRA decomposes the weight UPDATE into two small matrices:
  ΔW = A × B
  where:
    A = [d × r]  (d = original dimension, r = LoRA rank, e.g., 64)
    B = [r × k]  (k = output dimension)

  Instead of updating W (4096×4096 = 16M params)
  We update A+B (4096×64 + 64×4096 = 524K params — 30x smaller!)
```

**Analogy:**
```
Original model = A massive textbook (1000 pages)
LoRA adapter   = A sticky-note booklet (10 pages)

You only write new knowledge on sticky notes.
At inference, you read textbook + sticky notes together.
Final result = Full textbook understanding + new domain knowledge
```

**LoRA Key Parameters:**

| Parameter | What it Controls | Effect |
|---|---|---|
| `lora_r` (rank) | Size of adapter matrices | Higher r = more capacity, more VRAM |
| `lora_alpha` | Scale factor for LoRA update | Higher = stronger LoRA influence |
| `lora_dropout` | Regularization on adapters | Prevents overfitting |
| Target modules | Which layers get LoRA | Usually q_proj, v_proj, k_proj |

**Typical Values:**
```yaml
lora_r: 16          # Small and fast
lora_r: 64          # Standard (good balance)
lora_r: 128         # Large (high capacity, more VRAM)

lora_alpha: 16      # Usually = lora_r or half of it
lora_dropout: 0.05  # Standard regularization
```

## 6.3 QLoRA — Quantized LoRA

**Definition:**
> QLoRA = LoRA applied on top of a **4-bit quantized base model**. The base model is frozen and quantized (to save VRAM), and only the LoRA adapters are trained in full precision.

**Memory savings example:**
```
LLaMA-3 8B model:
  Full FP16 training: ~16 GB VRAM
  LoRA (FP16 base):   ~14 GB VRAM
  QLoRA (4-bit base): ~6-8 GB VRAM  ← Fits on a single GPU!
```

**How QLoRA Works:**
```
Step 1: Load base model in 4-bit (using BitsAndBytes NF4)
Step 2: Freeze all base model weights (they stay 4-bit)
Step 3: Add LoRA adapters in FP16/BF16
Step 4: Train ONLY the LoRA adapters
Step 5: At inference: base model (4-bit) + adapters (FP16)
```

**QLoRA vs LoRA:**

| Feature | LoRA | QLoRA |
|---|---|---|
| Base model precision | FP16 / BF16 | INT4 (NF4) |
| VRAM required | ~14 GB (7B model) | ~6 GB (7B model) |
| Training speed | Faster | Slightly slower |
| Accuracy | Higher | Slightly lower (quantization noise) |
| Best for | Good GPU (A100, RTX 3090+) | Limited VRAM (RTX 3060, Colab T4) |

**Enable QLoRA in config:**
```yaml
quantization_bit: 4     # Enable 4-bit quantization of base model
quantization_method: bnb # Use BitsAndBytes
finetuning_type: lora    # Still LoRA, but on quantized base
```

## 6.4 Full Fine-Tuning

**Definition:**
> ALL weights of the model are updated during training. No freezing, no adapters.

```
What gets trained:
  ✅ Attention (Q, K, V, O projections)
  ✅ Feed-Forward Network (up, gate, down projections)
  ✅ Layer Normalization
  ✅ Embeddings (input + output)
```

**When to use:**
- You have a LOT of GPU memory (multiple A100s or H100s)
- You need maximum accuracy
- Domain adaptation where the model needs deep structural changes

**VRAM requirements:**
```
7B  model Full FT → ~28-56 GB VRAM (depending on optimizer)
13B model Full FT → ~52-100 GB VRAM
70B model Full FT → Requires 4-8 × A100 80GB
```

## 6.5 DPO — Direct Preference Optimization

**Definition:**
> DPO trains the model on **chosen vs rejected** response pairs to align model behavior with human preferences — WITHOUT needing a separate reward model.

**Training data format:**
```json
{
  "prompt": "Explain what photosynthesis is.",
  "chosen": "Photosynthesis is the process by which plants use sunlight to convert CO₂ and water into glucose and oxygen.",
  "rejected": "I don't really know, plants do something with light I think."
}
```

**DPO vs PPO:**
```
PPO (full RLHF):
  Step 1: Train Reward Model (separate model)
  Step 2: Use reward model to score outputs
  Step 3: Train policy with PPO using reward signals
  → Complex, 2-model pipeline, hard to tune

DPO:
  Step 1: Just provide chosen/rejected pairs
  Step 2: DPO loss directly optimizes preference
  → Simple, 1-model pipeline, stable
```

## 6.6 PPO — Proximal Policy Optimization (RLHF)

**Definition:**
> PPO is the reinforcement learning step of RLHF (Reinforcement Learning from Human Feedback). A reward model scores the LLM's outputs, and PPO updates the LLM to maximize that reward.

**Full RLHF Pipeline:**
```
Step 1: Supervised Fine-Tuning (SFT)
           → Train base model on instructions

Step 2: Reward Model Training
           → Train separate model to score responses
           → Input: (prompt + response)
           → Output: scalar reward score

Step 3: PPO Fine-Tuning
           → Generate responses
           → Score with reward model
           → Update LLM to produce higher-scoring responses
           → KL divergence penalty prevents model from drifting too far
```

**This is how ChatGPT-style alignment works!**

## 6.7 Reward Modeling

**Definition:**
> Train a model that learns to assign a **numeric quality score** to a (prompt, response) pair. This is the first step of full RLHF.

**Data needed:** Same chosen/rejected pairs as DPO.
**Output:** A model that outputs a scalar score (e.g., 8.5 / 10).

## 6.8 KTO — Kahneman-Tversky Optimization

**Definition:**
> KTO is an improved variant of DPO. Based on Kahneman-Tversky prospect theory from economics/psychology.

**Advantages over DPO:**
- Works well with **low-data** preference training
- More stable training signal
- Does NOT strictly require paired (chosen, rejected) examples

## 6.9 Pretraining

**Definition:**
> Train on raw text to predict the next token. This is how foundation models are trained originally.

**Use case in LLaMA Factory:**
- Continue pretraining on domain-specific text (medical papers, code repositories)
- Teach new vocabulary or language
- NOT instruction following — just token-level prediction

---

# 7. Dataset Formats

LLaMA Factory supports three main dataset formats. You must choose the right one based on your training task.

## 7.1 Alpaca Format (Instruction Fine-Tuning)

**Best for:** SFT, standard instruction-following tasks

**Structure:**
```json
[
  {
    "instruction": "What is preference alignment in LLMs?",
    "input": "",
    "output": "Preference alignment is the process of training LLMs to follow human preferences and values, typically using RLHF or DPO techniques."
  },
  {
    "instruction": "Translate the following to French.",
    "input": "Hello, how are you?",
    "output": "Bonjour, comment allez-vous?"
  }
]
```

**Column breakdown:**

| Column | Required? | Description |
|---|---|---|
| `instruction` | ✅ Yes | The task or question for the model |
| `input` | ⚪ Optional | Additional context or input text |
| `output` | ✅ Yes | The expected/target response |

**How LLaMA Factory processes it:**
```
Alpaca → Constructs prompt:
  "Below is an instruction that describes a task...
   ### Instruction: {instruction}
   ### Input: {input}
   ### Response: {output}"

Loss is calculated ONLY on the response tokens.
```

## 7.2 ShareGPT Format (Chat Fine-Tuning)

**Best for:** Multi-turn conversation fine-tuning

**Structure:**
```json
[
  {
    "conversations": [
      {"from": "user",      "value": "Hello! Can you help me with Python?"},
      {"from": "assistant", "value": "Of course! I'd be happy to help. What Python question do you have?"},
      {"from": "user",      "value": "How do I read a CSV file?"},
      {"from": "assistant", "value": "You can read a CSV file using pandas: `pd.read_csv('file.csv')` or using the built-in csv module."}
    ]
  }
]
```

**Column breakdown:**

| Field | Role |
|---|---|
| `conversations` | Array of conversation turns |
| `from` | Speaker identifier: `"user"` or `"assistant"` |
| `value` | The text content of that turn |

**Advantages:**
- Handles multi-turn chat naturally
- Masking option available for conversation history
- Closest to how ChatGPT-style models are trained

## 7.3 DPO Format (Preference Training)

**Best for:** DPO, KTO, Reward Model training

**Structure:**
```json
[
  {
    "prompt": "Explain the concept of RLHF.",
    "chosen": "RLHF stands for Reinforcement Learning from Human Feedback. It involves training a reward model on human preference data, then using it to fine-tune an LLM via PPO. This process aligns the model's outputs with human values.",
    "rejected": "RLHF is some kind of training thing. I'm not sure how it works exactly."
  }
]
```

**Column breakdown:**

| Column | Description |
|---|---|
| `prompt` | The input question or task |
| `chosen` | The preferred, high-quality response |
| `rejected` | The lower-quality or unwanted response |

**Decision Table — Which Format to Use?**

| Task | Format | Stage in LF |
|---|---|---|
| Instruction fine-tuning | Alpaca | SFT |
| Chat / Conversation fine-tuning | ShareGPT | SFT |
| Preference alignment (no reward model) | DPO | DPO |
| Training a reward model | DPO (chosen/rejected) | Reward Modeling |
| Full RLHF pipeline | DPO first, then RLHF | Reward Model → PPO |
| Pretraining on raw text | Plain text file | Pretraining |

---

# 8. WebUI (LlamaBoard) — Step-by-Step Guide

The WebUI is launched with:
```bash
llamafactory-cli webui
# Opens at: http://localhost:7860
```

## 8-Step WebUI Workflow

### Step 1: Base Model Select

```
Top section of WebUI:
  → Hub Name: huggingface / modelscope / openmind
  → Model name/path: meta-llama/Meta-Llama-3-8B-Instruct
  → Template: llama3 (auto-detected or manual)
  → Finetuning type: LoRA / Full / Freeze
  → Checkpoint path: (optional) load existing adapter
```

**Hub Name explained:**
- `huggingface` → Download from HuggingFace Hub (default, global)
- `modelscope` → Download from ModelScope (faster for users in China)
- `openmind` → Load from local folder / offline models

### Step 2: Dataset Load

```
Dataset section:
  → Dataset: select from list (e.g., alpaca_en, custom)
  → Dataset format: alpaca / sharegpt
  → Preview button: see first few examples
  → Max samples: limit dataset size for quick runs
  → Val size (%): reserve for validation
```

**Adding a custom dataset:**
1. Place your `train.json` in `LLaMA-Factory/data/` folder
2. Register it in `LLaMA-Factory/data/dataset_info.json`:
```json
{
  "my_custom_dataset": {
    "file_name": "train.json",
    "columns": {
      "prompt": "instruction",
      "response": "output"
    }
  }
}
```

### Step 3: Training Configuration

```
Training Parameters section:
  → Stage: SFT / Reward Model / PPO / DPO / KTO / Pretraining
  → Learning rate: 2e-4 (typical for LoRA)
  → Epochs: 3 (typical)
  → Max length (cutoff_len): 1024
  → Batch size (per device): 1 or 2
  → Gradient accumulation steps: 8
  → LR Scheduler: cosine
  → Warmup ratio: 0.03
```

### Step 4: GPU Optimization

```
GPU optimization section:
  → Compute type: bf16 / fp16
  → Quantization bit: 4 / 8 / none
  → Flash attention: enable (if compatible GPU)
  → Gradient checkpointing: enable (saves VRAM)
  → Unsloth: enable for Colab/laptop
```

### Step 5: Start Training

```
Final section:
  → Output dir: output/my_model
  → Click "Start" button
  → Loss curve appears in real-time
  → Training logs shown below
```

### Step 6: Evaluation

```
After training:
  → Switch to "Evaluate" tab
  → Load checkpoint
  → Run on validation set
  → View BLEU, Rouge, or Perplexity metrics
```

### Step 7: Chat With Your Model

```
Inference / Chat tab:
  → Load your trained checkpoint
  → Type a message
  → See real-time response from your fine-tuned model
  → Compare base model vs fine-tuned model
```

### Step 8: Export Model

```
Export tab:
  → Export dir: path/to/exported_model
  → Options: merge LoRA into base model
  → Quantize to 4-bit or 8-bit
  → Click Export
  → Saved as .safetensors files (HF compatible)
```

---

# 9. CLI — Command Line Interface Reference

The CLI provides full control without the WebUI. All training is driven by YAML config files.

## Complete CLI Commands

| Command | What it Does |
|---|---|
| `llamafactory-cli train config.yaml` | Run training (SFT, LoRA, QLoRA, Full FT, DPO, PPO) |
| `llamafactory-cli chat config.yaml` | Interactive CLI chat with trained model |
| `llamafactory-cli eval config.yaml` | Run evaluation on validation dataset |
| `llamafactory-cli export config.yaml` | Merge LoRA adapters and export final model |
| `llamafactory-cli api config_api.yaml` | Launch OpenAI-compatible API server |
| `llamafactory-cli webui` | Launch browser-based WebUI |
| `llamafactory-cli webchat` | Launch web-based chat interface |
| `llamafactory-cli version` | Show installed version |

## CLI Training Examples

```bash
# SFT with LoRA
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml

# DPO training
llamafactory-cli train examples/train_lora/llama3_lora_dpo.yaml

# Full fine-tuning (multi-GPU with DeepSpeed)
FORCE_TORCHRUN=1 llamafactory-cli train examples/train_full/llama3_full_sft_ds3.yaml

# Export merged model
llamafactory-cli export examples/merge_lora/llama3_lora_sft.yaml

# API server
llamafactory-cli api examples/inference/llama3.yaml
```

## API Server Usage

After launching with `llamafactory-cli api`, you get an **OpenAI-compatible endpoint**:

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="your-api-key"
)

response = client.chat.completions.create(
    model="your-model",
    messages=[{"role": "user", "content": "Explain LLaMA Factory"}]
)
print(response.choices[0].message.content)
```

---

# 10. YAML Configuration — Complete Parameter Reference

The YAML config file is the heart of LLaMA Factory's CLI workflow. Every parameter is documented below.

## Complete QLoRA Config Example

```yaml
### Model
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct
template: llama3

### Method
finetuning_type: lora
stage: sft

### Dataset
dataset: custom
dataset_format: alpaca
train_file: data/train.json
cutoff_len: 1024

### Training
output_dir: output/llama3-qlora
per_device_train_batch_size: 1
gradient_accumulation_steps: 8
num_train_epochs: 3
learning_rate: 2.0e-4
lr_scheduler_type: cosine
warmup_ratio: 0.03

### LoRA
lora_r: 64
lora_alpha: 16
lora_dropout: 0.05

### QLoRA
quantization_bit: 4
quantization_method: bnb

### Compute
bf16: true
gradient_checkpointing: true
flash_attn: auto

### Logging
report_to: none
logging_steps: 10
save_steps: 100
```

---

## 10.1 Hub & Model Parameters

### Hub Name (Model Download Source)

```yaml
hub_name: huggingface   # Default
```

| Value | Source | Use Case |
|---|---|---|
| `huggingface` | HuggingFace Hub | Default for global users |
| `modelscope` | ModelScope Hub | Chinese users, Chinese models |
| `openmind` | Local/Offline | Air-gapped machines, local NAS |

### Model Parameters

```yaml
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct
# Can be:
#   → HuggingFace model ID: "meta-llama/Meta-Llama-3-8B-Instruct"
#   → Local directory path: "/models/llama3-8b"

template: llama3
# Template defines prompt format for each model
# Options: llama3, gemma, mistral, qwen, chatglm4, phi, baichuan, etc.
```

---

## 10.2 Finetuning Method

```yaml
finetuning_type: lora   # Most common choice
```

| Value | Description | VRAM Need | Accuracy |
|---|---|---|---|
| `lora` | LoRA adapters only | Low | Good |
| `full` | All weights train | Very High | Best |
| `freeze` | Freeze most, train last N layers | Medium | Medium |
| `oft` | Orthogonal Fine-Tuning (LoRA alternative) | Low | Good |

**When to choose:**

```
VRAM < 16 GB   → lora (or QLoRA with quantization_bit: 4)
VRAM 16-40 GB  → lora (full precision)
VRAM 40-80 GB  → full or freeze
Multi-GPU      → full with DeepSpeed
Research       → oft (for stability experiments)
```

---

## 10.3 Quantization Parameters

### Quantization Bit

```yaml
quantization_bit: 4     # 4-bit quantization (QLoRA)
# Options: none, 8, 4
```

| Value | Precision | VRAM Savings | Accuracy Impact |
|---|---|---|---|
| `none` | Full (FP16/BF16) | 0% | None — best accuracy |
| `8` | 8-bit INT | ~50% | Very minimal |
| `4` | 4-bit NF4 | ~75% | Small (typically <1%) |

### Quantization Method

```yaml
quantization_method: bnb   # Recommended default
```

| Value | Full Name | Stability | Speed | Notes |
|---|---|---|---|---|
| `bnb` | BitsAndBytes | High | Fast | Most stable, universally supported |
| `hqq` | High Quality Quantization | High | Medium | Better accuracy than bnb, slightly heavier |
| `etqq` | Experimental TQ Quantization | Low | Fast | Experimental, not stable for all models |

---

## 10.4 RoPE Scaling (Context Window Extension)

RoPE (Rotary Position Embedding) scaling extends the model's maximum context window.

```yaml
rope_scaling: yarn   # Recommended for context extension
```

| Value | Method | Use Case |
|---|---|---|
| `none` | No scaling | Use original context length |
| `linear` | Linear position scaling | Basic long-context extension |
| `dynamic` | NTK-by-parts scaling | More stable long-context |
| `yarn` | Yet Another RoPE Extension | SOTA — best for 8K→32K→128K |
| `llama3` | LLaMA-3 specific | Use ONLY with LLaMA-3 models |

**Context extension example:**
```yaml
# Extend LLaMA-3 8B from 8K to 32K context:
rope_scaling: yarn
model_max_length: 32768
```

**Analogy:**
```
Original context = A ruler that measures up to 30cm
RoPE scaling     = Extending that ruler to 1 meter
  linear scaling → stretch uniformly (may lose fine detail)
  yarn scaling   → smart extension (maintains accuracy at all lengths)
```

---

## 10.5 Speed Enhancers

```yaml
flash_attn: auto   # Recommended
```

| Value | Description | Speed Gain | VRAM Savings | Notes |
|---|---|---|---|---|
| `auto` | LF picks fastest available | Best | Yes | Recommended default |
| `flash_attn` | FlashAttention-2 kernel | High | High | Needs compatible GPU (Ampere+) |
| `unsloth` | Unsloth optimization | Very High | Very High | Best for Colab/laptop (T4, RTX) |
| `liger_kernel` | Fused kernels (triton) | High | Medium | Stable, works across GPUs |

**When to use Unsloth:**
```
Limited VRAM (Colab free, RTX 3060 6GB, T4 15GB):
  → flash_attn: unsloth
  → Reported: 2x faster, 50% less VRAM vs vanilla training
```

**When to use FlashAttention-2:**
```
Modern GPUs (A100, H100, RTX 4090, RTX 3090):
  → flash_attn: flash_attn
  → Or just: flash_attn: auto  (LF will pick it automatically)
```

---

## 10.6 Training Stage

```yaml
stage: sft   # Most common
```

| Value | Full Name | Input Format | Use Case |
|---|---|---|---|
| `sft` | Supervised Fine-Tuning | Instruction + Output | General fine-tuning, most common |
| `rm` | Reward Modeling | Chosen + Rejected | RLHF step 1 |
| `ppo` | Proximal Policy Optimization | Prompts only | RLHF step 2 (needs reward model) |
| `dpo` | Direct Preference Optimization | Chosen + Rejected | Preference alignment, simpler than PPO |
| `kto` | Kahneman-Tversky Optimization | Chosen + Rejected | Stable DPO alternative |
| `pt` | Pretraining | Raw text | Continue pretraining |

---

## 10.7 Core Training Parameters

### Learning Rate

```yaml
learning_rate: 2.0e-4   # For LoRA
# For Full FT: 1e-5 to 5e-5 (lower, to avoid catastrophic forgetting)
```

| Setting | Value | When to Use |
|---|---|---|
| LoRA / QLoRA | `2e-4` to `5e-4` | Standard LoRA training |
| Full Fine-Tune | `1e-5` to `5e-5` | All weights training |
| DPO | `5e-7` to `1e-6` | Preference alignment (very low!) |

### Epochs

```yaml
num_train_epochs: 3
```

**What is an epoch?**
> One complete pass through the entire training dataset.

```
Example:
  Dataset = 1000 samples
  batch_size = 100
  → 1 epoch = 10 training steps

  num_train_epochs: 3
  → 3 epochs = 30 total training steps
  → Model sees every example 3 times
```

**Recommended epochs by scenario:**

| Scenario | Epochs |
|---|---|
| Large dataset (50K+ samples) | 1-2 |
| Medium dataset (5K-50K) | 2-5 |
| Small dataset (<5K) | 5-10 |
| Overfitting observed | Reduce epochs |
| Loss still decreasing at end | Add epochs |

### Max Length (cutoff_len)

```yaml
cutoff_len: 1024
# Options: 512, 1024, 2048, 4096, 8192
```

**Effect of cutoff_len:**
```
Lower cutoff (512):
  → Faster training (less computation per sample)
  → Sequences longer than 512 are TRUNCATED
  → Risk: lose context for long documents

Higher cutoff (4096):
  → More computation per step
  → Full context preserved for longer texts
  → More VRAM needed
```

### Batch Size & Gradient Accumulation

```yaml
per_device_train_batch_size: 1
gradient_accumulation_steps: 8
# Effective batch size = 1 × 8 = 8
```

**Why gradient accumulation?**
```
Limited VRAM prevents large batches.

Without accumulation:
  batch_size = 1 → Too small → noisy gradients → slow learning

With accumulation:
  batch_size = 1, accumulation_steps = 8
  → Process 1 sample × 8 times → accumulate gradients → one update
  → Effective batch size = 8 (same quality!)
  → VRAM requirement of batch_size=1 (low!)
```

**Recommended combinations by VRAM:**

| Available VRAM | batch_size | accum_steps | Effective batch |
|---|---|---|---|
| 6 GB | 1 | 8 | 8 |
| 8 GB | 1 | 8 | 8 |
| 16 GB | 2 | 4 | 8 |
| 24 GB | 4 | 2 | 8 |
| 40 GB | 8 | 1 | 8 |

### LR Scheduler

```yaml
lr_scheduler_type: cosine   # Recommended
```

| Scheduler | Pattern | Use Case |
|---|---|---|
| `cosine` | Smooth decay following cosine curve | Most recommended — smooth, stable |
| `linear` | Linear decay to 0 | Simple, slightly less smooth |
| `constant` | No decay | When fine-tuning on small data |
| `cosine_with_restarts` | Cosine with periodic resets | For long training runs |

```
cosine scheduler visualized:
  LR
  ↑ 2e-4
  │ ╭─────╮
  │ │     ╰──────╮
  │ │             ╰────╮
  │ │                   ╰────→ near 0
  └────────────────────────→ Steps
```

### Warmup

```yaml
warmup_ratio: 0.03   # 3% of total training steps
# OR
warmup_steps: 100    # Fixed warmup steps
```

**Why warmup?**
```
Without warmup:
  LR starts at 2e-4 immediately
  → Large updates on randomly-initialized LoRA adapters
  → Model can become unstable at the start

With warmup:
  LR starts at ~0, gradually increases to 2e-4
  → Smooth start → stable training
  → Especially important for full fine-tuning
```

---

## 10.8 Extra Configurations

### Logging Steps

```yaml
logging_steps: 10
# Log training loss/metrics every 10 steps
```

**Understanding multiple log outputs:**
```
Dataset = 1000 samples, batch = 100 → 10 steps/epoch
Epochs = 3 → 30 total steps

logging_steps: 5 → prints 6 times (step 5, 10, 15, 20, 25, 30)
  Each print shows ONE loss value — this is NORMAL.
  Multiple losses ≠ multiple epochs!
```

### Save Steps

```yaml
save_steps: 100
# Save model checkpoint every 100 steps
```

### NEFTune Alpha

```yaml
neftune_alpha: 5.0   # Typical value: 0 (disabled) to 15
```

**What is NEFTune?**
> NEFTune adds **random noise** to input embeddings during training. This surprisingly improves generalization (model performs better on unseen data).

```
Without NEFTune: Model may memorize training examples
With NEFTune:    Model learns more robust patterns
                  → Better performance on held-out test data
Typical range: 5–15 (start with 5, tune if needed)
```

### Sequence Packing

```yaml
packing: true         # Enable sequence packing
neat_packing: true    # Enable clean boundary packing
```

**What is packing?**
```
Without packing:
  Example 1: "User: Hello. Assistant: Hi." → 20 tokens, padded to 1024 → 1004 WASTED tokens
  Example 2: "User: What is 2+2? Assistant: 4." → 15 tokens, padded to 1024 → 1009 WASTED tokens

With packing:
  Example 1 + Example 2 concatenated → 35 tokens → NO waste
  One GPU step processes 2 examples instead of 1 → ~50% throughput increase!
```

**Neat packing** ensures that attention doesn't cross example boundaries (no cross-contamination between packed examples).

### Train on Prompt

```yaml
train_on_prompt: false   # Default (recommended for SFT)
```

- `false` → Loss calculated ONLY on output tokens (standard SFT)
- `true` → Loss also calculated on instruction/prompt tokens (rarely needed)

### Mask History

```yaml
mask_history: true
```

In multi-turn ShareGPT format:
- `true` → Loss only on the LAST assistant turn
- `false` → Loss on ALL assistant turns

### Gradient Checkpointing

```yaml
gradient_checkpointing: true   # Enable to save VRAM
```

**Tradeoff:**
```
gradient_checkpointing: false
  → All activations kept in VRAM during forward pass
  → Faster backward pass
  → More VRAM needed

gradient_checkpointing: true
  → Activations recomputed during backward pass (trade compute for memory)
  → ~30-40% VRAM savings
  → ~20-30% slower training
  → HIGHLY recommended for low-VRAM setups!
```

### Enable External Logger

```yaml
report_to: wandb          # or: tensorboard, mlflow, swanlab, none
```

---

## 10.9 Freeze Tuning Parameters

```yaml
finetuning_type: freeze
freeze_trainable_layers: 2     # Train last 2 transformer blocks
freeze_trainable_modules: all  # Which modules within those layers
freeze_extra_modules: []       # Any additional specific modules
```

| Parameter | Description |
|---|---|
| `freeze_trainable_layers` | Number of final layers to train (others frozen) |
| `freeze_trainable_modules` | Within trainable layers: `all`, `q_proj`, `v_proj`, etc. |
| `freeze_extra_modules` | Modules in frozen layers to still train (e.g., `lm_head`) |

**Analogy:**
```
Freeze tuning = Teaching a student who already knows the subject
  → Freeze early chapters (already learned, don't change)
  → Only re-train the last chapters (new material or corrections)
  → Medium VRAM, medium accuracy
```

---

## 10.10 LoRA Configurations

```yaml
lora_r: 64               # LoRA rank — adapter matrix dimension
lora_alpha: 16           # Scaling factor for LoRA updates
lora_dropout: 0.05       # Dropout on LoRA layers (regularization)
lora_target: all         # Which modules get LoRA (or: q_proj,v_proj)
loraplus_lr_ratio: 16.0  # B matrix LR = this × base LR
create_new_adapter: false # Create a fresh adapter (don't load existing)
use_rslora: false         # Rank-stabilized LoRA
use_dora: false           # Weight-decomposed LoRA
use_pissa: false          # PiSSA (principal singular values) LoRA
```

### LoRA Rank (r) Explained

| Rank | Parameters | Quality | VRAM | Use Case |
|---|---|---|---|---|
| `r=8` | Minimal | Basic | Very low | Quick testing |
| `r=16` | Low | Good | Low | Small datasets, fast |
| `r=64` | Medium | Better | Medium | Standard — recommended |
| `r=128` | High | Best | High | Large datasets, max quality |

**Formula for parameter count:**
```
For a weight matrix W of shape [d_in × d_out]:
  LoRA parameters = r × (d_in + d_out)

  Example: LLaMA-3 8B q_proj = [4096 × 4096]
  With r=64:
    A = [4096 × 64] = 262,144 params
    B = [64 × 4096]  = 262,144 params
    Total = 524,288 params per layer
    (vs 16,777,216 for the full weight — 32x smaller!)
```

### LoRA Alpha Explained

```
lora_alpha controls the SCALE of the LoRA update:
  Effective update = (lora_alpha / lora_r) × ΔW

  lora_r = 64, lora_alpha = 16:
    scale = 16/64 = 0.25 (small, conservative update)

  lora_r = 64, lora_alpha = 64:
    scale = 64/64 = 1.0 (full update)

  lora_r = 64, lora_alpha = 128:
    scale = 128/64 = 2.0 (aggressive update)

Rule of thumb:
  lora_alpha = lora_r    → balanced
  lora_alpha = lora_r/4  → conservative (stable, less change)
```

### Advanced LoRA Variants

**DoRA (Weight-Decomposed LoRA):**
```yaml
use_dora: true
# Decomposes weight into magnitude + direction
# Updates them separately → more expressive than LoRA
# Better quality, slightly more VRAM
```

**PiSSA (Principal Singular Values and Singular Vectors Adaptation):**
```yaml
use_pissa: true
# Initializes LoRA from principal components of original weights
# Better starting point → faster convergence
```

**rsLoRA (Rank-Stabilized LoRA):**
```yaml
use_rslora: true
# Scales alpha by sqrt(r) instead of r
# More stable training at high ranks
```

---

## 10.11 RLHF Configurations

```yaml
# For DPO / KTO
beta: 0.1              # DPO loss temperature
ftx_gamma: 0.0         # Weight of SFT loss in combined loss
dpo_loss: sigmoid      # DPO loss shape
ref_model: ""          # Reference model path (for DPO)

# For PPO
reward_model: ""       # Path to reward model
reward_model_type: lora
score_norm: false      # Normalize reward scores
whiten_rewards: false  # Remove mean, normalize variance
```

### Beta Value in DPO

```
beta controls how strongly the model is pushed toward preferred outputs:
  Low beta (0.1):  Gentle push, model stays close to SFT behavior
  High beta (1.0): Strong push, model drastically changes output style

Typical range: 0.1 – 0.5
  Lower = more stable, less alignment
  Higher = more alignment, may become unstable
```

### DPO Loss Types

| Loss Type | Behavior |
|---|---|
| `sigmoid` | Standard DPO loss (original paper) — most stable |
| `margin` | Margin-based — requires explicit margin parameter |
| `hinge` | Hinge loss — zero gradient when margin satisfied |

---

## 10.12 Multimodal Configurations

LLaMA Factory also supports vision-language models (Qwen-VL, LLaVA, etc.):

```yaml
freeze_vision_tower: true           # Freeze image encoder (train only language)
freeze_multi_modal_projector: false # Train vision→text mapping (projector)
freeze_language_model: false        # Freeze LLM, train only projector

image_resolution: 512   # Image size fed to vision encoder
video_fps: 1            # Video frame extraction rate
image_max_pixels: 1003520
image_min_pixels: 3136
```

**Training strategies for multimodal:**

| Strategy | Freeze Vision | Freeze Projector | Freeze LLM | Use Case |
|---|---|---|---|---|
| Language only | ✅ | ✅ | ❌ | Cheapest — only update LLM weights |
| Full multimodal | ❌ | ❌ | ❌ | Max accuracy — train everything |
| Projector tuning | ✅ | ❌ | ✅ | Mid approach — learn vision→text mapping |

---

## 10.13 GaLore (Gradient Memory Optimization)

GaLore = **Gradient Low-Rank Projection**. Saves VRAM by projecting gradients to a low-rank space before accumulation.

```yaml
use_galore: true
galore_rank: 16          # Rank of gradient projection (lower = less VRAM)
galore_update_interval: 200  # Steps between updating projection
galore_scale: 0.25       # Scale of gradient updates
galore_proj_type: std    # Projection type: std or reverse_std
galore_layerwise: true   # Apply GaLore layer-by-layer
```

**GaLore vs LoRA:**
```
LoRA:   Adapts weights through low-rank structure
GaLore: Compresses GRADIENTS during full training

Use GaLore with finetuning_type: full
  → Gets you close to full FT accuracy
  → With much less VRAM than standard full FT

GaLore memory savings:
  Standard Full FT (13B): ~100+ GB
  GaLore Full FT (13B):   ~24-40 GB (on fewer GPUs!)
```

---

## 10.14 APOLLO Optimizer

APOLLO = Advanced Optimizer for Large Language Models. Better stability than Adam for large models.

```yaml
use_apollo: true
apollo_rank: 16
apollo_update_interval: 200
apollo_scale: 0.25
apollo_proj_type: std
```

**When to use:**
- Large models (13B+) where Adam is unstable
- Experiments with full fine-tuning at scale
- Research setting for stability experiments

---

## 10.15 BAdam Optimizer

BAdam = **Block-wise Adam**. Applies Adam optimization layer-by-layer rather than all at once.

```yaml
use_badam: true
badam_mode: layer          # Options: layer, ratio
badam_switch_mode: ascending   # Order: ascending, descending, random
badam_switch_interval: 50  # Steps between layer switches
badam_update_ratio: 0.05   # Fraction of layers updated per step (ratio mode)
```

**Analogy:**
```
Standard Adam: Updates ALL weights simultaneously (huge memory peak)

BAdam: Updates one block of layers at a time
       Layer 1 updated → Layer 2 updated → ... → Layer N updated
       Memory peak = memory for ONE block (much smaller!)
```

---

## 10.16 SwanLab (Experiment Tracking)

```yaml
use_swanlab: true
swanlab_project: my_llm_project
swanlab_experiment_name: llama3_qlora_v1
swanlab_workspace: my_team
swanlab_api_key: your-api-key
swanlab_mode: cloud         # Options: cloud, offline
```

**Comparison of tracking options:**

| Tool | Config value | Notes |
|---|---|---|
| None | `report_to: none` | No tracking |
| TensorBoard | `report_to: tensorboard` | Local, needs tensorboard server |
| WandB | `report_to: wandb` | Cloud, needs wandb account |
| MLflow | `report_to: mlflow` | Enterprise-grade tracking |
| SwanLab | `use_swanlab: true` | Chinese-friendly cloud tracking |

---

## 10.17 Output & Device Parameters

```yaml
output_dir: output/llama3-qlora    # Where model/checkpoints are saved
overwrite_output_dir: true         # Overwrite if directory exists

# Device settings
num_gpus: 1                        # Number of GPUs to use
deepspeed: ds_z2_config.json       # DeepSpeed config for multi-GPU

# DeepSpeed stages
# Stage 0: No partitioning (standard DataParallel)
# Stage 1: Partition optimizer states across GPUs
# Stage 2: Partition gradients + optimizer states (recommended)
# Stage 3: Partition model params + gradients + optimizer states
# Offload: Move optimizer states/parameters to CPU RAM

offload_optimizer: cpu             # Offload optimizer state to CPU
offload_param: cpu                 # Offload model params to CPU
```

**DeepSpeed Stage Guide:**

| Stage | What's Partitioned | VRAM Savings | Communication Overhead |
|---|---|---|---|
| Stage 0 | Nothing | None | None |
| Stage 1 | Optimizer states | Moderate | Low |
| Stage 2 | + Gradients | High | Medium |
| Stage 3 | + Model parameters | Very High | Higher |
| Stage 3 + Offload | + CPU RAM | Maximum | Highest |

---

# 11. Epochs vs Logging Steps — Deep Explanation

This is a common source of confusion for beginners. Let's clarify definitively.

## Epoch Definition

> **Epoch** = one complete pass through the entire training dataset.

```
Example:
  Dataset size  = 1000 samples
  batch_size    = 100 samples per step
  Steps per epoch = 1000 / 100 = 10 steps

  num_train_epochs = 3
  Total steps = 10 × 3 = 30 steps
```

## Logging Step Definition

> **Logging step** = frequency (in training steps) at which training metrics (loss, learning rate) are printed/logged.

```yaml
logging_steps: 5    # Print metrics every 5 training steps
```

## Complete Worked Example

```
Setup:
  Dataset = 1000 samples
  batch_size = 100
  gradient_accumulation = 1
  num_train_epochs = 3
  logging_steps = 5

Calculation:
  Steps per epoch = 1000 / 100 = 10 steps
  Total steps = 10 × 3 = 30 steps

  Logging happens at: step 5, 10, 15, 20, 25, 30
  Total log outputs = 30 / 5 = 6 log entries

Log output looks like:
  {'loss': 1.5234, 'epoch': 0.5, 'step': 5}   ← mid epoch 1
  {'loss': 1.3210, 'epoch': 1.0, 'step': 10}  ← end of epoch 1
  {'loss': 1.1498, 'epoch': 1.5, 'step': 15}  ← mid epoch 2
  {'loss': 0.9823, 'epoch': 2.0, 'step': 20}  ← end of epoch 2
  {'loss': 0.8567, 'epoch': 2.5, 'step': 25}  ← mid epoch 3
  {'loss': 0.7234, 'epoch': 3.0, 'step': 30}  ← end of epoch 3

⚠️ IMPORTANT: 6 loss outputs ≠ 6 epochs!
   Multiple losses = multiple LOG POINTS within 3 epochs
   This is NORMAL and expected!
```

## Common Beginner Mistake

```
❌ Wrong interpretation:
  "I see 30 loss values printed — so it trained for 30 epochs!"

✅ Correct interpretation:
  If logging_steps=1 and 30 total steps → 30 log entries, but still only 3 epochs!
  num_train_epochs is what controls epochs, not the number of log outputs.
```

## Loss Curve Interpretation

```
Good training curve:
  Epoch 1: Loss = 1.52 → 1.18 (large drop — fast learning)
  Epoch 2: Loss = 1.18 → 0.93 (moderate drop)
  Epoch 3: Loss = 0.93 → 0.81 (smaller drop — converging)

Warning signs:
  Loss not decreasing → LR too low, dataset problem, or already converged
  Loss increasing     → LR too high, overfitting, or data issue
  Loss oscillating    → LR too high, reduce it
  Loss = 0 or NaN    → Data error, LR too high, or gradient explosion
```

---

# 12. Working Example — Gemma + Unix Commands Dataset

This section documents the actual notebook/project using LLaMA Factory for real fine-tuning.

## Setup

```
Base Model:  google/gemma-1.1-2b-it
Dataset:     harpomaxx/unix-commands (from HuggingFace)
Method:      LoRA fine-tuning
Interface:   WebUI + CLI
Goal:        Teach Gemma to explain Unix commands
```

## 12.1 Dataset Preparation

**harpomaxx/unix-commands** dataset format (Alpaca-compatible):
```json
[
  {
    "instruction": "Explain the 'ls -la' Unix command.",
    "input": "",
    "output": "The 'ls -la' command lists all files in the current directory in long format (-l), including hidden files (-a). It shows permissions, owner, size, and modification time for each file."
  },
  {
    "instruction": "What does 'grep -r pattern .' do?",
    "input": "",
    "output": "The 'grep -r pattern .' command recursively searches for the pattern in all files starting from the current directory (.). It prints each line where the pattern is found along with the filename."
  }
]
```

**Register in dataset_info.json:**
```json
{
  "unix_commands": {
    "hf_hub_url": "harpomaxx/unix-commands",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
  }
}
```

## 12.2 WebUI Training Walkthrough

```
Step 1 — Model:
  Hub name: huggingface
  Model path: google/gemma-1.1-2b-it
  Template: gemma
  Finetuning type: LoRA

Step 2 — Dataset:
  Dataset: unix_commands
  Format: alpaca
  Max samples: 5000 (or all)
  Val size: 0.1 (10% validation)
  Cutoff len: 512

Step 3 — Training Config:
  Stage: SFT
  Learning rate: 2e-4
  Epochs: 3
  Batch size: 2
  Gradient accumulation: 4
  LR scheduler: cosine
  Warmup ratio: 0.03
  logging_steps: 10

Step 4 — GPU Optimization:
  Compute type: bf16
  Quantization: 4-bit (QLoRA mode)
  Flash attention: auto
  Gradient checkpointing: ✅

Step 5 — LoRA config:
  LoRA rank: 64
  LoRA alpha: 16
  LoRA dropout: 0.05
  LoRA target: all

Step 6 — Output:
  Output dir: output/gemma-unix-commands
  Click START
```

## 12.3 CLI Training with YAML

**gemma_unix_lora.yaml:**
```yaml
### Model
model_name_or_path: google/gemma-1.1-2b-it
template: gemma

### Method
stage: sft
do_train: true
finetuning_type: lora

### Dataset
dataset: unix_commands
dataset_dir: data
cutoff_len: 512
max_samples: 5000
val_size: 0.1
overwrite_cache: true
preprocessing_num_workers: 4

### Output
output_dir: output/gemma-unix-commands
logging_steps: 10
save_steps: 100
plot_loss: true
overwrite_output_dir: true

### Train
per_device_train_batch_size: 2
gradient_accumulation_steps: 4
learning_rate: 2.0e-4
num_train_epochs: 3.0
lr_scheduler_type: cosine
warmup_ratio: 0.03
bf16: true
gradient_checkpointing: true

### LoRA
lora_r: 64
lora_alpha: 16
lora_dropout: 0.05
lora_target: all

### QLoRA
quantization_bit: 4
quantization_method: bnb
```

**Run training:**
```bash
llamafactory-cli train gemma_unix_lora.yaml
```

**Export merged model:**
```yaml
# gemma_export.yaml
model_name_or_path: google/gemma-1.1-2b-it
adapter_name_or_path: output/gemma-unix-commands
template: gemma
finetuning_type: lora
export_dir: output/gemma-unix-merged
export_legacy_format: false
```

```bash
llamafactory-cli export gemma_export.yaml
```

## 12.4 Inference with PeftModel

After training, you can load and use the fine-tuned model with HuggingFace PEFT:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# Load base model
base_model_id = "google/gemma-1.1-2b-it"
tokenizer = AutoTokenizer.from_pretrained(base_model_id)
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Load LoRA adapter
adapter_path = "output/gemma-unix-commands"
model = PeftModel.from_pretrained(base_model, adapter_path)
model.eval()

# Inference
def generate_response(instruction):
    prompt = f"<bos><start_of_turn>user\n{instruction}<end_of_turn>\n<start_of_turn>model\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            do_sample=True,
        )

    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    return response

# Test
print(generate_response("Explain the 'find . -name *.py' command."))
```

**Using merged model directly (no PEFT needed):**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "output/gemma-unix-merged",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("output/gemma-unix-merged")
```

---

# 13. Decision Guide — Which Training Method to Use?

## By VRAM Available

```
VRAM < 8 GB (Colab free, RTX 3060):
  → QLoRA (4-bit) + Unsloth + gradient_checkpointing
  → batch_size=1, gradient_accumulation=8
  → lora_r=64, cutoff_len=512

VRAM 8-16 GB (RTX 3080, RTX 3090, T4):
  → QLoRA (4-bit) OR LoRA (FP16 base)
  → batch_size=1-2, gradient_accumulation=4-8
  → lora_r=64, cutoff_len=1024

VRAM 16-24 GB (A10G, RTX 4090):
  → LoRA (FP16) comfortably
  → batch_size=2-4, gradient_accumulation=2-4
  → lora_r=128, cutoff_len=2048

VRAM 40-80 GB (A100):
  → Full Fine-Tuning for 7B models
  → LoRA for 13B-70B models
  → All options available

Multi-GPU (2+ GPUs with 80GB each):
  → Full Fine-Tuning for 70B models
  → Use DeepSpeed stage 2 or 3
```

## By Task

| Goal | Stage | Method | Dataset Format |
|---|---|---|---|
| Follow instructions | SFT | LoRA / QLoRA | Alpaca |
| Chat fine-tuning | SFT | LoRA / QLoRA | ShareGPT |
| Preference alignment | DPO | LoRA / QLoRA | DPO (chosen/rejected) |
| Full RLHF | RM → PPO | LoRA for RM, then PPO | DPO format → prompts |
| Stable preference FT | KTO | LoRA | DPO format |
| Domain pretraining | PT | Full / LoRA | Raw text |
| Max accuracy, any task | SFT | Full FT | Alpaca / ShareGPT |

## By Model Size

| Model Size | Recommended Method | Notes |
|---|---|---|
| < 3B (Phi-2, Gemma-2B) | LoRA or even Full FT | Small enough for full FT on good GPU |
| 7-8B (LLaMA-3 8B, Mistral 7B) | QLoRA (4-bit) + LoRA | Most practical setup |
| 13B | QLoRA mandatory for single GPU | Or multi-GPU full FT |
| 30-70B | LoRA + 4-bit on multi-GPU | Or DeepSpeed full FT on cluster |
| 70B+ | Requires multi-GPU cluster | QLoRA + DeepSpeed or FSDP |

## Decision Flowchart

```
START: I want to fine-tune an LLM
  │
  ├─ Do I have >40GB VRAM per GPU?
  │    Yes → Full Fine-Tuning
  │    No  ↓
  │
  ├─ Do I have 16-40GB VRAM?
  │    Yes → LoRA (FP16 base model)
  │    No  ↓
  │
  ├─ Do I have <16GB VRAM?
  │    Yes → QLoRA (4-bit base + LoRA adapters)
  │          + gradient_checkpointing: true
  │          + flash_attn: unsloth (for <10GB)
  │
  └─ What is my task?
       Instruction following? → SFT
       Preference alignment?  → DPO (simple) or PPO (complex)
       Reward model?          → RM stage
       Domain adaptation?     → SFT or PT
```

---

# 14. Common Errors & Fixes

## Error: CUDA Out of Memory (OOM)

```
RuntimeError: CUDA out of memory. Tried to allocate 2.50 GiB...
```

**Fixes (try in order):**
```
1. Reduce cutoff_len: 2048 → 1024 → 512
2. Set per_device_train_batch_size: 1
3. Increase gradient_accumulation_steps to compensate
4. Enable gradient_checkpointing: true
5. Enable 4-bit quantization: quantization_bit: 4
6. Enable flash attention: flash_attn: unsloth
7. Reduce lora_r: 128 → 64 → 16
```

## Error: Model not found / Template not found

```
ValueError: Template 'xxx' not found in templates.
```

**Fix:**
```
Use the correct template name:
  google/gemma-1.1-2b-it  → template: gemma
  meta-llama/Meta-Llama-3 → template: llama3
  mistralai/Mistral-7B    → template: mistral
  Qwen/Qwen2-7B           → template: qwen

List all templates: cat LLaMA-Factory/src/llamafactory/data/template.py
```

## Error: Dataset not found

```
FileNotFoundError: data/my_dataset.json not found
```

**Fix:**
```
1. Place your file in: LLaMA-Factory/data/
2. Register in: LLaMA-Factory/data/dataset_info.json
3. Use the registered name in your config (not the filename)
```

## Error: NaN Loss

```
Training: loss = nan
```

**Fixes:**
```
1. Reduce learning_rate: 2e-4 → 1e-4 → 5e-5
2. Add warmup: warmup_ratio: 0.03 or warmup_steps: 50
3. Check dataset — ensure output field is not empty
4. Ensure correct template is selected for the model
5. Try bf16: false, fp16: true (or vice versa)
```

## Error: Slow Training

```
Training steps taking very long
```

**Fixes:**
```
1. Enable flash_attn: flash_attn (if supported GPU)
2. Enable flash_attn: unsloth (for Colab)
3. Enable packing: true (pack short sequences)
4. Reduce cutoff_len (shorter sequences = faster steps)
5. Use bf16: true instead of fp32
```

## Error: Loss Not Decreasing

```
After many epochs, loss stays at ~1.5
```

**Fixes:**
```
1. Increase learning_rate: 5e-5 → 2e-4
2. Check dataset — ensure instruction field is not empty
3. Verify template matches the model family
4. Increase lora_r: 16 → 64 (more adapter capacity)
5. Add more epochs
6. Check if model is already fine-tuned on this domain
```

## Error: Generation Quality Issues (Repetition / Gibberish)

```
Model repeats itself or generates garbage
```

**Fixes:**
```
Inference side (generation config):
  repetition_penalty: 1.1   # Add this
  temperature: 0.7
  top_p: 0.9
  top_k: 50

Training side:
  Verify template is correct
  Check dataset quality (garbage in = garbage out)
  Ensure loss converged properly
```

## Error: BitsAndBytes / QLoRA Issues

```
ImportError: bitsandbytes not found
# OR
RuntimeError: CUDA capability not supported by bitsandbytes
```

**Fixes:**
```bash
# Install bitsandbytes
pip install bitsandbytes

# For older GPUs / non-standard CUDA:
pip install bitsandbytes --prefer-binary

# Verify GPU compatibility:
python -c "import bitsandbytes; print(bitsandbytes.__version__)"

# For CPU-only (fallback):
# Set quantization_bit to none and use CPU training (slow)
```

---

# 15. Comparison Tables

## Training Methods Comparison

| Feature | Full FT | Freeze | LoRA | QLoRA | OFT |
|---|---|---|---|---|---|
| Parameters trained | 100% | ~10-30% | ~0.1-1% | ~0.1-1% | ~0.1-1% |
| VRAM (7B model) | ~28-56 GB | ~20-35 GB | ~14 GB | ~6-8 GB | ~14 GB |
| Accuracy | Best | Good | Good | Good (-5%) | Good |
| Speed | Slow | Medium | Fast | Medium | Fast |
| Catastrophic forgetting | High risk | Medium risk | Low risk | Low risk | Low risk |
| Adapter merging needed | No | No | Yes | Yes | Yes |
| Best for | Max accuracy | Layered control | Production | Low VRAM | Stability |

## Training Stages Comparison

| Stage | Objective | Data Needed | Common Use |
|---|---|---|---|
| SFT | Learn instruction→output | Instruction + Output | Most common |
| PT | Next-token prediction | Raw text | Domain adaptation |
| RM | Score good vs bad | Chosen + Rejected | RLHF step 1 |
| PPO | RL-based alignment | Prompts + Reward model | RLHF step 2 |
| DPO | Preference alignment | Chosen + Rejected | Simpler alternative to PPO |
| KTO | Stable preference | Chosen + Rejected | Low-data preference FT |

## Dataset Format Comparison

| Format | Columns | Best For | Multi-turn? |
|---|---|---|---|
| Alpaca | instruction, input, output | SFT — simple Q&A | ❌ No |
| ShareGPT | conversations[{from, value}] | Chat models | ✅ Yes |
| DPO | prompt, chosen, rejected | Preference training | ❌ No |

## Flash Attention Variants

| Option | Speed | VRAM Savings | GPU Requirement |
|---|---|---|---|
| `auto` | Best available | Varies | Any |
| `flash_attn` | High | High | Ampere+ (RTX 30xx, A100) |
| `unsloth` | Very High | Very High | Any CUDA GPU |
| `liger_kernel` | High | Medium | Any modern GPU |

## LR Scheduler Comparison

| Scheduler | LR Pattern | Training Stability | Recommended |
|---|---|---|---|
| `cosine` | Smooth cosine decay | High | ✅ Yes |
| `linear` | Linear decay to 0 | Good | OK |
| `constant` | No decay | Medium | Only for very short runs |
| `cosine_with_restarts` | Periodic cosine | Variable | For cyclic training |

---

# 16. Quick Reference Cheat Sheet

## Minimal Working QLoRA Config

```yaml
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct
template: llama3
stage: sft
finetuning_type: lora
dataset: your_dataset
cutoff_len: 1024
output_dir: output/my_model
per_device_train_batch_size: 1
gradient_accumulation_steps: 8
num_train_epochs: 3
learning_rate: 2.0e-4
lr_scheduler_type: cosine
warmup_ratio: 0.03
lora_r: 64
lora_alpha: 16
lora_dropout: 0.05
quantization_bit: 4
bf16: true
gradient_checkpointing: true
report_to: none
```

## CLI Quick Reference

```bash
# Launch WebUI
llamafactory-cli webui

# Train
llamafactory-cli train config.yaml

# Chat (CLI)
llamafactory-cli chat config.yaml

# Evaluate
llamafactory-cli eval config.yaml

# Export/Merge
llamafactory-cli export config.yaml

# API Server
llamafactory-cli api api_config.yaml

# Version
llamafactory-cli version
```

## Key Parameter Cheat Sheet

| Parameter | Low-VRAM Value | High-VRAM Value | Default |
|---|---|---|---|
| `quantization_bit` | `4` | `none` | `none` |
| `lora_r` | `16-32` | `64-128` | `64` |
| `lora_alpha` | `8-16` | `16-64` | `16` |
| `per_device_train_batch_size` | `1` | `4-8` | `1` |
| `gradient_accumulation_steps` | `8-16` | `1-2` | `8` |
| `cutoff_len` | `512` | `2048-4096` | `1024` |
| `gradient_checkpointing` | `true` | `false` | `false` |
| `flash_attn` | `unsloth` | `flash_attn` | `auto` |
| `learning_rate` | `2e-4` | `2e-4` | `2e-4` |
| `num_train_epochs` | `3` | `3` | `3` |

## Model → Template Mapping

| Model | Template |
|---|---|
| `meta-llama/Meta-Llama-3-*` | `llama3` |
| `meta-llama/Llama-2-*` | `llama2` |
| `google/gemma-*` | `gemma` |
| `mistralai/Mistral-*` | `mistral` |
| `mistralai/Mixtral-*` | `mistral` |
| `Qwen/Qwen2-*` | `qwen` |
| `Qwen/Qwen-*` | `qwen` |
| `microsoft/phi-*` | `phi` |
| `microsoft/Phi-3-*` | `phi3` |
| `THUDM/chatglm-*` | `chatglm3` |
| `THUDM/glm-4-*` | `glm4` |
| `deepseek-ai/deepseek-*` | `deepseek` |
| `01-ai/Yi-*` | `yi` |
| `baichuan-inc/Baichuan*` | `baichuan2` |

## VRAM Quick Estimator

```
Base VRAM for model loading:
  Model params (billions) × precision_bytes × overhead_factor

  FP16:  7B  → 7 × 2 = 14 GB base
  BF16:  7B  → 7 × 2 = 14 GB base
  4-bit: 7B  → 7 × 0.5 = 3.5 GB + overhead ≈ 6 GB

Additional training overhead:
  Gradients:   ~same as model (FP32)
  Optimizer:   ~2× model size (Adam)
  Activations: depends on batch_size × cutoff_len

LoRA adapters (r=64, 7B model):
  ≈ 0.5% of model params ≈ 35M × 2 bytes ≈ 70 MB (negligible)

Rule of thumb for LoRA:
  Total VRAM ≈ model_size_GB × 2 + 2 GB overhead

For QLoRA:
  Total VRAM ≈ model_size_4bit_GB + 2 GB overhead

Examples:
  7B LoRA FP16:  14 + 2 = ~16 GB
  7B QLoRA 4-bit: 6 + 2  = ~8 GB
  13B QLoRA 4-bit: 10 + 2 = ~12 GB
```

## Common LoRA Target Modules

```yaml
# Train ALL attention and MLP layers (recommended, simple)
lora_target: all

# Train only specific modules (manual selection):
lora_target: q_proj,k_proj,v_proj,o_proj          # Attention only
lora_target: q_proj,v_proj                        # Minimal (classic LoRA paper)
lora_target: q_proj,k_proj,v_proj,gate_proj,up_proj,down_proj  # Attn + MLP
```

## Stage × Format Quick Reference

```
SFT    → Alpaca format  → instruction, input, output
SFT    → ShareGPT format → conversations: [{from, value}, ...]
DPO    → DPO format     → prompt, chosen, rejected
RM     → DPO format     → prompt, chosen, rejected (same!)
PPO    → Prompt only    → Just the input prompts
KTO    → DPO format     → prompt, chosen, rejected
PT     → Text only      → Plain text (no special format)
```

## Memory Saving Priority Order

```
Apply these from top to bottom until VRAM fits:

1. quantization_bit: 4                (biggest saving — ~70%)
2. gradient_checkpointing: true       (~30-40% saving)
3. flash_attn: unsloth                (~50% saving in some cases)
4. cutoff_len: reduce to 512          (quadratic saving with attention)
5. per_device_train_batch_size: 1     (obvious direct saving)
6. gradient_accumulation_steps: 8+   (maintain effective batch without VRAM)
7. lora_r: reduce to 16              (small saving, last resort)
```

---

# Summary Mental Model

```
START: I want to fine-tune an LLM
         │
         ▼
CHOOSE METHOD (How to update weights):
  Low VRAM  → QLoRA (4-bit base + LoRA adapters)
  Med VRAM  → LoRA (FP16 base + LoRA adapters)
  High VRAM → Full Fine-Tuning
         │
         ▼
CHOOSE STAGE (What objective):
  Instruction following → SFT
  Preference alignment  → DPO (or PPO for full RLHF)
  Score responses       → Reward Modeling
  Raw text learning     → Pretraining
         │
         ▼
CHOOSE INTERFACE:
  Quick experiment      → WebUI (llamafactory-cli webui)
  Production/pipeline   → CLI (llamafactory-cli train config.yaml)
         │
         ▼
CHOOSE DATASET FORMAT:
  Single-turn Q&A       → Alpaca
  Multi-turn chat       → ShareGPT
  Preference data       → DPO format (prompt, chosen, rejected)
         │
         ▼
TRAIN, EVALUATE, EXPORT:
  llamafactory-cli train  config.yaml  → Train
  llamafactory-cli eval   config.yaml  → Evaluate
  llamafactory-cli export config.yaml  → Merge + Export
  llamafactory-cli api    config.yaml  → Serve
         │
         ▼
RESULT: Fine-tuned model saved as .safetensors
        Ready for inference via PeftModel or merged directly
```

---

*Source: LLaMA Factory — Finetune-LLAMA-FACTORY-Params.pdf + WebUI walkthrough PDFs + CLI documentation*
*Topics: WebUI → CLI → YAML config → Dataset formats → LoRA/QLoRA/DPO/PPO → All parameters documented*
