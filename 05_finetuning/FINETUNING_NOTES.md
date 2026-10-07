# 🧠 LLM Fine-Tuning — Complete In-Depth Notes
### Source: 05_finetuning — Instruction Finetuning + Non-Instruction Pretraining Notebooks

---

# TABLE OF CONTENTS

1. [What is Fine-Tuning?](#1-what-is-fine-tuning)
2. [The 4 Stages of LLM Development](#2-the-4-stages-of-llm-development)
3. [Pre-training vs Fine-Tuning — Core Differences](#3-pre-training-vs-fine-tuning--core-differences)
4. [Domain-Specific Knowledge: Why General Models Fall Short](#4-domain-specific-knowledge-why-general-models-fall-short)
5. [Data Engineering for Fine-Tuning](#5-data-engineering-for-fine-tuning)
   - 5.1 Prebuilt Datasets from Hugging Face
   - 5.2 Building Your Own Domain Corpus from PDFs
   - 5.3 Paragraph Splitting and Cleaning
   - 5.4 CSV, JSONL, and Dataset Formats
6. [Causal Language Modeling — The Core Objective](#6-causal-language-modeling--the-core-objective)
   - 6.1 Next-Token Prediction
   - 6.2 Why `labels = input_ids.copy()`
   - 6.3 Internal Label Shifting in HuggingFace
   - 6.4 Tokenization Arguments Demystified
   - 6.5 Context Windows & Chunking
7. [Stage 1: Non-Instruction Domain Fine-Tuning (Continued Pre-training)](#7-stage-1-non-instruction-domain-fine-tuning-continued-pre-training)
   - 7.1 What it Teaches the Model
   - 7.2 Full Fine-Tuning
   - 7.3 Selective Layer Freezing
   - 7.4 LoRA (Low-Rank Adaptation)
   - 7.5 QLoRA (Quantized LoRA)
   - 7.6 Training Loop & TrainingArguments
8. [LoRA — Deep Dive](#8-lora--deep-dive)
   - 8.1 The Problem LoRA Solves
   - 8.2 LoRA Mathematics
   - 8.3 Which Layers to Target
   - 8.4 LoRA Config Reference Table
   - 8.5 Adapter Merging (`merge_and_unload`)
9. [Stage 2: Instruction Fine-Tuning (SFT — Supervised Fine-Tuning)](#9-stage-2-instruction-fine-tuning-sft--supervised-fine-tuning)
   - 9.1 Why Continued Pre-training Alone Is Not Enough
   - 9.2 Instruction Prompt Templates
   - 9.3 The Alpaca Format (Our Primary Template)
   - 9.4 LLaMA-2 Chat Format
   - 9.5 ChatML Format
   - 9.6 Benchmark Instruction Datasets
10. [Response Masking — The Most Critical SFT Detail](#10-response-masking--the-most-critical-sft-detail)
    - 10.1 The Problem Without Masking
    - 10.2 The `-100` Label Trick
    - 10.3 Masking Code Implementation
    - 10.4 Verification Checklist
11. [Two-Stage LoRA Pipeline](#11-two-stage-lora-pipeline)
    - 11.1 Stage 1 → Domain Adapter
    - 11.2 Merge & Unload
    - 11.3 Stage 2 → Instruction Adapter
12. [Text Generation & Inference Control](#12-text-generation--inference-control)
    - 12.1 Greedy vs Sampling
    - 12.2 Temperature
    - 12.3 Top-P (Nucleus Sampling)
    - 12.4 Top-K
    - 12.5 Repetition Penalty
    - 12.6 Beam Search
13. [Preference Alignment (RLHF & DPO)](#13-preference-alignment-rlhf--dpo)
    - 13.1 What Alignment Means
    - 13.2 RLHF Pipeline (PPO)
    - 13.3 Direct Preference Optimization (DPO) — Math
    - 13.4 DPO vs RLHF Comparison
    - 13.5 Preference Datasets
14. [Memory & Hardware Economics of Fine-Tuning](#14-memory--hardware-economics-of-fine-tuning)
    - 14.1 VRAM Breakdown
    - 14.2 Mixed Precision (FP16 / BF16)
    - 14.3 Gradient Accumulation
    - 14.4 Model Memory Table
15. [TrainingArguments — Complete Reference](#15-trainingarguments--complete-reference)
16. [Common Fine-Tuning Pitfalls & How to Fix Them](#16-common-fine-tuning-pitfalls--how-to-fix-them)
17. [Fine-Tuning Datasets Master Reference](#17-fine-tuning-datasets-master-reference)
18. [Decision Guide — When to Use What](#18-decision-guide--when-to-use-what)
19. [Key Formulas Quick Reference](#19-key-formulas-quick-reference)
20. [Mental Model Summary](#20-mental-model-summary)

---

# 1. What is Fine-Tuning?

**Definition:**
> Fine-tuning is the process of continuing the training of a **pre-trained model** on a **smaller, task-specific dataset** to adapt its knowledge or behavior to a particular domain, task, or interaction style — without retraining from scratch.

OR in simpler terms:
> Fine-tuning is "teaching a smart person with general knowledge to become an expert in one specific field, using a targeted curriculum."

## Analogy

```
Pre-training: A student completes a full 15-year education
              — learns reading, math, science, history, world knowledge.

Fine-tuning:  That same student joins a 3-month medical school residency.
              — They don't forget general knowledge.
              — They specialize deeply in cardiology / pharmacology.

Domain FT:    Add domain terminology and facts.
Instruction FT: Teach the student HOW to answer questions, not just know facts.
Preference Alignment: Teach the student WHEN to say "I don't know" vs guess.
```

## Key Facts

| Property | Fine-Tuning | Training from Scratch |
|---|---|---|
| Starting point | Pre-trained model | Random weights |
| Data needed | Thousands of examples | Billions of tokens |
| Compute | Hours/Days (1 GPU) | Weeks/Months (thousands of GPUs) |
| Result | Specialized model | General model |
| Cost | Low ($5 – $200 typically) | Very high ($1M – $100M) |

---

# 2. The 4 Stages of LLM Development

Every state-of-the-art LLM (GPT-4, LLaMA-3, Claude, Mistral) goes through these four sequential stages:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                          THE 4 STAGES OF MODERN LLM DEVELOPMENT                              │
├─────────────────┬──────────────────────────┬─────────────────────────┬────────────────────────┤
│  1. PRE-TRAINING│ 2. DOMAIN ADAPTATION     │ 3. INSTRUCTION TUNING   │ 4. PREFERENCE          │
│  (Foundation)   │    (Continued Pretrain)  │    (SFT)                │    ALIGNMENT           │
├─────────────────┼──────────────────────────┼─────────────────────────┼────────────────────────┤
│ Massive web     │ Raw domain corpus        │ Task-oriented prompt-   │ Human/AI preference    │
│ corpora         │ (PDFs, research papers,  │ response pairs          │ pairs (chosen/rejected)│
│ (3T+ tokens)    │ clinical trials)         │ (Alpaca, ChatML format) │                        │
│                 │                          │                         │                        │
│ General world   │ Unsupervised next-       │ Supervised loss with    │ Direct Preference      │
│ knowledge       │ token prediction only    │ Response Masking (-100) │ Optimization (DPO)     │
│                 │                          │                         │ OR RLHF (PPO)          │
│ Next-token      │ Ingests domain vocab,    │ Teaches conversational  │                        │
│ prediction      │ entities & factual       │ behavior, instruction   │ Safety, tone,          │
│                 │ domain knowledge         │ adherence               │ harmlessness, truth    │
├─────────────────┼──────────────────────────┼─────────────────────────┼────────────────────────┤
│ TinyLlama-1.1B  │ We do this in Stage 1    │ We do this in Stage 2   │ We cover theory here   │
│ already done!   │ of this notebook         │ of this notebook        │ (DPO, RLHF datasets)   │
└─────────────────┴──────────────────────────┴─────────────────────────┴────────────────────────┘
```

**Important:** We are using `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` as our base model.
This model was pre-trained on **3 Trillion tokens** for ~1.4 million gradient steps. Stage 1 is already done!

---

# 3. Pre-training vs Fine-Tuning — Core Differences

| Aspect | Pre-training | Domain Adaptation (Stage 2) | Instruction Fine-Tuning (Stage 3) |
|---|---|---|---|
| **Goal** | Learn general language patterns | Learn domain vocabulary & facts | Learn to follow instructions |
| **Data** | Billions of web documents | Domain PDFs, papers, notes | Q&A / Instruction-Response pairs |
| **Data size** | 1T – 15T tokens | 50K – 10M tokens | 1K – 100K instruction pairs |
| **Loss type** | Causal LM (all tokens) | Causal LM (all tokens) | Causal LM + **Response Masking** |
| **Objective** | Predict next token | Adapt domain vocabulary | Follow user instructions |
| **Example input** | Random web pages | Pharma research papers | "Explain Metformin's mechanism" |
| **Example output** | Next token continuation | Domain-specific completion | Structured clinical answer |
| **Compute** | Huge (1000s of GPUs) | Medium (1–8 GPUs) | Small-Medium (1–4 GPUs) |

---

# 4. Domain-Specific Knowledge: Why General Models Fall Short

When you ask a general model: `"Explain the mechanism of action of Metformin."`

A **base model (no domain fine-tuning)** might respond:
```
"Metformin is a drug. Explain the mechanism of action of Aspirin.
Chapter 4 of Medical Textbooks explains the following pharmacological principles..."
```

It autocompletes like text it has seen — often continuing with unrelated text from training data.

A **domain-adapted model** responds:
```
"Metformin activates AMP-activated protein kinase (AMPK) in the liver,
reducing hepatic gluconeogenesis and improving glucose uptake..."
```

A **domain-adapted + instruction-tuned model** responds cleanly:
```
"### Mechanism of Action of Metformin:
1. AMPK Activation: Primary mechanism...
2. Hepatic Gluconeogenesis Inhibition: ...
3. Glucose Uptake Enhancement: ..."
```

## Why This Happens

```
Domain terminology:  General model = low probability for "NPC1L1", "AMPK", "gluconeogenesis"
                     Domain model  = high probability for clinical pharmacology terms

Instruction following: Base model = no concept of "Instruction → Response" pattern
                       SFT model  = trained explicitly to decode instruction and produce response
```

---

# 5. Data Engineering for Fine-Tuning

## 5.1 Prebuilt Datasets from Hugging Face

Hugging Face provides thousands of ready-to-use datasets for fine-tuning:

```python
from datasets import Dataset, load_dataset

# Load a complete dataset
dataset = load_dataset("roneneldan/TinyStories", split="train")
print(dataset)   # Dataset of 2M+ short story examples
print(dataset[0])  # {'text': 'Once upon a time...' }
```

### Popular Non-Instruction (Continued Pretraining) Datasets

| Dataset Name | Domain | Size | Use Case |
|---|---|---|---|
| `HuggingFaceFW/fineweb` | Curated web crawl | 15 Trillion tokens | State-of-the-art general pretraining |
| `ncbi/pubmed` | Medical Abstracts | Millions of papers | Biomedical domain adaptation |
| `datajuicer/the-pile-pubmed-abstracts-refined-by-data-juicer` | Refined biomedical | Filtered corpus | High-signal clinical fine-tuning |
| `open-llm-leaderboard/open_llm_corpus` | Research papers | Large | Scientific reasoning |
| `Skylion007/openwebtext` | General web text | 40GB | GPT-2 style pretraining |
| `armanc/scientific_papers` | arXiv + PubMed | Long-form papers | Scientific language |
| `roneneldan/TinyStories` | Synthesized stories | 2M stories | SLM grammar & coherence |

## 5.2 Building Your Own Domain Corpus from PDFs

When domain data doesn't exist on HuggingFace, you extract it from your own documents:

```python
import fitz  # PyMuPDF — pip install PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text page-by-page from a PDF using PyMuPDF.
    Returns a list of strings — one per page.
    """
    text_blocks = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text("text").strip()
            if text:
                text_blocks.append(text)
    return text_blocks

# Usage:
pdf_texts = extract_text_from_pdf("/content/Metformin.pdf")
# Returns: ['Metformin is one of the most...', 'Clinical trials have...', ...]
```

**Why PyMuPDF?**
- Much faster than pdfminer, pypdf2
- Preserves paragraph structure
- Handles multi-column layouts, tables, headers

## 5.3 Paragraph Splitting and Cleaning

Raw PDF text is noisy. We split on paragraph boundaries and filter tiny fragments:

```python
import re

def split_paragraphs(pages, min_length=30):
    """
    Split each page's text into individual paragraphs.
    Removes headers, page numbers, and garbage fragments.
    """
    paragraphs = []
    for page_text in pages:
        # Split on blank lines (standard paragraph separator)
        chunks = re.split(r'\n\s*\n', page_text)
        for chunk in chunks:
            clean = chunk.strip()
            if len(clean) > min_length:  # Skip headers, page numbers
                paragraphs.append(clean)
    return paragraphs
```

### Why This Matters

| Step | What Happens | Example |
|---|---|---|
| **1. Data Collection** | Crawl/collect domain text | PDFs, research papers, clinical notes |
| **2. Cleaning / Filtering** | Remove HTML, junk, duplicates | `strip()` + length filter |
| **3. Splitting / Chunking** | Split into paragraphs using regex | `re.split(r'\n\s*\n', page_text)` |
| **4. Tokenization** | Convert text → token IDs via BPE | `"Metformin"` → `[4819]` |
| **5. Training** | Next-token prediction on each chunk | predict `"activates"` given `"Metformin"` |

## 5.4 CSV, JSONL, and Dataset Formats

After extraction, save in structured formats for reloading:

```python
from datasets import Dataset
import pandas as pd

# Build dataset
data = [{"text": p} for p in paragraphs]
dataset = Dataset.from_list(data)

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("pharma_domain.csv", index=False)

# Save to JSONL (JSON Lines — one JSON object per line)
df.to_json("pharma_domain.jsonl", orient="records", lines=True)

# Reload later
dataset = load_dataset("csv",  data_files="pharma_domain.csv",  split="train")
dataset = load_dataset("json", data_files="pharma_domain.jsonl", split="train")
```

**CSV vs JSONL:**

| Format | Pros | Cons | Best For |
|---|---|---|---|
| `.csv` | Easy to open in Excel/Sheets | Poor handling of newlines in text | Simple tabular data |
| `.jsonl` | Handles multiline strings, dicts | Slightly larger file | Complex instruction datasets |
| `.parquet` | Binary, compressed, very fast | Hard to read manually | Large-scale production pipelines |

---

# 6. Causal Language Modeling — The Core Objective

## 6.1 Next-Token Prediction

The entire foundation of GPT-style models is predicting the next word in a sequence.

**Mathematical Objective (Negative Log-Likelihood Loss):**

```
L_CLM(θ) = - Σ log P_θ(w_t | w_1, w_2, ..., w_{t-1})
               t=1 to T

Where:
  θ = model parameters
  w_t = the t-th token in the sequence
  The model must predict each token given ALL previous tokens
```

**In Plain English:**
Given the sentence `"Metformin activates AMPK"`, the model is penalized if it:
- Given `"Metformin"` → doesn't predict `"activates"` 
- Given `"Metformin activates"` → doesn't predict `"AMPK"`

## 6.2 Why `labels = input_ids.copy()`

This is one of the most confusing lines for beginners. Let's break it down completely.

```python
def tokenize_fn(examples):
    tokens = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)
    tokens["labels"] = tokens["input_ids"].copy()  # ← WHY IS THIS HERE?
    return tokens
```

**Step-by-step explanation:**

```
input_ids  = [  1,  4819,  1823,  9402,  123,  2  ]
               BOS  "Met"  "acti" "AMPK"  ...  EOS

labels     = [  1,  4819,  1823,  9402,  123,  2  ]
               (SAME as input_ids — exact clone)
```

**What HuggingFace does internally during loss computation:**

```
Position 0 (BOS)   → predict token at position 1 ("Metformin")
Position 1 (Met)   → predict token at position 2 ("activates")
Position 2 (acti)  → predict token at position 3 ("AMPK")
...and so on

SHIFTED COMPARISON:
  logits[0] vs labels[1]
  logits[1] vs labels[2]
  logits[t] vs labels[t+1]  ← internal offset done automatically!
```

**The Golden Rule:**
> `AutoModelForCausalLM` shifts logits against labels internally.
> So simply set `labels = input_ids` — the model handles the prediction offset!

## 6.3 Internal Label Shifting in HuggingFace

```
Full sequence:  [BOS, "Metformin", "activates", "AMPK",  EOS]
input_ids:      [ 1,   4819,        1823,         9402,    2  ]
labels:         [ 1,   4819,        1823,         9402,    2  ]

During forward pass, model internally shifts:
  Prediction at pos 0 → should match labels[1] = 4819  ("Metformin")
  Prediction at pos 1 → should match labels[2] = 1823  ("activates")
  Prediction at pos 2 → should match labels[3] = 9402  ("AMPK")
  Prediction at pos 3 → should match labels[4] = 2     (EOS)
  Prediction at pos 4 → IGNORED (EOS is last, no target)
```

## 6.4 Tokenization Arguments Demystified

```python
tokens = tokenizer(
    examples["text"],
    truncation=True,        # ← Cut sequences longer than max_length
    padding="max_length",   # ← Pad sequences shorter than max_length
    max_length=512          # ← Fixed sequence length
)
```

| Argument | Options | What it Does | Why We Need It |
|---|---|---|---|
| `truncation=True` | True / False | Cuts off text beyond `max_length` | Prevents VRAM overflow on long texts |
| `padding="max_length"` | `"max_length"`, `True`, `"longest"` | Pads short sequences with `<pad>` tokens | Enables batching (all sequences same length) |
| `max_length=512` | Any integer | Maximum sequence length | 512 = standard for most fine-tuning tasks |
| `return_tensors="pt"` | `"pt"`, `"np"`, `None` | Returns PyTorch tensors / NumPy / Python lists | Use `"pt"` for inference, `None` for dataset.map |

**What padding looks like:**

```
Original text : "Metformin activates AMPK."
Tokenized     : [1, 4819, 1823, 9402, 29889, 2]       ← 6 tokens
After padding : [1, 4819, 1823, 9402, 29889, 2, 2, 2, ...2]  ← padded to 512
attention_mask: [1,    1,    1,    1,      1, 1, 0, 0, ...0]  ← 0 for pad positions
```

**The attention_mask:**
- `1` → real token — model should attend to this
- `0` → padding token — model should IGNORE this during attention

## 6.5 Context Windows & Chunking

How much text can a model process at once? This is the context window:

| Model Era | Max Context Window | Approx Words | Common Training Chunk Size |
|---|---|---|---|
| **GPT-1 (2018)** | 512 tokens | ~350 words | 512 tokens |
| **GPT-2 (2019)** | 1,024 tokens | ~750 words | 1,024 tokens |
| **GPT-3 (2020)** | 2,048 tokens | ~1,500 words | 2,048 tokens |
| **GPT-3.5 / ChatGPT (2022)** | 4,096 tokens | ~3,000 words | 2k–4k during FT |
| **TinyLlama (2023)** | 2,048 tokens | ~1,500 words | 512–1024 for fine-tuning |
| **LLaMA-3 (2024)** | 8,192 tokens | ~6,000 words | 2k–4k for instruction FT |
| **GPT-4 / Claude-3 (2024)** | 128,000 tokens | ~100,000 words | Long-context FT |

**Why we use `max_length=512` for fine-tuning:**
- Smaller = fits more examples per GPU batch
- Smaller = faster training iterations
- Most instruction Q&A pairs fit within 512 tokens

---

# 7. Stage 1: Non-Instruction Domain Fine-Tuning (Continued Pre-training)

## 7.1 What it Teaches the Model

Stage 1 trains on raw, unstructured domain text with **no instructions or Q&A format**.

**What the model learns:**
- New domain vocabulary (e.g., `"gluconeogenesis"`, `"NPC1L1"`, `"AMPK"`, `"BQ.1"`)
- Co-occurrence patterns (e.g., `"Metformin"` often appears with `"insulin sensitivity"`, `"AMPK"`)
- Domain-specific sentence patterns and clinical writing styles
- Factual relationships between entities

**What the model does NOT learn:**
- How to answer questions
- How to follow the format `"### Instruction: ... ### Response: ..."`
- How to stop talking and let the user continue

## 7.2 Full Fine-Tuning

**Definition:**
> Every single parameter in the model is updated during training.

```python
model = AutoModelForCausalLM.from_pretrained(model_name)
# No parameter freezing — everything is trainable

training_args = TrainingArguments(
    output_dir="./llama-pharma-domain",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=2,
    save_steps=500,
    learning_rate=2e-5,     # ← Small LR for full FT to avoid catastrophic forgetting
    fp16=True,
    report_to="none"
)

trainer = Trainer(model=model, args=training_args, train_dataset=tokenized)
trainer.train()
```

### Pros & Cons of Full Fine-Tuning

| Pros | Cons |
|---|---|
| Maximum learning capacity | Requires enormous VRAM (full parameter gradients) |
| Best possible adaptation quality | Risk of catastrophic forgetting |
| Proven results for small models | Expensive checkpoint storage (full model per save) |
| | Slow — all layers compute gradients |

**Memory cost for full fine-tuning:**
```
For each trainable parameter, you need:
  FP16 weight:        2 bytes
  FP32 gradient:      4 bytes
  Adam optimizer m₁:  4 bytes
  Adam optimizer m₂:  4 bytes
  ─────────────────────────────
  Total per param:   14 bytes (minimum)

TinyLlama-1.1B → 1.1B × 14 bytes ≈ 15.4 GB VRAM  (just for the model!)
```

## 7.3 Selective Layer Freezing

**Definition:**
> Freeze the early layers of the model. Only update the top N transformer blocks and the language modeling head (`lm_head`).

**Rationale:**
- Early layers encode fundamental grammar, syntax, and broad linguistic patterns — no need to re-learn these
- Top layers encode task-specific and high-level semantic representations — these are updated for domain content

```python
# Step 1: Freeze EVERYTHING
for param in model.parameters():
    param.requires_grad = False

# Step 2: Selectively unfreeze last 4 transformer blocks + lm_head
for name, param in model.named_parameters():
    if any(f"layers.{i}." in name for i in range(20, 24)):  # TinyLlama has 22 layers (0-21)
        param.requires_grad = True
    if "lm_head" in name:
        param.requires_grad = True

# Verification
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
total     = sum(p.numel() for p in model.parameters())
print(f"Trainable: {trainable/total*100:.2f}% of {total:,} parameters")
```

**What you typically see:**
```
Trainable: ~15-25% of 1,100,000,000 parameters
→ Only ~165M-275M params get gradients
→ VRAM requirement drops dramatically
```

### Which Layers Are Where (TinyLlama Example)

```
model.model.embed_tokens       ← Embedding Layer (FROZEN in freezing strategy)
model.model.layers.0           ← Layer 0 — very basic syntax (FROZEN)
model.model.layers.1           ← Layer 1 — morphology (FROZEN)
...
model.model.layers.18          ← Layer 18 — high-level semantics (TRAINED)
model.model.layers.19          ← Layer 19 — task representations (TRAINED)
model.model.layers.20          ← Layer 20 — output formatting (TRAINED)
model.model.layers.21          ← Layer 21 — final abstraction (TRAINED)
model.lm_head                  ← Output vocab projection (TRAINED)
```

## 7.4 LoRA (Low-Rank Adaptation)

See Section 8 for the complete mathematical deep dive. Summary here:

```python
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,  # Model is a decoder-only Causal LM
    r=8,                            # Low rank — dimension of adapter matrices
    lora_alpha=16,                  # Scaling factor (α = 2×r is standard)
    lora_dropout=0.05,              # Regularization dropout
    target_modules=["q_proj", "v_proj"],  # Which attention projections to adapt
    bias="none"                     # Don't fine-tune bias parameters
)

model_lora = get_peft_model(model, lora_config)
model_lora.print_trainable_parameters()
# Output: trainable params: 851,968 || all params: 1,100,048,384 || trainable%: 0.077
```

## 7.5 QLoRA (Quantized LoRA)

QLoRA combines 4-bit / 8-bit quantization with LoRA. The base model is loaded in compressed precision, and LoRA adapters are trained in FP16:

```python
from transformers import BitsAndBytesConfig

# 8-bit loading (simpler, still very effective)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,   # bitsandbytes INT8 loading
    device_map="auto"    # Automatically places model on GPU
)

# OR 4-bit loading (maximum VRAM savings)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",         # NormalFloat4 — best for LLM weights
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True     # Double quantization for extra savings
)
model = AutoModelForCausalLM.from_pretrained(
    model_name, quantization_config=bnb_config, device_map="auto"
)
```

### Memory Comparison: Full FT vs Selective Freeze vs LoRA vs QLoRA

| Method | Base Model VRAM | Trainable % | Total VRAM Estimate (1.1B) |
|---|---|---|---|
| Full Fine-Tuning (FP32) | ~4.4 GB | 100% | ~15 GB + optimizer states |
| Full Fine-Tuning (FP16) | ~2.2 GB | 100% | ~8 GB + gradients |
| Selective Layer Freezing | ~2.2 GB (FP16) | 15-25% | ~4-5 GB |
| LoRA (r=8, FP16) | ~2.2 GB | 0.077% | ~2.5 GB |
| QLoRA (8-bit + LoRA) | ~1.1 GB | 0.077% | ~1.5 GB |
| QLoRA (4-bit + LoRA) | ~0.55 GB | 0.077% | ~1.0 GB |

## 7.6 Training Loop & TrainingArguments

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./tinyllama-lora",         # Where to save checkpoints
    num_train_epochs=5,                     # 5 full passes over the dataset
    per_device_train_batch_size=1,          # 1 example per GPU per step
    gradient_accumulation_steps=8,         # Simulate batch_size=8 by accumulating
    learning_rate=2e-4,                    # LoRA uses higher LR than full FT
    fp16=True,                             # Use mixed precision (FP16) 
    logging_steps=20,                      # Log loss every 20 steps
    save_total_limit=1,                    # Keep only the latest checkpoint
    report_to="none"                       # Disable W&B, TensorBoard, etc.
)

trainer = Trainer(
    model=model_lora,
    args=training_args,
    train_dataset=tokenized_dataset
)

trainer.train()
```

**Effective batch size calculation:**
```
effective_batch_size = per_device_train_batch_size × gradient_accumulation_steps × num_GPUs
                     = 1 × 8 × 1
                     = 8  ← model sees 8 examples per parameter update
```

---

# 8. LoRA — Deep Dive

## 8.1 The Problem LoRA Solves

Fine-tuning a 7B parameter model fully requires:
- Storing gradients for 7B parameters × 4 bytes = **28 GB VRAM** just for gradients
- AdamW optimizer states (m₁, m₂) × 7B × 4 bytes each = **56 GB more**
- Total: **~100+ GB VRAM** — impossible on any consumer/prosumer GPU

LoRA's answer: **Freeze the original weights. Only train tiny rank-decomposed matrices.**

## 8.2 LoRA Mathematics

For any weight matrix `W₀ ∈ ℝ^(d×k)` in the network (e.g., Query projection), LoRA injects:

```
W_output = W₀ + ΔW
         = W₀ + (α/r) × (B × A)

Where:
  W₀ ∈ ℝ^(d×k)   ← Original frozen weight (not changed during training)
  A  ∈ ℝ^(r×k)   ← Low-rank matrix (random Gaussian init)
  B  ∈ ℝ^(d×r)   ← Low-rank matrix (ZERO init → ΔW=0 at start)
  r              ← Rank (hyperparameter, typically 4-16)
  α              ← Scaling factor (typically 16-32)
  α/r            ← Effective learning rate scaling
```

**Why initialize B=0?**
```
At training start:
  B = zeros → B × A = zeros matrix → ΔW = 0
  W_output = W₀ + 0 = W₀  (model starts identical to base!)

As training proceeds:
  B learns non-zero values
  W_output gradually diverges from W₀ in task-specific directions
```

### Parameter Count Comparison

```
Full weight matrix W₀ ∈ ℝ^(4096×4096):  4096 × 4096 = 16,777,216 parameters

LoRA with r=8:
  Matrix A:  8 × 4096   =    32,768 parameters
  Matrix B:  4096 × 8   =    32,768 parameters
  Total:              =    65,536 parameters   ← 256× fewer!

Parameter savings: 99.6% reduction in trainable parameters!
```

### Visual Architecture

```
Input x ──────────────────────────────────────────┐
         │                                         │
         ▼                                         │
  ┌──────────────────────┐                         │
  │  Frozen W₀           │                         │
  │  (Pre-trained)       │                         │
  │  d × k dims          │                         │
  └──────────────────────┘                         │
         │                                         │
         │                          LoRA path:     │
         │                          ┌──────────┐   │
         │                  x ──→  │ A (r×k)  │   │
         │                         └──────────┘   │
         │                              │          │
         │                          ┌──────────┐   │
         │                          │ B (d×r)  │   │
         │                         └──────────┘   │
         │                              │ ×α/r    │
         ▼                              ▼          │
    W₀x  ──────────────────────── +  BAx ─────────┘
                                   │
                                   ▼
                              Output (updated)
```

## 8.3 Which Layers to Target

| Layer Name | What it Does | Target for LoRA? |
|---|---|---|
| `q_proj` | Query projection in attention | ✅ Always (most impactful) |
| `v_proj` | Value projection in attention | ✅ Always (most impactful) |
| `k_proj` | Key projection in attention | ✅ Optional (add for more capacity) |
| `o_proj` | Output projection in attention | ✅ Optional |
| `up_proj` | Feed-forward network (up) | ⚡ Optional (larger model) |
| `gate_proj` | SwiGLU gate in FFN | ⚡ Optional |
| `down_proj` | Feed-forward network (down) | ⚡ Optional |
| `embed_tokens` | Token embeddings | ❌ Rarely (embed vocab rarely needs update) |
| `lm_head` | Output vocab projection | ❌ Keep frozen (affects all token probs) |

**Standard choices:**

```
Minimal (fast training):  target_modules=["q_proj", "v_proj"]
Balanced (recommended):   target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]
Maximum (full attention):  target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                                          "up_proj", "gate_proj", "down_proj"]
```

## 8.4 LoRA Config Reference Table

```python
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],
    bias="none"
)
```

| Parameter | Value | Meaning | Impact |
|---|---|---|---|
| `task_type` | `CAUSAL_LM` | Model type = decoder-only (GPT-style) | Ensures correct integration point |
| `r` | 4–16 | Rank of low-rank decomposition | Higher r = more capacity but more params |
| `lora_alpha` | 16–32 | Scaling factor for updates | Standard: set α = 2×r |
| `lora_dropout` | 0.05–0.1 | Dropout on LoRA activations | Regularization; prevents overfitting |
| `target_modules` | `["q_proj","v_proj"]` | Which linear layers get LoRA | More modules = more expressivity |
| `bias` | `"none"` | Whether to train bias terms | `"none"` = don't update biases |

**Rule of thumb for `r` vs `lora_alpha`:**

```
r=4,  alpha=8   → Very efficient, small datasets
r=8,  alpha=16  → Standard choice (most papers use this)
r=16, alpha=32  → Higher quality, more VRAM
r=64, alpha=128 → Full LoRA (comparable to full fine-tuning in quality)
```

## 8.5 Adapter Merging (`merge_and_unload`)

After Stage 1 training, LoRA weights can be merged permanently into the base model:

```python
from peft import PeftModel

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(model_name)

# Load Stage 1 LoRA adapter
stage1_peft = PeftModel.from_pretrained(base_model, "./stage1_domain_adapter")

# MERGE: fuses W₀ + ΔW into a single weight matrix
merged_model = stage1_peft.merge_and_unload()
# Result: merged_model has NO PEFT hooks — clean model with domain knowledge baked in!
```

**What `merge_and_unload()` does mathematically:**

```
Before merge:
  W_output = W₀ + (α/r)(B × A)   ← computed each forward pass

After merge:
  W_merged = W₀ + (α/r)(B × A)   ← permanently stored as single matrix
  LoRA matrices A and B are deleted
  Model returns to standard (non-PEFT) structure
```

**Why merge before Stage 2?**
```
Purpose: Free the PEFT hooks so a fresh Stage 2 LoRA can be attached cleanly
         to the domain-enriched weights.

Without merge: Stage 2 adapter would be applied ON TOP of Stage 1 adapter.
               Complex, messy, harder to save/load.

With merge: Clean slate. Stage 2 LoRA applied to weights that already know the domain.
```

---

# 9. Stage 2: Instruction Fine-Tuning (SFT — Supervised Fine-Tuning)

## 9.1 Why Continued Pre-training Alone Is Not Enough

After Stage 1, the model is a better autocompleter for domain text. But:

```
User asks : "Explain the mechanism of action of Metformin."

Stage 1 model output:
  "Explain the mechanism of action of Aspirin.
   Aspirin inhibits COX-1 and COX-2 enzymes...
   See also: Mechanism of Action of Ibuprofen. Chapter 4..."
   ← IT CONTINUED THE SENTENCE AS IF IT WERE A TEXTBOOK INDEX!

Stage 2 (Instruction-tuned) model output:
  "Metformin activates AMPK (AMP-activated protein kinase) in hepatic cells,
   which leads to:
   1. Inhibition of gluconeogenesis
   2. Increased glucose uptake in skeletal muscle
   3. Improved insulin sensitivity..."
   ← STRUCTURED, DIRECT, RESPONSIVE!
```

**The fundamental difference:**
```
Stage 1 model = understands WHAT "Metformin" is
Stage 2 model = understands WHAT TO DO when asked about it
```

## 9.2 Instruction Prompt Templates

The instruction format is how you structure input-output pairs. Different models use different conventions:

### 9.3 The Alpaca Format (Our Primary Template)

Stanford Alpaca's format is simple, widely supported, and easy to implement:

```
### Instruction:
{instruction}

### Input:
{optional_context}

### Response:
{target_response}
```

**Implementation:**

```python
def format_example(example):
    """
    Converts a raw dict with 'instruction', 'input', 'output' keys
    into Alpaca-formatted text string.
    """
    if example['input']:  # Has additional context
        prompt = (
            f"### Instruction:\n{example['instruction']}\n"
            f"### Input:\n{example['input']}\n"
            f"### Response:\n{example['output']}"
        )
    else:  # No additional context
        prompt = (
            f"### Instruction:\n{example['instruction']}\n"
            f"### Response:\n{example['output']}"
        )
    return {"text": prompt}

dataset = dataset.map(format_example)
```

**Real example output:**
```
### Instruction:
Explain the mechanism of action of Metformin.

### Input:
None

### Response:
Metformin activates AMP-activated protein kinase (AMPK), which increases
glucose uptake and fatty acid oxidation while inhibiting hepatic
gluconeogenesis, thereby lowering blood glucose levels.
```

### 9.4 LLaMA-2 Chat Format

Meta's official format for instruction-tuned LLaMA models:

```
<s>[INST] <<SYS>>
{system_message}
<</SYS>>

{user_message} [/INST] {assistant_response} </s>
```

Example:
```
<s>[INST] <<SYS>>
You are a helpful pharmacology assistant. Provide clear, accurate information.
<</SYS>>

Explain the mechanism of action of Metformin. [/INST]
Metformin primarily acts through AMPK activation... </s>
```

### 9.5 ChatML Format

OpenAI's format used by Mistral, Qwen, and many fine-tunes:

```
<|im_start|>system
You are a helpful assistant specialized in pharmacology.<|im_end|>
<|im_start|>user
Explain the mechanism of action of Metformin.<|im_end|>
<|im_start|>assistant
Metformin activates AMPK...<|im_end|>
```

### Format Comparison

| Format | Used By | Special Tokens | Best For |
|---|---|---|---|
| Alpaca | General community, Vicuna | None (pure text) | Simple instruction following |
| LLaMA-2 Chat | Meta LLaMA-2 family | `[INST]`, `<<SYS>>`, `</s>` | Multi-turn with system prompt |
| ChatML | GPT-4, Mistral, Qwen | `<|im_start|>`, `<|im_end|>` | Production assistants |
| Phi-3 | Microsoft Phi | `<|user|>`, `<|assistant|>` | Small efficient models |

**Important Rule:**
> Always use the same format at inference time that you used during training.
> Mixing formats at inference = gibberish output!

## 9.6 Benchmark Instruction Datasets

### Domain-Specific Instruction Datasets

| Dataset Identifier | Domain | Size | Key Characteristic |
|---|---|---|---|
| `Amod/mental_health_counseling_conversations` | Healthcare/Mental Health | ~3.5k dialogues | Multi-turn empathetic counseling |
| `medalpaca/medical_meadow_mediqa` | Medical QA | Large | Clinical question answering |
| `FreedomIntelligence/medical-o1-reasoning-SFT` | Medical Reasoning | Large | Step-by-step clinical reasoning |

### General Instruction Datasets

| Dataset Identifier | Domain | Size | Key Characteristic |
|---|---|---|---|
| `yahma/alpaca-cleaned` | General tasks | 52k pairs | Cleaned Stanford Alpaca (removes bad examples) |
| `tatsu-lab/alpaca` | General tasks | 52k pairs | Original Stanford Alpaca (GPT-3.5 generated) |
| `Open-Orca/OpenOrca` | Reasoning + CoT | 1M+ pairs | Detailed chain-of-thought reasoning |
| `OpenAssistant/oasst1` | Conversational | 66k trees | Human-generated multi-turn dialogs |
| `WizardLM/WizardLM_evol_instruct_70k` | Complex instructions | 70k pairs | Progressively complex instruction evolution |

### How to Inspect a Dataset

```python
from datasets import load_dataset

dataset = load_dataset("Amod/mental_health_counseling_conversations", split="train")
print(dataset)                    # Dataset({features: ['Context', 'Response'], num_rows: 3512})
print(dataset[0])                 # {'Context': 'I have been feeling...', 'Response': 'I can hear...'}
print(dataset.column_names)       # ['Context', 'Response']

# Format for instruction fine-tuning
def format_mental_health(example):
    return {
        "text": f"[INST] {example['Context']} [/INST] {example['Response']}"
    }

formatted = dataset.map(format_mental_health)
```

---

# 10. Response Masking — The Most Critical SFT Detail

## 10.1 The Problem Without Masking

If you train on full sequences (prompt + response) without masking, loss is computed on EVERY token:

```
Loss = Loss(Instruction tokens) + Loss(Response tokens)
```

**Why this is wrong:**

```
Token: [###, Instruction:, Explain, the, mechanism, of, Metformin, .,  ###, Response:, Metformin, activates, AMPK]
Loss:  [ ✗   ✗           ✗ ✗     ✗          ✗  ✗          ✗  ✗    ✗          ✓          ✓         ✓  ]
       └─────────────────────────────────── WASTED ────────────────────────┘ └────── CORRECT ──────┘
```

**The consequences:**
1. The model spends learning capacity memorizing prompt phrasing
2. At test time, prompts come from users — the model doesn't "write" them
3. Response quality degrades because optimizer is confused by gradient signal from prompts
4. The model might optimize to predict the `"### Instruction:"` header rather than useful responses

## 10.2 The `-100` Label Trick

PyTorch's `CrossEntropyLoss` has a special `ignore_index` parameter:

```python
loss_fn = torch.nn.CrossEntropyLoss(ignore_index=-100)
# Any position where labels[i] == -100 contributes ZERO to the loss!
# No gradient flows through those positions.
```

So we mask all prompt tokens by setting their label to `-100`:

```
Token:  [###,   Instruction:,   Explain,  ...  Response:,  Metformin,  activates,   AMPK ]
Labels: [-100,     -100,         -100,    ...   -100,       4819,       1823,         9402]
         ← IGNORED by loss  →                              ← TRAINED on these tokens    →
```

**Loss is ONLY computed on the response tokens!**

## 10.3 Masking Code Implementation

```python
def tokenize_and_mask(example):
    """
    Tokenizes instruction text and masks prompt tokens with -100.
    Loss is only computed on response tokens.
    """
    text = example["text"]   # Full formatted string: "### Instruction:\n...\n### Response:\n..."
    
    # Tokenize full text (prompt + response)
    enc = tokenizer(text, truncation=True, padding="max_length", max_length=512)
    input_ids = enc["input_ids"]
    
    # Find where '### Response:' starts
    response_marker = "### Response:"
    response_start = text.find(response_marker)
    
    if response_start != -1:
        # Tokenize ONLY the prefix text (everything before Response starts)
        prefix_text = text[:response_start + len(response_marker)]
        response_token_start = len(tokenizer(prefix_text, truncation=True)["input_ids"])
    else:
        response_token_start = 0  # Safety fallback — train on everything
    
    # Clone input_ids as labels
    labels = input_ids.copy()
    
    # Mask all prompt tokens (positions 0 to response_token_start)
    for i in range(response_token_start):
        labels[i] = -100
    
    # Also mask padding tokens
    for i in range(len(input_ids)):
        if input_ids[i] == tokenizer.pad_token_id:
            labels[i] = -100
    
    enc["labels"] = labels
    return enc

# Apply to dataset
tokenized = dataset.map(tokenize_and_mask, batched=False)
```

**Verification — check your masking is working:**

```python
sample_labels = tokenized[0]["labels"]
active_tokens = [l for l in sample_labels if l != -100]
masked_tokens = [l for l in sample_labels if l == -100]

print(f"Total tokens:   {len(sample_labels)}")
print(f"Masked (-100):  {len(masked_tokens)}  ← prompt + padding, no gradient")
print(f"Active tokens:  {len(active_tokens)}  ← response only, contributes to loss")
print(f"First 5 active: {active_tokens[:5]}")  # Should be start of response

# Decode active tokens to verify they're the response:
print(tokenizer.decode(active_tokens[:20]))  # Should print beginning of response
```

## 10.4 Verification Checklist

| Check | What to Look For |
|---|---|
| Masked ratio | 30-70% masked is healthy (depending on prompt length) |
| Active token content | Decoding active tokens should yield your response text |
| Loss decreasing | Loss should still decrease — too few active tokens = no learning |
| No all-masked samples | If all tokens are `-100`, that sample contributes nothing |

---

# 11. Two-Stage LoRA Pipeline

## 11.1 Stage 1 → Domain Adapter

```
Step 1: Start with TinyLlama base model (frozen)
Step 2: Attach Stage 1 LoRA adapter (q_proj, v_proj)
Step 3: Train on raw domain text (Metformin, Atorvastatin, mRNA, AI papers)
         ← Causal LM loss on ALL tokens (no masking)
         ← Model learns domain vocabulary & factual co-occurrences
Step 4: Save Stage 1 adapter to disk
```

```python
# Stage 1 training
stage1_lora = LoraConfig(task_type=TaskType.CAUSAL_LM, r=8, lora_alpha=16,
                         lora_dropout=0.05, target_modules=["q_proj","v_proj"], bias="none")
domain_model = get_peft_model(base_model, stage1_lora)
domain_trainer = Trainer(model=domain_model, args=stage1_args, train_dataset=tokenized_domain)
domain_trainer.train()
domain_model.save_pretrained("./stage1_domain_lora")
```

## 11.2 Merge & Unload

```
Step 5: Load Stage 1 adapter
Step 6: Call merge_and_unload()  ← permanently fuse ΔW_domain into W₀
         Resulting model = TinyLlama + domain knowledge, no PEFT overhead
Step 7: Now ready for Stage 2 fresh LoRA
```

```python
# Merge Stage 1 domain adapter
base = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
with_stage1 = PeftModel.from_pretrained(base, "./stage1_domain_lora")
merged = with_stage1.merge_and_unload()
# merged is now a standard AutoModelForCausalLM with domain knowledge baked in!
```

## 11.3 Stage 2 → Instruction Adapter

```
Step 8: Attach FRESH Stage 2 LoRA adapter to the merged model
Step 9: Train on instruction dataset WITH response masking
         ← Loss only on response tokens
         ← Model learns to follow instructions in Alpaca format
Step 10: Save final model
```

```python
# Stage 2 instruction tuning
stage2_lora = LoraConfig(task_type=TaskType.CAUSAL_LM, r=8, lora_alpha=16,
                         lora_dropout=0.05, target_modules=["q_proj","v_proj"], bias="none")
instruction_model = get_peft_model(merged, stage2_lora)
instruction_trainer = Trainer(model=instruction_model, args=stage2_args, train_dataset=tokenized_instructions)
instruction_trainer.train()
instruction_model.save_pretrained("./stage2_instruction_lora")
tokenizer.save_pretrained("./stage2_instruction_lora")
```

### Complete Two-Stage Flowchart

```
TinyLlama Base (1.1B, Frozen)
          │
          │ Attach Stage 1 LoRA
          ▼
[Base + Stage1 LoRA Adapters]
          │
          │ Train on raw domain text (Metformin.pdf, etc.)
          │ Loss: Causal LM on all tokens
          ▼
Domain-Adapted Model
(Understands "AMPK", "gluconeogenesis", "NPC1L1", etc.)
          │
          │ merge_and_unload()
          │ W_merged = W₀ + (α/r)(B₁×A₁)
          ▼
[Merged Model — clean, no PEFT hooks]
          │
          │ Attach Stage 2 LoRA
          ▼
[Merged + Stage2 LoRA Adapters]
          │
          │ Train on instruction pairs
          │ Loss: Causal LM with -100 masking on prompt tokens
          ▼
FINAL: Domain Specialist + Instruction-Following Assistant
       (Knows Pharmacology + Answers questions in structured format!)
```

---

# 12. Text Generation & Inference Control

## 12.1 Greedy vs Sampling

```python
# Greedy decoding — always pick the most probable next token
outputs = model.generate(**inputs, max_new_tokens=100, do_sample=False)

# Sampling — draw from the probability distribution
outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True, temperature=0.8)
```

**Comparison:**

| Strategy | Method | Output Style | Best For |
|---|---|---|---|
| Greedy Decoding | argmax at each step | Deterministic, often repetitive | Short factual answers |
| Beam Search | Keep top-k beams | Higher quality but conservative | Translation, summarization |
| Sampling | Draw from distribution | Creative, diverse | Creative writing, brainstorming |
| Nucleus (Top-P) | Restrict to top-p cumulative prob | Controlled creativity | Most dialog tasks |

## 12.2 Temperature

Temperature `T` rescales the logit distribution before softmax:

```
Standard softmax:      p_i = exp(z_i) / Σ exp(z_j)

With temperature T:    p_i = exp(z_i / T) / Σ exp(z_j / T)
```

**Effect:**

```
T = 0.1  → Almost deterministic (peaked distribution, very confident)
T = 0.7  → Balanced (good for factual domain questions)
T = 1.0  → Unchanged softmax (raw model probabilities)
T = 1.5  → Creative, risky, more hallucinations
T > 2.0  → Nearly random, incoherent
```

```python
# Conservative / factual
outputs = model.generate(**inputs, temperature=0.3, do_sample=True)

# Balanced / standard
outputs = model.generate(**inputs, temperature=0.7, do_sample=True)

# Creative / experimental
outputs = model.generate(**inputs, temperature=1.2, do_sample=True)
```

## 12.3 Top-P (Nucleus Sampling)

Only sample from the smallest set of tokens whose cumulative probability ≥ P:

```
Suppose vocabulary probs (sorted descending):
  "activates" = 0.42
  "inhibits"  = 0.28
  "promotes"  = 0.17   ← cumsum = 0.87 ≥ 0.85 (our top_p)
  "blocks"    = 0.08   ← would be excluded
  "enhances"  = 0.03   ← excluded
  ...rest...  ← all excluded

With top_p=0.85: sample from {"activates", "inhibits", "promotes"} only
```

```python
outputs = model.generate(**inputs, top_p=0.9, do_sample=True, temperature=0.8)
```

**Rule:** Higher top_p = more diverse (include more tokens). Lower top_p = more focused.

## 12.4 Top-K

Restrict sampling to only the K most probable tokens:

```python
outputs = model.generate(**inputs, top_k=50, do_sample=True)
# Only consider the 50 most probable next tokens at each step
```

**Top-K vs Top-P:**

| Approach | Method | Issue |
|---|---|---|
| Top-K | Fixed count of candidates (e.g., always 50) | When distribution is peaked, K=50 includes bad tokens; when flat, too restrictive |
| Top-P | Dynamic count based on cumulative prob | Adapts to distribution shape — better in practice |

In practice: **Use Top-P instead of Top-K, or combine both.**

## 12.5 Repetition Penalty

Penalizes tokens that have already appeared in the output:

```python
outputs = model.generate(**inputs, repetition_penalty=1.15)
# logit of already-generated tokens divided by 1.15 before sampling
```

```
Without penalty: "Metformin activates AMPK. AMPK activates AMPK. AMPK is activated by..."
With penalty 1.15: "Metformin activates AMPK, leading to improved glucose uptake and..."
```

**Values:**
```
1.0  = No penalty (default)
1.1  = Mild — reduces obvious loops
1.15 = Standard — good balance
1.3  = Strong — forces topic variety (sometimes too aggressive)
```

## 12.6 Beam Search

Maintains K candidate sequences (beams) simultaneously:

```
Beam width = 3
Step 1: ["Metformin a...", "Metformin is...", "Metformin acts..."]
Step 2: expand each beam with top tokens, keep best 3
...
Final: return highest-scoring complete sequence
```

```python
outputs = model.generate(**inputs, num_beams=4, max_new_tokens=100)
```

**When to use beam search:** Translation, structured summarization, code generation where quality matters more than speed.

### Complete Generation Example

```python
prompt = "### Instruction:\nExplain the mechanism of action of Metformin.\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=150,       # Don't generate more than 150 new tokens
    temperature=0.7,           # Balanced creativity
    top_p=0.9,                 # Nucleus sampling — focus on top 90% probability mass
    do_sample=True,            # Enable sampling (not greedy)
    repetition_penalty=1.15,   # Prevent repetitive loops
    pad_token_id=tokenizer.eos_token_id  # Needed if pad token not set
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# Extract only the response part:
if "### Response:" in response:
    response = response.split("### Response:")[1].strip()
print(response)
```

---

# 13. Preference Alignment (RLHF & DPO)

After SFT, models follow instructions — but they may still:
- Be verbose when conciseness is better
- Hallucinate confidently
- Be sycophantic (agree with wrong claims)
- Produce unsafe or biased outputs

**Preference Alignment** teaches the model WHAT KIND of response is preferred, not just how to respond.

## 13.1 What Alignment Means

```
SFT teaches: "What answer to give"
Alignment teaches: "How good is this answer vs that answer"

Example:
  Prompt: "Is Metformin safe in pregnancy?"
  
  Response A (bad): "Yes, absolutely safe! Give it without worry."
  Response B (good): "Metformin is classified as FDA Category B in pregnancy.
                      Evidence is mixed — some studies show safety while others
                      urge caution. Clinical judgment and ob/gyn consultation
                      are recommended."

Alignment: Model learns to prefer Response B over Response A.
```

## 13.2 RLHF Pipeline (PPO)

**RLHF = Reinforcement Learning from Human Feedback**

The full pipeline has 3 steps:

### Step 1: Collect Preference Data
```
Human raters see: Prompt + Response A + Response B
They pick the better response.
Dataset: {prompt, chosen_response, rejected_response}
```

### Step 2: Train a Reward Model
```
Reward Model RM: inputs (prompt, response) → scalar score

Trained to score chosen responses higher than rejected ones:
  Loss = -log(σ(RM(x, y_chosen) - RM(x, y_rejected)))
       = Bradley-Terry preference model
```

### Step 3: PPO Optimization
```
Maximize expected reward while staying close to SFT policy:

max_π E_{x,y~π}[RM(x,y)] - β × KL(π(y|x) || π_ref(y|x))

Where:
  π       = current policy (our model being trained)
  π_ref   = reference model (SFT model — we don't want to drift too far)
  β       = KL coefficient (typically 0.1 — controls how much we can change)
  RM(x,y) = reward from the reward model
  KL      = Kullback-Leibler divergence penalty (prevents reward hacking)
```

**The KL penalty is critical:** Without it, the model learns to "game" the reward model by producing nonsense that tricks it into giving high scores.

### RLHF Pipeline Flow

```
SFT Model (Stage 2)
     │
     ├──────────────────────────────────────────┐
     │                                          │
     ▼                                          ▼
Reward Model Training              Policy Optimization (PPO)
(on preference pairs)              (maximize reward - KL penalty)
     │                                          │
     ▼                                          ▼
RM outputs scalar score        Policy generates response
for any (prompt, response)     RM scores it
                               PPO updates policy to increase score
                                    │
                                    ▼
                              RLHF-Aligned Model
```

## 13.3 Direct Preference Optimization (DPO) — Math

**DPO eliminates the reward model entirely!**

It uses the closed-form relationship between the optimal reward and optimal policy:

```
The optimal policy satisfying the RLHF objective is:
  π*(y|x) = π_ref(y|x) × exp(RM*(x,y)/β) / Z(x)

Where Z(x) is a partition function (normalization constant).

Inverting this:
  RM*(x,y) = β × log(π*(y|x)/π_ref(y|x)) + β × log Z(x)

Substituting into the Bradley-Terry loss and simplifying:
  L_DPO(π_θ; π_ref) = -E_{(x, y_w, y_l)}[
    log σ(
      β × log(π_θ(y_w|x)/π_ref(y_w|x))  ←  ratio for "winning" response
      -
      β × log(π_θ(y_l|x)/π_ref(y_l|x))  ←  ratio for "losing" response
    )
  ]

Where:
  y_w = chosen (winning) response
  y_l = rejected (losing) response
  σ   = sigmoid function
  β   = temperature (typically 0.1)
  π_θ = our training model
  π_ref = reference SFT model (frozen)
```

**In plain English:**
> DPO trains the model to assign higher probability to chosen responses relative to the reference model, and lower probability to rejected responses — all without any reward model!

### DPO Implementation with TRL

```python
from trl import DPOTrainer, DPOConfig

# Dataset format: {"prompt": ..., "chosen": ..., "rejected": ...}

dpo_config = DPOConfig(
    beta=0.1,                # KL penalty coefficient
    output_dir="./dpo-model",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    learning_rate=5e-7,      # Very small LR for alignment (don't overfit)
    fp16=True,
    report_to="none"
)

trainer = DPOTrainer(
    model=instruction_model,    # The SFT model to align
    ref_model=ref_model,        # Frozen copy of SFT model (or None — auto-creates)
    tokenizer=tokenizer,
    train_dataset=preference_dataset,
    args=dpo_config
)

trainer.train()
```

## 13.4 DPO vs RLHF Comparison

| Aspect | RLHF (PPO) | DPO |
|---|---|---|
| Reward Model | Required (extra training) | Not needed! |
| Training Steps | 3 (SFT → RM → PPO) | 2 (SFT → DPO) |
| Complexity | High (PPO has many hyperparameters) | Low (just a loss function) |
| Stability | Less stable (PPO can be unstable) | More stable |
| Compute Cost | Very high (RM + policy training) | Lower (just one model) |
| Quality | Excellent | Comparable / sometimes better |
| Popular Use | InstructGPT, early ChatGPT | LLaMA-2-Chat, Mistral-Instruct |

## 13.5 Preference Datasets

| Dataset | Focus | Scale | Key Format |
|---|---|---|---|
| `Anthropic/hh-rlhf` | Helpful & Harmless responses | 160k dialogs | `{chosen: ..., rejected: ...}` |
| `argilla/ultrafeedback-binarized-preferences-cleaned` | General instruction quality | 60k pairs | Multi-attribute ranked pairs |
| `xinlai/Math-Step-DPO-10K` | Mathematical step reasoning | 10k steps | Correct vs incorrect derivations |
| `Intel/orca_dpo_pairs` | Chain-of-thought reasoning | 12.9k pairs | GPT-4 vs weaker model |
| `lvwerra/stack-exchange-paired` | Programming Q&A | 1M+ pairs | Upvoted vs downvoted SO answers |

---

# 14. Memory & Hardware Economics of Fine-Tuning

## 14.1 VRAM Breakdown

When fine-tuning on a GPU, VRAM is consumed by:

```
1. Model Parameters (weights)
   FP32: 4 bytes/param
   FP16: 2 bytes/param
   INT8: 1 byte/param
   INT4: 0.5 bytes/param

2. Gradients (same precision as params, only for trainable params)
   FP32: 4 bytes/trainable param

3. Optimizer States (AdamW)
   m₁ (momentum):   4 bytes/trainable param
   m₂ (variance):   4 bytes/trainable param
   Total AdamW:     8 bytes/trainable param + sometimes FP32 master weights

4. Activations (forward pass cache for backprop)
   Scales with: batch_size × sequence_length × hidden_dim × num_layers

5. Overhead (CUDA context, PyTorch memory manager, etc.)
   Typically 500MB - 2GB
```

### Real VRAM Estimates for TinyLlama-1.1B

| Configuration | Model Weights | Gradients | Optimizer | Activations | Total (approx) |
|---|---|---|---|---|---|
| Full FT (FP32) | 4.4 GB | 4.4 GB | 8.8 GB | ~2 GB | ~20 GB |
| Full FT (FP16) | 2.2 GB | 2.2 GB | 8.8 GB (FP32 optim) | ~1 GB | ~14 GB |
| Selective Freeze (FP16) | 2.2 GB | 0.5 GB | 1.0 GB | ~0.7 GB | ~4.5 GB |
| LoRA r=8 (FP16) | 2.2 GB | 0.01 GB | 0.02 GB | ~0.5 GB | ~3 GB |
| QLoRA 8-bit + LoRA | 1.1 GB | 0.01 GB | 0.02 GB | ~0.4 GB | ~2 GB |
| QLoRA 4-bit + LoRA | 0.55 GB | 0.01 GB | 0.02 GB | ~0.3 GB | ~1 GB |

## 14.2 Mixed Precision (FP16 / BF16)

HuggingFace Trainer handles mixed precision automatically:

```python
# FP16 — supported on all modern Ampere and newer NVIDIA GPUs
training_args = TrainingArguments(..., fp16=True)

# BF16 — better numerical stability, supported on A100, H100, 3090, 4090
training_args = TrainingArguments(..., bf16=True)
```

**FP16 vs BF16:**

| Property | FP16 | BF16 |
|---|---|---|
| Exponent bits | 5 | 8 (same as FP32!) |
| Mantissa bits | 10 | 7 |
| Range | Narrower (overflow risk) | Same as FP32 (no overflow) |
| Precision | Higher | Lower |
| Training stability | Needs loss scaling | Stable without loss scaling |
| Best for | Inference, lightweight FT | Training large models |

## 14.3 Gradient Accumulation

When batch_size=1 is too small but VRAM can't fit larger batches:

```python
training_args = TrainingArguments(
    per_device_train_batch_size=1,    # Only 1 sample fits in memory
    gradient_accumulation_steps=8,    # Accumulate 8 steps before updating
)
# Effective batch size = 1 × 8 = 8 (same as if batch_size=8 fit in memory!)
```

**How it works:**
```
Step 1: Forward pass on sample 1 → compute loss → backward pass → store gradient
Step 2: Forward pass on sample 2 → compute loss → backward pass → ACCUMULATE gradient
...
Step 8: Forward pass on sample 8 → compute loss → backward pass → ACCUMULATE gradient
        → NOW call optimizer.step() → clear accumulated gradients
```

**Trade-off:** Effective batch size is the same, but 8× more forward/backward passes (slower per effective update).

## 14.4 Model Memory Table — All Common LLMs

| Model | Parameters | FP16 Size | 8-bit Size | 4-bit Size | GPU Required |
|---|---|---|---|---|---|
| TinyLlama-1.1B | 1.1B | 2.2 GB | 1.1 GB | 0.55 GB | RTX 3060 12GB |
| Phi-2 (2.7B) | 2.7B | 5.4 GB | 2.7 GB | 1.35 GB | RTX 3060 12GB |
| LLaMA-2-7B | 7B | 14 GB | 7 GB | 3.5 GB | RTX 3090/4090 |
| LLaMA-2-13B | 13B | 26 GB | 13 GB | 6.5 GB | 2× RTX 3090 |
| LLaMA-2-70B | 70B | 140 GB | 70 GB | 35 GB | 4–8× A100 80GB |
| Mixtral-8×7B | ~47B | ~94 GB | ~47 GB | ~24 GB | 2–4× A100 |

---

# 15. TrainingArguments — Complete Reference

```python
from transformers import TrainingArguments

args = TrainingArguments(
    # === OUTPUT & CHECKPOINTING ===
    output_dir="./model-output",          # Where to save model + checkpoints
    overwrite_output_dir=True,            # Overwrite existing output dir
    save_strategy="epoch",                # When to save: "epoch", "steps", "no"
    save_steps=500,                       # Save checkpoint every 500 steps
    save_total_limit=2,                   # Keep only last 2 checkpoints (saves disk)
    
    # === TRAINING EPOCHS & BATCHING ===
    num_train_epochs=3,                   # 3 complete passes over dataset
    per_device_train_batch_size=1,        # Samples per GPU per step
    per_device_eval_batch_size=4,         # Samples per GPU per eval step
    gradient_accumulation_steps=8,        # Accumulate 8 steps before update
    
    # === LEARNING RATE ===
    learning_rate=2e-4,                   # 2e-4 for LoRA, 2e-5 for full FT
    weight_decay=0.01,                    # L2 regularization
    lr_scheduler_type="cosine",           # LR schedule: cosine decay
    warmup_ratio=0.03,                    # 3% of steps used for LR warmup
    warmup_steps=0,                       # OR fixed warmup steps (use one or other)
    
    # === PRECISION ===
    fp16=True,                            # FP16 mixed precision (most GPUs)
    bf16=False,                           # BF16 (A100/H100 preferred)
    
    # === LOGGING ===
    logging_dir="./logs",                 # TensorBoard log directory
    logging_steps=20,                     # Log every 20 training steps
    logging_first_step=True,              # Log the very first step
    report_to="none",                     # "none", "wandb", "tensorboard", "all"
    
    # === EVALUATION ===
    evaluation_strategy="epoch",          # When to evaluate: "epoch", "steps", "no"
    eval_steps=500,                       # Eval every 500 steps if "steps"
    load_best_model_at_end=True,          # Load best checkpoint at end of training
    metric_for_best_model="eval_loss",    # Which metric to track for best model
    
    # === OPTIMIZATION ===
    optim="adamw_torch",                  # Optimizer: "adamw_torch", "adamw_8bit"
    max_grad_norm=1.0,                    # Gradient clipping threshold
    
    # === DATALOADER ===
    dataloader_num_workers=0,             # CPU workers for data loading
    dataloader_pin_memory=True,           # Pin tensors to VRAM for faster transfer
    
    # === EFFICIENCY ===
    group_by_length=True,                 # Group similar-length sequences for efficiency
    gradient_checkpointing=True,          # Trade compute for memory (saves ~20% VRAM)
    auto_find_batch_size=False,           # Auto-detect largest batch size that fits
)
```

| Hyperparameter | Domain FT (Stage 1) | Instruction FT (Stage 2) | Notes |
|---|---|---|---|
| `num_train_epochs` | 2–5 | 3–10 | Instruction FT may need more epochs on small datasets |
| `learning_rate` | 1e-4 to 3e-4 | 2e-4 to 5e-4 | Higher LR for LoRA (fewer params) |
| `per_device_batch_size` | 1–2 | 1 | 1 is typical for large models on single GPU |
| `gradient_accumulation` | 8–16 | 4–8 | Compensates for small batch size |
| `fp16` | True | True | Always use if GPU supports it |
| `save_total_limit` | 1 | 1–2 | Saves disk space |
| `warmup_ratio` | 0.03 | 0.05 | SFT benefits from slightly longer warmup |

---

# 16. Common Fine-Tuning Pitfalls & How to Fix Them

## Problem 1: Loss Not Decreasing

```
Symptom: Training loss stays flat or oscillates
Causes:
  - Learning rate too low → increase LR by 5-10×
  - Learning rate too high → decrease LR by 5-10×
  - Dataset too small → need at least 100-1000 examples
  - All labels masked to -100 → check response masking logic

Fix checklist:
  □ Print loss every 5-10 steps to confirm it's decreasing
  □ Check learning rate (LoRA: 2e-4, full FT: 2e-5)
  □ Verify at least some labels are NOT -100
  □ Ensure dataset has enough diversity (not identical examples)
```

## Problem 2: CUDA Out of Memory (OOM)

```
Error: RuntimeError: CUDA out of memory

Fixes (try in order):
  1. Reduce per_device_train_batch_size to 1
  2. Increase gradient_accumulation_steps to compensate
  3. Enable gradient_checkpointing=True in TrainingArguments
  4. Reduce max_length from 512 to 256
  5. Switch to LoRA if doing full fine-tuning
  6. Use load_in_8bit=True or load_in_4bit=True

Quick debug:
  import torch, gc
  gc.collect()
  torch.cuda.empty_cache()
  torch.cuda.memory_summary()  # Shows what's using VRAM
```

## Problem 3: Model Generates Repetitive Output

```
Symptom: Model loops: "AMPK activates AMPK. AMPK activates AMPK."

Causes:
  - repetition_penalty not set
  - Temperature too low
  - Model didn't converge properly

Fix:
  outputs = model.generate(
      **inputs,
      repetition_penalty=1.15,  # ← ADD THIS
      temperature=0.7,           # ← Raise if too low
      top_p=0.9
  )
```

## Problem 4: Catastrophic Forgetting

```
Symptom: After fine-tuning, model forgets how to do general tasks.

Causes:
  - Learning rate too high in full fine-tuning
  - Too many epochs on tiny dataset

Fix:
  - Use LoRA instead of full fine-tuning
  - Reduce learning rate (2e-5 instead of 2e-4 for full FT)
  - Mix some general instruction data with domain-specific data
  - Reduce num_train_epochs
```

## Problem 5: Response Format Not Followed

```
Symptom: Model ignores "### Response:" and continues the prompt

Causes:
  - Instruction dataset too small (<100 examples)
  - Inconsistent formatting in training data
  - Missing response masking → prompt tokens confuse the model

Fix:
  - Ensure all training examples use EXACTLY the same template
  - Add at least 500-1000 high-quality instruction pairs
  - Verify response masking is applied correctly
  - Test with the EXACT prompt format used during training
```

## Problem 6: Tokenizer Pad Token Warning

```
Warning: tokenizer does not have a padding token

Fix:
  if tokenizer.pad_token is None:
      tokenizer.pad_token = tokenizer.eos_token
      tokenizer.pad_token_id = tokenizer.eos_token_id

Why: TinyLlama and LLaMA-based models don't have a dedicated <pad> token.
     Setting it to EOS is the standard workaround.
```

---

# 17. Fine-Tuning Datasets Master Reference

## Non-Instruction (Continued Pre-training) Datasets

| Dataset | Domain | Size | HF Link |
|---|---|---|---|
| `HuggingFaceFW/fineweb` | General web text | 15T tokens | Best for continued pretraining |
| `ncbi/pubmed` | Biomedical abstracts | Millions | Medical domain adaptation |
| `datajuicer/the-pile-pubmed-abstracts-refined-by-data-juicer` | Medical | Filtered | High-quality biomedical |
| `open-llm-leaderboard/open_llm_corpus` | Research papers | Large | Scientific language |
| `Skylion007/openwebtext` | Web text | 40GB | General pretraining |
| `armanc/scientific_papers` | arXiv + PubMed | Long-form | Scientific writing |
| `roneneldan/TinyStories` | Synthetic stories | 2M | SLM benchmarking |
| `EleutherAI/the_pile` | Diverse (25 sources) | 825GB | Comprehensive pretraining mix |

## Instruction Fine-Tuning Datasets

| Dataset | Domain | Size | Format |
|---|---|---|---|
| `Amod/mental_health_counseling_conversations` | Healthcare | 3.5k | Context/Response |
| `yahma/alpaca-cleaned` | General | 52k | Instruction/Input/Output |
| `tatsu-lab/alpaca` | General | 52k | Instruction/Input/Output |
| `Open-Orca/OpenOrca` | Reasoning CoT | 1M+ | System/User/Assistant |
| `OpenAssistant/oasst1` | Conversational | 66k | Multi-turn trees |
| `WizardLM/WizardLM_evol_instruct_70k` | Complex | 70k | Instruction/Output |
| `databricks/databricks-dolly-15k` | General | 15k | Human-written |
| `HuggingFaceH4/ultrachat_200k` | Multi-turn chat | 200k | Human-like dialogs |
| `meta-math/MetaMathQA` | Mathematics | 395k | Math instruction-response |

## Preference Alignment Datasets

| Dataset | Domain | Size | Format |
|---|---|---|---|
| `Anthropic/hh-rlhf` | Helpful & Harmless | 160k | chosen/rejected |
| `argilla/ultrafeedback-binarized-preferences-cleaned` | General | 60k | chosen/rejected |
| `xinlai/Math-Step-DPO-10K` | Math reasoning | 10k | step-level preferred/rejected |
| `Intel/orca_dpo_pairs` | Reasoning | 12.9k | GPT-4 vs weaker model |
| `lvwerra/stack-exchange-paired` | Programming | 1M+ | Upvoted/downvoted answers |
| `jondurbin/airoboros-3.1` | Multi-domain | 33k | Curated instruction pairs |

---

# 18. Decision Guide — When to Use What

## By Fine-Tuning Objective

| Goal | Recommended Method | Why |
|---|---|---|
| Add domain vocabulary (pharma, legal, finance) | Stage 1 Continued Pretraining + LoRA | Causal LM on raw text ingests domain facts |
| Teach instruction following & Q&A | Stage 2 SFT with Response Masking | Explicit prompt→response training |
| Improve tone, safety, conciseness | Stage 3 DPO | Preference pairs directly optimize output quality |
| Single GPU, limited VRAM | QLoRA (4-bit) | Largest VRAM savings with minimal quality loss |
| Highest quality possible | Full fine-tuning on multi-GPU | All params updated |
| Fast prototyping | LoRA r=4, small dataset | Minimal setup, fast iteration |

## By Hardware Available

```
Available VRAM → Recommended Strategy:
┌──────────────────────────────────────────────────────────────────┐
│ < 8 GB  → QLoRA (4-bit), max_length=128, batch_size=1            │
│ 8-12 GB → LoRA (r=8), max_length=256, batch_size=1               │
│ 16 GB   → LoRA (r=16), max_length=512, batch_size=2              │
│ 24 GB   → LoRA (r=32) or selective freezing, max_length=512      │
│ 40 GB+  → Full fine-tuning (FP16), max_length=2048               │
│ 80 GB+  → Full fine-tuning (BF16), large batch, long context     │
└──────────────────────────────────────────────────────────────────┘
```

## By Dataset Size

| Dataset Size | Strategy | Expected Outcome |
|---|---|---|
| < 100 examples | LoRA, few epochs | Rapid overfitting — use for toy experiments only |
| 100–1,000 | LoRA, r=4-8, heavy regularization | Usable specialization, watch for overfitting |
| 1,000–10,000 | LoRA r=8-16, standard settings | Good domain specialization |
| 10,000–100,000 | LoRA r=16-32 or selective freeze | Strong instruction following |
| 100,000+ | Full fine-tuning or large LoRA | Production-grade specialist model |

## Fine-Tuning Strategy Comparison Matrix

```
┌────────────────────────────────────────────────────────────────────────────────────┐
│                      FINE-TUNING STRATEGIES COMPARISON                             │
├───────────────────────┬─────────────────────────┬──────────────────────────────────┤
│ Full Fine-Tuning      │ Selective Layer Freeze  │ LoRA / QLoRA (PEFT)              │
├───────────────────────┼─────────────────────────┼──────────────────────────────────┤
│ Updates 100% params   │ Freezes early layers    │ Freezes 100% base params         │
│                       │ Unfreezes top N + head  │ Adds trainable low-rank matrices │
│ Highest VRAM cost     │ 10-25% params trained   │ < 0.2% params trained            │
│ (~14 bytes/param)     │                         │                                  │
│ Risk: catastrophic    │ Good compromise          │ Minimal VRAM footprint           │
│ forgetting            │                         │ Enables adapter swapping         │
│ Slow training         │ Moderate speed          │ Fast training                    │
│ Best quality ceiling  │ Good quality            │ Near-full-quality in practice    │
└───────────────────────┴─────────────────────────┴──────────────────────────────────┘
```

---

# 19. Key Formulas Quick Reference

```
CAUSAL LM LOSS:
  L_CLM(θ) = -Σ log P_θ(w_t | w_1,...,w_{t-1})

LABEL SETUP (Non-Instruction):
  labels = input_ids.copy()
  (All tokens contribute to loss)

LABEL SETUP (Instruction — Response Masking):
  labels[i] = -100  for i < response_start  ← masked, ignored by loss
  labels[i] = input_ids[i]  for i >= response_start  ← trained

LORA WEIGHT UPDATE:
  W_output = W₀ + (α/r)(B × A)
  A ∈ ℝ^(r×k)  initialized: Gaussian
  B ∈ ℝ^(d×r)  initialized: zeros (ensures ΔW=0 at start)

LORA PARAMETER SAVINGS:
  Original W₀: d × k parameters
  LoRA: r×k + d×r = r(d+k) parameters
  Savings: (d×k - r(d+k)) / (d×k) ≈ 1 - r/min(d,k)
  For d=k=4096, r=8: savings = 99.6%

TEMPERATURE:
  p_i(T) = exp(z_i/T) / Σ exp(z_j/T)
  T→0: greedy (argmax)
  T=1: raw distribution
  T>1: flattened (more random)

PPO RLHF OBJECTIVE:
  max_π E[RM(x,y)] - β × KL(π(y|x) || π_ref(y|x))

DPO LOSS:
  L_DPO = -E[(x,y_w,y_l)][log σ(β log(π_θ(y_w|x)/π_ref(y_w|x))
                                - β log(π_θ(y_l|x)/π_ref(y_l|x)))]

EFFECTIVE BATCH SIZE:
  effective_bs = per_device_bs × gradient_accumulation_steps × num_GPUs

VRAM ESTIMATE (LoRA):
  VRAM ≈ model_params × bytes_per_param + (trainable_params × 4 + 8) bytes + activations
  For TinyLlama LoRA FP16: ≈ 2.2 GB base + 0.1 GB LoRA states + ~0.5 GB activations ≈ 3 GB
```

---

# 20. Mental Model Summary

```
START: General Purpose Pre-trained LLM (e.g., TinyLlama-1.1B)
       Knows: General language, world knowledge, basic reasoning
       Doesn't know: Medical pharmacology, how to answer clinical questions
            │
            ▼
STAGE 1: NON-INSTRUCTION DOMAIN FINE-TUNING
  Input: Raw unstructured PDFs / research papers
  Loss:  Causal LM on ALL tokens
  Method: LoRA (r=8, target q_proj+v_proj)
  Output: Domain-adapted model
         - Knows: "AMPK", "gluconeogenesis", "NPC1L1", "mRNA LNPs"
         - Still: Autocompleter — doesn't know to answer questions
            │
            │ merge_and_unload()  ← bake domain weights permanently
            ▼
STAGE 2: INSTRUCTION FINE-TUNING (SFT)
  Input: Structured prompt-response pairs (Alpaca format)
  Loss:  Causal LM with RESPONSE MASKING (-100 on prompt tokens)
  Method: Fresh LoRA (r=8, target q_proj+v_proj)
  Output: Domain Specialist Assistant
         - Knows: Domain facts + HOW to answer questions
         - Responds in structured "### Response:" format
         - Follows "### Instruction: ... ### Response:" pattern
            │
            ▼
STAGE 3 (OPTIONAL): PREFERENCE ALIGNMENT (DPO / RLHF)
  Input: {prompt, chosen_response, rejected_response} triplets
  Loss:  DPO loss comparing chosen vs rejected responses
  Output: Aligned Specialist
         - Safe, concise, calibrated uncertainty
         - Won't hallucinate confidently
         - Won't give dangerous medical advice without caveats
            │
            ▼
PRODUCTION DEPLOYMENT:
  - Export merged weights to .safetensors (HuggingFace / vLLM)
  - OR convert to GGUF for CPU/edge deployment (llama.cpp)
  - Run with vLLM, TGI, Ollama, or llama.cpp

RESULT: A specialized, instruction-following, safe domain expert!
```

---

*Source: `05_finetuning/Instruction_finetuning_on_domain_specific_dataset.ipynb` + `non_Instruction_pretrain_llm_finetuning_on_domain_specific_data.ipynb`*
*Topics: Data engineering → Causal LM → Full FT vs LoRA → SFT → Response Masking → DPO/RLHF → Production*

