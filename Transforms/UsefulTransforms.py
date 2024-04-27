from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter


writer = SummaryWriter("logs")
img = Image.open("../data/val/ants/800px-Meat_eater_ant_qeen_excavating_hole.jpg")

trans_totensor = transforms.ToTensor()

img_tensor = trans_totensor(img)

writer.add_image("img", img_tensor)

# Normalize

trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
writer.close()