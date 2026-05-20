################################################################


# Example 1: Linear search — check every element

def linear_search(lst, target):
    for i,val in enumerate(lst): # Worst case; visiting every element
        if val == target:
            return i # Returning index
    return -1
print(sorted(list(set([1,2,2,3,4,5,5,5,6,7]))))
print(linear_search(sorted(list(set([1,2,2,3,4,5,5,5,6,7]))), 5))


################################################################


# Example 2: Find the maximum in an unsorted list

def find_max(lst, target):
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val
print(find_max([3, 100, 2, 1], 9))


################################################################


# Example 3: Sum all elements

def total(lst):
    return sum(lst)                 
print(total([1,2,3,4,5,6]))


################################################################


# Example 4: Reverse a list

def rev(lst):
    return list(reversed(lst)) # Method 1
    return lst[::-1] # Method 2 (More preferred)
print(rev([11,22,33]))


################################################################


# Example 5: Count occurrences

from collections import Counter
def count_items(lst):
    return Counter(lst)
print(count_items(["abc", "bcd", "abc"]))


################################################################


# Example 6: Copy a list




################################################################