import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = torch.ones(4, 3)
print(A, B, sep='\n')
print(torch.mm(A, B))
