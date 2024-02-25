from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")  # 写入logs文件夹下

image_path = "F:\\pythonProject\\Learning-torch\\data\\train\\bees_image\\29494643_e3410f0d37.jpg"

img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(img_array.shape)

writer.add_image("test", img_array, 2, dataformats='HWC')
'''
参数:
tag (str):数据标识符
img_tensor(torch。tensor,numpy。narray(或string/blobname):图像数据
global_step (int):记录的全局步长值
walltime (float):可选覆盖默认的walltime (time.time())
事件发生后的几秒钟
dataformats (str):表单的图像数据格式规范
CHW, HWC, HW, WH等。
'''

for i in range(100):
    writer.add_scalar("y = x", i, i)  # 标量

# 打开logs的文件：终端命令 tensorboard --logdir=logs  注意文件路径要正确
# tensorboard --logdir=logs --port=6007  重新设置端口
'''
参数:
tag (str):数据标识符
scalar_value (float或string/blobname):要保存的值  # y轴
global_step (int):记录的全局步长值  # x轴
walltime (float):可选覆盖默认的walltime (time.time())
事件发生后的几秒钟
new_style (boolean):是使用新样式(张量字段)还是旧样式
样式(simple_value字段)。新的样式可以导致更快的数据加载。
'''

writer.close()
