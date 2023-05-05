import torch

x = torch.arange(4.0)
print(x)
x.requires_grad_(True)
print(x.grad)

y = x * x
print(y)
# y.sum().backward()
y.backward(torch.ones(len(x)))
print(x.grad)

