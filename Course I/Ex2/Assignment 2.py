# Plot A

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dir_budget.csv")

plt.xlabel('Months')
plt.ylabel('Number of movies')

plt.xticks(range(1,13),df[["Month"]].values.flatten())


plt.bar(range(1,13),df[["movie"]].values)

plt.show()


# Plot B