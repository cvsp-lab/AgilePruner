# [ICLR 2026] An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models 

<a href="https://sites.google.com/view/changwoobaek00/%ED%99%88">Changwoo Baek</a><sup>*</sup>, Jouwon Song<sup>*</sup>, <a href="https://www.pnu-cvsp.com/members/sohyeon">Sohyeon Kim</a><sup>*</sup>, <a href="https://www.pnu-cvsp.com/prof">Kyeongbo Kong</a><sup>†</sup>

<sup>*</sup>Equal contribution, <sup>†</sup>Corresponding author

[**🌐 Project Page**](https://cvsp-lab.github.io/ADA-VTP/) | [**📄 Paper**](#) (Coming Soon)

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

**Detailed implementation code is coming soon.** 🚧

Stay tuned for updates! ⏳

## 📧 Contact

For questions or collaborations, please contact:
- [Changwoo Baek](https://sites.google.com/view/changwoobaek00/%ED%99%88)
- Jouwon Song
- [Sohyeon Kim](https://www.pnu-cvsp.com/members/sohyeon)
- [Kyeongbo Kong](https://www.pnu-cvsp.com/prof) (Corresponding author)

## 🙏 Acknowledgements

We thank [LLaVA](https://github.com/haotian-liu/LLaVA) and [FasterVLM](https://github.com/Theia-4869/FasterVLM) for their excellent work and open-source contributions.

## 📜 License

This project is licensed under the Apache License 2.0 
