# Exercise 2.4 No. 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

mlb_player_table = pd.io.parsers.read_csv("mlb_players.csv")

values = mlb_player_table[["Age"]].values
no_of_bins = 20

#plt.hist(values, no_of_bins, histtype='step',
#align='mid', color='g')

plt.title("MLB Players Age")

sns.distplot(mlb_player_table['Age'], hist=True, kde=True, 
             bins=no_of_bins, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
             
plt.show()




# Exercise 2.4 No. 2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mlb_player_table = pd.io.parsers.read_csv("mlb_players.csv")

values = mlb_player_table[["Height(inches)"]].values
df = mlb_player_table[["Height(inches)"]]

plt.boxplot(values, sym='b+', widths=.5)

#tips = sns.load_dataset(values)
ax = sns.swarmplot(data=values, zorder=0)
sns.boxplot(data=values, 
                 showcaps=False,boxprops={'facecolor':'None'},
                 showfliers=False,whiskerprops={'linewidth':0}, ax=ax)

plt.title("MLB Players Height")

plt.show()


