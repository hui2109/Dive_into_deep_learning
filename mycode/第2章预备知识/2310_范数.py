import torch

u = torch.tensor([3.0, -4.0])
print(torch.norm(u))  # L2范数
print(torch.abs(u).sum())  # L1范数
print(torch.norm(torch.ones(4, 9)))  # 弗罗贝尼乌斯范数
