# Notebook cell-by-cell audit
Cell numbers are 1-based JSON order, including Markdown and commented cells. All 247 source cells and relevant outputs were read; original notebooks were not executed here. Source snippets below identify each cell, and linked extracts preserve the complete cell and outputs. Stored success is distinguished from source intent.

## DPO_Training.ipynb
47-cell detailed TRL DPO/QLoRA workflow; inline 4 pairs, optional JSON and external dataset; evaluation, saved metrics, adapter reload. Chapters: 05,09,10. Source cells exactly match Final version; output metadata differs. One held-out pair and matching metrics do not prove independent runs.
[Original](../../../DPO_Training.ipynb) · [All sources](DPO_Training_source.txt) · [Full cells and saved outputs](DPO_Training_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | markdown | # Direct Preference Optimization (DPO) with Qwen2.5-0.5B-Instruct | None stored |
| 2 | markdown | ## What was wrong or incomplete in the original code? | None stored |
| 3 | markdown | ## 1. Install dependencies | None stored |
| 4 | code | %pip install -q -U transformers datasets trl peft accelerate bitsandbytes sentencepiece | stream |
| 5 | markdown | > After the installation cell finishes, restart the Colab runtime once if Colab asks you to do so. Then continue from the imports cell. | None stored |
| 6 | markdown | ## 2. Imports and reproducibility | None stored |
| 7 | code | import gc | stream |
| 8 | markdown | ## 3. Configuration | None stored |
| 9 | code | MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct" | stream |
| 10 | markdown | ## 4. Detect hardware and select numerical precision | None stored |
| 11 | code | HAS_CUDA = torch.cuda.is_available() | stream |
| 12 | markdown | ## 5. Build or load the preference dataset | None stored |
| 13 | code | INLINE_DATA = [ | display_data, stream |
| 14 | markdown | ## 6. Validate and split the dataset | None stored |
| 15 | code | required_columns = {"chosen", "rejected"} | stream |
| 16 | markdown | ## 7. Load and configure the tokenizer | None stored |
| 17 | code | tokenizer = AutoTokenizer.from_pretrained( | display_data, stream |
| 18 | markdown | ## 8. Configure optional 4-bit QLoRA | None stored |
| 19 | code | quantization_config = None | stream |
| 20 | markdown | ## 9. Configure LoRA | None stored |
| 21 | code | peft_config = LoraConfig( | stream |
| 22 | markdown | ## 10. Configure DPO training | None stored |
| 23 | code | model_init_kwargs = { | stream |
| 24 | markdown | ## 11. Create the DPO trainer | None stored |
| 25 | code | trainer = DPOTrainer( | display_data, stream |
| 26 | markdown | ## 12. Evaluate before training | None stored |
| 27 | code | initial_metrics = trainer.evaluate() | display_data, stream |
| 28 | markdown | ## 13. Train the model | None stored |
| 29 | code | train_result = trainer.train() | stream, display_data |
| 30 | markdown | ## 14. Evaluate after training | None stored |
| 31 | code | final_metrics = trainer.evaluate() | display_data, stream |
| 32 | markdown | ## 15. Inspect the training log | None stored |
| 33 | code | history = pd.DataFrame(trainer.state.log_history) | display_data, display_data (PNG inspected) |
| 34 | markdown | ## 16. Save the LoRA adapter and tokenizer | None stored |
| 35 | code | trainer.save_model(OUTPUT_DIR) | stream |
| 36 | markdown | ## 17. Release training memory | None stored |
| 37 | code | del trainer | stream |
| 38 | markdown | ## 18. Load the trained PEFT adapter for inference | None stored |
| 39 | code | inference_load_kwargs = { | stream, display_data |
| 40 | markdown | ## 19. Generate a response | None stored |
| 41 | code | def generate_response( | stream |
| 42 | markdown | ## 20. Test several prompts | None stored |
| 43 | code | test_prompts = [ | stream |
| 44 | markdown | ## 21. Download the trained adapter from Colab | None stored |
| 45 | code | import shutil | stream |
| 46 | markdown | ## Notes for real training | None stored |
| 47 | markdown | ## Official references | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## DPO_Training_Final.ipynb
Same 47 source cells as DPO_Training; recorded later dependency versions and same main metrics. Chapters: 05,09,10. Final name does not imply an implementation change; tiny evaluation and T4 precision flag need qualification.
[Original](../../../DPO_Training_Final.ipynb) · [All sources](DPO_Training_Final_source.txt) · [Full cells and saved outputs](DPO_Training_Final_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | markdown | # Direct Preference Optimization (DPO) with Qwen2.5-0.5B-Instruct | None stored |
| 2 | markdown | ## What was wrong or incomplete in the original code? | None stored |
| 3 | markdown | ## 1. Install dependencies | None stored |
| 4 | code | %pip install -q -U transformers datasets trl peft accelerate bitsandbytes sentencepiece | stream |
| 5 | markdown | > After the installation cell finishes, restart the Colab runtime once if Colab asks you to do so. Then continue from the imports cell. | None stored |
| 6 | markdown | ## 2. Imports and reproducibility | None stored |
| 7 | code | import gc | stream |
| 8 | markdown | ## 3. Configuration | None stored |
| 9 | code | MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct" | stream |
| 10 | markdown | ## 4. Detect hardware and select numerical precision | None stored |
| 11 | code | HAS_CUDA = torch.cuda.is_available() | stream |
| 12 | markdown | ## 5. Build or load the preference dataset | None stored |
| 13 | code | INLINE_DATA = [ | display_data, stream |
| 14 | markdown | ## 6. Validate and split the dataset | None stored |
| 15 | code | required_columns = {"chosen", "rejected"} | stream |
| 16 | markdown | ## 7. Load and configure the tokenizer | None stored |
| 17 | code | tokenizer = AutoTokenizer.from_pretrained( | display_data, stream |
| 18 | markdown | ## 8. Configure optional 4-bit QLoRA | None stored |
| 19 | code | quantization_config = None | stream |
| 20 | markdown | ## 9. Configure LoRA | None stored |
| 21 | code | peft_config = LoraConfig( | stream |
| 22 | markdown | ## 10. Configure DPO training | None stored |
| 23 | code | model_init_kwargs = { | stream |
| 24 | markdown | ## 11. Create the DPO trainer | None stored |
| 25 | code | trainer = DPOTrainer( | display_data, stream |
| 26 | markdown | ## 12. Evaluate before training | None stored |
| 27 | code | initial_metrics = trainer.evaluate() | display_data, stream |
| 28 | markdown | ## 13. Train the model | None stored |
| 29 | code | train_result = trainer.train() | stream, display_data |
| 30 | markdown | ## 14. Evaluate after training | None stored |
| 31 | code | final_metrics = trainer.evaluate() | display_data, stream |
| 32 | markdown | ## 15. Inspect the training log | None stored |
| 33 | code | history = pd.DataFrame(trainer.state.log_history) | display_data, display_data (PNG inspected) |
| 34 | markdown | ## 16. Save the LoRA adapter and tokenizer | None stored |
| 35 | code | trainer.save_model(OUTPUT_DIR) | stream |
| 36 | markdown | ## 17. Release training memory | None stored |
| 37 | code | del trainer | stream |
| 38 | markdown | ## 18. Load the trained PEFT adapter for inference | None stored |
| 39 | code | inference_load_kwargs = { | stream, display_data |
| 40 | markdown | ## 19. Generate a response | None stored |
| 41 | code | def generate_response( | stream |
| 42 | markdown | ## 20. Test several prompts | None stored |
| 43 | code | test_prompts = [ | stream |
| 44 | markdown | ## 21. Download the trained adapter from Colab | None stored |
| 45 | code | import shutil | stream |
| 46 | markdown | ## Notes for real training | None stored |
| 47 | markdown | ## Official references | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## Final_DPO.ipynb
15-cell prototype: full downloaded UltraFeedback, Qwen2.5-0.5B LoRA, training and inference. Chapters: 05,09,10. Inline literal unused; bad device precision branches, boundary warnings and KeyboardInterrupt. End-to-end success unverified.
[Original](../../../Final_DPO.ipynb) · [All sources](Final_DPO_source.txt) · [Full cells and saved outputs](Final_DPO_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | code | [; { | execute_result |
| 2 | code | !pip install torch transformers datasets trl peft accelerate bitsandbytes sentencepiece | stream, display_data |
| 3 | code | import os; import json | None stored |
| 4 | code | MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct" | None stored |
| 5 | code | # with open(DATA_PATH, "r", encoding="utf-8") as f: | None stored |
| 6 | code | from datasets import load_dataset; dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train") | display_data |
| 7 | code | tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True) | display_data |
| 8 | code | model = AutoModelForCausalLM.from_pretrained( | stream, display_data |
| 9 | code | peft_config = LoraConfig( | None stored |
| 10 | code | training_args = DPOConfig( | None stored |
| 11 | code | trainer = DPOTrainer( | display_data, stream |
| 12 | code | trainer.train() | stream, display_data, error: KeyboardInterrupt |
| 13 | code | trainer.save_model(OUTPUT_DIR) | None stored |
| 14 | code | import torch; from transformers import AutoTokenizer, AutoModelForCausalLM | None stored |
| 15 | code | (empty) | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## Final_GRPO_Practical.ipynb
54 cells: 8-prompt SmolLM heuristic-reward workflow, then separate Unsloth Qwen/GSM8K XML reward workflow. Chapters: 06,08,09,10,11. First path saved default DAPO loss; lexical reward is not correctness. Second path no outputs, batch/group and numeric parsing need verification.
[Original](../../../Final_GRPO_Practical.ipynb) · [All sources](Final_GRPO_Practical_source.txt) · [Full cells and saved outputs](Final_GRPO_Practical_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | code | !pip install -q -U datasets transformers trl peft accelerate bitsandbytes | None stored |
| 2 | markdown | torchao is an optional PyTorch optimization/quantization package. Our GRPO practical does not need it. But PEFT detects the old installed torchao version and… | None stored |
| 3 | code | import re | None stored |
| 4 | markdown | \| Code component         \| Story character                                    \| | None stored |
| 5 | code | data = [ | None stored |
| 6 | markdown | Prompt goes to model | None stored |
| 7 | markdown | In GRPO, our dataset mainly provides prompts. The model generates multiple answers for each prompt, then reward functions compare those answers with referenc… | None stored |
| 8 | code | def format_prompt(example): | None stored |
| 9 | code | dataset = Dataset.from_list(data) | display_data, execute_result |
| 10 | code | dataset | None stored |
| 11 | markdown | {; 'prompt': 'Question: Explain reinforcement learning in simple terms.\nAnswer in simple English:', | None stored |
| 12 | code | model_id = "HuggingFaceTB/SmolLM-135M-Instruct" | None stored |
| 13 | code | tokenizer = AutoTokenizer.from_pretrained(model_id) | None stored |
| 14 | code | model = AutoModelForCausalLM.from_pretrained( | stream, display_data |
| 15 | code | lora_config = LoraConfig( | None stored |
| 16 | markdown | 1. Rule-based/verifiable reward | None stored |
| 17 | markdown | \| Approach                                    \| What it means                                                            \| Where it is used                  … | None stored |
| 18 | markdown | \| Component                \| PPO                        \| GRPO                                                        \| | None stored |
| 19 | code | #Text cleaning | None stored |
| 20 | markdown | "   Reinforcement   Learning IS useful. " | None stored |
| 21 | code | #This function safely extracts the answer text from either a normal string or chat-message format, and converts unknown formats into a string. | None stored |
| 22 | code | #It cleans both texts, compares their character/word sequence using SequenceMatcher, and returns a similarity score from 0 to 1—1 means identical and 0 means… | None stored |
| 23 | code | # This function extracts unique words of at least 3 letters from both texts and returns the fraction of reference-text words (b) that also appear in the gene… | None stored |
| 24 | code | # It acts like a teacher that compares the model’s answer with the answer key and gives marks out of 5. | None stored |
| 25 | code | # It acts like a teacher who rewards complete and properly written answers and penalizes short, vague, or unhelpful answers. | None stored |
| 26 | code | # It acts like a teacher who rewards readable, properly sized answers and penalizes unclear or repetitive output. | None stored |
| 27 | markdown | In GRPO, the model does not directly learn from a fixed label like SFT. It generates multiple answers, and then reward functions score those answers. This co… | None stored |
| 28 | markdown | In GRPO, reward function is the teacher signal. For a demo, we can manually write simple rewards like correctness, helpfulness, and clarity. But in real syst… | None stored |
| 29 | code | training_args = GRPOConfig( | None stored |
| 30 | code | trainer = GRPOTrainer( | None stored |
| 31 | code | import trl | stream |
| 32 | code | trainer.train() | display_data, execute_result |
| 33 | code | trainer.save_model("grpo_output_final") | execute_result |
| 34 | code | base_model_id = "HuggingFaceTB/SmolLM-135M-Instruct" | display_data, execute_result |
| 35 | code | def generate_answer(question, max_new_tokens=100): | None stored |
| 36 | code | print(generate_answer("Explain AI in simple terms.")) | stream |
| 37 | markdown | ## GRPO with unsloth | None stored |
| 38 | code | !pip install -U unsloth vllm | None stored |
| 39 | code | from unsloth import FastLanguageModel | None stored |
| 40 | code | model = FastLanguageModel.get_peft_model( | None stored |
| 41 | code | SYSTEM_PROMPT = """ | None stored |
| 42 | code | import re | None stored |
| 43 | code | def extract_xml_answer(text: str) -> str: | None stored |
| 44 | code | def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]: | None stored |
| 45 | code | def int_reward_func(completions, **kwargs) -> list[float]: | None stored |
| 46 | code | def soft_format_reward_func(completions, **kwargs) -> list[float]: | None stored |
| 47 | code | def strict_format_reward_func(completions, **kwargs) -> list[float]: | None stored |
| 48 | code | def count_xml(text) -> float: | None stored |
| 49 | code | from trl import GRPOConfig, GRPOTrainer | None stored |
| 50 | code | trainer = GRPOTrainer( | None stored |
| 51 | code | trainer.train() | None stored |
| 52 | code | model.save_lora("grpo_saved_lora") | None stored |
| 53 | code | from vllm import SamplingParams | None stored |
| 54 | code | model.save_pretrained_merged( | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## Final_ORPO_Practical.ipynb
33 cells: standard experimental TRL ORPO on 100 UltraFeedback examples; separate older Unsloth environment on 500. Chapters: 07,08,09,10,11. First training has output but saved inference CUDA assert; second path no outputs. State-dependent deletion, version mixing and prompt extraction issues.
[Original](../../../Final_ORPO_Practical.ipynb) · [All sources](Final_ORPO_Practical_source.txt) · [Full cells and saved outputs](Final_ORPO_Practical_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | code | del trainer | error: AcceleratorError |
| 2 | code | !pip uninstall -y torchao | stream |
| 3 | code | !pip install -U "torchao>=0.16.0" | stream |
| 4 | code | # Install once. | stream |
| 5 | code | import gc | stream |
| 6 | code | # --------------------------------------------------------- | None stored |
| 7 | code | # --------------------------------------------------------- | stream |
| 8 | code | # --------------------------------------------------------- | display_data |
| 9 | code | # --------------------------------------------------------- | stream, display_data |
| 10 | code | # --------------------------------------------------------- | display_data, stream |
| 11 | code | # # --------------------------------------------------------- | None stored |
| 12 | code | # Reduce total training time. | None stored |
| 13 | code | orpo_args = ORPOConfig( | None stored |
| 14 | code | # --------------------------------------------------------- | None stored |
| 15 | code | # --------------------------------------------------------- | stream, display_data |
| 16 | code | # --------------------------------------------------------- | stream |
| 17 | code | # --------------------------------------------------------- | error: AcceleratorError |
| 18 | markdown | # with unsloth | None stored |
| 19 | code | # Run this in a fresh Google Colab runtime. | None stored |
| 20 | code | import gc | None stored |
| 21 | code | model_name = "Qwen/Qwen2-0.5B-Instruct" | None stored |
| 22 | code | model, tokenizer = FastLanguageModel.from_pretrained( | None stored |
| 23 | code | model = FastLanguageModel.get_peft_model( | None stored |
| 24 | code | dataset = load_dataset( | None stored |
| 25 | code | def format_preference_example(example): | None stored |
| 26 | code | # Unsloth's preference-trainer optimization patch. | None stored |
| 27 | code | from trl import ORPOConfig, ORPOTrainer | None stored |
| 28 | code | trainer = ORPOTrainer( | None stored |
| 29 | code | train_result = trainer.train() | None stored |
| 30 | code | model.save_pretrained(output_dir) | None stored |
| 31 | code | FastLanguageModel.for_inference(model) | None stored |
| 32 | code | merged_output_dir = "./qwen2_orpo_merged_16bit" | None stored |
| 33 | code | # # Run in a fresh Colab runtime. | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## RL_Fundamental.ipynb
28 cells: bandit-like dictionary, synthetic DQN update, Stable-Baselines3 PPO CarRacing demo. Chapters: 01,04,11. First is not full Q-learning; DQN has no environment/replay loop; requested100 PPO steps collect2048 due rollout length.
[Original](../../../RL_Fundamental.ipynb) · [All sources](RL_Fundamental_source.txt) · [Full cells and saved outputs](RL_Fundamental_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | code | # RL basic form | None stored |
| 2 | code | import random | None stored |
| 3 | code | # reward system | None stored |
| 4 | code | # learning rate | stream |
| 5 | code | Q[action] = Q[action] + alpha * (reward - Q[action]) | None stored |
| 6 | code | Q | execute_result |
| 7 | code | # # Initially: | None stored |
| 8 | markdown | Have you ever wondered… | None stored |
| 9 | code | import torch; import torch.nn as nn | None stored |
| 10 | code | model = DQN(state_size, action_size) | None stored |
| 11 | code | # Dummy batch | None stored |
| 12 | code | reward = torch.randn(32) | None stored |
| 13 | code | # Predicted Q values for current state | None stored |
| 14 | code | # Pick Q-value of the action actually taken | None stored |
| 15 | code | # Compute target Q value | None stored |
| 16 | code | # Compute loss | None stored |
| 17 | code | # Update model weights | None stored |
| 18 | markdown | No one explicitly tells the model: | None stored |
| 19 | code | !pip install stable-baselines3 | stream |
| 20 | code | !pip install swig | stream |
| 21 | code | !pip install "gymnasium[box2d]" | stream |
| 22 | code | import gymnasium as gym | stream |
| 23 | code | # Create environment (real RL env) | stream |
| 24 | code | # Create RL model (agent) | stream |
| 25 | code | # Train agent | stream, execute_result |
| 26 | code | # Test agent | None stored |
| 27 | code | for _ in range(1000): | None stored |
| 28 | markdown | This code shows the core training step of DQN | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.

## RLHF_with_PPO_Final_Code.ipynb
23 cells: 4-pair RewardTrainer, frozen RM/reference, trainable critic, experimental PPOTrainer and final inference. Chapters: 02,03,04,09,10,11. Default inline dataset rather than local file. No eval, 6 episodes, singleton variance warning, full-prompt inference; internal tensors delegated to installed TRL.
[Original](../../../RLHF_with_PPO_Final_Code.ipynb) · [All sources](RLHF_with_PPO_Final_Code_source.txt) · [Full cells and saved outputs](RLHF_with_PPO_Final_Code_cells.md)
| Cell | Type | Source role / identifying content | Saved output |
|---|---|---|---|
| 1 | code | # ========================================================= | stream |
| 2 | code | # ========================================================= | stream |
| 3 | code | # ========================================================= | None stored |
| 4 | code | # ========================================================= | None stored |
| 5 | code | # ========================================================= | display_data |
| 6 | code | # # ----------------------------- | None stored |
| 7 | code | # # ----------------------------- | None stored |
| 8 | code | # ========================================================= | stream |
| 9 | code | # ========================================================= | stream, display_data |
| 10 | code | # 7) REWARD TRAINING CONFIG | None stored |
| 11 | code | # ========================================================= | display_data, stream |
| 12 | code | # ========================================================= | None stored |
| 13 | code | # ========================================================= | None stored |
| 14 | code | # ========================================================= | display_data |
| 15 | code | # Reward model - trained above, fixed during PPO | display_data |
| 16 | code | # Value model - trainable value head for PPO | display_data |
| 17 | code | # ========================================================= | display_data, stream |
| 18 | code | #========================================================= | None stored |
| 19 | code | # ========================================================= | stream |
| 20 | code | # ========================================================= | stream, display_data |
| 21 | code | # ========================================================= | display_data, stream |
| 22 | code | # ========================================================= | display_data, stream |
| 23 | code | (empty) | None stored |

**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.
