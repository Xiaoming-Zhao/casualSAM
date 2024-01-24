The original repo is the official repository of [CausalSAM, ECCV 2022](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930020.pdf).

This repo is modified to tailor to the need of the work [PGDVS, ICLR 2024](https://arxiv.org/abs/2310.08587).

## casualSAM
### non-exhaustive requirements:
2. skimage
3. ImageIO
4. Pillow
5. configargparse
6. tqdm

### download midas checkpoints:
`bash download_depth_ckpt.sh`

### fill in davis dataset path
L12 in configs/__init__.py

### run training
`bash ./experiments/davis/train.sh`
