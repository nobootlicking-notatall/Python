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

import copy
l1 = [1,2,[3],4]
l2 = copy.deepcopy(l1) # .deepcopy() creates a complete separate inpedendent copy of the list including all nested items. Usually, the .copy() (Shallow copy) would reference changes to the nested items as well
print(l1,l2)
l1[2][0] = 33
print(l1,l2)


################################################################


# Example 7: Finding factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))


################################################################


# Example 8: Two-pointer technique (Converging)

def palindrome(obj):
    left, right = 0, len(obj)-1
    while left < right:
        if obj[left] != obj[right]:
            return False
        left += 1
        right -= 1
    return True
print(palindrome("NamaN"))


################################################################


# Example 9: Sliding window algorithm

def sliding(nums, size):
    n = len(nums)
    if size > n:
        return None
    window_sum = sum(nums[:size])
    max_sum = window_sum
    for i in range(n-size):
        window_sum = window_sum - nums[i] + nums[i+size]
        max_sum = max(window_sum, max_sum)
    return max_sum
print(sliding([11,22,33,44,55], 2))


################################################################


# Example 10: Hash Map/Dictionary Construction

def manual(list1):
    freq_map = {}
    for item in list1:
        if item not in freq_map:
            freq_map[item] = 1
        elif item in freq_map:
                freq_map[item] += 1
    return freq_map
print(manual(["donu", "ponu", "tonu", "donu"]))


################################################################


# Example 11: Dictionary Comprehension

items = ['apple', 'banana', 'cherry']
fruits_length = {fruit: len(fruit) for fruit in items}; print(fruits_length)


################################################################


# Example 12: Grouping Values in Python Dicts

from collections import defaultdict
list_of_pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = defaultdict(list)
for k,v in list_of_pairs:
    my_dict["ok"].append(v)
print(dict(my_dict))

list_of_pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = {}
for k,v in list_of_pairs:
    if "ok" not in my_dict.keys():
        my_dict["ok"] = []
    my_dict["ok"].append(v)
print(dict(my_dict))


################################################################


# Example 13: Iterating with a 'for' loop

text = "abracadabra"
freq_dict = {}
for char in text:
    freq_dict[char] = freq_dict.get(char, 0) + 1
print(freq_dict)


################################################################


# Example 14: Removing Duplicate Elements

items = [1, 2, 2, 3, 1]
unique_items = list(dict.fromkeys(items))
print(unique_items)


################################################################