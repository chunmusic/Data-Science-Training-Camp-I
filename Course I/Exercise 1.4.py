# Exercise 1.4
import pandas as pd
import numpy as np

# No. 1

import pandas as pd

df = pd.read_csv("homes.csv")

df = df.replace('-', np.NaN)
print(df)


# No. 2

print(df.isnull())


# No. 3

df["Baths"] = df.replace('NaN', df["Baths"].median())
print(df)


# No. 4

print("No.4")
df = df[df.List.notnull()]
print(df)

# No. 5

print("No5")

index_count = 0
check_null = df.isnull().sum()
print(check_null)
print(len(df.columns))

for i in range(len(df.columns)):
  if check_null[i] >3: 
    print(check_null.index[i])
    remove = check_null.index[i]
    df_drop = df[df[remove].notnull()]


print(df_drop)

# No. 6
print("No.6")
r_df = df_drop.reset_index()
print(r_df)