# Exercise 4.1


# 1
import numpy as np
import pandas as pd

print("This is the original matrix A:")

df = pd.read_csv("homes.csv")
A = df.columns.values
print(A)

# 2

print("The matrix U, s, and Vh of the SVD are as follows:")

U, s, Vh = np.linalg.svd(A, full_matrices=False)

print(np.shape(U), np.shape(s), np.shape(Vh))
print("Data U")
print(U)
print("Data s")
print(s)
print("Data Vh")
print(Vh)


# 3
print("By deleting three columns from U, s, and Vh, we get the following reconstructed matrix:")
