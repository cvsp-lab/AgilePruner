# [ICLR 2026] AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models 

<a href="https://sites.google.com/view/changwoobaek00/%ED%99%88">Changwoo Baek</a><sup>&ast;</sup>, Jouwon Song<sup>&ast;</sup>, <a href="https://www.pnu-cvsp.com/members/sohyeon">Sohyeon Kim</a><sup>&ast;</sup>, <a href="https://www.pnu-cvsp.com/prof">Kyeongbo Kong</a><sup>&dagger;</sup>

<sup>&ast;</sup>Equal contribution, <sup>&dagger;</sup>Corresponding author

[**🌐 Project Page**](https://cvsp-lab.github.io/AgilePruner/) | [**📄 Paper**](http://arxiv.org/abs/2603.01236)

## 🎉 News

- **[2026/01]** 🔥 Our paper has been accepted to **ICLR 2026!** 🎊
- **[2026/02]** 🚀 Project page is now live!

## 📖 Overview

Large Vision-Language Models (LVLMs) have adopted visual token pruning strategies to mitigate substantial computational overhead incurred by extensive visual token sequences. While prior works primarily focus on either attention-based or diversity-based pruning methods, in-depth analysis of these approaches' characteristics and limitations remains largely unexplored.

In this work, we conduct thorough empirical analysis using effective rank (erank) as a measure of feature diversity and attention score entropy to investigate visual token processing mechanisms and analyze the strengths and weaknesses of each approach.

## 🔍 Key Findings

Our analysis reveals two key insights:

1. Diversity aware hybrid pruning methods preserve less feature diversity than intended, and **the diversity they do retain is closely tied to increased hallucination** frequency compared to attention-based pruning.

<p align="center">
  <img src="docs/images/hal_concept.png" alt="Key Findings" width="600">
</p>

2. **Attention-based approaches are more effective on simple images** where visual evidence is concentrated, while **diversity-based methods better handle complex images** with distributed features.

<p align="center">
  <img src="docs/images/key_findings.png" alt="Key Findings" width="600">
</p>

Building on these empirical insights, we show that incorporating image-aware adjustments into existing hybrid pruning strategies consistently improves their performance. We also provide a minimal instantiation of our empirical findings through a simple adaptive pruning mechanism.

## 💻 Code

This repository contains the full training-free implementation on top of [LLaVA](https://github.com/haotian-liu/LLaVA). The pruning method itself — effective rank (`effective_rank`), the adaptive threshold rule (`calculate_adaptive_tau`, Eq. 6 in the paper), and the token-selection procedure (`select_diverse_tokens_by_attention_and_distance`) — lives in [`llava/model/llava_arch.py`](llava/model/llava_arch.py).

### 🏝️ Environment

```bash
git clone https://github.com/cvsp-lab/AgilePruner.git
cd AgilePruner
conda create -n agilepruner python=3.10 -y
conda activate agilepruner
pip install -e .
```

(Optional) Install FlashAttention for further inference acceleration:
```bash
pip install flash-attn --no-build-isolation
```

### 📦️ Model

Download the corresponding [LLaVA](https://github.com/haotian-liu/LLaVA/blob/main/docs/MODEL_ZOO.md) checkpoint from Hugging Face 🤗, e.g. [liuhaotian/llava-v1.5-7b](https://huggingface.co/liuhaotian/llava-v1.5-7b). 

### 📊 Data

Download each benchmark's data following [EVAL.md](EVAL.md).

### 📋️ Evaluation

Each benchmark has its own script under `scripts/v1_5/eval/`. Pass the number of visual tokens to retain as the argument:
```bash
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/${DATASET}.sh ${VISUAL_TOKEN_NUMBER}
```
For example, to keep 64 of the 576 visual tokens (89% reduction) on POPE:
```bash
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/pope.sh 64
```
Full per-benchmark setup and submission instructions are in [EVAL.md](EVAL.md).

### 🔖 Citation

If you find AgilePruner useful for your research, please cite:
```bibtex
@inproceedings{baek2026agilepruner,
      title={AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models},
      author={Baek, Changwoo and Song, Jouwon and Kim, Sohyeon and Kong, Kyeongbo},
      booktitle={International Conference on Learning Representations (ICLR)},
      year={2026},
      eprint={2603.01236},
      archivePrefix={arXiv},
}
```

## 📧 Contact

For questions or collaborations, please contact:
- [Changwoo Baek](https://sites.google.com/view/changwoobaek00/%ED%99%88)
- [Kyeongbo Kong](https://www.pnu-cvsp.com/prof) (Corresponding author)

## 🙏 Acknowledgements

We thank [LLaVA](https://github.com/haotian-liu/LLaVA) and [FasterVLM](https://github.com/Theia-4869/FasterVLM) for their excellent work and open-source contributions.

## 📜 License

This project is licensed under the Apache License 2.0 
