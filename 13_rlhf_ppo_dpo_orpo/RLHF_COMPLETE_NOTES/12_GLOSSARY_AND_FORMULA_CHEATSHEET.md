# 12 — Glossary and formula cheat sheet

[Home](README.md) · [Previous: Interview preparation](11_INTERVIEW_PREPARATION.md) · [Next: Home](README.md)

## Glossary

| Term | Definition |

|---|---|

| RLHF | Reinforcement learning from human feedback; commonly preference RM training followed by RL policy optimization. |

| SFT | Supervised fine-tuning; imitation of demonstrated responses using token likelihood. |

| PPO | Proximal Policy Optimization; clipped local policy-gradient surrogate, commonly actor-critic. |

| DPO | Direct Preference Optimization; offline pairwise likelihood fit through policy/reference ratios. |

| GRPO | Group Relative Policy Optimization; rollout-based same-prompt relative-reward advantages, originally without learned critic. |

| ORPO | Odds Ratio Preference Optimization; chosen SFT plus odds-ratio preference loss without a reference model. |

| Policy | State-conditioned action distribution; in an LLM, next-token probabilities. |

| Reference policy | Baseline distribution fixed during standard preference/RL regularization, possibly implemented through sharing/caching. |

| Old/behavior policy | Policy distribution that generated stored rollout actions; PPO ratio denominator. |

| Reward model | Scalar preference scorer trained from feedback comparisons. |

| Reward signal | Actual numeric score used by optimization, whether supplied by model, rules or environment. |

| Critic | Learned value predictor used to estimate expected future return and advantages. |

| Value function | Vπ(s), expected return from a state under policy π. |

| Action-value function | Qπ(s,a), expected return after a specified first action and policy continuation. |

| Advantage | Q−V; action return relative to policy baseline. |

| Return | Discounted sum of future rewards along a trajectory. |

| Rollout | Collection of sampled policy trajectories and associated training statistics. |

| Trajectory | Ordered states/actions/rewards; an LLM generated response with prefixes. |

| Episode | One interaction/generation until a terminal/stopping condition. |

| MDP | Markov decision process: states, actions, transitions, rewards, initial distribution and discount. |

| Markov property | Current state contains relevant information needed to predict next transition/reward. |

| Discount factor | γ; controls contribution of later rewards to return. |

| Termination / truncation | Genuine task ending versus artificial stopping/time limit; bootstrap treatment can differ. |

| KL divergence | Asymmetric expected log-density ratio between distributions. |

| Entropy | Expected negative log probability; a distribution uncertainty/diversity measure. |

| GAE | Generalized Advantage Estimation; weighted sum of TD residuals. |

| TD learning | Temporal-difference learning; uses bootstrapped future estimates in updates. |

| Monte Carlo learning | Learning from sampled completed returns without a bootstrap target. |

| Importance sampling | Distribution-change reweighting by target/sampling probability ratio. |

| Clipping | PPO objective mechanism limiting further incentive for beneficial ratio changes beyond a chosen interval; distinct from gradient norm clipping. |

| Log probability | Natural logarithm of probability; sequence log likelihood adds token log probabilities. |

| Odds ratio | Ratio of p/(1−p) values for two candidates. |

| Log odds | log p−log(1−p), not just log p. |

| Chosen/rejected pair | Same-context winner and loser as encoded by preference columns. |

| Bradley–Terry model | Logistic probability of pairwise preference from a scalar reward difference. |

| Reward hacking | Optimizing proxy scores through behavior that fails intended quality. |

| On-policy / off-policy | Learning mainly from current-policy trajectories versus allowing a different behavior distribution. |

| Offline / online | Optimization from fixed data versus collecting fresh interaction/generation data in the loop. |

| Actor-critic | Policy optimization with a value predictor supporting return/advantage estimation. |

| Q-learning / SARSA | Value updates using greedy next action target versus policy-sampled next action target. |

| DQN | Deep Q-network; neural action values, commonly replay and target network. |

| Exploration / exploitation | Trying uncertain actions versus favoring currently estimated good actions. |

| Partition function | Z(x), normalization of reference-weighted exponentiated reward in DPO derivation. |

| Implicit reward | Policy/reference log ratio interpreted as reward up to a prompt-only constant in DPO. |

| Completion mask | Selects response tokens scored by an objective; excludes prompt and padding. |

| Attention mask | Identifies active tokens for attention; separate from objective scoring masks. |

| Chat template | Model-specific serialization of user/system/assistant messages and special tokens. |

| BOS / EOS / PAD | Beginning-of-sequence, end-of-sequence and padding token conventions. |

| Logits | Unnormalized token scores before softmax. |

| Length-normalized likelihood | Geometric mean of response token probabilities; used in original ORPO odds scoring. |

| Group size | G, number of sampled answers for one GRPO prompt. |

| Zero-variance group | Group whose rewards are identical; comparative normalized advantage is zero with stable handling. |

| Outcome / process supervision | Reward for complete response versus intermediate reasoning steps. |

| DAPO aggregation | Later token-weighted objective variant; recorded GRPOConfig default differs from original response-mean weighting. |

| LoRA | Low-rank adapters updating selected layers with relatively few trainable parameters. |

| QLoRA | Low-rank training with a quantized frozen base model, commonly 4-bit. |

| PEFT | Parameter-efficient fine-tuning library/method category used for adapters. |

| Gradient accumulation | Sum microbatch gradients before an optimizer step to increase effective batch. |

| Gradient checkpointing | Recompute activations during backward to save activation memory. |

| Checkpoint | Saved training/model state; faithful resume requires optimizer/scheduler/RNG as well as model. |

| Calibration | Agreement between modeled scores/probabilities and observed quality or preference frequencies. |

| Length bias | Preference/reward/objective dependence on response length beyond intended task quality. |

| Distribution shift | Mismatch between training/scorer data and later inputs or policy-generated responses. |

| Mode collapse | Reduced behavioral diversity such as repetitive answers across prompts. |

| Catastrophic forgetting | Loss of previously useful abilities during later training. |

| KTO | Kahneman–Tversky Optimization; direct alignment from desirable/undesirable judgments; mentioned, not implemented here. |

| SimPO | Simple Preference Optimization; distinct reference-free preference method mentioned by ORPO PDF. |

| RLVR | Reinforcement learning with verifiable rewards; reward source category, not one optimizer. |

| CoT / PoT | Chain-of-thought / program-of-thought response styles in source DeepSeekMath discussion. |

| vLLM | Generation engine used by source Unsloth GRPO alternative. |

| NF4 | NormalFloat4 quantization format configured in the detailed DPO QLoRA path. |

| Explained variance | 1−Var(target−prediction)/Var(target); critic diagnostic undefined for constant targets. |


## Formula cheat sheet

All logs are natural. Rewards use R, ratios use ρ, and coefficients are distinguished by algorithm. Equations assume the stated masks/support/terminal handling; implementation variants belong in their algorithm chapter.


### Return


$$
G_t=\sum_{k=0}^{T-1-t}\gamma^kR_{t+k}
$$


**Calculates / used in:** RL/PPO. **Symbols:** R is reward after an action, T episode actions, γ discount. **Interpretation:** Counts future feedback from time t; terminal means no further value.


### Values and advantage


$$
V^\pi(s)=\mathbb E[G_t|s];\quad Q^\pi(s,a)=\mathbb E[G_t|s,a];\quad A^\pi=Q^\pi-V^\pi
$$


**Calculates / used in:** RL/PPO. **Symbols:** π policy, s state, a action. **Interpretation:** Value averages policy actions; advantage centers the chosen action.


### Bellman expectation


$$
Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\pi(s');\quad V^\pi(s)=\sum_a\pi(a|s)Q^\pi(s,a)
$$


**Calculates / used in:** RL. **Symbols:** r expected immediate reward, P transition probability. **Interpretation:** Separate first reward from expected discounted future.


### Bellman optimality


$$
Q^*(s,a)=r(s,a)+\gamma\sum_{s'}P(s'|s,a)\max_{a'}Q^*(s',a')
$$


**Calculates / used in:** Q-learning/DQN. **Symbols:** Star optimal values; a′ possible next action. **Interpretation:** Greedy next-state target under specified reward.


### TD and Q update


$$
Q(s,a)\leftarrow Q(s,a)+\alpha[R+\gamma(1-d)\max_{a'}Q(s',a')-Q(s,a)]
$$


**Calculates / used in:** Q-learning/DQN. **Symbols:** α update rate, d terminal flag. **Interpretation:** Moves toward a bootstrap target, not certain ground truth.


### Policy gradient


$$
\nabla J\propto\mathbb E_{s\sim d^\pi,a\sim\pi}[A^\pi(s,a)\nabla\log\pi_\theta(a|s)]
$$


**Calculates / used in:** Policy gradients/PPO/GRPO. **Symbols:** dπ normalized discounted occupancy, θ trainable actor. **Interpretation:** Score-function estimator; occupancy normalization determines constant.


### Importance ratio


$$
\rho_t=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}=e^{\ell_{\theta,t}-\ell_{old,t}}
$$


**Calculates / used in:** PPO/GRPO. **Symbols:** ℓ selected action logp, old frozen behavior distribution. **Interpretation:** Weights new likelihood on old actions; reference is a different role.


### Entropy and KL


$$
H(p)=-\sum_a p(a)\log p(a);\quad D_{KL}(p\|q)=\sum_a p(a)\log\frac{p(a)}{q(a)}
$$


**Calculates / used in:** RL regularization. **Symbols:** p target policy distribution, q supported baseline. **Interpretation:** Entropy describes uncertainty; KL describes asymmetric drift.


### GAE


$$
\delta_t=R_t+\gamma(1-d_t)V_{old}(s_{t+1})-V_{old}(s_t);\quad \hat A_t=\delta_t+\gamma\lambda_{GAE}(1-d_t)\hat A_{t+1}
$$


**Calculates / used in:** PPO. **Symbols:** λGAE residual weighting; d genuine terminal. **Interpretation:** Mixes short and long credit estimates; targets detached.


### Value loss


$$
\hat G_t=\hat A_t^{raw}+V_{old}(s_t);\quad \mathcal L_V=\tfrac12\mathbb E[(V_\phi(s_t)-\hat G_t)^2]
$$


**Calculates / used in:** PPO. **Symbols:** φ critic parameters; raw advantage before actor normalization. **Interpretation:** Fits predicted return to rollout target; optional value clipping differs.


### PPO surrogate


$$
L^{CLIP}=\mathbb E[\min(\rho\hat A,\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)\hat A)]
$$


**Calculates / used in:** PPO. **Symbols:** ε clip width; Â fixed rollout advantage. **Interpretation:** Maximize this; minimizing actor loss negates it. No hard update bound.


### One possible total PPO loss


$$
\mathcal L=-L^{CLIP}+c_V\mathcal L_V-c_HH+\kappa_{explicit}D_{KL}
$$


**Calculates / used in:** PPO variant. **Symbols:** cV value weight, cH entropy weight, κ explicit KL if used. **Interpretation:** Library-specific; avoid unintended KL duplication with shaped rewards.


### RM comparison


$$
P(y_w\succ y_l|x)=\sigma(r_\psi(x,y_w)-r_\psi(x,y_l));\quad \mathcal L_{RM}=-\mathbb E\log P
$$


**Calculates / used in:** RM/DPO derivation. **Symbols:** ψ RM parameters, x shared prompt, yw/yl preferred/less preferred. **Interpretation:** Logistic pairwise utility model; prompt additive constants cancel.


### DPO optimal policy


$$
\pi^*(y|x)=\frac{\pi_{ref}(y|x)e^{r(x,y)/\beta}}{Z(x)};\quad Z(x)=\sum_y\pi_{ref}(y|x)e^{r(x,y)/\beta}
$$


**Calculates / used in:** DPO derivation. **Symbols:** β>0 KL penalty; finite Z, reference support required. **Interpretation:** Exponential reward tilt of reference, not guaranteed neural optimum.


### Implicit reward


$$
\hat r_\theta(x,y)=\beta\log\frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)}
$$


**Calculates / used in:** DPO. **Symbols:** Reward defined up to c(x); true derivation includes βlogZ. **Interpretation:** Relative policy promotion acts as latent preference utility.


### DPO loss


$$
\mathcal L_{DPO}=-\mathbb E\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)
$$


**Calculates / used in:** DPO. **Symbols:** θ current policy, β scale, reference fixed, responses use completion-summed logps. **Interpretation:** Fit reference-adjusted pair margin; chosen absolute likelihood can fall.


### Group advantage


$$
\mu=\frac1G\sum_iR_i;\quad s=\sqrt{\frac1G\sum_i(R_i-\mu)^2};\quad\hat A_{i,t}=\frac{R_i-\mu}{s+\varepsilon_{norm}}
$$


**Calculates / used in:** Outcome GRPO. **Symbols:** G responses per prompt; practical εnorm; sample/population std conventions vary. **Interpretation:** Within-prompt relative signal; all equal rewards yield zero with stable handling.


### Original GRPO objective


$$
J=\mathbb E\left[\frac1G\sum_i\frac1{T_i}\sum_t\left(\min(\rho_{i,t}\hat A_{i,t},\operatorname{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)\hat A_{i,t})-\kappa_{GRPO}\hat K_{i,t}\right)\right]
$$


**Calculates / used in:** Original GRPO. **Symbols:** Ti active response length; κGRPO explicit KL coefficient. **Interpretation:** Response/group mean weighting differs from later token-mean defaults.


### Positive KL estimator


$$
q=\pi_{ref}(a|s)/\pi_\theta(a|s);\quad\hat K=q-\log q-1
$$


**Calculates / used in:** Original GRPO. **Symbols:** q reference/current ratio, expectation claim under current-policy action sampling. **Interpretation:** Nonnegative pointwise; reused old-policy samples require care.


### Sequence scoring


$$
\ell=\sum_tm_t\log\pi_\theta(y_t|x,y_{<t});\quad\bar\ell=\ell/\sum_tm_t;\quad p=e^{\bar\ell}
$$


**Calculates / used in:** DPO sum; ORPO mean. **Symbols:** mt completion mask; nonempty active targets required. **Interpretation:** p is geometric mean, not a normalized distribution over full responses.


### ORPO odds


$$
\operatorname{odds}(p)=\frac p{1-p};\quad\Delta_{OR}=\log\frac{p_w/(1-p_w)}{p_l/(1-p_l)}
$$


**Calculates / used in:** ORPO. **Symbols:** pw/pl normalized completion likelihood scores, strictly between0 and1. **Interpretation:** Log odds includes complement probability; distinguish probability ratio.


### ORPO total


$$
\mathcal L_{ORPO}=\mathcal L_{SFT}+\lambda_{OR}\left[-\mathbb E\log\sigma(\Delta_{OR})\right]
$$


**Calculates / used in:** ORPO. **Symbols:** λOR balances components; source TRL calls it beta; chosen NLL usually token averaged. **Interpretation:** Imitation and preference in one objective without a reference.


### Logistic loss identity


$$
-\log\sigma(z)=\operatorname{softplus}(-z)
$$


**Calculates / used in:** RM/DPO/ORPO. **Symbols:** z RM reward difference, DPO margin or ORPO log-odds difference. **Interpretation:** Stable way to compute preference loss; different methods supply different margins.


## Five-minute final comparison

| Method | Essential supervision | Core calculation | Typical extra roles | First debugging checks |
|---|---|---|---|---|
| PPO RLHF | Prompts plus scorer for fresh rollouts | Clipped advantage-ratio surrogate + critic loss | Reference, RM/function, critic | Old/reference distinction, shaped rewards, GAE, masks |
| DPO | Offline chosen/rejected pairs | −logσ(β×relative log-ratio margin) | Fixed reference scoring | Shared context, summed completion logps, ref frozen |
| GRPO | Prompts plus group scorer | Group-normalized advantages and policy objective | Reference in original; optional RM | Group size/batch, reward std, parser, aggregation variant |
| ORPO | Offline chosen/rejected pairs | Chosen NLL + λ×odds comparison loss | No separate reference/RM/critic | Mean logps, log(1−p) numerics, NLL balance |

**Do not confuse:** PPO old policy with reference; RM with critic; DPO β with ORPO coefficient; true sequence probability with ORPO normalized score; observed source output with newly measured results.

**Source anchors:** detailed DPO notebook cells23–31; PPO cells14–20; GRPO first path cells24–32 and second path42–51; ORPO cells13–17 and25–29. See [notebook audit](assets/source_audit/NOTEBOOK_AUDIT.md) for every cell and [inventory](SOURCE_INVENTORY.md) for all sources.
