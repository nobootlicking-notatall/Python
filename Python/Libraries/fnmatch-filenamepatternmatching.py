# fnmatch
# The fnmatch module is a utility in Python used for Unix shell-style wildcard matching
# * => Matches everything (any number of characters)
# ? => Matches any single character
# [seq] => Matches any character in the provided sequence
# [!seq] => Matches any character not in the provided sequence

import fnmatch
# OR
from fnmatch import fnmatch

# * => Wildcard character; used to search when the number of characters are UNKNOWN
print(fnmatch("powershell", "power*")) # True

# ? => Wildcard character; used to search when the number of characters are KNOWN
print(fnmatch("python", "pyth??")) # True

# fnmatch with the help of recursion
example = ["python", "powershell", "sql"]
print([x for x in example if fnmatch(x, "s??")]) # Returns ['sql'], else error if false

# Finding patterns inside a nested list
example = ["python", "powershell", "sql", ["Azure", ["Intune", "Defender"]]]
def break_list(obj): # Recursive function to break down a nested list into a single-line flat list for easy recursion
    flat = []
    for item in obj:
        if isinstance(item, list):
            flat.extend(break_list(item))
        else:
            flat.append(item)
    return flat
flat_list = break_list(example) # Storing the output in a outside the function and calling it
print([x for x in flat_list if fnmatch(x, "*nd?r")]) # Finding the pattern from the broken nested list using recursion


# Boolean Value for fnmatch and fnmatchcase
import fnmatch
from fnmatch import fnmatchcase
print(fnmatchcase("Dhruv Verma", "Dhruv ?*")) # Returns True


import fnmatch
print(fnmatch.filter(flat_list, "powershell")) # Returns ['powershell']
print(bool(fnmatch.filter(flat_list, "powershell"))) # If found, returns True

