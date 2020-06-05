# Student No.: COIM4022
# Assignment III

# No. 1
import pandas as pd
import numpy as np
from scipy.stats import skew, skewtest
from scipy.stats import kurtosis, kurtosistest



df = pd.read_csv("dir_budget.csv")

imdb = df["imdb_score"]
budget = df["budget"]

#s = skew(imdb)
#zscore, pvalue = skewtest(imdb)
#print(zscore)
#print(skewtest(imdb)[1])
#print(skewtest(imdb))

print(f"IMDB Mean: {imdb.mean()}\t Median: {imdb.median()}\t Lower Quar.: {imdb.quantile(0.25)}\t Upper Quar.:{imdb.quantile(0.75)}")
print(f"IMDB Skewness: {skew(imdb)}\tp-value: {skewtest(imdb)[1]}\tz-score: {skewtest(imdb)[0]}")
print(f"IMDB Kurtosis: {kurtosis(imdb)}\tp-value: {kurtosistest(imdb)[1]}\tz-score: {kurtosistest(imdb)[0]}")

print(f"\nBudget Mean: {budget.mean()}\t Median: {budget.median()}\t Lower Quar.: {budget.quantile(0.25)}\t Upper Quar.:{budget.quantile(0.75)}")
print(f"Budget Skewness: {skew(budget)}\tp-value: {skewtest(budget)[1]}\tz-score: {skewtest(budget)[0]}")
print(f"Budget Kurtosis: {kurtosis(budget)}\tp-value: {kurtosistest(budget)[1]}\tz-score: {kurtosistest(budget)[0]}")


# No. 2

import math

print("\nMovies Frequency per floored IMDB Score")

floor = np.floor(df["imdb_score"])

#print(player_table["Position"].value_counts())

print(floor.value_counts())


# No. 3

budget_binned = pd.qcut(df["budget"], q=10, precision=0)

print(budget_binned.value_counts())



# No. 4
print("\nContingency table of IMDB score (floored) vs Budget Intervals")


vs = pd.crosstab(floor,budget_binned,normalize='columns')*100

pd.set_option('display.max_columns',5)

print(vs)



# No. 5
from scipy.stats import ttest_ind

group1 = floor == 6
group2 = floor == 7

variable = df["budget"]
variance1 = variable[group1].var()
variance2 = variable[group2].var()

t, pvalue = ttest_ind(variable[group1], variable[group2],
            axis=0, equal_var=False)

print(f"\nBudget variance of IMDB score of 6 (floored): {variance1}")
print(f"Budget variance of IMDB score of 7 (floored): {variance2}")

print("\nt-test result of budget used in movies with IMDB score of 6 and 7")
print(f"t statistic: {t}\tp-value: {pvalue}")

if pvalue < 0.05:
  print("Since pvalue < 5%, the two means are significantly different.")
else:
  print("Since pvalue > 5%, we cannot say that the two means are significantly different.")



# No. 6

from scipy.stats import f_oneway

group5 = floor == 5
group6 = floor == 6
group7 = floor == 7
group8 = floor == 8


variable = df["budget"]

f, anova_pvalue = f_oneway(variable[group5],
                     variable[group6],
                     variable[group7],
                     variable[group8])

print("\nOne-way ANOVA on budget used for movies with IMDB score of 5, 6, 7, and 8 (floored)")
print(f"F value: {f}\t\tp-value: {anova_pvalue}")


if anova_pvalue < 0.05:
  print("Since pvalue < 5%, the four means are significantly different.")
else:
  print("Since pvalue > 5%, we cannot say that the four means are significantly different.")



# No. 7

print("\nCovariance Table:")

df = pd.read_csv('dir_budget.csv')

df_drop = df.drop(['director_expense'],axis=1)

print(df_drop.corr()) 
print("\nCorrelation Table:")

print(df_drop.corr()) 


# No. 8

import imp 
from scipy.stats import spearmanr
from scipy.stats.stats import pearsonr

a = df["imdb_score"]
b = df["budget"]
#print(a)
rho_coef, rho_p = spearmanr(a, b)
r_coef, r_p = pearsonr(a, b)

print("\nCorrelation of IMDB score vs budget")
print(f"Pearson: {r_coef}")
print(f"Spearman: {rho_coef}")


# No. 9
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(vs.values)
print(f'Chi-square {chi2}   p-value {p}') 

print("\nChi-square test on IMDB score (floored) vs Budget Intervals")
print(f"Chi-square: {chi2}\t\tp-value: {p}")

if p < 0.05: 
  print("Since pvalue < 5%, the budget intervalse can be effectively used for\ndistinguishing between IMDB scores.")
else:
  print("Since pvalue > 5%, we cannot say that the budget intervalse can be\n effectively used fordistinguishing between IMDB scores.")


# No. 10

from sklearn.preprocessing import scale

imdb_score = df['imdb_score'].values
imdb_scale = scale(imdb_score)

budget = df['budget'].values
budget_scale = scale(budget)

from scipy.stats.stats import pearsonr

transformations = {'x': lambda x: x,
                  '1/x': lambda x: 1/x,
                  'x**(1/2)': lambda x: x**(1/2),
                  'x**(1/3)': lambda x: x**(1/3),
                  'x**2': lambda x: x**2, 
                  'log10(x)': lambda x: np.log10(x),
                  'log(x)': lambda x: np.log(x),
                  'log2(x)': lambda x: np.log2(x),
                   }

a = imdb_score
b = budget

print("\nTransformed Correlation of IMDB score and budget:")

for tformation in transformations:
  b_transformed = transformations[tformation](b)
  pearsonr_coef, pearsonr_p = pearsonr(a, b_transformed)
  print(f"Transformation: {tformation}\t Pearson's r: {pearsonr_coef:.3f}")
  

print("\nAfter scaling of IMDB score and budget,")
print(f"the transformation x gives the highest Pearson's r correlation.")
