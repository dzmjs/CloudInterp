
import cv2
import imageio

# 读取两张图像
img1 = cv2.imread('images/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20250424111500000.JPG')
img2 = cv2.imread('images/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20250424121500000.JPG')

assert img1 is not None, "cloud1.png not found"
assert img2 is not None, "cloud2.png not found"
assert img1.shape == img2.shape, "图片尺寸不一致"

num_frames = 10  # 动画补间帧的数量
frames = []

for i in range(num_frames + 1):
    alpha = i / num_frames
    # alpha 线性插值，生成中间帧
    inter = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
    frames.append(inter)

# 保存动画为 GIF
frames_rgb = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
imageio.mimsave('cloud_interp.gif', frames_rgb, duration=0.1)

# 或者保存为 MP4 视频
h, w = img1.shape[:2]
out = cv2.VideoWriter('cloud_interp.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 12, (w, h))
for frame in frames:
    out.write(frame)
out.release()
