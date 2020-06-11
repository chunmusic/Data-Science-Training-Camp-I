# Exercise 5.1
import pandas as pd
import numpy as np

# 1


df = pd.DataFrame(np.random.randn(14, 4),
    index=['a','b','c','d','e','f','g','h','i','j','k','l','m','n'], 
    columns = ['A1', 'A2', 'A3','A4'])

df1 = df.loc[:,['A1','A2','A3']]
print(df1)


# 2

df2 = df1.iloc[:10,:]
print(df2)


# 3

df3 = df2.iloc[::2]
print(df3)


# 4

df4 = df3[(df3['A1']<=0.5) & (df3['A1']>=-0.5)]

print(df4)



# 5
df5 = df4["A3"]
df5 = df5[-1:]

print(df5)
