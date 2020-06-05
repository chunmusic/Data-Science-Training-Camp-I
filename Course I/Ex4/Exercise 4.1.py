# Exercise 4.1


# 1
import numpy as np
import pandas as pd

print("This is the original matrix A:")

df = pd.read_csv("homes.csv")

A = df.values

print(A)

# 2

print("The matrix U, s, and Vh of the SVD are as follows:")

U, s, Vh = np.linalg.svd(A, full_matrices=False)

print("Data U")
print(U)
print("Data s")
print(s)
print("Data Vh")
print(Vh)


# 3
print("By deleting three columns from U, s, and Vh, we get the following reconstructed matrix:")


Us = np.dot(U[:,:6], np.diag(s[:6]))
UsVh = np.dot(Us, Vh[:6,:])

print(np.round(UsVh,1))