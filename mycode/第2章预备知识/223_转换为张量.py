import os

import pandas as pd
import torch

data_file = os.path.join('..', 'resource', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
inputs = pd.get_dummies(inputs, dummy_na=True)

# 转换为张量
X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X, y)
