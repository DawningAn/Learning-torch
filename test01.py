# -*- coding = utf-8 -*-
# @Time : 2022/4/17 17:43
# @Author : Juyi
# @File : test01.py
# @Software : PyCharm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# cv 绘制的简单操作

# 创建一个空白图像

img = np.zeros((512, 512, 3), np.uint8)
# 绘制图形
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX  # FONT_HERSHEY_SCRIPT_COMPLEX  FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
# 图像展示
# OpenCV 使用 BGR 格式，matplotlib/PyQt 使用 RGB 格式。使用 matplotlib/PyQt 显示 openCV 图像，要将 BGR 格式转换为 RGB 格式
plt.imshow(img)  # [:, :, ::-1]
# plt.title('result', plt.xticks([]), plt.yticks([]))
plt.show()
