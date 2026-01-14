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

