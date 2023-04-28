import torch

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A, A.shape, A.sum())

print('--------------------')

# 轴0
A_sum_axis0 = A.sum(axis=0)
print(A_sum_axis0, A_sum_axis0.shape)

# 轴1
A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1, A_sum_axis1.shape)

print('--------------------')

# 求均值
print(A.mean(), A.sum() / A.numel())
# 按轴求均值
print(A.mean(axis=0), A.sum(axis=0) / A.shape[0])

print('--------------------')

# 非降维求和
sum_A = A.sum(axis=1, keepdims=True)
print(sum_A)
print(A / sum_A)

print('--------------------')

# 累计总和
print(A.cumsum(axis=0))
