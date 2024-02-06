import torch

x = torch.randn(4,4)
print(x)

y = x.view(16)
print(y)

z = x.view(-1, 8)
print(z)

print(x.size(), y.size(), z.size())

# 如果张量中只有一个元素，可以用.item() 将值取出，作为一个python number
x = torch.randn(1)
print(x)
print(x.item())

