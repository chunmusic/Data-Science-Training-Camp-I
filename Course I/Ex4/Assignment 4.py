# Student No.: C0IM4022
# Assignment IV

# No. 1
import pandas as pd
import numpy as np

df = pd.read_csv("cars.csv", sep=';',index_col='Car')

X = df.drop(columns='Origin')
print(X)

y = df['Origin']
print(y)



# No. 2
print("\nPerforming SVD on cars dataset")

U, s, Vh = np.linalg.svd(X, full_matrices=False)
np.set_printoptions(suppress=True)
s_percentage = (s/sum(s)*100).round(2)

print("U")
print(U)
print("s")
print(s)
print("Vh")
print(Vh)

print("\ns_percentage")
print(s_percentage)

print("\nReconstructed data:")

k = 2

old_df = df.values
new_df = np.round(np.dot(np.dot(U[:,:k], np.diag(s[:k])),Vh[:k,:]),1)

#print(old_df)
print(new_df)


# No. 3

print("\nPerforming Factor Analysis on cars dataset")

import imp
from sklearn.decomposition import FactorAnalysis
factor = FactorAnalysis(n_components=6).fit(X)

cols = df.columns.tolist()

factor_comp = np.round(factor.components_,3)

print(pd.DataFrame(factor_comp,columns=cols[1:]))

print(f"Number of components: 6")


# 4
print("\nPerforming PCA on cars dataset")

from sklearn.decomposition import PCA
pca = PCA().fit(X)
evr = pca.explained_variance_ratio_
pca_comp = np.round(pca.components_,3)

print(f'Explained variance by each component:\n {evr}')

print(pd.DataFrame(pca_comp,columns=cols[1:]))

print(f"Number of optimal components: 1")


# 5

print("\nPerforming t-SNE algorithm on cars dataset")

import imp
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
tsne = TSNE(init='pca',
            perplexity=50, # Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50.
            early_exaggeration=500, # For larger values, the space between natural clusters will be larger in the embedded space. Again, the choice of this parameter is not very critical.
            n_iter=1000 # Maximum number of iterations for the optimization. Should be at least 250.
            )

df = pd.read_csv("cars.csv", sep=';',index_col='Car')

X = df.drop(columns='Origin').values

y = df['Origin']


y = y.values.flatten()


Tx = tsne.fit_transform(X)


plt.xticks([], [])
plt.yticks([], [])
for target in np.unique(y):
  selection = y==target
  X1, X2 = Tx[selection, 0], Tx[selection, 1]
  plt.plot(X1, X2, 'o', ms=3)
  c1, c2 = np.median(X1), np.median(X2)
  plt.text(c1, c2, target, fontsize=18, fontweight='bold')

plt.show()


# 6
print("\nPerforming k-clustering on cars dataset (k=3)")

df = pd.read_csv("cars.csv", sep=';',index_col='Car')

X = df.drop(columns='Origin').values

y = df['Origin']

y = y.values

np.set_printoptions(suppress=True)


import imp
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

pca = PCA(n_components=3)
Cx = pca.fit_transform(scale(X))
evr = pca.explained_variance_ratio_

print(f'Explained variance {evr}')


from sklearn.cluster import KMeans
clustering = KMeans(n_clusters=3, n_init=3, random_state=1)

clustering.fit(Cx)

import numpy as np
ms = np.column_stack((y,clustering.labels_))
df =  pd.DataFrame(ms, columns = ['Origin', 'Clusters'])
ctab = pd.crosstab(df['Origin'], df['Clusters'], margins=True)

print(ctab)



# 7
print("\nPerforming DBScan on cars dataset")
import imp
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

df = pd.read_csv("cars.csv", sep=';',index_col='Car')

X = df.drop(columns='Origin').values

y = df['Origin']

y = y.values

np.set_printoptions(suppress=True)


pca = PCA(n_components=3)
Cx = pca.fit_transform(scale(X))

evr = pca.explained_variance_ratio_

print(f'Explained variance {evr}')


from sklearn.cluster import DBSCAN
import numpy as np
DB = DBSCAN(eps=3, min_samples=10)

DB.fit(Cx)

from collections import Counter
print(f'No. clusters: {len(np.unique(DB.labels_))}')
print(Counter(DB.labels_))

ms = np.column_stack((y,DB.labels_))
df = pd.DataFrame(ms,
                  columns = ['Origin', 'Clusters'])
print(pd.crosstab(df['Origin'], df['Clusters'], margins=True))



# 8
print("\nPerforming agglomerative clustering on cars dataset")


import imp
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

df = pd.read_csv("cars.csv", sep=';',index_col='Car')

X = df.drop(columns='Origin').values

y = df['Origin']

y = y.values

np.set_printoptions(suppress=True)


pca = PCA(n_components=3)
Cx = pca.fit_transform(scale(X))

evr = pca.explained_variance_ratio_

print(f'Explained variance {evr}')


from sklearn.cluster import AgglomerativeClustering
import numpy as np
DB = AgglomerativeClustering(n_clusters=3)

DB.fit(Cx)


print("Cross-tabulation:")

from collections import Counter
print(f'No. clusters: {len(np.unique(DB.labels_))}')
print(Counter(DB.labels_))

ms = np.column_stack((y,DB.labels_))
df = pd.DataFrame(ms,
                  columns = ['Origin', 'Clusters'])
print(pd.crosstab(df['Origin'], df['Clusters'], margins=True))

