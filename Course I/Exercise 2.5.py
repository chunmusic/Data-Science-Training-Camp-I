# Exercise 2.5

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plb

homes_table = pd.io.parsers.read_csv("homes.csv")

x = homes_table[["List"]].values
y = homes_table[["Age"]].values

plt.scatter(x, y, s=[100], marker='s', c='black')

z = np.polyfit(x.flatten(), y.flatten(), 1)
p = np.poly1d(z)
plb.plot(x, p(x), 'k-')

plt.show()