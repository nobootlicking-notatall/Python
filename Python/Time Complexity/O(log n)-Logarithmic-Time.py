################################################################


# Example 1: Binary Search - the classic O(log n) algorithm

l1 = [2, 3, 4, 6, 7, 8, 9]
def binary_search(lst, target):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search(l1, 8))


################################################################


# Example 2: Count how many times you can halve n until reaching 1

def count_halves(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count
print(count_halves(5))

# Using Recursive Function

def count_halves(n):
    if n <= 1:
        return 0
    return 1 + count_halves(n//2)
print(count_halves(8))


################################################################


# Example 3: Python's bisect module (binary search built-in)

import bisect
l2 = [1, 3, 5, 7, 9, 11, 13]
b1 = bisect.bisect_left(l2, 13)
print(b1) # [1, 3, 5, 7, 9, 11, >ANS: 6< 13]
b2 = bisect.bisect_right(l2, 13)
print(b2) # [1, 3, 5, 7, 9, 11, 13 >ANS: 7<]


################################################################


# Example 4: Power by squaring

def fast_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp//2)
        return half * half
    return base * fast_power(base, exp-1) # For odd exponents. (-1) reduced so the power becomes even
print(fast_power(2,4))
print(fast_power(2,5))

# 3,4 = 9 * 9 = 81 (half x half)
# 3,2 = 3^2 = 3 * 3 = 9 (half x half)
# 3,1 = 3^1 = 3 * 1 = 3 (base * fast_power(base, exp-1))
# 3,0 = returns 1 = 1

# 3^5 = 3 * 81 = 243
# 3^4 = 9 * 9 = 81
# 3^2 = 3 * 3 = 9
# 3^1 = 3 * 1 = 3
# 3^0 = returns 1 = 1

# SIMILAR

def fast_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp//2)
        return half * half
    elif exp % 2 != 0:
        return base * fast_power(base, exp-1)
print(fast_power(2,6))

# To Handle Negative Exponent

def fast_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp//2)
        return half * half
    elif exp < 0:
        return 1/fast_power(base, -exp)
    return base * fast_power(base, exp-1)
print(fast_power(2, -2))


################################################################