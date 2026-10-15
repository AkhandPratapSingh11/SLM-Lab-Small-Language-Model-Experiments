# 🏆 Master Alignment Study Guide: RL, RLHF, PPO, DPO, ORPO & GRPO

> **Complete Technical Reference & Research Companion for Small Language Model (SLM) Alignment**
> Location: `/nuvodata/User_data/ak57139k/anmolpro/SLM_Experiment/13_rlhf_ppo_dpo_orpo`

---

# Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [Complete File Inventory](#2-complete-file-inventory)
3. [What This Module Is Teaching](#3-what-this-module-is-teaching)
4. [Prerequisites](#4-prerequisites)
5. [Reinforcement Learning Fundamentals](#5-reinforcement-learning-fundamentals)
6. [RL for Language Models](#6-rl-for-language-models)
7. [RLHF Pipeline Architecture](#7-rlhf-pipeline-architecture)
8. [Reward Modeling](#8-reward-modeling)
9. [PPO: Proximal Policy Optimization](#9-ppo-proximal-policy-optimization)
10. [RLHF + PPO Code Implementation](#10-rlhf--ppo-code-implementation)
11. [Why PPO Is Difficult for LLMs](#11-why-ppo-is-difficult-for-llms)
12. [DPO Theory](#12-dpo-theory)
13. [DPO Mathematical Derivation](#13-dpo-mathematical-derivation)
14. [DPO Implementation](#14-dpo-implementation)
15. [Comparison of DPO Notebooks](#15-comparison-of-dpo-notebooks)
16. [ORPO Theory](#16-orpo-theory)
17. [ORPO Implementation](#17-orpo-implementation)
18. [GRPO Theory](#18-grpo-theory)
19. [GRPO Implementation](#19-grpo-implementation)
20. [PPO vs DPO vs ORPO vs GRPO Comparison](#20-ppo-vs-dpo-vs-orpo-vs-grpo-comparison)
21. [Conceptual Evolution](#21-conceptual-evolution)
22. [Mathematical Cheat Sheet](#22-mathematical-cheat-sheet)
23. [Code-to-Concept Mapping](#23-code-to-concept-mapping)
24. [Dataset Analysis](#24-dataset-analysis)
25. [Models](#25-models)
26. [Hyperparameters Reference](#26-hyperparameters-reference)
27. [Dependencies & Environment](#27-dependencies--environment)
28. [Reproduction & Execution Guide](#28-reproduction--execution-guide)
29. [Code Review & Potential Issues](#29-code-review--potential-issues)
30. [Research Methodology](#30-research-methodology)
31. [File-by-File Reference](#31-file-by-file-reference)
32. [Recommended Learning Path](#32-recommended-learning-path)
33. [Interview & Exam Questions](#33-interview--exam-questions)
34. [Final Mental Model](#34-final-mental-model)

---

# 1. Executive Summary

This study guide provides an exhaustive technical analysis of the repository module located at `/nuvodata/User_data/ak57139k/anmolpro/SLM_Experiment/13_rlhf_ppo_dpo_orpo`.

The module represents an end-to-end curriculum on **Post-Training Alignment and Preference Optimization for Small Language Models (SLMs)**. It bridges classical Reinforcement Learning (RL), human-aligned preference optimization, and rule-based reasoning reinforcement learning:
1. **Classical RL Foundations & Deep Q-Learning:** Tabular bandit updates, Deep Q-Networks (DQN) with experience replay and target networks, and actor-critic policy gradients (Stable-Baselines3 PPO on Gymnasium).
2. **Classical RLHF (Reinforcement Learning from Human Feedback):** A 4-model architecture (Policy, Value/Critic, Reward Model, Reference Model) utilizing Hugging Face TRL's modern `PPOTrainer` and `RewardTrainer` on `SmolLM2-135M-Instruct`.
3. **Implicit Reward Modeling via DPO (Direct Preference Optimization):** Elimination of the explicit reward model and PPO rollout loop by parameterizing the Bradley-Terry preference objective directly via policy and reference log-probabilities on `Qwen2.5-0.5B-Instruct`.
4. **Monolithic Reference-Free Alignment via ORPO (Odds Ratio Preference Optimization):** Combining supervised fine-tuning (SFT) and preference alignment into a single training stage without a reference model or reward model using an odds-ratio penalty on `Qwen2-0.5B-Instruct`.
5. **Reasoning-Oriented Alignment via GRPO (Group Relative Policy Optimization):** DeepSeekMath / DeepSeek-R1 style policy gradient optimization that eliminates the critic/value network entirely by estimating advantages from group-normalized rewards across multiple sampled completions per prompt, evaluated on `SmolLM-135M-Instruct` and `Qwen2.5-0.5B-Instruct` with Unsloth + vLLM on GSM8K math reasoning with XML tags.

---

# 2. Complete File Inventory

The directory contains **15 core files** across three primary modalities:

| # | Filename | Type | Size / Pages / Lines | Core Role in Module |
|---|---|---|---|---|
| 1 | `RL_Fundamental.ipynb` | Jupyter Notebook | 28 cells (25 code, 3 md) | Fundamental RL: 2-arm Bandit, PyTorch DQN implementation, SB3 PPO on CarRacing-v3 |
| 2 | `RLHF_with_PPO_Final_Code.ipynb` | Jupyter Notebook | 23 cells (23 code, 0 md) | End-to-end RLHF pipeline: Bradley-Terry Reward Model training + 4-model TRL PPO training |
| 3 | `Final_DPO.ipynb` | Jupyter Notebook | 15 cells (15 code, 0 md) | Initial/pedagogical DPO baseline script using TRL DPOTrainer on Qwen2.5-0.5B-Instruct |
| 4 | `DPO_Training.ipynb` | Jupyter Notebook | 47 cells (21 code, 26 md) | Refactored, production-grade DPO notebook with extensive markdown, bugfixes, pre/post eval |
| 5 | `DPO_Training_Final.ipynb` | Jupyter Notebook | 47 cells (21 code, 26 md) | Sibling clone of `DPO_Training.ipynb` with identical code cells, containing run logs |
| 6 | `Final_ORPO_Practical.ipynb` | Jupyter Notebook | 33 cells (32 code, 1 md) | ORPO practical: Part 1 (HF TRL ORPOTrainer), Part 2 (Unsloth FastLanguageModel + PatchDPOTrainer) |
| 7 | `Final_GRPO_Practical.ipynb` | Jupyter Notebook | 54 cells (42 code, 12 md) | GRPO practical: Part 1 (TRL GRPOTrainer + custom text rewards), Part 2 (Unsloth + vLLM + GSM8K XML rewards) |
| 8 | `RLHF-Updated-Recent-Latest.pdf` | Scanned Tablet Notes | 50 pages (45 content, 5 trailing blank) | Comprehensive visual notes: Why SFT fails, RL taxonomy, DQN mechanics, PPO clipping, full RLHF pipeline |
| 9 | `DPO-Handwritten-Notes.pdf` | Scanned Tablet Notes | 18 pages (all content) | DPO mathematical derivation, Bradley-Terry formulation, implicit reward, loss graphs, numerical examples |
| 10 | `DPO-Updated-handwritten-notes.pdf` | Scanned Tablet Notes | 19 pages (18 content, 1 trailing blank) | Revision 2 of DPO handwritten notes |
| 11 | `DPO-Handwritten-final-update-Notes.pdf` | Scanned Tablet Notes | 21 pages (18 content, 3 trailing blank) | Revision 3 of DPO handwritten notes |
| 12 | `GRPO-Handwritten-Final-Notes.pdf` | Scanned Tablet Notes | 12 pages (all content) | DeepSeekMath lineage, PPO vs GRPO architectural comparison, group relative advantage formulation, reward signal vs model |
| 13 | `LLM-Finetuning-ORPO.pdf` | Typed Digital Notes | 17 pages (14,960 text chars) | Complete lecture script on ORPO: EMNLP 2024 paper background, monolithic design, odds vs probability, numerical walkthrough, industry adoption |
| 14 | `reward_preferences_dataset.jsonl` | JSONL Dataset | 20 lines (4,673 bytes) | Pairwise preference dataset with schema: `{"prompt": str, "chosen": str, "rejected": str}` |
| 15 | `README.md` | Markdown | 19 lines (1,151 bytes) | Module syllabus and architectural overview outlining objectives across PPO, DPO, KTO, ORPO, GRPO |

---

# 3. What This Module Is Teaching

```
                           ┌───────────────────────────┐
                           │      Pretrained LLM       │
                           │(Knowledge & Token Modeling)│
                           └─────────────┬─────────────┘
                                         │
                                         ▼
                           ┌───────────────────────────┐
                           │   Supervised Fine-Tuning  │
                           │   (SFT: Instruction/Chat) │
                           └─────────────┬─────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│  Classical RLHF  │           │Direct Preference │           │ Reasoning-Guided │
│  (Online RL)     │           │  Optimization    │           │    Online RL     │
├──────────────────┤           ├──────────────────┤           ├──────────────────┤
│• Pairwise Data   │           │• Offline Pairs   │           │• Verifiable Tasks│
│• Train Reward RM │           │• Closed-Form RM  │           │• Rule Rewards    │
│• PPO Policy Loop │           │• DPO (Ref Model) │           │• GRPO (No Critic)│
│• Actor-Critic    │           │• ORPO (1-Stage)  │           │• Group Baselines │
└────────┬─────────┘           └────────┬─────────┘           └────────┬─────────┘
         │                              │                              │
         ▼                              ▼                              ▼
  Aligned Conversational LLM     Aligned Conversational LLM      DeepSeek-R1 Style Reasoning
```

### The Three Alignment Paradigms Taught:
1. **Classical RLHF (PPO):** Train a scalar Reward Model $r_\psi(x, y)$ on pairwise preferences using Bradley-Terry loss. Freeze it. Use PPO with a learned Critic $V_\phi(s)$ to provide token-level advantage estimates, regularized by a KL divergence penalty against frozen $\pi_{\text{ref}}$.
2. **Direct Preference (DPO & ORPO):** Algebraically eliminate the explicit reward model and RL loop by showing that optimal policy $\pi^*$ analytically specifies the reward. Parameterize Bradley-Terry directly with policy and reference log probabilities (DPO). ORPO further merges SFT and preference tuning into a single reference-free stage using odds ratios.
3. **Group-Relative Reasoning (GRPO):** For verifiable domains (math, code), replace human preference pairs with deterministic rule evaluators. Eliminate the critic model entirely by sampling a group of $G$ outputs per prompt and standardizing rewards relative to the group mean and variance.

---

# 4. Prerequisites

- **Probability & Statistics:** Joint probability chains, conditional distributions, expectations, odds ratios ($\frac{p}{1-p}$), Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$, and KL divergence.
- **Deep Learning Architectures:** Autoregressive Transformers, causal masking, sequence classification heads, LoRA, and 4-bit NormalFloat (NF4) quantization.
- **Reinforcement Learning:** MDP formulation, state transitions, Bellman optimality, on-policy vs off-policy updates, actor-critic architectures, advantage estimation.
- **Tooling:** PyTorch, Hugging Face `transformers`, `peft`, `datasets`, and `trl` (Transformer Reinforcement Learning), Unsloth, vLLM.

---

# 5. Reinforcement Learning Fundamentals

```
                   Action a_t
       ┌───────────────────────────────┐
       ▼                               │
┌──────────────┐               ┌───────────────┐
│ Environment  │               │     Agent     │
│              ├──────────────►│               │
└──────────────┘  State s_t    └───────────────┘
                  Reward r_t
```

### Core Concepts and Equations:
1. **Discounted Return ($G_t$):**
   $$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}$$
   - Measures cumulative future rewards discounted by $\gamma \in [0, 1)$. In LLM generation, $\gamma = 1.0$ is common since episodes span a single prompt-response.
2. **State-Value Function ($V^\pi(s)$):**
   $$V^\pi(s) = \mathbb{E}_\pi \left[ G_t \mid s_t = s \right]$$
   - "How good is it to be in state $s$?"
3. **Action-Value Function ($Q^\pi(s, a)$):**
   $$Q^\pi(s, a) = \mathbb{E}_\pi \left[ G_t \mid s_t = s, a_t = a \right] = r(s, a) + \gamma \sum_{s'} P(s' \mid s, a) V^\pi(s')$$
   - "How good is it to take action $a$ in state $s$?"
4. **Advantage Function ($A^\pi(s, a)$):**
   $$A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$$
   - "How much better or worse is action $a$ compared to the baseline expected performance in state $s$?"

---

# 6. RL for Language Models

| RL Concept | LLM Equivalent | Implementation in Code |
|---|---|---|
| **Agent** | Autoregressive Policy Network ($\pi_\theta$) | `AutoModelForCausalLM` |
| **State ($s_t$)** | Token context: Prompt $x$ + prefix tokens $y_{<t}$ | `input_ids[:, :t]` |
| **Action ($a_t$)** | Next emitted token $y_t \in \mathcal{V}$ | `input_ids[:, t]` |
| **Policy ($\pi(a_t \mid s_t)$)** | Softmax over vocabulary logits | `F.softmax(logits, dim=-1)` |
| **Reward ($r_t$)** | Terminal score from Reward Model or Rule Verifier | $r_\psi(x, y)$ or regex score |
| **Episode ($\tau$)** | One full prompt-response rollout ending at EOS | `[x, y_1, \dots, y_T]` |
| **Environment** | Prompt dataset + Reward evaluator | DataLoader + Reward Function |

---

# 7. RLHF Pipeline Architecture

```
   [Pretrained Base LLM]
             │
             ▼
   [Supervised Fine-Tuning (SFT)] ───► Forms SFT Policy π_SFT
             │
             ├────────────────────────────────────────┐
             ▼                                        ▼
   [Collect Preference Data]              [Initialize Reference Model]
    (x, y_chosen, y_rejected)                    π_ref = π_SFT (Frozen)
             │
             ▼
   [Train Reward Model r_ψ]
   (Bradley-Terry Classification)
             │
             ▼
    [Freeze Reward Model]
             │
             ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        PPO ONLINE TRAINING LOOP                        │
│                                                                        │
│  1. Sample Prompt: x ~ D                                               │
│  2. Rollout: π_θ generates completion y = (y_1, ..., y_T)              │
│  3. Score Rollout: r_total = r_ψ(x, y) - β * D_KL(π_θ || π_ref)        │
│  4. Critic Predicts Values: V_ϕ(s_t) for all t                         │
│  5. Generalized Advantage Estimation: A_t = GAE(r_total, V_ϕ)          │
│  6. Multi-Epoch PPO Updates:                                           │
│     - Update Actor π_θ using Clipped Surrogate Objective               │
│     - Update Critic V_ϕ using Clipped MSE Value Loss                   │
└────────────────────────────────────────────────────────────────────────┘
             │
             ▼
   [Aligned Policy Model π_θ]
```

### The 4 Concurrent Models in RLHF:
1. **Actor / Policy ($\pi_\theta$):** The model being aligned; generates rollouts, updated via policy gradients.
2. **Reference Model ($\pi_{\text{ref}}$):** Frozen copy of $\pi_{\text{SFT}}$ providing KL divergence penalty.
3. **Reward Model ($r_\psi$):** Evaluates completed prompt-response pairs with scalar scores. Frozen during PPO.
4. **Critic / Value Model ($V_\phi$):** Predicts expected future reward from state $s_t$, providing the baseline for advantage estimation.

---

# 8. Reward Modeling

The Bradley-Terry model posits:
$$p^*(y_w \succ y_l \mid x) = \sigma\left(r^*(x, y_w) - r^*(x, y_l)\right) = \frac{1}{1 + e^{-(r^*(x, y_w) - r^*(x, y_l))}}$$

The reward model loss function minimizes negative log-likelihood:
$$\mathcal{L}_{\text{RM}}(\psi) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma\left(r_\psi(x, y_w) - r_\psi(x, y_l)\right) \right]$$

---

# 9. PPO: Proximal Policy Optimization

1. **Probability Ratio:**
   $$r_t(\theta) = \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)}$$
2. **Clipped Surrogate Objective:**
   $$\mathcal{L}^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \; \text{clip}\left(r_t(\theta), 1 - \epsilon, 1 + \epsilon\right) \hat{A}_t \right) \right]$$
   - Clipping prevents destructive updates when $r_t(\theta)$ strays beyond $[1-\epsilon, 1+\epsilon]$ (typically $[0.8, 1.2]$).
3. **KL Penalty Regularization:**
   $$R(s_t, a_t) = r(s_t, a_t) - \beta_{\text{KL}} \log \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\text{ref}}(a_t \mid s_t)}$$

---

# 10. RLHF + PPO Code Implementation

From `RLHF_with_PPO_Final_Code.ipynb`:
- **Model:** `HuggingFaceTB/SmolLM2-135M-Instruct`.
- **Reward Model Training:** Trained using TRL `RewardTrainer` with `RewardConfig` and saved to `./rm_out`.
- **4-Model PPO Setup:**
  ```python
  ppo_trainer = PPOTrainer(
      args=ppo_args,
      processing_class=tok,
      model=policy,
      ref_model=ref_model,
      reward_model=reward_model,
      value_model=value_model,
      train_dataset=ppo_train_dataset,
  )
  ppo_trainer.train()
  ```

---

# 11. Why PPO Is Difficult for LLMs

1. **Massive Memory Footprint:** 4 copies of the model (Actor, Critic, Reference, Reward) must reside in GPU memory.
2. **Dynamic Generation Overhead:** Rollouts require slow autoregressive decoding during training.
3. **Training Instability & Value Function Errors:** Noisy critic value baselines destabilize advantage estimates.
4. **Reward Hacking:** The policy exploits blind spots in neural reward models to score high rewards on adversarial text.

---

# 12. DPO Theory

Under KL-constrained reward maximization:
$$\max_{\pi} \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi(y|x)} \left[ r(x, y) \right] - \beta D_{\text{KL}}\left(\pi(y \mid x) \parallel \pi_{\text{ref}}(y \mid x)\right)$$

The optimal policy $\pi^*$ has the closed-form analytical solution:
$$\pi^*(y \mid x) = \frac{1}{Z(x)} \pi_{\text{ref}}(y \mid x) \exp\left(\frac{1}{\beta} r(x, y)\right)$$
Where $Z(x) = \sum_y \pi_{\text{ref}}(y \mid x) \exp\left(\frac{1}{\beta} r(x, y)\right)$ is the partition function.

---

# 13. DPO Mathematical Derivation

### Step 1: Invert Optimal Policy to Express Implicit Reward
Taking logs:
$$\log \pi^*(y \mid x) = \log \pi_{\text{ref}}(y \mid x) + \frac{1}{\beta} r(x, y) - \log Z(x)$$
$$r(x, y) = \beta \log \frac{\pi^*(y \mid x)}{\pi_{\text{ref}}(y \mid x)} + \beta \log Z(x)$$

### Step 2: Substitute into Bradley-Terry Preference Model
$$r(x, y_w) - r(x, y_l) = \left[ \beta \log \frac{\pi^*(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} + \beta \log Z(x) \right] - \left[ \beta \log \frac{\pi^*(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} + \beta \log Z(x) \right]$$

The partition function terms $\beta \log Z(x)$ **cancel out identically**:
$$r(x, y_w) - r(x, y_l) = \beta \log \frac{\pi^*(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi^*(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)}$$

### Step 3: Formulate the DPO Loss Objective
$$\mathcal{L}_{\text{DPO}}(\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$

---

# 14. DPO Implementation

From `DPO_Training.ipynb`:
- Model: `Qwen/Qwen2.5-0.5B-Instruct` with LoRA ($r=8, \alpha=16$).
- TRL `DPOTrainer` computes reference probabilities under LoRA with zero memory duplication by calling `with model.disable_adapter():`.
- Initial loss starts at $-\log(0.5) \approx 0.6931$ and converges smoothly down to $\approx 0.04$.

---

# 15. Comparison of DPO Notebooks

| Dimension | `Final_DPO.ipynb` | `DPO_Training.ipynb` | `DPO_Training_Final.ipynb` |
|---|---|---|---|
| **Role** | Initial / Buggy baseline | Clean production refactor | Executed clone with run logs |
| **Cell Count** | 15 code, 0 md | 21 code, 26 md | 21 code, 26 md |
| **Dataset** | Shows 4 samples but never uses them; loads all 63K UltraFeedback rows | Configurable (`inline`, `json`, `ultrafeedback`), schema validation, 80/20 train/test split | Identical to `DPO_Training.ipynb` |
| **Precision** | Erroneously enables BF16 on CPU | Robust GPU BF16 detection | Identical to `DPO_Training.ipynb` |
| **Evaluation** | None | Pre- and post-training evaluation | Contains run outputs |

---

# 16. ORPO Theory

```
                                  ORPO ARCHITECTURE
                                  
         Input Pair: (Prompt x, Chosen Response y_w, Rejected Response y_l)
                                          │
                                          ▼
                               ┌──────────────────────┐
                               │ Single Policy Model  │  (No Reference Model!)
                               │       π_θ            │
                               └──────────┬───────────┘
                                          │
                   ┌──────────────────────┴──────────────────────┐
                   ▼                                             ▼
       [SFT Cross-Entropy Loss]                      [Odds Ratio Penalty]
     Maximizes likelihood of y_w                  Penalizes high odds of y_l
          L_SFT(π_θ; y_w)                         L_OR = -log σ(log(Odds_w / Odds_l))
                   │                                             │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
                         Total Loss: L_ORPO = L_SFT + λ * L_OR
```

1. **Odds Formulation:**
   $$\text{odds}_\theta(y \mid x) = \frac{P_\theta(y \mid x)}{1 - P_\theta(y \mid x)}$$
2. **ORPO Combined Objective:**
   $$\mathcal{L}_{\text{ORPO}}(\theta) = \mathbb{E}_{(x, y_w, y_l)} \left[ \mathcal{L}_{\text{SFT}}(\theta) + \lambda \mathcal{L}_{\text{OR}}(\theta) \right]$$
   Where:
   $$\mathcal{L}_{\text{OR}}(\theta) = -\log \sigma\left( \log \frac{\text{odds}_\theta(y_w \mid x)}{\text{odds}_\theta(y_l \mid x)} \right)$$

---

# 17. ORPO Implementation

From `Final_ORPO_Practical.ipynb`:
- Model: `Qwen/Qwen2-0.5B-Instruct` on UltraFeedback.
- Part 1: Standard Hugging Face TRL `ORPOTrainer`.
- Part 2: Unsloth `FastLanguageModel` with `PatchDPOTrainer()` and `adamw_8bit` optimizer.

---

# 18. GRPO Theory

```
                                  GRPO ARCHITECTURE
                                  
                          Prompt x ~ P(X)  (e.g., Math Problem)
                                     │
                                     ▼
                ┌─────────────────────────────────────────┐
                │        Sample a Group of G Outputs      │
                │        {y_1, y_2, y_3, ..., y_G}        │
                └────────────────────┬────────────────────┘
                                     │
                                     ▼
                ┌─────────────────────────────────────────┐
                │    Deterministic Reward Scoring         │
                │    {r_1, r_2, r_3, ..., r_G}            │
                │    (Unit Tests, XML Format, Math Sol)   │
                └────────────────────┬────────────────────┘
                                     │
                                     ▼
                ┌─────────────────────────────────────────┐
                │   Group Normalization (No Critic Model!)│
                │   Mean: μ = (1/G) Σ r_i                 │
                │   Std:  σ = sqrt((1/G) Σ (r_i - μ)^2)   │
                │   Advantage: A_i = (r_i - μ) / (σ + ε)  │
                └────────────────────┬────────────────────┘
                                     │
                                     ▼
                ┌─────────────────────────────────────────┐
                │       Clipped Policy Gradient Update    │
                │     + Token-level KL Penalty vs π_ref   │
                └─────────────────────────────────────────┘
```

1. **Group Statistics:**
   $$\mu = \frac{1}{G} \sum_{i=1}^G r_i, \qquad \sigma = \sqrt{\frac{1}{G} \sum_{i=1}^G (r_i - \mu)^2}$$
2. **Normalized Relative Advantage:**
   $$A_i = \frac{r_i - \mu}{\sigma + \epsilon}$$
3. **GRPO Objective:** Uses clipped policy gradients with group advantages $A_i$, completely eliminating the Critic model $V_\phi$.

---

# 19. GRPO Implementation

From `Final_GRPO_Practical.ipynb`:
- Part 1: TRL `GRPOTrainer` on `SmolLM-135M-Instruct` with custom heuristic rewards (`correctness`, `helpfulness`, `clarity`).
- Part 2: Unsloth + vLLM DeepSeek-R1 style reasoning on `Qwen2.5-0.5B-Instruct` with GSM8K math:
  - System Prompt enforces `<reasoning> ... </reasoning> <answer> ... </answer>`.
  - 5 rule rewards: XML tag counting, regex formatting, integer check, and exact answer match ($+2.0$).

---

# 20. PPO vs DPO vs ORPO vs GRPO Comparison

| Property | PPO / RLHF | DPO | ORPO | GRPO |
|---|---|---|---|---|
| **RL-Based?** | Yes (Actor-Critic) | No (Offline Classification) | No (Offline SFT + OR) | Yes (Policy Gradient without Critic) |
| **Explicit Reward Model?** | Yes ($r_\psi$ Classifier) | No | No | No (Deterministic Rule Verifiers) |
| **Reference Model?** | Yes (KL penalty) | Yes (In denominator) | **No** (Reference-free) | Optional/Yes (KL drift control) |
| **Critic / Value Model?** | Yes ($V_\phi$) | **No** | **No** | **No** (Group Mean $\mu$) |
| **Data Requirement** | Prompts ($x$) | Pairs ($x, y_w, y_l$) | Pairs ($x, y_w, y_l$) | Prompts + Verifiable Solutions |
| **On-Policy vs Offline** | Strictly On-Policy | Completely Offline | Completely Offline | Strictly On-Policy |
| **Rollouts in Training?** | Yes | No | No | Yes (Group of $G$ outputs) |
| **GPU Memory Overhead** | **Extreme** (4 models) | Moderate (Policy + Ref) | **Minimal** (Single model) | Moderate (Policy + Rollout Buffer) |
| **Typical Use** | Frontier chat models | Standard post-training | Fast SLM preference tuning | Reasoning & Math (DeepSeek-R1) |

---

# 21. Conceptual Evolution

```
Pretrained Base LLM
        │  Problem: Knows facts, but can't follow instructions
        ▼
Supervised Fine-Tuning (SFT)
        │  Problem: Hallucinates, cannot distinguish better vs worse
        ▼
Classical RLHF (PPO + Reward Model)
        │  Adds: Preference ranking + exploration; Removes: Blind imitation
        │  Problem: 4 models, extreme GPU memory, training instability
        ▼
Direct Preference Optimization (DPO)
        │  Adds: Closed-form implicit reward, stable offline optimization
        │  Removes: Explicit reward model, critic model, rollout generation
        │  Problem: Requires prior SFT phase and frozen reference model in VRAM
        ▼
Odds Ratio Preference Optimization (ORPO)
        │  Adds: Monolithic 1-stage training (SFT + preference simultaneously)
        │  Removes: Frozen reference model, separate SFT phase
        │  Problem: Weak on open-ended complex multi-step reasoning
        ▼
Group Relative Policy Optimization (GRPO)
        │  Adds: Group-based comparative advantage, rule-based verification
        │  Removes: Critic/value model, dependency on subjective human preference labels
        ▼
Reasoning-Oriented RL (DeepSeek-R1 / RLVR)
```

---

# 22. Mathematical Cheat Sheet

- **Discounted Return:** $G_t = \sum_{k=0}^\infty \gamma^k r_{t+k}$
- **Advantage:** $A(s, a) = Q(s, a) - V(s)$
- **Bradley-Terry:** $P(y_w \succ y_l \mid x) = \sigma(r(x, y_w) - r(x, y_l))$
- **Reward Model Loss:** $\mathcal{L}_{\text{RM}} = -\mathbb{E}[\log \sigma(r_\psi(x, y_w) - r_\psi(x, y_l))]$
- **PPO Ratio:** $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$
- **PPO Clipped Loss:** $\mathcal{L}^{\text{CLIP}} = -\hat{\mathbb{E}}_t [\min(r_t \hat{A}_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon)\hat{A}_t)]$
- **DPO Implicit Reward:** $r(x, y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$
- **DPO Loss:** $\mathcal{L}_{\text{DPO}} = -\mathbb{E}[\log \sigma(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)})]$
- **ORPO Odds:** $\text{odds}_\theta(y|x) = \frac{P_\theta(y|x)}{1 - P_\theta(y|x)}$
- **ORPO Loss:** $\mathcal{L}_{\text{ORPO}} = \mathcal{L}_{\text{SFT}} - \lambda \log \sigma(\log \frac{\text{odds}(y_w)}{\text{odds}(y_l)})$
- **GRPO Advantage:** $A_i = \frac{r_i - \mu}{\sigma + \epsilon}, \quad \mu = \frac{1}{G}\sum r_i, \quad \sigma = \sqrt{\frac{1}{G}\sum (r_i - \mu)^2}$

---

# 23. Code-to-Concept Mapping

| Concept | Target File | Section / Cell Index | Concrete Function / Class | Practical Explanation |
|---|---|---|---|---|
| **Bandit Update** | `RL_Fundamental.ipynb` | Cell 4 | `Q[action] += alpha * (reward - Q[action])` | Tabular memory update of scalar expected reward |
| **Target Q Value** | `RL_Fundamental.ipynb` | Cell 14 | `target_model(next_state).max(1)[0]` | Bellman target estimation with frozen target network |
| **Reward Tokenizer** | `RLHF_with_PPO_Final_Code.ipynb` | Cell 4 | `AutoTokenizer.from_pretrained` | Sets `padding_side="right"`, configures pad token |
| **Reward Training** | `RLHF_with_PPO_Final_Code.ipynb` | Cells 9–10 | `trl.RewardTrainer`, `RewardConfig` | Fits Bradley-Terry classification head on preference pairs |
| **4-Model PPO Init** | `RLHF_with_PPO_Final_Code.ipynb` | Cells 13–15 | `AutoModelForCausalLM`, `...Classification` | Instantiates policy, ref_model, reward_model, value_model |
| **PPO Training** | `RLHF_with_PPO_Final_Code.ipynb` | Cells 18–19 | `trl.PPOTrainer.train()` | Runs on-policy rollouts, advantage estimation, policy updates |
| **DPO Dataset Split** | `DPO_Training.ipynb` | Cell 14 | `dataset.train_test_split(test_size=0.2)` | Prevents data leakage, creates validation split |
| **DPO Execution** | `DPO_Training.ipynb` | Cell 24 | `trl.DPOTrainer`, `DPOConfig` | Calculates implicit reward log-ratios without explicit RM |
| **ORPO Unsloth Patch**| `Final_ORPO_Practical.ipynb` | Cell 25 | `unsloth.PatchDPOTrainer()` | Overrides preference trainer kernels for memory savings |
| **ORPO Loss Run** | `Final_ORPO_Practical.ipynb` | Cell 27 | `trl.ORPOTrainer`, `ORPOConfig` | Single-stage SFT + Odds-Ratio penalty execution |
| **Heuristic Rewards** | `Final_GRPO_Practical.ipynb` | Cells 23–25 | `correctness_reward`, `clarity_reward` | Non-neural rule scoring using word overlap and regex |
| **GRPO Group Train** | `Final_GRPO_Practical.ipynb` | Cells 28–29 | `trl.GRPOTrainer`, `GRPOConfig` | Group sampling ($G=4$) and group relative advantage updates |
| **XML Regex Verifier**| `Final_GRPO_Practical.ipynb` | Cells 43–47 | `xmlcount_reward_func`, `correctness...` | DeepSeek-R1 style rule verifiers for math answers and XML tags |

---

# 24. Dataset Analysis

1. `reward_preferences_dataset.jsonl`: 20 pairs with schema `{"prompt", "chosen", "rejected"}`.
2. `trl-lib/ultrafeedback_binarized`: Conversational preference pairs used in DPO and ORPO practicals.
3. `openai/gsm8k`: Grade school math problems with solutions ending in `#### <integer>`, used in GRPO reasoning practical.

---

# 25. Models

- `HuggingFaceTB/SmolLM2-135M-Instruct`: Policy & Reference in PPO practical.
- `./rm_out`: Trained Reward Model & Critic/Value model checkpoint in PPO practical.
- `Qwen/Qwen2.5-0.5B-Instruct`: Policy model in DPO and GRPO (reasoning) practicals.
- `Qwen/Qwen2-0.5B-Instruct`: Policy model in ORPO practical.
- `HuggingFaceTB/SmolLM-135M-Instruct`: Policy model in GRPO (heuristic) practical.

---

# 26. Hyperparameters Reference

- **PPO:** Learning rate = `1e-6`, episodes = `6`, response length = `16`, batch size = `1`.
- **DPO:** Learning rate = `5e-5`, $\beta = 0.1$, batch size = `1`, gradient accumulation = `8`.
- **ORPO:** Learning rate = `8e-6`, $\beta = 0.1$, batch size = `1`, gradient accumulation = `4`.
- **GRPO:** Learning rate = `5e-6` to `1e-5`, group size $G = 4$, temperature = `0.7` to `0.9`.

---

# 27. Dependencies & Environment

- `torch`: Tensor operations and autograd.
- `transformers`: Model architectures and decoding.
- `trl`: `PPOTrainer`, `RewardTrainer`, `DPOTrainer`, `ORPOTrainer`, `GRPOTrainer`.
- `peft`: LoRA / QLoRA parameter-efficient training.
- `accelerate`: Device placement and multi-GPU dispatch.
- `bitsandbytes`: 4-bit NormalFloat quantization and 8-bit optimizers.
- `unsloth` & `vllm`: Fast kernels and paged attention decoding.

---

# 28. Reproduction & Execution Guide

1. **Environment:** Run `pip install torch transformers datasets trl peft accelerate bitsandbytes sentencepiece`.
2. **PPO Run:** Open `RLHF_with_PPO_Final_Code.ipynb`. Run cells 0–10 to train the Reward Model, then cells 11–21 to train and test PPO.
3. **DPO Run:** Open `DPO_Training.ipynb`. Run cells 0–30. Observe loss drop from $0.6931$ to $\approx 0.04$.
4. **ORPO Run:** Open `Final_ORPO_Practical.ipynb`. Run cells 17–32 with Unsloth.
5. **GRPO Run:** Open `Final_GRPO_Practical.ipynb`. Run cells 36–53 with Unsloth on GSM8K.

---

# 29. Code Review & Potential Issues

1. **CUDA Device-Side Assert (`Final_ORPO_Practical.ipynb` Cell 16):** `torch.multinomial` crashed due to un-normalized logits containing NaN/inf. *Fix:* Add `repetition_penalty=1.1`, set `max_grad_norm=1.0`, verify valid float values.
2. **Precision CPU Crash (`Final_DPO.ipynb` Cell 9):** `bf16=not torch.cuda.is_available()` forces BF16 on CPUs lacking hardware support. *Fix:* Use `torch.cuda.is_bf16_supported()`.
3. **Variable Abandonment (`Final_DPO.ipynb` Cell 0):** Inline data was created but never assigned to a dataset variable.
4. **Prompt Decoding Leak (`Final_DPO.ipynb` Cell 13):** Decoded entire output rather than slicing new tokens (`outputs[0][input_length:]`).

---

# 30. Research Methodology

- **Goal:** Demonstrate that small language models ($\le 0.5\text{B}$) can be effectively aligned using parameter-efficient fine-tuning (LoRA/QLoRA) across PPO, DPO, ORPO, and GRPO within modest compute budgets.
- **Empirical Validation:** Demonstrated DPO loss convergence and GRPO XML reasoning tag compliance on consumer hardware.

---

# 31. File-by-File Reference

*See Section 2 table for detailed mapping of all 15 files.*

---

# 32. Recommended Learning Path

```
Step 1: RL Foundations (RL_Fundamental.ipynb)
   ↓
Step 2: Classical RLHF (RLHF-Updated-Recent-Latest.pdf + RLHF_with_PPO_Final_Code.ipynb)
   ↓
Step 3: Direct Preference Optimization (DPO-Handwritten-final-Notes.pdf + DPO_Training.ipynb)
   ↓
Step 4: Monolithic ORPO (LLM-Finetuning-ORPO.pdf + Final_ORPO_Practical.ipynb)
   ↓
Step 5: Reasoning RL (GRPO-Handwritten-Final-Notes.pdf + Final_GRPO_Practical.ipynb)
```

---

# 33. Interview & Exam Questions

1. **Why is DPO initial loss $\approx 0.6931$?**
   At step 0, $\pi_\theta = \pi_{\text{ref}}$, so log ratios are 0, $\Delta = 0$, $\mathcal{L} = -\log \sigma(0) = -\log(0.5) \approx 0.6931$.
2. **Why does GRPO not need a Critic model?**
   It uses the mean reward of sampled group outputs as the baseline, computing advantage $A_i = \frac{r_i - \mu}{\sigma + \epsilon}$.
3. **How does TRL avoid loading two models during LoRA DPO?**
   It loads one model and toggles adapters off via `with model.disable_adapter():` to evaluate reference log probabilities.

---

# 34. Final Mental Model

- Use **PPO** for large-scale, nuanced conversational alignment when you have ample GPU compute and infrastructure.
- Use **DPO** as the default standard for offline conversational preference tuning.
- Use **ORPO** when GPU memory is constrained and you want a single-stage training pipeline without a reference model.
- Use **GRPO** for reasoning, mathematics, and code generation where ground-truth verification rules exist.

