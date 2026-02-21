# NumPy
# -----

import numpy as np

# Accessing the elements
# ----------------------

num1 = np.array([1,2,3,4,5])
num2 = np.array([6,7,8,9,10])


print(num1[0], num2[-1]) # 1 10 # Type: numpy.int64
print(num1[:4][::-2]) # [4 2] # Type: numpy.ndarray

# Sorting on criteria
print(num1[num1 <= 3]) # Sorts all elements smaller or equal to 3 # Type: numpy.ndarray
print(num2[num2 < num1]) # Prints elements of 'num2' that are greater than the elements of 'num1' # Type: numpy.ndarray
print(num1[num1 > 2][0]) # Sorts elements in 'num1' greater than 2 and prints the element at index '0' # Type: numpy.int64
print(num1[num1 % 2 == 0]) # Sorts the elements according to the criteria/condition

num1[-1:] = 11; print(num1) # Modifies the element of a numpy array at index '-1' to 11 # Output: [1 2 3 4 11]
num1[1:-2] = [99]; print(num1) # Modifies the elements in the range provided # Output: [1 99 99 4 5]
num1[1:3] = [55]; print(num1) # Modifies all elements specified in [start:end:step] index
num1[1::2] = [55]; print(num1) # Modifies all elements specified in [start:end:step] index
num1[3:] = [20,30]; print(num1) # Modifies multiple the elements specified in the range
num1[[2,3,0]] = 99; print(num1) # Instead of slicing the elements of the numpy array, the indexes have been directly used. This is also known as 'Fancy Indexing'.
