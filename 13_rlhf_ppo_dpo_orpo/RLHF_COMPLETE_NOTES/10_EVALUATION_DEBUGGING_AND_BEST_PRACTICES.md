# 10 — Evaluation, debugging, and best practices

[Home](README.md) · [Previous: Practical implementation guide](09_PRACTICAL_IMPLEMENTATION_GUIDE.md) · [Next: Interview preparation](11_INTERVIEW_PREPARATION.md)


## 1. Evaluate the intended behavior independently of the optimized proxy

Keep a fixed held-out prompt suite with task rubrics and a baseline model. For open-ended preferences, use blinded pairwise comparisons and report annotator/judge disagreement. For verifiable tasks, score correctness with an appropriate parser or tests. Match decoding settings and inspect multiple seeds/samples. Use a disjoint validation set for checkpoint selection and untouched test data for final reporting.

The source DPO run evaluates only one preference pair and generates mostly training-topic prompts. PPO and first GRPO have no explicit held-out evaluation loop. ORPO's stored inference fails. These sources are engineering demonstrations, not rigorous comparative experiments.

## 2. Metrics and what they can establish

| Metric | Relevant algorithms | Interpretation and limit |
|---|---|---|
| Training/validation loss | All, using each objective | Fit to that objective; losses across algorithms/scales are not comparable |
| Preference accuracy | RM, DPO, ORPO; independent eval for all | Fraction ranked correctly; distinguish raw likelihood, implicit reward and odds scores; tie handling matters |
| Reward score | PPO/GRPO | Scorer output, not necessarily real quality; report components/calibration |
| Policy/reference KL | PPO RLHF, GRPO with reference; diagnostic DPO | Drift on sampled/test prefixes; estimator, direction and sampling distribution matter |
| Entropy | All if measured; rollout methods especially | Token diversity/uncertainty; more entropy can mean worse answers |
| PPO clip fraction | PPO, clipped GRPO variants | Fraction with clipping active under a defined formula; high value can indicate excessive movement or advantage/ratio issues |
| Value loss | PPO critic | Target fit in shaped reward scale; low value loss does not validate RM |
| Explained variance | PPO critic | `1−Var(target−value)/Var(target)`; undefined for constant targets, negative means worse variance than a constant predictor |
| Chosen/rejected logps | DPO/ORPO | Track each absolute score and margin; sum versus mean must be stated |
| Implicit reward margin | DPO | β times policy/reference log-ratio difference; may rise while both candidate logps fall |
| Odds preference margin | ORPO | Difference of normalized-score log odds; different from DPO reward margin |
| Group reward std and zero-variance fraction | GRPO | Available comparative signal, not absolute correctness |
| Response length/EOS/truncation rate | All | Detect length shortcuts, incomplete answers and mode changes |
| Instruction following, task correctness, safety, regression | All | Independent intended-behavior evaluation; needs a sound rubric and representative coverage |

At policy=reference DPO implicit rewards tie at zero, so a strict comparison accuracy can be zero with loss log2. In a mixed training/evaluation history, NaN in missing DataFrame columns need not be a nonfinite loss event. Source PPO's singleton variance warning can affect one metric without implying every gradient is invalid.

Track class/topic/length slices. A high average score can conceal failures on short prompts, rare topics or difficult tasks. Length-controlled evaluation helps expose verbosity shortcuts; it should not discourage detail when the task needs it.

## 3. Troubleshooting grounded in actual source issues

| Symptom | Plausible causes | How to verify | Recommended repairs | Methods |
|---|---|---|---|---|
| NaN or infinite loss | Empty masks, zero std, log(1−p) near zero, FP16 overflow, extreme rewards/LR | Count scored tokens, inspect input IDs, component losses, group std, gradients in FP32 | Reject empty completions, stable log-space functions, numerical eps/thresholds, support-aware precision, reduce offending scale/LR | All; odds ORPO, groups GRPO |
| Reward rises but quality falls | Reward hacking, length/format shortcut, scorer distribution shift | Blind independent judgments, length/component plots, adversarial examples | Fix reward coverage, retrain scorer on fresh examples, conservative stopping/KL, independent validation | PPO/GRPO; proxy overfit also offline methods |
| KL grows rapidly | Large LR, weak anchor, reward scale jump, reference misconfigured | Verify fixed ref parameters/template; plot token KL and score scale | Lower update pressure, tune documented KL coefficient, improve rewards, reduce rollout reuse | PPO/GRPO; diagnostic DPO |
| PPO oscillates/diverges | Poor critic, stale rollouts, tiny batch, bad normalization, ratio bug | Value loss/explained variance, old/new logps, active masks, clip fraction | Better rollout batch and value targets, fewer reuse epochs, lower LR, correct ratio/masks | PPO |
| DPO loss flat near log2 | No gradients, identical candidates/reference effect, malformed pairs, insufficient steps | Print trainable count/gradients; inspect z and complete scored responses | Fix adapter setup, data and masks; use meaningful pairs and validated settings | DPO |
| Prefix mismatch warning | Boundary merges, duplicate template/BOS/EOS, inconsistent whitespace/history | Decode prompt/full tokens and trainer masks | Use one supported template path; repair histories; verify tokenizer boundary logic | DPO/ORPO/RM |
| Loss improves but held-out preference worsens | Overfit, easy labels, leakage, evaluator bias | Prompt-group split, hard pairs, independent judges, logp/length slices | Better data, early stopping, smaller steps, evaluation diversity | All |
| GRPO rewards have no variance | All correct/all wrong, duplicates, broken parser, missing metadata | Count group duplicates; test reward on known answers; inspect passed gold column | Appropriate task difficulty/diversity, reliable parser and reward granularity, verify metadata; skip/handle constant groups | GRPO |
| ORPO preference dominates NLL | Large coefficient, scale mismatch, noisy labels | Log each unweighted loss and weighted gradient contribution | Tune λ in that implementation, improve labels/targets, consistent token averaging | ORPO |
| OOM | Long paired batches, grouped KV cache, multiple copies, live trainers at reload | Peak memory by phase; inspect live objects/model copies and sequence lengths | Smaller microbatch/length/group, accumulation, LoRA/quantization/checkpointing, explicit object release | All |
| Padding corrupts loss | EOS-as-pad confusion, labels include padding, incorrect position IDs | Decode scored tokens; compare padded/unpadded example logps | Separate attention/loss masks; mask padding by positions, keep real EOS; correct position handling | All |
| CUDA assert during cleanup/inference | Earlier asynchronous error, invalid token IDs, embedding/tokenizer mismatch, incompatible kernels | Fresh process, synchronous diagnostic run, ID bounds, config/generation IDs, CPU reproduction | Restart poisoned context; correct IDs/vocab/special tokens and compatible versions | ORPO source; possible all |
| Resume differs unexpectedly | Only adapter saved, missing RNG/optimizer/scheduler, changed data order | List checkpoint state files, compare model/data hashes and config | Save full supported training checkpoints; reload same environment/data/seed | All |
| GRPO initialization rejects batch | Effective generation batch incompatible with G; wrong version keywords | Inspect installed config signature and grouping calculation | Set compatible generation batch/steps/devices; match supported API | GRPO second source path |
| Poor answers despite low loss | Wrong metric, easy synthetic negatives, truncation, capability limits | Independent correctness and new prompts; examine full completions | Improve data/model/task fit; adjust truncation; choose checkpoint by quality | All |

Do not change several variables at once unless fixing a known dependency. Establish a minimal failing batch; preserve its token IDs, masks and config under a generated experiment directory. A CUDA traceback can point after the original fault, as the source ORPO cleanup cell demonstrates.

## 4. Hyperparameters and trade-offs

| Parameter | Scope | What increasing it can do; what to monitor |
|---|---|---|
| Learning rate | All | Faster movement, more instability/drift; finite gradients, KL and quality |
| Microbatch size | All | More simultaneous data, more memory; useful-token count and step noise |
| Effective batch/accumulation | All; grouping differs in RL | Lower sampling noise and fewer optimizer steps per example; LR/schedule interactions |
| Sequence length | All | Retain longer context/answers; more memory and truncation interactions |
| PPO clip ε | PPO/GRPO variants | Wider allowed incentive range; ratio/clip fraction/KL |
| KL coefficient κ | PPO RLHF/GRPO | Stronger penalty for drift at fixed score scale; can under-optimize rewards |
| GAE λ | PPO | Longer-horizon return weighting; bias/variance depends on critic error |
| Discount γ | PPO/RL | Greater weight on later rewards; changes credit/target meaning |
| DPO β | DPO | Scales logistic margin; tied to KL derivation, gradient saturation and data fit |
| Group size G | GRPO | More potential comparative samples; more rollout cost and possible duplicates |
| ORPO λ (`beta` in source config) | ORPO | More relative preference pressure; monitor chosen NLL and regressions |
| Sampling temperature | Rollouts/inference | More diversity; can worsen correctness and change reward variance |
| Top-p | Sampling | Restricts tail sampling; distribution and exploration change |
| Epochs/optimization reuse | All; distinctions matter | More fit, also overfit and stale rollout risk |
| Gradient norm clipping | All | Caps gradient norm, separate from probability clipping; too tight can slow learning |
| Mixed precision | All | Memory/speed trade-off; FP16 scaling/BF16 support/numerical reductions |
| Reward weights/scaling | PPO/GRPO | Alters effective preference among goals and relative KL strength |

Source settings are examples, not optimal recipes: DPO β=.1; first GRPO G4/temperature.9/β=.01; ORPO coefficient .1; PPO LR1e−6 with six episodes. Tune on the actual model/data with held-out metrics. Printed defaults from one release are not universal defaults.

## 5. Three source-based debugging exercises

**DPO chosen logp decreased but accuracy improved.** Inspect reference-adjusted margin rather than conclude the loss is broken. The stored chosen drop≈7.28 and rejected drop≈23.35 produce a positive β=.1 margin≈1.61. Then inspect independent generations to see whether the probability shift helped the intended behavior.

**GRPO “correctness” improves for a wrong but verbose answer.** The first path scores character similarity plus keyword recall and style heuristics. Test a word-overlap answer containing a false statement. Its reward reveals a scorer flaw; changing PPO clipping cannot repair semantic verification.

**ORPO cleanup cell raises CUDA assert.** Restart and inspect earlier operations and vocabulary/generation IDs in a small reproduction. Do not infer the cleanup routine is the cause or that reinstalling torchao always fixes it. Select one consistent environment path before attributing the failure to the odds objective.

## Revision

Monitor objective-specific metrics plus independent task behavior. DataFrame gaps, singleton variance and asynchronous CUDA faults have different causes. Debug masks, context, rewards and versions before tuning more epochs or declaring alignment success.
