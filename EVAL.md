# Evaluation

*Adapted from [FasterVLM](https://github.com/Theia-4869/FasterVLM)'s `EVAL.md`, adjusted for AgilePruner's scripts and directory layout.*

We evaluate AgilePruner with different [LLaVA](https://github.com/haotian-liu/LLaVA) models on a diverse set of multimodal benchmarks. To ensure reproducibility, we evaluate the models with greedy decoding following the original LLaVA.

## Scripts

Before preparing task-specific data, **you MUST first download [eval.zip](https://drive.google.com/file/d/1atZSBBrAX54yYpxtVVW33zFvcnaHeFPy/view?usp=sharing)**. It contains custom annotations, scripts, and the prediction files with vanilla LLaVA-1.5. Extract it to `./playground/data/eval`. This also provides a general structure for all datasets.

Every script below takes the number of visual tokens to retain as its first argument.

### VQAv2

1. Download [`test2015`](http://images.cocodataset.org/zips/test2015.zip) and put it under `./playground/data/eval/vqav2`.
2. Multi-GPU inference.
```Shell
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/v1_5/eval/vqav2.sh 64
```
3. Submit the results to the [evaluation server](https://eval.ai/web/challenges/challenge-page/830/my-submission): `./playground/data/eval/vqav2/answers_upload`.

### GQA

1. Download the [data](https://cs.stanford.edu/people/dorarad/gqa/download.html) and [evaluation scripts](https://cs.stanford.edu/people/dorarad/gqa/evaluate.html) following the official instructions and put under `./playground/data/eval/gqa`. You may need to modify `eval.py` as [this](https://gist.github.com/haotian-liu/db6eddc2a984b4cbcc8a7f26fd523187) due to the missing assets in the GQA v1.2 release.
2. Multi-GPU inference.
```Shell
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/v1_5/eval/gqa.sh 64
```

### ScienceQA

1. Under `./playground/data/eval/scienceqa`, download `images`, `pid_splits.json`, `problems.json` from the `data/scienceqa` folder of the ScienceQA [repo](https://github.com/lupantech/ScienceQA).
2. Single-GPU inference and evaluate.
```Shell
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/svqa.sh 64
```

### TextVQA

1. Download [`TextVQA_0.5.1_val.json`](https://dl.fbaipublicfiles.com/textvqa/data/TextVQA_0.5.1_val.json) and [images](https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip) and extract to `./playground/data/eval/textvqa`.
2. Single-GPU inference and evaluate.
```Shell
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/tvqa.sh 64
```

### POPE

1. Download `coco` from [POPE](https://github.com/AoiDragon/POPE/tree/e3e39262c85a6a83f26cf5094022a782cb0df58d/output/coco) and put under `./playground/data/eval/pope` (annotations only — `coco/` should contain just the three `coco_pope_*.json` files). Put the COCO `val2014` images directly under `./playground/data/eval/pope/val2014`, as a sibling of `coco/`, not inside it.
2. Single-GPU inference and evaluate.
```Shell
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/pope.sh 64
```

### MME

1. Download the data following the official instructions [here](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models/tree/Evaluation).
2. Download images to `MME_Benchmark_release_version`.
3. Put the official `eval_tool` and `MME_Benchmark_release_version` under `./playground/data/eval/MME`.
4. Single-GPU inference and evaluate.
```Shell
CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/mme.sh 64
```

> **Not yet included in this release:** the paper also reports VizWiz, MMBench, and MMBench-CN (Table 7). Scripts for these three aren't in `scripts/v1_5/eval/` yet — add them following the same `model_vqa_loader.py` / `model_vqa_mmbench.py` pattern as the scripts above if you need to reproduce those columns.

## Scripts with LLaVA-NeXT (LLaVA-1.6)

To evaluate AgilePruner with LLaVA-NeXT, replace `v1_5` with `v1_6` in the shell scripts. For example, to evaluate VQAv2 with LLaVA-NeXT:

```Shell
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 bash scripts/v1_6/eval/vqav2.sh 64
```

## Ablations

To sweep a fixed (non-adaptive) similarity threshold instead of the adaptive rule — reproducing the constant-`tau` ablation in Table 12 — set `DIST_THRESHOLD` before running any script above:
```Shell
DIST_THRESHOLD=0.1 CUDA_VISIBLE_DEVICES=0 bash scripts/v1_5/eval/pope.sh 64
```

## Results

See [README.md](README.md#-results) and the paper for full results across benchmarks, models (LLaVA-1.5-7B/13B, LLaVA-NeXT-7B, Qwen2.5-VL-7B), and the CHAIR hallucination evaluation.
