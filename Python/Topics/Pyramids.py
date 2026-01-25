# Pyramids

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

n = 3
for i in range(1,n+1): # 1 2 3
    print(" " * (n-i + 1) + "*" * i)

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
# <none> => 1-1 =>   None
# 1 => 2-1 = 1 =>    1
# 21 => 3-1 = 2 =>   21
# 321 => 4-1 = 3 =>  321
# 4321 => 5-1 = 4 => 4321
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
