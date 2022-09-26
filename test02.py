# -*- coding = utf-8 -*-
# @Time : 2022/4/17 20:13
# @Author : Juyi
# @File : test02.py
# @Software : PyCharm


# 获取并修改图像中的像素点
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = np.zeros((256, 256), np.uint8)
plt.imshow(img)
plt.show()
# B G R 通道
# img = cv.imread("F:\Picture\he.png")
# # 获取某个像素点的值
# px = img[100, 100]
# # 仅获取某个像素点的值
# bule = img[100, 100, 0]
# # 修改某个位置的像素值
# img[100, 100] = [255, 255, 255]
