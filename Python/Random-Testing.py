# l1 = ['A', 'B']
# lower_l1 = list(item.lower() for item in l1)
# print(lower_l1.index('b'))
# position = list(map(str.lower, l1)).index('b'); print(position)

# a = [1, 2, 3, 4]
# a[0] = [5]
# a[0:1] = [5] # [5] or [5,]
# print(a)

# b = [x for x in range(20)]; print(b)
# a = [int(x) for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit() if
# (int(x) in ([x for x in range(20)])))]; print(a)

# a = [10,20]
# b = [1,2]
# for a,b in zip(a,b):
#     print(a-b)

# print(1 + True)
# print(bool(1) + True)

# print(0 + False)
# print(bool(0) + False)

# print(True and False)
# print(False and True)
# print(True and True)
# print(False and False)
# print(True or False)
# print(False or True)
# print(True or True)
# print(False or False)

# l1 = ['apple', 'orange', 'tomato']
# for items in l1:
#     l1.remove(items)
# print(l1)

# x = 32
# y = '32'
# print(x is int(y))

# a = input("Enter a number: ")
# if a >= "":
# 	print("Space detected")
# else:
# 	val = int(a)
# 	try:
# 		match val:
# 			case 1:
# 				print("--1--")
# 			case 2:
# 				print("--2--")
# 			case _:
# 				print("Attempting decoding...")
# 	except ValueError:
# 		print("Please enter an integer")

# a = " "
# b = "    "
# print(b > a)

# li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# val1, val2 = 0,''
# for x in li:
# 	if(type(x) == int or type(x) == float):
# 		val1 = val1 + x
# 	elif(type(x) == str):
# 		val2 = val2 + x
# 	else:
# 		break
# print(val1, val2)

# from functools import reduce
# l1 = [1,2,3]
# result = reduce(lambda x,y: x + y**2, l1); print(result) # 1st Case: x,y=1,2 => 1 + 2**2 = 5 || 2nd Case: x,y = 5 + 3**2 = 14 || Answer: 14

# inp1,inp2 = input("Enter 2 numbers: ").split()
# op1 = input("Enter an arithmetic operator: ")
# inp3 = int(inp1)
# inp4 = int(inp2)
# match op1:
#     case '+':
#         print(inp3 + inp4)
#     case '-':
#         print(inp3 - inp4)
#     case '*':
#         print(inp3 * inp4)
#     case '/':
#         print(inp3 / inp4)
#     case 'q':
#         print(inp3 // inp4)
#     case 'r':
#         print(inp3 % inp4)

# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)

# row = 4
# for i in range(1,4):
#     print('*' * i)

# row = 4
# for i in range(row-1,0,-1):
#     print('*' * i)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# num = 123
# strnum = str(num)
# spl = "".join(reversed(strnum)); print(spl)

# num = 456
# strnum = str(num)
# rev = strnum[::-1]; print(rev)

# i = 1
# while i <= 5:
#     print(i)
#     if i == 3:
#         pass
#     i += 1

# print("Harry"[2:-1])

# a = "Hello,o"
# print("/".join(a))
# print(a.split(" , "))
# print(a.split(","))

# sentence = "Do you know what Putin said? He said Donald Trump is a genius. I do think that he is"
# print(sentence.find("genius"))
# print(sentence.replace("genius", "duffer"))

# sentence = "Betty bought a butter, but the butter was bitter. So, Betty bought a better butter to make the bitter butter better."
# print(sentence.count("Betty"))
# print(sentence.split())
# count = 0
# for i,word in enumerate(sentence.split()):
#     if word == "Betty":
#         print(f"Found {word} at index {i}")
#         count += 1
# print(count)

# sentence = "Betty bought a butter, but the butter was bitter. So, Betty bought a better butter to make the bitter butter better."
# lowersen = sentence.lower().split()
# betty = [word for word in lowersen if "betty" in word]; print(betty)

# sentence = "Betty bought a butter, but the butter was bitter. So, Betty bought a better butter to make the bitter butter better."
# print(sentence.replace("Betty", "Dhruv"))
# print(sentence.startswith("B"))
# print(sentence.endswith("."))
# print(sentence.isspace())
# print(sentence.zfill(120)) # This method counts the number of characters in the string first. Specify the count exceeding the length of the string, as it overrides with respect to the length.

# s = "Radar" # Palindrome
# r = s.lower()[::-1]
# print(s.lower() == r) # Method 1 ends
# l = s.lower()
# check = ""
# for i in range(len(l)-1, -1, -1):
#     check += l[i]
# if l == check:
#     print("The string is palindrome")
# else:
#     print("The string is NOT palindrome")

# s1 = "Dear {},\n\nThis is an automated email. Kindly ignore this message.\n\nRegards,\nAdministrator\n-----\n-----\n"
# t1 = ("Rana Ji, Prakash, Dhruv")
# for names in t1.split(", "):
#     print(s1.format(names))

# print("Mesomorph"[-6:])

# s1 = "Python is awesome"
# print(s1.replace("awesome", "fire"))

# square = lambda x: x **2
# print(square(4))

# my_logic = lambda x: x > 10
# print(my_logic(1), id(my_logic(1)))

# add = lambda a,b: a + b; print(add(5,not False))

# square = lambda s: s ** 2; print(square(4))

# is_even = lambda e: e % 2 == 0; print(is_even(40))

# x = 4 + 5j
# print(abs(x))
# import math
# print(math.sqrt(41))

# a = 3 + 1 + 3j
# my_abs = lambda a: abs(a); print(my_abs(a))

# import math
# a = 25
# sqrt_num = lambda sn: math.sqrt(sn); print(sqrt_num(a))

# num = 1,2
# avg = lambda av: sum(av)/len(av); print(avg(num))
# avg = lambda av: sum(num)/len(num); print(avg(num))

# l1 = ['a', 'b']
# l2 = ['a']
# check = lambda chk: all(x in l1 for x in chk); print(check(l2))

# l1 = [1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,5]
# l2 = []
# i = 0
# while i < len(l1):
#     un = l1[i]
#     if un not in l2:
#         l2.append(un)
#     i += 1
# print(l2)

# while l1.count(2):
#     l1.remove(2)
# print(l1)

# l1 = ['a' ,'b', 'c']
# for items in l1:
#     l1.remove(items)
#     print(l1)

# a = "radar"
# b = a[::-1]
# print(b)
# print(b == a)
# print(b is a)
# print(id(a), id(b))

# a = "s"
# l1 = ['q', 'r', 's', 't']
# f1 = lambda f: a in l1; print(f1(a))
# f1 = lambda f: all(x in l1 for x in f); print(f1(a))

# from collections import Counter
# l1 = ['a', 'b', 'a', 'a']
# l2 = ['a']
# check = lambda chk: all(x in l1 for x in chk); print(check(l2))
# cnt = Counter()
# for word in l1:
#     cnt[word] += 1
# print(cnt)
# check = lambda chk: {
#     item: l1_count[item] for item in chk if item in l1_count # { key_expr : value_expr  for  var  in  iterable  [if  condition] }
# }
# l1_count = Counter(l1); print(check(l2)) # {'a': 3}
# lc = Counter(l1); print(lc) # Counter({'a': 3, 'b': 1})
# print(l1_count['a']) # 3

# add_el = lambda *args: sum(args); print(add_el(1,2,3,4,5)) # 15

# from collections import Counter
# l1 = ['a', 'b', 'a', 'a']
# l2 = ['a']
# cnt = Counter()
# check = lambda chk: {
#     item: l1_count[item] for item in chk if item in l1_count # { key_expr : value_expr  for  var  in  iterable  [if  condition] }
# }
# l1_count = Counter(l1); print(check(l2))
# l1_count => {'a': 3, 'b': 1}
# for item in chk => 'l2' is passed to the chk variable. 'item' stoes the value inside 'l2'
# item: l1_count[item] => 'item' stores the value of 'l2' and 'l1_count[item]' looks up the count of that item from 'l1_count' Counter
# if item in l1_count => 'a' in {'a': 3, 'b': 1} => True
# Output: {'a': 3}

# from collections import Counter
# l1 = ['a', 'b', 'c', 'c', 'b', 'b']
# l2 = ['b']
# l1_counter = Counter(l1); print(l1_counter)

# check = lambda c: {
#     item: l1_counter[item] for item in c if item in l1_counter
# }; print(check(l2))

# from collections import Counter
# c = Counter(a=3, b=1)
# d = Counter(a=1, b=2)
# print(c + d)
# print(c - d)
# print(c & d) # Intersection
# print(c | d) # Union

# # Binary of 32
# print(bin(32))
# print(f"{32:b}") # Binary without 0b prefix

# print(3 & 6)
# print(6 | 7)

# from collections import Counter
# nested_list = [[1,2,3], [2,3,4], [3,4,5], [1,2,3]]; print(Counter(map(tuple,nested_list)))

# a = ['a', 'b', 'c']
# b = ",".join(a); print(b)

# from collections import Counter
# l1 = ['a', 'b', 'a', 'a']
# l2 = ['a']
# l1_c = Counter(l1)
# check = lambda chk: {
#     item: l1_c[item] for item in chk if item in l1_c
# }
# print(check(l2))

# string1 = "s"
# find = lambda f: f in string1; print(find(string1))

# names = ["UK-02", "US-01", "IN-03"]
# print(sorted(names, key = lambda x: x[-1], reverse=True))

# name_id = ["001-Amit", "002-Shiv", "003-Dhruv"]
# print(sorted(name_id, key = lambda item: item[:4], reverse=True))

# from functools import reduce
# num = [1,2,3,4,5]
# total = reduce(lambda x,y: x+y, num)
# print(total)

# from functools import reduce
# num = [1,2,3,4,5]
# total = reduce(lambda x,y: x*y, num)
# print(total)

# from functools import reduce
# num = [1,2,3,4,5]
# min = reduce(lambda x,y: x if x<y else y, num)
# print(min)

# print(f"\n nested loops continued")
# count =0
# for i in range(3):
#     count+=1
#     if count ==2:
#         continue

# count =0
# for i in range(2):
#     for items in range(3):
#         if items ==2:
#             continue
#         count+=1
#         print(i,items,count)


# count = 0
# for i in range(2):#[0][1]
#     for j in range(3):#[0][1][2]
#         count += 1
#         print(i,j,count)

# n = 6
# for i in range(1, 6): # 1 2 3 4 5
#     print(" " * (n-i), end='')
#     for j in range(1, i+1):
#         print(j, end='')
#     for k in range(i-1, 0, -1):
#         print(k, end='')
#     print()

# n = 4
# for i in range(1,4): # 1 2 3
#     print("q" * (n-i), end='')
#     for j in range(i, i+1):
#         print(i, end='')
#     print()

# for i in range(3):
#     for j in range(1,4):
#         print(i,j)
# 'i' loop

# i = 0
# while i < 4:
#     for j in range(3):
#         print(j)
#     i += 1

# for num in range(2,12):
#     for i in range(2, num): # 'i' iterating over num. 'i' in the range will check if num is divisible by any number in the range. If yes, it will break the loop
#         if num % i == 0:
#             break
#         else: # If num is not divisible by any number in the range, it will print num
#             print(num)
#             break

# for num in range(2,10):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#         else:
#             print(num)
#             break

# num = [1,2,3,4]
# sq = list(map(lambda x: x**2, num)); print(sq)

# n = [10,11,12,13,14,15]
# s = lambda x: x**2; print(tuple(map(s,n)))

# from functools import reduce
# num = [1,2,3,4]
# sum = reduce(lambda x,y: x+y, num); print(sum)

# name_id = ['003-Charlie', '002-Bob', '001-Alice']
# s = sorted(name_id, key = lambda t: t[0:4]); print(s)

# devices = ["UK-01", "US-01", "UK-02", "IN-05"]
# s = filter(lambda x: x.startswith("UK"), devices); print(list(s))

# servers = [("Web-01", 16), ("DB-01", 64), ("App-01", 32)]
# servers.sort(key = lambda r: r[1]); print(servers)

# string1 = "string"
# find = lambda f: True if f in string1 else False; print(find("s")) # True

# names = ["Bob", "Alice", "Cassandra"]
# ls = sorted(names, key = lambda l: len(l), reverse=True); print(ls)

# servers = [" p-web-01 ", " d-sql-02 ", "p-app-01", "  p-mail-99  ", "t-test-01"]
# prod = list(map(lambda e: e.strip().upper(), filter(lambda e: e.strip().startswith("p-"), servers))); print(prod)
# Evaluation, Transformation
# Evaluation => It creates a temporary clean version of the data
# Transformation => It transforms the data into the required format

# mylist = [1,2,3]
# newlist = mylist + [4]
# mylist += [4]
# print(mylist)
# print(newlist)

# for i in range(1,2):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")

# d1 = {
#     "skill": "intune",
#     "skill2": "Azure"
# }
# k1 = ['key1', 'key2']
# v1 = ['value1', 'value2']
# d2 = set(sorted(zip(k1,v1))); print(d2)
# print(hash(d1["skill"]))
# print(hash(d1["skill2"]))
# print(d1["right hand"][1])
# for i in range(len(d1["right hand"])):
#     print(hash(d1["right hand"][i]))
# print(id(d1["right hand"][0]) == id(d1["right hand"][2]))
# print(id(d1["right hand"][0]) is id(d1["right hand"][2])) # False
# a = id(d1); print(a)

# print(d1.items())
# if "Intune".lower() in list(d1.values()):
#     print(f"Present {"Intune".lower()}")
# else:
#     pass

# for item in d1.values():
#     if item.lower() == 'intune':
#         print("Present")
#     else:
#         pass

# print(" ".join(d1.values()))
# print(list(d1.values()))

# d1 = {
#     "key3": "longest",
#     "key1": "long",
#     "key2": "longer"
# }
# d2 = dict.fromkeys(['a', 'b'], [1,2,3])
# d2['a'].append(4)
# print(d2)

# l1 = ['a', 'b']
# l2 = ['a']
# check = lambda chk: all(x in chk for x in l2); print(check(l1))

# l1 = ['a', 'b']
# l2 = ['a', 'c']
# check = lambda chk: any(x in chk for x in l2); print(check(l1))

# string1 = "string"
# find = lambda f: "Present" if f in string1 else "Absent"; print(find("rin"))

# add = [1,2,3,4,5,6,7,8,9,10]
# add_el = lambda *nd: sum(nd); print(add_el(*add))

# from collections import Counter
# l1 = ['a', 'b', 'a', 'a']
# l2 = ['a']
# l1_count = Counter(l1) # Counter({'a': 3, 'b': 1})
# check = lambda chk: {
#     item: l1_count[item] for item in chk if item in l1_count # { key_expr : value_expr  for  var  in  iterable  [if  condition] }
# }
# print(check(l2))

# names = ["Bob", "Alice", "Cassandra"]
# ls = sorted(names, key = lambda l: len(l), reverse=False); print(ls)

# name_id = ['003-Charlie', '002-Bob', '001-Alice']
# id_sort = sorted(name_id, key = lambda id: id[:4]); print(id_sort)

# servers = [("Web-01", 16), ("DB-01", 64), ("App-01", 32)]
# ram_sort = sorted(servers, key = lambda ram: ram[1]); print(ram_sort)

# devices = ["UK-01", "US-04", "UK-06", "IN-05"]
# devices_sort = sorted(devices, key = lambda us: us.startswith('UK'))
# devices_filter = filter(lambda filt: filt.lower().startswith('uk'), devices)
# print(list(devices_filter))

# num = [1,2,3,4,5]
# from functools import reduce
# sum = reduce((lambda x,y: x+y), num); print(sum)
# add_num = map(lambda a: a+5, num); print(list(add_num))
# mult = reduce((lambda x,y: x*y), num); print(mult)
# mult = map(lambda m: m*2, num); print(reduce(lambda x,y: x*y, mult))
# num = [1,2,3,4,5]
# mul = map(lambda x: x**4, num); print(list(mul))
# set_num = set(map(lambda x: x**2, num)); print(sorted(set_num, reverse=True))

# import subprocess
# def pwsh_script(script_path = "D:/Dhruv/Python/PwshToPy.ps1"):
#     try:
#         result = subprocess.run(
#             ["powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File", script_path],
#             capture_output=True, # Catches the output in a variable instead of printing it directly
#             text=True, # Displays the data in a readable text rather than 0 or 1
#             check=True # Raises 'CalledProcessError' if the command returns a non-zero exit code
#         )
#         print(result.stdout) # Displays the output
#     except subprocess.CalledProcessError as e:
#         print(f"Error occurred while running script: {e}")
#         print(f"Error output: {e.stderr}")
#     except FileNotFoundError:
#         print("PowerShell is not installed or the script path is incorrect.")
# pwsh_script()

# n = (1,2,3,4,5)
# from functools import reduce
# gr8 = reduce((lambda x,y: x if x > y else y), n); print(gr8)

# d1 = {
#     "key1": "value-1",
#     "key2": ["value-01", {"i": {"k1":"v1"}}]
# }
# d2 = {
#     "key2": "value-2",
#     "key3": "value-3"
# }
# merged1 = {**d1, **d2}; print(merged1)
# merged2 = d1 | d2; print(merged2)
# s = sorted(d1, key = lambda l: len(d1[l])); print(s)

# import json
# json_output = json.dumps(d1, indent=4); print(json_output)

# d1['key2'] = 'value01'
# d1.update(key2 = 'value02')
# print(d1)

# d1 = {
#     "key1": "value-1",
#     "key2": {"x": 11, "y": 22}
# }
# d1["key2"]["x"] = "eleven"
# d1.update(key2 = {"x": "XI"})
# d1['key3'] = {"key03":"value-3-2", 'key003': {"test1"}}
# d1.pop('key2')
# d1.popitem()
# del d1['key1']
# d1.clear()
# d1 = {}
# del d1['key3']['key03']
# print(d1)

# d1 = {
#     "key1": "9",
#     "key2": "12222",
#     "key0": "1"
# }
# for i in d1:
#     print(i, d1[i])
# print(min(d1))
# print(max(d1))
# print(sorted(d1))
# print(len(d1['key2']))
# s = sorted(d1, key = lambda e: d1[e]); print(s)
# s = sorted(d1.values(), key = lambda e: e); print(s)

# d2 = dict.fromkeys(d1.values()); print(d2)
# d2 = dict.fromkeys(d1.values(), 0); print(d2)
# d2 = dict.fromkeys(d1.values(), 0); d1.update(d2); print(d1, d2)

# d1 = {
#     "key1": "9",
#     "key2": "12222",
#     "key0": "1"
# }
# print(d1.items())
# d3 = {value:key for key,value in d1.items()}; print(d3)
# d4 = {key:value for key,value in d1.items() if value.startswith('1')}; print(d4)

# from collections import defaultdict
# groups = defaultdict(int)
# data = [("fruit", "apple"), ("vegetable", "carrot"), ("fruit", "banana")]
# for category, name in data:
#     groups[category] += 1; print(groups)

# from collections import defaultdict
# letters = defaultdict(int)
# for letter in "Mississippi":
#     letters[letter] += 1
# print(dict(letters))

# from collections import Counter,defaultdict
# items = ("test1", "test2", "test1", "test1")
# i = defaultdict(int)
# for it in items:
#     i[it] += 1
# print(dict(i))
# print(Counter(items))

# from collections import defaultdict
# my_word = "Mississippi"
# d1 = defaultdict(list)
# for index, word in enumerate(my_word):
#     if word == 'i':
#         d1[word].append(index)
# print(dict(d1))

# from collections import defaultdict
# def default_value():
#     return "Default Value"
# d1 = defaultdict(default_value)
# d1['a'] = 1
# d1['x']
# print(dict(d1))

# from collections import Counter
# words = ["apple", "orange", "apple", "pear", "orange", "apple"]
# print(Counter(words).most_common(1))

# numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
# even = {v*2 for v in numbers.values() if v % 2 == 0}; print(sorted(even))

# dict_a = {"x": 1, "y": 2}
# dict_b = {"y": 3, "z": 4}
# print(dict_a | dict_b)
# print({**dict_a, **dict_b})

# from collections import defaultdict
# raw_logs = [
#     {"ip": "192.168.1.1", "status": 200, "path": "/home"},
#     {"ip": "10.0.0.5", "status": 404, "path": "/admin"},
#     {"ip": "192.168.1.1", "status": 200, "path": "/login"},
#     {"ip": "10.0.0.5", "status": 404, "path": "/config"},
# ]
# ip_address = defaultdict(list) # Initializes 'ip_address' as a defaultdict with a list as the default value
# for ip_entry in raw_logs:
#     ip_address[ip_entry['ip']].append(ip_entry['path'])
# for ip,p in ip_address.items():
#     print(f"{p} is currently accessed in {ip}")

# from collections import defaultdict
# transactions = [
#     {"category": "Electronics", "price": 499.99},
#     {"category": "Books", "price": 15.50},
#     {"category": "Electronics", "price": 25.00},
#     {"category": "Books", "price": 10.00}
# ]
# sum = defaultdict(float)
# for i in transactions:
#     sum[i["category"]] += i["price"]
# print(dict(sum))
# print(type(transactions[0]))

# from collections import defaultdict
# def tree(): # Tree structure
#     return defaultdict(tree)
# products = tree()
# products['store']['product']['shoes']['nike'] = "In Stock"
# products['blog']['posts']['videos'] = "Published"
# print(products)
# import json
# print(json.dumps(products, indent=4))

# from collections import deque # deque stands for double-ended queue, that allows to remove elements from both ends. This makes it useful in applications like task scheduling, sliding window problems and real-time data processing.
# queue = deque(["Ticket1", "Ticket2"])
# print(queue)
# queue.append("Ticket3") # Enqueue
# print(queue)
# print(queue.popleft())  # Dequeue -> Output: "Ticket1"
# print(queue)

# def binary(array, target):
#     left, right = 0, len(array) - 1 # left = 0, right = 4
#     print(left, right)
#     while left <= right: # 0 <= 4
#         mid = (left + right) // 2 # mid = (0 + 4) // 2 = 2
#         if array[mid] == target: # if array[2] == 40 # False
#             return mid
#         elif array[mid] < target: # if array[2] < 40 # True
#             left = mid + 1 # left = 2 + 1 = 3
#         else:
#             right = mid - 1
#     return -1
# print(binary(array = [10,20,30,40,50], target = 50))

# import time
# start = time.time()



# end = time.time()
# print(f"Time taken: {end - start:.4f} seconds")

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     right = [y for y in arr if y > pivot]
#     equal = [z for z in arr if z == pivot]
#     return (quicksort(left) + equal + quicksort(right))
# list1 = [9,2,8,3,6,6,5,1,2]
# print(quicksort(list1))

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def quick_sort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)
#         quick_sort(arr, low, p - 1)
#         quick_sort(arr, p + 1, high)

# arr = [1, 7, 4, 1, 10, 9, -2]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)



# def partition(arr, low, high): # (arr, 0, 3)
#     pivot = arr[high]  # We pick 2 as the pivot
#     i = low - 1        # 'i' is the boundary for small numbers
#     # 'j' is the scanner looking at each number
#     for j in range(low, high): # (0, 3)
#         if arr[j] <= pivot: # if arr[0] <= 2
#             i += 1
#             # SWAP: Move the small number to the left of the boundary
#             arr[i], arr[j] = arr[j], arr[i] 
#     # Final SWAP: Put the pivot (2) in its permanent home
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
# def quick_sort(arr, low, high): # ([1, 2, 4, 3], 0, 3)
#     if low < high: # if 0 < 3 # True
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)  # Sort the left side
#         quick_sort(arr, pi + 1, high) # Sort the right side

# # Test with simple positive numbers
# nums = [3, 1, 4, 2]
# quick_sort(nums, 0, len(nums) - 1)
# print(f"Sorted List: {nums}")



# def selection_sort(arr):
#     for i in range(len(arr)): # 0 1 2 3 4
#         # 1. Assume the first unsorted item is the smallest
#         min_idx = i
#         # 2. Look at the rest of the list to find the REAL smallest
#         for j in range(i + 1, len(arr)): # 1 2 3 4
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # 3. SWAP the smallest found with the first unsorted position
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# data = [64, 25, 12, 22, 11]
# selection_sort(data)
# print(data)



# for row in range(1,4):
#     for col in range(1,4):
#         print(f"({row}, {col})", end = " ")
#     print()

# for i in range(1,6):
#     print("*" * i)

# for i in range(5,0,-1):
#     print("*" * i)

# n = 0
# for i in range(2,-1,-1):
#     print(" " * i + "*" * (2 * n + 1))
#     n += 1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end = ' ')
#     print()

# for i in range(1,5): # 1 2 3 4
#     print(" " * (5-i), end='')
#     for j in range(1,i+1):
#         print(j, end='')
#     for k in range(i-1,0,-1):
#         print(k, end='')
#     print()

# rows = 5
# for i in range(1,rows+1): # 1 2 3 4 5
#     for j in range(i,rows):
#         print(" ", end='')
#     for k in range(1,(2*i - 1) + 1):
#         print(i, end='')
#     print()

# rows = 5
# for i in range(1,rows): # 1 2 3 4
#     print(" " * (rows-i), end='')
#     for j in range(2*i - 1):
#         print(i, end='')
#     print()

# n = 4
# for i in range(1,n+1): # 1 2 3 4
#     print((" " * i) + ("*" * (n-i + 1)))

# n = 3
# for i in range(1,n+1): # 1 2 3
#     print(" " * (n-i + 1) + "*" * i)

# n = 3
# for i in range(1,n+1): # 1 2 3
#     print(" " * (n-i) + "*" * (2 * i - 1))

# n = 5
# for i in range(n):
#     print("* " * n)

# rows = 5
# for i in range(rows): # 0 1 2 3 4
#     for j in range(rows): # 0 1 2 3 4
#         if i==0 or i==rows-1 or j==0 or j==rows-1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

# for num in range(2,10):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# for i in range(1,6):
#     for j in range(0,i):
#         print("*", end='')
#     print()

# for i in [1,2,3]:
#     for j in [4,5,6]:
#         print(i,j)

# rows = 4
# for i in range(0,rows): # 0 1 2 3
#     print(" " * (rows-i), end='')
#     for j in range(1,i+1):
#         print(j, end='')
#     for k in range(i-1,0,-1):
#         print(k, end='')
#     print()

# row = 4
# for i in range(1,row+1): # 1 2 3 4
#     print(" " * (row-i), end='')
#     for j in range(1,i+1):
#         print(j, end='')
#     for k in range(i-1, 0, -1):
#         print(k, end='')
#     print()

# space = 3
# for i in range(space): # 0 1 2
#     print(" " * (space - i - 1), end='')
#     print(chr(i + 65) * (2 * i + 1), end='')
#     print()

# n = 6
# for i in range(0,6): # 0 1 2 3 4 5
#     print(" " * i, end='')
#     print("*" * (2*(n-i)- 1), end='')
    # for j in range(2 * (n-i) - 1):
    #     print("*", end='')
    # print()

# n = 6
# for i in range(0,n): # 0 1 2 3 4 5
#     print(" " * (n-i - 1), end='')
#     print("*" * (2*i + 1), end='')
#     for j in range(2*i + 1):
#         print("*", end='')
#     print()

# n = 5
# for i in range(n): # 0 1 2 3 4
#     print("z" * (n-i), end='')
#     for j in range(2*i + 1):
#         print("*", end='')
#     print()

# n = 4
# for i in range(0,n): # 0 1 2 3
    # print(" " * i + "*" * (2*(n-i) - 1), end='')
    # for j in range(2*(n-i) -1):
    #     print("*", end='')
    # print()

# n = 3
# for i in range(n): # 0 1 2
#     print(" " * (n-i-1) + "*" * (2*i + 1))
# for j in range(1,n): # 1 2
#     print(" " * j + "*" * (2* (n-j) -1))

# n = 1
# items = 4
# for i in range(items): # 0 1 2 3
#     print("*" * (n))
#     n += 1
# for j in range(items-1, 0, -1): # 3 2 1
#     print("*" * j)

# n = 4
# for i in range(1,n+1): # 1 2 3 4
#     print(" " * (n-i), end='')
#     print("*" * i)

# n = 3
# for i in range(1,n+1): # 1 2 3 # rows
#     for j in range(n-i): # 0,2=0,1 || 0,1=1 || 0,0=None # spaces
#         print(" ", end='')
#     for k in range(i): # 0,1=0 || 0,2=0,1 || 0,3=0,1,2 # stars
#         print("*", end='')
#     print()

# rows = 4
# for i in range(rows): # 0 1 2 3 # rows
#     for spaces in range(rows-i-1): # 3 2 1 None # spaces
#         print(" ", end='')
#     for star in range(2*i+1): # Stars
#         if star == 0 or star == (2*i) or i == rows-1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# rows = 5
# for i in range(rows): # 0 1 2 3 4
#     for j in range(rows): # 0 1 2 3 4
#         print("*", end='')
#     print()

# n = 5
# for i in range(1,n+1): # 1 2 3 4 5
#     for j in range(i):
#         print("*", end='')
#     print()


# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("*", end='')
#     print()


# n = 5
# for i in range(n): # 0 1 2 3 4
#     for j in range(n-i-1): # 0,4  0,3  0,2  0,1  0,None
#         print(" ", end='')
#     for k in range(i+1):
#         print("*", end='')
#     print()


# n = 4
# for i in range(1,n+1): # 1 2 3 4
#     for j in range(i): # 0,1  0,2  0,3  0,4
#         print(j, end='')
#     print()

# n = 4
# for i in range(1,n+1): # 1 2 3 4
#     for j in range(i): # 0,1  0,2  0,3  0,4
#         print(i, end='')
#     print()

# n = 4
# for i in range(n,0,-1): # 4,0,-1 = 4 3 2 1
#     for j in range(i,0,-1):
#         print(j, end='')
#     print()

# n = 4
# for i in range(n-1,-1,-1): # 3 2 1 0
#     for j in range(1,i+2):
#         print(j, end='')
#     print()


# n = 4
# for i in range(1,n+1): # 1,5 = 1 2 3 4
#     print(" " * (n-i), end='')
#     for j in range(1,i+1): # 1,2  1,3  1,4  1,5
#         print(j, end='')
#     print()


# n = 4
# for i in range(n): # 0 1 2 3
#     for j in range(0,i):
#         print(" ", end='')
#     for k in range(1,n-i+1): # 1,5  1,4  1,3  1,2
#         print(k, end='')
#     print()


# n = 5
# for i in range(1,n+1): # 1,6 = 1 2 3 4 5
#     for j in range(1,i+1):
#         if i==1 or i==n or j==1 or j==i:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# n = 5
# for i in range(n): # 0 1 2 3 4
#     for j in range(n-i-1): # 0,4=0123  0,3=012  0,2=01  0,1=0  0,0=None
#         print(" ", end='')
#     for k in range(1,i+2): # 1 2 3 4 5
#         if i==0 or i==n-1 or k==1 or k==i+1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# n = 5
# for i in range(n): # 0 1 2 3 4
#     for j in range(n-i-1): # 0,4  0,3  0,2  0,1  0,0
#         print(" ", end='')
#     for k in range(1,i+2):
#         if i==0 or i==n-1 or k==1 or k==i+1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# rows = 3
# for i in range(rows): # 0 1 2
#     for j in range(1,i+2): # 1,2=1  1,3=1,2  1,4=1,2,3
#         print(chr(j+64), end='')
#     print()


# from math import factorial
# rows = 5
# for n in range(rows): # 0 1 2 3 4
#     for space in range(1,rows-n): # 1,5  1,4  1,3  1,2  1,1=None
#         print(" ", end='')
#     for r in range(n+1):
#         print(factorial(n)//(factorial(r) * factorial(n-r)), end='')
#     print()


# for i in range(5): # 0 1 2 3 4
#     for j in range(5): # 0 1 2 3 4
#         print((i+j)%2, end=' ')
#     print()


# upper = 3
# for i in range(1,upper+1): # 1,4 = 1 2 3
#     for j in range(upper - i): # 0,2  0,1  0,0=None
#         print(" ", end='')
#     for k in range(2*i - 1): # 0,1  0,3  0,5
#         if i==0 or k==0 or k==2*i-2:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()
# lower = 3
# for m in range(lower-1,0,-1): # 2 1
#     print(" " * (lower-m), end='')
#     for n in range(2*m - 1): # 0,3  0,1
#         if m==1 or n==0 or n==2*m-2:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(j%2, end=' ')
#     print()


# num = 1
# for i in range(1,5): # 1 2 3 4
#     for j in range(i): # 0,1  0,2  0,3  0,4
#         print(num, end=' ')
#         num += 1
#     print()


# num = 1
# for i in range(1,4): # 1 2 3
#     print("*" * i + " " + "*" * i, end='')
#     print()
# print("*" * (i * 2 + 2))
# for j in range(3,0,-1): # 3 2 1
#     print("*" * j + " " + "*" * j, end='')
#     print()


# row = int(input("Enter a number greater than 0: "))
# for i in range(1,row+1): # 1 2 3
#     print("*" * i + " " * (2 * (row - i) + 1) + "*" * i, end='')
#     print()
# print("*" * (2 * row) + "*")
# for j in range(row): # 0,3=0,1,2
#     print("*" * (row - j) + " " * (2 * j + 1) + "*" * (row-j), end='')
#     print()


# rows = 5
# for row in range(rows): # 0 1 2 3 4
#     for col in range(rows): # 0,5 = 0 1 2 3 4
#         if row==col or col==rows-(row+1):
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# max = 3
# attempts = 0
# while True:
#     p = input("Enter password: ")
#     if p == "pswd":
#         print("Access Granted")
#         break
#     elif attempts == 2:
#         print("Account Locked")
#         break
#     else:
#         attempts += 1
#         print(f"Try again. Attempts remaining: {max-attempts}")


# n = 1
# for i in range(1,5): # 1 2 3 4
#     for j in range(i):
#         print(n, end=' ')
#         n += 1
#     print()