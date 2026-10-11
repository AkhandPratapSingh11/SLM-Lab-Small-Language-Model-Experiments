# 11 — Interview preparation

[Home](README.md) · [Previous: Evaluation, debugging, and best practices](10_EVALUATION_DEBUGGING_AND_BEST_PRACTICES.md) · [Next: Glossary and formula cheat sheet](12_GLOSSARY_AND_FORMULA_CHEATSHEET.md)

## How to answer

Start with the interview-ready answer, then justify it with the assumptions or a source example. Formula details are expanded in Chapters 01–07. The questions below distinguish definitions, implementation choices and actual stored output.


## Beginner


### Q01. What is RLHF?


**Interview-ready answer:** A workflow that uses human feedback to improve a policy, commonly by fitting a reward model from comparisons and optimizing an LLM with PPO.


**Reasoning / example:** Feedback supplies a proxy for preferred behavior. RLHF is broader than one four-model architecture; distinguish the classical PPO pipeline from offline preference methods.


**Common incorrect answer:** “Human feedback guarantees a perfectly aligned model.”


### Q02. How does SFT differ from RLHF?


**Interview-ready answer:** SFT imitates demonstrated responses; classical RLHF optimizes feedback-derived reward on generated responses.


**Reasoning / example:** SFT minimizes chosen-token NLL. RLHF can compare multiple plausible answers through a reward proxy. SFT can teach safety/tone when demonstrations contain them; it simply lacks an explicit pairwise rejection term.


**Common incorrect answer:** “SFT cannot learn any preferences or safety behavior.”


### Q03. What is a policy?


**Interview-ready answer:** A rule or distribution for selecting an action from a state; an LLM policy gives next-token probabilities conditional on the prompt and prefix.


**Reasoning / example:** πθ(a|s) has trainable parameters θ. Greedy decoding makes action selection deterministic but does not erase the underlying probability model.


**Common incorrect answer:** “The policy is the reward function.”


### Q04. What is a reward model?


**Interview-ready answer:** A model that assigns a scalar score to a prompt-response pair, often trained to rank chosen answers above rejected ones.


**Reasoning / example:** A scalar head on a transformer can learn −logσ(rw−rl). Pairwise scores have prompt-dependent additive ambiguity and need held-out validation.


**Common incorrect answer:** “The output score is calibrated absolute truth.”


### Q05. What are chosen and rejected responses?


**Interview-ready answer:** Two candidate responses to the same prompt, ordered by the annotation preference.


**Reasoning / example:** Chosen is preferred within that pair, not necessarily ideal in every respect. The local dataset encodes labels through its chosen/rejected fields and has no numeric scores.


**Common incorrect answer:** “Rejected always means factually false, or a separate label field exists here.”


### Q06. What is a reference policy for?


**Interview-ready answer:** It provides a fixed baseline distribution for regularization or reference-relative preference scoring.


**Reasoning / example:** PPO RLHF commonly penalizes drift from it; standard DPO uses its chosen/rejected logps. An adapter-disabled base or cached scores can implement this role under the right conditions.


**Common incorrect answer:** “No separate model copy means no reference exists.”


### Q07. What is KL divergence?


**Interview-ready answer:** An asymmetric measure of distribution difference: DKL(p||q)=Σ p log(p/q).


**Reasoning / example:** It averages a log ratio under p, is nonnegative in expectation, and is zero for equal distributions. A single sampled log ratio may be negative.


**Common incorrect answer:** “KL is symmetric or is always nonnegative for every sampled log ratio.”


### Q08. What is an advantage function?


**Interview-ready answer:** Aπ(s,a)=Qπ(s,a)−Vπ(s): the action’s expected return relative to the policy’s average in that state.


**Reasoning / example:** Positive advantage encourages that action in policy-gradient learning. Estimates such as GAE or group normalization are noisy training signals, not exact true advantages.


**Common incorrect answer:** “Advantage always equals immediate reward minus value.”


### Q09. How do reward and return differ?


**Interview-ready answer:** Reward is one feedback value; return sums discounted future rewards.


**Reasoning / example:** For rewards [0,0,10] and γ=.9, initial return is8.1. A terminal response score may be one reward in a sequence with intermediate KL shaping.


**Common incorrect answer:** “Return is the critic prediction rather than the target it estimates.”


### Q10. How do agent, state and action map to an LLM?


**Interview-ready answer:** The model is the agent; prompt plus generated prefix is the state; the next token is the action.


**Reasoning / example:** Appending the token transitions to a longer prefix. EOS or a stopping rule ends the episode, and scoring can occur per token or at the response level.


**Common incorrect answer:** “Language-model actions are continuous because text is complex.”


### Q11. What is an MDP and the Markov property?


**Interview-ready answer:** An MDP specifies states, actions, transition probabilities, rewards and initial-state distribution; the current state summarizes relevant history for the next transition.


**Reasoning / example:** Velocity must be included if position alone is insufficient in a game. Full visible prefix is a convenient state for autoregressive generation, but hidden external context can complicate the model.


**Common incorrect answer:** “Every arbitrary observation is automatically Markov.”


### Q12. What is the critic, and how is it different from the RM?


**Interview-ready answer:** The critic predicts future return from a prefix; the RM scores a completed response’s preference quality.


**Reasoning / example:** The PPO notebook initializes both from rm_out, then freezes reward_model and trains value_model to rollout targets. Same starting checkpoint does not imply the same objective.


**Common incorrect answer:** “RM and critic are synonyms.”


## Intermediate


### Q13. How does PPO work in classical RLHF?


**Interview-ready answer:** Collect fresh-policy responses, score and KL-shape rewards, estimate advantages/returns, and update actor and critic with clipped policy and value losses.


**Reasoning / example:** Stored old logps define the behavior denominator; the frozen reference anchors behavior separately. PPOTrainer in the supplied notebook owns this loop.


**Common incorrect answer:** “The notebook implements its own GAE tensors by hand.”


### Q14. Why does PPO use clipping?


**Interview-ready answer:** To cap further surrogate benefit from an overly large beneficial action-probability ratio change.


**Reasoning / example:** With A>0 and ε=.2, ratio1.5 contributes1.2A on the minimum branch. Harmful-direction changes remain penalized; shared network weights may still move probabilities beyond the interval.


**Common incorrect answer:** “Clipping hard-limits all weight updates or rewrites probabilities.”


### Q15. What is GAE?


**Interview-ready answer:** A discounted weighted sum of TD residuals: Ât=Σl(γλ)^lδt+l.


**Reasoning / example:** δt=Rt+γVnext−Vcurrent with termination handling. λ trades shorter bootstrap estimates against longer, typically higher-variance estimates; raw Â plus old V can form critic targets.


**Common incorrect answer:** “GAE is simply reward normalization.”


### Q16. Why does PPO commonly use a critic?


**Interview-ready answer:** A learned state-value baseline reduces variance and supports token-level advantage/return estimation.


**Reasoning / example:** An action-independent baseline does not change the expected policy gradient because Σπ∇logπ=0. A poor critic can bias bootstrap estimates and destabilize training.


**Common incorrect answer:** “The critic supplies the human preference label.”


### Q17. Why do log probabilities appear in policy gradients?


**Interview-ready answer:** The identity ∇p=p∇logp lets us estimate a probability-dependent reward gradient from sampled trajectories.


**Reasoning / example:** The trajectory log likelihood is a sum of action logps. Weighting ∇logπ by a detached return or advantage gives a score-function estimator without differentiating through the reward scorer.


**Common incorrect answer:** “Log is only used to make displayed numbers smaller.”


### Q18. What is importance sampling in PPO?


**Interview-ready answer:** Reweight old-policy actions by current/old action probability at the stored state.


**Reasoning / example:** ρ=exp(ℓcurrent−ℓold) motivates Eold[ρÂ]. This local surrogate does not exactly repair a changed state distribution, and extreme ratios raise variance.


**Common incorrect answer:** “Current/reference probability is the PPO clip ratio.”


### Q19. How does DPO optimize offline pairs?


**Interview-ready answer:** It minimizes negative log sigmoid of the β-scaled chosen-minus-rejected policy/reference log-ratio difference.


**Reasoning / example:** A latent reward can be reparameterized by an optimal KL-regularized policy. Pairwise reward differences cancel the prompt-only normalization and permit direct policy fitting.


**Common incorrect answer:** “DPO labels generated rollouts with an explicit learned RM.”


### Q20. Why does standard DPO still use a reference?


**Interview-ready answer:** The reward–policy correspondence is expressed relative to a fixed reference distribution and carries KL-regularized optimization structure.


**Reasoning / example:** Reference scoring can be separate, shared through adapters, or precomputed for exact pairs. Removing all reference terms changes the standard objective.


**Common incorrect answer:** “ref_model=None proves reference-free training.”


### Q21. How do you compute a response log probability?


**Interview-ready answer:** Sum selected next-token log probabilities over response tokens, with prompt and padding excluded.


**Reasoning / example:** Shift logits to predict token j+1 from position j. Standard DPO uses summed completion logps; ORPO’s odds score uses completion means. Changing aggregation changes the objective.


**Common incorrect answer:** “Average and sum are interchangeable for variable-length answers.”


### Q22. Why do chat templates and masks matter?


**Interview-ready answer:** They determine the conditioning context and exactly which tokens the loss scores.


**Reasoning / example:** Duplicate special tokens, unequal pair histories or boundary merges can move the completion boundary. Attention masks and loss masks have different purposes. Final_DPO stores a prompt-prefix mismatch warning.


**Common incorrect answer:** “A mask error only changes efficiency.”


### Q23. What is GRPO group normalization?


**Interview-ready answer:** For each prompt, subtract its group mean reward and divide by group standard deviation, with numerical handling as needed.


**Reasoning / example:** Rewards [1,0,1,0] give mean .5 and population std .5, hence advantages [1,−1,1,−1]. Outcome advantages are broadcast over response tokens.


**Common incorrect answer:** “Only mean subtraction fully describes original normalized GRPO.”


### Q24. Does GRPO require a reward model?


**Interview-ready answer:** It requires a reward signal; that signal can come from rules, tests, human/judge feedback or a learned model.


**Reasoning / example:** The first notebook path uses similarity/style functions; the original DeepSeekMath paper also uses learned reward models. Removing a critic does not remove scoring.


**Common incorrect answer:** “GRPO improves by comparing answers without any external criterion.”


### Q25. How does ORPO combine supervised and preference loss?


**Interview-ready answer:** Total loss is chosen-token NLL plus a weighted negative log sigmoid of the chosen/rejected normalized-likelihood log odds ratio.


**Reasoning / example:** The same policy supplies both scores. λ balances imitation and preference; the source configs call this coefficient beta. No separate reference is required.


**Common incorrect answer:** “ORPO is DPO with the reference terms removed and no SFT component.”


### Q26. What is the difference between probability ratio and odds ratio?


**Interview-ready answer:** Probability ratio is pw/pl; odds ratio is [pw/(1−pw)]/[pl/(1−pl)].


**Reasoning / example:** For .75 and .25, the probability ratio is3 but odds ratio is9. Log odds also contains log(1−p), so replacing it with a log probability changes the loss.


**Common incorrect answer:** “Odds is just another name for probability.”


### Q27. How does effective batch size relate to gradient accumulation?


**Interview-ready answer:** For ordinary data-parallel updates it is approximately microbatch×accumulation×world size; rollouts and GRPO candidate grouping add distinct constraints.


**Reasoning / example:** The DPO source uses1×8 on one device. GRPO candidates repeat prompts, so four candidate examples may be one prompt group. PPO also partitions rollout batches into minibatches.


**Common incorrect answer:** “All trainer batch counts mean unique prompts.”


### Q28. What does LoRA save and how should it reload?


**Interview-ready answer:** It trains low-rank adapters and saves adapter weights/configuration, which reload with the matching base model and tokenizer.


**Reasoning / example:** The detailed DPO notebooks use AutoPeftModelForCausalLM; GRPO uses PeftModel with an explicit base. Quantization reduces frozen base storage but does not remove activation costs.


**Common incorrect answer:** “An adapter alone contains a complete standalone model or full optimizer state.”


## Advanced


### Q29. Derive the main PPO clipped objective.


**Interview-ready answer:** Start with the old-policy importance-ratio surrogate Eold[ρÂ], clip ρ around1, and take the minimum of unclipped and clipped advantage-weighted contributions.


**Reasoning / example:** For A≥0 this is min(ρ,1+ε)A; for A<0 it is max(ρ,1−ε)A. Maximization then removes additional incentive in the favorable excessive-change direction; it is a heuristic local surrogate, not a strict trust-region proof.


**Common incorrect answer:** “Take min of ratios without accounting for the sign of A.”


### Q30. Derive the connection between KL-regularized reward optimization and DPO.


**Interview-ready answer:** Optimizing Eπ[r]−βDKL(π||πref) with probability normalization yields π*=πref exp(r/β)/Z. Rearrange reward and cancel βlogZ in a same-prompt Bradley–Terry comparison.


**Reasoning / example:** The derivative is r−β(log(π/πref)+1)+η=0. Reparameterizing with πθ produces the DPO logistic loss. Support, finite Z and preference-model assumptions must be stated.


**Common incorrect answer:** “DPO recovers one unique absolute reward function or guarantees neural training finds π*.”


### Q31. How should DPO beta be interpreted?


**Interview-ready answer:** It is the KL penalty parameter in the fixed-reward derivation and scales the logistic preference margin in the training loss.


**Reasoning / example:** Larger β weakens reward tilt at fixed r, but also affects gradient magnitude and saturation at fixed log-ratio margin. Actual drift depends on optimization/data/reference and cannot be inferred from beta alone.


**Common incorrect answer:** “Larger beta always means a stronger useful update or always less observed KL.”


### Q32. How does reward hacking occur?


**Interview-ready answer:** A policy exploits a mismatch between the optimized scorer and intended quality, producing high-scoring but poor answers.


**Reasoning / example:** The GRPO notebook rewards length, punctuation and avoiding uncertainty phrases, which can be gamed without semantic correctness. Evaluate with independent task tests/judgments and broaden reward coverage.


**Common incorrect answer:** “Reward hacking requires malicious intent from the model.”


### Q33. What happens when policy drift from the reference is large?


**Interview-ready answer:** It may move into regions where reward/data generalization is poor and lose useful baseline behavior, although some drift is necessary for improvement.


**Reasoning / example:** Measure KL under clearly stated sampling conditions plus independent quality and regression tests. Increase regularization or reduce update pressure only with evidence; no universal safe KL exists.


**Common incorrect answer:** “Zero KL is the best possible aligned outcome.”


### Q34. Compare PPO’s value estimate with GRPO’s group baseline.


**Interview-ready answer:** PPO predicts prefix-conditioned future return with a learned critic; GRPO derives a same-prompt empirical baseline from multiple scored responses.


**Reasoning / example:** A critic can model varying future prospects at each token. Outcome GRPO gives a sequence-level relative signal to tokens and avoids learned value approximation, at the cost of group generation and variance/normalization issues.


**Common incorrect answer:** “The group mean is an exact value function for every prefix.”


### Q35. Why can equal-reward GRPO groups fail to teach preference?


**Interview-ready answer:** All centered rewards are zero and standard deviation is zero; stabilized normalization yields zero comparative advantage.


**Reasoning / example:** All-right and all-wrong groups both have this problem. A KL term can still act, and a missing numerical stabilizer can cause NaN. Improve task difficulty/diversity/scorer granularity instead of pretending std division creates information.


**Common incorrect answer:** “No critic means no zero-variance issue.”


### Q36. How can length bias affect these algorithms?


**Interview-ready answer:** Annotators, reward models and loss aggregation can correlate longer answers with preference or weight long sequences differently.


**Reasoning / example:** Every local chosen answer is longer in characters. DPO sums logps, ORPO normalizes its odds score, and original GRPO response means differ from DAPO token means. Length-controlled evaluation and hard pairs are needed; normalization is not a universal cure.


**Common incorrect answer:** “Length normalization eliminates all preference bias.”


### Q37. What if chosen/rejected masks are wrong?


**Interview-ready answer:** The objective may score prompt/padding or mismatched contexts instead of the desired responses, invalidating the preference comparison.


**Reasoning / example:** An empty completion can give divide-by-zero in normalized scores. Unequal prompt context breaks partition cancellation assumptions. Decode scored tokens, count masks and compare padded/unpadded logps.


**Common incorrect answer:** “The error just adds a constant and does not affect gradients.”


### Q38. Is the positive GRPO KL estimator automatically exact on reused rollout data?


**Interview-ready answer:** No. q−logq−1 is nonnegative pointwise and has the desired KL expectation under current-policy action sampling with appropriate support.


**Reasoning / example:** Groups are collected from πold. Reuse, sampling mismatch, estimator gradients and optional bias corrections must be distinguished from the pointwise nonnegativity claim.


**Common incorrect answer:** “Positive samples guarantee an unbiased loss gradient under any data distribution.”


### Q39. How does ORPO’s normalized score differ from a whole-response probability?


**Interview-ready answer:** It is the geometric mean of response token probabilities, exp(mean logp), rather than their product.


**Reasoning / example:** It does not sum to1 across different response candidates, so a .75/.25 illustration is not a general two-class model. ORPO applies odds to this normalized likelihood score; token-average SFT is a separate aggregation decision.


**Common incorrect answer:** “It is calibrated confidence that the whole answer is correct.”


### Q40. Why can DPO loss improve while both candidate likelihoods fall?


**Interview-ready answer:** It optimizes their reference-adjusted difference, so the rejected likelihood can fall more than the chosen likelihood.


**Reasoning / example:** Stored chosen logp decreases from−51.20 to−58.49 and rejected from−53.96 to−77.31. The β=.1 implicit reward margin becomes≈1.61. Independent quality must determine whether that shift helped.


**Common incorrect answer:** “A chosen likelihood decrease mathematically proves DPO is implemented incorrectly.”


## Scenario


### Q41. You have only the supplied 20 preference pairs and little VRAM. What would you do?


**Interview-ready answer:** Use a small LoRA DPO or ORPO smoke experiment after mask/schema checks, while collecting larger harder data and a disjoint evaluation set.


**Reasoning / example:** All winners are longer and negatives are obvious. Reference sharing can make DPO practical; ORPO reduces reference work but changes the objective. Twenty pairs cannot justify robust alignment claims.


**Common incorrect answer:** “Switch to GRPO without a scorer or claim 100% one-pair accuracy proves success.”


### Q42. Your PPO RM trains on four rows. Is it ready for broad online optimization?


**Interview-ready answer:** No broad readiness is established; first evaluate rankings on diverse held-out and policy-generated responses.


**Reasoning / example:** The source uses one epoch without RM evaluation. Online exploration may exploit random/new scalar-head errors. More policy episodes cannot repair a poor preference proxy.


**Common incorrect answer:** “The successful save message proves the reward model is trustworthy.”


### Q43. The DPO log-history DataFrame contains NaNs. How would you diagnose it?


**Interview-ready answer:** Inspect original event dictionaries and explicit finite losses/gradients before declaring numerical divergence.


**Reasoning / example:** Eval and final-summary events lack training fields, so Pandas fills absent columns with NaN. If actual loss is nonfinite, check masks, precision and token IDs; distinguish missing data from arithmetic NaN.


**Common incorrect answer:** “Every displayed NaN means the model weights are corrupt.”


### Q44. The GRPO notebook says batch must divide by G but its second path uses batch1 and G4. What would you check?


**Interview-ready answer:** Inspect the installed effective generation batch across devices/steps and configure a supported grouping scheme.


**Reasoning / example:** The second path reinstalls unpinned packages and has no saved outputs. The first-path signature cannot certify its config. Per-device divisibility is not a universal rule, but default single-device1/G4 may be incompatible.


**Common incorrect answer:** “It must be valid because the notebook is named Final.”


### Q45. ORPO inference raises a CUDA assert after a reported training result. What next?


**Interview-ready answer:** Restart the poisoned runtime, reproduce a tiny generation synchronously, and inspect vocabulary/token IDs, EOS/PAD config and dependency compatibility.


**Reasoning / example:** CUDA errors are asynchronous; the cleanup traceback can point later than the cause. The notebook has two environment paths and initial state-dependent deletes. Training output does not establish successful inference.


**Common incorrect answer:** “Always reinstall torchao or reduce beta without inspecting the failing input.”


### Q46. A verifiable math task has almost all wrong GRPO samples. How would you proceed?


**Interview-ready answer:** Verify parsing/reward metadata, choose learnable difficulty, and improve sampling/model/SFT so groups contain useful differences.


**Reasoning / example:** If all rewards are zero, stabilized group advantages vanish. Add reliable partial credit only if it tracks desired behavior; pure format bonuses can reward wrong answers. Increase G only if compute and useful diversity justify it.


**Common incorrect answer:** “Invent random reward noise so the optimizer always has variance.”


### Q47. A company asks for the universally best optimizer. How would you answer?


**Interview-ready answer:** There is no universal winner: compare supervision, fresh-answer scoring needs, generation budget, reference/critic costs and held-out task results.


**Reasoning / example:** Offline pairs suggest DPO/ORPO; verifiable group rewards suggest GRPO; a validated flexible RM with rollout budget can justify PPO. Source demos do not provide a controlled head-to-head benchmark.


**Common incorrect answer:** “DPO is always safest because a PDF ranks its popularity.”


### Q48. Can you rerun the whole ORPO notebook sequentially in one runtime?


**Interview-ready answer:** It needs repair/separation: initial deletes depend on previous state, and standard versus Unsloth sections request different TRL environments.


**Reasoning / example:** Use one clean environment path, inspect its import/signatures, validate formatting and run a small batch. Do not mix experimental processing_class and older tokenizer keywords uncritically.


**Common incorrect answer:** “Pinned TRL alone guarantees every dependency and runtime state is compatible.”


### Q49. The racing notebook requests 100 timesteps but reports 2048. Is this fabricated?


**Interview-ready answer:** Not necessarily: on-policy PPO collects a complete n_steps=2048 rollout, so the requested minimum is exceeded.


**Reasoning / example:** The saved Stable-Baselines3 output explicitly records one 2048-step iteration. This is still a tiny learning run and the reward−58.6 does not establish driving competence.


**Common incorrect answer:** “learn(total_timesteps=100) must produce exactly100 environment transitions.”


### Q50. Your reward-trained checkpoint initializes both RM and critic. Is that a bug?


**Interview-ready answer:** Not inherently. Reward and value models may share initialization while training to different targets thereafter.


**Reasoning / example:** The PPO source freezes reward_model and leaves value_model trainable. Verify per-prefix value use, target scale and model interface; copying weights alone does not make the critic calibrated for shaped returns.


**Common incorrect answer:** “They must remain the same model forever or can never initialize from each other.”


## Rapid revision: the final fifteen minutes

1. Draw the classical pipeline: pretrained/SFT policy → preference pairs → RM → PPO → independent evaluation.
2. State the roles: policy generates; reference gives baseline probabilities; RM scores answers; critic predicts return.
3. Recite `return=sum future discounted rewards`, `advantage=Q−V`, and `GAE=sum weighted TD residuals`.
4. PPO: ratio=current/old, clipped min surrogate, actor minus sign under minimization, separate critic loss. No hard update bound.
5. DPO: chosen-minus-rejected policy/reference log-ratio margin → negative log sigmoid. Fixed reference; partition function cancels within a prompt.
6. GRPO: sample group → score → mean/std → relative advantages → clipped token objective and original explicit KL. Equal rewards erase comparison signal.
7. ORPO: chosen NLL + weighted preference loss on normalized-likelihood log odds. No reference. Probability, odds and log odds differ.
8. Source pitfalls: stateless bandit demo; dummy DQN batch; unused Final_DPO literal; identical detailed DPO source; GRPO DAPO default and second-path grouping; ORPO CUDA errors and split environments; local file not default active data.
9. Debug in order: data/context → token IDs/templates/masks → scoring/advantages → precision/versions → updates → independent evaluation.
10. Finish selection answers with a held-out pilot and regression checks. Never turn a saved loss or one-example accuracy into a broad alignment claim.
