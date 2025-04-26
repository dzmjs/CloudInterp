import base64
import numpy as np
import cv2
import json

def imread_base64(b64_string):
    # 如果有 "data:image/xxx;base64," 头，要去掉
    if ',' in b64_string:
        b64_string = b64_string.split(',')[1]
    img_bytes = base64.b64decode(b64_string)
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

def ndarray_to_base64img(img: np.ndarray, format: str = 'png') -> str:
    # img: numpy 数组 (H,W,C)
    # format: "png" or "jpg"
    _, buf = cv2.imencode(f'.{format}', img)
    b64 = base64.b64encode(buf).decode('utf-8')
    return f"data:image/{format};base64,{b64}"

def get_steps():
    # 这里可以动态返回步数，也可以根据前端文本框动态获取
    return 20
def interp(img1Str, img2Str):
    # 读取两张图像
    #img1 = cv2.imread('images/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20250424111500000.JPG')
    #img2 = cv2.imread('images/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20250424121500000.JPG')
    img1 = imread_base64(img1Str)
    img2 = imread_base64(img2Str)

    assert img1 is not None, "cloud1.png not found"
    assert img2 is not None, "cloud2.png not found"
    assert img1.shape == img2.shape, "图片尺寸不一致"

    num_frames = get_steps()  # 动画补间帧的数量
    frames = []

    for i in range(num_frames + 1):
        alpha = i / num_frames
        # alpha 线性插值，生成中间帧
        inter = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        frames.append(inter)

    # 保存动画为 GIF
    frames_rgb = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]
    frames_pngs= [ndarray_to_base64img(p) for p in frames_rgb]
    return json.dumps(frames_pngs)

if __name__ == '__main__':
    img1 = cv2.imread('images/tt1.jpg')
    str1=ndarray_to_base64img(img1)
    img2 = cv2.imread('images/tt2.jpg')
    str2=ndarray_to_base64img(img2)
    result = interp(str1, str2)
    print(result)

