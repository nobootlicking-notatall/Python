# Recursive Function
# A recirsive function repeats itself until a specific condition is met
# Understanding Flows: https://pythontutor.com/visualize.html#mode=display


def fact(num):
    if num <= 1:
        return 1
    return (num * fact(num-1))
print(fact(5))
# Workflow
# --------
# 5 is passed to num
# fact(num-1) is triggered
# fact(num-1) > 5 > (5-1)=4 > (4-1)=3 > (3-1)=2 > (2-1)=1
# num <= 1 condition met
# return (num * fact(num-1)) > 5 * 4 * 3 * 2 * 1 = 120 # Output


def factorial(limit, num=1):
    if num > limit:
        return 0
    return num + factorial(limit, num+1)
print(factorial(5, num=1))
# Workflow
# --------
# limit=5, num starts from 1
# num+1 = 1 > 1+1=2 > 2+1=3 > 3+1=4 > 4+1=5
# 'num' now smaller than limit (Condition is met, 0 is returned, proceeding with the next step)
# return num + factorial(limit, num+1) > 1+2+3+4+5 = 15


