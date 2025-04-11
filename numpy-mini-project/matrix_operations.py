import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Matrix multiplication
product = np.dot(A, B)

# Transpose
transpose_A = np.transpose(A)

# Inverse
inverse_A = np.linalg.inv(A)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Dot Product:\n", product)
print("Transpose of A:\n", transpose_A)
print("Inverse of A:\n", inverse_A)
