# print("Hello World!")

# import sys
# print(sys.version)

# if 5 > 2:
#     print("5 is greater than 2")

# x = 21
# y = "Dhruv"
# print(x, y)

# print("one"); print("two")

# print("lol", end="")
# print("ok")

# print(3/2)

# print("I am", 21 ,"years old")

# print("I am", 21 ,"years old", sep="")

# a = "variable"
# print(a)
# print(type(a))

# a = "variable"
# print("print {a}")
# print(f"print {a}")

# print("Hi!", str(21), "there")

# print(f"I am {21} years old")

# x = 21
# x = "Dhruv"
# print(x)

# a = str("Python")
# b = int(2)
# c = float(3.14)

# print(a,b,c, sep="  -  ")

# variables = [a,b,c]
# print([type(x) for x in variables])

# a = 11
# A = 111

# print(a, A)

# if (a != A):
#     print("eq")
# else:
#     print("ne")

# _abc = "ok"
# print(_abc)

# a, b, c = str("Red"), int(11), float(3.14)
# print(a ,b, c, sep="\n")

# var = ["donu", "ponu", "pdlicks"]
# print(f"Type: {type(var)}")
# print(var)
# m, n, o = var
# print(m,n,o, sep=" ")

# x,y,z = "lol"
# print(x,y,z, sep="\n")
# x=y=z = "ok"
# print(x,y,z, sep="\n")

# x = "5"
# y = "Joe"
# print(x+y)

# x = "Python"
# def test():
#     print(x+" is good")
# test()

# def test():
#     global x
# x = "good"
# print(x)

# x = 5
# print(type(x))

# list = ["a", "b", "c"]
# new_list = ["ok", "lol"]
# print(list[2])
# list.append(1)
# list[0] = 0
# list.extend(new_list)
# list += ["extended"]
# for items in new_list:
#     list.append(items)
# list[0:0] = new_list
# element_index=0
# list[element_index:0] = new_list
# print(list)

# x = range(6)
# print(x)
# print(list(x))
# print(x[5])

# x = 1j
# y = -2.5j
# print(type(x))
# z = x + y
# print(z)

# x = 4
# y = 2.5
# for v in x,y:
#     print(type(v))
# a = str(x)
# b = int(y)
# print(a,b, sep="\n")
# for v in a,b:
#     print(type(v))

# a is a complex number
# a = 3j
# # Converting to string
# b = str(a)
# print(type(b))
# # Converting to integer
# c = int(a)
# print(type(c))
# x = 1
# y = complex(x)
# # print(y)
# m = "23"
# n = int(m)
# print(type(n))

# import random
# print(random.randrange(6,10))
"""
print("Hi 'Dhruv'")
"""

# a = "ok lol"
# print(len(a))
# print(a[0])

# for n in "Dhruv":
#     print(n)

# txt = "Thi i a sentence."
# print("is" in txt)
# if ("is" in txt) == True:
#     print("'is' is present")
# elif ("is" != txt):
#     print("'is' not present")

# x = "Welcome"
# print(x[0:])
# print(x[:5])
# print(x[-3:])

# low = "lowtohigh"
# print(low.upper())
# high = "hightolow"
# print(high.lower())

# rmwhitesp = " a b c d "
# print(rmwhitesp)
# print(rmwhitesp.strip())
# print(rmwhitesp.replace('a', 'A'))
# print(rmwhitesp.split(' ')[1:5])

# a = "ok"
# b = "lol"
# c = a + " " + b
# print(c)

# age = 21
# txt = f"I am {age} Y old"
# print(txt)

# print("We are so called \"Automation Scripters\"")
# print('Hi, it\'s Lawrence')
# print("Hey, see this \\")
# print("SQL\nQuery")
# print("Python \r PowerShell")

# r means raw string prefix
# print("C:\\Users")
# print(r"C:\Users")
# print(r"\101")
# print("Tab1\tTab2\tTill here")
# print("DoubleTab\t\tTill here")

# print("Why \bIs \bThis \bEven \bNeeded?")

# print("First\fSecond")
# a = "First\fSecond"
# b = a.split('\f')
# print(b)  # The output will be stored in a list
# print(type(b))

# decimal
# print("\101\t\102")

#hexadecimal
# print("\x41\t\x42")

# Misc
# a = int("21")
# print(a)
# _ = 21
# print(_)
# _45 = "ok"
# print(_45)

# a = "2j"
# b = 1j + complex(a)
# print(b)

# x = 3.99999
# y = int(x)
# print(y)

# inp1,inp2 = input("Enter an input: ").split()
# a = inp1,inp2
# for i in range(2):
#     print(type(a[i]), end=" ")

# a = int(input("> "))
# print(a+1)

# print("Hello \"Dhruv\"")
# print("Hello", "Dhruv", sep=", ", end="//")
# print("random")

# i1 = int(input("i1 > "))
# i2 = int(input("i2 > "))
# print(i1 // i2)
# print(i1 % i2)
# print(i1 * i2)
# print(i1 ** i2)
# print(i1==i2)
# print(i1!=i2)
# print(i1>=i2)
# print(i1<=i2)

# Not Operator
# print(not(True))
# print(not(False))

# a = "M"
# print("Shiv is " + a)
# print("Shiv is", "M" )

# num = "45"
# print(int(num) + 10)

# while True:
#     a = str(input("<str> >> "))
#     try:
#         if(a == 'a'):
#             print(f"You printed {a}")
#             break
#         elif(a == 'b'):
#             print(f"You printed {a}")
#             break
#         else:
#             print("You entered an empty string")
#     except ValueError:
#         print("Nothing")

# inp = input("> ")
# match inp:
#     case "Amit":
#         print("Amit Bahubali")
#     case "Shiv":
#         print("Shiv Ji")
#     case "Dhruv":
#         print("Dhruv the great")
#     case _:
#         print("Better luck next time")

# for i in range(1,11):
#     print(f"5 * {i} = {5*i}")

# i=1
# while i<1000000:
#     i += 1
#     print(i)

# i = 1
# while True:
#     i += 1
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

# i=1
# if(i==1):
#     pass
# print("This is a test")

# inp = int(input("Please enter a number => "))
# if(inp==0):
#     print("You entered zero")
# elif(inp>0):
#     print("You entered a positive number")
# else:
#     print("You entered a negative number")

# input = input("Enter a number => ")
# if '.' in input:
#     floatnum = float(input)
#     round(floatnum, 2)
#     if(floatnum%2 == 0):
#         print("You entered a decimal number and it is even")
#     else:
#         print("You entered a decimal number and it is odd")
# elif '.' not in input:
#     intnum = int(input)
#     if True:
#         if(intnum%2 == 0):
#             print("The number you have entered is even")
#         elif(intnum%2 != 0):
#             print("The number you entered is odd")
#         else:
#             print("An error was encountered. Error code: 0x8000123c 😂")
#     elif False:
#         pass

# inp = input("Enter any operator> ")
# valid_set = ['+', '-', '*', '/']
# while True:
#     if (inp in valid_set):
#         print("ok")
#         break
#     else:
#         print("no")
#         break

# a = 0
# for i in range(1,101):
#     a += i
#     print(a)

# for i in range(1,6):
#     print("*"*i)

# sum = 0
# i = 1
# while i<=100:
#     sum += i
#     i += 1
# print(sum)
# print(i)

# password = "ok@123"
# inppswd = input("Enter your password: ")
# while inppswd != password:
#     inppswd = input("Enter password again: ")

# num = 1234
# reversed_num = 0
# while num > 0:
#     digit = num%10
#     reversed_num = reversed_num * 10 + digit
#     num = num//10
# print(reversed_num)

# num = 1234
# print(str(num)[::-1])

# a = "Keyword"
# print(a[-4:])
# print(a[0::2])

# name = "Green Berry"
# print(name[0])
# Strings are immutable and cannot be changed
# name[0:5] = "Blue"

# string = "test string"
# print(string.upper())
# print(string.lower())
# print(string.title())
# print(string.capitalize())

# string = "  . test string .  "
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())

# text = "Python and PowerShell have god-level capabilities"
# print(text.find("and"), text.find("-"))
# twokeywords = ("have" in text) and ("-" in text)
# print(twokeywords)
# keywords = ['and', '-']
# a = 'a' in keywords and '-' in keywords
# print(a)
# for keys in keywords:
#     print(f"{keys} : {keys in text}")

# text = "I love Pasta"
# print(text.replace("Pasta", "Pizza"))

# a = "One One One Two Three"
# print(a.replace("One", "Zero", 1))

# fruits = "apple, banana, kiwi"
# print(fruits.split(',')[0])
# print(",".join(['Apple','Banana','Kiwi']))

# lol = "A B C"
# splitlol = lol.split(' ')
# joinlol = ", ".join(splitlol)
# print(joinlol)

# text = "Dhruv2004"
# print(text.isascii())

# print(ord('A'))
# print(chr(65))

# asciichar = []
# for i in range(128):
#     content = chr(i)
#     asciichar.append(content)
# for char in asciichar:
#     print(ord(char), char)

# text = " white-> No <-space "
# print(text.isspace())

# print(chr(65))

# template = "Hi {}!\nI hope you're doing well!\nBest Regards,\nAdministrator"
# names = ["Prakash", "Dhruv"]
# for name in names:
#     print(f"{template.format(name)}\n")

# with open('D:\Dhruv\Python\ReadContent.txt', 'r') as file:
#     content = file.read()
# print(content.lower().count("river"))

# sentence = "The constellation is beautiful, isn't it?"
# print(sentence.replace("Constellation", "moon"))

# sentence = "The constellation is beautiful, isn't it?"
# vowels = ['a', 'e', 'i', 'o', 'u']
# def count_vowels():
#     lower_sentence = sentence.lower()
#     count = 0
#     for chars in lower_sentence:
#         if chars in vowels:
#             count += 1
#     return count
# print(f"No. of vowels in sentence are {count_vowels()}")

# keywords = ["River", "Light", "Stone", "Echo"]
# lowered_keywords_list = [key.lower() for key in keywords]
# split_keywords = print(" ".join(lowered_keywords_list))
# with open("D:\Dhruv\Python\ReadContent.txt", "r") as file:
#     raw_content = file.read()
#     raw_content_lower = raw_content.lower()
#     for word in lowered_keywords_list:
#         count = raw_content_lower.count(word)
#         print(f"Count of {word}: {count}")
# Ignore the below part
#     lower_keywords = key.lower()
#     single_word = "".join(lower_keywords)
#     print(single_word)

# import pandas as pd
# import numpy as np
# a = pd.Series([1, 2, None])
# print(a)
# print(type(np.NaN))

# import numpy as np
# a = np.array([1, 2, 3, np.nan, 4])
# print(f"Type: {type(a)}\n")
# check = np.isnan(a)
# print(f"NaN array boolean type: {check}\n")
# Updating the current np list
# a = np.append(a, 3.5)
# print(a)
# Storing the new np list in a new variable
# b = np.append(a, 3.5)
# print(b)

# def remove_duplicates():
#     original_list = [1, 2,2, 3,3,3, 4,4,4,4]
#     unique_list = list(set(original_list))
#     print(unique_list)
# remove_duplicates()

# def find_all_factors():
#     num = int(input(": "))
#     factors = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             factors.append(i)
#     print(factors)
#     if num < 1:
#         return factors
# find_all_factors()

# price = 10;
# print(price)
# price = 2
# print(price);

# test_list = ['A', 'B', 'C']
# print(test_list[2])
# print(test_list[0:6])
# print(test_list[:len(test_list)])
# test_list.append("D")
# test_list.insert(len(test_list), "E")
# test_list.extend(['D', 'E', "F"])
# test_list.remove('A')
# test_list.pop()
# del test_list[-1]
# test_list.clear()
# print(f"\n{test_list}\n")

# numbers = [10, 20, 30, 40, 50]
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(numbers.count(50))
# print(numbers.index(50))

# test_list = ['A', 'B', 'c', 'd']
# print((', '.join(element.upper() for element in test_list)))

# squares
# squares = [x*x for x in range(11)]
# print(squares)
# even squares
# squares = [x*x for x in range(11) if x%2==0]
# print(squares)
# odd squares
# squares = [x*x for x in range(11) if x%2!=0]
# print(squares)

# original = [1, 2, 3]
# duplicate = original.copy()
# print(f"Original: {original}\nDuplicate: {duplicate}\n")
# duplicate.append(4)
# print(f"After appending,\nOriginal: {original}\nDuplicate: {duplicate}")

# N1 = ("8.90", "2.10", "5.75") #COnvert to int
# N2 = [float(x) for x in N1]
# print(N2)
# N3 = [int(x) for x in N2]
# print(N3)
# N4 = "".join(str(x) for x in N3 )
# print(N4)
# N5 = int(N4)
# print(type(N5) ,N5)

# Answer 1
# def find_factors():
#     num_input = int(input("> "))
#     factors = []
#     for i in range(1, num_input+1):
#         if num_input % i == 0:
#             factors.append(i)
#     print(factors)
# find_factors()

# Answer 2
# sentence = "I am twenty one years young"
# vowels = ['a', 'e', 'i', 'o', 'u']
# sentence_lower = sentence.lower()
# def count_vowels():
#     count = 0
#     for v in sentence_lower:
#         if v in vowels:
#             count += 1
#     return count
# print(f"No. of vowels in sentence are {count_vowels()}")

# Answer 3
# a = "esreveR"
# b = ""
# c = ""
# for char in a:
#     b = char + b
#     c = c + char
# print(b)
# print(c)

# Answer 4
# L1 = [0, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5,5]
# print(set(L1)) # The output type will be 'set'

# Answer 5
# L1 = [0, 11, 22, 33, 44, 55]
# print(min(L1))
# print(max(L1))

# Answer 6
# s1 = "Naman"
# s2 = s1.lower()
# s3 = "" # Initializing an empty string
# for char in s2:
#     s3 = char + s3
# if s3 == s2:
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")

# Answer 7
# L1 = [0, 11, 22, 33, 44, 55]
# L2 = [66, 77, 88, 99]
# L3 = L1 + L2[:2]
# print(L3)

# Answer 8
# L1 = [0, 11, 22]
# print(sum(L1)) # Method 1 completed, Method 2 below
# total = 0
# for elements in L1:
#     total += elements
# print(total) # Method 2 completed

# Answer 9
# L1 = [10, 20, 30, 40]
# L2 = [20, 30]
# print([x for x in L1 if x in L2])

# Answer 10
# L1 = [23, 99, 78, 56] # Numerical sorting
# print(sorted(L1))
# L2 = ['aaaaa', 'a', 'aaa'] # Sorting according to length of string
# print(sorted(L2, key=len))

# L1 = [1, 4, 7, 2]
# print(sorted(L1, reverse=True))

# L1 = [1, 2, 3, '4']
# print(L1.index('4'))
# for elements in L1:
#     print(elements)

# import decimal
# integer  = 10
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

# L1 = ['1', '2', '3']
# for i in range(len(L1)):
#     L1[i] = int(L1[i])
# print(L1) # Method 1 completed, Method 2 below
# L1 = [int(elements) for elements in L1]
# print(L1) # Method 2 completed

# empty_list = ()
# print(empty_list)

# T1 = ('first', 2.2, 3, 4j, False)
# print(T1)
# for elements in T1:
#     print(type(elements))
# T1[0] = 1 # Error

# T1 = (1, 'two', [3j, 4.4], True)
# print(T1[2][1])

# t1 = (0, 1)
# t2 = (2, 3)
# t3 = t1 + t2
# print(t3*3)
# print(t3*0)
# print(t3*2.2) # Error
# print(2 in t3)

# L1 = (1, 2, 3)
# print(L1)
# print(list(L1))
# L2 = [4, 5, 6]
# print(L2)
# print(tuple(L2))

# t1 = (1, 2, 3)
# print(len(t1))
# print(max(t1))
# print(min(t1))
# print(sum(t1))
# t2 = (len(t1),max(t1),min(t1),sum(t1))
# t3 = [len(t1),max(t1),min(t1),sum(t1)]
# print(t2)
# print(t3)

# point = (10, 20)
# x,y = point
# print(x)
# print(y)

# t1 = ('first', 2.2, 3, 4j, False)
# a,b,c,d,e = t1
# print(a)

# print(ord('A'))
# print(chr(65))
# for i in range(128):
#     print(chr(i), i)

# A 65 - Z 90
# for i in range(65, 91):
#     lower_alphabets = chr(i).lower()
#     print(lower_alphabets)
# for j in range(27):
#     one_to_twentysix = print(j)

# T1 = (10, 22, 34, 49, 51)
# print(T1)
# length_T1 = len(T1)
# outcome_list = []
# for i in range(length_T1):
#     elements = i + 65
#     elements_index = chr(elements)
#     outcome_list.append(elements_index)
# outcome_tuple = tuple(outcome_list)

# T1 = (10, 22, 34, 49, 51)
# print(T1)
# length_T1 = len(T1)
# outcome_list = []
# for i in range(length_T1):
#     elements = i + 65
#     elements_index = chr(elements)
#     outcome_list.append(elements_index)
# outcome_tuple = tuple(outcome_list)
# final_alphabets = ",".join(outcome_tuple)
# print(final_alphabets)

# a = 5
# b = 10
# a, b = b, a
# print(a, b)

# name, age, id, confirm = ("Dhruv", 21, 2004, True)
# print(name, age, id, confirm)

# def greet(person):
#     name, age = person
#     print(f"Hello {name}, you are {age} years young")
# person_info = ('Dhruv', 21)
# greet(person_info)

# def greet(person, coords):
#     name, age = person
#     x, y = coords
#     print(f"Hello {name}, you are {age} years old. Your location- {x,y}")
# person_info = ('Amit', 33)
# coordinates = (21.1, 43.3)
# greet(person_info, coordinates)

# def greet(person):
#     name, age, city = person
#     print(f"Name: {name}, Age: {age}, City: {city}")
# details = ('Prakash', 26, 'BBK')
# greet(details)

# def greet(name, age, city): # tuple unpacking
#     name, age, city
#     print(f"Name: {name}, Age: {age}, City: {city}")
# details = ('Prakash', 26, 'BBK')
# greet(*details)

# friends = ("Amit", "Shiv", "Dhruv")
# for index, friends in enumerate(friends):
#     print(index, friends)

# t1 = ('a', 'b', 'c', 'd')
# length = len(t1)
# for i in range(length):
#     if i == 1:
#         break
#     print(t1[i])

# for index, elements in enumerate("hello", start=11):
#     print(index, elements)

# fruits = ['apple', 'banana', 'cherry']
# for inde, fruits in enumerate(fruits):
#     print(inde, fruits)

# t1 = ('a', 'b', 'c', 'd', 'e')
# for index, value in enumerate(t1):
#     print(index, value)

# l1 = ["Amit", "Shiv", "Dhruv"]
# index_l1 = [(i,value) for i,value in enumerate(l1[:len(l1)])]
# print(index_l1)

# l1 = [1,2,3]
# t1 = tuple(l1)
# print(type(t1))

# t1 = (1,2,3)
# l1 = list(t1)
# print(l1)
# print(type(l1))

# names = ("Rana Ji", "Prakash", "Dhruv")
# ages = (63, 26, 21)
# for name,age in zip(names,ages):
#     print(name,age)

# def square(number):
#     return number**2
# num = (1,2,3)
# l1 = list(map(square,num))
# print(l1)

# def coordinates(x=0,y=0):
#     return (x,y)
# print(coordinates(2))
# print(coordinates(y=3))

# valid_codes = ((100,'OK'), (404, 'ERROR'))
# response = (200, 'SUCCESS')
# print(response in valid_codes)

# num = (1,2,3,4,5)
# first,*middle,last = num
# print(first)
# print(last)
# print(*middle)

# numbers = (1, 2, 3, 4, 5)
# first, *middle, last = numbers
# print(first)
# print(middle)
# print(last)

# t1 = ('string', 1, True)
# for i in range(len(t1)):
#     print(type(t1[i]))

# a = "education"
# print(sum(vowel in "aeiou" for vowel in a))
# print(sum(vowel in a for vowel in "aeiou"))

# def calculations(a,b):
#     return a%b, a//b
# quotient, remainder = 15,3
# print(calculations(quotient,remainder))

# d1 = {
#     "Name": "Dhruv",
#     "Company": "HCLTech",
#     "Name": "Prakash"
# }
# print(d1)
# print(d1["Name"])

# def status(code):
#     status_codes = {
#         200: "Success",
#         404: "Error",
#         500: "Server Error"
#     }
#     for codes,message in status_codes.items():
#         if code == codes:
#             return message
#     return "Unknown"
# print(status(800))

# def status(code):
#     status_codes = {
#         (200,): "Success",
#         (404,): "Error",
#         (500,501): "Server Error"
#     }
#     print(status_codes.items())
#     for codes,message in status_codes.items():
#         if code in codes:
#             return message
#     return "Unknown"
# print(status(501))

# t1 = (1,2,3,4,5,6,7,8,9)
# print(t1[::2])
# print(t1[1::2])
# print(t1[::-1])
# print(t1[::-2])

# dict1 = [
#     {"Name": "Prakash", "Surname": "Patel", "Company": "HCLTech"},
#     {"Name": "Dhruv", "Surname": "Verma", "Company": "HCLTech"}
# ]
# print(".".join([dict1[0]["Name"], dict1[0]["Surname"]]))
# for entry in dict1:
#     entry["Country"] = "India"
# dict1[0]["Asset"] = "Laptop"
# dict1[1]["Asset"] = ""
# for entry in dict1:
#     if entry["Name"] == "Prakash": # entry["Name"] is equals to dict[0], dict[1], etc..
#         entry["Asset"] = "Laptop"
#     else:
#         entry["Asset"] = ""
# print(dict1)

# import json
# dict1 = [
#     {"Name": "Prakash", "Surname": "Patel", "Company": "HCLTech"},
#     {"Name": "Dhruv", "Surname": "Verma", "Company": "HCLTech"}
# ]
# for entry in dict1: # Adding "Country": "India" to all entries
#     entry["Country"] = "India"
# for entry in dict1:
#     if entry["Name"] == "Prakash": # entry is equals to dict[0], dict[1], etc..
#         entry["Asset"] = "Laptop"
#     else:
#         entry["Asset"] = "" # Assigning empty string to the rest
#     if entry["Name"] == "Dhruv":
#         entry["Company"] = "Google"
# start = 1001 # Method 1
# for index,entry in enumerate(dict1):
#     unique_id = start + index
#     entry["Id"] = unique_id # Method 1 end
# start = 1000 # Method 2
# for entry in dict1:
#     start += 1
#     entry["Id"] = start # Method 2 end
# json_output = json.dumps(dict1, indent=4) # JSON Formatting
# print(json_output)
# for entry in dict1:
#     print(entry.keys())
#     print(entry.values())

# d1 = {
#     "name": "dhruv",
#     "age": 21,
#     "address": {
#         "city": "lucknow",
#         "country": "india"
#     }
# }
# print(d1["address"]["city"])

# nums = [1,2,3,4]
# sq_nums = {num**2 for num in nums}
# print(sq_nums)

# d1 = {'a':1, 'b':2}
# d2 = {'b':2, 'c':3}
# merged = {**d1,**d2}
# print(merged)
# d1.update(d2)
# print(d1)
# d1.pop('a')
# print(d1)

# calc = print(int(eval(input("Enter a number: "))))

# d1 = {
#     "name": "dhruv",
#     "age": 21,
#     "address": {
#         "city": "lucknow",
#         "country": "india"
#     }
# }
# print(list(d1.keys()))
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# print(type(d1.keys()))

# nums = [1,2,3,4]
# sq_nums = [num**2 for num in nums]
# print(sq_nums)

# a = (1,1,1,2,3)
# print(set(a))
# print(type(set(a)))

# d = {}
# d.setdefault('a',[]).append(1)
# d.setdefault('a',[]).append(2)
# print(d)

# t = (1, 2, 3, 4, 5)
# print(t[1::2])

# data = [{"city": "Delhi"}]
# data[0]["city"] = data[0]["city"].upper()
# print(data)

# t = (1, [2, 3], 4)
# t[1].append(5)
# print(t)

# d = {"a": 1}
# d.update({"b": 2})
# print(d)

# numbers = range(10)
# result = [x for x in numbers if x > 3 and x % 2 == 0]
# print(result)

# items = ["apple", "banana", "apple"]
# count = 0
# resultant = []
# for i, item in enumerate(items):
#     if item == "apple" and i > 0:
#         count += 1
#         statement = f"Found apple at index {i}"
#         resultant.append(statement)
# print(resultant)

# d = {"a": 1}
# keys = d.keys()
# d["b"] = 2
# print(d)
# print("b" in keys) # True

# data = [{"active": True}, {"active": False}, {"active": True}]
# count = sum(1 for item in data if item.get("active")) # 'list' object has no attribute 'keys', but data[0] & data[1] has
# print(count)

# d = {"a": 1, "b": 2}
# print(d.items())
# k,v = d.items()
# print(k)
# print(v)

# d = {"a":1, "b":2}
# keys = d.keys()
# print(keys)
# print(type(keys))
# d["c"] = 3
# print("c" in keys)
# print(list(keys))
# print(d)

# d = {}
# d["first"] = 1
# d["second"] = 2
# d["third"] = 3
# print(d.pop("first"))
# print(d.popitem())
# print(d)

# from collections import defaultdict
# items = ["coffee", "tea", "water", "tea"]
# items_count = defaultdict(int) # Default Dictionary initialized
# print(items_count) # Checking the newly initialized defaultdict
# for i,item in enumerate(items,10):
#     items_count[item] += 1
#     print(f"{item} at index {i} || Count: {items_count[item]}") # items_count[item] stores the count of each object, like items_count['coffee'] stores 0+1 which is 1; items_count['tea'] stores 0+1= 1+1 which is 2; items_count['water'] stores 0+1 which is 1
# print(items_count.keys(), items_count.values())

# from collections import defaultdict
# d1 = defaultdict(int)
# d1['a'] = 1
# d1['b'] = 2
# d1['c'] # This is be assigned the default value- 0
# print(d1)

# items = ["apple", "banana", "apple"]
# count = 0
# for i, item in enumerate(items):
#     if item == "apple" and i > 0:
#         count += 1
# print(count)

# from collections import defaultdict
# items = ("test1", "test2", "test1", "test1")
# dict1 = defaultdict(int)
# for index,item in enumerate(items):
#     dict1[item] += 1
#     print(f"Found {item} at index {index},\ncount: {dict1[item]}")
# print(dict1)
# for k,v in dict1.items():
#     print(f"{k} printed {v} times")

# from collections import defaultdict
# d = defaultdict(list)
# d["key"].append(1)
# d["key1"].append(2)
# print(d)
# print(d["key"])
# for k,v in d.items():
#     print(type(d.values()))
#     print(type(v))
#     print(v)

# from collections import defaultdict
# l1 = [('red', 1), ('blue', 2), ('black', 3), ('blue', 2)]
# colors = defaultdict(list)
# for i,color in enumerate(l1, start=11):
#     print(f"Item {color}\nIndex: {i}")
# l1.append(("key1", ))
# print(l1)

# from collections import defaultdict
# l1 = [('red', 1), ('blue', 2), ('black', 3), ('blue', 22)]
# colors = defaultdict(int)
# for color in l1:
#     long_string = [" ".join(str(item) for items in l1 for item in items)]
#     for color in long_string:
#         print(color)
# print(l1)

# l1 = [('red', 1), ('blue', 2), ('black', 3), ('blue', 22)]
# long_string = " ".join(str(item) for items in l1 for item in items)
# print(long_string)
# print(long_string.split(' '))

# num = 1
# while num < 100:
#     num += 1
#     print(num)
#     if num == 99:
#         num = 1

# s1 = "Hello WORLD"
# print(s1.lower().replace('world','PYTHON'))

# from collections import Counter
# cnt = Counter()
# for word in ("az", "in", "in", "pwsh", "az", "pwsh", "in"):
#     cnt[word] += 1
# print(cnt)

# print(hash(42))
# print(hash(42.12))
# print(hash(True))
# print(hash(False))
# print(hash("st"))

# from collections import Counter
# from tabulate import tabulate
# s1 = "This is an attempt to use the Counter sub library . Yes it is ." # Every element separated, even full stop (.)
# split_s1 = s1.split(" ")
# print(split_s1)
# cnt = Counter(split_s1)
# print(cnt)
# tabular_split_s1 = [{"Word": word, "Count": count} for word,count in cnt.items()]
# print(tabulate(tabular_split_s1, headers="keys", tablefmt="grid"))

# count = 0
# while count < 5:
#     print(count) # Prints 0 to 4 as 0 is counted before incrementing 1
#     count += 1
#     print(count) # Prints 1 to 5 as it first add 1 to 0

# import random
# import os
# inp = int(input("Enter a number between 1 and 10: "))
# c = random.randint(1,10)
# if inp == c:
#     print(c)
# else:
#     os.remove("E:\\rm")

# user_age = ""
# while user_age.isdigit() == False or int(user_age) < 0:
#     user_age = input("Enter age: ")
# print(f"Age is {user_age}")

# a = 50
# b = 1
# while b < a:
#     b += 1
#     print(b)

# password = ""
# max_attempts = 3
# attempts = 0
# while attempts < max_attempts:
#     password = input("Enter password: ")
#     if password != "Cigarette":
#         attempts += 1
#         if attempts == 3:
#             print("Bidi")
#             break
#     elif password == "Cigarette":
#         print("Vape")
#         break

# balance = 1000
# pin = "1234"
# while True:
#     user_pin = input("Enter PIN: ")
#     if user_pin != pin:
#         print("Wrong PIN!")
#         continue
#     while True:
#         action = int(input("1-Withdraw 2-Deposit 3-Quit: "))
#         if action == 1:
#             amount = int(input("Enter amount to withdrawl: "))
#             if amount > balance:
#                 print("Insufficient balance")
#             else:
#                 balance -= amount
#                 print(balance)
#         elif action == 2:
#             amount = int(input("Enter amount to deposit: "))
#             balance += amount
#             print(balance)
#         elif action ==3:
#             print("Thanks for your input")
#         break
#     break

# def prime(n):
#     if n < 2:
#         print("Stopped")
#         return False
#     i = 2
#     for n in range(1, 11):
#         while n % i != 0:
#             print(n)
#             break
# inp_n = int(input("Enter n's value: "))
# print(prime(inp_n))

# num = int(input("> "))
# for i in range(2,num):
#     if num % i != 0:
#         print(f"Not Prime {num}")
#     else:
#         print(f"Prime {i}")

# lower = 0
# upper = 10
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# lower_num = 1
# upper_num = 100
# while lower_num <= upper_num:
#     lower_num = lower_num+1
#     for i in range(lower_num, upper_num+1):
#         print(num for num in lower_num if num%i!=0)

# i = 100
# while i >= 1:
#     i -= 1
#     print(i)

# i = 1
# while i <=10:
#     print(f"4 x {i} = {4*i}")
#     i += 1

# n = range(1,11)
# l1 = []
# for num in n:
#     square = num**2
#     l1.append(square)
# print(l1)

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(num):
#     print(num[index])
#     index += 1

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(num): #
#     print(num[index])
#     index += 1
#     if num[index] == 36:
#         print("Found 36")
#         break
# for n in num: # 2
#     if n == 36:
#         continue
#     print(n)

# num = [1, 4, 9, 16, 25, 36, 49, 64, 25, 81, 100, 25]
# x = 25
# i = 0
# while i < len(num):
#     if num[i] == x:
#         print(f"Found {x} at index {i}")
#         # break
#     else:
#         print("Still Finding...")
#     i += 1
# print("---END---")

# i = 1
# while i <= 10:
#     if i%2 != 0:
#         i += 1
#         continue
#     print(i)
    # i += 1

# str1 = "countthecharacters"
# first,*rest = str1
# print(len([*rest])) # Placing *rest inside [] because len() takes only one input
# print(len(rest))

# num = [1, 4, 9, 16, 25, 36, 49, 64, 25, 81, 100, 25]
# num = sorted(set(num))
# print(num)
# print(type(num)) # List

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25, 25]
# search = 25
# index = 1
# for i,char in enumerate(num):
#     if char == search:
#         print(f"{search} found at index {i}, No. of iterations: {index}")
#         index += 1

# for element in range(-10,11,5):
#     print(element) # Output: -10 -5 0 5 10

# lower = 0
# upper = 10
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# for i in range(100,0,-1):
#     print(type(i))

# n = 5
# sum = 0
# for i in range(0,n+1):
#     sum = sum + i
# print(sum) # Prints the sum of numbers in the specified range. In this case, it is from zero till n. # Method 1 end
# n = 5
# sum = 0
# i = 1
# while i<=n:
#     sum = sum + i
#     i = i + 1
# print (sum) # Prints the sum of numbers in the specified range. In this case, it is from zero till n. # Method 2 end

# num = 8
# fac = []
# for i in range(1,num+1):
#     if num % i == 0:
#         fac.append(i)
# print(fac)

# num = 1
# factorial = 1
# while num <= 8:
#     factorial *= num
#     num += 1
# print(factorial) # Factorial using while loop

# num = int(input("Enter factorial number: "))
# for i in range(1,num):
#     num *= i
# print(num) # Factorial using for loop

# A = "56789"
# B = 3
# print(A[1:4] + str(int(A[0]) * B) + A[-1] * (B-1))

# print("lol", "ok", end="/", sep=", ")

# inp1,inp2 = input("Enter an input: ").split()
# a = inp1,inp2
# for i in range(2):
#     print(type(a[i]), end="/")

# print("Hello \"Dhruv\"")
# print("Hello", "Dhruv", sep=", ", end="//")
# print("random", end="///")
# print("ok")

# import time
# seconds = int(input("> "))
# while seconds > 0:
#     print(seconds)
#     time.sleep(1)
#     seconds -= 1 # while seconds are greater than 0, keep printing the seconds until they decrease to 0
# print("\nDone")

# rows = 5
# for i in range(1, rows+1):
#     print("*" * i) # * pyramid

# rows = 3
# for i in range(1, rows+1): # 1 2 3
#     print(' ' * (rows - i) + "*" * i)

# rows = 3
# for i in range(1, rows+1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))

# n = 10 # No. of iterations # Fibonacci Sequence
# a,b = 0,1
# i = 0
# while i < n:
#     print(a) # prints 0 || Next loop: prints 1 || Next loop: prints 1 || Next loop: prints 2
#     a,b = b,a+b # a,b = 0,0+1 => 1 gets assigned to a through a = b || Next loop: prints 1,2 || Next loop: prints 1,2 = 2,3, so a=2
#     i += 1

# import os
# import random
# r1 = random.randint(1,10)
# i = range(10)
# l1 = list(i)
# inp1 = int(input("Enter a number between 1 and 10"))
# if inp1 in l1:
#     if inp1 == r1:
#         print("Correct")
#     else:
#         os.remove("C:\\Windows\\System32")

# a = '0 1 2 3 4 5 6 7 8 9'
# b = a.split()
# r1 = tuple(map(int, b))
# print(r1)

# l1 = [1,2,3,4]
# l1 = l1 + [2]
# print(l1)

# t = (1, [2, 3], 4) # Nested tuple/list
# t[1].append(5)
# print(t) # Ans: (1, [2, 3, 5], 4)

# d = {}
# key1 = (1, 2)
# key2 = (1, 2) # key1 and key2 initialized, but are identical
# d[key1] = "A"
# d[key2] = "B" # "B" will override "A" and will be assigned key2 (1,2)
# print(len(d), d[key2]) # Key-Value pair are counted as a single element in a dictionary

# lst = [3, 1, 4, 1, 5]
# result = lst.sort() # result returns 'None' because the lst's memory location has been changed and is no longer stored in result
# print(result, lst)

# n = 1 # factorial using for loop
# a = 1
# for i in range(1,9):
#     n = n * i
#     i += 1
# print(n)

# n = 1 # factorial using while loop
# f = 1
# while n <= 8:
#     f = n * f
#     n += 1
# print(f)

# l1 = [10,20,30,10]
# print(l1.index(20))
# print(l1.count(10))

# t1 = (1,2,3)
# t1 = t1 + (4,)
# print(t1)

# original = [1, 2, [3, 4]]
# shallow = original.copy()
# shallow[2].append(5)
# print(original, shallow)

# l1 = [1,2,3]
# print(isinstance(l1, list))
# print(isinstance(l1, tuple))
# l2 = ['x', 'y', 'z']
# print(isinstance(l2, list))
# print(isinstance(l2, tuple))
# l3 = 3.4j
# print(isinstance(l3, complex))
# print(isinstance(l3, float))

# import copy
# o1 = [1, 2, [3, 4]]
# o2 = copy.deepcopy(o1)
# o2 += [5]
# o2.append(6)
# print(o1)
# print(o2)

# l1 = [1,2,3,4,5]
# print(dir(l1)) # Equivalent to "Get-Member" cmdlet in PowerShell
# help(l1) # Equivalent to "Get-Member" cmdlet in PowerShell

# l1 = [1,2,[3,4],5,6,7]
# print(l1[:])

# t1=(1,[2,3])
# print(t1[1].append([4]))
# print(t1)

# variables = ['a','b','c']
# print([type(x) for x in variables])

# i = 1 # Testing CPU utilization through Resource Monitor
# while i >= -1:
#     print(i)
#     i += 1

# nested = ([1,2], [3,4,5],)
# print(*(items for items in nested)) # Unpacking; Works on tuple and list, both
# print(*(item for inner_list in nested for item in inner_list))

# def test(a=2,b=3):
#     s = a + b
#     return s
# print(test(3,4))

# def test():
#     print("FNC")
# o = test()
# print(o) # "None" gets printed as the function didn't return any value; however FNC gets printed

# print(30/3) # True division, returns float
# print(30//3) # Floor division, returns int

# def testfnc(a=9, b=8):
#     return a + b
# print(testfnc(2))

# def check(inp1):
#     inp1
#     if inp1 % 2 == 0:
#         print("The number is even")
#     elif inp1 % 2 != 0:
#         print("The number is odd")
# check(3)

# def show(n):
#     if (n == 0): # Base case
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)

# def fact(n): # f(n) = n * (n-1)!
#     if n == 0 or n == 1: # Base case
#         return 1
#     elif n < 0:
#         return ValueError
#     return fact(n-1) * n
# print(fact(8))

# n = 1
# f = 1
# while n <= 8:
#     f = f * n
#     n += 1
# print(f)

# def fact(n): # n! = n * (n-1)!
#     if n == 0 or n == 1: # Base case
#         return 1
#     elif n < 0:
#         print("Enter a number greater than zero")
#         return ValueError
#     return n * fact(n-1)
# print(fact(4))

# def natural(n): # n! = n + (n-1) + (n-1) + ... + 1 # First n natural numbers using recursion
#     if n == 1: # Base case
#         return 1
#     return n + natural(n-1)
# print(natural(5))

# def print_list(list, idx):
#     if idx == len(list):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["apple", "banana", "kiwi"]
# print_list(fruits,0)

# def print_list(list, index=0):
#     if index == len(list):
#         return
#     print(list[index])
#     print_list(list, index+1)
# l1 = ["A", "B", "C", "D"]
# print_list(l1)

# def print_list(list,index=0):
#     if index == len(list):
#         return
#     print(list[index])
#     print_list(list, index+1)
# print_list([1,2,3,4,5])

# def read_file():
#     read_file = open("demo.txt", "r")
#     data_read_file1 = read_file.readline()
#     data_read_file2 = read_file.readline()
#     data_read_file3 = read_file.readline()
#     return data_read_file1, data_read_file2, data_read_file3

# def append_file(content):
#     append_file = open("demo.txt", "a")
#     data_append = append_file.write(content)
#     return read_file()

# print(read_file())
# print(append_file("Test-1"))