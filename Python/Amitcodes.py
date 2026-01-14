# nested = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# i = [item for items in nested for item in items]; print(i)
# i = [items[0] for items in nested]; print(i)
# print(nested)
# for item in nested:
#     if 1 in item:
#         print(item)



# clothes = ['t-shirt', "jeans", 'bra']

# for color in colors:
#     for i,cloth in enumerate(clothes):
#         print(i, color, cloth)

# for index, item in enumerate(range(128)):
#     print(index, chr(item))

# products = [
#     {"name": "Laptop", "price": 1200, "stock": 5},
#     {"name": "Mouse", "price": 25, "stock": 50},
#     {"name": "Monitor", "price": 300, "stock": 15}
# ]
# sort = sorted(products, key = lambda s: s['price']); print(sort)
# sort = sorted(products, key = lambda s: s['stock'], reverse=True); print(sort)

# num = lambda n: [n for n in range(11) if n % 2 == 0]; print(num(11))

# l1 = [1,2,3,4,5]
# print(list(map(lambda num: num**2, l1)))
# from functools import reduce
# print(reduce(lambda x,y: x+y, l1))

# emails = ["user@gmail.com", "admin@company.org", "info@startup.io", "spam-mail"]
# gmail = filter(lambda email: "@" in email and email.endswith("gmail.com"), emails); print(list(gmail))

# from functools import reduce
# l1 = [110,55,22,77,44]
# print(reduce(lambda a,b: a if a < b else b, l1))
# print(reduce(lambda a,b: a if a > b else b, l1))

# from collections import Counter
# l1 = ['abc', 'mno', 'xyz']
# l2 = "a"
# result = lambda find: [find for find in l1 if l2 in find]; print(result(l2)) # Not logical
# result = lambda find: [find for find in l1]; print(result(l2))
# result = lambda find: [find for find in ['abc', 'mno', 'xyz'] if l2 in find]; print(result(l2), l2) # Logical

# a = "print('Hello')"
# eval(a)
# exec(a)

# from collections import Counter
# l1 = ['abc', 'mno', 'xyz']
# l2 = ['abc']
# l1_cnt = Counter(l1); print(l1_cnt)
# l2_cnt = Counter(l2); print(l2_cnt)
# check = lambda items: {item: l1_cnt[item] for item in items if item in l2_cnt}; print(check(l1))
# c = lambda items: [item for item in items if item in l2]; print(c(l1)) # For reference

# for i in range(1,6): # 1 2 3 4 5
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# (1 1) (1 2) (1 3) 
# (2 1) (2 2) (2 3) 
# (3 1) (3 2) (3 3)

# for row in range(1,4):
#     for col in range(1,4):
#         print(f"({row} {col})", end = ' ')
#     print()

# for i in range(1,2):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")

# grades = [
#     [85, 90, 78], # Student 1
#     [92, 88, 95], # Student 2
#     [70, 72, 80]  # Student 3
# ]
# for student in grades:
#     total = 0
#     for score in student:
#         total = total + score
#     print(f"Average: {total/len(student)}")

# devices = [
#     {"name": "UK-LON-01", "os": "Windows", "disk_free": 50},
#     {"name": "US-NYC-02", "os": "macOS", "disk_free": 120},
#     {"name": "UK-MAN-05", "os": "Windows", "disk_free": 10}
# ]
# sort = sorted(devices, key = lambda p: p['disk_free']); print(sort)
# print(sorted(devices, key = lambda l: "Windows OS" if l['os'] == 'Windows' else "No Windows OS machine found"))
# devices.sort(key = lambda l: "Windows OS" if l['os'] == 'Windows' else "No Windows OS machine found"); print(devices)
# windows = filter(lambda l: l['os'] == 'Windows', devices); print(list(windows))
# actual = sorted(filter(lambda w: w['os'] == 'Windows', devices), key=lambda df: df['disk_free'], reverse=True); print(actual)
# result = [{"os": d['os'] for d in devices}, {'disk_free': d['disk_free'] for d in devices}]; print(result)

# from ForAmitSir import n
# print(n())