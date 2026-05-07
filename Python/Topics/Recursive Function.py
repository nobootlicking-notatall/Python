# Recursive Function
# A recirsive function repeats itself until a specific condition is met
# Understanding Flows: https://pythontutor.com/visualize.html#mode=display


###########################################################################


def fact(num):
    if num <= 1:
        return 1
    return (num * fact(num-1))
print(fact(5))

# Workflow
# --------
# 5 is passed to num
# fact(num-1) is triggered
# fact(num-1) > 5 > (5-1)=4 > (4-1)=3 > (3-1)=2 > (2-1)=1
# num <= 1 condition met
# return (num * fact(num-1)) > 5 * 4 * 3 * 2 * 1 = 120 # Output


###########################################################################


def fib(limit, num=1):
    if num > limit:
        return 0
    return num + fib(limit, num+1)
print(fib(5, num=1))

# Workflow
# --------
# limit=5, num starts from 1
# num+1 = 1 > 1+1=2 > 2+1=3 > 3+1=4 > 4+1=5 > num becomes 6
# 'num' now greater than limit (Condition is met, 0 is returned, proceeding with the next step)
# return num + fib(limit, num+1) > 1+2+3+4+5 = 15 # Output


def fib(num):
    if num < 1:
        return 0
    return num + fib(num-1)
print(fib(5))

# Workflow
# --------
# num = 5
# return num + fib(num-1) > 5 > 5+4=9 > 9+3=12 > 12+2=14 > 14+1=15 > num becomes 0
# The condition num < 1 is met
# Output: 15


###########################################################################


list1 = [1,2,3,4,5]
def list_sum(lst, pointer=0):
    if pointer >= len(lst):
        return 0
    return lst[pointer] + list_sum(lst, pointer+1)
print(list_sum(list1))

# Workflow
# --------
# 'list1' is passed to 'lst' variable and the pointer is set to zero by default to start the indexing from the first element
# return lst[pointer] + list_sum(lst, pointer+1) > list1[0]+list1[1]+...+len(list1) > 1+2+3+4+5 > 15
# The 'pointer' stops at 4 because pointer >= len(lst) condition is met at 5 >= 5. Zero is returned and the numbers are added.
# Output: 15


###########################################################################


data = [1, [2, [3, [4]]]]
def nested_count(obj):
    if not isinstance(obj, list):
        return 0
    return 1 + sum(nested_count(x) for x in obj)
print(nested_count(data))

# Workflow
# --------
# 'data' is passed to the 'obj' variable
# return 1 + sum(nested_count(x) for x in obj) > 1 + sum(<add the first value found in the nested onject>) > 1+1,[2,[3,4]] > 1+1 > function repeats (2,[3,4]) > 1+2 > function repeats ([3,4]) > 1+3
# When the function reaches elements like 3 and 4, which are integers (not lists), not isinstance(obj, list) becomes True, so the function returns 0. Finally the numbers are added and the sum is returned.
# Output: 4


###########################################################################


data = [-10, -1, -2, -3]
def max_list(lst, pointer=0):
    if pointer == len(lst)-1:
        return lst[pointer]
    return max(lst[pointer], max_list(lst, pointer+1))
print(max_list(data))

# Workflow
# --------
# 'data' is passed to the 'lst' variable
# 'pointer=0' is set as default argument as we plan to go from the first element to the end (length of the list passed)
# return lst[pointer] > returns the last object (not zero), as it will consider 0 has an element and alters the list
# return max(lst[pointer], max_list(lst, pointer+1)) > max() returns the value > lst[pointer], max_list(lst, pointer+1) > lst[0]..lst[1]...lst[n] > 'n' signifies the length of the list as len(lst) as goes till 4


###########################################################################


nested = [1, [2, [3, 4]], 5]
def flatten(obj):
    if not isinstance(obj, list):
        return [obj]
    result = []
    for x in obj:
        result.extend(flatten(x))
    return result
print(flatten(nested))

# Workflow
# --------
# 'nested' is passed to the 'obj' variable
# for x in obj: result.extend(flatten(x)) > Iterates through every element present inside obj, performs recursion using flatten() and extends the elements into the 'result' list
# if not isinstance(obj, list): return [obj] > If list is not detected, the single element is returned. [] are used to return the single element inside a list so it can be later added to the empty list


###########################################################################