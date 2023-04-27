import torch

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y)
print(torch.exp(x))

print('--------------------')

X = torch.arange(12, dtype=torch.float32).reshape((-1, 4))
Y = torch.tensor([
    [2.0, 1, 4, 3],
    [1, 2, 3, 4],
    [4, 3, 2, 1]
])
print(torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1))

print('--------------------')

print(X == Y)
print(X < Y)
print(X > Y)
print(X.sum())

print('--------------------')

# 广播方法
a = torch.arange(6).reshape((3, 1, 2))
b = torch.arange(2).reshape((1, 2))
print(a, b)
print(a + b)

print('--------------------')

# 索引
print(X)
print(X[-1], X[1:3], X[-1, 3])
X[1, 2] = 9
print(X)
