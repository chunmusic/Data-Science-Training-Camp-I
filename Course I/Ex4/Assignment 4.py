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
U, s, Vh = np.linalg.svd(X, full_matrices=False)

#print(type(Vh))

new_U = []
new_Vh = []

'''
for i in U:
  
  i = i[i > 0.01]
  new_U.append(i.tolist())

s = s[s > 0.01]

for j in Vh:
  
  j = j[j > 0.01]
  new_Vh.append(j.tolist())
  

UU = np.asarray(new_U)

VVh = np.asarray(new_Vh)

Us = np.dot(UU , np.diag(s))
#UsVh = np.dot(Us, np.asarray(VVh))



s = s[s > 0.01]
Vh = Vh[Vh > 0.01]

'''


Us = np.dot(U, np.diag(s))
UsVh = np.dot(Us, Vh)

print(UsVh)s


# No. 3
print("\nPerforming Factor Analysis on cars dataset")

print(f"Number of components: {...}")


# 4
print("\nPerforming PCA on cars dataset")

print(f"Number of optimal components: {...}")


# 5
print("\nPerforming t-SNE algorithm on cars dataset")

#plt.show()


# 6
print("\nPerforming k-clustering on cars dataset (k=3)")


# 7
print("\nPerforming DBScan on cars dataset")


# 8
print("\nPerforming agglomerative clustering on cars dataset")

print("Cross-tabulation:")