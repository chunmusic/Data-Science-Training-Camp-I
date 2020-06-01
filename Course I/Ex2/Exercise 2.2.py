# Exercise 2.2

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("airtravel.csv")

ax = plt.axes()
ax.grid(ls = '--')

plt.xlabel('Months')
plt.ylabel('Number of flights')


plt.xticks(range(1,13),df[["Month"]].values.flatten())

plt.plot(range(1,13),df[["1958"]].values, 
         ls='-', color='r', marker='s')
         
plt.plot(range(1,13),df[["1960"]].values, 
         ls='--', color='b', marker='o')
         
plt.annotate(xy=[7,622], s="Summer Holiday", size=9)
plt.annotate(xy=[11,390], s="Thanksgiving", size=9)

ax.set_facecolor('#D3D3D3') 
plt.grid(color='w')

plt.legend(['1958', '1960'], loc=1 ,frameon = False, fancybox = True)


plt.show()


