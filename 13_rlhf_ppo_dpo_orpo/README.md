# 🏆 Module 13 — Alignment: RLHF, PPO, DPO, ORPO & GRPO

> **Reinforcement Learning from Human Feedback & Preference Optimization** — from classical PPO with reward models to direct preference methods (DPO, KTO, ORPO) and DeepSeek-R1 reasoning with GRPO.

---

## 🎯 Objectives & Scope
- **Classical RLHF:**
  - Training a Bradley-Terry **Reward Model (RM)** on pairwise comparison data.
  - Policy optimization with **PPO (Proximal Policy Optimization)** and Generalized Advantage Estimation (GAE).
  - KL divergence penalty to prevent policy collapse.
- **Reference-Free Direct Preference Alignment:**
  - **DPO (Direct Preference Optimization):** Closed-form implicit reward modeling from `{prompt, chosen, rejected}` pairs.
  - **KTO (Kahneman-Tversky Optimization):** Alignment based on prospect theory using unpaired binary signals.
  - **ORPO (Odds Ratio Preference Optimization):** Monolithic instruction tuning + odds ratio penalty without a reference model.
- **Reasoning Alignment:**
  - **GRPO (Group Relative Policy Optimization):** DeepSeek-R1 style rule-based mathematical and reasoning alignment without a value critic model.
