# Exercise 3.4

# 1

import pandas as pd

df = pd.read_csv('homes.csv')
print("correlation for all variables in homes:")

print(df.corr())

# 2

import imp
from scipy.stats import spearmanr
from scipy.stats.stats import pearsonr

a = df['Sell']
b = df['Taxes']

rho_coef, rho_p = spearmanr(a, b)
r_coef, r_p = pearsonr(a, b)

print("Spearman and Pearson's correlation between Sell and Taxes.")

print(f'Pearson r: {r_coef}')
print(f'Spearman r: {rho_coef}')


# 3

print("Sell, list, area, and taxes columns (binned):")

pcts = [0, .2, .4, .6, .8, 1]

homes_binned = pd.concat(
  [pd.qcut(df.iloc[:,1], pcts, precision=1),
  pd.qcut(df.iloc[:,2], pcts, precision=1),
  pd.qcut(df.iloc[:,7], pcts, precision=1),
  pd.qcut(df.iloc[:,8], pcts, precision=1)],
  join='outer', axis=1)

print(homes_binned)


# 4
print("Contingecy table:")

import imp
from scipy.stats import chi2_contingency

table = pd.crosstab(df['Rooms'], homes_binned['Taxes'])

print(table)

#5
print("Chi-square test:")

chi2, p, dof, expected = chi2_contingency(table.values)
print(f'Chi-square {chi2}   p-value {p}')




