# Exercise 3.1

#1
import pandas as pd

df = pd.io.parsers.read_csv("homes.csv")

print("Mean Sell:")
print(df[['Sell']].mean(numeric_only=True))

print("Mean List:")
print(df[['List']].mean(numeric_only=True))


#2
print("Median Sell:")
print(df[['Sell']].median(numeric_only=True))

print("Median List:")
print(df[['List']].median(numeric_only=True))


#3 
print("Range Sell:")
print(df[['Sell']].max(numeric_only=True) -
      df[['Sell']].min(numeric_only=True))
print("Range List:")
print(df[['List']].max(numeric_only=True) -
      df[['List']].min(numeric_only=True))

#4
print("10% and 90% Quantile of Sell:")
print(df[['Sell']].quantile([0.1,0.9]))

print("10% and 90% Quantile of List:")
print(df[['List']].quantile([0.1,0.9]))

#5
from scipy.stats import skew, skewtest
from scipy.stats import kurtosis, kurtosistest

variable = df['Sell']

s = skew(variable)
k = kurtosis(variable)


print("Skewness for Sell Price")
print(f'Skewness {s}')


print("Kurtosis for Sell Price")
print(f'Kurtosis {k}')




