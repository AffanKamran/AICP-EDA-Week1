import numpy as np

# Create a sample array
sample_array = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

# Compute mean, standard deviation, and variance along the second axis (axis=1)
mean_values = np.mean(sample_array, axis=1)
std_values = np.std(sample_array, axis=1)
variance_values = np.var(sample_array, axis=1)

print("Sample Array:")
print(sample_array)

print("\nMean along the second axis:")
print(mean_values)

print("\nStandard Deviation along the second axis:")
print(std_values)

print("\nVariance along the second axis:")
print(variance_values)
