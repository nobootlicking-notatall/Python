# Pyramids

# https://pythontutor.com/render.html#mode=display


##################################################################


# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*" * i)

# i = 1 2 3 4 5

# 1 * "*" = *
# 2 * "*" = **
# 3 * "*" = ***
# 4 * "*" = ****
# 5 * "*" = *****

##################################################################

# *****
# ****
# ***
# **
# *

for i in range(5,-1,-1):
    print("*" * i)

# i = 5 4 3 2 1

# Make sure to use "-1" in the range to enable Python print the range in reverse order

# 5 * "*" = *****
# 4 * "*" = ****
# 3 * "*" = ***
# 2 * "*" = **
# 1 * "*" = *

##################################################################

#    *
#   **
#  ***

# Method 1
n = 3
for i in range(1,n+1): # 1 2 3
    print(" " * (n-i + 1) + "*" * i)

# Method 2
n = 3
for i in range(1,n+1): # 1 2 3 # rows
    for j in range(n-i): # 0,2=0,1 || 0,1=1 || 0,0=None # spaces
        print(" ", end='')
    for k in range(i): # 0,1=0 || 0,2=0,1 || 0,3=0,1,2 # stars
        print("*", end='')
    print()

##################################################################

#  ****
#   ***
#    **
#     *

n = 4
for i in range(1,n+1): # 1 2 3 4
    print((" " * i) + ("*" * (n-i + 1)))

# i = 1 2 3 4
# 1 * " " = " "    + "*" * (4-1 + 1) = " " +  "***"  = " ****"
# 2 * " " = "  "   + "*" * (4-2 + 1) = "  " +  "**"  = "  ***"
# 3 * " " = "   "  + "*" * (4-3 + 1) = "   " +  "*"  = "   **"
# 4 * " " = "    " + "*" * (4-4 + 1) = "    " + "*"  = "    *"

##################################################################

#   *
#  ***
# *****

n = 0 # 2*n - 1
for i in range(2,-1,-1):
    print(" " * i + "*" * (2*n + 1))
    n += 1

# For printing the stars in the pyramid, we use (2*n + 1) algorithm
# n = 0
# Hence for 0, (2*n + 1) becomes (2*0 + 1) = 1
# For 1, (2*n + 1) becomes (2*1 + 1) = 3
# For 2, (2*n + 1) becomes (2*2 + 1) = 5

# Print the leading spaces
# i = 2 1 0
# 2 * " " = "  "
# 1 * " " = " "
# 0 * " " = ""

# Adding both

# "  " + "*" =   __*
# " " + "***" =  _***
# "" + "*****" = *****
# _ denotes a whitespace


##################################################################


#   *
#  ***
# *****
#  ***
#   *

n = 3
for i in range(n): # 0 1 2
    print(" " * (n-i-1) + "*" * (2*i + 1))
for j in range(1,n): # 1 2
    print(" " * j + "*" * (2* (n-j) -1))

# Breakdown

#   *
#  ***
# *****
# for i in range(n): # 0 1 2
#     print(" " * (n-i-1) + "*" * (2*i + 1))

#  ***
#   *
# for j in range(1,n): # 1 2
#     print(" " * j + "*" * (2* (n-j) -1))


##################################################################


# *
# **
# ***
# ****
# ***
# **
# *

n = 1
items = 4
for i in range(items): # 0 1 2 3
    print("*" * (n))
    n += 1
for j in range(items-1, 0, -1): # 3 2 1
    print("*" * j)

# Breakdown

# *
# **
# ***
# ****
# for i in range(items): # 0 1 2 3
#     print("*" * (n))
#     n += 1 # Incrementing 'n' by 1 # n=1 || n=2 || n=3 || n=4

# ***
# **
# *
# for j in range(items-1, 0, -1): # 3 2 1
#     print("*" * j)


##################################################################



# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()

# 'i' denotes the number of rows
# 'j' defines the elements in the each row
# print() prints the numbers in a new line

# i = 1 = j range (1, 2) => 1 
# i = 2 = j range (1, 3) => 12
# i = 3 = j range (1, 4) => 123
# i = 4 = j range (1, 5) => 1234
# i = 5 = j range (1, 6) => 12345


##################################################################


# 54321
# 4321
# 321
# 21
# 1

for i in range(5,0,-1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# i = 5 4 3 2 1
# j = (5,0), (4,0), (3,0), (2,0), (1,0)
# print() prints the numbers in a new line

##################################################################

#      1
#     121
#    12321
#   1234321
#  123454321

n = 6
for i in range(1, 6): # 1 2 3 4 5
    print(" " * (n-i), end='') # Printing leading spaces
    for j in range(1, i+1): # Printing first part of pyramid
        print(j, end='')
    for k in range(i-1, 0, -1): # Printing second part of pyramid
        print(k, end='')
    print()

# Steps Breakdown: -

# Print Leading spaces
#_____  => n-1 = 5
#____   => n-2 = 4
#___    => n-3 = 3
#__     => n-4 = 2
#_      => n-5 = 1
#<none> => n-6 = 0

# Divide the pyramid into 2 parts
# Print numbers after space. Use end='' to print numbers in the same line # range(1, i+1)
#     1 => (1, 1+1) = (1, 2) =     1
#    12 => (1, 2+1) = (1, 3) =    12
#   123 => (1, 3+1) = (1, 4) =   123
#  1234 => (1, 4+1) = (1, 5) =  1234
# 12345 => (1, 5+1) = (1, 6) = 12345

# Print the second part of pyramid # range(i-1, 0, -1)
# <none> => 1-1 = 1,0 =>   None
# 1 => 2-1 = 1,0 =>    1
# 21 => 3-1 = 2,0 =>   21
# 321 => 4-1 = 3,0 =>  321
# 4321 => 5-1 = 4,0 => 4321
# Add the second part of pyramid using end=''

##################################################################

#      1
#     222
#    33333
#   4444444
#  555555555

n = 6
for i in range(1,6): # 1 2 3 4 5
    print(" " * (n-i), end='') # Printing leading spaces
    for j in range(2 * i - 1): # Algorithm: (2n - 1)
        print(i, end='')
    print()

# 2n - 1 => 2*0 - 1 => None
# 2n - 1 => 2*1 - 1 => 1 =>     1
# 2n - 1 => 2*2 - 1 => 3 =>    222
# 2n - 1 => 2*3 - 1 => 5 =>   33333
# 2n - 1 => 2*4 - 1 => 7 =>  4444444
# 2n - 1 => 2*5 - 1 => 9 => 555555555

##################################################################

# *****
# *   *
# *   *
# *   *
# *****

rows = 5
for i in range(rows): # 0 1 2 3 4
    for j in range(rows): # 0 1 2 3 4
        if i==0 or i==rows-1 or j==0 or j==rows-1: # "i" denotes the rows and "j" denotes the ELEMENTS of the rows. "i==0" denotes first row and "i==rows-1" denotes last row. "j==0" denotes first element of the first row and "j==rows-1" denotes last element of the last row.
            print("*", end='')
        else:
            print(" ", end='')
    print()


##################################################################


#    *
#   * *
#  *   *
# *******

rows = 4
for i in range(rows): # 0 1 2 3
    for spaces in range(rows-i-1): # 3 2 1 None
        print(" ", end='')
    for star in range(2*i+1):
        if star == 0 or star == (2*i) or i == rows-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Steps

# "i" in range => Define the number of rows
# "space" in range => Trailing spaces
# "star" in range => Visualize the triangle pyramid
# if and else conditions to print the outward stars and fill gaps inside the triangle
# "i == rows-1" prints the entire bottom row


##################################################################


# *
# **
# * *
# *  *
# *****

n = 5
for i in range(1,n+1): # 1,6 = 1 2 3 4 5
    for j in range(1,i+1): # 1,2=1 || 1,3=1,2 || 1,4=1,2,3 || 1,5=1,2,3,4 || 1,6=1,2,3,4,5
        if i==1 or i==n or j==1 or j==i:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Steps

# Rows
# for i in range(1,n+1)
# (1,n+1) = (1,5+1) = (1,6) = 1 2 3 4 5 = 5 rows

# Columns
# for j in range(1,i+1)
# 1,2 = 1
# 1,3 = 1 2
# 1,4 = 1 2 3
# 1,5 = 1 2 3 4
# 1,6 = 1 2 3 4 5

# i==1 => first row => all stars
# i==n => i==5 => last row => all stars
# j==1 => first star of every row
# j==i => last star of every row


##################################################################


#     *
#    **
#   * *
#  *  *
# *****

n = 5
for i in range(n): # 0 1 2 3 4
    for j in range(n-i-1): # 0,4=0123  0,3=012  0,2=01  0,1=0  0,0=None
        print(" ", end='')
    for k in range(1,i+2): # 1 2 3 4 5
        if i==0 or i==n-1 or k==1 or k==i+1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Steps

# n = 5 # Number of rows

# for j in range(n-i-1)
# 0,4=0123 => ____
# 0,3=012  => ___
# 0,2=01   => __
# 0,1=0    => _
# 0,0=None => None

# for k in range(1,i+2)
# 1,0+2 = 1,2 =     1 =     *
# 1,1+2 = 1,3 =    12 =    **
# 1,2+2 = 1,4 =   123 =   ***
# 1,3+2 = 1,5 =  1234 =  ****
# 1,4+2 = 1,6 = 12345 = *****

# i==0 => top row
# i==n-1 => bottom row
# k==1 => left edge
# k==i+1 => right edge


##################################################################


# A
# BB
# CCC

rows = 3
for i in range(rows):
    for j in range(1,i+2): # 1,2=1  1,3=1,2  1,4=1,2,3
        print(chr(i+65), end='')
    print()

# Steps

# for i in range(rows)
# range => 0 1 2 = 3 rows

# for j in range(1,i+2)
# range => (1,2), (1,3), (1,4)

# chr(i+65)
# chr(0+65) = chr(65) = A || j in range => A (1,2) = A
# chr(1+65) = chr(65) = B || j in range => B (1,3) = BB
# chr(2+65) = chr(65) = C || j in range => C (1,4) = CCC


##################################################################


# A
# AB
# ABC

rows = 3
for i in range(rows):
    for j in range(1,i+2):
        print(chr(j+64), end='')
    print()

# Steps

# for i in range(rows)
# range => 0 1 2 = 3 rows

# for j in range(1,i+2)
# range => (1,2)=1 , (1,3)=1,2 , (1,4)=1,2,3

# chr(j+64)
# chr(1+64) = chr(65) = A || j in range => A 1st place = A
# chr(1+64) chr(2+64) = chr(65) chr(66) = AB || j in range => A 1st place, B 2nd place = BC
# chr(1+64) chr(2+64) chr(3+64) = chr(65) chr(66) chr(67) = ABC || j in range => A 1st place, B 2nd place, C 3rd place = ABC


##################################################################


# 0 1 0 1 0 
# 1 0 1 0 1 
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0

for i in range(5): # 0 1 2 3 4
    for j in range(5): # 0 1 2 3 4
        print((i+j)%2, end=' ')
    print()

# Concept:

# If (row + column) % 2 == 0 → print 1
# Else → print 0

# For i=0, j=0,1,2,3,4
# 0%2=0, 1%2=1, 2%2=0, 3%2=1, 4%2=0
# and so on.


##################################################################


# 1 0 1 0 1 
# 1 0 1 0 1 
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1

for i in range(1,6):
    for j in range(1,6):
        print(j%2, end=' ')
    print()

# Concept:

# If row % 2 == 0 → print 1
# Else → print 0

# For i=0, j=1,2,3,4,5
# 1%2=1, 2%2=0, 3%2=1, 4%2=0, 5%2=1
# and so on.


##################################################################


#     1
#    11
#   121
#  1331
# 14641

from math import factorial
rows = 5
for n in range(rows): # 0 1 2 3 4
    for space in range(1,rows-n): # 1,5  1,4  1,3  1,2  1,1=None
        print(" ", end='')
    for r in range(n+1):
        print(factorial(n)//(factorial(r) * factorial(n-r)), end='')
    print()

# Concept Breakdown:

# Outer loop (n) → controls the row number
# First inner loop (space) → prints leading spaces for triangle shape
# Second inner loop (r) → calculates and prints each value in the row
# factorial() → used to compute combinations (nCr)
# Values are printed without spaces to form the triangle


##################################################################


#   *
#  * *
# *   *
#  * *
#   *

upper = 3
for i in range(1,upper+1): # 1,4 = 1 2 3
    for j in range(upper - i): # 0,2  0,1  0,0=None
        print(" ", end='')
    for k in range(2*i - 1): # 0,1  0,3  0,5
        if i==0 or k==0 or k==2*i-2:
            print("*", end='')
        else:
            print(" ", end='')
    print()
lower = 3
for m in range(lower-1,0,-1): # 2 1
    print(" " * (lower-m), end='')
    for n in range(2*m - 1): # 0,3  0,1
        if m==1 or n==0 or n==2*m-2:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Upper Half Logic
# Outer loop (i) controls the row number
# First inner loop (j) prints leading spaces → centers the diamond
# Second inner loop (k) controls the width: 2*i - 1
# Print * only when:
# k == 0 → left edge
# k == 2*i - 2 → right edge
# Print space for inner positions to keep it hollow

# Lower Half Logic
# Outer loop (m) runs in reverse to form the bottom
# Leading spaces increase as rows go down
# Width is 2*m - 1
# Print * when:
# n == 0 → left edge
# n == 2*m - 2 → right edge
# m == 1 → bottom tip
# Else print space


##################################################################


