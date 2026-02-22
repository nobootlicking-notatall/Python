# NumPy
# -----

import numpy as np

# Accessing the elements
# ----------------------

num1 = np.array([1,2,3,4,5])
num2 = np.array([6,7,8,9,10])


print(len(num1)) # Prints the length of a numpy array

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
num1[[2,3,0]] = 99; print(num1) # Instead of slicing the elements of the numpy array, the indexes have been directly used. This is also known as 'Fancy Indexing' # Output: [99 2 99 99 5]


# Modifying the NumPy array
# -------------------------

num1 = np.array([1,2,3,4,5])
num2 = np.array([6,7,8,9,10])

print(num1 + 1) # Adds 1 to every element in 'num1' array
num1 += 1; print(num1) # Works the same as above

num1 *= 2; print(num1) # Multiplies every element of 'num1' array by 2
print(num1 * 2) # Works the same as above
num1[num1 >= 4] *= 11; print(num1) # Modifying only selected elements # Output: [1 2 3 44 55]

num1[num1 % 2 != 0] = 0; print(num1) # Replaces odd numbers with 0 # Output: [0 2 0 4 0]

n1 = np.where(num1 > 3, 100, num1); print(n1)
# The above notation follows "output_array = np.where(condition, value_if_true, value_if_false)" format
# If the condition is met, modify the value by <specified_value>
# Else, print the num1 elements
num1[num1 == 2] = 22; print(num1) # Replace a specific element by it's value # Output: [1 22 3 4 5]

np.put(num1, [1], [99]); print(num1) # Replaces the element in an array. numpy. .put(<array>, <element>, <new_element>)

np.place(num1, num1 < 3, 00); print(num1) # Replaces the element in an array provided a condition. .place(<array>, <condition>, <new_element>)

print(np.clip(num1, 3, 4)) # Clip Value: All values under 3 becomes 3, and all the values above 4 becomes 4. Works based upon elements # Output: [3 3 3 4 4]

num1 = num1[::-1]; print(num1) # Reverses the array
num1[:] = num1[::-1]; print(num1) # Works the same as above

num1[::2] = 0; print(num1) # Replaces every alternate element # Output: [0 2 0 4 0]

num1[0], num1[1] = num1[1], num1[0]; print(num1) # Swapping the values # Output: [2 1 3 4 5]

n1 = np.array([True,False,False,False,False])
num1[n1] = 100; print(num1) # Modify an existing array # Output: [100 2 3 4 5]

# Modify an array using logical operators
num1[(num1 >= 4) & (num1==5)] = 777; print(num1) # Uses '&' (AND) operator. Both conditions are required to met in order to change the value. # Output: [1 2 3 4 777]

num1[(num1 == 4) | (num1==5)] = 777; print(num1) # Uses '|' (OR) operator. If either condition is met, num1 will be returned with modified value(s). # Output: [1 2 3 777 777]


# Iteration
# ---------

for i in range(len(num1)):
    if num1[i] % 2 == 0:
        num1[i] += 1
print(num1)
# Output: [1 3 3 5 5]
# Steps: -
# [1 2 3 4 5]
# [1 3 3 4 5]
# [1 3 3 4 5]
# [1 3 3 5 5]
# [1 3 3 5 5]

