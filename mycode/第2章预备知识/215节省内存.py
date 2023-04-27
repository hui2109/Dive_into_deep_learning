import torch

X = torch.arange(12, dtype=torch.float32).reshape((-1, 4))
Y = torch.tensor([
    [2.0, 1, 4, 3],
    [1, 2, 3, 4],
    [4, 3, 5, 1]
])
before = id(Y)
# Y = Y + X
# Y += X
Y[:] = Y + X
print(id(Y) == before)
