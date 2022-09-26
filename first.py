# -*- coding = utf-8 -*-
# @Time : 2022/4/17 17:06
# @Author : Juyi
# @File : first.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import cv2 as cv
# import numpy as np

lena = cv.imread("F:\Picture\he.png", 0)  # 读取路径下的图片

# 读取图像的三种不同参数，1， 0， -1
# 1 表示彩色模式加载图像，任何图像的透明度都将被忽略。也是默认参数
# 0 表示以灰度模式加载图像
# -1 表示包括alpha通道的加载图像模式
# 在 openCV中显示
cv.imshow("image", lena)  # 显示图像的窗口名称和要加载的图像

cv.waitKey(0)  # 表示给图像留下的绘制时间，0 则代表永远等待下去

# cv.imwrite(r'F:\Picture\test02.png', lena)  # 文件名和保存位置，还有要保存的图像

# 在 matplotlib 中展示
# plt.imshow(lena)
# plt.show()

