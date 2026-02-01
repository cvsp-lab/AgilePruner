# An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models

**ICLR 2026**

[**Project Page**](https://higokri.github.io/ADA-VTP/) | [**Paper**](#) (Coming Soon)

## Overview

Large Vision-Language Models (LVLMs) have adopted visual token pruning strategies to mitigate substantial computational overhead incurred by extensive visual token sequences. While prior works primarily focus on either attention-based or diversity-based pruning methods, in-depth analysis of these approaches' characteristics and limitations remains largely unexplored.

In this work, we conduct thorough empirical analysis using effective rank (erank) as a measure of feature diversity and attention score entropy to investigate visual token processing mechanisms and analyze the strengths and weaknesses of each approach.

## Key Findings

Our analysis reveals two key insights:

1. **Diversity-based pruning methods preserve substantially less feature diversity than intended**, and the diversity they do retain is closely tied to increased hallucination frequency compared to attention-based pruning.

2. **Attention-based approaches are more effective on simple images** where visual evidence is concentrated, while **diversity-based methods better handle complex images** with distributed features.

Building on these empirical insights, we show that incorporating image-aware adjustments into existing hybrid pruning strategies consistently improves their performance. We also provide a minimal instantiation of our empirical findings through a simple adaptive pruning mechanism.

## Code

**Detailed implementation code is coming soon.**

Stay tuned for updates!

## Citation

```bibtex
@inproceedings{baek2026adavtp,
  title={An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in Large Vision-Language Models},
  author={Baek, Changwoo and Song, Jouwon and Kim, Sohyeon and Kong, Kyeongbo},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2026}
}
```

## Contact

For questions or collaborations, please contact:
- Kyeongbo Kong (Corresponding author)
- Changwoo Baek
- Jouwon Song
- Sohyeon Kim

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.