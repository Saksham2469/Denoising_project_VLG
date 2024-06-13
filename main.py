import cv2
import numpy as np
import os
from tqdm import tqdm

path = r"./test/low/"
output_path = r'./test/predicted/'

img_files = [f for f in os.listdir(path) if f.endswith('.png')]
tot_img = len(img_files)

def solve():
    with tqdm(total=tot_img) as pqs:
        for i, name in enumerate(img_files):
            img_path = os.path.join(path, name)
            img = cv2.imread(img_path)
            img = cv2.bilateralFilter(img, 9, 75, 75)
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            img = cv2.filter2D(img, -1, kernel)
            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
            img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)     
            
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            img_hsv[:,:,1] = np.uint8(np.clip(img_hsv[:,:,1] * 1.7, 0, 255))
            img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
            op_path = os.path.join(output_path, name)
            cv2.imwrite(op_path, img)
            pqs.update(1)
            pqs.set_postfix({"Progress": f"{(i + 1) / tot_img * 100:.1f}%"})

solve()
