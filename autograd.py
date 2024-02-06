import torch

x1 = torch.ones(4, 4)
print(x1)

# 如果将.requires_grad设置为True，它将追踪在这个类上定义的所有操作。当代码要反向传播时，直接调用.backward()就可以自动计算所有梯度
# 在这个Tensor上的所有梯度将被累加进属性.grad中
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)

z = x * 2
print(z)
# grad_fn属性
# Tensor若是用户自定义的，则其对应的grad_fn is None
print(x.grad_fn)
print(y.grad_fn)
print(z.grad_fn)

z = y * y * 3
out = z.mean()
print(z, out)

a = torch.randn(2, 2)
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)

out.backward()
print(x.grad)
