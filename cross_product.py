import numpy as np

matrix1 = np.array([[1, 2, 3],                           # Create two matrices (2D arrays)
                    [4, 5, 6]])
matrix2 = np.array([[7, 8, 9],
                    [10, 11, 12]])
cross_product = np.cross(matrix1, matrix2, axis=1)      # Compute the cross-product along the second axis (axis=1)
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nCross-product along the second axis:")
print(cross_product)

