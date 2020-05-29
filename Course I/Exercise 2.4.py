# Exercise 2.4 No. 1

import pandas as pd
import matplotlib.pyplot as plt

mlb_player_table = pd.io.parsers.read_csv("mlb_players.csv")

values = mlb_player_table[["Age"]].values
no_of_bins = 20

plt.hist(values, no_of_bins, histtype='step',
align='mid', color='g')

plt.title("MLB Players Age")

plt.show()



# Exercise 2.4 No. 2

import pandas as pd
import matplotlib.pyplot as plt

mlb_player_table = pd.io.parsers.read_csv("mlb_players.csv")

values = mlb_player_table[["Height(inches)"]].values

plt.boxplot(values, sym='b+', widths=.5)

plt.title("MLB Players Height")

plt.show()