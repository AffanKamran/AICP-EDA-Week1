import numpy as np
matrix_3x3 = np.array([[4, 7, 2],
                       [5, 3, 1],
                       [9, 0, 8]])

determinant_value_3x3 = np.linalg.det(matrix_3x3)

print("Matrix (3x3):")
print(matrix_3x3)

print("\nDeterminant:")
print(determinant_value_3x3)