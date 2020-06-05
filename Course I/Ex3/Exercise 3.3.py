# Exercise 3.3

#1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("homes.csv")

boxplots = df.boxplot(column='Baths', 
            fontsize=6, rot=90)

#plt.suptitle("")
plt.show()

print("Boxplot Categorized by the Number of Bathrooms:")



#2
#var_1_bathroom=
#var_2_bathroom=

print("Performing t-tests on houses 'Sell' price with 1 and 2 bathroom:")

import pandas as pd
#import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv("homes.csv")

group1 = df["Baths"] == 1
group2 = df["Baths"] == 2

variable = df["Sell"]
variance1 = variable[group1].var()
variance2 = variable[group2].var()

print(f"'1 Bathroom' Variance: {variance1}")
print(f"'2 Bathroom' Variance: {variance2}")

t, pvalue = ttest_ind(variable[group1], variable[group2],
            axis=0, equal_var=False)

print(f"t statistic {t}")
print(f"p-value {pvalue}")



#print("Conclusion: ...")



#3 
print("One-way ANOVA test on on houses land area ('Acres') with 1, 2, and 3 bathrooms:")


import pandas as pd
from scipy.stats import f_oneway

df = pd.read_csv("homes.csv")

group1 = df["Baths"] == 1
group2 = df["Baths"] == 2
group3 = df["Baths"] == 3

variable = df["Acres"]

f, pvalue = f_oneway(variable[group1],
                     variable[group2],
                     variable[group3])

print(f"One-way ANOVA F-value {f}")
print(f"p-value {pvalue}")



#print("Conclusion: ...")
