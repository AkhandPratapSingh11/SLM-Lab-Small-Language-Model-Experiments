# 00 — Learning roadmap

[Home](README.md) · [Previous: Home](README.md) · [Next: Reinforcement learning fundamentals](01_REINFORCEMENT_LEARNING_FUNDAMENTALS.md)


## How to use this knowledge base

This course follows your sources from the left/right reward demo through actor-critic RLHF and the three alternative optimization paths. The practical chapters explain the supplied notebooks without executing or altering them. Equations use natural logarithms. Numerical examples are illustrative unless explicitly labeled **saved notebook output** or **measured dataset audit**.

Each algorithm chapter develops intuition, a mathematical objective, a worked example, implementation mapping, limitations, and revision points. The [inventory](SOURCE_INVENTORY.md), [page ledger](assets/source_audit/PDF_PAGE_LEDGER.md), and [notebook audit](assets/source_audit/NOTEBOOK_AUDIT.md) provide the evidence trail.

## Suggested sequence and exercises

| Stage | Read | What you should be able to do before continuing |
|---|---|---|
| Foundations | Chapters 01–03 | Explain reward versus return; compute V, Q and advantage; validate a preference pair |
| Intermediate | Chapters 04–07 | Calculate PPO clipping, DPO margin, GRPO normalization and ORPO odds by hand |
| Engineering | Chapters 08–10 | Select an algorithm, inspect masks, read trainer defaults, diagnose a failing run |
| Advanced revision | Chapters 11–12 plus derivations in 04–07 | Defend assumptions, distinguish algorithm from library, discuss failure modes |

Use sessions of 45–90 minutes as a flexible study suggestion, not a required schedule. Start with the game examples in Chapter 01, then rewrite them as prompt/token/response examples. For each algorithm, draw its data flow from memory before opening its notebook.

1. Run the local data validator in Chapter 09; explain why 20 clean rows are still insufficient for robust alignment.
2. Recompute the DQN example: reward 5, next-state maximum 6, discount 0.9 gives target 10.4. Explain why this is a bootstrap target rather than ground truth.
3. Calculate PPO with positive and negative advantage. Show why clipping is asymmetric with respect to advantage sign.
4. Derive DPO's optimal policy from KL-regularized reward maximization and cancel its partition function in a pairwise comparison.
5. Compare GRPO rewards `[1, 0, 1, 0]` with `[1, 1, 1, 1]`. Explain the loss of comparative signal.
6. Reproduce the ORPO 0.75/0.25 odds example. Then explain why normalized sequence scores need not sum to one across candidate answers.
7. Audit the source notebooks using the cell tables. Pick one actual issue and describe a minimal repair in a separate experiment, preserving the originals.

## Prerequisites introduced gradually

You need basic Python functions, lists and dictionaries; tensor shapes; gradients as directions of local change; probabilities and conditional probabilities. Chapter 01 introduces expectation, logarithms, discounting and KL. Chapter 09 explains token shifting and masking. A full implementation also requires understanding your installed trainer version and GPU precision support.

## Revision workflow

After each chapter, explain its revision points aloud without looking. On the next day, redo its worked example. Before interviews, review the model-role table in Chapter 02, selection guide in Chapter 08, scenario questions in Chapter 11, and formulas in Chapter 12. Before training, use the dataset/mask checks and debugging tables rather than relying on interview summaries.

## Evidence boundaries

The supplied PDFs include rasterized typed text as well as handwriting, annotated screenshots and diagrams. All 137 pages were visually reviewed; trailing blank pages and small illegible screenshot details are recorded. All 247 notebook cells were read, including commented alternatives and stored outputs. Outputs are historical artifacts, not reproducible experiments performed here. Current upstream documentation/source was consulted for definitions and API distinctions; it does not establish the exact implementation of every historical installed release.
