# Lambda
# lambda <argument>: <expression>
# Pass arguments to the expression

# Basic Math Operations using lambda
# ----------------------------------

# Addition
add = lambda a,b: a + b; print(add(6,5)) # Passes 6,5 arguments to a + b expression. Prints 11
# Various other methods can be used with add() such as print(add(5,not False)) # Output: 6
# The same code can be modified to perform subtraction (a - b)

# Square
square = lambda s: s ** 2; print(square(4)) # Passes 4 to "s ** 2" # Output: 16
# The same can be done with multiplication (s * <any_number>)

# Odd or Even
is_even = lambda e: e % 2 == 0; print(is_even(4)) # This will evaluate whether the value passed in "is_even" leaves a remainder 0 or not. If yes, then the number is even, else vice-versa.
# The same can be modified to check for odd integers by changing the arthmetic operator to "!=" (not equals to)
# "%" works on the first level only. For example: - If we input 4.4, 0.4 will be the remainder and would return False as 0.4 is not equals to 0.

# Absolute Value Calculation
# Complex Expression
a = 3 + 4j
my_abs = lambda a: abs(a); print(my_abs(a)) # 3 and 4 from 'a' gets passed to my_abs. This is the absolute value represented by √(a^2 + b^2) => √(3^2 + 4^2) => √(9 + 16) => √25 = 5.0 (float value)

# Integer Value
import math
a = 25
sqrt_num = lambda sn: math.sqrt(sn); print(sqrt_num(a)) # Returns 5.0 (float value). √a => √25 => 5.0

# Average
num = 1,2
avg = lambda av: sum(num)/len(num); print(avg(num)) # In this method, 'num' is passed to 'av' and 'av' is passed to 'sum' and 'len'.
avg = lambda av: sum(av)/len(av); print(avg(num)) # In this method, argument 'av' iterates through each element present inside 'num', performs the addition, and divide it by it's length printing the average of the numbers.

# Find Keywords
l1 = ['a', 'b']
l2 = ['a']
check = lambda chk: all(x in chk for x in l2); print(check(l2)) # all() returns True if all elements of 'l2' are present in 'l1', else False. In this, 'x' is iterating through each element in l1 and checking if the passed argument exist in l1 or not.

check = lambda chk: any(x in chk for x in l2); print(check(l1)) # In this case, 'any()' returns True if any element of 'l2' is present in 'l1', else False. In this, 'x' is iterating through each element in l1 and checking if the passed argument exist in l1 or not.

# Check a String in a List
string1 = "string"
find = lambda f: True if f in string1 else False; print(find("s")) # True # 'f' checks if the element passed in the print statement exists in 'string1'

# Handle Undefined Number of Arguments

add = [1,2,3,4,5,6,7,8,9,10]
add_el = lambda *nd: sum(nd); print(add_el(*add)) # *nd is used to handle undefined number of arguments. '*add' unpacks the values inside 'add' and passes them to 'nd'. 'nd' stores the values inside 'add' and 'sum' adds them up.

add_el = lambda *args: sum(args); print(add_el(1,2,3,4,5)) # Output: 15 # *args is used to handle undefined number of arguments

# Count Occurrences
from collections import Counter
l1 = ['a', 'b', 'a', 'a']
l2 = ['a']
l1_count = Counter(l1) # Counter({'a': 3, 'b': 1})
check = lambda chk: {
    item: l1_count[item] for item in chk if item in l1_count # { key_expr : value_expr  for  var  in  iterable  [if  condition] }
}
print(check(l2))
# l1_count => {'a': 3, 'b': 1}
# for item in chk => 'l2' is passed to the chk variable. 'item' stoes the value inside 'l2'
# if item in l1_count => 'a' in {'a': 3, 'b': 1} => True
# item: l1_count[item] => 'a': {'a': 3, 'b': 1}['a'] => 'a': 3
# Output: {'a': 3}


# Operations on List
# ------------------

# Length Sorting
names = ["Bob", "Alice", "Cassandra"]
ls = sorted(names, key = lambda l: len(l), reverse=True); print(ls)

# Sort List
name_id = ['003-Charlie', '002-Bob', '001-Alice']
print(sorted(name_id, key = lambda item: item[:4])) # 'item' checks for the first 3 characters of each element in 'name_id'. Use 'reverse = True' to sort in descending order

# Nested List-Tuple Sorting
servers = [("Web-01", 16), ("DB-01", 64), ("App-01", 32)]
servers.sort(key = lambda r: r[1]); print(servers) # 'r' iterates through the first element of each tuple of 'servers' and sorts them accordingly

# Filter List
devices = ["UK-01", "US-01", "UK-02", "IN-05"]
s = filter(lambda x: x.startswith("UK"), devices); print(list(s)) # 'x' checks if the element starts with "UK" and filters them accordingly

# Filter List (Case Insensitive)
s = filter(lambda x: x.lower().startswith("uk"), devices); print(list(s)) # 'x' checks if the element starts with "uk" and filters them accordingly ignoring case sensitivity

# Adding all elements in a list and Return a Single Value
from functools import reduce # The 'reduce' is applied to the items of an iterable to reduce the entire sequence into a single accumulated value.
num = [1,2,3,4,5]
total = reduce(lambda x,y: x+y, num) # 'x' stores the first element of 'num' and 'y' stores the second element of 'num'. 'x+y' adds the first and second element of 'num' and stores it in 'x'. This process is repeated until all elements are added.
print(total)

# Adding <any_number> to a list
from functools import reduce
num = [1,2,3,4,5]
add_num = map(lambda an: an + 5, num); print(list(add_num))

# Multiplying all elements in a list and Return a Single Value
from functools import reduce
num = [1,2,3,4,5]
total = reduce(lambda x,y: x*y, num)
print(total)
# Multiplying all elements in a list
num = [1,2,3,4,5]
mul = map(lambda x: x**4, num); print(list(mul))
# The result can be printed using 'list' or 'tuple' or 'set'. For 'set', use sorted() to print the elements in an ordered manner.

# Finding the maximum element in a list
from functools import reduce
num = [1,2,3,4,5]
max = reduce(lambda x,y: x if x > y else y, num)
print(max)
# The same can be done to find the minimum element in a list => min = reduce(lambda x,y: x if x<y else y, num)

