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



# Exercise 5.1 B
import pandas as pd

fruit_name = pd.read_csv('fruit_name.csv', index_col='fruitId')
fruit_score = pd.read_csv('fruit_score.csv', index_col='name')

# Fruit name vs Average Score

df1 = fruit_name.loc[:,'fruit_name']
df2 = fruit_score.groupby(['fruitId']).mean()

df = pd.concat([df1, df2], axis=1, sort=False)

print(df)