import cv2
import numpy as np
import imageio
import glob
import os

# 步骤1：收集所有云图文件路径，并排序
# 假设图片都在 ./clouds/ 目录下， 文件后缀为 .JPG
img_dir = './images/'
img_files = sorted(glob.glob(os.path.join(img_dir, '*.JPG')))

# 确认有足够图片
assert len(img_files) >= 2, "至少需要2张图片"

# 可以调整补间帧数
num_inter_frames = 24    # 每对图片之间插8帧

frames = []

for i in range(len(img_files) - 1):
    img1 = cv2.imread(img_files[i])
    img2 = cv2.imread(img_files[i+1])
    assert img1.shape == img2.shape, "图片尺寸不一致"

    # 先加原始帧
    if i == 0:  
        frames.append(img1)

    # 建立补间帧
    for j in range(1, num_inter_frames + 1):
        alpha = j / (num_inter_frames + 1)
        inter = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        frames.append(inter)
    frames.append(img2)

# 将opencv的BGR转换为RGB用于保存gif
frames_rgb = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
# 保存为GIF动画
# imageio.mimsave('all_clouds_interp.gif', frames_rgb, duration=0.1)
# 或保存为mp4
h, w = frames[0].shape[:2]
out = cv2.VideoWriter('all_clouds_interp.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 12, (w, h))
for frame in frames:
    out.write(frame)
out.release()