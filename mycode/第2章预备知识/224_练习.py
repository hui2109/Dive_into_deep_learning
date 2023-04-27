import os

import pandas as pd
import torch

os.makedirs(os.path.join('..', 'resource', 'data'), exist_ok=True)
data_file = os.path.join('..', 'resource', 'data', 'house_tiny_P.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Size,Alley,Price\n')
    f.write('NA,NA,Pave,127500\n')
    f.write('2,120,NA,106000\n')
    f.write('4,89,NA,178100\n')
    f.write('NA,NA,NA,140000\n')

data = pd.read_csv(data_file)
print(data)
data = data.drop(data.isna().sum(axis=0).idxmax(), axis=1)
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
inputs = pd.get_dummies(inputs, dummy_na=True)

# 转换为张量
X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X, y)
