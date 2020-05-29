# Exercise 2.3 No. 1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.io.parsers.read_csv("airtravel.csv")

value = df[["1958"]]
colors = ['c','c','c','c','c','c','b','b','c','c','c','c']
labels = df.Month
explode = [0.1, 0.1, 0.1, 0.1 ,0.1 ,0.1,0.2, 0.2, 0.1, 0.1 ,0.1 ,0.1]

plt.pie(value, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%', shadow=True)
plt.title('Number of flights in 1958')

plt.show()


# Exercise 2.3 No. 2

import pandas as pd
import matplotlib.pyplot as plt

df = pd.io.parsers.read_csv("airtravel.csv")
df = df.drop(["Month"], 1)
df_sum = pd.DataFrame(df.sum())

#print(df_sum)

x_coord = range(0,len(df_sum))
values = df_sum[0]
colors = ['c' for i in x_coord]
widths = [0.6 for i in x_coord]

plt.xticks(x_coord,df_sum.index)

plt.ylabel('Sum of flights')

plt.bar(x_coord,values,color=colors, width=widths)
plt.show()

