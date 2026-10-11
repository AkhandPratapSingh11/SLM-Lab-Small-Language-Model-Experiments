# Source inventory and consolidation
All 15 expected sources were inspected without modifying them. Original SHA-256 values are in [the hash manifest](assets/source_audit/original_hashes.json). Page counts: 137; notebook cells: 247. [Page ledger](assets/source_audit/PDF_PAGE_LEDGER.md) and [cell ledger](assets/source_audit/NOTEBOOK_AUDIT.md) provide granular traceability.
## PDF sources
| Source | Pages and unique contribution | Chapters | Limits / corrections |
|---|---|---|---|
| [DPO-Handwritten-Notes.pdf](../DPO-Handwritten-Notes.pdf) | 18. Older equation/implicit-reward progression and additive-offset example. | 02,03,05,08,11,12 | Raster handwriting; blank pages listed in ledger. Reference and reward-ratio notation repaired, likelihood trend qualified. |
| [DPO-Updated-handwritten-notes.pdf](../DPO-Updated-handwritten-notes.pdf) | 19. Explicit offset ambiguity and paper-result caveat. | 02,03,05,08,11,12 | Raster handwriting; blank pages listed in ledger. Reference and reward-ratio notation repaired, likelihood trend qualified. |
| [DPO-Handwritten-final-update-Notes.pdf](../DPO-Handwritten-final-update-Notes.pdf) | 21. Expanded agenda and logistic numeric confidence discussion. | 02,03,05,08,11,12 | Raster handwriting; blank pages listed in ledger. Reference and reward-ratio notation repaired, likelihood trend qualified. |
| [GRPO-Handwritten-Final-Notes.pdf](../GRPO-Handwritten-Final-Notes.pdf) | 12. Groups [1,0,1,0] and [9,6,2], coder-to-math context, reward versus RM distinction. | 06,08,11,12 | Raster handwriting; mean-only advantage clarified with original std normalization. Small branching fragment uncertain; timeline claims not treated as benchmarks. |
| [LLM-Finetuning-ORPO.pdf](../LLM-Finetuning-ORPO.pdf) | 17. Geometric likelihood/odds explanation, .75/.25 toy calculation and reversal, monolithic motivation. | 07,08,11,12 | Embedded text plus formula imagery; blank p10. Odds arithmetic corrected. Adoption/employment claims unverified. |
| [RLHF-Updated-Recent-Latest.pdf](../RLHF-Updated-Recent-Latest.pdf) | 50. Games, treasure, Q10/50/20, DQN4→10.4/MSE40.96, PPO ratio1.2/advantage examples and four-model pipeline. | 01,02,03,04,08,11,12 | Raster handwriting and blank pages. Tiny p3 screenshot uncertain. Hard-bound clipping, immediate reward advantage, taxonomy and safety claims qualified. |

## Notebook sources
| Source | Cells / actual workflow | Chapters | Limits |
|---|---|---|---|
| [DPO_Training.ipynb](../DPO_Training.ipynb) | 47. 47-cell detailed TRL DPO/QLoRA workflow; inline 4 pairs, optional JSON and external dataset; evaluation, saved metrics, adapter reload. | 05,09,10 | Source cells exactly match Final version; output metadata differs. One held-out pair and matching metrics do not prove independent runs. |
| [DPO_Training_Final.ipynb](../DPO_Training_Final.ipynb) | 47. Same 47 source cells as DPO_Training; recorded later dependency versions and same main metrics. | 05,09,10 | Final name does not imply an implementation change; tiny evaluation and T4 precision flag need qualification. |
| [Final_DPO.ipynb](../Final_DPO.ipynb) | 15. 15-cell prototype: full downloaded UltraFeedback, Qwen2.5-0.5B LoRA, training and inference. | 05,09,10 | Inline literal unused; bad device precision branches, boundary warnings and KeyboardInterrupt. End-to-end success unverified. |
| [Final_GRPO_Practical.ipynb](../Final_GRPO_Practical.ipynb) | 54. 54 cells: 8-prompt SmolLM heuristic-reward workflow, then separate Unsloth Qwen/GSM8K XML reward workflow. | 06,08,09,10,11 | First path saved default DAPO loss; lexical reward is not correctness. Second path no outputs, batch/group and numeric parsing need verification. |
| [Final_ORPO_Practical.ipynb](../Final_ORPO_Practical.ipynb) | 33. 33 cells: standard experimental TRL ORPO on 100 UltraFeedback examples; separate older Unsloth environment on 500. | 07,08,09,10,11 | First training has output but saved inference CUDA assert; second path no outputs. State-dependent deletion, version mixing and prompt extraction issues. |
| [RL_Fundamental.ipynb](../RL_Fundamental.ipynb) | 28. 28 cells: bandit-like dictionary, synthetic DQN update, Stable-Baselines3 PPO CarRacing demo. | 01,04,11 | First is not full Q-learning; DQN has no environment/replay loop; requested100 PPO steps collect2048 due rollout length. |
| [RLHF_with_PPO_Final_Code.ipynb](../RLHF_with_PPO_Final_Code.ipynb) | 23. 23 cells: 4-pair RewardTrainer, frozen RM/reference, trainable critic, experimental PPOTrainer and final inference. | 02,03,04,09,10,11 | Default inline dataset rather than local file. No eval, 6 episodes, singleton variance warning, full-prompt inference; internal tensors delegated to installed TRL. |

## Dataset and original README
| Source | Inspection result | Chapters / limits |
|---|---|---|
| [reward_preferences_dataset.jsonl](../reward_preferences_dataset.jsonl) | All20 lines parsed; exact fields prompt/chosen/rejected are nonempty strings; no invalid rows or exact duplicates; chosen longer in characters20/20. | 03,09,10,11. No scores, reference_answer, splits or annotation provenance. [Statistics](assets/source_audit/dataset_report.json). |
| [README.md](../README.md) | Entire existing chapter links/context read; its alignment-method framing preserved as orientation. | 00,02,08. Standard DPO incorrectly categorized reference-free; corrected here, original untouched. |

## Consolidation policy
The final/updated PDFs refine organization but do not erase older useful examples. DPO offset examples and final sigmoid interpretation are both retained; common pipeline material is centralized in Chapter02. The two long DPO notebook sources are identical, so one execution walkthrough is shared with separate recorded environments. Final_DPO is a distinct prototype, not automatically preferred by filename. Both GRPO and ORPO notebooks contain two materially separate environments/workflows. Historical saved outputs, current upstream implementation checks, canonical paper definitions and recommendations are explicitly separated.

## Extraction limits
All pages received image review and auxiliary OCR; tiny inset text and isolated handwritten fragments cannot always be transcribed exactly. Blank pages are explicitly listed. Raw extracted math is not accepted uncritically. All cell types, comments and saved text/HTML/PNG outputs were inspected, but notebooks were not retrained and outputs may be stale. This knowledge base documents runnable intent, not a claim of reproduced GPU training. See [corrections](CORRECTIONS_AND_LIMITATIONS.md) and [external verification](EXTERNAL_REFERENCES.md).
