import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
x = torch.arange(4, dtype=torch.float32)
print(A, x, A.shape, x.shape)
print(torch.mv(A, x))


