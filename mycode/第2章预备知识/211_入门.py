import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())
print(x.size())

print('--------------------')

X = x.reshape(-1, 4)
print(X)

print('--------------------')

print(torch.zeros(2, 3, 4))
print(torch.randn(3, 4))
