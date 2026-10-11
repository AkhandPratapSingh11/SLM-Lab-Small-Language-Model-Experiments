# External references and verification record

The supplied sources are primary evidence about local code and teaching examples. External references verify algorithm definitions and clarify mistakes. Retrieval took place during this documentation build on 2026-10-11. [HTTP verification](assets/references/verification.json) and [additional retrieval results](assets/references/verification_extra.json) and [supplemental paper verification](assets/references/supplemental_verification.json) record statuses. Retrieved content is retained under assets/references for audit; no external decorative imagery is used.

| Reference | Verified relevance | URL |
|---|---|---|
| Schulman et al., *Proximal Policy Optimization Algorithms*, 2017, arXiv1707.06347 | Original ratio/clipped surrogate and actor-critic context; HTML endpoint was a short fallback, canonical paper additionally retrieved | https://arxiv.org/abs/1707.06347 |
| Schulman et al., *High-Dimensional Continuous Control Using Generalized Advantage Estimation*, 2015, arXiv1506.02438 | GAE identity/title record; relevant advantage-estimation primary reference | https://arxiv.org/abs/1506.02438 |
| Ouyang et al., *Training language models to follow instructions with human feedback*, 2022, arXiv2203.02155 | Classical SFT/RM/PPO workflow record | https://arxiv.org/abs/2203.02155 |
| Rafailov et al., *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*, 2023, arXiv2305.18290 | §4 optimal policy, reward reparameterization, pairwise loss; original limited experimental setting | https://arxiv.org/abs/2305.18290 |
| Shao et al., *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*, 2024, arXiv2402.03300 | §4.1 outcome/process GRPO, group baseline, explicit KL, trained reward sources; model training context | https://arxiv.org/abs/2402.03300 |
| Hong, Lee and Thorne, *ORPO: Monolithic Preference Optimization without Reference Model*, 2024, arXiv2403.07691 | Length-normalized probability score, odds and combined loss; primary model scope | https://arxiv.org/abs/2403.07691 |
| ORPO EMNLP2024 publication | Confirms authors/title/venue; no need to retain unverified current employment or acceptance-rate claims | https://aclanthology.org/2024.emnlp-main.626/ |
| Hugging Face TRL DPO docs | Direct pair format, reference/PEFT behavior and current variants | https://huggingface.co/docs/trl/dpo_trainer |
| Hugging Face TRL GRPO docs | Group generation, configuration, reward scaling and later objective variants | https://huggingface.co/docs/trl/grpo_trainer |
| Hugging Face TRL ORPO docs | ORPO data/objective and interface context; release compatibility still needs checking | https://huggingface.co/docs/trl/orpo_trainer |
| TRL upstream DPO source | Current implementation contrast, not exact historical1.8/1.9 source proof | https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py |
| TRL upstream GRPO source | Current grouping/normalization/aggregation implementation contrast | https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py |
| TRL upstream ORPO source | Completion-average logps, stable log1mexp and subtract-negative-preference sign convention | https://github.com/huggingface/trl/blob/main/trl/experimental/orpo/orpo_trainer.py |
| TRL upstream reward source | Current prompt extraction/full-conversation preprocessing contrast | https://github.com/huggingface/trl/blob/main/trl/trainer/reward_trainer.py |

## Retrieval limitations and version boundaries

Several PPO documentation URLs returned HTTP200 with tiny redirect/fallback content, and the current guessed experimental PPO source returned404. HTTP success alone does not establish useful technical documentation. Canonical PPO equations were verified against the original paper; the exact historical TRL1.6.0 internal loss defaults and resume behavior were not established from live upstream. The notebook explicitly delegates those computations, so the chapters describe canonical behavior and flag defaults needing inspection.

GAE and InstructGPT landing records establish identity/relevance; detailed formulas/pipeline are additionally verified against downloaded primary PDFs where recorded in the supplemental verification file. DPO/DeepSeekMath/ORPO HTML includes equations and was read around relevant sections; the ORPO appendix explicitly defines geometric-mean likelihood. Upstream main source can change and does not pin a historical commit. Saved notebook version strings and requested install versions are labeled separately.

## Related methods mentioned in sources

KTO and SimPO appear in the original README/ORPO PDF but not as runnable implementations. Their primary references are [KTO, arXiv2402.01306](https://arxiv.org/abs/2402.01306) and [SimPO, arXiv2405.14734](https://arxiv.org/abs/2405.14734). Identity/relevance were checked during supplemental retrieval; these methods receive brief context rather than unsupported full notebook walkthroughs.

The GRPO PDF's later model-release timeline and ORPO PDF's adoption rankings, current-employment statements and unrelated deployment/domain claims remain source-context leads. They are not used as verified selection criteria. Paper benchmark numbers are tied to the original evaluator/model setup, never attributed to local training.
