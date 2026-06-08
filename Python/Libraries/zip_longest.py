# zip_longest
# -----------
# This method aggregates multiple iterables into tuple and fills in any mission values with "None" by default


#############################################################


from itertools import zip_longest


#############################################################


from itertools import zip_longest

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92]
for name,score in zip_longest(names, scores):
    print(f"{name} scored {score}")

# Result

# Alice scored 85
# Bob scored 92
# Charlie scored None


#############################################################


# Specifying missing values

from itertools import zip_longest

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92]
for name,score in zip_longest(names, scores, fillvalue="zero"):
    print(f"{name} scored {score}")

# Result

# Alice scored 85
# Bob scored 92
# Charlie scored zero


#############################################################


# Method 1
# --------
from itertools import zip_longest

data = [1, 2, 3, 4, 5, 6, 7]
args = [iter(data)] * 3
chunks = list(zip_longest(*args, fillvalue="Empty"))
print(chunks)

# Result

# [(1, 2, 3), (4, 5, 6), (7, 'Empty', 'Empty')]

# Method 2
# --------
from itertools import zip_longest

data = [1, 2, 3, 4, 5, 6, 7]
args = [iter(data)] * 3
chunks = lambda z: (list(zip_longest(*z, fillvalue="Empty"))); print(chunks(args))

# Method 3
# --------
from itertools import zip_longest

data = [1, 2, 3, 4, 5, 6, 7]
chunks = lambda data,size: (list(zip_longest(*[iter(data)] * 3, fillvalue="Empty"))); print(chunks(data,3))


#############################################################


# Three-Lists Operation

from itertools import zip_longest

nums = [1,2,3]
alphabets = ["a", "b"]
special = ["?"]
for num,alpha,sp in zip_longest(nums,alphabets,special, fillvalue="Empty"):
    print(f"{num} == {alpha} == {sp}")

# Result

# 1 == a == ?
# 2 == b == Empty
# 3 == Empty == Empty


#############################################################