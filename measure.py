import sys
import os
import numpy as np
import pandas as pd

import cv2
from setuptools import glob

from imresize import imresize

sys.path.insert(0, "./PerceptualSimilarity")
from lpips import lpips
import tqdm

import torch

from skimage.metrics import peak_signal_noise_ratio as psnr
n_imgs = 100


def fiFindByWildcard(wildcard):
    return glob.glob(os.path.expanduser(wildcard), recursive=True)


def dprint(d):
    out = []
    for k, v in d.items():
        out.append(f"{k}: {v:0.4f}")
    print(", ".join(out))


def t(array):
    return torch.Tensor(np.expand_dims(array.transpose([2, 0, 1]), axis=0).astype(np.float32)) / 255


def imread(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    return img[:, :, [2, 1, 0]]


def lpips_analysis(gt, srs, scale):
    from collections import OrderedDict
    results = OrderedDict()

    gt = imread(gt)
    h, w, _ = gt.shape
    gt = gt[:(h//8)*8, :(w//8)*8]
    srs = [imread(sr) for sr in srs]

    lpipses_sp = []
    lpipses_gl = []
    lrpsnrs = []
    n_samples = len(srs)

    for sample_idx in tqdm.trange(n_samples):
        sr = srs[sample_idx]

        h1, w1, _ = gt.shape
        sr = sr[:h1, :w1]

        lpips_sp = loss_fn_alex_sp(2 * t(sr) - 1, 2 * t(gt) - 1)
        lpipses_sp.append(lpips_sp)
        lpipses_gl.append(lpips_sp.mean().item())

        imgA_lr = imresize(sr, 1 / scale)
        imgB_lr = imresize(gt, 1 / scale)
        lrpsnr = psnr(imgA_lr, imgB_lr)
        lrpsnrs.append(lrpsnr)

    lpips_gl = np.min(lpipses_gl)

    results['LPIPS_mean'] = np.mean(lpipses_gl)
    results['LRPSNR_worst'] = np.min(lrpsnrs)
    results['LRPSNR_mean'] = np.mean(lrpsnrs)

    lpipses_stacked = torch.stack([l[0, 0, :, :] for l in lpipses_sp], dim=2)

    lpips_best_sp, _ = torch.min(lpipses_stacked, dim=2)
    lpips_loc = lpips_best_sp.mean().item()

    score = (lpips_gl - lpips_loc) / lpips_gl * 100

    results['score'] = score

    dprint(results)

    return results


name, gt_dir, srs_dir, n_samples, scale = sys.argv[1:]

gt_dir = os.path.expanduser(gt_dir)
srs_dir = os.path.expanduser(srs_dir)
n_samples = int(n_samples)
scale = int(scale)

########################################
# Get Paths
########################################

gt_imgs_raw = fiFindByWildcard(os.path.join(gt_dir, '*.png'))
srs_imgs_raw = fiFindByWildcard(os.path.join(srs_dir, '*.png'))

gt_imgs = []
srs_imgs = []

for img_idx in range(100):
    gt = os.path.expanduser(os.path.join(gt_dir, f'0{801 + img_idx:03d}.png'))
    if gt in gt_imgs_raw:
        gt_imgs.append(gt)
    else:
        raise RuntimeError("Not Found: ", gt)

    if n_samples > 1:
        srs_imgs.append([])
        for i in range(n_samples):
            sr = os.path.join(srs_dir, f'{img_idx:06d}_sample{i:05d}.png')
            if sr in srs_imgs_raw:
                srs_imgs[-1].append(sr)
            else:
                raise RuntimeError("Not Found: ", sr)
    else:
        srs_imgs.append([])
        sr = os.path.join(srs_dir, f'{img_idx:06d}.png')
        if sr in srs_imgs_raw:
            srs_imgs[-1].append(sr)
        else:
            raise RuntimeError("Not Found: ", sr)

print("Found required images.")

loss_fn_alex_sp = lpips.LPIPS(spatial=True)

results = []

for img_idx in range(n_imgs):
    results.append(lpips_analysis(gt_imgs[img_idx], srs_imgs[img_idx], scale))

df = pd.DataFrame(results)
df_mean = df.mean()

df.to_csv(f"./{name}.csv")
df_mean.to_csv(f"./{name}_mean.csv")

print()
print(df_mean.to_string())
