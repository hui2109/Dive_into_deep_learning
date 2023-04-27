import os

import pandas as pd

data_file = os.path.join('..', 'resource', 'data', 'house_tiny.csv')
data = pd.read_csv(data_file)
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
print(inputs)

print('--------------------')

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
