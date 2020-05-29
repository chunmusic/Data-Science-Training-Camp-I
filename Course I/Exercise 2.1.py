# Exercise 2.1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("airtravel.csv")

ax = plt.axes()
ax.grid(ls = '--')

plt.xticks(range(1,13),df[["Month"]].values.flatten())

plt.plot(range(1,13),df[["1958"]].values, 
         ls='-', color='r', marker='s')
plt.plot(range(1,13),df[["1960"]].values, 
         ls='--', color='b', marker='o')
plt.show()