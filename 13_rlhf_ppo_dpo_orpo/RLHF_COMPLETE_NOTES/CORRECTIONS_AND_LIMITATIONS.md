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


## Math rendering repair — 2026-10-11

Recursive inspection included every Markdown file under `13_rlhf_ppo_dpo_orpo/`, including source-audit extracts and third-party tooling documentation. The final parser inspection covers 320 Markdown files after adding local validation dependencies. Only eight learning chapters contained actual legacy display equations: 01,02,03,04,05,06,07 and12. All65 display equations now use `$$` delimiter lines with blank paragraph boundaries. Inline equations use `$...$`. No formulas in tables/lists/code required delimiter migration; escaped vendor array brackets, URL parentheses, currency and literal LaTeX examples were preserved.

**Substantive clarification:** Chapter01's TD residual previously used a generic critic `V_phi`, while its return target used `V_old`. Both now explicitly use the same frozen rollout-time critic `V_old = V_phi_old` before optimization. This resolves a potential implementation mismatch; numerical examples and canonical PPO/GRPO/DPO/ORPO objectives are unchanged. The other64 formula bodies were preserved exactly, and conversion checks confirmed all65 bodies unchanged before this documented clarification. Code/literal spans were preserved.

**Validation:** GitHub-compatible Markdown parsed with remark-parse, remark-gfm and remark-math. KaTeX0.16.47 strictly rendered all65 display and5 inline expressions with zero errors. Delimiters pair correctly, block spacing passes, and no malformed braces/unknown commands were found. PPO clipping, DPO partition-function cancellation and implicit reward, GRPO normalization/KL, ORPO geometric likelihood/odds, reward/critic roles, TD residual, GAE and raw return targets were reviewed without changing their intended objectives. [Detailed math validation](assets/math_validation.json) and [migration preservation checks](assets/math_migration.json) retain evidence.

The target application viewer is unknown. These files require GitHub's math support or a Markdown preview with MathJax/KaTeX enabled. Plain Markdown viewers may still display LaTeX literally. The [rendered HTML preview](assets/math_preview/01_REINFORCEMENT_LEARNING_FUNDAMENTALS.html) uses locally bundled KaTeX CSS/fonts and pre-rendered HTML/MathML, so it works without a math-enabled Markdown viewer. Eight chapter previews are available in `assets/math_preview/`; Mermaid diagrams in these previews appear as their code source rather than rendered diagrams.
