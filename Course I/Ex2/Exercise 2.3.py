# Exercise 2.3 No. 1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.io.parsers.read_csv("airtravel.csv")


value = df[["1958"]]
colors = ['b','b','b','b','b','b','r','r','b','b','b','b']
labels = df.Month
explode = [0.1, 0.1, 0.1, 0.1 ,0.1 ,0.1,0.3, 0.3, 0.1, 0.1 ,0.1 ,0.1]

patches, texts, autotexts = plt.pie(value, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%', shadow=True)

for autotext in autotexts:
    autotext.set_color('white')

plt.title('Number of flights in 1958')



plt.show()




# Exercise 2.3 No. 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.io.parsers.read_csv("airtravel.csv")
df = df.drop(["Month"], 1)
df_sum = pd.DataFrame(df.sum())

#print(df_sum)

x_coord = range(0,len(df_sum))
values = df_sum[0]
colors = ['c' for i in x_coord]
widths = [0.6 for i in x_coord]

fig, ax = plt.subplots()

plt.xticks(x_coord,df_sum.index)

plt.ylabel('Sum of flights')

yy = df_sum[0].values

for index,data in enumerate(yy):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=20))
plt.tight_layout()

plt.ylim(ymin=4000, ymax= 6000)

ax.yaxis.set_ticks(np.arange(4000, 6000, 200))

plt.bar(x_coord,values,color=colors, width=widths)
plt.show()

