import torch
import numpy as np

# Torch Tensor与Numpy array共享底层内存空间，改变其中一个的值，另一个也会随之改变
a = torch.ones(5)
print(a)

# Tensor转Numpy array
b = a.numpy()
print(b)
print(type(b))

a.add_(1)  # 就地加法，a + 1 赋值给a
print("a:", a)
print("b:", b)

# Numpy array转Tensor
a = np.ones(5)
print("a:", a)

b = torch.from_numpy(a)
print("b:", b)

print('-' * 10)
np.add(a, 1, out=a)
print("a:", a)
print("b:", b)

print('-' * 10)
# cuda Tensor可以用.to()方法来将其移动到任意设备上
x = torch.randn(1)
if torch.cuda.is_available():
    # 定义一个设备对象
    device = torch.device("cuda")
    # 在GPU上创建一个Tensor
    y = torch.randn_like(x, device=device)  # like 指形状相同
    # y = torch.ones_like(x, device=device)  # like 指形状相同
    # 将在CPU上的x张量移动到GPU上
    x = x.to(device)
    # x,y都在GPU上，才能进行加法运算
    print("x:", x)
    print("y:", y)

    print("x + y:", x + y)
