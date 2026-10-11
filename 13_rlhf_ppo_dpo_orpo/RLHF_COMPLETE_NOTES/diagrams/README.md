# Diagram and plot library

Original educational diagrams. Mermaid sources can be reused in supported Markdown renderers; no external image attribution is needed. Analytical plots show illustrative objective behavior, not measured training results.


## 01 classical rlhf

[Reusable source](01_classical_rlhf.mmd)

```mermaid
flowchart TD
    P["Pretraining: next-token prediction"] --> S["SFT: instruction demonstrations"]
    S --> C["Generate candidates for prompts"]
    C --> H["Annotators compare responses"]
    H --> D["Chosen and rejected pairs"]
    D --> R["Train scalar reward model"]
    S --> A["Initialize policy and frozen reference"]
    R --> PPO["PPO rollouts and actor-critic updates"]
    A --> PPO
    PPO --> E["Held-out evaluation and regression tests"]
    E --> C
```


## 02 model roles

[Reusable source](02_model_roles.mmd)

```mermaid
flowchart LR
    X["Prompt and generated prefix"] --> P["Policy: trainable token distribution"]
    P --> Y["Sampled response"]
    X --> V["Critic: trainable expected return"]
    Y --> R["Frozen reward model: response score"]
    Y --> F["Frozen reference: token log probabilities"]
    P --> L["Policy log probabilities"]
    L --> K["KL shaping relative to reference"]
    F --> K
    K --> A["Returns and advantages"]
    R --> A
    V --> A
    A --> U["Actor and critic losses"]
    U --> P
    U --> V
```


## 03 ppo loop

[Reusable source](03_ppo_loop.mmd)

```mermaid
flowchart TD
    X["Sample prompts"] --> G["Old policy generates responses"]
    G --> B["Store tokens, masks, old logps and values"]
    B --> R["Score response and compute reference logps"]
    R --> K["Token KL shaping plus terminal reward"]
    K --> A["GAE and value targets; detach rollout targets"]
    A --> M["Shuffle rollout minibatches"]
    M --> N["Current policy logps and current values"]
    N --> L["Clipped actor loss plus critic loss"]
    L --> U["Backward, clip gradients, optimizer step"]
    U --> T{"More optimization epochs?"}
    T -->|Yes| M
    T -->|No| X
```


## 04 ppo clipping

[Reusable source](04_ppo_clipping.mmd)

```mermaid
flowchart TD
    R["Ratio rho = exp(current logp - old logp)"] --> A{"Advantage sign"}
    A -->|Positive| P["min(rho, 1 + epsilon) times A"]
    A -->|Negative| N["max(rho, 1 - epsilon) times A"]
    P --> O["Cap incentive for beneficial ratio changes"]
    N --> O
    O --> U["Optimize surrogate; no hard probability bound"]
```


## 05 dpo pipeline

[Reusable source](05_dpo_pipeline.mmd)

```mermaid
flowchart LR
    D["Offline prompt, chosen, rejected"] --> T["Shared template and completion masks"]
    T --> P["Policy forward passes with gradients"]
    T --> R["Frozen reference scoring or cached logps"]
    P --> M["Beta times chosen-minus-rejected log-ratio margin"]
    R --> M
    M --> L["Negative log sigmoid of margin"]
    L --> U["Update policy or LoRA adapter"]
```


## 06 dpo logps

[Reusable source](06_dpo_logps.mmd)

```mermaid
flowchart TD
    W["Chosen completion"] --> PW["Policy sum of completion logps"]
    W --> RW["Reference sum of completion logps"]
    L["Rejected completion"] --> PL["Policy sum of completion logps"]
    L --> RL["Reference sum of completion logps"]
    PW --> SW["Chosen relative score"]
    RW --> SW
    PL --> SL["Rejected relative score"]
    RL --> SL
    SW --> M["Margin = beta times score difference"]
    SL --> M
    M --> LOSS["softplus of negative margin"]
```


## 07 grpo groups

[Reusable source](07_grpo_groups.mmd)

```mermaid
flowchart TD
    X["One prompt"] --> G["Sample G completions from old policy"]
    G --> R["Reward function or reward model scores each"]
    R --> N["Group mean and standard deviation"]
    N --> A["Normalized relative advantages"]
    A --> P["Token ratios and clipped policy surrogate"]
    F["Reference token probabilities"] --> K["Optional explicit KL loss in library variants"]
    P --> U["Policy update; no learned critic in original GRPO"]
    K --> U
    U --> X
```


## 08 orpo objective

[Reusable source](08_orpo_objective.mmd)

```mermaid
flowchart LR
    D["Offline preference pair"] --> P["One trainable language model"]
    P --> W["Chosen masked token logps"]
    P --> L["Rejected masked token logps"]
    W --> S["Chosen supervised NLL"]
    W --> O["Length-normalized log odds difference"]
    L --> O
    O --> R["Negative log sigmoid preference loss"]
    S --> T["NLL plus lambda times preference loss"]
    R --> T
    T --> U["Update same model; no frozen reference"]
```


## 09 all data flows

[Reusable source](09_all_data_flows.mmd)

```mermaid
flowchart TD
    D["Verified local prompt, chosen, rejected strings"] --> PA["DPO or ORPO preference formatting"]
    PA --> OFF["Offline teacher-forced optimization"]
    D --> RM["Full prompt plus response pairs for reward model"]
    RM --> PPO["PPO: prompt rollouts scored by reward model"]
    D --> X["Prompt-only rollout dataset"]
    X --> PPO
    X --> GR["GRPO: groups of generated responses"]
    GOLD["Gold answer metadata or external reward oracle"] --> GR
    GR --> ONLINE["Online policy updates"]
    PPO --> ONLINE
```


## 10 selection tree

[Reusable source](10_selection_tree.mmd)

```mermaid
flowchart TD
    X{"Can you score fresh generated answers reliably?"} -->|Yes| V{"Verifiable task and group generation affordable?"}
    V -->|Yes| G["Consider GRPO; inspect variance and grouping"]
    V -->|No| P["Consider PPO; budget for critic and rollouts"]
    X -->|No| D{"High-quality offline preference pairs available?"}
    D -->|No| C["Collect data or improve SFT before preference training"]
    D -->|Yes| S{"Want integrated chosen SFT and reference-free objective?"}
    S -->|Yes| O["Consider ORPO; tune supervised/preference balance"]
    S -->|No| DP["Consider DPO with stable reference scoring"]
    G --> E["Pilot and compare on held-out task and regression evaluation"]
    P --> E
    O --> E
    DP --> E
```


## 11 end to end

[Reusable source](11_end_to_end.mmd)

```mermaid
flowchart TD
    D["Audit data and deduplicate prompts"] --> S["Split by prompt or topic"]
    S --> M["Choose base model, tokenizer and dependency versions"]
    M --> T["Apply template once; inspect lengths and masks"]
    T --> A["Select algorithm and explicit configuration"]
    A --> B["One-batch forward/backward sanity check"]
    B --> R["Baseline evaluation"]
    R --> F["Training with finite-loss checks and checkpoints"]
    F --> E["Held-out preference and generation evaluation"]
    E --> C["Save configuration, adapter, tokenizer and full resume state"]
    C --> L["Fresh-process reload and compare with baseline"]
```


## 12 rl to llm

[Reusable source](12_rl_to_llm.mmd)

```mermaid
flowchart LR
    S["State: prompt plus generated prefix"] --> P["Agent policy: LLM next-token distribution"]
    P --> A["Action: sampled next token"]
    A --> E["Transition: append token to prefix"]
    E --> S
    E --> T{"EOS or stopping condition?"}
    T -->|Yes| R["Sequence reward plus possible token shaping"]
    R --> U["Estimate advantages and update policy"]
    U --> P
```


## 13 reward pair

[Reusable source](13_reward_pair.mmd)

```mermaid
sequenceDiagram
    participant D as Preference dataset
    participant RM as Scalar reward model
    participant O as Optimizer
    D->>RM: Same prompt plus chosen full response
    RM-->>O: Chosen score
    D->>RM: Same prompt plus rejected full response
    RM-->>O: Rejected score
    O->>O: Negative log sigmoid of reward difference
    O->>RM: Gradient update to reward parameters
```


## Reproducible analytical plots

![PPO clipping](../assets/plots/ppo_clipping.svg)

For fixed advantages +1 and −1, clipping width0.2; current/old ratios vary independently. These curves are surrogate incentives, not hard constraints.

![Logistic preference loss](../assets/plots/preference_loss.svg)

−logσ(βm) against illustrative reference-adjusted log-probability margin m, for β0.1/0.5/1. No training data used. [Generator](../assets/plot_objectives.py).
