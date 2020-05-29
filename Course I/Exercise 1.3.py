# Exercise 1.3
# No. 1

import pandas as pd
print("no.1")

df = pd.read_csv("bmi.csv")
print(df.drop_duplicates())

# No. 2

print("no.2")
df = pd.read_csv("bmi.csv")

print("Number of data (original): " + str(len(df)))
df = df.drop_duplicates()
print("Number of data (no duplicates): " + str(len(df)))



# No. 3

print("no.3")
df = pd.read_csv("bmi.csv")

gender_group = df.groupby("Sex").describe().stack()

print(gender_group)


# No. 4

print("no.4")
df = pd.read_csv("bmi.csv")

#gender_group = df.groupby("Sex")

gender_group_desc = df.groupby("Sex").describe()
gen_gr_desc_countmean = gender_group_desc.loc[:,(slice(None),['min','max'])]


print(gen_gr_desc_countmean)