import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plb

homes_table = pd.io.parsers.read_csv("homes.csv")

x = homes_table[["List"]].values
y = homes_table[["Age"]].values

#areas_binned = pd.cut(homes_table['Acres'], q=6)
areas_binned = pd.cut(homes_table['Acres'], bins=6, labels=False)
areas_v = areas_binned.values
areas_v = (areas_v+1)*100

plt.scatter(x, y, s=areas_v, marker='s', c='black')

z = np.polyfit(x.flatten(), y.flatten(), 1)
p = np.poly1d(z)
plb.plot(x, p(x), 'k-')

print(areas_v)

plt.show()