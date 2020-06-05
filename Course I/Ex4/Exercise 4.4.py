# Exercise 4.4

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
evr = pca.explained_variance_ratio_

print(f'Explained variance {evr}')

# No.2

from sklearn.cluster import KMeans
clustering = KMeans(n_clusters=16, n_init=16, random_state=1)

clustering.fit(Cx)

import numpy as np
ms = np.column_stack((ground_truth,clustering.labels_))
df =  pd.DataFrame(ms, columns = ['Ground truth', 'Clusters'])
ctab = pd.crosstab(df['Ground truth'], df['Clusters'], margins=True)

print(ctab)


# No.3

from sklearn.cluster import KMeans
import numpy as np

inertia = list()
for k in range(10, 30):
  clustering = KMeans(n_clusters=k,
                      n_init=16, random_state=1)
  clustering.fit(Cx)
  inertia.append(clustering.inertia_)
delta_inertia = np.diff(inertia) * (-1)


# No.4

import matplotlib.pyplot as plt
plt.figure()
x_range = [k for k in range(11, 30)]
plt.xticks(x_range)
plt.plot(x_range, delta_inertia, 'ko-')
plt.xlabel('Number of clusters')
plt.ylabel('Rate of change of inertia')
plt.show()