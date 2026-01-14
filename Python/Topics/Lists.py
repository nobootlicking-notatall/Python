# Lists always follow the left to right indexing, so make sure to use the positive or negative indexes from left to right


# Indexing
# --------
list1 = [1, 2, 3, 4, 5]

print(len(list1)) # Prints the number of elements in a list
print(list1[0:]) # Python assumes the blank after colon as the last index, which is often denoted by len(lis1)
print(list1[:len(list1)]) # Python assumes the blank before colon as 0, which is the starting index
print(list1[-1]) # Negative indexing
print(list1[:]) # Python prints the whole list
print(list1[-3:-1]) # Negative indexing slicing, following left to right order
print(list1[0:99]) # Python handles out-of-range indices gracefully, hence it will print the output
print(list1[-5:2]) # Python handles out-of-range indices gracefully, hence it will print the output
# Step: list1[start:stop:step]
print(list1[0:len(list1):2]) # List Step parameter, skips one character and prints every two

# NOTE: Python has in-place mutators which do not change the number of elements. Hence they can be printed in a norml print statement. Methods like .remove(), .append(), .pop(), .popitem(), etc. need to be defined in a separate variable. Only supported methods work!


# Modifying
# ---------
list2 = [1, 2, 3, 4, 5]

# Add elements using arithmetic operators
print(list2 + [6]) # Adding element to the list
list2[1:1] = [11,22,33] # Add elements inside a list
list2[1] = [11,22,33] # Add list inside a list
print(list2 + [True] + ["string-1"] + [8j]) # Lists are heteregenous, it can hold different data types
list2 += [11,22]; print(list2) # Adds 11,22 at the end

# Add elements using methods
list2_append = list2.append('Append'); print(list2) # .append() adds elements to the end of the list
list2.extend([1,2]); print(list2) # Extends the given elements or another list at the end
list2.insert(len(list2), 100); print(list2) # Inserts a new element || .insert(index, element). Here, the index is the length of the list, which will insert the element at the end

# NOTE: The similarity between append and extend is that they both accept single argument. But, for inserting multiple arguments, .extend() is used. This can done by providing the elements inside a list. .append(), on the other hand, inserts a list inside the list when the same is being done.

del list2[0] # Deletes the element in a more readable way
del list2[1:3]; print(list2) # Deletes the elements in index
del list2[1:5:2]; print(list2) # Deletes the elements in index with step
list2[-2:] = []; print(list2) # Delete a portion of values inside a list
list2.pop(); print(list2) # Delete the last element
list2.pop(1); print(list2) # Deletes the list element by index
remove_list2 = list2.remove(1); print(list2) # .remove() removes the specified element name

list2[:] = []; print(list2) # Clears a list. ":" points to all the present elements
list2.clear(); print(list2) # Clears a list
del list2[:]; print(list2) # Clears a list in a more readable manner

modify_list2 = list2[-1] = 1; print(list2) # Replacing an item using indexing
list2[0:2] = [1,4,3,8,9]; print(list2) # Modifying the elements using slicing

list2.sort(); print(list2) # Sorts the elements in ascending order by default
list2.sort(reverse=True); print(list2) # reverse=True argument sorts the elements in the descending order
list2.sort(key=str.lower); print(list2) # Sort the elements while ignoring case-sensitivity. This method does not change the original case of the elements.
list2.sort(key=str.upper); print(list2) # Sort the elements while ignoring case-sensitivity. This method too returns the elements in their original case.
list2.sort(key=len); print(list2) # Sorts the elements according to the length of characters. "reverse" can also be used along with it.

# NOTE: If the elements in the list are strings, .sort() will sort the objects according to their ASCII values. For example is we .sort(reverse=True) on ['A', 'a'], it will output ['a', 'A'] as a's ASCII value is 97 and A's is 65.

list02 = sorted(list2); print(list02) # Sorted, when used creates a new list stored in a different variable and does not change the original form of the previous list.

# NOTE: key=len, str.upper/lower, reverse=True/False can be used with sorted.

print(list2[::-1]) # Prints the list in reverse order
print(list2[::-2]) # Prints the list in reverse order and prints every two elements
list2.reverse(); print(list2) # Reverse the order
list02 = list(reversed(list2)); print(list02) # reversed() reverses a list and stores in another variable and does not tamper the original list.


# Querying
# --------
list3 = [1, 2, 3, 2, 4, 5, 2]

# Finding the elements through index
print(list3.index(2)) # Returns the first occurence of item in the list
print(list3.index(2,2,6)) # Returns the index of first occurence of item within a given index. .index(element, start_index, end_index-1)

# Exists or not
list3 = [1, 2, 3, 2, 4, 5, 2]
print(3 in list3) # Checks whether an element exists or not
# For strings
list03 = ['str', 'another_str']
print('str' in list03) # Searches for string inside a list
print('str' in list03[1]) # Searches for string inside a string

# STEPS TO FIND THE INDEX OF MULTIPLE REPEATING ELEMENTS
repeat_list = [1, 2, 3, 3, 4, 3, 5, 6]
for index,item in enumerate(repeat_list):
    if item == 3:
        print(f"Found {item} at index: {index}")


# List Comprehension
# ------------------
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_square_list4 = [x*x for x in list4 if x%2==0]
print(even_square_list4)
# Here, x*x is the expression || x is the item || list3 is the iterable || x%2==0 is the condition

