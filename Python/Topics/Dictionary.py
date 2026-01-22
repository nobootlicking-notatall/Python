# Dictionary
# Dictionary is an unordered collection where data values are stored in key-value pairs.
# Every element in a dictionary is stored in the memory with a unique address and a hash value is generated therefore.


# Viewing and Searching Dictionary
# --------------------------------

d1 = {
    "key1": "value-1",
    "key2": ["value-01", "value-02"]
}
print(d1) # Output: {'key1': 'value-1', 'key2': ['value-01', 'value-02']}

# Accessing values in dictionary
print(d1["key1"]) # Output: value-1
print(d1["key2"][0]) # Accessing dictionary values inside a list

# Memory Address and Hash Value
print(hash(d1["key1"])) # Hash Value of 'value-1'
print(id(d1["key1"])) # Memory Address of 'value-1'

print(len(d1)) # Returns the number of key-value pairs present inside the dictionary
print(len(d1["key1"])) # Returns the length of the value associated with "key1"

print(d1.keys()) # Returns all the keys present inside the dictionary
print(d1.values()) # Returns all the values present inside the dictionary
print(d1.items()) # Returns all the key-value pairs present inside the dictionary

print(d1.get("key01", "Not Found")) # Python looks for the first argument provided in parenthesis within 'd1' and returns the value associated with it. If the key is not found, it returns the second argument provided in parenthesis.

print("key1" in d1) # Works to check if a key is present
print("value-1" in d1.values()) # Add .values() to check for a value

import json # Prints the dictionary in a JSON-formatted way
json_output = json.dumps(d1, indent=4); print(json_output)


# Modifying Dictionary
# --------------------

d1 = {
    "key1": "value-1",
    "key2": ["value-01", "value-02"]
}

d1["key1"] = 21 # Updates "key1" value to 21

d1.update(key1 = 33) # Updates "key1" value to 33


# Nested Dictionary
# -----------------

d1 = {
    "key1": "value-1",
    "key2": {"x": 11, "y": 22}
}

# Accessing Elements
print(d1["key2"]["x"]) # Accessing elements inside the nested dictionary # Output: 11
print(d1["key2"].keys()) # Prints "x", "y" # Type: dict_keys
print(d1["key2"].values()) # Prints 11, 22 # Type: dict_values
print(d1["key2"].items()) # Prints ('x', 11), ('y', 22) # Type: dict_items

# Updating Elements
d1.update(key2 = {"x": "Eleven"}) # Updates "key2" value to 'Eleven'

# Adding Elements
d1["key3"] = "Value Added" # Adds a new key-value pair to the dictionary
d1["key4"] = {"N1": "Blue", "N2": "Green"} # Add a new-key nested pair to the dictionary

# Deleting
d1.pop("key1") # Removes the key-value pair associated with "key1" # .pop() requires atleast 1 argument. Works with a key, not index.
d1.popitem() # Removes the last key-value pair # .popitem() does not require any arguments. Deletes the last element.
del d1["key2"]["y"] # Removes the key-value pair associated with "key2" in a more readable manner
del d1["key2"] # Removes the key-value pair associated with "key2" in a more readable manner
del d1 # Removes the dictionary
d1.clear() # Removes all key-value pairs from the dictionary
d1 = {} # Removes all key-value pairs from the dictionary


# Iteration
# ---------

d1 = {
    "key1": "value-1",
    "key2": {"x": 11, "y": 22}
}

for i in d1:
    print(i) # Output: key1, key2 # Type: str # Prints all keys present inside the dictionary
    print(d1[i]) # Equivalent to d1["<key>"]. # This will output every value associated with all the keys


# Sorting
# -------

print(min(d1)) # Sorts the keys according to their length
print(max(d1)) # Sorts the keys according to their length
print(sorted(d1)) # Sorts the keys in alphabetical order

# Sorting Methods
s1 = sorted(d1.values(), key = lambda k: len(k)); print(s1) # Sorts the values in ascending order and returns the VALUES in a list
s1 = sorted(d1, key = lambda k: len(d1[k])); print(s1) # Sorts the keys in ascending order and returns the KEYS in a list


# Copying
# -------

# dict.fromkeys(iterable, value=None)

d2 = dict.fromkeys(d1); print(d2) # Creates a new dictionary named "d2", and the KEYS of 'd1' are copied to 'd2' by default. Typically, the values are set to None.

d2 = dict.fromkeys(d1.values()); print(d2) # Creates a new dictionary named "d2", and the VALUES of 'd1' are copied to 'd2' by default as KEYS. Typically, the values are set to None.

d2 = dict.fromkeys(d1, 0); print(d2) # This follows "dict.fromkeys(iterable, value=None)" format. The value is set to 0.


# Dictionary Comprehension
# ------------------------

# Swapping Keys and Values
print(d1.items()) # IMPORTANT: For reference
d3 = {value: key for key, value in d1.items()} # Swapping keys and values


# DefaultDict
# -----------

from collections import defaultdict

def default_value():
    return "Default Value"
d1 = defaultdict(default_value)
d1['a'] = 1 # Passed key "a" and value "1"
d1['x'] # Passed key "x" but NO value. Hence default_value() is passed as the value. Value= "Default Value"
print(dict(d1)) # Output: {'a': 1, 'x': 'Default Value'}

raw_logs = [
    {"ip": "192.168.1.1", "status": 200, "path": "/home"},
    {"ip": "10.0.0.5", "status": 404, "path": "/admin"},
    {"ip": "192.168.1.1", "status": 200, "path": "/login"},
    {"ip": "10.0.0.5", "status": 404, "path": "/config"},
]
ip_address = defaultdict(list) # Initializes 'ip_address' as a defaultdict with a list as the default value
for ip_entry in raw_logs: # "ip_entry" iterates over the list in "raw_logs"
    ip_address[ip_entry['ip']].append(ip_entry['path']) # Appends the value of "path" to the list associated with the key "ip"
for ip,p in ip_address.items():
    print(f"{p} is currently accessed in {ip}") # Prints the list associated with the key "ip"

transactions = [
    {"category": "Electronics", "price": 499.99},
    {"category": "Books", "price": 15.50},
    {"category": "Electronics", "price": 25.00},
    {"category": "Books", "price": 10.00}
]
sum = defaultdict(float) # Initializes 'sum' as a defaultdict with a float as the default value
for i in transactions: # "i" iterates over the dictionary in "transactions"
    sum[i["category"]] += i["price"] # Adds the value of "price" to the float associated with the key "category". "category" gets added as a key first and the values associated with it gets added later on, without creating a second entry for the same element in "category".
print(dict(sum)) # Output: {'Electronics': 524.99, 'Books': 25.5}