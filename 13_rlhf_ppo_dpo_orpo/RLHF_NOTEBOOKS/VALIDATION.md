# Validation scope and results

All13 notebooks are real nbformat4.5 JSON notebooks. Their cell sources passed Python AST syntax validation and notebook schema validation. Default CPU paths were executed top-to-bottom in fresh Jupyter kernels, with real text/plot outputs saved into each notebook. The final run sets Hugging Face Hub/dataset offline mode to ensure no model or dataset downloads are needed. Execution details and elapsed times are recorded in [validation_report.json](validation_report.json).

## What was verified

- RL chain Q-learning learns a state-dependent greedy policy; exact Bellman solution satisfies its linear recurrence; source crossroad value33 and discounted return8.1 are checked.
- REINFORCE actor and learned-baseline gradients are nonzero and finite; detached baseline prevents actor loss from updating critic.
- GAE numerical example advantages[.575,.5], targets[.975,1.0]; time-limit bootstrap is preserved while recurrence cannot cross reset boundaries.
- PPO stores detached old logps, computes fixed targets before normalization, optimizes clipped actor/value/entropy losses in rollout minibatches, and evaluates a synthetic chain.
- Actual20-row JSONL schema/hash verified via source path or read-only Git blob. Split14/3/3 is seeded and prompt-disjoint; no invented labels/scores/reference_answer fields.
- Causal logps shift logits/targets by one, mask prompt/padding, score EOS once, reject empty completions, and verify precisely which logit positions receive gradients. These tests run in DPO, ORPO and end-to-end notebooks.
- DPO baseline loss log2 and frozen-reference gradients checked; small GRU training loss falls, with real validation results printed rather than guaranteed generalization claims.
- GRPO [1,0,1,0] normalized advantages and constant-group zeros checked; synthetic bandit sampling/training plots are actual measurements.
- ORPO.75/.25 arithmetic total.298218 checked; log1mexp branch stability and near-one finite gradients tested; supervised/preference components plotted separately.
- RewardTrainer/PPOTrainer, DPOTrainer, GRPOTrainer and ORPOTrainer CPU smoke workflows executed with a tiny randomly initialized local GPT-2, not a downloaded pretrained checkpoint. DPO/ORPO local exports reload with matching logits.
- End-to-end SFT/DPO/ORPO starts from comparable SFT weights, reports real validation/test pair metrics, exports checkpoints and confirms reload equivalence.
- All10 pinned TRL trainer/config imports succeeded. [Runtime signatures](api_references/runtime_signatures.json), exact wheel source and [20 constructor checks](api_call_validation.json) cover keyword compatibility, including unexecuted GPU branches.
- All121 Markdown mathematical expressions passed strict KaTeX parsing/rendering: [results](math_validation.json). Notebook Markdown uses inline dollars and separate display-dollar lines.
-13 notebooks,108 cells,57 executed code cells and10 stored PNG plots. The plot figures distinguish analytical/illustrative curves from measured toy runs. [Collection checks](collection_checks.json).

## Fix discovered by execution

TRL0.22.2 GRPO with nonzero KL creates its non-PEFT reference by reloading `model.config._name_or_path`. A newly initialized in-memory GPT-2 had an empty path, which failed reference loading. Notebook09 now saves its tiny random initialization under `runtime/grpo_initial/` and reloads it locally before constructing GRPOTrainer. The KL reference resolves to identical local initial weights; final offline execution verifies no Hub fallback is needed. The failed development output was replaced by successful rerun output; no failures are hidden as successful training.

## Dependencies and limitations

Actual execution: Python3.13.9, PyTorch2.8.0+cpu, NumPy2.2.6, Matplotlib3.10.6, Transformers4.56.2, TRL0.22.2, Datasets4.3.0, PEFT0.17.1, Accelerate1.10.1. Full installed versions are in [resolved-environment.txt](resolved-environment.txt). APIs are deliberately pinned; later releases may move PPO/ORPO and change loss defaults.

No CUDA/pretrained branch was executed. Signature checks do not establish GPU performance, real tokenizer/model compatibility on every hardware stack, or successful pretrained optimization. Set RUN_PRETRAINED_GPU intentionally, use compatible CUDA PyTorch, and validate a forward/backward batch and independent evaluation before scaling. The CPU random GPT-2 smoke runs have no meaningful instruction-following ability; GRPO rewards can all be zero. Twenty preference pairs and three test pairs are insufficient for robust generalization claims. Numerical correctness and executable workflows are the verified result.

The original15 PDFs/notebooks/dataset/README were already absent from the working tree at task start. Their Git HEAD blobs matched the earlier source hashes, were inspected read-only and remain unchanged. Their pre-existing deletions were not restored or altered. Existing RLHF_COMPLETE_NOTES files were read but not edited. All generated notebooks, tooling, dependencies, caches, kernel specs, plots, checkpoints and reports reside inside RLHF_NOTEBOOKS. Environment/cache/runtime folders are ignored by Git.
