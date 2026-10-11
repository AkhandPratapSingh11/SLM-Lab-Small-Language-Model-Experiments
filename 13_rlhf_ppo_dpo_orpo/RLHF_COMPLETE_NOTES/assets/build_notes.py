from pathlib import Path
import json
import re
OUT = Path(__file__).resolve().parents[1]
def write(name, text):
    path=OUT/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text.strip()+'\n',encoding='utf-8')
chapters = [
('00_LEARNING_ROADMAP.md','Learning roadmap'),
('01_REINFORCEMENT_LEARNING_FUNDAMENTALS.md','Reinforcement learning fundamentals'),
('02_LLM_ALIGNMENT_AND_RLHF.md','LLM alignment and RLHF'),
('03_PREFERENCE_DATA_AND_REWARD_MODELS.md','Preference data and reward models'),
('04_PPO_IN_DEPTH.md','PPO in depth'),
('05_DPO_IN_DEPTH.md','DPO in depth'),
('06_GRPO_IN_DEPTH.md','GRPO in depth'),
('07_ORPO_IN_DEPTH.md','ORPO in depth'),
('08_ALGORITHM_COMPARISON.md','Algorithm comparison and selection'),
('09_PRACTICAL_IMPLEMENTATION_GUIDE.md','Practical implementation guide'),
('10_EVALUATION_DEBUGGING_AND_BEST_PRACTICES.md','Evaluation, debugging, and best practices'),
('11_INTERVIEW_PREPARATION.md','Interview preparation'),
('12_GLOSSARY_AND_FORMULA_CHEATSHEET.md','Glossary and formula cheat sheet')]
def chapter(index,text):
    # GitHub/remark-math display syntax; leave code and literal examples unchanged.
    text = re.sub(r"(?m)^\\\[$", "$$", text)
    text = re.sub(r"(?m)^\\\]$", "$$", text)
    text = re.sub(r"(?m)^\$\$(\n)(?=\$\$)", "$$\n\n", text)
    prev=chapters[index-1] if index else ('README.md','Home')
    nex=chapters[index+1] if index+1<len(chapters) else ('README.md','Home')
    write(chapters[index][0],f'# {index:02d} — {chapters[index][1]}\n\n[Home](README.md) · [Previous: {prev[1]}]({prev[0]}) · [Next: {nex[1]}]({nex[0]})\n\n'+text)

diagrams={
'01_classical_rlhf':'''flowchart TD
    P["Pretraining: next-token prediction"] --> S["SFT: instruction demonstrations"]
    S --> C["Generate candidates for prompts"]
    C --> H["Annotators compare responses"]
    H --> D["Chosen and rejected pairs"]
    D --> R["Train scalar reward model"]
    S --> A["Initialize policy and frozen reference"]
    R --> PPO["PPO rollouts and actor-critic updates"]
    A --> PPO
    PPO --> E["Held-out evaluation and regression tests"]
    E --> C''',
'02_model_roles':'''flowchart LR
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
    U --> V''',
'03_ppo_loop':'''flowchart TD
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
    T -->|No| X''',
'04_ppo_clipping':'''flowchart TD
    R["Ratio rho = exp(current logp - old logp)"] --> A{"Advantage sign"}
    A -->|Positive| P["min(rho, 1 + epsilon) times A"]
    A -->|Negative| N["max(rho, 1 - epsilon) times A"]
    P --> O["Cap incentive for beneficial ratio changes"]
    N --> O
    O --> U["Optimize surrogate; no hard probability bound"]''',
'05_dpo_pipeline':'''flowchart LR
    D["Offline prompt, chosen, rejected"] --> T["Shared template and completion masks"]
    T --> P["Policy forward passes with gradients"]
    T --> R["Frozen reference scoring or cached logps"]
    P --> M["Beta times chosen-minus-rejected log-ratio margin"]
    R --> M
    M --> L["Negative log sigmoid of margin"]
    L --> U["Update policy or LoRA adapter"]''',
'06_dpo_logps':'''flowchart TD
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
    M --> LOSS["softplus of negative margin"]''',
'07_grpo_groups':'''flowchart TD
    X["One prompt"] --> G["Sample G completions from old policy"]
    G --> R["Reward function or reward model scores each"]
    R --> N["Group mean and standard deviation"]
    N --> A["Normalized relative advantages"]
    A --> P["Token ratios and clipped policy surrogate"]
    F["Reference token probabilities"] --> K["Optional explicit KL loss in library variants"]
    P --> U["Policy update; no learned critic in original GRPO"]
    K --> U
    U --> X''',
'08_orpo_objective':'''flowchart LR
    D["Offline preference pair"] --> P["One trainable language model"]
    P --> W["Chosen masked token logps"]
    P --> L["Rejected masked token logps"]
    W --> S["Chosen supervised NLL"]
    W --> O["Length-normalized log odds difference"]
    L --> O
    O --> R["Negative log sigmoid preference loss"]
    S --> T["NLL plus lambda times preference loss"]
    R --> T
    T --> U["Update same model; no frozen reference"]''',
'09_all_data_flows':'''flowchart TD
    D["Verified local prompt, chosen, rejected strings"] --> PA["DPO or ORPO preference formatting"]
    PA --> OFF["Offline teacher-forced optimization"]
    D --> RM["Full prompt plus response pairs for reward model"]
    RM --> PPO["PPO: prompt rollouts scored by reward model"]
    D --> X["Prompt-only rollout dataset"]
    X --> PPO
    X --> GR["GRPO: groups of generated responses"]
    GOLD["Gold answer metadata or external reward oracle"] --> GR
    GR --> ONLINE["Online policy updates"]
    PPO --> ONLINE''',
'10_selection_tree':'''flowchart TD
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
    DP --> E''',
'11_end_to_end':'''flowchart TD
    D["Audit data and deduplicate prompts"] --> S["Split by prompt or topic"]
    S --> M["Choose base model, tokenizer and dependency versions"]
    M --> T["Apply template once; inspect lengths and masks"]
    T --> A["Select algorithm and explicit configuration"]
    A --> B["One-batch forward/backward sanity check"]
    B --> R["Baseline evaluation"]
    R --> F["Training with finite-loss checks and checkpoints"]
    F --> E["Held-out preference and generation evaluation"]
    E --> C["Save configuration, adapter, tokenizer and full resume state"]
    C --> L["Fresh-process reload and compare with baseline"]''',
'12_rl_to_llm':'''flowchart LR
    S["State: prompt plus generated prefix"] --> P["Agent policy: LLM next-token distribution"]
    P --> A["Action: sampled next token"]
    A --> E["Transition: append token to prefix"]
    E --> S
    E --> T{"EOS or stopping condition?"}
    T -->|Yes| R["Sequence reward plus possible token shaping"]
    R --> U["Estimate advantages and update policy"]
    U --> P''',
'13_reward_pair':'''sequenceDiagram
    participant D as Preference dataset
    participant RM as Scalar reward model
    participant O as Optimizer
    D->>RM: Same prompt plus chosen full response
    RM-->>O: Chosen score
    D->>RM: Same prompt plus rejected full response
    RM-->>O: Rejected score
    O->>O: Negative log sigmoid of reward difference
    O->>RM: Gradient update to reward parameters'''
}
for name,source in diagrams.items():write('diagrams/'+name+'.mmd',source)
def diagram(name):return '\n```mermaid\n'+diagrams[name]+'\n```\n\nReusable source: [diagram](diagrams/'+name+'.mmd).\n'

chapter(0,r'''
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
''')

chapter(1,r'''
## 1. Intuition: learning from consequences

Imagine a robot in a game. It sees a crossroad, chooses left or right, receives feedback, and changes its future decisions. The RLHF PDF uses game playing, a self-driving car and a baby learning to walk as analogies (pages 10 and 15). Their useful shared idea is **interaction → reward → update**. Feedback still comes from a designed environment or a person; “no teacher” does not mean no supervision or no human choices.

The notebook [RL_Fundamental.ipynb](../RL_Fundamental.ipynb) begins with `actions = ["left", "right"]`, a dictionary `Q`, and `get_reward`: right earns +1 and left earns −1. With learning rate `alpha = 0.1`, the update is

\[
Q(a)\leftarrow Q(a)+\alpha[R-Q(a)].
\]

Here Q is an estimate of immediate reward for each action, R is observed feedback, and α determines how much a new observation changes the estimate. Starting from zero, two right observations give 0.1 then 0.19. This is a **stateless bandit-like reward-estimation demo**, not full state-dependent Q-learning: it has no next state, discounted future term, or environment transition. The loop always chooses randomly, so exploration does not become exploitation automatically. The greedy choice in the comments would select `max(Q, key=Q.get)` afterward. Cell 5 repeats one update using the last loop variables, which changes Q again if executed.

## 2. Basic vocabulary

| Term | Game example | LLM example |
|---|---|---|
| Agent | Robot making decisions | Trainable language model |
| Environment | Game rules and transitions | Token-prefix transition plus response scoring system |
| State s | Position and relevant game information | Prompt and all previously generated tokens |
| Action a | Left/right movement | Next generated token |
| Reward R | Points earned by an action or episode | Correctness, preference score, or shaped token reward |
| Reward function | Rule assigning points | Function or model mapping prompt/response to score |
| Policy πθ(a\|s) | Distribution over moves | Softmax next-token distribution; θ are model parameters |
| Episode | One run until game ends | One generation until EOS, length limit, or stopping rule |
| Trajectory τ | States, actions and rewards in order | Generated token sequence and associated prefixes/rewards |
| Terminal state | Goal/death; no further task rewards | End of completed generation |
| Return Gt | Discounted future total points | Discounted shaped rewards remaining in a response |

A **stochastic policy** samples actions with specified probabilities. A **deterministic policy** maps each state to one action. An LLM has a probabilistic policy even when inference chooses a deterministic argmax. Training rollouts generally need sampling diversity.

Use R_t for the reward received after action a_t. For an episode with T actions,

\[
G_t=\sum_{k=0}^{T-1-t}\gamma^kR_{t+k},\quad
J(\theta)=\mathbb E_{\tau\sim\pi_\theta}[G_0].
\]

γ∈[0,1] is the discount factor, t indexes time, and expectation averages over random initial states, transitions and policy actions. With rewards `[0, 0, 10]` and γ=0.9, the initial return is 8.1. γ=1 is common for finite response-level LLM rewards, but it is not universal and does not make infinite-horizon undiscounted sums automatically finite.

## 3. Markov decision processes

An MDP is `(S, A, P, r, d0, γ)`: state space S, action space A, transition probability P(s′|s,a), expected immediate reward r(s,a), initial-state distribution d0(s), and discount γ. Terminal behavior or a finite horizon completes an episodic specification. Reward may more generally depend on `(s,a,s′)`.

The **Markov property** says the current state contains the information needed to predict the next transition and reward; earlier history adds nothing after conditioning on that state. A robot's position alone might fail this if velocity matters. An LLM prefix is a convenient state because autoregressive decisions condition on its whole available context. Tool use and hidden external state can require a richer state or a partially observable formulation.

MDPs separate what the agent controls (policy) from how the world responds (transitions/rewards). This separation lets us derive value recursions and optimize decisions rather than memorize one correct output.

## 4. Value, action value and advantage

\[
V^\pi(s)=\mathbb E_\pi[G_t\mid s_t=s],\quad
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid s_t=s,a_t=a],\quad
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s).
\]

V averages the future return under the policy from a state. Q fixes the first action, then follows that policy. Advantage measures whether that action is better than the policy's average at the same state. A reward model's completed-response score is different from a critic's prefix-conditioned expected return.

**Source crossroad example:** the RLHF PDF pages 19–20 assigns Q(left)=10, Q(right)=50, Q(straight)=20. Under an illustrative policy `(0.2, 0.5, 0.3)`, V=0.2×10+0.5×50+0.3×20=33. Thus advantages are −23, +17, −13, and their policy-weighted average is zero. These are hypothetical expected returns, not measured scores or probabilities.

### Bellman expectation equations: deriving the recursion

Split the first reward from the return: `G_t = R_t + γG_{t+1}`. Apply conditional expectation and average over the action and next state:

\[
Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s'),
\]
\[
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a)
=\sum_a\pi(a\mid s)\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s')\right].
\]

The sums become integrals for continuous spaces. Terminal-state V is zero when no rewards remain. If a move earns 2 and reaches a state valued at 5 with γ=0.9, its Q is 6.5.

### Bellman optimality equations

For the best achievable policy, replace the action average with the best action:

\[
V^*(s)=\max_a\left[r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^*(s')\right],
\]
\[
Q^*(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\max_{a'}Q^*(s',a').
\]

The star denotes an optimal value under the stated reward and dynamics, not moral correctness. Maximizing a flawed reward can produce flawed behavior.

## 5. Ways to learn

| Approach | Update idea | Trade-off and relevance |
|---|---|---|
| Monte Carlo | Wait for episode return; move V toward G | No bootstrap; potentially high variance; useful return intuition |
| TD(0) | V(s)←V(s)+α[R+γV(s′)−V(s)] | Bootstraps from an estimate; lower variance but possible bias; PPO critic prerequisite |
| Q-learning | Q(s,a)←Q(s,a)+α[R+γ max_a′Q(s′,a′)−Q(s,a)] | Off-policy optimal-action target; source DQN demo |
| SARSA | Q(s,a)←Q(s,a)+α[R+γQ(s′,a′)−Q(s,a)] | On-policy next sampled action; accounts for current exploratory behavior |
| Value-based | Learn values and derive action selection | Q-learning/DQN; not the supplied LLM preference trainers |
| Policy-based | Directly optimize πθ | Natural fit to pretrained autoregressive LLMs |
| Actor-critic | Actor learns actions; critic estimates return | PPO's common implementation |

**On-policy** updates primarily use trajectories collected by the policy being optimized. PPO uses a frozen recent behavior policy and reuses a rollout for a few epochs; its ratios handle this local mismatch, but arbitrarily old replay is not canonical PPO. **Off-policy** methods can learn from a different behavior distribution. DPO and ORPO are offline pairwise objectives, not ordinary off-policy TD algorithms; GRPO is rollout-based and close to on-policy in its original formulation.

Exploration tries uncertain actions to discover outcomes. Exploitation favors what currently looks best. Epsilon-greedy Q-learning mixes random choices with greedy action selection. LLM temperature and sampling controls affect exploration, but higher temperature can lower answer quality and change rollout probabilities.

## 6. The actual DQN and racing demonstrations

Cells 9–17 of `RL_Fundamental.ipynb` create a network `4→128→2`, its frozen-for-target-computation copy `target_model`, Adam with 1e−3, and MSE loss. Dummy states have shape `[32,4]`, actions `[32]`, network output `[32,2]`. `gather(1, action.unsqueeze(1)).squeeze(1)` selects one predicted action value per row. Under `no_grad`, `target = reward + 0.99 * next_q * (1-done)` produces `[32]` bootstrap targets. Backpropagation updates only the main network.

The dummy random states and rewards do not come from an environment. There is no replay buffer, epsilon-greedy interaction loop, repeated optimization, or target synchronization after initialization. Cell 28 correctly states these omissions. The PDF's grid-world example (pages 25–28) has current Q=4, reward=5, next max=6, γ=0.9: target=10.4, TD error=6.4, squared error=40.96. Calling 10.4 the “correct value” requires qualification: it is correct **relative to this target estimate**, which can change during learning.

Cells 19–27 switch to Stable-Baselines3 PPO with Gymnasium `CarRacing-v3`, `CnnPolicy`, learning rate 0.0003, `n_steps=2048`, batch size 64. `learn(total_timesteps=100)` is a requested minimum budget; **saved output shows 2048 timesteps**, because a full rollout is collected. The stored mean episode reward −58.6 is one historical tiny-run result, not evidence that driving was learned. `render_mode="human"` requires a display; for headless experiments select an appropriate supported rendering mode. Test resets on either termination or truncation, and should close the environment afterward.

LLM tokens are discrete. The PDF's contrast between DQN and continuous steering (page 29) explains a limitation of standard finite-output DQN, but it does not make LLM actions continuous. PPO is convenient because it directly optimizes an existing token policy; DQN-style methods are not mathematically impossible for a finite vocabulary.

## 7. Why policy gradients use log probabilities

A gradient tells us how a small parameter change affects an objective. Write trajectory probability as initial-state probability times transition probabilities times policy probabilities. If transitions and rewards do not depend directly on θ,

\[
\nabla_\theta J
=\mathbb E_\tau\left[G_0\nabla_\theta\log p_\theta(\tau)\right],\quad
\nabla_\theta\log p_\theta(\tau)=\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t).
\]

This uses the identity `∇p = p∇log p` (the likelihood-ratio trick). Causality allows replacing the full return by future rewards: past rewards cannot be affected by the current sampled action. A policy-gradient theorem form is

\[
\nabla_\theta J\ \propto\
\mathbb E_{s\sim d^\pi,a\sim\pi_\theta}
[Q^\pi(s,a)\nabla_\theta\log\pi_\theta(a\mid s)].
\]

Here dπ is the discounted state occupancy distribution; the proportionality accounts for its normalization. In an episodic estimator for the discounted start-state objective, one can write `E[Σ_t γ^t G_t ∇logπ(a_t|s_t)]`. Practical finite-horizon undiscounted objectives use γ=1. State clearly which objective and occupancy weighting you use.

Subtracting an action-independent baseline b(s) leaves the expected gradient unchanged because `Σ_a π(a|s)∇logπ(a|s)=∇Σ_aπ(a|s)=0`. Setting b≈V reduces variance and gives an advantage estimate. Baselines and rollout targets are detached in the actor loss. With a positive advantage, maximizing `A logπ` encourages that action; an optimizer minimizing a loss uses `−A logπ`. The PDF's “update proportional to reward times log probability” (page 13) is intuition, not a complete parameter-update equation.

## 8. Importance sampling, entropy and KL

For target distribution p and sampling distribution q with sufficient support,

\[
\mathbb E_{a\sim p}[f(a)]
=\mathbb E_{a\sim q}\left[\frac{p(a)}{q(a)}f(a)\right].
\]

PPO uses current-to-old **action** probability ratios at stored states. This does not exactly correct the entire changed state distribution; it motivates a local surrogate. Large ratios have high variance and motivate clipping.

Entropy of a token policy is

\[
H(\pi(\cdot|s))=-\sum_a\pi(a|s)\log\pi(a|s).
\]

An entropy bonus can encourage diversity; excessive pressure can hurt correctness. For two distributions,

\[
D_{KL}(p\|q)=\sum_a p(a)\log\frac{p(a)}{q(a)}\ge0.
\]

KL is asymmetric, zero for equal distributions, and requires reference support where p has mass. For p=(0.8,0.2), q=(0.5,0.5), KL≈0.193 nats. A sampled log ratio can be negative even though its expectation under p is nonnegative. The old rollout policy and the longer-lived reference policy serve different roles.

## 9. GAE: connect rewards to policy updates

A one-step temporal-difference residual is

\[
\delta_t=R_t+\gamma(1-d_t)V_{\mathrm{old}}(s_{t+1})-V_{\mathrm{old}}(s_t).
\]

$d_t$ is a genuine terminal indicator. $V_{\mathrm{old}}=V_{\phi_{\mathrm{old}}}$ denotes the fixed rollout-time critic estimate, with critic parameters $\phi_{\mathrm{old}}$. Use these same detached estimates in the TD residual and return target; $V_\phi$ later denotes the critic being optimized. Generalized Advantage Estimation mixes short and long bootstrap estimates:

\[
\hat A_t^{GAE}=\sum_{l=0}^{T-1-t}(\gamma\lambda_{GAE})^l\delta_{t+l},
\quad \hat G_t=\hat A_t+V_{old}(s_t).
\]

Continuation factors are also needed across terminal boundaries; above the sum is confined to a single episode. Recursive code uses `A_t = δ_t + γλ(1-d_t)A_{t+1}`. λ near 0 favors short estimates; near 1 favors long returns and generally higher variance. Value error and truncation handling influence bias.

Example: rewards `[0,1]`, values `[0.4,0.5]`, terminal value 0, γ=1 and λ=0.95. Residuals are 0.1 and 0.5; advantages are 0.575 and 0.5. Value targets are 0.975 and 1.0. With λ=1, the first target becomes the Monte Carlo return 1.0. Raw advantage-plus-old-value targets are formed before any optional actor-advantage normalization.

At a time-limit truncation, the underlying task may continue, so value bootstrap can be appropriate. At genuine terminal completion, future task value is zero. Prompt and padding tokens must not accidentally become rollout actions in these sums.

## 10. Map the framework to autoregressive language

For prompt x and response y=(y1,…,yT),

\[
\pi_\theta(y|x)=\prod_{t=1}^T\pi_\theta(y_t|x,y_{<t}),\quad
\log\pi_\theta(y|x)=\sum_{t=1}^T\log\pi_\theta(y_t|x,y_{<t}).
\]

State is `(x,y<t)`, action is yt, and the transition appends that token. A terminal response score can be placed on the final active token; KL or other shaping can supply intermediate rewards. Some systems instead optimize whole-response bandit objectives. Never assume all rewards are token-level or all objectives aggregate identically.
''' + diagram('12_rl_to_llm') + r'''
## Revision and interview takeaway

Reward is immediate feedback; return sums future feedback; V predicts expected return; Q conditions on an action; advantage compares Q with V. PPO learns an actor and commonly a critic; GRPO uses group-derived comparisons; DPO and ORPO learn from offline pairs. The three demonstrations in your RL notebook are a bandit-like update, a dummy DQN training step, and a short library PPO run—not one complete algorithm implementation.

Further reading: [Sutton and Barto, Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html); [GAE, Schulman et al., 2015](https://arxiv.org/abs/1506.02438). The GAE paper was retrieved for identity and relevance; the textbook is a supplementary reading link rather than evidence about your notebook.
''')

chapter(2,r'''
## 1. Why alignment follows language modeling

Pretraining teaches a model to predict text from broad corpora. It can learn syntax, facts and reasoning patterns while also learning unreliable or undesirable behavior. SFT teaches it to respond to instructions by imitating demonstrations. Preferences add information about **which of several plausible responses is better under an annotation rubric**.

The RLHF PDF pages 3–8 uses exam preparation, politeness, and the France/Germany capital example. The DPO PDFs use “explain gravity to a 10-year-old”: both a clear explanation and an unnecessarily technical answer may be fluent, but the user prefers the age-appropriate answer. These examples motivate preference learning beyond one target response. SFT can also learn safety and tone from suitable demonstrations; it is inaccurate to claim it cannot teach human values. Its ordinary likelihood objective simply does not contain an explicit chosen-versus-rejected comparison.

Alignment is a goal and ongoing evaluation process. Optimizing a proxy does not guarantee honesty, harmlessness or every user's values. The PDF statements that alignment “ensures” these properties should be read as intended outcomes, not guarantees.

## 2. What each training stage learns

| Stage | Typical data/objective | What changes |
|---|---|---|
| Pretraining | Next-token likelihood on broad text | General language and representations |
| SFT | Prompt plus demonstrated answer; masked response NLL | Instruction-following behavior |
| Preference collection | Same prompt with ranked candidate responses | Dataset, not necessarily model weights |
| Reward-model training | Pairwise scalar-score comparison | Reward model parameters ψ |
| PPO RLHF | Fresh policy responses and proxy rewards | Policy θ and critic φ |
| Evaluation/iteration | Held-out generations and independent judgments | Decisions about data, rewards and checkpoints |

These are common stages, not a mandatory universal pipeline. ORPO integrates chosen imitation and pairwise preference training in one objective. DPO avoids a separately trained reward model and rollout loop. GRPO uses group-scored rollouts. Synthetic annotation is often called reinforcement learning from AI feedback or preference learning from AI feedback depending on the optimizer; the word “human” does not prove the supplied dataset was human annotated.
''' + diagram('01_classical_rlhf') + r'''
## 3. Four model roles, independent of how many copies are loaded

| Role | Input → output | During reward training | During PPO policy optimization | Can share or reuse components? |
|---|---|---|---|---|
| Policy πθ | Prefix → vocabulary logits/probabilities | Usually not the object optimized by RM loss | Trainable actor | Can be LoRA on frozen backbone |
| Reference πref | Same tokens/prefix → reference logps | Often retained from initial SFT model | Frozen for regularization | Can be adapter-disabled backbone or cached scores for offline pairs |
| Reward rψ | Full prompt and completed response → scalar | Trained from pairwise preference labels | Usually frozen scorer | May use same architecture as policy with scalar head; may instead be a rule function |
| Critic Vφ | Prefix/state → expected remaining return | Not trained by the pairwise RM objective as a critic | Trained to rollout return targets | Can share backbone with actor or be separate; may initialize from RM |

“Four roles” does not imply four independent full-size transformers in every system. Sharing saves memory but couples gradients and requires careful freezing. Offline reference caching removes repeated forward passes only for the exact tokenization and fixed pairs cached.

### Reward model versus critic

The reward model learns **which completed answer is preferred**. The critic estimates **how much shaped future reward the current policy expects from a prefix**. Their objectives and conditioning differ. A reward score 8 for a final answer and critic prediction 6 yield a simple terminal advantage estimate +2 only in a one-step illustration. Real token-level PPO often uses GAE and KL-shaped returns.

In your PPO notebook, `reward_model` and `value_model` both load `./rm_out`. The reward copy is frozen; the value copy trains. Initializing from the same weights does not make them the same role or keep their parameters equal.

### If a role is missing or misconfigured

A policy without trainable parameters cannot learn. A reference that updates accidentally moves the regularization target. An RM scored on answer-only text can miss the prompt's intent. A critic trained to raw RM scores while the actor uses a different shaped return is inconsistent. A separate critic is absent by design in original GRPO, DPO and ORPO; that absence is not a bug in those algorithms.
''' + diagram('02_model_roles') + r'''
## 4. Reward regularization and the proxy problem

A common response-level objective is

\[
\max_\theta\ \mathbb E_{x,y\sim\pi_\theta}[r_\psi(x,y)]
-\kappa\mathbb E_x D_{KL}(\pi_\theta(\cdot|x)\|\pi_{ref}(\cdot|x)).
\]

x is a prompt, y a response, κ≥0 sets the relative penalty, and response KL refers to complete-response distributions. Autoregressive sampled log ratios estimate its decomposition along generated prefixes. The PPO clip ratio instead compares current and **old rollout** policies; those two comparisons must not be confused.

## 5. Challenges and practical mitigations

| Challenge | Mechanism | Useful mitigations and remaining limit |
|---|---|---|
| Reward hacking | Policy finds high-scoring text that is not useful | Adversarial scorer checks, task tests, independent human review; proxies remain imperfect |
| RM overoptimization | Strong optimization exploits scorer blind spots | KL monitoring, early stopping, multiple independent evaluations; KL cannot certify correctness |
| Distribution shift | Generated text differs from RM training comparisons | Add policy-generated hard examples; evaluate by prompt category |
| Inconsistent preferences | Annotators disagree or criteria conflict | Explicit rubric, repeat labels, uncertainty/tie handling; no unique universal preference |
| Instability | Bad scaling, noisy advantage, large update | Conservative learning rate, finite checks, gradient clipping, rollout diagnostics |
| Mode collapse | Many prompts receive repetitive responses | Diversity/entropy/length monitoring and broad evaluations; entropy alone is insufficient |
| Catastrophic forgetting | Specialized optimization harms prior abilities | Regression suite, chosen SFT mixing when appropriate, conservative stopping |
| Length bias | Score rewards verbosity instead of substance | Length-matched annotation, length stratification, reward component audit |
| Reward calibration | Reward scale shifts without stable meaning | Held-out ranking calibration, documented normalization; pairwise scores have additive ambiguity |

A high reward and a good generation are separate observations. Optimizing a reward can help the intended task when the proxy generalizes, but the intended task must be evaluated independently.

## 6. Alternative paths in this repository

**PPO-based RLHF** trains a reward model from pairs and optimizes fresh responses with an actor-critic loop. PPO itself is a general RL optimizer and does not inherently require a learned preference scorer or an SFT reference.

**DPO** trains directly on offline pairs using policy-versus-reference likelihood differences. It has an implicit reward interpretation, not a separately fitted scalar reward network.

**GRPO** samples multiple answers for each prompt and uses relative rewards as advantages. A rule-based reward is a legitimate scorer; a learned RM is also legitimate. The original DeepSeekMath paper includes learned reward models and process supervision, so the later reasoning-notebook rule demo should not be treated as the entire original method.

**ORPO** jointly imitates chosen answers and optimizes chosen/rejected odds without a separate reference. Both ORPO notebook paths begin from an instruction-tuned model; the ability to integrate SFT does not require beginning from raw pretrained weights.

The root README mentions **KTO**, which uses desirable/undesirable judgments rather than necessarily paired comparisons, and the ORPO PDF mentions **SimPO**, a reference-free preference method with its own score/margin objective. Neither has an implemented trainer in these seven notebooks. See [external references](EXTERNAL_REFERENCES.md) for scope and supporting papers.

## Revision

Distinguish training stages, model roles and physical model copies. RM scores responses; critic predicts returns. The classical pipeline is one alignment workflow. Reference regularization, offline pairwise objectives and group-relative rollouts solve different engineering problems and retain different failure modes.
''')

chapter(3,r'''
## 1. From human judgment to a pair

For one prompt x, annotate a preferred response yw and a less preferred response yl. “Chosen” means preferred **within the presented comparison**, not an absolute correctness certificate. The gravity example in the DPO notes ranks clarity for a child; the local exam example ranks structured advice above panic. Candidate generation and label generation are separate processes: AI-generated answers can still receive human labels, and AI labels can rank human-written answers.

A useful rubric specifies correctness, relevance, tone, safety, completeness and allowed uncertainty. Compare answers under the same prompt and context. Retain annotator disagreement rather than forcing false certainty, and decide explicitly how to represent ties. The provided JSONL has no tie or confidence fields, so those properties cannot be recovered.

Filter malformed pairs, empty answers, contradictory contexts, truncated answers and label mistakes. Deduplicate before splitting. Group paraphrases or related conversations into the same split so a validation answer cannot leak through a nearby training prompt. Use topic/task stratification and separate test prompts that are never used for reward tuning or checkpoint selection.

## 2. A scalar reward model and Bradley–Terry loss

A transformer can represent the full prompt+response and pass its final relevant representation through a scalar head. Let `rψ(x,y)` be the real-valued score, with ψ the trainable reward parameters. Under a Bradley–Terry model at unit preference scale,

\[
P(y_w\succ y_l\mid x)=\sigma(r_\psi(x,y_w)-r_\psi(x,y_l)),\quad
\sigma(z)=\frac1{1+e^{-z}},
\]
\[
\mathcal L_{RM}(\psi)=-\mathbb E_{(x,y_w,y_l)\sim D}
\log\sigma(r_\psi(x,y_w)-r_\psi(x,y_l)).
\]

D is the comparison dataset; `≻` means preferred. A sigmoid converts a score difference into a modeled pairwise probability. This assumes a scalar utility representation and logistic pairwise noise; real preferences can violate these assumptions.

Why this loss? The observed label says the winner wins. Its Bernoulli likelihood is the sigmoid value; negative log-likelihood gives the minimization loss. If chosen score=2 and rejected=−1, difference=3, modeled win probability≈0.9526 and loss≈0.0486. Reversing them gives difference=−3 and loss≈3.0486. This same comparison logic underlies the implicit reward derivation of DPO.

Adding any prompt-only constant c(x) to both rewards leaves the comparison unchanged. The DPO PDFs preserve the useful example `(8,3)` and `(108,103)`: both differences are 5 and induce the same pairwise probability. Absolute score levels cannot be uniquely recovered from pairwise labels alone.
''' + diagram('13_reward_pair') + r'''
## 3. Normalization, calibration and generalization

Pairwise accuracy measures ranking, not whether a score is an absolute quality probability. Check validation pairwise likelihood and reliability of modeled win probabilities on new comparisons. Mean/std normalization can control score scale for RL, but it changes the effective strength relative to KL. Compute normalization statistics on an appropriate fixed training/calibration distribution, document them, and avoid mixing raw and normalized scores in actor/critic targets.

A reward head initialized from a causal LM is usually newly initialized. The PPO notebook's saved load report names `score.weight` as missing; this is expected and requires training. Four preference pairs and one epoch cannot establish broad scorer generalization. Overfitting can manifest as excellent training ranking but poor ranking on policy-generated answers.

## 4. Measured audit of your JSONL

Source: [reward_preferences_dataset.jsonl](../reward_preferences_dataset.jsonl). Full machine-readable report: [dataset_report.json](assets/source_audit/dataset_report.json).

| Check | Measured result |
|---|---:|
| Nonempty records parsed | 20 |
| Invalid JSON lines | 0 |
| Field set per record | Exactly `prompt`, `chosen`, `rejected` |
| Types | All three fields are strings in all records |
| Missing/blank values | 0 / 0 |
| Identical chosen/rejected pairs | 0 |
| Exact duplicate records | 0 |
| Duplicate prompts after lowercase/strip | 0 |
| Chosen longer than rejected in characters | 20 of 20 |

| Field | Character min / max / mean | Whitespace-word min / max / mean |
|---|---|---|
| prompt | 11 / 54 / 33.8 | 3 / 9 / 6.1 |
| chosen | 75 / 131 / 96.75 | 10 / 19 / 14.2 |
| rejected | 32 / 76 / 58.1 | 7 / 13 / 8.8 |

These are Python string lengths and `str.split()` counts, **not tokenizer lengths**. Token counts depend on model tokenizer and formatting and were not measured by loading a model here.

A verified representative record is:

```json
{
  "prompt": "What is AI?",
  "chosen": "AI is the ability of machines to perform tasks that usually require human intelligence.",
  "rejected": "AI is random magic with no real meaning."
}
```

The rows cover study advice, fitness, teaching, productivity, coding, stress and elementary ML concepts. All chosen answers are visibly sensible relative to deliberately weak or false alternatives. This is useful demonstration material but weak evidence for subtle preference learning. No annotator IDs, numeric scores, timestamps, provenance, explicit label field, reference answer or predefined split exists. The schema encodes the preference by column assignment.

All winners are longer in characters. This creates a strong possible length shortcut. The audit establishes the correlation, not that any model actually learned it. Add length-matched hard negatives, correctly scoped responses and topic diversity before serious training. Review medical/fitness advice under a suitable rubric; syntactic cleanliness does not validate every domain claim.

## 5. Actual usage and transformations

The PPO notebook cells 6–7 contain a **commented** local JSONL loader for `/content/reward_preferences_dataset.jsonl`. Active cell 8 uses four inline rows matching the first four records. None of the active DPO/ORPO/GRPO paths directly loads this local JSONL by default.

For the robust DPO notebooks, select `DATA_SOURCE="json"` and set `JSON_PATH` to the actual JSONL filename in a separate run. Hugging Face's JSON loader supports JSONL. The notebook default `preference_data.json` is not the provided filename. The plain-text conversion wraps prompt as user messages and chosen/rejected as assistant completions.

For **ORPO**, the same plain preference schema is structurally suitable after the installed trainer's supported formatting. It does not need a reference answer field or separate reward scores.

For **reward training**, render each full conversation `[user prompt, assistant answer]` for both candidates so the scalar scorer sees x and y. Confirm the installed `RewardTrainer` joins or extracts prompts as intended; answer-only tokenization is not interchangeable with prompt-conditioned scoring.

For **PPO rollout training**, keep prompts and tokenize them with the policy's template; pairwise labels train an RM separately. A frozen trained RM must score new answers. Simply assigning the chosen response's label to every generated answer is invalid.

For **GRPO**, prompts can be reused, but a reliable scorer for newly generated completions is still necessary. You may deliberately transform `chosen` to `reference_answer` for the notebook's similarity demo; this is a new metadata field, not a field originally present. A single chosen answer is not an exhaustive oracle for all valid answers, and text similarity is not mathematical verification.

## 6. Executable loading and validation

This stdlib-only example runs from the source directory, reads the originals, and writes nothing:

```python
from pathlib import Path
import json

path = Path("reward_preferences_dataset.jsonl")
rows = []
required = {"prompt", "chosen", "rejected"}
with path.open(encoding="utf-8") as handle:
    for line_number, line in enumerate(handle, 1):
        if not line.strip():
            raise ValueError(f"Blank line {line_number}")
        row = json.loads(line)
        if not isinstance(row, dict) or set(row) != required:
            raise ValueError(f"Unexpected schema at line {line_number}")
        if not all(isinstance(row[k], str) and row[k].strip() for k in required):
            raise ValueError(f"Invalid string at line {line_number}")
        if row["chosen"].strip() == row["rejected"].strip():
            raise ValueError(f"Identical answers at line {line_number}")
        rows.append(row)
print(len(rows), rows[0])
```

The reusable [validator](assets/validate_dataset.py) also measures lengths and duplicates. It reports defects rather than silently inventing or renaming fields.

## Revision

Good data must have correct context, meaningful labels, hard comparisons and leakage-resistant splits. The local file is clean JSONL with 20 pairs, but its small size and universal winner-length correlation limit conclusions. Reward models learn comparisons; their scores need validation before driving online optimization.
''')

chapter(4,r'''
## 1. Why PPO: improve a policy without rewarding an excessive step

A vanilla policy-gradient update increases the likelihood of actions with positive advantage. If we optimize repeatedly on one rollout, a large parameter change can make that rollout a poor representation of the new policy. PPO uses a local probability-ratio surrogate with clipping to remove further incentive for some overly large beneficial changes.

The RLHF PDF pages 30–36 uses old P(right)=0.60, new P(right)=0.72, reward 5 and value estimate 3. That gives ratio 1.2 and an illustrative advantage +2. This is a one-step pedagogical example; a full response has many token probabilities and usually uses GAE rather than immediate reward minus value.

PPO is a general policy optimizer. In classical LLM RLHF it is useful because it can optimize a nondifferentiable response-level reward model score through sampled token log probabilities, while a critic reduces estimator variance.

## 2. Architecture and rollout data

The actor samples responses from a frozen **old behavior policy** during rollout collection. Store response tokens, active-token masks, old action log probabilities and old critic values. Score complete responses with a frozen RM or other reward source. Score the same actions with the frozen reference. Construct shaped rewards, advantages and return targets before optimizing several minibatches.

A common sampled shaping choice is

\[
k_t=\log\pi_{old}(a_t|s_t)-\log\pi_{ref}(a_t|s_t),\quad
R_t=-\kappa k_t+\mathbb 1[t=T-1]r_\psi(x,y).
\]

κ is the RLHF KL coefficient, T is the number of active response tokens, and rψ is a terminal response score. The expected sampled log ratio under the rollout policy is the corresponding KL. Padding and prompt positions must be excluded. Some implementations use another KL estimator, include EOS penalties, normalize scores, or add an explicit KL loss instead. These are implementation choices, not all confirmed notebook features.

The critic predicts Vφ(st), the remaining shaped return. A final RM score does not directly provide an expected value at every prefix. The critic learns that temporal prediction from rollout targets.
''' + diagram('03_ppo_loop') + r'''
## 3. Derive the ratio surrogate

For stored state/action data from πold, define

\[
\rho_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
=\exp(\ell_{\theta,t}-\ell_{old,t}).
\]

ρ is called r_t in many papers; here ρ avoids confusion with reward. ℓ is the selected token's log probability, θ the current actor parameters, and the denominator is fixed during the optimization of a rollout. At collection, ρ≈1. Recompute the numerator on the exact stored tokens, not on newly generated answers.

Importance sampling motivates the surrogate `E_old[ρ_t Â_t]`. A fixed advantage weights how much increasing an action's relative probability is desirable. This is a local approximation and does not fully correct new-policy state occupancy or guarantee improvement.

## 4. Clipped PPO objective and its sign

The maximized clipped surrogate is

\[
L^{CLIP}(\theta)=\mathbb E_t\left[
\min\left(\rho_t\hat A_t,
\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\hat A_t\right)
\right].
\]

ε>0 determines the ratio interval, usually around 1. Ât is a detached rollout advantage, often normalized for the actor. The minimum chooses the more pessimistic objective. Its effect depends on advantage sign:

\[
\ell_t^{CLIP}=\begin{cases}
\min(\rho_t,1+\epsilon)\hat A_t,&\hat A_t\ge0,\\
\max(\rho_t,1-\epsilon)\hat A_t,&\hat A_t<0.
\end{cases}
\]

For a positive advantage, ratios above the upper limit stop increasing this sample's surrogate. For a negative advantage, ratios below the lower limit stop improving it. Harmful-direction changes remain penalized outside the interval. An optimizer minimizing a loss uses `loss_policy = -mean(clipped_surrogate)`; replacing `min` with `max` without also changing the signs is wrong.

### Worked clipping table

Illustrative ε=0.2; all advantages are fixed during this calculation.

| Advantage | Ratio | Unclipped ρA | Clipped ratio × A | Minimum | Effect |
|---:|---:|---:|---:|---:|---|
| +2 | 1.5 | 3.0 | 2.4 | 2.4 | Stops extra incentive to increase |
| +2 | 0.5 | 1.0 | 1.6 | 1.0 | Still discourages too-low likelihood |
| −2 | 0.5 | −1.0 | −1.6 | −1.6 | Stops extra incentive to decrease |
| −2 | 1.5 | −3.0 | −2.4 | −3.0 | Still penalizes too-high likelihood |

With old probability 0.60 and new 0.95, ρ≈1.583. A positive-advantage sample contributes as if its ratio were 1.2 to the clipped branch. PPO does **not** overwrite the new probability with 0.72. Other samples, shared parameters, critic losses and optimizer momentum can move it further. The source PDF pages 44–45 partly explains this but suggests bounded gradients/updates too strongly: surrogate clipping is not a hard KL or weight-update constraint.
''' + diagram('04_ppo_clipping') + r'''
![Illustrative clipped surrogate for positive and negative advantage](assets/plots/ppo_clipping.svg)

Plot assumptions: ε=0.2; A=+1 or −1; all states/advantages held fixed. These are analytical curves, not recorded training results. Reproduce with [plot code](assets/plot_objectives.py).

## 5. GAE, critic objective and full training loss

For token reward Rt, genuine termination flag dt, critic Vφ and discount γ,

\[
\delta_t=R_t+\gamma(1-d_t)V_{old}(s_{t+1})-V_{old}(s_t),
\quad \hat A_t=\delta_t+\gamma\lambda_{GAE}(1-d_t)\hat A_{t+1}.
\]

Return targets may be `Ĝt = Ât + Vold(st)` using raw advantages. Some trainers whiten rewards or actor advantages; the critic target must stay in the correct scale. See the two-step numerical example in [Chapter 01](01_REINFORCEMENT_LEARNING_FUNDAMENTALS.md).

A basic critic minimization loss is

\[
\mathcal L_V(\phi)=\frac12\mathbb E_t[(V_\phi(s_t)-\hat G_t)^2].
\]

Some implementations also clip value predictions around old values and take the larger squared error. That is a separate mechanism from policy-ratio clipping. Define it only if the installed trainer actually uses it.

One possible total minimization loss is

\[
\mathcal L_{total}=-L^{CLIP}+c_V\mathcal L_V-c_H\mathbb E_tH(\pi_\theta(\cdot|s_t))
+\kappa_{explicit}\mathbb E_tD_{KL}(\pi_\theta\|\pi_{ref}).
\]

cV weights the critic, cH the entropy bonus, and κexplicit an optional explicit KL term. If KL already shapes rewards, adding a second penalty changes the objective; do not accidentally count it twice. The PPO surrogate is only one part of a practical RLHF implementation. The source notebook does not write these tensors or all coefficients by hand; the trainer implements its own full loss and defaults.

A categorical entropy bonus requires the vocabulary distribution, while a mean sampled negative log probability is an estimator with a different gradient interpretation unless used correctly. Metrics named entropy, KL and non-score reward must be read in the context of the trainer.

## 6. Complete execution-order walkthrough of your PPO notebook

Source: [RLHF_with_PPO_Final_Code.ipynb](../RLHF_with_PPO_Final_Code.ipynb). Cell numbers are **1-based JSON cell order**, including empty/commented cells. Full source and stored outputs are preserved in [cell extract](assets/source_audit/RLHF_with_PPO_Final_Code_cells.md).

| Cells | Actual code and configuration | Theory/data mapping and practical assessment |
|---|---|---|
| 1–2 | Lower-bound installs; imports `RewardTrainer`, `RewardConfig`, and experimental `PPOTrainer`, `PPOConfig` | Recorded output says TRL 1.6.0, CUDA unavailable. APIs are experimental; lower bounds are not a reproducible lock |
| 3 | Seed 42; `dtype=float16` on CUDA else float32; `clear_memory()` | Seeds Python/Torch; CUDA dtype selection does not establish native BF16 support; `empty_cache` cannot free live tensors |
| 4 | Active `model_name="HuggingFaceTB/SmolLM2-135M-Instruct"` | The Qwen model line is commented; policy/RM initialization uses SmolLM2 |
| 5 | `tok_rm`, right padding, EOS fallback | Tokenizer for RM; last relevant token pooling and template consistency matter |
| 6–7 | Commented JSONL loading and transformation | Local file is not loaded during default execution |
| 8 | Four inline `raw_reward_data` rows → `make_chat_prompt` → `make_reward_example` → `reward_ds` | Prompt template with assistant generation prefix; chosen/rejected append EOS. Verify trainer joins prompt and answer; all four match the local file's first records |
| 9 | `rm=AutoModelForSequenceClassification(...,num_labels=1)` | Scalar preference scorer; missing `score.weight` load report reflects new scalar head |
| 10 | `rm_args`: batch 1, epoch 1, LR 1e−5, max length 256, no eval/save strategy | No held-out RM validation. Gradient checkpointing is enabled; trainer fp16/bf16 both false |
| 11–12 | `rm_trainer.train()`, save `./rm_out`; delete RM/trainer/tokenizer | RM stage ends; weights persist on disk. No broad preference-generalization evidence |
| 13 | Policy tokenizer `tok`, left padding | Prompts padded for batched generation; same model vocabulary/template as reward stage |
| 14 | `policy` trainable causal LM; `ref_model` separate causal LM, eval mode and gradients frozen | Actor and fixed KL reference. Old rollout logps are trainer-managed, not `ref_model` |
| 15 | `reward_model` reloads `./rm_out`, eval, all gradients disabled | Frozen scorer of generated responses |
| 16 | `value_model` reloads `./rm_out`, checkpointing enabled, not frozen | Critic initialized from reward weights; same initial architecture, distinct training target |
| 17 | Four `prompt_ds` rows → `tokenize_for_ppo` → `input_ids`, `length`; truncation 128 | Fresh rollout prompts; no chosen/rejected labels in PPO dataset. Filtering length≤128 after truncation cannot detect originally overlong prompts |
| 18 | `ppo_args`: batch 1, accumulation 1, LR 1e−6, 1 minibatch, 1 PPO epoch, 6 episodes, response length 16 | Extremely small smoke demo; discount, GAE λ, KL coefficient, clipping, reward whitening and value clipping are not explicitly set |
| 19–20 | `PPOTrainer(...model=policy, ref_model, reward_model, value_model, train_dataset=...)`; `.train()` | Trainer owns rollouts, logps, values, GAE and losses. No custom PPO loop/tensor calculation appears in notebook |
| 21 | Save policy and tokenizer to `./ppo_out` | Final artifact save; `save_strategy="no"` means no periodic resume checkpoints are configured |
| 22–23 | Load `infer_model`, template prompt, sample 80 tokens; decode entire generated sequence; empty final cell | Inference demonstrates loading, but displayed output includes prompt. Trainer/model objects remain live before reload; cache clearing alone does not release them |

### What the stored outputs establish

The saved execution shows reward training, PPO initialization, policy training and save messages on CPU. A `var()` warning in PPO metrics says degrees of freedom are ≤0 for a singleton ratio-statistic sample. That can explain a diagnostic NaN without proving the optimization loss itself became NaN. The final response discusses exam preparation and includes the full chat prompt. It is not a held-out comparison or a before/after quality test.

### Canonical PPO details delegated to the library

Token-level old/current/reference logps, critic values, KL shaping, GAE, value targets, clipping and minibatch loss are handled by the trainer. Their typical tensor shapes are `[B,T]` for selected token logps/values/rewards, `[B,T]` for active masks, and `[B,T,Vocab]` for full logits where materialized. This describes the architecture, not locally defined notebook variables. Exact masks, defaults, EOS treatment and target normalization require inspection of the installed TRL 1.6.0 implementation. Current upstream PPO paths have moved or disappeared, so live docs cannot verify that historical release's details.

## 7. Practical engineering and improvements

Collect a rollout batch large enough for stable statistics, then use a few optimization epochs and minibatches. The number of fresh prompts/responses, per-device minibatch size and gradient accumulation are related but distinct. Too much reuse makes the rollout stale. On ordinary data-parallel supervised-style updates, effective batch≈microbatch×accumulation×world size; PPO also has a rollout budget and minibatch partitioning that must be checked in its config.

For the source demo, first validate RM inputs and evaluate its rankings on genuinely held-out pairs. Use fresh prompts rather than only the four reward-training prompts. Log raw score, KL-shaped reward, response length, value loss, clip fraction and actor ratio statistics. Specify coefficients explicitly after verifying their names in the installed API.

Set mixed precision based on actual support; FP16 weights with both training precision flags disabled are not the same as FP32 training. Use appropriate loss scaling for FP16 where supported. Clip gradient norm separately from PPO probability-ratio clipping. Gradient checkpointing trades recomputation for activation memory; disable training cache as appropriate and re-enable it for generation if supported.

Save full trainer state (optimizer, scheduler, RNG and step), not just final model weights, when resume is required. The notebook has a final save but no explicit resume example. Keep independent evaluation and stop before proxy overoptimization. Release all live model/trainer references before loading another full model when memory is tight. Decode `generated_ids[0, input_length:]` for answer-only inference.

## 8. Common mistakes

Confusing reference with old policy breaks ratio meaning. Treating reward minus value as exact token advantage ignores future shaped rewards. Forgetting completion masks trains on prompt/padding actions. Recomputing old probabilities after an update invalidates the fixed denominator. Differentiating through returns or old values changes the estimator. Claiming clipping guarantees stability overstates its protection. A learned RM is required by this RLHF notebook, but not by general PPO with environment/rule rewards.

## Revision

PPO collects recent-policy trajectories, calculates detached advantages and targets, then updates actor and critic with a clipped surrogate and value loss. Its old policy supports local rollout reuse; the RLHF reference anchors behavior. Your notebook is a six-episode trainer-based demonstration with a four-pair reward model, not a validated alignment run.

Primary reference: [Schulman et al., Proximal Policy Optimization Algorithms, 2017](https://arxiv.org/abs/1707.06347); [GAE](https://arxiv.org/abs/1506.02438). See [reference verification notes](EXTERNAL_REFERENCES.md) for historical PPO API limits.
''')

chapter(5,r'''
## 1. Motivation: move the preference comparison into the policy objective

Classical PPO RLHF fits a scalar reward model, generates responses, estimates advantages with a critic and optimizes a policy. DPO asks whether we can fit the preference relation directly through policy probabilities. It uses a mathematical correspondence between rewards and optimal KL-regularized policies, eliminating an explicit reward model and online rollout loop.

The DPO PDFs' useful teaching progression is: chosen relative score, rejected relative score, their difference, sigmoid, negative logarithm. Their gravity, fever and simple-AI examples emphasize comparative preference. Preserve that intuition, but do not interpret DPO as guaranteed monotonic growth of each chosen answer's absolute likelihood. The supplied saved outputs give a concrete counterexample.

## 2. Derive the reward–policy relationship

Fix one prompt x and reward function r(x,y). Consider the response-level optimization

\[
\max_\pi\sum_y\pi(y|x)r(x,y)
-\beta\sum_y\pi(y|x)\log\frac{\pi(y|x)}{\pi_{ref}(y|x)},
\quad \sum_y\pi(y|x)=1.
\]

β>0 is the KL penalty coefficient in this formulation. The reference must have support for responses to which the policy assigns positive mass; normalization must be finite. This is a distribution-level derivation, not proof that finite neural-network training reaches the optimum.

Introduce multiplier η(x) for normalization. Differentiate with respect to π(y|x):

\[
r(x,y)-\beta\left[\log\frac{\pi(y|x)}{\pi_{ref}(y|x)}+1\right]+\eta(x)=0.
\]

Solve and normalize:

\[
\pi^*(y|x)=\frac{\pi_{ref}(y|x)e^{r(x,y)/\beta}}{Z(x)},\quad
Z(x)=\sum_y\pi_{ref}(y|x)e^{r(x,y)/\beta}.
\]

Z is the partition function ensuring probabilities sum to one. Higher reward tilts the reference toward that response. At a fixed reward, larger β makes the tilt weaker, so the optimum stays nearer the reference.

Rearrange:

\[
r(x,y)=\beta\log\frac{\pi^*(y|x)}{\pi_{ref}(y|x)}+\beta\log Z(x).
\]

This is the reward reparameterization. A policy-induced implicit reward can be written `r̂θ(x,y)=β log[πθ(y|x)/πref(y|x)]` after choosing a prompt-dependent reward offset. It is not just an unlogged probability ratio. Scores differing by c(x) induce the same pairwise preferences.

### Cancel the difficult partition function

Under Bradley–Terry, `P(yw ≻ yl | x)=σ(r(x,yw)−r(x,yl))`. Substitute the reward reparameterization: βlogZ(x) cancels because both responses have the **same prompt**. Thus we can fit preferences without estimating Z or training a separate scalar network.

The assumptions are a scalar reward model of preferences, logistic comparison likelihood, a fixed supported reference, and an expressive enough policy class. DPO does not establish that every human preference is representable by one consistent scalar utility.

## 3. Standard DPO loss, term by term

\[
\mathcal L_{DPO}(\theta)=-\mathbb E_{(x,y_w,y_l)\sim D}
\log\sigma\left(\beta\left[
\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}
-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right).
\]

x is the prompt; yw is the winner; yl the loser; πθ the trainable model; πref a fixed reference; β the scaling inherited from the KL derivation; σ the logistic sigmoid; D the pairwise dataset.

Define completion sequence log probabilities `ℓθ,w`, `ℓref,w`, `ℓθ,l`, `ℓref,l`. The margin is

\[
z=\beta[(\ell_{\theta,w}-\ell_{ref,w})-(\ell_{\theta,l}-\ell_{ref,l})],
\quad \mathcal L=-\log\sigma(z)=\operatorname{softplus}(-z).
\]

The subtraction compares how much the policy has promoted the winner **relative to the reference**, against its promotion of the loser. A large positive margin makes loss small. Use stable `logsigmoid` or `softplus`; do not exponentiate long sequence likelihoods and divide tiny probabilities.

### Worked examples preserved from the sources

If the already β-scaled chosen/rejected scores are 2 and −1, z=3, σ(z)≈0.9526, loss≈0.0486. Reverse them to −2 and +1: z=−3 and loss≈3.0486. DPO final PDF page 14 calls 95.26% “confidence”; this is a model comparison probability under the assumed link function, not validated real-world confidence.

An explicit log-probability example: `ℓθ,w=−4`, `ℓref,w=−5`, `ℓθ,l=−6`, `ℓref,l=−5`, β=0.1. Winner score=0.1, loser score=−0.1, z=0.2, loss≈0.5981. The loss can improve even if both answers lose absolute probability as long as the rejected likelihood falls more relative to the reference.

At initialization with policy=reference, both implicit rewards are zero, z=0 and loss=log2≈0.6931. A strict `winner_reward > loser_reward` accuracy metric counts equal scores as false, explaining the source's initial 0.0 preference accuracy rather than implying the original model knows no good answers.
''' + diagram('05_dpo_pipeline') + diagram('06_dpo_logps') + r'''
![Illustrative pairwise logistic loss](assets/plots/preference_loss.svg)

This common scalar curve also describes RM and ORPO losses when their respective margins are substituted. It is illustrative; [plot code](assets/plot_objectives.py) reproduces it.

## 4. Gradient and beta: two related interpretations

For fixed reference logps,

\[
\nabla_\theta\mathcal L
=-\beta\sigma(-z)\left[
\nabla_\theta\log\pi_\theta(y_w|x)-\nabla_\theta\log\pi_\theta(y_l|x)
\right].
\]

The factor σ(−z) gives more weight to misranked/hard comparisons. The loss encourages winner-over-loser relative likelihood through shared parameters; it does not independently control every sequence probability. Easy comparisons can saturate.

At fixed reward in the optimal-policy derivation, larger β means stronger KL regularization. At fixed observed log-ratio margin during neural training, increasing β also steepens the logistic scaling and can change saturation/gradient magnitude. Dataset, learning rate, epochs, reference choice and loss variants affect the actual outcome. Therefore “larger beta always makes stronger preference learning” or “always produces a closer policy” is too simple. `beta=0.1` in your notebooks is a demo configuration, not a universal optimum.

## 5. Tokens, masks and reference behavior

Standard causal DPO uses the **sum** of log probabilities of completion tokens:

\[
\ell_\theta(x,y)=\sum_t m_t\log\pi_\theta(y_t|x,y_{<t}),
\]

where mt=1 only for included completion tokens (including EOS if the chosen convention includes it). Prompt/padding positions have zero loss mask. A mean log probability changes the sequence scoring and standard objective unless a specific length-normalized variant is intended.

Shift logits by one token: logits at position j predict input token j+1. Input attention masks exclude padding from attention; completion loss masks exclude prompt tokens from scoring. They solve different problems. Labels `−100` are a training ignore sentinel and must never be passed directly as a gather index. Correct padded position IDs and causal attention remain necessary, especially for left padding.

Apply the model's chat template exactly once. Choose whether data already contains complete conversations or separate prompt/completion messages. The chosen and rejected histories must agree. Adding BOS/EOS again after a template already supplied them can shift the boundary. Tokenization of `prompt + answer` need not equal concatenation of independently tokenized prompt and answer due to boundary token merges; inspect the full tokenized sequence and trainer's boundary logic.

A separate frozen model is one reference implementation. With LoRA over an untouched frozen base, disabling the newly trained adapter can supply the initial reference distribution. If the desired reference already includes an SFT adapter, disabling all adapters would instead revert to the wrong base unless a frozen reference adapter or equivalent mechanism is retained. Cached reference logps must match exact formatted pairs, masks and truncation. `ref_model=None` is not synonymous with “no reference policy.”

## 6. All three notebooks compared using actual code

| Item | DPO_Training.ipynb | DPO_Training_Final.ipynb | Final_DPO.ipynb |
|---|---|---|---|
| Source cells | 47 | 47; identical source to preceding notebook | 15; compact prototype |
| Model | Qwen2.5-0.5B-Instruct | Same | Same |
| Active data | Four inline ML examples | Same | Full `trl-lib/ultrafeedback_binarized`, no subset |
| Local JSON option | `DATA_SOURCE="json"`; default filename differs from local JSONL | Same | Loader and path commented |
| Eval | Seeded split; 3 train / 1 eval for inline demo | Same | None |
| LoRA | r=16, α=32, all-linear, dropout .05 | Same | r=8, α=16, q/v/k/o projections |
| 4-bit | NF4, double quantization, conditional CUDA loading | Same | bitsandbytes installed; no quantization config used |
| Batch/accumulation | 1 / 8 | Same | 2 / 4 |
| Optimization | LR 5e−5, β .1, 40 inline steps; otherwise 1 epoch | Same | LR 1e−5, β .1, 3 epochs |
| Precision code | CUDA/support checks; CPU float32 | Same | BF16 whenever CUDA, FP16 whenever CPU: unsafe flags |
| Reload | `AutoPeftModelForCausalLM` | Same | `AutoModelForCausalLM`; version-dependent adapter autodetection |
| Saved execution | 40-step outputs and metrics | Same main metrics despite different saved version strings | KeyboardInterrupt in cell 12; no verified completed save/inference |

Do not infer improvements simply from “Final” in a filename. The 47-cell pipelines are the better documented starting point. Their source is identical, so consolidate the walkthrough and preserve output provenance differences.

### Execution order for both 47-cell notebooks

| Cells | Objects/data produced | Why they matter and what to inspect |
|---|---|---|
| 1–5 | Intro, correction list, unpinned `%pip install -U` | The claimed prior bugs correspond to the compact prototype; installs need a tested lock |
| 6–7 | Imports, `SEED=42`, Python/NumPy/Transformers seeds and printed versions | Reproducibility within an environment; saved outputs are not a requirements file |
| 8–11 | `MODEL_NAME`, `DATA_SOURCE`, `JSON_PATH`, hardware flags and `COMPUTE_DTYPE` | Selects dataset and precision; saved T4 BF16 output needs native/emulated-support verification |
| 12–13 | `INLINE_DATA`, `convert_plain_text_to_conversational`, `dataset` | Four ML concepts; plain strings become user/assistant message lists. Optional JSON checks field names but not all row values |
| 14–15 | `train_dataset`, `eval_dataset` | Seeded held-out split, only one eval example in active demo |
| 16–19 | `tokenizer`, left padding; `quantization_config` | Template/IDs plus conditional 4-bit NF4/double-quant compute configuration |
| 20–21 | `peft_config` | r16/α32 all-linear LoRA; base parameters frozen by PEFT |
| 22–23 | `model_init_kwargs`, `training_args` | `dtype`, SDPA, max length512, sigmoid loss, checkpointing, cosine schedule, eval10/save20, two checkpoints retained |
| 24–25 | `trainer=DPOTrainer(model=MODEL_NAME, ref_model=None, ...)` | Reference behavior is library/PEFT-managed; trainer owns chosen/rejected tokenization and loss. Quantization keyword acceptance is version-dependent |
| 26–31 | `initial_metrics`, `train_result`, `final_metrics` | Baseline loss, training and after-loss evaluation; no independent pretraining text-generation baseline |
| 32–33 | `history` DataFrame and loss plot | Mixed event rows can contain missing columns; displayed NaNs alone do not prove numerical failure |
| 34–37 | Saved adapter/tokenizer; delete trainer, collect garbage | Trainer save includes adapters with periodic checkpoints; verify full-state checkpoint before resume |
| 38–39 | `model=AutoPeftModelForCausalLM`, saved tokenizer | Correct explicit PEFT reload; optional quantized inference kwargs |
| 40–43 | `generate_response`, `test_prompts` | Applies template, stores input length, decodes new tokens only. Tests mostly repeat training concepts |
| 44–47 | Local ZIP creation, real-training warnings, official links | Colab convenience and limitations; not alignment validation |

Exact cell source/outputs: [DPO_Training](assets/source_audit/DPO_Training_cells.md), [DPO_Training_Final](assets/source_audit/DPO_Training_Final_cells.md).

### Compact prototype execution order

[Final_DPO.ipynb](../Final_DPO.ipynb) cell 1 displays a four-row literal but does not assign it to `dataset`. Cells 2–4 install/import and set Qwen/output constants. Cell 5's local loader is commented. Cell 6 assigns the downloaded UltraFeedback training split; the displayed literal is unused. Cells 7–9 load tokenizer/model and LoRA. Cell 10 sets the three-epoch config and incorrect precision flags. Cell 11 constructs `DPOTrainer`. Saved output warns about tokenized prompt versus prompt+rejected prefix mismatch, so boundary formatting requires inspection. Cell 12 is interrupted. Cells 13–14 define save and inference but have no saved execution outputs proving they ran. Cell 15 is empty.

The inference fallback catches every template exception and silently switches to a raw prompt; this can conceal a meaningful format mismatch. Modern Transformers may auto-detect PEFT adapters, so plain `AutoModelForCausalLM` loading is not universally broken; explicit PEFT loading makes intent/version requirements clearer. Prototype decoding includes the prompt. `device_map="auto"` is primarily an inference dispatch convenience and needs care for distributed training.

## 7. Interpret the saved evaluation correctly

Both detailed notebooks store initial eval loss 0.693147 and final 0.182760 on **one held-out pair**, with training loss≈0.077171 over 40 steps. Chosen logp changes from −51.2026 to −58.4874; rejected from −53.9604 to −77.3133. With β=.1, chosen implicit reward≈−0.7285 and rejected≈−2.3353; margin≈1.6068. The model lowered both absolute sequence probabilities while improving their relative preference margin.

That is a direct code-grounded correction to “chosen probability always increases.” One-pair preference accuracy 1.0 is not a broad alignment result. The stored loss curves are nearly identical, so they are not independent evidence of version robustness. The before/after metrics match exactly despite saved versions differing; reproducibility/provenance is unverified.

![Historical stored DPO training curve; not newly measured](assets/source_audit/DPO_Training_cell_33_output_2.png)

Historical output limitations: one generation's overfitting analogy is awkward, and another claims regression models use linear relationships; nonlinear regression is valid. Preference loss improvements do not establish factual accuracy. The T4 output says BF16 supported; T4 lacks native BF16 tensor-core support, so inspect device capability and the installed PyTorch support-check semantics, including emulation, before adopting that setting.

## 8. Recommended implementation approach and pitfalls

Use the 47-cell pipeline's schema validation, split, optional quantization, PEFT saving/reloading and completion-only generation as the starting pattern. Connect the actual JSONL intentionally, strengthen value/type checks, build a larger prompt-separated evaluation set and pin a tested environment. Inspect trainer-created completion masks on one batch before training. Specify intended loss/reference behavior explicitly and test adapter-disabled reference scores before updates.

DPO can overfit noisy/easy pairs, suppress both candidate likelihoods, exploit length shortcuts, and drift outside the data distribution. Monitor held-out relative rewards, both absolute logps, lengths, independent task quality and regressions. Reference conditioning motivates regularization but is not a hard bound on model drift. Memory depends on reference sharing/caching, pair sequence lengths, optimizer states and LoRA—not just the number of named model roles.

## Revision

DPO substitutes a policy/reference log ratio for a latent reward and fits pairwise logistic preferences. Z cancels within a prompt. Standard DPO uses a fixed reference and completion-summed logps. Your best source pipeline delegates the loss to TRL; its 40-step four-example run proves a demonstration can produce artifacts, not general alignment.

Primary reference: [Rafailov et al., Direct Preference Optimization: Your Language Model is Secretly a Reward Model, 2023](https://arxiv.org/abs/2305.18290); [official TRL DPO documentation](https://huggingface.co/docs/trl/dpo_trainer). The PDF's approximately 61% versus 57% TL;DR comparison is supported by the original paper under its specified evaluator/baseline setting; it is not a result from these notebooks or a universal ranking.
''')

chapter(6,r'''
## 1. Why group-relative learning

A large critic can be expensive and hard to train from sparse end-of-response rewards. The original DeepSeekMath formulation replaces that learned value baseline with comparisons among answers to the same prompt. GRPO samples a group, scores it, and reinforces answers that outperform their group.

The GRPO PDF pages 2–3 traces DeepSeek-Coder-Base-v1.5 7B → continued mathematical pretraining → math SFT → DeepSeekMath-RL. The paper confirms 120B math-related tokens as a major part of a larger continued-training mixture and introduces GRPO in 2024. Do not replace the coder checkpoint with the distinct DeepSeek-LLM family. The PDF's later family timeline contains claims beyond the original paper; these are source-context items with unverified release details, not prerequisites or evidence for the algorithm.

The motivating sentence “GRPO is PPO without a critic” captures one important difference but omits group sampling, normalization, token/sequence weighting and explicit KL placement. Later implementations may change all of those.

## 2. Workflow and group example

For each prompt x, sample G responses `yi ~ πold(·|x)`. An outcome scorer produces Ri for each answer. Compute their mean and standard deviation, then normalize each score into a relative advantage.

The PDF's `2+2` example (page 4) samples `[4,5,4,6]` with rewards `[1,0,1,0]`. Mean μ=0.5; using population std, s=0.5. Centered rewards are `[+.5,−.5,+.5,−.5]`; normalized advantages are `[+1,−1,+1,−1]` (before any numerical epsilon). The handwritten `reward−mean` values are a useful introductory baseline but omit the std division in original outcome GRPO.

The page-8 example rewards `[9,6,2]` has mean 17/3≈5.667; centered values `[3.333,.333,−3.667]`; population std≈2.867; normalized advantages≈`[1.162,.116,−1.279]`. These are pedagogical scores, not DeepSeek or notebook measurements.
''' + diagram('07_grpo_groups') + r'''
## 3. Original outcome-supervision mathematics

\[
\mu_x=\frac1G\sum_{i=1}^G R_i,\quad
s_x=\sqrt{\frac1G\sum_i(R_i-\mu_x)^2},\quad
\hat A_{i,t}=\frac{R_i-\mu_x}{s_x+\varepsilon_{norm}}.
\]

G is responses per prompt, i indexes responses, t indexes completion tokens, and εnorm is a numerical stabilizer added in practical code. Original outcome normalization is described using group std; whether code uses population std, sample std, a stabilizer or threshold must be checked. The same sequence advantage is broadcast to included tokens in outcome supervision.

For response yi of length Ti,

\[
\rho_{i,t}=\frac{\pi_\theta(y_{i,t}|x,y_{i,<t})}{\pi_{old}(y_{i,t}|x,y_{i,<t})},
\]
\[
J_{GRPO}=\mathbb E_{x,\{y_i\}\sim\pi_{old}}\left[
\frac1G\sum_i\frac1{T_i}\sum_{t=1}^{T_i}
\left\{\min(\rho_{i,t}\hat A_{i,t},
\operatorname{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)\hat A_{i,t})
-\kappa_{GRPO}\hat K_{i,t}\right\}\right].
\]

This shows original response-mean then group-mean weighting; completion masks replace the valid-token sum in padded batches. θ is current policy, πold collected the group, ε is PPO-style clip width, κGRPO is the KL coefficient. A minimization implementation uses `−J`. This is distinct from DPO's β inside a preference sigmoid.

One positive pointwise KL estimator used in the original paper is

\[
q_{i,t}=\frac{\pi_{ref}(y_{i,t}|s_{i,t})}{\pi_\theta(y_{i,t}|s_{i,t})},
\quad \hat K_{i,t}=q_{i,t}-\log q_{i,t}-1\ge0.
\]

For actions sampled from πθ, its expectation equals `DKL(πθ||πref)` when both distributions have compatible support and are normalized. Samples actually come from πold, so reused old-policy data raises sampling/gradient approximation questions; some libraries apply bias corrections or alternative estimators. Nonnegative samples do not remove these distinctions. The original GRPO KL term is added explicitly to the objective rather than included inside reward normalization, unlike common PPO RLHF shaping.

### Process supervision in the original paper

DeepSeekMath also explores scores at the end of reasoning steps. Normalized process rewards contribute to token advantages through sums of subsequent step rewards. The sequence-level broadcast formula above is **outcome supervision**, not the sole original GRPO variant. A separately learned critic is absent, but reward baselines and advantage computation remain value-related computations.

### Later library variants

Token-mean aggregation over the entire batch differs from averaging each response first: longer responses carry different weight. DAPO-style and fixed-denominator variants change length/normalization behavior. `scale_rewards="group"`, batch normalization, no std scaling, token/sequence importance ratios, asymmetric clipping and iteration counts are separate configuration choices. A zero KL coefficient may avoid needing reference forward passes; original GRPO includes a reference penalty.

The saved TRL **1.7.0** signature in notebook cell 31 lists `loss_type="dapo"`, `scale_rewards="group"`, `num_iterations=1`, ε=.2 and β default 0.0. The source cell 29 sets β=.01 but does **not** set `loss_type`. Therefore its recorded library path defaults to a DAPO aggregation variant, not necessarily the exact original response-mean GRPO objective. This is stronger evidence than assuming a `GRPOTrainer` name proves paper fidelity.

## 4. Equal rewards, variance and diversity

If `[1,1,1,1]` are all correct, μ=1, std=0 and centered advantages are zero. With a numerical stabilizer, the preference-gradient contribution is zero; without one, division yields NaN. KL or other losses can still update parameters. The same problem occurs for all-wrong groups. Log the fraction of constant-reward groups and whether the scorer sees the right answer metadata.

Increasing G increases chances of useful within-prompt differences, but requires more generation tokens and memory. Temperature too low yields duplicate responses; too high yields mostly junk and unstable reward comparisons. Reward normalization can overweight a tiny reward gap in an otherwise homogeneous group; changing std scaling changes the learning objective. Choose meaningful tasks, appropriate difficulty and reward resolution rather than adding arbitrary noise to labels.

For mathematical correctness, exact answer checks or tests can provide reliable signals when parsing and tolerances are designed carefully. Open-ended answers often need a learned or judge-based scorer. Format rewards certify format, not reasoning validity. A reward model is optional; a reward signal remains essential, as the handwritten pages 9–11 emphasize.

## 5. The first notebook path: eight-prompt similarity demonstration

Source: [Final_GRPO_Practical.ipynb](../Final_GRPO_Practical.ipynb). Full [cell extract](assets/source_audit/Final_GRPO_Practical_cells.md) preserves Markdown, comments and stored outputs.

| Cells | Actual data flow and configuration | Implication |
|---|---|---|
| 1–4 | Unpinned installs; removes torchao for reported conflict; imports regex/SequenceMatcher/Dataset/TRL/PEFT | Environment workaround is specific to recorded setup, not a requirement of GRPO |
| 5–11 | Eight `prompt` and `reference_answer` rows; `format_prompt` creates `Question: ...\nAnswer in simple English:` | Reference metadata survives `.map`; gold text is for reward functions, not teacher-forced SFT |
| 12–15 | `HuggingFaceTB/SmolLM-135M-Instruct` (not SmolLM2); tokenizer left padding; FP16 on CUDA; LoRA r8/α16 q/v | Text prompt format is custom plain text; training and inference use it consistently |
| 16–18 | Markdown reward-source/model-role comparisons | Correctly allows rules or learned reward; “PPO RM present” applies to RLHF pattern, not all PPO |
| 19–23 | `normalize_text`, `get_completion_text`, `similarity_score`, `keyword_overlap_score` | Character sequence similarity and set-based keyword recall; neither proves semantic correctness |
| 24 | `correctness_reward`: `2.5*sim + 2.5*overlap`, returns 0 if `reference_answer` missing | Range 0–5 when inputs valid; missing metadata silently erases this reward |
| 25 | `helpfulness_reward`: length bands, punctuation bonus, bad-phrase penalty | Rewards superficial style; “not sure” can be honest, so automatic penalty is potentially harmful |
| 26 | `clarity_reward`: alphabetic content, length band, repeated-character penalty | Readability heuristic; English alphabet check is not multilingual quality |
| 27–30 | `GRPOConfig`, trainer with three reward functions and `remove_unused_columns=False` | Extra metadata must reach scorer. Equal reward weighting is library-managed; no custom advantage/loss tensors in notebook |
| 31–32 | Prints TRL signature then trains | Recorded TRL1.7.0 and DAPO default; saved 10-step TrainOutput exists |
| 33–36 | Save adapter/tokenizer, reload with `PeftModel`; generate via same custom prompt | Saved response includes prompt because whole sequence is decoded; no held-out evaluation loop |

Cell 29 config: LR1e−5, per-device batch4, accumulation1, `num_generations=4`, completion length80, temperature.9, top_p.95, β=.01, max_steps10, checkpoint every10, checkpointing false, fp16 on CUDA. Group batch constraints concern the effective generation batch across devices/steps in the installed version. “Per-device batch must always be divisible by G” is too broad.

The comment in cell 23 says keyword overlap example is 3/5=.6 for `Machine learning learns from data`; the regex includes words of at least three letters and set sizes, which indeed yields five words for that reference. SequenceMatcher operates on normalized **characters**, not semantic embeddings or necessarily word-level sequences. The heuristic reward may favor copying gold text, punctuation and length while missing factual errors.

Saved output: 10 optimizer steps, training loss≈.063335, reported epoch1.25, and an AI definition. That loss is not comparable numerically to DPO/ORPO losses and does not measure held-out correctness. Generation reaches an incomplete final item; truncation and length should be inspected.

## 6. The second path: GSM8K reasoning with Unsloth and vLLM

| Cells | Actual implementation | Checks and limitations |
|---|---|---|
| 37–40 | New Unsloth/vLLM installs; Qwen2.5-0.5B-Instruct, max sequence1024, 4-bit, fast inference, LoRA rank16; all attention/MLP projections | Distinct workflow; dependency compatibility is unpinned. VRAM utilization .6 is vLLM planning, not a memory guarantee |
| 41 | `SYSTEM_PROMPT`, XML reasoning/answer format | Teaches an output format; valid XML-like tags do not certify reasoning |
| 42 | `get_gsm8k_questions`: loads `openai/gsm8k`, parses text after `####`, builds system/user message prompt and `answer` metadata | Full train split, no demo subset or eval split in source; missing delimiter returns None |
| 43–44 | `extract_xml_answer`, exact-string `correctness_reward_func`: 2 for gold match else0 | Equivalent numeric answers like `12.0` vs `12` can lose reward; malformed tags need stricter parser |
| 45 | `int_reward_func`: .5 for `.isdigit()` | Negative/decimal values fail; output type is not answer correctness |
| 46–48 | Soft/strict regex rewards .5 each; `count_xml` fractional tag/trailing-text rewards | Formatting can accumulate substantial reward for incorrect numeric answers; trailing-text expressions should be checked on boundary cases |
| 49–51 | LR5e−6, Adam betas .9/.99, decay.1, cosine/warmup.1, paged8bit optimizer; per-device batch1, accumulation1, G4; prompt256/completion768, max_steps100, grad norm.1 | Conflicts with earlier single-device grouping setting for versions requiring effective generation batch divisible by G; verify or configure generation batch/steps, do not assume runnable |
| 52–54 | Save LoRA, `fast_generate` apple-count test, merged16bit save | Source present; no stored outputs from this second path establish training or export success |

The second config omits explicit β, loss type, std convention and generation batch settings. The first path's TRL version output cannot prove versions after its new installation cells. No group sampling, mean/std calculation, ratio tensor or custom clipped objective is handwritten in either path; `GRPOTrainer` owns them. The reference can be an adapter-disabled base when supported, but exact behavior must be verified in the selected version.

## 7. Recommended use and debugging

Use the first path to learn the reward-function interface, then replace text similarity with a task-appropriate scorer before drawing quality conclusions. For reasoning, start with a small GSM8K subset, a robust gold-answer parser and a supported effective grouping config. Keep a disjoint test set. Test reward functions on correct, wrong, equivalent, empty and malformed completions before training. Log each reward component, group std, zero-variance fraction, completion lengths, format success, exact correctness and KL separately.

The absence of a critic can save parameter/optimizer memory, but G responses and long reasoning sequences can dominate generation cost. Beware unvalidated `device_map="auto"` in distributed training, scorer metadata columns dropped by preprocessing, format reward overwhelming correctness, truncated answers and all-identical samples.

## Revision

Original GRPO estimates a baseline and normalized advantage from a same-prompt group, uses a clipped token-ratio objective and explicit reference KL, and avoids a learned critic. Your notebook has one stored 10-step heuristic run plus an unexecuted-output GSM8K path; its recorded default loss aggregation is DAPO-style. Reward design and grouping are central, not incidental details.

Primary reference: [Shao et al., DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models, 2024, §4.1](https://arxiv.org/abs/2402.03300); [official TRL GRPO documentation](https://huggingface.co/docs/trl/grpo_trainer). The paper's 51.7% MATH result belongs to its model and evaluation setting, not your small-model notebook.
''')

chapter(7,r'''
## 1. Intuition: imitate the chosen answer and discourage the rejected one

SFT maximizes the likelihood of demonstrated answers. Shared language patterns can also raise unwanted answers' likelihood. ORPO combines chosen-answer negative log-likelihood with an odds-based chosen/rejected comparison in one training objective. It removes the separate frozen reference distribution used in standard DPO.

The ORPO PDF pages 3–8 describes this as monolithic, single-stage instruction plus preference learning. It can start from a pretrained model, but your two notebook paths actually load `Qwen/Qwen2-0.5B-Instruct`. Single-stage optimization does not mean no earlier pretraining/SFT occurred in that checkpoint.

ORPO uses offline preference pairs, without PPO rollouts, a learned critic or a separate RM. Reference-free design changes the objective; it is not standard DPO with a model copy deleted.

## 2. Define sequence likelihood carefully

Let y contain T response tokens and mt be its completion mask. The true autoregressive sequence log probability is

\[
\ell_\theta(x,y)=\sum_{t=1}^{T}\log\pi_\theta(y_t|x,y_{<t}).
\]

A sum-based SFT sequence NLL is `−ℓθ(x,yw)=−logπθ(yw|x)`. Practical trainers generally average the chosen-token NLL over included tokens to control loss scale.

The ORPO paper defines the score used in its odds through **length-normalized likelihood**:

\[
\bar\ell_\theta(x,y)=\frac{\sum_t m_t\log\pi_\theta(y_t|x,y_{<t})}{\sum_t m_t},
\quad p_\theta(x,y)=e^{\bar\ell_\theta(x,y)}.
\]

p is the geometric mean of completion token probabilities. It lies in (0,1], but scores over different responses do **not** form a normalized distribution over those responses. Calling p the calibrated chance that an entire answer occurs is incorrect. In this chapter π denotes true sequence likelihood, while p denotes ORPO's normalized likelihood score. This distinction is missing from the source PDF's elementary 0.75/0.25 example and matters in implementation.

## 3. Probability, odds, log odds and odds ratio

For a probability-like score p∈(0,1),

\[
\operatorname{odds}(p)=\frac{p}{1-p},\quad
\operatorname{logodds}(p)=\log p-\log(1-p).
\]

Odds compares an event's probability with its complement. Applying this transform to ORPO's normalized likelihood scores gives an odds-based preference surrogate; it does not magically calibrate the scores.

For chosen score pw and rejected pl,

\[
OR_\theta(x,y_w,y_l)=\frac{p_w/(1-p_w)}{p_l/(1-p_l)},
\quad \Delta_{OR}=\log OR
=(\bar\ell_w-\bar\ell_l)-[\log(1-e^{\bar\ell_w})-\log(1-e^{\bar\ell_l})].
\]

Do not substitute `ℓw−ℓl` alone for log odds; that is a log probability ratio and changes the objective. For small p, odds approaches p, but that is an approximation, not equality.

The preference minimization loss is

\[
\mathcal L_{OR}=-\mathbb E_D\log\sigma(\Delta_{OR}),\quad
\mathcal L_{ORPO}=\mathcal L_{SFT}+\lambda_{OR}\mathcal L_{OR}.
\]

λOR≥0 balances the chosen imitation and preference loss. The paper often uses λ; your TRL configs call this `beta=.1`. That β is a coefficient multiplying the ORPO preference component, not DPO's KL-derived beta or GRPO's KL penalty coefficient.

### Derivation of the comparison objective

If OR is the odds-based preference strength, `σ(logOR)=OR/(1+OR)`. Positive log odds means the winner has higher odds; the sigmoid maps that difference to a bounded preference score. For an observed winner, negative log of that score gives the logistic comparison loss. This is ORPO's designed surrogate, not a Bradley–Terry fit of a separately trained reward network.

The derivative `d logodds(p)/d log p = 1/(1-p)` shows how the odds transform changes gradient weighting. As p approaches 1, numerical conditioning becomes difficult; computing raw probabilities in low precision can round them to exactly 1. Stable log-space computation and finite checks matter.

## 4. Reproduce the source's worked example

ORPO PDF pages 11–16 uses prompt `2+2`, chosen `4`, rejected `5`, illustrative scores pw=.75 and pl=.25.

| Quantity | Calculation | Value |
|---|---|---:|
| Chosen SFT NLL in the one-token illustration | −ln(.75) | .287682 |
| Chosen odds | .75/.25 | 3 |
| Rejected odds | .25/.75 | 1/3 |
| Odds ratio | 3/(1/3) | 9 |
| Log odds ratio | ln9 | 2.197225 |
| Sigmoid preference score | 9/(1+9) | .9 |
| Preference loss | −ln(.9) | .105361 |
| Total with λOR=.1 | .287682+.1×.105361 | .298218 |

The PDF rounds intermediate values to .288 and .105, giving approximately .2985; using unrounded values gives .298218. This is rounding clarification, not a different algorithm. The .75/.25 values are chosen for a simple demonstration; real normalized sequence scores need not sum to 1.

Reverse pw and pl: odds ratio=1/9, Δ≈−2.197225, sigmoid=.1, preference loss≈2.302585. Chosen SFT loss=−ln(.25)≈1.386294; total at λ=.1≈1.616553. Both components penalize the reversed ranking in this example.
''' + diagram('08_orpo_objective') + r'''
## 5. Stable executable mathematical snippet

This PyTorch example operates on already computed completion-mean logps and a chosen-token NLL. It implements the objective components, not an entire trainer:

```python
import math
import torch
import torch.nn.functional as F

def log1mexp(log_p):
    # log(1-exp(log_p)); input must be strictly negative.
    if not torch.all(log_p < 0):
        raise ValueError("Require log p < 0; inspect empty masks and rounding")
    log_p = log_p.float()
    far = log_p < -math.log(2)
    result = torch.empty_like(log_p)
    result[far] = torch.log1p(-torch.exp(log_p[far]))
    result[~far] = torch.log(-torch.expm1(log_p[~far]))
    return result

chosen_mean_logps = torch.tensor([math.log(.75)], requires_grad=True)
rejected_mean_logps = torch.tensor([math.log(.25)], requires_grad=True)
log_odds_difference = (
    chosen_mean_logps - log1mexp(chosen_mean_logps)
    - rejected_mean_logps + log1mexp(rejected_mean_logps)
)
preference_loss = -F.logsigmoid(log_odds_difference).mean()
chosen_token_nll = -chosen_mean_logps.mean()  # One-token illustrative batch
loss = chosen_token_nll + .1 * preference_loss
assert torch.isfinite(loss)
loss.backward()
print(loss.item())
```

Use FP32 for sensitive log-odds arithmetic where appropriate. Empty completion masks must be rejected before division. Silent clamping can hide a formatting bug; if used for robust numerics, document its effect. Trainer token-average SFT across a batch can differ from mean-of-sequence NLL when lengths vary.

Current fetched TRL ORPO source calls `get_batch_logps(...average_log_prob=True)`, computes `log_odds` in FP32, returns `beta*logsigmoid(log_odds)` as a **negative-valued reward-like term**, and subtracts it from NLL in the final loss. That sign convention equals NLL plus beta times positive preference loss. A helper returning negative values does not imply the loss sign is wrong. Upstream source docstrings still mention reference logps in one helper despite ORPO being reference-free; read the actual code.

## 6. Actual standard-TRL notebook path

Source: [Final_ORPO_Practical.ipynb](../Final_ORPO_Practical.ipynb). Full [cell extract](assets/source_audit/Final_ORPO_Practical_cells.md) retains both paths and errors.

| Cells | Actual code/configuration | Explanation and issues |
|---|---|---|
| 1 | Deletes `trainer`, `model`, calls gc/Torch cache functions before local imports | Depends on previous runtime state; clean execution can NameError. Saved output instead shows an asynchronous CUDA assert, so it cannot establish a clean run |
| 2–5 | Uninstall then upgrade torchao≥.16; install `trl==1.9.2` with other unpinned packages; experimental ORPO imports | Different strategy from GRPO's torchao removal; environment-specific, not algorithmic. Saved optional binary-load warnings |
| 6–7 | Qwen2-0.5B-Instruct, UltraFeedback, output path; supported CUDA/BF16/FP16 branching | Qwen2 differs from DPO's Qwen2.5. Saved output says CUDA/BF16 true; actual GPU capability not printed here |
| 8–9 | Fast tokenizer right padding, EOS fallback; causal model compute dtype, cache disabled, pad ID set | Attention masks/ignored labels must match padding; trainer owns data tokenization |
| 10–12 | Load/shuffle seed42, subset100; cell11 older config commented; cell12 repeats subset100 | Saved external dataset columns are chosen/rejected/score_chosen/score_rejected, not the local JSONL schema. Implicit conversational prompts can be extracted by supported trainers |
| 13 | ORPOConfig: LR8e−6, beta.1, epoch1, batch1/accum4, max length512, checkpointing, log10, save epoch | β weights preference component. No eval dataset or eval strategy set; reproducibility limited by unpinned surrounding libs |
| 14–15 | LoRA r8/α16 q/k/v/o, dropout.05; create trainer and `.train()` | No separate reference/RM/critic object. Loss internals are delegated to ORPOTrainer |
| 16–17 | Save adapter/tokenizer, `trained_model=trainer.model`, enable cache, template prompt and completion-only decode | Using trainer model retains active adapter. Saved inference raises CUDA assert, so successful generated response is not established |

Cell 15 stored `TrainOutput` says global_step25, training loss≈3.204586, epoch1.0. This matches 100 examples with effective pair batch4 on one device. It is an output artifact with no held-out preference or task comparison. The trainer warns that it set `remove_unused_columns=False`; make that explicit when using that version. Neither the total loss nor warnings prove why inference failed.

After a CUDA device-side assert, restart the process/runtime to clear the poisoned context. Check token IDs against embedding size, generation EOS/PAD IDs, labels, special-token vocabulary changes and version compatibility. Use synchronous CUDA launches in a separate diagnostic run if needed. The cleanup-cell traceback may report an earlier asynchronous error; “empty_cache caused it” is not a justified diagnosis.

## 7. Actual Unsloth path and versions

| Cells | Implementation | Assessment |
|---|---|---|
| 18–20 | Fresh-runtime instruction; install Unsloth and pinned Transformers4.56.2, TRL.22.2, Datasets4.3.0; import `PatchDPOTrainer` | Distinct environment from experimental TRL1.9.2; do not install both paths in one live interpreter |
| 21–23 | Qwen2-0.5B-Instruct, sequence512, 4-bit; Unsloth LoRA r8/α16, all attention+MLP projections, dropout0, seed42, optimized checkpointing | QLoRA path reduces base memory; dropout0 is chosen for optimized implementation, not mandatory ORPO math |
| 24–25 | Shuffle/subset500; `format_preference_example` extracts chosen prompt history and final chosen/rejected assistant content, adds EOS | Check rejected history equals chosen history and both last roles are assistant. Existing function checks only length≥2, not those invariants |
| 26–28 | `PatchDPOTrainer()`; ORPO imports from top-level TRL; config LR8e−6, β.1, epoch1, batch1/accum4, prompt/completion256, 8bit Adam, warmup.1; `tokenizer=...` | Keyword and patch compatibility require verification in pinned environment. Pinned version does not make all unpinned dependencies reproducible |
| 29–32 | Train, save adapters, Unsloth inference with new-token slicing, merged16bit export | No stored outputs from this path establish completion or export success |
| 33 | Fully commented consolidated Unsloth alternative | Duplicate source teaching material; does not execute |

Here source versions are installation **requests**, not proof of installed successful runs. Experimental `processing_class` and older `tokenizer` interfaces must not be mixed. The notebook does not implement custom odds loss functions or calculate its own loss tensors; the equations above explain the trainer's intended behavior and fetched upstream implementation, with historical-version boundaries marked.

## 8. Trade-offs and corrections

ORPO removes reference forward passes, which can reduce memory/compute compared with otherwise similar DPO loading a separate reference. DPO reference caching/sharing, fused operations and different sequence lengths can narrow or reverse practical comparisons. “ORPO always needs less memory” is too broad.

A large preference coefficient can damage chosen imitation or encourage shortcuts; a small one approaches SFT. Monitor chosen NLL and preference component separately, plus held-out quality. Length-normalization changes bias but does not eliminate all length bias. No reference KL anchor means regression tests and stopping criteria become especially important.

The PDF page 9 calls DPO universally “safest” and ranks industry adoption. Those are unverified broad claims and do not justify a technical selection rule. Paper validation up to 7B (PDF page17) describes the original study, not a hard algorithm size limit. Later model examples and external deployment claims are retained as source-context leads in the audit rather than treated as benchmark evidence here.

## Revision

ORPO uses one trainable policy, chosen SFT NLL, and an odds-ratio comparison of length-normalized completion likelihoods. Probability ratio, odds ratio and log odds are distinct. Your notebook contains a stored 100-example TRL run with inference failure plus a separate unverified-output 500-example Unsloth path.

Primary reference: [Hong, Lee and Thorne, ORPO: Monolithic Preference Optimization without Reference Model, 2024](https://arxiv.org/abs/2403.07691); [EMNLP paper record](https://aclanthology.org/2024.emnlp-main.626/); [official TRL ORPO docs](https://huggingface.co/docs/trl/orpo_trainer).
''')

chapter(8,r'''
## 1. Compare objectives and required information first

Choose the optimizer from the supervision available and the engineering budget. Offline pairs support direct preference objectives; fresh-answer scoring supports rollout methods. More components do not automatically mean better alignment, and fewer components do not remove data/reward problems.

| Dimension | PPO (classical LLM RLHF use) | Standard DPO | Original outcome GRPO | Standard ORPO |
|---|---|---|---|---|
| Core idea | Actor-critic optimization with clipped local updates | Fit preference likelihood via policy/reference ratios | Group-relative advantages for sampled answers | Chosen imitation plus odds preference penalty |
| Main objective | Clipped advantage surrogate plus critic and optional entropy; RLHF KL shaping/penalty | −logσ of β-scaled difference of policy/reference log ratios | Group/response average clipped token surrogate minus explicit KL | Chosen-token NLL + λ×negative log sigmoid of log odds ratio |
| Policy-stage dataset | Prompts; rewards from scored fresh responses | Same-prompt chosen/rejected pairs | Prompts with scorer metadata if required | Same-prompt chosen/rejected pairs |
| Pairwise labels | Needed to train preference RM in classical pipeline; not by PPO itself | Required in standard pairwise objective | Not required if rewards are available; learned RM may use pairs | Required |
| Reward model | Typical classical RLHF scorer; rules/environment also valid | No separate RM | Optional reward source; original paper uses learned models too | No separate RM |
| Reference | Typical RLHF KL anchor; not intrinsic to general PPO | Standard formulation requires distribution/scoring | Original formulation includes reference KL | Not required |
| Critic | Learned return predictor in common PPO | None | No separate learned critic in original | None |
| Online/offline | Fresh rollouts, local reuse | Offline fixed pairs | Fresh groups, local reuse | Offline fixed pairs |
| Samples during optimization | Policy-generated responses | No online response generation needed | Multiple policy-generated responses | No online response generation needed |
| Responses per prompt | Often one per rollout prompt; can be more | Two supplied candidates, not generated online | G>1 for meaningful group comparison | Two supplied candidates, not generated online |
| Cost drivers | Rollouts, scorer/ref forwards, actor+critic backward | Pair policy forwards/backward and ref scoring/caching | G×generation tokens, rewards, policy/ref forwards | Pair policy forwards/backward plus chosen NLL |
| Memory drivers | Policy optimizer+critic, scorer/ref weights, rollout tensors/cache | Trainable policy/adapter, pair activations, reference or cached scores | Policy/adapter, grouped KV caches, reference if used | Policy/adapter and pair activations |
| Implementation complexity | High: masks, rollout semantics, return targets, multiple roles | Moderate: formatting, likelihoods and reference | High: sampling/grouping/rewards and variants | Moderate: formatting and numerically stable odds |
| Tuning/stability | Sensitive to score scale, learning rate, value quality and KL | Usually simpler loop; β/data/epochs still matter | Sensitive to reward variance, grouping/diversity, normalization and KL | Sensitive to NLL/preference balance and score normalization |
| Common uses | Optimize flexible feedback on newly generated outputs | Offline helpfulness/style/safety preference tuning | Reasoning, coding, tasks with scalable answer rewards | Joint instruction/preference optimization with no reference |
| Strengths | Flexible rewards and fresh-policy exploration | Simple offline supervised-style optimization | Critic-free comparative baseline, flexible reward sources | Single-stage objective and no ref scoring |
| Limitations | Scorer/critic reliability and expensive rollout machinery | Offline coverage limits; relative likelihood can improve while both scores fall | Generation overhead; equal-reward groups lose signal | No KL reference anchor; coefficient and odds conditioning matter |
| Failure modes | Reward exploitation, value error, large KL, stale rollouts | Mask/template mismatch, noisy labels, length shortcuts, regression | Zero variance, format gaming, incorrect parsing, length weighting | Odds numerical failure, preference domination, masking/format errors |

The “typical PPO” column is the RLHF notebook's pattern, not a universal requirement for PPO in a game. The GRPO column is original outcome GRPO, not every modern trainer default. Memory rankings depend on model sizes, precision, sharing, caching, response length and rollout settings.

## 2. Model roles separate from model copies

| Role | PPO RLHF | DPO | GRPO original | ORPO |
|---|---|---|---|---|
| Trainable policy | Yes | Yes | Yes | Yes |
| Frozen reference policy | Typical KL anchor | Yes, possibly shared/cached | Yes for original KL; optional in some β=0 variants | No |
| Separately trained RM | Common, but another reward source can replace it | No | Optional source; no removal of reward requirement | No |
| Learned value/critic | Common actor-critic PPO | No | No in original group-baseline formulation | No |

Reference predicts baseline probabilities; RM predicts preference scores; critic predicts future return. A frozen backbone with adapter disabled can implement a reference under the right initialization conditions. It is still a reference distribution.

## 3. Decision guide with realistic examples
''' + diagram('10_selection_tree') + r'''
**Only offline pairs and a capable instruction model:** DPO is a reasonable baseline. Use the detailed DPO notebook's split, formatting and PEFT workflow. With the local 20 examples, limit claims to a smoke demonstration and collect harder data before choosing a deployment checkpoint.

**Offline pairs and integrated instruction learning, with tight reference budget:** ORPO may be reasonable. Evaluate whether chosen responses are good SFT targets, choose a tested trainer environment, and monitor supervised and preference components separately. Lack of a separate reference is a resource/objective trade-off, not evidence of superior stability.

**Reliable math/test-case reward and capacity to generate groups:** GRPO is a reasonable candidate. The GSM8K notebook shows the intended interface; fix grouping and parsers first. Prefer answer equivalence/task tests over superficial format scores, and watch equal-reward groups.

**An explicit preference RM and need to optimize new policy-generated responses:** PPO RLHF is reasonable if you can budget critic, reference, scorer and rollout engineering. The source SmolLM2 demo illustrates those roles; four RM pairs do not provide an adequate scorer for broad online exploration.

**No reliable pairs or scorer:** improve SFT or collect evaluation/preference data first. Choosing a different optimizer cannot manufacture trustworthy supervision. In all cases, run small pilots on identical held-out tasks and keep resource measurements separate from illustrative estimates.

## 4. Misconceptions corrected

| Claim | Correction |
|---|---|
| DPO and ORPO are identical | DPO uses reference-relative sequence likelihoods; ORPO combines chosen NLL with same-policy normalized-likelihood odds |
| GRPO is simply PPO without a critic in every implementation | Original group advantages, sampling and KL/aggregation are specific; the recorded trainer defaults to DAPO aggregation |
| PPO always needs a separately trained RM | Game/environment rewards and rule rewards are valid; classical RLHF commonly uses an RM |
| DPO never uses a reference model | Standard DPO needs a reference distribution. Sharing/caching can avoid a second full copy |
| All four take the same dataset | DPO/ORPO use pairs; PPO/GRPO optimize rollouts from prompts and require a reward source |
| Lower loss means better alignment | Loss optimizes a proxy; evaluate independent quality, correctness and regressions |
| Increasing beta always helps | β names different coefficients in different methods; trade-offs and saturation vary |
| GRPO needs no reward | It needs a reward signal; only the separately learned critic is omitted in the original |
| Clipping keeps all probabilities in a fixed range | It caps incentive on one sample's favorable branch, not network output values |
| DPO always raises chosen probability | Source saved chosen logps fell while rejected logps fell more; relative margin improved |
| No reference means no risk of drift | ORPO lacks that anchor; data, NLL balance and independent evaluation matter |
| More response samples guarantee improvement | Extra generation may be duplicate, equally scored or reward-gaming text |

## 5. Source-specific recommended starting points

Start RL intuition with `RL_Fundamental.ipynb`, remembering the bandit/DQN/PPO boundaries. Start offline preference engineering with either 47-cell DPO notebook because their source is identical and more complete than `Final_DPO`. Use PPO for architectural study and add RM validation before scaling. Use GRPO's first path to inspect reward interfaces and its second path as a repair-required reasoning experiment. Choose exactly one ORPO dependency path in a fresh environment.

## Revision

Pick supervision first, then resource budget, then objective and implementation. Compare on the same held-out suite. No source notebook establishes one method as universally superior, safer or more efficient.
''')

chapter(9,r'''
## 1. Dependencies that actually appear

| Library/tool | Actual role in the notebooks |
|---|---|
| PyTorch | Tensors, autograd, neural models, precision and CUDA |
| Transformers/Tokenizers | Auto causal/scalar models, tokenizer/chat templates, generation |
| Datasets | JSON/external data loading, mapping, splitting and subsets |
| TRL | RewardTrainer, DPOTrainer, GRPOTrainer, experimental PPO/ORPO |
| Accelerate | Device/distributed/mixed-precision orchestration through trainers |
| PEFT | LoRA config, adapter wrapping and explicit reload |
| bitsandbytes | 4-bit NF4 model quantization and 8-bit optimizers when configured |
| Unsloth | Optimized LoRA/QLoRA and GRPO/ORPO alternative paths |
| vLLM | Fast grouped generation/LoRA inference in GRPO alternative |
| NumPy/Pandas | Seeds and DPO metric-history inspection |
| stable-baselines3/Gymnasium/Box2D/SWIG | Racing PPO demonstration and environment dependencies |
| torchao | Optional optimization package involved in recorded compatibility workarounds |
| sentencepiece | Installed tokenizer support; not explicitly used through direct import |

No training libraries were installed or model training run to produce this documentation. The source extract and external code inspection establish behavior; they do not certify a runnable current environment.

### Versions: observed outputs versus requested installs

| Notebook/path | Verifiable source evidence | What remains uncertain |
|---|---|---|
| DPO_Training | Stored PyTorch2.11.0+cu128, Transformers5.14.1, Datasets5.0.0, TRL1.8.0, PEFT.19.1 | Exact resolved full dependency tree and run provenance |
| DPO_Training_Final | Stored PyTorch2.11.0+cu128, Transformers5.14.1, Datasets5.0.1, TRL1.9.2, PEFT.20.0 | Main metrics identical to preceding notebook despite version differences |
| PPO | Stored TRL1.6.0, CUDA false; installs lower bounds | Exact remaining versions, historical loss defaults, resume semantics |
| GRPO first path | Stored TRL1.7.0 signature | Other resolved versions; second path reinstalls packages |
| ORPO standard | Requested `trl==1.9.2`; experimental imports | No printed TRL version proves resolved installation; surrounding dependencies unpinned |
| ORPO Unsloth | Requested Transformers4.56.2, TRL.22.2, Datasets4.3.0 | Unsloth/PEFT/Accelerate/bitsandbytes versions and successful execution unverified |
| Final_DPO, RL fundamentals | Unpinned installs | Resolved release versions not established |

A stored warning says `torch_dtype` is deprecated in that environment in favor of `dtype`; historical releases use `torch_dtype`. Another warning reports `warmup_ratio` deprecation. Record the environment and check signatures rather than mechanically replacing keywords across versions. Current docs and the ORPO source show experimental movement; historical API locations are not stable.

Executable inspection in a **selected training environment**:

```python
import inspect
import importlib.metadata as metadata
for package in ("torch", "transformers", "datasets", "trl", "accelerate", "peft"):
    print(package, metadata.version(package))
from trl import DPOConfig, DPOTrainer, GRPOConfig
print(inspect.signature(DPOConfig))
print(inspect.signature(DPOTrainer))
print(inspect.signature(GRPOConfig))
```

For experimental PPO/ORPO imports, use the module path confirmed in that installed release. Do not combine the two ORPO environments in one runtime. Freeze a successfully tested complete environment after the smoke check; this knowledge base does not invent a guaranteed requirements lock.

## 2. End-to-end workflow grounded in these sources

1. Parse and validate the actual local data. Keep original hashes and reject malformed rows.
2. Deduplicate/group related prompts, then create training/validation/test splits. The one-row DPO validation is pedagogical, not sufficient model selection.
3. Select a base model and exact revision. Source choices include Qwen2/Qwen2.5 .5B and SmolLM/SmolLM2 135M; their templates/vocabularies differ.
4. Load the matching tokenizer; check EOS/PAD IDs, embedding vocabulary size, precision support and chat template.
5. Build pairs for DPO/ORPO/RM or prompt metadata for PPO/GRPO. Never transfer external UltraFeedback score fields to the local JSONL by assumption.
6. Choose the objective and explicit version-compatible configuration. Verify reference behavior or reward function before constructing a long run.
7. Inspect token lengths, truncation, completion labels, attention masks and the trainer's actual collated batch.
8. Run one small forward/backward step. Check finite loss/gradients, nonzero supervised tokens and correct trainable parameters.
9. Evaluate the unmodified baseline on a fixed task suite. Save decoding settings and a disjoint preference evaluation.
10. Train with logs, periodic checkpoints and sample inspection. Stop on independent quality/regression evidence, not just loss.
11. Save adapter/model, tokenizer/template, config and full resume state when required.
12. Reload in a fresh process and compare generations with the baseline under the same sampling settings.
13. Record seed, data hash/split, model revision, environment, objective/coefficients, reward definition and measured resource use.
''' + diagram('11_end_to_end') + r'''
## 3. Reusable data transformations using verified fields

Executable when `datasets` is installed; run from the source directory:

```python
from datasets import load_dataset
pairs = load_dataset("json", data_files="reward_preferences_dataset.jsonl", split="train")
assert set(pairs.column_names) == {"prompt", "chosen", "rejected"}

def conversational(row):
    return {
        "prompt": [{"role": "user", "content": row["prompt"]}],
        "chosen": [{"role": "assistant", "content": row["chosen"]}],
        "rejected": [{"role": "assistant", "content": row["rejected"]}],
    }
chat_pairs = pairs.map(conversational)
rollout_prompts = pairs.remove_columns(["chosen", "rejected"])

# This intentionally creates NEW metadata for the heuristic GRPO demo.
def add_demo_reference(row):
    return {"prompt": row["prompt"], "reference_answer": row["chosen"]}
demo_grpo = pairs.map(add_demo_reference, remove_columns=pairs.column_names)
```

These are transformations, not evidence that the local file was used by the active source notebooks. For RM, construct full chosen/rejected conversations including prompt context. For externally downloaded complete conversations, verify shared histories before splitting the final answer off:

```python
def split_conversation_pair(row):
    chosen, rejected = row["chosen"], row["rejected"]
    if len(chosen) < 2 or len(rejected) < 2:
        raise ValueError("Require history and final answer")
    if chosen[:-1] != rejected[:-1]:
        raise ValueError("Chosen/rejected prompt histories differ")
    if chosen[-1]["role"] != "assistant" or rejected[-1]["role"] != "assistant":
        raise ValueError("Final role must be assistant")
    return {"prompt": chosen[:-1], "chosen": [chosen[-1]], "rejected": [rejected[-1]]}
```

This check addresses an omission in ORPO's `format_preference_example`; it is meant for conversational external rows, not local plain strings.

## 4. Tokenization, boundary and mask inspection

Executable with a selected tokenizer already loaded:

```python
messages = [{"role": "user", "content": "What is AI?"}]
prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(repr(prompt_text))
answer = "AI is the ability of machines to perform tasks that usually require human intelligence."
full_text = tokenizer.apply_chat_template(
    messages + [{"role": "assistant", "content": answer}],
    tokenize=False, add_generation_prompt=False,
)
prompt_ids = tokenizer(prompt_text, add_special_tokens=False)["input_ids"]
full_ids = tokenizer(full_text, add_special_tokens=False)["input_ids"]
print("prompt length", len(prompt_ids), "full length", len(full_ids))
print("prefix equality", full_ids[:len(prompt_ids)] == prompt_ids)
print(tokenizer.convert_ids_to_tokens(full_ids[-12:]))
```

If prefix equality fails, do not assume a loss boundary by independent string length; inspect tokenizer merges and the trainer's supported boundary logic. The compact DPO prototype has exactly this kind of warning. Some templates/versions can return assistant token masks; verify support before relying on them.

For a trainer-collated batch, print key names and shapes first. Different releases expose labels versus explicit completion masks differently. Inspect active tokens and decode the scored answer region:

```python
batch = next(iter(trainer.get_train_dataloader()))  # Trainer must already exist.
print({k: tuple(v.shape) for k, v in batch.items() if hasattr(v, "shape")})
# For a label-based causal batch, adapt prefix keys to the observed schema.
if "labels" in batch:
    labels = batch["labels"]
    valid = labels != -100
    assert valid[:, 1:].sum(1).min().item() > 0
    assert not (valid & ~batch["attention_mask"].bool()).any()
```

For DPO/ORPO keys such as chosen labels, apply the same checks to each side only after observing actual keys. Generation-oriented GRPO/PPO data loaders may initially contain prompts, so rollout masks are inspected at the trainer rollout stage instead. Do not present one loader schema as universal.

## 5. Sequence log-probability calculation

The reusable [tensor helpers](assets/tensor_patterns.py) contain this executable PyTorch pattern. It calculates standard completion-summed logps; set `average=True` for the normalized score needed by ORPO. Inputs have logits `[B,L,V]`, input IDs `[B,L]`, completion mask `[B,L]`, attention mask `[B,L]`.

```python
import torch
import torch.nn.functional as F

def completion_logps(logits, input_ids, completion_mask, attention_mask, average=False):
    if logits.shape[:2] != input_ids.shape:
        raise ValueError("Logit/input shapes disagree")
    if completion_mask.shape != input_ids.shape or attention_mask.shape != input_ids.shape:
        raise ValueError("Mask shapes disagree")
    target_ids = input_ids[:, 1:]
    if target_ids.numel() and (target_ids.min() < 0 or target_ids.max() >= logits.shape[-1]):
        raise ValueError("Token ID outside output vocabulary")
    # A target token needs an active prediction context and active target.
    valid = (completion_mask[:, 1:].bool() & attention_mask[:, 1:].bool()
             & attention_mask[:, :-1].bool())
    count = valid.sum(-1)
    if (count == 0).any():
        raise ValueError("Empty scored completion after shift/truncation")
    selected = F.log_softmax(logits[:, :-1].float(), dim=-1).gather(
        -1, target_ids.unsqueeze(-1)
    ).squeeze(-1)
    total = selected.masked_fill(~valid, 0.0).sum(-1)
    return total / count if average else total
```

This helper assumes input IDs are valid padded token IDs rather than −100 labels; full causal attention and correct position IDs are the model's responsibility. The shifted previous-attention check avoids scoring a target from a padded predecessor. Full FP32 log-softmax can be memory intensive; production trainers may use selective/fused log-softmax. A reference forward must disable gradients and reproduce the same deterministic scoring conditions.

## 6. Finite loss, seeds, metrics and checkpoints

Executable fragments with an existing model/optimizer/trainer:

```python
import random
import torch
random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(42)
if not torch.isfinite(loss).all():
    raise FloatingPointError("Nonfinite loss: inspect inputs, masks and reward scale")
loss.backward()
for name, param in model.named_parameters():
    if param.grad is not None and not torch.isfinite(param.grad).all():
        raise FloatingPointError(f"Nonfinite gradient: {name}")
# For FP16 GradScaler, unscale before checking/clipping gradients.
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
optimizer.zero_grad(set_to_none=True)
```

A norm of 1.0 is an example, not universally best. Log finite loss, gradient norm and component metrics by optimizer step. DataFrame missing values can mean an evaluation event lacks training columns, as in the DPO source history; inspect event dictionaries before diagnosing NaNs.

Saving example with all generated experiment outputs kept under this knowledge base:

```python
from pathlib import Path
run_dir = Path("RLHF_COMPLETE_NOTES/assets/experiments/my_run")
run_dir.mkdir(parents=True, exist_ok=True)
trainer.save_model(str(run_dir))
tokenizer.save_pretrained(str(run_dir))
trainer.save_state()
# Verify that args.output_dir also points under run_dir before training.
# When supported and a FULL checkpoint exists:
# trainer.train(resume_from_checkpoint=str(run_dir / "checkpoint-20"))
```

`save_state()` alone is not a complete optimizer checkpoint; periodic Trainer checkpoints should retain optimizer/scheduler/RNG when resume is needed. Checkpoint names and resume support differ for experimental/custom trainers. A LoRA adapter must reload with its correct base revision and tokenizer; optimizer state is irrelevant for inference but essential for faithful resume.

Seed reproducibility is conditional on versions, data order, distributed operations and sampling kernels. Record all of them. Training loss curves without data/config provenance are insufficient experiment records.

## 7. Resource planning with stated assumptions

Let P be parameter count and b bytes per parameter. Weight storage is approximately P×b, excluding quantization metadata and runtime overhead. A 0.5B model's 16-bit weights are roughly 1GB in decimal units; 135M gives roughly .27GB. Nominal 4-bit storage is P×.5 bytes plus scale/metadata; loading, activations and adapters make total VRAM substantially larger.

For a full-parameter Adam mixed-precision setup, an illustrative accounting is 2 bytes low-precision weights + 2 bytes gradients + 4 bytes master weights + 8 bytes FP32 moments≈16 bytes per trainable parameter, or about8GB for .5B **before activations**. Optimizer implementations and distributed sharding change this. LoRA largely reduces trainable gradient/moment storage, but the base weights and forward activations remain.

| Choice | Main impact |
|---|---|
| Longer sequences | More activations/KV cache; naive attention can scale quadratically, memory-efficient attention alters materialization |
| Larger microbatch | More simultaneous pair/rollout activations |
| Gradient accumulation | Larger effective batch with lower microbatch peak; still changes step/noise dynamics |
| DPO separate reference | Extra weights and no-grad forward; sharing/caching can reduce this |
| PPO critic | Trainable critic weights, gradients, optimizer and activations |
| GRPO group G | More generated tokens/cache and scorer work per unique prompt |
| Mixed precision | Reduces many tensors; some reductions/log-odds/optimizer states stay FP32 |
| Checkpointing | Lower activation memory at extra forward recomputation |
| LoRA/QLoRA | Lower optimizer/trainable storage; pair/rollout activation cost remains |
| Longer generation | More sequential rollout compute and KV cache; may hide final answer via truncation |

Measure actual peak allocation and wall time on a small pilot. Compare **unique prompts**, generated responses, scored tokens and optimizer steps separately. GRPO batch4 with G4 can represent fewer unique prompts than four; do not equate candidate count with prompt count. `device_map="auto"` can dispatch model weights but does not by itself make a distributed training configuration correct.

## Revision

Use actual schema and actual trainer version; inspect masks before updates; measure finite losses, independent evaluation and resource use; save/reload the correct adapter/base/tokenizer. The source notebooks provide patterns and pitfalls, not a version-independent training recipe.
''')

chapter(10,r'''
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
''')

questions = [
('Beginner','What is RLHF?','A workflow that uses human feedback to improve a policy, commonly by fitting a reward model from comparisons and optimizing an LLM with PPO.','Feedback supplies a proxy for preferred behavior. RLHF is broader than one four-model architecture; distinguish the classical PPO pipeline from offline preference methods.','Human feedback guarantees a perfectly aligned model.'),
('Beginner','How does SFT differ from RLHF?','SFT imitates demonstrated responses; classical RLHF optimizes feedback-derived reward on generated responses.','SFT minimizes chosen-token NLL. RLHF can compare multiple plausible answers through a reward proxy. SFT can teach safety/tone when demonstrations contain them; it simply lacks an explicit pairwise rejection term.','SFT cannot learn any preferences or safety behavior.'),
('Beginner','What is a policy?','A rule or distribution for selecting an action from a state; an LLM policy gives next-token probabilities conditional on the prompt and prefix.','πθ(a|s) has trainable parameters θ. Greedy decoding makes action selection deterministic but does not erase the underlying probability model.','The policy is the reward function.'),
('Beginner','What is a reward model?','A model that assigns a scalar score to a prompt-response pair, often trained to rank chosen answers above rejected ones.','A scalar head on a transformer can learn −logσ(rw−rl). Pairwise scores have prompt-dependent additive ambiguity and need held-out validation.','The output score is calibrated absolute truth.'),
('Beginner','What are chosen and rejected responses?','Two candidate responses to the same prompt, ordered by the annotation preference.','Chosen is preferred within that pair, not necessarily ideal in every respect. The local dataset encodes labels through its chosen/rejected fields and has no numeric scores.','Rejected always means factually false, or a separate label field exists here.'),
('Beginner','What is a reference policy for?','It provides a fixed baseline distribution for regularization or reference-relative preference scoring.','PPO RLHF commonly penalizes drift from it; standard DPO uses its chosen/rejected logps. An adapter-disabled base or cached scores can implement this role under the right conditions.','No separate model copy means no reference exists.'),
('Beginner','What is KL divergence?','An asymmetric measure of distribution difference: DKL(p||q)=Σ p log(p/q).','It averages a log ratio under p, is nonnegative in expectation, and is zero for equal distributions. A single sampled log ratio may be negative.','KL is symmetric or is always nonnegative for every sampled log ratio.'),
('Beginner','What is an advantage function?','Aπ(s,a)=Qπ(s,a)−Vπ(s): the action’s expected return relative to the policy’s average in that state.','Positive advantage encourages that action in policy-gradient learning. Estimates such as GAE or group normalization are noisy training signals, not exact true advantages.','Advantage always equals immediate reward minus value.'),
('Beginner','How do reward and return differ?','Reward is one feedback value; return sums discounted future rewards.','For rewards [0,0,10] and γ=.9, initial return is8.1. A terminal response score may be one reward in a sequence with intermediate KL shaping.','Return is the critic prediction rather than the target it estimates.'),
('Beginner','How do agent, state and action map to an LLM?','The model is the agent; prompt plus generated prefix is the state; the next token is the action.','Appending the token transitions to a longer prefix. EOS or a stopping rule ends the episode, and scoring can occur per token or at the response level.','Language-model actions are continuous because text is complex.'),
('Beginner','What is an MDP and the Markov property?','An MDP specifies states, actions, transition probabilities, rewards and initial-state distribution; the current state summarizes relevant history for the next transition.','Velocity must be included if position alone is insufficient in a game. Full visible prefix is a convenient state for autoregressive generation, but hidden external context can complicate the model.','Every arbitrary observation is automatically Markov.'),
('Beginner','What is the critic, and how is it different from the RM?','The critic predicts future return from a prefix; the RM scores a completed response’s preference quality.','The PPO notebook initializes both from rm_out, then freezes reward_model and trains value_model to rollout targets. Same starting checkpoint does not imply the same objective.','RM and critic are synonyms.'),
('Intermediate','How does PPO work in classical RLHF?','Collect fresh-policy responses, score and KL-shape rewards, estimate advantages/returns, and update actor and critic with clipped policy and value losses.','Stored old logps define the behavior denominator; the frozen reference anchors behavior separately. PPOTrainer in the supplied notebook owns this loop.','The notebook implements its own GAE tensors by hand.'),
('Intermediate','Why does PPO use clipping?','To cap further surrogate benefit from an overly large beneficial action-probability ratio change.','With A>0 and ε=.2, ratio1.5 contributes1.2A on the minimum branch. Harmful-direction changes remain penalized; shared network weights may still move probabilities beyond the interval.','Clipping hard-limits all weight updates or rewrites probabilities.'),
('Intermediate','What is GAE?','A discounted weighted sum of TD residuals: Ât=Σl(γλ)^lδt+l.','δt=Rt+γVnext−Vcurrent with termination handling. λ trades shorter bootstrap estimates against longer, typically higher-variance estimates; raw Â plus old V can form critic targets.','GAE is simply reward normalization.'),
('Intermediate','Why does PPO commonly use a critic?','A learned state-value baseline reduces variance and supports token-level advantage/return estimation.','An action-independent baseline does not change the expected policy gradient because Σπ∇logπ=0. A poor critic can bias bootstrap estimates and destabilize training.','The critic supplies the human preference label.'),
('Intermediate','Why do log probabilities appear in policy gradients?','The identity ∇p=p∇logp lets us estimate a probability-dependent reward gradient from sampled trajectories.','The trajectory log likelihood is a sum of action logps. Weighting ∇logπ by a detached return or advantage gives a score-function estimator without differentiating through the reward scorer.','Log is only used to make displayed numbers smaller.'),
('Intermediate','What is importance sampling in PPO?','Reweight old-policy actions by current/old action probability at the stored state.','ρ=exp(ℓcurrent−ℓold) motivates Eold[ρÂ]. This local surrogate does not exactly repair a changed state distribution, and extreme ratios raise variance.','Current/reference probability is the PPO clip ratio.'),
('Intermediate','How does DPO optimize offline pairs?','It minimizes negative log sigmoid of the β-scaled chosen-minus-rejected policy/reference log-ratio difference.','A latent reward can be reparameterized by an optimal KL-regularized policy. Pairwise reward differences cancel the prompt-only normalization and permit direct policy fitting.','DPO labels generated rollouts with an explicit learned RM.'),
('Intermediate','Why does standard DPO still use a reference?','The reward–policy correspondence is expressed relative to a fixed reference distribution and carries KL-regularized optimization structure.','Reference scoring can be separate, shared through adapters, or precomputed for exact pairs. Removing all reference terms changes the standard objective.','ref_model=None proves reference-free training.'),
('Intermediate','How do you compute a response log probability?','Sum selected next-token log probabilities over response tokens, with prompt and padding excluded.','Shift logits to predict token j+1 from position j. Standard DPO uses summed completion logps; ORPO’s odds score uses completion means. Changing aggregation changes the objective.','Average and sum are interchangeable for variable-length answers.'),
('Intermediate','Why do chat templates and masks matter?','They determine the conditioning context and exactly which tokens the loss scores.','Duplicate special tokens, unequal pair histories or boundary merges can move the completion boundary. Attention masks and loss masks have different purposes. Final_DPO stores a prompt-prefix mismatch warning.','A mask error only changes efficiency.'),
('Intermediate','What is GRPO group normalization?','For each prompt, subtract its group mean reward and divide by group standard deviation, with numerical handling as needed.','Rewards [1,0,1,0] give mean .5 and population std .5, hence advantages [1,−1,1,−1]. Outcome advantages are broadcast over response tokens.','Only mean subtraction fully describes original normalized GRPO.'),
('Intermediate','Does GRPO require a reward model?','It requires a reward signal; that signal can come from rules, tests, human/judge feedback or a learned model.','The first notebook path uses similarity/style functions; the original DeepSeekMath paper also uses learned reward models. Removing a critic does not remove scoring.','GRPO improves by comparing answers without any external criterion.'),
('Intermediate','How does ORPO combine supervised and preference loss?','Total loss is chosen-token NLL plus a weighted negative log sigmoid of the chosen/rejected normalized-likelihood log odds ratio.','The same policy supplies both scores. λ balances imitation and preference; the source configs call this coefficient beta. No separate reference is required.','ORPO is DPO with the reference terms removed and no SFT component.'),
('Intermediate','What is the difference between probability ratio and odds ratio?','Probability ratio is pw/pl; odds ratio is [pw/(1−pw)]/[pl/(1−pl)].','For .75 and .25, the probability ratio is3 but odds ratio is9. Log odds also contains log(1−p), so replacing it with a log probability changes the loss.','Odds is just another name for probability.'),
('Intermediate','How does effective batch size relate to gradient accumulation?','For ordinary data-parallel updates it is approximately microbatch×accumulation×world size; rollouts and GRPO candidate grouping add distinct constraints.','The DPO source uses1×8 on one device. GRPO candidates repeat prompts, so four candidate examples may be one prompt group. PPO also partitions rollout batches into minibatches.','All trainer batch counts mean unique prompts.'),
('Intermediate','What does LoRA save and how should it reload?','It trains low-rank adapters and saves adapter weights/configuration, which reload with the matching base model and tokenizer.','The detailed DPO notebooks use AutoPeftModelForCausalLM; GRPO uses PeftModel with an explicit base. Quantization reduces frozen base storage but does not remove activation costs.','An adapter alone contains a complete standalone model or full optimizer state.'),
('Advanced','Derive the main PPO clipped objective.','Start with the old-policy importance-ratio surrogate Eold[ρÂ], clip ρ around1, and take the minimum of unclipped and clipped advantage-weighted contributions.','For A≥0 this is min(ρ,1+ε)A; for A<0 it is max(ρ,1−ε)A. Maximization then removes additional incentive in the favorable excessive-change direction; it is a heuristic local surrogate, not a strict trust-region proof.','Take min of ratios without accounting for the sign of A.'),
('Advanced','Derive the connection between KL-regularized reward optimization and DPO.','Optimizing Eπ[r]−βDKL(π||πref) with probability normalization yields π*=πref exp(r/β)/Z. Rearrange reward and cancel βlogZ in a same-prompt Bradley–Terry comparison.','The derivative is r−β(log(π/πref)+1)+η=0. Reparameterizing with πθ produces the DPO logistic loss. Support, finite Z and preference-model assumptions must be stated.','DPO recovers one unique absolute reward function or guarantees neural training finds π*.'),
('Advanced','How should DPO beta be interpreted?','It is the KL penalty parameter in the fixed-reward derivation and scales the logistic preference margin in the training loss.','Larger β weakens reward tilt at fixed r, but also affects gradient magnitude and saturation at fixed log-ratio margin. Actual drift depends on optimization/data/reference and cannot be inferred from beta alone.','Larger beta always means a stronger useful update or always less observed KL.'),
('Advanced','How does reward hacking occur?','A policy exploits a mismatch between the optimized scorer and intended quality, producing high-scoring but poor answers.','The GRPO notebook rewards length, punctuation and avoiding uncertainty phrases, which can be gamed without semantic correctness. Evaluate with independent task tests/judgments and broaden reward coverage.','Reward hacking requires malicious intent from the model.'),
('Advanced','What happens when policy drift from the reference is large?','It may move into regions where reward/data generalization is poor and lose useful baseline behavior, although some drift is necessary for improvement.','Measure KL under clearly stated sampling conditions plus independent quality and regression tests. Increase regularization or reduce update pressure only with evidence; no universal safe KL exists.','Zero KL is the best possible aligned outcome.'),
('Advanced','Compare PPO’s value estimate with GRPO’s group baseline.','PPO predicts prefix-conditioned future return with a learned critic; GRPO derives a same-prompt empirical baseline from multiple scored responses.','A critic can model varying future prospects at each token. Outcome GRPO gives a sequence-level relative signal to tokens and avoids learned value approximation, at the cost of group generation and variance/normalization issues.','The group mean is an exact value function for every prefix.'),
('Advanced','Why can equal-reward GRPO groups fail to teach preference?','All centered rewards are zero and standard deviation is zero; stabilized normalization yields zero comparative advantage.','All-right and all-wrong groups both have this problem. A KL term can still act, and a missing numerical stabilizer can cause NaN. Improve task difficulty/diversity/scorer granularity instead of pretending std division creates information.','No critic means no zero-variance issue.'),
('Advanced','How can length bias affect these algorithms?','Annotators, reward models and loss aggregation can correlate longer answers with preference or weight long sequences differently.','Every local chosen answer is longer in characters. DPO sums logps, ORPO normalizes its odds score, and original GRPO response means differ from DAPO token means. Length-controlled evaluation and hard pairs are needed; normalization is not a universal cure.','Length normalization eliminates all preference bias.'),
('Advanced','What if chosen/rejected masks are wrong?','The objective may score prompt/padding or mismatched contexts instead of the desired responses, invalidating the preference comparison.','An empty completion can give divide-by-zero in normalized scores. Unequal prompt context breaks partition cancellation assumptions. Decode scored tokens, count masks and compare padded/unpadded logps.','The error just adds a constant and does not affect gradients.'),
('Advanced','Is the positive GRPO KL estimator automatically exact on reused rollout data?','No. q−logq−1 is nonnegative pointwise and has the desired KL expectation under current-policy action sampling with appropriate support.','Groups are collected from πold. Reuse, sampling mismatch, estimator gradients and optional bias corrections must be distinguished from the pointwise nonnegativity claim.','Positive samples guarantee an unbiased loss gradient under any data distribution.'),
('Advanced','How does ORPO’s normalized score differ from a whole-response probability?','It is the geometric mean of response token probabilities, exp(mean logp), rather than their product.','It does not sum to1 across different response candidates, so a .75/.25 illustration is not a general two-class model. ORPO applies odds to this normalized likelihood score; token-average SFT is a separate aggregation decision.','It is calibrated confidence that the whole answer is correct.'),
('Advanced','Why can DPO loss improve while both candidate likelihoods fall?','It optimizes their reference-adjusted difference, so the rejected likelihood can fall more than the chosen likelihood.','Stored chosen logp decreases from−51.20 to−58.49 and rejected from−53.96 to−77.31. The β=.1 implicit reward margin becomes≈1.61. Independent quality must determine whether that shift helped.','A chosen likelihood decrease mathematically proves DPO is implemented incorrectly.'),
('Scenario','You have only the supplied 20 preference pairs and little VRAM. What would you do?','Use a small LoRA DPO or ORPO smoke experiment after mask/schema checks, while collecting larger harder data and a disjoint evaluation set.','All winners are longer and negatives are obvious. Reference sharing can make DPO practical; ORPO reduces reference work but changes the objective. Twenty pairs cannot justify robust alignment claims.','Switch to GRPO without a scorer or claim 100% one-pair accuracy proves success.'),
('Scenario','Your PPO RM trains on four rows. Is it ready for broad online optimization?','No broad readiness is established; first evaluate rankings on diverse held-out and policy-generated responses.','The source uses one epoch without RM evaluation. Online exploration may exploit random/new scalar-head errors. More policy episodes cannot repair a poor preference proxy.','The successful save message proves the reward model is trustworthy.'),
('Scenario','The DPO log-history DataFrame contains NaNs. How would you diagnose it?','Inspect original event dictionaries and explicit finite losses/gradients before declaring numerical divergence.','Eval and final-summary events lack training fields, so Pandas fills absent columns with NaN. If actual loss is nonfinite, check masks, precision and token IDs; distinguish missing data from arithmetic NaN.','Every displayed NaN means the model weights are corrupt.'),
('Scenario','The GRPO notebook says batch must divide by G but its second path uses batch1 and G4. What would you check?','Inspect the installed effective generation batch across devices/steps and configure a supported grouping scheme.','The second path reinstalls unpinned packages and has no saved outputs. The first-path signature cannot certify its config. Per-device divisibility is not a universal rule, but default single-device1/G4 may be incompatible.','It must be valid because the notebook is named Final.'),
('Scenario','ORPO inference raises a CUDA assert after a reported training result. What next?','Restart the poisoned runtime, reproduce a tiny generation synchronously, and inspect vocabulary/token IDs, EOS/PAD config and dependency compatibility.','CUDA errors are asynchronous; the cleanup traceback can point later than the cause. The notebook has two environment paths and initial state-dependent deletes. Training output does not establish successful inference.','Always reinstall torchao or reduce beta without inspecting the failing input.'),
('Scenario','A verifiable math task has almost all wrong GRPO samples. How would you proceed?','Verify parsing/reward metadata, choose learnable difficulty, and improve sampling/model/SFT so groups contain useful differences.','If all rewards are zero, stabilized group advantages vanish. Add reliable partial credit only if it tracks desired behavior; pure format bonuses can reward wrong answers. Increase G only if compute and useful diversity justify it.','Invent random reward noise so the optimizer always has variance.'),
('Scenario','A company asks for the universally best optimizer. How would you answer?','There is no universal winner: compare supervision, fresh-answer scoring needs, generation budget, reference/critic costs and held-out task results.','Offline pairs suggest DPO/ORPO; verifiable group rewards suggest GRPO; a validated flexible RM with rollout budget can justify PPO. Source demos do not provide a controlled head-to-head benchmark.','DPO is always safest because a PDF ranks its popularity.'),
('Scenario','Can you rerun the whole ORPO notebook sequentially in one runtime?','It needs repair/separation: initial deletes depend on previous state, and standard versus Unsloth sections request different TRL environments.','Use one clean environment path, inspect its import/signatures, validate formatting and run a small batch. Do not mix experimental processing_class and older tokenizer keywords uncritically.','Pinned TRL alone guarantees every dependency and runtime state is compatible.'),
('Scenario','The racing notebook requests 100 timesteps but reports 2048. Is this fabricated?','Not necessarily: on-policy PPO collects a complete n_steps=2048 rollout, so the requested minimum is exceeded.','The saved Stable-Baselines3 output explicitly records one 2048-step iteration. This is still a tiny learning run and the reward−58.6 does not establish driving competence.','learn(total_timesteps=100) must produce exactly100 environment transitions.'),
('Scenario','Your reward-trained checkpoint initializes both RM and critic. Is that a bug?','Not inherently. Reward and value models may share initialization while training to different targets thereafter.','The PPO source freezes reward_model and leaves value_model trainable. Verify per-prefix value use, target scale and model interface; copying weights alone does not make the critic calibrated for shaped returns.','They must remain the same model forever or can never initialize from each other.')
]
qa=['## How to answer','Start with the interview-ready answer, then justify it with the assumptions or a source example. Formula details are expanded in Chapters 01–07. The questions below distinguish definitions, implementation choices and actual stored output.']
last=None
for i,(level,q,a,reason,wrong) in enumerate(questions,1):
    if level!=last:qa += ['\n## '+level];last=level
    qa += [f'\n### Q{i:02d}. {q}',f'\n**Interview-ready answer:** {a}',f'\n**Reasoning / example:** {reason}',f'\n**Common incorrect answer:** “{wrong}”']
qa += [r'''
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
''']
chapter(11,'\n\n'.join(qa))

glossary={
'RLHF':'Reinforcement learning from human feedback; commonly preference RM training followed by RL policy optimization.',
'SFT':'Supervised fine-tuning; imitation of demonstrated responses using token likelihood.',
'PPO':'Proximal Policy Optimization; clipped local policy-gradient surrogate, commonly actor-critic.',
'DPO':'Direct Preference Optimization; offline pairwise likelihood fit through policy/reference ratios.',
'GRPO':'Group Relative Policy Optimization; rollout-based same-prompt relative-reward advantages, originally without learned critic.',
'ORPO':'Odds Ratio Preference Optimization; chosen SFT plus odds-ratio preference loss without a reference model.',
'Policy':'State-conditioned action distribution; in an LLM, next-token probabilities.',
'Reference policy':'Baseline distribution fixed during standard preference/RL regularization, possibly implemented through sharing/caching.',
'Old/behavior policy':'Policy distribution that generated stored rollout actions; PPO ratio denominator.',
'Reward model':'Scalar preference scorer trained from feedback comparisons.',
'Reward signal':'Actual numeric score used by optimization, whether supplied by model, rules or environment.',
'Critic':'Learned value predictor used to estimate expected future return and advantages.',
'Value function':'Vπ(s), expected return from a state under policy π.',
'Action-value function':'Qπ(s,a), expected return after a specified first action and policy continuation.',
'Advantage':'Q−V; action return relative to policy baseline.',
'Return':'Discounted sum of future rewards along a trajectory.',
'Rollout':'Collection of sampled policy trajectories and associated training statistics.',
'Trajectory':'Ordered states/actions/rewards; an LLM generated response with prefixes.',
'Episode':'One interaction/generation until a terminal/stopping condition.',
'MDP':'Markov decision process: states, actions, transitions, rewards, initial distribution and discount.',
'Markov property':'Current state contains relevant information needed to predict next transition/reward.',
'Discount factor':'γ; controls contribution of later rewards to return.',
'Termination / truncation':'Genuine task ending versus artificial stopping/time limit; bootstrap treatment can differ.',
'KL divergence':'Asymmetric expected log-density ratio between distributions.',
'Entropy':'Expected negative log probability; a distribution uncertainty/diversity measure.',
'GAE':'Generalized Advantage Estimation; weighted sum of TD residuals.',
'TD learning':'Temporal-difference learning; uses bootstrapped future estimates in updates.',
'Monte Carlo learning':'Learning from sampled completed returns without a bootstrap target.',
'Importance sampling':'Distribution-change reweighting by target/sampling probability ratio.',
'Clipping':'PPO objective mechanism limiting further incentive for beneficial ratio changes beyond a chosen interval; distinct from gradient norm clipping.',
'Log probability':'Natural logarithm of probability; sequence log likelihood adds token log probabilities.',
'Odds ratio':'Ratio of p/(1−p) values for two candidates.',
'Log odds':'log p−log(1−p), not just log p.',
'Chosen/rejected pair':'Same-context winner and loser as encoded by preference columns.',
'Bradley–Terry model':'Logistic probability of pairwise preference from a scalar reward difference.',
'Reward hacking':'Optimizing proxy scores through behavior that fails intended quality.',
'On-policy / off-policy':'Learning mainly from current-policy trajectories versus allowing a different behavior distribution.',
'Offline / online':'Optimization from fixed data versus collecting fresh interaction/generation data in the loop.',
'Actor-critic':'Policy optimization with a value predictor supporting return/advantage estimation.',
'Q-learning / SARSA':'Value updates using greedy next action target versus policy-sampled next action target.',
'DQN':'Deep Q-network; neural action values, commonly replay and target network.',
'Exploration / exploitation':'Trying uncertain actions versus favoring currently estimated good actions.',
'Partition function':'Z(x), normalization of reference-weighted exponentiated reward in DPO derivation.',
'Implicit reward':'Policy/reference log ratio interpreted as reward up to a prompt-only constant in DPO.',
'Completion mask':'Selects response tokens scored by an objective; excludes prompt and padding.',
'Attention mask':'Identifies active tokens for attention; separate from objective scoring masks.',
'Chat template':'Model-specific serialization of user/system/assistant messages and special tokens.',
'BOS / EOS / PAD':'Beginning-of-sequence, end-of-sequence and padding token conventions.',
'Logits':'Unnormalized token scores before softmax.',
'Length-normalized likelihood':'Geometric mean of response token probabilities; used in original ORPO odds scoring.',
'Group size':'G, number of sampled answers for one GRPO prompt.',
'Zero-variance group':'Group whose rewards are identical; comparative normalized advantage is zero with stable handling.',
'Outcome / process supervision':'Reward for complete response versus intermediate reasoning steps.',
'DAPO aggregation':'Later token-weighted objective variant; recorded GRPOConfig default differs from original response-mean weighting.',
'LoRA':'Low-rank adapters updating selected layers with relatively few trainable parameters.',
'QLoRA':'Low-rank training with a quantized frozen base model, commonly 4-bit.',
'PEFT':'Parameter-efficient fine-tuning library/method category used for adapters.',
'Gradient accumulation':'Sum microbatch gradients before an optimizer step to increase effective batch.',
'Gradient checkpointing':'Recompute activations during backward to save activation memory.',
'Checkpoint':'Saved training/model state; faithful resume requires optimizer/scheduler/RNG as well as model.',
'Calibration':'Agreement between modeled scores/probabilities and observed quality or preference frequencies.',
'Length bias':'Preference/reward/objective dependence on response length beyond intended task quality.',
'Distribution shift':'Mismatch between training/scorer data and later inputs or policy-generated responses.',
'Mode collapse':'Reduced behavioral diversity such as repetitive answers across prompts.',
'Catastrophic forgetting':'Loss of previously useful abilities during later training.',
'KTO':'Kahneman–Tversky Optimization; direct alignment from desirable/undesirable judgments; mentioned, not implemented here.',
'SimPO':'Simple Preference Optimization; distinct reference-free preference method mentioned by ORPO PDF.',
'RLVR':'Reinforcement learning with verifiable rewards; reward source category, not one optimizer.',
'CoT / PoT':'Chain-of-thought / program-of-thought response styles in source DeepSeekMath discussion.',
'vLLM':'Generation engine used by source Unsloth GRPO alternative.',
'NF4':'NormalFloat4 quantization format configured in the detailed DPO QLoRA path.',
'Explained variance':'1−Var(target−prediction)/Var(target); critic diagnostic undefined for constant targets.'}
formula_entries=[
('Return',r'G_t=\sum_{k=0}^{T-1-t}\gamma^kR_{t+k}','R is reward after an action, T episode actions, γ discount.','RL/PPO','Counts future feedback from time t; terminal means no further value.'),
('Values and advantage',r'V^\pi(s)=\mathbb E[G_t|s];\quad Q^\pi(s,a)=\mathbb E[G_t|s,a];\quad A^\pi=Q^\pi-V^\pi','π policy, s state, a action.','RL/PPO','Value averages policy actions; advantage centers the chosen action.'),
('Bellman expectation',r"Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\pi(s');\quad V^\pi(s)=\sum_a\pi(a|s)Q^\pi(s,a)",'r expected immediate reward, P transition probability.','RL','Separate first reward from expected discounted future.'),
('Bellman optimality',r"Q^*(s,a)=r(s,a)+\gamma\sum_{s'}P(s'|s,a)\max_{a'}Q^*(s',a')",'Star optimal values; a′ possible next action.','Q-learning/DQN','Greedy next-state target under specified reward.'),
('TD and Q update',r"Q(s,a)\leftarrow Q(s,a)+\alpha[R+\gamma(1-d)\max_{a'}Q(s',a')-Q(s,a)]",'α update rate, d terminal flag.','Q-learning/DQN','Moves toward a bootstrap target, not certain ground truth.'),
('Policy gradient',r'\nabla J\propto\mathbb E_{s\sim d^\pi,a\sim\pi}[A^\pi(s,a)\nabla\log\pi_\theta(a|s)]','dπ normalized discounted occupancy, θ trainable actor.','Policy gradients/PPO/GRPO','Score-function estimator; occupancy normalization determines constant.'),
('Importance ratio',r'\rho_t=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}=e^{\ell_{\theta,t}-\ell_{old,t}}','ℓ selected action logp, old frozen behavior distribution.','PPO/GRPO','Weights new likelihood on old actions; reference is a different role.'),
('Entropy and KL',r'H(p)=-\sum_a p(a)\log p(a);\quad D_{KL}(p\|q)=\sum_a p(a)\log\frac{p(a)}{q(a)}','p target policy distribution, q supported baseline.','RL regularization','Entropy describes uncertainty; KL describes asymmetric drift.'),
('GAE',r'\delta_t=R_t+\gamma(1-d_t)V_{old}(s_{t+1})-V_{old}(s_t);\quad \hat A_t=\delta_t+\gamma\lambda_{GAE}(1-d_t)\hat A_{t+1}','λGAE residual weighting; d genuine terminal.','PPO','Mixes short and long credit estimates; targets detached.'),
('Value loss',r'\hat G_t=\hat A_t^{raw}+V_{old}(s_t);\quad \mathcal L_V=\tfrac12\mathbb E[(V_\phi(s_t)-\hat G_t)^2]','φ critic parameters; raw advantage before actor normalization.','PPO','Fits predicted return to rollout target; optional value clipping differs.'),
('PPO surrogate',r'L^{CLIP}=\mathbb E[\min(\rho\hat A,\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)\hat A)]','ε clip width; Â fixed rollout advantage.','PPO','Maximize this; minimizing actor loss negates it. No hard update bound.'),
('One possible total PPO loss',r'\mathcal L=-L^{CLIP}+c_V\mathcal L_V-c_HH+\kappa_{explicit}D_{KL}','cV value weight, cH entropy weight, κ explicit KL if used.','PPO variant','Library-specific; avoid unintended KL duplication with shaped rewards.'),
('RM comparison',r'P(y_w\succ y_l|x)=\sigma(r_\psi(x,y_w)-r_\psi(x,y_l));\quad \mathcal L_{RM}=-\mathbb E\log P','ψ RM parameters, x shared prompt, yw/yl preferred/less preferred.','RM/DPO derivation','Logistic pairwise utility model; prompt additive constants cancel.'),
('DPO optimal policy',r'\pi^*(y|x)=\frac{\pi_{ref}(y|x)e^{r(x,y)/\beta}}{Z(x)};\quad Z(x)=\sum_y\pi_{ref}(y|x)e^{r(x,y)/\beta}','β>0 KL penalty; finite Z, reference support required.','DPO derivation','Exponential reward tilt of reference, not guaranteed neural optimum.'),
('Implicit reward',r'\hat r_\theta(x,y)=\beta\log\frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)}','Reward defined up to c(x); true derivation includes βlogZ.','DPO','Relative policy promotion acts as latent preference utility.'),
('DPO loss',r'\mathcal L_{DPO}=-\mathbb E\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right)','θ current policy, β scale, reference fixed, responses use completion-summed logps.','DPO','Fit reference-adjusted pair margin; chosen absolute likelihood can fall.'),
('Group advantage',r'\mu=\frac1G\sum_iR_i;\quad s=\sqrt{\frac1G\sum_i(R_i-\mu)^2};\quad\hat A_{i,t}=\frac{R_i-\mu}{s+\varepsilon_{norm}}','G responses per prompt; practical εnorm; sample/population std conventions vary.','Outcome GRPO','Within-prompt relative signal; all equal rewards yield zero with stable handling.'),
('Original GRPO objective',r'J=\mathbb E\left[\frac1G\sum_i\frac1{T_i}\sum_t\left(\min(\rho_{i,t}\hat A_{i,t},\operatorname{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)\hat A_{i,t})-\kappa_{GRPO}\hat K_{i,t}\right)\right]','Ti active response length; κGRPO explicit KL coefficient.','Original GRPO','Response/group mean weighting differs from later token-mean defaults.'),
('Positive KL estimator',r'q=\pi_{ref}(a|s)/\pi_\theta(a|s);\quad\hat K=q-\log q-1','q reference/current ratio, expectation claim under current-policy action sampling.','Original GRPO','Nonnegative pointwise; reused old-policy samples require care.'),
('Sequence scoring',r'\ell=\sum_tm_t\log\pi_\theta(y_t|x,y_{<t});\quad\bar\ell=\ell/\sum_tm_t;\quad p=e^{\bar\ell}','mt completion mask; nonempty active targets required.','DPO sum; ORPO mean','p is geometric mean, not a normalized distribution over full responses.'),
('ORPO odds',r'\operatorname{odds}(p)=\frac p{1-p};\quad\Delta_{OR}=\log\frac{p_w/(1-p_w)}{p_l/(1-p_l)}','pw/pl normalized completion likelihood scores, strictly between0 and1.','ORPO','Log odds includes complement probability; distinguish probability ratio.'),
('ORPO total',r'\mathcal L_{ORPO}=\mathcal L_{SFT}+\lambda_{OR}\left[-\mathbb E\log\sigma(\Delta_{OR})\right]','λOR balances components; source TRL calls it beta; chosen NLL usually token averaged.','ORPO','Imitation and preference in one objective without a reference.'),
('Logistic loss identity',r'-\log\sigma(z)=\operatorname{softplus}(-z)','z RM reward difference, DPO margin or ORPO log-odds difference.','RM/DPO/ORPO','Stable way to compute preference loss; different methods supply different margins.')]
gtext=['## Glossary','| Term | Definition |','|---|---|']+[f'| {k} | {v} |' for k,v in glossary.items()]
gtext += ['\n## Formula cheat sheet','All logs are natural. Rewards use R, ratios use ρ, and coefficients are distinguished by algorithm. Equations assume the stated masks/support/terminal handling; implementation variants belong in their algorithm chapter.']
for title,formula,symbols,alg,intuition in formula_entries:
 gtext += [f'\n### {title}',f'\n$$\n{formula}\n$$',f'\n**Calculates / used in:** {alg}. **Symbols:** {symbols} **Interpretation:** {intuition}']
gtext += [r'''
## Five-minute final comparison

| Method | Essential supervision | Core calculation | Typical extra roles | First debugging checks |
|---|---|---|---|---|
| PPO RLHF | Prompts plus scorer for fresh rollouts | Clipped advantage-ratio surrogate + critic loss | Reference, RM/function, critic | Old/reference distinction, shaped rewards, GAE, masks |
| DPO | Offline chosen/rejected pairs | −logσ(β×relative log-ratio margin) | Fixed reference scoring | Shared context, summed completion logps, ref frozen |
| GRPO | Prompts plus group scorer | Group-normalized advantages and policy objective | Reference in original; optional RM | Group size/batch, reward std, parser, aggregation variant |
| ORPO | Offline chosen/rejected pairs | Chosen NLL + λ×odds comparison loss | No separate reference/RM/critic | Mean logps, log(1−p) numerics, NLL balance |

**Do not confuse:** PPO old policy with reference; RM with critic; DPO β with ORPO coefficient; true sequence probability with ORPO normalized score; observed source output with newly measured results.

**Source anchors:** detailed DPO notebook cells23–31; PPO cells14–20; GRPO first path cells24–32 and second path42–51; ORPO cells13–17 and25–29. See [notebook audit](assets/source_audit/NOTEBOOK_AUDIT.md) for every cell and [inventory](SOURCE_INVENTORY.md) for all sources.
''']
chapter(12,'\n\n'.join(gtext))

write('README.md',r'''
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
''')

write('EXTERNAL_REFERENCES.md',r'''
# External references and verification record

The supplied sources are primary evidence about local code and teaching examples. External references verify algorithm definitions and clarify mistakes. Retrieval took place during this documentation build on 2026-10-11. [HTTP verification](assets/references/verification.json) and [additional retrieval results](assets/references/verification_extra.json) record statuses. Retrieved content is retained under assets/references for audit; no external decorative imagery is used.

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
''')

write('CORRECTIONS_AND_LIMITATIONS.md',r'''
# Corrections, source traceability and remaining limits

No original was edited. “Correction” below means the generated notes repair or qualify the source statement. Cell numbers are1-based source JSON order; pages are PDF page order.

| Source location | Source issue or ambiguity | Correction / interpretation | Chapter |
|---|---|---|---|
| Root README, reference-free section | DPO grouped under “Reference-Free” | Standard DPO uses a reference distribution; sharing/caching can remove a separate copy | 02,05,08 |
| RL_Fundamental cells2–5 | Immediate-reward Q dictionary called RL/Q learning generally | Stateless bandit-like estimate, no next state/future term; random loop never turns greedy; cell5 repeats last update | 01 |
| RL_Fundamental cells9–17 | Dummy DQN batch | Core update only; no real transitions/replay/epsilon-greedy/periodic target sync | 01 |
| RL_Fundamental cells24–25 | Requested100 steps with n_steps2048 | Stored run collected2048; tiny budget not learned-driving evidence | 01,11 |
| RLHF PDF pp12–14 | “No teacher/no labels” and rigid taxonomy | RL uses designed feedback; RL is an ML paradigm and can use neural networks; SFT also learns behavioral values | 01,02 |
| RLHF PDF pp23,25–28 | Target treated as correct ground truth; simple loss=target−prediction | Bootstrap target is estimate-dependent; DQN notebook uses MSE (40.96 in grid example) | 01 |
| RLHF PDF pp29–31 | DQN continuous limitation used as LLM rationale | LLM tokens are discrete; policy optimization fits pretrained LM distribution, not because actions are continuous | 01 |
| RLHF PDF pp30–36,44–45 | Advantage=reward−value; clipping phrased as bounding update | Valid one-step illustration; canonical GAE uses future shaped rewards. Surrogate caps incentive, not weights/probabilities globally | 01,04 |
| RLHF PDF pp4,8,42 | Alignment ensures safe behavior; PPO never uses direct humans | Intended goal, not guarantee; classical notebook uses RM, general PPO may use many reward sources | 02,04 |
| DPO PDFs various score explanations; final pp9–17 | Chosen likelihood↑, rejected↓ asserted as overall effect | Relative margin is optimized; source saved chosen and rejected logps both fall | 05,10 |
| DPO updated p11; old p17 | Rewards8/3 and108/103 | Useful additive-offset example retained; pairwise utility depends on difference | 03,05 |
| DPO final p14 | Sigmoid≈.9526 described as confidence | Model-based comparison probability/score under link assumptions, not calibrated quality confidence | 05 |
| DPO PDFs implicit reward tables | Reward described as probability ratio | Correct βlog(policy/reference) up to prompt-only constant; missing conditioning made explicit | 05 |
| DPO_Training and DPO_Training_Final | Filenames suggest separate implementations | All47 source cells identical; recorded versions differ; exact matching metrics are not independent reproducibility evidence | 05,09 |
| Detailed DPO cell24 Markdown | ref_model=None described as initial model generically | PEFT adapter-disabled base is correct only when it represents intended initial reference; existing SFT adapter may need preservation | 05 |
| Detailed DPO stored cell11 | T4 BF16=True | Verify native capability versus API emulation; do not treat saved support flag as native BF16 hardware proof | 05,09 |
| Final_DPO cells1,5,6 | Displayed pairs not assigned; local loader commented | Active dataset is downloaded full UltraFeedback, not inline or local JSONL | 05 |
| Final_DPO cells8,10 | BF16 on any CUDA, FP16 on CPU; model FP16 separate from flags | Use supported precision branches; full dataset/no eval/interrupt do not establish complete training | 05 |
| Final_DPO stored cell11 | Prompt token mismatch warnings | Inspect shared template and full token boundary; do not dismiss warning | 05,09 |
| PPO cells6–8 | Commented local JSONL loader | Default uses four inline rows; real local data loading requires explicit path/config | 03,04 |
| PPO cells15–16 | RM and value copy both initialized rm_out | Valid possible initialization, different subsequent objectives; reward frozen, critic trainable | 02,04 |
| PPO cells17,22 | Filtering after truncation; cache clear with live objects; full-sequence decode | Measure original lengths; release references before reload; slice newly generated tokens | 04,09 |
| PPO stored cell20 | Singleton variance warning | Could affect metric variance; not proof of a nonfinite training objective | 04,10 |
| GRPO PDF pp4,8 | Centered reward called advantage without std division | Preserve centered illustration and add original normalized advantage; define std convention | 06 |
| GRPO PDF pp7,9–11 | “Why better” and RM absent | No universal superiority; reward signal required, original paper can use learned reward models | 06,08 |
| GRPO cell24 | Correctness named for text similarity/keyword recall | Lexical heuristic, not semantic correctness; missing metadata silently returns zeros | 06 |
| GRPO cells25–26 | Punctuation/length and uncertainty penalties | Reward-gaming and anti-calibration risks; independent tests needed | 06,10 |
| GRPO cells29,31 | Claimed generic divisibility; loss_type omitted | Effective grouping is release-dependent; saved1.7 signature default is DAPO aggregation | 06 |
| GRPO second cells43–49 | Naive answer extraction, isdigit, batch1/G4 | Equivalent numbers can fail; signed/decimal valid answers penalized; grouping requires repair/verification | 06 |
| ORPO PDF pp11–16 | Sequence probability and odds lack normalized likelihood explanation | Paper uses geometric-mean completion likelihood in odds; not a full-response calibrated distribution | 07 |
| ORPO PDF pp12–15 | Rounded .288/.105 total .2985 | Unrounded toy total .298218 at coefficient .1; arithmetic/notation clarified | 07 |
| ORPO PDF pp8–9,17 | Universal memory/adoption/safety claims and7B scope | Memory conditional on loading; no universal safety ranking; original validation scope not size limit | 07,08 |
| ORPO cell1 | State-dependent deletion before imports | Clean-run repair needed; saved CUDA error may be asynchronous from earlier operations | 07,10 |
| ORPO cells4,19,27–28 | TRL1.9.2 experimental versus .22.2 top-level paths | Separate environments; check signatures/patch compatibility, do not run install sections interchangeably | 07,09 |
| ORPO cell25 | Extracts chosen history without rejected-history/role validation | Compare both histories and final roles; consistent prompt is mandatory | 07,09 |
| ORPO stored cells1,17 | CUDA device-side asserts | Successful end-to-end inference not established; restart and reproduce with ID/version checks | 07,10 |

## Extraction and validation limits

All137 PDF page images were reviewed. Raster PDFs lack embedded text; OCR is an auxiliary imperfect transcript and cannot be trusted for equations. Several source pages are blank (see ledger). Small text in embedded screenshots/infographic decorations and a few handwritten fragments cannot be transcribed exactly; no missing symbol was guessed and presented as a source fact. Major equations/examples were reconstructed against papers and readable page context. Original rendered pages remain available for reinspection.

All247 notebook cells were parsed and read, including Markdown, commented alternatives and outputs. Extracts retain all text/HTML outputs and PNG plots, but no notebook was executed. Stored outputs may be stale, copied or from multiple environments; exact execution provenance cannot be guaranteed. The second GRPO and second ORPO paths have no stored execution outputs. Their source definitions can be analyzed without claiming success.

The local dataset is20 clean string pairs with a marked character-length correlation; annotation provenance, confidence, token lengths and generalization were not established. Exact historical trainer defaults beyond printed signatures were not reproduced; current upstream code is version-labeled verification context. Some current PPO endpoints are unavailable/fallbacks. These limits are reported rather than hidden as “complete verification.”
''')
