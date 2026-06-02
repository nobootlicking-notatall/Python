# namedtuple
# A similar approach of creating a simple, lighweight data structures similar to a class, but without the actual requirement to create a class


#################################################


from collections import namedtuple


#################################################


from collections import namedtuple

emp = namedtuple("Employee_Name", ["name",  "age"])
emp1 = emp("Amit", 34)
emp2 = emp("Shiv", 25)
emp3 = emp("Prakash", 25)
emp4 = emp("Dhruv", 22)

print(emp1.name, emp1.age)
print(emp2.name, emp2.age)
print(emp3.name, emp3.age)
print(emp4.name, emp4.age)


#################################################


from collections import namedtuple

library = namedtuple("Books", ["Name", "Subject"])

intune = library("Advanced Intune", "Cloud PKI")

print(getattr(intune, "Name"))


#################################################