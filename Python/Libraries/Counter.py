# Counter
# -------
# Counter is a dictionary subclass for counting hashable objects.
# It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counter only accepts 1 argument. Multiple arguments needs to be passed in a list.

# Import Counter
from collections import Counter

# String
char_counts = Counter("abcd-abc-ab-a"); print(char_counts)
# Output: Counter({'a': 4, 'b': 3, '-': 3, 'c': 2, 'd': 1})
# Type: collections.Counter

# List
list_count = Counter(['a', 'b', 'c', 'a', 'b', 'a']); print(list_count)
# Output: Counter({'a': 3, 'b': 2, 'c': 1})
# Type: collections.Counter
nested_list = [[1,2,3], [2,3,4], [3,4,5], [1,2,3]]; print(Counter(map(tuple,nested_list))) # Use map() to convert list to tuple
# Output: Counter({(1, 2, 3): 2, (2, 3, 4): 1, (3, 4, 5): 1})

# Tuple
tuple_count = Counter(('a', 'b', 'c', 'a', 'b', 'a')); print(tuple_count)
# Output: Counter({'a': 3, 'b': 2, 'c': 1})
# Type: collections.Counter
nested_tuple = [(1,2,3), (2,3,4), (3,4,5), (1,2,3)]; print(Counter(nested_tuple))
# Output: Counter({(1, 2, 3): 2, (2, 3, 4): 1, (3, 4, 5): 1})

# Dictionary
dict_count = Counter({'a': 3, 'b': 2, 'c': 1}); print(dict_count)
# Output: Counter({'a': 3, 'b': 2, 'c': 1})
# Type: collections.Counter

# Set
set_count = Counter({'a', 'b', 'c', 'a', 'b', 'a'}); print(set_count)
# Output: Counter({'a': 3, 'b': 2, 'c': 1})
# Type: collections.Counter

