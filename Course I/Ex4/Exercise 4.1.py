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

np.set_printoptions(suppress=True)
s_percentage = (s/sum(s)*100).round(2)

print(s_percentage)


# 3
print("By deleting three columns from U, s, and Vh, we get the following reconstructed matrix:")


k = 6

old_df = df.values
new_df = np.round(np.dot(np.dot(U[:,:k], np.diag(s[:k])),Vh[:k,:]),1)

print(old_df[:2,:2])
print(new_df[:2,:2])