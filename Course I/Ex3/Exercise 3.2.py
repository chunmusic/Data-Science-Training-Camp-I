# Exercise 3.2

#1
import pandas as pd

df = pd.io.parsers.read_csv("homes.csv")

print("Number of House for each no. of bathroom:")
print(df["Baths"].value_counts())


#2
print("Number of house for each area:")
area = pd.qcut(df["Acres"], q=10, precision=0)

print(area.value_counts())


#3 

print("Number of bathroom vs Area of the house:")
vs = pd.crosstab(df["Baths"],area)
print(vs)


#4
print("Number of bathroom vs Area of the house (in %):")


vs = pd.crosstab(df["Baths"],area,normalize='columns') * 100

pd.set_option('display.max_columns',5)
print(vs)