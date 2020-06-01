# Plot A

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dir_budget.csv")

df = df.groupby("title_year").describe()
#print(df["budget"]["count"])

fig = plt.figure()

plt.xlabel('Year')
plt.ylabel('Number of movies')

fig.suptitle('Plot A', fontsize=20)

labels = "number of movie"
handles = [plt.Rectangle((4,4),2,2, color='black')]
plt.legend(handles, labels)

plt.annotate(xy=[2015,50], s="Highest", size=9)


plt.bar(df.index,df["budget"]["count"], color = 'black')

plt.show()




# Plot B

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dir_budget.csv")

df_director = df["director_name"].values

#print(df_director)

james = df.loc[df["director_name"]== "James Cameron"]
nolan = df.loc[df["director_name"]== "Christopher Nolan"]

#print(james)
#print(nolan)

james_1990_1994 = 0
james_1995_1999 = 0
james_2000_2004 = 0
james_2005_2009 = 0
james_2010_2014 = 0
james_2015_2019 = 0

nolan_1990_1994 = 0
nolan_1995_1999 = 0
nolan_2000_2004 = 0
nolan_2005_2009 = 0
nolan_2010_2014 = 0
nolan_2015_2019 = 0


for i in james["title_year"]:
  if (i >= 1990 and i <= 1994):
    james_1990_1994 = james_1990_1994 + 1
  if (i >= 1995 and i <= 1999):
    james_1995_1999 = james_1995_1999 + 1
  if (i >= 2000 and i <= 2004):
    james_2000_2004 = james_2000_2004 + 1
  if (i >= 2005 and i <= 2009):
    james_2005_2009 = james_2005_2009 + 1
  if (i >= 2010 and i <= 2014):
    james_2010_2014 = james_2010_2014 + 1
  if (i >= 2015 and i <= 2019):
    james_2015_2019 = james_2015_2019 + 1


for i in nolan["title_year"]:
  if (i >= 1990 and i <= 1994):
    nolan_1990_1994 = nolan_1990_1994 + 1
  if (i >= 1995 and i <= 1999):
    nolan_1995_1999 = nolan_1995_1999 + 1
  if (i >= 2000 and i <= 2004):
    nolan_2000_2004 = nolan_2000_2004 + 1
  if (i >= 2005 and i <= 2009):
    nolan_2005_2009 = nolan_2005_2009 + 1
  if (i >= 2010 and i <= 2014):
    nolan_2010_2014 = nolan_2010_2014 + 1
  if (i >= 2015 and i <= 2019):
    nolan_2015_2019 = nolan_2015_2019 + 1


james_list = [james_1990_1994,james_1995_1999,james_2000_2004,james_2005_2009,james_2010_2014,james_2015_2019]
nolan_list = [nolan_1990_1994,nolan_1995_1999,nolan_2000_2004,nolan_2005_2009,nolan_2010_2014,nolan_2015_2019]

year = ["1990-1994","1995-1999","2000-2004","2005-2009","2010-2014","2015-2019"]

df_j = pd.DataFrame(james_list, index= year)
df_n = pd.DataFrame(nolan_list, index= year)

#df_f = pd.DataFrame(data=[year,james_list], columns=columns, dtype='float')

#binned_year = pd.cut(df["title_year"], bins=5, labels=False)

#print(year)

fig = plt.figure()

plt.xlabel('Year')
plt.ylabel('Number of movies')

fig.suptitle('Plot B', fontsize=20)

# Place a legend to the right of this smaller subplot.



plt.annotate(xy=[3,3], s="Highest", size=10)

plt.plot(df_j,ls='-', color='black', marker='o',label = "James Cameron")
plt.plot(df_n,ls='-', color='orange', marker='s',label = "Christopher Nolan")
plt.legend(bbox_to_anchor=(.40, 0.9), loc='upper right', borderaxespad=0.)


plt.show()





# Plot C


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dir_budget.csv")


df_name = df.groupby("director_name").sum()

df_budget = df_name.sort_values(['budget'], ascending=False).groupby('budget').head(10)

df_budget = df_budget.head(10)


fig = plt.figure()


value = df_budget['budget']
colors = ['black','dimgray','dimgrey','gray','grey','darkgray','darkgrey','silver','lightgray','lightgrey']
labels = df_budget.index
explode = [0.3, 0.3, 0.3, 0.1 ,0.1 ,0.1,0.1, 0.1, 0.1, 0.1]

patches, texts, autotexts = plt.pie(value, colors=colors, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True)

for autotext in autotexts:
    autotext.set_color('white')

fig.suptitle('Plot C: Total Cost', fontsize=15)

plt.legend(bbox_to_anchor=(1.55, 1), loc='upper left', borderaxespad=0.)



plt.show()




# Plot D


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plb

df = pd.read_csv("dir_budget.csv")
fig = plt.figure()


x = df[["budget"]].values
y = df[["imdb_score"]].values

plt.xlabel('Budget')
plt.ylabel('IMBD Score')

plt.scatter(x, y, s=[100], marker='x', c='orange')

z = np.polyfit(x.flatten(), y.flatten(), 1)
p = np.poly1d(z)
plb.plot(x, p(x), 'k-')

fig.suptitle('Plot D', fontsize=20)

labels = "D"
handles = [plt.Rectangle((4,4),2,2, color='black')]
plt.legend(handles, labels)



plt.show()








