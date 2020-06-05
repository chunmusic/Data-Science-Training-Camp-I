# Exercise 4.2
# Do this exercise in the provided part_A.py and part_B.py ^

#partA

print("This is the result of the Factor Analysis on homes.csv:")

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv('homes.csv')

X = df.values[:,1:]
Y = df.values[:,0]
cols = df.columns.tolist()

import imp

from sklearn.decomposition import FactorAnalysis
factor = FactorAnalysis(n_components=8).fit(X)

factor_comp = np.round(factor.components_,3)

print(pd.DataFrame(factor_comp,columns=cols[1:]))


print("The number of optimal components for this is 8")



#PartB

X = df.values[:,1:]
Y = df.values[:,0]
cols = df.columns.tolist()

import imp
from sklearn.decomposition import PCA
pca = PCA().fit(X)
evr = pca.explained_variance_ratio_
pca_comp = np.round(pca.components_,3)


print(pd.DataFrame(pca_comp,columns=cols[1:]))


print("This is the result of the PCA on homes.csv:")

print("The number of optimal components to keep  is 8")