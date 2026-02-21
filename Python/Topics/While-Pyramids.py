# Pyramids using while loops
# --------------------------
# https://pythontutor.com/visualize.html#mode=edit


####################################################################


# *
# **
# ***
# ****
# *****

star = 1
while star <= 5:
    print("*" * star, end='')
    star += 1
    print()


####################################################################


# *****
# ****
# ***
# **
# *

i = 5
while i > 0:
    print("*" * i, end='')
    i -= 1
    print()


####################################################################


#     *
#    **
#   ***
#  ****
# *****

star = 5
while star >= 1:
    star -= 1
    print(" " * star + "*" * (5-star), end='')
    print()


i = 1
space = 5
while i <= space:
    print(" " * (space-i), end='')
    star = i
    while star <= i:
        print("*" * star, end='')
        star += 1
    i += 1
    print()


####################################################################


# *****
#  ****
#   ***
#    **
#     *

i = 0
rows = 5
while i <= rows-1:
    print(" " * i + "*" * (rows - i), end='')
    i += 1
    print()


i = 0
rows = 5
while i <= rows-1:
    print(" " * i, end='')
    stars = rows - i
    while stars > 0:
        print("*", end='')
        stars -= 1
    i += 1
    print()


####################################################################


#     *
#    ***
#   *****
#  *******
# *********

i = 1
rows = 5
while i <= rows:
    print(" " * (rows - i) + "*" * (2 *i - 1), end='')
    i += 1
    print()


i = 1
space = 5
while i <= 5:
    print(" " * (space-i), end='')
    star = i
    while star <= i:
        print("*" * (2 * (star) - 1), end='')
        star += 1
    i += 1
    print()


####################################################################


#   *
#  ***
# *****
#  ***
#   *

i = 0
rows = 3
while i < rows:
    print(" " * (rows-i-1) + "*" * (2 * i + 1), end='')
    i += 1
    print()
j = 0
while j+1 < rows:
    print(" " * (j+1) + "*" * (rows - 2 * j), end='')
    j += 1
    print()


i = 0
rows = 3
while i < rows:
    print(" " * (rows-i-1), end='')
    upper = 2 * i + 1
    while upper > 0:
        print("*", end='')
        upper -= 1
    i += 1
    print()
j = 1
while j < rows:
    print(" " * j, end='')
    lower = 2 * (rows - j) - 1
    while lower > 0:
        print("*", end='')
        lower -= 1
    j += 1
    print()


####################################################################


# *
# **
# ***
# ****
# ***
# **
# *

i = 1
rows = 4
while i <= rows:
    print("*" * i, end='')
    i += 1
    print()
j = 1
while j < rows:
    print("*" * (rows - j), end='')
    j += 1
    print()


####################################################################


# 1 
# 2 2 
# 3 3 3 

i = 1
rows = 3
while i <= rows:
    j = 1
    while j <= i:
        print(i, end=' ')
        j += 1
    i += 1
    print()


####################################################################


# 1
# 1 2
# 1 2 3

i = 1
rows = 3
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    i += 1
    print()


####################################################################


# 54321
# 4321
# 321
# 21
# 1

i = 5
while i >= 1:
    j = i
    while j >= 1:
        print(j, end='')
        j -= 1
    i -= 1
    print()


####################################################################


#     1
#    222
#   33333
#  4444444
# 555555555

i = 1
rows = 5
while i <= rows:
    print(" " * (rows-i), end='')
    j = 1
    while j <= 2 * i - 1:
        print(i, end='')
        j += 1
    i += 1
    print()


####################################################################


# A
# BB
# CCC
# DDDD
# EEEEE

i = 0
rows = 5
while i < rows:
    j = 0
    while j <= i:
        print(chr(i+65), end='')
        j += 1
    i += 1
    print()


####################################################################


# A
# AB
# ABC
# ABCD
# ABCDE

i = 0
rows = 5
while i < rows:
    j = 0
    while j <= i:
        print(chr(j+65), end='')
        j += 1
    i += 1
    print()


####################################################################


# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

i = 1
columns = 5
while i <= columns:
    j = 1
    while j <= columns:
        print(j, end=' ')
        j += 1
    i += 1
    print()


####################################################################


# 0 1 0 1 0 
# 1 0 1 0 1 
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0

i = 0
columns = 5
while i < columns: # 0 1 2 3 4
    j = 0
    while j < columns: # 0 1 2 3 4
        if (i+j)%2==0:
            print(0, end=' ')
        else:
            print(1, end=' ')
        j += 1
    i += 1
    print()


####################################################################


# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1 

i = 1
columns = 5
while i <= columns: # 1 2 3 4 5
    j = 0
    while j < columns: # 0 1 2 3 4
        if (i+j)%2==0:
            print(0, end=' ')
        else:
            print(1, end=' ')
        j += 1
    i += 1
    print()


####################################################################


# Floyd's Triangle

# 1
# 23
# 456

i = 1
rows = 3
num = 1
while i <= rows:
    j = 1
    while j <= i:
        print(num, end=' ')
        num += 1
        j += 1
    i += 1
    print()


####################################################################


# *****
# *   *
# *   *
# *   *
# *****

i = 1
rows = 5
while i <= rows:
    j = 1
    while j <= rows:
        if j==1 or j==rows or i==1 or i==rows:
            print("*", end='')
        else:
            print(" ", end='')
        j += 1
    i += 1
    print()


####################################################################


# *
# **
# * *
# *  *
# *****

i = 1
rows = 5
while i <= 5:
    j = 1
    while j <= i:
        if i==1 or i==rows or j==1 or j==i:
            print("*", end='')
        else:
            print(" ", end='')
        j += 1
    i += 1
    print()


####################################################################


#     *
#    **
#   * *
#  *  *
# *****

i = 1
rows = 5
while i <= 5:
    print(" " * (rows-i), end='')
    j = 1
    while j <= i:
        if j==1 or j==i or i==rows:
            print("*", end='')
        else:
            print(" ", end='')
        j += 1
    i += 1
    print()


####################################################################


#   *
#  * *
# *   *
#  * *
#   *




i = 1
upper = 3
while i <= upper:
    print(" " * (upper-i), end='')
    j = 1
    while j <= 2 * i - 1:
        if j==1 or j==2*i-1:
            print("*", end='')
        else:
            print(" ", end='')
        j += 1
    print()
    i += 1
j = 0
while j < upper-1:
    print(" " * (j+1), end='')
    k = 0
    while k < upper - 2 * j:
        if k==0 or k==upper-2*j-1:
            print("*", end='')
        else:
            print(" ", end='')
        k += 1
    print()
    j += 1


####################################################################


# *     *
# **   **
# *** ***
# *******
# *** ***
# **   **
# *     *

i = 1
rows = int(input("Enter a number greater than zero: "))
while i <= rows:
    print("*" * i + " " * (2 * (rows - i) + 1) + "*" * i, end='')
    print()
    i += 1
print("*" * (2 * rows) + "*")
j = 1
while j <= rows:
    print("*" * (rows-j+1) + " " * (2 * j - 1) + "*" * (rows-j+1), end='')
    print()
    j += 1


####################################################################





####################################################################