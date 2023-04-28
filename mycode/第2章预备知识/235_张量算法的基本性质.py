import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()
print(A, A+B)
print(A * B)



