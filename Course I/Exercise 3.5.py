# Exercise 3.5

# 1

import pandas as pd

df = pd.read_csv('homes.csv')

import imp
from sklearn.preprocessing import scale

sell_variable = df['Sell'].values
sell_scale = scale(sell_variable)
print("SALE")
print(sell_scale)

tax_variable = df['Taxes'].values
tax_scale = scale(tax_variable)
print("TAXES")
print(tax_scale)



# 2

import numpy as np
from scipy.stats.stats import pearsonr

transformations = {'x': lambda x: x,
                  '1/x': lambda x: 1/x,
                  'x**2': lambda x: x**2,
                  'x**3': lambda x: x**3,
                  'log(x)': lambda x: np.log(x)}

a = df['Sell'].values
b = df['Taxes'].values

for transformation in transformations:
  b_transformed = transformations[transformation](b)
  pearsonr_coef, pearsonr_p = pearsonr(a, b_transformed)
  print(f'Transformation: {transformation} \t Pearson\'s r: {pearsonr_coef:.3f}')