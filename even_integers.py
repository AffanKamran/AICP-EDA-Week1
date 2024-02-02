import numpy as np
even_integers = []
for num in range(30, 71):                      # Iterate through the range from 30 to 70
    if num % 2 == 0:                           # Check if the number is even
        even_integers.append(num)              # If even, append to the list
even_integers_array = np.array(even_integers)  # Convert the list to a NumPy array
print("All even integers from 30 to 70 are:")
print(even_integers)