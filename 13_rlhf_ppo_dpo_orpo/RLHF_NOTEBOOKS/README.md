# Executable RL and LLM alignment notebooks

Thirteen progressive notebooks connect the source PDFs, original notebook behavior, real20-row preference schema, and corrected RLHF_COMPLETE_NOTES to executable demonstrations. All default training is small CPU work using synthetic environments, a character GRU, or a randomly initialized local GPT-2 architecture. No pretrained checkpoints are downloaded automatically. Real-model GPU sections are guarded by `RUN_PRETRAINED_GPU = False`.

## Learning order

| Notebook | Implementation and purpose | Default resources |
|---|---|---|
| [01 RL fundamentals](01_RL_Fundamentals.ipynb) | Returns, crossroad values, exact Bellman solution, real chain Q-learning | CPU, PyTorch/NumPy |
| [02 Policy gradients/actor-critic](02_Policy_Gradients_Actor_Critic.ipynb) | REINFORCE with learned baseline, detached advantages, GAE and truncation tests | CPU |
| [03 Reward modeling](03_RLHF_Reward_Modeling.ipynb) | Actual dataset audit/split, bag-of-words Bradley–Terry reward model | CPU |
| [04 PPO from scratch](04_PPO_From_Scratch.ipynb) | Episodic rollouts, fixed old logps, minibatches, actor/critic/entropy, GAE | CPU |
| [05 PPO LLM fine-tuning](05_PPO_LLM_Finetuning.ipynb) | RewardTrainer then four-model token PPO; optional pretrained workflow | Local tiny CPU trainer; optional CUDA |
| [06 DPO from scratch](06_DPO_From_Scratch.ipynb) | KL derivation, response-masked causal logps, frozen reference GRU training | CPU |
| [07 DPO using TRL](07_DPO_Using_TRL.ipynb) | Local tiny trainer, metrics, masks, checkpoints/reload; optional pretrained LoRA | CPU smoke; optional CUDA |
| [08 GRPO from scratch](08_GRPO_From_Scratch.ipynb) | Group-normalized rewards and one-token contextual policy with exact KL | CPU |
| [09 GRPO using TRL](09_GRPO_Using_TRL.ipynb) | Numeric reward parsing, explicit grouping/loss variant, local trainer | CPU smoke; optional CUDA |
| [10 ORPO from scratch](10_ORPO_From_Scratch.ipynb) | Stable geometric-likelihood odds, NLL plus preference, GRU training | CPU |
| [11 ORPO using TRL](11_ORPO_Using_TRL.ipynb) | Local trainer, evaluation/save/reload; optional LoRA | CPU smoke; optional CUDA |
| [12 Algorithm comparison](12_PPO_DPO_GRPO_ORPO_Comparison.ipynb) | Objectives, roles, analytical plots, assumed state-memory and selection | CPU |
| [13 End-to-end alignment](13_End_to_End_LLM_Alignment.ipynb) | SFT baseline, DPO/ORPO from same starting weights, fixed validation/test, export/reload | CPU |

Each notebook has learning objectives, symbol-by-symbol equations, implementation mapping, runnable examples, exercises and takeaways. Code needed for core losses/masking is repeated deliberately so notebooks run independently. Examples distinguish educational weighting choices and faithful objective components from library variants. Mathematical comparisons do not equate incomparable loss scales.

## Setup

Run from this directory, the module directory, or repository root. Python3.12/3.13 is recommended; actual validation environment is recorded in `resolved-environment.txt`. CPU PyTorch2.8.0, Transformers4.56.2, TRL0.22.2, Datasets4.3.0, PEFT0.17.1 and Accelerate1.10.1 form the chosen API environment. No unpinned notebook pip-upgrades or mixed live install sections are used.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --index-url https://download.pytorch.org/whl/cpu torch==2.8.0
.venv/bin/python -m pip install --cache-dir .cache/pip -r requirements-cpu.txt
.venv/bin/python -m pip install --cache-dir .cache/pip jupyterlab
JUPYTER_RUNTIME_DIR="$PWD/.jupyter/runtime" IPYTHONDIR="$PWD/.ipython" .venv/bin/jupyter lab
```

Choose the `.venv` Python kernel. Standard Jupyter handles `$...$` inline math and `$$` display math. Notebooks locate the collection and place Matplotlib/Hugging Face caches, checkpoints and metrics inside `runtime/`. To reproduce terminal notebook validation, run:

```bash
.venv/bin/python -B validate_notebooks.py
```

This installs a temporary kernel specification inside `.jupyter/`, executes notebooks with a180-second per-cell limit and writes real outputs into the notebooks plus `validation_report.json`; validation runs offline to prevent accidental Hub downloads. Optional GPU branches stay off. No benchmark results are fabricated; saved outputs belong to this validation run. Runtime/cache/environment directories are ignored by Git.

## API compatibility

`api_references/` contains exact TRL0.22.2 wheel trainer/config source and `runtime_signatures.json` from successful imports. Recipes use `processing_class`. PPO uses the modern model/reference/reward/value-model constructor, not the legacy `.step()` API. ORPO is imported at top level in this pinned release. GRPO sets `loss_type='grpo'`, beta, group size and generation parameters explicitly because the release defaults to DAPO. Future TRL releases can move/delete PPO/ORPO; do not silently swap versions. Upstream reference: https://huggingface.co/docs/trl/v0.22.2/index and https://pypi.org/project/trl/0.22.2/ .

For CUDA, create a separate environment inside this directory and install a PyTorch build supported by the GPU/driver. Use supported BF16 only where native support is verified; otherwise these examples use FP32 rather than blindly enabling BF16/CPU FP16. Parameter counts, prompt/response length, batch, G responses, critic/reference copies and activations control memory. The optional135M pretrained examples are short workflow checks, not validated alignment runs. They have not been GPU-executed here unless explicitly stated in the validation report.

## Source preservation and dataset availability

At task start all15 original source files were missing from the working tree (pre-existing Git deletions). Their Git HEAD blobs matched the hash manifest in RLHF_COMPLETE_NOTES. They were inspected read-only; no original was restored, deleted or edited. [Source inspection](source_inspection.json) records this. The dataset loader uses the original path if present, otherwise its verified Git blob. It never substitutes invented pair fields. If using a source archive without Git and without the original JSONL, restore your own dataset availability before executing dataset notebooks.

Verified schema is exactly `prompt`, `chosen`, `rejected`, all strings,20 records. Train14/validation3/test3 split is seeded and prompt-disjoint. Every chosen response is longer in characters: length is a confound. No scores, answer metadata, annotation provenance or original splits are assumed. GRPO numeric gold answers belong to clearly labeled synthetic arithmetic records.

The PDFs' Q10/50/20, GRPO groups [1,0,1,0]/[9,6,2], DPO additive utility offsets and ORPO.75/.25 examples are retained. Existing implementation flaws motivate repairs: source RL dictionary is not state-dependent Q-learning; source DPO versions share code; reference-free DPO framing is corrected; source GRPO lexical/isdigit rewards are replaced by explicit numeric checks; source ORPO environments are separated by one pinned setup. See [existing corrections](../RLHF_COMPLETE_NOTES/CORRECTIONS_AND_LIMITATIONS.md).

## Limits

CPU models are very small and largely synthetic. Real20-pair scoring does not establish semantic reasoning, human preference generalization or safety. Group reward variance can be zero for random models. GPU/pretrained paths are opt-in and require independent task evaluation. Read `VALIDATION.md` and `validation_report.json` for actual execution status rather than assuming that source code proves successful training.
