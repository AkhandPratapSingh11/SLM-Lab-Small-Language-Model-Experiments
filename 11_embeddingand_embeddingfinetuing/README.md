# 🧬 Module 11 — Embeddings & Embedding Model Fine-Tuning

> **Fine-Tuning Dense Embedding Models for Retrieval-Augmented Generation (RAG) & Semantic Search** — training custom bi-encoders, contrastive loss functions, and Matryoshka representations.

---

## 🎯 Objectives & Scope
- **Modern Embedding Architectures:**
  - **BAAI BGE** (bge-base, bge-large, bge-m3)
  - **Alibaba GTE** (gte-large)
  - **ModernBERT** (8K context bidirectional encoder)
- **Contrastive Learning Losses:**
  - `MultipleNegativesRankingLoss` (MNRL) with in-batch negatives.
  - `CosineSimilarityLoss` & `TripletLoss`.
  - **Matryoshka Representation Learning (MRL)** for multi-dimensional scalable embeddings (e.g., 256, 512, 768 dimensions).
- **RAG & Search Evaluation:**
  - MTEB (Massive Text Embedding Benchmark) evaluation metrics.
  - Hit Rate@K, MRR@K, and NDCG@K scoring.
