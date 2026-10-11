# RLHF complete learning notes

A source-grounded beginner-to-advanced course on reinforcement learning, classical PPO RLHF, DPO, GRPO and ORPO. It integrates all six PDFs, seven notebooks, the local preference JSONL and the original module README. It includes corrected derivations, actual code walkthroughs, reusable diagrams, reproducible illustrative plots, debugging tools and 50 interview questions.

**Start with the roadmap, then Chapters 01–07 in order.** Use Chapters 08–10 while planning or debugging a run, and Chapters 11–12 for revision. Original sources remain in the parent source directory and are linked read-only; all generated resources are inside this directory.

## Contents

| Level | Chapter | What you learn |
|---|---|---|
| Orientation | [00 Learning roadmap](00_LEARNING_ROADMAP.md) | Sequence, exercises and evidence boundaries |
| Foundation | [01 RL fundamentals](01_REINFORCEMENT_LEARNING_FUNDAMENTALS.md) | MDP, values, Bellman, TD, gradients, GAE, LLM mapping; three actual RL demos |
| Foundation | [02 Alignment and RLHF](02_LLM_ALIGNMENT_AND_RLHF.md) | Training stages, four model roles, reward/critic distinction and challenges |
| Foundation | [03 Preference data and reward models](03_PREFERENCE_DATA_AND_REWARD_MODELS.md) | Pair annotation, Bradley–Terry loss, verified local dataset and transformations |
| Intermediate → advanced | [04 PPO](04_PPO_IN_DEPTH.md) | Ratio/clipping, GAE, full actor-critic workflow and SmolLM2 notebook |
| Intermediate → advanced | [05 DPO](05_DPO_IN_DEPTH.md) | KL derivation, implicit rewards, masks/reference behavior and all three notebooks |
| Intermediate → advanced | [06 GRPO](06_GRPO_IN_DEPTH.md) | Groups/normalization, original versus DAPO variants, heuristic and GSM8K paths |
| Intermediate → advanced | [07 ORPO](07_ORPO_IN_DEPTH.md) | Normalized likelihood odds, chosen NLL and two implementation environments |
| Engineering | [08 Comparison and selection](08_ALGORITHM_COMPARISON.md) | Objectives, models, data, compute, decision tree and misconceptions |
| Engineering | [09 Practical guide](09_PRACTICAL_IMPLEMENTATION_GUIDE.md) | Versions, data/mask/logp helpers, checks, saving/reload and resource planning |
| Engineering | [10 Evaluation and debugging](10_EVALUATION_DEBUGGING_AND_BEST_PRACTICES.md) | Metrics, symptoms, hyperparameters and source-grounded debugging cases |
| Revision | [11 Interview preparation](11_INTERVIEW_PREPARATION.md) | 50 questions with short answers, reasoning, examples and incorrect answers |
| Revision | [12 Glossary and formulas](12_GLOSSARY_AND_FORMULA_CHEATSHEET.md) | Vocabulary, equations with symbols/uses and compact comparison |

## Evidence, diagrams and executable resources

- [Source inventory](SOURCE_INVENTORY.md): all 15 sources, chapter mapping, overlap and limitations.
- [Corrections register](CORRECTIONS_AND_LIMITATIONS.md): technical corrections, uncertainty and code repair guidance.
- [External references](EXTERNAL_REFERENCES.md): verified primary papers/docs and API retrieval limits.
- [PDF page ledger](assets/source_audit/PDF_PAGE_LEDGER.md): every one of 137 pages, topic and visual-reading notes.
- [Notebook audit](assets/source_audit/NOTEBOOK_AUDIT.md): every one of 247 source cells, outputs and execution-order mapping.
- [Diagrams and analytical plots](diagrams/README.md): 13 Mermaid sources and two original reproducible plots.
- [Dataset validator](assets/validate_dataset.py), [tensor helpers](assets/tensor_patterns.py), [plot generator](assets/plot_objectives.py), [documentation validator](assets/verify_notes.py).
- [Quality-assurance report](QA_REPORT.md) and [terminal completion report](COMPLETION_REPORT.txt).

## Revision and implementation workflow

After each chapter, redraw its workflow and recompute its example. Before interviews, review the model-role table, comparison, scenario questions and formula sheet. Before training, inspect the exact data schema, model template, masks and installed trainer signatures, then run a small finite forward/backward check. Evaluate against a baseline on disjoint prompts; keep full checkpoint state when resuming.

## Important evidence limits

The sources are teaching materials and stored notebook outputs. No source notebook was retrained here. The JSONL has only 20 pairs, with every chosen response longer in characters. One-pair DPO accuracy, tiny PPO/GRPO runs and the ORPO saved training result are not general alignment evidence. The GSM8K and Unsloth ORPO paths have no stored outputs proving successful execution. Blank PDF pages and small unreadable screenshot details are recorded explicitly. Mathematical derivations and upstream code verification are distinct from historical installed-library behavior.

## Viewing mathematical equations

Equations use GitHub-compatible `$...$` inline math and `$$` display delimiter lines. Use GitHub or enable MathJax/KaTeX in your Markdown preview. For viewers without math support, open the [pre-rendered fundamentals chapter](assets/math_preview/01_REINFORCEMENT_LEARNING_FUNDAMENTALS.html) in a browser; all eight formula-bearing chapters have HTML previews in `assets/math_preview/`. See [math validation](assets/math_validation.json) and the [correction record](CORRECTIONS_AND_LIMITATIONS.md#math-rendering-repair--2026-10-11).

The HTML previews use local KaTeX styles and fonts. After cloning, install the pinned rendering tools with `npm ci --prefix assets/tooling --cache assets/tooling/npm-cache` from this knowledge-base directory. Installed dependencies and npm cache are ignored by Git.
