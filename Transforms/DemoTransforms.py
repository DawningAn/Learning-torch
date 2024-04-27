from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter

# 1.ToTensor的用法
# 读取图片
img_path = "../data/train/ants_image/0013035.jpg"
img = Image.open(img_path)

tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)  # ctrl + p 显示参数
print(tensor_img)

writer = SummaryWriter("logs")
writer.add_image("tensor_img",tensor_img)  # tensorboard --logdir=Transforms/logs

writer.close()

