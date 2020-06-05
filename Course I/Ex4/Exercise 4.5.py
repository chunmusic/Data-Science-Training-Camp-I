# Exercise 4.5

# No.1

import pandas as pd

data = pd.read_csv('data.txt', sep="   ", header=None)
truth = pd.read_csv('ground_truth.txt', header=None)

X = data.values
ground_truth = truth.values

import imp
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

pca = PCA(n_components=30)
Cx = pca.fit_transform(scale(X))

# No.2

from sklearn.cluster import DBSCAN
import numpy as np
DB = DBSCAN(eps=373, min_samples=65)

DB.fit(Cx)

from collections import Counter
print(f'No. clusters: {len(np.unique(DB.labels_))}')
print(Counter(DB.labels_))

ms = np.column_stack((ground_truth,DB.labels_))
df = pd.DataFrame(ms,
                  columns = ['Ground truth', 'Clusters'])
print(pd.crosstab(df['Ground truth'], df['Clusters'], margins=True))
