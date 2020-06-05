# Exercise 4.3

# No.1

import pandas as pd

data = pd.read_csv('data.txt', sep="   ", header=None)
truth = pd.read_csv('ground_truth.txt', header=None)

X = data.values
ground_truth = truth.values.flatten()

import imp
from sklearn.manifold import TSNE
tsne = TSNE(init='pca',
            perplexity=50, # Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50.
            early_exaggeration=25, # For larger values, the space between natural clusters will be larger in the embedded space. Again, the choice of this parameter is not very critical.
            n_iter=300 # Maximum number of iterations for the optimization. Should be at least 250.
            )

Tx = tsne.fit_transform(X)

print(Tx)

# No.2

import numpy as np
import matplotlib.pyplot as plt
plt.xticks([], [])
plt.yticks([], [])
for target in np.unique(ground_truth):
  selection = ground_truth==target
  X1, X2 = Tx[selection, 0], Tx[selection, 1]
  plt.plot(X1, X2, 'o', ms=3)
  c1, c2 = np.median(X1), np.median(X2)
  plt.text(c1, c2, target, fontsize=18, fontweight='bold')

plt.show()